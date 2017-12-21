# Reaction-Game
Reaction game based on Circuit Playground Express

* The neopixels will cycle counter clockwise. All will be blue except one which will be redistribution
* The object of the game is to touch the pad A7 right when one of the LEDs changes to redistribution
* When first started the neopixels will all flash blue except for #1 being RED indicating the initial difficulty setting of 1 (easiest)
* Press push button A to start the game. It will turn off the neopixels for 1 second so you can prepare then begin cycling until you press A7
* If you get it right a little victory tone set is played and all the neopixels turn GREEN
* If you miss then there is a sadder tone and the neopixels go RED
* After you touch A7 you can hit push button B to play again
* If you want to increase the difficulty press push button A. Difficulty is 1..5 and the number of RED neopixels shows the current difficulty setting
* Difficulty 5 has the game run as fast as it can
