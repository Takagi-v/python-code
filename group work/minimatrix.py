# Framework for IEEE course final project
# Fan Cheng, 2022
import random

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

        if newdim[0] * newdim[1] != self.dim[0] * self.dim[1]:
            raise ValueError("Newdim is not suitable for this matrix")
        
        ele = []
        for i in range(self.dim[0]):
            for j in range(self.dim[1]):
                ele.append(self.data[i][j])

        k = 0
        newdata = []
        for i_ in range(newdim[0]):

            newele = []
            for j_ in range(newdim[1]):
                newele.append(ele[k])
                k += 1
            newdata.append(newele)

        return Matrix(data=newdata)
       
    
    def dot(self, other):

        if self.dim[1] != other.dim[0]:
            raise Exception("DimError: the col of self isn't equal the row of other")
        
        result = Matrix(dim=(self.dim[0],other.dim[1]))

        for i in range(self.dim[0]):

            for j in range(other.dim[1]):

                number = 0
                for k in range(other.dim[0]):
                    number += self.data[i][k] * other.data[k][j]
                
                result.data[i][j] = number

        return result
    
    
    def T(self):
        copy = (self.data).copy()
        newMat = Matrix(dim = (self.dim[1],self.dim[0]))

        for i in range(self.dim[1]):
            
            for j in range(self.dim[0]):
                 newMat.data[i][j] = copy[j][i]

        return newMat
    
  
    
    def sum(self, axis=None):
        if axis == 0:

            newMat = []
            for i  in range(self.dim[1]):

                num = 0
                for j  in range(self.dim[0]):
                    num += self.data[j][i]

                newMat.append(num)

            return Matrix(data=[newMat])

        if axis == 1:

            newMat = []
            for i in range(self.dim[0]):

                num = 0
                for j in range(self.dim[1]):
                    num += self.data[i][j]

                newMat.append([num])

            return Matrix(data=newMat)

        if axis == None:

            num = 0
            for i in range(self.dim[0]):
                for j in range(self.dim[1]):
                    num += self.data[i][j]

            return Matrix(data=[[num]])
        
        
    def copy(self):
        import copy
        matrix_copy=[copy.deepcopy(row) for row in self.data]
        copy_ = Matrix(data=matrix_copy)
        return copy_
    
    
    
    def Kronecker_product(self, other):

        result = []
        for row1 in self.data:

            for row2 in other.data:

                temp_row = []
                for ele1 in row1:
                    temp_row.extend(ele1 * ele2 for ele2 in row2)

                result.append(temp_row)

        newMat = Matrix(data=result)
        return newMat
    
    
    
    def __getitem__(self, key):

        if isinstance(key[1],slice):

            row_start = key[0].start
            row_stop = key[0].stop
            col_start = key[1].start
            col_stop = key[1].stop

            if row_start == None:
                row_start = 0
            if col_start == None:
                col_start = 0
            if row_stop == None:
                row_stop = self.dim[0]
            if col_stop == None:
                col_stop = self.dim[1]
            

            result = []
            for i in range(row_start,row_stop):

                temp_row = []
                for j in range(col_start,col_stop):
                    temp_row.append(self.data[i][j])

                result.append(temp_row)
            
            return Matrix(data=result)
        
        else:
            return self.data[key[0]][key[1]]
        
        
    
    def __setitem__(self, key, value):

        if isinstance(key[1],slice):

            row_start = key[0].start
            row_stop = key[0].stop
            col_start = key[1].start
            col_stop = key[1].stop

            if row_start == None:
                row_start = 0
            if col_start == None:
                col_start = 0
            if row_stop == None:
                row_stop = self.dim[0]
            if col_stop == None:
                col_stop = self.dim[1]

            for i in range(row_start,row_stop):
                for j in range(col_start,col_stop):
                    self.data[i][j] = value.data[i-row_start][j-col_start]

        else:
            self.data[key[0]][key[1]] = value
            
            
    
    def __pow__(self, n):
        if self.dim[0] != self.dim[1]:
            raise ValueError("The matrix is not square ")
            
        result = Matrix(data=self.data)
    
        for i in range(n-1):
            result = result.dot(self)
                
        return result
    
    
    def __add__(self, other):
        if self.dim[0] != other.dim[0] or self.dim[1] != other.dim[1]:
            raise ValueError("The two matrix have different dim")
        
        newMat = Matrix(dim=(self.dim[0],self.dim[1]))
        for i in range(self.dim[0]):
            for j in range(self.dim[1]):
                newMat.data[i][j] = self.data[i][j] + other.data[i][j]
                
        return newMat


    def __sub__(self, other):        
        if self.dim[0] != other.dim[0] or self.dim[1] != other.dim[1]:
            raise ValueError("The two matrix have different dim")
        
        newMat = Matrix(dim=(self.dim[0],self.dim[1]))
        for i in range(self.dim[0]):
            for j in range(self.dim[1]):
                newMat.data[i][j] = self.data[i][j] - other.data[i][j]
                
        return newMat
    
    
    def __mul__(self, other):
        if self.dim[0] != other.dim[0] or self.dim[1] != other.dim[1]:
            raise ValueError("The two matrix have different dim")
        
        newMat = Matrix(dim=self.dim)
        for i in range(self.dim[0]):
            
            for j in range(self.dim[1]):
                newMat.data[i][j] =self.data[i][j] * other.data[i][j]
                
        return newMat

    def __len__(self):
        return self.dim[0] * self.dim[1]

    def __str__(self):
        import copy
        result=copy.deepcopy(self.data)
        for i in range(self.dim[0]):
            for j in range(self.dim[1]):
                result[i][j]=str(result[i][j])
        norm=[0]*self.dim[1]
        for i in range(self.dim[0]):
            for j in range(self.dim[1]):
                norm[j]=max(len(result[i][j]),norm[j])
        for i in range(self.dim[0]):
            for j in range(self.dim[1]):
                result[i][j]=' '*(norm[j]-len(result[i][j]))+result[i][j]
        result=str(result)
        result=result.replace(',','')
        result=result.replace("'",'')
        result=result.replace("] [","]\n [")
        return result+'\n'
    def det(self):
        if self.dim[0]!=self.dim[1]:
            raise ValueError("This matrice can not calculate determinant")
        matrix_copy=self.copy().data
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
        matrix_copy=self.copy().data
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
        matrix_copy=self.copy().data
        if x<y:
            temp=self.T()
            matrix_copy=temp.copy().data
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
    pass

