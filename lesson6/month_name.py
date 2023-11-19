def convert_mouth_to_days(a):
    dt = {
        "January": 31,
        "February": 28,
        "March": 31,
        "April": 30,
        "May": 31,
        "June": 30,
        "July": 31,
        "August": 30,
        "September": 31,
        "October": 30,
        "November": 31,
        "December": 30,
    }
    return dt[a]


a = "January"
print(convert_mouth_to_days(a))
