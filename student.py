from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self,root): 
        self.root=root
        self.root.geometry("1350x690+0+0")
        self.root.title("Student")
           
        # ========variables=======      
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.va_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_phone=StringVar()
        self.var_photo=StringVar()
            
         #image1
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
        
        title_lbl=Label(bg_img,text="Student Detail !",font=("times new roman",30,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1350,height=50)
        
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=5,y=60,width=1335,height=470)
        
        #left label frame
        
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Detail",font=("times new roman",12,"bold"))
        Left_frame.place(x=15,y=10,width=630,height=450)
                
        #current course
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Course Information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=7,y=10,width=610,height=130)
        
        #course
        
        course_label=Label(current_course_frame,text="Course:",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=0,padx=10,sticky=W)
             
        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="read only")
        course_combo["values"]=("Select Course","MCA","MBA","M.Tech","M.Pharma", "M.sc Ag")
        course_combo.current(0)
        course_combo.grid(row=0,column=1,padx=2,pady=2,sticky=W) 
        
        #Department
        
        dep_label=Label(current_course_frame,text="Department:",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=2,padx=10,sticky=W)
        
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="read only")
        dep_combo["values"]=("Select Department","Computer Application","IT","CS","Finance","Marketing","HR","Pharmaceutics","Clinical Pharmacy","Gentics")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
        
        # year
        year_label=Label(current_course_frame,text="Year:",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)
        
        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="read only")
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W) 
        
        # Semester
        semester_label=Label(current_course_frame,text="Semester:",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)
        
        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="read only")
        semester_combo["values"]=("Select Semester","1","2","3","4")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W) 
        
        #Student Information
        student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Student Information",font=("times new roman",12,"bold"))
        student_frame.place(x=7,y=150,width=610,height=265)
        #student ID
        studentId_label=Label(student_frame,text="Student ID:",font=("times new roman",12,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,sticky=W)
        
        studentId_entry=ttk.Entry(student_frame,textvariable=self.va_std_id,width=20,font=("times new roman",12,"bold"))
        studentId_entry.grid(row=0,column=1,padx=10,sticky=W)
        
        #Stdent name
        studentName_label=Label(student_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        studentName_entry=ttk.Entry(student_frame,textvariable=self.var_std_name,width=17,font=("times new roman",12,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        
        #phone Number
        phone_label=Label(student_frame,text="Phone no.:",font=("times new roman",12,"bold"),bg="white")
        phone_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
        phone_entry=ttk.Entry(student_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        phone_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
        #roll number
        roll_label=Label(student_frame,text="Roll No.:",font=("times new roman",12,"bold"),bg="white")
        roll_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        
        roll_entry=ttk.Entry(student_frame,textvariable=self.var_roll,width=15,font=("times new roman",12,"bold"))
        roll_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        
        #Gender
        gender_label=Label(student_frame,text="Gender:",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
                
        gender_combo=ttk.Combobox(student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="read only")
        gender_combo["values"]=("Select Gender","Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W) 
        
        #DOB
        dob_label=Label(student_frame,text="DOB:",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)        
        dob_entry=ttk.Entry(student_frame,textvariable=self.var_dob,width=15,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        
       #Radio Button
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=4,column=0)  
        radiobtn2=ttk.Radiobutton(student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=4,column=1)
         
        # button frame
        
        btn_frame=Frame(student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=2,y=155,width=600,height=80)        
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=16,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0) 
        
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=16,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1) 
        
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=16,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)
        
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=16,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)  
        
        #button frame for 2 line
        btn_frame1=Frame(student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=2,y=190,width=600,height=80)
        
        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo",width=65 ,font=("times new roman",12,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)  
                        
        #right label frame
        
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Detail",font=("times new roman",12,"bold"))
        Right_frame.place(x=665,y=10,width=630,height=450)
                
        #table frame
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=0,y=30,width=625,height=350)
        
        scroll_x=ttk.Scrollbar (table_frame, orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar (table_frame, orient=VERTICAL)
        self.student_table=ttk. Treeview(table_frame,column=("dep","course","year","sem","id","name","roll","gender","dob","phone","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("roll", text="Roll no")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("photo", text="Photo")
          
        self.student_table["show"]="headings"
        
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=50)
        self.student_table.column("dob",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("photo",width=50)
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
        #--------->>>Function for Adding data base<<<<<-------------
    
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                    self.var_dep.get(),
                                                                                    self.var_course.get(),
                                                                                    self.var_year.get(),
                                                                                    self.var_semester.get(),
                                                                                    self.va_std_id.get(),
                                                                                    self.var_std_name.get(),
                                                                                    self.var_roll.get(),
                                                                                    self.var_gender.get(),
                                                                                    self.var_dob.get(),
                                                                                    self.var_phone.get(),
                                                                                    self.var_radio1 .get()                
                                                                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added Sucessfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)  
                               
    #==========fatch data=======
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select  * from student")
        data=my_cursor.fetchall()
        
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
#   ===== get  corsor===========
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
            
        self.var_dep.set(data[0]),   
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.va_std_id.set(data[4]), 
        self.var_std_name.set(data[5]),
        self.var_roll.set(data[6]),
        self.var_gender.set(data[7]),
        self.var_dob.set(data[8]),
        self.var_phone.set(data[9]),
        #self.var_photo.set(data[10])
        self.var_radio1.set(data[10])
               
    #  ================= update data==========
    def update_data(self):    
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update the Data",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Roll=%s,Gender=%s,Dob=%s,Phone=%s,PhotoSample=%s where Student_id=%s" ,(
                                                                                    self.var_dep.get(),
                                                                                    self.var_course.get(),
                                                                                    self.var_year.get(),
                                                                                    self.var_semester.get(),
                                                                                   
                                                                                    self.var_std_name.get(),
                                                                                    self.var_roll.get(),
                                                                                    self.var_gender.get(),
                                                                                    self.var_dob.get(),
                                                                                    self.var_phone.get(),
                                                                                    self.var_radio1.get() ,
                                                                                    self.va_std_id.get()
                                                                                   ))
                else:
                    if  not Update:
                        return 
                messagebox.showinfo("Success","Student details successfully updateed",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close() 
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root) 
                
                
#    ==== delete the data
    def delete_data(self):
        if self.va_std_id.get()=="":
            messagebox.showerror("Error","Student ID must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to Delete this student data",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.va_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showerror("Delete","Successfully deleted student data",parent=self.root) 
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
                
    #  reset the data 
    
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.va_std_id.set("")
        self.var_std_name.set("")
        self.var_roll.set("")
        self.var_gender.set("")
        self.var_dob.set("")
        self.var_phone.set("")
        self.var_radio1.set("")
                
     #  ====   ===  Generate data set or take a photo sample
    
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Roll=%s,Gender=%s,Dob=%s,Phone=%s,PhotoSample=%s where Student_id=%s" ,(
                                                                                    self.var_dep.get(),
                                                                                    self.var_course.get(),
                                                                                    self.var_year.get(),
                                                                                    self.var_semester.get(),
                                                                                   
                                                                                    self.var_std_name.get(),
                                                                                    self.var_roll.get(),
                                                                                    self.var_gender.get(),
                                                                                    self.var_dob.get(),
                                                                                    self.var_phone.get(),
                                                                                    self.var_radio1.get() ,
                                                                                    self.va_std_id.get()  ==id+1
                                                                                   ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()  
                #=================Load predifined data on face frontal from open cv========
                
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #=== Saclling factor=1.3
                    #Minimun neighbour=5
                    
                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("cropped  Face",face)
                    
                    if cv2.waitKey(1)==13 or int (img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data set Completed!!")
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
                
if __name__ =="__main__": 
    root=Tk()
    obj=Student(root)
    root.mainloop()