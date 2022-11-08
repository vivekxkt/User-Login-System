

# PROJECT NAME - USER REGESTRATION FORM WITH MYSQL CONNECTIVITY       [      PROJECT / CODE INFO      ] 
 
#                                                                     -- > PROJECT CODE : 01
#                                                                     -- > PROJECT STARTED : 22-OCT-2022
#                                                                     -- > PROJECT ENDED   : 24-OCT-2022


#                                                                     -- > NUM OF CLASSES USED  :  1
#                                                                     -- > NUM OF FUNCTIONS USED  :  16
#                                                                     -- > TOTAL LINES OF CODE  :  640
#                                                                     -- > CODING LEVEL  :  INTERMEDIATE
#                                                                     -- > RESULT INTERFACE : NORMAL
#                                                                     -- > BUGS REMAINING  :  0 (TILL DATE)


# CHANGES MADE IN PROJECT SINCE IT WAS LAST UPDATED  -- >            [        UPDATES / CHANGES        ]

#                                                            -- > ADDED A NEW HOME SCREEN
#                                                            -- > CUSTOMISED THE REGESTRATION PAGE
#                                                            -- > ADDED A NEW WAY TO CHANGE PASSWORD ie: VIA EMAIL
#                                                            -- > ADDED A BUTTON " FORGET USERNAME ?" : RESET PAGE
#                                                            -- > ADDED A BUTTON " LOG IN " : SIGN UP PAGE
#                                                            -- > REMOVED THE DISABLED STATE OF RESET BUTTON : RESET PAGE


# PROJECT UPDATION DATE(S) -- >                                      -- > PROJECT LAST UPDATED   : 30-OCT-2022




from msilib.schema import CheckBox      
from sqlite3 import IntegrityError
import mysql.connector
from tkinter import *
from tkinter import messagebox
from tkinter.font import BOLD
import ctypes
import PyInstaller

#------------------------------------------------------------------------------------------------------------------->
#                                         # INITIALISATION

class User:
    
    def __init__(self,root):
        self.root=root
        self.root.title("Home page")
        self.root.geometry("600x300")
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
        root.tk.call('tk', 'scaling', 1.5)
        self.root.resizable(False,False)
        
        label_1=Label(self.root,text="REGISTRATION FORM",font=(BOLD,30))
        label_1.pack(pady=30)
        
        label_2= Label(root,text="Welcome to the regestration forms click next to continue",font=5)
        label_2.pack(pady=10)
        
        next_button=Button(root,text="Next",font=10,bd=4,relief=RAISED,command=self.page_1)
        next_button.pack(pady=10)
        
    def page_1(self):
        root.destroy()
        self.pg1_win=Tk() 
        self.pg1_win.title("Home page")
        self.pg1_win.geometry("600x600")
        self.pg1_win.resizable(False,False)
        
        label_1=Label(self.pg1_win,text="REGISTRATION FORM",font=(BOLD,30))
        label_1.pack(pady=30)  
         
        reg_button=Button(self.pg1_win,font=10,bd=4,relief=RAISED,text="Create New Account",command=self.reg_page)
        reg_button.pack(pady=10)
        
        login_button=Button(self.pg1_win,font=10,bd=4,relief=RAISED,text="Log in",command=self.login_page)
        login_button.pack(pady=20)
        
        

#-------------------------------------------------------------------------------------------------------------------> 
#                                           # USER LOG IN PAGE

    def login_page(self):
        # self.pg1_win.destroy()
        self.window=Tk()
        
        
        self.window.geometry("600x600")
        self.window.title("log In page")
        self.window.tk.call('tk','scaling',1.75)
        self.window.resizable(False,False)
        
        #heading
        label_2=Label(self.window,text="Log In User",font=(BOLD,30),pady=30)
        label_2.pack()
        
        #username
        label_3=Label(self.window,text="Username")
        label_3.pack()
        
        self.text_1=Entry(self.window,font=40,bd=5)
        self.text_1.pack()
        
        #password
        label_4=Label(self.window,text="Password")
        label_4.pack()
        
        self.text_2=Entry(self.window,font=40,bd=5)
        self.text_2.config(show="*")
        self.text_2.pack()
        
        #Phone number
        label_5=Label(self.window,text="Phone Number ")
        label_5.pack()        
        self.text_3=Entry(self.window,font=40,bd=5)
        self.text_3.pack()
        
        #log in 
        b_login=Button(self.window,text="Log In",command=self.user_login)
        b_login.pack(pady=20)
        
        #reset password
        self.f_login=Button(self.window,text="Reset Password",command=self.reset_password_page)
        self.f_login.pack(pady=10)
        
    
            
#------------------------------------------------------------------------------------------------------------------->  
#                                       # USER REGESTRATION / SIGN UP PAGE
       
    def reg_page(self):
        self.pg1_win.destroy()
        
        window_2=Tk()
        
        window_2.geometry("600x700")
        window_2.title("Registeration Page")
        window_2.tk.call('tk','scaling',1.75)
        window_2.resizable(False,False)
        
        #headding
        label_win_1=Label(window_2,text="Register User",font=(BOLD,40))
        label_win_1.place(x=95,y=20)
        
        #first name
        reg_text_1=Label(window_2,text="First Name :",font=20)
        reg_text_1.place(x=60,y=140)
        
        self.reg_entry_1=Entry(window_2,font=40,bd=5)
        self.reg_entry_1.place(x=220,y=140)
        
        #last name
        reg_text_2=Label(window_2,text="Last Name :",font=20)
        reg_text_2.place(x=60,y=180)
        
        self.reg_entry_2=Entry(window_2,font=40,bd=5)
        self.reg_entry_2.place(x=220,y=180)
    
        #username
        reg_text_3=Label(window_2,text="Username :",font=20)
        reg_text_3.place(x=60,y=240)
        
        self.reg_entry_3=Entry(window_2,font=40,bd=5)
        self.reg_entry_3.place(x=220,y=240)
        
        #password
        reg_text_4=Label(window_2,text="Password :",font=20)
        reg_text_4.place(x=60,y=280)
        
        self.reg_entry_4=Entry(window_2,font=40,bd=5)
        self.reg_entry_4.config(show="*")
        self.reg_entry_4.place(x=220,y=280)
        
        #email id
        self.reg_text_5=Label(window_2,text="Email Id :",font=20)
        self.reg_text_5.place(x=60,y=345)
        
        self.reg_entry_5=Entry(window_2,font=40,bd=5)
        self.reg_entry_5.place(x=220,y=345)
        
        #phone number
        reg_text_6=Label(window_2,text="Phone number :",font=20)
        reg_text_6.place(x=60,y=390)
        
        self.reg_entry_6=Entry(window_2,font=40,bd=5)
        self.reg_entry_6.place(x=220,y=390)
        
        self.x=IntVar()
        chk=Checkbutton(window_2,text="I agree with terms and conditions",font=4,variable=self.x,
                        onvalue=1,offvalue=0,command=self.display)
        chk.place(x=60,y=480)
        
        self.reg_signup=Button(window_2,text="Sign Up",font=(BOLD,13),command=self.reg_user)
        self.reg_signup.config(state=DISABLED)
        self.reg_signup.place(x=60,y=540)
        
        log_but = Button(window_2,text= "Go to log in Screen",font=(BOLD,13),command=self.login_page)
        log_but.place(x=300,y=540)

    def display(self):
        k=self.x.get()
        
        if(k==1):
            self.reg_signup.config(state=ACTIVE)
            
        else:
            self.reg_signup.config(state=DISABLED)
            
        
        
        
#-------------------------------------------------------------------------------------------------------------------> 
#                                    # USER REGESTRATION DETAILS SUBMITTING TO DATABASE 
     
    def reg_user(self):
        
        First_Name =self.reg_entry_1.get()
        Last_Name= self.reg_entry_2.get()
        Username=self.reg_entry_3.get()
        Password=self.reg_entry_4.get()
        Email_id=self.reg_entry_5.get()
        Phone_number=self.reg_entry_6.get()
        
        if ((First_Name=='')or(Last_Name=='')or(Username=='')or(Password=='')or(Email_id=='')or(Phone_number=='')):
            messagebox.showerror(title="Error",message="Some fields are empty ")
            
        else:
            try:
                mydb = mysql.connector.connect(host='localhost',port='3306',user='sqluser',password='password',database='register')
                mycursor=mydb.cursor()
                
                
                mycursor.execute("select * from sign_up where Username = (%s)",(Username,))
                
                x=0
                for i in mycursor:
                    x+=1
                        
                if x>=1:
                    messagebox.showerror(title="Error",message="Entered Username is already present ")
                
                else:
                
                    mycursor.execute("insert into sign_up values(%s,%s,%s,%s,%s,%s)",(First_Name,Last_Name,Username,Password,Email_id,Phone_number))
                    mydb.commit()
                    messagebox.showinfo(title="Regestration Details",message="Regestration Successful !")
                    
                    self.login_page()
                    
            except IntegrityError :
                messagebox.showerror(title="Error",message="Entered email is already present")    
#-------------------------------------------------------------------------------------------------------------------> 
#                                      # USER LOG IN DETAILS SUBMITTING TO DATABASE

    def user_login(self):
        mydb = mysql.connector.connect(host='localhost',port='3306',user='sqluser',password='password',database='register')
        mycursor=mydb.cursor()

        username_1=self.text_1.get()
        password_1=self.text_2.get()
        phone_numb=self.text_3.get()
        
        mycursor.execute("Select * from sign_up where Username = %s and Password = %s and Phone_number = %s",(
                         username_1,password_1,phone_numb)) # It will check if there is any entry present in register table

        c=0
        
        for i in mycursor:
            c+=1
            
        if c>=1:
            #checking if there is already a logged in user in (log in) table or not
            mycursor.execute("Select * from Log_in where Username = %s and Password = %s and Phone_number = %s",(
                         username_1,password_1,phone_numb))
            x=0
            
            for i in mycursor:
                x+=1
                
            if  x>=1:
                messagebox.showinfo(title="Log In",message="Logged in successfully")
            else:   
                messagebox.showinfo(title="Log In",message="You are now logged in")
                mycursor.execute("insert into Log_in values(%s,%s,%s)",(username_1,password_1,phone_numb))
                mydb.commit()
                
        else:
            messagebox.showerror(title="Log in error",message="Incorrect details please recheck!")


#-------------------------------------------------------------------------------------------------------------------> 
#                                    # PASSWORD RESET PAGE
        
    def reset_password_page(self):
        self.window.destroy()
        
        #new window
        self.reset_win=Tk()
        
        self.reset_win.geometry("600x700")
        self.reset_win.title("Password Reset")
        self.reset_win.tk.call('tk','scaling',1.75)
        self.reset_win.resizable(False,False)
        
        #headding
        res_label=Label(self.reset_win,text="Password Reset",font=(BOLD,30))
        res_label.place(x=120,y=30)
        
        #username
        user_label=Label(self.reset_win,text="Username",font=10)
        user_label.place(x=120,y=140)
        
        self.user_text=Entry(self.reset_win,font=60,relief=SUNKEN,bd=3)
        self.user_text.place(x=120,y=180)
        
        # FORGOT USERNAME BUTTON
        reset_username=Button(self.reset_win,text="Forgot Username ?",bd=3,relief=RAISED,command=self.user_reset)
        reset_username.place(x=370,y=176)
        
        #password 
        password_label_1=Label(self.reset_win,text="New Password",font=10)
        password_label_1.place(x=120,y=240)
        
        self.password_text_1=Entry(self.reset_win,font=60,relief=SUNKEN,bd=3)
        self.password_text_1.config(show="*",fg="black")
        self.password_text_1.place(x=120,y=280)
        
        
        #Confirm password
        password_label_2=Label(self.reset_win,text="Confirm Password",font=10)
        password_label_2.place(x=120,y=340)
        
        
        self.password_text_2=Entry(self.reset_win,font=60,relief=SUNKEN,bd=3)
        self.password_text_2.config(show="*",fg="black")
        self.password_text_2.place(x=120,y=380)
        
        
        # Check Password Button
        self.match_button=Button(self.reset_win,text="Check Password",command=self.match)  
        self.match_button.place(x=370,y=375) 
        
        
        #reset button
        self.reset_button=Button(self.reset_win,text="Reset",bd=4,relief=RAISED,font=10,command=self.confirm_mobile)
        self.reset_button.place(x=120,y=440)
        
        
#------------------------------------------------------------------------------------------------------------------->
#                                    # FORGET USERNAME WINDOW

    def user_reset(self):
        user_win=Tk()
        self.reset_win.destroy()
        user_win.geometry("600x600")
        user_win.title("Username  Reset")
        user_win.tk.call('tk','scaling',1.75)
        user_win.resizable(False,False)
        
        #headding
        label_diff=Label(user_win,text="Confirmation",font=(BOLD,30))
        label_diff.pack(pady=20)

        #email address label
        label_email=Label(user_win,text="Enter your Email address",font=5)
        label_email.pack(pady=10)

        #email address entry box
        self.entry_user=Entry(user_win,font=40,relief=RAISED,bd=4)
        self.entry_user.pack()
        
        #Phone number label
        label_ph=Label(user_win,text="Mobile number",font=5)
        label_ph.pack(pady=10)

        #Phone number entry box
        self.entry_ph=Entry(user_win,font=40,relief=RAISED,bd=4)
        self.entry_ph.pack()

        #Confirm button
        self.button_user=Button(user_win,text="Confirm",font=5,command=self.user_conf)
        self.button_user.pack(pady=20)
        
        
    def user_conf(self):
        x=self.entry_user.get()
        z=self.entry_ph.get()
        
        if((x=='')or(z=='')):
            messagebox.showerror(title="Error",message="Some fields are empty")
            
        else:
            #calling database
            mydb = mysql.connector.connect(host='localhost',port='3306',user='sqluser',password='password',database='register')
            mycursor=mydb.cursor()
            #finding Entered user in sign up database
            
            mycursor.execute("Select * from sign_up where Email_id  = (%s) and Phone_number = %s",(x,z))
            
            c=0
            
            for i in mycursor:
                c+=1
                
            if c>=1:
                self.conf_win=Tk()
                self.conf_win.geometry("600x600")
                self.conf_win.title("Username  Reset")
                self.conf_win.tk.call('tk','scaling',1.75)
                self.conf_win.resizable(False,False)
                
                label_diff=Label(self.conf_win,text="Username Reset",font=(BOLD,30))
                label_diff.pack(pady=20)

                label_email=Label(self.conf_win,text="Enter new username",font=5)
                label_email.pack(pady=10)

                self.entry_user_1=Entry(self.conf_win,font=40,relief=RAISED,bd=4)
                self.entry_user_1.pack()

                self.button_user_1=Button(self.conf_win,text="Confirm",font=5,command=self.confirm)
                self.button_user_1.pack(pady=20)
                
            else:
                messagebox.showerror(title="Error",message="Incorrect details")
            
        
    def confirm(self):
        x=self.entry_user_1.get()   # USERNAME
        y=self.entry_user.get()     # EMAIL ADDRESS
        z=self.entry_ph.get()       # PHONE NUMBER
                
        if (x==''):
            messagebox.showerror(title="Error",message="Some fields are empty")
            
        else:
            #calling database
            mydb = mysql.connector.connect(host='localhost',port='3306',user='sqluser',password='password',database='register')
            mycursor=mydb.cursor()


            mycursor.execute("update log_in set Username = %s where Phone_number = %s",(x,z))
            mydb.commit()
            mycursor.execute("update sign_up set Username = %s where Email_id = %s",(x,y))
            mydb.commit()
            
            messagebox.showinfo(title="Info",message="Your Username has been changed")
            self.conf_win.destroy()
            
        
        
#------------------------------------------------------------------------------------------------------------------->    

#                                       # CHECK PASSWORD BUTTON IN PASSWORD RESET WINDOW
   
    def match(self):
        a=self.password_text_1.get()
        b=self.password_text_2.get()
        c=self.user_text.get()
        
        if ((a=='') or (b=='') or (c=='')):
            messagebox.showerror(title="Error",message="Some fields are empty")
        
        else:
            while(a==b):
                self.match_button['text']='Password Matched'
                
                
                break
            else:
                self.match_button['text']="Does not match"
                
                 
#------------------------------------------------------------------------------------------------------------------->            
#                                              # CONFIORM MOBILE BUTTON 

    def confirm_mobile(self):
        
        a = self.password_text_1.get()
        b = self.password_text_2.get()
        
        if(a=="" or b==''):
            messagebox.showerror(title="Error",message="Some fields are empty !")
        
        if(a!=b):
            messagebox.showerror(title="Error",message="Password does not match")
        else:
            #calling database
            mydb = mysql.connector.connect(host='localhost',port='3306',user='sqluser',password='password',database='register')
            mycursor=mydb.cursor()
            #finding Entered user in login database
            username_confirm=self.user_text.get()
            mycursor.execute("Select * from log_in where Username = (%s)",(username_confirm,))
            
            c=0
            
            for i in mycursor:
                c+=1
                
            if c>=1:
                    
                self.confirm_win=Tk()
                
                    
                self.confirm_win.geometry("600x600")
                self.confirm_win.title("Confirmation")
                self.confirm_win.tk.call('tk','scaling',1.75)
                self.confirm_win.resizable(False,False)
                    
                #label
                label=Label(self.confirm_win,text="Confirm Mobile",font=(BOLD,30))
                label.pack(pady=20)

                #Phone number label
                label_phone=Label(self.confirm_win,text="Phone number",font=10)
                label_phone.pack(pady=20)

                #entry box for phone number
                self.entry_phone=Entry(self.confirm_win,font=35,relief=RAISED,bd=4)
                self.entry_phone.pack()

                #confirmation button
                button_confirm=Button(self.confirm_win,text="Confirm",font=10,bd=3,command=self.change_password)
                button_confirm.pack(pady=15)
                
                button_diff=Button(self.confirm_win,text="Use different method",font=10,bd=3,command=self.diff_method)
                button_diff.pack(pady=50)
                    
            else:
                messagebox.showerror(title="Error",message="No user found")
                
#------------------------------------------------------------------------------------------------------------------->                     
#                                        #USE DIFFERENT METHOD BUTTON
                                        
    def diff_method(self):
        self.confirm_win.destroy()
        diff_win=Tk()
        diff_win.geometry("600x600")
        diff_win.title("Password Reset")
        diff_win.tk.call('tk','scaling',1.75)
        diff_win.resizable(False,False)
        
        label_diff=Label(diff_win,text="Confirmation",font=(BOLD,30))
        label_diff.pack(pady=20)

        label_email=Label(diff_win,text="Enter your Email address",font=5)
        label_email.pack(pady=10)

        self.entry_diff=Entry(diff_win,font=40,relief=RAISED,bd=4)
        self.entry_diff.pack()

        self.button_confirm=Button(diff_win,text="Confirm",font=5,command=self.final_conf)
        self.button_confirm.pack(pady=20)
        
#------------------------------------------------------------------------------------------------------------------->

#                                        #FINAL CONFIRMATION BUTTON

    def final_conf(self):
        username_confirm=self.user_text.get()
        password_change=self.password_text_2.get()
        email_confirm=self.entry_diff.get()
        
        if email_confirm=='':
            messagebox.showerror(title="Error",message="Some fields are empty")
            
        else:
        
            self.button_confirm['text']='Please wait'

            x= messagebox.askyesnocancel(title="Confirmation",message="Are you sure you want to save the changes ?")
            
            if(x==YES):
                mydb = mysql.connector.connect(host='localhost',port='3306',user='sqluser',password='password',database='register')
                mycursor=mydb.cursor()
     
                mycursor.execute("Select * from sign_up where Username = (%s) and Email_id = (%s)",(username_confirm,email_confirm))
                
                c=0
                
                for i in mycursor:
                    c+=1
                    
                if c>=1:
                
                    mycursor.execute("update log_in set Password = %s where Username = %s",(password_change,username_confirm))
                    mydb.commit()
                    mycursor.execute("update sign_up set Password = %s where Username = %s",(password_change,username_confirm))
                    mydb.commit()
                    messagebox.showinfo(title="Info",message="Your password has been changed")
                    self.button_confirm['text']='Confirm'
                    
                elif(c==1):
                    messagebox.showerror(title="Error",message="Entered email in incorrect")
                    self.button_confirm['text']='Confirm'
                
                else:
                    messagebox.showerror(title="Error",message="Entered email in incorrect")
                    self.button_confirm['text']='Confirm'
                    
            elif (x==NO):
                messagebox.showerror(title="Info",message="Your password has not been changed")
                self.button_confirm['text']='Confirm'

                
            else:
                messagebox.showinfo(title="Info",message="You canceled the process")
                self.button_confirm['text']='Confirm'

#------------------------------------------------------------------------------------------------------------------->        
#                                            #CHANGE PASSWORD BUTTON
        
           
    def change_password(self):
        mydb = mysql.connector.connect(host='localhost',port='3306',user='sqluser',password='password',database='register')
        mycursor=mydb.cursor()

        username_change=self.user_text.get()
        password_change=self.password_text_2.get()
        phone_change=self.entry_phone.get()
        
        mycursor.execute("Select * from log_in where Username = (%s) and Phone_number = (%s)",(username_change,phone_change))
        
        c=0
        
        for i in mycursor:
            c+=1
            
        if c>=1:
            mycursor.execute("update log_in set Password = %s where Username = %s",(password_change,username_change))
            mydb.commit()
            mycursor.execute("update sign_up set Password = %s where Username = %s",(password_change,username_change))
            mydb.commit()
            messagebox.showinfo(title="Info",message="Your password has been changed")
                
        elif(c==1):
            messagebox.showerror(title="Info",message="Entered phone number is incorrect")
                
        else:
            messagebox.showerror(title="Info",message="Entered phone number is incorrect")
            
#------------------------------------------------------------------------------------------------------------------->        

#window and object declaration

root=Tk()

obj=User(root)

root.mainloop()
