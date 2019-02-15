def add_days(n_days, day=0, month=0, year=0):
    thirty_days = {9, 4, 6, 11}
    leap_year = year % 4 == 0

    if n_days + day <= 30 and month != 2:
        return n_days + day, month, year
    elif month not in thirty_days and n_days + day <= 31 and month != 2:
        return n_days + day, month, year
    elif month == 2 and leap_year and n_days + day <= 29:
        return n_days + day, month, year
    elif month in thirty_days:
        month = month + 1 if month != 12 else 1
        year = year if month != 1 else year + 1
        return n_days + day - 30, month, year
    elif month != 2:
        month = month + 1 if month != 12 else 1
        year = year if month != 1 else year + 1
        return n_days + day - 31, month, year
    elif leap_year:
        month = month + 1 if month != 12 else 1
        year = year if month != 1 else year + 1
        return n_days + day - 29, month, year
    else:
        month = month + 1 if month != 12 else 1
        year = year if month != 1 else year + 1
        return n_days + day - 28, month, year

def compute():
    # 6 Jan 1901 is a Sunday
    day = 6
    month = 1
    year = 1901
    
    count = 0
    while year != 2001:
        day, month, year = add_days(7, day=day, month=month, year=year)
        count = count + 1 if day == 1 else count

    return count

# slightly easier
def compute_probabilistic():
    return 100 * 12 // 7

if __name__ == '__main__':
    print(compute())
    print(compute_probabilistic())