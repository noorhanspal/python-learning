age = int(input("Enter age: "))
if age < 18:
    raise ValueError("Age must be 18 or above")
else:
    print("You are eligible")
