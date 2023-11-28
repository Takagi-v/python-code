def add(str1, str2):
    num1 = [int(digit) for digit in str1[::-1]]
    num2 = [int(digit) for digit in str2[::-1]]
    num = []
    x = 0
    while len(num1) < len(num2):
        num1.append(0)
    while len(num2) < len(num1):
        num2.append(0)
    for i in range(len(num1)):
        num.append((num1[i] + num2[i] + x) % 10)
        x = (num1[i] + num2[i]) // 10
    if x == 1:
        num.append(1)
    num = num[::-1]
    s = ""
    for i in num:
        s += str(i)
    return s


c = add("22222222222222", "8773849905050505")
print(c)
