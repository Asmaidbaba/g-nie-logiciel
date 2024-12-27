    print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Update Salary")
        print("4. Delete Employee")
        print("5. Exit")

        choice = int(input("chose an option: "))
        if choice == 1:
            name = input("type name : ")
            salary = float(input("type salalry: "))
            position = input("type position: ")
            insertEmployee(name , salary , position)
        elif choice == 2:
            ViewAllEmpolyees()
        elif choice == 3:
            id = int(input("type their ID: "))
            salary = float(input("type the new salary: "))
            UpdateEmployee(id , salary)
        elif choice == 4:
            id = int(input("type their id: "))
            DeleteEmployee(id)
        elif choice == 5:
            print("goodbye!!")
            break
        else:
            print("try again!!")