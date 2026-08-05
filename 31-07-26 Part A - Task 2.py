"""A simple menu-driven Student Management System.

Student records are stored in memory while the program is running.
"""


# The list that stores every student record as a dictionary.
students = []


def get_student_id():
    """Read and validate a positive numeric student ID from the user."""
    while True:
        student_id = input("Enter student ID: ").strip()
        if student_id.isdigit() and int(student_id) > 0:
            return int(student_id)
        print("Please enter a valid positive numeric ID.")


def find_student(student_id):
    """Return the student dictionary with the supplied ID, or None if absent."""
    for student in students:
        if student["id"] == student_id:
            return student
    return None


def add_student():
    """Add a new student after checking that the ID is unique."""
    print("\n--- Add Student ---")
    student_id = get_student_id()

    if find_student(student_id):
        print("A student with this ID already exists.")
        return

    name = input("Enter student name: ").strip()
    course = input("Enter course: ").strip()
    students.append({"id": student_id, "name": name, "course": course})
    print("Student added successfully.")


def view_students():
    """Display all saved student records in a readable table."""
    print("\n--- Student List ---")
    if not students:
        print("No student records found.")
        return

    print(f"{'ID':<10}{'Name':<25}{'Course':<20}")
    print("-" * 55)
    for student in students:
        print(f"{student['id']:<10}{student['name']:<25}{student['course']:<20}")


def search_student():
    """Find and show one student record by ID."""
    print("\n--- Search Student ---")
    student = find_student(get_student_id())

    if student:
        print(f"ID: {student['id']}")
        print(f"Name: {student['name']}")
        print(f"Course: {student['course']}")
    else:
        print("Student not found.")


def update_student():
    """Update the name and/or course of an existing student."""
    print("\n--- Update Student ---")
    student = find_student(get_student_id())

    if not student:
        print("Student not found.")
        return

    # Empty input keeps the existing value unchanged.
    new_name = input(f"Enter new name [{student['name']}]: ").strip()
    new_course = input(f"Enter new course [{student['course']}]: ").strip()
    if new_name:
        student["name"] = new_name
    if new_course:
        student["course"] = new_course
    print("Student record updated successfully.")


def delete_student():
    """Delete a student record after a confirmation prompt."""
    print("\n--- Delete Student ---")
    student = find_student(get_student_id())

    if not student:
        print("Student not found.")
        return

    confirmation = input(f"Delete {student['name']}? (yes/no): ").strip().lower()
    if confirmation == "yes":
        students.remove(student)
        print("Student record deleted successfully.")
    else:
        print("Deletion cancelled.")


def show_menu():
    """Print the main menu options."""
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")


def main():
    """Run the program until the user chooses to exit."""
    actions = {
        "1": add_student,
        "2": view_students,
        "3": search_student,
        "4": update_student,
        "5": delete_student,
    }

    while True:
        show_menu()
        choice = input("Choose an option (1-6): ").strip()

        if choice == "6":
            print("Thank you for using the Student Management System.")
            break

        action = actions.get(choice)
        if action:
            action()
        else:
            print("Invalid choice. Please select a number from 1 to 6.")


# Start the program only when this file is run directly.
if __name__ == "__main__":
    main()
