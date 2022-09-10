from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox

class DetailsRoom:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

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

        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="New Room Add",font=("times new roman",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=540,height=350)

         #===============lables and entries=================

        #Floor

        lbl_floor=Label(labelframeleft,text="Floor",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_floor.grid(row=0,column=0,sticky=W)

        self.var_floor=StringVar()

        entry_floor=ttk.Entry(labelframeleft,textvariable=self.var_floor,width=20,font=("arial",13,"bold"))
        entry_floor.grid(row=0,column=1,sticky=W)

        #room no

        lbl_floor=Label(labelframeleft,text="Room No",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_floor.grid(row=1,column=0,sticky=W)
        self.var_RoomNo=StringVar()


        entry_floor=ttk.Entry(labelframeleft,textvariable=self.var_RoomNo,width=20,font=("arial",13,"bold"))
        entry_floor.grid(row=1,column=1,sticky=W)

        #room type

        lbl_floor=Label(labelframeleft,text="Room Type",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_floor.grid(row=2,column=0,sticky=W)

        self.var_RoomType=StringVar()

        entry_floor=ttk.Entry(labelframeleft,textvariable=self.var_RoomType,width=20,font=("arial",13,"bold"))
        entry_floor.grid(row=2,column=1,sticky=W)



        #=============btns==================================

        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=412,height=40)

        btn_add=Button(btn_frame,text="ADD",command=self.add_data,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btn_add.grid(row=0,column=0,padx=1)

        btn_update=Button(btn_frame,text="UPDATE",command=self.update,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btn_update.grid(row=0,column=1,padx=1)

        btn_delete=Button(btn_frame,text="DELETE",command=self.mDelete,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btn_delete.grid(row=0,column=2,padx=1)

        btn_reset=Button(btn_frame,text="RESET",command=self.reset,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btn_reset.grid(row=0,column=3,padx=1)


        #=================table frame system============================

        Table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Show Room Details",font=("times new roman",12,"bold"),padx=2)
        Table_frame.place(x=600,y=55,width=600,height=350)

        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.room_table=ttk.Treeview(Table_frame,column=("floor","roomno","roomType"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("floor",text="Floor")
        self.room_table.heading("roomno",text="Room_No")
        self.room_table.heading("roomType",text="Room_Type")
        

        self.room_table["show"]="headings"

        self.room_table.column("floor",width=100)
        self.room_table.column("roomno",width=100)
        self.room_table.column("roomType",width=100)
        
        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    #add data
    def add_data(self):
        if self.var_floor.get()=="" or self.var_RoomType.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:
            try:
            
                conn=mysql.connector.connect(host="localhost",user="root",password="root",database="python")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into details values(%s,%s,%s)",(self.var_floor.get(),self.var_RoomNo.get(),self.var_RoomType.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","New Room Added Successfully",parent=self.root)
  
            except Exception as es:
                messagebox.showwarning("Warning",f"Something Went Wrong:{str(es)}",parent=self.root)

    # fetch data
    def fetch_data(self):

        conn=mysql.connector.connect(host="localhost",user="root",password="root",database="python")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from details")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
        conn.commit()
        conn.close() 
        #get cursor

    def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"] 

        self.var_floor.set(row[0])
        self.var_RoomNo.set(row[1])
        self.var_RoomType.set(row[2])

    #updateFunction
    def update(self):
        if self.var_floor.get()=="":
            messagebox.showerror("Error","Please enter Floor Number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="root",database="python")
            my_cursor=conn.cursor()
            my_cursor.execute("update details set Floor=%s,Room_Type=%s where Room_No=%s",(self.var_floor.get(),self.var_RoomType.get(),self.var_RoomNo.get()))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Room Details has been Updated Successfully",parent=self.root)

        #delete
    def mDelete(self):

        mDelete=messagebox.askyesno("Hotel Management System", "Do You want delete this RoomDetails",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",user="root",password="root",database="python")
            my_cursor=conn.cursor()
            query="delete from details where Room_No=%s"
            value=(self.var_RoomNo.get(),)
            my_cursor.execute(query,value)
        else:

            if not mDelete:

                return

        
        conn.commit()
        self.fetch_data()
        conn.close()
        #reset
    def reset(self): 
        self.var_floor.set("")
        self.var_RoomNo.set("")
        self.var_RoomType.set("")








if __name__ == "__main__":
    root=Tk()
    obj=DetailsRoom(root)
    root.mainloop()
