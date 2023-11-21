# EasyPicoPCB project : https://github.com/Mick3DIY/EasyPicoPCB
# Raspberry Pi Pico : https://www.raspberrypi.com/products/raspberry-pi-pico/
# Documentation, tutorials : https://projects.raspberrypi.org
# MicroPython : https://micropython.org
# Thonny IDE : https://thonny.org
from machine import Pin
import utime

# Default values for Thonny IDE plotter window
valueMin = "Min:-0.25"
valueMax = "Max:1.25"
# Default value for blinking LEDs (startup)
valueSleep = 0.5
# Default value for looping
looping = True

# External button S1 (GPIO16, pin 21) -> decrease value/speed
buttonS1 = Pin(16, Pin.IN, Pin.PULL_DOWN)
# External button S2 (GPIO17, pin 22) -> stop looping
buttonS2 = Pin(17, Pin.IN, Pin.PULL_DOWN)
# External button S3 (GPIO18, pin 24) -> increase value/speed
buttonS3 = Pin(18, Pin.IN, Pin.PULL_DOWN)

# External LED LED1 (GPIO15, pin 20)
led1 = Pin(15, Pin.OUT)
# External LED LED2 (GPIO14, pin 19)
led2 = Pin(14, Pin.OUT)
# External LED LED3 (GPIO13, pin 17)
led3 = Pin(13, Pin.OUT)
# Pico on-board LED (GPIO25)
ledOnboard = Pin(25, Pin.OUT)

# Handler for buttons IRQ
def buttons_handler(pin):
    global valueSleep, looping
    if buttonS1.value() == 1:
        # Minimal low value : 0.2s
        if valueSleep >= 0.2:
            valueSleep = valueSleep - 0.1
    if buttonS2.value() == 1:
        looping = False
    if buttonS3.value() == 1:
        # Maximum high value : 2s
        if valueSleep <= 2:
            valueSleep = valueSleep + 0.1

# Buttons triggers
buttonS1.irq(trigger=Pin.IRQ_RISING, handler=buttons_handler)
buttonS2.irq(trigger=Pin.IRQ_RISING, handler=buttons_handler)
buttonS3.irq(trigger=Pin.IRQ_RISING, handler=buttons_handler)

while looping:
    ledOnboard.on()
    led1.on()
    print(valueMin, "Led1:1", "Led2:0", "Led3:0", valueMax)
    utime.sleep(valueSleep)
    led1.off()
    print(valueMin, "Led1:0", "Led2:0", "Led3:0", valueMax)

    led2.on()
    print(valueMin, "Led1:0", "Led2:1", "Led3:0", valueMax)
    utime.sleep(valueSleep)
    led2.off()
    print(valueMin, "Led1:0", "Led2:0", "Led3:0", valueMax)

    led3.on()
    print(valueMin, "Led1:0", "Led2:0", "Led3:1", valueMax)
    utime.sleep(valueSleep)
    led3.off()
    print(valueMin, "Led1:0", "Led2:0", "Led3:0", valueMax)

    ledOnboard.off()
    utime.sleep(0.5)

# Turn off all LEDs when exit loop
led1.off()
led2.off()
led3.off()
ledOnboard.off()
