from flask import Flask, request, render_template
from input_processing import validate, format_model_inputs
from model import Model

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        form_input = request.form
        
        # Format model inputs
        model_inputs = format_model_inputs(form_input)

        # Make prediction using your CatBoost model (assuming Model is correctly implemented)
        prediction = Model().predict(model_inputs)

        # Interpret prediction
        churn_prediction = "Customer is likely to churn" if prediction == 1 else "Customer is unlikely to churn"

        return render_template('index.html', prediction=churn_prediction)

    return render_template('index.html')

# Method 2: Via POST API (one prediction at a time)
@app.route('/api/predict_one', methods=['POST'])
def predict_one():
    request_data = request.get_json()  # optional: print request_data as log
    errors = validate(request_data)
    if len(errors) > 0:
        return {'errors': errors}, 400

    # Format model inputs
    model_inputs = format_model_inputs(request_data)

     # Make prediction using your CatBoost model (assuming Model is correctly implemented)
    prediction = Model().predict(model_inputs)
    
    # Interpret prediction
    churn_prediction = "Customer is likely to churn" if prediction == 1 else "Customer is unlikely to churn"

    return {'prediction': churn_prediction}

if __name__ == '__main__':
    app.run(debug=True)
