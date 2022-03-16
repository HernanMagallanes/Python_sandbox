import pyinputplus as pyip

total_cost, sandwich_cost = 0, 0

breads_prices = {'wheat': 10, 'white': 12, 'sourdough': 14}
proteins_prices = {'chicken': 10, 'turkey': 20, 'ham': 30, 'tofu': 40}
cheeses_prices = {'cheddar': 5, 'swiss': 6, 'mozzarella': 7}

print('Welcome ! \n')

print('what type of bread ?')
bread = pyip.inputMenu(['wheat', 'white', 'sourdough'])
sandwich_cost += breads_prices[bread]

print('what type of meat ?')
protein = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'])
sandwich_cost += proteins_prices[protein]

with_cheese = pyip.inputYesNo('want cheese ?  ')

if with_cheese == 'yes' or with_cheese == 'y':
    print('what type of cheese ?')
    cheese = pyip.inputMenu(['cheddar', 'swiss', 'mozzarella'])
    sandwich_cost += cheeses_prices[cheese]
    pass

condiment = pyip.inputYesNo('want condiment ?  ')

if condiment:
    sandwich_cost += 2

prompt_e = 'How many sandwiches ?'
n_sandwiches = pyip.inputInt('How many sandwiches ?  ')

total_cost = sandwich_cost * n_sandwiches

print('\n')
print(f'orders:{n_sandwiches} sandwich: ${sandwich_cost}  ')
print(f'Total: ${total_cost}')
