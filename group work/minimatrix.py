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
        r"""
        将矩阵从(m,n)维拉伸为newdim=(m1,n1)
        该函数不改变 self

        Args:
                newdim: 一个元组 (m1, n1) 表示拉伸后的矩阵形状。如果 m1 * n1 不等于 self.dim[0] * self.dim[1],
                                应抛出异常

        Returns:
                Matrix: 一个 Matrix 类型的返回结果, 表示 reshape 得到的结果
        """
        pass

    def dot(self, other):
        r"""
        矩阵乘法：矩阵乘以矩阵
        按照公式 A[i, j] = \sum_k B[i, k] * C[k, j] 计算 A = B.dot(C)

        Args:
                other: 参与运算的另一个 Matrix 实例

        Returns:
                Matrix: 计算结果

        Examples:
                >>> A = Matrix(data=[[1, 2], [3, 4]])
                >>> A.dot(A)
                >>> [[ 7 10]
                         [15 22]]
        """
        pass

    def T(self):
        r"""
        矩阵的转置

        Returns:
                Matrix: 矩阵的转置

        Examples:
                >>> A = Matrix(data=[[1, 2], [3, 4]])
                >>> A.T()
                >>> [[1 3]
                         [2 4]]
                >>> B = Matrix(data=[[1, 2, 3], [4, 5, 6]])
                >>> B.T()
                >>> [[1 4]
                         [2 5]
                         [3 6]]
        """

    def sum(self, axis=None):
        r"""
        根据指定的坐标轴对矩阵元素进行求和

        Args:
                axis: 一个整数，或者 None. 默认值: None
                          axis = 0 表示对矩阵进行按列求和，得到形状为 (1, self.dim[1]) 的矩阵
                          axis = 1 表示对矩阵进行按行求和，得到形状为 (self.dim[0], 1) 的矩阵
                          axis = None 表示对矩阵全部元素进行求和，得到形状为 (1, 1) 的矩阵

        Returns:
                Matrix: 一个 Matrix 类的实例，表示求和结果

        Examples:
                >>> A = Matrix(data=[[1, 2, 3], [4, 5, 6]])
                >>> A.sum()
                >>> [[21]]
                >>> A.sum(axis=0)
                >>> [[5 7 9]]
                >>> A.sum(axis=1)
                >>> [[6]
                         [15]]
        """
        pass

    def copy(self):
        r"""
        返回matrix的一个备份

        Returns:
                Matrix: 一个self的备份
        """
        pass

    def Kronecker_product(self, other):
        r"""
        计算两个矩阵的Kronecker积，具体定义可以搜索，https://baike.baidu.com/item/克罗内克积/6282573

        Args:
                other: 参与运算的另一个 Matrix

        Returns:
                Matrix: Kronecke product 的计算结果
        """
        pass

    def __getitem__(self, key):
        r"""
        实现 Matrix 的索引功能，即 Matrix 实例可以通过 [] 获取矩阵中的元素（或子矩阵）

        x[key] 具备以下基本特性：
        1. 单值索引
                x[a, b] 返回 Matrix 实例 x 的第 a 行, 第 b 列处的元素 (从 0 开始编号)
        2. 矩阵切片
                x[a:b, c:d] 返回 Matrix 实例 x 的一个由 第 a, a+1, ..., b-1 行, 第 c, c+1, ..., d-1 列元素构成的子矩阵
                特别地, 需要支持省略切片左(右)端点参数的写法, 如 x 是一个 n 行 m 列矩阵, 那么
                x[:b, c:] 的语义等价于 x[0:b, c:m]
                x[:, :] 的语义等价于 x[0:n, 0:m]

        Args:
                key: 一个元组，表示索引

        Returns:
                索引结果，单个元素或者矩阵切片

        Examples:
                >>> x = Matrix(data=[
                                        [0, 1, 2, 3],
                                        [4, 5, 6, 7],
                                        [8, 9, 0, 1]
                                ])
                >>> x[1, 2]
                >>> 6
                >>> x[0:2, 1:4]
                >>> [[1 2 3]
                         [5 6 7]]
                >>> x[:, :2]
                >>> [[0 1]
                         [4 5]
                         [8 9]]
        """
        pass

    def __setitem__(self, key, value):
        r"""
        实现 Matrix 的赋值功能, 通过 x[key] = value 进行赋值的功能

        类似于 __getitem__ , 需要具备以下基本特性:
        1. 单元素赋值
                x[a, b] = k 的含义为，将 Matrix 实例 x 的 第 a 行, 第 b 处的元素赋值为 k (从 0 开始编号)
        2. 对矩阵切片赋值
                x[a:b, c:d] = value 其中 value 是一个 (b-a)行(d-c)列的 Matrix 实例
                含义为, 将由 Matrix 实例 x 的第 a, a+1, ..., b-1 行, 第 c, c+1, ..., d-1 列元素构成的子矩阵 赋值为 value 矩阵
                即 子矩阵的 (i, j) 位置赋值为 value[i, j]
                同样地, 这里也需要支持如 x[:b, c:] = value, x[:, :] = value 等省略写法

        Args:
                key: 一个元组，表示索引
                value: 赋值运算的右值，即要赋的值

        Examples:
                >>> x = Matrix(data=[
                                        [0, 1, 2, 3],
                                        [4, 5, 6, 7],
                                        [8, 9, 0, 1]
                                ])
                >>> x[1, 2] = 0
                >>> x
                >>> [[0 1 2 3]
                         [4 5 0 7]
                         [8 9 0 1]]
                >>> x[1:, 2:] = Matrix(data=[[1, 2], [3, 4]])
                >>> x
                >>> [[0 1 2 3]
                         [4 5 1 2]
                         [8 9 3 4]]
        """
        pass

    def __pow__(self, n):
        r"""
        矩阵的n次幂，n为自然数
        该函数应当不改变 self 的内容

        Args:
                n: int, 自然数

        Returns:
                Matrix: 运算结果
        """
        pass

    def __add__(self, other):
        r"""
        两个矩阵相加
        该函数应当不改变 self 和 other 的内容

        Args:
                other: 一个 Matrix 实例

        Returns:
                Matrix: 运算结果
        """
        pass

    def __sub__(self, other):
        r"""
        两个矩阵相减
        该函数应当不改变 self 和 other 的内容

        Args:
                other: 一个 Matrix 实例

        Returns:
                Matrix: 运算结果
        """
        pass

    def __mul__(self, other):
        r"""
        两个矩阵 对应位置 元素  相乘
        注意 不是矩阵乘法dot
        该函数应当不改变 self 和 other 的内容

        Args:
                other: 一个 Matrix 实例

        Returns:
                Matrix: 运算结果

        Examples:
                >>> Matrix(data=[[1, 2]]) * Matrix(data=[[3, 4]])
                >>> [[3 8]]
        """
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
        r"""
        计算方阵的行列式。对于非方阵的情形应抛出异常。
        要求: 该函数应不改变 self 的内容; 该函数的时间复杂度应该不超过 O(n**3).
        提示: Gauss消元

        Returns:
                一个 Python int 或者 float, 表示计算结果
        """
        pass

    def inverse(self):
        r"""
        计算非奇异方阵的逆矩阵。对于非方阵或奇异阵的情形应抛出异常。
        要求: 该函数应不改变 self 的内容; 该函数的时间复杂度应该不超过 O(n**3).
        提示: Gauss消元

        Returns:
                Matrix: 一个 Matrix 实例，表示逆矩阵
        """
        pass

    def rank(self):
        r"""
        计算矩阵的秩
        要求: 该函数应不改变 self 的内容; 该函数的时间复杂度应该不超过 O(n**3).
        提示: Gauss消元

        Returns:
                一个 Python int 表示计算结果
        """
        pass


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
    r"""
    将若干矩阵按照指定的方向拼接起来
    若给定的输入在形状上不对应，应抛出异常
    该函数应当不改变 items 中的元素

    Args:
            items: 一个可迭代的对象，其中的元素为 Matrix 类型。
            axis: 一个取值为 0 或 1 的整数，表示拼接方向，默认值 0.
                      0 表示在第0维即行上进行拼接
                      1 表示在第1维即列上进行拼接

    Returns:
            Matrix: 一个 Matrix 类型的拼接结果

    Examples:
            >>> A, B = Matrix([[0, 1, 2]]), Matrix([[3, 4, 5]])
            >>> concatenate((A, B))
            >>> [[0 1 2]
                     [3 4 5]]
            >>> concatenate((A, B, A), axis=1)
            >>> [[0 1 2 3 4 5 0 1 2]]
    """
    pass


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
