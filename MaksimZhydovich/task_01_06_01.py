
# Convert a given tuple of positive integers into an integer

def main():
    input_tuple = (1, 2, 3, 4)

    result = 0
    for el in input_tuple:
        result *= 10
        result += el

    print(f"Result: {result}")


if __name__ == "__main__":
    main()
