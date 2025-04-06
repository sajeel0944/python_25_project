import random

arr : list[str] = ["Rock", "Paper", "Scissors"]


def guess(user_select : str):
    random_choice = random.choice(arr)
    print(f"You : {user_select} , player : {random_choice}")

    if random_choice == user_select:
        print("\n🎉 It's a tie!")
    elif (user_select == "Rock" and random_choice == "Scissors") or \
         (user_select == "Paper" and random_choice == "Rock") or \
         (user_select == "Scissors" and random_choice == "Paper"):
        print("\n✅ You win!")
    else:
        print("\n❌ You lose!")


def main():
    while True:
        manage = input("\nPlay Game? (Yes/No): ")

        if manage.lower() == "yes":
            try:
                count : int = 1
                print("\nChoose an option:")
                for i in arr:
                    print(f"{count}. {i}")
                    count += 1
                user_input = input("\nSelect option (1-3):")
                if user_input == "":
                    print("\nPlase select option")
                else:
                    convert_number : int = int(user_input) 
                    get_value = arr[convert_number -1]
                    guess(get_value)
            except ValueError as e:
                print("\nEnter olny number")
        else:
            print("Good by")
            break


if __name__ in "__main__":
    main()