# Tower of Hanoi
# puzzle uses a stack of disks of different sizes
# and tree poles

# To solve the puzzle, the player must move the stack of disks
# to one of the other poles.

#  Restrictions:
# 1. move one disk at a time
# 2. move disks to and from the top of a tower
# 3. never place a larger disk on top of a smaller disk

import copy
import sys

TOTAL_DISKS = 5

# start with all disks on tower A
SOLVED_TOWER = list(range(TOTAL_DISKS, 0, -1))


def main():
    # runs the game
    print('The tower of hanoi')

    # dicts represent the towers A, B, C
    # values represent disks size

    towers = {'A': copy.copy(SOLVED_TOWER), 'B': [], 'C': []}

    while True:
        display_towers(towers)

        # user moves
        fromTower, toTower = get_player_move(towers)

        # move disk
        disk = towers[fromTower].pop()
        towers[toTower].append(disk)

        # check towers
        if SOLVED_TOWER in (towers['B'], towers['C']):
            display_towers(towers)
            print('Puzzle solved! Well done!')
            sys.exit()


def get_player_move(towers):
    """
    asks the player for move.
    returns fromTower, toTower
    """

    while True:
        print("Enter the letters of 'from' and 'to' or QUIT.")
        print('')

        response = input('> ').upper().strip()

        if response == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        # validation
        if response not in ('AB', 'AC', 'BA', 'BC', 'CA', 'CB'):
            print('Enter one of AB, AC, BA, BC, CA or CB.')
            continue

        fromTower, toTower = response[0], response[1]

        if len(towers[fromTower]) == 0:
            print('You selected a tower with no disks.')
            continue

        elif len(towers[toTower]) == 0:
            return fromTower, toTower

        elif towers[toTower][-1] < towers[fromTower][-1]:
            print("Can't put larger disks on top of smaller ones.")
            continue

        else:
            # valid move
            return fromTower, toTower


def display_towers(towers):
    """
    Display the three towers with their disks
    """
    for level in range(TOTAL_DISKS, -1, -1):
        for tower in (towers['A'], towers['B'], towers['C']):
            if level >= len(tower):
                # display pole with no disk
                display_disk(0)
            else:
                # display the disk
                display_disk(tower[level])
        print()

    # display tower labels
    emptySpace = ' ' * (TOTAL_DISKS)
    print("{0} A{0}{0} B{0}{0} C\n".format(emptySpace))


def display_disk(width):
    """
    display a disk of the given width.
    width 0 means no disk.
    """
    emptySpace = ' ' * (TOTAL_DISKS - width)

    if width == 0:
        print(f'{emptySpace}||{emptySpace}', end='')
    else:
        disk = '@' * width
        numLabel = str(width).rjust(2, '_')
        print(f'{emptySpace}{disk}{numLabel}{disk}{emptySpace}', end='')


if __name__ == '__main__':
    main()
