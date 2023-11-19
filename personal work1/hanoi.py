def Hanoi_plus(n, x, y, z):
    if n == 1:
        print(f"{x}->{y}")
        print(f"{y}->{z}")
        return
    Hanoi_plus(n - 1, x, y, z)
    print(f"{x}->{y}")
    Hanoi_plus(n - 1, z, y, x)
    print(f"{y}->{z}")
    Hanoi_plus(n - 1, x, y, z)


Hanoi_plus(3, "A", "B", "C")
