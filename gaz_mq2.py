from machine import Pin
from time import sleep_ms

led = Pin(2, Pin.OUT)
gaz = Pin(26, Pin.IN, pull=Pin.PULL_DOWN)

while True:
    sleep_ms(100)
    if gaz.value() == 0:
        led.value(1)   # allume la LED
    else:
        led.value(0)   # éteint la LED 
        
