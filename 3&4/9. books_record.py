'''a program that collects details (title, author, ISBN, cost) for five books, 
stores them in a list of dictionaries, and then displays the information.'''

def books_dict():
    books = []  
    print("--- Please enter the details for 5 books ---")

    for i in range(5):
        print(f"\n--- Book {i + 1} ---")
        
        # Get input from the user for each detail
        title = input("Enter the title: ")
        author = input("Enter the author: ")
        isbn = input("Enter the ISBN: ")

        # Loop to ensure a valid number is entered for the cost
        while True:
            try:
                cost = float(input("Enter the cost: $"))
                break  # Exit the loop if the input is a valid float
            except ValueError:
                print("Invalid input. Please enter a number for the cost.")

        # Create a dictionary for the current book's details
        book_info = {
            'title': title,
            'author': author,
            'isbn': isbn,
            'cost': f"{cost:.2f}"
        }
        
        # Add the book's dictionary to our list of books
        books.append(book_info)

    # --- Print the final list of books ---
    print("\n-----------------------------------------")
    print("Here are the details of the books you entered:")
    print("-----------------------------------------")

    for i in range(len(books)):
        print(f"\n--- Book {i + 1} ---")
        print(books[i])


# Run the program
if __name__ == "__main__":
    books_dict()
