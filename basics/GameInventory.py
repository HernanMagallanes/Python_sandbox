# Game inventory
# data structure to model the player 's inventory

# Part I
# display inventory with correct format

stuff1 = {'rope': 1,
          'torch': 6,
          'gold coin': 42,
          'dagger': 1,
          'arrow': 12, }


def display_inventory(stuff_dict):
    total_items = 0
    print('Inventory:')

    for k, v in stuff_dict.items():
        total_items += v
        print(v, k)

    print(f'\n Total number of items : {total_items}')
    pass


# Part II
# add loot to the inventory and display new inventory

stuff2 = {'rope': 1,
          'gold coin': 42}

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def add_to_inventory(stuff_dict, loot):
    # items in out inventory
    aux_lst = list(stuff_dict.keys())

    for item in loot:
        if item in aux_lst:
            # print(f'item add: {item} \n')
            stuff_dict[item] += 1

        else:
            # print(f'new item : {item} \n')
            stuff_dict.update({item: 1})

    pass


# Part I
display_inventory(stuff1)
print('')

# Part II
display_inventory(stuff2)
print('')

add_to_inventory(stuff2, dragonLoot)
display_inventory(stuff2)
