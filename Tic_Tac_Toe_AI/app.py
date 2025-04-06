import random
import time

board = [" " for _ in range(9)]


# Display the Board
def display():
    print("\n")
    for i in range(3):
        print(" | ".join(board[i * 3:(i + 1) * 3]))
        if i < 2:
            print("-" * 9)
    print("\n")


# Check for a Winner
def check_winner(player: str) -> bool:
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)              # Diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False


# AI Move
def ai_o():
    while True:
        ram = random.randint(0, 8)
        if board[ram] == " ":
            board[ram] = "o"
            break


# Reset the Game
def reset_game():
    global board
    board = [" " for _ in range(9)]
    display()


# Main Game Loop
def main():
    print("\n\t\tWelcome to Tic-Tac-Toe!\n")
    display()
    
    player_name = "x"

    while True:
        try:
            # Player Move
            user_input = int(input(f"Player {player_name}, enter a position (1-9): ")) - 1

            if 0 <= user_input < 9 and board[user_input] == " ":
                board[user_input] = player_name
                display()

                # Check Player Win
                if check_winner(player_name):
                    print(f"🎉 Player {player_name} wins! 🎉")
                    user_permission = input("\nPlay Again? (Yes/No): ").lower()
                    if user_permission == "yes":
                        reset_game()
                        continue
                    else:
                        print("\nGoodbye!")
                        break


                #  AI Move
                time.sleep(1)
                print("AI is thinking...\n")
                ai_o()
                display()

                #  Check AI Win
                if check_winner("o"):
                    print("🤖 AI wins! Better luck next time!")
                    user_permission = input("\nPlay Again? (Yes/No): ")
                    if user_permission.lower() == "yes":
                        reset_game()
                        continue
                    else:
                        print("\nGoodbye!")
                        break
                    

            else:
                print("\n❌ Invalid move! Try again.")

        except ValueError:
            print("\n❌ Invalid input! Please enter a number between 1-9.")


if __name__ == "__main__":
    main()
