import mysql.connector
import getpass

# -------- DATABASE CONNECT --------
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="568900",
    database="studentdb"
)

cursor = con.cursor()
print("Database connected successfully")

# -------- REGISTER --------
def register():
    username = input("Enter username: ").strip().lower()
    password = getpass.getpass("Enter password: ").strip()

    sql = "INSERT INTO users(username,password) VALUES(%s,%s)"
    val = (username, password)

    cursor.execute(sql, val)
    con.commit()
    print("User registered successfully")

# -------- LOGIN --------
def login():
    username = input("Enter username: ").strip().lower()
    password = getpass.getpass("Enter password: ").strip()

    sql = "SELECT * FROM users WHERE LOWER(username)=%s AND password=%s"
    val = (username, password)

    cursor.execute(sql, val)
    data = cursor.fetchone()

    if data:
        print("Login successful ✅")
        
        # 🔥 yaha main project open hoga
        import main   # student management file name main.py hona chahiye

    else:
        print("Invalid username or password ❌")

# -------- MENU --------
while True:
    print("\n===== LOGIN SYSTEM =====")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        register()

    elif choice == "2":
        login()

    elif choice == "3":
        print("Thank you")
        break

    else:
        print("Invalid choice")
