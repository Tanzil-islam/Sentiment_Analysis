# app.py
from flask import Flask, request, jsonify, render_template
import model  # Import the custom model module

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Render the HTML page

@app.route('/predict', methods=['POST'])
def predict():
    try:
        comment = request.form['comment']  # Get text input from HTML form
        prediction = model.make_prediction(comment)
        return render_template('index.html', input=comment, prediction=prediction)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
