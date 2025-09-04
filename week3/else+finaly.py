try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Result is:", result)
finally:
    print("This will always execute")
