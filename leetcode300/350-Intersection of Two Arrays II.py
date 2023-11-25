from collections import Counter


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        intersection = []
        for num, count in count1.items():
            if num in count2:
                intersection.extend([num] * min(count, count2[num]))
        return intersection
