class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        cmax = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                cmax += 1
                ans = max(cmax, ans)
            if nums[i] == 0:
                cmax = 0
        return ans
