n = int(input())
ma1 = [[0] * n for i in range(n)]
for i in range(0, n):
    for j in range(0, n):
        ma1[i][j] = i + 1
ma2 = [[0] * n for i in range(n)]
for i in range(0, n):
    for j in range(0, n):
        ma2[i][j] = j + 1
print(ma1)
print(ma2)
