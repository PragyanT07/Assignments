'''a program that implements an employee management system; it uses an 'employee' class to represent 
employee details and functions to add new employees to an 'employees.csv' file and view all existing
employee records from the file. it includes comprehensive error handling.'''

import pandas as pd; 'import pandas for data handling and csv operations'
import os; 'import os for file system checks'

# represents an employee with various attributes
class Employee:
    # initializes a new employee object
    def __init__(self, empid, name, address, contact_number, spouse_name, number_of_child, salary):
        self.empid = empid
        self.name = name
        self.address = address
        self.contact_number = contact_number
        self.spouse_name = spouse_name
        self.number_of_child = number_of_child
        self.salary = salary

    # converts the employee object's attributes into a dictionary
    def to_dict(self):
        return {
            "empid": self.empid,
            "name": self.name,
            "address": self.address,
            "contact_number": self.contact_number,
            "spouse_name": self.spouse_name,
            "number_of_child": self.number_of_child,
            "salary": self.salary
        }

def add_employee_to_csv(employee, filename="employees.csv"):
    df_new = pd.DataFrame([employee.to_dict()]) # create dataframe for new employee

    try:
        if os.path.exists(filename):
            # if file exists, read it and concatenate new data
            df_existing = pd.read_csv(filename)
            df_combined = pd.concat([df_existing, df_new], ignore_index=True)
        else:
            # if file doesn't exist, new data is the combined data
            df_combined = df_new
        
        df_combined.to_csv(filename, index=False) # write (or overwrite) the csv file
        print(f"\nemployee '{employee.name}' added successfully to {filename}")

    except Exception as e:
        print(f"\nan error occurred while writing to the file: {e}") # catch file write errors

# reads and displays all employee records from the specified csv file
def view_employees(filename="employees.csv"):
    try:
        df = pd.read_csv(filename) # read csv into dataframe
        if df.empty:
            print("\nthe employee list is empty.") # message for empty file
        else:
            print("\n--- list of employees ---")
            for index, row in df.iterrows(): # iterate through dataframe rows
                print(f"\n--- employee id: {row['empid']} ---") # print employee id as header
                print(f"  name            : {row['name']}")
                print(f"  address         : {row['address']}")
                print(f"  contact number  : {row['contact_number']}")
                print(f"  spouse's name   : {row['spouse_name']}")
                print(f"  number of child : {row['number_of_child']}")
                print(f"  salary          : {row['salary']:.2f}") # format salary to 2 decimal places
                print("-----------------------------")
            
    except FileNotFoundError:
        print(f"\nthe file '{filename}' does not exist yet. please add an employee first.") # error if file not found
    except Exception as e:
        print(f"\nan error occurred while reading the file: {e}") # catch other file read errors

# main function for the employee management system
def main():
    while True: # main program loop
        print("\n--- employee management menu ---")
        print("1. add a new employee")
        print("2. view all employees")
        print("3. exit")
        
        choice = input("enter your choice (1-3): ")

        if choice == '1':
            print("\nplease enter the details for the new employee:")
            try:
                # get employee details from user with type conversion
                emp_id = input("enter employee id: ") # keep as string for flexibility, or int if strictly numeric
                emp_name = input("enter name: ")
                emp_address = input("enter address: ")
                emp_contact = input("enter contact number: ")
                emp_spouse = input("enter spouse's name: ")
                emp_children = int(input("enter number of children: ")) # convert to int
                emp_salary = float(input("enter salary: ")) # convert to float

                # create employee object
                new_employee = Employee(emp_id, emp_name, emp_address, emp_contact, emp_spouse, emp_children, emp_salary)
                
                add_employee_to_csv(new_employee) # add employee to csv

            except ValueError:
                print("\ninvalid input. please ensure employee id, number of children, and salary are numbers.") # specific value error for numeric inputs
            except Exception as e:
                print(f"\nan unexpected error occurred: {e}") # catch other errors during input

        elif choice == '2':
            view_employees() # view all employees

        elif choice == '3':
            print("\nexiting program. goodbye.")
            break # exit main loop
            
        else:
            print("\ninvalid choice. please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()
