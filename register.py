
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk


class Register:
    '''Responsible for showing data into the window'''

    def __init__(self, root):
        # Shows root file to the window
        self.root = root
        # Shows window title
        self.root.title("Registration Window")
        # Shows window screen's height and width
        self.root.geometry("1350x700+0+0")
        # set background color to white
        self.root.config(bg='white')

        # ===== Background Image ========
        self.bg = ImageTk.PhotoImage(file='images/bg.jpg')
        bg = Label(self.root, image=self.bg).place(x=250,y=0, relwidth=1, relheight=1) 

        # ===== Left Image ========
        self.left = ImageTk.PhotoImage(file='images/bg-1.jpg')
        left = Label(self.root, image=self.left).place(x=80,y=100, width=400, height=500) 

        # ===== Register Frame =====
        frame1 = Frame(self.root, bg="white")
        frame1.place(x=400,y=100, width=700, height=500)
        
        # ------------ Row 1
        title = Label(frame1, text= "REGISTER HERE", font=('times new roman',15, 'bold'), bg='white', fg='green').place(x=50, y=30)

        # ------------ Row 2
        
        f_name = Label(frame1, text='First Name',font=('times new roman',15, 'bold'), bg='white', fg='green' ).place(x=50, y=100)
        self.txt_fname = Entry(frame1, font=('times new roman',15, 'bold'), bg='lightgrey', fg='green')
        self.txt_fname.place(x=50, y=130, width=250)
        
        l_name = Label(frame1, text='Last Name',font=('times new roman',15, 'bold'), bg='white', fg='green' ).place(x=370, y=100)
        self.txt_lname = Entry(frame1, font=('times new roman',15, 'bold'), bg='lightgrey', fg='green')
        self.txt_lname.place(x=370, y=130, width=250)

        # ------------- Row 3
        contact = Label(frame1, text='Contact No.',font=('times new roman',15, 'bold'), bg='white', fg='green' ).place(x=50, y=170)
        self.txt_contact = Entry(frame1,  font=('times new roman',15, 'bold'), bg='lightgrey', fg='green')
        self.txt_contact.place(x=50, y=200, width=250)

        email = Label(frame1, text='Email',font=('times new roman',15, 'bold'), bg='white', fg='green' ).place(x=370, y=170)
        self.txt_email = Entry(frame1, font=('times new roman',15, 'bold'), bg='lightgrey', fg='green')
        self.txt_email.place(x=370, y=200, width=250)

        # ------------- Row 4
        question = Label(frame1, text='Security Question',font=('times new roman',15, 'bold'), bg='white', fg='green' ).place(x=50, y=250)
        
        self.cmb_quest = ttk.Combobox(frame1,font=('times new roman',13), state='readonly', justify=CENTER)
        self.cmb_quest['values']=('Select', 'Your First Pet Name', 'Your Birth Place', 'Your Best Friend Name')
        self.cmb_quest.place(x=50, y=280, width=250)
        self.cmb_quest.current(0)

        answer = Label(frame1, text='Answer',font=('times new roman',15, 'bold'), bg='white', fg='green' ).place(x=370, y=250)
        self.txt_answer = Entry(frame1, font=('times new roman',15, 'bold'), bg='lightgrey', fg='green')
        self.txt_answer.place(x=370, y=280, width=250)

        # ------------- Row 5
        password = Label(frame1, text='Password',font=('times new roman',15, 'bold'), bg='white', fg='green' ).place(x=50, y=330)
        self.txt_password = Entry(frame1, font=('times new roman',15, 'bold'), bg='lightgrey', fg='green')
        self.txt_password.place(x=50, y=360, width=250)

        cpassword = Label(frame1, text='Confirm Password',font=('times new roman',15, 'bold'), bg='white', fg='green' ).place(x=370, y=330)
        self.txt_cpassword = Entry(frame1, font=('times new roman',15, 'bold'), bg='lightgrey', fg='green')
        self.txt_cpassword.place(x=370, y=360, width=250)

        # ------- Terms -----
        self.var_chk=IntVar()
        chk = Checkbutton(frame1, text="I Agree The Terms & Conditions", variable=self.var_chk, onvalue=1, offvalue=0, font=('times new roman',13, 'italic'), bg='white', fg='green').place(x=50,y=400)
        
        self.btn_img = ImageTk.PhotoImage(file='images/btn.jpg')
        btn = Button(frame1, text="Register", font=('times new roman', 20),bd=0, fg='white', image=self.btn_img, height=30, width= 300, compound=CENTER, cursor='hand2', command=self.register_data).place(x=50,y=440)
        
        signin_btn = Button(self.root, text="Sign In", font=('times new roman', 20),bd=0, fg='white', bg='green', cursor='hand2').place(x=160,y=470,width=150)

    def register_data(self):
        if self.txt_fname.get() == "" \
            or self.txt_lname.get() == "" \
            or self.txt_contact.get() == "" \
            or self.txt_email.get() == "" \
            or self.txt_password.get() =="" \
            or self.cmb_quest.get() == "Select"\
            or self.txt_cpassword.get() =="":
            messagebox.showerror('Error', 'All Fields Are Required', parent=self.root)
        elif self.txt_password.get() != self.txt_cpassword.get():
            messagebox.showerror('Error', 'Password & Confirm password should be same', parent=self.root)
        elif self.var_chk.get() == 0:
            messagebox.showerror('Error', 'Please agree our terms & condition', parent=self.root)
        else:
            messagebox.showinfo('Success', 
            f'Name:\t{self.txt_fname.get()} {self.txt_lname.get()},\
            \nContact:\t{self.txt_contact.get()}\
            \nEmail:\t{self.txt_email.get()}\
            \nCmb:\t{self.cmb_quest.get()}\
            \nAnswer:\t{self.txt_answer.get()}\
            \nPassword:\t{self.txt_password.get()}\
            \nConfirm:\t{self.txt_cpassword.get()}'\
            )

        print(f'Name:\t{self.txt_fname.get()} {self.txt_lname.get()},\
        \nContact:\t{self.txt_contact.get()}\
        \nEmail:\t{self.txt_email.get()}\
        \nCmb:\t{self.cmb_quest.get()}\
        \nAnswer:\t{self.txt_answer.get()}\
        \nPassword:\t{self.txt_password.get()}\
        \nConfirm:\t{self.txt_cpassword.get()}')

# Initiates windows root screen
root = Tk()

# passes instance to the model
obj = Register(root)

# Starts loop for showing the window until the next command.
root.mainloop()

