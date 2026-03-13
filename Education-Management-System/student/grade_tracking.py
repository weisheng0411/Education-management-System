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

    print("\nStudent ID not found or no enrolled courses. Please check your TP number.")

#grades_menu()
