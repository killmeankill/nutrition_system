from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])  # Allow both GET and POST methods
def index():
    if request.method == 'POST':  # Handling form submission
        # Safely handle form data here
        client_data = {
            'inbody_date': request.form.get('inbody_date', ''),
            'weight': float(request.form.get('weight', 0)),
            'muscle_mass': float(request.form.get('muscle_mass', 0)),
            'body_fat': float(request.form.get('body_fat', 0)),
            'protein_weight': float(request.form.get('protein_weight', 0)),
            'bmr': float(request.form.get('bmr', 0)),
            'height': float(request.form.get('height', 0)),
            'age': int(request.form.get('age', 0)),
            'gender': request.form.get('gender', ''),
            'activity_level': request.form.get('activity_level', 'sedentary'),
            'medical_conditions': request.form.get('medical_conditions', ''),
            'allergies': request.form.get('allergies', ''),
            'target_weight': float(request.form.get('target_weight', 0)),
            'timeframe': int(request.form.get('timeframe', 0)),
            'current_calories': float(request.form.get('current_calories', 0)),
            'favorite_foods': request.form.get('favorite_foods', ''),
            'daily_routine': request.form.get('daily_routine', ''),
            'motivation_level': int(request.form.get('motivation_level', 0)),
            'exercise_willingness': request.form.get('exercise_willingness', ''),
            'motivation_reason': request.form.get('motivation_reason', '')
        }

        recommendations = {
            "diet_plan": f"Based on your goal to reach {client_data['target_weight']} kg in {client_data['timeframe']} months, maintain a daily calorie intake of {client_data['bmr']} calories.",
            "exercise_suggestion": "Consider moderate-intensity exercise 5 times a week for 30-60 minutes.",
            "hydration_tips": "Drink at least 2.5 liters of water daily to stay hydrated."
        }

        return render_template('output.html', client_data=client_data, recommendations=recommendations)

    return render_template('input_form.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
