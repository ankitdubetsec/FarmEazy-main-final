from tkinter import *
from tkinter import messagebox
import ast
import pymysql
def nextpage():
    window.destroy()
    import loginpage2
def clear():
    email.delete(0,END)
    user.delete(0, END)
    code.delete(0, END)
    conform_code.delete(0, END)
    email.insert(0, 'Email')
    user.insert(0, 'Username')
    code.insert(0, 'Password')
    conform_code.insert(0, 'Confirm Password')
def connect_database():

    if email.get()=='' or user.get()=='' or code.get()=='' or conform_code.get()=='' or email.get()=='Email' or user.get()=='Username' \
            or code.get()=='Password' or conform_code.get()=='Confirm Password':
        messagebox.showerror('Error','All fields are required')

    elif code.get() != conform_code.get():
        messagebox.showerror("Error",'Password mismatch')
    else:
        try:
            con = pymysql.connect(host='localhost',user='root',password='Root@1234')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Database Connectivity Issue,Please Try Again')
            return
    try:
        query='create database farmeazy'
        mycursor.execute(query)
        query='use farmeazy'
        mycursor.execute(query)
        query='create table signup(id int auto_increment primary key not null,email varchar(50),username varchar(100),' \
              'password varchar(20))'
        mycursor.execute(query)
    except:
        mycursor.execute('use farmeazy')
    query='select * from signup where username=%s'
    mycursor.execute(query,(user.get()))
    row=mycursor.fetchone()
    if row != None:
        messagebox.showerror('Error','Username already exists')
    else:
        query='insert into signup(email,username,password) values(%s,%s,%s)'
        mycursor.execute(query,(email.get(),user.get(),code.get()))
        con.commit()
        con.close()
        messagebox.showinfo('Success','Account created successfully')
        clear()
        window.destory()
        import loginpage


def hide1():
    openeye1.config(file='images/closeye.png')
    code.config(show='*')
    eyebutton1.config(command=show1)

def show1():
    openeye1.config(file='images/openeye.png')
    code.config(show='')
    eyebutton1.config(command=hide1)

def hide2():
    openeye2.config(file='images/closeye.png')
    conform_code.config(show='*')
    eyebutton2.config(command=show2)

def show2():
    openeye2.config(file='images/openeye.png')
    conform_code.config(show='')
    eyebutton2.config(command=hide2)
window = Tk()
window.title("SignUp")
window.geometry('925x600+300+100')
window.configure(bg="#fff")
window.resizable(False,False)

img = PhotoImage(file="images/farmerwithmobile.png")
Label(window,image=img,border=0,bg='white').place(x=50,y=90)

frame=Frame(window,width=350,height=450,bg="#fff")
frame.place(x=480,y=50)

heading=Label(frame,text="Sign Up",fg="forest green",bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=100,y=5)


def on_enter(e):
    email.delete(0,'end')
def on_leave(e):
    if email.get()=='':
        email.insert(0,'Email')
email = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
email.place(x=30,y=90)
email.insert(0,'Email')
email.bind('<FocusIn>',on_enter)
email.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=117)
###########-------------------
def on_enter(e):
    user.delete(0,'end')
def on_leave(e):
    if user.get()=='':
        user.insert(0,'Username')
user = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=160)
user.insert(0,'Username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=187)

###########-------------------
def on_enter(e):
    code.delete(0,'end')
def on_leave(e):
    if code.get()=='':
        code.insert(0,'Password')
code= Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
code.place(x=30,y=230)
code.insert(0,'Password')
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_leave)
openeye1=PhotoImage(file='images/openeye.png')
eyebutton1=Button(frame,image=openeye1,bd=0,bg='white',activebackground='white',cursor='hand2',command=hide1)
eyebutton1.place(x=295,y=230)
Frame(frame,width=295,height=2,bg='black').place(x=25,y=257)
#################----------------------

def on_enter(e):
    conform_code.delete(0,'end')
def on_leave(e):
    if conform_code.get()=='':
        conform_code.insert(0,'Confirm Password')
conform_code= Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
conform_code.place(x=30,y=300)
conform_code.insert(0,'Confirm Password')
conform_code.bind('<FocusIn>',on_enter)
conform_code.bind('<FocusOut>',on_leave)
openeye2=PhotoImage(file='images/openeye.png')
eyebutton2=Button(frame,image=openeye2,bd=0,bg='white',activebackground='white',cursor='hand2',command=hide2)
eyebutton2.place(x=295,y=300)
Frame(frame,width=295,height=2,bg='black').place(x=25,y=327)
###########______________

Button(frame,width=39,pady=7,text='Sign Up',bg="lime green",fg="white",border=0,command=connect_database).place(x=35,y=360)
label=Label(frame,text='I have an account',fg="black",bg='white',font=('Microsoft YaHei UI Light',9))
label.place(x=90,y=420)

signin=Button(frame,width=6,text="Sign in",border=0,bg='white',cursor='hand2',fg="forest green",command=nextpage)
signin.place(x=200,y=420)
window.mainloop()