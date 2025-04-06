import random

def guess(num : int):
    random_number = random.randint(1,12)

    if random_number == num:
        print("\nYou guess corrrect number")
    else:
        print("\nYou guess wrong number")

def main():
    while True:
        manage = input("\nGuess Number Yes/NO : ")

        if manage.lower() == "yes":
            try:
                user_input = input("\nEnter your number : ")
                if user_input == "":
                    print("\nplase enter number")
                else:
                    convert_number : int = int(user_input) 
                    guess(convert_number)
            except ValueError as e:
                print("\nEnter olny number")
        else:
            print("Good by")
            break


if __name__ in "__main__":
    main()