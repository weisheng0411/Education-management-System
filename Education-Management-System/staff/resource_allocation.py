def open_resource():
    resources=[]
    with open("resource.txt",'r')as gFile:
        for line in gFile:
            line=line.rstrip().split(",")
            #index label
            item={
                "Classroom":line[0],
                "Resource":line[1],
                "Number":line[2],
                "Available":line[3]
            }
            resources.append(item)
        return resources

def update_resource():
    resources=open_resource()
    with open("resource.txt", 'w') as gFile:
        for resource in resources:
            gFile.write(",".join(resource.values())+"\n")
            print(f"Classroom: {resource['Classroom']} \t\t Resource: {resource['Resource']} \t\t Quantity: {resource['Number']}\n")

def continue_searching():
    while True:
        try:
            proceed = input("\nContinue searching?(Y/N):").capitalize()
            if proceed == 'Y':
                return True
            elif proceed == 'N':
                print("Thank you for searching!")
                return False
            else:
                raise ValueError("Invalid input. Please enter only Y or N")
        except ValueError as e:
            print(e)

def search_by_classroom():
    resources=open_resource()
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

def search_by_resource():
    resources=open_resource()
    while True:
        resource_enter=input("Enter the resource name:").capitalize()
        found=False #track if the resource is found
        for resource in resources:
            if resource['Resource']==resource_enter:
                print(f"The {resource_enter} is in {resource['Classroom']} with quantity {resource['Number']}")
                found=True #mark as found
        if not found:
            print("Sorry,classroom entered is not found")
        if not continue_searching():
            break

def resource_allocation():
    resources=open_resource()
    update_resource()
    while True:
        classroom=input("Enter the classroom to allocate resource:").title()
        class_found=False
        for resource in resources:
            if classroom ==resource['Classroom']:
                class_found=True
                break
        if not class_found:
            print(f"Classroom {classroom} not found. Please enter again\n")
            continue

        while True:
            allocate_resource=input("Enter the resource name need to allocate:").capitalize()
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
            try:
                quantity = int(input(f"Enter the quantity of {allocate_resource} to allocate: "))
                if quantity <= 0:
                    raise ValueError("Quantity must be greater than 0!")
                break  # Exit loop if valid
            except ValueError as e: #e is the error that made by the user
                print(f"Invalid input: {e}")

        done_allocate=False
        for resource in resources:
            if resource['Resource']==allocate_resource:
                available=int(resource['Available'])
                number=int(resource['Number'])
                if quantity > available:
                    print(f"\nNot enough {allocate_resource}. Only {available} left.")
                    break #print one time available message
                else:
                    resource['Available'] = str(available - quantity)
                    resource['Number']=str(number+quantity)
                    done_allocate=True
                break

        if done_allocate:
            with open("resource.txt", 'w') as gFile:
                for resource in resources:
                    gFile.write(",".join(resource.values()) + "\n")

            print("Update Resource List:")
            update_resource()

        proceed_again=input("\nProceed allocated?(Y/N):").capitalize()
        if proceed_again == 'N':
            print("Resource allocation completed!")
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
        print("3. Allocate resource")
        print("4. Exit")

        try:
            choice=int(input("Enter your choice:"))
            if choice ==1:
                search_by_classroom()
            elif choice==2:
                search_by_resource()
            elif choice==3:
                resource_allocation()
            elif choice==4:
                print("Thank you for visiting!")
                break
            else:
                print("Invalid choice!")
        except ValueError:
            print("Invalid input! Only integer 1-3 is allowed.")

# resource_allocation_menu()
