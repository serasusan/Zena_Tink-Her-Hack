from flask import Flask,render_template
app = Flask(__name__, static_url_path='/static')
@app.route('/')
def user_page():
    return render_template('index1.html')
if __name__ == "__main__":
    app.run(debug = True)