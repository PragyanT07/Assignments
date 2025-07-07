'''a program implements a basic library book management system; it uses object-oriented programming (oop)
to manage books and their status; functionalities include adding, issuing, returning, searching, and viewing books.'''

import pandas as pd; 'import pandas for data manipulation and csv file handling'
import os; 'import os for file system operations like checking file existence'

# utility function to clear the console screen
def clearScreen():
    # clears the console based on the operating system
    os.system('cls' if os.name == 'nt' else 'clear')

class Book:
    # represents a single book in the library.
    def __init__(self, isbn, title, author, is_issued=False):
        # initializes a new book object.
        self.isbn = isbn
        self.title = title
        self.author = author
        self.is_issued = is_issued # boolean: true if issued, false if available

    def to_dict(self):
        # converts the book object's attributes into a dictionary.
        # useful for creating pandas dataframes.
        return {
            "isbn": self.isbn,
            "title": self.title,
            "author": self.author,
            "is_issued": self.is_issued
        }

class Library:
    # manages the collection of books and handles file operations.
    def __init__(self, filename="books.csv"):
        # initializes the library with a csv filename and loads existing books.
        self.filename = filename
        self.books_df = self.load_books() # dataframe to hold all book records

    def load_books(self):
        # loads book data from the csv file into a pandas dataframe.
        # creates an empty dataframe if the file doesn't exist or on error.
        try:
            if os.path.exists(self.filename):
                # read existing csv, ensuring isbn is read as string
                return pd.read_csv(self.filename, dtype={'isbn': str})
            else:
                # return empty dataframe with defined columns if file not found
                return pd.DataFrame(columns=["isbn", "title", "author", "is_issued"])
        except Exception as e:
            # catches errors during file loading (e.g., corrupted csv)
            print(f"an error occurred while loading books: {e}")
            # return empty dataframe to prevent further errors
            return pd.DataFrame(columns=["isbn", "title", "author", "is_issued"])

    def save_books(self):
        # saves the current state of the books dataframe to the csv file.
        try:
            # write dataframe to csv, without index column
            self.books_df.to_csv(self.filename, index=False)
        except Exception as e:
            # catches errors during file saving
            print(f"an error occurred while saving books: {e}")

    def add_book(self):
        # prompts user for book details and adds a new book to the library.
        try:
            isbn = input("enter isbn: ").strip()
            # check if a book with this isbn already exists
            if not self.books_df[self.books_df['isbn'] == isbn].empty:
                print("\nerror: a book with this isbn already exists.")
                return # exit if isbn is not unique

            title = input("enter title: ").strip()
            author = input("enter author: ").strip()
            
            new_book = Book(isbn, title, author) # create new book object
            
            # create a dataframe for the new book and concatenate with existing books
            new_book_df = pd.DataFrame([new_book.to_dict()])
            self.books_df = pd.concat([self.books_df, new_book_df], ignore_index=True)
            
            self.save_books() # save changes to file
            print(f"\nbook '{title}' added successfully.")
        except Exception as e:
            # catches errors during book addition
            print(f"\nan error occurred while adding the book: {e}")

    def issue_book(self):
        # prompts user for isbn and marks the book as issued.
        try:
            isbn = input("enter the isbn of the book to issue: ").strip()
            # find the index of the book by isbn
            book_indices = self.books_df.index[self.books_df['isbn'] == isbn].tolist()

            if not book_indices: # if no book found with this isbn
                print("\nerror: no book found with this isbn.")
                return

            # get the actual index (assuming unique isbn, take first match)
            book_idx = book_indices[0] 

            if self.books_df.loc[book_idx, 'is_issued']: # check if already issued
                print("\nerror: this book is already issued.")
            else:
                self.books_df.loc[book_idx, 'is_issued'] = True # set to issued
                self.save_books() # save changes
                title = self.books_df.loc[book_idx, 'title']
                print(f"\nbook '{title}' has been issued successfully.")
        except Exception as e:
            # catches errors during book issuing
            print(f"\nan error occurred: {e}")

    def return_book(self):
        # prompts user for isbn and marks the book as available.
        try:
            isbn = input("enter the isbn of the book to return: ").strip()
            # find the index of the book by isbn
            book_indices = self.books_df.index[self.books_df['isbn'] == isbn].tolist()

            if not book_indices: # if no book found with this isbn
                print("\nerror: no book found with this isbn.")
                return

            # get the actual index
            book_idx = book_indices[0] 

            if not self.books_df.loc[book_idx, 'is_issued']: # check if not issued
                print("\nerror: this book was not issued.")
            else:
                self.books_df.loc[book_idx, 'is_issued'] = False # set to available
                self.save_books() # save changes
                title = self.books_df.loc[book_idx, 'title']
                print(f"\nbook '{title}' has been returned successfully.")
        except Exception as e:
            # catches errors during book return
            print(f"\nan error occurred: {e}")

    def search_book(self):
        # prompts for a search term (title or author) and displays matching books.
        if self.books_df.empty:
            print("\nthe library is empty. no books to search.")
            return # exit if no books in library
            
        search_term = input("enter title or author to search: ").strip().lower() # get search term, convert to lowercase
        
        # search in title or author columns (case-insensitive, partial match)
        results = self.books_df[
            self.books_df['title'].astype(str).str.lower().str.contains(search_term, na=False) |
            self.books_df['author'].astype(str).str.lower().str.contains(search_term, na=False)
        ]

        if results.empty: # if no matching books found
            print("\nno books found matching your search term.")
        else:
            print("\n--- search results ---")
            for index, row in results.iterrows(): # iterate and print search results
                status = "issued" if row['is_issued'] else "available" # get status string
                print(f"  title: {row['title']}, author: {row['author']}, isbn: {row['isbn']}, status: {status}")
            print("----------------------")

    def view_all_books(self):
        # displays details of all books currently in the library.
        if self.books_df.empty:
            print("\nthe library is empty. please add a book first.")
            return # exit if no books

        print("\n--- all books in library ---")
        for index, row in self.books_df.iterrows(): # iterate and print all books
            status = "issued" if row['is_issued'] else "available" # get status string
            # formatted print for alignment
            print(f"  title: {row['title']:<30} | author: {row['author']:<20} | isbn: {row['isbn']:<15} | status: {status}")
        print("----------------------------")

def main():
    # main function to run the library management system.
    # provides a menu-driven interface for all library functionalities.
    library = Library() # create a library instance
    while True: # main program loop
        clearScreen() # clear screen for clean menu display
        print("--- library management system ---")
        print("1. add a new book")
        print("2. issue a book")
        print("3. return a book")
        print("4. search for a book")
        print("5. view all books")
        print("6. exit")
        
        choice = input("enter your choice (1-6): ").strip() # get user choice
        clearScreen() # clear screen after choice

        if choice == '1':
            library.add_book() # call add book method
        elif choice == '2':
            library.issue_book() # call issue book method
        elif choice == '3':
            library.return_book() # call return book method
        elif choice == '4':
            library.search_book() # call search book method
        elif choice == '5':
            library.view_all_books() # call view all books method
        elif choice == '6':
            print("\nexiting the system. goodbye.")
            break # exit main loop
        else:
            print("\ninvalid choice. please enter a number between 1 and 6.")

        input("press enter to return back to the menu") # pause for user to read output

if __name__ == "__main__":
    main()
