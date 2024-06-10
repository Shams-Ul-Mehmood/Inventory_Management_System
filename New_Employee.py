from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk , messagebox
import sqlite3

class Add_Employee:
    def __init__(self , root_Object):
        self.rootObject = root_Object
        self.rootObject.geometry("1100x370+220+130")
        self.rootObject.title("Inventory Management System | Developed By Shams Afridi")
        self.rootObject.config(bg="white")
        self.rootObject.focus_force()

        #---------------> Employee-Attributes <---------------
        self.search_By = StringVar()
        self.search_Text = StringVar()

        self.employee_Id = StringVar()
        self.employee_Name = StringVar()
        self.employee_Gender = StringVar()
        self.employee_Age = StringVar()
        # self.employee_Address = StringVar()
        self.employee_Date_Of_Birth = StringVar()
        self.employee_Contact = StringVar()
        self.employee_Email = StringVar()
        self.employee_Employment_Status = StringVar()
        self.employee_Position = StringVar()
        self.employee_Salary = StringVar()
        self.employee_Attendence = StringVar()
        self.employee_Date_Of_Joining = StringVar()
        self.employee_Experience = StringVar()

        #-----------------> Employee-Details-Title <-----------------------
        employee_Details_Title = Label( self.rootObject , text="Employee Entry Form" , font=("goudy old style",15) , bg="#273746" , fg="white" ).place(x=50,y=20,width=1000)

        #---------------------> Employee-Details Contents <------------------------
        self.employee_Id_Label = Label( self.rootObject , text="Emp ID" , font=("goudy old style",15) , bg="white" ).place(x=50,y=70)
        self.employee_Id_Text_Field = Entry( self.rootObject , textvariable=self.employee_Id , font=("goudy old style",15) , bg="lightyellow" ).place(x=150,y=70,width=180)
        
        self.employee_Name_Label = Label( self.rootObject , text="Name" , font=("goudy old style",15) , bg="white" ).place(x=350,y=70)
        self.employee_Name_Text_Field = Entry( self.rootObject , textvariable=self.employee_Name , font=("goudy old style",15) , bg="lightyellow" ).place(x=500,y=70,width=180)

        self.employee_Gender_Label = Label( self.rootObject , text="Gender" , font=("goudy old style",15) , bg="white" ).place(x=750,y=70)
        # self.employee_Gender_Text_Field = Entry( self.rootObject , textvariable=self.employee_Gender_Label , font=("goudy old style",15) , bg="lightyellow" ).place(x=830,y=70,width=180)
        employee_Gender_ComboBox = ttk.Combobox( self.rootObject , textvariable=self.employee_Gender , values=("Select","Male","Female","Other") , state="readonly" , justify=CENTER , font=("goudy old style",15) )
        employee_Gender_ComboBox.place(x=850,y=70,width=180)
        employee_Gender_ComboBox.current(0)

        self.employee_Age_Label = Label( self.rootObject , text="Age" , font=("goudy old style",15) , bg="white" ).place(x=50,y=115)
        self.employee_Age_Text_Field = Entry( self.rootObject , textvariable=self.employee_Age , font=("goudy old style",15) , bg="lightyellow" ).place(x=150,y=115,width=180)

        self.employee_Email_Label = Label( self.rootObject , text="Email" , font=("goudy old style",15) , bg="white" ).place(x=350,y=115)
        self.employee_Email_Text_Field = Entry( self.rootObject , textvariable=self.employee_Email , font=("goudy old style",15) , bg="lightyellow" ).place(x=500,y=115,width=180)

        self.employee_Date_Of_Birth_Label = Label( self.rootObject , text="D.O.B" , font=("goudy old style",15) , bg="white" ).place(x=750,y=115)
        self.employee_DOB_Text_Field = Entry( self.rootObject , textvariable=self.employee_Date_Of_Birth , font=("goudy old style",15) , bg="lightyellow" ).place(x=850,y=115,width=180)
        
        self.employee_Contact_Label = Label( self.rootObject , text="Contact" , font=("goudy old style",15) , bg="white" ).place(x=50,y=165)
        self.employee_Contact_Text_Field = Entry( self.rootObject , textvariable=self.employee_Contact , font=("goudy old style",15) , bg="lightyellow" ).place(x=150,y=165,width=180)
                
        self.employee_Employment_Status_Label = Label( self.rootObject , text="Status" , font=("goudy old style",15) , bg="white" ).place(x=350,y=165)
        self.employee_Employement_Status_Text_Field = Entry( self.rootObject , textvariable=self.employee_Employment_Status , font=("goudy old style",15) , bg="lightyellow" ).place(x=500,y=165,width=180)

        self.employee_Position_Label = Label( self.rootObject , text="Position" , font=("goudy old style",15) , bg="white" ).place(x=750,y=165)
        self.employee_Position_Text_Field = Entry( self.rootObject , textvariable=self.employee_Position , font=("goudy old style",15) , bg="lightyellow" ).place(x=850,y=165,width=180)

        self.employee_Salary_Label = Label( self.rootObject , text="Salary" , font=("goudy old style",15) , bg="white" ).place(x=50,y=215)
        self.employee_Salary_Text_Field = Entry( self.rootObject , textvariable=self.employee_Salary , font=("goudy old style",15) , bg="lightyellow" ).place(x=150,y=215,width=180)
        
        self.employee_Attendence_Label = Label( self.rootObject , text="Attendence" , font=("goudy old style",15) , bg="white" ).place(x=350,y=215)
        self.employee_Attendence_Text_Field = Entry( self.rootObject , textvariable=self.employee_Attendence , font=("goudy old style",15) , bg="lightyellow" ).place(x=500,y=215,width=180)

        self.employee_Experience_Label = Label( self.rootObject , text="Experience" , font=("goudy old style",15) , bg="white" ).place(x=750,y=215)
        self.employee_Experience_Text_Field = Entry( self.rootObject , textvariable=self.employee_Experience , font=("goudy old style",15) , bg="lightyellow" ).place(x=850,y=215,width=180)

        self.employee_Date_Of_Joining_Label = Label( self.rootObject , text="Joining Date" , font=("goudy old style",15) , bg="white" ).place(x=500,y=265)
        self.employee_Date_Of_Joining_Text_Field = Entry( self.rootObject , textvariable=self.employee_Date_Of_Joining , font=("goudy old style",15) , bg="lightyellow" ).place(x=620,y=265,width=180)

        self.employee_Address_Label = Label( self.rootObject , text="Address" , font=("goudy old style",15) , bg="white" ).place(x=50,y=265)
        self.employee_Address_Text_Field = Text( self.rootObject , font=("goudy old style",15) , bg="lightyellow" )
        self.employee_Address_Text_Field.place(x=150,y=270,width=300,height=70)

        #------------------> Buttons Section <-------------------------------
        save_Button = Button( self.rootObject , text="Save" , font=("goudy old style",15) , bg="#008000" , fg="white" , cursor="hand2" , command=self.save ).place(x=500,y=300,width=110,height=40)
        update_Button = Button( self.rootObject , text="Update" , font=("goudy old style",15) , bg="#2B65EC" , fg="white" , cursor="hand2" ).place(x=620,y=300,width=110,height=40)
        delete_Button = Button( self.rootObject , text="Delete" , font=("goudy old style",15) , bg="#FF0000" , fg="white" , cursor="hand2" ).place(x=740,y=300,width=110,height=40)
        clear_Button = Button( self.rootObject , text="Clear" , font=("goudy old style",15) , bg="#4E5180" , fg="white" , cursor="hand2" ).place(x=860,y=300,width=110,height=40)

        #---------------------> Employee-Information-Table <--------------------------
        employee_Table_Frame = Frame( self.rootObject , bd=3 , relief=RIDGE )
        employee_Table_Frame.place( x = 0 , y = 380 , relwidth = 1 , height=150 )

        horizental_Scroll_Bar = Scrollbar( employee_Table_Frame , orient=HORIZONTAL )
        vertical_Scroll_Bar = Scrollbar( employee_Table_Frame , orient=VERTICAL )

        self.employee_Table = ttk.Treeview( employee_Table_Frame , columns=( "employee_id" , "employee_name" , "employee_gender" , "employee_age" , "employee_address" , "employee_dob" , "employee_contact" , "employee_email" , "employee_employment_status" , "employee_position" , "employee_salary" , "employee_attendence" , "employee_doj" , "employee_experience" ) , xscrollcommand=horizental_Scroll_Bar.set , yscrollcommand=vertical_Scroll_Bar.set )
        horizental_Scroll_Bar.pack( side=BOTTOM , fill=X )
        vertical_Scroll_Bar.pack( side=RIGHT , fill=Y )
        horizental_Scroll_Bar.config( command=self.employee_Table.xview )
        vertical_Scroll_Bar.config( command=self.employee_Table.yview )

        self.employee_Table.heading( "employee_id" , text="Employee ID" )
        self.employee_Table.heading( "employee_name" , text="Name" )
        self.employee_Table.heading( "employee_gender" , text="Gender" )
        self.employee_Table.heading( "employee_age" , text="Age" )
        self.employee_Table.heading( "employee_address" , text="Address" )
        self.employee_Table.heading( "employee_dob" , text="Date-Of-Birth" )
        self.employee_Table.heading( "employee_contact" , text="Contact" )
        self.employee_Table.heading( "employee_email" , text="Email" )
        self.employee_Table.heading( "employee_employment_status" , text="Status" )
        self.employee_Table.heading( "employee_position" , text="Position" )
        self.employee_Table.heading( "employee_salary" , text="Salary" )
        self.employee_Table.heading( "employee_attendence" , text="Attendence" )
        self.employee_Table.heading( "employee_doj" , text="Joining Date" )
        self.employee_Table.heading( "employee_experience" , text="Experience" )
        
        self.employee_Table["show"] = "headings"

        self.employee_Table.column( "employee_id" , width=90 )
        self.employee_Table.column( "employee_name" , width=90 )
        self.employee_Table.column( "employee_gender" , width=90 )
        self.employee_Table.column( "employee_age" , width=90 )
        self.employee_Table.column( "employee_address" , width=90 )
        self.employee_Table.column( "employee_dob" , width=90 )
        self.employee_Table.column( "employee_contact" , width=90 )
        self.employee_Table.column( "employee_email" , width=90 )
        self.employee_Table.column( "employee_employment_status" , width=90 )
        self.employee_Table.column( "employee_position" , width=90 )
        self.employee_Table.column( "employee_salary" , width=90 )
        self.employee_Table.column( "employee_attendence" , width=90 )
        self.employee_Table.column( "employee_doj" , width=90 )
        self.employee_Table.column( "employee_experience" , width=90 )
        
        self.employee_Table.pack( fill=BOTH , expand=1 )
    
    #------------------> Database Section <-----------------------
    def save( self ):
        database_Connection = sqlite3.connect(database=r"Inventory_Management_System.db")
        queryCursor = database_Connection.cursor()
        try:
            if self.employee_Id.get() == "":
                messagebox.showerror("Error" , "Employee-ID Must Be Required" , parent=self.rootObject)
            elif self.employee_Name.get() == '':
                messagebox.showerror("Error" , "Employee-Name Must Be Required" , parent=self.rootObject)
            # elif self.employee_Address.get() == "":
            #     messagebox.showerror("Error" , "Employee-Address Must Be Required" , parent=self.rootObject)
            elif self.employee_Age.get() == '':
                messagebox.showerror("Error" , "Employee-Age Must Be Required" , parent=self.rootObject)
            elif self.employee_Contact.get() == "":
                messagebox.showerror("Error" , "Employee-Contact Must Be Required" , parent=self.rootObject)
            elif self.employee_Date_Of_Joining.get() == '':
                messagebox.showerror("Error" , "Employee-Joining-Date Must Be Required" , parent=self.rootObject)
            elif self.employee_Date_Of_Birth.get() == "":
                messagebox.showerror("Error" , "Employee-Date-Of-Birth Must Be Required" , parent=self.rootObject)
            elif self.employee_Email.get() == '':
                messagebox.showerror("Error" , "Employee-Email Must Be Required" , parent=self.rootObject)
            elif self.employee_Experience.get() == "":
                messagebox.showerror("Error" , "Employee-Experience Must Be Required" , parent=self.rootObject)
            elif self.employee_Salary.get() == '':
                messagebox.showerror("Error" , "Employee-Salary Must Be Required" , parent=self.rootObject)
            # elif self.employee_Gender.get() == "":
            #     messagebox.showerror("Error" , "Employee-Gender Must Be Required" , parent=self.rootObject)
            elif self.employee_Employment_Status.get() == '':
                messagebox.showerror("Error" , "Employee-Employment-Status Must Be Required" , parent=self.rootObject)
            elif self.employee_Position.get() == '':
                messagebox.showerror("Error" , "Employee-Position Must Be Required" , parent=self.rootObject)
            else:
                queryCursor.execute("select * from Employee where employee_id = ?",( self.employee_Id.get() , ) )
                row = queryCursor.fetchone()
                if row != None:
                    messagebox.showerror("Error" , f"This Employee-ID({row}) Is Already Assigned To Someone So,\nPlease Try different Employee-ID" , parent = self.rootObject)
                else:
                    queryCursor.execute("insert into Employee ( employee_id , employee_name , employee_gender , employee_age , employee_address , employee_dob , employee_contact , employee_email , employee_employment_status , employee_position , employee_salary , employee_attendence , employee_doj , employee_experience ) values( ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? ) " , ( self.employee_Id.get() , self.employee_Name.get() , self.employee_Gender.get() , self.employee_Age.get() , self.employee_Address_Text_Field.get('1.0',END) , self.employee_Date_Of_Birth.get() , self.employee_Contact.get() , self.employee_Email.get() , self.employee_Employment_Status.get() , self.employee_Position.get() , self.employee_Salary.get() , self.employee_Attendence.get() , self.employee_Date_Of_Joining.get() , self.employee_Experience.get() ) )
                    database_Connection.commit()
                    messagebox.showinfo("Success" , "Successfully New Employee Added" , parent=self.rootObject)


        except Exception as exception_error:
            messagebox.showerror("Error" , f"Error due to : {str(exception_error)} " , parent = self.rootObject)


if __name__ == "__main__":
    root_Object = Tk()
    
    add_Employee = Add_Employee( root_Object )
    root_Object.resizable( False , False )
    root_Object.mainloop()  # mainloop() use to keep open output-window.