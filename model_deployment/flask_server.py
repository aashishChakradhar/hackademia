from flask import Flask, request, jsonify
import joblib
import os

#initialize flask app
app = Flask(__name__)
model = joblib.load('model_deployment/iris_logistic_regression.pkl')

#define a route for the prediction API
@app.route('/predict',methods = ['POST'])
def predict():
    data = request.get_json(force = True)
    prediction = model.predict([data['features']])
    return jsonify({'prediction':int(prediction[0])})

#run the flask app
if __name__ == '__main__':
    app.run(host=os.getenv('IP','0.0.0.0'),
        port = int(os.getenv('PORT',4444)))