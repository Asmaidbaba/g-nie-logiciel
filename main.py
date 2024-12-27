import mysql.connector

def MyConnect():
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "salma",
        database = "test_py"
    )
    return mydb

def insertEmployee(name, salary, position):

    mydb = MyConnect()
    mycursor = mydb.cursor()

    sql = "insert into employee (name, salary, position) values (%s, %s, %s)"
    val = (name , salary, position)

    mycursor.execute(sql,val)

    mydb.commit()

    print(mycursor.rowcount,"employee added")
    mydb.close()

def ViewAllEmpolyees():

    mydb = MyConnect()
    mycursor = mydb.cursor()

    sql = "SELECT * FROM employee"
    mycursor.execute(sql)

    rows = mycursor.fetchall()
    for row in rows:
        print(row)

def UpdateEmployee(id, new_salary):
    mydb = MyConnect()
    mycursor = mydb.cursor()

    sql = "update employee set salary= %s where id = %s"
    val=(new_salary , id)

    mycursor.execute(sql , val)
    mydb.commit()
    print(mycursor.rowcount , "updated")

def DeleteEmployee(id):
    mydb = MyConnect()
    mycursor = mydb.cursor()

    sql = "delete from employee where id = %s"
    val = (id,)
    mycursor.execute(sql , val)
    mydb.commit()
    print(mycursor.rowcount , "deleted")

def Main():
    while True:
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

if __name__ == "__main__":
    Main()
