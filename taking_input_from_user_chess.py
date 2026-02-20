row = int(input("enter the size of row: "))
col = int(input("enter the size of column: "))

for i in range(row):
    for j in range(col):
        if (i + j) % 2 == 0:
            print("W", end=" ")

        else:
            print("B", end=" ")

    print()
            

