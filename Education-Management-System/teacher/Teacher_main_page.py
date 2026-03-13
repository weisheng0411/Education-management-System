from teacher import *

def main_menu():
    while True:
        # ... Print your main menu header ...

        print("\n------------------------------------------------------")
        print("---------Teacher Management System--------------------")
        print("------------------------------------------------------")
        print("1. Course Creation and Management")
        print("2. Student Enrolment")
        print("3. Grade and Assessment")
        print("4. Attendances Tracking")
        print("5. Report Generation")
        print("6. Exit")
        print("------------------------------------------------------")

        try:
            selection = int(input("Please enter your choice (1-6): "))
            if selection == 1:
                # Go to the sub-menu in Course_creation_and_management
                course_creation_and_management_menu()
            elif selection == 2:
                student_enrolment_menu()
            elif selection == 3:
                Grade_and_Assessment_Menu()
            elif selection == 4:
                attendance_tracking_menu()
            elif selection == 5:
                report_generation_menu()
            elif selection == 6:
                print("Thank you for visiting the system.\nExiting Teacher Management Page...")
                break
            else:
                print("Invalid choice! Please enter a number between 1 and 6.\n")
        except ValueError:
            print("Invalid input! Only integers 1–6 are allowed.\nPlease try again.")

main_menu()
