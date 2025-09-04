class NegativeNumberError(Exception):
    pass

try:
    num = int(input("Enter a positive number: "))
    if num < 0:
        raise NegativeNumberError("Negative number not allowed!")
    print("Number is:", num)
except NegativeNumberError as e:
    print("Error:", e)
