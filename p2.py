
a='abcd'
b='xyz'

c = ''.join(map(''.join, zip(a, b)))

print(c)