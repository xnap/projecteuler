# 9 * 999 = 8991, so not possible 1 * 3
# 9 * 9999 = 89991, so possible 1 * 4 = 5
# 99 * 99 = 9801, so not possible 2 * 2
# 10 * 100 = 1000, so possible 2 * 3 = 4
# 100 * 100 = 10000, so not possible 3 * 3

def pandigital(i, j, k):
    s = set()
    for w in (i, j, k):
        while w > 0:
            q = w % 10
            if q == 0 or q in s:
                return False
            s.add(q)
            w //= 10
    return len(s) == 9

sum = 0
d = set()
for i in range(1, 10):
    for j in range(1000, 10000):
        k = i * j
        if pandigital(i, j, k):
            print(i, j, k)
            if not k in d:
                sum += k
                d.add(k)

for i in range(10, 100):
    for j in range(100, 1000):
        k = i * j
        if pandigital(i, j, k):
            print(i, j, k)
            if not k in d:
                sum += k
                d.add(k)

print(sum)

# print(pandigital(39, 186, 7254))