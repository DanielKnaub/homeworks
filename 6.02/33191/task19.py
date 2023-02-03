def f(x, y, h):
    if h == 3 and x+y >= 91:
        return 1
    elif h == 3 and x+y < 91:
        return 0
    elif x+y >= 91 and h < 3:
        return 0
    else:
        if h % 2 == 0:
            return f(x+1, y, h+1) or f(x, y+1, h+1) or f(x*4, y, h+1) or f(x, y*4, h+1)
        else:
            return f(x+1, y, h+1) or f(x, y+1, h+1) or f(x*4, y, h+1) or f(x, y*4, h+1)

for x in range(1, 86):
    if f(x, 5, 1):
        print(x)
        break