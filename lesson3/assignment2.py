#1
a=input()
b=input()
c=input()
a=int(a)
b=int(b)
c=int(c)
print(a," ",b," ",c)
a=float(a)
b=float(b)
c=float(c)
print(a," ",b," ",c)
#2
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
#3
#输入表达式，用eval函数求出表达式的值并输出结果
s=input()
a=eval(s)
print(f"{s}={a}")
#4#输入a,b
a=int(input())
b=int(input())
#交换a,b的值
a,b=b,a
print(a-b)
#6
import math
def area(a,b,c):
  '''求三角形面积'''
  p=(a+b+c)/2
  t=p*(p-a)*(p-b)*(p-c)
  t=math.sqrt(t)
  print(t)
def angle(a,b,c):
  '''求三角弧度值'''
  cosC=(a**2+b**2-c**2)/(2*a*b)
  cosA=(b**2+c**2-a**2)/(2*c*b)
  cosB=(c**2+a**2-b**2)/(2*a*c)
  print(math.acos(cosA)," ",math.acos(cosB)," ",math.acos(cosC))
def circumcircle(a,b,c):
  '''求外接圆半径与面积'''
  cosC=(a**2+b**2-c**2)/(2*a*b)
  cosA=(b**2+c**2-a**2)/(2*c*b)
  cosB=(c**2+a**2-b**2)/(2*a*c)
  sinA=math.sqrt(1-cosA**2)
  r1=(a/sinA)/2
  s1=r1**2*math.pi
  print(r1)
  print(s1)
def incircle(a,b,c):
  '''求内切圆半径与面积'''
  p=(a+b+c)/2
  t=p*(p-a)*(p-b)*(p-c)
  t=math.sqrt(t)
  r2=(t*2)/(a+b+c)
  s2=r2**2*math.pi
  print(r2)
  print(s2)
a=float(input())
b=float(input())
c=float(input())
area(a,b,c)
angle(a,b,c)
circumcircle(a,b,c)
incircle(a,b,c)
#7
import math
def f(x1,y1,r1,   x2,y2,r2):
  dis=math.sqrt(abs(x1**2-x2**2))+math.sqrt(abs(y1**2-y2**2))
  r=abs(r1-r2)
  if r>dis:
    print("0")
    return
  if r==dis and r1!=r2:
    print("1")
    return
  if r==dis and r1==r2:
    print("infinite")
    return
  if r<dis and r1+r2>dis:
    print("2")
    return
  if r1+r2==dis:
    print("1")
    return
  if r1+r2<dis:
    print("0")
    return
x1=float(input())
y1=float(input())
r1=float(input())
x2=float(input())
y2=float(input())
r2=float(input())
f(x1,y1,r1,  x2,y2,r2)



