# CircuitPlaygroundExpress_ReactionGame

import board
import neopixel
import time
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
    for i in range(len(pixels)):
        pixels[i] = BLACK
        if i == len(pixels)-1:
            pixels[0] = PURPLE
        else:
            pixels[i+1] = PURPLE
            time.sleep(delay)
    won()

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
        time.sleep(.1)
        pixels.fill(BLACK)
        time.sleep(.1)
    # Give player 1 second to get ready for the game to start
    time.sleep(1)
    game(.5)
