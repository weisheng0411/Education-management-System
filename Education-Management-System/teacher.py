from datetime import datetime

# open file functions
def open_teacher():
    teachers = []  # List to store teacher records
    try:
        with open("teachers.txt", "r") as f:
            for line in f:
                parts = line.rstrip().split(",")  # Split each line by comma
                if len(parts) < 4:
                    print("Warning: Incomplete teacher record found and skipped.")  # Skip invalid record
                    continue
                teacher = {
                    "Teacher ID": parts[0].strip().upper(),  # Teacher ID in uppercase
                    "Day": parts[1].strip(),  # Day info
                    "Instructor": parts[2].strip(),  # Instructor name
                    "Available time": parts[3].strip()  # Available time
                }
                teachers.append(teacher)
        return teachers  # Return list of teachers
    except FileNotFoundError:
        print("Warning: teachers.txt not found.")
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


def save_course(courses):
    """
    Save course data to course.txt using the following fields:
    Course ID, Teacher ID, Course Name, Instructor, Assignment, Lecture Notes, Lesson Plan
    """
    with open("course.txt", "w") as f:
        for course in courses:
            f.write(f"{course['Course ID']},{course['Course Name']},{course['Teacher ID']},"
                    f"{course['Instructor']},{course['Assignment']},{course['Lecture Notes']},{course['Announcement']},"
                    f"{course['Lesson Plan']}\n")


def open_enrolments():
    enrolments = []  # List for enrolment records
    try:
        with open("enrolments.txt", "r") as f:
            for line in f:
                fields = line.rstrip().split(",")  # Split line by comma
                if len(fields) < 2:
                    print(f"Skipping invalid enrolment line: {line}")  # Skip invalid record
                    continue
                enrolment = {
                    "Student ID": fields[0].strip().upper(),  # Student ID in uppercase
                    "Course ID": fields[1].strip().upper()  # Course ID in uppercase
                }
                enrolments.append(enrolment)
        return enrolments  # Return list of enrolments
    except FileNotFoundError:
        print("Warning: enrolments.txt not found.")
    return None


def save_enrolments(enrolments):
    with open("enrolments.txt", "w") as f:
        for e in enrolments:
            # Write each enrolment record
            f.write(f"{e['Student ID']},{e['Course ID']}\n")


def open_students():
    students = []  # List for student records
    try:
        with open("students.txt", "r") as sFile:
            for line in sFile:
                fields = line.rstrip().split(",")  # Split line by comma
                if len(fields) < 2:
                    print(f"Skipping invalid student line: {line}")
                    continue
                student = {
                    "Student ID": fields[0].strip(),  # Student ID
                    "Name": fields[1].strip()  # Student Name
                }
                students.append(student)
            return students  # Return list of students
    except FileNotFoundError:
        print("Warning: students.txt not found.")
    return None


def open_grades():
    grades = []  # List for grade records
    try:
        with open("grades.txt", "r") as f:
            for line in f:
                fields = line.rstrip().split(",")  # Split line by comma
                if len(fields) < 6:
                    print("Skipping invalid line:", line.strip())
                    continue
                record = {
                    "student ID": fields[0].strip().upper(),  # Student ID in uppercase
                    "course ID": fields[1].strip().upper(),  # Course ID in uppercase
                    "assignment score": fields[2].strip(),  # Assignment score
                    "exam score": fields[3].strip(),  # Exam score
                    "gpa": fields[4].strip(),  # GPA
                    "feedback": fields[5].strip(),  # Feedback
                    "performance": fields[6].strip() if len(fields) >= 7 else ""  # Performance (optional)
                }
                grades.append(record)
        return grades  # Return list of grades
    except FileNotFoundError:
        print("Warning: grades.txt not found.")
        return None


def save_grades(data):
    with open("grades.txt", "w") as f:
        for record in data:
            # Write each grade record as comma-separated values
            line = ",".join([
                record.get("student ID", "").strip().upper(),
                record.get("course ID", "").strip().upper(),
                record.get("assignment score", "").strip(),
                record.get("exam score", "").strip(),
                record.get("gpa", "").strip(),
                record.get("feedback", "").strip(),
                record.get("performance", "").strip()
            ])
            f.write(line + "\n")


def open_attendances():
    attendances = []  # List for attendance records
    try:
        with open("attendances.txt", "r") as record:
            for line in record:
                fields = line.rstrip().split(',')
                while len(fields) < 13:
                    fields.append("")  # Pad missing fields with empty strings
                detail = {
                    "Student ID": fields[0].strip(),
                    "Event Attendance": fields[1].strip(),
                    "Course 1": fields[2].strip(),
                    "Course 1 Attendance": fields[3].strip(),
                    "Course 2": fields[4].strip(),
                    "Course 2 Attendance": fields[5].strip(),
                    "Course 3": fields[6].strip(),
                    "Course 3 Attendance": fields[7].strip(),
                    "Course 4": fields[8].strip(),
                    "Course 4 Attendance": fields[9].strip(),
                    "Course 5": fields[10].strip(),
                    "Course 5 Attendance": fields[11].strip(),
                    "Total Attendance": fields[12].strip()
                }
                attendances.append(detail)
        return attendances  # Return list of attendance records
    except FileNotFoundError:
        print("Error: attendances.txt not found.")
        return None


def verify_enrollment(student_id, course_id):
    enrolments = open_enrolments()  # Get enrolment records
    if enrolments is None:
        return False
    for e in enrolments:
        if e["Student ID"] == student_id and e["Course ID"] == course_id:
            return True  # Enrollment found
    return False  # Not enrolled


def parse_attendance(att_str):
    att_str = att_str.strip()
    if not att_str:
        return (0, 0)  # No data provided
    try:
        attended, total = att_str.split("/")  # Expected format "attended/total"
        return int(attended.strip()), int(total.strip())
    except ValueError:
        return (0, 0)


def recalc_total_attendance(record):
    total_attended = 0
    total_possible = 0
    if record["Event Attendance"]:
        ea, et = parse_attendance(record["Event Attendance"])
        total_attended += ea
        total_possible += et
    for i in range(1, 6):
        key = "Course " + str(i) + " Attendance"
        if record.get(key):
            ca, ct = parse_attendance(record[key])
            total_attended += ca
            total_possible += ct
    if total_possible == 0:
        record["Total Attendance"] = ""
    else:
        record["Total Attendance"] = f"{total_attended}/{total_possible}"  # Update total attendance


# function 1: Course Management Functions
def teacher_create_course():
    courses = open_course()
    if not courses:
        return

    teacher_id = input("Please enter Teacher ID: ").strip().upper()

    # Find courses taught by the teacher
    teacher_courses = []
    for course in courses:
        if course["Teacher ID"] == teacher_id:
            teacher_courses.append(course)

    if not teacher_courses:
        print("Teacher ID does not exist; cannot create course.")
        return

    # Show teacher's current courses
    print("\nTeacher verified. Welcome,", teacher_courses[0]["Instructor"])
    print("Current courses assigned to this teacher:")
    index = 1
    for course in teacher_courses:
        print(f"{index}. Course ID: {course['Course ID']}\n   Course Name: {course['Course Name']} \n")
        index += 1

        # Let the teacher select a course
    try:
        choice = int(input("\nSelect a course by entering its index: "))
        if choice < 1 or choice > len(teacher_courses):
            print("Invalid choice. Please select a valid course index.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    selected_course = teacher_courses[choice - 1]
    if selected_course["Course ID"].strip() and selected_course["Course Name"].strip():
        print("Error: The selected course is already assigned. You cannot create a new course here.")
        return

    print(f"\nYou selected an empty course slot.")

    course_id = input("\nPlease enter new Course ID: ").strip().upper()

    # Check if Course ID already exists
    for course in courses:
        if course["Course ID"] == course_id:
            print("Error: Course ID already exists. Please try again.")
            return

    # Get course details from input
    course_name = input("Please enter Course Name: ").strip()
    assignment = input("Please enter Assignment information: ").strip()
    lecture_notes = input("Please enter Lecture Notes: ").strip()
    announcement = input("Please enter Announcement: ").strip()
    lesson_plan = input("Please enter Lesson Plan: ").strip()

    if not (course_id and course_name and assignment and lecture_notes and announcement and lesson_plan):
        print("Error: All fields are required. Please try again.")
        return

    new_course = {
        "Course ID": course_id,
        "Course Name": course_name,
        "Teacher ID": teacher_id,
        "Instructor": teacher_courses[0]["Instructor"],
        "Assignment": assignment,
        "Lecture Notes": lecture_notes,
        "Announcement": announcement,
        "Lesson Plan": lesson_plan
    }

    courses = [course for course in courses if course["Course ID"].strip()]
    # Append new course to list
    courses.append(new_course)

    # Writing to file directly inside the function
    try:
        with open("course.txt", "w") as file:
            for course in courses:
                file.write(",".join([
                    course["Course ID"],
                    course["Course Name"],
                    course["Teacher ID"],
                    course["Instructor"],
                    course["Assignment"],
                    course["Lecture Notes"],
                    course["Announcement"],
                    course["Lesson Plan"]
                ]) + "\n")  # Ensure only one newline per course
    except FileNotFoundError:
        print("Warning: course.txt not found.")

    # Displaying updated courses
    print("\n--------------------------------------------------")
    print("Course created successfully! Current courses:")
    index = 1
    for course in teacher_courses + [new_course]:
        if course["Course ID"].strip():
            print(f"{index}. Course ID: {course['Course ID']}, Course Name: {course['Course Name']}")
            index += 1
    print("--------------------------------------------------")


def update_course():
    courses = open_course()
    if courses is None:
        return

    while True:
        course_id = input("\nPlease enter the Course ID to update: ").strip().upper()
        if course_id:
            break
        else:
            print("Error: Course ID cannot be empty. Please enter a valid Course ID.")
            return

    course_found = None
    for course in courses:
        if course["Course ID"] == course_id:
            course_found = course
            break

    if course_found is None:
        print("Course not found. Returning to menu.")
        return

    # Loop to allow multiple updates until user decides to exit
    while True:
        print("\n--------------------------------------")
        print("--------- Current Course Info --------")
        print("--------------------------------------")
        print(f"Course ID:       {course_found['Course ID']}")  # Display current course info
        print(f"Course Name:     {course_found['Course Name']}")
        print(f"Teacher ID:      {course_found['Teacher ID']}")
        print(f"Instructor:      {course_found['Instructor']}")
        print(f"Assignment:      {course_found['Assignment']}")
        print(f"Lecture Notes:   {course_found['Lecture Notes']}")
        print(f"Announcement:   {course_found['Announcement']}")
        print(f"Lesson Plan:     {course_found['Lesson Plan']}")
        print("--------------------------------------")
        input("Press Enter to continue...")  # Pause for user review

        # Let user choose field to update
        print("\nSelect the field to update:")
        print("1. Instructor")
        print("2. Assignment")
        print("3. Lecture Notes")
        print("4. Announcement")
        print("5. Lesson Plan")
        print("6. Return to main menu")

        try:
            choice = int(input("Please enter your choice (1-5): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue

        if choice == 1:
            print(f"Old Instructor: {course_found['Instructor']}")  # Show old value
            course_found['Instructor'] = input("New Instructor: ").strip()  # Update field
            save_course(courses)
            print("Instructor updated successfully!\n")
        elif choice == 2:
            print(f"Old Assignment: {course_found['Assignment']}")
            course_found['Assignment'] = input("New Assignment: ").strip()
            save_course(courses)
            print("Assignment updated successfully!\n")
        elif choice == 3:
            print(f"Old Lecture Notes: {course_found['Lecture Notes']}")
            course_found['Lecture Notes'] = input("New Lecture Notes: ").strip()
            save_course(courses)
            print("Lecture Notes updated successfully!\n")
        elif choice == 4:
            print(f"Old Announcement: {course_found['Announcement']}")
            course_found['Announcement'] = input("New Announcement: ").strip()
            save_course(courses)
            print("Announcement updated successfully!\n")
        elif choice == 5:
            print(f"Old Lesson Plan: {course_found['Lesson Plan']}")
            course_found['Lesson Plan'] = input("New Lesson Plan: ").strip()
            save_course(courses)
            print("Lesson Plan updated successfully!\n")
        elif choice == 6:
            print("Returning to main menu.\n")
            break
        else:
            print("Invalid choice, please enter a number between 1 and 5.")


def view_course(courses):
    print("\n=== Course List ===")
    if not courses:
        print("No course records available.")
    else:
        counter = 1
        for course in courses:
            if 'Course ID' in course and 'Course Name' in course and course['Course ID'] and course['Course Name']:
            # Print each course record in a formatted manner
                print(f"{counter}. Course ID: {course['Course ID']}")
                print(f"   Course Name:    {course['Course Name']}")
                print(f"   Teacher ID:     {course['Teacher ID']}")
                print(f"   Instructor:     {course['Instructor']}")
                print(f"   Assignment:     {course['Assignment']}")
                print(f"   Lecture Notes:  {course['Lecture Notes']}")
                print(f"   Announcement:  {course['Announcement']}")
                print(f"   Lesson Plan:    {course['Lesson Plan']}")
                print("--------------------------------------------------")
                counter += 1

def schedule():
    teachers = open_teacher()
    if teachers is None:
        return  # If the teacher file cannot be read, exit immediately

    # Prompt the user for the Teacher ID
    teacher_id_input = input("Please enter the Teacher ID to update the available time: ").strip().upper()
    if not teacher_id_input:
        print("Error: Teacher ID cannot be empty. Returning to course management menu.")
        return

    # Find all teacher records that match the entered Teacher ID
    matching_records = []
    for t in teachers:
        if t["Teacher ID"] == teacher_id_input:
            matching_records.append(t)

    if not matching_records:
        print("Teacher ID not found. Returning to course management menu.")
        return

    # Display all matching records (without using enumerate)
    print("\n====================================================")
    print(f"   The following records were found for Teacher ID = {teacher_id_input}:")
    print("====================================================\n")
    i = 1
    print("\n====================================================")
    for record in matching_records:
        print(f"{i}. Day: {record['Day']} - Instructor: {record['Instructor']} - Available Time: {record['Available time']}")
        i += 1
    print("====================================================\n")
    # Ask the user to select which record to update
    while True:
        try:
            choice = int(input("Please select a record number to update: "))
            if 1 <= choice <= len(matching_records):
                break
            else:
                print(f"Invalid selection. Please enter a number between 1 and {len(matching_records)}.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Retrieve the chosen record
    selected_record = matching_records[choice - 1]

    # Prompt the user to enter the new available time
    new_time = input("Please enter the new Available Time: ").strip()
    if new_time:
        try:
            start_time, end_time = new_time.split("-")
            datetime.strptime(start_time, "%H:%M")
            datetime.strptime(end_time, "%H:%M")

            # Update only if time format is valid
            selected_record["Available time"] = new_time
            print("Available Time updated successfully!")

        except (ValueError, IndexError):
            print("Invalid time slot format! Please use HH:MM-HH:MM format. (e.g. 12:00-14:00)")

    else:
        print("No new Available Time was entered.")

    # Write the updated teacher records back to teachers.txt
    with open("teachers.txt", "w") as f:
        for t in teachers:
            f.write(f"{t['Teacher ID']},{t['Day']},{t['Instructor']},{t['Available time']}\n")

def course_creation_and_management_menu():
    # Main menu for course management functions
    while True:
        courses = open_course()
        print("\n------------------------------------------------------")
        print("--------- Course Creation and Management Menu --------")
        print("------------------------------------------------------")
        print("1. Create course (after teacher verification)")
        print("2. Update course")
        print("3. View all courses")
        print("4. Schedule")
        print("5. Exit")
        print("------------------------------------------------------")

        try:
            opt = int(input("Please enter your choice (1-5): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue

        if opt == 1:
            teacher_create_course()  # Create new course
        elif opt == 2:
            update_course()  # Update existing course
        elif opt == 3:
            view_course(courses)  # View all courses
        elif opt == 4:
            schedule()  # Update teacher schedule
        elif opt == 5:
            print("Exiting course management menu.")
            break
        else:
            print("Invalid selection, please enter a number between 1 and 5.")


# function 2:Student Enrolment Functions
def course_exists(course_id):
    courses = open_course()
    if courses is None:
        return False
    for course in courses:
        if course["Course ID"].upper() == course_id.upper():
            return True  # Course found
    return False  # Course does not exist


def student_enroll(enrolments):
    enrolled = open_enrolments()
    students = open_students()

    if students is None:
        return
    if enrolled is None:
        return

    print("\n=== Student Enrolment ===")
    for enrol in enrolled:
        print(f"Student ID: {enrol['Student ID']}, Course ID: {enrol['Course ID']}")
    print("--------------------------------------------------")
    print("\n=== Available Students ===")
    for student in students:
        print(f"Student ID: {student['Student ID']}, Name: {student['Name']}")  # Display each student
    print("--------------------------------------------------")

    while True:
        student_id = input("Enter Student ID: ").upper()
        student_name = input("Enter Student Name: ")
        if student_id == "" or student_name == "":
            print("No data is entered. Returning to menu.")
            return

        found = False
        for s in students:
            if s["Student ID"].upper() == student_id and s["Name"].lower() == student_name.lower():
                found = True
                break

        if not found:
            print("Error: This student (ID & Name) was not found in students.txt. Please try again.\n")
            continue

        course_id = input("Enter Course ID: ").strip().upper()
        if not course_id:
            print("Error: Course ID is required. Please try again.\n")
            continue

        if not course_exists(course_id):
            print("Error: The course does not exist in course.txt. Cannot enrol student in a non-existing course.\n")
            return

        exists = False
        for e in enrolments:
            if e["Student ID"].upper() == student_id and e["Course ID"].upper() == course_id:
                exists = True
                break
        if exists:
            print("Error: The enrolment already exists. Please try again.\n")
            continue

        new_enrolment = {
            "Student ID": student_id,
            "Course ID": course_id,
        }
        enrolments.append(new_enrolment)
        save_enrolments(enrolments)
        print("--------------------------------------------------")
        print("Student enrolment successful!\n")
        print(f"1. Student ID: {new_enrolment['Student ID']}")
        print(f"2. Course ID: {new_enrolment['Course ID']}")
        print("--------------------------------------------------")
        input("Press Enter to continue...")
        break


def remove_student():
    try:
        with open('enrolments.txt', 'r') as wFile:
            content = wFile.read()
            print("Current Enrolments:")
            print(content)
    except FileNotFoundError:
        print("Warning: enrolments.txt not found.")

    enrolments = open_enrolments()
    if enrolments is None:
        return

    print("\n=== Remove Student Enrolment ===")
    student_id = input("Enter Student ID to remove: ").strip().upper()
    course_id = input("Enter Course ID to remove: ").strip().upper()

    updated_enrolments = [e for e in enrolments if
                          not (e["Student ID"].upper() == student_id and e["Course ID"].upper() == course_id)]

    if len(updated_enrolments) == len(enrolments):
        print("Error: No matching enrolment found for the given Student ID and Course ID.\n")
    else:
        save_enrolments(updated_enrolments)
        print(f"Enrolment for Student ID {student_id} in Course ID {course_id} removed successfully!\n")
        input("Press Enter to continue...")


def student_enrolment_menu():
    while True:
        enrolments = open_enrolments()
        if enrolments is None:
            return

        print("\n------------------------------------------------------")
        print("---------------- Student Enrolment -------------------")
        print("------------------------------------------------------")
        print("1. Enrol Student")
        print("2. Remove Student")
        print("3. Exit")
        print("------------------------------------------------------")

        try:
            opt = int(input("Please enter your choice (1-3): "))
        except ValueError:
            print("Invalid input! Only integers 1-3 are allowed.")
            continue

        if opt == 1:
            student_enroll(enrolments)
        elif opt == 2:
            remove_student()
        elif opt == 3:
            print("Returning to main menu.")
            break
        else:
            print("Invalid choice, please enter a number between 1 and 3.")


# function 3:Grade and Assessment Functions
def display_enrolments():
    enrolments = open_enrolments()
    if enrolments is None or len(enrolments) == 0:
        print("No enrolment records found.")
        return
    print("\n=== Current Enrolment Records ===")
    for rec in enrolments:
        print("Student ID:", rec["Student ID"], "| Course ID:", rec["Course ID"])  # Display each enrolment
    print("---------------------------------\n")


def grading_assignment_score():
    display_enrolments()  # Show enrolment records
    student_id = input("Enter student ID: ").strip().upper()
    course_id = input("Enter course ID: ").strip().upper()

    if not verify_enrollment(student_id, course_id):
        print("Error: This student is not enrolled in the specified course.")
        return

    data = open_grades()
    if data is None:
        return

    record = None
    for rec in data:
        if rec["student ID"] == student_id and rec["course ID"] == course_id:
            record = rec
            break

    if record is None:
        # Create new grade record if not exists
        record = {
            "student ID": student_id,
            "course ID": course_id,
            "assignment score": "",
            "exam score": "",
            "gpa": "",
            "feedback": "",
            "performance": ""
        }
        data.append(record)

    try:
        score = float(input("Enter assignment score (0-100): "))
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return
    if not 0 <= score <= 100:
        print("Score must be between 0 and 100!")
        return
    record["assignment score"] = str(score)  # Update assignment score
    save_grades(data)
    print("Assignment score saved successfully.")
    print("You entered assignment score: {:.2f}%".format(score))


def grading_exam_score():
    display_enrolments()  # Display enrolments
    student_id = input("Enter student ID: ").strip().upper()
    course_id = input("Enter course ID: ").strip().upper()

    if not verify_enrollment(student_id, course_id):
        print("Error: This student is not enrolled in the specified course.")
        return

    data = open_grades()
    if data is None:
        return

    record = None
    for rec in data:
        if rec["student ID"] == student_id and rec["course ID"] == course_id:
            record = rec
            break

    if record is None:
        # Create new record if not exists
        record = {
            "student ID": student_id,
            "course ID": course_id,
            "assignment score": "",
            "exam score": "",
            "gpa": "",
            "feedback": "",
            "performance": ""
        }
        data.append(record)

    try:
        score = float(input("Enter exam score (0-100): "))
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return
    if not 0 <= score <= 100:
        print("Score must be between 0 and 100!")
        return
    record["exam score"] = str(score)  # Update exam score
    save_grades(data)
    print("Exam score saved.")
    print("You entered exam score: {:.2f}%".format(score))


def grading_gpa():
    display_enrolments()  # Show enrolment records
    student_id = input("Enter student ID: ").strip().upper()
    course_id = input("Enter course ID: ").strip().upper()

    if not verify_enrollment(student_id, course_id):
        print("Error: This student is not enrolled in the specified course.")
        return

    data = open_grades()
    if data is None:
        return

    record = None
    for rec in data:
        if rec["student ID"] == student_id and rec["course ID"] == course_id:
            record = rec
            break

    if record is None:
        record = {
            "student ID": student_id,
            "course ID": course_id,
            "assignment score": "",
            "exam score": "",
            "gpa": "",
            "feedback": "",
            "performance": ""
        }
        data.append(record)

    try:
        assignment = float(record.get("assignment score", 0))
        exam = float(record.get("exam score", 0))
    except ValueError:
        print("Existing score data is invalid!")
        return

    avg = (assignment + exam) / 2  # Calculate average score
    # Determine GPA based on average
    if avg >= 80:
        gpa = "4.0"
    elif avg >= 75:
        gpa = "3.7"
    elif avg >= 70:
        gpa = "3.3"
    elif avg >= 65:
        gpa = "3.0"
    elif avg >= 60:
        gpa = "2.7"
    elif avg >= 55:
        gpa = "2.3"
    elif avg >= 50:
        gpa = "2.0"
    else:
        gpa = "Fail"
    record["gpa"] = gpa  # Update GPA
    save_grades(data)
    print("GPA calculated:", gpa)
    print("Calculated using assignment score:", assignment, "and exam score:", exam)
    input("Press Enter to continue...")


def give_feedback():
    display_enrolments()  # Show enrolment records
    student_id = input("Enter student ID: ").strip().upper()
    course_id = input("Enter course ID: ").strip().upper()

    if not verify_enrollment(student_id, course_id):
        print("Error: This student is not enrolled in the specified course.")
        return

    data = open_grades()
    if data is None:
        data = []

    record = None
    for rec in data:
        if rec["student ID"] == student_id and rec["course ID"] == course_id:
            record = rec
            break

    if record is None:
        # Create new record if none exists
        record = {
            "student ID": student_id,
            "course ID": course_id,
            "assignment score": "",
            "exam score": "",
            "gpa": "",
            "feedback": "",
            "performance": ""
        }
        data.append(record)

    feedback = input("Enter feedback evaluation: ")
    record["feedback"] = feedback  # Update feedback field
    save_grades(data)
    print("Feedback evaluation saved.")
    print("You entered feedback:", feedback)


def grade_and_assessment_menu():
    while True:
        print("\n------------------------------------------------------")
        print("--------- Grade and Assessment Menu ---------")
        print("------------------------------------------------------")
        print("1. Grade Assignment Score")
        print("2. Grade Exam Score")
        print("3. Calculate GPA")
        print("4. Give Feedback")
        print("5. Exit")
        print("------------------------------------------------------")
        try:
            opt = int(input("Please enter your choice (1-5): "))
        except ValueError:
            print("Invalid input! Only integers 1-5 are allowed.")
            continue
        if opt == 1:
            grading_assignment_score()
        elif opt == 2:
            grading_exam_score()
        elif opt == 3:
            grading_gpa()
        elif opt == 4:
            give_feedback()
        elif opt == 5:
            print("Returning to main menu...")
            break
        else:
            print("Invalid choice, please enter a number between 1 and 5.")


# function 4:Attendance Tracking Functions
def upload_or_update_attendance():
    print("\n--- Upload/Update Attendance Page---")
    display_enrolments()  # Show enrolment records
    student_id = input("Enter student ID: ").strip().upper()
    course_id = input("Enter course ID: ").strip().upper()

    if not verify_enrollment(student_id, course_id):
        print("Error: Please enrol student into course.")
        return

    event_att = input("Enter Event Attendance (e.g. 1/4) [press Enter to skip]: ").strip()
    course_att = input("Enter Course Attendance: ").strip()

    attendances = open_attendances()
    if attendances is None:
        attendances = []

    record = None
    for att in attendances:
        if att["Student ID"].upper() == student_id:
            record = att
            break

    if record is None:
        # Create a new attendance record for the student
        record = {
            "Student ID": student_id,
            "Event Attendance": "",
            "Course 1": "",
            "Course 1 Attendance": "",
            "Course 2": "",
            "Course 2 Attendance": "",
            "Course 3": "",
            "Course 3 Attendance": "",
            "Course 4": "",
            "Course 4 Attendance": "",
            "Course 5": "",
            "Course 5 Attendance": "",
            "Total Attendance": ""
        }
        attendances.append(record)

    if event_att:
        record["Event Attendance"] = event_att  # Update event attendance

    course_found = False
    for i in range(1, 6):
        if record.get(f"Course {i}").strip().upper() == course_id:
            record[f"Course {i} Attendance"] = course_att  # Update existing course attendance
            course_found = True
            break

    if not course_found:
        assigned = False
        for i in range(1, 6):
            if not record.get(f"Course {i}").strip():
                record[f"Course {i}"] = course_id  # Assign course if empty slot is found
                record[f"Course {i} Attendance"] = course_att
                assigned = True
                break
        if not assigned:
            print("Warning: This student already has 5 courses filled. No more courses can be added.")

    recalc_total_attendance(record)  # Recalculate total attendance

    with open("attendances.txt", "w") as f:
        for att in attendances:
            line = ",".join([
                att["Student ID"],
                att["Event Attendance"],
                att["Course 1"],
                att["Course 1 Attendance"],
                att["Course 2"],
                att["Course 2 Attendance"],
                att["Course 3"],
                att["Course 3 Attendance"],
                att["Course 4"],
                att["Course 4 Attendance"],
                att["Course 5"],
                att["Course 5 Attendance"],
                att["Total Attendance"]
            ])
            f.write(line + "\n")

    print("\n--- Attendance Record Updated Successfully ---")
    print("Student ID:        " + record["Student ID"])
    print("Event Attendance:  " + record["Event Attendance"])
    print("Course ID:         " + course_id)
    print("Course Attendance: " + course_att)


def attendance_tracking_menu():
    while True:
        print("\n----------- Attendance System Menu -----------")
        print("1) Upload/Update Attendance")
        print("2) Exit")
        choice = input("Please choose (1-2): ").strip()
        if choice == "1":
            upload_or_update_attendance()
        elif choice == "2":
            print("Program terminated.")
            break
        else:
            print("Invalid input, please choose 1 or 2.\n")


# function 5:Report Generation Functions
def generation_performances(grades):
    print("=== Performance Report (Grades) ===")
    student_id = input("Please enter the student ID to view grades (leave blank to view all): ").strip().upper()
    if not student_id:
        selected_records = grades  # Show all if blank
    else:
        selected_records = [record for record in grades if record["student ID"] == student_id]
    if not selected_records:
        print("No grade records found for the specified student or no records at all.")
        return
    for record in selected_records:
        print(f"Student ID: {record['student ID']}")
        print(f"Course ID: {record['course ID']}")
        print(f"Assignment Score: {record['assignment score']}")
        print(f"Exam Score: {record['exam score']}")
        print(f"GPA: {record['gpa']}")
        print(f"Feedback: {record['feedback']}")
        print("--------------------------------------------------")


def generation_participation(attendances):
    print("=== Participation Report (Attendances) ===")
    student_id = input("Please enter the student ID to view attendance (leave blank to view all): ").strip().upper()

    if not student_id:
        selected_records = attendances  # Display all records if blank
    else:
        selected_records = [record for record in attendances if record["Student ID"].upper() == student_id]

    if not selected_records:
        print("No attendance records found for the specified student or no records at all.")
        return

    for record in selected_records:
        print(f"Student ID: {record['Student ID']}")
        print(f"Event Attendance: {record['Event Attendance']}")
        for i in range(1, 6):
            course_key = f"Course {i}"
            att_key = f"Course {i} Attendance"
            course_name = record.get(course_key, "").strip()
            course_att = record.get(att_key, "").strip()
            if course_name:
                print(f"{course_key}: {course_name}")
                print(f"{course_key} Attendance: {course_att}")
        print(f"Total Attendance: {record['Total Attendance']}")
        print("--------------------------------------------------")


def report_generation_menu():
    while True:
        grades = open_grades()
        attendances = open_attendances()

        print("\n------------------------------------------------------")
        print("---------------- Student Reports ---------------------")
        print("------------------------------------------------------")
        print("1. Generate Performance Report")
        print("2. Generate Attendance Report")
        print("3. Exit")
        print("------------------------------------------------------")

        try:
            opt = int(input("Please enter your choice (1-3): "))
        except ValueError:
            print("Invalid input! Only integers 1-3 are allowed.")
            continue

        if opt == 1:
            generation_performances(grades)
        elif opt == 2:
            generation_participation(attendances)
        elif opt == 3:
            print("Returning to main menu.")
            break
        else:
            print("Invalid choice, please enter a number between 1 and 3.")


def main_menu():
    while True:
        # ... Print your main menu header ...

        print("\n------------------------------------------------------")
        print("---------Teacher Management System--------------------")
        print("------------------------------------------------------")
        print("1. Course Creation and Management")
        print("2. Student Enrolment")
        print("3. Grade and Assessment")
        print("4. Attendances Tracking")
        print("5. Report Generation")
        print("6. Exit")
        print("------------------------------------------------------")

        try:
            selection = int(input("Please enter your choice (1-6): "))
            if selection == 1:
                course_creation_and_management_menu()
            elif selection == 2:
                student_enrolment_menu()
            elif selection == 3:
                grade_and_assessment_menu()
            elif selection == 4:
                attendance_tracking_menu()
            elif selection == 5:
                report_generation_menu()
            elif selection == 6:
                print("Thank you for visiting the system.\nExiting Teacher Management Page...")
                break
            else:
                print("Invalid choice! Please enter a number between 1 and 6.\n")
        except ValueError:
            print("Invalid input! Only integers 1–6 are allowed.\nPlease try again.")


# main_menu()
