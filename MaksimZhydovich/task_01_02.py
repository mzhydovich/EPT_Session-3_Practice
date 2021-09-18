
# Count the number of characters in a string ignoring case of letters

def main():
    print("Hello!")
    user_str = input("Enter the string: ").lower()

    characters = {}
    for ch in user_str:
        if ch in characters.keys():
            characters[ch] += 1
        else:
            characters[ch] = 1

    print(f"Number of characters in your string: {characters}")


if __name__ == "__main__":
    main()
