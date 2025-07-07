'''A program that reads and displays student data from a "students.csv" file,
including fields like name, ID, course, level, and section.'''

import pandas as pd; 'importing to handle csv file'

def student_data(filename="students.csv"):
    try:
        # read CSV into a pandas DataFrame
        df = pd.read_csv(filename, header=0) 

        print("--- Student Details ---")

        # Iterate over DataFrame rows
        for index, row in df.iterrows():
            # Access data by column name
            name = row['name']
            student_id = row['id']
            course = row['course']
            level = row['level']
            section = row['section']

            # Print formatted details for each student
            print("\n-------------------------")
            print(f"  Name:    {name}")
            print(f"  ID:      {student_id}")
            print(f"  Course:  {course}")
            print(f"  Level:   {level}")
            print(f"  Section: {section}")
        
        print("\n-------------------------") # End of display

    except FileNotFoundError:
        # Handle case where CSV file doesn't exist
        print(f"Error: The file '{filename}' was not found. Please ensure 'students.csv' is in the same directory.")

    except KeyError as ke:
        # Handle case where expected columns are missing
        print(f"Error: Missing expected column in '{filename}'. Please check CSV headers. Details: {ke}")

    except pd.errors.EmptyDataError:
        # Handle case where CSV file is empty
        print(f"Error: The file '{filename}' is empty. No data to read.")

    except Exception as e:
        # Catch any other unexpected errors
        print(f"An unexpected error occurred: {e}")

# Running the code
if __name__ == "__main__":
    student_data()
