s = set()

for i in range(2,101):
    for j in range(2,101):
        s.add(pow(i,j))

print(len(s))