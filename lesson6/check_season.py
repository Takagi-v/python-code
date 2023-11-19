def check_season(a, b):
    if a >= 2 and a <= 5:
        if a == 2 and b > 5:
            return "Spring"
        if a == 5 and b <= 6:
            return "Spring"
    if a >= 5 and a <= 8:
        if a == 5 and b > 6:
            return "Summer"
        if a == 8 and b <= 8:
            return "Summer"
    if a >= 8 and a <= 11:
        if a == 8 and b > 8:
            return "Autumn"
        if a == 11 and b <= 9:
            return "Autumn"
    if a >= 11 or a <= 2:
        if a == 11 and b > 9:
            return "Winter"
        if a == 2 and b <= 5:
            return "Winter"


a, b = 11, 5
print(check_season(a, b))
