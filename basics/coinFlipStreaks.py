# flip 100 coins 'H' or 'T'
# result  > list() Ex: H H T T H T

# 1st generates streaks
# list len 100 (experiment)

# 2nd check for a streak of 6
# 10.000 times > count 6 streak in experiment
# chance of streak of 6 coins equal (%)


import random


def coin_exp_list(n_coins=100):
    exp_list = []

    for i in range(0, n_coins):
        coin = random.randint(0, 1)
        if coin <= 0.5:
            exp_list.append('H')
        else:
            exp_list.append('T')

    return exp_list


def coin_exp_str(n_coins=100):
    exp_str = ''

    for i in range(0, n_coins):
        coin = random.randint(0, 1)
        if coin <= 0.5:
            exp_str += 'H'
        else:
            exp_str += 'T'

    return exp_str


N = 10_000
# N = 10
n = 100

# total chance - avg of chances
# p_total = p_total_count / total_intents
p_total_count, total_intents = 0, 0

for experimentNumber in range(N):
    # steaks by exp
    streak_count_in_exp = 0
    # total intents by exp
    number_of_intents_in_exp = 0
    # chance in exp (%)
    # p_exp = (streak_count_in_exp / number_of_intents_in_exp) * 100

    exp = coin_exp_str(n)
    # print(f'Experiment N: {experimentNumber}')

    # streak check
    for c in range(len(exp)):
        number_of_intents_in_exp += 1
        streak_check = exp[c:c + 6]

        if len(streak_check) != 6:
            # print('Not enough coins')
            break

        if streak_check == 'HHHHHH' or streak_check == 'TTTTTT':
            streak_count_in_exp += 1
            # streak_count_total += 1

    p_exp = (streak_count_in_exp / number_of_intents_in_exp) * 100

    p_exp_round = round(p_exp, 2)
    p_total_count += p_exp_round

    total_intents += number_of_intents_in_exp

    # print(f'Streaks: {streak_count_in_exp}')
    if N < 20:
        print('\n')
        print(f'Chance of a streak: {p_exp_round} %')
        # print(p_total_count)
        # print(total_intents)

p_total = p_total_count / total_intents
p_total_round = round(p_total, 2)

print('\n')
print(f'Total chance of a streak: {p_total_round} %')
