# Program make a simple calculator

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # take input from the user
    operator = input("Enter choice(1/2/3/4): ")

    # check if Operator is one of the four options
    if operator in ('1', '2', '3', '4'):
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        if operator == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")

        elif operator == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")

        elif operator == '3':
            print(f"{num1} x {num2} = {multiply(num1, num2)}")

        elif operator == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")

        # check if user wants another calculation
        # break the while loop if answer is No
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break
    else:
        print("Invalid Input")
