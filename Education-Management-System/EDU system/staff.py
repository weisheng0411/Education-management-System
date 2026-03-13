import random
from datetime import datetime

#function 1: student record
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

def update_student_status(pupil_id,new_status):
    """
    update the status of students in the student records
    :param pupil_id: The student_id which need to be updated
    :param new_status:the new status need to be updated to the student's status (withdraw,transfer)
    """
    students=open_students() #read students list from students.txt
    if students is None:  # If the file was missing, stop execution and return to menu
        return

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
                print(f"Student ID:{student['Student ID']}\t\tStudent Name:{student['Name']:<15}\t\tContact:"
                      f"{student['Contact']:<15}\t\tGender:{student['Gender']:<15}\t\tStudent status:{student['Student Status']:<15}")
    else:
        print("Updating issue occur")

def generate_id():
    students = open_students()
    if students is None:  # If the file was missing, stop execution and return to menu
        return

    while True:
        #Generate a unique random student ID following the format 'TP......'
        student_id = f"TP{random.randint(1, 99):02d}{random.randint(1, 99):02d}{random.randint(1, 99):02d}"
        for student in students: #return the generated student ID if the ID is not existed in students.txt
            if student_id not in student['Student ID']:
                return student_id

def register_student():
    #this function is to register a new students and append the information into students.txt
    students = open_students()
    if students is None:  # If the file was missing, stop execution and return to menu
        return
    while True:
        try:
            name = str(input("Please enter the student's name:")).title()
            while True:
                if name!='':
                    break
                else:
                    print("Invalid input. Name field cannot be empty!")
                    return
            while True:
                contact = input("Please enter the student's contact:")
                if contact.isdigit(): #valid the input is all in digit
                    break
                else:
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
            new_student = [register_id,name,email or " ",contact,emergency_contact or " ",
                               gender,student_status,tuition_fees or " ",payment or " "]

            # append new student to the students.txt file
            with open("students.txt", 'a') as tFile:
                #convert the new_student list into single string
                tFile.write(",".join(new_student)+"\n")

            print("\nRegister successful!\n")
            print(f"Assigned Student ID:{register_id}")
            print(f"Student Name:{name}\nContact:{contact}\nGender:{gender}\nStudent status:{student_status}")
            break

        except Exception as e: #handle errors such as TypeError,ValueError and indentation error
            print(f"Invalid input!{e} has occurred!")

def action(pupil_id):
    """
    This function is to let staff can check information of student and change the status of the students from active to
    withdraw and transfer
    :param pupil_id:use the pupil_id to perform the action
    """
    students = open_students()
    if students is None:  # If the file was missing, stop execution and return to menu
        return
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
                    if student['Student ID']==pupil_id: #check if the pupil_id is inside the students.txt
                        print(f"Student ID:{student['Student ID']}\t\tStudent Name:{student['Name']:<15}\t\tContact:"
                              f"{student['Contact']:<15}\t\tGender:{student['Gender']:<15}\t\tStudent status:{student['Student Status']:<15}")
            elif selection == 2:
                #call the update_student_status and change the status to 'Transfer'
                update_student_status(pupil_id,"Transfer")
            elif selection == 3:
                # call the update_student_status and change the status to 'Withdraw'
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
    if students is None:  # If the file was missing, stop execution and return to the menu
        return

    print("\nHere is the current student list:")
    for student in students:
        print(f"Student ID:{student['Student ID']}\t\tStudent Name:{student['Name']:<15}\t\tContact:"
              f"{student['Contact']:<15}\t\tGender:{student['Gender']:<15}\t\tStudent status:{student['Student Status']:<15}")
    while True:
        print("\nSelect student menu")
        print("1. Enter Student ID")
        print("2. Finish searching")

        try:
            chosen=int(input("Please select action:"))
            if chosen ==1:
                pupil_id=input("Please enter student ID: ").upper()
                for student in students:
                    if student['Student ID']==pupil_id: #Check if the entered Student ID exists in the student records.
                        action(pupil_id) #call the action function with list that contain related pupil_id
                        break
                else:
                    #print student not found message if the pupil_id is not in students.txt
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
        print("2. Check Student Status")
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

#Function 2: timetable management
def convert_time(time):
    """
    This function is to convert the time format to 24 hours method
    :param time: time input by staff
    :return: return the time format as HH:MM format
    """
    try:
        return datetime.strptime(time, '%H:%M')  # Validate time format as 24 hours method (HH:MM)
    except ValueError:
        raise ValueError("Invalid time format. Please enter in HH:MM format.")

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

def open_teacher():
    """
    Reads the teachers.txt file
    :return: return teachers list after identify each column as dictionary
    return None if the file is not found
    """
    teachers=[]
    try:
        with open("teachers.txt",'r')as instructor:
            for column in instructor:
                column=column.rstrip().split(",")
                item={
                    "Teacher ID":column[0],
                    "Day": column[1],
                    "Instructor":column[2],
                    "Available Time":column[3]
                }
                teachers.append(item)
            return teachers
    except FileNotFoundError:
        print("Warning: teachers.txt not found.")
        return None

def update_timetable():
    schedule=open_timetable()
    if schedule is None: #if file not found ,return to menu
        return
    print()
    print("-"*60,"Current Timetable","-"*60)
    index=1
    with open("schedule.txt",'w')as hFile:
        for item in schedule:
            hFile.write(",".join(item.values())+"\n")
            print(f"{index}. Course ID:{item['Course ID']:<10}\t\tDay:{item['Day']:<10}\t\tTime Slot:{item['Time Slot']:<10}"
                  f"\t\tInstructor:{item['Instructor']:<15}\t\tVenue:{item['Venue']:<10}")
            print("-"*140)
            index+=1

def view_teachers(instructor_name,class_day):
    teachers=open_teacher()
    if teachers is None:
        return
    found=False
    print()
    print("-" * 40, "Instructors Available Time", "-" * 40)
    for item in teachers:
        if item['Instructor'].strip() == instructor_name and item['Day'].strip() == class_day:
            print(f"Teacher ID: {item['Teacher ID']:<5}\tDay: {item['Day']:<10}"
                  f"\tInstructor: {item['Instructor']:<15}\tAvailable Time: {item['Available Time']:<10}")
            print("-" * 110)
            found = True
    if not found:
        print("No matching instructor available for the course. ")

def edit_schedule():
    schedule=open_timetable()
    teachers=open_teacher()
    if schedule is None or teachers is None:
        return
    while True:
        print("-"*40,"Action Menu","-"*40)
        print("1. Scheduling Class")
        print("2. Rescheduling Class")
        print("3. Exit")

        try:
            option=int(input("Enter your option:"))
            if option==1:
                update_timetable()
                bil=int(input("Enter line number need to schedule:"))
                if 1<= bil<=len(schedule): #ensure the input number is within the valid range of schedule list
                    real_bil = bil - 1 #decrement 1 to find out the real number in schedule
                    if schedule[real_bil]['Time Slot'] == " ":
                        scheduling=input("Enter the time slot of the class schedule in 24 hours method (eg. 12:00-14:00):")

                        try: #valid the time format is HH:MM-HH:MM format
                            start_time, end_time = scheduling.split("-") #split the entered time by -
                            # Validate time format
                            start_time = convert_time(start_time)
                            end_time = convert_time(end_time)
                            if start_time >= end_time:
                                print("Error: Start time must be before end time.")
                                continue
                        except ValueError:
                            print("Invalid time format. Please enter in HH:MM-HH:MM format.")
                            continue
                        schedule[real_bil]['Time Slot']=scheduling #update the time slot in schedule
                        with open("schedule.txt", 'w') as hFile:
                            for item in schedule:  # write the entire schedule back to the schedule.txt
                                hFile.write(",".join(item.values()) + "\n") #convert dictionary to comma-separated string
                    else:
                        print("The schedule selected already have time slot. Please select Rescheduling Class if wanted.\n")
                        continue
                else:
                    print("The line number was not in the timetable.")
                print("Schedule successful!")
                update_timetable()
            elif option==2:
                update_timetable()
                print("")
                bil = int(input("Enter line number of the timetable need to reschedule:"))
                if 1 <= bil <= len(schedule): #validate the number of line of the timetable
                    real_bil = bil - 1
                    selected_class=schedule[real_bil] #identify the line of the schedule
                    instructor_name=selected_class['Instructor'].strip()
                    class_day=selected_class['Day'].strip()
                    view_teachers(instructor_name,class_day)

                    found=False
                    for teacher in teachers:
                        if teacher['Instructor'].strip()==instructor_name and teacher['Day'].strip()==class_day:
                            try:
                                time_start, time_end = teacher['Available Time'].split("-")
                                new_start, new_end = input("Enter new time (HH:MM-HH:MM): ").split("-")

                                # Validate new time format
                                new_start = convert_time(new_start)
                                new_end = convert_time(new_end)

                                # Convert available time to datetime for comparison
                                time_start = convert_time(time_start)
                                time_end = convert_time(time_end)

                                if time_start <= new_start <= time_end and time_start <= new_end <= time_end:
                                    #strftime is to formate the datetime format as system default it as %Y#M#D%H%M
                                    schedule[real_bil]['Time Slot']=f"{new_start.strftime('%H:%M')}-{new_end.strftime('%H:%M')}"
                                    print("Reschedule successful!")

                                    with open("schedule.txt", 'w') as hFile:
                                        for item in schedule:  # write the entire schedule back to the schedule.txt
                                            hFile.write(",".join(item.values()) + "\n")
                                    update_timetable()
                                    found=True
                                    break
                                else:
                                    print("Error:New time slot is outside the instructor's available hours.")
                                    found=True
                                    break
                            except ValueError:
                                print("Invalid time format. Please enter in HH:MM-HH:MM format.")
                    if not found:
                        print("Attention: The selected instructor is not free at that day.")
                else:
                    print("Invalid line number.")
            elif option==3:
                print("Exiting the page...")
                break
            else:
                print("Please enter number 1-3 only.")
        except ValueError:
            print("Invalid option. Please enter only integer.")

def timetable_menu():
    while True:
        print("")
        title = "Timetable Management Page"
        width = 40
        print("=" * width)
        print(title.center(width))
        print("=" * width)
        print("1. View Class Schedule")
        print("2. Edit Schedule In Timetable")
        print("3. Exit")

        try:
            choose=int(input("\nEnter your action:"))
            if choose ==1 :
                update_timetable()
            elif choose==2:
                edit_schedule()
            elif choose==3:
                print("Thank you for visiting!")
                break
            else:
                print("Invalid choice!")
        except ValueError:
            print("Invalid input! Only integer 1-3 is allowed.")


#Function 3 : Resource Allocation
def open_resource():
    """
    Reads resource.txt file
    :return: return resources after identify each line as dictionary
    """
    resources=[] #empty list to store data
    try:
        with open("resource.txt",'r')as gFile:
            for line in gFile:
                line=line.rstrip().split(",")#remove whitespace and split each line become a list
                #index label and store in dictionary
                item={
                    "Classroom":line[0],
                    "Resource":line[1],
                    "Number":line[2],
                    "Available":line[3]
                }
                resources.append(item)
            return resources
    except FileNotFoundError:
        print("Error: resource.txt not found.")
    return None

def update_resource():
    """
    write the update resource list into resource.txt
    :return: return to menu page if file not found
    """
    resources=open_resource()
    if resources is None:
        return
    print("-" * 35, "Current Resource List", "-" * 35)
    with open("resource.txt", 'w') as gFile:
        for resource in resources:
            gFile.write(",".join(resource.values())+"\n")
            print(f"Classroom: {resource['Classroom']} \t\t Resource: {resource['Resource']:<10} "
                  f"\t\t Quantity: {resource['Number']:<5}\t\t Available:{resource['Available']}")
        print("")

def continue_searching():
    """
    Ask the staff whether they want to continue searching.
    """
    while True:
        try:
            proceed = input("\nContinue searching?(Y/N):").capitalize()
            if proceed == 'Y':
                return True #continue searching
            elif proceed == 'N':
                print("Thank you for searching!")
                return False #stop searching
            else:
                raise ValueError("Invalid input. Please enter only Y or N")
        except ValueError as e:
            print(e)

def search_by_classroom(): #seach the classroom has what resources
    resources=open_resource()
    if resources is None:
        return
    while True:
        classroom=input("Enter the classroom name:").capitalize()
        found=False #track a match when found

        for resource in resources: #check the classroom one by one
            if resource['Classroom']==classroom:
                print(f"Classroom {classroom} contain {resource['Resource']} with quantity {resource['Number']}")
                found=True

        if not found:
            print("Sorry,classroom entered is not found")
        if not continue_searching():
            break

def search_by_resource(): #search the resource is in which class
    resources=open_resource()
    if resources is None:
        return
    while True:
        resource_enter=input("Enter the resource name:").capitalize()
        found=False #track if the resource is found
        for resource in resources:
            if resource['Resource']==resource_enter:
                print(f"The {resource_enter} is in {resource['Classroom']} with quantity {resource['Number']}")
                found=True #mark as found
        if not found:
            print("Sorry,resource entered is not found")
        if not continue_searching():
            break

def resource_maintain():
    resources=open_resource()
    update_resource()
    if resources is None:
        return
    while True:
        print("Select an action:")
        print("1. Create new classroom and resource")
        print("2. Update existing resource")
        print("3. Exit")

        choice=int(input("Please enter your action:"))
        try:
            if choice==1:
                print("\n----------CREATING NEW CLASSROOM AND RESOURCE----------")
                while True:
                    classroom=input("Enter the classroom name:").strip().title()
                    if classroom=='':
                        print("The field cannot be empty!")
                        continue
                    for resource in resources:
                        if classroom==resource['Classroom']:
                            add_resource=input("The classroom already exists. Add a new resource to it?(Y/N):").capitalize()
                            if add_resource=='N':
                                print("Returning to main menu.")
                                return
                            elif add_resource=='Y':
                                break
                            else:
                                print("Invalid input. Please enter 'Y' or 'N'.")
                                continue
                    add_resource=input("Enter the resource name to add:").title()
                    for resource in resources:
                        if resource['Resource']==add_resource and resource['Classroom']==classroom:
                            print(F"Classroom {classroom} already have {add_resource}.\nChoose update or allocate if needed.\n")
                            return
                    try:
                        quantity=int(input(f"Enter the quantity of {add_resource} to be add:"))
                        available_quantity=int(input("Enter the available quantity of the resource:"))
                        if quantity<0 or available_quantity<0:
                            print("Invalid input. Number of quantity cannot be negative")
                            continue
                        with open("resource.txt",'a')as gFile:
                            gFile.write(f"{classroom},{add_resource},{quantity},{available_quantity}\n")
                        print(f"Classroom '{classroom}' with {quantity} resource '{add_resource}' created successfully.\n")
                        resources=open_resource()
                        update_resource()
                        break
                    except ValueError:
                        print("Invalid quantity. Please enter a valid integer.")
            elif choice==2:
                print("\n----------UPDATING EXISTING RESOURCE----------")
                classroom=input("Enter the classroom name to update:").strip().title()
                give_resource=input("Enter the resource name to update:").strip().title()

                found=False
                for resource in resources:
                    if resource['Classroom']==classroom and resource['Resource']==give_resource:
                        found=True
                        print(f"Current Quantity: {resource['Number']}\t\tAvailable: {resource['Available']}")
                        try:
                            update_quantity = input("Enter the updated quantity amount or Enter for remain: ")
                            update_available = input("Enter the updated available amount or Enter for remain: ")

                            if update_quantity:
                                update_quantity = int(update_quantity)
                                if update_quantity < 0:
                                    print("Invalid input! Quantity cannot be negative.")
                                    break
                                resource['Number'] = str(update_quantity) #update when have input

                            if update_available:
                                update_available = int(update_available)
                                if update_available < 0:
                                    print("Invalid input! Quantity cannot be negative.")
                                    break
                                resource['Available'] = str(update_available) #update when have input

                            with open("resource.txt", "w") as gFile:
                                for item in resources:
                                    gFile.write(",".join(item.values()) + "\n")
                            print("Update successfully!\n")
                            update_resource()
                        except ValueError:
                            print("Invalid input! Please enter a valid integer.\n")
                        break
                if not found:
                    print(f"Classroom '{classroom}' or resource '{give_resource}' not found. Please re-enter.\n")
            elif choice==3:
                print("Thank you for entering maintenance page. Exiting menu...")
                break
        except ValueError:
            print("Invalid input! Please enter number 1-3 only.\n")

def resource_allocate():
    resources=open_resource()
    update_resource()
    if resources is None:
        return
    while True: #ask staff to enter the classroom name
        classroom=input("Enter the classroom to allocate resource:").title()
        class_found=False
        for resource in resources:
            if classroom ==resource['Classroom']:
                class_found=True
                break
        if not class_found:
            print(f"Classroom {classroom} not found. Please retry or select to create a new classroom.\n")
            return

        while True: #ask staff to enter the name of resource need to allocated
            allocate_resource=input("Enter the resource name need to update:").capitalize()
            found_resource=False
            for resource in resources:
                if resource['Classroom']==classroom and resource['Resource']==allocate_resource:
                    found_resource=True
                    break
            if not found_resource:
                print(f"Resource '{allocate_resource}' not found in {classroom}. Please enter a valid resource.\n")
                continue
            break

        while True:
            try: #ask staff for the quantity of the resource need to allocate
                quantity = int(input(f"Enter the quantity of {allocate_resource} to update: "))
                if quantity <= 0: #valid the quantity input is bigger than 0
                    raise ValueError("Quantity must be greater than 0!")
                break  # Exit loop if valid
            except ValueError as e: #e is the error that made by the user
                print(f"Invalid input: {e}")

        done_allocate=False
        for resource in resources:
            if resource['Classroom']==classroom and resource['Resource']==allocate_resource:
                available=int(resource['Available']) #convert string into integer
                number=int(resource['Number']) #convert string into integer
                if quantity > available:
                    print(f"\nNot enough {allocate_resource}. Only {available} left.")
                    break #print one time available message
                else:
                    resource['Available'] = str(available - quantity) #deduct allocated quantity from available
                    resource['Number']=str(number+quantity) #updated allocated number
                    done_allocate=True
                break

        if done_allocate: #write the update quantity to the resource.txt
            with open("resource.txt", 'w') as gFile:
                for resource in resources:
                    gFile.write(",".join(resource.values()) + "\n")

            print("Update Resource List:")
            update_resource()

        proceed_again=input("\nProceed allocated?(Y/N):").capitalize()
        if proceed_again == 'N':
            print("Resource allocation completed!Exiting the page.")
            return

def resource_allocation_menu():
    while True:
        print("")
        title = "Resource Allocation Page"
        width = 40
        print("=" * width)
        print(title.center(width))
        print("=" * width)
        print("1. Search by class name")
        print("2. Search by resource name")
        print("3. Maintain resource")
        print("4. Allocate resource")
        print("5. Exit")

        try:
            choice=int(input("Enter your choice:"))
            if choice ==1:
                search_by_classroom()
            elif choice==2:
                search_by_resource()
            elif choice==3:
                resource_maintain()
            elif choice==4:
                resource_allocate()
            elif choice==5:
                print("Thank you for visiting!")
                break
            else:
                print("Invalid choice!")
        except ValueError:
            print("Invalid input! Only integer 1-3 is allowed.")

#Function 4 :Event Management
def open_event(): #read event.txt file
    events=[]
    try:
        with open("event.txt",'r')as vFile:
            for line in vFile:
                line=line.rstrip().split(",")#remove whitespace and split each line become a list
                #store each list in a dictionary with index label
                program={
                    "Category":line[0],
                    "Title":line[1],
                    "Date":line[2],
                    "Duration":line[3],
                    "Venue":line[4],
                    "Leader":line[5]
                }
                events.append(program) #add each event program to the events list
            return events
    except FileNotFoundError:
        print("Warning: 'event.txt' not found. ")
    return None #return an empty list is file is missing

def update_event():
    events=open_event()
    if events is None:
        return

    with open("event.txt", 'w') as vFile:
        index = 1
        for event in events:
            vFile.write(",".join(event.values()) + "\n")
            print(f"Category:{event['Category']}\n")
            print("Event details:")
            print(f"{index}. Title: {event['Title']:<50}\tDate: {event['Date']:<10}\tDuration: {event['Duration']:<10}"
                  f"\tVenue: {event['Venue']:<13}\tLeader: {event['Leader']:<10}")
            index += 1
            print("-" * 150)

def register_event():
    events = open_event()
    if events is None:
        return

    while True:
        print("-" * 50, "REGISTER NEW EVENT", "-" * 50)

        while True:
            category=input("Enter event category(Academic/Extracurricular/Conference/Seminar):").capitalize()
            # validate the input of user is within the listed category
            if category not in ["Academic","Extracurricular","Conference","Seminar"]:
                print("Entered category is not found.\n")
                continue
            else:
                break

        title=input("Enter event title:").title().strip()
        while True:
            try:
                date=input("Enter event date (dd/mm/yyyy):").strip() #validate the date format
                datetime.strptime(date,"%d/%m/%Y")
                break
            except ValueError:
                print("Invalid date format! Please enter the date in DD/MM/YYYY format.\n")

        while True:
            duration=input("Enter event duration(HH:MM-HH:MM):").strip()
            try:
                start_time,end_time=duration.split("-")
                datetime.strptime(start_time,"%H:%M")
                datetime.strptime(end_time,"%H:%M")
                break
            except ValueError:
                print("Invalid time slot format! Please use HH:MM-HH:MM format. (e.g. 12:00-14:00)")

        venue=input("Enter event venue:").strip().capitalize()
        leader=input("Enter event leader:").strip().title()

        new_event=f"{category},{title},{date},{duration},{venue},{leader}"
        with open("event.txt",'a')as vFile:
            vFile.write(new_event+"\n")

        print("Register successful!\n")
        print("-" * 50, "Update Event List", "-" * 50)
        update_event()

        proceed= input("Proceed register?(Y/N):").capitalize()
        if proceed == 'N':
            print("Event Register Completed!\nThank You for Visiting!")
            return

def manage_event():
    events=open_event()
    if events is None:
        return
    while True:
        print("")
        print("-" * 50, "Action Page", "-" * 50)
        print("1. Delete Event")
        print("2. Edit Event Content")
        print("3. Skip the step")

        try:
            selection = int(input("\nPlease Enter your choice:"))
            if selection == 1:
                print("-" * 50, "DELETING EVENT PAGE", "-" * 50)
                update_event()
                line_number=int(input("Enter the number of event need to be delete:"))
                if 1<= line_number <= len(events):
                    #delete the real number in the list
                    del events[line_number-1]

                    #update the delete list to the file
                    with open("event.txt",'w')as vFile:
                        for event in events:
                            vFile.write(",".join(event.values())+"\n")

                    print("Event deleted!\n")
                    print("-" * 50, "Update Event List", "-" * 50)
                    update_event()
                else:
                    print("The number is not in event list.")
                    continue
            elif selection == 2:
                update_event()
                while True:
                    try:
                        num = int(input("Enter the number of the event edit: "))
                        if 1 <= num <= len(events):
                            event=events[num-1] #get the selected event dictionary from list
                            part = input("Please enter the part of the event to edit(Title/Date/"
                                         "Venue/Duration/Leader):").title()
                            if part not in event:
                                print("The part you enter is not found in the event list. Please enter again.\n")
                                continue

                            # edit the part to whatever new
                            edition = input(f"Edit {part} to :").strip().title()

                            if part == "Date":
                                try:
                                    # check if the date is input as correct format
                                    datetime.strptime(edition, "%d/%m/%Y")
                                except ValueError:
                                    print("Invalid date format! Use DD/MM/YYYY.")
                                    continue

                            if part =="Duration":
                                try:
                                    start_time,end_time=edition.split("-")
                                    datetime.strptime(start_time,"%H:%M")
                                    datetime.strptime(end_time,"%H:%M")
                                except ValueError:
                                    print("Invalid time slot format! Please use HH:MM-HH:MM format. (e.g. 12:00-14:00)")
                                    continue

                            event[part] = edition #change the part to edition entered
                            with open("event.txt",'w')as vFile:
                                for event in events:
                                    vFile.write(",".join(event.values())+"\n")

                            print("Event edited!\n")
                            print("-" * 50, "Update Event List", "-" * 50)
                            update_event()
                            break
                        else:
                            print("Invalid number. Please enter bill in the event list!")
                    except ValueError:
                        print("Invalid input. Please enter a valid number.\n")

            elif selection==3:
                print("Skipping Page...")
                break
            else:
                print("Please enter number 1-3 only.")
        except ValueError:
            print("Invalid input. Only integer 1-3 is allowed.")

def event_menu():
    while True:
        print("")
        title = "Event Management Page"
        width = 40
        print("=" * width)
        print(title.center(width))
        print("=" * width)
        print("1. View Event")
        print("2. Register Event")
        print("3. Manage Event")
        print("4. Exit")

        try:
            choose=int(input("\nEnter your action:"))
            if choose ==1 :
                update_event()
            elif choose==2:
                register_event()
            elif choose==3:
                manage_event()
            elif choose==4:
                print("Thank you for visiting!")
                break
            else:
                print("Invalid choice!")
        except ValueError:
            print("Invalid input! Only integer 1-3 is allowed.")

#Function 5 : Communication
def open_mailbox(): #read mail.txt file
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
        print("Error: mail.txt not found.")
    return None #return None if no existing file

def update_mailbox():
    mailboxes = open_mailbox()
    if mailboxes is None:
        return

    with open("mail.txt", 'w') as message:
        print("")
        print("=" * 15, "MAILBOX CONTENT", "=" * 15)
        for mail in mailboxes:
            message.write(",".join(mail.values()) + "\n")
            print(f"Name:{mail['Name']}")
            print(f"Role:{mail['Role']}")
            print(f"Email:{mail['Message']}")
            print(f"Reply:{mail['Reply']}")
            print("-" * 50)

def reply_mailbox():
    mailboxes = open_mailbox()
    if mailboxes is None:
        return
    while True:
        print("")
        print("=" * 10, "ACTION MENU", "=" * 10)
        print("1. Reply Mail")
        print("2. Skip Reply")

        try:
            choose = int(input("Enter your action: "))
            if choose==1:
                reply_sender = input("Reply Email from which role(STUDENT/PARENT/TEACHER):").strip().upper()
                reply = input("Reply Email from (name) :")
                found = False
                for mail in mailboxes:
                    if mail['Name']==reply and mail['Role'].upper()==reply_sender:
                        if mail['Role'].upper() == "PARENT": #if role entered is parent enter student financial page
                            students = open_students() #call the function

                            print("\n========== Student Fee Details ==========")
                            for student in students: #if parent is entered. print financial report of student
                                print(f"Student ID:{student['Student ID']}")
                                print(f"Student Name: {student['Name']}")
                                print(f"Tuition Fees(RM): {student['Tuition Fees(RM)']}")
                                print(f"Payment: {student['Payment']}")
                                print("-" * 40)

                        reply_text=input("Enter your reply: ").strip()
                        mail['Reply']=reply_text
                        found = True
                        break

                if not found:
                    print("The role/name you enter is not in the list. Please try again.")
                    continue

                #update mailbox with the reply content
                with open("mail.txt",'w')as message:
                    for mail in mailboxes:
                        message.write(",".join(mail.values())+"\n")

                #call update function to display the mailbox after updated
                update_mailbox()
            elif choose==2:
                print("Skipping page...")
                return
            else:
                print("Invalid input.Please enter only integer 1-4.")
        except ValueError:
            print("Invalid input. Please enter valid integer.")

def communication_menu():
    while True:
        print("")
        title = "Communication Page"
        width = 40
        print("=" * width)
        print(title.center(width))
        print("=" * width)
        print("1. View Mailbox")
        print("2. Reply Mailbox")
        print("3. Exit")

        try:
            choose=int(input("\nEnter your action:"))
            if choose ==1 :
                update_mailbox()
            elif choose==2:
                reply_mailbox()
            elif choose==3:
                print("Thank you for visiting!")
                break
            else:
                print("Invalid choice!")
        except ValueError:
            print("Invalid input! Only integer 1-3 is allowed.")

#Staff Main Menu
def main_menu():
    while True:
        #display staff management system
        print("")
        title="Staff Management System"
        width=40
        print("="*width)
        print(title.center(width))
        print("="*width)
        print("\nMain Menu:")
        print("1. Student Records")
        print("2. Timetable Management")
        print("3. Resource Allocation")
        print("4. Event Management")
        print("5. Communication")
        print("6. Exit\n")
        print("="*width)

        try:
            selection = int(input("Please enter your choice (1-6): "))

            if selection==1: #move to student_record.py
                student_record_menu()
            elif selection==2: #move to timetable_management.py
                timetable_menu()
            elif selection==3: #move to resource_allocation.py
                resource_allocation_menu()
            elif selection==4: #move to event_management.py
                event_menu()
            elif selection==5: #move to communication.py
                communication_menu()
            elif selection == 6: #exit the staff management page
                print("Thank you for visiting the system.\nExiting Staff Management Page...")
                break
            else:
                print("Invalid choice! Please enter a number between 1-6.")

        except ValueError: #raise ValueError if user input invalid data format
            print("Invalid input! Only integer between 1-6 is allowed.\nPlease enter a valid number.")

# main_menu()
