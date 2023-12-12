class Solution(object):
    def flipLights(self, n, presses):
        """
        :type n: int
        :type presses: int
        :rtype: int
        """
        ans = set()
        for i in range(2**4):
            pressArr = [(i >> j) & 1 for j in range(4)]
            if sum(pressArr) % 2 == presses % 2 and sum(pressArr) <= presses:
                status = pressArr[0] ^ pressArr[2] ^ pressArr[3]
                if n >= 2:
                    status |= (pressArr[0] ^ pressArr[1]) << 1
                if n >= 3:
                    status |= (pressArr[0] ^ pressArr[2]) << 2
                if n >= 4:
                    status |= (pressArr[0] ^ pressArr[1] ^ pressArr[3]) << 3
                ans.add(status)
        return len(ans)
'''
首先，不需要考虑按钮按动的顺序，而只需要考虑每个按钮被按了几次，在按钮按动次数一样的情况下，顺序不影响灯泡最后的状态。更进一步地，不需要考虑每个按钮具体被按了几次，而只需要考虑被按了奇数次还是偶数次即可，某个键每多按或少按 2 次及其倍数次，也不影响最后的状态。
其次,观察每个按钮的效果,可以发现所有按钮可以根据编号划分为以下4组,周期为6.
'''