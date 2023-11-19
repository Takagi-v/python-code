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

