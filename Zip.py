# The sip() function is used to combine multiple iterable like (tuple , list)
# into single iterable of tuples

a = [1,2,3,4]
b = [5,6,7,8]

print(list(zip(a,b)))