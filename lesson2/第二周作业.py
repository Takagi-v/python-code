#1(a)
print("      (()__(()")
print("      /       \\ ")
print("     ( /    \\  \\ ")
print("      \\ o o    /")
print("      (_()_)__/ \\")
print("     / _,==.____  \\")
print("    (   |--|      )")
print("    /\\_.|__|'-.__/\\_")
print("   / (        /     \\")
print("   \\  \\      (      /")
print("    )  '._____)    /")
print(" (((____.--(((____/")
#1(b)
print("    ......       ............  .............  ...        ...   ")
print("  ...    ...     ............  .............  ...        ...   ")
print("   ...               ...            ...       ...        ...   ")
print("     ...             ...            ...       ...        ...   ")
print("       ...           ...            ...       ...        ...   ")
print("         ...         ...            ...       ...        ...   ")
print("  ...     ...       ...             ...        ............    ")
print("     .....         ...              ...          ........      ")
#1(c)
print("*       ")
print("    *   ")
print(" *      ")
print("     *  ")
print("  *     ")
print("      * ")
print("   *    ")
print("       *")
#1(d)
print("""                          忆江南
                   作者：白居易 年代：唐
江南好，风景旧曾谙。日出江花红胜火，春来江水绿如蓝。能不忆江南？
江南忆，最忆是杭州。山寺月中寻桂子，郡亭枕上看潮头。何日更重游？
江南忆，其次忆吴宫。吴酒一杯春竹叶，吴娃双舞醉芙蓉。早晚复相逢？""")
#3
import math
a=3
b=4
c=3
p=(a+b+c)/2
t=p*(p-a)*(p-b)*(p-c)
print(math.sqrt(t))
#4
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
S=abs((a1*b2-a2*b1)/2)
print("%.2f"% S)
#5
a=1
b=2
c=-1
d=b**2-4*a*c
if d<0:
  print("无解")
elif d==0:
  print("x1=x2=",-b/2*a)
elif d>0:
  print((-b+math.sqrt(d))/2*a,(-b-math.sqrt(d))/2*a)
#6
a,b,c=1,1,1
m1=(4*a-b**2)/4*a
a,b,c=-1,1,1
m2=(4*a-b**2)/4*a
print(m1,m2)
  