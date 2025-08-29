def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): 
    if b == 0: 
        return "Cannot divide by zero"
    return a / b

while True:
    print("\n1.Add  2.Sub  3.Mul  4.Div  5.Exit")
    ch = input("Choice: ")
    if ch == "5":
        print("Bye!")
        break
    if ch in ("1","2","3","4"):
        a = float(input("a: "))
        b = float(input("b: "))
        if ch == "1": print("Ans:", add(a,b))
        elif ch == "2": print("Ans:", sub(a,b))
        elif ch == "3": print("Ans:", mul(a,b))
        else: print("Ans:", div(a,b))
    else:
        print("Invalid choice")
