# display list of lists right-justified

tableDate = [
    ['apples', 'oranges', 'cherries', 'banana'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose']
]


def print_table(table):
    rows, cols = len(table), len(table[1])
    # store col width
    col_widths = []
    index = 0

    # find longest string in each list
    for r in table:
        aux_lst = []

        for c in r:
            aux_lst.append(len(c))

        col_widths.append(max(aux_lst))
        index += 1

    # print each line first item in each list
    line = ''

    for c in range(0, cols):
        for r in range(0, rows):
            s = table[r][c].rjust(col_widths[0])
            line += s

        print(line)
        line = ''
    pass


print_table(tableDate)
