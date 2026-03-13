import random

def open_students():
    students=[] #create an empty list to store student data
    try:
        with open("students.txt", 'r') as tFile:
            for line in tFile:
                line=line.rstrip().split(",") #split each line become a list and remove whitespace
                #set the limit of the append block inside the list
                #leave empty column when the data input is always less than 9
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
                    "Tuition Fees":line[7],
                    "Payment":line[8]
                }
                students.append(student) #add student dictionary to the list
            return students # return the list containing student dictionary
    except FileNotFoundError:
        print("Warning: 'students.txt' not found. Returning to main menu..")
    return None

def update_student_status(pupil_id,new_status):
    students=open_students() #read students list from students.txt
    update=False #check if the update is success

    for student in students:
        if student['Student ID']==pupil_id: #if student id is found
            student['Student Status']=new_status #change the student status to new_status
            update=True #set the update status is true as update success
            break

    if update:
        print("Update successful! New student list:")
        # update the new_status to students.txt
        with open("students.txt", 'w')as tFile:
            for student in students:
                #combine the elements of a dictionary in file into single string separate by ','
                tFile.write(",".join(student.values()) + "\n")
                print(f"Student ID:{student['Student ID']}\t\tStudent Name:{student['Name']}\t\tContact:{student['Contact']}\t\tGender:{student['Gender']}\t\tStudent status:{student['Student Status']}")
    else:
        print("Updating issue occur")

def generate_id():
    students = open_students()
    while True:
        student_id = f"TP{random.randint(1, 99):02d}{random.randint(1, 99):02d}{random.randint(1, 99):02d}" #generate random student ID
        if student_id not in students:
            return student_id

def register_student():
    students = open_students()  # Ensure the file exists before registration
    if students is None:  # If the file was missing, stop execution
        return

    while True:
        try:
            name = str(input("Please enter the student's name:")).title()
            while True:
                contact = input("Please enter the student's contact:")
                if contact.isdigit(): #valid the input is all digit
                    break
                print("Invalid input. Please enter integer only!")

            while True:
                try:
                    gender = str(input("Please enter the student's gender(Male/Female):")).capitalize()
                    if gender not in ["Male", "Female"]: #valid the input only male and female
                        raise ValueError("Invalid input. Please enter Male or Female only.")
                    break
                except ValueError as e:
                    print(e)

            student_status="Active" #automatic register new student as 'Active' status
            register_id = generate_id()
            #leave empty space to update by other role
            email=" "
            emergency_contact=" "
            tuition_fees=" "
            payment=" "

            # ensure all information store in list with empty values also
            new_student = [register_id,name,email or " ",contact,emergency_contact or " ",gender,student_status,tuition_fees or " ",payment or " "]

            # append new student to the students.txt file
            with open("students.txt", 'a') as tFile:
                #convert the list into single string
                tFile.write(",".join(new_student)+"\n")

            print("\nRegister successful!\n")
            print(f"Assigned Student ID:{register_id}")
            print(f"Student Name:{name}\nContact:{contact}\nGender:{gender}\nStudent status:{student_status}")
            break

        except Exception as e:
            print(f"Invalid input!{e} has occur!")

def action(pupil_id):
    students = open_students()
    while True:
        print("\nAction list:")
        print("1. Check Information")
        print("2. Student Transfer")
        print("3. Student Withdraw")
        print("4. Exit")

        try:
            selection = int(input("Please choose an action:"))
            if selection == 1:
                for student in students:
                    if student['Student ID']==pupil_id:
                        print(f"Student ID:{student['Student ID']}\t\tStudent Name:{student['Name']}\t\tContact:{student['Contact']}\t\tGender:{student['Gender']}\t\tCourse status:{student['Student Status']}")
            elif selection == 2:
                update_student_status(pupil_id,"Transfer")
            elif selection == 3:
                update_student_status(pupil_id,"Withdraw")
            elif selection == 4:
                print("Exiting action page...")
                return
            else:
                print("Invalid choice! Please enter again")
        except ValueError:
            print("Invalid input. Please enter number 1-3 only.")

def select_student():
    students = open_students()
    if students is None:  # If the file was missing, stop execution
        return

    # print a current student list for view
    print("Here is the current student list:\n")
    for student in students:
        print(f"Student ID:{student['Student ID']}\t\tStudent Name:{student['Name']}\t\tContact:{student['Contact']}\t\tGender:{student['Gender']}\t\tCourse status:{student['Student Status']}")
    while True:
        print("\nSelect student menu")
        print("1. Enter Student ID")
        print("2. Finish searching")

        try:
            chosen=int(input("Please select action:"))
            if chosen ==1:
                pupil_id=input("Please enter student ID: ").upper()
                for student in students:
                    if student['Student ID']==pupil_id: #check if pupil_id is in the student_list['Student ID']
                        action(pupil_id) #call the action function with list that contain same pupil_id
                        break
                else:
                    print("Student not found!")
                    continue
            elif chosen==2:
                print("Thanks for searching. Exiting searching page...")
                break
            else:
                print("Invalid choice!")
        except ValueError:
            print("Invalid input! Please enter number 1-2 only.")

def student_record_menu():
    while True:
        print("")
        title = "Student Records Page"
        width = 40
        print("=" * width)
        print(title.center(width))
        print("=" * width)
        print("1. Register New Student")
        print("2. Check Active Student")
        print("3. Exit")

        try:
            choose=int(input("\nEnter your action:"))
            if choose ==1 :
                register_student()
            elif choose==2:
                select_student()
            elif choose==3:
                print("Thank you for visiting!")
                break
            else:
                print("Invalid choice!")
        except ValueError:
            print("Invalid input! Only integer 1-3 is allowed.")

# student_record_menu()
