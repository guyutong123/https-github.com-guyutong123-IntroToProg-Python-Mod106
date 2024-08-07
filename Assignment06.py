# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   yu tong Gu,8/6/24, Created Script
# ------------------------------------------------------------------------------------------ #
"""
Description:
    This script implements a Course Registration Program. It allows the user to
    register students for courses, display current data, save data to a file,
    and exit the program.
"""

import json

# Constants
MENU: str = """
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course
    2. Show current data  
    3. Save data to a file
    4. Exit the program
-----------------------------------------
"""
FILE_NAME: str = "Enrollments.json"

# Variables
menu_choice: str = ""
students: list = []


#The program includes functions with the following names and parameters:
#ooutput_error_messages(message: str, error: Exception = None)
#ooutput_menu(menu: str)
#oinput_menu_choice()
#ooutput_student_courses(student_data: list)
##oinput_student_data(student_data: list)
#oread_data_from_file(file_name: str, student_data: list):
#owrite_data_to_file(file_name: str, student_data: list):

class FileProcessor:
    """Performs File Processing Tasks"""

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """Reads data from a file into a list of dictionary rows"""
        try:
            with open(file_name, 'r') as file:
                student_data.extend(json.load(file))
        except FileNotFoundError as e:
            IO.output_error_messages("File not found.", e)
        except json.JSONDecodeError as e:
            IO.output_error_messages("File is empty or corrupted.", e)

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """Writes data from a list of dictionary rows to a file"""
        try:
            with open(file_name, 'w') as file:
                json.dump(student_data, file)
        except Exception as e:
            IO.output_error_messages("Failed to write to file.", e)


class IO:
    """Performs Input and Output Tasks"""

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """Outputs error messages to the user"""
        if error:
            print(f"Error: {message} - {error}")
        else:
            print(f"Error: {message}")

    @staticmethod
    def output_menu(menu: str):
        """Displays the menu to the user"""
        print(menu)

    @staticmethod
    def input_menu_choice():
        """Gets the menu choice from the user"""
        return input("Enter your choice: ").strip()

    @staticmethod
    def output_student_courses(student_data: list):
        """Displays the current student course data"""
        for students in student_data:
            student = {'student_first_name': ' ', 'student_last_name': ' ', 'course_name': ' '}
            student['student_first_name'] = students['FirstName']
            student['student_last_name'] = students['LastName']
            student['course_name'] = students['CourseName']
            print(f"Student: {student['student_first_name']} {student['student_last_name']}, Course: {student['course_name']}")

    @staticmethod
    def input_student_data(student_data: list):
        """Gets student data from the user and adds it to the student data list"""
        try:
            student_first_name = input("What is the student's first name? ").strip()
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")

            student_last_name = input("What is the student's last name? ").strip()
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")

            course_name = input("Enter course name: ").strip()

            if not student_first_name or not student_last_name or not course_name:
                raise ValueError("All fields must be filled out.")

            student_data.append({
                "FirstName": student_first_name,
                "LastName": student_last_name,
                "CourseName": course_name
            })
        except ValueError as e:
            IO.output_error_messages("Invalid input.", e)


def main():
    """Main program logic"""
    FileProcessor.read_data_from_file(FILE_NAME, students)

    while True:
        IO.output_menu(MENU)
        menu_choice = IO.input_menu_choice()

        if menu_choice == "1":
            IO.input_student_data(students)
        elif menu_choice == "2":
            IO.output_student_courses(students)
        elif menu_choice == "3":
            FileProcessor.write_data_to_file(FILE_NAME, students)
        elif menu_choice == "4":
            break
        else:
            IO.output_error_messages("Invalid menu choice. Please try again.")


if __name__ == "__main__":
    main()
