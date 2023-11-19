class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        set1 = set()
        for i in nums:
            if i not in set1:
                set1.add(i)
            else:
                return True
        return False
