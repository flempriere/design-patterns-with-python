import tkinter as tk


def build_ui():
    root = tk.Tk()
    root.geometry("100x150")

    label_frame = tk.LabelFrame(
        root, text="State Data", borderwidth=7, relief=tk.RAISED
    )
    label_frame.pack(pady=5)

    tk.Label(label_frame, text="State").pack()
    tk.Label(label_frame, text="Abbrev").pack()
    tk.Label(label_frame, text="Capital").pack()
    tk.Label(label_frame, text="Founded").pack()

    tk.mainloop()


if __name__ == "__main__":
    build_ui()
