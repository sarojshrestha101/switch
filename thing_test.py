from thing import PiThing
import time

pi_thing = PiThing()

# current switch state
switch = pi_thing.read_switch()

print("switch: {}".format(switch))

while True:
	print(pi_thing.rpi_temp())
	time.sleep(.5)
