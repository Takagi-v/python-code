def sub(str1, str2):
    num1 = [int(digit) for digit in str1[::-1]]
    num2 = [int(digit) for digit in str2[::-1]]
    num = []
    flag = 0
    if len(num1) < len(num2):
        flag = 1
        num1,num2=num2,num1
    if len(num1)==len(num2):
        k=len(num1)-1
        while num1[k]==num2[k]:
            k-=1
        if num1[k]<num2[k]:
            flag=1
            num1,num2=num2,num1
    x = 0
    while len(num1) < len(num2):
        num1.append(0)
    while len(num2) < len(num1):
        num2.append(0)
    for i in range(len(num1)):
        dif = num1[i] - num2[i] - x
        if dif < 0:
            x = 1
            dif += 10
        else:
            x = 0
        num.append(dif)
    while len(num) > 1 and num[-1] == 0:
        num.pop()
    num = num[::-1]
    s = ""
    for i in num:
        s += str(i)
    return s if flag == 0 else "-" + s


a = "12300"
b = "11700"
print(int(sub(a, b)))
