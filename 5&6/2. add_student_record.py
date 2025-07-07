'''a program that facilitates adding new student records to a CSV file named "students.csv";
it prompts the user to input details such as name, ID, course, level, and section;the new record
is then appended to the end of the existing file, ensuring data persistence. '''


import pandas as pd; 'importing to handle csv files'
import os; 'importing to check the file status'

def add_student_record(filename):
    try:
        # check if the file exists before proceeding
        if not os.path.exists(filename):
            print(f"Error: The file '{filename}' was not found.")
            print("This program only appends records to an existing file. Please create it first.")
            return # exit if file doesn't exist

        print("--- Enter New Student Details ---")
        
        # get input for each student detail
        name = input("Enter the student's name: ")
        student_id = input("Enter the student's ID: ")
        course = input("Enter the student's course: ")
        level = input("Enter the student's level: ")
        section = input("Enter the student's section: ")

        # create a dictionary for the new student's data.
        new_student_data = {
            'name': [name],
            'id': [student_id],
            'course': [course],
            'level': [level],
            'section': [section]
        }

        # create a pandas DataFrame from the new student's data
        new_df_row = pd.DataFrame(new_student_data)

        # append the new DataFrame row to the CSV file
        new_df_row.to_csv(filename, mode='a', header=False, index=False)

        print(f"\nSuccess! Student '{name}' has been added to {filename}.")

    except Exception as e:
        # catch any unexpected errors during the process
        print(f"An error occurred: {e}")

# Running the code
if __name__ == "__main__":
    add_student_record("students.csv")
