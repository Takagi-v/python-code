# Test code for IEEE course final project
# Fan Cheng, 2024

import minimatrix as mm

#Test your code here!
# The following code is only for your reference
# Please write the test code yourself

a = mm.narray([4, 5])
b=mm.ones([2,4])
c=mm.ones_like(a)
d=mm.nrandom([4,2])
e=mm.nrandom_like(d)
@mm.vectorize
def f(x):
  return x+2
print(f(b))

# print(a)
# print(a.shape())
# print(a.reshape([2, 6]))

# ma1 = mm.Matrix(2,3)
# ma2 = mm.Matrix(3,4)

# print(ma1 * ma2)



