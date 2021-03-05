import tkinter as tk
from tkinter import messagebox

AFCOLOR = 'green' # цвет текста кнопки при наведении мыши
FCOLOR = 'blue'   # цвет текста кнопки
px = 2            # отступ по х
py = 2            # отступ по у
BD = 3            # граница
F = 18            # размер шрифта
BG = '#3FBFD2'    # цвет окна root


"""Функция добавления цифры на экран screen"""
def add_digit(num):
    value = screen.get()                    # считываем содержимое экрана
    if value[0] == '0' and len(value) == 1: # если там только ноль, то берем содержимое без него
        value = value[1:]
    screen.delete(0, tk.END)                # удаляем содержимое экрана
    screen.insert(0, value + str(num))      # вставляем содержимое с добавлением цифры-значения кнопки

"""Функция добавлени точки"""
def add_dot(operation):
    value = screen.get()           # считываем содержимое экрана
    if value[-1] == '.':           # если эта точка стоит в последним символом
        value = value[:-1]         # тогда убираем эту точку
        value += operation         # иначе если точки в содержимом нет - то добавляем ее
    elif '.' in value:             # если точка уже есть в содержимом экрана
        value = value              # если точка в содержимом есть, но она не в конце, то ничего не добавится
    else:
        value += operation         # иначе если точки в содержимом нет - то добавляем ее
    screen.delete(0, tk.END)       # удаляем содержимое экрана
    screen.insert(0, value)        # вставляем содержимое с добавлением цифры-значения кнопки


"""Функция добавления операции на экран screen"""
def add_operation(operation):
    value = screen.get()                     # считываем содержимое экрана
    if value[-1] in '+-*/=':                 # если последний знак содержимого уже есть знак какой то операции
        value = value[:-1]                   # то удаляем его из содержимого экрана, чтоб не было знака за знаком
    elif '+' in value or '-' in value or '*' in value or '/' in value:
        make_calc()                          # если в содержимом уже есть знак операции не на последнем месте
        value = screen.get()                 # тогда вызываем функцию make_calc() для производства вычисления и считываем данные с экрана
    value += operation                       # если знаков нет в содержимом экрана, то добавляем в конец символ операции кнопки
    screen.delete(0, tk.END)                 # удаляем содержимое экрана
    screen.insert(0, value)                  # вставляем содержимое с добавлением цифры-значения кнопки

"""Функция выполнения вычислений"""
def make_calc():
    value = screen.get()                       # считываем содержимое экрана
    if value[-2] == '/' and value[-1] == '0':  # проверяем на запись деления на ноль
        value = value[:-1]                     # если проверка проходит - удаляем последний символ ноля из содержимого экрана
        screen.delete(0, tk.END)               # удаляем содержимое экрана
        screen.insert(0, value)                # вставляем содержимое с добавлением цифры-значения кнопки
    else:
        if value[-1] in '+-*/':                # если последний символ содержимого экрана знак операции и потом нажимается кнопка '='
            value = value + value[:-1]         # тогда к содержимому экрана добавляется еще раз содержимое экрана, но без последнего символа операции
        screen.delete(0, tk.END)               # удаляем содержимое экрана
        try:
            screen.insert(0, eval(value))      # добавляем на екран результат функции eval(value)
        except (NameError, SyntaxError):       # в случае ошибок появится окно с предупреждением (messagebox)
            messagebox.showinfo('Внимание', 'На ноль делить нельзя')
            screen.insert(0, 0)                # на экран выводим ноль
        except ZeroDivisionError:              # в случае ошибок появится окно с предупреждением (messagebox)
            messagebox.showerror('Внимание', 'Ведите цифры')
            screen.insert(0, 0)                # на экран выводим ноль

"""функция очистки экрана"""
def clean_calc():
    screen.delete(0, tk.END)
    screen.insert(0, '0')

"""Функция добавления кнопок с цифрами"""
def add_digit_button(digit):
    return tk.Button(root,
                     font=('Arial', F),                 # шрифт кнопки
                     text=str(digit),                   # добавляем символ цифры на кнопку
                     bd=BD,                             # розмер граници кнопки
                     command=lambda: add_digit(digit))  # в качестве исполняемой операции через lambda вызываем функцию add_digit()
                                                        # lambda - чтоб функция add_digit() не выполнялась сразу при создании кнопки

"""Функция добавления кнопок операций"""
def add_operation_button(operation):
    return tk.Button(root,
                     font=('Arial', F),                   # шрифт кнопки
                     text=operation,                      # добавляем символ цифры на кнопку
                     activeforeground=AFCOLOR,            # цвет текста кнопки при наведении курсора мыши
                     fg=FCOLOR,                           # цвет текста кнопки
                     bd=BD,                               # розмер граници кнопки
                     command=lambda: add_operation(operation))  # в качестве исполняемой операции через lambda вызываем функцию add_operation()
                                                          # lambda - чтоб функция add_operation() не выполнялась сразу при создании кнопки

"""Функция добавления кнопки точки"""
def add_dot_button(operation):
    return tk.Button(root,
              font=('Arial', F),                   # шрифт кнопки
              text=operation,                      # добавляем символ цифры на кнопку
              activeforeground=AFCOLOR,            # цвет текста кнопки при наведении курсора мыши
              fg=FCOLOR,                           # цвет текста кнопки
              bd=BD,                               # розмер граници кнопки
              command=lambda: add_dot(operation))  # в качестве исполняемой операции через lambda вызываем функцию add_dot()
                                                   # lambda - чтоб функция add_dot() не выполнялась сразу при создании кнопки

"""Функция добавления кнопки '=' - выполнение вычисления"""
def add_calc_button(operation):
    return tk.Button(root,
                     font=('Arial', F),                 # шрифт кнопки
                     text=operation,                    # добавляем символ цифры на кнопку
                     activeforeground=AFCOLOR,          # цвет текста кнопки при наведении курсора мыши
                     fg=FCOLOR,                         # цвет текста кнопки
                     bd=BD,                             # розмер граници кнопки
                     command=lambda: make_calc())       # в качестве исполняемой операции через lambda вызываем функцию make_calc()
                                                        # lambda - чтоб функция make_calc() не выполнялась сразу при создании кнопки

"""Функция добавления кнопки очистки экрана"""
def add_clean_button(operation):
    return tk.Button(root,
                     font=('Arial', F),                 # шрифт кнопки
                     text=operation,                    # добавляем символ цифры на кнопку
                     activeforeground=AFCOLOR,          # цвет текста кнопки при наведении курсора мыши
                     fg='red',                          # цвет текста кнопки
                     bd=BD,                             # розмер граници кнопки
                     command=lambda: clean_calc())      # в качестве исполняемой операции через lambda вызываем функцию clean_calc()
                                                        # lambda - чтоб функция clean_calc() не выполнялась сразу при создании кнопки

"""Функция для набора цифр и операций с клавиатуры"""
def press_key(event):
    if event.char.isdigit():                      # Если в пришедшем событии есть символ цифры
        add_digit(event.char)                     # Тогда выполняется функция add_digit(символ_цифры)
    elif event.char in '+-*/':                    # Если в пришедшем событии есть символ операции
        add_operation(event.char)                 # Тогда выполняется функция add_operation(символ_операции)
    elif event.char == '=' or event.char == '\r': # Если в пришедшем событии есть символ '=' или нажат Enter
        make_calc()                               # Тогда выполняется функция make_calc()


root = tk.Tk()                     # Создаем главное окно
root.geometry('270x362+500+200')   # задаем размеры главного окна
root.resizable(False, False)       # делаем окно неизменяемых размеров
root.title('Калькулятор')          # задаем титульную надпись главного окна
root.config(bg=BG)                 # задаем цвет главного окна
root.bind('<Key>', press_key)      # задаем слушатель событий - какие событыя слышать и что выполнять (слушает нажатие кнопок на клавиатуре)


screen = tk.Entry(root, font=('Arial', 20), width=17, bd=BD, justify=tk.RIGHT) # Создаем екран калькулятора
screen.insert(0, '0')                                                          # устанавливаем изначально ноль
screen.grid(row=0, column=0, columnspan=4, stick='we', padx=px, pady=py)       # задаем параметры расположения екрана

add_digit_button(1).grid(row=1, column=0, stick='wnes', padx=px, pady=py)  # создаем кнопки с цифрами
add_digit_button(2).grid(row=1, column=1, stick='wnes', padx=px, pady=py)
add_digit_button(3).grid(row=1, column=2, stick='wnes', padx=px, pady=py)
add_digit_button(4).grid(row=2, column=0, stick='wnes', padx=px, pady=py)
add_digit_button(5).grid(row=2, column=1, stick='wnes', padx=px, pady=py)
add_digit_button(6).grid(row=2, column=2, stick='wnes', padx=px, pady=py)
add_digit_button(7).grid(row=3, column=0, stick='wnes', padx=px, pady=py)
add_digit_button(8).grid(row=3, column=1, stick='wnes', padx=px, pady=py)
add_digit_button(9).grid(row=3, column=2, stick='wnes', padx=px, pady=py)
add_digit_button(0).grid(row=4, column=0, stick='wnes', padx=px, pady=py)

add_operation_button('+').grid(row=1, column=3, stick='wnes', padx=px, pady=py) # создаем кнопки с операциями
add_operation_button('-').grid(row=2, column=3, stick='wnes', padx=px, pady=py)
add_operation_button('/').grid(row=3, column=3, stick='wnes', padx=px, pady=py)
add_operation_button('*').grid(row=4, column=3, stick='wnes', padx=px, pady=py)

add_dot_button('.').grid(row=4, column=1, stick='wnes', padx=px, pady=py)   # создаем кнопку добавления точки
add_calc_button('=').grid(row=4, column=2, stick='wnes', padx=px, pady=py)  # создаем кнопку '='

add_clean_button('C').grid(row=5, column=0, columnspan=4 ,stick='wnes', padx=px, pady=py) # создаем кнопку очистки экрана


root.grid_columnconfigure(0, minsize=60)  # задаем минимальные размеры столбцов
root.grid_columnconfigure(1, minsize=60)
root.grid_columnconfigure(2, minsize=60)
root.grid_columnconfigure(3, minsize=60)

root.grid_rowconfigure(0, minsize=60)     # задаем минимальные размены строк
root.grid_rowconfigure(1, minsize=60)
root.grid_rowconfigure(2, minsize=60)
root.grid_rowconfigure(3, minsize=60)
root.grid_rowconfigure(4, minsize=60)
root.grid_rowconfigure(5, minsize=60)

root.mainloop()                           # цикл главного окна