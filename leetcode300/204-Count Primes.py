class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt = 0
        if n < 3:
            return 0
        prime = [1] * n
        prime[0] = prime[1] = 0
        for i in range(2, int(n**0.5) + 1):
            if prime[i]:
                prime[i * i : n : i] = [0] * ((n - 1) // i - i + 1)
        return sum(prime)
