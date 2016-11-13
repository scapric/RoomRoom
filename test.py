from flask import render_template
from flask import Flask, Response
from flask import request, jsonify
import time

STATIC_FOLDER = "."

app = Flask(__name__, 
            static_folder=STATIC_FOLDER, 
            static_url_path="")

variable = "Hello"

@app.route('/')
def hello_world():
    # return "<b>"+variable+"</b><br><input/>"
	return render_template('index.html', variable=variable)

@app.route('/<speed>')
def hello_world2(speed = None):
	global variable
	variable = speed
	return render_template('index.html', variable=variable)

@app.route('/', methods = ['POST'])
def doStuff():
    # return "<b>"+variable+"</b><br><input/>"
	global variable
	variable = request.form['direction']

	return render_template('index.html', variable=variable)


@app.route('/cpu', methods= ['GET'])
def stuff():
	cpu=0

	return jsonify(cpu=cpu)


def move():
	

# from flask import render_template

# @app.route('/hello/')
# @app.route('/hello/<name>')
# def hello(name=None):
#     return render_template('hello.html', name1=name)