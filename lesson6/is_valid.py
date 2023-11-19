def is_valid(s):
    a = [False] * 6
    a[5] = True
    for i in s:
        if i >= "a" and i <= "z":
            a[0] = True
        if i >= "A" and i <= "Z":
            a[1] = True
        if i >= "0" and i <= "9":
            a[2] = True
        if i == "$" or i == "#" or i == "@":
            a[3] = True
        if len(s) >= 6 and len(s) <= 16:
            a[4] = True
    for i in range(0, 5):
        if a[i] == False:
            a[5] = False
            break
    return a[5]


s = "Hh1234$"
s1 = "1234H$"
print(is_valid(s))
print(is_valid(s1))
