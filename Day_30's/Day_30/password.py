from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if website == "" or password == "":
        messagebox.showinfo(title=website, message="Please add info ")

    else:
        is_ok = messagebox.askokcancel (title=website, message=f"These are the details entered:\nEmail :{email} "
                                   f"\n Password:{password}  \n Is it ok to save?")
        if is_ok:
            with open("data.txt", mode="a") as file:
                file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=100, pady=50)


canvas = Canvas(width=200 ,height=200,  highlightthickness=0)
logo_img= PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

titre_website = Label(text="Website")
titre_website.grid(column=0, row=1, sticky="w")

website_entry = Entry(width=52)
website_entry.grid(column=1, row=1, columnspan=2)

titre_email = Label(text="Email/username")
titre_email.grid(column=0, row=2, sticky="w")

email_entry = Entry(width=52)
email_entry.grid(column=1,row=2, columnspan=2)
email_entry.insert(0, "Sara_di@hotmail.be")


titre_pass = Label(text="Password")
titre_pass.grid(column=0, row=3, sticky="w")

password_entry = Entry(width=33)
password_entry.grid(column=1, row=3)

button_pass = Button(text="Generate Password", command=generate_pass)
button_pass.grid(column=2, row=3)

bouton_add = Button(text="add", width=45, command=save_data)
bouton_add.grid(column=1,row=4, columnspan=2)

window.mainloop()