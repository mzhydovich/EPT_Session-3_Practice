
# Makes a pretty print of a part of the multiplication table

def main():
    a, b, c, d = input("Enter borders of the table: ").split()

    # print start indent
    print(f"{'':<7}", end="")

    # print column numbers
    for column in range(int(c), int(d) + 1):
        print(f"{column:<7}", end="")
    print()

    for row in range(int(a), int(b) + 1):
        # print row number
        print(f"{row:<7}", end="")

        for column in range(int(c), int(d) + 1):
            # print multiplication
            print(f"{row * column:<7}", end="")
        print()


if __name__ == "__main__":
    main()
