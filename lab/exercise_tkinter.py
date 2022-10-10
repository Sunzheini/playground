from tkinter import *
from tkinter import messagebox
from tkinter import colorchooser
from tkinter import filedialog
from tkinter import ttk


# General
window = Tk()               # instantiate an instance of a window
window.geometry("700x700")  # size
window.title("Maxi is supermen")   # title of window

icon = PhotoImage(file='../staticfiles/download.png')   # convert image
window.iconphoto(True, icon)    # change icon image

window.config(background='#2b2828')     # window background


# -------------------------------------------------------------
# Labels
photo = PhotoImage(file='../staticfiles/download.png')  # for the label
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
    image=photo,
    compound='bottom',   # image appears underneath the text
)
label.pack()    # puts @ top center
# label.place(x=0, y=0)   # top left coordinates in pixels (1px = 0.26mm)


# -------------------------------------------------------------
# Buttons
def click():
    print('You clicked!')


photo2 = PhotoImage(file='../staticfiles/download.png')  # for the button
button = Button(
    window,     # container of button
    text='lololol',
    command=click,      # function
    font=("Comic Sans", 15),
    fg='#00FF00',
    bg='black',
    activeforeground='#00FF00',   # stays the same as fg when not clicked
    activebackground='black',    # when clicked
    # state=DISABLED,      # can no longer click on the button
    #image=photo2,
    #compound='bottom',      # image appears underneath the text
)
button.pack()


# -------------------------------------------------------------
# Entry Widget + Submit Button + Delete Button + Backspace Button
def submit():
    my_string = entry.get()     # get string from input
    print(my_string)
    entry.config(state=DISABLED)    # disable after submitting


def delete():
    entry.delete(0, END)    # delete character from 0 to last


def backspace():
    entry.delete(len(entry.get())-1, END)  # second-to-last char, last char


entry = Entry(
    window,
    font=("Arial", 25),
    fg='#00FF00',
    bg='black',
    # show='*',       # for passwords: show symbols when typing
)
entry.insert(
    0,                  # from th beginning position
    'default text',     # default text
)
entry.pack(side=LEFT)       # packs not from top but from left

submit_button = Button(
    window,
    text='Submit',
    command=submit,
)
submit_button.pack(side=RIGHT)

delete_button = Button(
    window,
    text='Delete',
    command=delete,
)
delete_button.pack(side=LEFT)

backspace_button = Button(
    window,
    text='Backspace',
    command=backspace,
)
backspace_button.pack(side=LEFT)


# -------------------------------------------------------------
# Check Buttons

def display():
    if x.get() == 1:
        print("Agreed")


x = IntVar()     # datatype should reflect what is stored in the variable (BooleanVar, StringVar, etc.)

check_button = Checkbutton(
    window,
    text='I am supermen',
    variable=x,
    onvalue=1,      # by default returns 0 or 1
    offvalue=0,
    command=display,
)

check_button.pack()

# -------------------------------------------------------------
# Radio Buttons


def order():
    if x.get() == 0:
        print('pizza')


food = ['pizza', 'hamburger', 'hotdog']
x = IntVar()

for i in range(len(food)):
    radiobutton = Radiobutton(
        window,
        text=food[i],
        variable=x,             # groups together if they share the same variable
        value=i,                # assigns each button a different value
        # indicatoron=False,      # eliminate circle buttons
        command=order,
    )
    radiobutton.pack(anchor='w')    # aligns to west

# -------------------------------------------------------------
# Sliding Scale

scale = Scale(
    window,
    from_=0,
    to=100,
    length=100,
    orient=VERTICAL,
    tickinterval=5,     # numeric indicators on the scale
    # showvalue=False,    # hides current value
    troughcolor='#69EAFF',
)

scale.set(50)       # sets current value

scale.pack()

# -------------------------------------------------------------
# List Box


def submit():
    foodz = []

    for j in listbox.curselection():
        foodz.insert(j, listbox.get(j))

    print(*foodz, end='')


def add():
    listbox.insert(listbox.size(),      # gives us current position on the item we are on
                   entryBox.get()       # insert a new item
                   )
    # listbox.delete(listbox.curselection())      # deletes
    listbox.config(height=listbox.size())


listbox = Listbox(
    window,
    bg='#f7ffde',
    selectmode=MULTIPLE,    # can select multiple items
)

listbox.pack()
listbox.insert(1, 'pizza')      # items inside the listbox
listbox.insert(2, 'hamburger')
listbox.insert(3, 'doner')

listbox.config(height=listbox.size())        # change height of listbox depending on items

entryBox = Entry(window)
entryBox.pack()

submit1Button = Button(window, text='submit', command=submit)
submit1Button.pack()

add1Button = Button(window, text='add', command=add)
add1Button.pack()

# -------------------------------------------------------------
# Message Box


def somemessage():
    # messagebox.showinfo(title='info_message', message='Daniel is Noob!!!')    # normal box

    # messagebox.showwarning(title='info_message', message='Daniel is Noob!!!')    # warning box
    # you can put while 1 for infinite

    # messagebox.showerror(title='info_message', message='Daniel is Noob!!!')  # error box

    # if messagebox.askokcancel(title='info_message', message='Daniel is Noob!!!'):   # choice
    #     print('yes')
    # else:
    #     print('no')

    answer = messagebox.askquestion(title='info_message', message='Daniel is Noob!!!', icon='warning')
    if answer == 'yes':
        print('ffff')


button_m_b = Button(window, text='messagebox', command=somemessage)
button_m_b.pack()

# -------------------------------------------------------------
# Color Picker


def colorchooser():
    color = colorchooser.askcolor()
    print(color)            # prints ((118, 152, 203), '#7698cb')


buttoncolor = Button(window, text='colorpicker', command=colorchooser)
buttoncolor.place(x=100, y=300)

# -------------------------------------------------------------
# Text Area


def sumbittext():
    input = text_widget.get('1.0', END)     # get the text
    print(input)


text_widget = Text(window, height=3, width=6)
text_widget.place(x=100, y=400)
textbutton = Button(window, command=sumbittext)
textbutton.place(x=100, y=350)

# -------------------------------------------------------------
# Opening Files
def openfile():
    filepath = filedialog.askopenfilename()     # opens explorer for the file, saving it in 'filepath'
    # filepath = filedialog.asksaveasfile()     # can also save files


filebutton = Button(window, text='openfile', command=openfile)
filebutton.place(x=150, y=350)

# -------------------------------------------------------------
# Menu Bar      # like the one on the programs


def openFile():
    print('openFile')


def saveFile():
    print('saveFile')


menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar, tearoff=False)
menubar.add_cascade(label='File', menu=fileMenu)       # dropdown menu
fileMenu.add_command(label='Open', command=openFile)
fileMenu.add_command(label='Save', command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label='Exit', command=quit)

editMenu = Menu(menubar, tearoff=False)
menubar.add_cascade(label='Edit', menu=fileMenu)

# -------------------------------------------------------------
# Frame     # a rectangular container to group and hold widgets

frame1 = Frame(window, bg='pink', bd=5, relief=RAISED)
frame1.place(x=250, y=350)

buttondzw = Button(frame1, text='w')
buttondza = Button(frame1, text='a')
buttondzs = Button(frame1, text='s')
buttondzd = Button(frame1, text='d')

buttondzw.pack(side=TOP)
buttondza.pack(side=LEFT)
buttondzs.pack(side=LEFT)
buttondzd.pack(side=LEFT)

# -------------------------------------------------------------
# New Windows


def createwindow():
    new_window = Toplevel()     # new window on top of other windows, linked to a botton window

    # new_window = Tk()       # independent window
    # window.destroy()        # close the old window


Button(window, text='create', command=createwindow).place(x=350, y=350)

# -------------------------------------------------------------
# Separate Tabs

notebook = ttk.Notebook(window)     # manages a collection of windows and displays
tab1 = Frame(notebook)      # new frame for tab1
tab2 = Frame(notebook)

notebook.add(tab1, text='tab 1')
notebook.add(tab2, text='tab 2')
notebook.place(x=50, y=50)

Label(tab1, text='Hello tab1').pack()
Label(tab2, text='Hello tab2').pack()

# -------------------------------------------------------------
# Grid Geometry Manager - 2:27:00










# -------------------------------------------------------------

window.mainloop()           # display window, listen for events
