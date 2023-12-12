import bisect


class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters.sort()
        ans = 0
        for house in houses:
            j = bisect.bisect_right(heaters, house)
            i = j - 1
            rightDistance = heaters[j] - house if j < len(heaters) else float("inf")
            leftDistance = house - heaters[i] if i >= 0 else float("inf")
            curDistance = min(leftDistance, rightDistance)
            ans = max(ans, curDistance)
        return ans
'''bisect(list, value, lo=0, hi=len(list), key=None)：在有序列表中查找将值插入的位置，并返回该位置的索引，它是 bisect_right 的别名。
bisect_left(list, value, lo=0, hi=len(list), key=None)：在有序列表中查找将值插入的位置，并返回左侧的索引（相同值的最左边位置）。
bisect_right(list, value, lo=0, hi=len(list), key=None)：在有序列表中查找将值插入的位置，并返回右侧的索引（相同值的最右边位置）。
insort(list, value, lo=0, hi=len(list), key=None)：将值插入有序列表中的适当位置，它是 insort_right 的别名。
insort_left(list, value, lo=0, hi=len(list), key=None)：将值插入有序列表中的最左侧位置。
insort_right(list, value, lo=0, hi=len(list), key=None)：将值插入有序列表中的最右侧位置。'''