class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num==1:
            return False
        sum=1
        d=2
        while d*d <=num:
            if num%d==0:
                sum+=d
                if d*d <num:
                    sum+=num/d
            d+=1
        return sum==num