def happy_number(n):
    st = {n}
    while n != 1:
        x = sum_of_digit_squares(n)
        if x == 1:
            return True
        if x in st:
            return False
        st.add(x)
        n = x
    return True


def sum_of_digit_squares(n):
    total = 0
    while n > 0:
        total += (n % 10) ** 2
        n //= 10
        return total


ans = []
for x in range(1001):
    if happy_number(x):
        ans.append(x)
print(len(ans))


class Solution(object):
    def isHappy(self, n):
        """
        :type n:int
        :rtype:bool
        """
        set1 = set()
        while n not in set1:
            set1.add(n)
            temp = 0
            while n:
                n, val = divmod(n, 10)
                temp += val**2
            n = temp
        return True if n == 1 else False
