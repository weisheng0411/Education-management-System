# student
def open_course():
    courses = []  # create an empty list to store student data
    try:
        with open("course.txt", 'r') as course_File:
            for line in course_File:
                line = line.rstrip().split(",")  # split each line become a list and remove whitespace
                while len(line) < 9:
                    line.append("")
                # store each list in a dictionary
                course = {
                    "Course ID": line[0],
                    "Course Name": line[1],
                    "Teacher ID": line[2],
                    "Instructor": line[3],
                    "Assignment": line[4],
                    "Lecture Notes": line[5],
                    "Announcement": line[6],
                    "Lesson Plan": line[7]
                }
                courses.append(course)  # add student dictionary to the list
        return courses
    except FileNotFoundError:
        print("Warning : course.txt not found.")
        return None

def open_students():
    students=[] #create an empty list to store student data
    try:
        with open("students.txt", 'r') as tFile:
            for line in tFile:
                line=line.rstrip().split(",") #split each line become a list and remove whitespace
                #set the limit of the append block inside the list
                while len(line)<9:
                    line.append("")
                #store each list in a dictionary
                student = {
                    "Student ID": line[0],
                    "Name": line[1],
                    "Email": line[2],
                    "Contact": line[3],
                    "Emergency Contact": line[4],
                    "Gender":line[5],
                    "Student Status":line[6],
                    "Tuition Fees(RM)":line[7],
                    "Payment":line[8]
                }
                students.append(student) #add student dictionary to the list
        return students #return the list containing student dictionary
    except FileNotFoundError:
        print("Warning : students.txt not found.")
        return None

def open_enrolments():
    enrolments = []  # create an empty list to store student data
    try:
        with open("enrolments.txt", 'r') as enrolments_file:
            for line in enrolments_file:
                line = line.rstrip().split(",")  # split each line become a list and remove whitespace
                while len(line) < 3:
                    line.append("")
                # store each list in a dictionary
                enrolment = {
                    "Student ID": line[0],
                    "Course ID": line[1]
                }
                enrolments.append(enrolment) # add student dictionary to the list
        return enrolments
    except FileNotFoundError:
        print("Warning : enrolments.txt not found.")
        return None

def update_enrolments(enrolled):
    try:
        with open("enrolments.txt", "w") as file:
            for enrol in enrolled:
                file.write(",".join([
                    enrol["Student ID"],
                    enrol["Course ID"],
                ]) + "\n")
    except FileNotFoundError:
        print("Warning : enrolments.txt not found.")
        return None

def course_enrolment_menu():
    while True:
        print("\n-------------------------------------")
        print("--------Course Enrolment Menu--------")
        print("-------------------------------------")
        print("1. Browse Available Courses")
        print("2. Enrol in a Course")
        print("3. View Enrolled Course")
        print("4. Exit")
        print("------------------------------------")

        try:
            opt = int(input("Enter your choice (1/2/3): "))

            if opt == 1:
                browse_course()
            elif opt == 2:
                enrol_in_course()
            elif opt == 3:
                view_enrol_course()
            elif opt == 4:
                break
            else:
                print("Invalid choice")

        except ValueError:
            print("Invalid input! Only integer between 1-4 is allowed.")

def browse_course():
    """
    use course.txt
    :return: display all course
    """
    courses = open_course()
    if courses is None:
        return

    print("")
    title = "Available Courses"
    width = 40
    print("=" * width)
    print(title.center(width))
    print("=" * width)

    for course in courses:
        print(f"Course ID: {course["Course ID"]} Course Name: {course["Course Name"]}")
        print("=" * width)
    input("Enter to continue...")

def enrol_in_course():
    students = open_students()
    courses = open_course()
    enrolled = open_enrolments()

    if students is None:
        return
    if courses is None:
        return
    if enrolled is None:
        return

    tp_number = input("\nEnter your TP number: ").upper()

    student_found = None
    for student in students:
        if student["Student ID"] == tp_number:
            student_found = student
            break  # stop when found student id
    if student_found:
        browse_course()
        print("student ID founded")

        course_id = input("Enter the Course ID you want to enrol in: ").upper()
        course_found = None
        for course in courses:
            if course["Course ID"] == course_id:
                course_found = course
                break # stop when course id found

        if course_found: # if student is already enrolled in the course, it displays a message and returns
            for enrol in enrolled:
                if enrol["Student ID"] == tp_number and enrol["Course ID"] == course_id:
                    input(f"Student {tp_number} is already enrolled in {course_id}.")
                    return

            enrolled.append({"Student ID": tp_number, "Course ID": course_id})
            update_enrolments(enrolled) # update the file with the new enrollment

            input(f"Student {tp_number} enrolled in {course_id} successfully!")

        else:
            print("Course ID not found")
    else:
        print("Student ID not found")

def view_enrol_course():
    students = open_students()
    enrolments = open_enrolments()

    if students is None:
        return
    if enrolments is None:
        return

    tp_number = input("\nEnter your TP number: ").upper()

    student_found = None
    for student in students:
        if student["Student ID"] == tp_number:
            student_found = student
            break  # stop when found student id

    if student_found: # check student exists
        enrolled_course = [] # create empty list to stores
        for enrolment in enrolments:
            if enrolment["Student ID"] == tp_number:
                enrolled_course.append(enrolment["Course ID"])

        if enrolled_course: # check if student is enrolled in any course, if yes will print the enrolled course
            print(f"\nCourses enrolled by {tp_number}:")
            for course_id in enrolled_course:
                print(f"  - {course_id}")

        else:
            print(f"Student {tp_number} is not enrolled in any courses.")
    else:
        print("Student ID not found.")
    input("\npress enter to continue...")


# course_enrolment_menu()
