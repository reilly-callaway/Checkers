#Idea for text-based interactive menu for a game.

from msvcrt import getch#Magics that will register left/right arrow presses
from os	import system	#Magics including able clear terminal/command line

ArrowPosition = 0

# Left '\xe0' 'K' = 224 75
# Right '\xe0' 'M' = 224 77
# Enter '\r' = 13
# ESC ...   = 27

key = 0

options = ["Play", "Rules", "Settings", "sWag3KawL5u"]

while key != 27:
	key = ord(getch())
	system('CLS')
	if key == 13:
		print("Option \"{}\" Selected".format(options[ArrowPosition-1]))
	elif key == 224:
		key = ord(getch())
		if key == 75 and ArrowPosition > 1:
			ArrowPosition -= 1
		elif key == 77 and ArrowPosition < 4:
			ArrowPosition += 1
	Space = 15

	# for i in options:
	#  	if len(i) > Space + 4: Space = len(i) + 4

	for m in range(20):
		print("This is filler text", end=" ")
	print()
	
	for n in options:
		print(" "*(Space-(len(n))), n, end="")
	print()

	print(" " * ((ArrowPosition * (Space+1)) - len(options[ArrowPosition-1]) - 1), "^", '\n', end="")
