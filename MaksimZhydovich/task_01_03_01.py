
# Accepts a sequence of words as input and prints the unique words in sorted form

def main():
    print("Hello!")
    input_sequence = input("Enter the sequence: ").split(" ")

    result = sorted(set(input_sequence))
    print(f"Result: {result}")


if __name__ == "__main__":
    main()
