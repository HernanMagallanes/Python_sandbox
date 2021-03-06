# Tic Tac Toe game
# 1st board
# 2nd turns (valid move)
# 3rd win / lose / tie (rules / valid moves)

import random
import sys

turn_counter = 0

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}


def print_board():
    global theBoard
    print('\n')
    print(theBoard['top-L'] + '|' + theBoard['top-M'] + '|' + theBoard['top-R'])
    print('-+-+-')
    print(theBoard['mid-L'] + '|' + theBoard['mid-M'] + '|' + theBoard['mid-R'])
    print('-+-+-')
    print(theBoard['low-L'] + '|' + theBoard['low-M'] + '|' + theBoard['low-R'])
    print('\n')


def print_moves():
    global theBoard
    line = ''
    c = 0
    print('\n Moves :')

    for k in theBoard:
        line += ' | ' + k

        if c == 2 or c == 5 or c == 8:
            print(line)
            line = ''

        c += 1

    pass


def who_start():
    coin = random.randint(0, 1)

    if coin == 0:
        print('\n You start !')
        return True

    print('PC start !')
    return False


def empty_spaces():
    global theBoard
    spaces = []

    for k, v in theBoard.items():
        if v == ' ':
            spaces.append(k)

    return spaces


def user_turn():
    global theBoard
    global turn_counter
    spaces = empty_spaces()

    while True:
        move = input('move: ')

        if move not in spaces:
            print('move not valid !')

        else:
            theBoard[move] = 'x'
            break

    turn_counter += 1
    print_board()

    if turn_counter >= 2:
        win_game()

    pc_turn()
    pass


def pc_turn():
    print('wait ...')
    global theBoard
    global turn_counter
    spaces = empty_spaces()

    pc_move = random.randint(1, len(spaces))
    c = 0

    while True:
        for k in theBoard.keys():
            if c == pc_move:

                if k not in spaces:
                    print('wait ... ')
                    pc_move = random.randint(1, 9)
                    continue

                else:
                    print('Move !')
                    # print(k)
                    theBoard[k] = 'o'
                    break
            c += 1
        break

    print_board()

    turn_counter += 1

    if turn_counter >= 2:
        win_game()

    user_turn()

    pass


def winner(mark):
    if mark == 'x':
        print('You win!')
        sys.exit()
    else:
        print(mark)
        sys.exit()

    pass


def win_game():
    global theBoard
    # 3 horizontal (top, mid, low)
    # 3 verticals (L, M, R)
    # 2 diagonals

    # mid-M in 1 H , 1 V and 2 D

    if theBoard['mid-M'] != ' ':

        lookup_mark = theBoard['mid-M']

        # vertical
        if theBoard['top-M'] == lookup_mark and theBoard['low-M'] == lookup_mark:
            winner(lookup_mark)

        # horizontal
        if theBoard['mid-L'] == lookup_mark and theBoard['mid-R'] == lookup_mark:
            winner(lookup_mark)

        # diagonal 1
        if theBoard['top-R'] == lookup_mark and theBoard['low-L'] == lookup_mark:
            winner(lookup_mark)

        # diagonal 2
        if theBoard['top-L'] == lookup_mark and theBoard['low-R'] == lookup_mark:
            winner(lookup_mark)

    # top-L in 1 H and 1 V

    if theBoard['top-L'] != ' ':
        lookup_mark = theBoard['top-L']

        # horizontal
        if theBoard['mid-L'] == lookup_mark and theBoard['mid-L'] == lookup_mark:
            winner(lookup_mark)

        # vertical
        if theBoard['mid-M'] == lookup_mark and theBoard['low-L'] == lookup_mark:
            winner(lookup_mark)

    # low-R in 1 H and 1 V

    if theBoard['low-R'] != ' ':
        lookup_mark = theBoard['low-R']

        # horizontal
        if theBoard['low-M'] == lookup_mark and theBoard['low-L'] == lookup_mark:
            winner(lookup_mark)

        # vertical
        if theBoard['top-R'] == lookup_mark and theBoard['mid-R'] == lookup_mark:
            winner(lookup_mark)

    pass


######## GAME ########

print_moves()
start = who_start()
print_board()

if start:
    user_turn()
pc_turn()
