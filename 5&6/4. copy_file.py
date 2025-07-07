'''a program that copies the content from one file to another with error handling
by prompting the user for both the input (source) and output (destination) file names.'''

import os; 'importing for file operations'

def copy_file():
    input_file = input("enter the name of the file to read from: ").strip() # get source file name
    output_file = input("enter the name of the file to write to: ").strip() # get destination file name

    try:
        # check if the input file exists
        if not os.path.exists(input_file):
            print(f"error: the file '{input_file}' does not exist.") # error if source file not found
            return # exit function
        
        # check if the output file already exists
        if os.path.exists(output_file):
            print(f"error: the file '{output_file}' already exists. choose a different name.") # error if destination file exists
            return # exit function
        
        # open input file in read mode and output file in write mode
        with open(input_file, 'r') as filein:
            content = filein.read() # read all content from source file
        
        with open(output_file, 'w') as fileout:
            fileout.write(content) # write content to destination file
        
        print(f"file '{input_file}' has been copied to '{output_file}'.") # success message

    except IOError as io_error:
        # handle specific i/o errors (e.g., permissions, invalid path)
        print(f"an i/o error occurred: {io_error}")
    except Exception as e:
        # catch any other unexpected errors
        print(f"an unexpected error occurred: {e}")

# Running the code
if __name__ == "__main__":
    copy_file()
