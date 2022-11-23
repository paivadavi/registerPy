from tkinter import *

import database
from database import register
import sqlite3 as sql


def register():
    connection = sql.connect('registration.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO usersdata VALUES (:name_value,:surname_value,:email_value,:password_value)",
                   {
                       'name_value': name_value.get(),
                       'surname_value': surname_value.get(),
                       'email_value': email_value.get(),
                       'password_value': password_value.get()

                   })
    connection.commit()
    connection.close()



root = Tk()

root.title("RegisterPy")
root.geometry("600x600")
root.resizable(False, False)

Label(root, text="Python Registration", font="sans-serif 25").pack(pady=50)
Label(text="Name", font=23).place(x=100, y=150)
Label(text="Surname", font=23).place(x=100, y=200)
Label(text="Email", font=23).place(x=100, y=250)
Label(text="Password", font=23).place(x=100, y=300)

#entry
name_value = StringVar()
surname_value = StringVar()
email_value = StringVar()
password_value = StringVar()

name_entry = Entry(root, textvariable=name_value, width=30, bd=2, font=20)
name_entry.place(x=200, y=150)

surname_entry = Entry(root, textvariable=surname_value, width=30, bd=2, font=20)
surname_entry.place(x=200, y=200)

email_entry = Entry(root, textvariable=email_value, width=30, bd=2, font=20)
email_entry.place(x=200, y=250)

password_entry = Entry(root, textvariable=password_value, width=30, bd=2, font=20)
password_entry.place(x=200, y=300)

# check button
check_value = IntVar()
check_btn = Checkbutton(text="remember me?", variable=check_value)
check_btn.place(x=200, y=340)

register_btn = Button(text="Register", font=20, width=11, height=2,
                      command=register
                      )
register_btn.place(x=250, y=380)







root.mainloop()