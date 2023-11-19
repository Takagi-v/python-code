def check_num(a):
    if a[0] == "0" and len(a) > 1:
        return False
    for i in a:
        if i >= "9" or i <= "0":
            return False
    return True


a = "1234ser"
b = "1234"
print(check_num(a))
print(check_num(b))
