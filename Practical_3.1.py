# Program to identify whether a number is Odd or Even

num = int(input("Enter a number: "))
if (num % 2 == 0):
    print(num, "is an Even number")
elif (num % 2 == 1):
    print(num, "is an Odd number")
else:
    print("Incorrect input")
