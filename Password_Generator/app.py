import string
import random


def generator(password_length:int)-> str:
    if password_length > 4 :
        uppercase = random.choice(string.ascii_uppercase)
        lowercase = random.choice(string.ascii_lowercase)
        digit = random.choice(string.digits)
        special_char = random.choice(string.punctuation)
        remaining_chars = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=password_length-4))

        password = list(uppercase + lowercase + digit + special_char + remaining_chars)
        random.shuffle(password)
        
        return ''.join(password)
    
    else:
        print("You put number greater than 4")


def main():
    print("\n\t\tWellcome To Password Generator")
    try:
        user_input = input("\nEnter the password length : ")

        if user_input == "":
            print("\nPlease Enter Number")
        else :
            save = generator(int(user_input))
            print(f"Password : {save}")
    except Exception as e:
        print("\nPlease Enter Only Number")


if __name__ in "__main__":
    main()