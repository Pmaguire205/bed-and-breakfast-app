from tkinter import *
from tkinter import font
from PIL import ImageTk, Image #install pil
from tkmacosx import* # this is just the tkinter that works fully on mac 
import sqlite3
from tkinter import messagebox
from tkinter import scrolledtext
import re
from tkinter import ttk
import tkinter as tk
class Login_page:

    def __init__(self,window):
        #creating the window 
        self.window= window
        self.window.geometry("1000x700")
        self.window.title("Login screen")
        self.window.configure(bg = "white")
        #To zoom the page 
        self.window.state("zoomed")
        self.window.resizable(False,False)
 


        #logo image
        self.side_image = Image.open("Picture 1.png")
        photo1 = ImageTk.PhotoImage(self.side_image)
        self.panel= Label(self.window,image = photo1)
        self.panel.image = photo1
        self.panel.place(x=275, y=50)

        #Login frame for login details 
        self.login_frame = Frame(self.window, bg="white", width = 700, height= 500)
        self.login_frame.place(x=100, y=180)

        self.heading = Label(self.login_frame, text = "Log into your account", font = ("Arial Rounded MT",70), bg="white")
        self.heading.place(x=10,y=0)
        
        #Username labels 
        self.username = Label(self.login_frame, text = "Username", font = ("Avenir Next",30), bg="white")
        self.username.place(x=60,y=150)
        self.username_entry = Entry(self.login_frame,width = 30,bg = "#e2f0d9",highlightthickness = 0,font = ("Avenir Next",21),relief=FLAT)
        self.username_entry.place(x=225,y=155,height = 40)
        #password labels
        self.password = Label(self.login_frame, text = "Password", font = ("Avenir Next",30), bg="white")
        self.password.place(x=60,y=275)
        self.password_entry = Entry(self.login_frame,width = 30,font = ("Avenir Next",21),show = "*",bg = "#e2f0d9",highlightthickness = 0,relief=FLAT)
        self.password_entry.place(x=225,y=275,height = 40)



        # show/hide password button
        self.new_show_image = Image.open("show.png")
        self.show_image = self.new_show_image.resize((30,30))
        self.show_image1 = ImageTk.PhotoImage(self.show_image) 
        self.show_button_panel = Label(self.login_frame,image = self.show_image1,bg = "white")
        self.show_button_panel.image = self.show_image1
        self.show_button = Button(self.window, image = self.show_image1,bd=0,cursor = "hand2",highlightthickness = 0,command = self.show)
        self.show_button.place(x=725,y=455,width = 45,height = 40)

        self.new_hide_image = Image.open("hide.png")
        self.hide_image = self.new_hide_image.resize((30,30))
        self.hide_image1 = ImageTk.PhotoImage(self.hide_image) 
        self.hide_button_panel = Label(self.login_frame,image = self.hide_image1,bg = "white")
        self.hide_button_panel.image = self.hide_image1




        

        #right hand side image
        self.shape_image = Image.open("shape design.png")
        photo2 = ImageTk.PhotoImage(self.shape_image)
        self.panel2= Label(self.window,image = photo2)
        self.panel2.image = photo2
        self.panel2.place(x=950, y=0,height = 1000)
        #submit button
        self.submit_button =  Image.open("submit_button.png")
        photo3 = ImageTk.PhotoImage(self.submit_button)
        self.sb_label = Label(self.login_frame,image = photo3,bg = "white")
        self.sb_label.image= photo3

        
        self.sign_in = Button(self.login_frame, image = photo3,cursor = "hand2",command =self.submit,bg = "white",borderwidth = 0)
        self.sign_in.place(x=300,y=418,width = 200, height = 50)
        #forgot password button
        self.fp_button = Button(self.login_frame, text= "Forgot password",font = ("Avenir Next",15,"underline"),bd=0,cursor = "hand2",activebackground = "honeydew",bg="white",command = self.forgot_password)
        self.fp_button.place(x=450,y=250, width = 150, height = 20)
        

    def submit(self):
        username = self.username_entry.get()
        print(username)
        password = self.password_entry.get()
        print(password)
        self.window.destroy()
        window=Tk()
        Main_menu(window)
        

    def forgot_password(self):
        self.small_window = Toplevel()
        self.small_window.geometry("750x500")
        self.small_window.title("Forgot Password")
        self.small_window.configure(bg = "white")
        #To zoom the page 
        self.small_window.state("zoomed")
        self.small_window.resizable(True,True)

        #Background image
        background_image = Image.open("forgot_password background.png")
        bg1 = ImageTk.PhotoImage(background_image)
        bg_panel= Label(self.small_window,image = bg1)
        bg_panel.image = bg1
        bg_panel.pack(fill = "both", expand = "yes")

        

        #Frame for text
        fp_frame = Frame(self.small_window, bg = "white", width = 400, height= 500)
        fp_frame.place(x=180, y=0)

        fp_heading = Label(fp_frame, text = "Forgot Password?",font = ("Aharoni",30,"bold"),bg = "white")
        fp_heading.place(x=70,y=100)

        fp_username = Label(fp_frame, text="Username",font = ("Avenir Next",18), bg="white")
        fp_username.place(x=50,y=220)
        self.fp_username_entry = Entry(fp_frame,width = 30,bg = "#e2f0d9",highlightthickness = 0,font = ("Avenir Next",15),relief=FLAT)
        self.fp_username_entry.place(x=140,y=225,width = 200, height = 28)

        #Lock icon
        fp_lock = Image.open("lock.png")
        newfp_lock = fp_lock.resize((70,70))
        fp_photo = ImageTk.PhotoImage(newfp_lock)
        fp_panel1= Label(fp_frame,image = fp_photo,bg = "white")
        fp_panel1.image = fp_photo
        fp_panel1.place(x=160, y=20)

        #Submit icon
        fp_submit =  Image.open("fp_submit.png")
        new_fp_submit = fp_submit.resize((225,70)) 
        fp_photo1 = ImageTk.PhotoImage(new_fp_submit)
        fp_panel2 = Label(fp_frame,image = fp_photo1,bg = "white")
        fp_panel2.image= fp_photo1
        #Submit button
        fp_submit_button = Button(fp_frame,image = fp_photo1,bd=0,cursor = "hand2",highlightthickness = 0, command=self.security_question)
        fp_submit_button.place(x=100,y=358, width= 200,height = 40)
        #Back to login page button
        fp_loginpage = Button(fp_frame, text ="Back to login", font = ("Avenir Next",14,"underline"),bd=0,cursor = "hand2",bg="white",command = self.back_to_login)
        fp_loginpage.place(x= 140,y = 440,height = 20)

    def security_question(self):
        username = self.fp_username_entry.get()
        print(username)
        self.small_window.destroy()
        self.small_window1 = Toplevel()
        self.small_window1.geometry("750x500")
        self.small_window1.title("Security Question")
        self.small_window1.configure(bg = "white")
        #To zoom the page 
        self.small_window1.state("zoomed")
        self.small_window1.resizable(True,True)

        #Background image
        background_image = Image.open("forgot_password background.png")
        bg1 = ImageTk.PhotoImage(background_image)
        bg_panel= Label(self.small_window1,image = bg1)
        bg_panel.image = bg1
        bg_panel.pack(fill = "both", expand = "yes")

        

        #Frame for text
        fp_frame = Frame(self.small_window1, bg = "white", width = 400, height= 500)
        fp_frame.place(x=180, y=0)

        fp_heading = Label(fp_frame, text = "Reset Password?",font = ("Aharoni",30,"bold"),bg = "white")
        fp_heading.place(x=70,y=100)


        fp_security_question = Label(fp_frame, text="What was your first pet’s name?",font = ("Avenir Next",18), bg="white")
        fp_security_question.place(x=60,y=180)
        fp_security_question_entry = Entry(fp_frame,width = 30,bg = "#e2f0d9",highlightthickness = 0,font = ("Avenir Next",15),relief=FLAT)
        fp_security_question_entry.place(x=45,y=245,width = 300, height = 28)

        #Lock icon
        fp_lock = Image.open("lock.png")
        newfp_lock = fp_lock.resize((70,70))
        fp_photo = ImageTk.PhotoImage(newfp_lock)
        fp_panel1= Label(fp_frame,image = fp_photo,bg = "white")
        fp_panel1.image = fp_photo
        fp_panel1.place(x=160, y=20)

        #Submit icon
        fp_submit =  Image.open("fp_submit.png")
        new_fp_submit = fp_submit.resize((225,70)) 
        fp_photo1 = ImageTk.PhotoImage(new_fp_submit)
        fp_panel2 = Label(fp_frame,image = fp_photo1,bg = "white")
        fp_panel2.image= fp_photo1
        #Submit button
        fp_submit_button = Button(fp_frame,image = fp_photo1,bd=0,cursor = "hand2",highlightthickness = 0, command = self.change_password)
        fp_submit_button.place(x=100,y=358, width= 200,height = 40)
        #Back to login page button
        fp_loginpage = Button(fp_frame, text ="Back to login", font = ("Avenir Next",14,"underline"),bd=0,cursor = "hand2",bg="white",command = self.back_to_login1)
        fp_loginpage.place(x= 140,y = 440,height = 20)



    def change_password(self):
        self.small_window1.destroy()
        self.small_window2 = Toplevel()
        self.small_window2.geometry("750x500")
        self.small_window2.title("Security Question")
        self.small_window2.configure(bg = "white")
        #To zoom the page 
        self.small_window2.state("zoomed")
        self.small_window2.resizable(True,True)

        #Background image
        background_image = Image.open("forgot_password background.png")
        bg1 = ImageTk.PhotoImage(background_image)
        bg_panel= Label(self.small_window2,image = bg1)
        bg_panel.image = bg1
        bg_panel.pack(fill = "both", expand = "yes")

        

        #Frame for text
        fp_frame = Frame(self.small_window2, bg = "white", width = 400, height= 500)
        fp_frame.place(x=180, y=0)

        fp_heading = Label(fp_frame, text = "Password reset?",font = ("Aharoni",30,"bold"),bg = "white")
        fp_heading.place(x=70,y=100)


        self.fp_password = Label(fp_frame, text="Password",font = ("Avenir Next",16), bg="white")
        self.fp_password.place(x=60,y=180)
        self.fp_password_entry = Entry(fp_frame,width = 30,bg = "#e2f0d9",highlightthickness = 0,font = ("Avenir Next",15),relief=FLAT,show = "")
        self.fp_password_entry.place(x=150,y=180,width = 200, height = 28)

        self.fp_password_confirm = Label(fp_frame, text="Confirm Password",font = ("Avenir Next",16), bg="white")
        self.fp_password_confirm.place(x=0,y=250)
        self.fp_password_confirm_entry = Entry(fp_frame,width = 30,bg = "#e2f0d9",highlightthickness = 0,font = ("Avenir Next",15),relief=FLAT,show = "*")
        self.fp_password_confirm_entry.place(x=150,y=250,width = 200, height = 28)

        #Unlock icon
        fp_lock = Image.open("unlock.png")
        newfp_lock = fp_lock.resize((70,70))
        fp_photo = ImageTk.PhotoImage(newfp_lock)
        fp_panel1= Label(fp_frame,image = fp_photo,bg = "white")
        fp_panel1.image = fp_photo
        fp_panel1.place(x=160, y=20)

        #Submit icon
        fp_submit =  Image.open("fp_submit.png")
        new_fp_submit = fp_submit.resize((225,70)) 
        fp_photo1 = ImageTk.PhotoImage(new_fp_submit)
        fp_panel2 = Label(fp_frame,image = fp_photo1,bg = "white")
        fp_panel2.image= fp_photo1
        #Submit button
        fp_submit_button = Button(fp_frame,image = fp_photo1,bd=0,cursor = "hand2",highlightthickness = 0,command=self.cp_submit )
        fp_submit_button.place(x=100,y=358, width= 200,height = 40)
        #Back to login page button
        fp_loginpage = Button(fp_frame, text ="Back to login", font = ("Avenir Next",14,"underline"),bd=0,cursor = "hand2",bg="white",command = self.back_to_login2)
        fp_loginpage.place(x= 140,y = 440,height = 20)

#this is the show/hide button of the password entry in the login page
    def show(self):
        self.hide_button = Button(self.window, image = self.hide_image1,bd=0,cursor = "hand2",highlightthickness = 0,command = self.hide)
        self.hide_button.place(x=725,y=455,width = 45,height = 40)
        self.password_entry.config(show="")
    def hide(self):
        self.show_button = Button(self.window, image = self.show_image1,bd=0,cursor = "hand2",highlightthickness = 0,command = self.show)
        self.show_button.place(x=725,y=455,width = 45,height = 40)
        self.password_entry.config(show="*")

## this is the back to login for the forgot password page 
    def back_to_login(self):
        self.small_window.destroy()
## this is the back to login page for the security question page 
    def back_to_login1(self):
        self.small_window1.destroy()
## this is the back to login page for the chnage password page
    def back_to_login2(self):
        self.small_window2.destroy()
## this is the submnit button for the change password page
    def cp_submit(self):
        if self.fp_password_entry.get() == self.fp_password_confirm_entry.get():
            print(self.fp_password_entry.get())
            self.small_window2.destroy()
        else:
            print("the passwords does not match up")


class Main_menu:
    
    def __init__(self,window): #
        #creating the window 
        self.mm_window= window
        self.mm_window.geometry("1400x850")
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

        #Guest button
        self.guest_icon =  Image.open("Guests_icon.png")
        self.guest_icon_resize = self.guest_icon.resize((70,70))
        self.guest_icon = self.guest_icon_resize 
        guest_icon_photo = ImageTk.PhotoImage(self.guest_icon)
        self.gb_label = Label(self.mm_window,image =guest_icon_photo ,bg = "white")
        self.gb_label.image= guest_icon_photo
        self.guest_button = Button(self.mm_window, image = guest_icon_photo ,command=self.guest_files,cursor = "hand2",bg = "#c4dfb4",borderwidth = 0)
        self.guest_button.place(x=1300,y=550,width = 80, height = 80)

        guest_icon_heading = Label(self.mm_window, text = "Guests",font = ("Avenir Next",15),bg = "#c4dfb4")
        guest_icon_heading.place(x=1300,y=630,width = 80)


        #Rooms button
        self.room_icon =  Image.open("rooms_icon.png")
        self.room_icon_resize = self.room_icon.resize((70,70))
        self.room_icon = self.room_icon_resize 
        room_icon_photo = ImageTk.PhotoImage(self.room_icon)
        self.rb_label = Label(self.mm_window,image =room_icon_photo ,bg = "#c4dfb4")
        self.rb_label.image= room_icon_photo
        self.room_button = Button(self.mm_window, image = room_icon_photo ,command=self.guest_files,cursor = "hand2",bg = "#c4dfb4",borderwidth = 0)
        self.room_button.place(x=1200,y=550,width = 80, height = 80)

        room_icon_heading = Label(self.mm_window, text = "Rooms",font = ("Avenir Next",15),bg = "#c4dfb4")
        room_icon_heading.place(x=1200,y=630,width = 80)

        #Menu button
        self.menu_icon =  Image.open("menu_icon.png")
        self.menu_icon_resize = self.menu_icon.resize((70,70))
        self.menu_icon = self.menu_icon_resize 
        menu_icon_photo = ImageTk.PhotoImage(self.menu_icon)
        self.mb_label = Label(self.mm_window,image =menu_icon_photo ,bg = "white")
        self.mb_label.image= menu_icon_photo
        self.menu_button = Button(self.mm_window, image = menu_icon_photo ,cursor = "hand2",bg = "#c4dfb4",borderwidth = 0)
        self.menu_button.place(x=1100,y=550,width = 80, height = 80)

        menu_icon_heading = Label(self.mm_window, text = "Menu",font = ("Avenir Next",15),bg = "#c4dfb4")
        menu_icon_heading.place(x=1120,y=630,width = 40)

        #Staff button
        self.staff_icon =  Image.open("staff_icon.png")
        self.staff_icon_resize = self.staff_icon.resize((70,70))
        self.staff_icon = self.staff_icon_resize 
        staff_icon_photo = ImageTk.PhotoImage(self.staff_icon)
        self.sb_label = Label(self.mm_window,image =staff_icon_photo ,bg = "#a8d18e")
        self.sb_label.image= staff_icon_photo
        self.staff_button = Button(self.mm_window, image = staff_icon_photo ,command=self.guest_files,cursor = "hand2",bg = "#c4dfb4",borderwidth = 0)
        self.staff_button.place(x=1000,y=550,width = 80, height = 80)
        staff_icon_heading = Label(self.mm_window, text = "Rooms",font = ("Avenir Next",15),bg = "#a8d18e")
        staff_icon_heading.place(x=1000,y=630,width = 80)

        ##      User icon

        self.guest_icon = Image.open("add_user_icon.png")
        self.guest_icon_resize = self.guest_icon.resize((175,175))
        self.guest_icon = self.guest_icon_resize
        self.guest_icon_photo = ImageTk.PhotoImage(self.guest_icon)
        self.gi_label = Label(self.mm_window,image =self.guest_icon_photo ,bg = "#a8d18e")
        self.gi_label.image = self.guest_icon_photo
        self.gi_label.place(x=1100,y=225)

##      main menu heading
        self.main_menu_heading = Image.open("main menu heading.png")
        self.main_menu_heading_resize = self.main_menu_heading.resize((400,75))
        self.main_menu_heading = self.main_menu_heading_resize
        self.mmh_photo = ImageTk.PhotoImage(self.main_menu_heading)
        self.mmh_label= Label(self.mm_window,image = self.mmh_photo,bg = "white")
        self.mmh_label.image = self.mmh_photo
        self.mmh_label.place(x=150, y=0)
##      notice board heading
        self.notice_board_heading = Label(self.mm_window,text = "Notice Board", font = ("Avenir Next",30,"bold"),bg ="white",highlightthickness = 0)
        self.notice_board_heading.place(x=250,y=120)
##      notice board image
        self.notice_board = Image.open("notice board.png")
        self.notice_board_resize = self.notice_board.resize((700,450))
        self.notice_board = self.notice_board_resize
        self.mmnb_photo = ImageTk.PhotoImage(self.notice_board)
        self.mmnb_label= Label(self.mm_window,image = self.mmnb_photo,bg = "white")
        self.mmnb_label.image = self.mmnb_photo
        self.mmnb_label.place(x=100, y=200)
        

    def guest_files(self): #ask why when I pen 
        self.mm_window.destroy()
        self.gf_window= Tk()
        self.gf_window.geometry("1400x850")
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
        
##      Search heading
        self.search_heading = Label(self.gf_window, text = "Search", font = ("Aharoni",60,"bold"),bg = "white")
        self.search_heading.place(x=350, y=150)

##      Search icon

        self.search_icon = Image.open("search icon.png")
        self.search_icon_resize = self.search_icon.resize((45,45))
        self.search_icon = self.search_icon_resize
        self.search_icon_photo = ImageTk.PhotoImage(self.search_icon)
        self.si_label = Label(self.gf_window,image =self.search_icon_photo ,bg = "white")
        self.si_label.image = self.search_icon_photo
        self.si_label.place(x=600,y=167)

        #Frame for search entry  
        self.search_frame = Frame(self.gf_window, bg="#e2f0d9", width = 850, height= 550)
        self.search_frame.place(x=20, y=400)

        #Frame for search entry2 
        self.search_frame2 = Frame(self.gf_window, bg="white", width = 600, height= 100)
        self.search_frame2.place(x=170, y=250)

##      guest record heading 
        self.guest_heading_image = Image.open("Guest records.png")
        self.guest_heading_image_resize = self.guest_heading_image.resize((300,75))
        self.guest_heading_image = self.guest_heading_image_resize
        photo_guest_heading = ImageTk.PhotoImage(self.guest_heading_image)
        self.guest_label = Label(self.gf_window,image = photo_guest_heading)
        self.guest_label.image = photo_guest_heading
        self.guest_label.place(x=150, y=0,height = 75)


##      User icon

        self.guest_icon = Image.open("add_user_icon.png")
        self.guest_icon_resize = self.guest_icon.resize((175,175))
        self.guest_icon = self.guest_icon_resize
        self.guest_icon_photo = ImageTk.PhotoImage(self.guest_icon)
        self.gi_label = Label(self.gf_window,image =self.guest_icon_photo ,bg = "#a8d18e")
        self.gi_label.image = self.guest_icon_photo
        self.gi_label.place(x=1100,y=225)


##      Save button
        self.save_guest_icon = Image.open("save_icon.png")
        self.save_guest_icon_resize = self.save_guest_icon.resize((75,75))
        self.save_guest_icon = self.save_guest_icon_resize
        self.save_guest_photo = ImageTk.PhotoImage(self.save_guest_icon)
        self.sg_label = Label(self.gf_window,image =self.save_guest_photo ,bg = "#c4dfb4")
        self.sg_label.image = self.save_guest_photo
        self.sg_button = Button(self.gf_window, image = self.save_guest_photo,command = self.guest_add,cursor = "hand2",bg = "#c4dfb4",borderwidth = 0)
        self.sg_button.place(x=1125, y=500)

        self.sg_heading = Label(self.gf_window, text = "Add", font = ("Avenir Next",20),bg = "#c4dfb4")
        self.sg_heading.place(x=1160, y= 585)

##      Edit button
        self.edit_guest_icon = Image.open("edit icon.png")
        self.edit_guest_icon_resize = self.edit_guest_icon.resize((75,75))
        self.edit_guest_icon = self.edit_guest_icon_resize
        self.edit_guest_photo = ImageTk.PhotoImage(self.edit_guest_icon)
        self.eg_label = Label(self.gf_window,image =self.edit_guest_photo ,bg = "#a8d18e")
        self.eg_label.image = self.edit_guest_photo
        self.edit_button = Button(self.gf_window,command = self.guest_edit,image = self.edit_guest_photo,cursor = "hand2",bg = "#a8d18e",borderwidth = 0)
        self.edit_button.place(x=975,y=500)

        self.eg_heading = Label(self.gf_window, text = "Edit", font = ("Avenir Next",20),bg = "#a8d18e")
        self.eg_heading.place(x=1010, y= 585)

##      delete button
        self.delete_guest_icon = Image.open("delete icon.png")
        self.delete_guest_icon_resize = self.delete_guest_icon.resize((75,75))
        self.delete_guest_icon = self.delete_guest_icon_resize
        self.delete_guest_photo = ImageTk.PhotoImage(self.delete_guest_icon)
        self.dg_label = Label(self.gf_window,image =self.delete_guest_photo ,bg = "#c4dfb4")
        self.dg_label.image = self.delete_guest_photo
        self.delete_button = Button(self.gf_window,image = self.delete_guest_photo,cursor = "hand2",bg = "#c4dfb4",borderwidth = 0)
        self.delete_button.place(x=1275,y=500)

        self.dg_heading = Label(self.gf_window, text = "Delete", font = ("Avenir Next",20),bg = "#c4dfb4")
        self.dg_heading.place(x=1310, y= 585)

        ##      Back button
        self.back_icon = Image.open("back icon.png")
        self.back_icon_resize = self.back_icon.resize((225,80))
        self.back_icon = self.back_icon_resize
        self.back_photo = ImageTk.PhotoImage(self.back_icon)
        self.back_label = Label(self.gf_window,image =self.back_photo ,bg = "#e2f0d9")
        self.back_label.image = self.back_photo
        self.back_button = Button(self.gf_window,image = self.back_photo,command = self.back_search_guess,cursor = "hand2",bg = "white",borderwidth = 0)
        self.back_button.place(x=1082,y=640,width = 200, height = 62)
        
        def SearchCustomer():
            #removing records currently displayed
            
            global frame_details
            frame_details.destroy()

            #creating frame for the new records found in database
            frame_details = Frame(self.search_frame)
            frame_details.grid(row=2, column=0, columnspan=2, padx=25, pady=10)


            
            searchData = search.get()
            connection = sqlite3.connect("Guestrecord.db")
            cursor = connection.cursor()

            cursor.execute("SELECT * FROM tb1Guest1 WHERE guestFirstname=?", [searchData])
            searchResults = cursor.fetchone()
            if searchResults != None:
                n = 1
                for row in cursor.execute("SELECT * FROM tb1Guest1 WHERE guestFirstname= ?", [searchData]):
                     c = 0        
                     for item in row:
                         Label(frame_details,bg = "white", text=str(item),font=("Avenir Next",12),width=11).grid(row=n,column=c, padx=0, pady=1)
                         c = c+1
                n = n +1
            else:
                Label(frame_details,bg = "white" ,text="No results matching the search criteria", font=("Avenir Next", 14)).grid(row = 0, column=1, columnspan=4)

            connection.commit()
            connection.close()
        global frame_details

##        #Creating a frame for the heading section - this will span over the entire window
##        frame_heading = Frame(self.search_frame2,bg="#e2f0d9",)
##        frame_heading.grid(row=0, column=0, columnspan=2, padx=50, pady=50)

        #Creating a frame for  the data entry, this will be used for labels and text boxes
        frame_headings = Frame(self.search_frame)
        frame_headings.grid(row=1, column=0, columnspan=2, padx=25, pady=10)

        my_scrollbar = Scrollbar(self.search_frame)
        my_scrollbar.grid(row=2,column=2)
        

        frame_details = Canvas(self.search_frame)

        frame_details.grid(row=2, column=0, padx=25, pady=10)
        


        
        #create frame for buttons
        frame_buttons = Frame(self.search_frame)
        frame_buttons.grid(row = 3, column=0, columnspan=1, padx=60,pady=5)




        #Inserting a label into the top frame

        First_name_heading = Label(self.search_frame2,bg = "white", text = "First Name", font=("Avenir Next",20))
        First_name_heading.place(x=20, y=40)
        
    ##      Search icon

        search_icon = Image.open("search icon.png")
        search_icon_resize = search_icon.resize((20,20))
        search_icon = search_icon_resize
        search_icon_photo = ImageTk.PhotoImage(search_icon)


        search = Entry(self.search_frame2, width=30,bg="#e2f0d9",font=("Avenir Next",18),highlightthickness = 0,relief=FLAT)
        search.place(x = 140, y =40)
        searchButton = Button(self.search_frame2, image=search_icon_photo,height = 35, width =35, command=SearchCustomer,bg ="white")
        searchButton.place(x= 500, y = 38)

    ##Labels for the headings of data to be displayed from database
        Label(frame_headings, text="GuestID",font=("Avenir Next",12), width = 11,bg = "white").grid(row=0,column=0, padx=0, pady=1)   
        Label(frame_headings, text="Title",font=("Avenir Next",12), width = 11,bg = "white").grid(row=0,column=1, padx=0, pady=1)
        Label(frame_headings, text="FirstName",font=("Avenir Next",12), width =11,bg = "white").grid(row=0, column=2,padx=0,pady=1)
        Label(frame_headings, text="Surname",font=("Avenir Next",12), width = 11,bg = "white").grid(row=0, column=3,padx=0,pady=1)
        Label(frame_headings, text="DOB",font=("Avenir Next",12), width = 11,bg = "white").grid(row=0, column=4,padx=0,pady=1)
        Label(frame_headings, text="Payment",font=("Avenir Next",12), width = 11,bg = "white").grid(row=0, column=5,padx=0,pady=1)
        Label(frame_headings, text="Email",font=("Avenir Next",12), width = 11,bg = "white").grid(row=0, column=6,padx=0,pady=1)
        Label(frame_headings, text="PhoneNumber",font=("Avenir Next",12), width = 11,bg = "white").grid(row=0, column=7,padx=0,pady=1)
        Label(frame_headings, text="Address",font=("Avenir Next",12), width = 11,bg = "white").grid(row=0, column=8,padx=0,pady=1)
        Label(frame_headings, text="Postcode",font=("Avenir Next",12), width = 11,bg = "white").grid(row=0, column=9,padx=0,pady=1)


        #Returning all data for customers from the database and displaying under the relevant heading
        connection = sqlite3.connect("Guestrecord.db")
        cursor = connection.cursor()
        n = 0
        for x in cursor.execute("SELECT * FROM tb1Guest1"):
            c = 0
            for item in x:
                Label(frame_details,bg = "white", text=str(item),font=("Avenir Next",12),width=11).grid(row=n,column=c, padx=0, pady=1)
                c = c+1
            n = n + 1
        connection.commit()
        connection.close()


    def guest_add(self):
        try:
            self.gf_window.destroy()
        except:
            print("nothing")
        try:
            self.ge_window.destroy()
        except:
            print("nothing")
        self.ga_window= Tk()
        self.ga_window.geometry("1400x850")
        self.ga_window.title("Add New Guests")
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
        self.new_guest_frame.place(x=100, y=150)

##      GuestID
        self.guest_ID = Label(self.new_guest_frame, text = "GuestID:", font = ("Avenir Next",20,"bold"), bg="white")
        self.guest_ID.place(x=40,y=15)
        self.guest_ID_entry = Entry(self.new_guest_frame,width = 15,bg = "#e2f0d9",highlightthickness = 0,font = ("Avenir Next",20),relief=FLAT)
        self.guest_ID_entry.place(x=155,y=20,height = 25)
          
        #Name of guest  
        self.guest_name = Label(self.new_guest_frame, text = "First Name:", font = ("Avenir Next",20,"bold"), bg="white")
        self.guest_name.place(x=40,y=115)
        self.guest_name_entry = Entry(self.new_guest_frame,width = 50,bg = "#e2f0d9",highlightthickness = 0,font = ("Avenir Next",20),relief=FLAT)
        self.guest_name_entry.place(x=160,y=120,height = 25)
          
        self.guest_surname = Label(self.new_guest_frame, text = "Surname:", font = ("Avenir Next",20,"bold"), bg="white")
        self.guest_surname.place(x=40,y=165)
        self.guest_surname_entry = Entry(self.new_guest_frame,width = 50,bg = "#e2f0d9",highlightthickness = 0,font = ("Avenir Next",20),relief=FLAT)
        self.guest_surname_entry.place(x=160,y=170,height = 25)

##      title
        self.guest_title = Label(self.new_guest_frame, text = "Title:", font = ("Avenir Next",20,"bold"), bg="white")
        self.guest_title.place(x=40,y=215)
        self.guest_title_entry = Entry(self.new_guest_frame,width = 50,bg = "#e2f0d9",highlightthickness = 0,font = ("Avenir Next",20),relief=FLAT)
        self.guest_title_entry.place(x=160,y=220,height = 25)
##      Date of birth
        self.guest_DOB = Label(self.new_guest_frame, text = "DOB:", font = ("Avenir Next",20,"bold"), bg="white")
        self.guest_DOB.place(x=40,y=265)
        self.guest_DOB_entry = Entry(self.new_guest_frame,width = 50,bg = "#e2f0d9",highlightthickness = 0,font = ("Avenir Next",20),relief=FLAT)
        self.guest_DOB_entry.place(x=160,y=270,height = 25)
##      Payment type
        self.guest_payment = Label(self.new_guest_frame, text = "Payment:", font = ("Avenir Next",20,"bold"), bg="white")
        self.guest_payment.place(x=40,y=315)
        self.guest_payment_entry = Entry(self.new_guest_frame,width = 50,bg = "#e2f0d9",highlightthickness = 0,font = ("Avenir Next",20),relief=FLAT)
        self.guest_payment_entry.place(x=160,y=320,height = 25)
##      Email
        self.guest_email = Label(self.new_guest_frame, text = "Email:", font = ("Avenir Next",20,"bold"), bg="white")
        self.guest_email.place(x=40,y=365)
        self.guest_email_entry = Entry(self.new_guest_frame,width = 50,bg = "#e2f0d9",highlightthickness = 0,font = ("Avenir Next",20),relief=FLAT)
        self.guest_email_entry.place(x=160,y=370,height = 25)
##      PhoneNumber
        self.guest_phone = Label(self.new_guest_frame, text = "Phone No:", font = ("Avenir Next",20,"bold"), bg="white")
        self.guest_phone.place(x=40,y=415)
        self.guest_phone_entry = Entry(self.new_guest_frame,width = 50,bg = "#e2f0d9",highlightthickness = 0,font = ("Avenir Next",20),relief=FLAT)
        self.guest_phone_entry.place(x=160,y=420,height = 25)
##      Adress
        self.guest_adress = Label(self.new_guest_frame, text = "Address:", font = ("Avenir Next",20,"bold"), bg="white")
        self.guest_adress.place(x=40,y=465)
        self.guest_adress_entry = Entry(self.new_guest_frame,width = 50,bg = "#e2f0d9",highlightthickness = 0,font = ("Avenir Next",20),relief=FLAT)
        self.guest_adress_entry.place(x=160,y=470,height = 25)
##      Postcode
        self.guest_postcode = Label(self.new_guest_frame, text = "Postcode:", font = ("Avenir Next",20,"bold"), bg="white")
        self.guest_postcode.place(x=40,y=515)
        self.guest_postcode_entry = Entry(self.new_guest_frame,width = 50,bg = "#e2f0d9",highlightthickness = 0,font = ("Avenir Next",20),relief=FLAT)
        self.guest_postcode_entry.place(x=160,y=520,height = 25)

##      Save button
        self.save_guest_icon = Image.open("save_icon.png")
        self.save_guest_icon_resize = self.save_guest_icon.resize((75,75))
        self.save_guest_icon = self.save_guest_icon_resize
        self.save_guest_photo = ImageTk.PhotoImage(self.save_guest_icon)
        self.sg_label = Label(self.ga_window,image =self.save_guest_photo ,bg = "#e2f0d9")
        self.sg_label.image = self.save_guest_photo
        self.sg_button = Button(self.ga_window, image = self.save_guest_photo,command = self.save,cursor = "hand2",bg = "white",borderwidth = 0)
        self.sg_button.place(x=1125, y=500)

        self.sg_heading = Label(self.ga_window, text = "Add", font = ("Avenir Next",20),bg = "#c4dfb4")
        self.sg_heading.place(x=1160, y= 585)

##      Edit button
        self.edit_guest_icon = Image.open("edit icon.png")
        self.edit_guest_icon_resize = self.edit_guest_icon.resize((75,75))
        self.edit_guest_icon = self.edit_guest_icon_resize
        self.edit_guest_photo = ImageTk.PhotoImage(self.edit_guest_icon)
        self.eg_label = Label(self.ga_window,image =self.edit_guest_photo ,bg = "#a8d18e")
        self.eg_label.image = self.edit_guest_photo
        self.edit_button = Button(self.ga_window,command = self.guest_edit,image = self.edit_guest_photo,cursor = "hand2",bg = "white",borderwidth = 0)
        self.edit_button.place(x=975,y=500)

        self.eg_heading = Label(self.ga_window, text = "Edit", font = ("Avenir Next",20),bg = "#a8d18e")
        self.eg_heading.place(x=1010, y= 585)
        
##      delete button
        self.delete_guest_icon = Image.open("delete icon.png")
        self.delete_guest_icon_resize = self.delete_guest_icon.resize((75,75))
        self.delete_guest_icon = self.delete_guest_icon_resize
        self.delete_guest_photo = ImageTk.PhotoImage(self.delete_guest_icon)
        self.dg_label = Label(self.ga_window,image =self.delete_guest_photo ,bg = "#e2f0d9")
        self.dg_label.image = self.delete_guest_photo
        self.delete_button = Button(self.ga_window,image = self.delete_guest_photo,cursor = "hand2",bg = "white",borderwidth = 0,command = self.DeleteGuest)
        self.delete_button.place(x=1275,y=500)

        self.dg_heading = Label(self.ga_window, text = "Delete", font = ("Avenir Next",20),bg = "#c4dfb4")
        self.dg_heading.place(x=1310, y= 585)

##      Back button
        self.back_icon = Image.open("back icon.png")
        self.back_icon_resize = self.back_icon.resize((175,62))
        self.back_icon = self.back_icon_resize
        self.back_photo = ImageTk.PhotoImage(self.back_icon)
        self.back_label = Label(self.ga_window,image =self.back_photo ,bg = "#e2f0d9")
        self.back_label.image = self.back_photo
        self.back_button = Button(self.ga_window,image = self.back_photo,command = self.back_add_guess,cursor = "hand2",bg = "white",borderwidth = 0)
        self.back_button.place(x=1082,y=640,width = 200, height = 62)


##      User icon

        self.guest_icon = Image.open("user icon.png")
        self.guest_icon_resize = self.guest_icon.resize((175,175))
        self.guest_icon = self.guest_icon_resize
        self.guest_icon_photo = ImageTk.PhotoImage(self.guest_icon)
        self.gi_label = Label(self.ga_window,image =self.guest_icon_photo ,bg = "#a8d18e")
        self.gi_label.image = self.guest_icon_photo
        self.gi_label.place(x=1100,y=225)

    def guest_edit(self):
        try:
            self.gf_window.destroy()
        except:
            print("nothing")
        try:
            self.ga_window.destroy()
        except:
            print("nothing")

        self.ge_window= Tk()
        self.ge_window.geometry("1400x850")
        self.ge_window.title("Edit Guests")
        self.ge_window.configure(bg = "white")
        #To zoom the page 
        self.ge_window.state("zoomed")
        self.ge_window.resizable(0,0)

        #right hand side image
        shape_image1 = Image.open("shape design.png")
        photo2 = ImageTk.PhotoImage(shape_image1)
        label2= Label(self.ge_window,image = photo2)
        label2.image = photo2
        label2.place(x=950, y=0,height = 1000)
        
##      New guest record heading 
        self.guest_heading_image = Image.open("Guest records heading.png")
        self.guest_heading_image_resize = self.guest_heading_image.resize((400,75))
        self.guest_heading_image = self.guest_heading_image_resize
        photo_guest_heading = ImageTk.PhotoImage(self.guest_heading_image)
        self.guest_label = Label(self.ge_window,image = photo_guest_heading)
        self.guest_label.image = photo_guest_heading
        self.guest_label.place(x=150, y=0,height = 75)

        #Frame for entry details for new guest 
        self.new_guest_frame = Frame(self.ge_window, bg="white", width = 700, height= 700)
        self.new_guest_frame.place(x=100, y=150)

##      GuestID
        self.guest_ID = Label(self.new_guest_frame, text = "GuestID:", font = ("Avenir Next",20,"bold"), bg="white")
        self.guest_ID.place(x=40,y=15)
        self.guest_ID_entry = Entry(self.new_guest_frame,width = 15,bg = "#e2f0d9",highlightthickness = 0,font = ("Avenir Next",20),relief=FLAT)
        self.guest_ID_entry.place(x=155,y=20,height = 25)
          
        #Name of guest  
        self.guest_name = Label(self.new_guest_frame, text = "First Name:", font = ("Avenir Next",20,"bold"), bg="white")
        self.guest_name.place(x=40,y=115)
        self.guest_name_entry = Entry(self.new_guest_frame,width = 50,bg = "#e2f0d9",highlightthickness = 0,font = ("Avenir Next",20),relief=FLAT)
        self.guest_name_entry.place(x=160,y=120,height = 25)
          
        self.guest_surname = Label(self.new_guest_frame, text = "Surname:", font = ("Avenir Next",20,"bold"), bg="white")
        self.guest_surname.place(x=40,y=165)
        self.guest_surname_entry = Entry(self.new_guest_frame,width = 50,bg = "#e2f0d9",highlightthickness = 0,font = ("Avenir Next",20),relief=FLAT)
        self.guest_surname_entry.place(x=160,y=170,height = 25)

##      title
        self.guest_title = Label(self.new_guest_frame, text = "Title:", font = ("Avenir Next",20,"bold"), bg="white")
        self.guest_title.place(x=40,y=215)
        self.guest_title_entry = Entry(self.new_guest_frame,width = 50,bg = "#e2f0d9",highlightthickness = 0,font = ("Avenir Next",20),relief=FLAT)
        self.guest_title_entry.place(x=160,y=220,height = 25)
##      Date of birth
        self.guest_DOB = Label(self.new_guest_frame, text = "DOB:", font = ("Avenir Next",20,"bold"), bg="white")
        self.guest_DOB.place(x=40,y=265)
        self.guest_DOB_entry = Entry(self.new_guest_frame,width = 50,bg = "#e2f0d9",highlightthickness = 0,font = ("Avenir Next",20),relief=FLAT)
        self.guest_DOB_entry.place(x=160,y=270,height = 25)
##      Payment type
        self.guest_payment = Label(self.new_guest_frame, text = "Payment:", font = ("Avenir Next",20,"bold"), bg="white")
        self.guest_payment.place(x=40,y=315)
        self.guest_payment_entry = Entry(self.new_guest_frame,width = 50,bg = "#e2f0d9",highlightthickness = 0,font = ("Avenir Next",20),relief=FLAT)
        self.guest_payment_entry.place(x=160,y=320,height = 25)
##      Email
        self.guest_email = Label(self.new_guest_frame, text = "Email:", font = ("Avenir Next",20,"bold"), bg="white")
        self.guest_email.place(x=40,y=365)
        self.guest_email_entry = Entry(self.new_guest_frame,width = 50,bg = "#e2f0d9",highlightthickness = 0,font = ("Avenir Next",20),relief=FLAT)
        self.guest_email_entry.place(x=160,y=370,height = 25)
##      PhoneNumber
        self.guest_phone = Label(self.new_guest_frame, text = "Phone No:", font = ("Avenir Next",20,"bold"), bg="white")
        self.guest_phone.place(x=40,y=415)
        self.guest_phone_entry = Entry(self.new_guest_frame,width = 50,bg = "#e2f0d9",highlightthickness = 0,font = ("Avenir Next",20),relief=FLAT)
        self.guest_phone_entry.place(x=160,y=420,height = 25)
##      Adress
        self.guest_adress = Label(self.new_guest_frame, text = "Address:", font = ("Avenir Next",20,"bold"), bg="white")
        self.guest_adress.place(x=40,y=465)
        self.guest_adress_entry = Entry(self.new_guest_frame,width = 50,bg = "#e2f0d9",highlightthickness = 0,font = ("Avenir Next",20),relief=FLAT)
        self.guest_adress_entry.place(x=160,y=470,height = 25)
##      Postcode
        self.guest_postcode = Label(self.new_guest_frame, text = "Postcode:", font = ("Avenir Next",20,"bold"), bg="white")
        self.guest_postcode.place(x=40,y=515)
        self.guest_postcode_entry = Entry(self.new_guest_frame,width = 50,bg = "#e2f0d9",highlightthickness = 0,font = ("Avenir Next",20),relief=FLAT)
        self.guest_postcode_entry.place(x=160,y=520,height = 25)

##      Save button
        self.save_guest_icon = Image.open("save_icon.png")
        self.save_guest_icon_resize = self.save_guest_icon.resize((75,75))
        self.save_guest_icon = self.save_guest_icon_resize
        self.save_guest_photo = ImageTk.PhotoImage(self.save_guest_icon)
        self.sg_label = Label(self.ge_window,image =self.save_guest_photo ,bg = "#e2f0d9")
        self.sg_label.image = self.save_guest_photo
        self.sg_button = Button(self.ge_window, image = self.save_guest_photo,command = self.guest_add,cursor = "hand2",bg = "white",borderwidth = 0)
        self.sg_button.place(x=1125, y=500)

        self.sg_heading = Label(self.ge_window, text = "Add", font = ("Avenir Next",20),bg = "#c4dfb4")
        self.sg_heading.place(x=1160, y= 585)

##      Edit button
        self.edit_guest_icon = Image.open("edit icon.png")
        self.edit_guest_icon_resize = self.edit_guest_icon.resize((75,75))
        self.edit_guest_icon = self.edit_guest_icon_resize
        self.edit_guest_photo = ImageTk.PhotoImage(self.edit_guest_icon)
        self.eg_label = Label(self.ge_window,image =self.edit_guest_photo ,bg = "#a8d18e")
        self.eg_label.image = self.edit_guest_photo
        self.edit_button = Button(self.ge_window,command = self.edit,image = self.edit_guest_photo,cursor = "hand2",bg = "white",borderwidth = 0)
        self.edit_button.place(x=975,y=500)

        self.eg_heading = Label(self.ge_window, text = "Edit", font = ("Avenir Next",20),bg = "#a8d18e")
        self.eg_heading.place(x=1010, y= 585)
        
##      delete button
        self.delete_guest_icon = Image.open("delete icon.png")
        self.delete_guest_icon_resize = self.delete_guest_icon.resize((75,75))
        self.delete_guest_icon = self.delete_guest_icon_resize
        self.delete_guest_photo = ImageTk.PhotoImage(self.delete_guest_icon)
        self.dg_label = Label(self.ge_window,image =self.delete_guest_photo ,bg = "#e2f0d9")
        self.dg_label.image = self.delete_guest_photo
        self.delete_button = Button(self.ge_window,image = self.delete_guest_photo,cursor = "hand2",bg = "white",borderwidth = 0)
        self.delete_button.place(x=1275,y=500)

        self.dg_heading = Label(self.ge_window, text = "Delete", font = ("Avenir Next",20),bg = "#c4dfb4")
        self.dg_heading.place(x=1310, y= 585)

##      Back button
        self.back_icon = Image.open("back icon.png")
        self.back_icon_resize = self.back_icon.resize((175,62))
        self.back_icon = self.back_icon_resize
        self.back_photo = ImageTk.PhotoImage(self.back_icon)
        self.back_label = Label(self.ge_window,image =self.back_photo ,bg = "#e2f0d9")
        self.back_label.image = self.back_photo
        self.back_button = Button(self.ge_window,image = self.back_photo,command = self.back_edit_guess,cursor = "hand2",bg = "white",borderwidth = 0)
        self.back_button.place(x=1082,y=640,width = 200, height = 62)


##      User icon

        self.guest_icon = Image.open("user icon.png")
        self.guest_icon_resize = self.guest_icon.resize((175,175))
        self.guest_icon = self.guest_icon_resize
        self.guest_icon_photo = ImageTk.PhotoImage(self.guest_icon)
        self.gi_label = Label(self.ge_window,image =self.guest_icon_photo ,bg = "#a8d18e")
        self.gi_label.image = self.guest_icon_photo
        self.gi_label.place(x=1100,y=225)
   


    def save(self):
        #this connects to the database - if the database 
        #doesnt exist it will create it

        connection = sqlite3.connect("Guestrecord.db")
        cursor = connection.cursor()


        #Creating tables in Database - Only creates the 
        #table if they do not exist already

        #sets up the fields needed for the customer table

        sqlCommand = """
           CREATE TABLE IF NOT EXISTS tb1Guest1
           (
           guestID INTEGER NOT NULL,
           guestTitle TEXT,
           guestFirstname TEXT,
           guestSurname TEXT,
           guestDOB DATE,
           guestPaymentType TEXT,
           guestEmail TEXT,
           guestPhoneNumber INTEGER,
           guestAddress TEXT,
           guestPostcode TEXT,
           primary key (guestID)
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
        gTitle = self.guest_title_entry.get()
        gFirstname = self.guest_name_entry.get()
        gSurname = self.guest_surname_entry.get()
        gDob = self.guest_DOB_entry.get()
        gPayment_type = self.guest_payment_entry.get()
        gEmail = self.guest_email_entry.get()
        gPhoneNumber = self.guest_phone_entry.get()
        gAddress = self.guest_adress_entry.get()
        gPostcode = self.guest_postcode_entry.get()



        #creating a record of all the fields entered
        GuestRec = [gTitle,gFirstname,gSurname,gDob,gPayment_type,gEmail,gPhoneNumber,gAddress,gPostcode]

        cursor.execute("INSERT INTO tb1Guest1 VALUES(Null,?,?,?,?,?,?,?,?,?)",GuestRec)

        connection.commit()
        connection.close()


    def edit(self):
         connection = sqlite3.connect("Guestrecord.db")
         cursor = connection.cursor()
         
         gGuestID = self.guest_ID_entry.get()
         gTitle = self.guest_title_entry.get()
         gFirstname = self.guest_name_entry.get()
         gSurname = self.guest_surname_entry.get()
         gDob = self.guest_DOB_entry.get()
         gPayment_type = self.guest_payment_entry.get()
         gEmail = self.guest_email_entry.get()
         gPhoneNumber = self.guest_phone_entry.get()
         gAddress = self.guest_adress_entry.get()
         gPostcode = self.guest_postcode_entry.get()
         #Code to edit fields using the GuestID to find the relevant record - will need verification to ensure there is data in the field.
         if gGuestID != "":
            if gFirstname != "":
               cursor.execute("UPDATE  tb1Guest1 SET guestFirstname = ? WHERE guestID = ?", (gFirstname, gGuestID))
            if gSurname != "":
               cursor.execute("UPDATE tb1Guest1 SET guestSurname = ? WHERE guestID = ?",(gSurname, gGuestID))
            if gTitle != "":
               cursor.execute("UPDATE tb1Guest1 SET guestTitle = ? WHERE guestID = ?",(gTitle, gGuestID))
            if gDob != "":
               cursor.execute("UPDATE tb1Guest1 SET guestDOB = ? WHERE guestID = ?",(gDob, gGuestID))
            if gPayment_type != "":
               cursor.execute("UPDATE tb1Guest1 SET guestPaymentType = ? WHERE guestID = ?",(gPayment_type, gGuestID))
            if gEmail != "":
               cursor.execute("UPDATE tb1Guest1 SET guestEmail = ? WHERE guestID = ?",(gEmail, gGuestID))
            if gPhoneNumber != "":
               cursor.execute("UPDATE tb1Guest1 SET guestPhoneNumber = ? WHERE guestID = ?",(gPhoneNumber, gGuestID))
            if gAddress != "":
               cursor.execute("UPDATE tb1Guest1 SET guestAddress = ? WHERE guestID = ?",(gAddress, gGuestID))
            if gPostcode != "":
                cursor.execute("UPDATE tb1Guest1 SET guestPostcode = ? WHERE guestID = ?",(gPostcode, gGuestID))  
                messagebox.showinfo(title = "Edit Guest", message = "You have successfully changed the Guest details")
                connection.commit()
                connection.close()

    def DeleteGuest(self):
             gGuestID = self.guest_ID_entry.get()
             connection = sqlite3.connect("Guestrecord.db")
             cursor = connection.cursor()         
             cursor.execute("DELETE FROM tb1Guest1 WHERE guestID = ? ", gGuestID)
             connection.commit()
             connection.close()

    def back_add_guess(self):
        self.ga_window.destroy()
        window=Tk()
        Main_menu(window)
        
    def back_edit_guess(self):
        self.ge_window.destroy()
        window=Tk()
        Main_menu(window)

    def back_search_guess(self):
        self.gf_window.destroy()
        window=Tk()
        Main_menu(window)

    
        
        
def page():
    window=Tk()
    Login_page(window)
    window.mainloop()

if __name__ == "__main__":
    page()
        
