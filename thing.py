import RPi.GPIO as GPIO
import os
import time 

switch_pin = 37
first_led = 35

class PiThing(object):
	"""this is Rpi internet things"""
	def __init__(self):
		GPIO.setwarnings(False)
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(first_led, GPIO.OUT)
		GPIO.setup(switch_pin, GPIO.IN)
		

	def read_switch(self):
		""" Read the state of the switch !!"""
		return GPIO.input(switch_pin)
		

	def set_led(self, value):
		"""changes the LED to the passed in values, either True for on or false for off"""
		GPIO.output(first_led, value)

	def rpi_temp(self):
		"""reading temperature of the raspberry pi"""
		tempInString = os.popen('vcgencmd measure_temp').read()
		parshing = tempInString[5:9]
		tempInFloat = float(parshing)
		return	tempInFloat