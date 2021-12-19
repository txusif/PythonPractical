#  To implment List manipulation

list1 = [1, 2, 3, 4, 5, 6, 7]
print(list1)
print("First element:", list1[0])
print("Element between 2-5:", list1[1:5])
print("Last 3 elements:", list1[4:])

list2 = ['a', 'b', 'c', 'd', 'e']
print(list2)

list3 = list1 + list2
print(list3)

list3[1] = 4
print(list3)

del(list3[2])
print(list3)

print("Printing list3 four times")
for i in range(1, 5):
    print(list3)

for i in list3:
    print(i)

print("3 exist in list3:",3 in list3)

print("Count of number 4 in list3:", list3.count(4))

list3.append("8")
print(list3)

list3.insert(5, 'a')
print(list3)

print("Length of list3:", len(list3))

list3.reverse()
print(list3)

list1.sort()
print(list1)

list2.sort()
print(list2)

print("Maximum in list1 is:", max(list1), "Minimum in list1 is:", min(list1))
print("Maximum in list2 is:", max(list2), "Minimum in list2 is:", min(list2))