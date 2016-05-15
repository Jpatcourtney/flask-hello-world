# ---- Flask Hello World ---- #
#!flask/bin/python

# imports the Flask class from the flask package 
from flask import Flask

# creates the application object
app = Flask(__name__)

# Helps with error handling and allows for "automatic reload"
app.config["DEBUG"] = True

# decorators used to link following function to urls
@app.route('/')
@app.route('/hello')
# define the view function
def hello_world():
    return "Hello, World!?!?!?!?!"

# a dynamic route
@app.route('/test/<search_query>')
def search(search_query):
    return search_query

# dynamic integer route
@app.route('/integer/<int:value>')
def int_type(value):
    print value+1
    return 'Correct'

# dynamic float route
@app.route('/float/<float:value>')
def float_type(value):
    print value+1
    return "Correct"

# dynamic route that can contain slashes (a path)
@app.route('/path/<path:value>')
def path_type(value):
    print value
    return "Correct"

# more dynamics
@app.route('/name/<name>')
def index(name):
    if name.lower() == "michael":
        return 'Hello, {}'.format(name), 200
    else:
        return "Not Found", 404




# this starts the development server with the run() method
if __name__ == "__main__":
    app.run()