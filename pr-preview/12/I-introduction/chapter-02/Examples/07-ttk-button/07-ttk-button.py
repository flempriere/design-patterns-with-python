import tkinter as tk
import tkinter.messagebox
import tkinter.ttk as ttk

# Set up the window
root = tk.Tk()


# Write a slogan out to a message box
def display_slogan():
    tk.messagebox.showinfo("Our Message", "Tkinter is easy to use")


# create a button to call the message
slogan = ttk.Button(root, text="Hello", command=display_slogan)
slogan.pack(side=tk.LEFT, padx=10)

# create a quit button
ttk.Style().configure("W.TButton", foreground="red")
quit_button = ttk.Button(root, text="QUIT", command=quit, style="W.TButton")
quit_button.pack(side=tk.RIGHT, padx=10)

root.mainloop()
