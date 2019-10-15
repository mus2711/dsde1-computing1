

def period(length=5, gravity=9.8):
    import math as m
    if isinstance(length and gravity, (float, int)):
        if length and gravity <= 0:
            print('Input positive numbers only.')
        else:
            return 2*m.pi*((length/gravity)**0.5)
    else:
        print('Please input only numbers.') 

userlength = float(input('input length: '))
usergravity = float(input('input gravity: '))
print(period(userlength, usergravity))
