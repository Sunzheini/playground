from tkinter import *

# General
window = Tk()               # instantiate an instance of a window
window.geometry("600x600")  # size
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
    image=photo2,
    compound='bottom',      # image appears underneath the text
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
# Check Buttons - 34:07





# -------------------------------------------------------------

window.mainloop()           # display window, listen for events
