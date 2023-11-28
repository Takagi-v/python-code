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
def merge1(lst):
    s=''
    for i in lst:
        s+=str(i)
    return s
def clear1(lst):
    while len(lst)>1 and lst[0]==0:
        lst.pop(0)
    return lst
def div(str1, str2):
    num1 = [int(digit) for digit in str1]
    num2 = [int(digit) for digit in str2]
    quotient = []
    remainder = num1.copy()
    if int(sub(merge1(num1[0:len(num2)]),merge1(num2)))>0:
        t=len(num1)-len(num2)+1
    else: t=len(num1)-len(num2)
    for i in range(t):
        divisor=num2
        temp=int(sub(merge1(remainder),merge1(divisor)))
        while temp>0:
            divisor+=[0]
            temp=int(sub(merge1(remainder),merge1(divisor)))
        divisor.pop()
        q=0
        flag=int(sub(merge1(remainder),mul(str(q),merge1(divisor))))
        l=0
        while flag>0:
          q+=1
          if int(mul(str(q),merge1(divisor)))==int(merge1(remainder)):
              l=1
              break
          flag=int(sub(merge1(remainder),mul(str(q),merge1(divisor))))
        if l==1:
            quotient.append(q)
            remainder='0'
            break
        temp=mul(str(q-1),merge1(divisor))
        print(remainder,temp)
        remainder=sub(merge1(remainder),temp)
        quotient.append(q-1)
    return merge1(quotient),remainder
a='8773849905050505'
b='123'
print(div(a,b))
        
   