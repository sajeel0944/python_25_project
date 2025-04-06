import random

arr : list[str] = []


def random_select() -> str:
    countries = ["pakistan", "india", "canada", "brazil", "germany", "argentina", "italy", "japan", "norway", "switzerland"]
    select = random.choice(countries)
    return select


def manage_value() -> str:

    save_word = random_select()
    find_legth = len(save_word)
    
    for i in range(find_legth):
        arr.append("_")
    
    return(save_word)


def main():
    print("\t\t\nWelcome to Hangman!\n")

    save_word = manage_value()
    # print(save_word)

    count : int = 6
    try:
        while count > 0:
            print(f"\nYou have {count} attempts left.")
            for display in arr:
                print(f"{display}" , end=" ")

            user_input = input("\n\nEnter a letter:  ")
            find_word = save_word.find(user_input)
            # print(find_word)
            if find_word != -1:
                arr[find_word] = user_input
            else:
                count -= 1

            if "_" not in arr: 
                print("\nCongratulations! You guessed the word:", save_word)
                break

        print("\nTime is over! The word was:", save_word)
    except Exception as e :
        print("\nSomethink was wrong")


if __name__ in "__main__":
    main()