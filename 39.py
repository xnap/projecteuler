# a+b+c = 120
# a^2 + b^ = c^2

def count(p):
    cnt = 0
    for a in range(1, p//3):
        for b in range(a, (p-a)//2):
            c = p - a - b
            if a * a + b * b == c * c:
                # print(a, b, c)
                cnt += 1
    return cnt

# print(count(840))
max = 0
val = 0
for p in range(1, 1001):
    t = count(p)
    if t > max:
        val = p
        max = t
print(max)
print(val)

