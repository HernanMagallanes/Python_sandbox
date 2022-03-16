# Rock, Paper, Scissors game

# 1st  instruction
# 2nd move (Loop) - exit user win
# msg, board
# 3rd end - q -> exit

# pc move - var random - if 3 returns
# user move - input
# game - if

from random import randint
import sys

print('\n \t Rock, Paper, Scissors !!! \n ')

# Board
win_counter, lose_count, tie_count = 0, 0, 0
print(f'Board: {win_counter} Wins, {lose_count} Losses, {tie_count} Ties')

continue_game = True

while continue_game:

    user_move = str(input('Enter your move:  (1)Rock , (2)Paper , (3)Scissors or (q)Quit : '))

    # Quit game
    if user_move != 'r' and user_move != 'p' and user_move != 's':
        if user_move != '1' and user_move != '2' and user_move != '3':
            print('\n Bye !')
            sys.exit()
            # handling errors

    if user_move == 'r' or user_move == str(1):
        user_move = 'r'
        print("Rock vs ...")

    elif user_move == 'p' or user_move == str(2):
        user_move = 'p'
        print("Paper vs ...")

    elif user_move == 's' or user_move == str(3):
        user_move = 's'
        print("Scissors vs ...")

    pc_var = randint(0, 2)

    if pc_var < 1:
        # Rock: 0
        pc_move = 'r'
        print("Rock \n")

    elif pc_var < 2:
        # Paper: 1
        pc_move = 'p'
        print("Paper \n")

    else:
        # Scissors: 3
        pc_move = 's'
        print("Scissors \n")

    # Tie
    if user_move == pc_move:
        tie_count += 1

        print('Is is a Tie!')
        print(f'{win_counter} Wins, {lose_count} Losses, {tie_count} Ties \n')
        continue

    # Game
    if user_move == 'r':
        if pc_move == 's':
            win_counter += 1
            continue_game = False

            print('You Win!')
            print(f'{win_counter} Wins, {lose_count} Losses, {tie_count} Ties \n')

        else:
            lose_count += 1

            print('You lose! ')
            print(f'{win_counter} Wins, {lose_count} Losses, {tie_count} Ties \n')

    elif user_move == 'p':
        if pc_move == 'r':
            win_counter += 1
            continue_game = False

            print('You Win!')
            print(f'{win_counter} Wins, {lose_count} Losses, {tie_count} Ties \n')

        else:
            lose_count += 1

            print('You lose!')
            print(f'{win_counter} Wins, {lose_count} Losses, {tie_count} Ties \n')

    elif user_move == 's':
        if pc_move == 'p':
            win_counter += 1
            continue_game = False

            print('You Win!')
            print(f'{win_counter} Wins, {lose_count} Losses, {tie_count} Ties \n')

        else:
            lose_count += 1

            print('You lose!')
            print(f'{win_counter} Wins, {lose_count} Losses, {tie_count} Ties \n')
