import time

def count(num:int):
    while num > 0:
        mins, secs = divmod(num, 60) #  num ko 60 se divide karke minutes aur seconds alag karega.
        timer = f"{mins:02d}:{secs:02d}" # 02d ka matlab hai 2 digit number. agar number single digit ho to leading zero add hoga.
        print(timer, end="\r")  # \r sy porani line remove ho jaye gi or new line print hoye gi
        time.sleep(1)
        num -= 1

    print("\n\nTime's up")


def main():
    print("\n\t\tWellcome to countdown timer")

    while True:
        user_input = input("\nEnter the countdown time in seconds: ")
        try:
            if user_input == "":
                print("\nPlease enter number")
            else:
                count(int(user_input))
        except ValueError as e:
            print("\nEnter only number")

        user_paly_again = input("\nDo you want to start another timer? (yes/no): ")

        if user_paly_again.lower() == "yes":
            pass
        else:
            print("\nGood By")
            break
        
if __name__ in "__main__":
    main()