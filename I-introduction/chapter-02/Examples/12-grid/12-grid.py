import tkinter as tk

root = tk.Tk()
root.title("grid")

# Add widgets to the first row
label_1 = tk.Label(root, text="Name")
label_1.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

entry_1 = tk.Entry(root)
entry_1.grid(row=0, column=1)

# Add widgets to the second row
label_2 = tk.Label(root, text="Address")
label_2.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

entry_2 = tk.Entry(root)
entry_2.grid(row=1, column=1, padx=5)

root.mainloop()
