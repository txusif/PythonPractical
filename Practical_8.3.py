# Program to print all Even numbers till n terms using function

def even(x):
    "This function prints Even numbers"
    for x in range(2,x+1):
        if x % 2 == 0:
           print(x,end=" ")
    
print(even.__doc__)
even(50)