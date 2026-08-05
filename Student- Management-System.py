"""Provide a menu-driven, in-memory student record manager.

The application lets a user add, view, search, update, and delete student
records during one terminal session. Each record is stored as a dictionary
containing an integer ``id`` plus ``name`` and ``course`` strings. Records are
not persisted, so they are cleared when the program exits.
"""


# Application data store. Keeping this in memory makes the project simple but
# means records are only available for the lifetime of the running program.
students = []


def get_student_id():
    """Prompt until the user enters a positive integer student ID.

    Returns:
        int: A validated student ID greater than zero.
    """
    while True:
        student_id = input("Enter student ID: ").strip()
        if student_id.isdigit() and int(student_id) > 0:
            return int(student_id)
        print("Please enter a valid positive numeric ID.")


def find_student(student_id):
    """Find a student record by its ID.

    Args:
        student_id (int): The ID to look up.

    Returns:
        dict | None: The matching record, or ``None`` when it does not exist.
    """
    for student in students:
        if student["id"] == student_id:
            return student
    return None


def add_student():
    """Collect details and add a student only when its ID is unique."""
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
    """Print every saved student record in an aligned table."""
    print("\n--- Student List ---")
    if not students:
        print("No student records found.")
        return

    print(f"{'ID':<10}{'Name':<25}{'Course':<20}")
    print("-" * 55)
    for student in students:
        print(f"{student['id']:<10}{student['name']:<25}{student['course']:<20}")


def search_student():
    """Prompt for an ID and display its matching student record, if any."""
    print("\n--- Search Student ---")
    student = find_student(get_student_id())

    if student:
        print(f"ID: {student['id']}")
        print(f"Name: {student['name']}")
        print(f"Course: {student['course']}")
    else:
        print("Student not found.")


def update_student():
    """Update an existing student's name and/or course.

    Leaving either prompt blank preserves that field's current value.
    """
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
    """Remove an existing student only after the user confirms deletion."""
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
    """Display the numbered operations available in the main menu."""
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")


def main():
    """Run the input loop and dispatch each selected menu operation."""
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
