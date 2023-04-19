def f(x, A):
    return (A < 50) and ((x % A != 0) <= ((x % 10 == 0) <= (x % 12 != 0)))

for A in range(256, 1, -1):
    flag = True
    for x in range(1, 256):
        if not(f(x, A)):
            flag = False
    if flag:
        print(A)
        break
