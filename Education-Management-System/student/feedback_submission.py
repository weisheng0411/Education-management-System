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
        name = input("Enter your name: ").strip().title()
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

# feedback_menu()
