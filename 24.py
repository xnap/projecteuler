def next_perm(str):
    l = len(str)
    for k in range(l-1, -1, -1):
        if str[k] > str[k-1]:
            for z in range(l-1, k-1, -1):
                if str[z] > str[k-1]:
                    tmp = str[k-1]
                    str[k-1] = str[z]
                    str[z] = tmp
                    str[k:] = sorted(str[k:])
                    return

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# a = [0, 1, 2]
i = 1

while i < 1000000:
    next_perm(a)
    # print(i, ''.join(map(str, a)))
    i += 1

print(''.join(map(str, a)))