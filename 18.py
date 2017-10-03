ls = []

for line in open('18.input'):
    cur = line.strip().split(" ")

    nl = []
    for index, v in enumerate(cur):
        # print(index, value)
        value = int(v)
        if len(ls) == 0:
            nl.append(value)
        elif index == 0:
            nl.append(value + ls[0])
        elif index == len(ls):
            nl.append(value + ls[index-1])
        else:
            nl.append(value + max(ls[index-1], ls[index]))
    ls = nl

print(max(ls))


