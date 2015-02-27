import os

def PlayerTurn(player):
	print('Player {}\'s turn:'.format(player))
	PieceX, PieceY = input('Piece?(x,y): ').split(',')
	PieceX, PieceY = int(PieceX)-1, int(PieceY)-1
	if board[PieceY][PieceX] == player:
		MoveX, MoveY = input('Move?(x,y): ').split(',')
		MoveX, MoveY = int(MoveX)-1, int(MoveY)-1
		if (MoveX == PieceX + 1 or MoveX == PieceX - 1) and (MoveY == PieceY + 1 or MoveY == PieceY - 1) and board[MoveY][MoveX] == '-':
			board[PieceY][PieceX] = '-'
			board[MoveY][MoveX] = player #Standard Move
		elif (MoveX == PieceX + 2 or MoveX == PieceX - 2) and (MoveY == PieceY + 2 or MoveY == PieceY - 2) and (board[MoveY][MoveX] == '-') and (board[int(PieceY+((MoveY-PieceY)/2))][int(PieceX+((MoveX-PieceX)/2))] != '-' and board[int(PieceY+((MoveY-PieceY)/2))][int(PieceX+((MoveX-PieceX)/2))] != player):
			board[PieceY][PieceX] = '-'							#Scoring Happens here
			board[MoveY][MoveX] = player 						#Jump move
			board[int(PieceY+((MoveY-PieceY)/2))][int(PieceX+((MoveX-PieceX)/2))] = '-' #Need to configure this so you have option 
			Score[player] += 1																#to make another jump move if possible
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
	if Score[Player1] >= 12: break;
	os.system('CLS')
	PrintBoard()
	PlayerTurn(Player2)
	if Score[Player2] >= 12: break;
	os.system('CLS')

