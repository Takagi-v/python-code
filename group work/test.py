def est(g):
  def wrapper(a):
    a[0]=g(a[0])
    a[1]=g(a[1])
    return a
  return wrapper
@est
def f(x):
  return x**2
@est
def my_abs(x):
  if x>=0:return x
  else: return -x
b=[1,-2]
print(my_abs(b))