from tkinter import *
#from PIL import ImageTk
import sqlite3


def submit():
    conn = sqlite3.connect("daniel_app.db")
    c = conn.cursor()

    # submit
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :zipcode)",
              {
                  'f_name': f_name.get(),
                  'l_name': l_name.get(),
                  'address': address.get(),
                  'zipcode': zipcode.get(),
              })

    conn.commit()
    conn.close()

    # clear the textbox
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    zipcode.delete(0, END)


def query():
    conn = sqlite3.connect("daniel_app.db")
    c = conn.cursor()

    # query
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()

    print_records = ''
    for r in records:            # records[0] is first line from database
        print_records += str(r) + '\n'

    query_label = Label(root, text=print_records)
    query_label.grid(row=8, column=0, columnspan=2)

    conn.commit()
    conn.close()


def delete():
    conn = sqlite3.connect("daniel_app.db")
    c = conn.cursor()

    # delete
    c.execute("DELETE FROM addresses WHERE oid = " + delete_box.get())

    conn.commit()
    conn.close()


def edit():
    conn = sqlite3.connect("daniel_app.db")
    c = conn.cursor()

    # edit
    c.execute("DELETE FROM addresses WHERE oid = " + delete_box.get())

    conn.commit()
    conn.close()


root = Tk()
root.title("Daniel's APP")
root.eval("tk::PlaceWindow . center")       # place windows in the center

x = root.winfo_screenwidth() // 2           # 3: left edge starts from, 1/3 of screen width
y = int(root.winfo_screenheight() * 0.2)    # top edge starts from 20% of screen height
root.geometry('500x600+' + str(x) + '+' + str(y))


# create db
conn = sqlite3.connect("daniel_app.db")
c = conn.cursor()

# create table - run 1 time only - needs to be uncommented also when running pyinstaller
c.execute("""
    CREATE TABLE IF NOT EXISTS addresses(
    first_name text,
    last_name text,
    address text,
    zipcode integer
    )
""")

# labels
f_name_label = Label(root, text="first name")
f_name_label.grid(row=0, column=0)
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)

l_name_label = Label(root, text="last name")
l_name_label.grid(row=1, column=0)
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)

address_label = Label(root, text="address")
address_label.grid(row=2, column=0)
address = Entry(root, width=30)
address.grid(row=2, column=1, padx=20)

zipcode = Label(root, text="zipcode")
zipcode.grid(row=3, column=0)
zipcode = Entry(root, width=30)
zipcode.grid(row=3, column=1, padx=20)

delete_box = Label(root, text="delete")
delete_box.grid(row=9, column=0)
delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1, padx=20)


# buttons
submit_bt = Button(root, text="Add Record To Database", command=submit)
submit_bt.grid(row=4, column=0, columnspan=2, pady=10, padx=10)

query_bt = Button(root, text="Get Record From Database", command=query)
query_bt.grid(row=6, column=0, columnspan=2, pady=10, padx=10)

query_bt = Button(root, text="Delete", command=delete)
query_bt.grid(row=10, column=0, columnspan=2, pady=10, padx=10)


# commit changes and close connection
conn.commit()
conn.close()

# -----------------------------------------------------------------------
root.mainloop()
