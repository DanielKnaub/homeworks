import itertools

def f(s):
    while '00' not in s:
        s = s.replace('01', '210', 1)
        s = s.replace('02', '320', 1)
        s = s.replace('03', '3012', 1)
    return s

for i in range(1, 256):
    flag = False
    for s in itertools.combinations_with_replacement('123', i):
        x = '0' + ''.join(s) + '0'
        string = f(x)
        if string.count('1') == 26 and string.count('2') == 54 and string.count('3') == 48:
            flag = len(x)
    if flag:
        print(flag)
        break
