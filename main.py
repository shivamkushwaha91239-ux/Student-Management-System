import mysql.connector

# database connect
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="568900",   # apna mysql password
    database="studentdb"
)

cursor = con.cursor()
print("Database connected successfully")

# ---------------- ADD STUDENT ----------------
def add_student():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    course = input("Enter course: ")
    email = input("Enter email: ")

    sql = "insert into students(name,age,course,email) values(%s,%s,%s,%s)"
    val = (name, age, course, email)

    cursor.execute(sql, val)
    con.commit()
    print("Student added successfully")

# ---------------- SHOW STUDENTS ----------------
def show_students():
    cursor.execute("select * from students")
    data = cursor.fetchall()

    print("\n--- All Students ---")
    for row in data:
        print(row)

# ---------------- SEARCH STUDENT ----------------
def search_student():
    name = input("Enter name to search: ")

    sql = "SELECT * FROM students WHERE LOWER(name) LIKE LOWER(%s)"
    val = ("%" + name + "%",)

    cursor.execute(sql, val)
    data = cursor.fetchall()

    if data:
        print("\n--- Student Found ---")
        for row in data:
            print(row)
    else:
        print("Student not found")

# ---------------- DELETE STUDENT ----------------
def delete_student():
    name = input("Enter name to delete: ")
    sql = "delete from students where name=%s"
    val = (name,)

    cursor.execute(sql, val)
    con.commit()
    print("Student deleted")

# ---------------- UPDATE STUDENT ----------------
def update_student():
    name = input("Enter student name to update: ")

    new_course = input("Enter new course: ")
    new_email = input("Enter new email: ")

    sql = "update students set course=%s, email=%s where name=%s"
    val = (new_course, new_email, name)

    cursor.execute(sql, val)
    con.commit()
    print("Student updated successfully")

# ---------------- MENU ----------------
while True:
    print("\n===== STUDENT MANAGEMENT =====")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Update Student")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        show_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        update_student()

    elif choice == "6":
        break

    else:
        print("Invalid choice")
