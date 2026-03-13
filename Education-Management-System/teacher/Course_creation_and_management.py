def open_teacher():
    """
    Load teacher data from teachers.txt.
    Each line: Teacher ID, Day, Instructor, Available time
    """
    teachers = []
    try:
        with open("teachers.txt", "r") as f:
            for line in f:
                parts = line.rstrip().split(",")
                if len(parts) < 4:
                    print("Warning: Incomplete teacher record found and skipped.")
                    continue
                teacher = {
                    "Teacher ID": parts[0].strip().upper(),
                    "Day": parts[1].strip(),
                    "Instructor": parts[2].strip(),
                    "Available time": parts[3].strip()
                }
                teachers.append(teacher)
        return teachers
    except FileNotFoundError:
        print("Warning: teachers.txt not found.")
        return None  # Return an empty list if file not found

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
                    f"{course['Instructor']},{course['Assignment']},{course['Lecture Notes']},{course['Announcement']}"
                    f"{course['Lesson Plan']}\n")

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

 # Check if course ID already exists
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

    if not (course_id and course_name and assignment and lecture_notes and lesson_plan):
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

    # *Writing to file directly inside the function*
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

    # *Displaying updated courses*
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
            print("Invalid choice, please enter a number between 1 and 6.")


def view_course(courses):
    print("\n=== Course List ===")
    if not courses:
        print("No course records available.")
    else:
        counter = 1
        for course in courses:
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
        print(
            f"{i}. Day: {record['Day']} - Instructor: {record['Instructor']} - Available Time: {record['Available time']}")
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
    # We expect a format like: HH:MM-HH:MM (e.g., 12:00-14:00)
    new_time = input("Please enter the new Available Time (HH:MM-HH:MM): ").strip()
    if not new_time:
        print("No new Available Time was entered.")
        return

    # Check if the input contains exactly one '-'
    if "-" not in new_time:
        print("Invalid time slot format! Please use HH:MM-HH:MM format. (e.g. 12:00-14:00)")
        return

    # Split into start_time and end_time
    start_time_str, end_time_str = new_time.split("-", 1)

    # Helper function to check HH:MM format manually
    def is_valid_hhmm_format(time_str):
        # Must contain a colon
        if ":" not in time_str:
            return False
        parts = time_str.split(":")
        if len(parts) != 2:
            return False

        hour_str, minute_str = parts[0], parts[1]
        # Check that hour and minute are digits
        if not (hour_str.isdigit() and minute_str.isdigit()):
            return False

        hour = int(hour_str)
        minute = int(minute_str)

        # Hour must be 0–23, minute must be 0–59
        if not (0 <= hour <= 23):
            return False
        if not (0 <= minute <= 59):
            return False

        return True

    # Validate both start_time and end_time
    if not (is_valid_hhmm_format(start_time_str) and is_valid_hhmm_format(end_time_str)):
        print("Invalid time slot format! Please use HH:MM-HH:MM format. (e.g. 12:00-14:00)")
        return

    # If everything is valid, update the record
    selected_record["Available time"] = new_time
    print("Available Time updated successfully!")

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

# Run the main menu
course_creation_and_management_menu()
