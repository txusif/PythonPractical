# Program to accept a number and print its Factorial

num = int(input("Enter a number: "))

i = num
fact = 1
while (i >= 1):
    fact = fact * i
    i = i - 1
print("Factorial of", num, "is", fact)
