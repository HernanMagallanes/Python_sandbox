# Conway's game of life simulation
# example of cellular automata

# square board (0: dead, 1:alive)
# living square has 2 or 3 neighbors
# it continues to live om the next step
# if dead square has exactly 4 or living neighbors
# it comes alive on the next step
# each other square remains dead

# list of lists to represent the board
# inner list represents each column
# live '#' , dead ' '

import random
import copy
import time

WIDTH, HEIGHT = 60, 20

# list of list of cell

nextCells = []

for x in range(WIDTH):
    # new column
    column = []
    for y in range(HEIGHT):
        # if (x, y) in ((1, 0), (2, 1), (0, 2), (1, 2), (2, 2)):
        if random.randint(0, 1) == 0:
            # add a  living cell
            column.append('#')
        else:
            # add a  dead cell
            column.append(' ')

    nextCells.append(column)

# main program loop
while True:
    print('\n\n\n\n\n')
    currentCells = copy.deepcopy(nextCells)

    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='')
        print()

    # calculate the next step's cells based on current step's cells
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # neighboring coordinates
            # `% WIDTH` ensures leftCoord is always between 0 and WIDTH-1
            leftCoord = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT

            # count number of living neighbors
            numNeighbors = 0

            # top-left / top / top-right
            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbors += 1
            if currentCells[x][aboveCoord] == '#':
                numNeighbors += 1
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbors += 1

            # left / right
            if currentCells[leftCoord][y] == '#':
                numNeighbors += 1
            if currentCells[rightCoord][y] == '#':
                numNeighbors += 1

            # bottom-left / bottom / bottom-right
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbors += 1
            if currentCells[x][belowCoord] == '#':
                numNeighbors += 1
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbors += 1

            # set cell based on Conway's game of life rules
            if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
                # living cells with 2 or 3 neighbors stay live
                nextCells[x][y] = '#'
            elif currentCells[x][y] == ' ' and numNeighbors == 3:
                # dead cells with 3 neighbors become alive
                nextCells[x][y] = '#'
            else:
                # everything else dies or stay dead
                nextCells[x][y] = ' '

    time.sleep(1)
