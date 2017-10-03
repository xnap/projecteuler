# one two three four five six seven eight nine ten 
# eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen 
# twenty thirty forty fifty sixty seventy eighty ninety
# hundred

under_20 = (0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8)
tys = (0, 0, 6, 6, 5, 5, 5, 7, 6, 6)
def cal(n):
    if n == 0:
        return 0
    if n < 20:
        return under_20[n]
    if n == 1000:
        return 11
    elif n >= 100:
        t = int(n / 100)
        w = cal(n % 100)
        if w == 0:
            return under_20[t] + 7
        else:
            return under_20[t] + 10 + w
    else:
        t = int(n / 10)
        return tys[t] + cal(n % 10)

sum = 0
for i in range(1, 1001):
    sum += cal(i)

print(sum)
