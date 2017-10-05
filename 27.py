def is_prime(n):
    if n <= 1:
        return False
    else:
        i = 2
        while True:
            if i * i > n:
                return True
            elif n % i == 0:
                return False
            else:
                i += 1

def count(a, b):
    n = 0
    while True:
        if not is_prime(n * n + a * n + b):
            return n
        n += 1

# print(count(-79, 1601))
win = (0, 0, 0)
for a in range(-999, 1000):
    for b in range(-1000, 1001):
        num = count(a, b)
        if num > win[0]:
            win = (num, a, b)

print(win[1] * win[2])