import tkinter as tk

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tk.Canvas(window, width=200, height=200)
logo = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

#Labels
secret_label = tk.Label(text="Description: ")
secret_label.grid(column=0, row=1)
username_label = tk.Label(text="Username: ")
username_label.grid(column=0, row=2)
password_label = tk.Label(text="Password: ")
password_label.grid(column=0, row=3)

#Entries
description_entry = tk.Entry(width=35)
description_entry.grid(column=1, row=1, columnspan=2)
username_entry = tk.Entry(width=35)
username_entry.grid(column=1, row=2, columnspan=2)
password_entry = tk.Entry(width=18)
password_entry.grid(column=1, row=3)

#Buttons
generate_password_button = tk.Button(text="Generate Password")
generate_password_button.grid(column=2, row=3, columnspan=2)
add_button = tk.Button(text="Add", width=36)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()