import random as r
number = (r.randint(1,10))
print('Choose a number between 1 to 10')
guess = input()
if guess == number:
    print('You guessed correct!')
else:
    txt = 'You guessed the wrong number, the number was {}'
    print(txt.format(number))