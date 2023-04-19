def f(n):
    lst = [int(x) for x in str(n) if int(x) % 2]
    if len(lst) == 4:
        sum1 = lst[0] + lst[1]
        sum2 = lst[2] + lst[3]
        string = str(min(sum1, sum2)) + str(max(sum2, sum1))
        return int(string)

lst = []
for n in range(1001, 10000):
    if f(n) == 616:
        lst.append(n)

print(len(lst))