import time
import sys
import json
from datetime import datetime
from gpiozero import LED
from gpiozero import Button

import requests

button = Button(26)
led = LED(12)

def enqueue_for_later(data):
    with open('failed_requests.txt', 'a') as f:
        f.write(json.dumps(data)+'\n')


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
        resp = requests.post('http://192.168.0.118:5000/intervals/add', json=data)
        if resp.status_code != requests.codes.ok:
            enqueue_for_later(data)
        time.sleep(0.3)
        

if __name__ == '__main__':
    main()
