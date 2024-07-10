from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector


class Register_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Register window")
        self.root.geometry("1550x800+0+0")
        self.root.config(bg="#BF3EFF")
        
        
        #----------variables declaration-----------------
        
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_Contact = StringVar()
        self.var_email = StringVar()
        self.var_security_Question = StringVar()
        self.var_security_answer = StringVar()
        self.var_password = StringVar()
        self.var_confirm_password = StringVar()
        
                
        left_image = Image.open("Register_left_image.jpg")
        left_image = left_image.resize((470,550))
        self.left_photoImage = ImageTk.PhotoImage(left_image)
        
        register_frame = Frame(self.root,bg="white",bd=5,relief=RIDGE)
        register_frame.place(x=630,y=100,width=700,height=550)
        
        left_img_label = Label(self.root,image=self.left_photoImage,bd=5,relief=RIDGE)
        left_img_label.place(x=170,y=100,width=470,height=550)
        
        reg_here_label = Label(register_frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="#007FFF",bg="White")
        reg_here_label.place(x=30,y=20)
        
        first_name_label = Label(register_frame,text="First Name",font=("times new roman",15,"bold"),fg="black",bg="White")
        first_name_label.place(x=30,y=80)
        
        self.first_name_entry = ttk.Entry(register_frame,textvariable=self.var_fname,font=("times new roman",10,))
        self.first_name_entry.place(x=30,y=120,width=250)
        
        last_name_label = Label(register_frame,text="Last Name",font=("times new roman",15,"bold"),fg="black",bg="White")
        last_name_label.place(x=380,y=80)
        
        self.last_name_entry = ttk.Entry(register_frame,textvariable=self.var_lname,font=("times new roman",10,))
        self.last_name_entry.place(x=380,y=120,width=250)
        
        contact_label = Label(register_frame,text="Contact No",font=("times new roman",15,"bold"),fg="black",bg="White")
        contact_label.place(x=30,y=180)
        
        self.contact_entry = ttk.Entry(register_frame,textvariable=self.var_Contact,font=("times new roman",10,))
        self.contact_entry.place(x=30,y=220,width=250)
        
        email_label = Label(register_frame,text="Email",font=("times new roman",15,"bold"),fg="black",bg="White")
        email_label.place(x=380,y=180)
        
        self.email_entry = ttk.Entry(register_frame,textvariable=self.var_email,font=("times new roman",10,))
        self.email_entry.place(x=380,y=220,width=250)
        
        security_label = Label(register_frame,text="Select Security Question",font=("times new roman",15,"bold"),fg="black",bg="White")
        security_label.place(x=30,y=260)
        
        self.security_combo_box = ttk.Combobox(register_frame,textvariable=self.var_security_Question,font=("arial",10,),width=24,state="readonly")
        self.security_combo_box.place(x=30,y=305,width=250,height=30)
        self.security_combo_box["values"]=("Select Option","Your Birth Place","Your Father name","Favorite Cricketer")
        self.security_combo_box.current(0)
        
        security_answer_label = Label(register_frame,text="Security Answer",font=("times new roman",15,"bold"),fg="black",bg="White")
        security_answer_label.place(x=380,y=260)
        
        self.security_answer_entry = ttk.Entry(register_frame,textvariable=self.var_security_answer,font=("times new roman",10,))
        self.security_answer_entry.place(x=380,y=300,width=250)
        
        password_label = Label(register_frame,text="Password",font=("times new roman",15,"bold"),fg="black",bg="White")
        password_label.place(x=30,y=350)
        
        self.password_entry = ttk.Entry(register_frame,textvariable=self.var_password,font=("times new roman",10,))
        self.password_entry.place(x=30,y=390,width=250)
        
        confirm_label= Label(register_frame,text="Confirm Password",font=("times new roman",15,"bold"),fg="black",bg="White")
        confirm_label.place(x=380,y=350)
        
        self.confirm_entry = ttk.Entry(register_frame,textvariable=self.var_confirm_password,font=("times new roman",10,))
        self.confirm_entry.place(x=380,y=390,width=250)        
        
        self.var_check = IntVar()
        check_button = Checkbutton(register_frame,variable=self.var_check,text="I agree the term and conditions",font=("times new roman",10,"bold"),fg="black",bg="White",onvalue=1,offvalue=0)
        check_button.place(x=30,y=430)
        
        register_button = Button(register_frame,command=self.register_data,text="Register Now",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="black",bg="#007FFF",activeforeground="black",activebackground="#007FFF",cursor="hand2")
        register_button.place(x=250,y=460,width=200,height=50)
        
    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_security_Question.get() == "Select Optio0 ":
            messagebox.showerror("Error","All fields are required")
        elif self.var_password.get() != self.var_confirm_password.get():
            messagebox.showerror("Error","password & confirm password must be same")
        elif self.var_check.get() == 0:
            messagebox.showerror("Error","please agree terms and conditions")
        else:
            sql_connect = mysql.connector.connect(host="localhost",user="root",password="Avnish@2511",database="mydata")
            sql_cursor = sql_connect.cursor()
            query = ("select * from register where email=%s")
            value = (self.var_email.get(),)
            sql_cursor.execute(query,value)
            row = sql_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","user already exist,please try another email")
            else:
                sql_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                            self.var_fname.get(),
                                                                                            self.var_lname.get(),
                                                                                            self.var_Contact.get(),
                                                                                            self.var_email.get(),
                                                                                            self.var_security_Question.get(),
                                                                                            self.var_security_answer.get(),
                                                                                            self.var_password.get()
                                                                                        ))
            sql_connect.commit()
            sql_connect.close()
            messagebox.showinfo("success","Register successfully")
            
    
    
        

        
        
        
        
        
        
if __name__ == "__main__":
    root=Tk()
    app=Register_window(root)
    root.mainloop()