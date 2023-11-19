class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dt = {}
        for i, n in enumerate(nums):
            if n in dt:
                if i - dt[n] <= k:
                    return True
            dt[n] = i
        return False
