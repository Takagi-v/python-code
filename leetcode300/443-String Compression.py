from collections import Counter


class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        cur = chars[0]
        cnt = 0
        ans = []
        for c in chars + [""]:
            if c == cur:
                cnt += 1
            else:
                ans += [cur]
                if cnt != 1:
                    ans += list(str(cnt))
                cnt = 1
                cur = c
        chars[:] = ans
        return len(chars)
