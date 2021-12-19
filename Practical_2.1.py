# Write a program to calculate Percentage

sub1 = int(input("Enter Subject 1 marks: "))
sub2 = int(input("Enter Subject 2 marks: "))
sub3 = int(input("Enter Subject 2 marks: "))

total = sub1 + sub2 + sub3
percent = total/3
percent1 = (total/3)*100

print("Total ", total)
print("Percentage: ", percent,"%")
print("Percentage1:", percent1,"%")
