rows, columns = input().split()
rows = int(rows)
columns = int(columns)
for i in range(1, rows, 2):
    print((".|." * i).center(columns, "-"))
print("WELCOME".center(columns, "-"))
for i in range(rows - 2, -1, -2):
    print((".|." * i).center(columns, "-"))
    