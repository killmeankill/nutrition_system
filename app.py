from flask import Flask, render_template, request

app = Flask(__name__)

# Function to calculate daily caloric needs
def calculate_calories(weight, height, age, gender, activity_level):
    """Calculate daily caloric needs."""
    if gender == 'male':
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161

    # Adjust BMR based on activity level
    activity_multiplier = {
        'sedentary': 1.2,
        'lightly_active': 1.375,
        'moderately_active': 1.55,
        'very_active': 1.725
    }

    return bmr * activity_multiplier[activity_level]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Gather data from the form
        client_data = {
            'inbody_date': request.form['inbody_date'],
            'weight': float(request.form['weight']),
            'height': float(request.form['height']),
            'age': int(request.form['age']),
            'gender': request.form['gender'],
            'activity_level': request.form['activity_level'],
            'target_weight': float(request.form['target_weight']),
            'timeframe': int(request.form['timeframe']),
        }

        # AI Nutrition Plan
        daily_calories = calculate_calories(
            weight=client_data['weight'],
            height=client_data['height'],
            age=client_data['age'],
            gender=client_data['gender'],
            activity_level=client_data['activity_level']
        )

        # Recommendation message
        recommendation = f"""
        Your daily caloric needs are approximately {daily_calories:.2f} kcal.
        To reach your target weight of {client_data['target_weight']} kg in {client_data['timeframe']} months,
        aim for a calorie intake of {daily_calories - 500:.2f} kcal per day.
        """

        return render_template('results.html', recommendation=recommendation)
    
    return render_template('input_form.html')

if __name__ == '__main__':
    app.run(debug=True)
