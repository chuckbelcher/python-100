year = int(input('What year would you like to check? '))

if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
    print('Yep its a leap year')
else:
    print('nope, not a leap year')
