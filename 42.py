val = []
for i in open('p042_words.txt'):
    s = i.split(',')
    for ss in s:
        sum = 0
        for l in ss:
            if ord(l) > 64 and ord(l) < 91:
                sum += ord(l) - 64
        val.append(sum)

min = min(val)
max = max(val)

s = set()

w = 1
while w * (w +1) // 2 <= max:
    s.add(w * (w + 1)//2)
    w += 1
# print(sorted(s))

cnt = 0
for q in val:
    if q in s:
        cnt += 1
print(cnt)