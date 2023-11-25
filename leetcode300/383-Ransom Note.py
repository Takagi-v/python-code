from collections import Counter


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        count1 = Counter(ransomNote)
        count2 = Counter(magazine)
        for num, count in count1.items():
            if num not in count2:
                return False
            if count > count2[num]:
                return False
        return True
