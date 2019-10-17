def period(length , gravity):
    import math as m
    if isinstance(length, (float, int)):
        if length <= 0:
            return 'Input positive numbers only.'
        if gravity <= 0:
            return 'Input positive numbers only.'
        else:
            return 2*m.pi*((length/gravity)**0.5)
    else: 
        return 'Please input only numbers.'

# print(period(7.5,-9.8))
            