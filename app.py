from flask import Flask, render_template, request
import joblib
import numpy as np
model = joblib.load('best_model.pkl')
scaler = joblib.load('scaler.pkl')
label_encoder = joblib.load('label_encoder.pkl')

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get input data from the form
        haematocrit = float(request.form['haematocrit'])
        haemoglobin=float(request.form['haemoglobin'])
        erythrocyte = float(request.form['erythrocyte'])
        leucocyte = float(request.form['leucocyte'])
        thrombocyte = float(request.form['thrombocyte'])
        mch = float(request.form['mch'])
        mchc = float(request.form['mchc'])
        mcv = float(request.form['mcv'])
        age = int(request.form['age'])
        sex = int(request.form['sex'])
        input_data = np.array([[haematocrit, haemoglobin, erythrocyte, leucocyte, thrombocyte, mch, mchc, mcv, age, sex]])
        input_data_scaled = scaler.transform(input_data)
        prediction = model.predict(input_data_scaled)
        prediction_label = label_encoder.inverse_transform(prediction)
        return render_template('index.html', prediction=prediction_label[0])

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)