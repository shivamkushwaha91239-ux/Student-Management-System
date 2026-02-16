import tkinter as tk
from tkinter import messagebox

import mysql.connector
import os

# -------- DATABASE CONNECT --------
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="568900",   # apna mysql password
    database="studentdb"
)
cursor = con.cursor()

# -------- REGISTER FUNCTION --------
def register():
    username = entry_user.get().strip().lower()
    password = entry_pass.get().strip()

    if username == "" or password == "":
        messagebox.showerror("Error", "All fields required")
        return

    sql = "INSERT INTO users(username,password) VALUES(%s,%s)"
    val = (username, password)

    cursor.execute(sql, val)
    con.commit()

    messagebox.showinfo("Success", "User Registered Successfully")

# -------- LOGIN FUNCTION --------
from tkinter import messagebox
import os

def login():
    username = entry_user.get()
    password = entry_pass.get()

    sql = "SELECT * FROM users WHERE username=%s AND password=%s"
    val = (username, password)

    cursor.execute(sql, val)
    data = cursor.fetchone()

    if data:
        messagebox.showinfo("Success", "Login Successful")

        root.destroy()   # login window band

        # main.py open karo
        os.system("python main.py")

    else:
        messagebox.showerror("Error", "Invalid Username or Password")



# -------- GUI WINDOW --------
root = tk.Tk()
root.title("Shivam Software Login")
root.geometry("400x300")
root.config(bg="navy blue")  # background color set karne ke liye

# Title
title = tk.Label(root, text="LOGIN SYSTEM", font=("Arial", 18, "bold"), bg="black", fg="white")
title.pack(pady=20)  #login system heading show karne ke liye

# Username
tk.Label(root, text="Username", bg="black", fg="white").pack() #username label show karne ke liye
entry_user = tk.Entry(root, width=30) #text field for username input karne ke liye
entry_user.pack(pady=5)

# Password
tk.Label(root, text="Password", bg="red", fg="white").pack() #password label show karne ke liye
entry_pass = tk.Entry(root, width=30, show="*") 
entry_pass.pack(pady=5) #text field for password input karne ke liye, show="*" se password hide ho jata hai

# Buttons
tk.Button(root, text="Register", width=15, bg="green", fg="white", command=register).pack(pady=10) # register button click karne par register function call hoga
tk.Button(root, text="Login", width=15, bg="blue", fg="white", command=login).pack() # login button click karne par login function call hoga

root.mainloop()  # GUI window ko run karne ke liye / window is running until user closes it
