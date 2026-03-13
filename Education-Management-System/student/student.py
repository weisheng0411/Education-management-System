def open_accounts():
    """
    Reads accounts.txt file
    :return: return None if file not exists
    """
    accounts=[] #empty list to store account
    try: #handle file not found error
        with open("accounts.txt",'r')as login:
            for row in login:
                row=row.rstrip().split(",")#remove whitespace and split each line become a list
                #store each list in a dictionary
                item={
                    "Role":row[0],
                    "Username":row[1],
                    "Password":row[2]
                }
                accounts.append(item)
            return accounts #return dictionary to the account list
    except FileNotFoundError:
        print("Warning : accounts.txt not found.")
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

def open_grades():
    grades=[] #create an empty list to store grade data
    try:
        with open("grades.txt", 'r') as grade_file:
            for line in grade_file:
                line=line.rstrip().split(",") #split each line become a list and remove whitespace
                #set the limit of the append block inside the list
                while len(line)<7:
                    line.append("")
                #store each list in a dictionary
                grade = {
                    "Student ID": line[0],
                    "Course ID": line[1],
                    "Assignment Grade": line[2],
                    "Exam Grade": line[3],
                    "GPA": line[4],
                    "Feedback": line[5],
                    "Performance":line[6]
                }
                grades.append(grade) #add grade dictionary to the list
        return grades #return the list containing student dictionary
    except FileNotFoundError:
        print("Warning : grades.txt not found.")
        return None

def open_mailbox():
    mailbox=[] #create an empty list to store data
    try:
        with open("mail.txt", 'r')as message:
            for line in message:
                line=line.rstrip().split(',') #remove whitespace and split each line become a list
                #store each student list in a dictionary
                detail={
                    'Name':line[0],
                    'Role':line[1],
                    'Message':line[2],
                    'Reply':line[3]if len(line) > 3 else ""  #add reply column if having reply message else empty
                }
                mailbox.append(detail) #add dictionary into mailbox list
        return mailbox #return list containing dictionary into mailbox
    except FileNotFoundError:
        print("Warning : mail.txt not found.")
        return None

def update_student_file(students):
    try:
        with open("students.txt", "w") as update_file:
            for student in students: # loop through each student dictionary
                update_file.write(",".join([ # join all values with comma and write to files
                    student["Student ID"],
                    student["Name"],
                    student["Email"],
                    student["Contact"],
                    student["Emergency Contact"],
                    student["Gender"],
                    student["Student Status"],
                    student["Tuition Fees(RM)"],
                    student["Payment"]
                ]) + "\n") # add newline after each student data
    except FileNotFoundError:
        print("Warning : students.txt not found.")
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

def information_menu():
    while True:
        print("\n-----------------------------------")
        print("---------Information Menu----------")
        print("-----------------------------------")
        print("1. Update Information")
        print("2. Exit")
        print("-----------------------------------")

        opt = int(input("Enter your choice (1/2): "))

        try:
            if opt == 1:
                upd_information()
            elif opt == 2:
                print("Return to Student Menu")
                break
            else:
                print("Invalid choice, please Enter (1/2)")
        except ValueError:
            print("Invalid input! Only integer 1-2 is allowed.")

def upd_information():
    """
    will print out correct personal information
    ask for student enter new personal information
    :return: update student personal information
    """

    tp_number = input("\nEnter your TP number: ").upper()

    students = open_students()

    if students is None:
        return

    student_found = None
    for student in students:
        if student["Student ID"] == tp_number:
            student_found = student
            break # stop when found student id
    while True:
        if student_found:
            print("\n--------------------------------------")
            print("---------Current Information----------")
            print("--------------------------------------")
            print(f"TP Number: {student_found['Student ID']}")
            print(f"Name: {student_found['Name']}")
            print(f"Email: {student_found['Email']}")
            print(f"Contact Number: {student_found['Contact']}")
            print(f"Emergency Contact: {student_found['Emergency Contact']}")
            print("--------------------------------------") # print out all current information

            print("\n1. Email address")
            print("2. Contact Number")
            print("3. Emergency Contact")
            print("4. Exit")

            try:
                choice = int(input("Select the choice you want to update (1/2/3/4): "))

                if choice == 1:
                    print(f"Old Email Address: {student_found['Email']}")
                    student_found['Email'] = input("New Email Address: ")

                elif choice == 2:
                    print(f"Old Contact Number: {student_found['Contact']}")
                    student_found['Contact'] = input("New Contact Number: ")

                elif choice == 3:
                    print(f"Old Emergency Contact: {student_found['Emergency Contact']}")
                    student_found['Emergency Contact'] = input("New Emergency Contact: ")

                elif choice == 4:
                    print("Return to Student Menu\n")
                    break
                else:
                    print("Invalid choice. No changes made.")

                update_student_file(students) # calling function to update new information
                print("Update Information successfully!")

            except ValueError:
                print("Invalid choice, please enter a valid number (1-4).")
        else:
            print("tp_number not found")
            return

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
    if student_found:
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
    else:
        print("Username not found!")

def grades_menu():
    while True:
        print("")
        title = "Grades Tracking Menu"
        width = 40
        print("=" * width)
        print(title.center(width))
        print("=" * width)
        print("1. View Grades")
        print("2. Exit")

        try:
            opt = int(input("\nYour choice: "))

            if opt == 1:
                grades_track()
            elif opt ==2:
                break
            else:
                print("Invalid choice, please enter a valid number (1-2).")
        except ValueError:
            print("Invalid input! Please enter a number.")

def grades_track():
    grades = open_grades()

    if grades is None:
        return

    tp_number = input("\nEnter your TP number: ").upper()

    student_courses = []
    for grade in grades:
        if grade["Student ID"] == tp_number:
            student_courses.append(grade) # Get all course grades for the student

    if student_courses:
        while True:
            print("\nCourses Enrolled:")
            index = 1
            course_map = {}  # make course in dictionary
            for course in student_courses:
                if course["Course ID"] not in course_map.values():  # avoid duplicate data
                    print(f"  {index}. {course['Course ID']}")
                    course_map[index] = course["Course ID"]
                    index += 1 # every course will add 1 selection
            print(f"  {index}. Exit")

            try:
                opt = int(input("\nSelect a course number to view grades: "))
                if 1 <= opt < index: # make sure option is between 1 - index-1
                    selected_course_id = course_map[opt]

                    selected_course = None
                    for grade in student_courses:
                        if grade["Course ID"] == selected_course_id:
                            selected_course = grade
                            break  # find the grades of this course
                    print("")
                    title = "Grades Tracking"
                    width = 40
                    print("=" * width)
                    print(title.center(width))
                    print("=" * width)
                    print(f"Course: {selected_course['Course ID']}")
                    print(f"Assignment Grade: {selected_course['Assignment Grade']}")
                    print(f"Exam Grade: {selected_course['Exam Grade']}")
                    print(f"GPA: {selected_course['GPA']}")
                    print("-" * width)

                    print("\n1. Back to Course Selection")
                    print("2. Exit")

                    opt = int(input("Select an option: "))
                    if opt == 1:
                        continue
                    elif opt == 2:
                        print("Exiting grades tracking...")
                        break
                    else:
                        print("Invalid choice, please enter a valid number (1-2).")
                        return
                elif opt == index:
                    print("Exiting grades tracking...")
                    return
                else:
                    print("Invalid choice, please enter a valid course number.")
            except ValueError:
                print("Invalid input! Please enter a number.")
    else:
        print("\nStudent ID not found or no enrolled courses. Please check your TP number.")

def feedback_menu():
    while True:
        print("")
        title = "Feedback Submission"
        width = 40
        print("=" * width)
        print(title.center(width))
        print("=" * width)
        print("1. Submit a feedback")
        print("2. Exit")

        try:
            opt = int(input("Select an option: "))

            if opt == 1:
                submit_feedback()
            elif opt ==2:
                break
            else:
                print("Invalid choice, please enter a valid number (1-2).")
                return
        except ValueError:
            print("Invalid choice, please enter a valid number (1-2).")


def submit_feedback():
    students = open_students()
    mailboxes = open_mailbox()

    if students is None:
        return
    if mailboxes is None:
        return

    tp_number = input("\nEnter your TP number: ").upper()
    student_found = None
    for student in students:
        if student["Student ID"] == tp_number:
            student_found = student
            break  # stop when found student id

    if student_found:
        name = input("Enter your name: ").strip().upper()
        msg = input("Enter your feedback message: ").strip()
        role = "Student"  # keep the role to student

        # new submission dictionary
        new_submission = {
            "Name": name,
            "Role": role,
            "Message": msg,
            "Reply": ""  # reply only for staff , keep it empty
        }

        mailboxes.append(new_submission)
        with open("mail.txt", "w") as message:
            for mail in mailboxes: # loop through mailboxes
                message.write(",".join(mail.values()) + "\n") # write each feedback entry as a comma-separated line.

        print("Feedback submitted successfully!")
    else:
        input("Student ID not found, make sure enter correct student ID.")

def login_student_menu():

        print("")
        title = "Student Login Menu"
        width = 40
        print("=" * width)
        print(title.center(width))
        print("=" * width)
        print("1. Create account")
        print("2. Login account")
        print("3. Exit")

        try:
            opt = int(input("\nYour choice: "))

            if opt == 1:
                create_student_acc()
            elif opt == 2:
                login_student_acc()
            elif opt == 3:
                return
        except ValueError:
            print("Invalid input! Only integer between 1-3 is allowed.")


def create_student_acc():
    new_user = input("Please enter your new username: ").upper()
    new_pass = input("Please enter your password: ")
    role = "Student"

    accounts = open_accounts()
    if accounts is None:
        return

    account_found = None
    for account in accounts:
        if account["Username"] == new_user:
            account_found = account
            break  # stop when account correct

    if account_found:
        print("Account already exist!")

    if not account_found:

        new_account = {
            "Role": role,
            "Username": new_user,
            "Password": new_pass,
        }

        accounts.append(new_account)
        with open("accounts.txt", "w") as message:
            for acc in accounts:
                message.write(",".join(acc.values()) + "\n")

        print(f"\nyour username: {new_user}")
        print(f"your password: {new_pass}")
        print("Account created successful!")


def login_student_acc():
    username = input("Please enter your username: ").upper()
    password = input("Please enter your password: ")

    accounts = open_accounts()
    if accounts is None:
        return

    account_found = None
    for account in accounts:
        if account["Username"] == username and account["Password"] == password:
            account_found = account
            break  # stop when account correct

    if account_found:
        print("Login successful!")
        student_menu()
    else:
        print("Account not found!")


def student_menu():
    while True:
        print("")
        title = "Student Menu"
        width = 40
        print("=" * width)
        print(title.center(width))
        print("=" * width)
        print("1. Update Personal Information")
        print("2. Course Enrolment")
        print("3. Course Material Access")
        print("4. Grades Tracking")
        print("5. Feedback Submission")
        print("6. Exit")
        print("-" * width)

        try:
            opt = int(input("\nYour choice: "))

            if opt == 1:
                information_menu()
            elif opt == 2:
                course_enrolment_menu()
            elif opt == 3:
                course_material_access()
            elif opt == 4:
                grades_menu()
            elif opt == 5:
                feedback_menu()
            elif opt == 6:
                print("Exiting Student Menu")
                break
        except ValueError:
            print("Invalid input! Only integer between 1-6 is allowed.")

login_student_menu()
