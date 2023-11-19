def sum_of_two(n):
    sum = 0
    x = 2
    for i in range(n):
        sum += x
        x = x * 10 + 2
    return sum


n = int(input())
print(sum_of_two(n))
