import time
from datetime import datetime
from gpiozero import LED
from gpiozero import Button

button = Button(26)
led = LED(12)



while True:
	button.wait_for_press()
	led.on()
	print('on: ', datetime.now())
	time.sleep(0.3)

	button.wait_for_press()
	led.off()
	print('off: ', datetime.now())
	time.sleep(0.3)
