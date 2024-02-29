from tkinter import *
from PIL import Image, ImageTk
from Employee import Employee_Module
class Inventory_Management_System:
    def __init__(self , root_Object):
        self.rootObject = root_Object
        self.rootObject.geometry("1550x900+0+0")
        self.rootObject.title("Inventory Management System | Developed By Shams Afridi")
        self.rootObject.config(bg="white")

        # ---------> Inventory Management System Title <--------------
        self.title_icon = PhotoImage(file="./pictures/cart_logo_2.png")
        inventory_Management_System_Title = Label( self.rootObject , text="Inventory Management System" , font=("times new roman", 40, "bold") , bg="#273746" ,fg="white" , anchor="w" , padx=20 , image=self.title_icon , compound=LEFT ).place(x=0 , y=0 , relwidth=1 , height=70 )

        # -----> Logout-Button <--------
        logout_button = Button( self.rootObject , text="Logout" , font=("times new roman",15,"bold") , bg="white" , fg="black" , cursor="hand2" ).place(x=1350 , y=5 , height=60 , width=150 )

        # --------> clock <---------
        self.label_clock = Label( self.rootObject , text="Welcome To Inventory Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS" , font=("times new roman", 15) , bg="#616A6B" , fg="white" )
        self.label_clock.place(x=0 , y=70 , relwidth=1 , height=30 )

        # -------> Left Menu <--------
        self.menu_Logo = Image.open("./pictures/menu__logo.jpg")
        self.menu_Logo = self.menu_Logo.resize((200,200) ,Image.BICUBIC)
        self.menu_Logo = ImageTk.PhotoImage( self.menu_Logo )

        left_Menu = Frame( self.rootObject , bd=2 , relief=RIDGE , bg="white" )
        left_Menu.place( x = 0 , y = 102 , width = 200 , height = 690 )

        menu_Logo_Label = Label( left_Menu , image = self.menu_Logo )
        menu_Logo_Label.pack( side=TOP , fill=X )

        menu_Label = Label( left_Menu , text="Menu" , font=("times new roman",20) , bg="#008080" , fg="white" ).pack( side=TOP , fill=X )

        # -----------> Left Menu Buttons <------------
        self.arrow_Button_Icon = Image.open("./pictures/arrow_button_icon_5.png")
        self.arrow_Button_Icon = self.arrow_Button_Icon.resize( (30,30) , Image.BICUBIC )
        self.arrow_Button_Icon = ImageTk.PhotoImage( self.arrow_Button_Icon )
        employee_Button = Button( left_Menu , text="Employee" , font=("times new roman",20,"bold") , bg="white" , cursor="hand2" , bd=4 , image=self.arrow_Button_Icon , compound=LEFT , padx=5 , anchor="w" , command=self.employee_Section ).pack( side=TOP , fill=X )
        supplier_Button = Button( left_Menu , text="Supplier" , font=("times new roman",20,"bold") , bg="white" , cursor="hand2" , bd=4 , image=self.arrow_Button_Icon , compound=LEFT , padx=5 , anchor="w" ).pack( side=TOP , fill=X )
        product_Button = Button( left_Menu , text="Product" , font=("times new roman",20,"bold") , bg="white" , cursor="hand2" , bd=4 , image=self.arrow_Button_Icon , compound=LEFT , padx=5 , anchor="w" ).pack( side=TOP , fill=X )
        sales_Button = Button( left_Menu , text="Sales" , font=("times new roman",20,"bold") , bg="white" , cursor="hand2" , bd=4 , image=self.arrow_Button_Icon , compound=LEFT , padx=5 , anchor="w" ).pack( side=TOP , fill=X )
        category_Button = Button( left_Menu , text="Category" , font=("times new roman",20,"bold") , bg="white" , cursor="hand2" , bd=4 , image=self.arrow_Button_Icon , compound=LEFT , padx=5 , anchor="w" ).pack( side=TOP , fill=X )
        exit_Button = Button( left_Menu , text="Exit" , font=("times new roman",20,"bold") , bg="white" , cursor="hand2" , bd=4 , image=self.arrow_Button_Icon , compound=LEFT , padx=5 , anchor="w" ).pack( side=TOP , fill=X )

        # -------------> Content <----------------

        self.employee_label = Label( self.rootObject , text="Total Employee\n[0]" , bg="#273746" , fg="white" , bd = 3 , relief=RIDGE , font=("goudy old style",20,"bold") )
        self.employee_label.place( x = 300 , y = 170 , width = 300 , height = 150 )
        self.supplier_label = Label( self.rootObject , text="Total Supplier\n[0]" , bg="#273746" , fg="white" , bd = 3 , relief=RIDGE , font=("goudy old style",20,"bold") )
        self.supplier_label.place( x = 650 , y = 170 , width = 300 , height = 150 )
        self.product_label = Label( self.rootObject , text="Total Product\n[0]" , bg="#273746" , fg="white" , bd = 3 , relief=RIDGE , font=("goudy old style",20,"bold") )
        self.product_label.place( x = 1000 , y = 170 , width = 300 , height = 150 )
        self.sales_label = Label( self.rootObject , text="Total Sales\n[0]" , bg="#273746" , fg="white" , bd = 3 , relief=RIDGE , font=("goudy old style",20,"bold") )
        self.sales_label.place( x = 300 , y = 360 , width = 300 , height = 150 )
        self.category_label = Label( self.rootObject , text="Total Category\n[0]" , bg="#273746" , fg="white" , bd = 3 , relief=RIDGE , font=("goudy old style",20,"bold") )
        self.category_label.place( x = 650 , y = 360 , width = 300 , height = 150 )

        # --------> footer <---------
        footer_label = Label( self.rootObject , text="Inventory Management System | Developed By Shams Afridi" , font=("times new roman", 12) , bg="#616A6B" , fg="white" ).pack( side=BOTTOM , fill=X )
    
    #----------------------------> Employee-Module <---------------------
    def employee_Section(self):
        self.employee_Window = Toplevel( self.rootObject )
        self.employee = Employee_Module( self.employee_Window )


if __name__ == "__main__":
    root_Object = Tk()
    inventory_Management_System = Inventory_Management_System( root_Object )
    root_Object.mainloop()  # mainloop() use to keep open output-window.