''' a program that accepts a list of names and returns the sorted order of names back.'''

def sort_names(names):
    # Filter out any empty strings that might result from extra commas or just spaces
    names = [name for name in names if name]

    if not names:
        print("No names entered.")

    else:
        sorted_names = sorted(names)
        return sorted_names

if __name__ == "__main__":
    # Test Case
    names1 = ["Zoe", "Anna", "Ben", "Chris"]
    print(f"\nOriginal List 1: {names1}")
    sorted_names1 = sort_names(names1)
    print(f"Sorted List 1: {sorted_names1}")

    # Test Case 2
    names2 = ["Alice", "bob", "Charlie", "David", "alice"]
    print(f"\nOriginal List 2: {names2}")
    sorted_names2 = sort_names(names2)
    print(f"Sorted List 2: {sorted_names2}")

    # Test Case 3
    names3 = []
    print(f"\nOriginal List 3: {names3}")
    sorted_names3 = sort_names(names3)
    print(f"Sorted List 3: {sorted_names3}")

    # Test Case 4
    names4 = ["Xavier"]
    print(f"\nOriginal List 4: {names4}")
    sorted_names4 = sort_names(names4)
    print(f"Sorted List 4: {sorted_names4}")
