import tkinter as tk
root = tk.Tk()
root.title("Tkinter Example")

label = tk.Label(root, text="Hello, Tkinter!")
label.pack(padx=20, pady=20)

root.mainloop()