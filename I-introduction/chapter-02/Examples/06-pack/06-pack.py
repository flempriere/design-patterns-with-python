import tkinter as tk

root = tk.Tk()

# Create first row, taking up the entire X dimension
first_row = tk.Frame(root)
first_row.pack(fill=tk.X)

# Add widgets to the first row
label_1 = tk.Label(first_row, text="Name", width=7)
label_1.pack(side=tk.LEFT, padx=5, pady=5)

entry_1 = tk.Entry(first_row)
entry_1.pack(fill=tk.X, padx=5, pady=5)  # fill the remaining X space

# Create the second row, again taking the entire X dimension
second_row = tk.Frame(root)
second_row.pack(fill=tk.X)

# Add widgets to the second row
label_2 = tk.Label(second_row, text="Address", width=7)
label_2.pack(side=tk.LEFT, padx=5, pady=5)

entry_2 = tk.Entry(second_row)
entry_2.pack(fill=tk.X, padx=5, pady=5)

root.mainloop()
