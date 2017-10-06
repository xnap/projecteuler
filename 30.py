# 9^5 = 59049
# 1 * 9^5 = 59049
# 2 * 9^5 = 118098
# 3 * 9^5 = 177147
# 4 * 9^5 = 236196
# 5 * 9^5 = 295245
# 6 * 9^5 = 354294
# 7 * 9^5 = 413343

# set the upper bound on 354294

def digit_5(n):
    sum = 0
    while n > 0:
        sum += pow(n%10, 5)
        n //= 10
    return sum

sum = 0
for i in range(2,354295):
    if i == digit_5(i):
        sum += i
        # print(i)
print(sum)