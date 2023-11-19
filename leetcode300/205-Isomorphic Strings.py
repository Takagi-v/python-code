class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        dt = {}
        set1 = set()
        for i in range(len(s)):
            if s[i] in dt:
                if dt[s[i]] != t[i]:
                    return False
            elif t[i] in set1:
                return False
            else:
                dt[s[i]] = t[i]
                set1.add(t[i])
        return True
