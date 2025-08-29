def grade(p):#function define
    if p >=90: return "A"
    if p >=75: return "B"
    if p >=60: return "C"
    if p >=40: return "D"
    return "F"
marks = float(input("percentage: "))
print ("grade :",grade(marks))# function call