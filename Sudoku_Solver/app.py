import random 


def display(board:list[list[int]]):
    for row in board:
        print(" ".join(str(num) for num in row))
        
    
def solve_sudoku(board:list[list[int]]):
    for i in range(9):
        for col in range(9):
            if board[i][col] == 0:
                ram = random.randint(1, 9) 
                board[i][col] = ram

    for row in board:
        print(" ".join(str(num) for num in row))


def main():

    board : list[list[int]] = [
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

    print("\nOriginal Sudoku Board\n")
    display(board)

    print("\nRandomly Filled Sudoku Board\n")
    solve_sudoku(board)

    

if __name__ in "__main__":
    main()
