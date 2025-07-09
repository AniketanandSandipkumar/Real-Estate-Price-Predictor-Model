from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
model = pickle.load(open('randomreg.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Fetch all 10 numerical inputs
        under_construction = int(request.form['under_construction'])
        rera = int(request.form['rera'])
        bhk = int(request.form['bhk'])
        sqft = float(request.form['sqft'])
        ready_to_move = int(request.form['ready_to_move'])
        resale = int(request.form['resale'])
        longitude = float(request.form['longitude'])
        latitude = float(request.form['latitude'])
        dealer = int(request.form['dealer'])
        owner = int(request.form['owner'])

        # Arrange input in the right order
        input_features = np.array([[under_construction, rera, bhk, sqft,
                                    ready_to_move, resale, longitude, latitude,
                                    dealer, owner]])
        
        prediction = model.predict(input_features)

        return render_template('index.html', prediction_text=f"🏠 Estimated Price: ₹ {prediction[0]:,.2f} Lacs")

    except Exception as e:
        return render_template('index.html', prediction_text=f"⚠️ Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
