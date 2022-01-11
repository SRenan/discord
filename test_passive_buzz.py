import RPi.GPIO as GPIO
import time

## GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT) # LEF
GPIO.setup(12, GPIO.OUT) # Active buzzer
GPIO.setup(18, GPIO.OUT) # Passive buzzer

pin = 18

b = GPIO.PWM(pin, 440) 

freqs = range(300, 3100, 200)

b.start(0.5) 
for ii in reversed(freqs):
  b.ChangeFrequency(ii)
  time.sleep(0.2)

b.stop()
GPIO.cleanup()

