class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in nums1:
            k = nums2.index(i)
            flag = 0
            for j in range(k + 1, len(nums2)):
                if nums2[j] > i:
                    ans.append(nums2[j])
                    flag = 1
                    break
            if flag == 0:
                ans.append(-1)
        return ans
