import math


def reverse_list(l: list):
    """
    Reverse a list without using any built-in functions.
    The function should return a reversed list.
    Input l is a list that may contain any type of data.
    """
    if len(l) == 0:
        return l
    left = 0
    right = len(l) - 1
    while left < right:
        temp = l[right]
        l[right] = l[left]
        l[left] = temp
        left += 1
        right -= 1
    return l


pass

# test cases
print("------Reversing list starts------")
print(reverse_list([]))
print(reverse_list([1]))
print(reverse_list([1, 2]))
print(reverse_list([1, 2, 3, 4]))
print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list([1, 2, "test", 4, {"x": 12}]))
print("------Reversing list ends------")

SODUKU_ARR = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def solve_sudoku(matrix):
    """
    Write a program to solve a 9x9 Sudoku board.
    The board must be completed so that every row, column, and 3x3 section
    contains all digits from 1 to 9.
    Input: a 9x9 matrix representing the board.
    """
    for i in range(9):
        for j in range(9):
            if matrix[i][j] not in SODUKU_ARR:
                for num in range(1, 10):
                    if check(matrix, i, j, num):
                        matrix[i][j] = num
                        if solve_sudoku(matrix):
                            return True
                matrix[i][j] = 0
                return False
    return True


pass


def check(matrix, row, column, num):
    # Check whether there is any value in the row equal to the num
    for i in range(9):
        if matrix[row][i] == num:
            return False

    # Check whether there is any value in the column equal to the num
    for j in range(9):
        if matrix[j][column] == num:
            return False

    # Judge which grid the num is located in
    row_start = int(math.floor(row / 3)) * 3
    column_start = int(math.floor(column / 3)) * 3

    # Check whether there is any value in the 3*3-grid equal to the num
    for i in range(row_start, row_start + 3):
        for j in range(column_start, column_start + 3):
            if matrix[i][j] == num:
                return False
    return True


print("------sudoku starts------")
matrix = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
for row in matrix:
    print(row)
print("------changed------")
solve_sudoku(matrix)
for row in matrix:
    print(row)
print("------sudoku ends------")
