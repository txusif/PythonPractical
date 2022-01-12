# Put the following code in a file and name it as mycalculator

# Program make a simple calculator

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def sub(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

# Make another file and execute the following code

# from mycalculator import *

a=int(input("Enter number1: "))

b=int(input("Enter number2: "))

print("addition",add(a,b))

print("subtraaction",sub(a,b))

print("multiply",multiply(a,b))

print("division",divide(a,b))