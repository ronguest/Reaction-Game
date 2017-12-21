# CircuitPlaygroundExpress_ReactionGame

import board
import neopixel
import time
import random
from analogio import AnalogIn
from adafruit_circuitplayground.express import cpx

RED = (0x10, 0, 0) # 0x100000 also works
YELLOW=(0x10, 0x10, 0)
GREEN = (0, 0x10, 0)
AQUA = (0, 0x10, 0x10)
BLUE = (0, 0, 0x10)
PURPLE = (0x10, 0, 0x10)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FAILURE_TONE = 50
VICTORY_TONE = 500

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=.2)
pixels.fill(BLACK)
pixels.show()

def game(delay):
    # Seed the random function with noise
    a4 = AnalogIn(board.A4)
    a5 = AnalogIn(board.A5)
    a6 = AnalogIn(board.A6)
    a7 = AnalogIn(board.A7)

    seed  = a4.value
    seed += a5.value
    seed += a6.value
    seed += a7.value

    random.seed(seed)

    # The LEDs are 1..10 from a player's perspective
    # but 0..9 in terms of the pixels array index
    target = random.randint(0, 9)
    print("Player target =",target+1)
    #time.sleep(5)

    pixels.fill(BLACK)
    while True:
        for i in range(len(pixels)):
            if i == target:
                pixels[i] = RED
            else:
                pixels[i] = BLUE
            if i == 0:
                pixels[len(pixels)-1] = BLACK
            else:
                pixels[i-1] = BLACK

            time.sleep(delay)
            if cpx.touch_A5:
                print("Player touched A5, i = ",i+1)
                if i == target:
                    won()
                else:
                    lost()
                return

def lost():
    pixels.fill(RED)
    cpx.play_tone(FAILURE_TONE, 1.5)
    pixels.fill(BLACK)

def won():
    pixels.fill(GREEN)
    cpx.play_tone(VICTORY_TONE, .3)
    cpx.play_tone(1.5*VICTORY_TONE, .3)
    cpx.play_tone(2*VICTORY_TONE, .3)
    cpx.play_tone(2.5*VICTORY_TONE, .3)
    pixels.fill(BLACK)

while True:
    while not cpx.button_b:
        # Wait until player pushes button B before starting, flash blue while waiting
        pixels.fill(BLUE)
        time.sleep(.3)
        pixels.fill(BLACK)
        time.sleep(.1)
    # Give player 1 second to get ready for the game to start
    time.sleep(1)
    game(.05)
