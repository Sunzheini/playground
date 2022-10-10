from tkinter import *
from tkinter import messagebox
from tkinter import colorchooser
from tkinter import filedialog
from tkinter import ttk
import time


# # General
# window = Tk()               # instantiate an instance of a window
# window.geometry("700x700")  # size
# window.title("Maxi is supermen")   # title of window
#
# icon = PhotoImage(file='../staticfiles/download.png')   # convert image
# window.iconphoto(True, icon)    # change icon image
#
# window.config(background='#2b2828')     # window background
#
#
# # -------------------------------------------------------------
# # Labels
# photo = PhotoImage(file='../staticfiles/download.png')  # for the label
# label = Label(
#     window,         # container of label
#     text='Hi,Maimuna',
#     font=('Arial', 20, 'bold'),
#     fg='#00FF00',      # font color
#     bg='black',
#     relief=RAISED,      # border style
#     bd=10,      # border width
#     padx=20,    # width of space between the text and the border
#     pady=20,    # height of space between the text and the border
#     image=photo,
#     compound='bottom',   # image appears underneath the text
# )
# label.pack()    # puts @ top center
# # label.place(x=0, y=0)   # top left coordinates in pixels (1px = 0.26mm)
#
#
# # -------------------------------------------------------------
# # Buttons
# def click():
#     print('You clicked!')
#
#
# photo2 = PhotoImage(file='../staticfiles/download.png')  # for the button
# button = Button(
#     window,     # container of button
#     text='lololol',
#     command=click,      # function
#     font=("Comic Sans", 15),
#     fg='#00FF00',
#     bg='black',
#     activeforeground='#00FF00',   # stays the same as fg when not clicked
#     activebackground='black',    # when clicked
#     # state=DISABLED,      # can no longer click on the button
#     #image=photo2,
#     #compound='bottom',      # image appears underneath the text
# )
# button.pack()
#
#
# # -------------------------------------------------------------
# # Entry Widget + Submit Button + Delete Button + Backspace Button
# def submit():
#     my_string = entry.get()     # get string from input
#     print(my_string)
#     entry.config(state=DISABLED)    # disable after submitting
#
#
# def delete():
#     entry.delete(0, END)    # delete character from 0 to last
#
#
# def backspace():
#     entry.delete(len(entry.get())-1, END)  # second-to-last char, last char
#
#
# entry = Entry(
#     window,
#     font=("Arial", 25),
#     fg='#00FF00',
#     bg='black',
#     # show='*',       # for passwords: show symbols when typing
# )
# entry.insert(
#     0,                  # from th beginning position
#     'default text',     # default text
# )
# entry.pack(side=LEFT)       # packs not from top but from left
#
# submit_button = Button(
#     window,
#     text='Submit',
#     command=submit,
# )
# submit_button.pack(side=RIGHT)
#
# delete_button = Button(
#     window,
#     text='Delete',
#     command=delete,
# )
# delete_button.pack(side=LEFT)
#
# backspace_button = Button(
#     window,
#     text='Backspace',
#     command=backspace,
# )
# backspace_button.pack(side=LEFT)
#
#
# # -------------------------------------------------------------
# # Check Buttons
#
# def display():
#     if x.get() == 1:
#         print("Agreed")
#
#
# x = IntVar()     # datatype should reflect what is stored in the variable (BooleanVar, StringVar, etc.)
#
# check_button = Checkbutton(
#     window,
#     text='I am supermen',
#     variable=x,
#     onvalue=1,      # by default returns 0 or 1
#     offvalue=0,
#     command=display,
# )
#
# check_button.pack()
#
# # -------------------------------------------------------------
# # Radio Buttons
#
#
# def order():
#     if x.get() == 0:
#         print('pizza')
#
#
# food = ['pizza', 'hamburger', 'hotdog']
# x = IntVar()
#
# for i in range(len(food)):
#     radiobutton = Radiobutton(
#         window,
#         text=food[i],
#         variable=x,             # groups together if they share the same variable
#         value=i,                # assigns each button a different value
#         # indicatoron=False,      # eliminate circle buttons
#         command=order,
#     )
#     radiobutton.pack(anchor='w')    # aligns to west
#
# # -------------------------------------------------------------
# # Sliding Scale
#
# scale = Scale(
#     window,
#     from_=0,
#     to=100,
#     length=100,
#     orient=VERTICAL,
#     tickinterval=5,     # numeric indicators on the scale
#     # showvalue=False,    # hides current value
#     troughcolor='#69EAFF',
# )
#
# scale.set(50)       # sets current value
#
# scale.pack()
#
# # -------------------------------------------------------------
# # List Box
#
#
# def submit():
#     foodz = []
#
#     for j in listbox.curselection():
#         foodz.insert(j, listbox.get(j))
#
#     print(*foodz, end='')
#
#
# def add():
#     listbox.insert(listbox.size(),      # gives us current position on the item we are on
#                    entryBox.get()       # insert a new item
#                    )
#     # listbox.delete(listbox.curselection())      # deletes
#     listbox.config(height=listbox.size())
#
#
# listbox = Listbox(
#     window,
#     bg='#f7ffde',
#     selectmode=MULTIPLE,    # can select multiple items
# )
#
# listbox.pack()
# listbox.insert(1, 'pizza')      # items inside the listbox
# listbox.insert(2, 'hamburger')
# listbox.insert(3, 'doner')
#
# listbox.config(height=listbox.size())        # change height of listbox depending on items
#
# entryBox = Entry(window)
# entryBox.pack()
#
# submit1Button = Button(window, text='submit', command=submit)
# submit1Button.pack()
#
# add1Button = Button(window, text='add', command=add)
# add1Button.pack()
#
# # -------------------------------------------------------------
# # Message Box
#
#
# def somemessage():
#     # messagebox.showinfo(title='info_message', message='Daniel is Noob!!!')    # normal box
#
#     # messagebox.showwarning(title='info_message', message='Daniel is Noob!!!')    # warning box
#     # you can put while 1 for infinite
#
#     # messagebox.showerror(title='info_message', message='Daniel is Noob!!!')  # error box
#
#     # if messagebox.askokcancel(title='info_message', message='Daniel is Noob!!!'):   # choice
#     #     print('yes')
#     # else:
#     #     print('no')
#
#     answer = messagebox.askquestion(title='info_message', message='Daniel is Noob!!!', icon='warning')
#     if answer == 'yes':
#         print('ffff')
#
#
# button_m_b = Button(window, text='messagebox', command=somemessage)
# button_m_b.pack()
#
# # -------------------------------------------------------------
# # Color Picker
#
#
# def colorchooser():
#     color = colorchooser.askcolor()
#     print(color)            # prints ((118, 152, 203), '#7698cb')
#
#
# buttoncolor = Button(window, text='colorpicker', command=colorchooser)
# buttoncolor.place(x=100, y=300)
#
# # -------------------------------------------------------------
# # Text Area
#
#
# def sumbittext():
#     input = text_widget.get('1.0', END)     # get the text
#     print(input)
#
#
# text_widget = Text(window, height=3, width=6)
# text_widget.place(x=100, y=400)
# textbutton = Button(window, command=sumbittext)
# textbutton.place(x=100, y=350)
#
# # -------------------------------------------------------------
# # Opening Files
# def openfile():
#     filepath = filedialog.askopenfilename()     # opens explorer for the file, saving it in 'filepath'
#     # filepath = filedialog.asksaveasfile()     # can also save files
#
#
# filebutton = Button(window, text='openfile', command=openfile)
# filebutton.place(x=150, y=350)
#
# # -------------------------------------------------------------
# # Menu Bar      # like the one on the programs
#
#
# def openFile():
#     print('openFile')
#
#
# def saveFile():
#     print('saveFile')
#
#
# menubar = Menu(window)
# window.config(menu=menubar)
#
# fileMenu = Menu(menubar, tearoff=False)
# menubar.add_cascade(label='File', menu=fileMenu)       # dropdown menu
# fileMenu.add_command(label='Open', command=openFile)
# fileMenu.add_command(label='Save', command=saveFile)
# fileMenu.add_separator()
# fileMenu.add_command(label='Exit', command=quit)
#
# editMenu = Menu(menubar, tearoff=False)
# menubar.add_cascade(label='Edit', menu=fileMenu)
#
# # -------------------------------------------------------------
# # Frame     # a rectangular container to group and hold widgets
#
# frame1 = Frame(window, bg='pink', bd=5, relief=RAISED)
# frame1.place(x=250, y=350)
#
# buttondzw = Button(frame1, text='w')
# buttondza = Button(frame1, text='a')
# buttondzs = Button(frame1, text='s')
# buttondzd = Button(frame1, text='d')
#
# buttondzw.pack(side=TOP)
# buttondza.pack(side=LEFT)
# buttondzs.pack(side=LEFT)
# buttondzd.pack(side=LEFT)
#
# # -------------------------------------------------------------
# # New Windows
#
#
# def createwindow():
#     new_window = Toplevel()     # new window on top of other windows, linked to a botton window
#
#     # new_window = Tk()       # independent window
#     # window.destroy()        # close the old window
#
#
# Button(window, text='create', command=createwindow).place(x=350, y=350)
#
# # -------------------------------------------------------------
# # Separate Tabs
#
# notebook = ttk.Notebook(window)     # manages a collection of windows and displays
# tab1 = Frame(notebook)      # new frame for tab1
# tab2 = Frame(notebook)
#
# notebook.add(tab1, text='tab 1')
# notebook.add(tab2, text='tab 2')
# notebook.place(x=50, y=50)
#
# Label(tab1, text='Hello tab1').pack()
# Label(tab2, text='Hello tab2').pack()

# -------------------------------------------------------------
# -------------------------------------------------------------
# Grid Geometry Manager (on separate window)
# window2 = Tk()
#
# titleNLabel = Label(window2, text="title label").grid(row=0, column=0, columnspan=2)
#
# firstNLabel = Label(window2, text="fn label").grid(row=1, column=0)
# firstNEntry = Entry(window2).grid(row=1, column=1)
#
# lastNLabel = Label(window2, text="fn label").grid(row=2, column=0)
# lastNEntry = Entry(window2).grid(row=2, column=1)
#
# commonNLabel = Label(window2, text="c label").grid(row=3, column=0, columnspan=2)   # takes 2 columns

# -------------------------------------------------------------
# -------------------------------------------------------------
# Progress Bar
# window3 = Tk()
#
# def download():
#     tasks = 10
#     x = 0
#     while x < tasks:
#         time.sleep(0.2)
#         prbar['value'] += 10
#         x += 1
#         percent.set(str(x/tasks*100) + '%')
#         window3.update_idletasks()      # update after each iteration
#
#
# percent = StringVar()
#
# prbar = ttk.Progressbar(window3, orient=VERTICAL)
# prbar.pack(pady=10)
# percentLabel = Label(window3, textvariable=percent).pack()
# progressButton = Button(window3, text='download', command=download).pack()
#
# # -------------------------------------------------------------
# # Canvas - draw graphs, plots, images
#
# canvas = Canvas(window3, height=200, width=200)
# canvas.create_line(0, 0, 200, 200, width=3)      # start and end
# canvas.create_rectangle(50, 50, 100, 100)
# canvas.pack()
#
# # -------------------------------------------------------------
# # Key Events
#
# def do_something(event):
#     print("pressed " + event.keysym)     # display what button is pressed
#     labelkey.config(text=event.keysym)   # display on window
#
#
# window3.bind("<Key>", do_something)       # event (i.e. press w), function
# labelkey = Label(window3)
# labelkey.pack()
#
# # -------------------------------------------------------------
# # Mouse Events
#
# def mouse_something(event):
#     print("pressed " + str(event.x) + ' ' + str(event.y))
#     labelkey.config(text=event.x)
#
#
# window3.bind("<Button-1>", mouse_something)   # Button-1, Button-2 (scrollwheel press), Button-3 (right)
#                                               # Enter - when mouse enters widget area
#                                               # Motion - where the mouse moved (for games!)
# # -------------------------------------------------------------
# # Drag and Drop
#
#
# def drag_start(event):
#     ddlabel.startX = event.x        # where we clicked within the label
#     ddlabel.startY = event.y
#
#
# def drag_motion(event):
#     x = ddlabel.winfo_x() - ddlabel.startX + event.x
#     y = ddlabel.winfo_y() - ddlabel.startY + event.y
#     ddlabel.place(x=x, y=y)
#
# # get coords of our label relative to the window that we are in
#
#
# ddlabel = Label(window3, bg='red', width=10, height=5)
# ddlabel.place(x=130, y=100)
#
# ddlabel.bind('<Button-1>', drag_start)
# ddlabel.bind('<B1-Motion>', drag_motion)

# -------------------------------------------------------------
# -------------------------------------------------------------
# Animations

WIDTH = 500
HEIGHT = 500

xVelocity = 3
yVelocity = 2

window4 = Tk()

canvas = Canvas(window4, width=WIDTH, height=HEIGHT)
canvas.pack()

bg_image = PhotoImage(file='../staticfiles/desert.png')
background = canvas.create_image(0, 0, image=bg_image, anchor=NW)

photo_image = PhotoImage(file='../staticfiles/cactus.png')
my_image = canvas.create_image(0, 0, image=photo_image, anchor=NW)

image_width = photo_image.width()
image_height = photo_image.height()

while True:
    coordinates = canvas.coords(my_image)       # get coordinates
    print(coordinates)

    if coordinates[0] >= (WIDTH - image_width) or coordinates[0] < 0:
        xVelocity = -xVelocity
    canvas.move(my_image, xVelocity, 0)     # move with destination velocity

    if coordinates[1] >= (HEIGHT - image_height) or coordinates[1] < 0:
        yVelocity = -yVelocity
    canvas.move(my_image, xVelocity, yVelocity)

    window4.update()
    time.sleep(0.01)



# -------------------------------------------------------------

# window.mainloop()           # display window, listen for events
# window2.mainloop()
# window3.mainloop()
window4.mainloop()










