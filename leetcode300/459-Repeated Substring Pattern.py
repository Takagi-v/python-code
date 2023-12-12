class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        flag = False
        for i in range(len(s) // 2):
            if len(s) % (i + 1) != 0:
                continue
            mul = len(s) // (i + 1)
            if s[: i + 1] * mul == s:
                flag = True
                break
        return flag
