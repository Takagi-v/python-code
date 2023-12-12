class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        highbit = 0
        for i in range(1, 30 + 1):
            if num >= (1 << i):
                highbit = i
            else:
                break
        mask = (1 << (highbit + 1)) - 1
        return num ^ mask
