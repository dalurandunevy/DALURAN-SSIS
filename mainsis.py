#import libraries
from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import sqlite3
import csv


#function to define database
def Database():
    global conn, cursor
    #creating student database
    conn = sqlite3.connect("ssis.db")
    cursor = conn.cursor()
    #creating person table
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS person (No INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, ID_Number TEXT NOT NULL, Last_Name TEXT NOT NULL,First_Name TEXT NOT NULL,Course TEXT NOT NULL,Year_Level TEXT NOT NULL,Gender TEXT NOT NULL)")

#defining function for creating GUI Layout
def DisplayForm():
    #creating window
    display_screen = Tk()
    #setting width and height for window
    display_screen.geometry("1200x450")
    #setting title for window
    display_screen.title("Student Information System")
    global tree
    global SEARCH
    global DELETE
    global IDNumber,LastName,FirstName,Course,YearLevel,Gender
    SEARCH = StringVar()
    IDNumber = StringVar()
    LastName = StringVar()
    FirstName = StringVar()
    Course = StringVar()
    YearLevel = StringVar()
    Gender = StringVar()


    #creating frames for layout
    #topview frame for heading
    TopViewForm = Frame(display_screen, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)

    #first right frame for registration from
    RFrom = Frame(display_screen, width="350", bg="lightpink")
    RFrom.pack(side=RIGHT, fill=Y)

    #seconf right frame for search form
    RightViewForm = Frame(display_screen, width=425,bg="cyan")
    RightViewForm.pack(side=RIGHT, fill=Y)
    
    #mid frame for displaying students record
    MidViewForm = Frame(display_screen, width=700)
    MidViewForm.pack(side=LEFT)

    #label for heading
    lbl_text = Label(TopViewForm, text="STUDENT INFORMATION SYSTEM", font=('palatino',30), width=600,bg="lightpink",fg="Black")
    lbl_text.pack(fill=X)

    #creating registration form in first right frame
    Label(RFrom, text="ID Number  ", font=("Arial", 10),bg="yellow").pack(side=TOP)
    Entry(RFrom,font=("Arial",10,"bold"),textvariable=IDNumber).pack(side=TOP, padx=20, fill=X)
    Label(RFrom, text="Last Name ", font=("Arial", 10),bg="yellow").pack(side=TOP)
    Entry(RFrom, font=("Arial", 10, "bold"),textvariable=LastName).pack(side=TOP, padx=20, fill=X)
    Label(RFrom, text="First Name ", font=("Arial", 10),bg="yellow").pack(side=TOP)
    Entry(RFrom, font=("Arial", 10, "bold"),textvariable=FirstName).pack(side=TOP, padx=20, fill=X)
    Label(RFrom, text="Course ", font=("Arial", 10),bg="yellow").pack(side=TOP)
    Entry(RFrom, font=("Arial", 10, "bold"),textvariable=Course).pack(side=TOP, padx=20, fill=X)
    Label(RFrom, text="Year Level ", font=("Arial", 10),bg="yellow").pack(side=TOP)
    Entry(RFrom, font=("Arial", 10, "bold"),textvariable=YearLevel).pack(side=TOP, padx=20, fill=X)
    Label(RFrom, text="Gender ", font=("Arial", 10),bg="yellow").pack(side=TOP)
    Entry(RFrom, font=("Arial", 10, "bold"),textvariable=Gender).pack(side=TOP, padx=20, fill=X)
    Button(RFrom,text="ADD",font=("palatino", 10, "bold"),command=register).pack(side=TOP, padx=20,pady=10, fill=X)
    Button(RFrom,text="EXIT",font=("palatino", 10, "bold"),command=Exit).pack(side=TOP, padx=20,pady=10, fill=X)
    
    #creating search label and entry in second frame
    lbl_txtsearch = Label(RightViewForm, text="Enter ID Number to Search", font=('arial', 10),bg="yellow")
    lbl_txtsearch.pack()

    #creating search entry
    search = Entry(RightViewForm, textvariable=SEARCH, font=('palatino', 12), width=25)
    search.pack(side=TOP, padx=10, fill=X)


    #creating search button
    btn_search = Button(RightViewForm, text="SEARCH", font=("palatino", 10, "bold"), command=SearchRecord)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X,)
    #creating view button
    btn_view = Button(RightViewForm, text="VIEW ALL", font=("palatino", 10, "bold"), command=DisplayData)
    btn_view.pack(side=TOP, padx=10, pady=10, fill=X)
    #creating reset button
    btn_reset = Button(RightViewForm, text="RESET", font=("palatino", 10, "bold"), command=Reset)
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
    #creating delete button
    btn_delete = Button(RightViewForm, text="DELETE", font=("palatino", 10, "bold"), command=Delete)
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
    #creating update button
    btn_delete = Button(RightViewForm, text="UPDATE", font=("palatino", 10, "bold"), command=Update)
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
    

    #setting scrollbar
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm,columns=("No", "ID Number", "Last Name", "First Name", "Course","Year Level","Gender"),
                        selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)

    #setting headings for the columns
    tree.heading('No', text="No", anchor=W)
    tree.heading('ID Number', text="ID Number", anchor=W)
    tree.heading('Last Name', text="Last Name", anchor=W)
    tree.heading('First Name', text="First Name", anchor=W)
    tree.heading('Course', text="Course", anchor=W)
    tree.heading('Year Level', text="Year Level", anchor=W)
    tree.heading('Gender', text="Gender", anchor=W)

    #setting width of the columns
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=100)
    tree.column('#2', stretch=NO, minwidth=0, width=100)
    tree.column('#3', stretch=NO, minwidth=0, width=100)
    tree.column('#4', stretch=NO, minwidth=0, width=100)
    tree.column('#5', stretch=NO, minwidth=0, width=100)
    tree.pack()
    DisplayData()

# Opening the ssisdata.csv file
file = open('ssisdata.csv')

# Reading the contents of the
# data.csv file
contents = csv.reader(file)


#function to insert data into database 
def register():
    Database()
    #getting form data
    IDNumber1=IDNumber.get()
    LastName1=LastName.get()
    FirstName1=FirstName.get()
    Course1=Course.get()
    YearLevel1=YearLevel.get()
    Gender1=Gender.get()
    #applying empty validation
    if IDNumber.get()=='' or LastName.get()=='' or FirstName.get()=='' or Course.get()==''or YearLevel.get()==''or Gender.get()=='':
        tkMessageBox.showinfo("Warning","fill the empty field!!!")
    else:
        #execute query
        conn.execute('INSERT INTO person (ID_Number,Last_Name,First_Name,Course,Year_Level,Gender)\
              VALUES (?,?,?,?,?,?)',(IDNumber1, LastName1, FirstName1, Course1, YearLevel1, Gender1));
        conn.commit()
        tkMessageBox.showinfo("Message","Stored successfully")
        #refresh table data
        DisplayData()
        conn.close()

def Update():
    Database()
    #getting form data
    IDNumber1=IDNumber.get()
    LastName1=LastName.get()
    FirstName1=FirstName.get()
    Course1=Course.get()
    YearLevel1=YearLevel.get()
    Gender1=Gender.get()
    #applying empty validation
    if IDNumber1=='' or LastName1==''or FirstName1=='' or Course1==''or YearLevel1==''or Gender1=='':
        tkMessageBox.showinfo("Warning","fill the empty field!!!")
    else:
        #getting selected data
        curItem = tree.focus()
        contents = (tree.item(curItem))
        selecteditem = contents['values']
        #update query
        conn.execute('UPDATE person SET ID_Number=?,Last_Name=?,First_Name=?,Course=?,Year_Level=?, Gender=? WHERE No=?',(IDNumber1, LastName1, FirstName1, Course1, YearLevel1, Gender1, selecteditem[0]))
        conn.commit()
        tkMessageBox.showinfo("Message","Updated successfully")
        #reset form
        Reset()
        #refresh table data
        DisplayData()
        conn.close()

def Delete():
    #open database
    Database()
    if not tree.selection():
        tkMessageBox.showwarning("Warning","Select data to delete")
    else:
        result = tkMessageBox.askquestion('Confirm', 'Are you sure you want to delete this record?',
                                          icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents = (tree.item(curItem))
            selecteditem = contents['values']
            tree.delete(curItem)
            cursor=conn.execute("DELETE FROM person WHERE No = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()

def Reset():
    #clear current data from table
    tree.delete(*tree.get_children())
    #refresh table data
    DisplayData()
    #clear search text
    SEARCH.set("")
    IDNumber.set("")
    LastName.set("")
    FirstName.set("")
    Course.set("")
    YearLevel.set("")
    Gender.set("")

#function to search data
def SearchRecord():
    #open database
    Database()
    #checking search text is empty or not
    if SEARCH.get() != "":
        #clearing current display data
        tree.delete(*tree.get_children())
        #select query with where clause
        cursor=conn.execute("SELECT * FROM person WHERE ID_Number LIKE ?", ('%' + str(SEARCH.get()) + '%',))
        #fetch all matching records
        fetch = cursor.fetchall()
        #loop for displaying all records into GUI
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()

def DisplayData():
    #open database
    Database()
    #clear current data
    tree.delete(*tree.get_children())
    #select query
    cursor=conn.execute("SELECT * FROM person")
    #fetch all data from database
    fetch = cursor.fetchall()
    #loop for displaying all data in GUI
    for data in fetch:
        tree.insert('', 'end', values=(data))
        tree.bind("<Double-1>",OnDoubleClick)
    cursor.close()
    conn.close()

def OnDoubleClick(self):
    #getting focused from item from treeview
    curItem=tree.focus()
    contents=(tree.item(curItem))
    selecteditem=contents['values']
    #set values in the fields
    IDNumber.set(selecteditem[1])
    LastName.set(selecteditem[2])
    FirstName.set(selecteditem[3])
    Course.set(selecteditem[4])
    YearLevel.set(selecteditem[5])
    Gender.set(selecteditem[6])

def Exit():
    result = tkMessageBox.askquestion('Student Information System', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        exit()

#calling function
DisplayForm()
if __name__=='__main__':
    
#Running Application
 mainloop()