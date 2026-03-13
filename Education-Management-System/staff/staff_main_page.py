import student_record
import timetable_management
import resource_allocation
import event_management
import communication

def main_menu():
    while True:
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

            if selection==1:
                student_record.student_record_menu()
            elif selection==2:
                timetable_management.timetable_menu()
            elif selection==3:
                resource_allocation.resource_allocation_menu()
            elif selection==4:
                event_management.event_menu()
            elif selection==5:
                communication.communication_menu()
            elif selection == 6:
                print("Thank you for visiting the system.\nExiting Staff Management Page...")
                break
            else:
                print("Invalid choice! Please enter a number between 1-6.")

        except ValueError:
            print("Invalid input! Only integer between 1-6 is allowed.\nPlease enter a valid number.")


main_menu()
