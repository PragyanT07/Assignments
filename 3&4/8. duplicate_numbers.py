'''a program that defines a function that accepts a list of numbers as input and
processes the list to remove any duplicate values and returns a new list
containing only the unique elements. '''

# accepts a list of numbers and returns a new list with duplicate values removed.
def duplicate_numbers(num):
    new_num = [] # an empty list to store unique elements

    for i in range(len(num)):
        # if the number is not already in our unique_numbers list, add it
        if num[i] not in new_num:
            new_num.append(num[i])
    return new_num

# Main execution block to test the function
if __name__ == "__main__":
    # Test Case 1
    test_list1 = [1, 2, 4, 6, 99, 5, 7, 1, 5, 8, 90]
    print(f"\nOriginal List 1: {test_list1}")
    result_list1 = duplicate_numbers(test_list1)
    print(f"List after removing duplicates: {result_list1}")

    # Test Case 2
    test_list2 = [10, 20, 30, 40, 50]
    print(f"\nOriginal List 2: {test_list2}")
    result_list2 = duplicate_numbers(test_list2)
    print(f"List after removing duplicates: {result_list2}")

    # Test Case 3
    test_list3 = [7, 7, 7, 7, 7]
    print(f"\nOriginal List 3: {test_list3}")
    result_list3 = duplicate_numbers(test_list3)
    print(f"List after removing duplicates: {result_list3}")

    # Test Case 4
    test_list4 = []
    print(f"\nOriginal List 4: {test_list4}")
    result_list4 = duplicate_numbers(test_list4)
    print(f"List after removing duplicates: {result_list4}")