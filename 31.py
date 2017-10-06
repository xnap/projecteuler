# 200 = a * 100 + b * 50 + c * 20 + d * 10 + e * 5 + f * 2 + g

def count(money, level):
    if level == 1:
        return 1
    elif level == 2:
        possible = money // 2
        sum = 0
        for i in range(0, possible + 1):
            sum += count(money - i * 2, 1)
        return sum
    elif level == 5:
        possible = money // 5
        sum = 0
        for i in range(0, possible + 1):
            sum += count(money - i * 5, 2)
        return sum
    elif level == 10:
        possible = money // 10
        sum = 0
        for i in range(0, possible + 1):
            sum += count(money - i * 10, 5)
        return sum
    elif level == 20:
        possible = money // 20
        sum = 0
        for i in range(0, possible + 1):
            sum += count(money - i * 20, 10)
        return sum
    elif level == 50:
        possible = money // 50
        sum = 0
        for i in range(0, possible + 1):
            sum += count(money - i * 50, 20)
        return sum
    elif level == 100:
        possible = money // 100
        sum = 0
        for i in range(0, possible + 1):
            sum += count(money - i * 100, 50)
        return sum
    elif level == 200:
        possible = money // 200
        sum = 0
        for i in range(0, possible + 1):
            sum += count(money - i * 200, 100)
        return sum

print(count(200, 200))

