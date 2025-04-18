from tkinter import *


window = Tk()
window.title("Login Form")
window.geometry("340x340")
window.resizable(0, 0)
window.config(bg='#333333')

# ========== Creating Widgets ===========#
login_label = Label(window, text="Login",)
username_label = Label(window, text="Username")
username_entry = Entry(window,)
password_label = Label(window, text="Password")
password_entry = Entry(window, show="*")
login_button = Button(window, text="login",)

# ========== Placing Widgets ===========#
login_label.grid(row=0, column=0, columnspan=2)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1,padx=5)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1,padx=5)
login_button.grid(row=3,column=0,columnspan=2)




window.mainloop()