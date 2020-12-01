import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("Window")

mainframe = ttk.Frame(root, padding='3 3 200 12')
mainframe.grid(column=0, row=0, sticky='nwes')
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

one = tk.StringVar(value="First")
two = tk.StringVar(value="Second")
three = tk.StringVar(value="Third")

first = ttk.Entry(mainframe, width=10, textvariable=one)
first.grid(column=1, row=1, sticky='we')
second = ttk.Entry(mainframe, width=10, textvariable=two, state='readonly')
second.grid(column=1, row=2, sticky='we')
third = ttk.Entry(mainframe, width=10, textvariable=three, state='disabled')
third.grid(column=1, row=3, sticky='we')
ttk.Label(mainframe, text='Fourth').grid(column=1, row=4, sticky='we')

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.mainloop()
