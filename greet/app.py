from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/welcome')
def welcome_page():
    return """<h1>Welcome!</h1>"""

@app.route('/welcome/home')
def welcome_home():
    return """<h1>Welcome Home</h1>"""

@app.route('/welcome/back')
def welcome_back():
    return """<h1>Welcome Back</h1>"""