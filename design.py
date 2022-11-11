from tkinter import *
from tkinter.font import BOLD
import ctypes

root = Tk()
root.title("Regestration Form")
root.geometry("925x500")
root.resizable(False,False)
root.config(bg="#fff")
ctypes.windll.shcore.SetProcessDpiAwareness(1)

img = PhotoImage(file = "login.png")

img_label = Label(root,image=img,bg="white")
img_label.place(x=50,y=50)

frame=Frame(root,width=350,height=380,bg="white")
frame.place(x=500,y=50)

heading = Label(frame,text = "Log In",fg = "#0900BD",font=(BOLD,30),bg="white")
heading.place(x=125,y = 10)

def on_enter(e):
    user_entry.delete(0,'end')
    
def on_leave(e):
    name = user_entry.get()
    if name == '':
        user_entry.insert(0,"Username")
            
user_entry =  Entry(frame,font=(BOLD,13),border=0)
user_entry.place(x=30,y=90 )
user_entry.insert(0,"Username")
user_entry.bind("<FocusIn>",on_enter)
user_entry.bind("<FocusOut>",on_leave)

user_box = Frame(frame,width = 350,height = 2,bg="black")
user_box.place(x=23,y=117)

def on_enter(e):
    pass_entry.delete(0,'end')
    
def on_leave(e):
    name = pass_entry.get()
    if name == '':
        pass_entry.insert(0,"Password")
            

pass_entry =  Entry(frame,font=(BOLD,13),border=0)
pass_entry.place(x=30,y=150 )
pass_entry.insert(0,"Password")
pass_entry.bind("<FocusIn>",on_enter)
pass_entry.bind("<FocusOut>",on_leave)

user_box = Frame(frame,width = 350,height = 2,bg="black")
user_box.place(x=23,y=177)

def on_enter(e):
    ph_entry.delete(0,'end')
    
def on_leave(e):
    name = ph_entry.get()
    if name == '':
        ph_entry.insert(0,"Phone number")
            

ph_entry =  Entry(frame,font=(BOLD,13),border=0)
ph_entry.place(x=30,y=210 )
ph_entry.insert(0,"Phone number")
ph_entry.bind("<FocusIn>",on_enter)
ph_entry.bind("<FocusOut>",on_leave)

user_box = Frame(frame,width = 350,height = 2,bg="black")
user_box.place(x=23,y=237)

SignIn_button = Button(frame,text="Sign In",font=5,padx=100,fg="white",bg="#2384C2",bd=0
                       ,activebackground="blue",activeforeground="white")
SignIn_button.place(x=40,y=260)

forget_button = Button(frame,text="Forgot password ?",font=(BOLD,11),bg="white",fg="blue",bd=0,
                       activebackground="white",activeforeground="black")
forget_button.place(x=115,y=310)


root.mainloop()