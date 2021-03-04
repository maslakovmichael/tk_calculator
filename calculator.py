import tkinter as tk
from tkinter import messagebox

ACTIVE_FCOLOR = 'green'
FCOLOR = 'red'
px = 2
py = 2
BD = 3
F = 18
BG = '#3FBFD2'

def add_digit(num):
    pass

def add_operation(operation):
    pass

def make_calc():
    pass

def clear_calc():
    pass


def add_digit_button(digit):
    return tk.Button(root, font=('Arial', F), text=str(digit), bd=BD,
                     activeforeground=ACTIVE_FCOLOR, fg=FCOLOR, command=lambda: add_digit(digit))

def add_operation_button(operation):
    return tk.Button(root, font=('Arial', F), text=operation, bd=BD,
                     activeforeground=ACTIVE_FCOLOR, fg=FCOLOR, command=lambda: add_operation(operation))

def add_calc_button(operation):
    return tk.Button(root, font=('Arial', F), text=operation, bd=BD,
                     activeforeground=ACTIVE_FCOLOR, fg=FCOLOR, command=lambda: make_calc())

def add_clear_button(operation):
    return tk.Button(root, font=('Arial', F), text=operation, bd=BD,
                     activeforeground=ACTIVE_FCOLOR, fg=FCOLOR, command = lambda: clear_calc())


def press_key(event):
    pass

root = tk.Tk()
root.geometry('270x310+500+200')
root.title('Калькулятор')
root.config(bg=BG)
# root.bind('<key>', press_key)

screen = tk.Entry(root, font=('Arial', 20), width=17, bd=BD, justify=tk.RIGHT)
screen.insert(0, '0')
screen.grid(row=0, column=0, columnspan=4, sticky='we', padx=px, pady=py)

add_digit_button(1).grid(row=1, column=0, sticky='wens', padx=px, pady=py)
add_digit_button(2).grid(row=1, column=1, sticky='wens', padx=px, pady=py)
add_digit_button(3).grid(row=1, column=2, sticky='wens', padx=px, pady=py)
add_digit_button(4).grid(row=2, column=0, sticky='wens', padx=px, pady=py)
add_digit_button(5).grid(row=2, column=1, sticky='wens', padx=px, pady=py)
add_digit_button(6).grid(row=2, column=2, sticky='wens', padx=px, pady=py)
add_digit_button(7).grid(row=3, column=0, sticky='wens', padx=px, pady=py)
add_digit_button(8).grid(row=3, column=1, sticky='wens', padx=px, pady=py)
add_digit_button(9).grid(row=3, column=2, sticky='wens', padx=px, pady=py)
add_digit_button(0).grid(row=4, column=0, sticky='wens', padx=px, pady=py)

add_operation_button('+').grid(row=1, column=3, sticky='wens', padx=px, pady=py)
add_operation_button('-').grid(row=2, column=3, sticky='wens', padx=px, pady=py)
add_operation_button('/').grid(row=3, column=3, sticky='wens', padx=px, pady=py)
add_operation_button('*').grid(row=4, column=3, sticky='wens', padx=px, pady=py)

add_clear_button('C').grid(row=4, column=1, sticky='wens', padx=px, pady=py)
add_clear_button('=').grid(row=4, column=2, sticky='wens', padx=px, pady=py)

root.grid_rowconfigure(0, minsize=60)
root.grid_rowconfigure(1, minsize=60)
root.grid_rowconfigure(2, minsize=60)
root.grid_rowconfigure(3, minsize=60)
root.grid_rowconfigure(4, minsize=60)

root.columnconfigure(0, minsize=60)
root.columnconfigure(1, minsize=60)
root.columnconfigure(2, minsize=60)
root.columnconfigure(3, minsize=60)

root.mainloop()