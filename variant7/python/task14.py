x = 25 ** 5 + 5 ** 14 - 5

s = ''
while x > 0:
    s = str(x%5) + s
    x //= 5

print(s.count('4'))