from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox

class Cust_win:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        #=============Variables=================
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_cust_name=StringVar()
        self.var_cust_mother=StringVar()
        self.var_cust_gender=StringVar()
        self.var_cust_post=StringVar()
        self.var_cust_mobile=StringVar()
        self.var_cust_email=StringVar()
        self.var_cust_nationality=StringVar()
        self.var_cust_idproof=StringVar()
        self.var_cust_idnumber=StringVar()
        self.var_cust_address=StringVar()











        #=================Title======================

        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS", font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        #================logo========================

        img2=Image.open(r"F:\project\symbol1.jpg")
        img2=img2.resize((100,40),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)


        #================lebel frame===================

        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",font=("times new roman",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)


        #===============lables and entries=================
        #cust_ref

        lbl_cust_ref=Label(labelframeleft,text="Customer Ref:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)

        entry_ref=ttk.Entry(labelframeleft,textvariable=self.var_ref,width=29,font=("arial",13,"bold"),state="readonly")
        entry_ref.grid(row=0,column=1)

         #cust_name

        lbl_cust_ref=Label(labelframeleft,text="Customer Name:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=1,column=0,sticky=W)

        txtname=ttk.Entry(labelframeleft,textvariable=self.var_cust_name,width=29,font=("arial",13,"bold"))
        txtname.grid(row=1,column=1)


         #mother name

        lbl_cust_ref=Label(labelframeleft,text="Mother Name:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=2,column=0,sticky=W)

        txtmother=ttk.Entry(labelframeleft,textvariable=self.var_cust_mother,width=29,font=("arial",13,"bold"))
        txtmother.grid(row=2,column=1)


         #Gender

        lbl_cust_ref=Label(labelframeleft,text="Gender:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=3,column=0,sticky=W)
        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_cust_gender,font=("arial",12,"bold"),width=27,state="readonly")
        combo_gender["value"]=("Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)

        

        #Postcode

        lbl_cust_ref=Label(labelframeleft,text="Postcode:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=4,column=0,sticky=W)

        txtpass=ttk.Entry(labelframeleft,textvariable=self.var_cust_post,width=29,font=("arial",13,"bold"))
        txtpass.grid(row=4,column=1)

        #Mobno

        lbl_cust_ref=Label(labelframeleft,text="Mobile:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=5,column=0,sticky=W)

        txtmob=ttk.Entry(labelframeleft,textvariable=self.var_cust_mobile,width=29,font=("arial",13,"bold"))
        txtmob.grid(row=5,column=1)

        #email

        lbl_cust_ref=Label(labelframeleft,text="Email:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=6,column=0,sticky=W)

        txtemail=ttk.Entry(labelframeleft,textvariable=self.var_cust_email,width=29,font=("arial",13,"bold"))
        txtemail.grid(row=6,column=1)

        #natitality

        lbl_cust_ref=Label(labelframeleft,text="Nationality:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=7,column=0,sticky=W)
        combo_nat=ttk.Combobox(labelframeleft,textvariable=self.var_cust_nationality,font=("arial",12,"bold"),width=27,state="readonly")
        combo_nat["value"]=("India","British","American")
        combo_nat.current(0)
        combo_nat.grid(row=7,column=1)

        

        #idproof

        lbl_cust_ref=Label(labelframeleft,text="Id Proof Type:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=8,column=0,sticky=W)

        combo_id=ttk.Combobox(labelframeleft,textvariable=self.var_cust_idproof,font=("arial",12,"bold"),width=27,state="readonly")
        combo_id["value"]=("AadharCard","DrivringLicence","Passport")
        combo_id.current(0)
        combo_id.grid(row=8,column=1)

        


        #idno

        lbl_cust_ref=Label(labelframeleft,text="Id Number:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=9,column=0,sticky=W)

        txtid=ttk.Entry(labelframeleft,textvariable=self.var_cust_idnumber,width=29,font=("arial",13,"bold"))
        txtid.grid(row=9,column=1)

        #address

        lbl_cust_ref=Label(labelframeleft,text="Address:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=10,column=0,sticky=W)

        txtaddress=ttk.Entry(labelframeleft,textvariable=self.var_cust_address,width=29,font=("arial",13,"bold"))
        txtaddress.grid(row=10,column=1)


        #=====================btn==============================

        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btn_add=Button(btn_frame,text="ADD",command=self.add_data,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btn_add.grid(row=0,column=0,padx=1)

        btn_update=Button(btn_frame,text="UPDATE",command=self.update,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btn_update.grid(row=0,column=1,padx=1)

        btn_delete=Button(btn_frame,text="DELETE",command=self.mDelete,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btn_delete.grid(row=0,column=2,padx=1)

        btn_reset=Button(btn_frame,text="RESET",command=self.reset,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btn_reset.grid(row=0,column=3,padx=1)


        #=================table frame============================

        Table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",font=("times new roman",12,"bold"),padx=2)
        Table_frame.place(x=435,y=50,width=860,height=490)


        labelSearchBy=Label(Table_frame,text="Search By:",bg="red",fg="white",font=("arial",12,"bold"))
        labelSearchBy.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var=StringVar()

        combo_search=ttk.Combobox(Table_frame,textvariable=self.search_var,font=("arial",12,"bold"),width=24,state="readonly")
        combo_search["value"]=("Mobile","Ref")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)

        self.txt_search=StringVar()

        txtSearch=ttk.Entry(Table_frame,width=24,textvariable=self.txt_search,font=("arial",13,"bold"))
        txtSearch.grid(row=0,column=2,padx=2)

        btn_search=Button(Table_frame,text="SEARCH",command=self.search,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btn_search.grid(row=0,column=3,padx=1)

        btn_Showall=Button(Table_frame,text="SHOW ALL",command=self.fetch_data,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btn_Showall.grid(row=0,column=4,padx=1)


        #=================show data table===============

        detail_table=Frame(Table_frame,bd=2,relief=RIDGE)
        detail_table.place(x=0,y=50,width=860,height=350)



        scroll_x=ttk.Scrollbar(detail_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(detail_table,orient=VERTICAL)

        self.Cust_Details_Table=ttk.Treeview(detail_table,column=("ref","name","mother","gender","post","mobile","email","nationality","idproof","idnumber","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("ref",text="Refer No")
        self.Cust_Details_Table.heading("name",text="name")
        self.Cust_Details_Table.heading("mother",text="Mother Nmae")
        self.Cust_Details_Table.heading("gender",text="Gender")
        self.Cust_Details_Table.heading("post",text="Postcode")
        self.Cust_Details_Table.heading("mobile",text="Mobile")
        self.Cust_Details_Table.heading("email",text="Email")
        self.Cust_Details_Table.heading("nationality",text="Nationality")
        self.Cust_Details_Table.heading("idproof",text="Id proof")
        self.Cust_Details_Table.heading("idnumber",text="Id Number")
        self.Cust_Details_Table.heading("address",text="Address")

        self.Cust_Details_Table["show"]="headings"

        self.Cust_Details_Table.column("ref",width=100)
        self.Cust_Details_Table.column("name",width=100)
        self.Cust_Details_Table.column("mother",width=100)
        self.Cust_Details_Table.column("gender",width=100)
        self.Cust_Details_Table.column("post",width=100)
        self.Cust_Details_Table.column("mobile",width=100)
        self.Cust_Details_Table.column("email",width=100)
        self.Cust_Details_Table.column("nationality",width=100)
        self.Cust_Details_Table.column("idproof",width=100)
        self.Cust_Details_Table.column("idnumber",width=100)
        self.Cust_Details_Table.column("address",width=100)
        
        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


    def add_data(self):
        if self.var_cust_mobile.get()=="" or self.var_cust_mother.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:
            try:
            
                conn=mysql.connector.connect(host="localhost",user="root",password="root",database="python")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_ref.get(),self.var_cust_name.get(),self.var_cust_mother.get(),self.var_cust_gender.get(),self.var_cust_post.get(),self.var_cust_mobile.get(),self.var_cust_email.get(),self.var_cust_nationality.get(),self.var_cust_idproof.get(),self.var_cust_idnumber.get(),self.var_cust_address.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Customer has been added",parent=self.root)
            
            



               
            except Exception as es:
                messagebox.showwarning("Warning",f"Something Went Wrong:{str(es)}",parent=self.root)


    def fetch_data(self):

        conn=mysql.connector.connect(host="localhost",user="root",password="root",database="python")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
        conn.commit()
        conn.close()


    def get_cursor(self,event=""):
        cursor_row=self.Cust_Details_Table.focus()
        content=self.Cust_Details_Table.item(cursor_row)
        row=content["values"]

        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_cust_mother.set(row[2]),
        self.var_cust_gender.set(row[3]),
        self.var_cust_post.set(row[4]),
        self.var_cust_mobile.set(row[5]),
        self.var_cust_email.set(row[6]),
        self.var_cust_nationality.set(row[7]),
        self.var_cust_idproof.set(row[8]),
        self.var_cust_idnumber.set(row[9]),
        self.var_cust_address.set(row[10])
    
    def update(self):
        if self.var_cust_mobile.get()=="":
            messagebox.showerror("Error","Please enter Mobile Number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="root",database="python")
            my_cursor=conn.cursor()
            my_cursor.execute("update customer set Name=%s,Mother=%s,Gender=%s,Post=%s,Mobile=%s,Email=%s,Nationality=%s,IdProof=%s,IdNumber=%s,Address=%s where Ref=%s",(self.var_cust_name.get(),self.var_cust_mother.get(),self.var_cust_gender.get(),self.var_cust_post.get(),self.var_cust_mobile.get(),self.var_cust_email.get(),self.var_cust_nationality.get(),self.var_cust_idproof.get(),self.var_cust_idnumber.get(),self.var_cust_address.get(),self.var_ref.get()))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Customer Details has been Updated Successfully",parent=self.root)

    def mDelete(self):

        mDelete=messagebox.askyesno("Hotel Management System", "Do You want delete this customer",parent=self.root)
        if mDelete:
            conn=mysql.connector.connect(host="localhost",user="root",password="root",database="python")
            my_cursor=conn.cursor()
            query="delete from customer where Ref=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:

            if not mDelete:

                return

        
        conn.commit()
        self.fetch_data()
        conn.close()
    
    def reset(self):
        #self.var_ref.set(""),
        self.var_cust_name.set(""),
        self.var_cust_mother.set(""),
        #self.var_cust_gender.set(""),
        self.var_cust_post.set(""),
        self.var_cust_mobile.set(""),
        self.var_cust_email.set(""),
        #self.var_cust_nationality.set(""),
        #self.var_cust_idproof.set(""),
        self.var_cust_idnumber.set(""),
        self.var_cust_address.set("")
         
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

    def search(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="root",database="python")
        my_cursor=conn.cursor()

        my_cursor.execute("select * from customer where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len (rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()




        
        













        
        
        

        



if __name__ == "__main__":
    root=Tk()
    obj=Cust_win(root)
    root.mainloop()

