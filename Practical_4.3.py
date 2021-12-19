# Program to print all even numbers between 15 to 50

print("Using For loop")
for i in range(15, 51):
    if (i % 2 == 0):
        print(i, end=" ")

print("\nUsing While loop")
i = 15
while (i <= 50):
    if (i % 2 == 0):
        print(i, end=" ")
    i = i + 1
