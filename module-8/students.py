"""
Author: Lane Dorscher
Date: 07/29/2026
Course: CSD-325
Assignment: 8.2
Description:
    Loads student records from a JSON file, provides methods for modifying
    the student collection, and saves the updated records back to JSON.
"""

import json
import sys


class Students:
    """Manages student records stored in a JSON file."""

    __RECORD_FORMAT = "{last_name}, {first_name} : ID = {student_id} , Email = {email}"

    def __init__(self, filename):
        """Initialize the student collection from the specified JSON file."""
        self.__filename = filename
        self.__students = []

        ## Exception handling for files since it could be invalid path or contain wrong data
        try:
            with open(filename, "r") as f:
                self.__students = json.load(f)
        except FileNotFoundError:
            print(f"Error: '{filename}' was not found.")
            sys.exit(1)
        except json.JSONDecodeError:
            print(f"Error: '{filename}' does not contain valid JSON.")
            sys.exit(1)

    def get_students(self):
        """Return the complete collection of student records."""
        return self.__students

    def get_filename(self):
        """Return the filename of the student collection."""
        return self.__filename

    def find_students(self, f_name=None, l_name=None, student_id=None, email=None):
        """
        Search for students matching the provided criteria.
        If multiple criteria are provided, all must match.
        Returns a list of matching students.
        """
        matches = []

        for student in self.__students:
            if student is None:
                continue
            if f_name is not None and student["F_Name"] != f_name:
                continue
            if l_name is not None and student["L_Name"] != l_name:
                continue
            if student_id is not None and student["Student_ID"] != student_id:
                continue
            if email is not None and student["Email"] != email:
                continue

            matches.append(student)
        return matches

    def add_student(self, last_name, first_name, student_id, email):
        """Add a new student record to the collection."""
        new_student = {
            "F_Name": first_name,
            "L_Name": last_name,
            "Student_ID": student_id,
            "Email": email
        }

        self.__students.append(new_student)

    def remove_student(self, student):
        """Remove the specified student record from the collection."""
        self.__students.remove(student)

    def save_students(self):
        """Save the current student collection to the JSON file."""
        with open(self.__filename, "w") as file:
            json.dump(self.__students, file, indent=4)

    def __str__(self):
        """Return all student records as formatted text."""
        records = []

        for student in self.__students:
            if student is None:
                continue

            record = self.__RECORD_FORMAT.format(
                last_name=student["L_Name"],
                first_name=student["F_Name"],
                student_id=student["Student_ID"],
                email=student["Email"]
            )

            records.append(record)

        return "\n".join(records)

def main():
    students = Students("student.json")

    print("\nWelcome to the JSON updater!")
    print(f">> Original {students.get_filename()} Contents <<")
    print(students)
    print()

    students.add_student(
        "Dorscher",
        "Lane",
        88888,
        "lmdorscher@my365.bellevue.edu"
    )

    print(">> Appended Student Contents <<")
    print(students)
    print()

    students.save_students()
    print(f"{students.get_filename()} has been updated.")

    print()
    print(f"Count of 'Lane' student(s): {str(len(students.find_students(f_name="Lane")))}")
    print()
    print("Goodbye!")


if __name__ == "__main__":
    main()