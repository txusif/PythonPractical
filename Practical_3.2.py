# Program to fing greatest of the 3 numbers

a = int(input("Enter number1: "))
b = int(input("Enter number2: "))
c = int(input("Enter number3: "))

if (a > b) and (a > c):
    print(a, "is the greatest number")
elif (b > a) and (b > c):
    print(b, "is the greatest number")
else:
    print(c, "is the greatest number")
