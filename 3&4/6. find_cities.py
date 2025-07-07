''' a program that searches for a city in a list, returns index or 'not found' message.'''

def search_cities(cities, city):
    if city.lower() in cities:
        return cities.index(city.lower())
    else:
        # if the city is not found, return a proper message
        return f"{city} is not present in the list."
    
# Main execution block
if __name__ == "__main__":
    my_cities = ["London", "Paris", "New York", "Tokyo", "London", "Sydney"]
    for i in range(len(my_cities)):
        my_cities[i] = my_cities[i].lower()
    print(f"\nSearching in list: {my_cities}")

    # Test Case 1
    search_term1 = "London"
    result1 = search_cities(my_cities, search_term1)
    if isinstance(result1, int):
        print(f"'{search_term1}' found at index: {result1}")
    else:
        print(result1)

    # Test Case 2
    search_term2 = "Berlin"
    result2 = search_cities(my_cities, search_term2)
    if isinstance(result2, int):
        print(f"'{search_term2}' found at index: {result2}")
    else:
        print(result2)

    # Test Case 3
    search_term3 = "new york"
    result3 = search_cities(my_cities, search_term3)
    if isinstance(result3, int):
        print(f"'{search_term3}' found at index: {result3}")
    else:
        print(result3)

    # Test Case 4
    empty_cities = []
    search_term4 = "Anywhere"
    result4 = search_cities(empty_cities, search_term4)
    if isinstance(result4, int):
        print(f"'{search_term4}' found at index: {result4}")
    else:
        print(result4)

    

