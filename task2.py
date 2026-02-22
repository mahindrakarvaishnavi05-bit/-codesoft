


result = float(input("Enter first number: "))


while True:
    print("\nChoose operation:")
    print("+  Add")
    print("-  Subtract")
    print("*  Multiply")
    print("/  Divide")
    print("5  Exit")

    op = input("Enter operation: ")

    
    if op == "5":
        print("Final Result =", result)
        break

    
    num = float(input("Enter next number: "))

    
    if op == "+":
        result = result + num

    elif op == "-":
        result = result - num

    elif op == "*":
        result = result * num

    elif op == "/":
        if num != 0:
            result = result / num
        else:
            print("Error: Division by zero not allowed")
            continue

    else:
        print("Invalid operation")
        continue

    
    print("Current Result =", result)
