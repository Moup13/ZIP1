import sys

a = [1, 2, 3, 4]
b = (1, 3, 4, 5, 3)
ca = set(a)
cb = set(b)

print(f'type of a is {type(a)}, a = {a}')
print(f'type of b is {type(b)}, b = {b}')
print(f'type of ca looks like {ca}')
print(f'type of cb looks like {cb}')
print(f'type of ca is {type(ca)}, sizeof(ca) = {sys.getsizeof(ca)}')
print(f'type of cb is {type(cb)}, sizeof(cb) = {sys.getsizeof(cb)}')
