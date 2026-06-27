import tkinter as tk
import tkinter.messagebox

# Set up the window
root = tk.Tk()


# Write a slogan out to a message box
def display_info():

    tk.messagebox.showinfo("Info", "Consider yourself informed")


def display_warning():
    tk.messagebox.showwarning("Warning", "You should be careful...")


def display_error():
    tk.messagebox.showerror("Error", "Well that didn't work!")


info_button = tk.Button(root, text="INFO", fg="Blue", command=display_info)
info_button.pack(side=tk.LEFT, padx=10)

warning_button = tk.Button(root, text="WARNING", fg="Yellow", command=display_warning)
warning_button.pack(padx=10)

error_button = tk.Button(root, text="ERROR", fg="red", command=display_error)
error_button.pack(side=tk.RIGHT, padx=10)

root.mainloop()
