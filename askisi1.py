import random

sum = 0
games = 100
small = medium = large = 9 #not necessary
box = 9
ring_size = 3

#for same size
def sameSize(table):
    #horizontal
    for j in range(ring_size):
        if table[0][j] == table[1][j] == table[2][j] == True:
        #table[box][ring_size]
            return True
        elif table[3][j] == table[4][j] == table[5][j] == True:
            return True
        elif table[6][j] == table[7][j] == table[8][j] == True:
            return True
    #vertical
    for j in range(ring_size):
        if table[0][j] == table[3][j] == table[6][j] == True:
            return True
        elif table[1][j] == table[4][j] == table[7][j] == True:
            return True
        elif table[2][j] == table[5][j] == table[8][j] == True:
            return True
    #diagonal
    for i in range(ring_size):
        if table[0][i] == table[4][i] == table[8][i] == True:
            return True
        elif table[2][i] == table[4][i] == table[6][i] == True:
            return True

#from smaller to bigger
def smallTobig(table):
    win = victory()
    #horizontal
    if table[0][0] == table[1][1] == table[2][2] == True:
        win = True
    elif table[0][2] == table[1][1] == table[2][0] == True:
        win = True
    elif table[3][0] == table[4][1] == table[5][2] == True:
        win = True
    elif table[3][0] == table[4][1] == table[5][2] == True:
        win = True
    elif table[6][0] == table[7][1] == table[8][2] == True:
        win = True
    elif table[6][2] == table[7][1] == table[8][0] == True:
        win = True
    #vertical
    if table[0][0] == table[3][1] == table[6][2] == True:
            return True
    elif table[0][2] == table[3][1] == table[6][0] == True:
            return True
    elif table[1][0] == table[4][1] == table[7][2] == True:
        return True
    elif table[1][2] == table[4][1] == table[7][0] == True:
        return True
    elif table[2][0] == table[5][1] == table[8][1] == True:
        return True
    elif table[2][2] == table[5][1] == table[8][0] == True:
        return True
    #diagonal
    if table[0][0] == table[4][1] == table[8][2] == True:
        win = True
    elif table[0][2] == table[4][1] == table[8][0] == True:
        win = True
    elif table[2][0] == table[4][1] == table[6][2] == True:
        win = True
    elif table[2][2] == table[4][1] == table[6][0] == True:
        win = True
    return win

def victory():
    win = False
    return win

for i in range(games):
    #box[small,medium,large]
    box1 = [False, False, False]
    box2 = [False, False, False]
    box3 = [False, False, False]
    box4 = [False, False, False]
    box5 = [False, False, False]
    box6 = [False, False, False]
    box7 = [False, False, False]
    box8 = [False, False, False]
    box9 = [False, False, False]

    table = [box1, box2, box3, box4, box5, box6, box7, box8, box9]

    win = victory()
    while (win is False):
        random_box = random.choice([0,1,2,3,4,5,6,7,8])
        random_size_ring = random.choice([0,1,2])
        if not table[random_box][random_size_ring]:
            sum += 1
            table[random_box][random_size_ring] = True
        if not win:
            win = sameSize(table)
        if not win:
            win = smallTobig(table)

    average = (sum/100)
    print("Random box, Random size: " + str(random_box) + "," + str(random_size_ring))

print("\nAverage number of movements for 100 games: " + str(average))