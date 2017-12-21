# Reaction-Game
Reaction game based on Circuit Playground Express

* The neopixels will cycle counter clockwise. All will be blue except one which will be red which is the player's target
* The object of the game is to touch the pad A7 right when the one LED changes to red (random for each game)
* When first started the neopixels will all flash blue except for #1 being RED indicating the initial difficulty setting of 1 (easiest)
* Press push button B to start the game. It will turn off all of the neopixels for 1 second so you can prepare then begin cycling until you touch A7
* If you get it right a little victory tone set is played and all the neopixels turn GREEN
* If you miss then there is a sadder tone and the neopixels go RED
* You can hit push button B to play again
* If you want to increase the difficulty press push button A. Difficulty is 1 to 5 and the number of RED neopixels shows the current difficulty setting
* Difficulty 5 has the game run as fast as it can

I referred to the Simple Simon game for ideas on how to do some of this: https://learn.adafruit.com/circuit-playground-simple-simon/the-structure-of-struct?view=all#circuitpython-version
