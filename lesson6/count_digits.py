def count_digit(a):
    evenx,oddx=0,0
    for i in a:
        if i % 2 == 0:
            evenx += 1
        else:
            oddx += 1
    return oddx, evenx


a = [123, 234, 345, 121, 232]
print(count_digit(a))
