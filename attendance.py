from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self,root): 
        self.root=root
        self.root.geometry("1350x690+0+0")
        self.root.title("Addendance Records")
        
        ########### variables############
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()
                  
        # image  
        img=Image.open(r"C:\Users\rajan\OneDrive\Pictures\pho.png")
        img=img.resize((500,150),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=450,height=150)
         #image2
        img2=Image.open(r"C:\Users\rajan\OneDrive\Pictures\pho2.jpg")
        img2=img2.resize((450,150),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
    
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=450,y=0,width=450,height=150)
        #image3
        img3=Image.open(r"C:\Users\rajan\OneDrive\Pictures\pho3.png")
        img3=img3.resize((450,150),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=900,y=0,width=450,height=150)  
               
         # bg image 4
        img4=Image.open(r"C:\Users\rajan\OneDrive\Pictures\pho4.jpg")
        img4=img4.resize((1350,690),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=150,width=1350,height=690)
        
        title_lbl=Label(bg_img,text="Attendence !",font=("times new roman",30,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1350,height=50)
        
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=5,y=60,width=1335,height=470)
                
        # left frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Detail",font=("times new roman",12,"bold"))
        Left_frame.place(x=15,y=10,width=630,height=450)
        
        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=5,y=10,width=620,height=300)

        #Attendance  ID
        attendanceId_label=Label(left_inside_frame,text="Attendacne ID:",font=("times new roman",12,"bold"),bg="white")
        attendanceId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        attendanceId_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("times new roman",12,"bold"))
        attendanceId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        
        #name
        rollLabel=Label(left_inside_frame,text="Roll :",font=("times new roman",12,"bold"),bg="white")
        rollLabel.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        atten_roll=ttk.Entry(left_inside_frame,width=18,textvariable=self.var_atten_roll,font=("times new roman",12,"bold"))
        atten_roll.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        
        #date        
        nameLabel=Label(left_inside_frame,text="Name:",font=("times new roman",12,"bold"),bg="white")
        nameLabel.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
        atten_name=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_name,font=("times new roman",12,"bold"))
        atten_name.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
        #department
        depLabel=Label(left_inside_frame,text="Department:",font=("times new roman",12,"bold"),bg="white")
        depLabel.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        
        atten_dep=ttk.Entry(left_inside_frame,width=18,textvariable=self.var_atten_dep,font=("times new roman",12,"bold"))
        atten_dep.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        
        #time
        timeLabel=Label(left_inside_frame,text="Time:",font=("times new roman",12,"bold"),bg="white")
        timeLabel.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        
        atten_time=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_time,font=("times new roman",12,"bold"))
        atten_time.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        
        #date
        dateLabel=Label(left_inside_frame,text="Date:",font=("times new roman",12,"bold"),bg="white")
        dateLabel.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        
        atten_date=ttk.Entry(left_inside_frame,width=18,textvariable=self.var_atten_date,font=("times new roman",12,"bold"))
        atten_date.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        
        #attendeance
        attendanceLabel=Label(left_inside_frame,text="Attendacne Status:",font=("times new roman",12,"bold"),bg="white")
        attendanceLabel.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        
        self.atten_status=ttk.Combobox(left_inside_frame,width=20,textvariable=self.var_atten_attendance,font="comicsansns 11 bold",state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=10)
        self.atten_status.current(0)
        
        # button
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=2,y=200,width=600,height=38)
        
        save_btn=Button(btn_frame,text="Import csv",width=21,command=self.importCsv,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0) 
        
        update_btn=Button(btn_frame,text="Export csv",width=21,command=self.exportCsv,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1) 
            
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=21,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)  
        
        #right frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Record",font=("times new roman",12,"bold"))
        Right_frame.place(x=665,y=10,width=630,height=450)
        
        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=620,height=380)
        
        #scrollbar
        scoll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scoll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.AttendanceReportTable=ttk.Treeview(table_frame,columns=("id","roll","name","department","time","date","attendance"),xscrollcommand=scoll_x.set,yscrollcommand=scoll_y.set)
        
        scoll_x.pack(side=BOTTOM,fill=X)
        scoll_y.pack(side=RIGHT,fill=Y)
        
        scoll_x.config(command=self.AttendanceReportTable.xview)
        scoll_y.config(command=self.AttendanceReportTable.yview)    
        
        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")        
        self.AttendanceReportTable["show"]="headings" 
        self.AttendanceReportTable.column("id",width=100)  
        self.AttendanceReportTable.column("roll",width=50)
        self.AttendanceReportTable.column("name",width=150)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)
        
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
        ###  fetch data ################
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
    
    #import csv        
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="open CSV",filetypes=(("CSV File","*.csv"),("All file","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)                       
                    
     #   export csv
     
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to Export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="open CSV",filetypes=(("CSV File","*.csv"),("All file","*.*")),parent=self.root)
            with open(fln, mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i) 
                messagebox.showinfo("Data Export","Your Data Exported to "+os.path.basename(fln)+"Successfully")
        except Exception as es:
            messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)        
        
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])
        
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")
        
if __name__=="__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()