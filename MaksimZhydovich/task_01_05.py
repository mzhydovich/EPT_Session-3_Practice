
# Print all unique values of all dictionaries in a list

def main():
    arr = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
           {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]

    unique_values = set()
    for dictionary in arr:
        unique_values.update(dictionary.values())

    print(f"Unique values: {unique_values}")


if __name__ == "__main__":
    main()
