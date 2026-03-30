number = int(input("Enter a number: "))

for i in range(1, 11): #ek thi das ni range ma j code hovo joye
    print(number, "x", i, "=", number * i)

    # define two values: "i" and "number",
    # 1. number = desired number to become the base of table
    # 2. i = from range 1 to 10 from which the number will get multiplied
    # 3. arrange all the outcomes in such a manner it looks like a table; print(number x i = number*i)