def transform(n):
    return n / 2 if n % 2 == 0 else 3 * n + 1

map = {1:0}
def chain_length(n):
    if n in map:
        return map[n]
    else:
        t = chain_length(transform(n)) + 1
        map[n] = t
        return t

max = 1

for i in range(1, 1000000):
    w = chain_length(i)
    if map[max] < map[i]:
        max = i
print(max)
