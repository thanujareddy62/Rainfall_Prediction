from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd
app = Flask(__name__)

# Load the model
with open('best_bagging_clf_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            # Extract and convert form data
            v1 = float(request.form["v1"])
            v2 = float(request.form["v2"])
            v3 = float(request.form["v3"])
            v4 = float(request.form["v4"])
            v5 = float(request.form["v5"])
            v6 = float(request.form["v6"])
            v7 = float(request.form["v7"])
            v8 = float(request.form["v8"])
            v9 = float(request.form["v9"])
            v10 = float(request.form["v10"])
            v11 = float(request.form["v11"])

            # Create DataFrame with feature names
            data = pd.DataFrame([[v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11]], 
                                columns=['MinTemp', 'MaxTemp', 'Rainfall', 'Evaporation', 'Sunshine', 
                                         'Humidity9am', 'Humidity3pm', 'Pressure3pm', 
                                         'Cloud9am', 'Cloud3pm', 'RainToday_Yes'])
            
            # Predict using the model
            prediction = model.predict(data)
            value=""
            if(prediction[0]==0):
                value="No rain Tomorrow"

            
            else:
                value="There will be rain Tomorrow"
            

            # Render the result in HTML
            return render_template('index.html', prediction=value)

        except Exception as e:
            return str(e)

if __name__ == '__main__':
    app.run(debug=True)
