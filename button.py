import time
import sys
from datetime import datetime
from gpiozero import LED
from gpiozero import Button

import requests

button = Button(26)
led = LED(12)


def main():
    while True:
        button.wait_for_press()
        led.on()
        start = datetime.now()
        time.sleep(0.3)

        button.wait_for_press()
        led.off()
        end = datetime.now()
        data = {
            'started': start.isoformat(),
            'ended': end.isoformat()
        }
        requests.post('http://192.168.0.118/intervals/add', json=data)
        time.sleep(0.3)
        

if __name__ == '__main__':
    main()
