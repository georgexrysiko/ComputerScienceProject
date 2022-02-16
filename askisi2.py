import random

sum = 0
games = 100
small = medium = large = 9 #not necessary
row  = box = ring_size = 3

#for same size
def sameSize(table):
    #horizontal
    for i in range(row):
        for j in range(ring_size):
            if table[i][0][j] == table[i][1][j] == table[i][2][j] == True:
            #table[row][box][ring_size]
                return True
    #vertical
    for i in range(box):
        for j in range(ring_size):
            if table[0][i][j] == table[1][i][j] == table[2][i][j] == True:
                return True
    #diagonal
    for i in range(ring_size):
        if table[2][0][i] == table[1][1][i] == table[0][2][i] == True:
            return True
        elif table[0][0][i] == table[1][1][i] == table[2][2][i] == True:
            return True

#from smaller to bigger
def smallTobig(table):
    win = victory()
    #horizontal
    for i in range(row):
        if table[i][0][0] == table[i][1][1] == table[i][2][2] == True:
            return True
        elif table[i][0][2] == table[i][1][1] == table[i][2][0] == True:
            return True
    #vertical
    for i in range(box):
        if table[0][i][0] == table[1][i][1] == table[2][i][2] == True:
            return True
        elif table[0][i][2] == table[1][i][1] == table[2][i][0] == True:
            return True
    #diagonal
    if table[0][0][0] == table[1][1][1] == table[2][2][2] == True:
        return True
    elif table[0][0][2] == table[1][1][1] == table[2][2][0] == True:
        return True
    elif table[2][0][2] == table[1][1][1] == table[0][2][0] == True:
        return True
    elif table[2][0][0] == table[1][1][1] == table[0][2][2] == True:
        return True
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

    row1 = [box1, box2, box3]
    row2 = [box4, box5, box6]
    row3 = [box7, box8, box9]

    table = [row1, row2, row3]

    win = victory()
    while (win is False):
        random_row = random.choice([0,1,2])
        random_box = random.choice([0,1,2])
        random_size_ring = random.choice([0,1,2])
        if  not table[random_row][random_box][random_size_ring]:
            sum += 1
            table[random_row][random_box][random_size_ring] = True
        if not win:
            win = sameSize(table)
        if not win:
            win = smallTobig(table)

    average = (sum/games)

print("Average number of movements for 100 games: " + str(average))