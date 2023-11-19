# 判断一个年份是不是回文年，譬如 2002， 1991， 1221都是回文
def is_palindrome_year(year):
    if year < 10:
        return True
    if year < 100:
        a = year % 10
        year //= 10
        b = year
        if a == b:
            return True
        return False
    if year < 1000:
        a = year % 10
        year //= 10
        year //= 10
        c = year
        if a == c:
            return True
        else:
            return False
    a = year % 10
    year //= 10
    b = year % 10
    year //= 10
    c = year % 10
    year //= 10
    d = year
    if a == d and b == c:
        return True
    else:
        return False


n = int(input())
print(is_palindrome_year(n))
