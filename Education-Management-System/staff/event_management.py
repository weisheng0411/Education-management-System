from datetime import datetime

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
            print(f"{index}. Title: {event['Title']:<50}\tDate: {event['Date']:<10}\tVenue: {event['Venue']:<7}"
                  f"\tDuration: {event['Duration']:<10}\tLeader: {event['Leader']:<10}")
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

        duration=input("Enter event duration(h/m):").strip()
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
            print("-" * 50, "DELETING EVENT PAGE", "-" * 50)
            if selection == 1:
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
                            part = input("Please enter the part of the event to edit(Title/Date/Venue/Duration/Leader):").title()
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


# event_menu()
