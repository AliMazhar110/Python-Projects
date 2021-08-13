import tkinter
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    password_entry.delete(0, tkinter.END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_list = [choice(letters) for _ in range(randint(8, 10))]
    numbers_list = [choice(numbers) for _ in range(randint(2, 4))]
    symbols_list = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = letters_list + numbers_list + symbols_list
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(tkinter.END, password)
    pyperclip.copy(password)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get().upper()
    if len(website) == 0:
        messagebox.showwarning(title="Field Empty", message="Please! Fill all the details.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                website_list = [key for key in data.keys()]
        except FileNotFoundError:
            messagebox.showerror(title="No Data", message="No Data Available At The Moment.")
        else:
            if website not in website_list:
                messagebox.showerror(title="Mismatch", message=F"No Details for {website} In The Data.")
            else:
                new_dict = data[website]
                messagebox.showinfo(title=website, message="Email: " + new_dict["email"] +
                                                           "\nPassword: " + new_dict["password"])


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get().upper()
    email = email_entry.get()
    password = password_entry.get()
    is_ok = False
    if website == "" or password == "":
        messagebox.showwarning(title="Field Empty", message="Please! Fill all the details.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                              f"\nPassword: {password} \nIs it ok to save?")

    if is_ok:
        # new dict for json file
        new_dict = {website: {
            "email": email,
            "password": password
        }}
        try:
            with open(file="data.json", mode="r") as data_file:
                # reading old data
                data = json.load(data_file)
                # updating old data with new data
                data.update(new_dict)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                # saving the data in file
                json.dump(new_dict, data_file, indent=4)
        else:
            with open("data.json", "w") as data_file:
                # saving the data in file
                json.dump(data, data_file, indent=4)
        finally:
            # clearing the entry after saving the data
            website_entry.delete(0, tkinter.END)
            password_entry.delete(0, tkinter.END)
            website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #

# screen setup
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# canvas setup
canvas = tkinter.Canvas(width=200, height=200)
logo_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# website label
website_label = tkinter.Label(text="Website:")
website_label.grid(column=0, row=1, padx=5, pady=5)

# email label
email_label = tkinter.Label(text="Email/Username:")
email_label.grid(column=0, row=2, padx=5, pady=5)

# password label
password_label = tkinter.Label(text="Password:")
password_label.grid(column=0, row=3, padx=5, pady=5)

# website entry
website_entry = tkinter.Entry(width=21)
website_entry.grid(column=1, row=1, sticky="EW", padx=5, pady=5)
website_entry.focus()

# email entry
email_entry = tkinter.Entry(width=35)
email_entry.insert(tkinter.END, "luqmani.mazhar.ali@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW", padx=5, pady=5)

# password entry
password_entry = tkinter.Entry(width=21)
password_entry.grid(column=1, row=3, sticky="EW", padx=5, pady=5)

# generate password button
generate_password = tkinter.Button(text="Generate Password", command=password_generator)
generate_password.grid(column=2, row=3, sticky="EW", padx=5, pady=5)

# add button
add_button = tkinter.Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW", padx=5, pady=5)

# search button
search_button = tkinter.Button(text="Search", command=find_password)
search_button.grid(column=2, row=1, sticky="EW", padx=5, pady=5)

window.mainloop()
