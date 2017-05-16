from flask import *
import random
import time
from thing import PiThing 

app = Flask(__name__)
pi_thing = PiThing()

@app.route('/')
def hello_world():
	
	return render_template('index.html', message = random.uniform(30, 40), switch = pi_thing.read_switch(), temp = pi_thing.rpi_temp())

@app.route('/led/<int:led_state>', methods = ['POST'])
def led(led_state):
	if led_state == 0:
		pi_thing.set_led(False)
	elif led_state == 1:
		pi_thing.set_led(True)
	else:
		return ('Unknow LED state!!', 400)

	return('',200)

@app.route('/switch')
def switch():
		
	def get_switch_values():
	        while True:
	        	yield('data: {}\n \n'.format(random.uniform(0,500)))
	        	time.sleep(1)
	
	return Response(get_switch_values(), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)
