import math
a=3
b=4
c=3
p=(a+b+c)/2
t=p*(p-a)*(p-b)*(p-c)
print(math.sqrt(t))


x1=0.1
y1=0.1
x2=0.3
y2=0.3
x3=0.4
y3=0.5
a1=x2-x1
b1=y2-y1
a2=x3-x1
b2=y3-y1
s=abs((a1*b2-a2*b1)/2)
print(s)