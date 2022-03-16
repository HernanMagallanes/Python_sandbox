# list -> 'str1, str2 and str_last '

# insert elements in a list
def insert_element():
    list_to_fill = []
    loop_var = True

    while loop_var:
        new_str = input('insert : ')
        if new_str != '':
            list_to_fill.append(str(new_str))
        else:
            loop_var = False

    return list_to_fill


# list to str
def list_to_string(lst):
    try:
        line = lst[0]
        last_line_index = len(lst) - 1

        if len(lst) != 1:
            for i, item in enumerate(lst):
                if i == 0:
                    continue
                if i == last_line_index:
                    line += ' and ' + item
                    break

                line += ', ' + str(item)

        print(line)

    except IndexError:
        print('empty list')


aux = input('Example(1) or Insert(2) : ')

if aux == '1':
    spam = ['apples', 'bananas', 'tofu', 'cats']
    list_to_string(spam)

elif aux == '2':
    print('\n Insert value for a list')
    print('End with enter')

    aux_list = insert_element()
    list_to_string(aux_list)
