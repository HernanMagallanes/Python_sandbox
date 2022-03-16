import pyinputplus as pyip
import random
import time

n_questions = 10
correct_answers = 0

for question in range(n_questions):
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)

    promp = '#%s: %s x %s = ' % (question, num1, num2)

    try:
        pyip.inputStr(promp, allowRegexes=['^%s$' % (num1 * num2)],
                      blockRegexes=[('.*', 'Incorrect!')],
                      timeout=8, limit=3)
    except pyip.TimeoutException:
        print('Out of time!')

    except pyip.RetryLimitException:
        print('Out of tries!')

    else:
        print('Correct!')
        correct_answers += 1

    time.sleep(1)

print('Score: %s / %s' % (correct_answers, n_questions))
