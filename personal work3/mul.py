def strtolist(s):
    sign=1
    if s[0]=='-':
        sign=-1
        s=s[1:]
    lst=[int(digit) for digit in s[::-1]]
    return sign,lst
def listtostr(sign,lst):
    s=''.join(map(str,lst))
    return s if sign==1 else '-'+s
def mul_list(lst1, lst2):
    num1 = lst1
    num2 = lst2
    num = [0] * (len(num1) + len(num2))
    for i in range(len(num1)):
        carry = 0
        for j in range(len(num2)):
            temp = num1[i] * num2[j] + num[i + j] + carry
            num[i + j] = temp % 10
            carry = temp // 10
        num[i + len(num2)] += carry
    while len(num) > 0 and num[-1] == 0:
        num.pop()
    return num[::-1]

def mul(str1,str2):
    sign1,lst1=strtolist(str1)
    sign2,lst2=strtolist(str2)
    ans=mul_list(lst1,lst2)
    return listtostr(1,ans) if sign1==sign2 else listtostr(-1,ans)
print(mul('-1234565','456'))