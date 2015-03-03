#Idea for text-based interactive menu for a game.

from msvcrt import getch#Magics that will register left/right arrow presses
from os	import system	#Magics including able clear terminal/command line

ArrowPosition = 0

# Left '\xe0' 'K' = 224 75
# Right '\xe0' 'M' = 224 77
# Enter '\r' = 13
key = 0

while key != 27:
	key = ord(getch())
	system('CLS')
	if key == 13:
		print("Option {} Selected".format(ArrowPosition))
	elif key == 224:
		key = ord(getch())
		if key == 75 and ArrowPosition > 1:
			ArrowPosition -= 1
		elif key == 77 and ArrowPosition < 10:
			ArrowPosition += 1
	
	print('01234567890')
	print(" " * (ArrowPosition - 1), "^", '\n', end="")