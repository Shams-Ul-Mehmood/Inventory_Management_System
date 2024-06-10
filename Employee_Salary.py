from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk

class EmployeeSalary:
    def __init__(self , root_Object):
        self.rootObject = root_Object
        self.rootObject.geometry("1100x480+220+130")
        self.rootObject.title("Inventory Management System | Developed By Shams Afridi")
        self.rootObject.config(bg="white")
        self.rootObject.focus_force()

        #-----------------> Employee-Salary-Details-Title <-----------------------
        employee_Salary_Details_Title = Label( self.rootObject , text="Employee Salary Details" , font=("goudy old style",15) , bg="#273746" , fg="white" ).place(x=50,y=15,width=1000)

        #---------------------> Employee-Information-Table <--------------------------
        employee_Table_Frame = Frame( self.rootObject , bd=3 , relief=RIDGE )
        employee_Table_Frame.place( x = 50 , y = 55 , width = 1000 , height=404 )

        horizental_Scroll_Bar = Scrollbar( employee_Table_Frame , orient=HORIZONTAL )
        vertical_Scroll_Bar = Scrollbar( employee_Table_Frame , orient=VERTICAL )

        self.employee_Table = ttk.Treeview( employee_Table_Frame , columns=( "employee_id" , "employee_name" , "employee_salary" , "salary_time" , "salary_date" ) , xscrollcommand=horizental_Scroll_Bar.set , yscrollcommand=vertical_Scroll_Bar.set )
        horizental_Scroll_Bar.pack( side=BOTTOM , fill=X )
        vertical_Scroll_Bar.pack( side=RIGHT , fill=Y )
        horizental_Scroll_Bar.config( command=self.employee_Table.xview )
        vertical_Scroll_Bar.config( command=self.employee_Table.yview )

        self.employee_Table.heading( "employee_id" , text="Employee ID" )
        self.employee_Table.heading( "employee_name" , text="Name" )
        self.employee_Table.heading( "employee_salary" , text="Salary" )
        self.employee_Table.heading( "salary_time" , text="Time" )
        self.employee_Table.heading( "salary_date" , text="Date" )
        
        self.employee_Table["show"] = "headings"

        self.employee_Table.column( "employee_id" , width=90 )
        self.employee_Table.column( "employee_name" , width=90 )
        self.employee_Table.column( "employee_salary" , width=90 )
        self.employee_Table.column( "salary_time" , width=90 )
        self.employee_Table.column( "salary_date" , width=90 )
        
        self.employee_Table.pack( fill=BOTH , expand=1 )


if __name__ == "__main__":
    root_Object = Tk()
    
    add_Employee = EmployeeSalary( root_Object )
    root_Object.resizable( False , False )
    root_Object.mainloop()  # mainloop() use to keep open output-window.
