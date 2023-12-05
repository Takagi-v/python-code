from collections import Counter


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        cnt1 = [0] * 26
        cnt2 = [0] * 26
        sa = []
        l = len(p)
        for c in p:
            cnt1[ord(c) - 97] += 1
        for c in s[: l - 1]:
            cnt2[ord(c) - 97] += 1
        for i in range(0, len(s) - l + 1):
            cnt2[ord(s[i + l - 1]) - 97] += 1

            if cnt1 == cnt2:
                sa.append(i)
            cnt2[ord(s[i]) - 97] -= 1
        return sa


# ord函数为返回单个字符的ASCII码值，输入字符串会报错
