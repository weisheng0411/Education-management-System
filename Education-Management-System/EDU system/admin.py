from datetime import datetime

#Function 1: System Administration
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

def update_account():
    accounts=open_accounts()
    if accounts is None: #if file not found ,return to menu
        return
    print()
    print("-"*30,"User Accounts","-"*30)
    index=1
    with open("accounts.txt",'w')as login:
        for account in accounts:
            login.write(",".join(account.values())+"\n")
            print(f"{index}. Role:{account['Role']:<10}\t\tUsername:{account['Username']:<10}\t\tPassword:{account['Password']:<10}")
            print("-"*75)
            index+=1

def manage_account():
    accounts=open_accounts()
    if accounts is None: #if file not found ,return to menu
        return
    while True:
        print("-"*40,"Action Menu","-"*40)
        print("1. Create Account")
        print("2. Edit Account")
        print("3. Delete Account")
        print("4. Exit")

        try:
            selection = int(input("\nPlease Enter your choice:"))
            if selection==1:
                print("-" * 40, "CREATING ACCOUNT PAGE", "-" * 40)
                while True:
                    try:
                        role=input("Enter the role of user (Student/Staff/Teacher):").capitalize()
                        if role not in ["Student","Staff","Teacher"]:  # valid the input
                            raise ValueError("Invalid input. Please enter Student/Staff/Teacher only.")
                        break
                    except ValueError as e:
                        print(e)

                while True:
                    username=input("Enter the username of the user:").upper()
                    password=input("Enter the password of the user:")

                    exists = False
                    for acc in accounts:
                        if acc["Username"] == username and acc["Role"] == role:
                            exists = True
                            break
                    if exists:
                        print("\nThe account already exists. Please enter a different username or role.\n")
                    else:
                        new_account=f"{role},{username},{password}"
                        with open("accounts.txt", 'a') as login:
                            login.write(new_account+"\n")

                        print("\nAccount created successful!\n")
                        accounts = open_accounts()  # Reload accounts list after adding a new account
                        update_account()
                        break

            elif selection == 2:
                print("-" * 40, "EDITING ACCOUNT PAGE", "-" * 40)
                update_account()
                while True:
                    try:
                        num = int(input("Enter the number of account to edit: "))
                        if 1 <= num <= len(accounts):
                            account = accounts[num - 1]  # get the selected event dictionary from list
                            part = input("Please enter the field of the account to edit(Role/Username/Password):").title()
                            if part not in account:
                                print("The field you enter is not found in the account page. Please enter again.\n")
                                continue

                            # edit the part to whatever new
                            edition = input(f"Edit {part} to :").strip()

                            account[part] = edition  # change the part to edition entered
                            with open("accounts.txt", 'w') as vFile:
                                for account in accounts:
                                    vFile.write(",".join(account.values()) + "\n")

                            print("Account edited!\n")
                            print("-" * 50, "Update User Account", "-" * 50)
                            update_account()
                            break
                        else:
                            print("Invalid number. Please enter bill in the Account Page!")
                    except ValueError:
                        print("Invalid input. Please enter a valid number.\n")
            elif selection == 3:
                print("-" * 40, "DELETING ACCOUNT PAGE", "-" * 40)
                update_account()
                line_number = int(input("Enter the number of account needs to delete:"))
                if 1 <= line_number <= len(accounts):
                    # delete the real number in the list
                    del accounts[line_number - 1]

                    # update the delete list to the file
                    with open("accounts.txt", 'w') as vFile:
                        for account in accounts:
                            vFile.write(",".join(account.values()) + "\n")

                    print("Account deleted!\n")
                    print("-" * 50, "Update User Account", "-" * 50)
                    accounts = open_accounts()  # Reload the list after deletion
                    update_account()
                else:
                    print("The number is not in Account Page.")
                    continue
            elif selection==4:
                print("Skipping Page...")
                break
            else:
                print("Please enter number 1-3 only.")
        except ValueError:
            print("Invalid input. Only integer 1-3 is allowed.")

def system_administration_menu():
    while True:
        print("")
        title = "System Administration Page"
        width = 40
        print("=" * width)
        print(title.center(width))
        print("=" * width)
        print("1. View User Accounts")
        print("2. Manage User Accounts")
        print("3. Exit")

        try:
            choose=int(input("\nEnter your action:"))
            if choose ==1 :
                update_account()
            elif choose==2:
                manage_account()
            elif choose==3:
                print("Thank you for visiting!")
                break
            else:
                print("Invalid choice!")
        except ValueError:
            print("Invalid input! Only integer 1-3 is allowed.")

#Function 2: Student Management
def open_students():
    """
    This function is to open the students.txt file
    :return: return None if file not exists
    """
    students=[] #create an empty list to store student data
    try:
        with open("students.txt", 'r') as tFile:
            for line in tFile:
                line=line.rstrip().split(",") #split each line become a list and remove whitespace
                #ensure each students record has exactly 9 field by appending empty space if needed
                while len(line)<9:
                    line.append("")
                #store each list in a dictionary by identify the index number
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
            return students # return the list containing student dictionary
    except FileNotFoundError:
        print("Warning: 'students.txt' not found. Returning to main menu..")
    return None #return None if the file is not found

def view_students_records():
    students = open_students()  # Read students list from students.txt
    if students is None:  # If the file is missing, stop execution and return to menu
        return
    print("\n" + "-" * 30 + " Student Records " + "-" * 30)
    index = 1
    with open("students.txt", 'w') as tFile:
        for student in students:
            tFile.write(",".join(student.values()) + "\n")
            print(f"  Student {index}:")
            print(f"  Student ID       : {student['Student ID']}")
            print(f"  Name             : {student['Name']}")
            print(f"  Email            : {student['Email']}")
            print(f"  Contact          : {student['Contact']}")
            print(f"  Emergency Contact: {student['Emergency Contact']}")
            print(f"  Gender           : {student['Gender']}")
            print(f"  Student Status   : {student['Student Status']}")
            print(f"  Tuition Fees(RM) : {student['Tuition Fees(RM)']}")
            print(f"  Payment          : {student['Payment']}")
            print("-" * 75)
            index += 1

def open_grades():
    grades=[] #create an empty list to store grade data
    try:
        with open("grades.txt", 'r') as tFile:
            for line in tFile:
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
        print("Warning: 'grades.txt' not found. Returning to main menu..")
    return None #return None if the file is not found

def view_grades():
    grades=open_grades() # Read students list from students.txt
    if grades is None:  # If the file is missing, stop execution and return to menu
        return
    print("\n" + "-" * 30 + " Student Records " + "-" * 30)
    index = 1
    with open("grades.txt", 'w') as tFile:
        for grade in grades:
            tFile.write(",".join(grade.values()) + "\n")
            print(f"  Student {index}:")
            print(f"  Student ID       : {grade['Student ID']}")
            print(f"  Course ID        : {grade['Course ID']}")
            print(f"  Assignment Grade : {grade['Assignment Grade']}")
            print(f"  Exam Grade       : {grade['Exam Grade']}")
            print(f"  GPA              : {grade['GPA']}")
            print(f"  Performance      : {grade['Performance']}")
            print("-" * 75)
            index += 1

def update_students_records():
    students = open_students()  # Read students list from students.txt
    if students is None:  # If the file is missing, stop execution and return to menu
        return
    while True:
        view_students_records()
        while True:
            try:
                num = int(input("Enter the number of student to edit: "))
                if 1 <= num <= len(students):
                    student= students[num - 1]  # get the selected event dictionary from list
                    part = input("Please enter the field of the student to update:")
                    if part not in student:
                        print("The field you enter is not found in the student details. Please enter again.\n")
                        continue

                    # edit the part to whatever new
                    edition = input(f"Edit {part} to :").strip()

                    student[part] = edition  # change the part to edition entered
                    with open("students.txt", 'w') as vFile:
                        for student in students:
                            vFile.write(",".join(student.values()) + "\n")

                    print("Account edited!\n")
                    print("-" * 50, "Update User Account", "-" * 50)
                    print(f"  Student {num}:")
                    print(f"  Student ID       : {student['Student ID']}")
                    print(f"  Name             : {student['Name']}")
                    print(f"  Email            : {student['Email']}")
                    print(f"  Contact          : {student['Contact']}")
                    print(f"  Emergency Contact: {student['Emergency Contact']}")
                    print(f"  Gender           : {student['Gender']}")
                    print(f"  Student Status   : {student['Student Status']}")
                    print(f"  Tuition Fees(RM) : {student['Tuition Fees(RM)']}")
                    print(f"  Payment          : {student['Payment']}")
                    print("-" * 75)
                    break
                else:
                    print("Invalid number. Please enter bill in the Account Page!")
            except ValueError:
                print("Invalid input. Please enter a valid number.\n")

        proceed= input("\nProceed updating?(Y/N):").capitalize()
        if proceed== 'N':
            print("Student Records updated successfully!Exiting the page.")
            return

def update_academic_performance():
    grades=open_grades()
    if grades is None:
        return
    while True:
        view_grades()
        try:
            num = int(input("Enter the number of student to update academic performance: "))
            if 1 <= num <= len(grades):
                selected_grade= grades[num - 1]  # get the selected event dictionary from list
                if (selected_grade['Assignment Grade'] == '' and selected_grade['Exam Grade'] == ''
                        and selected_grade['GPA'] == ''):
                    print("Error: The fields of grade are empty.\nAcademic performance update fails.\nReturn to menu list.")
                    return

                try:
                    gpa = float(selected_grade['GPA'])
                except ValueError:
                    print("Error: Invalid GPA value.\nAcademic performance update fails.")
                    return

                if gpa == 4.0:
                    performance="A+"
                elif gpa >= 3.7:
                    performance="A"
                elif gpa >= 3.0:
                    performance="B"
                elif gpa >= 2.0:
                    performance="C"
                elif gpa >= 1.0:
                    performance="D"
                else:
                    performance="F"

                selected_grade['Performance']=performance

                with open("grades.txt", 'w') as tFile:
                    for grade in grades:
                        tFile.write(",".join(grade.values()) + "\n")

                print("Academic Performance Updated!\n")
                print("-" * 50, "Update Grades", "-" * 50)
                print(f"  Student {num}:")
                print(f"  Student ID       : {selected_grade['Student ID']}")
                print(f"  Course ID        : {selected_grade['Course ID']}")
                print(f"  Assignment Grade : {selected_grade['Assignment Grade']}")
                print(f"  Exam Grade       : {selected_grade['Exam Grade']}")
                print(f"  GPA              : {selected_grade['GPA']}")
                print(f"  Performance      : {performance}")
                print("-" * 75)
            else:
                print("Invalid number. Please enter bill in the student list!")
        except ValueError:
            print("Invalid input. Please enter a valid number.\n")

        proceed= input("\nProceed updating?(Y/N):").capitalize()
        if proceed== 'N':
            print("Academic Performance updated successfully!Exiting the page.")
            return

def student_management_menu():
    while True:
        print("")
        title = "Student Management Page"
        width = 40
        print("=" * width)
        print(title.center(width))
        print("=" * width)
        print("1. View Student Records")
        print("2. Update Student Records")
        print("3. Update Academic Performance")
        print("4. Exit")

        try:
            choose=int(input("\nEnter your action:"))
            if choose ==1 :
                view_students_records()
            elif choose==2:
                update_students_records()
            elif choose==3:
                update_academic_performance()
            elif choose==4:
                print("Thank you for visiting!")
                break
            else:
                print("Invalid choice!")
        except ValueError:
            print("Invalid input! Only integer 1-3 is allowed.")

#Function 3 : Course Management
def open_course():
    courses = []  # create an empty list to store student data
    try:
        with open("course.txt", 'r') as study:
            for line in study:
                line = line.rstrip().split(",")  # split each line become a list and remove whitespace
                while len(line) < 9:
                    line.append("")
                # store each list in a dictionary
                course = {
                    "Course ID": line[0],
                    "Course Name": line[1],
                    "Teacher ID":line[2],
                    "Instructor": line[3],
                    "Assignment": line[4],
                    "Lecture Notes": line[5],
                    "Announcement": line[6],
                    "Lesson Plan": line[7]
                }
                courses.append(course)  # add student dictionary to the list
        return courses
    except FileNotFoundError:
        print("Warning: 'course.txt' not found. Returning to main menu..")
    return None  # return None if the file is not found

def view_course():
    courses = open_course()
    if courses is None:
        return
    print()
    print("-" * 50, "Course Information", "-" * 50)
    index = 1
    with open("course.txt", 'w') as study:
        for course in courses:
            study.write(",".join(course.values()) + "\n")
            print(f"{index}. Course ID:{course['Course ID']:<15}\t\tCourse Name:{course['Course Name']:<15}"
                f"\t\tTeacher ID:{course['Teacher ID']:<15}Instructor:{course['Instructor']:<10}")
            print("-" * 120)
            index += 1

def create_course():
    courses=open_course()
    accounts=open_accounts()
    if courses is None:
        return
    while True:
        print("-" * 50, "CREATING COURSE PAGE", "-" * 50)
        course_id=input("Enter Course ID or enter to skip:").upper()
        course_name=input("Enter Course Name or enter to skip:").upper()

        while True:
            teacher_id=input("Enter Teacher ID:").strip().upper()
            if teacher_id=="":
                print("Teacher ID cannot be empty!")
                continue

            found=False
            for account in accounts:
                if teacher_id ==account['Username']:
                    found=True
                    break
            if found:
                break
            else:
                print("Teacher ID not found in the list. Please try again.")
                return

        instructor=input("Enter instructor name or enter to skip:").title()

        exists=False
        for course in courses:
            if course['Course ID'].strip() == "" or course['Course Name'].strip() == "":
                continue
            if course_id==course['Course ID'] and course_name==course['Course Name']:
                print(f"The course {course_id} is already exists .Please create again")
                exists=True
                break
        if not exists:
            new_course = f"{course_id},{course_name},{teacher_id},{instructor}," "," "," "," " "
            with open("course.txt", 'a') as study:
                study.write(new_course+"\n")
            print("Course create successful!")
            view_course()

        proceed = input("\nProceed creating?(Y/N):").capitalize()
        if proceed == 'N':
            print("Course creating successfully!Exiting the page.")
            return

def update_course():
    courses = open_course()
    if courses is None:
        return
    while True:
        view_course()
        try:
            num = int(input("Enter the number of course to edit: "))
            if 1 <= num <= len(courses):
                course= courses[num - 1]  # get the selected event dictionary from list
                part = input("Please enter the field of the course to update:").strip()
                if part not in course:
                    print("The field you enter is not found in the course details. Please enter again.\n")
                    continue

                # edit the part to whatever new
                edition = input(f"Edit {part} to :").strip()

                course[part] = edition  # change the part to edition entered
                with open("course.txt", 'w') as vFile:
                    for course in courses:
                        vFile.write(",".join(course.values()) + "\n")
                print("\n Course updated successfully!")
                view_course()
            else:
                print("The number you have entered is outside the range of list.Please re-enter the number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.\n")

        proceed = input("Do you want to update another course? (Y/N): ").strip().upper()
        if proceed == 'N':
            print("Course update completed. Returning to main menu.")
            break  # Exit loop

def delete_course():
    courses = open_course()
    if courses is None:
        return
    while True:
        view_course()
        try:
            num = int(input("Enter the number of  course to delete: "))
            if 1 <= num <= len(courses):
                del courses[num-1]
                with open("course.txt", 'w') as vFile:
                    for course in courses:
                        vFile.write(",".join(course.values()) + "\n")
                print("\n Course deleted successfully!")
                view_course()
            else:
                print("Invalid course number. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.\n")

        proceed = input("Do you want to delete another course? (Y/N): ").strip().upper()
        if proceed == 'N':
            print("Course deleting process completed. Returning to main menu.")
            break  # Exit loop

def course_management_menu():
    while True:
        print("")
        title = "Course Management Page"
        width = 40
        print("=" * width)
        print(title.center(width))
        print("=" * width)
        print("1. Create Course")
        print("2. Update Course")
        print("3. Delete Course")
        print("4. Exit")

        try:
            choose=int(input("\nEnter your action:"))
            if choose ==1 :
                create_course()
            elif choose==2:
                update_course()
            elif choose==3:
                delete_course()
            elif choose==4:
                print("Thank you for visiting!")
                break
            else:
                print("Invalid choice!")
        except ValueError:
            print("Invalid input! Only integer 1-3 is allowed.")

#Function 4: Class Schedule
def open_timetable():
    """
    Reads schedule.txt file
    :return: return None if file not exists
    """
    schedule=[] #empty list to store timetable
    try: #handle file not found error
        with open("schedule.txt",'r')as hFile:
            for row in hFile:
                row=row.rstrip().split(",")#remove whitespace and split each line become a list
                #store each list in a dictionary
                item={
                    "Course ID":row[0],
                    "Day":row[1],
                    "Time Slot":row[2],
                    "Instructor":row[3],
                    "Venue":row[4]
                }
                schedule.append(item)
            return schedule #return dictionary to the schedule list
    except FileNotFoundError:
        print("Warning : schedule.txt not found.")
        return None

def view_schedule():
    schedule=open_timetable()
    if schedule is None: #if file not found ,return to menu
        return
    print()
    print("-"*60,"Current Schedule","-"*60)
    index=1
    with open("schedule.txt",'w')as hFile:
        for item in schedule:
            hFile.write(",".join(item.values())+"\n")
            print(f"{index}. Course ID:{item['Course ID']:<10}\t\tDay:{item['Day']:<10}\t\tTime Slot:{item['Time Slot']:<10}"
                  f"\t\tInstructor:{item['Instructor']:<15}\t\tVenue:{item['Venue']:<10}")
            print("-"*140)
            index+=1

def create_schedule():
    schedule = open_timetable()
    if schedule is None:  # if file not found ,return to menu
        return

    while True:
        print("-" * 40, "CREATING SCHEDULE PAGE", "-" * 40)
        course_id=input("Enter the course ID:").strip().upper()
        day=input("Enter the class day:").capitalize()
        time_slot = " "
        time_slot.strip()
        instructor=input("Enter the instructor name:").title()
        venue=input("Enter class venue:").capitalize()

        while True:
            if course_id=='' or day=='' or instructor=='' or venue=='':
                print("Each field cannot be empty. Returning to menu page.")
                return
            else:
                pass

            exists = False
            for item in schedule:
                if course_id == item['Course ID'] and day==item['Day'] and instructor == item['Instructor']:
                    print(f"The class schedule already exists, please enter new class schedule.")
                    exists = True
                    break
            if not exists:
                new_schedule=[course_id,day,time_slot or"",instructor,venue]
                with open("schedule.txt", 'a') as hFile:
                    hFile.write(",".join(new_schedule) + "\n")
                print("Schedule create successful!")
                view_schedule()

            proceed = input("\nProceed creating?(Y/N):").capitalize()
            if proceed == 'N':
                print("Schedule creating successfully!Exiting the page.")
            return

def update_schedule():
    schedule = open_timetable()
    if schedule is None:  # if file not found ,return to menu
        return
    while True:
        view_schedule()
        try:
            num = int(input("Enter the number of schedule to edit: "))
            if 1 <= num <= len(schedule):
                item= schedule[num - 1]  # get the selected event dictionary from list
                part = input("Please enter the field of the course to update:").strip()
                if part not in item:
                    print("The field you enter is not found in the course details. Please enter again.\n")
                    continue

                # edit the part to whatever new
                edition = input(f"Edit {part} to :").strip().title()
                if part=='Time Slot':
                    try:
                        start_time, end_time = edition.split("-")
                        datetime.strptime(start_time, "%H:%M")
                        datetime.strptime(end_time, "%H:%M")
                    except ValueError:
                        print("Invalid time slot format! Please use HH:MM-HH:MM format. (e.g. 12:00-14:00)")
                        continue
                updated_day = item["Day"]
                updated_time = item["Time Slot"]
                updated_venue=item['Venue']

                if part == "Day":
                    updated_day = edition
                elif part == "Time Slot":
                    updated_time = edition
                elif part=='Venue':
                    updated_venue=edition

                for other in schedule:
                    if other['Day']==updated_day and other['Time Slot']==updated_time and other['Venue']==updated_venue:
                        print("The class schedule is overlap with other class. Please recheck the schedule!")
                        break
                else:
                    item[part] = edition

                    with open("schedule.txt", 'w') as vFile:
                        for item in schedule:
                            vFile.write(",".join(item.values()) + "\n")

                    print("\n Course updated successfully!")
                    view_schedule()
            else:
                print("The number you have entered is outside the range of list.Please re-enter the number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.\n")

        proceed = input("Do you want to update another course? (Y/N): ").strip().upper()
        if proceed == 'N':
            print("Course update completed. Returning to main menu.")
            break  # Exit loop

def schedule_menu():
    while True:
        print("")
        title = "Class Schedule Management Page"
        width = 40
        print("=" * width)
        print(title.center(width))
        print("=" * width)
        print("1. Create Class Schedule")
        print("2. Update Class Schedule")
        print("3. Exit")

        try:
            choose=int(input("\nEnter your action:"))
            if choose ==1 :
                create_schedule()
            elif choose==2:
                update_schedule()
            elif choose==3:
                print("Thank you for visiting!")
                break
            else:
                print("Invalid choice!")
        except ValueError:
            print("Invalid input! Only integer 1-3 is allowed.")

#Function 5 : Report Generation
def open_attendances():
    attendances = []  # create an empty list to store data
    try:
        with open("attendances.txt", 'r') as record:
            for line in record:
                line = line.rstrip().split(',')  # remove whitespace and split each line become a list
                # store each attendance in a dictionary

                while len(line)<13:
                    line.append("") #leave empty space by ensuring the list always have 13 fields

                detail = {
                    'Student ID': line[0],
                    'Event Attendance': line[1],
                    'Course 1': line[2],
                    'Course 1 Attendance': line[3],
                    'Course 2':line[4],
                    'Course 2 Attendance':line[5],
                    'Course 3':line[6],
                    'Course 3 Attendance': line[7],
                    'Course 4':line[8],
                    'Course 4 Attendance':line[9],
                    'Course 5':line[10],
                    'Course 5 Attendance':line[11],
                    'Total Attendance':line[12]
                }
                attendances.append(detail)  # add dictionary into attendance list
        return attendances  # return list containing dictionary into attendance
    except FileNotFoundError:
        print("Error: attendances.txt not found.")
    return None  # return None if no existing file

def attendance_report():
    attendances=open_attendances()
    if attendances is None:
        return

    overall_day_attend = 0 #overall_day_attend for student is 0
    overall_day = 0 #overall_day of class is 0

    for attendance in attendances:
        attend_day=0 #attend_day is 0
        total_day=0 #total_day is 0
        #loop through five courses to calculate total attendance
        for value in ['Event Attendance','Course 1 Attendance','Course 2 Attendance','Course 3 Attendance','Course 4 Attendance','Course 5 Attendance']:
            present=attendance[value].strip() #remove space

            if present:
                split_day=present.split("/") #split '98/100' to '98' and '100'
                sum_of_day_attend=int(split_day[0]) #value of '98'
                sum_of_day=int(split_day[1]) #value of '100'

                attend_day+=sum_of_day_attend #total up the sum_of_day_attend of one student
                total_day+=sum_of_day #total up the total_day of one student
            else:
                pass

        overall_day_attend += attend_day #total up the overall_day_attend of all student
        overall_day += total_day #total up the overall_day of every class
        attendance['Total Attendance']=f"{attend_day}/{total_day}" #update 'Total Attendance' in the dictionary

    #write total attendance into attendances.txt
    with open("attendances.txt",'w')as record:
        for attendance in attendances:
            record.write(",".join(attendance.values())+"\n")

    print("\n============ Attendance Report ===========")
    for attendance in attendances: #print every student report
        total_attendance=attendance['Total Attendance']
        attend_day,total_day=total_attendance.strip().split("/")
        attend_day=int(attend_day)
        total_day=int(total_day)
        percentage=(attend_day/total_day)*100
        print(f"Student ID:{attendance['Student ID']}\t\tAttendance: {percentage:.2f}%")
        print("==========================================")
    overall = (overall_day_attend/ overall_day) * 100 #print the overall attendance percentage
    print(f"Overall Percentage:{overall:.2f}%")

def academic_report():
    grades=open_grades()
    print("\n========== Academic Performance ==========")
    for grade in grades:
        print(f"  Student ID       : {grade['Student ID']}")
        print(f"  Assignment Grade : {grade['Assignment Grade']}")
        print(f"  Exam Grade       : {grade['Exam Grade']}")
        print(f"  GPA              : {grade['GPA']}")
        print(f"  Performance      : {grade['Performance']}")
        print("-"*40)

def financial_student_report():
    students = open_students()
    print("\n========== Financial Report of Students ==========")
    for student in students:  # if parent is entered. print financial report of student
        print(f"Student ID       : {student['Student ID']}")
        print(f"Student Name     : {student['Name']}")
        print(f"Tuition Fees(RM) : {student['Tuition Fees(RM)']}")
        print(f"Payment          : {student['Payment']}")
        print("-" * 40)

def financial_institution_report():
    students = open_students()
    tuition_fees = 0
    total_expenses=0
    for student in students:
        if student['Payment'].strip().lower() == "yes":
            tuition_fees += int(student['Tuition Fees(RM)'])
    try:
        with open("expenses.txt", "r") as school:
            for line in school:
                expenses,amount=line.strip().split(",")
                total_expenses += float(amount)

        net_balance = tuition_fees - total_expenses
        print("\n======== Financial Report of Institution ========")
        print(f"Total income     : RM {tuition_fees:.2f}")
        print(f"Total expenses   : RM {total_expenses:.2f}")
        print(f"Net Balance      : RM {net_balance:.2f}")
        print("-" * 50)
    except FileNotFoundError:
        print("Warning: 'expenses.txt' not found. ")
        return

def report_generation_menu():
    while True:
        print("")
        title = "Report Generation Page"
        width = 40
        print("=" * width)
        print(title.center(width))
        print("=" * width)
        print("1. Attendance Report")
        print("2. Academic Performance Report")
        print("3. Financial Reports(Students)")
        print("4. Financial Reports(Institution)")
        print("5. Exit")

        try:
            choose=int(input("\nEnter your action:"))
            if choose ==1 :
                attendance_report()
            elif choose==2:
                academic_report()
            elif choose==3:
                financial_student_report()
            elif choose==4:
                financial_institution_report()
            elif choose==5:
                print("Thank you for visiting!")
                break
            else:
                print("Invalid choice!")
        except ValueError:
            print("Invalid input! Only integer 1-3 is allowed.")

#Admin main menu
def main_menu():
    while True:
        #display staff management system
        print("")
        title="Administrator Management System"
        width=40
        print("="*width)
        print(title.center(width))
        print("="*width)
        print("\nMain Menu:")
        print("1. System Administration")
        print("2. Student Management")
        print("3. Course Management")
        print("4. Class Schedule")
        print("5. Report Generation")
        print("6. Exit\n")
        print("="*width)

        try:
            selection = int(input("Please enter your choice (1-6): "))

            if selection==1:
                system_administration_menu()
            elif selection==2:
                student_management_menu()
            elif selection==3:
                course_management_menu()
            elif selection==4:
                schedule_menu()
            elif selection==5:
                report_generation_menu()
            elif selection == 6:
                print("Thank you for visiting the system.\nExiting Admin Management Page...")
                break
            else:
                print("Invalid choice! Please enter a number between 1-6.")

        except ValueError: #raise ValueError if user input invalid data format
            print("Invalid input! Only integer between 1-6 is allowed.\nPlease enter a valid number.")

# main_menu()

