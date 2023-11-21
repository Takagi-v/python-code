class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dt1, dt2 = {}, {}
        for i in s:
            if i in dt1:
                dt1[i] = dt1[i] + 1
            else:
                dt1[i] = 1
        for i in t:
            if i in dt2:
                dt2[i] = dt2[i] + 1
            else:
                dt2[i] = 1
        return dt1 == dt2

import collections
class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        cnt1 = collections.Counter(s)
        cnt2 = collections.Counter(t)
        return not (cnt1 - cnt2) and not (cnt2 - cnt1)
