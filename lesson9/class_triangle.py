class Triangle:
    def __init__(self, a=0, b=0, c=0) -> None:
        self.a, self.b, self.c = a, b, c

    def is_valid(self):
        return (
            self.a > 0
            and self.b > 0
            and self.c > 0
            and self.a + self.b > self.c
            and self.b + self.c > self.a
            and self.c + self.a > self.b
        )

    def set_edge(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def area(self):
        q = (self.a + self.b + self.c) / 2
        return (q * (q - self.a) * (q - self.b) * (q - self.c)) ** 0.5

    def print(self):
        print(f"Triangle:{self.a},{self.b},{self.c}")

    def print_area(self):
        print(f"area:{self.area():.3f}")


t1 = Triangle(3, 4, 5)
if t1.is_valid():
    t1.print()
    t1.print_area()
