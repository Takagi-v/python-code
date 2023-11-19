# 	Write a program to read a series of numbers from the console, such that if the input number x:
def f():
    x = int(input())
    while x != 0:
        if x == -1:
            x = int(input())
            continue
        while x != 0:
            print(x % 10, end="")
            x //= 10
        x = int(input())
    return


f()
