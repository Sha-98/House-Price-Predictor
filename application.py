from flask import Flask, render_template, request
import pandas as pd
import pickle
import numpy as np

application = app = Flask(__name__)
data=pd.read_csv('Cleaned_data.csv')
pipe = pickle.load(open("RidgeModel.pkl","rb"))


@app.route('/' , methods=['GET'])
def index():

    location = sorted(data['location'].unique())
    return render_template('index.html', location=location)


@app.route('/predict', methods=['POST'])

def predict():
    location = request.form.get('location')
    bhk = request.form.get('bhk')
    balcony = request.form.get('balcony')
    sqft = request.form.get('total_sqft')

    print(location, bhk, balcony, sqft)
    input = pd.DataFrame([[location, sqft, balcony, bhk]], columns = ['location', 'total_sqft', 'balcony' , 'bhk'])
    prediction = pipe.predict(input)[0]*100000

    return str(np.round(prediction,2))

if __name__ == "__main__":
    app.run(debug=True, port=5001)



    