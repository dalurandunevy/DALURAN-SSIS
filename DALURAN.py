# Import Libraries
# Author: Dunevy Daluran
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import tkinter.ttk as ttk
import csv
import os

# Define Variables
class Student:
    
    def __init__ (self,root):
        self.root = root
        blank_space = ""
        self.root.title(200 * blank_space + "Student Information System")
        self.root.geometry("1350x575+0+0")
        self.root.resizable(False,False)
        self.data = dict()
        self.temp = dict()
        self.filename = "data.csv"
        
        Student_First_Name = StringVar()
        Student_Last_Name = StringVar()
        Student_IDNumber = StringVar()
        Student_YearLevel = StringVar()
        Student_Gender = StringVar()
        Student_Course = StringVar()
        searchbar = StringVar()
        
        if not os.path.exists('data.csv'):
            with open('data.csv', mode='w') as csv_file:
                fieldnames = ["Student ID Number", "Last Name", "First Name", "Gender", "Year Level", "Course"]
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
        
        else:
            with open('data.csv', newline='') as csv_file:
                reader = csv.DictReader(csv_file)
                for row in reader:
                    self.data[row["Student ID Number"]] = {'Last Name': row["Last Name"], 'First Name': row["First Name"], 'Gender': row["Gender"],'Year Level': row["Year Level"], 'Course': row["Course"]}
            self.temp = self.data.copy()
        
        
         
# Create Update Delete List (CRUDL)
        
        def iExit():
            iExit = tkinter.messagebox.askyesno("Confirm","Do you really want to exit?")
            if iExit > 0:
                root.destroy()
                return
            
        def addStudent():
            with open('data.csv', "a", newline="") as file:
                csvfile = csv.writer(file)
                if Student_IDNumber.get()=="" or Student_First_Name.get()==""  or Student_Last_Name.get()=="" or Student_YearLevel.get()=="":
                    tkinter.messagebox.showerror("Warning","Fill in the information")
                else:
                    self.data[Student_IDNumber.get()] = {'Last Name': Student_Last_Name.get(), 'First Name': Student_First_Name.get(), 'Gender': Student_Gender.get(),'Year Level': Student_YearLevel.get(), 'Course': Student_Course.get()}
                    self.saveData()
                    tkinter.messagebox.showinfo("Student Information System", "Stored Successfully!")
                Reset()
                displayData()
                    
        
        def Reset():
            Student_IDNumber.set("")
            Student_First_Name.set("")
            Student_Last_Name.set("")
            Student_YearLevel.set("")
            Student_Gender.set("")
            Student_Course.set("")
        
        
        
        def displayData():
            tree.delete(*tree.get_children())
            with open('data.csv') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    IDNumber=row['Student ID Number']
                    LastName=row['Last Name']
                    FirstName=row['First Name']
                    YearLevel=row['Year Level']
                    Course=row['Course']
                    Gender=row['Gender']
                    tree.insert("",END, values=(IDNumber, LastName, FirstName,Gender, YearLevel, Course))
                    
      
        
        def deleteData():
            if tree.focus()=="":
                tkinter.messagebox.showerror("Warning","Select a Student Record from the Table")
                return
            id_no = tree.item(tree.focus(),"values")[0]
            
            self.data.pop(id_no, None)
            self.saveData()
            tkinter.messagebox.askyesno("Confirm","Do you really want to delete this record?")
            tree.delete(tree.focus())
            
        
        def searchData():
            if self.searchbar.get() in self.data:
                vals = list(self.data[self.searchbar.get()].values())
                tree.delete(*tree.get_children())
                tree.insert("",0, values=(self.searchbar.get(), vals[0],vals[1],vals[2],vals[3],vals[4],))
            elif self.searchbar.get() == "":
                displayData()
            else:
                tkinter.messagebox.showerror("Warning","Student not found!")
                return
            
               
        
        def editData():
            if tree.focus() == "":
                tkinter.messagebox.showerror("Student Information System", "Select a Student Record from the Table")
                return
            values = tree.item(tree.focus(), "values")
            Student_IDNumber.set(values[0])
            Student_Last_Name.set(values[1])
            Student_First_Name.set(values[2])
            Student_Gender.set(values[3])
            Student_YearLevel.set(values[4])
            Student_Course.set(values[5])
       
    
       
        def updateData():
            with open('data.csv', "a", newline="") as file:
                csvfile = csv.writer(file)
                if Student_IDNumber.get()=="" or Student_First_Name.get()=="" or Student_Last_Name.get()=="" or Student_YearLevel.get()=="":
                    tkinter.messagebox.showinfo("Student Information System","Select a Student Record from the Table")
                else:
                    self.data[Student_IDNumber.get()] = {'Last Name': Student_Last_Name.get(), 'First Name': Student_First_Name.get(), 'Gender': Student_Gender.get(),'Year Level': Student_YearLevel.get(), 'Course': Student_Course.get()}
                    self.saveData()
                    tkinter.messagebox.showinfo("Student Information System", "Updated Successfully!")
                Reset()
                displayData()     

# FRAMES
        
        MainFrame = Frame(self.root, bd=7, width=1300, height=750, relief=RIDGE, bg="light green")
        MainFrame.grid()
        
        BotFrame = Frame(MainFrame,  width=1330, height=130, relief=RIDGE,bg="light green")
        BotFrame.grid(row=2, column=0)
        
        TitleFrame = Frame(MainFrame, bg="light green", width=1500, height=100, relief=RIDGE)
        TitleFrame.grid(row=0, column=0)
        
        MidFrame = Frame(MainFrame, bd=5,bg="orange", width=1500, height=450, relief=RIDGE)
        MidFrame.grid(row=1, column=0)
        
        SearchFrame = Frame(MainFrame, width = 1340, height = 100, relief = RIDGE)
        SearchFrame.grid(row =3, column =0)
        
        LeftFrame = Frame(MidFrame, bd=5, width=1600, height=400, padx=2, bg="cyan", relief=RIDGE)
        LeftFrame.pack(side=RIGHT)

        RightFrame = Frame(MidFrame, bd=5, width=900, height=400, padx=2, bg="cyan", relief=RIDGE)
        RightFrame.pack(side=LEFT)
        
        LeftFrame1 = Frame(RightFrame, bd=5,bg="pink", width=500, height=300, padx=2, pady=4, relief=RIDGE)
        LeftFrame1.pack(side=TOP, padx=0, pady=0)
        
        
        
# Title
        
        self.lblTitle = Label(TitleFrame, font=('Palatino',40,'bold'), text="STUDENT INFORMATION SYSTEM",bg="red",fg="yellow",bd=7)
        self.lblTitle.grid(row=0, column=0, padx=135)
        

# Variables in GUI        
        
        self.lblStudentID = Label(LeftFrame1, font=('Arial',12,'bold'), text="STUDENT ID NO.:",bg="yellow", bd=5 , anchor=W)
        self.lblStudentID.grid(row=0, column=0, sticky=W, padx=5)
        self.txtStudentID = Entry(LeftFrame1, font=('Arial',12,'bold'), width=40, justify='left', textvariable = Student_IDNumber)
        self.txtStudentID.grid(row=0, column=1)
        
        self.lblLastName = Label(LeftFrame1, font=('Arial',12,'bold'), text="LAST NAME:",bg="yellow",bd=7, anchor=W)
        self.lblLastName.grid(row=1, column=0, sticky=W, padx=5)
        self.txtLastName = Entry(LeftFrame1, font=('Arial',12,'bold'), width=40, justify='left', textvariable = Student_Last_Name)
        self.txtLastName.grid(row=1, column=1)
        
        self.lblFirstName = Label(LeftFrame1, font=('Arial',12,'bold'), text="FIRST NAME:",bg="yellow", bd=7, anchor=W)
        self.lblFirstName.grid(row=2, column=0, sticky=W, padx=5)
        self.txtFirstName = Entry(LeftFrame1, font=('Arial',12,'bold'), width=40, justify='left', textvariable = Student_First_Name)
        self.txtFirstName.grid(row=2, column=1)
        
        self.lblCourse = Label(LeftFrame1, font=('Arial',12,'bold'), text="COURSE:",bg="yellow", bd=7, anchor=W)
        self.lblCourse.grid(row=4, column=0, sticky=W, padx=5)
        self.txtCourse = Entry(LeftFrame1, font=('Arial',12,'bold'), width=40, justify='left', textvariable = Student_Course)
        self.txtCourse.grid(row=4, column=1)
        
        self.lblGender = Label(LeftFrame1, font=('Arial',12,'bold'), text="GENDER:", bg="yellow",bd=7, anchor=W)
        self.lblGender.grid(row=5, column=0, sticky=W, padx=5)
        
        self.cboGender = ttk.Combobox(LeftFrame1, font=('Arial',12,'bold'), state='readonly', width=38, textvariable = Student_Gender)
        self.cboGender['values'] = ('FEMALE', 'MALE')
        self.cboGender.grid(row=5, column=1)
        
        self.lblYearLevel = Label(LeftFrame1, font=('Arial',12,'bold'), text="YEAR LEVEL:", bg="yellow",bd=7, anchor=W)
        self.lblYearLevel.grid(row=6, column=0, sticky=W, padx=5)
        
        self.cboYearLevel = ttk.Combobox(LeftFrame1, font=('Arial',12,'bold'), state='readonly', width=38, textvariable = Student_YearLevel)
        self.cboYearLevel['values'] = ('1ST YEAR', '2ND YEAR', '3RD YEAR', '4TH YEAR')
        self.cboYearLevel.grid(row=6, column=1)
        
        self.searchbar = Entry(self.root, font=('Arial',12,'bold'), textvariable = searchbar, width = 33)
        self.searchbar.place(x=350,y=102)
        
        
        
# GUI Buttons
        
        self.btnAddNew=Button(self.root, pady=1,bd=4,font=('Arial',16,'bold'), padx=12, width=8,fg="black", bg="pink", text='ADD', command=addStudent)
        self.btnAddNew.place(x=105,y=450)
        
        self.btnReset=Button(self.root, pady=1,bd=4,font=('Arial',16,'bold'), padx=12, width=8,fg="black", bg="pink", text='RESET', command=Reset)
        self.btnReset.place(x=105,y=500)
        
        self.btnUpdate=Button(self.root, pady=1,bd=4,font=('Arial',16,'bold'), padx=12, width=8,fg="black", bg="pink", text='UPDATE', command=updateData)
        self.btnUpdate.place(x=305,y=450)

        self.btnEdit=Button(self.root, pady=1,bd=4,font=('Arial',16,'bold'), padx=12, width=8,fg="black", bg="pink", text='EDIT', command = editData)
        self.btnEdit.place(x=305,y=500)

        self.btnDisplay=Button(self.root, pady=1,bd=4, font=('Arial', 16, 'bold'),padx=12,width=8, fg="black", bg="pink", text="VIEW ALL" , command=displayData)
        self.btnDisplay.place(x=505,y=450)

        self.btnDelete=Button(self.root, pady=1,bd=4,font=('Arial',16,'bold'), padx=12, width=8,fg="red", bg="pink", text='DELETE',command = deleteData)
        self.btnDelete.place(x=505,y=500)

        self.btnExit=Button(self.root, pady=1,bd=4,font=('Arial',16,'bold'), padx=2, width=8,fg="red",bg="yellow", text='EXIT',command = iExit)
        self.btnExit.place(x=705,y=480)

        self.btnSearch=Button(self.root, pady=1,bd=4,font=('Arial',9,'bold'), padx=2, width=30, text='ENTER ID NUMBER TO SEARCH:',fg="yellow",bg="green", command = searchData)
        self.btnSearch.place(x=120,y=99)

        
        
# Tree View

        scroll_y=Scrollbar(LeftFrame, orient=VERTICAL)
        
        tree = ttk.Treeview(LeftFrame, height=15, columns=("Student ID Number", "Last Name", "First Name", "Gender", "Year Level", "Course"), yscrollcommand=scroll_y.set)

        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_y.config(command=tree.yview)

        tree.heading("Student ID Number", text="Student ID Number")
        tree.heading("Last Name", text="Last Name")
        tree.heading("First Name", text="First Name")
        tree.heading("Gender", text="Gender")
        tree.heading("Year Level", text="Year Level")
        tree.heading("Course", text="Course")
        tree['show'] = 'headings'

        tree.column("Student ID Number", width=120)
        tree.column("Last Name", width=100)
        tree.column("First Name", width=100)
        tree.column("Gender", width=70)
        tree.column("Year Level", width=70)
        tree.column("Course", width=80)
        tree.pack(fill=BOTH,expand=1)
        
        displayData()

# Saving the Data to csv
    def saveData(self):
        temps = []
        with open('data.csv', "w", newline ='') as update:
            fieldnames = ["Student ID Number","Last Name","First Name","Gender","Year Level","Course"]
            writer = csv.DictWriter(update, fieldnames=fieldnames, lineterminator='\n')
            writer.writeheader()
            for id, val in self.data.items():
                temp ={"Student ID Number": id}
                for key, value in val.items():
                    temp[key] = value
                temps.append(temp)
            writer.writerows(temps)
            

if __name__ =='__main__':
    root = Tk()
    application = Student (root)
    root.mainloop()

