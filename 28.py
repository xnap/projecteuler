# 1    = 1
# 3, 5, 7, 9 = 12 * 2 = 6 * 4   k = 2
# 13, 17, 21, 25 = 38 * 2 = 19 * 4 k = 3
# 31, 37, 43, 49 = 80 * 2 = 40 * 4 k = 4


# (2k - 3)^2 + 2 * (k-1) 
# (2k - 1)^2 = 4k^2 - 4k + 1

def sum_level(k):
    if k == 1:
        return 1
    else:
        return ((2 * k-3) * (2*k-3) +  2*(k-1) + (2*k-1)*(2*k-1)) * 2

sum = 0
for i in range(1, 1001//2 + 2):
    sum += sum_level(i)
print(sum)


