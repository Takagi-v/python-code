#1.	给定一个列表，含有若干个数字，这些数字可能有重复的。请设计一个函数能够删除列表中的重复数字，并且降序输出剩下的不重复数字。
def remove_dup(a):
    b = set(a)
    c = list(sorted(b))
    c.reverse()
    return c


a = [3, 2, 1, 4, 2, 3, 5]
print(remove_dup(a))

#2.	Write a function that accepts sequence of strings as input and prints the lines after making all characters in the sentence capitalized.
def upper_str(a):
    return a.upper()


s = "Hello world"
s1 = "Practice makes perfect"
print(upper_str(s))
print(upper_str(s1))

#3.	Given two sored list a, b, merge them into a new sorted list c.
def merge_list(a, b):
    c = a + b
    c.sort()
    return c


a = [1, 2, 3]
b = [-1, 2, 4]
print(merge_list(a, b))

#4.Write a Python program to count the number of even and odd numbers from a series of numbers.
def count_digit(a):
    evenx,oddx=0,0
    for i in a:
        if i % 2 == 0:
            evenx += 1
        else:
            oddx += 1
    return oddx, evenx


a = [123, 234, 345, 121, 232]
print(count_digit(a))

#5.	Write a Python function to check the validity of password input by users. 
def is_valid(s):
    a = [False] * 6
    a[5] = True
    for i in s:
        if i >= "a" and i <= "z":
            a[0] = True
        if i >= "A" and i <= "Z":
            a[1] = True
        if i >= "0" and i <= "9":
            a[2] = True
        if i == "$" or i == "#" or i == "@":
            a[3] = True
        if len(s) >= 6 and len(s) <= 16:
            a[4] = True
    for i in range(0, 5):
        if a[i] == False:
            a[5] = False
            break
    return a[5]


s = "Hh1234$"
s1 = "1234H$"
print(is_valid(s))
print(is_valid(s1))

#6.	Write a Python function to check whether an alphabet is a vowel or consonant.
def check_al(s):
    dt = {"a", "A", "e", "E", "i", "I", "o", "O", "u", "U"}
    return s in dt


a = "a"
b = "b"
print(check_al(a))
print(check_al(b))

#7.	Write a Python function to convert month name to a number of days.
def convert_mouth_to_days(a):
    dt = {
        "January": 31,
        "February": 28,
        "March": 31,
        "April": 30,
        "May": 31,
        "June": 30,
        "July": 31,
        "August": 30,
        "September": 31,
        "October": 30,
        "November": 31,
        "December": 30,
    }
    return dt[a]


a = "January"
print(convert_mouth_to_days(a))

#8.	Write a Python function to check a string represent an integer or not.
def check_num(a):
    if a[0] == "0" and len(a) > 1:
        return False
    for i in a:
        if i >= "9" or i <= "0":
            return False
    return True


a = "1234ser"
b = "1234"
print(check_num(a))
print(check_num(b))

#9.	Write a Python function that accepts two integers representing a month and day and prints the season for that month and day.
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

#10.	Write a Python function to display the sign of the Chinese Zodiac for given year in which you were born.
def zodiac(a):
    s = a % 12
    dt = {
        0: "猴",
        1: "鸡",
        2: "狗",
        3: "猪",
        4: "鼠",
        5: "牛",
        6: "虎",
        7: "兔",
        8: "龙",
        9: "蛇",
        10: "马",
        11: "羊",
    }
    return dt[s]


a = 2004
print(zodiac(a))

#11.	Write a Python function to get next day of a given date.
def check_run(y):
    if y % 4 == 0:
        if y % 400 == 0:
            return True
        if y % 100 == 0:
            return False
        return True


def the_next_day(y, m, d):
    if m == 12 and d == 31:
        return y + 1, 1, 1
    dt = {
        "1": 31,
        "2": 28,
        "3": 31,
        "4": 30,
        "5": 31,
        "6": 30,
        "7": 31,
        "8": 30,
        "9": 31,
        "10": 30,
        "11": 31,
        "12": 30,
    }
    if check_run(y) and m == 2 and d == 29:
        return y, 3, 1
    if d == dt[m]:
        return y, m + 1, 1
    return y, m, d + 1


y, m, d = 1212, 2, 29
print(the_next_day(y, m, d))
y, m, d = 2009, 12, 31
print(the_next_day(y, m, d))

#12.	For the following speech, please write a program to 1)	Remove all unnecessary “--” “.” “,”2)	Transform all the words into lowercase3)	Count the words appeared in the speech4)	Count the letters appeared in the speech
def format_doc(a):
    a = a.replace("--", "")
    a = a.replace(".", "")
    a = a.replace(",", "")
    dt = {}
    dt1 = {}
    lst = a.split()
    for i in lst:
        if i in dt:
            dt[i] += 1
        else:
            dt[i] = 1
    for i in a:
        if (i >= "a" and i <= "z") or (i >= "A" and i <= "Z"):
            if i in dt1:
                dt1[i] += 1
            else:
                dt1[i] = 1
    return dt, dt1, a


s = """   Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.

    Now we are engaged in a great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure. We are met on a great battle-field of that war. We have come to dedicate a portion of that field, as a final resting place for those who here gave their lives that that nation might live. It is altogether fitting and proper that we should do this.

    But, in a larger sense, we can not dedicate -- we can not consecrate -- we can not hallow -- this ground. The brave men, living and dead, who struggled here, have consecrated it, far above our poor power to add or detract. The world will little note, nor long remember what we say here, but it can never forget what they did here. It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so nobly advanced. It is rather for us to be here dedicated to the great task remaining before us -- that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion -- that we here highly resolve that these dead shall not have died in vain -- that this nation, under God, shall have a new birth of freedom -- and that government of the people, by the people, for the people, shall not perish from the earth.

    Abraham Lincoln
November 19, 1863

"""
dt, dt1, c = format_doc(s)
print(dt)
print(dt1)
