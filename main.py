# Test immutable objects behaviour
a = 1
b = a
a += a
print('a:', a)
print('b:', b)

# Test mutable objects behaviour
a = [1]
b = a
a += a
print('a:', a)
print('b:', b)
