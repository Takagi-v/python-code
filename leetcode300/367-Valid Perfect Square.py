class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        for i in range(int(num**0.5 - 2), int(num**0.5 + 2)):
            if i * i == num:
                return True
        return False
