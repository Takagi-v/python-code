class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        temp = x ^ y
        ans = 0
        while temp > 0:
            if temp % 2 == 1:
                ans += 1
            temp >>= 1
        return ans
