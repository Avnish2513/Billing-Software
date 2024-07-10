from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import random,os
import tempfile
from time import strftime
from tkinter import messagebox


class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("Billing Software")
        
        # Variables declerations
        
        self.cust_name = StringVar()
        self.cust_mobile = StringVar()
        self.cust_email = StringVar()
        self.cust_bill_No = StringVar()
        self.search_bill = StringVar()
        self.product = StringVar()
        self.prices = IntVar()
        self.qty = IntVar()
        self.sub_total = StringVar()
        z=random.randint(1000,99999)
        self.cust_bill_No.set(z)
        self.tax_input = StringVar()
        self.total = StringVar()
        
        # Product categories
        
        self.category = ["Select option","Clothing","Shoes","Mobiles"]
        
        # Sub category of clothing
        
        self.sub_cat_clothing = ["Jeans","Shirts","T-shirts"]
        self.jeans = ["Spykar","Levis","Mufti"]
        self.price_spykar = 6000
        self.price_levis = 5000
        self.price_mufti = 4000
        
        self.t_shirts = ["Polo","Roadstar","Jack & Jones"]
        self.price_polo = 3000
        self.price_roadstar = 2500
        self.price_jack_jones = 2000
        
        self.shirts = ["Peter England","Louis Philipe","Park Avenue"]
        self.price_peter = 4000
        self.price_lousis = 3500
        self.price_park = 3000
        
        # sub category of shoes

        self.sub_cat_shoes = ["Sneakers","Casual","Boots"]
        self.Sneakers = ["Addidas","Puma","Nike"]
        self.price_Addidas = 2800
        self.price_puma = 2500
        self.price_nike = 2000
        
        self.casual = ["Bata","Red Chief","Spark"]
        self.price_bata = 2200
        self.price_red = 2000
        self.price_spark = 1800
        
        self.boot = ["Liberty","woodland","Metro"]
        self.price_liberty = 3800
        self.price_woodland = 3300
        self.price_metro = 2700
         
        # sub Category of mobiles
        
        self.sub_cat_mobiles = ["Iphone","Samsung","Real Me"]
        self.Iphone = ["Iphone 13","Iphone 14","Iphone 15"]
        self.price_13 = 75000
        self.price_14 = 80000
        self.price_15 = 90000
        
        self.Samsung = ["Galaxy A55","Galaxy A35","Galaxy M55"]
        self.price_A55 = 40000
        self.price_A35 = 30000
        self.price_M55 = 28000
        
        self.real_me = ["Realme 12 pro","Realme Narzo","Realme GT"]
        self.price_12_pro = 25000
        self.price_narz0 = 22000
        self.price_GT = 23000
        
        
        
        
        
        
        #Image-1
        img1=Image.open("img/b1.jpg")
        img1=img1.resize((500,130))
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        lb1_img1 = Label(self.root,image=self.photoimg1)
        lb1_img1.place(x=0,y=0,width=500,height=130)
        
        #Image-2
        img2=Image.open("img/girls.jpg")
        img2=img2.resize((500,130))
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        lb1_img2 = Label(self.root,image=self.photoimg2)
        lb1_img2.place(x=500,y=0,width=500,height=130)
        
        #Image-3
        img3=Image.open("img/girl1.jpg")
        img3=img3.resize((530,130))
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        lb1_img3 = Label(self.root,image=self.photoimg3)
        lb1_img3.place(x=1000,y=0,width=530,height=130)
        
        #Tittle-area
        
        Label_title=Label(self.root,text="Billing   Software",font=("times new roman",30,"bold"),bg="white",fg="blue")
        Label_title.place(x=0,y=130,width=1530,height=55)
        
        def time():
            s1=strftime("%H:%M:%S %p")
            time_label.config(text = s1)
            time_label.after(1000,time)
        
        time_label = Label(Label_title,font=("times new roman",15,"bold"),bg="white",fg="black")
        time_label.place(x=0,y=0,width=120,height=45)
        time()
        # Main working area
        
        main_frame = Frame(self.root,bd=5,relief=GROOVE,bg="white")
        main_frame.place(x=0,y=185,width=1530,height=630)
        
        # Customer frame area
        
        Customer_frame = LabelFrame(main_frame,text="Customer",font=("times new roman",12,"bold"),bg="white",fg="blue")
        Customer_frame.place(x=10,y=5,width=350,height=140)
        
        # Mobile
        
        self.mobile_lable = Label(Customer_frame,text="Mobile No.",font=("times new roman",12,"bold"),bg="white")
        self.mobile_lable.grid(row=0,column=0,padx=5,pady=2,sticky=W)
        
        self.mobile_Entry = ttk.Entry(Customer_frame,textvariable=self.cust_mobile,font=("arial",10,"bold"),width=24)
        self.mobile_Entry.grid(row=0,column=1,padx=25)
        
        # Customer Name
        
        self.customer_name = Label(Customer_frame,text="Customer Name",font=("times new roman",12,"bold"),bg="white",bd=4)
        self.customer_name.grid(row=1,column=0,padx=5,pady=2,sticky=W)
        
        self.customer_name_Entry = ttk.Entry(Customer_frame,textvariable=self.cust_name,font=("arial",10,"bold"),width=24)
        self.customer_name_Entry.grid(row=1,column=1,padx=25)
        
        # email
        
        self.email_label = Label(Customer_frame,text="Email",font=("times new roman",12,"bold"),bg="white",bd=4)
        self.email_label.grid(row=2,column=0,padx=5,pady=2,sticky=W)
        
        self.email_Entry = ttk.Entry(Customer_frame,textvariable=self.cust_email,font=("arial",10,"bold"),width=24)
        self.email_Entry.grid(row=2,column=1,padx=25)
        
        # Product Frame area
        
        Product_frame = LabelFrame(main_frame,text="Product",font=("times new roman",12,"bold"),bg="white",fg="blue")
        Product_frame.place(x=370,y=5,width=620,height=140)
        
        # Category
        
        self.category_label = Label(Product_frame,text="Select Categories",font=("times new roman",12,"bold"),bg="white")
        self.category_label.grid(row=0,column=0,padx=5,pady=2,sticky=W)
        
        self.category_combo_box = ttk.Combobox(Product_frame,values=self.category,font=("arial",10,"bold"),width=24,state="readonly")
        self.category_combo_box.current(0)
        self.category_combo_box.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        self.category_combo_box.bind("<<ComboboxSelected>>", self.Categories_1)
        
        # Sub-Category
        
        self.sub_category_label = Label(Product_frame,text="Sub Category",font=("times new roman",12,"bold"),bg="white")
        self.sub_category_label.grid(row=1,column=0,padx=5,pady=2,sticky=W)
        
        self.sub_category_combo_box = ttk.Combobox(Product_frame,values=[""],font=("arial",10,"bold"),width=24,state="readonly")
        self.sub_category_combo_box.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        self.sub_category_combo_box.bind("<<ComboboxSelected>>",self.product_add)
        
        # Product name
        
        self.product_name_label = Label(Product_frame,text="Product Name",font=("times new roman",12,"bold"),bg="white")
        self.product_name_label.grid(row=2,column=0,padx=5,pady=2,sticky=W)
        
        self.product_name_combo_box = ttk.Combobox(Product_frame,textvariable=self.product,font=("arial",10,"bold"),width=24,state="readonly")
        self.product_name_combo_box.grid(row=2,column=1,sticky=W,padx=5,pady=2)
        self.product_name_combo_box.bind("<<ComboboxSelected>>",self.price)
        
        # price
        
        self.price_label = Label(Product_frame,text="Price",font=("times new roman",12,"bold"),bg="white")
        self.price_label.grid(row=0,column=2,padx=5,pady=2,sticky=W)
        
        self.price_combo_box = ttk.Combobox(Product_frame,textvariable=self.prices,font=("arial",10,"bold"),width=24,state="readonly")
        self.price_combo_box.grid(row=0,column=3,sticky=W,padx=5,pady=2)
        
        # Quantity
        
        self.quantity_label = Label(Product_frame,text="Quantity",font=("times new roman",12,"bold"),bg="white")
        self.quantity_label.grid(row=1,column=2,padx=5,pady=2,sticky=W)
        
        self.quantity_Entry = ttk.Entry(Product_frame,textvariable=self.qty,font=("arial",10,"bold"),width=26)
        self.quantity_Entry.grid(row=1,column=3,padx=7)
        
        # Middle Frame
        
        Middle_frame = Frame(main_frame,bd=10)
        Middle_frame.place(x=10,y=150,width=980,height=340)
        
        #Image-1
        Middle_img1=Image.open("img/good.jpg")
        Middle_img1=Middle_img1.resize((480,340))
        self.Middle_photoimg1=ImageTk.PhotoImage(Middle_img1)
        
        Middle_label_img1 = Label(Middle_frame,image=self.Middle_photoimg1)
        Middle_label_img1.place(x=0,y=0,width=480,height=340)
        
        # #Image-2
        Middle_img2=Image.open("img/mall.jpg")
        Middle_img2=Middle_img2.resize((490,340))
        self.Middle_photoimg2=ImageTk.PhotoImage(Middle_img2)
        
        Middle_label_img2 = Label(Middle_frame,image=self.Middle_photoimg2)
        Middle_label_img2.place(x=492,y=0,width=490,height=340)
        
        # search area 
        
        search_frame = Frame(main_frame,bd=2,bg="white")
        search_frame.place(x=1020,y=15,width=500,height=40)
        
        self.Bill_Number_label = Label(search_frame,text="Bill Number",font=("times new roman",12,"bold"),bg="violet",fg="white")
        self.Bill_Number_label.grid(row=0,column=0,padx=5,pady=2,sticky=W)
        
        self.Bill_Number_Entry = ttk.Entry(search_frame,textvariable=self.search_bill,font=("arial",10,"bold"),width=26)
        self.Bill_Number_Entry.grid(row=0,column=1,padx=2,sticky=W)
        
        self.Search_button = Button(search_frame,command=self.find_bill,text="Search",font=("arial",10,"bold"),bg="blue",fg="white",cursor="hand2",width=10)
        self.Search_button.grid(row=0,column=2,padx=2)
        
        # Bill area in right side of main frame
        
        bill_area = LabelFrame(main_frame,text="Bill Area",font=("times new roman",12,"bold"),bg="white",fg="blue")
        bill_area.place(x=1000,y=45,width=480,height=440)
        
        scroll_y=Scrollbar(bill_area,orient=VERTICAL)
        self.text_area = Text(bill_area,yscrollcommand=scroll_y.set,font=("times new roman",12,"bold"),bg="white",fg="blue")
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.text_area.yview)
        self.text_area.pack(fill=BOTH,expand=1)
        
        # Bill counter area
        
        bill_counter = LabelFrame(main_frame,text="Bill counter",font=("times new roman",12,"bold"),bg="white",fg="blue")
        bill_counter.place(x=0,y=485,width=1520,height=115)
        
        # sub total
        
        self.sub_total_label = Label(bill_counter,text="Sub Total",font=("times new roman",12,"bold"),bg="white")
        self.sub_total_label.grid(row=0,column=0,padx=5,pady=2,sticky=W)
        
        self.sub_total_Entry = ttk.Entry(bill_counter,textvariable=self.sub_total,font=("arial",10,"bold"),width=26)
        self.sub_total_Entry.grid(row=0,column=1,padx=25)
        
        # Tax
        
        self.tax_label = Label(bill_counter,text="Gov Tax",font=("times new roman",12,"bold"),bg="white")
        self.tax_label.grid(row=1,column=0,padx=5,pady=2,sticky=W)
        
        self.tax_Entry = ttk.Entry(bill_counter,textvariable=self.tax_input,font=("arial",10,"bold"),width=26)
        self.tax_Entry.grid(row=1,column=1,padx=25)
        
        # Total Amount
        
        self.total_label = Label(bill_counter,text="Sub Total",font=("times new roman",12,"bold"),bg="white")
        self.total_label.grid(row=2,column=0,padx=5,pady=2,sticky=W)
        
        self.total_Entry = ttk.Entry(bill_counter,textvariable=self.total,font=("arial",10,"bold"),width=26)
        self.total_Entry.grid(row=2,column=1,padx=25)
        
        # Button Frame area
        
        button_frame = Frame(bill_counter,bd=2,bg="white")
        button_frame.place(x=320,y=0)
        
        self.add_to_cart_button = Button(button_frame,command=self.add_item,text="Add to Cart",font=("arial",10,"bold"),bg="blue",fg="white",height=3,width=20,cursor="hand2")
        self.add_to_cart_button.grid(row=0,column=0,pady=10,padx=15)
        
        self.generate_bill_button = Button(button_frame,command=self.generate_bill,text="Generate Bill",font=("arial",10,"bold"),bg="blue",fg="white",height=3,width=20,cursor="hand2")
        self.generate_bill_button.grid(row=0,column=1,pady=10,padx=15)
        
        self.Save_bill_button = Button(button_frame,command=self.save_bill,text="Save Bill",font=("arial",10,"bold"),bg="blue",fg="white",height=3,width=20,cursor="hand2")
        self.Save_bill_button.grid(row=0,column=2,pady=10,padx=15)
        
        self.print_button = Button(button_frame,text="Print",command=self.print_bill,font=("arial",10,"bold"),bg="blue",fg="white",height=3,width=20,cursor="hand2")
        self.print_button.grid(row=0,column=3,pady=10,padx=15)
        
        self.clear_button = Button(button_frame,command=self.clear,text="Clear",font=("arial",10,"bold"),bg="blue",fg="white",height=3,width=20,cursor="hand2")
        self.clear_button.grid(row=0,column=4,pady=10,padx=15)
        
        self.exit_button = Button(button_frame,command=self.root.destroy,text="Exit",font=("arial",10,"bold"),bg="blue",fg="white",height=3,width=20,cursor="hand2")
        self.exit_button.grid(row=0,column=5,pady=10,padx=15)
        self.welcome()
        
        #--------- button function -------------------
        self.l1=[]
    def add_item(self):
        Tax=1
        self.n = self.prices.get()
        self.m = self.qty.get()*self.n
        self.l1.append(self.m)
        if self.product.get() =="":
            messagebox.showerror("Error","Please select the product name")
        else:
            self.text_area.insert(END,f"\n {self.product.get()} \t\t\t {self.qty.get()} \t\t\t {self.m}")
            self.sub_total.set(str("Rs.%.2f"%(sum(self.l1))))
            self.tax_input.set(str("Rs.%.2f"%((((sum(self.l1))- (self.prices.get()))*Tax)/100)))
            self.total.set(str("Rs.%.2f"%((sum(self.l1)) + ((((sum(self.l1)) - (self.prices.get()))*Tax)/100))))
            
    def generate_bill(self):
        if self.product.get() =="":
            messagebox.showerror("Error","Please add to cart product")
        else:
            Text=self.text_area.get(9.0,(9.0+float(len(self.l1))))
            self.welcome()
            self.text_area.insert(END,Text)
            self.text_area.insert(END,"\n==================================================")
            self.text_area.insert(END,f"\n Sub Amount: \t\t\t{self.sub_total.get()}")
            self.text_area.insert(END,f"\n Tax Amount: \t\t\t{self.tax_input.get()}")
            self.text_area.insert(END,f"\n Total Amount: \t\t\t{self.total.get()}")
            self.text_area.insert(END,"\n==================================================")
    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save this bill")
        if op > 0:
            self.bill_data = self.text_area.get(1.0,END)
            f1=open("bills/"+str(self.cust_bill_No.get())+".txt","w")
            f1.write(self.bill_data)
            op = messagebox.showinfo("Saved",f" Bill No. {self.cust_bill_No.get()} saved successfully")
            f1.close()
                
    def print_bill(self):
        p1=self.text_area.get(1.0,"end-1c")
        filename = tempfile.mktemp(".txt")
        open(filename,"w").write(p1)
        os.startfile(filename,"print")
        
    def find_bill(self):
        found="no"
        for i in os.listdir("bills/"):
            if i.split(".")[0] == self.search_bill.get():
                f1 = open(f"bills/ {i}","r")
                self.text_area.delete(1.0,END)
                for d in f1:
                    self.text_area.insert(END,d)
                f1.close()
                found = "yes" 
        if found == "no":
            messagebox.showerror("Error","Invalid Bill Number")
            
    def clear(self):
        self.text_area.delete(1.0,END)
        self.cust_name.set("")
        self.cust_mobile.set("")
        self.cust_email.set("")
        self.search_bill.set("")
        self.product.set("")
        self.prices.set(0)
        self.qty.set(0)
        self.sub_total.set("")
        x=random.randint(1000,99999)
        self.cust_bill_No.set(str(x))
        self.tax_input.set("")
        self.total.set("")
        self.l1=[0]
        self.welcome()
        
        
        # bill display function
        
    def welcome(self):
        self.text_area.delete(1.0,END)
        self.text_area.insert(END,"\t           Welcome to A-Mart         ")
        self.text_area.insert(END,f"\n Bill Number : {self.cust_bill_No.get()}  ")
        self.text_area.insert(END,f"\n Customer Name : {self.cust_name.get()}  ")
        self.text_area.insert(END,f"\n Customer Mobile no : {self.cust_mobile.get()}  ")
        self.text_area.insert(END,f"\n Email : {self.cust_email.get()}  ")
                
        self.text_area.insert(END,"\n==================================================")
        self.text_area.insert(END,"\nProducts \t\tQTY \t\t\Price")
        self.text_area.insert(END,"\n==================================================")
                
        
        
        # Define function for combo box
    def Categories_1(self,event=""): 
        if self.category_combo_box.get() == "Clothing":
            self.sub_category_combo_box.config(value = self.sub_cat_clothing)
            self.sub_category_combo_box.current(0)
        
        if self.category_combo_box.get() == "Shoes":
            self.sub_category_combo_box.config(value = self.sub_cat_shoes)
            self.sub_category_combo_box.current(0)
        
        if self.category_combo_box.get() == "Mobiles":
            self.sub_category_combo_box.config(value = self.sub_cat_mobiles)
            self.sub_category_combo_box.current(0)
            
    def product_add(self,event=""):
        if self.sub_category_combo_box.get() == "Jeans":
            self.product_name_combo_box.config(value= self.jeans)
            self.product_name_combo_box.current(0)
        
        if self.sub_category_combo_box.get() == "Shirts":
            self.product_name_combo_box.config(value= self.shirts)
            self.product_name_combo_box.current(0)

        if self.sub_category_combo_box.get() == "T-shirts":
            self.product_name_combo_box.config(value= self.t_shirts)
            self.product_name_combo_box.current(0)
            
        # Shoes
        if self.sub_category_combo_box.get() == "Sneakers":
            self.product_name_combo_box.config(value= self.Sneakers)
            self.product_name_combo_box.current(0)
            
        if self.sub_category_combo_box.get() == "Casual":
            self.product_name_combo_box.config(value= self.casual)
            self.product_name_combo_box.current(0)
        
        if self.sub_category_combo_box.get() == "Boots":
            self.product_name_combo_box.config(value= self.boot)
            self.product_name_combo_box.current(0)
            
        # Mobiles
        if self.sub_category_combo_box.get() == "Iphone":
            self.product_name_combo_box.config(value= self.Iphone)
            self.product_name_combo_box.current(0)
            
        if self.sub_category_combo_box.get() == "Samsung":
            self.product_name_combo_box.config(value= self.Samsung)
            self.product_name_combo_box.current(0)
            
        if self.sub_category_combo_box.get() == "Real Me":
            self.product_name_combo_box.config(value= self.real_me)
            self.product_name_combo_box.current(0)
            
            
    def price(self,event=""):
        
        #jenas
        
        if self.product_name_combo_box.get() == "Spykar":
            self.price_combo_box.config(value=self.price_spykar)
            self.price_combo_box.current(0)
            self.qty.set(1)
        
        if self.product_name_combo_box.get() == "Levis":
            self.price_combo_box.config(value=self.price_levis)
            self.price_combo_box.current(0)
            self.qty.set(1)
            
        if self.product_name_combo_box.get() == "Mufti":
            self.price_combo_box.config(value=self.price_mufti)
            self.price_combo_box.current(0)
            self.qty.set(1)
            
        # shirts
                    
        if self.product_name_combo_box.get() == "Peter England":
            self.price_combo_box.config(value=self.price_peter)
            self.price_combo_box.current(0)
            self.qty.set(1)
            
            
        if self.product_name_combo_box.get() == "Louis Philipe":
            self.price_combo_box.config(value=self.price_lousis)
            self.price_combo_box.current(0)
            self.qty.set(1)
            
            
        if self.product_name_combo_box.get() == "Park Avenue":
            self.price_combo_box.config(value=self.price_park)
            self.price_combo_box.current(0)
            self.qty.set(1)
            
        # t-shirts
                
        if self.product_name_combo_box.get() == "Polo":
            self.price_combo_box.config(value=self.price_polo)
            self.price_combo_box.current(0)
            self.qty.set(1)
            
        if self.product_name_combo_box.get() == "Roadstar":
            self.price_combo_box.config(value=self.price_roadstar)
            self.price_combo_box.current(0)
            self.qty.set(1)
            
        if self.product_name_combo_box.get() == "Jack & Jones":
            self.price_combo_box.config(value=self.price_park)
            self.price_combo_box.current(0)
            self.qty.set(1)
            
        # sneakers
        
        
        if self.product_name_combo_box.get() == "Addidas":
            self.price_combo_box.config(value=self.price_Addidas)
            self.price_combo_box.current(0)
            self.qty.set(1)
            
        if self.product_name_combo_box.get() == "Puma":
            self.price_combo_box.config(value=self.price_puma)
            self.price_combo_box.current(0)
            self.qty.set(1)
            
        if self.product_name_combo_box.get() == "Nike":
            self.price_combo_box.config(value=self.price_nike)
            self.price_combo_box.current(0)
            self.qty.set(1)
            
        # casual
        
        
        if self.product_name_combo_box.get() == "Bata":
            self.price_combo_box.config(value=self.price_bata)
            self.price_combo_box.current(0)
            self.qty.set(1)
        
        if self.product_name_combo_box.get() == "Red Chief":
            self.price_combo_box.config(value=self.price_red)
            self.price_combo_box.current(0)
            self.qty.set(1)
            
        if self.product_name_combo_box.get() == "Spark":
            self.price_combo_box.config(value=self.price_spark)
            self.price_combo_box.current(0)
            self.qty.set(1)
            
        # Boots 
        
        if self.product_name_combo_box.get() == "Liberty":
            self.price_combo_box.config(value=self.price_liberty)
            self.price_combo_box.current(0)
            self.qty.set(1)
        
        if self.product_name_combo_box.get() == "woodland":
            self.price_combo_box.config(value=self.price_woodland)
            self.price_combo_box.current(0)
            self.qty.set(1)
        
        if self.product_name_combo_box.get() == "Metro":
            self.price_combo_box.config(value=self.price_metro)
            self.price_combo_box.current(0)
            self.qty.set(1)
            
        # Iphone        
        
        
        if self.product_name_combo_box.get() == "Iphone 13":
            self.price_combo_box.config(value=self.price_13)
            self.price_combo_box.current(0)
            self.qty.set(1)
             
        if self.product_name_combo_box.get() == "Iphone 14":
            self.price_combo_box.config(value=self.price_14)
            self.price_combo_box.current(0)
            self.qty.set(1)
            
        if self.product_name_combo_box.get() == "Iphone 15":
            self.price_combo_box.config(value=self.price_15)
            self.price_combo_box.current(0)
            self.qty.set(1)
            
        # samsung
                 
        if self.product_name_combo_box.get() == "Galaxy A55":
            self.price_combo_box.config(value=self.price_A55)
            self.price_combo_box.current(0)
            self.qty.set(1)
            
        if self.product_name_combo_box.get() == "Galaxy A35":
            self.price_combo_box.config(value=self.price_A35)
            self.price_combo_box.current(0)
            self.qty.set(1)
            
        if self.product_name_combo_box.get() == "Galaxy M55":
            self.price_combo_box.config(value=self.price_M55)
            self.price_combo_box.current(0)
            self.qty.set(1)
            
        #Real Me
       
        if self.product_name_combo_box.get() == "Realme 12 pro":
            self.price_combo_box.config(value=self.price_12_pro)
            self.price_combo_box.current(0)
            self.qty.set(1)
            
        if self.product_name_combo_box.get() == "Realme Narzo":
            self.price_combo_box.config(value=self.price_narz0)
            self.price_combo_box.current(0)
            self.qty.set(1)
        
        if self.product_name_combo_box.get() == "Realme GT":
            self.price_combo_box.config(value=self.price_GT)
            self.price_combo_box.current(0)
            self.qty.set(1)
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        
        
        
        
        
        
        
        
        
                                  
        
        
if __name__ == "__main__":
    root=Tk()
    obj=Bill_App(root)
    root.mainloop()