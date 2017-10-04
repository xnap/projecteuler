def get_week_of_day():
    week_of_day = 1
    for year in range(1900, 2001):
        for month in range(1, 13):
            yield (year, month, week_of_day)
            if month in (1, 3, 5, 7, 8, 10, 12):
                month += 1
                week_of_day += 31
            elif month in (4, 6, 9, 11):
                month += 1
                week_of_day += 30
            elif year % 400 == 0:
                month += 1
                week_of_day += 29
            elif year % 100 != 0 and year % 4 == 0:
                month += 1
                week_of_day += 29
            else:
                month += 1
                week_of_day += 28
            if (month == 13):
                month = 1
                year += 1
            week_of_day %= 7

sum = 0
for year, month, week_of_day in get_week_of_day():
    # print (year, month, week_of_day)
    if year < 1901:
        pass
    elif week_of_day == 0:
        sum += 1
print(sum)

