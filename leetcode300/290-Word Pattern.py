class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        p = s.split()
        l = len(p)
        if len(pattern) != l:
            return False
        dt = {}
        st = {}
        for i in range(l):
            if p[i] in dt:
                if pattern[i] not in st:
                    return False
                if dt[p[i]] != pattern[i]:
                    return False
            if pattern[i] in st:
                if p[i] not in dt:
                    return False
                if st[pattern[i]] != p[i]:
                    return False
            dt[p[i]] = pattern[i]
            st[pattern[i]] = p[i]
        return True
#输入:
#a = [1, 2, 3]b = ['a', 'b', 'c']result = #list(zip(a, b))print(result)
#输出：
#[(1, 'a'), (2, 'b'), (3, 'c')]