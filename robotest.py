#!/usr/bin/env python3

'''
robotest.py - Test the features of BreezyCreate2

This code is part of BreezyCreate2

The MIT License

Copyright (c) 2016 Simon D. Levy

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
'''
from flask import render_template
from flask import Flask, Response
from flask import request, jsonify
from breezycreate2 import Robot
import time
import urllib3
import requests


STATIC_FOLDER = "."

app = Flask(__name__, 
            static_folder=STATIC_FOLDER, 
            static_url_path="")

variable = "Hello"
variable1 = ""
variable2 = ""
variable3 = ""
variable4 = ""
variable5 = ""
variable6 = ""
variable7 = ""
variable8 = ""
variable9 = ""
distance = 0
moveX = []
moveY = []
currentDirection = 0
@app.route('/')
def hello_world():
	# http = urllib3.PoolManager()
	# r = http.request('POST', 'http://localhost:5000/asdf')
	return render_template('index.html', variable=variable, moveX = moveX, moveY = moveY)

@app.route('/<speed>')
def hello_world2(speed = None):
	global variable
	variable = speed
	return render_template('index.html', variable=variable, moveX = moveX, moveY = moveY)

@app.route('/', methods = ['POST'])
def doStuff():
    # return "<b>"+variable+"</b><br><input/>"
	global variable
	variable = request.form['direction']
	move()
	return render_template('index.html', variable=variable, moveX = moveX, moveY = moveY)


@app.route('/cpu', methods= ['GET'])
def stuff():
	updateVars(bot.printAll())
	return jsonify(variable1 = variable1, variable2 = variable2, variable3 = variable3, variable4 = variable4, variable5 = variable5, variable6 = variable6, variable7 = variable7, variable8 = variable8, variable9 = variable9, distance=distance, moveX = moveX, moveY = moveY)

def updateVars(object1):
	global variable1
	variable1 = object1.field1
	global variable2
	variable2 = object1.field2
	global variable3
	variable3 = object1.field3
	global variable4
	variable4 = object1.field4
	global variable5
	variable5 = object1.field5
	global variable6
	variable6 = object1.field6
	global variable7
	variable7 = object1.field7
	global variable8
	variable8 = object1.field8
	global variable9
	variable9 = object1.field9
	global distance
	distance = distance+object1.distance



def move():
	updateVars(bot.printAll())
	if(variable == "up"):
		if(currentDirection == 0):
			moveX.append(0)
			moveY.append(-10)
		elif(currentDirection == 1):
			moveX.append(7)
			moveY.append(-7)
		elif(currentDirection == 2):
			moveX.append(10)
			moveY.append(0)
		elif(currentDirection == 3):
			moveX.append(7)
			moveY.append(7)
		elif(currentDirection == 4):
			moveX.append(0)
			moveY.append(10)
		elif(currentDirection == 5):
			moveX.append(-7)
			moveY.append(7)
		elif(currentDirection == 6):
			moveX.append(-10)
			moveY.append(0)
		elif(currentDirection == 7):
			moveX.append(-7)
			moveY.append(-7)

		bot.setForwardSpeed(100)
		time.sleep(1)
		updateVars(bot.printAll())
		bot.setForwardSpeed(0)
	elif(variable == "down"):
		if(currentDirection == 4):
			moveX.append(0)
			moveY.append(-10)
		elif(currentDirection == 5):
			moveX.append(7)
			moveY.append(-7)
		elif(currentDirection == 6):
			moveX.append(10)
			moveY.append(0)
		elif(currentDirection == 7):
			moveX.append(7)
			moveY.append(7)
		elif(currentDirection == 0):
			moveX.append(0)
			moveY.append(10)
		elif(currentDirection == 1):
			moveX.append(-7)
			moveY.append(7)
		elif(currentDirection == 2):
			moveX.append(-10)
			moveY.append(0)
		elif(currentDirection == 3):
			moveX.append(-7)
			moveY.append(-7)

		bot.setForwardSpeed(-100)
		time.sleep(1)
		updateVars(bot.printAll())
		bot.setForwardSpeed(0)
	elif(variable == "left"):
		global currentDirection
		currentDirection = currentDirection - 1
		if(currentDirection<0):
			currentDirection = 7
		bot.setTurnSpeed(-100)
		time.sleep(1)
		updateVars(bot.printAll())
		bot.setTurnSpeed(0)	
	elif(variable == "right"):
		global currentDirection
		currentDirection = currentDirection + 1
		if(currentDirection>7):
			currentDirection = 0
		bot.setTurnSpeed(100)
		time.sleep(1)
		updateVars(bot.printAll())
		bot.setTurnSpeed(0)
	elif(variable =="close"):
		bot.close()
	updateVars(bot.printAll())
	print(variable)


# Create a Create2. This will automatically try to connect to your robot over serial
print("HELLO")


bot = Robot()

print("111")

# Play a note to let us know you're alive!
bot.playNote('A4', 100)
print("222")

# bot.setForwardSpeed(100)
# print("333")

# time.sleep(1)
# print("444")

# print("FIELD"+bot.printAll().field1)

# # Tell the Create2 to turn right slowly
# ##bot.setTurnSpeed(360)

# # Wait a second
# ##time.sleep(1)

# # Stop

# print("555")

# bot.setForwardSpeed(0)





# print("666")

# # Report bumper hits and wall proximity for 30 seconds
# start_time = time.time()
# while (time.time() - start_time) < 5:
#    #bot.setTurnSpeed(-100)
#    #bot.printAll()    
#    #print('Angle '+ str(bot.getAngle()))

#    bot.printAll()
#    #print('Distance: ' + str(bot.getDistance()))
#    #print('Angle '+ str(bot.getAngle()))
#    #print("##########")
#    print('Bumpers: ' + str(bot.getBumpers()) + '    Wall: ' + str(bot.getWallSensor()))
#    #print("##########")
#    print('Cliff: ' + str(bot.getCliffSensors()))

# ##    print('Forward111')
# ##    bot.setForwardSpeed(100)
# ##    bot.printAll()
# ##    time.sleep(1)
# ##    bot.setForwardSpeed(0)

#    print('Left111')
#    bot.setTurnSpeed(-100)
#    bot.printAll()
#    time.sleep(1)
#    bot.setTurnSpeed(0)

   
#    bot.printAll()

# ##    print('Forward222')
# ##    bot.setForwardSpeed(100)
# ##    bot.printAll()
# ##    time.sleep(1)
# ##    bot.setForwardSpeed(0)
   
#    print('Right222')
#    bot.setTurnSpeed(100)
#    bot.printAll()
#    time.sleep(1)
#    bot.setTurnSpeed(0)    
# # Close the connection
# bot.setTurnSpeed(0) 
# bot.close()


