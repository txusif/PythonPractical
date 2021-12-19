#  To implment Tuple manipulation

tup1 = (1, 2, 3, 4, 5, 6, 7)
print(tup1)
print("First element:", tup1[0])
print("Element between 2-5:", tup1[1:5])
print("Last 3 elements:", tup1[-3:])

tup2 = ('a', 'b', 'c', 'd', 'e')
print(tup2)

tup3 = tup1 + tup2
print(tup3)

# tup3[1] = 4
# print(tup3)

# del(tup3[3])
# print(tup3)

print("Printing tup3 four times")
print(tup3 * 4)

for i in tup3:
    print(i)

print("3 exist in list3:", 3 in tup3)

print("Count of number 4 in tup3:", tup3.count(4))

print("Length of tup3:", len(tup3))

print("Maximum in tup1 is:", max(tup1), "Minimum in tup1 is:", min(tup1))
print("Maximum in tup2 is:", max(tup2), "Minimum in tup2 is:", min(tup2))
