import math
a=float(input())
b=float(input())
c=float(input())
#求三角形面积
p=(a+b+c)/2
t=p*(p-a)*(p-b)*(p-c)
t=math.sqrt(t)
print(t)
#求三角弧度值
cosC=(a**2+b**2-c**2)/(2*a*b)
cosA=(b**2+c**2-a**2)/(2*c*b)
cosB=(c**2+a**2-b**2)/(2*a*c)
print(math.acos(cosA)," ",math.acos(cosB)," ",math.acos(cosC))
#求外接圆半径与面积
sinA=math.sqrt(1-cosA**2)
r1=(a/sinA)/2
s1=r1**2*math.pi
print(r1)
print(s1)
#求内切圆半径与面积
r2=(t*2)/(a+b+c)
s2=r2**2*math.pi
print(r2)
print(s2)

