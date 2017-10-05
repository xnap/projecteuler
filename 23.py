import math
def is_abundant(n):
    sum = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            sum += i
            if i > 1 and i * i < n:
                sum += n//i
        i += 1
    return n > 1 and sum > n

abundants = []
for i in range(1, 28124):
    if is_abundant(i):
        abundants.append(i)

candidates = set()
for i in range(1, 28124):
    candidates.add(i)

for i in abundants:
    for j in abundants:
        if i + j in candidates:
            candidates.remove(i + j)

sum = 0
for i in candidates:
    sum += i

print(sum)
