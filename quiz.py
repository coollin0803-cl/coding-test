import random


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


def solve_sudoku(matrix):
    """
    Write a program to solve a 9x9 Sudoku board.
    The board must be completed so that every row, column, and 3x3 section
    contains all digits from 1 to 9.
    Input: a 9x9 matrix representing the board.
    """
    row = 0
    col = 0
    sudoku_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(9):
        for j in range(9):
            if matrix[i][j] not in sudoku_array:
                matrix[i][j] = random.choice(sudoku_array)


pass
