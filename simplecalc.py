# defining functions
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y

def calculator(num1, num2, operation):
    if operation == "+":
        result = add(num1, num2)
    elif operation == "-":
        result = subtract(num1, num2)
    elif operation == "*":
        result = multiply(num1, num2)
    elif operation == "/":
        result = divide(num1, num2)
    else:
        print("Invalid operation. Please try again.")
        return None
    return result


def main():
    while True:
        num1_input = input("Enter the first number or 'q' to quit: ")
        if num1_input.lower() == 'q':
            break

        num2_input = input("Enter the second number or 'q' to quit: ")
        if num2_input.lower() == 'q':
            break

        operation = input("Enter the operation (+, -, *, /) or 'q' to quit: ")
        if operation.lower() == 'q':
            break

        try:
            num1 = float(num1_input)
            num2 = float(num2_input)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

# calling the calculator function defined earlier
        result = calculator(num1, num2, operation)

        if result is not None:
            print("The result is: ", result)


main()


def main():
    while True:
        num1_input = input("Enter the first number or 'q' to quit: ")
        if num1_input.lower() == 'q':
            break

        num2_input = input("Enter the second number or 'q' to quit: ")
        if num2_input.lower() == 'q':
            break

        operation = input("Enter the operation (+, -, *, /) or 'q' to quit: ")
        if operation.lower() == 'q':
            break

        try:
            num1 = float(num1_input)
            num2 = float(num2_input)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

# calling the calculator function defined earlier
        result = calculator(num1, num2, operation)

        if result is not None:
            print("The result is: ", result)


main()
