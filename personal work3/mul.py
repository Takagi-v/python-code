def mul(str1, str2):
    num1 = [int(digit) for digit in str1[::-1]]
    num2 = [int(digit) for digit in str2[::-1]]
    result = [0] * (len(num1) + len(num2))
    for i in range(len(num1)):
        x = 0
        for j in range(len(num2)):
            temp = num1[i] * num2[j] + result[i + j] + x
            result[i + j] = temp % 10
            x = temp // 10
        result[i + len(num2)] += x
    while len(result) > 0 and result[-1] == 0:
        result.pop()
    s = ""
    for i in result[::-1]:
        s += str(i)
    return s


a = "1234567"
b = "123"

