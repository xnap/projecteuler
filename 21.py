import math

def sum_of_div(n):
    sum = 0
    for i in range(1, int(math.sqrt(n))):
        if n % i == 0:
            if n > i:
                sum += i
            if n > n//i:
                sum += n//i
    return sum

sum = 0
for i in range(1, 10000):
    t = sum_of_div(i)
    if t > i and t < 10000:
        if i == sum_of_div(t):
            sum += t + i
print(sum)

