from tkinter import *
import sqlite3
root=Tk()
root.geometry("400x500")
#############to create table#################
#c.execute(""" CREATE TABLE address(
 #   first_name text,
#  last_name text,
 #   address text,
  #  city text,
# state text,
 #   zipcode integer)
  #  """)

#create submit fun
def submit():
    # create a database
    conn = sqlite3.connect('address_book.db')
    # create cursor
    c = conn.cursor()
    #insert into table
    c.execute("INSERT INTO address VALUES (:f_name,:l_name,:address,:city,:state,:zip)",
    {
        'f_name':f_name.get(),
        'l_name':l_name.get(),
        'address':address.get(),
        'city':city.get(),
        'state':state.get(),
        'zip':zip.get(),
    } )
    # commit changes
    conn.commit()
    # close connection
    conn.close()
    #clear text box
    f_name.delete(0,END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zip.delete(0, END)

def query():
    # create a database
    conn = sqlite3.connect('address_book.db')
    # create cursor
    c = conn.cursor()

    #query to d database
    c.execute("SELECT *, oid FROM address")
    records=c.fetchall()
    print(records)
    #loop inside the database
    print_records=''
    for record in records:
        print_records += str(record[0]) + " " + str(record[1])+ "\t\t"+str(record[6]) +"\n"
    query_lbl=Label(root,text=print_records)
    query_lbl.grid(row=12, column=0,columnspan=2)
    # commit changes
    conn.commit()
    # close connection
    conn.close()

def delete():
    # create a database
    conn = sqlite3.connect('address_book.db')
    # create cursor
    c = conn.cursor()
    #delete code
    c.execute("DELETE from address WHERE oid="+ delete_box.get())
    # commit changes
    conn.commit()
    # close connection
    conn.close()

#create text boxes
f_name=Entry(root, width=30)
f_name.grid(row=0,column=1,padx=20,pady=(10,0))
l_name=Entry(root, width=30)
l_name.grid(row=1,column=1)
address=Entry(root, width=30)
address.grid(row=2,column=1)
city=Entry(root, width=30)
city.grid(row=3,column=1)
state=Entry(root, width=30)
state.grid(row=4,column=1)
zip=Entry(root, width=30)
zip.grid(row=5,column=1)

delete_box=Entry(root, width=30)
delete_box.grid(row=9,column=1,pady=5)

#create text box labels/heading
f_name_lbl=Label(root, text="FIRST NAME")
f_name_lbl.grid(row=0,column=0,pady=(10,0))
l_name_lbl=Label(root, text="LAST NAME")
l_name_lbl.grid(row=1,column=0)
address_lbl=Label(root, text="ADDRESS")
address_lbl.grid(row=2,column=0)
city_lbl=Label(root, text="CITY")
city_lbl.grid(row=3,column=0)
state_lbl=Label(root, text="STATE")
state_lbl.grid(row=4,column=0)
zip_lbl=Label(root, text="ZIP-CODE")
zip_lbl.grid(row=5,column=0)

delete_box_lbl=Label(root, text="Selete ID")
delete_box_lbl.grid(row=9,column=0,pady=5)

#create submit buttton
submit_btn=Button(root, text="add to the record", command=submit)
submit_btn.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=100)

#create query button
querry_btn=Button(root, text="show records", command=query)
querry_btn.grid(row=7,column=0,columnspan=2,pady=10,padx=10,ipadx=137)

#create delete button
delete_btn=Button(root, text="delete record", command=delete)
delete_btn.grid(row=10,column=0,columnspan=2,pady=10,padx=10,ipadx=137)

root.mainloop()