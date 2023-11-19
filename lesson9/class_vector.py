class Vector:
    def __init__(self, n) -> None:
        self.n = n

    def get_loca(self, x):
        return self.n[x - 1]

    def mod_loca(self, x, y):
        self.n[x - 1] = y

    def length(self):
        sum = 0
        for i in self.n:
            sum += i**2
        return sum**0.5

    def print_length(self):
        print(self.length())

    def angle(self):
        a = self.n.copy()
        for i in a:
            i = i / self.length()

    def print_angle(self):
        print(self.angle())

    def dot(self, other):
        sum = 0
        for i in range(len(self.n)):
            sum += self.n[i] * other[i]
        return sum

    def scale(self, ratio):
        a = self.n.copy()
        for i in a:
            a = a * ratio
        return a

    def is_orthohonal(self, other):
        if self.dot(other):
            return False
        return True

    def __str__(self) -> str:
        return f"vector:{self.n}"

    def __le__(self, other):
        return self.n[0] <= other.n[0]

    def __lt__(self, other):
        return self.n[0] < other.n[0]

    def __eq__(self, other) -> bool:
        return self.n[0] == other.n[0]

    def __ne__(self, other) -> bool:
        return self.n[0] != other.n[0]

    def __gt__(self, other):
        return self.n[0] > other.n[0]

    def __ge__(self, other):
        return self.n[0] >= other.n[0]


a = [1, 2, 3]
b = [1, 3, 4]
c = [2, 3, 4]
s1 = Vector(a)
s2 = Vector(b)
s3 = Vector(c)
print(s1 == s2)
print(s2 < s3)
print(s1 <= s2)
print(s1)
print(s2)
print(s3)
