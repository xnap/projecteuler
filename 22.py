def gen():
    for line in open('p022_names.txt'):
        words = line.split(',')
        for w in sorted(words):
            yield w

def cal(s):
    sum = 0
    for c in s:
        if c >= 'A' and c <= 'Z':
            sum += ord(c) - 64
    return sum

pos = 1
sum = 0

for w in gen():
    sum += pos * cal(w)
    pos += 1
print(sum)
