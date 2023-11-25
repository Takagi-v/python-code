from collections import Counter


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = Counter(s)
        ans = 0
        flag = 0
        for i in count:
            if count[i] % 2 == 0:
                ans += count[i]
            else:
                ans += count[i] - 1
                flag = 1
        return ans if flag == 0 else ans + 1
