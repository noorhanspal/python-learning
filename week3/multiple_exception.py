try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(result)
except ValueError:
    print("Error: Invalid input, please enter a number")
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
