def mad_libs(name:str, place:str, adjective:str, verb:str):

    story = f"\nOne day, {name} went to {place}. There, they saw a {adjective} animal that was {verb}!"
    print("\nHere is your funny story: 🤣\n")
    print(story)
   

def main():
    try:

        print("\n\t\tWelcome to the Mad Libs Game! 🎭\n")

        name = input("Enter a name: ")
        place = input("Enter a place: ")
        adjective = input("Enter an adjective: ")
        verb = input("Enter a verb: ")

        if name == "" and place == "" and adjective == "" and verb == "" :
            print("\nplease enter all optional")
        else:
            mad_libs(name, place, adjective, verb)

    except Exception as e:
        print("Somethink was wrong")


if __name__ in "__main__":
    main()