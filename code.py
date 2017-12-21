# CircuitPlaygroundExpress_ReactionGame 

import board
import neopixel
import time
import math
import audiobusio

RED = (0x10, 0, 0) # 0x100000 also works
YELLOW=(0x10, 0x10, 0)
GREEN = (0, 0x10, 0)
AQUA = (0, 0x10, 0x10)
BLUE = (0, 0, 0x10)
PURPLE = (0x10, 0, 0x10)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=.2)
pixels.fill(BLACK)
pixels.show()

mic = audiobusio.PDMIn(board.MICROPHONE_CLOCK, board.MICROPHONE_DATA, frequency=16000)
time.sleep(0.11)
volume_sample = bytearray(120)
mic.record(volume_sample, len(volume_sample))
#print(volume_sample)
input_floor = max(volume_sample) - min(volume_sample) +1
print("Input floor: ", input_floor)

while True:
    for i in range(len(pixels)):
        pixels[i] = BLACK
        if i == len(pixels)-1:
            pixels[0] = GREEN
        else:
            pixels[i+1] = GREEN
        # Sample audio for a bit.
        mic.record(volume_sample, len(volume_sample))
        #print(volume_sample)
        magnitude = max(volume_sample) - min(volume_sample)
        print(magnitude)
        if magnitude > (input_floor + 30):
            pixels.fill(RED)
            time.sleep(5)
