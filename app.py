from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    val1 = request.form['MedInc']
    val2 = request.form['HouseAge']
    val3 = request.form['AveRooms']
    val4 = request.form['AveBedrms']
    val5 = request.form['Population']
    val6 = request.form['AveOccup']
    val7 = request.form['Latitude']
    val8 = request.form['Longitude']
    arr = np.array([val1, val2, val3, val4, val5, val6, val7, val8])
    arr = arr.astype(np.float64)
    pred = model.predict([arr])

    return render_template('index.html', data=float(pred))


if __name__ == '__main__':
    app.run(debug=True)
