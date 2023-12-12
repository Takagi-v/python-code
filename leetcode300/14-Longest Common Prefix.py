class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        prefix = strs[0]
        l = len(strs)
        for i in range(1, l):
            prefix = self.lcp(prefix, strs[i])
            if not prefix:
                break
        return prefix

    def lcp(self, str1, str2):
        l1 = min(len(str1), len(str2))
        index = 0
        while index < l1 and str1[index] == str2[index]:
            index += 1
        return str1[:index]
