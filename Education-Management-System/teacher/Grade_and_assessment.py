def open_enrolments():
    """
    Reads 'enrolments.txt' and returns a list of dictionaries.
    Each dictionary contains "Student ID" and "Course ID".
    """
    enrolments = []
    try:
        with open("enrolments.txt", "r") as f:
            for line in f:
                fields = line.rstrip().split(",")
                if len(fields) < 2:
                    print("Skipping invalid enrolment line:", line.strip())
                    continue
                enrolment = {
                    "Student ID": fields[0].strip().upper(),
                    "Course ID": fields[1].strip().upper()
                }
                enrolments.append(enrolment)
        return enrolments
    except FileNotFoundError:
        print("Warning: enrolments.txt not found.")
    return None


def display_enrolments():
    """
    Displays the current enrolment records.
    """
    enrolments = open_enrolments()
    if enrolments is None or len(enrolments) == 0:
        print("No enrolment records found.")
        return
    print("\n=== Current Enrolment Records ===")
    for rec in enrolments:
        print("Student ID:", rec["Student ID"], "| Course ID:", rec["Course ID"])
    print("---------------------------------\n")


def verify_enrollment(student_id, course_id):
    """
    Checks if the (student_id, course_id) pair exists in enrolments.txt.
    Returns True if found, otherwise False.
    """
    enrolments = open_enrolments()
    if enrolments is None:
        return
    for e in enrolments:
        if e["Student ID"] == student_id and e["Course ID"] == course_id:
            return True
    return False


def open_grades():
    """
    Reads 'grades.txt' and returns a list of dictionaries.
    Each record contains:
      "student ID", "course ID", "assignment score", "exam score",
      "gpa", "feedback", "performance"
    """
    grades = []
    try:
        with open("grades.txt", "r") as f:
            for line in f:
                fields = line.rstrip().split(",")
                if len(fields) < 6:
                    print("Skipping invalid line:", line.strip())
                    continue
                record = {
                    "student ID": fields[0].strip().upper(),
                    "course ID": fields[1].strip().upper(),
                    "assignment score": fields[2].strip(),
                    "exam score": fields[3].strip(),
                    "gpa": fields[4].strip(),
                    "feedback": fields[5].strip(),
                    "performance": fields[6].strip() if len(fields) >= 7 else ""
                }
                grades.append(record)
        return grades
    except FileNotFoundError:
        print("Warning: 'grades.txt' not found.")
    return None


def save_grades(data):
    """
    Writes the grades records to 'grades.txt'.
    Each record is written as a line with comma-separated fields.
    """
    with open("grades.txt", "w") as f:
        for record in data:
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


def Grading_assignment_score():
    """
    Grades an assignment:
      1. Displays current enrolment records.
      2. Prompts for student ID and course ID, and verifies the enrollment.
      3. Checks if a grade record exists in 'grades.txt'; if not, creates one.
      4. Updates the assignment score and saves the record.
    """
    display_enrolments()
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
        score = float(input("Enter assignment score (0-100): "))
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return
    if not 0 <= score <= 100:
        print("Score must be between 0 and 100!")
        return
    record["assignment score"] = str(score)
    save_grades(data)
    print("Assignment score saved successfully.")
    print("You entered assignment score: {:.2f}%".format(score))


def Grading_exam_score():
    """
    Grades an exam:
      - Displays enrolment records, verifies enrollment, then either finds or creates the grade record.
      - Updates the exam score and saves the record.
    """
    display_enrolments()
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
        score = float(input("Enter exam score (0-100): "))
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return
    if not 0 <= score <= 100:
        print("Score must be between 0 and 100!")
        return
    record["exam score"] = str(score)
    save_grades(data)
    print("Exam score saved.")
    print("You entered exam score: {:.2f}%".format(score))


def Grading_gpa():
    """
    Calculates GPA:
      - Displays enrolment records, prompts for student and course IDs, and verifies enrollment.
      - Retrieves the grade record (or creates one if missing), calculates GPA based on the
        assignment and exam scores, and saves the record.
    """
    display_enrolments()
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

    avg = (assignment + exam) / 2
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
    record["gpa"] = gpa
    save_grades(data)
    print("GPA calculated:", gpa)
    print("Calculated using assignment score: {} and exam score: {}".format(assignment, exam))
    input("Press Enter to continue...")


def Give_feedback():
    """
    Records feedback:
      - Displays enrolment records, prompts for student and course IDs, and verifies enrollment.
      - If a grade record is missing, a new one is created.
      - Updates the feedback and saves the record.
    """
    display_enrolments()
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
    record["feedback"] = feedback
    save_grades(data)
    print("Feedback evaluation saved.")
    print("You entered feedback:", feedback)


def Grade_and_Assessment_Menu():
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
            Grading_assignment_score()
        elif opt == 2:
            Grading_exam_score()
        elif opt == 3:
            Grading_gpa()
        elif opt == 4:
            Give_feedback()
        elif opt == 5:
            print("Returning to teacher menu...")
            break
        else:
            print("Invalid choice, please enter a number between 1 and 5.")


# Run the Grade and Assessment Menu
# Grade_and_Assessment_Menu()
