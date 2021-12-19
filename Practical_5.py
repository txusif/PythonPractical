# To implement various string manipulation

tx = "love yourz 2014"
print(tx)
print("1st letter:",tx[0])
print("8th letter:",tx[7])
print("First word:",tx[0:4])
print("last word:",tx[5:10])
print("Year:",tx[11: ])
print("Count of O in tx:",tx.count("o"))
print("Splitted string:",tx.split(" "))
print("Starts with l:",tx.startswith("l"))
print("Ends with 4:",tx.endswith("4"))
print("UPPER CASE:",tx.upper())
print("lower case:",tx.lower())
print("Capital case:",tx.capitalize())
print("Sentence Case:",tx.title())
print("Swap case:",tx.swapcase())