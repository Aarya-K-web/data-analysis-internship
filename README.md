# Student Management System

A small command-line Python application for managing student records during a
single program session.

## Features

- Add a student with a unique, positive numeric ID.
- View all students in a formatted table.
- Search for a student by ID.
- Update a student's name or course.
- Delete a student after confirmation.
- Validate menu choices and student IDs.

## Requirements

- Python 3 (no external packages are required).

## Run the program

From this project folder, run:

```powershell
python "Student- Management-System.py"
```

Choose an option from the displayed menu and follow the prompts. Enter `6` to
exit.

## How data is stored

Student records are dictionaries kept in the `students` list while the program
is running. They contain an `id`, `name`, and `course`. Because the project
does not use a file or database, all records are lost when the program exits.

## Project structure

```text
Student- Management-System.py  # Application source code
README.md                      # Project overview and usage instructions
```
