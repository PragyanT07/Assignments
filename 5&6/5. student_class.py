'''a program that defines a 'student' class with attributes like id, name, address, admission year, 
level, and section; it then instantiates a student object using user input and displays its details.'''

# represents a student with key attributes
class Student():
    # initializes a new student object with provided details
    def __init__(self, id, name, address, admission_year, level, section):
        self.id = id
        self.name = name
        self.address = address
        self.admission_year = admission_year
        self.level = level
        self.section = section

    # returns a formatted string of student details for printing.
    def __str__(self):
        return (f"id: {self.id}\n"
                f"name: {self.name}\n"
                f"address: {self.address}\n"
                f"admission year: {self.admission_year}\n"
                f"level: {self.level}\n"
                f"section: {self.section}")
    
# main execution block
if __name__ == "__main__":
    print("--- student details input ---")
    print("please enter the student's details:")
    
    try:
        # get input for each student attribute
        student_id = int(input("enter student id: "))
        student_name = input("enter name: ")
        student_address = input("enter address: ")
        student_admission_year = int(input("enter admission year: "))
        student_level = input("enter level: ")
        student_section = input("enter section: ")

        # create student object
        student1 = Student(student_id, student_name, student_address, 
                           student_admission_year, student_level, student_section)

        # display student details
        print("\nstudent details:")
        print(student1)

    except ValueError:
        # handle non-numeric input error
        print("\ninvalid input. please make sure to enter numbers for id and year.")
        
    except Exception as e:
        # catch any other unexpected errors
        print(f"\nan error occurred: {e}")
