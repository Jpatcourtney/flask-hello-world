# ---- Flask Hello World ---- #
#!flask/bin/python

# imports the Flask class from the flask package 
from flask import Flask

# creates the application object
app = Flask(__name__)

# decorators used to link following function to urls
@app.route('/')
@app.route('/hello')
# define the view function
def hello_world():
    return "Hello, World!"

# this starts the development server with the run() method
if __name__ == "__main__":
    app.run()