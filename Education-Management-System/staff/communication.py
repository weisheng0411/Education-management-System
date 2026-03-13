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
        print("Error: mail.txt not found.")
    return None #return None if no existing file

def update_mailbox():
    mailboxes = open_mailbox()
    if mailboxes is None:
        return

    with open("mail.txt", 'w') as message:
        print("")
        print("=" * 10, "MAILBOX CONTENT", "=" * 10)
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
            action=int(input("Enter your action: "))
            if action==1:
                reply_sender = input("Reply Email from which role(STUDENT/PARENT/TEACHER):").strip().upper()
                reply = input("Reply Email from (name) :").title()
                found = False
                for mail in mailboxes:
                    if mail['Name']==reply and mail['Role'].upper()==reply_sender:
                        if mail['Role'].upper() == "PARENT": #if role entered is parent enter student financial page
                            from student_record import open_students #import open students.txt function from student_record.py
                            students = open_students() #call the function

                            print("\n========== Student Fee Details ==========")
                            for student in students: #if parent is entered. print financial report of student
                                print(f"Student ID:{student['Student ID']}")
                                print(f"Student Name: {student['Name']}")
                                print(f"Tuition Fees: {student['Tuition Fees']}")
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
            elif action==2:
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

# communication_menu()
