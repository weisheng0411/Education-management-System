import upd_info
import course_enrol
import material_access
import grade_tracking
import feedback_submission

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


def login_student_menu():
    while True:
        print("")
        title = "Student Login Menu"
        width = 40
        print("=" * width)
        print(title.center(width))
        print("=" * width)
        print("1. Create account")
        print("2. Login account")
        print("3. Exit")

        try:
            opt = int(input("\nYour choice: "))

            if opt == 1:
                create_student_acc()
            elif opt == 2:
                login_student_acc()
            elif opt == 3:
                break
        except ValueError:
            print("Invalid input! Only integer between 1-3 is allowed.")


def create_student_acc():
    new_user = input("Please enter your new username: ").upper()
    new_pass = input("Please enter your password: ")
    role = "Student"

    accounts = open_accounts()
    if accounts is None:
        return

    account_found = None
    for account in accounts:
        if account["Username"] == new_user:
            account_found = account
            break  # stop when account correct

    if account_found:
        print("Account already exist!")

    if not account_found:

        new_account = {
            "Role": role,
            "Username": new_user,
            "Password": new_pass,
        }

        accounts.append(new_account)
        with open("accounts.txt", "w") as message:
            for acc in accounts:
                message.write(",".join(acc.values()) + "\n")

        print(f"\nyour username: {new_user}")
        print(f"your password: {new_pass}")
        print("Account created successful!")


def login_student_acc():
    username = input("Please enter your username: ").upper()
    password = input("Please enter your password: ")

    accounts = open_accounts()
    if accounts is None:
        return

    account_found = None
    for account in accounts:
        if account["Username"] == username and account["Password"] == password:
            account_found = account
            break  # stop when account correct

    if account_found:
        student_menu()
    else:
        print("Account not found!")


def student_menu():
    while True:
        print("")
        title = "Student Menu"
        width = 40
        print("=" * width)
        print(title.center(width))
        print("=" * width)
        print("1. Update Personal Information")
        print("2. Course Enrolment")
        print("3. Course Material Access")
        print("4. Grades Tracking")
        print("5. Feedback Submission")
        print("6. Exit")
        print("-" * width)

        try:
            opt = int(input("\nYour choice: "))

            if opt == 1:
                upd_info.information_menu()
            elif opt == 2:
                course_enrol.course_enrolment_menu()
            elif opt == 3:
                material_access.course_material_access()
            elif opt == 4:
                grade_tracking.grades_menu()
            elif opt == 5:
                feedback_submission.feedback_menu()
            elif opt == 6:
                print("Exiting Student Menu")
                break
        except ValueError:
            print("Invalid input! Only integer between 1-6 is allowed.")


login_student_menu()
