
# Calculate the length of a string without using the `len` function

def main():
    print("Hello!")
    user_str = input("Enter the string: ")

    len_of_user_str = 0
    for _ in user_str:
        len_of_user_str += 1

    print(f"The length of your string is {len_of_user_str}")


if __name__ == "__main__":
    main()
