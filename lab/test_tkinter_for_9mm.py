from tkinter import *
import threading


class PlayingField:
    FIELD_SIZE = 7
    F_SYMBOL = 'O'
    H_SEP = '-'
    V_SEP = '|'

    def __init__(self):
        self.matrix = []

# 2 - valid / invalid fields marking
    def create_field(self):
        self.matrix.append([self.F_SYMBOL, self.H_SEP, self.H_SEP, self.F_SYMBOL, self.H_SEP, self.H_SEP, self.F_SYMBOL])
        self.matrix.append([self.V_SEP, self.F_SYMBOL, self.H_SEP, self.F_SYMBOL, self.H_SEP, self.F_SYMBOL, self.V_SEP])
        self.matrix.append([self.V_SEP, self.V_SEP, self.F_SYMBOL, self.F_SYMBOL, self.F_SYMBOL, self.V_SEP, self.V_SEP])
        self.matrix.append([self.F_SYMBOL, self.F_SYMBOL, self.F_SYMBOL, ' ', self.F_SYMBOL, self.F_SYMBOL, self.F_SYMBOL])
        self.matrix.append([self.V_SEP, self.V_SEP, self.F_SYMBOL, self.F_SYMBOL, self.F_SYMBOL, self.V_SEP, self.V_SEP])
        self.matrix.append([self.V_SEP, self.F_SYMBOL, self.H_SEP, self.F_SYMBOL, self.H_SEP, self.F_SYMBOL, self.V_SEP])
        self.matrix.append([self.F_SYMBOL, self.H_SEP, self.H_SEP, self.F_SYMBOL, self.H_SEP, self.H_SEP, self.F_SYMBOL])

        print(f"--(Admin) Playing field {self.FIELD_SIZE}x{self.FIELD_SIZE} created--\n")

    def display_field(self):
        for i in range(len(self.matrix)):
            print(' '.join(self.matrix[i]))
        print()


def change1():
    if field.matrix[0][0] == 'O':
        field.matrix[0][0] = 'F'
    else:
        field.matrix[0][0] = 'O'
    field.display_field()
    print('changed!')


def change2():
    if field.matrix[0][3] == 'O':
        field.matrix[0][3] = 'F'
    else:
        field.matrix[0][3] = 'O'
    field.display_field()
    print('changed!')


def mid1():
    th = threading.Thread(target=change1)
    th.start()


def mid2():
    th = threading.Thread(target=change2)
    th.start()


field = PlayingField()
field.create_field()
field.display_field()


# General
window = Tk()               # instantiate an instance of a window
window.geometry("400x400")  # size
window.title("9 Men Morris")   # title of window

icon = PhotoImage(file='../staticfiles/download.png')   # convert image
window.iconphoto(True, icon)    # change icon image

window.config(background='#2b2828')     # window background

button1 = Button(
    window,     # container of button
    text='1',
    command=mid1,
    font=("Arial", 15),
    fg='#00FF00',
    bg='black',
    activeforeground='#00FF00',   # stays the same as fg when not clicked
    activebackground='grey',    # when clicked
)

button1.place(x=50, y=50)   # top left coordinates in pixels (1px = 0.26mm)


button2 = Button(
    window,     # container of button
    text='2',
    command=mid2,      # function
    font=("Arial", 15),
    fg='#00FF00',
    bg='black',
    activeforeground='#00FF00',   # stays the same as fg when not clicked
    activebackground='grey',    # when clicked
)

button2.place(x=110, y=50)   # top left coordinates in pixels (1px = 0.26mm)


label = Label(
    window,         # container of label
    text='Hi,Maimuna',
    font=('Arial', 20, 'bold'),
    fg='#00FF00',      # font color
    bg='black',
    relief=RAISED,      # border style
    bd=10,      # border width
    padx=20,    # width of space between the text and the border
    pady=20,    # height of space between the text and the border
)
label.place(x=110, y=250)


window.mainloop()           # display window, listen for events
