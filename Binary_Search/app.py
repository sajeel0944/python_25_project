
def search(arr:list[int], find_num:int) -> int:
    left = 0
    right = len(arr) - 1

    while left <= right:
        middle = (left + right) // 2
        
        if arr[middle] == find_num:
            return middle 
        elif arr[middle] > find_num:
            right = middle - 1
        else:
            left = middle + 1
    
    return -1  


def main():
    arr : list[int] = []
    try:
        while True:
            user_value = input("\nEnter sorted numbers separated by space: ")
            if user_value == "":
                break
            else:
                arr.append(int(user_value))
                continue    
        
        user_find : int = int(input("\nEnter the number to search: "))

        result = search(arr, user_find)

        if result == -1:
            print(f"\nElement {user_find} not found")
        else:
            print(f"\nElement {user_find} found at index {result}")

    except ValueError as e:
        print("\nEnter Only Number")


if __name__ in "__main__":
    main()