def open_enrolments():
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

def verify_enrollment(student_id, course_id):
    """
    Check if the (student_id, course_id) pair exists in enrolments.txt.
    Returns True if found, otherwise False.
    """
    enrolments = open_enrolments()
    if enrolments is None:
        return False
    for e in enrolments:
        if e["Student ID"] == student_id and e["Course ID"] == course_id:
            return True
    return False

def open_attendances():
    attendances = []
    try:
        with open("attendances.txt", "r") as record:
            for line in record:
                fields = line.rstrip().split(',')
                while len(fields) < 13:
                    fields.append("")
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
        return attendances
    except FileNotFoundError:
        print("Error: attendances.txt not found.")
        return None

def parse_attendance(att_str):
    att_str = att_str.strip()
    if not att_str:
        return (0, 0)
    try:
        attended, total = att_str.split("/")
        return int(attended.strip()), int(total.strip())
    except:
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
        if record[key]:
            ca, ct = parse_attendance(record[key])
            total_attended += ca
            total_possible += ct
    if total_possible == 0:
        record["Total Attendance"] = ""
    else:
        record["Total Attendance"] = str(total_attended) + "/" + str(total_possible)

def upload_or_update_attendance():
    print("\n--- Upload/Update Attendance ---")
    # First, get both student ID and course ID
    student_id = input("Enter Student ID: ").strip().upper()
    course_id = input("Enter Course ID: ").strip().upper()

    # Validate student and course existence and enrollment
    if not verify_enrollment(student_id, course_id):
        print("Error: This student is not enrolled in the specified course.")
        return

    # Now prompt for attendance inputs
    event_att = input("Enter Event Attendance (e.g., 1/4) [press Enter to skip]: ").strip()
    course_att = input("Enter Course Attendance: ").strip()

    # Read existing attendance records; if none, use an empty list
    attendances = open_attendances()
    if attendances is None:
        attendances = []

    # Look for an existing record for the student
    record = None
    for att in attendances:
        if att["Student ID"].upper() == student_id:
            record = att
            break

    # If no record exists, create a new blank record for the student
    if record is None:
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

    # Update Event Attendance if provided
    if event_att:
        record["Event Attendance"] = event_att

    # Check if the specified course is already in the record.
    # If it exists, update its attendance; otherwise, add it in the first empty slot.
    course_found = False
    for i in range(1, 6):
        if record["Course " + str(i)].strip().upper() == course_id:
            record["Course " + str(i) + " Attendance"] = course_att
            course_found = True
            break

    if not course_found:
        assigned = False
        for i in range(1, 6):
            if not record["Course " + str(i)].strip():
                record["Course " + str(i)] = course_id
                record["Course " + str(i) + " Attendance"] = course_att
                assigned = True
                break
        if not assigned:
            print("Warning: This student already has 5 courses filled. No more courses can be added.")

    recalc_total_attendance(record)

    # Write updated records back to attendances.txt
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

# Run the menu
# attendance_tracking_menu()
