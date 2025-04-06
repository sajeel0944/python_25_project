import random

class Minesweeper:
    def __init__(self, size, num_mines):
        self.size = size  # size of the board
        self.num_mines = num_mines  # number of mines
        self.board = self.create_board()  # the game board
        self.visible_board = [[' ' for _ in range(size)] for _ in range(size)]  # visible board with hidden cells
        self.game_over = False  # to check if the game is over
        self.revealed_cells = 0  # number of revealed cells

    def create_board(self):
        board = [[' ' for _ in range(self.size)] for _ in range(self.size)]
        
        mines_placed = 0
        while mines_placed < self.num_mines:
            row = random.randint(0, self.size - 1)
            col = random.randint(0, self.size - 1)
            if board[row][col] != 'X':  # 'X' represents a mine
                board[row][col] = 'X'
                mines_placed += 1
        
        for row in range(self.size):
            for col in range(self.size):
                if board[row][col] == 'X':
                    continue  # Skip mines
                mine_count = self.count_adjacent_mines(board, row, col)
                if mine_count > 0:
                    board[row][col] = str(mine_count)
        
        return board

    def count_adjacent_mines(self, board, row, col):
        # Check the 8 adjacent cells around (row, col)
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        count = 0
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < self.size and 0 <= c < self.size and board[r][c] == 'X':
                count += 1
        return count

    def display(self):
        print("\n".join([' '.join(row) for row in self.visible_board]))
    
    def reveal(self, row, col):
        if self.visible_board[row][col] != ' ':
            return  # Already revealed
        
        if self.board[row][col] == 'X':  # Mine hit
            self.game_over = True
            self.visible_board[row][col] = 'X'
            return
        
        self.visible_board[row][col] = self.board[row][col]
        self.revealed_cells += 1
        
        if self.board[row][col] == ' ':
            self.reveal_adjacent_cells(row, col)

    def reveal_adjacent_cells(self, row, col):
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < self.size and 0 <= c < self.size:
                self.reveal(r, c)

    def check_win(self):
        return self.revealed_cells == (self.size * self.size - self.num_mines)

    def play(self):
        print("Welcome to Minesweeper!")
        
        while not self.game_over:
            self.display()
            row = int(input("Enter row (0-{}): ".format(self.size - 1)))
            col = int(input("Enter column (0-{}): ".format(self.size - 1)))

            if not (0 <= row < self.size and 0 <= col < self.size):
                print("Invalid move, try again.")
                continue
            
            self.reveal(row, col)
            
            if self.game_over:
                self.display()
                print("Game Over! You hit a mine.")
                break
            
            if self.check_win():
                self.display()
                print("Congratulations! You won.")
                break


game = Minesweeper(size=5, num_mines=5)
game.play()




