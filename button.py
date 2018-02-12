import time
import sys
from datetime import datetime
from gpiozero import LED
from gpiozero import Button

button = Button(26)
led = LED(12)

def main():
    with open(sys.argv[1], "a") as f:
        while True:
            button.wait_for_press()
            led.on()
            f.write('%s\t' % (datetime.now(),))
            time.sleep(0.3)

            button.wait_for_press()
            led.off()
            f.write('%s\n' % (datetime.now(),))
            time.sleep(0.3)
            f.flush()

if __name__ == '__main__':
    main()
