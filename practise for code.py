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



window= Tk()
window.geometry("1000x700")
window.title("Login screen")
window.configure(bg = "white")
#To zoom the page 
window.state("zoomed")
window.resizable(False,False)

password = Label(window, text = "Password", font = ("Avenir Next",30), bg="white")
password.place(x=60,y=275)
password_entry = Entry(window,width = 30,font = ("Avenir Next",21),bg = "#e2f0d9",highlightthickness = 0,relief=FLAT)
password_entry.insert(0,"Password")
password_entry.place(x=225,y=275,height = 40)
def reset(*args):
    password_entry.delete(0, END)

password_entry.bind("<Button-1>", reset)
