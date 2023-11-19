class Solution:
    def moveZeroes(self, nums):
        cnt = 0
        for i in range(len(nums))[::-1]:
            if nums[i] == 0:
                del nums[i]
                cnt += 1
        nums += [0] * cnt
