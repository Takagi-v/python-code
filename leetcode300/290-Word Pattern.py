class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        p=s.split()
        l=len(p)
        if len(pattern)!=l:
            return False
        dt={}
        st={}
        for i in range(l):
            if p[i] in dt:
                if pattern[i] not in st:
                    return False
                if dt[p[i]]!=pattern[i]:
                    return False
            if pattern[i] in st:
                if p[i] not in dt:
                    return False
                if st[pattern[i]]!=p[i]:
                    return False
            dt[p[i]]=pattern[i]
            st[pattern[i]]=p[i]
        return True