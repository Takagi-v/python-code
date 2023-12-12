class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = b = c = float("-inf")
        d = e = float("inf")
        for num in nums:
            if num > a:
                a, b, c = num, a, b
            elif num > b:
                b, c = num, b
            elif num > c:
                c = num
            if num < d:
                d, e = num, d
            elif num < e:
                e = num
        return max(d * e * a, a * b * c)
