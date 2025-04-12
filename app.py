from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello, World!'
@app.route('/welcome')
def welcome():
    return 'Welcome to the Flask app!'  
if __name__ == '__main__':
    app.run(debug=True)