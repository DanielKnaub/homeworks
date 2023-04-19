x = 149

s = ''
while x > 0:
	s = str(x%4) + s
	x //= 4
print(s)
