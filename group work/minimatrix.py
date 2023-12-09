# Framework for IEEE course final project
# Fan Cheng, 2022

import random
import numpy as np

class Matrix:
    def __init__(self, data=None, dim=None, init_value=0):
        if data != None:
            self.data = data
            self.dim = (len(data), len(data[0]))
        elif dim != None:
            self.data = [[init_value] * dim[1] for i in range(dim[0])]
            self.dim = dim
        else:
            raise ValueError("Both data and dim cannot be None.")

    def shape(self):
        return self.dim

    def reshape(self, newdim):
        pass

    def dot(self, other):
        pass

    def T(self):
        copyy=(self.data).copy()
        newmat=Matrix(dim=(self.dim[1],self.dim[0]))
        for i in range(self.dim[1]):
            for j in range(self.dim[0]):
                newmat.data[i][j]=copyy[j][i]
        return newmat
    def sum(self, axis=None):
        pass

    def copy(self):
        pass

    def Kronecker_product(self, other):
        pass

    def __getitem__(self, key):
        pass

    def __setitem__(self, key, value):
        pass

    def __pow__(self, n):
        pass

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __len__(self):
        return self.dim[0] * self.dim[1]

    def __str__(self):
        result = "["
        result += "[" + " ".join(f"{x:3}" for x in self.data[0]) + "]"
        for row in self.data[1::]:
            result += "\n [" + " ".join(f"{x:3}" for x in row) + "]"
        result += "]"
        return result

    def det(self):
        if self.dim[0]!=self.dim[1]:
            raise ValueError("This matrice can not calculate determinant")
        matrix_copy=[row[:] for row in self.data]
        n=self.dim[0]
        result=1
        for i in range(n):
            pivot=matrix_copy[i][i]
            if pivot==0:
                for j in range(i+1,n):
                    if matrix_copy[j][i]!=0:
                        pivot=matrix_copy[j][i]
                        matrix_copy[i],matrix_copy[j]=matrix_copy[j],matrix_copy[i]
                        result*=-1
                        break
                else:
                    return 0
            for j in range(i+1,n):
                mul=matrix_copy[j][i]/pivot
                matrix_copy[j][i]=0
                for k in range(i,n):
                    matrix_copy[j][k]-=mul*matrix_copy[i][k]
        for i in range(n):
            result*=matrix_copy[i][i]
        return result

    def inverse(self):
        if self.dim[0]!=self.dim[1]:
            raise ValueError("This matrice doesn't have an inversed matrice")
        if self.det()==0:
            raise ValueError("This matrice is singular")
        matrix_copy=self.data
        imatrix_copy=I(self.dim[0]).data
        n=self.dim[0]
        for i in range(n):
            pivot=matrix_copy[i][i]
            if pivot==0:
                for j in range(i+1,n):
                    if matrix_copy[j][i]!=0:
                        pivot=matrix_copy[j][i]
                        matrix_copy[i],matrix_copy[j]=matrix_copy[j],matrix_copy[i]
                        imatrix_copy[i],imatrix_copy[j]=imatrix_copy[j],imatrix_copy[i]
                        break
            for j in range(n):
                matrix_copy[i][j]/=pivot
                imatrix_copy[i][j]/=pivot
            for j in range(n):
                if j!=i:
                    mul=matrix_copy[j][i]
                    for k in range(n):
                        matrix_copy[j][k]-=mul*matrix_copy[i][k]
                        imatrix_copy[j][k]-=mul*imatrix_copy[i][k]
        return Matrix(data=imatrix_copy)
                
        


    def rank(self):
        x=self.dim[0]
        y=self.dim[1]
        matrix_copy=[row[:] for row in self.data]
        if x<y:
            temp=self.T()
            matrix_copy=[row[:] for row in temp.data]
            y,x=x,y
        rankk=0
        for i in range(min(x,y)):
            pivot =matrix_copy[i][i]
            if pivot==0:
                for j in range(i+1,x):
                    if matrix_copy[j][i]!=0:
                        pivot=matrix_copy[j][i]
                        matrix_copy[i],matrix_copy[j]=matrix_copy[j],matrix_copy[i]
                        break
                else:
                    continue
            for j in range(i+1,x):
                mul=matrix_copy[j][i]/pivot
                matrix_copy[j][i]=0
                for k in range(i,y):
                    matrix_copy[j][k]-=mul*matrix_copy[i][k]
            rankk+=1
        return rankk
                    
                


def I(n):
    result=[]
    for i in range(n):
        temp=[0]*n
        temp[i]=1
        result.append(temp)
    m=Matrix(data=result)
    return m


def narray(dim, init_value=1):
    return Matrix(dim=dim,init_value=init_value)


def arange(start, end, step):
    result=[]
    temp=[]
    for i in range(start,end,step):
        temp.append(i)
    result.append(temp)
    return Matrix(data=result)


def zeros(dim):
    return Matrix(dim=dim,init_value=0)


def zeros_like(matrix):
    return Matrix(dim=matrix.dim)


def ones(dim):
    return Matrix(dim=dim,init_value=1)


def ones_like(matrix):
    return Matrix(dim=matrix.dim,init_value=1)


def nrandom(dim):
    result=[]
    for i in range(dim[0]):
        temp=[]
        for i in range(dim[1]):
            temp.append(random.random())
        result.append(temp)
    return Matrix(data=result)


def nrandom_like(matrix):
    return nrandom(matrix.dim)


def concatenate(items, axis=0):
    if axis==0:
        for item in items[1::]:
            if item.dim[1]!=items[0].dim[1]:
                raise ValueError("Matrices do not have the same number of columns.")
        concatenated_data=[row[:] for row in items[0].data]
        for item in items[1::]:
            concatenated_data.extend(item.data)
        return Matrix(data=concatenated_data)
    if axis==1:
        for item in items[1::]:
            if item.dim[0]!=items[0].dim[0]:
                raise ValueError("Matrices do not have the same number of rows")
        concatenated_data=[items[0].data[i][:] for i in range(items[0].dim[0])]
        for item in items[1::]:
            for i in range(item.dim[0]):
                concatenated_data[i].extend(item.data[i])    
        return Matrix(data=concatenated_data)

def vectorize(func):
    def wrapper(matrix):
        result=[]
        for row in matrix.data:
            temp=[]
            for elem in row:
                temp.append(func(elem))
            result.append(temp)
        return Matrix(data=result)
    return wrapper


if __name__ == "__main__":
    print("test here")
    x=Matrix(data=[[1,2,3],[2,3,545]])
    print(x)
    pass
