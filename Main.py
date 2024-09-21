import time
from GPIOEmulator.EmulatorGUI import GPIO

GPIO.setmode(GPIO.BCM)

led_pins = [5, 6, 13, 19, 26, 16, 20, 21]

for pin in led_pins:
    GPIO.setup(pin, GPIO.OUT)

button_pin = 18
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

running = False

patterns = [
    0b00011000,
    0b00100100,
    0b01000010,
    0b10000001,
    0b00000000,
    0b10000001,
    0b01000010,
    0b00100100,
    0b00011000
]

while True:
    if GPIO.input(button_pin) == GPIO.LOW:
        running = not running
        time.sleep(0.2)
    
    if running:
        for pattern in patterns:
            for i in range(8):
                GPIO.output(led_pins[i], (pattern >> i) & 1)
            time.sleep(1)
