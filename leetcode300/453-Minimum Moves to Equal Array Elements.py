class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_n = min(nums)
        res = 0
        for num in nums:
            res += num - min_n
        return res
