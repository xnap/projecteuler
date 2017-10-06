# 9! = 362880
# 7 * 9!= 2540160
# so the upper bound is 2540160
import math

def curious_number(n):
    sum = 0
    r = n
    while n > 0:
        sum += math.factorial(n%10)
        n //= 10
    return sum == r

sum = 0
for i in range(10, 2540160):
    if curious_number(i):
        print(i)
        sum += i
print(sum)