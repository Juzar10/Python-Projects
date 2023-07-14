from tkinter import*
cal = Tk()
cal.title("KALKULATOR")
MyMojo = Label(cal, text="KALKULATOR", font=("Times New Roman",
               20, 'bold')).grid(column=0, row=0, columnspan=4)
e = Entry(cal, width=35, borderwidth=5)
e.grid(column=0, row=1, columnspan=43)


def input_number(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current)+str(number))


def clear():
    e.delete(0, END)


def add():
    first_number = e.get()
    e.delete(0, END)
    global f_num
    global math
    math = "add"
    f_num = float(first_number)


def substract():
    first_number = e.get()
    e.delete(0, END)
    global f_num
    global math
    math = "substract"
    f_num = float(first_number)


def multiply():
    first_number = e.get()
    e.delete(0, END)
    global f_num
    global math
    math = "multiply"
    f_num = float(first_number)


def devide():
    first_number = e.get()
    e.delete(0, END)
    global f_num
    global math
    math = "devide"
    f_num = float(first_number)


def equal():
    second_number = e.get()
    e.delete(0, END)
    if math == "add":
        e.insert(0, f_num+float(second_number))
    if math == "substract":
        e.insert(0, f_num-float(second_number))
    if math == "multiply":
        e.insert(0, f_num*float(second_number))
    if math == "devide":
        e.insert(0, f_num/float(second_number))


button_1 = Button(cal, text="1", padx=30, pady=20, fg='black', bg='white', font=(
    "Times New Roman", 20, "bold"), command=lambda: input_number(1)).grid(row=4, column=0)
button_2 = Button(cal, text="2", padx=30, pady=20, bg='white', fg='black', font=(
    "Times New Roman", 20, "bold"), command=lambda: input_number(2)).grid(row=4, column=1)
button_3 = Button(cal, text="3", padx=30, pady=20, bg='white', fg='black', font=(
    "Times New Roman", 20, "bold"), command=lambda: input_number(3)).grid(row=4, column=2)

button_4 = Button(cal, text="4", padx=30, pady=20, bg='white', fg='black', font=(
    "Times New Roman", 20, "bold"), command=lambda: input_number(4)).grid(row=3, column=0)
button_5 = Button(cal, text="5", padx=30, pady=20, bg='white', fg='black', font=(
    "Times New Roman", 20, "bold"), command=lambda: input_number(5)).grid(row=3, column=1)
button_6 = Button(cal, text="6", padx=30, pady=20, bg='white', fg='black', font=(
    "Times New Roman", 20, "bold"), command=lambda: input_number(6)).grid(row=3, column=2)

button_7 = Button(cal, text="7", padx=30, pady=20, bg='white', fg='black', font=(
    "Times New Roman", 20, "bold"), command=lambda: input_number(7)).grid(row=2, column=0)
button_8 = Button(cal, text="8", padx=30, pady=20, bg='white', fg='black', font=(
    "Times New Roman", 20, "bold"), command=lambda: input_number(8)).grid(row=2, column=1)
button_9 = Button(cal, text="9", padx=30, pady=20, bg='white', fg='black', font=(
    "Times New Roman", 20, "bold"), command=lambda: input_number(9)).grid(row=2, column=2)

button_0 = Button(cal, text="0", padx=30, pady=20, bg='white', fg='black', font=(
    "Times New Roman", 20, "bold"), command=lambda: input_number(0)).grid(row=5, column=1)

button_clear = Button(cal, text="Clear", padx=5, pady=20, bg='green', fg='black', font=(
    "Times New Roman", 20, "bold"), command=clear).grid(row=5, column=0)
button_equal = Button(cal, text="=", padx=30, pady=20, bg='green', fg='black', font=(
    "Times New Roman", 20, "bold"), command=equal).grid(row=5, column=2)

button_add = Button(cal, text="+", padx=26, pady=20, bg='red', fg='black',
                    font=("Times New Roman", 20, "bold"), command=add).grid(row=5, column=3)
button_substract = Button(cal, text="-", padx=29, pady=20, bg='red', fg='black',
                          font=("Times New Roman", 20, "bold"), command=substract).grid(row=4, column=3)
button_multiply = Button(cal, text="*", padx=26, pady=20, bg='red', fg='black',
                         font=("Times New Roman", 20, "bold"), command=multiply).grid(row=3, column=3)
button_devide = Button(cal, text="/", padx=29, pady=20, bg='red', fg='black',
                       font=("Times New Roman", 20, "bold"), command=devide).grid(row=2, column=3)


cal.mainloop()
