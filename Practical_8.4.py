# Program to print Factorial of a number using function

def factorial(n):
    "This function prints Factorial of a number"
    fact = 1
    for i in range(1, n+1):
        fact = fact*i
    print("Factorial of", n, "is", fact)


print(factorial.__doc__)
factorial(5)
factorial(6)
