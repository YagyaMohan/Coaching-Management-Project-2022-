from tkinter import*
from tkinter import ttk


import matplotlib.pyplot as plt

from tkinter import messagebox
import datetime


root=Tk()
root.title('Epistêmê')
root.geometry("800x500")
root.state('zoomed')
result_window=Tk()
result_window.title('Results')
fee_window=Tk()
fee_window.title('Fees')
regis_window=Tk()
#regis_window.configure(bg="#FF0066")
regis_window.title('Registration')

from PIL import ImageTk,Image
#canvas=Canvas(root,width=500,height=500)
my_img=ImageTk.PhotoImage(Image.open("C:\\Users\\mohan\\OneDrive\\Desktop\\Python Projects\\episteme.png"))
image_label=Label(root,image=my_img)
image_label.place(x=0,y=10,relwidth=1,relheight=1)
episteme = Label(root, text="Epistêmê", font=("Times New Roman" ,30,'bold'),fg="#ff8080")
episteme.grid(row=1,column=8)





def resultfunc():
    import mysql.connector
    

    my_connect = mysql.connector.connect(host="localhost",user="root", passwd="yagya",database="coaching_project")
    my_conn = my_connect.cursor()
    my_conn.execute("SELECT * FROM results")
    i=0
    for result in my_conn:
        for j in range(len(result)):
            e = Entry(result_window, width=30, fg='blue')
            e.grid(row=i, column=j)
            e.insert(END, result[j])
        i=i+1

  



    
    #x=[1,2,3]#Graph
    #y=[4,5,6]
    #plt.plot(x,y)
    #plt.xlabel('x-axis')
    #plt.ylabel('y-axis')
    #plt.title('Cartesian Plane')
    #plt.show()


def feefunc():
    

    import mysql.connector
    my_connect = mysql.connector.connect(host="localhost",user="root", passwd="yagya",database="coaching_project")
    my_conn = my_connect.cursor()
    my_conn.execute("SELECT * FROM Fee_structure limit 0,5")
    i=0
    for fee_data in my_conn:
        for j in range(len(fee_data)):
            e = Entry(fee_window, width=30, fg='blue')
            e.grid(row=i, column=j)
            e.insert(END, fee_data[j])
        i=i+1
    
#Registration
first_name_instr=Label(regis_window,width=30,text="Student's First Name:",font=("Times New Roman" ,12))

first_name=Entry(regis_window,width=30,borderwidth=5,fg='blue',bg='white',font=("Times New Roman" ,12))
last_name_instr=Label(regis_window,width=30,text="Student's Last Name:",font=("Times New Roman" ,12))

last_name=Entry(regis_window,width=30,borderwidth=5,fg='blue',bg='white',font=("Times New Roman" ,12))

aadhaar_num_instr=Label(regis_window,width=30,text="Students's Aadhaar Number:",font=("Times New Roman" ,12))

aadhaar_num=Entry(regis_window,width=30,borderwidth=5,fg='blue',bg='white',font=("Times New Roman" ,12))

guard_aadhaar_num_instr=Label(regis_window,width=30,text="Guardian's Aadhaar Number:",font=("Times New Roman" ,12))

guard_aadhaar_num=Entry(regis_window,width=30,borderwidth=5,fg='blue',bg='white',font=("Times New Roman" ,12))

standard_list=['11th','12th','Dropper']
stud_class=ttk.Combobox(regis_window,value=standard_list,width=30,font=("Times New Roman" ,12))

stud_class_instr=Label(regis_window,width=30,borderwidth=5,text='Current Standard :',font=("Times New Roman" ,12))

age=Entry(regis_window,width=30,fg='blue',bg='white',borderwidth=5,font=("Times New Roman" ,12))

age_instr=Label(regis_window,text="Student's Age:",font=("Times New Roman" ,12))

target_exams_list=['JEE(M)','JEE(M+Adv)']
target_exams=ttk.Combobox(regis_window,value=target_exams_list,width=30,font=("Times New Roman" ,12))
target_exams_instr=Label(regis_window,text='Choose the exams you wish to appear for : ',font=("Times New Roman" ,10))

address_instr=Label(regis_window,text="Student's Current Address:",font=("Times New Roman" ,12))

address=Entry(regis_window,width=50,borderwidth=5,fg='blue',bg='white',font=("Times New Roman" ,12))



guardf_name_instr=Label(regis_window,text="Guardian's First Name:",font=("Times New Roman" ,12))

guardf_name=Entry(regis_window,width=30,borderwidth=5,fg='blue',bg='white',font=("Times New Roman" ,12))
guardl_name_instr=Label(regis_window,text="Guardian's Last Name:",font=("Times New Roman" ,12))

guardl_name=Entry(regis_window,width=30,borderwidth=5,fg='blue',bg='white',font=("Times New Roman" ,12))

guardians_mobile_instr=Label(regis_window,text="Guardian's Contact No.:",font=("Times New Roman" ,12))

guardians_mobile=Entry(regis_window,width=30,borderwidth=5,fg='blue',bg='white',font=("Times New Roman" ,12))

    

def regisfunc():
    first_name_instr.grid(row=1,column=0)
    first_name.grid(row=1,column=4)
    last_name_instr.grid(row=1,column=8)
    last_name.grid(row=1,column=12)
    aadhaar_num_instr.grid(row=2,column=0)
    aadhaar_num.grid(row=2,column=4)
    age_instr.grid(row=2,column=8)
    age.grid(row=2,column=12)
    stud_class_instr.grid(row=3,column=0)
    stud_class.grid(row=3,column=4)
    target_exams_instr.grid(row=3,column=8)
    target_exams.grid(row=3,column=12)
    address_instr.grid(row=4,column=0)
    address.grid(row=4,column=4)
    guardf_name_instr.grid(row=4,column=8)
    guardf_name.grid(row=4,column=12)
    guardl_name_instr.grid(row=5,column=0)
    guardl_name.grid(row=5,column=4)
    guard_aadhaar_num_instr.grid(row=5,column=8)
    guard_aadhaar_num.grid(row=5,column=12)
    guardians_mobile_instr.grid(row=6,column=0)
    guardians_mobile.grid(row=6,column=4)
    
    
        
    
    
def submitfunc():
    f_name_user=first_name.get()
    l_name_user=last_name.get()
    name_user=str(f_name_user)+" "+str(l_name_user)
    age_user=age.get()
    address_user=address.get()
    guardf_user=guardf_name.get()
    guardl_user=guardl_name.get()
    guard_user=str(guardf_user)+" "+str(guardl_user)
    target_exam_user=target_exams.get()
    std_user=stud_class.get()
    guardians_mobile_user=guardians_mobile.get()
    aadhaar_num_user=aadhaar_num.get()
    guard_aadhar_user=guard_aadhaar_num.get()
    if f_name_user==""or l_name_user==""  or age_user=="" or address_user=="" or guardf_user=="" or guardl_user=="" or target_exam_user=="" or std_user==""or guardians_mobile_user=="":
        messagebox.showwarning("showwarning","Blank entries in any of the fields won't be accepted")#Checked
    elif f_name_user.isalpha()==False or l_name_user.isalpha()==False or guardf_user.isalpha()==False or guardl_user.isalpha()==False:
        messagebox.showwarning("showwarning","Please enter valid entries for the name fields")#Checked
    elif age_user.isnumeric()==False:
         messagebox.showwarning("showwarning","Please enter a valid number for the age field.")#Checked
    elif guardians_mobile_user.isnumeric()==False or len(guardians_mobile_user)!=10:#Checked
        messagebox.showwarning("showwarning","Please enter a valid 10 digit number only for the mobile number fields")
    elif aadhaar_num_user.isnumeric()==False or guard_aadhar_user.isnumeric()==False or len(aadhaar_num_user)!=12 or len(guard_aadhar_user)!=12:#Checked
        messagebox.showwarning("showwarning","Please enter a valid 12 digit number only for the Aadhaar number fields")#Checked
    elif aadhaar_num_user==guard_aadhar_user:
        messagebox.showwarning("showwarning","Please enter unique Aadhaar Numbers only :")#Checked
    elif(std_user not in standard_list) or (target_exam_user not in target_exams_list) :#Checked
        messagebox.showwarning("showwarning","Please choose the valid entries from the combobox only :")
    #Uniqueness of  Aadhaar Numbers-Checked
    #Siblings-Checked
    #Duplicate registrations(adhaar)-To be checked
    
    
    
    else:
        import mysql.connector
        my_connect = mysql.connector.connect(host="localhost",user="root", passwd="yagya",database="coaching_project")
        my_conn = my_connect.cursor()
        sql_student = "INSERT INTO student_details VALUES (%s, %s,%s,%s,%s,%s,%s)"
        sql_guardian = "INSERT INTO guardian_details VALUES (%s, %s,%s,%s)"
        stud_value=(aadhaar_num_user,name_user,guard_aadhar_user,std_user,target_exam_user,address_user, age_user)
        guard_value=(aadhaar_num_user,guard_aadhar_user,guard_user,guardians_mobile_user)
        my_conn.execute(sql_student,stud_value)
        my_conn.execute(sql_guardian,guard_value)
        my_connect.commit()
        messagebox.showinfo("showinfo","Congratulations!You have been registered successfully")


submit_button=Button(regis_window,text='Submit',borderwidth=7.5,width=10,command=submitfunc)
submit_button.grid(row=11,column=6)
    
    
result=Button(root,text='Results',command=resultfunc,width=20,height=5,bg="#006A4E",fg="#FFD700",font=("Times New Roman" ,20,'bold'))
result.grid(row=3,column=7)
fee_structure=Button(root,text='Fee Structure',command=feefunc,width=20,height=5,bg="#FF7F50",fg="#AAFF00",font=("Times New Roman" ,20,'bold'))
fee_structure.grid(row=3,column=8)
registration=Button(root,text='Register Now',command= regisfunc,width=20,height=5,bg="#FF6347",fg="#808080",font=("Times New Roman" ,20,'bold'))
registration.grid(row=3,column=9)

