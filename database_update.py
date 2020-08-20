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
    #loop thru results
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
    #delete
    c.execute("DELETE from address WHERE oid="+ delete_box.get())
    # commit changes
    conn.commit()
    # close connection
    conn.close()


def save():
    # create a database
    conn = sqlite3.connect('address_book.db')
    # create cursor
    c = conn.cursor()
    # save this update code
    record_id=delete_box.get()
    c.execute("""UPDATE address SET 
                  f_name = :first,
                  l_name = :last,
                  address = :address,
                  city = :city,
                  state = :state,
                  zip = :zip

                  WHERE oid = :oid""",
              {
                  "first": f_name_editor.get(),
                  "last": l_name_editor.get(),
                  "address": address_editor.get(),
                  "city": city_editor.get(),
                  "state": state_editor.get(),
                  "zip": zip_editor.get(),

                  "oid": record_id

              })
    # commit changes
    conn.commit()
    # close connection
    conn.close()
    #to disapper the 2nd window
    editor.destroy()

def update():
    global editor
    editor = Tk()
    editor.title("update your database record")
    editor.geometry("400x400")
    # create a database connection
    conn = sqlite3.connect('address_book.db')
    # create cursor
    c = conn.cursor()

    # update code
    c.execute("SELECT* FROM address WHERE oid=" + delete_box.get())
    records=c.fetchall()

    #global all the variabale, as we r using this into other fuction
    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zip_editor

    # create update window text boxes
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1)
    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1)
    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1)
    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1)
    zip_editor = Entry(editor, width=30)
    zip_editor.grid(row=5, column=1)

    # create text box labels/heading
    f_name_lbl = Label(editor, text="FIRST NAME")
    f_name_lbl.grid(row=0, column=0, pady=(10, 0))
    l_name_lbl = Label(editor, text="LAST NAME")
    l_name_lbl.grid(row=1, column=0)
    address_lbl = Label(editor, text="ADDRESS")
    address_lbl.grid(row=2, column=0)
    city_lbl = Label(editor, text="CITY")
    city_lbl.grid(row=3, column=0)
    state_lbl = Label(editor, text="STATE")
    state_lbl.grid(row=4, column=0)
    zip_lbl = Label(editor, text="ZIP-CODE")
    zip_lbl.grid(row=5, column=0)

    #loop thru the results and put all d results into d new window
    for record in records:
        f_name_editor.insert(0,record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zip_editor.insert(0, record[5])

    #create save button
    update_btn = Button(editor, text="save updated record", command=save)
    update_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=134)

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

#create update button
update_btn=Button(root, text="update record", command=update)
update_btn.grid(row=11,column=0,columnspan=2,pady=10,padx=10,ipadx=134)


root.mainloop()