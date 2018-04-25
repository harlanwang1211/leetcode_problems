'''
Given a 32-bit signed integer, reverse digits of an integer.
For example；
>>> 123
>>> 321

>>> -120
>>> -21
'''
def reverse(x):
    reversed_x = int(str(abs(x))[-1::-1]) * (int(x > 0) - int(x <= 0))
    if (reversed_x <= 2**31 -1) and (reversed_x >= - 2**31):
        return reversed_x
    else:
        return 0

#print(reverse(-150))
#print(reverse(0))
#print(reverse(1563847412))
