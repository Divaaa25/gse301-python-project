# Basic student information
student_name = "Salau Busayo"          # string
matric_number = "22/66MA172"             # string
age = 20                                 # integer
cgpa = 4.71                              # float
is_active = True                         # boolean

# Courses and grades
courses_registered = ["ACC 301", "GSE 301", "FIN 345"]  # list
grades = {
    "ACC 301": "A",
    "FIN 345": "A",
    "GSE 301": "A"
}  # dictionary



# Tuple for fixed department info
department_info = ("Accounting Department", "Faculty of Management Science", 2025)

# Student profiles stored as dictionaries
student_1 = {
    "name": "Salau Busayo",
    "matric": "22/66MA172",
    "age": 20,
    "cgpa": 4.71,
    "is_active": True,
    "courses": ["ACC 301", "GSE 301", "FIN 345"],
    "outstanding_courses": 0
}

student_2 = {
    "name": "Jamiu Muheebulah",
    "matric": "22/66MB111",
    "age": 19,
    "cgpa": 3.85,
    "is_active": True,
    "courses": ["ACC 301", "GSE 301", "FIN 345"],
    "outstanding_courses": 0
}

student_3 = {
    "name": "Olusola Amos",
    "matric": "22/66MA148",
    "age": 22,
    "cgpa": 4.21,
    "is_active": True,
    "courses": ["ACC 301","FIN 345", "GSE 301"],
    "outstanding_courses": 0
}

student_4 = {
    "name": "Johnson Nicholas",
    "matric": "22/66MA097",
    "age": 19,
    "cgpa": 4.55,
    "is_active": True,
    "courses": ["FIN 345", "ACC 301", "GSE 301"],
    "outstanding_courses": 0
}

student_5 = {
    "name": "Oyeleke Jacob",
    "matric": "22/66MA161",
    "age": 20,
    "cgpa": 4.4,
    "is_active": True,
    "courses": ["ACC 301", "FIN 345", "GSE 301"],
    "outstanding_courses": 0
}

# List of students
students = [student_1, student_2, student_3, student_4, student_5]

# Set of unique courses
unique_courses = set()
for student in students:
    unique_courses.update(student["courses"])



def calculate_grade(score):
    if score >= 70:
        grade = "A"
    elif score >= 60:
        grade = "B"
    elif score >= 50:
        grade = "C"
    elif score >= 45:
        grade = "D"
    elif score >= 40:
        grade = "E"
    else:
        grade = "F"

    match grade:
        case "A":
            print("Excellent performance")
        case "B":
            print("Very good")
        case "C":
            print("Good effort")
        case "D":
            print("Fair")
        case "E":
            print("Needs improvement")
        case "F":
            print("Failed")

    return grade




def validate_age_and_cgpa():
    try:
        age_input = int(input("Enter age: "))
        cgpa_input = float(input("Enter CGPA: "))

        if not (16 <= age_input <= 40):
            raise ValueError("Age must be between 16 and 40")

        if not (0.0 <= cgpa_input <= 5.0):
            raise ValueError("CGPA must be between 0.0 and 5.0")

        return age_input, cgpa_input

    except ValueError as e:
        print("Invalid input:", e)
        return None, None



def analyze_assignment_scores():
    assignment_scores = [45, 67, 89, 72, 90, 55, 60, 78, 84, 69]

    top_3_scores = assignment_scores[:3]
    last_5_scores = assignment_scores[-5:]
    every_other_score = assignment_scores[::2]

    print("\nAssignment Score Analysis")
    print("Top 3 scores:", top_3_scores)
    print("Last 5 scores:", last_5_scores)
    print("Every other score:", every_other_score)


def demonstrate_set_operations():
    set_pass = {"Salau Busayo", "Jamiu Muheebulah", "Olusola Amos", "Johnson Nicholas", "Oyeleke Jacob"}
    set_merit = {"Salau Busayo", "Olusola Amos", "Johnson Nicholas", "Oyeleke Jacob"}

    print("\nSet Operations")
    print("Passed and Merit:", set_pass & set_merit)
    print("All students:", set_pass | set_merit)
    print("Passed but not merit:", set_pass - set_merit)




#Choice 1
def view_all_students(students):
    print("\nList of Students:")
    for index, student in enumerate(students, start=1):
        print(f"{index}. {student['name']}")


#Choice 2
def add_new_student(students):
    try:
        name = input("Enter name: ")
        matric = input("Enter matric number: ")
        age = int(input("Enter age: "))
        cgpa = float(input("Enter CGPA: "))
        is_active_input = input("Is the student active (yes/no): ").lower()
        courses_input = input("Enter courses (comma separated): ")

        is_active = True if is_active_input == "yes" else False
        courses = [course.strip() for course in courses_input.split(",")]

        new_student = {
            "name": name,
            "matric": matric,
            "age": age,
            "cgpa": cgpa,
            "is_active": is_active,
            "courses": courses,
            "outstanding_courses": 0
        }

        students.append(new_student)
        print("Student record added successfully.")

    except ValueError:
        print("Invalid input. Please enter correct data types.")


#Choice 3
def check_eligibility(student):
    if student["cgpa"] >= 2.5 and student["outstanding_courses"] == 0 and student["is_active"]:
        return True, f'{student["name"]} is eligible for graduation'
    else:
        return False, f'{student["name"]} is NOT eligible for graduation'
    
def eligibility_menu(students):
    name = input("Enter student name: ")

    for student in students:
        if student["name"].lower() == name.lower():
            status, message = check_eligibility(student)

            print("\nChecking eligibility...")
            print(f"Matric Number: {student['matric']}")
            print(f"CGPA: {student['cgpa']}")
            print(f"Outstanding Courses: {student['outstanding_courses']}")
            print(f"Active Status: {student['is_active']}")
            print("\nEligibility Result:")
            print(message)
            return

    print("Student not found.")

#Choice 4

def find_top_performer(students):
    top_student = max(students, key=lambda student: student["cgpa"])

    print("\nTop Performer:")
    print(f"Name: {top_student['name']}")
    print(f"Matric: {top_student['matric']}")
    print(f"CGPA: {top_student['cgpa']}")
    print(f"Courses: {top_student['courses']}")



while True:
    print("""
============================================
     Student Academic Performance System
============================================

Loading student records...

5 student profiles loaded successfully.
--------------------------------------------

Menu Options
1. View all students
2. Add new student
3. Check eligibility for graduation
4. Find top performer
5. Exit
--------------------------------------------
""")

    choice = input("Enter your choice: ")

    match choice:
        case "1":
            view_all_students(students)

        case "2":
            add_new_student(students)

        case "3":
            eligibility_menu(students)

        case "4":
            find_top_performer(students)

        case "5":
            print("Exiting the system...")
            print("Goodbye!")
            break

        case _:
            print("Invalid option. Please select between 1 and 5.")
