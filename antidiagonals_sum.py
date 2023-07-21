def anti_diagonals(num_rows, num_columns, matrix):
    for x in range(num_rows - 1):
        i = 0
        j = x
        while i < num_rows:
            if 0 <= j < num_columns:
                print(matrix[i][j], end=" ")
            else:
                print("0", end=" ")
            i += 1
            j -= 1
        print()
    for y in range(num_columns):
        i = y
        j = num_columns - 1
        while j >= 0:
            if 0 <= i < num_rows:
                print(matrix[i][j], end=" ")
            else:
                print("0", end=" ")
            i += 1
            j -= 1
        print()
matrix = []
num_rows = int(input())
num_columns = int(input())
for i in range(num_rows):
    matrix.append(list(map(int, input().split())))
anti_diagonals(num_rows, num_columns, matrix)
