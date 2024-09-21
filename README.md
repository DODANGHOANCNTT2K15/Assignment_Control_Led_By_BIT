# Assignment_Control_Led_By_BIT

# Python Program on Raspberry Pi to Control an 8-LED Array Connected to GPIO Pins

## Project Overview

This project demonstrates how to control an array of 8 LEDs connected to GPIO pins on a Raspberry Pi. The LEDs follow a predefined shifting pattern based on an 8-bit sequence, with a button used to start and stop the effect. The program can also be tested on a computer using a GPIO simulation library.

## Misson

1. One start/stop control button: run/stop LED effect
2. Control a series of 8 LEDs connected to 8 GPIO pins corresponding to 8 bits of 1 byte according to the following rule:
    - Initially, all bits are 0
    - Next, the 2 bits in the center have the value 1
    - Next, the 2 bits with the value 1 will move to the 2 opposite ends until they are close to the edges of the two sides and disappear
    - The 2 bits with the value 1 will appear from the 2 sides and move back to the center, then repeat
    - Image illustration example:
        00011000

        00100100

        01000010

        10000001

        00000000

        10000001

        01000010

        00100100

        00011000

## Hint 
- After each byte state is changed, write the bits to the corresponding GPIO ports to control the LED to light up (delay at least 1 second to observe the LED state before switching to the new state). Use the GPIO simulation library when running the test on the computer.
- If you don't have a physical kit you can use the GPIO pin emulator library by downloading the GPIOEmulator folder.