class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False
        a = [2, 3, 5]
        for i in a:
            while n % i == 0:
                n /= i
        return n == 1
