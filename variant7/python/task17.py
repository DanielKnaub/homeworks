with open('17.txt') as f:
    s = [int(i) for i in f]
    sum_list = []
    counter = 0
    for i in range(len(s)-1):
        for j in range(i+1, len(s)):
            if s[j] * s[i] % 34 != 0:
                counter += 1
                sum_list.append(s[i]+s[j])

print(counter, max(sum_list))