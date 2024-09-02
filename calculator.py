def calculator():
    a = int(input("enter a value:"))

    b = int(input("enter a value:"))

    operator = input("operator is:")

    if operator == "+":
        print(a + b)

    elif operator == "-":
        print(a - b)

    elif operator == "*":
        print(a * b)

    elif operator == "**":
        print(a ** b)

    elif operator == "/":
        print(a / b)

    else:
        print("INVALID OPERATOR")

calculator()
