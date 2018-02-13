import time
import sys
from datetime import datetime
from gpiozero import LED
from gpiozero import Button
from db import Session
from model import Interval

button = Button(26)
led = LED(12)
session = Session()


def main():
    while True:
        button.wait_for_press()
        led.on()
        start = datetime.now()
        time.sleep(0.3)

        button.wait_for_press()
        led.off()
        end = datetime.now()
        session.add(Interval(started=start,ended=end))
        session.commit()
        time.sleep(0.3)
        

if __name__ == '__main__':
    main()
