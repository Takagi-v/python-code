class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a, b, c = float("-inf"), float("-inf"), float("-inf")
        for num in nums:
            if num > a:
                a, b, c = num, a, b
            elif a > num > b:
                b, c = num, b
            elif b > num > c:
                c = num
        return a if c == (float("-inf")) else c
