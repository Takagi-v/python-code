class Solution(object):
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 9
        upper = 10**n - 1
        for left in range(upper, upper // 10, -1):
            p, x = left, left
            while x:
                p = p * 10 + x % 10
                x //= 10
            x = upper
            while x * x >= p:
                if p % x == 0:
                    return p % 1337
                x -= 1
