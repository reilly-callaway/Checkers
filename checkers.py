import os

def MultiJump(player, PieceX, PieceY):
	# Piece position = moved position.
	#Already did this before start of function!
													
	# check if new jump is possible --> if not return(turns over)
	if(True):#Jump move possible
		
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
			MultiJump(player, PieceX, PieceY)
		else:
			print('INVALID MOVE!!!')
			MultiJump(player, PieceX, PieceY)
		# If not --> Invalid move --> get input again. 
	else:
		return
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
			MultiJump(player, PieceX, PieceY)
		else:
			print('INVALID MOVE!!!')
			PlayerTurn(player)
	else:
		print('INVALID PIECE!!!')
		PlayerTurn(player)

def PrintBoard():
	print('Player1(X): {} Player2(O): {}'.format(Score[Player1], Score[Player2]))
	print('  1 2 3 4 5 6 7 8')
	for i, j in enumerate(board):
		print(i+1, end=' ')
		for k in j:
			print(k, end=' ')
		print()

Player1 = 'X'
Player2 = 'O'

Score = {Player1:0, Player2:0}

board = [
['X', '*', 'X', '*', 'X', '*', 'X', '*'],
['*', 'X', '*', 'X', '*', 'X', '*', 'X'], 
['X', '*', 'X', '*', 'X', '*', 'X', '*'], 
['*', '-', '*', '-', '*', '-', '*', '-'], 
['-', '*', '-', '*', '-', '*', '-', '*'],
['*', 'O', '*', 'O', '*', 'O', '*', 'O'], 
['O', '*', 'O', '*', 'O', '*', 'O', '*'],
['*', 'O', '*', 'O', '*', 'O', '*', 'O']]


while (True):
	PrintBoard()
	PlayerTurn(Player1)
	os.system('CLS')				#Remove this is using the IDLE, if using terminal/command line/cmd/whatever else you kids call it nowerdays:
	if Score[Player1] >= 2: break;	#It will clear the terminal of all text so it doesn't look like reprinting the board over and over. Just one board :)
	PrintBoard()			
	PlayerTurn(Player2)
	os.system('CLS')				#Remove this one too if using IDLE, I haven't tested it but it will probably break it :(
	if Score[Player2] >= 2: break;

PrintBoard()
print("Player 1 (X) WINS!!!" if Score[Player1] >= Score[Player2] else "Player 2 (O) WINS!!!")