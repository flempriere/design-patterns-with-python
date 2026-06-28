import tkinter as tk
from tkinter import messagebox

# Set up the window
root = tk.Tk()


# Write a slogan out to a message box
def display_slogan():
    messagebox.showinfo("Our Message", "Tkinter is easy to use")


# create a button to call the message
slogan = tk.Button(root, text="Hello", command=display_slogan)
slogan.pack(side=tk.LEFT, padx=10)

# create a quit button
quit_button = tk.Button(root, text="QUIT", fg="red", command=quit)
quit_button.pack(side=tk.RIGHT, padx=10)

root.mainloop()
