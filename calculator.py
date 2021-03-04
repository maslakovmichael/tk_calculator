import tkinter as tk
from tkinter import messagebox

AFCOLOR = 'green'
FCOLOR = 'red'
px = 2
py = 2
BD = 3
F = 18
BG = '#3FBFD2'

def add_digit(num):
    value = screen.get()
    if value[0] == '0' and len(value) == 1:
        value = value[1:]
    screen.delete(0, tk.END)
    screen.insert(0, value + str(num))


def add_operation(operation):
    value = screen.get()
    if value[-1] in '+-*/=':
        value = value[:-1]
    elif '+' in value or '-' in value or '*' in value or '/' in value:
        make_calc()
        value = screen.get()
    value += operation
    screen.delete(0, tk.END)
    screen.insert(0, value)


def make_calc():
    value = screen.get()
    if value[-2] == '/' and value[-1] == '0':
        value = value[:-1]
        screen.delete(0, tk.END)
        screen.insert(0, value)
    else:
        if value[-1] in '+-*/':
            value = value + value[:-1]
        screen.delete(0, tk.END)
        try:
            screen.insert(0, eval(value))
        except (NameError, SyntaxError):
            messagebox.showinfo('Внимание', 'На ноль делить нельзя')
            screen.insert(0, 0)
        except ZeroDivisionError:
            messagebox.showerror('Внимание', 'Ведите цифры')
            screen.insert(0, 0)

def clean_calc():
    screen.delete(0, tk.END)
    screen.insert(0, '0')


def add_digit_button(digit):
    return tk.Button(root,
                     font=('Arial', F),
                     text=str(digit),
                     bd=BD,
                     command=lambda: add_digit(digit))


def add_operation_button(operation):
    return tk.Button(root,
                     font=('Arial', F),
                     text=operation,
                     activeforeground=AFCOLOR,
                     fg=FCOLOR,
                     bd=BD,
                     command=lambda: add_operation(operation))


def add_calc_button(operation):
    return tk.Button(root,
                     font=('Arial', F),
                     text=operation,
                     activeforeground=AFCOLOR,
                     fg=FCOLOR,
                     bd=BD,
                     command=lambda: make_calc())


def add_clean_button(operation):
    return tk.Button(root,
                     font=('Arial', F),
                     text=operation,
                     activeforeground=AFCOLOR,
                     fg=FCOLOR,
                     bd=BD,
                     command=lambda: clean_calc())


def press_key(event):
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char in '+-*/':
        add_operation(event.char)
    elif event.char == '=' or event.char == '\r':
        make_calc()


root = tk.Tk()
root.geometry('270x310+500+200')
root.title('Калькулятор')
root.config(bg=BG)
root.bind('<Key>', press_key)


screen = tk.Entry(root, font=('Arial', 20), width=17, bd=BD, justify=tk.RIGHT)
screen.insert(0, '0')
screen.grid(row=0, column=0, columnspan=4, stick='we', padx=px, pady=py)

add_digit_button(1).grid(row=1, column=0, stick='wnes', padx=px, pady=py)
add_digit_button(2).grid(row=1, column=1, stick='wnes', padx=px, pady=py)
add_digit_button(3).grid(row=1, column=2, stick='wnes', padx=px, pady=py)
add_digit_button(4).grid(row=2, column=0, stick='wnes', padx=px, pady=py)
add_digit_button(5).grid(row=2, column=1, stick='wnes', padx=px, pady=py)
add_digit_button(6).grid(row=2, column=2, stick='wnes', padx=px, pady=py)
add_digit_button(7).grid(row=3, column=0, stick='wnes', padx=px, pady=py)
add_digit_button(8).grid(row=3, column=1, stick='wnes', padx=px, pady=py)
add_digit_button(9).grid(row=3, column=2, stick='wnes', padx=px, pady=py)
add_digit_button(0).grid(row=4, column=0, stick='wnes', padx=px, pady=py)

add_operation_button('+').grid(row=1, column=3, stick='wnes', padx=px, pady=py)
add_operation_button('-').grid(row=2, column=3, stick='wnes', padx=px, pady=py)
add_operation_button('/').grid(row=3, column=3, stick='wnes', padx=px, pady=py)
add_operation_button('*').grid(row=4, column=3, stick='wnes', padx=px, pady=py)

add_clean_button('C').grid(row=4, column=1, stick='wnes', padx=px, pady=py)
add_calc_button('=').grid(row=4, column=2, stick='wnes', padx=px, pady=py)

root.grid_columnconfigure(0, minsize=60)
root.grid_columnconfigure(1, minsize=60)
root.grid_columnconfigure(2, minsize=60)
root.grid_columnconfigure(3, minsize=60)

root.grid_rowconfigure(0, minsize=60)
root.grid_rowconfigure(1, minsize=60)
root.grid_rowconfigure(2, minsize=60)
root.grid_rowconfigure(3, minsize=60)
root.grid_rowconfigure(4, minsize=60)

root.mainloop()