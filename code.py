# CircuitPlaygroundExpress_ReactionGame
# Author: Ron Guest

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
speed = {
    1: 0.5,
    2: 0.1,
    3: 0.05,
    4: 0.02,
    5: 0.0
}

cpx.pixels.fill(BLACK)
cpx.pixels.show()

difficulty = 1

# The game itself. Choose a random target LED, start spinning the red LED until users touches pad A7
def game(delay):
    # The LEDs are 1..10 from a player's perspective
    # but 0..9 in terms of the pixels array index
    # target is the LED the user needs to 'capture' to win
    target = random.randint(0, 9)
    print("Player target =",target+1)
    print("Speed set to ", delay)
    #time.sleep(5)

    print("Range is ", range(cpx.pixels.n))
    print("Len of pixels is ", len(cpx.pixels))
    cpx.pixels.fill(BLACK)
    # Keep cycling LEDS until the user touches A7
    # Target LED is lit RED, others BLUE
    while True:
        for i in range(cpx.pixels.n):
            if i == target:
                cpx.pixels[i] = RED
            else:
                cpx.pixels[i] = BLUE
            # Handle the edge case of 0 wrapping backwards to 9
            if i == 0:
                cpx.pixels[len(cpx.pixels)-1] = BLACK
            else:
                cpx.pixels[i-1] = BLACK

            # Give the player time to react
            time.sleep(delay)
            if cpx.touch_A7:
                print("Player touched A7, i = ",i+1)
                if i == target:
                    won()
                else:
                    lost()
                return

def lost():
    cpx.pixels.fill(RED)
    cpx.play_tone(FAILURE_TONE, 1.5)
    cpx.pixels.fill(BLACK)

def won():
    cpx.pixels.fill(GREEN)
    cpx.play_tone(VICTORY_TONE, .3)
    cpx.play_tone(1.5*VICTORY_TONE, .3)
    cpx.play_tone(2*VICTORY_TONE, .3)
    cpx.play_tone(2.5*VICTORY_TONE, .3)
    cpx.pixels.fill(BLACK)

# Main loop of the game: bump difficulty setting if users presses A, start game when user presses B
while True:
    # Wait until player pushes button B before starting game, flash LEDs blue while waiting
    while not cpx.button_b:
        cpx.pixels.fill(BLUE)
        for i in range(difficulty):
            cpx.pixels[i] = RED
        # 5 is max difficulty, wrap to difficulty one after that
        if cpx.button_a:
            if difficulty < 5:
                difficulty += 1
            else:
                difficulty = 1
            print("Difficulty set to", difficulty)
            cpx.pixels[difficulty-1] = RED
        time.sleep(.3)
        # Fill "black" to turn them off momentarily for a flashing effect
        cpx.pixels.fill(BLACK)
        time.sleep(.1)
    # Give player 1 second to get ready for the game to start
    time.sleep(1)
    game(speed[difficulty])
