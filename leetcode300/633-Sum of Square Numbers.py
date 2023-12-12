class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        low, high = 0, int(c**0.5)
        while low <= high:
            cur = low * low + high * high
            if cur == c:
                return True
            elif cur < c:
                low += 1
            else:
                high -= 1
        return False
