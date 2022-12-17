from flask import Flask,render_template
app = Flask(__name__)
@app.route('/index1.html')
def user_page():
    return render_template('index1.html')