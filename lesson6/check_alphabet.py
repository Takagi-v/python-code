def check_al(s):
    dt = {"a", "A", "e", "E", "i", "I", "o", "O", "u", "U"}
    return s in dt


a = "a"
b = "b"
print(check_al(a))
print(check_al(b))
