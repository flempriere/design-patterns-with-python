import tkinter as tk
import tkinter.messagebox


# Write a slogan out to a message box
def ask_ok():
    tk.messagebox.askokcancel("R U OK Day", "How are you feeling?")


def ask_question():
    tk.messagebox.askquestion("Answer my riddles", "What is your favourite colour?")


def ask_retry():
    tk.messagebox.askretrycancel("Here we go again", "Shall we have another go?")


def ask_yesno():
    tk.messagebox.askyesno("Vibe check", "Are the vibes immaculate?")


def ask_yesnocancel():
    tk.messagebox.askyesnocancel("Choices...", "So many choices...")


button_params = [
    (ask_ok, "Ok"),
    (ask_question, "Question"),
    (ask_retry, "Retry"),
    (ask_yesno, "Yes / No"),
    (ask_yesnocancel, "Yes / No / Cancel"),
]

root = tk.Tk()
for cmd, label in button_params:
    but = tk.Button(root, text=label, command=cmd)
    but.pack(padx=10, pady=10)

root.mainloop()
