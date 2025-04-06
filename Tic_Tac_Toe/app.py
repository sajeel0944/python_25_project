board = [" " for _ in range(9)]


def display():
    print("\n")
    for i in range(3):
        print(" | ".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("-" * 9)
    print("\n")


# Function to check for a winner
def check_winner(player:str) -> bool:
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)              # Diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False


def main():
    print("\n\t\tWelcome to Tic-Tac-Toe!\n")
    player_name : str = "x"

    while True:
        try:
            user_input = int(input(f"Player {player_name}, enter a position (1-9): "))

            if user_input <=9 :

                if player_name == "x":
                    board[user_input -1] = player_name
                    display()
                    player_name = "o"
                elif player_name == "o":
                    board[user_input -1] = player_name
                    display()
                    player_name = "x"

                if check_winner(player_name):
                    print(f"Player {player_name} wins! ")
                    
                    user_permission : str = input("\nPlat Again This Game Yes/No : ")
                    if user_permission.lower() == "yes":
                        pass
                    else:
                        print("\nGood By")
                        break
            else:
                print("\nInvalid move! Try again.")
        except ValueError as e :
            print("\nInvalid input! Please enter a number between 1-9.")
        


if __name__ in "__main__":
    main()