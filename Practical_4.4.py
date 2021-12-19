# Program to print Fibonacci series

fivio = int(input("Enter the number of terms: "))
a = 0
b = 1
if (fivio == 1):
    print(a)
else:
    print(a, end=" ")
    print(b, end=" ")
    for i in range(2, fivio):
        c = a + b
        a = b
        b = c
        print(c, end=" ")