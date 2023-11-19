# 给定一个自然数n, 判断n是不是质数
# n=int(input())
# cnt=0
# prime=[0]
# def ge_prime(n):
#  vis=[0]*100
#  for i in range(2,n+1):
#    if vis[i]!=0:
#      prime.append(i)
#      cnt+=1
#    for j in range(0,int(cnt)) and i*prime[j]<=n:
#      vis[i*prime[j]]=True
#      if i%prime[j]==0:
#        break
# ge_prime(n)
# for i in range(0,cnt):
#  print(prime[i])
import math

n = int(input())
a = math.sqrt(n)


def is_prime(x):
    i = 1
    while i < a:
        i += 1
        if n % i <= 1e-6:
            return False
    return True


print(is_prime(n))
