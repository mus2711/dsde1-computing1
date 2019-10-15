import random as r
number = (r.randint(1,10))
print('Choose a number between 1 to 10')
i = 0

while i < 3:
    x = input('Your guess: ' )
    guess = int(x)
    if guess > 10 or guess < 1:
        print('Please choose a number only between 1 and 10.')
    elif guess == number:
        print('You guessed correct!')
        break
    else:
        i += 1
        wrong = 'You guessed the wrong number. Remaining guesses: {}'
        print(wrong.format(3-i))
        
if i == 3:
    txt = 'The number was {}'
    print(txt.format(number))