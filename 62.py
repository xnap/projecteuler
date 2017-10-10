def get_tuple(n):
    l = []
    while n > 0:
        l.append(n % 10)
        n //= 10
    return tuple(sorted(l))

m = {}
last_digit = 0
q = 1
while True:
    w = q*q*q
    r = get_tuple(w)
    found = False
    if last_digit != len(r):
        for key, value in m.items():
            if len(value) == 5:
                found = True
                print(key, value)
        m.clear()
        if found:
            break

    last_digit = len(r)

    if r in m:
        m[r].append(w)
    else:
        m[r] = [w]
    q += 1
