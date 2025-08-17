# from tkinter import messagebox

# from tkinter import *
# window = Tk()
# window.title("Welcome to Game")
# window.mainloop()   
# messagebox.showinfo("Welcome")

""" 
Guess a number - 2
Multiply - 5*2
Add - 8 + 10
Multiply  - 2 * 18
Add - 3 + 36


N -> 10N - 19 ->
2  = 10N - 19 
"""

import tkinter as tk

def show_input():
    user_input = "Hello"
    lbl.config(text=f"Input: {user_input}")

root = tk.Tk()
root.title("TextBox Input")
root.geometry("600x400")

txt = tk.Entry(root, width=50)
txt.pack()

btn = tk.Button(root, text="Print", command=show_input)
btn.pack()

lbl = tk.Label(root, text="")
lbl.pack()

root.mainloop()   