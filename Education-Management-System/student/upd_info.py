
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

# information_menu()
