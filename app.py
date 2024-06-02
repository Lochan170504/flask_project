from flask import Flask, render_template, request, jsonify
from chat import get_response
import mysql.connector
import requests

app = Flask(__name__)

db = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='',
    database='scholarship_demo'
)


@app.get("/")
def index_get():
    return render_template("base.html")

@app.route("/process_form", methods=["POST"])
def process_form():
    graduation = request.form['graduation']
    gender = request.form['gender']
    state = request.form['State']  # Adjusted to match the form field name
    
    # Execute database query based on user input
    cursor = db.cursor(dictionary=True)
    sql = "SELECT * FROM scholarships WHERE graduation = %s AND gender = %s AND State = %s"  # Adjusted to match the database column name
    cursor.execute(sql, (graduation, gender, state))
    scholarships = cursor.fetchall()
    
    if scholarships:
        return render_template('results.html', scholarships=scholarships)
    else:
        return render_template('no_results.html')

@app.route("/scholarship/<int:scholarship_id>")
def scholarship_description(scholarship_id):
    cursor = db.cursor(dictionary=True)
    sql = "SELECT * FROM scholarships WHERE scho_id = %s"  # Ensure column name matches your database
    cursor.execute(sql, (scholarship_id,))
    scholarship = cursor.fetchone()
    return render_template('scholarship_description.html', scholarship=scholarship)

@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    # TODO: Check if text is valid
    if not text:
        return jsonify({"error": "Invalid input"}), 400
    
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)

if __name__ == "__main__":
    app.run(debug=True)