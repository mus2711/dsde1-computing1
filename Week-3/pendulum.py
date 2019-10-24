def period(length , gravity):
    import math as m
    if isinstance(length, (float, int)) and isinstance(gravity, (float, int)):
        if length <= 0 or gravity <=0:
            return 'Input positive numbers only.'
        else:
            return 2*m.pi*((length/gravity)**0.5)
    else: 
        raise(TypeError)

print(period(7.5,'helo'))
            