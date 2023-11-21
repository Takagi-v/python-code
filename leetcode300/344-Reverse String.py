class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left = 0
        rig = len(s) - 1
        while left < rig:
            a = s[left]
            s[left] = s[rig]
            s[rig] = a
            left += 1
            rig -= 1


# 解法2
s = [1, 2, 3, 4]
s = s[::-1]
