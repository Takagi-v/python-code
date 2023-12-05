import math


class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        x = int(n**0.5) - 1
        return int(math.sqrt(n * 2 + 0.25) - 0.5)
