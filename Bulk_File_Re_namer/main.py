import os

def main():
    i = 0
    path = "C:/Users/pc/Pictures/sir zain/"

    for file_name in os.listdir(path):
        my_dest = "img" + str(i) + ".png"
        my_source = path + file_name
        my_dest = path + my_dest
        os.rename(my_source, my_dest)
        i += 1

        print(f"old name is {file_name} new name is {my_dest.replace("C:/Users/pc/Pictures/sir zain/", "")}")

    print("\nsuccessfully")

if __name__ in "__main__":
    main()