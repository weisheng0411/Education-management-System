from datetime import datetime

def convert_time(time):  # Convert time format for easy comparison
    try:
        return datetime.strptime(time, '%H:%M')  # Validate time format as 24 hours method (HH:MM)
    except ValueError:
        raise ValueError("Invalid time format. Please enter in HH:MM format.")

def open_timetable():
    """
    This function is to read the timetable file
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
            print(f"{index}. Course ID:{item['Course ID']}\t\tDay:{item['Day']}\t\tTime Slot:{item['Time Slot']}\t\tInstructor:{item['Instructor']}\t\tVenue:{item['Venue']}")
            print("-"*150)
            index+=1

def view_teachers():
    teachers=open_teacher()
    if teachers is None:
        return
    print()
    print("-" * 40, "Instructors Official Hours", "-" * 40)
    with open("teachers.txt", 'w') as instructor:
        for item in teachers:
            instructor.write(",".join(item.values()) + "\n") #convert dictionary into comma-separated string and write to file
            print(f"Teacher ID:{item['Teacher ID']}\t\tDay:{item['Day']}\t\tInstructor:{item['Instructor']}\t\tAvailable Time:{item['Available Time']}")
            print("-" * 100)

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
                if 1<= bil<=len(schedule):
                    real_bil = bil - 1
                    if schedule[real_bil]['Time Slot'] == " ":
                        scheduling=input("Enter the time slot of the class schedule in 24 hours method (eg. 12:00-14:00):")

                        try: #valid the time format is HH:MM-HH:MM format
                            start_time, end_time = scheduling.split("-")
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
                update_timetable()
            elif option==2:
                update_timetable()
                print("")
                view_teachers()
                bil = int(input("Enter line number of the timetable need to reschedule:"))
                if 1 <= bil <= len(schedule): #validate the number of line of the timetable
                    real_bil = bil - 1
                    selected_class=schedule[real_bil] #identify the line of the schedule
                    instructor_name=selected_class['Instructor'].strip()
                    class_day=selected_class['Day'].strip()

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
                        print("Error: Instructor not found or office hours do not match.")
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

# timetable_menu()
