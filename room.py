from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox

class RoomBooking:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")


        #========================variable=====================
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()

        #=================Title======================

        lbl_title=Label(self.root,text="ROOMBOOKING DETAILS", font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        #================logo========================

        img2=Image.open(r"F:\project\symbol1.jpg")
        img2=img2.resize((100,40),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)

         #================lebel frame===================

        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="RoomBooking Details",font=("times new roman",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)

         #===============lables and entries=================
        #cust_contact

        lbl_cust_contact=Label(labelframeleft,text="Customer Contact:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)

        entry_contact=ttk.Entry(labelframeleft,width=20,textvariable=self.var_contact,font=("arial",13,"bold"))
        entry_contact.grid(row=0,column=1,sticky=W)

        #=================fetch data Button==================

        btn_fetchdata=Button(labelframeleft,text="Fetch Data",command=self.Fetch_contact,font=("arial",8,"bold"),bg="black",fg="gold",width=8)
        btn_fetchdata.place(x=347,y=4)



         #check_in_date

        check_in_date=Label(labelframeleft,text="Chech_in Date:",font=("arial",12,"bold"),padx=2,pady=6)
        check_in_date.grid(row=1,column=0,sticky=W)

        txtcheck_in_date=ttk.Entry(labelframeleft,width=29,textvariable=self.var_checkin,font=("arial",13,"bold"))
        txtcheck_in_date.grid(row=1,column=1)


         #check_out_date

        check_out_date=Label(labelframeleft,text="Check_out Date",font=("arial",12,"bold"),padx=2,pady=6)
        check_out_date.grid(row=2,column=0,sticky=W)

        txtcheck_out_date=ttk.Entry(labelframeleft,width=29,textvariable=self.var_checkout,font=("arial",13,"bold"))
        txtcheck_out_date.grid(row=2,column=1)

        #room type

        check_RoomType=Label(labelframeleft,text=" Room Type",font=("arial",12,"bold"),padx=2,pady=6)
        check_RoomType.grid(row=3,column=0,sticky=W)

        conn=mysql.connector.connect(host="localhost",user="root",password="root",database="python")
        my_cursor=conn.cursor()
        my_cursor.execute("select Room_Type from details")
        ide=my_cursor.fetchall()

        combo_RoomType=ttk.Combobox(labelframeleft,textvariable=self.var_roomtype,font=("arial",12,"bold"),width=27,state="readonly")
        combo_RoomType["value"]=ide
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3,column=1)



        #AvailableRoom

        lblRoomAvailable=Label(labelframeleft,text="Available Room:",font=("arial",12,"bold"),padx=2,pady=6)
        lblRoomAvailable.grid(row=4,column=0,sticky=W)
       # txtRoomAvailable=ttk.Entry(labelframeleft,width=29,textvariable=self.var_roomavailable,font=("arial",13,"bold"))
        #txtRoomAvailable.grid(row=4,column=1)

        conn=mysql.connector.connect(host="localhost",user="root",password="root",database="python")
        my_cursor=conn.cursor()
        my_cursor.execute("select Room_No from details")
        rows=my_cursor.fetchall()

        combo_RoomNo=ttk.Combobox(labelframeleft,textvariable=self.var_roomavailable,font=("arial",12,"bold"),width=27,state="readonly")
        combo_RoomNo["value"]=rows
        combo_RoomNo.current(0)
        combo_RoomNo.grid(row=4,column=1)


        #Meal

        lblMeal=Label(labelframeleft,text="Meal:",font=("arial",12,"bold"),padx=2,pady=6)
        lblMeal.grid(row=5,column=0,sticky=W)
        txtMeal=ttk.Entry(labelframeleft,width=29,textvariable=self.var_meal,font=("arial",13,"bold"))
        txtMeal.grid(row=5,column=1)

        #no of days

        lblNoOfDays=Label(labelframeleft,text="No Of Days:",font=("arial",12,"bold"),padx=2,pady=6)
        lblNoOfDays.grid(row=6,column=0,sticky=W)
        txtNoOfDays=ttk.Entry(labelframeleft,width=29,textvariable=self.var_noofdays,font=("arial",13,"bold"))
        txtNoOfDays.grid(row=6,column=1)

        #paid tax

        lblNoOfDays=Label(labelframeleft,text="Paid Tax:",font=("arial",12,"bold"),padx=2,pady=6)
        lblNoOfDays.grid(row=7,column=0,sticky=W)
        txtNoOfDays=ttk.Entry(labelframeleft,width=29,textvariable=self.var_paidtax,font=("arial",13,"bold"))
        txtNoOfDays.grid(row=7,column=1)

         #sub total

        lblNoOfDays=Label(labelframeleft,text="Sub Total:",font=("arial",12,"bold"),padx=2,pady=6)
        lblNoOfDays.grid(row=8,column=0,sticky=W)
        txtNoOfDays=ttk.Entry(labelframeleft,width=29,textvariable=self.var_actualtotal,font=("arial",13,"bold"))
        txtNoOfDays.grid(row=8,column=1)

         # total cost

        lblNoOfDays=Label(labelframeleft,text="Total Cost:",font=("arial",12,"bold"),padx=2,pady=6)
        lblNoOfDays.grid(row=9,column=0,sticky=W)
        txtNoOfDays=ttk.Entry(labelframeleft,width=29,textvariable=self.var_total,font=("arial",13,"bold"))
        txtNoOfDays.grid(row=9,column=1)


        #=====================Bill btn==================
        btnBill=Button(labelframeleft,text="Bill",command=self.total,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnBill.grid(row=10,column=0,padx=1,sticky=W)



        #=============btns==================================

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



        #====================right side img=============================
        img3=Image.open(r"F:\project\bed.jpg")
        img3=img3.resize((520,300),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg=Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE)
        lblimg.place(x=760,y=55,width=520,height=200)

         #=================table frame system============================

        Table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",font=("times new roman",12,"bold"),padx=2)
        Table_frame.place(x=435,y=280,width=860,height=260)


        labelSearchBy=Label(Table_frame,text="Search By:",bg="red",fg="white",font=("arial",12,"bold"))
        labelSearchBy.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var=StringVar()

        combo_search=ttk.Combobox(Table_frame,textvariable=self.search_var,font=("arial",12,"bold"),width=24,state="readonly")
        combo_search["value"]=("Contact","Roomavailable")
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
        detail_table.place(x=0,y=50,width=860,height=180)



        scroll_x=ttk.Scrollbar(detail_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(detail_table,orient=VERTICAL)

        self.room_table=ttk.Treeview(detail_table,column=("contact","checkin","checkout","roomtype","roomavailable","meal","noofdays"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("contact",text="Contact")
        self.room_table.heading("checkin",text="Check-in")
        self.room_table.heading("checkout",text="Check-out")
        self.room_table.heading("roomtype",text="Room Type")
        self.room_table.heading("roomavailable",text="Room No")
        self.room_table.heading("meal",text="Meal")
        self.room_table.heading("noofdays",text="NoOfDays")
        

        self.room_table["show"]="headings"

        self.room_table.column("contact",width=100)
        self.room_table.column("checkin",width=100)
        self.room_table.column("checkout",width=100)
        self.room_table.column("roomtype",width=100)
        self.room_table.column("roomavailable",width=100)
        self.room_table.column("meal",width=100)
        self.room_table.column("noofdays",width=100)
        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


    #add data
    def add_data(self):
        if self.var_contact.get()=="" or self.var_checkin.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:
            try:
            
                conn=mysql.connector.connect(host="localhost",user="root",password="root",database="python")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(self.var_contact.get(),self.var_checkin.get(),self.var_checkout.get(),self.var_roomtype.get(),self.var_roomavailable.get(),self.var_meal.get(),self.var_noofdays.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Room Booked",parent=self.root)
  
            except Exception as es:
                messagebox.showwarning("Warning",f"Something Went Wrong:{str(es)}",parent=self.root)
    # fetch data
    def fetch_data(self):

        conn=mysql.connector.connect(host="localhost",user="root",password="root",database="python")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
        conn.commit()
        conn.close() 
        #getcursor
    def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"] 

        self.var_contact.set(row[0])
        self.var_checkin.set(row[1])
        self.var_checkout.set(row[2])  
        self.var_roomtype.set(row[3])
        self.var_roomavailable.set(row[4])
        self.var_meal.set(row[5])
        self.var_noofdays.set(row[6]) 

      #updateFunction
    def update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter Mobile Number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="root",database="python")
            my_cursor=conn.cursor()
            my_cursor.execute("update room set Check_in=%s,Check_out=%s,Roomtype=%s,Roomavailable=%s,Meal=%s,Noofdays=%s where Contact=%s",(self.var_checkin.get(),self.var_checkout.get(),self.var_roomtype.get(),self.var_roomavailable.get(),self.var_meal.get(),self.var_noofdays.get(),self.var_contact.get()))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Room Details has been Updated Successfully",parent=self.root)

            
      #detelet Function
    def mDelete(self):

        mDelete=messagebox.askyesno("Hotel Management System", "Do You want delete this customer",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",user="root",password="root",database="python")
            my_cursor=conn.cursor()
            query="delete from room where Contact=%s"
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
        else:

            if not mDelete:

                return

        
        conn.commit()
        self.fetch_data()
        conn.close() 

    def reset(self): 
        self.var_contact.set("")
        self.var_checkin.set("")
        self.var_checkout.set("")  
        self.var_roomtype.set("")
        self.var_roomavailable.set("")
        self.var_meal.set("")
        self.var_noofdays.set("") 
        self.var_paidtax.set("")
        self.var_actualtotal.set("")
        self.var_total.set("")
 


        #===================all data fetch================

    def Fetch_contact(self):
      if self.var_contact.get()=="":
        messagebox.showerror("Error","Please Enter Contact Number",parent=self.root)
      else:
        conn=mysql.connector.connect(host="localhost",user="root",password="root",database="python")
        my_cursor=conn.cursor()
        query=("select Name from customer where Mobile=%s")
        value=(self.var_contact.get(),)
        my_cursor.execute(query,value)
        row=my_cursor.fetchone()

        if row==None:
          messagebox.showerror("Error","This Number Not Found",parent=self.root)
        else:
          conn.commit()
          conn.close()

          showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
          showDataframe.place(x=450,y=55,width=300,height=180)

          lblName=Label(showDataframe,text="Name:",font=("arial",12,"bold"))
          lblName.place(x=0,y=0)

          lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
          lbl.place(x=90,y=0)

          conn=mysql.connector.connect(host="localhost",user="root",password="root",database="python")
          my_cursor=conn.cursor()
          query=("select Gender from customer where Mobile=%s")
          value=(self.var_contact.get(),)
          my_cursor.execute(query,value)
          row=my_cursor.fetchone()
          lblGender=Label(showDataframe,text="Gender:",font=("arial",12,"bold"))
          lblGender.place(x=0,y=30)

          lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
          lbl.place(x=90,y=30)

          conn=mysql.connector.connect(host="localhost",user="root",password="root",database="python")
          my_cursor=conn.cursor()
          query=("select Email from customer where Mobile=%s")
          value=(self.var_contact.get(),)
          my_cursor.execute(query,value)
          row=my_cursor.fetchone()
          lblGender=Label(showDataframe,text="Email:",font=("arial",12,"bold"))
          lblGender.place(x=0,y=60)

          lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
          lbl.place(x=90,y=60)

          conn=mysql.connector.connect(host="localhost",user="root",password="root",database="python")
          my_cursor=conn.cursor()
          query=("select Nationality from customer where Mobile=%s")
          value=(self.var_contact.get(),)
          my_cursor.execute(query,value)
          row=my_cursor.fetchone()
          lblGender=Label(showDataframe,text="Nationality:",font=("arial",12,"bold"))
          lblGender.place(x=0,y=90)

          lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
          lbl.place(x=90,y=90)

          conn=mysql.connector.connect(host="localhost",user="root",password="root",database="python")
          my_cursor=conn.cursor()
          query=("select Address from customer where Mobile=%s")
          value=(self.var_contact.get(),)
          my_cursor.execute(query,value)
          row=my_cursor.fetchone()
          lblGender=Label(showDataframe,text="Address:",font=("arial",12,"bold"))
          lblGender.place(x=0,y=120)

          lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
          lbl.place(x=90,y=120)

    #============Search===============
    def search(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="root",database="python")
        my_cursor=conn.cursor()

        my_cursor.execute("select * from room where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len (rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def total(self):
      inDate=self.var_checkin.get()
      outDate=self.var_checkout.get()
      inDate=datetime.strptime(inDate,"%d/%m/%Y")
      outDate=datetime.strptime(outDate,"%d/%m/%Y")
      self.var_noofdays.set(abs(outDate-inDate).days)

      if (self.var_meal.get()=="BreakFast" and self.var_roomtype.get()=="laxary"):
        q1=float(300)
        q2=float(700)
        q3=float(self.var_noofdays.get())
        q4=float(q1+q2)
        q5=float(q3+q4)
        Tax="Rs."+str("%.2f"%((q5)*0.1))
        ST="Rs."+str("%.2f"%((q5)))
        TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
        self.var_paidtax.set(Tax)
        self.var_actualtotal.set(ST)
        self.var_total.set(TT)

      elif (self.var_meal.get()=="BreakFast" and self.var_roomtype.get()=="Single"):
        q1=float(300)
        q2=float(500)
        q3=float(self.var_noofdays.get())
        q4=float(q1+q2)
        q5=float(q3+q4)
        Tax="Rs."+str("%.2f"%((q5)*0.1))
        ST="Rs."+str("%.2f"%((q5)))
        TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
        self.var_paidtax.set(Tax)
        self.var_actualtotal.set(ST)
        self.var_total.set(TT)
      elif (self.var_meal.get()=="BreakFast" and self.var_roomtype.get()=="Double"):
        q1=float(300)
        q2=float(600)
        q3=float(self.var_noofdays.get())
        q4=float(q1+q2)
        q5=float(q3+q4)
        Tax="Rs."+str("%.2f"%((q5)*0.1))
        ST="Rs."+str("%.2f"%((q5)))
        TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
        self.var_paidtax.set(Tax)
        self.var_actualtotal.set(ST)
        self.var_total.set(TT)

     

      elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Single"):
        q1=float(1000)
        q2=float(500)
        q3=float(self.var_noofdays.get())
        q4=float(q1+q2)
        q5=float(q3+q4)
        Tax="Rs."+str("%.2f"%((q5)*0.1))
        ST="Rs."+str("%.2f"%((q5)))
        TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
        self.var_paidtax.set(Tax)
        self.var_actualtotal.set(ST)
        self.var_total.set(TT)
      elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Double"):
        q1=float(1000)
        q2=float(600)
        q3=float(self.var_noofdays.get())
        q4=float(q1+q2)
        q5=float(q3+q4)
        Tax="Rs."+str("%.2f"%((q5)*0.1))
        ST="Rs."+str("%.2f"%((q5)))
        TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
        self.var_paidtax.set(Tax)
        self.var_actualtotal.set(ST)
        self.var_total.set(TT)
      elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="laxary"):
        q1=float(1000)
        q2=float(700)
        q3=float(self.var_noofdays.get())
        q4=float(q1+q2)
        q5=float(q3+q4)
        Tax="Rs."+str("%.2f"%((q5)*0.1))
        ST="Rs."+str("%.2f"%((q5)))
        TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
        self.var_paidtax.set(Tax)
        self.var_actualtotal.set(ST)
        self.var_total.set(TT)



      elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Double"):
        q1=float(900)
        q2=float(600)
        q3=float(self.var_noofdays.get())
        q4=float(q1+q2)
        q5=float(q3+q4)
        Tax="Rs."+str("%.2f"%((q5)*0.1))
        ST="Rs."+str("%.2f"%((q5)))
        TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
        self.var_paidtax.set(Tax)
        self.var_actualtotal.set(ST)
        self.var_total.set(TT)

      elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Single"):
        q1=float(900)
        q2=float(500)
        q3=float(self.var_noofdays.get())
        q4=float(q1+q2)
        q5=float(q3+q4)
        Tax="Rs."+str("%.2f"%((q5)*0.1))
        ST="Rs."+str("%.2f"%((q5)))
        TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
        self.var_paidtax.set(Tax)
        self.var_actualtotal.set(ST)
        self.var_total.set(TT)

      elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="laxary"):
        q1=float(900)
        q2=float(700)
        q3=float(self.var_noofdays.get())
        q4=float(q1+q2)
        q5=float(q3+q4)
        Tax="Rs."+str("%.2f"%((q5)*0.1))
        ST="Rs."+str("%.2f"%((q5)))
        TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
        self.var_paidtax.set(Tax)
        self.var_actualtotal.set(ST)
        self.var_total.set(TT)






          


















if __name__ == "__main__":
    root=Tk()
    obj=RoomBooking(root)
    root.mainloop()

