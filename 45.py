import math

def hexagonal(n):
    return n * (2 * n - 1)

def is_triangle(n):
    t = 1 + 8 * n
    q = int(math.sqrt(1 + t))
    if q * q == t or q * q + 2 * q + 1 == t:
        return True
    else:
        return False

def is_pentagonal(n):
    t = 1 + 24 * n
    q = int(math.sqrt(1 + t))
    if q * q == t and (q + 1)%6 == 0:
        return True
    elif q * q + 2 * q + 1 == t and (q + 2) % 6 == 0:
        return True
    else:
        return False

n = 144
while True:
    q = hexagonal(n)
    if is_pentagonal(q) and is_triangle(q):
        print(q)
        break
    n += 1
