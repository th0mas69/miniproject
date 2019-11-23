from tkinter import *
from tkinter import messagebox as ms
import sqlite3

# make database and users (if not exists already) table at programme start up
with sqlite3.connect('quit.db') as db:
    c = db.cursor()

c.execute("create TABLE user (username TEXT NOT NULL ,password TEXT NOT NULL, fullname TEXT, email TEXT, phone INTEGER, gender TEXT);")
db.commit()
db.close()
        
#main Class
class main:
    def __init__(self,master):
    	# Window 
        self.master = master
        # Some Usefull variables
        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()
        self.n_fullname = StringVar()
        self.n_email =  StringVar()
        self.n_phone = IntVar()
        self.gender = IntVar()
        #Create Widgets
        self.widgets()

    #Login Function
    def login(self):
    	#Establish Connection
        with sqlite3.connect('quit.db') as db:
            c = db.cursor()

        #Find user If there is any take proper action
        find_user = ('SELECT * FROM user WHERE username = ? and password = ?')
        c.execute(find_user,[(self.username.get()),(self.password.get())])
        result = c.fetchall()
        if result:
            self.logf.pack_forget()
            self.head['text'] = self.username.get() + '\n Logged In Successfully'
            self.head['pady'] = 150
        else:
            ms.showerror('Oops!','Username Not Found.')
            
    def new_user(self):
    	#Establish Connection
        with sqlite3.connect('quit.db') as db:
            c = db.cursor()

        #Find Existing username if any take proper action
        find_user = ('SELECT * FROM user WHERE username = ?')
        c.execute(find_user,[(self.username.get())])        
        if c.fetchall():
            self.username != None and self.password != None
            ms.showerror('Error!', 'Please fill required fields')
        elif c.fetchall():
            ms.showerror('Error!','Username Taken Try a Diffrent One.')
        else:
            ms.showinfo('Success!','Account Created!')
            self.log()
            
        
        #Create New Account 
        insert = 'INSERT INTO user(username,password,fullname, email, phone, gender) VALUES(?,?,?,?,?,?)'
        c.execute(insert,[(self.n_username.get()),(self.n_password.get()),(self.n_fullname.get()),(self.n_email.get()),(self.n_phone.get()),(self.gender.get())])
        db.commit()
        c.execute("UPDATE user SET gender='Male' where gender=1")
        c.execute("UPDATE user SET gender='Female' where gender=2")
        db.commit()

        #Frame Packing Methords
    def log(self):
        self.username.set('')
        self.password.set('')
        self.crf.pack_forget()
        self.head['text'] = 'LOGIN'
        self.logf.pack()
    def cr(self):
        self.n_username.set('')
        self.n_password.set('')
        self.logf.pack_forget()
        self.head['text'] = 'Create Account'
        self.crf.pack()
        
    #Draw Widgets
    def widgets(self):
        self.head = Label(self.master,text = 'LOGIN',font = ('Helvetica',35,'underline'),pady = 10)
        self.head.pack()
        self.logf = Frame(self.master,padx =10,pady = 10)
        Label(self.logf,text = 'Username: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.logf,textvariable = self.username,bd = 5,font = ('',15)).grid(row=0,column=1)
        Label(self.logf,text = 'Password: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.logf,textvariable = self.password,bd = 5,font = ('',15),show = '*').grid(row=1,column=1)
        Button(self.logf,text = ' Login ',bd = 3 ,font = ('bold',15),padx=5,pady=5,fg='white',bg='brown',command=self.login).grid()
        Button(self.logf,text = ' Create Account ',bd = 3 ,font = ('bold',15),padx=5,pady=5,fg='white',bg='brown',command=self.cr).grid(row=2,column=1)
        self.logf.pack()
        
        self.crf = Frame(self.master,padx =10,pady = 10)
        Label(self.crf,text = 'Username: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_username,bd = 5,font = ('',15)).grid(row=0,column=1)
        Label(self.crf,text = 'Password: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_password,bd = 5,font = ('',15),show = '*').grid(row=1,column=1)
        Label(self.crf,text = 'Fullname ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_fullname,bd = 5,font = ('',15)).grid(row=2,column=1)
        Label(self.crf,text = 'Email ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_email,bd = 5,font = ('',15)).grid(row=3,column=1)
        Label(self.crf,text = 'Phone Numer ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.crf, textvariable = self.n_phone,bd = 5,font = ('',15)).grid(row=4,column=1)
        Radiobutton(self.crf,text = 'Male',bd = 3 ,font = ('',15),padx=5,pady=5,variable = self.gender, value=1).grid()
        Radiobutton(self.crf,text = 'Female',bd = 3 ,font = ('',15),padx=5,pady=5,variable = self.gender, value=2).grid(row=5,column=1)
        Button(self.crf,text = 'Create Account',bd = 3 ,font = ('',15),padx=5,pady=5,fg='orange',bg='black',command=self.new_user).grid()
        Button(self.crf,text = 'Go to Login',bd = 3 ,font = ('',15),padx=5,pady=5,fg='yellow',bg='black',command=self.log).grid(row=6,column=1)

    

#create window and application object
root = Tk()
root.title("LOGIN FORM")
main(root)
root.mainloop()
