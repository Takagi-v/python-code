class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        s.sort()
        g.sort()
        ans = 0
        for i in range(len(s) - 1, -1, -1):
            for j in range(len(g) - 1, -1, -1):
                if s[i] >= g[j] and g[j] != 0:
                    ans += 1
                    g[j] = 0
                    break
        return ans
