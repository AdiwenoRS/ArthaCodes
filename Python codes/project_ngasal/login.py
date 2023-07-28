import tkinter as tk

def check_login():
    username = entry_username.get()
    password = entry_password.get()

    if username == "admin" and password == "1234":
        label_result.config(text="Login Successful!", fg="green")
    else:
        label_result.config(text="Login Failed!", fg="red")

root = tk.Tk()
root.title("Login")

label_username = tk.Label(root, text="Username:")
label_password = tk.Label(root, text="Password:")

entry_username = tk.Entry(root)
entry_password = tk.Entry(root, show="*")

button_login = tk.Button(root, text="Login", command=check_login)

label_result = tk.Label(root)

label_username.grid(row=0, column=0, sticky="W")
label_password.grid(row=1, column=0, sticky="W")

entry_username.grid(row=0, column=1)
entry_password.grid(row=1, column=1)

button_login.grid(row=2, column=0, columnspan=2, pady=10)

label_result.grid(row=3, column=0, columnspan=2)

root.mainloop()