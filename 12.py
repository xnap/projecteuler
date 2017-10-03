import math

def number_of_divs(n):
    cnt = 0
    for i in range(1, int(math.sqrt(n))):
        if n % i == 0:
            cnt += 1
            if i * i < n:
                cnt += 1
    return cnt

def generate():
    i = 1
    while True:
        yield i * (i + 1) / 2
        i += 1

for number in generate():
    if number_of_divs(number) > 500:
        print(number)
        break