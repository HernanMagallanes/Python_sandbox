import pyinputplus as pyip

while True:
    prompt = 'Want to know how to keep an idiot busy for hours ? \n'
    response = pyip.inputYesNo(prompt)

    if response == 'no':
        print('Thank you. Have a nice day.')
        break

''' 
pyip.inputStr()
pyip.inputNum()

pyip.inputChoice()
pyip.inputMenu()

pyip.inputDatetime()

pyip.inputYesNo()
pyip.inputBool()

pyip.inputEmail()
pyip.inputFilepath()
pyip.inputPassword()

pyip.inputNum()
# greaterThan
# lessThan
# min , max

# limit , default , timeout
# allowRegexes , blockRegexes

pyip.inputCustom()
# func
'''
