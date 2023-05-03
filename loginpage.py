from tkinter import *
from tkinter import messagebox
import pymysql

def nextpage():
    root.destroy()
    import signuppage
def login_user():
    if user.get()=='' or code.get()=='' or user.get()=='Username' or code.get()=='Password':
        messagebox.showerror('Error','All Fields are required')
    else:
        try:
            con = pymysql.connect(host='localhost',user='root',password='Root@1234')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Database Connectivity Issue,Please Try Again')
            return
        query = 'use farmeazy'
        mycursor.execute(query)
        query='select * from signup where username=%s and password=%s'
        mycursor.execute(query,(user.get(),code.get()))
        row=mycursor.fetchone()
        if row==None:
            messagebox.showerror('Error',"Invalid username or password")
        else:
            messagebox.showinfo('Welcome','Login is Successful')
            root.destroy()
            import myDashboardlog
def hide():
    openeye.config(file='images/closeye.png')
    code.config(show='*')
    eyebutton.config(command=show)

def show():
    openeye.config(file='images/openeye.png')
    code.config(show='')
    eyebutton.config(command=hide)

root = Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)


img = PhotoImage(file="images/myfarmer.png")
Label(root,image=img,bg='white',activebackground='white').place(x=50,y=50)

frame = Frame(root,width=350,height=350,bg='white')
frame.place(x=480,y=70)

heading= Label(frame,text="Sign in",fg="forest green",bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=100,y=5)

##############-------------------------
def on_enter(e):
    user.delete(0,'end')
def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')
user = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)
Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)
################3----------------------------
def on_enter(e):
    code.delete(0,'end')
def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0,'Password')
code = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
code.place(x=30,y=150)
code.insert(0,'Password')
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_leave)
Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)
openeye=PhotoImage(file='images/openeye.png')
eyebutton=Button(frame,image=openeye,bd=0,bg='white',activebackground='white',cursor='hand2',command=hide)
eyebutton.place(x=295,y=150)
############--------------------------------------------------------
Button(frame,width=39,pady=7,text="Sign in",bg="yellow green",fg='white',border=0,activeforeground='white',
        command=login_user).place(x=35,y=204)
label=Label(frame,text="Don't have an account?",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
label.place(x=75,y=270)

sign_up = Button(frame,width=6,text='Sign up',border=0,cursor='hand2',fg='lime green',bg='white',activebackground="white"
                 ,activeforeground='lime green',command=nextpage)
sign_up.place(x=215,y=270)
root.mainloop()
