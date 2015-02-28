import os

#If using the IDLE; remove all "os.system('CLS')" commands, they are pointed out in comments
#The command is designed for terminal/command line use.

#Important note: No error handling has been incorperated yet, if you enter co-ordinates in incorrectly, it will screw up
#If you try to move outside the board, it will screw up but as long as you play by the rules, all should be good :)

def PlayerTurn(player):
	print('Player {}\'s turn:'.format(player))
	PieceX, PieceY = input('Piece?(x,y): ').split(',')
	PieceX, PieceY = int(PieceX)-1, int(PieceY)-1		#Co-ordinates of the piece you want to move
	if board[PieceY][PieceX] == player:
		MoveX, MoveY = input('Move?(x,y): ').split(',') #Co-ordinates of where you want to move it to
		MoveX, MoveY = int(MoveX)-1, int(MoveY)-1
		if (MoveX == PieceX + 1 or MoveX == PieceX - 1) and (MoveY == PieceY + 1 or MoveY == PieceY - 1) and board[MoveY][MoveX] == '-':
			board[PieceY][PieceX] = '-'
			board[MoveY][MoveX] = player 				#Standard Move
			return										#Turns over
		elif (MoveX == PieceX + 2 or MoveX == PieceX - 2) and (MoveY == PieceY + 2 or MoveY == PieceY - 2) and (board[MoveY][MoveX] == '-') and (board[int(PieceY+((MoveY-PieceY)/2))][int(PieceX+((MoveX-PieceX)/2))] != '-' and board[int(PieceY+((MoveY-PieceY)/2))][int(PieceX+((MoveX-PieceX)/2))] != player):
			board[PieceY][PieceX] = '-'	
			board[MoveY][MoveX] = player 				#Jump move
			board[int(PieceY+((MoveY-PieceY)/2))][int(PieceX+((MoveX-PieceX)/2))] = '-' #Need to configure this so you have option 
			Score[player] += 1															#to make another jump move if possible
			PieceX, PieceY = MoveX, MoveY
			PrintBoard()
			MultiJump(player, PieceX, PieceY)
			return
		else:
			print('INVALID MOVE!!!')
			PlayerTurn(player)
	else:
		print('INVALID PIECE!!!')
		PlayerTurn(player)

def JumpMoveCheck(player, PieceY, PieceX):
	for Yadd in (1, -1):
		for Xadd in (1, -1):
			if (len(board)-1 > (PieceY + Yadd)) and (len(board[PieceY + Yadd])-1 > (PieceX + Xadd)) and (PieceY + Yadd >= 0) and (PieceX + Xadd >= 0):
				if(board[PieceY + Yadd][PieceX + Xadd] != '-' and board[PieceY + Yadd][PieceX + Xadd] != player and board[PieceY + (2*Yadd)][PieceX + (2*Xadd)] == '-'): return True;
	return False

def MultiJump(player, PieceX, PieceY):
	# Piece position = moved position.
	#Already did this before start of function!

	# check if new jump is possible --> if not return(turns over)
	if(JumpMoveCheck(player, PieceY, PieceX)):#Jump move possible
		# get input again for new move position
		MoveX, MoveY = input('Move?(x,y): ').split(',') #Co-ordinates of where you want to move it to
		MoveX, MoveY = int(MoveX)-1, int(MoveY)-1
		# check if jump move
		if (MoveX == PieceX + 2 or MoveX == PieceX - 2) and (MoveY == PieceY + 2 or MoveY == PieceY - 2) and (board[MoveY][MoveX] == '-') and (board[int(PieceY+((MoveY-PieceY)/2))][int(PieceX+((MoveX-PieceX)/2))] != '-' and board[int(PieceY+((MoveY-PieceY)/2))][int(PieceX+((MoveX-PieceX)/2))] != player):
			# If jump --> Make jump then repeat
			board[PieceY][PieceX] = '-'	
			board[MoveY][MoveX] = player 				#Jump move
			board[int(PieceY+((MoveY-PieceY)/2))][int(PieceX+((MoveX-PieceX)/2))] = '-' #Need to configure this so you have option 
			Score[player] += 1															#to make another jump move if possible
			PieceX, PieceY = MoveX, MoveY
			PrintBoard()
			MultiJump(player, PieceX, PieceY)
		else:
			print('INVALID MOVE!!!')
			MultiJump(player, PieceX, PieceY)
		# If not --> Invalid move --> get input again. 
	else:
		return

def PrintBoard():
	print('Player1(X): {} Player2(O): {}'.format(Score[Player1], Score[Player2]))
	print('  1 2 3 4 5 6 7 8')
	for i, j in enumerate(board):
		print(i+1, end=' ')
		for k in j:
			print(k, end=' ')		#Magic loops that unpack the board in a readable fashion
		print()

Player1 = 'X'						#If you don't like 'X''s and 'O''s you're welcome to change the pieces...
Player2 = 'O'						#But... It will mean you have to change all the X's and O's in the board below(Ya, have fun trying to do that :P)

Score = {Player1:0, Player2:0}

board = [
['X', '*', 'X', '*', 'X', '*', 'X', '*'],
['*', 'X', '*', 'X', '*', 'X', '*', 'X'],	#I could write some fancy loops here instead
['X', '*', 'X', '*', 'X', '*', 'X', '*'],	#But like, that requires thinking
['*', '-', '*', '-', '*', '-', '*', '-'],	#And honestly I thought just writing it out would be easier
['-', '*', '-', '*', '-', '*', '-', '*'],	#Now I think about it, it was probably a good idea purely for testing
['*', 'O', '*', 'O', '*', 'O', '*', 'O'],
['O', '*', 'O', '*', 'O', '*', 'O', '*'],	#You can move the pieces around to test it out if you want.
['*', 'O', '*', 'O', '*', 'O', '*', 'O']]

os.system('CLS')					#Remove this also if using the IDLE
while (True):
	PrintBoard()
	PlayerTurn(Player1)
	os.system('CLS')				#Remove this is using the IDLE, if using terminal/command line/cmd/whatever else you kids call it nowerdays:
	if Score[Player1] >= 12: break;	#It will clear the terminal of all text so it doesn't look like reprinting the board over and over. Just one board :)
	PrintBoard()			
	PlayerTurn(Player2)
	os.system('CLS')				#Remove this one too if using IDLE, I haven't tested it but it will probably break it :(
	if Score[Player2] >= 12: break;

PrintBoard()
print("Player 1 (X) WINS!!!" if Score[Player1] >= Score[Player2] else "Player 2 (O) WINS!!!")