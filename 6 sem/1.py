from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        value = str(feet.get())
        meters.set(eval(value))
    except ValueError:
        pass
    except NameError:
        meters.set("Неверный формат ввода")

# Создадим основное окно приложения
root = Tk()
root.title("Калькулятор")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

feet = StringVar()
feet_entry = ttk.Entry(mainframe, width=10, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="Введите выражение").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Ответ").grid(column=1, row=2, sticky=E)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

feet_entry.focus()

root.bind("<Return>", calculate)

root.mainloop()
