import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from django.views.generic import RedirectView
from django.conf.urls import url

# Create flask app
app = Flask(__name__)

# Load the pickle model
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home_page():
    return render_template('index.html')

@app.route("/predict", methods = ["POST"])
def predict():

    float_features = [float(x) for x in request.form.values()]
    features = [np.array(float_features)]
    prediction = model.predict(features)
    
    url_patterns = [

        url(r'^favicon\.ico$', RedirectView.as_view(url='/static/images/favicon.ico')),
    ]

    return render_template('index.html', prediction_text="The Flower Species is {}".format(prediction))

if __name__ == "__main__":
    app.run(debug=True)
