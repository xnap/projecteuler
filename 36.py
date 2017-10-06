def is_pan(s):
    # print(s)
    l = len(s)
    for i in range(l//2):
        if s[i] != s[l-1-i]:
            return False
    return True

sum = 0
for i in range(1, 1000000):
    if is_pan(str(i)) and is_pan('{0:b}'.format(i)):
        sum += i
        # print(i, '{0:b}'.format(i))
print(sum)
