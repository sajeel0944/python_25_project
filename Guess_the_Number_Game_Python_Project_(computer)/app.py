import random

def generate(num:int):
    random_number_2 = random.randint(1,12)

    if num == random_number_2:
        print("\nyou correct guess number")
    else:
        print("\nyou guess wrong number")

def main():
    while True:
        manage = input("Guess Number Yes/NO : ")

        if manage.lower() == "yes":
            random_number = random.randint(1,12)
            generate(random_number)
        else:
            print("Good By")
            break


if __name__ in "__main__":
    main()