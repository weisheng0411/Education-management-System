import admin
import student
import teacher
import staff

def login_account(role):
    accounts = admin.open_accounts()
    for attempt in range(3):
        print(f"\n--------{role} Login---------")
        username=input("Please enter your username:").upper()
        password=input("Please enter your password:")

        for account in accounts:
            if role==account['Role'] and username==account['Username'] and password==account['Password']:
                print("Login successful!")
                return True
        else:
            print("Invalid username or password . Please try again.\n")
            continue
    print("You have reach the limited attempt. Return to main page.")
    return False

def edu_main_page():
    while True:
        #display staff management system
        print("")
        title="Education Management System"
        width=40
        print("="*width)
        print(title.center(width))
        print("="*width)
        print("\nMain Menu:")
        print("1. Administrator")
        print("2. Student")
        print("3. Teacher")
        print("4. Staff")
        print("5. Exit\n")
        print("="*width)

        role_list={
            1:'Admin',
            2:'Student',
            3:'Teacher',
            4:'Staff'
        }

        try:
            selection = int(input("Please select your role(1-5): "))
            if selection==1:
                role=role_list[selection]
                if login_account(role):
                    admin.main_menu()
            elif selection==2:
                student.login_student_menu()
            elif selection==3:
                role = role_list[selection]
                if login_account(role):
                    teacher.main_menu()
            elif selection==4:
                role = role_list[selection]
                if login_account(role):
                    staff.main_menu()
            elif selection == 5:
                print("Thank you for visiting the system.\nExiting Education Management Page...")
                break
            else:
                print("Invalid choice! Please enter a number between 1-6.")

        except ValueError: #raise ValueError if user input invalid data format
            print("Invalid input! Only integer between 1-6 is allowed.\nPlease enter a valid number.")

edu_main_page()