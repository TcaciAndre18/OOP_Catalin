class Student:
    def __init__(self, first_name, last_name, email, enrollment_date, date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.enrollment_date = enrollment_date
        self.date_of_birth = date_of_birth

class Faculty:
    def __init__(self, name, abbreviation, study_field):
        self.name = name
        self.abbreviation = abbreviation
        self.students = []
        self.study_field = study_field

    def add_student(self, student):
        self.students.append(student)

    def graduate_student(self, email):
        self.students = [s for s in self.students if s.email != email]

    def display_enrolled_students(self):
        print(f"Enrolled students in {self.name}:")
        for student in self.students:
            print(student.email)

    def get_study_field(self):
        return self.study_field

    def has_student(self, email):
        return any(student.email == email for student in self.students)

class University:
    def __init__(self):
        self.faculties = {}

    def create_faculty(self, name, abbreviation, study_field):
        self.faculties[study_field] = Faculty(name, abbreviation, study_field)

    def assign_student(self, email, study_field, student):
        self.faculties[study_field].add_student(student)

    def graduate_student(self, email):
        for faculty in self.faculties.values():
            faculty.graduate_student(email)

    def display_enrolled_students(self):
        print("Enrolled students in all faculties:")
        for faculty in self.faculties.values():
            faculty.display_enrolled_students()

    def display_graduates(self):
        print("Graduates from all faculties:")
        for faculty in self.faculties.values():
            faculty.display_enrolled_students()  # Displaying enrolled students as graduates were removed

    def has_student(self, email):
        return any(faculty.has_student(email) for faculty in self.faculties.values())

    def display_faculties(self):
        print("University faculties:")
        for faculty in self.faculties.values():
            print(f"{faculty.study_field}: {faculty.name}")

    def display_faculties_by_field(self, study_field):
        print(f"Faculties in field {study_field}:")
        print(f"{study_field}: {self.faculties[study_field].name}")


def main():
    tum = University()

    # Create faculties
    tum.create_faculty("Mechanical Engineering Faculty", "ME", "Mechanical Engineering")
    tum.create_faculty("Software Engineering Faculty", "SE", "Software Engineering")
    tum.create_faculty("Food Technology Faculty", "FT", "Food Technology")
    tum.create_faculty("Urbanism and Architecture Faculty", "UA", "Urbanism and Architecture")
    tum.create_faculty("Veterinary Medicine Faculty", "VM", "Veterinary Medicine")

    # Interactive command line
    while True:
        print("TUM Board Menu:")
        print("1. Create and assign a student to a faculty.")
        print("2. Graduate a student from a faculty.")
        print("3. Display current enrolled students.")
        print("4. Display graduates.")
        print("5. Check if a student belongs to a faculty.")
        print("6. Create a new faculty.")
        print("7. Display University faculties.")
        print("8. Display all faculties belonging to a field.")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            # Create and assign a student to a faculty
            first_name = input("Enter student's first name: ")
            last_name = input("Enter student's last name: ")
            email = input("Enter student's email: ")
            enrollment_date = input("Enter student's enrollment date: ")
            date_of_birth = input("Enter student's date of birth: ")
            field = input("Enter student's field: ")
            tum.assign_student(email, field, Student(first_name, last_name, email, enrollment_date, date_of_birth))
            print("Student assigned successfully.")

        elif choice == "2":
            # Graduate a student from a faculty
            email = input("Enter student's email to graduate: ")
            tum.graduate_student(email)
            print("Student graduated successfully.")

        elif choice == "3":
            # Display current enrolled students
            tum.display_enrolled_students()

        elif choice == "4":
            # Display graduates
            tum.display_graduates()

        elif choice == "5":
            # Check if a student belongs to a faculty
            email = input("Enter student's email to check: ")
            if tum.has_student(email):
                print("The student belongs to this university.")
            else:
                print("The student does not belong to this university.")

        elif choice == "6":
            # Create a new faculty
            name = input("Enter faculty name: ")
            abbreviation = input("Enter faculty abbreviation: ")
            field = input("Enter faculty field: ")
            tum.create_faculty(name, abbreviation, field)
            print("Faculty created successfully.")

        elif choice == "7":
            # Display University faculties
            tum.display_faculties()

        elif choice == "8":
            # Display all faculties belonging to a field
            field = input("Enter field: ")
            tum.display_faculties_by_field(field)

        elif choice == "9":
            # Exit program
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
