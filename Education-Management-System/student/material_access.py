def open_course():
    courses = []  # create an empty list to store student data
    try:
        with open("course.txt", 'r') as tFile:
            for line in tFile:
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
                    "Student Status(RM)":line[6],
                    "Tuition Fees":line[7],
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
        with open("enrolments.txt", 'r') as tFile:
            for line in tFile:
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

def browse_course():
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

def course_material_access():
    students = open_students()
    enrolments = open_enrolments()
    courses = open_course()

    if students is None:
        return
    if enrolments is None:
        return
    if courses is None:
        return

    tp_number = input("\nEnter your TP number: ").upper()

    student_found = None
    for student in students:
        if student["Student ID"] == tp_number:
            student_found = student
            break  # stop when found student id

    enrolled_courses = []
    for enrolment in enrolments: # loop all course that match tp_number
        if enrolment["Student ID"] == tp_number:
            for course in courses:
                if course["Course ID"] == enrolment["Course ID"]:
                    enrolled_courses.append(course) # append matching course for further processing

    while True:
        print("\nCourses enrolled:")
        course_number = 1
        for course in enrolled_courses:
            print(f"  {course_number}. {course['Course Name']} ({course['Course ID']})")
            course_number += 1 # assign a number to each course for option
        print(f"  {course_number}. Exit") # Display student course enrolments

        opt = int(input("\nSelect a course number to view materials: "))

        if 1 <= opt < course_number:
            selected_course = enrolled_courses[opt - 1] # this can ensure the selected number is within a valid range

            print(f"\nCourse: {selected_course['Course Name']} ({selected_course['Course ID']})")
            print(f"Assignment: {selected_course['Assignment']}")
            print(f"Lecture Notes: {selected_course['Lecture Notes']}")
            print(f"Announcement: {selected_course['Announcement']}")

            print("\n1. Download Lecture Notes")
            print("2. Back to Course Selection")
            print("3. Exit")

            opt = int(input("Select an option: "))
            if opt == 1:
                input("Download successfully")
            elif opt == 2:
                continue
            elif opt == 3:
                print("Exiting course material access...")
                return
            else:
                print("Invalid choice, please enter a valid number (1-3).")

        elif opt == course_number:
            print("Exiting course material access...")
            break

        else:
            print("Invalid choice, please enter a valid course number.")

# course_material_access()


