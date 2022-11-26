from tkinter import *
from tkinter import font
from PIL import ImageTk, Image #install pil
from tkmacosx import* # this is just the tkinter that works fully on mac 
import sqlite3


class Main_menu:
    
    def __init__(self,window): #
        #creating the window 
        self.mm_window= window
        self.mm_window.geometry("1000x700")
        self.mm_window.title("Main menu screen")
        self.mm_window.configure(bg = "white")
        #To zoom the page 
        self.mm_window.state("zoomed")
        self.mm_window.resizable(0,0)

        #right hand side image
        self.shape_image = Image.open("shape design.png")
        self.photo2 = ImageTk.PhotoImage(self.shape_image)
        self.panel2= Label(self.mm_window,image = self.photo2)
        self.panel2.image = self.photo2
        self.panel2.place(x=950, y=0,height = 1000)

        #submit button
        self.guest_icon =  Image.open("Guests_icon.png")
        self.guest_icon_resize = self.guest_icon.resize((65,65))
        self.guest_icon = self.guest_icon_resize 
        guest_icon_photo = ImageTk.PhotoImage(self.guest_icon)
        self.gb_label = Label(self.mm_window,image =guest_icon_photo ,bg = "white")
        self.gb_label.image= guest_icon_photo
        self.guest_button = Button(self.mm_window, image = guest_icon_photo ,command=self.guest_files,cursor = "hand2",bg = "white",borderwidth = 0)
        self.guest_button.place(x=1280,y=550,width = 80, height = 80)

        guest_icon_heading = Label(self.mm_window, text = "Guests",font = ("Avenir Next",15),bg = "white")
        guest_icon_heading.place(x=1280,y=630,width = 80)


    def guest_files(self): #ask why when I pen 
        self.mm_window.destroy()
        self.gf_window= Tk()
        self.gf_window.geometry("1400x900")
        self.gf_window.title("Guest files")
        self.gf_window.configure(bg = "white")
        #To zoom the page 
        self.gf_window.state("zoomed")
        self.gf_window.resizable(0,0)

        #right hand side image
        shape_image1 = Image.open("shape design.png")
        photo2 = ImageTk.PhotoImage(shape_image1)
        label2= Label(self.gf_window,image = photo2)
        label2.image = photo2
        label2.place(x=950, y=0,height = 1000)

        #Add user button
        self.add_guest_icon = Image.open("add_user_icon.png")
        self.add_guest_icon_resize = self.add_guest_icon.resize((150,150))
        self.add_guest_icon = self.add_guest_icon_resize
        self.add_guest_photo = ImageTk.PhotoImage(self.add_guest_icon)
        self.ag_label = Label(self.gf_window,image =self.add_guest_photo ,bg = "white")
        self.ag_label.image = self.add_guest_photo
        self.ag_button = Button(self.gf_window, image = self.add_guest_photo,command = self.guest_add,cursor = "hand2",bg = "white",borderwidth = 0)
        self.ag_button.place(x=1125,y=300,width = 160, height = 160)

        guest_add_heading = Label(self.gf_window, text = "Add new guest record",font = ("Arial Rounded MT",14,"bold"),bg = "white")
        guest_add_heading.place(x=1125,y=460,width = 160)


    def guest_add(self):
        self.gf_window.destroy()
        self.ga_window= Tk()
        self.ga_window.geometry("1400x900")
        self.ga_window.title("Guests search file")
        self.ga_window.configure(bg = "white")
        #To zoom the page 
        self.ga_window.state("zoomed")
        self.ga_window.resizable(0,0)

        #right hand side image
        shape_image1 = Image.open("shape design.png")
        photo2 = ImageTk.PhotoImage(shape_image1)
        label2= Label(self.ga_window,image = photo2)
        label2.image = photo2
        label2.place(x=950, y=0,height = 1000)
        
##      New guest record heading 
        self.guest_heading_image = Image.open("Guest records heading.png")
        self.guest_heading_image_resize = self.guest_heading_image.resize((400,75))
        self.guest_heading_image = self.guest_heading_image_resize
        photo_guest_heading = ImageTk.PhotoImage(self.guest_heading_image)
        self.guest_label = Label(self.ga_window,image = photo_guest_heading)
        self.guest_label.image = photo_guest_heading
        self.guest_label.place(x=150, y=0,height = 75)

        #Frame for entry details for new guest 
        self.new_guest_frame = Frame(self.ga_window, bg="white", width = 700, height= 700)
        self.new_guest_frame.place(x=100, y=100)

##      GuestID
        self.guest_ID = Label(self.new_guest_frame, text = "GuestID:", font = ("Avenir Next",20,"bold"), bg="white")
        self.guest_ID.place(x=40,y=15)
        self.guest_ID_entry = Entry(self.new_guest_frame,width = 15,bg = "honeydew",highlightthickness = 0,font = ("Avenir Next",20),relief=FLAT)
        self.guest_ID_entry.place(x=155,y=20,height = 25)
          
        #Name of guest  
        self.guest_name = Label(self.new_guest_frame, text = "First Name:", font = ("Avenir Next",20,"bold"), bg="white")
        self.guest_name.place(x=40,y=115)
        self.guest_name_entry = Entry(self.new_guest_frame,width = 50,bg = "honeydew",highlightthickness = 0,font = ("Avenir Next",20),relief=FLAT)
        self.guest_name_entry.place(x=160,y=120,height = 25)
          
        self.guest_surname = Label(self.new_guest_frame, text = "Surname:", font = ("Avenir Next",20,"bold"), bg="white")
        self.guest_surname.place(x=40,y=165)
        self.guest_surname_entry = Entry(self.new_guest_frame,width = 50,bg = "honeydew",highlightthickness = 0,font = ("Avenir Next",20),relief=FLAT)
        self.guest_surname_entry.place(x=160,y=170,height = 25)

##      title
        self.guest_title = Label(self.new_guest_frame, text = "Title:", font = ("Avenir Next",20,"bold"), bg="white")
        self.guest_title.place(x=40,y=215)
        self.guest_title_entry = Entry(self.new_guest_frame,width = 50,bg = "honeydew",highlightthickness = 0,font = ("Avenir Next",20),relief=FLAT)
        self.guest_title_entry.place(x=160,y=220,height = 25)
##      Date of birth
        self.guest_DOB = Label(self.new_guest_frame, text = "DOB:", font = ("Avenir Next",20,"bold"), bg="white")
        self.guest_DOB.place(x=40,y=265)
        self.guest_DOB_entry = Entry(self.new_guest_frame,width = 50,bg = "honeydew",highlightthickness = 0,font = ("Avenir Next",20),relief=FLAT)
        self.guest_DOB_entry.place(x=160,y=270,height = 25)
##      Payment type
        self.guest_payment = Label(self.new_guest_frame, text = "Payment:", font = ("Avenir Next",20,"bold"), bg="white")
        self.guest_payment.place(x=40,y=315)
        self.guest_payment_entry = Entry(self.new_guest_frame,width = 50,bg = "honeydew",highlightthickness = 0,font = ("Avenir Next",20),relief=FLAT)
        self.guest_payment_entry.place(x=160,y=320,height = 25)
##      Email
        self.guest_email = Label(self.new_guest_frame, text = "Email:", font = ("Avenir Next",20,"bold"), bg="white")
        self.guest_email.place(x=40,y=365)
        self.guest_email_entry = Entry(self.new_guest_frame,width = 50,bg = "honeydew",highlightthickness = 0,font = ("Avenir Next",20),relief=FLAT)
        self.guest_email_entry.place(x=160,y=370,height = 25)
##      PhoneNumber
        self.guest_phone = Label(self.new_guest_frame, text = "Phone No:", font = ("Avenir Next",20,"bold"), bg="white")
        self.guest_phone.place(x=40,y=415)
        self.guest_phone_entry = Entry(self.new_guest_frame,width = 50,bg = "honeydew",highlightthickness = 0,font = ("Avenir Next",20),relief=FLAT)
        self.guest_phone_entry.place(x=160,y=420,height = 25)
##      Adress
        self.guest_adress = Label(self.new_guest_frame, text = "Address:", font = ("Avenir Next",20,"bold"), bg="white")
        self.guest_adress.place(x=40,y=465)
        self.guest_adress_entry = Entry(self.new_guest_frame,width = 50,bg = "honeydew",highlightthickness = 0,font = ("Avenir Next",20),relief=FLAT)
        self.guest_adress_entry.place(x=160,y=470,height = 25)
##      Postcode
        self.guest_postcode = Label(self.new_guest_frame, text = "Postcode:", font = ("Avenir Next",20,"bold"), bg="white")
        self.guest_postcode.place(x=40,y=515)
        self.guest_postcode_entry = Entry(self.new_guest_frame,width = 50,bg = "honeydew",highlightthickness = 0,font = ("Avenir Next",20),relief=FLAT)
        self.guest_postcode_entry.place(x=160,y=520,height = 25)

##        Save button
        self.save_guest_icon = Image.open("save_icon.png")
        self.save_guest_icon_resize = self.save_guest_icon.resize((75,75))
        self.save_guest_icon = self.save_guest_icon_resize
        self.save_guest_photo = ImageTk.PhotoImage(self.save_guest_icon)
        self.sg_label = Label(self.ga_window,image =self.save_guest_photo ,bg = "white")
        self.sg_label.image = self.save_guest_photo
        self.sg_button = Button(self.ga_window, image = self.save_guest_photo,command = self.save,cursor = "hand2",bg = "white",borderwidth = 0)
        self.sg_button.place(x=1150, y=500)

        


    def save(self):
        #this connects to the database - if the database 
        #doesnt exist it will create it

        connection = sqlite3.connect("Guestrecord.db")
        cursor = connection.cursor()


        #Creating tables in Database - Only creates the 
        #table if they do not exist already

        #sets up the fields needed for the customer table

        sqlCommand = """
           CREATE TABLE IF NOT EXISTS tblGuest1
           (
           GuestID INTEGER NOT NULL,
           GuestTitle TEXT,
           GuestFirstname TEXT,
           GuestSurname TEXT,
           GuestDOB DATE,
           GuestPaymentType TEXT,
           GuestEmail TEXT,
           GuestPhoneNumber INTEGER,
           GuestAddress TEXT,
           GuestPostcode TEXT,
           primary key (GuestID)
           )
        """
        #executes the command to create the table
        cursor.execute(sqlCommand)


        #saves all changes made to database and closes the connection to the database
        connection.commit()
        connection.close()



        connection = sqlite3.connect("Guestrecord.db")
        cursor = connection.cursor()

        #setting up variables to hold the data entered
        cTitle = self.guest_title_entry.get()
        cFirstname = self.guest_name_entry.get()
        cSurname = self.guest_surname_entry.get()
        cDob = self.guest_DOB_entry.get()
        cPayment_type = self.guest_payment_entry.get()
        cEmail = self.guest_email_entry.get()
        cPhoneNumber = self.guest_phone_entry.get()
        cAddress = self.guest_adress_entry.get()
        cPostcode = self.guest_postcode_entry.get()



        #creating a record of all the fields entered
        GuestRec = [cTitle,cFirstname,cSurname,cDob,cPayment_type,cEmail,cPhoneNumber,cAddress,cPostcode]

        cursor.execute("INSERT INTO tblGuest1 VALUES(Null,?,?,?,?,?,?,?,?,?)",GuestRec)

        connection.commit()
        connection.close()








        
        
        
      
    
    
        
def page():
    window=Tk()
    Main_menu(window)
    window.mainloop()

if __name__ == "__main__":
    page()
