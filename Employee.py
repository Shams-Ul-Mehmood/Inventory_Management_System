from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk

class Employee_Module:
    def __init__(self , root_Object):
        self.rootObject = root_Object
        self.rootObject.geometry("1100x500+220+130")
        self.rootObject.title("Inventory Management System | Developed By Shams Afridi")
        self.rootObject.config(bg="white")
        self.rootObject.focus_force()

        #-----------> Search Frame <----------------
        search_Frame = LabelFrame( self.rootObject , text="Search Employee" , font=("goudy old style",12,"bold") , bd = 2 , relief=RIDGE , bg="white" )
        search_Frame.place( x = 250 , y = 20 , width = 600 , height = 70 )

        #--------------> Search Frame Options <-------------------
        search_ComboBox = ttk.Combobox( search_Frame , values=("Select","ID","Name","Email","Contact") , state="readonly" , justify=CENTER , font=("goudy old style",15) )
        search_ComboBox.place( x = 10 , y = 7 , width=180 )
        search_ComboBox.current(0)

        textField_Search = Entry( search_Frame , font=("goudy old style",15) , bg="lightyellow" ).place(x=200,y=7,width=220,height=30)

        search_Button = Button( search_Frame , text="Search" , font=("goudy old style",15) , bg="#008000" , fg="white" , cursor="hand2" ).place(x=430,y=7,width=150,height=30)

        #-----------------> Employee-Details-Title <-----------------------
        employee_Details_Title = Label( self.rootObject , text="Employee Details" , font=("goudy old style",15) , bg="#273746" , fg="white" ).place(x=50,y=100,width=1000)






if __name__ == "__main__":
    root_Object = Tk()
    employee_Module = Employee_Module( root_Object )
    root_Object.mainloop()  # mainloop() use to keep open output-window.