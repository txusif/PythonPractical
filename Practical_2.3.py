# Write a program to print items of the list

list1 = [2, 3, -4, 6, 7, 9, 10]
for i in range(0, 7):
    print(list1[i])

print("-"*10)

# for print only positive numbers
for i in range(0, 7):
    if (list1[i] > 0):
        print(list1[i])
