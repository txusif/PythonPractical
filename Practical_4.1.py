# To implement iterative statement using while loop

num = int(input("Enter a number: "))
print("The table of", num, "is")

i = 1
while (i <= 10):
    print(num, "x", i, "=", (num*i))
    i = i + 1
