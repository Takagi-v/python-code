import math
a=1
b=2
c=-1
d=b**2-4*a*c
if d<0:
  print("无解")
elif d==0:
  print("x1=x2=",-b/a)
elif d>0:
  print("x1=",(-b+math.sqrt(d))/a)
  print("x2=",(-b-math.sqrt(d))/a)


a,b,c=1,1,1
m=(4*a-b**2)/4*a
if a>0:
  print("Max=",m)
a,b,c=-1,1,1
m=(4*a-b**2)/4*a
if a<0:
  print("Min=",m)
  