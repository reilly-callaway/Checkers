#Idea for text-based interactive menu for a game.

from msvcrt import getch#Magics that will register left/right arrow presses
from os	import system	#Magics including able clear terminal/command line
import webbrowser

import checkers
import settings

# Left '\xe0' 'K' = 224 75
# Right '\xe0' 'M' = 224 77
# Enter '\r' = 13
# ESC ...   = 27

system('MODE 50')
system('COLOR A')

ArrowPosition = 1
key = 0
options = ["Play", "Rules", "Settings"]
Space = len(max(options, key=len)) + 4

while key != 27:
	system('CLS')

	for m in range(10):
		print("This is filler text", end=" ")
	print()
	
	for n in options:
		print(" "*(Space-(len(n))), n, end="")
	print()

	print(" " * ((ArrowPosition * (Space+1)) - len(options[ArrowPosition-1]) - 1), "^", '\n', end="")

	key = ord(getch())

	if key == 13:
		print('Option "{}" Selected'.format(options[ArrowPosition-1]))
		if options[ArrowPosition-1] == "Play":
			checkers.Game()
		elif options[ArrowPosition-1] == "Rules":
			webbrowser.open('http://en.wikipedia.org/wiki/Draughts#General_rules', new=2)
		elif options[ArrowPosition-1] == "Settings":
			settings.Set()
	elif key == 224:
		key = ord(getch())
		if key == 75 and ArrowPosition > 1:
			ArrowPosition -= 1
		elif key == 77 and ArrowPosition < len(options):
			ArrowPosition += 1