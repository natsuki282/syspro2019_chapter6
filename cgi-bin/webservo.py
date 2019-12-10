#!/usr/bin/env python


import cgi
import cgitb
import time
import RPi.GPIO as GPIO

print('Content-type: text/html; charset=UTF-8\r\n')
print('Web SERVO')

print('<form action="" method="post">')
print('<input type="number" name="servo" min="-90" max="90">')
print('<input type="submit" name="turnbutton" value="TURN">')
print('</form>')

GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)
servo=GPIO.PWM(2,50)
servo.start(0.0)


form=cgi.FieldStorage()
rand=form.getvalue("servo")
value=form.getvalue("turnbutton")


if value=="TURN":
	ang=((0.0105*(float(rand)+90.0))+0.5)*5.0
	servo.ChangeDutyCycle(ang)
	time.sleep(1.0)

	GPIO.cleanup()
