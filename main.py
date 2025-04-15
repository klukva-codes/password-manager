from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

BG_COLOR = "#f7f5dd"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    passwort_input.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    random_letters = [choice(letters) for char in range(randint(8, 10))]
    random_symbols = [choice(symbols) for char in range(randint(2, 4))]
    random_numbers = [choice(numbers) for char in range(randint(2, 4))]

    password_list = random_numbers + random_symbols + random_letters
    shuffle(password_list)
    password = "".join(password_list)
    passwort_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_input.get()

    if len(website) == 0:
        messagebox.showinfo(title="Oops", message="Please don`t leve the field empty!")
    else:
        try:
            with open("data.json", mode='r') as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            messagebox.showinfo(title="Oops", message="No Data File Found")
        else:
            if website in data:
                email = data[website]['email']
                password = data[website]['password']
                messagebox.showinfo(title=website,
                                    message=f"Website: {website} \nEmail: {email} \nPassword: {password}")
            else:
                messagebox.showinfo(title="Oops", message="No Data File Found")
        finally:
            website_input.delete(0, END)
            passwort_input.delete(0, END)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_input.get()
    email = login_input.get()
    password = passwort_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }

    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don`t leve any fields empty!")
    else:
        try:
            with open("data.json", mode='r') as data_file:
                #читаем старые данные
                data = json.load(data_file)
        except FileNotFoundError:
            #создаем файл если его не было
            with open("data.json", mode='w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            is_ok = messagebox.askokcancel(title=website,
                                           message=f"There are the details entered?: \nEmail: {email} "
                                                   f"\nPassword: {password} \nIs it ok to save?")
            if is_ok:
                #добавляем к старым новые
                data.update(new_data)
                #сохраняем обновленные данне
                with open("data.json", mode='w') as data_file:
                    json.dump(data, data_file, indent=4)
        finally:
            #в любом случае очищаем поле ввода
            website_input.delete(0, END)
            passwort_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=30, bg=BG_COLOR)

canvas = Canvas(width=200, height=200, bg=BG_COLOR, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

#Labels
website_label = Label(text="Website:", bg=BG_COLOR)
website_label.grid(column=0, row=1)
login_label = Label(text="Email / Username:", bg=BG_COLOR, width=18)
login_label.grid(column=0, row=2)
password_label = Label(text="Password:", bg=BG_COLOR)
password_label.grid(column=0, row=3)

#Inputs
website_input = Entry(width=21, highlightbackground=BG_COLOR)
website_input.grid(column=1, row=1)
website_input.focus()


login_input = Entry(width=38, highlightbackground=BG_COLOR)
login_input.grid(column=1, row=2, columnspan=2)
login_input.insert(END, "myemail@gmail.com")


passwort_input = Entry(width=21, highlightbackground=BG_COLOR)
passwort_input.grid(column=1, row=3)


#Buttons
g_pass_button = Button(text="Generate Password", highlightbackground=BG_COLOR, command=generate_password)
g_pass_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, highlightbackground=BG_COLOR, command=save_data)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text='Search', width=13, highlightbackground=BG_COLOR, command=find_password)
search_button.grid(column=2, row=1)

window.mainloop()
