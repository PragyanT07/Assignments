'''a program that defines a function that accepts a list of numbers
and prints the occurrence (frequency) of each unique number in that list.'''

# accepts a list of numbers and prints the occurrence of each unique number
def occurence(num):
    if not num: # if the list is empty
        print("The list is empty.")
        return
    
    for number in num:
        occurence = num.count(number)
        print(f"The number {number} is repeated {occurence} times in the list.")

if __name__ == "__main__":
    # Test1
    list1 = [100, 1, 3, 4, 3, 5, 7, 8, 100]
    print(f"Testing with list1: {list1}")
    occurence(list1)

    # Test2
    list2 = [1, 2, 1, 3, 2, 1]
    print(f"\nTesting with list2: {list2}")
    occurence(list2)

    # Test3
    list3 = []
    print(f"\nTesting with list3: {list3}")
    occurence(list3)