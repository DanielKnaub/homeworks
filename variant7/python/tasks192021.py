def f1(s, m):
    if s >= 56:
        return m%2==0
    if m==0:
        return 0
    h = [f1(s+1, m-1), f1(s+2, m-1), f1(s*2, m-1)]
    return any(h) if (m-1)%2==0 else any(h)


def f(s, m):
    if s >= 56:
        return m%2==0
    if m==0:
        return 0
    h = [f(s+1, m-1), f(s+2, m-1), f(s*2, m-1)]
    return any(h) if (m-1)%2==0 else all(h)

print([s for s in range(1, 56) if f1(s, 2) and not f1(s, 1)][0])
print('==================')
print([s for s in range(1, 56) if f(s, 3) and not f(s, 1)])
print('==================')
print([s for s in range(1, 56) if f(s, 4) and not f(s, 2)])
