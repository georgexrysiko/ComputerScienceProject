import random

games = 100

def BishopTakesDown(random_numX1, random_numY1, random_numX2, random_numY2) :
	# If rook is at angle 45 or 225 degree from bishop's Position
	if (random_numX1 - random_numX2 == random_numY1 - random_numY2):
		return True
	# If rook is at angle 135 or 315 degree from bishop's Position
	elif (-random_numX1 + random_numX2 == random_numY1 - random_numY2):
		return True
	else:
		return False

def RookTakesDown (random_numX1, random_numY1, random_numX2, random_numY2):
	if (random_numX1 - random_numX2 == 0):
		return True
	elif (random_numY1 - random_numY2 == 0):
		return True
	else:
		False

def program(Xaxis, Yaxis):
	print("\n\nFor an "+ str(Xaxis) + "*"+ str(Yaxis) +" chessboard: \n")
	print("Player 1 has rook.\nPlayer 2 has bishop.\n")

	random_numX1 = 0
	random_numX2 = 0
	random_numY1 = 0
	random_numY2 = 0
	sum1 = 0
	sum2 = 0

	for i in range(games):
		random_numX1 = 0
		random_numX2 = 0
		random_numY1 = 0
		random_numY2 = 0

		while (True):
			if (random_numX1==random_numX2 and random_numY1==random_numY2):
				random_numX1 = random.randint(1, Xaxis)
				random_numY1 = random.randint(1, Yaxis)
				random_numX2 = random.randint(1, Xaxis)
				random_numY2 = random.randint(1, Yaxis)
			else:
				break

		print("\ncoords for bishop: (" + str(random_numX1) + "," + str(random_numY1) + ")")
		print("coords for rook: (" + str(random_numX2) + "," + str(random_numY2) + ")")

		if (BishopTakesDown(random_numX1, random_numY1, random_numX2, random_numY2)) :
			print("Bishop takes down rook. P2 wins!\n")
			sum2 = sum2 + 1
		elif (RookTakesDown(random_numX1, random_numY1, random_numX2, random_numY2)) :
			print("Rook takes down bishop. P1 wins!\n")
			sum1 = sum1 + 1
		else:
			print("Nobody wins!\n")

		if(i == games - 1):
			print("Game over!\n")
		else:
			print("Run game " + str(games - i-1) + " more times to find the grand winner!")

	print("Score: " + str(sum1) + "-" + str(sum2))

	if (sum1 > sum2):
		print("The grand winner is Player 1!")
	elif (sum1 < sum2):
		print("The grand winner is Player 2!")
	else:
		print("Draw!")


pairs = [[8,8], [7,7], [7,8]]

for p in pairs:
	program(p[0], p[1])