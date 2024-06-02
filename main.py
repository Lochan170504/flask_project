from flask import Flask, render_template, request, jsonify
from chat import get_response
import mysql.connector
import requests
from flask_babel import Babel, _

app = Flask(__name__)

db = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='',
    database='scholarship_demo'
)
babel = Babel(app)

# Configure the languages your application supports
app.config['LANGUAGES'] = {
    'en': 'English',
    'kn': 'Kannada'
}

# Set the directory where the translations are stored
app.config['BABEL_TRANSLATION_DIRECTORIES'] = 'C:/xampp/htdocs/flask_project/translations'

def get_locale():
    # Optionally use request.args.get('lang') to change language based on URL parameter
    return request.accept_languages.best_match(app.config['LANGUAGES'].keys())

app.jinja_env.globals.update(get_locale=get_locale)


@app.route('/')

@app.get("/")
def index_get():
    return render_template("index.html")

@app.route('/set_language', methods=['POST'])
def set_language():
    if request.method == 'POST':
        lang = request.form['lang']
        if lang in app.config['LANGUAGES']:
            return redirect(url_for('index', _locale=lang))
    return redirect(url_for('index'))

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