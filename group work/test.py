def I(n):
    """
    return an n*n unit matrix
    """
    result=[]
    for i in range(n):
        temp=[0]*n
        temp[i]=1
        result.append(temp)
    return result
print(I(3))