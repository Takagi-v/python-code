class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        target = abs(target)
        k = 0
        while target > 0:
            k += 1
            target -= k
        return k if target % 2 == 0 else k + 1 + k % 2
#脑筋急转弯：加到k时如果delta是偶数，那么必能凑出delta/2，如果不行就考虑k+1，k+2