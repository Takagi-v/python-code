class Solution:
    def removeDuplicates(self, nums) -> int:
        if len(nums) == 0:
            return 0
        p = 0
        q = 1
        while q < len(nums):
            if nums[p] != nums[q]:
                nums[p + 1] = nums[q]
                p += 1
            q += 1
        return p + 1


# 原地处理数组问题时一般双指针，不会存在一边删一边遍历，很混乱。
