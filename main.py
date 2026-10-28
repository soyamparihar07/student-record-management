
from database import (
    initialize_database,
    add_student,
    get_students,
    find_student,
    update_student,
    delete_student,
)


def main():
    initialize_database()

    while True:
        print("\n===== STUDENT RECORD MANAGEMENT =====")
        print("1. Add student")
        print("2. View all students")
        print("3. Search student")
        print("4. Update student")
        print("5. Delete student")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                sid = input("Student ID: ").strip()
                name = input("Name: ").strip()
                age = int(input("Age: "))
                course = input("Course: ").strip()
                email = input("Email: ").strip()

                if not all([sid, name, course, email]) or age <= 0:
                    print("Please enter valid details.")
                    continue

                add_student(sid, name, age, course, email)
                print("Student added successfully!")

            elif choice == "2":
                students = get_students()

                if not students:
                    print("No student records found.")
                else:
                    for student in students:
                        print(student)

            elif choice == "3":
                sid = input("Enter student ID: ").strip()
                student = find_student(sid)
                print(student if student else "Student not found.")

            elif choice == "4":
                sid = input("Student ID to update: ").strip()

                if not find_student(sid):
                    print("Student not found.")
                    continue

                name = input("New name: ").strip()
                age = int(input("New age: "))
                course = input("New course: ").strip()
                email = input("New email: ").strip()

                if not all([name, course, email]) or age <= 0:
                    print("Please enter valid details.")
                    continue

                update_student(sid, name, age, course, email)
                print("Student updated successfully!")

            elif choice == "5":
                sid = input("Student ID to delete: ").strip()

                if delete_student(sid):
                    print("Student deleted successfully!")
                else:
                    print("Student not found.")

            elif choice == "0":
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Try again.")

        except ValueError:
            print("Age must be a valid positive number.")
        except Exception as error:
            print(f"Something went wrong: {error}")


if __name__ == "__main__":
    main()
