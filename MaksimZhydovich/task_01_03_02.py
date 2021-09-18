
# Asks the user for a number and then prints out a list of all the divisors of that number

from math import sqrt


def main():
    print("Hello!")
    num = int(input("Enter the number: "))

    divisors = []
    for i in range(1, int(sqrt(num)) + 1):
        if num % i == 0:
            divisors.append(i)
            divisors.append(int(num / i))

    divisors.sort()
    print(f"Divisors of your number are: {divisors}")


if __name__ == "__main__":
    main()
