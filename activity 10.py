height = int(input("Enter height: "))
for row in range(1, height+1):
    for column in range(row):
        print(row, end=" ")
    print()