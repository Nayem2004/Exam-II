# program Exam ll

#Program for exam 2 data structures. 

class Student:
    def __init__(self, student_id, name, score):
        # Initializes a Student object with an ID, name, and score.
        self.student_id = student_id
        self.name = name
        self.score = score

    def __str__(self):
        # Returns a string representation of the student object
        return f"ID: {self.student_id}, Name: {self.name}, Score: {self.score}"

def add_student(student_list, student_id, name, score):
    # Creates a new Student object and adds it to the student list.
    student_list.append(Student(student_id, name, score))

def search_student(student_list, student_id):
    # Searches for a student by their ID in the student list.
    for student in student_list:
        if student.student_id == student_id:
            return str(student)  # Returns the student details if found.
    return "Student not found"  # Returns a message if not found

def sort_students(student_list):
    # Sorts the student list by scores in descending order.
    for i in range(len(student_list)):
        for j in range(0, len(student_list) - i - 1):
            if student_list[j].score < student_list[j + 1].score:
                # Swaps if the current score is less than the next score
                student_list[j], student_list[j + 1] = student_list[j + 1], student_list[j]

def main():
    # Creates an initial list of Student objects.
    students = [Student(1, "Nayem", 88),Student(2, "Breze", 72),Student(3, "Jose", 95)]
    
    # Displays the initial list of students.
    print("Initial list of students:")
    for student in students:
        print(student)

    # Adds a new student to the list.
    add_student(students, 4, "Alejandro", 90)
    print("\nAfter adding a new student:")
    for student in students:
        print(student)

    # Searches for a specific student by their ID
    print("\nSearch result for student ID 2:")
    print(search_student(students, 2))

    # Sorts the students by their scores in descending order.
    sort_students(students)
    print("\nStudents sorted by score in descending order:")
    for student in students:
        print(student)

# calls the main call main to run the program.
main()
