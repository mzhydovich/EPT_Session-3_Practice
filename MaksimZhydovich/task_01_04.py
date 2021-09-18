
# Sort a dictionary by key.

def main():
    print("Hello!")
    n = int(input("Enter size of unsorted dictionary: "))

    dictionary = {}
    print("Enter unsorted dictionary: ")
    for _ in range(n):
        data = input().split(" ")
        dictionary[data[0]] = data[1]

    sorted_keys = sorted(dictionary.keys())
    for key in sorted_keys:
        # create copy of dictionary[key]
        tmp = dictionary[key]
        # delete old pair
        del dictionary[key]
        # create new pair
        dictionary[key] = tmp

    print(f"Sorted dictionary: {dictionary}")


if __name__ == "__main__":
    main()
