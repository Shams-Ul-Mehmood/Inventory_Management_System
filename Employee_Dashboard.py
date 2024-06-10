from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from New_Employee import Add_Employee
from Employee_Salary import EmployeeSalary
from Employee_Attendence import EmployeeAttendence

class Employee_Module:
    def __init__(self , root_Object):
        self.rootObject = root_Object
        self.rootObject.geometry("1100x550+220+130")
        self.rootObject.title("Inventory Management System | Developed By Shams Afridi")
        self.rootObject.config(bg="white")
        self.rootObject.focus_force()

        #---------------> Employee-Attributes <---------------
        self.search_By = StringVar()
        self.search_Text = StringVar()

        self.employee_Id_Label = StringVar()
        self.employee_Name_Label = StringVar()
        self.employee_Gender_Label = StringVar()
        self.employee_Age_Label = StringVar()
        self.employee_Address_Label = StringVar()
        self.employee_Date_Of_Birth_Label = StringVar()
        self.employee_Contact_Label = StringVar()
        self.employee_Email_Label = StringVar()
        self.employee_Employment_Status_Label = StringVar()
        self.employee_Position_Label = StringVar()
        self.employee_Salary_Label = StringVar()
        self.employee_Attendence_Label = StringVar()
        self.employee_Date_Of_Joining_Label = StringVar()
        self.employee_Experience_Label = StringVar()

        #-----------> Attendence Frame <----------------
        attendence_Frame = LabelFrame( self.rootObject , text="Attendence" , font=("goudy old style",12,"bold") , bd = 2 , relief=RIDGE , bg="white" )
        attendence_Frame.place( x = 50 , y = 20 , width = 190 , height = 70 )
        attendence_Button = Button( attendence_Frame , text="Attendence" , font=("goudy old style",15) , bg="#2B65EC" , fg="white" , cursor="hand2" , command=self.checkEmployeeAttendence ).place(x=10,y=7,width=167,height=30)

        #-----------> Search Frame <----------------
        search_Frame = LabelFrame( self.rootObject , text="Search Employee" , font=("goudy old style",12,"bold") , bd = 2 , relief=RIDGE , bg="white" )
        search_Frame.place( x = 250 , y = 20 , width = 510 , height = 70 )

        #--------------> Search Frame Options <-------------------
        search_ComboBox = ttk.Combobox( search_Frame , textvariable=self.search_By , values=("Select","ID","Name","Email","Contact") , state="readonly" , justify=CENTER , font=("goudy old style",15) )
        search_ComboBox.place( x = 10 , y = 7 , width=160 )
        search_ComboBox.current(0)

        textField_Search = Entry( search_Frame , textvariable=self.search_Text , font=("goudy old style",15) , bg="lightyellow" ).place(x=180,y=7,width=180,height=30)

        search_Button = Button( search_Frame , text="Search" , font=("goudy old style",15) , bg="#008000" , fg="white" , cursor="hand2" ).place(x=370,y=7,width=130,height=30)

        #-----------> Salary Frame <----------------
        salary_and_Add_Employee_Frame = LabelFrame( self.rootObject , text="Salary & Add Employee" , font=("goudy old style",12,"bold") , bd = 2 , relief=RIDGE , bg="white" )
        salary_and_Add_Employee_Frame.place( x = 770 , y = 20 , width = 277 , height = 70 )
        salary_Button = Button( salary_and_Add_Employee_Frame , text="Salary" , font=("goudy old style",15) , bg="#4E5180" , fg="white" , cursor="hand2" , command=self.checkEmployeeSalary ).place(x=10,y=7,width=120,height=30)
        add_Employee_Button = Button( salary_and_Add_Employee_Frame , text="Add Employee" , font=("goudy old style",15) , bg="#A52A2A" , fg="white" , cursor="hand2" , command=self.addEmployee ).place(x=137,y=7,width=129,height=30)

        #-----------------> Employee-Details-Title <-----------------------
        employee_Details_Title = Label( self.rootObject , text="Employee Details" , font=("goudy old style",15) , bg="#273746" , fg="white" ).place(x=50,y=100,width=1000)

        #---------------------> Employee-Information-Table <--------------------------
        employee_Table_Frame = Frame( self.rootObject , bd=3 , relief=RIDGE )
        employee_Table_Frame.place( x = 50 , y = 135 , width = 1000 , height=404 )

        horizental_Scroll_Bar = Scrollbar( employee_Table_Frame , orient=HORIZONTAL )
        vertical_Scroll_Bar = Scrollbar( employee_Table_Frame , orient=VERTICAL )

        self.employee_Table = ttk.Treeview( employee_Table_Frame , columns=( "employee_id" , "employee_name" , "employee_gender" , "employee_age" , "employee_address" , "employee_dob" , "employee_contact" , "employee_email" , "employee_status" , "employee_position" , "employee_salary" , "employee_attendence" , "employee_doj" , "employee_experience" ) , xscrollcommand=horizental_Scroll_Bar.set , yscrollcommand=vertical_Scroll_Bar.set )
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
        self.employee_Table.heading( "employee_status" , text="Status" )
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
        self.employee_Table.column( "employee_status" , width=90 )
        self.employee_Table.column( "employee_position" , width=90 )
        self.employee_Table.column( "employee_salary" , width=90 )
        self.employee_Table.column( "employee_attendence" , width=90 )
        self.employee_Table.column( "employee_doj" , width=90 )
        self.employee_Table.column( "employee_experience" , width=90 )
        
        self.employee_Table.pack( fill=BOTH , expand=1 )

    #----------------> Check-Employee-Attendence <-----------------------
    def checkEmployeeAttendence(self):
        self.check_Employee_Attendence_Window = Toplevel( self.rootObject )
        self.check_Employee_Attendence_Window.resizable( False , False )
        self.employee_Attendence = EmployeeAttendence( self.check_Employee_Attendence_Window )

    #----------------> Add-Employee <-----------------------
    def addEmployee(self):
        self.add_Employee_Window = Toplevel( self.rootObject )
        self.add_Employee_Window.resizable( False , False )
        self.employee = Add_Employee( self.add_Employee_Window )
    
    #----------------> Check-Employee-Salary <-----------------------
    def checkEmployeeSalary(self):
        self.check_Employee_Salary_Window = Toplevel( self.rootObject )
        self.check_Employee_Salary_Window.resizable( False , False )
        self.employee_Salary = EmployeeSalary( self.check_Employee_Salary_Window )




if __name__ == "__main__":
    root_Object = Tk()
    employee_Module = Employee_Module( root_Object )
    root_Object.resizable( False , False )
    root_Object.mainloop()  # mainloop() use to keep open output-window.