#Author: Dev Butani

from backend import *
import tkinter as tk
from tkinter import messagebox  #for warnings

window=tk.Tk()
window.title("Academic Portal")
window.state('zoomed')  #for Linux, remove this command and uncomment the below command
#window.attributes('-zoomed', True)

bgimg=tk.PhotoImage(file='bgimg.png')
bgimg_label=tk.Label(window, image=bgimg)
bgimg_label.place(x=0, y=0, relwidth=1, relheight=1)

Welcome=tk.Frame(window, bg="Black")
Profile=tk.Frame(window, bg="Black")
SignInFrame=tk.LabelFrame(Welcome, text="Sign In", font=("Arial",20), bg="Black", fg='#00FFFF')
SignUpFrame=tk.LabelFrame(Welcome, text="Sign Up", font=("Arial",20), bg="Black", fg='#00FFFF')


def switch_to_welcome():              #unpacks Profile-frame widgets and packs Welcome-frame widgets
    classno=token_classno.get()
    Profile.pack_forget()
    Common_details.pack_forget()
    match classno:
        case 0:
            Teacher_details.pack_forget()
        case 1:
            Student_details.pack_forget()
            UG_details.pack_forget()
        case 2:
            Student_details.pack_forget()
            PG_details.pack_forget()
    Profile_Editing.pack_forget()
    edit_profile_button.pack_forget()
    profile_signout_button.pack_forget()
    deregister_button.pack_forget()

    Welcome.pack(padx=175, pady=175)
    welcome_label.pack()
    welcome_label.pack()
    SignInFrame.pack(padx=30, pady=30)
    signup_switch_button.pack()
    signin_showpass_var.set(0)
    signin_showpass()
    signup_showpass_var.set(0)
    signup_showpass()


def set_profile(token):                       #replaces Profile-frame widget entries with user data
    profile_firstname_entry.config(state='normal')
    profile_firstname_entry.delete(0, tk.END)
    if token.FirstName!=None: profile_firstname_entry.insert(0, token.FirstName)
    profile_firstname_entry.config(state='disabled')
    
    profile_lastname_entry.config(state='normal')
    profile_lastname_entry.delete(0, tk.END)
    if token.LastName!=None: profile_lastname_entry.insert(0, token.LastName)
    profile_lastname_entry.config(state='disabled')

    profile_department_entry.config(state='normal')
    profile_department_entry.delete(0, tk.END)
    if token.Department!=None: profile_department_entry.insert(0, token.Department)
    profile_department_entry.config(state='disabled')

    profile_age_spinbox.config(state='normal')
    profile_age_spinbox.delete(0, tk.END)
    if token.Age!=None: profile_age_spinbox.insert(0, int(token.Age))
    else: profile_age.set(18)
    profile_age_spinbox.config(state='disabled')
    
    if token.classno==0:
        teacher_designation_menu.config(state='normal')
        if token.Designation!=None: teacher_designation.set(token.Designation)
        else: teacher_designation.set(teacher_designation_list[0])
        teacher_designation_menu.config(state='disabled')
                    
        teacher_yearofjoining_spinbox.config(state='normal')
        teacher_yearofjoining_spinbox.delete(0, tk.END)
        if token.YearOfJoining!=None: teacher_yearofjoining_spinbox.insert(0, int(token.YearOfJoining))
        else: teacher_yearofjoining.set(2024)
        teacher_yearofjoining_spinbox.config(state='disabled')
        
        teacher_office_entry.config(state='normal')
        teacher_office_entry.delete(0, tk.END)
        if token.Office!=None: teacher_office_entry.insert(0, token.Office)
        teacher_office_entry.config(state='disabled')
        
    else:
        student_rollno_entry.config(state='normal')
        student_rollno_entry.delete(0, tk.END)
        if token.RollNo!=None: student_rollno_entry.insert(0, token.RollNo)
        student_rollno_entry.config(state='disabled')
        
        student_batchyear_spinbox.config(state='normal')
        student_batchyear_spinbox.delete(0, tk.END)
        if token.BatchYear!=None: student_batchyear_spinbox.insert(0, int(token.BatchYear))
        else: student_batchyear.set(2024)
        student_batchyear_spinbox.config(state='disabled')
        
        if token.classno==1:
            ug_degree_menu.config(state='normal')
            if token.Degree!=None: ug_degree.set(token.Degree)
            else: ug_degree.set(ug_degree_list[0])
            ug_degree_menu.config(state='disabled')
        else:
            pg_degree_menu.config(state='normal')
            if token.Degree!=None: pg_degree.set(token.Degree)
            else: pg_degree.set(pg_degree_list[0])
            pg_degree_menu.config(state='disabled')

def switch_to_profile(mode, token):          #unpacks Welcome-frame widgets and packs Profile-frame widgets
    Welcome.pack_forget()
    welcome_label.pack_forget()
    if mode==1:                                #Previous frame: Welcome(Sign In)
        SignInFrame.pack_forget()
        signup_switch_button.pack_forget()
    else:                                      #Previous frame: Welcome(Sign Up)
        SignUpFrame.pack_forget()
        signin_switch_button.pack_forget()
    
    Profile.pack(padx=175, pady=(175,20))
    Common_details.pack()
    match token.classno:
        case 0:
            Teacher_details.pack()
        case 1:
            Student_details.pack()
            UG_details.pack()
        case 2:
            Student_details.pack()
            PG_details.pack()
    Profile_Editing.pack(padx=10, pady=10)
    edit_profile_button.pack()
    profile_signout_button.pack()
    deregister_button.pack()

    token_classno.set(token.classno)
    token_userid.set(token.User_ID)
    token_password.set(token.Password)
    
    set_profile(token)


#---------------WELCOME FRAME--------------------

welcome_label=tk.Label(Welcome, text='WELCOME', font=("Arial", 30), bg="Black", fg='#80FF00')

class_options_list=["Teacher", "Student(UG)", "Student(PG)"]

#SIGN IN WIDGETS
signin_class_value=tk.StringVar(value=class_options_list[0])
signin_class_menu=tk.OptionMenu(SignInFrame, signin_class_value, *class_options_list)
signin_class_menu.config(font=("Arial",14), fg='#F0FF00', bg="Black", activeforeground='#F0FF00', activebackground="Black")
signin_class_menu.grid(row=0, column=1)

signin_class_label=tk.Label(SignInFrame, text="Sign in as: ", padx=5, pady=5, font=("Arial",14), fg="White", bg="Black")
signin_class_label.grid(row=0, column=0)

signin_userid_label=tk.Label(SignInFrame, text="User ID: ", padx=5, pady=5, font=("Arial",14), fg="White", bg="Black")
signin_userid_label.grid(row=1, column=0)

signin_password_label=tk.Label(SignInFrame, text="Password: ", padx=5, pady=5, font=("Arial",14), fg="White", bg="Black")
signin_password_label.grid(row=2, column=0)

signin_userid_entry=tk.Entry(SignInFrame, font=("Arial",14), fg='#F0FF00', bg="Black", insertbackground='#F0FF00')
signin_userid_entry.grid(row=1, column=1)

signin_password_entry=tk.Entry(SignInFrame, show='*', font=("Arial",14), fg='#F0FF00', bg="Black", insertbackground='#F0FF00')
signin_password_entry.grid(row=2, column=1)

signin_showpass_var=tk.IntVar(value=0)
def signin_showpass():                       #function tied to checkbutton to show/hide password
    if(signin_showpass_var.get()==1):
        signin_password_entry.config(show='')
    else:
        signin_password_entry.config(show='*')

signin_showpass_checkbutton=tk.Checkbutton(SignInFrame, text="show password", variable=signin_showpass_var, onvalue=1, offvalue=0, command=signin_showpass)
signin_showpass_checkbutton.config(bg="Black", fg="White", activebackground="Black", activeforeground="White",selectcolor="Black")
signin_showpass_checkbutton.grid(row=3, column=0)

def signin_submit():                                                #create token object of given class
    userclassno=class_options_list.index(signin_class_value.get())  #read user id and password from entry fields
    userId=signin_userid_entry.get()                                #make sign in attempt and inform result to user
    password=signin_password_entry.get()
    
    match userclassno:
        case 0: token=Teacher(userId, password)
        case 1: token=UG_Student(userId, password)
        case 2: token=PG_Student(userId, password)
    token.classno=userclassno

    status=token.User_Authentication()
    match status:
        case 0:
            signin_userid_entry.delete(0, tk.END)
            signin_password_entry.delete(0, tk.END)
            token.Retrieve_Data()
            switch_to_profile(1, token)
            messagebox.showinfo("Authentication Complete", "Successfully Signed In")
        case 1:
            messagebox.showerror("Error", "Invalid User ID or password")
        case 2:
            signin_userid_entry.delete(0, tk.END)
            signin_password_entry.delete(0, tk.END)
            messagebox.showinfo("Info", "Account has been disabled (excess incorrect login attempts) \n Contact Tech support")
    del token

signin_submit_button=tk.Button(SignInFrame, text="Sign In", command=signin_submit, font=("Arial",12), fg='#FFA000', bg="Black")
signin_submit_button.grid(row=4, column=0, columnspan=2)


#SIGN UP WIDGETS
signup_class_value=tk.StringVar(value=class_options_list[0])
signup_class_menu=tk.OptionMenu(SignUpFrame, signup_class_value, *class_options_list)
signup_class_menu.config(font=("Arial",14), fg='#F0FF00', bg="Black", activeforeground='#F0FF00', activebackground="Black")
signup_class_menu.grid(row=0, column=1)

signup_class_label=tk.Label(SignUpFrame, text="Sign up as: ", padx=5, pady=5, font=("Arial",14), fg="White", bg="Black")
signup_class_label.grid(row=0, column=0)

signup_email_label=tk.Label(SignUpFrame, text="Email: ", padx=5, pady=5, font=("Arial",14), fg="White", bg="Black")
signup_email_label.grid(row=1, column=0)

signup_password_label=tk.Label(SignUpFrame, text="Password: ", padx=5, pady=5, font=("Arial",14), fg="White", bg="Black")
signup_password_label.grid(row=2, column=0)

signup_confirmpass_label=tk.Label(SignUpFrame, text="Confirm Password: ", padx=5, pady=5, font=("Arial",14), fg="White", bg="Black")
signup_confirmpass_label.grid(row=3, column=0)

signup_email_entry=tk.Entry(SignUpFrame, font=("Arial",14), fg='#F0FF00', bg="Black", insertbackground='#F0FF00')
signup_email_entry.grid(row=1, column=1)

signup_password_entry=tk.Entry(SignUpFrame, show='*', font=("Arial",14), fg='#F0FF00', bg="Black", insertbackground='#F0FF00')
signup_password_entry.grid(row=2, column=1)

signup_confirmpass_entry=tk.Entry(SignUpFrame, show='*', font=("Arial",14), fg='#F0FF00', bg="Black", insertbackground='#F0FF00')
signup_confirmpass_entry.grid(row=3, column=1)

signup_showpass_var=tk.IntVar(value=0)
def signup_showpass():                              #function tied to checkbutton to show/hide password
    if(signup_showpass_var.get()==1):
        signup_password_entry.config(show='')
        signup_confirmpass_entry.config(show='')
    else:
        signup_password_entry.config(show='*')
        signup_confirmpass_entry.config(show='*')

signup_showpass_checkbutton=tk.Checkbutton(SignUpFrame, text="show password", variable=signup_showpass_var, onvalue=1, offvalue=0, command=signup_showpass)
signup_showpass_checkbutton.config(bg="Black", fg="White", activebackground="Black", activeforeground="White",selectcolor="Black")
signup_showpass_checkbutton.grid(row=4, column=0)

def signup_submit():                                                #create token object of given class
    userclassno=class_options_list.index(signup_class_value.get())  #read user id and password from entry fields
    email=signup_email_entry.get()                                  #make sign up attempt and inform result to user
    password=signup_password_entry.get()
    if password!=signup_confirmpass_entry.get():
        messagebox.showwarning("Warning", "Passwords do not match")
        return
    
    match userclassno:
        case 0: token=Teacher(email, password)
        case 1: token=UG_Student(email, password)
        case 2: token=PG_Student(email, password)
    token.classno=userclassno
    
    status=token.User_Registration()
    match status:
        case 0:
            signup_email_entry.delete(0, tk.END)
            signup_password_entry.delete(0, tk.END)
            signup_confirmpass_entry.delete(0, tk.END)          
            switch_to_profile(0, token)
            messagebox.showinfo("Registration Complete", "Your Account has been Created")
        case 1:
            messagebox.showwarning("Warning", "Invalid email address")
        case 2:            
            messagebox.showwarning("Warning", "User with this email already exists")
        case 3:
            messagebox.showwarning("Warning", "Password must not be 8-12 characters long")
        case 4:
            messagebox.showwarning("Warning", "Password must contain at least one digit, \n upper case and lower case character")
        case 5:
            messagebox.showwarning("Warning", "Password must contain one or more special characters \n [! @ # $ % & *]")
        case 6:
            messagebox.showwarning("Warning", "Password must not contain blank space")
    del token

signup_submit_button=tk.Button(SignUpFrame, text="Sign Up", command=signup_submit, font=("Arial",12), fg='#FFA000', bg="Black")
signup_submit_button.grid(row=5, column=0, columnspan=2)


#SWITCH BUTTONS
def switch_to_signin():   #unpack Sign Up labelframe widgets and pack Sign In labelframe widgets
    signup_email_entry.delete(0, tk.END)
    signup_password_entry.delete(0, tk.END)
    signup_confirmpass_entry.delete(0, tk.END)
    signup_showpass_var.set(0)
    SignUpFrame.pack_forget()
    signin_switch_button.pack_forget()
    SignInFrame.pack(padx=30, pady=30)
    signup_switch_button.pack()

def switch_to_signup():   #unpack Sign In labelframe widgets and pack Sign Up labelframe widgets
    signin_userid_entry.delete(0, tk.END)
    signin_password_entry.delete(0, tk.END)
    signin_showpass_var.set(0)
    SignInFrame.pack_forget()
    signup_switch_button.pack_forget()
    SignUpFrame.pack(padx=30, pady=30)
    signin_switch_button.pack()

signup_switch_button=tk.Button(Welcome, text="Sign Up Instead", command=switch_to_signup, font=("Arial",12), fg='#DC00FF', bg="Black")
signin_switch_button=tk.Button(Welcome, text="Sign In Instead", command=switch_to_signin, font=("Arial",12), fg='#DC00FF', bg="Black")


#------------------PROFILE FRAME---------------------

#Personal details
Common_details=tk.Frame(Profile, bg="Black")
profile_label=tk.Label(Common_details, text="Account Details", padx=20, pady=20, font=("Arial", 25), bg="Black", fg='#80FF00')
profile_label.grid(row=0, column=0, columnspan=2)

profile_firstname_label=tk.Label(Common_details, text="First Name: ", padx=5, pady=5, font=("Arial",14), fg="White", bg="Black")
profile_firstname_label.grid(row=1, column=0)

profile_firstname_entry=tk.Entry(Common_details, font=("Arial",14), fg='#F0FF00', bg="Black", insertbackground='#F0FF00', disabledforeground="Grey", disabledbackground="Black")
profile_firstname_entry.grid(row=1, column=1)

profile_lastname_label=tk.Label(Common_details, text="Last Name: ", padx=5, pady=5, font=("Arial",14), fg="White", bg="Black")
profile_lastname_label.grid(row=2, column=0)

profile_lastname_entry=tk.Entry(Common_details, font=("Arial",14), fg='#F0FF00', bg="Black", insertbackground='#F0FF00', disabledforeground="Grey", disabledbackground="Black")
profile_lastname_entry.grid(row=2, column=1)

profile_department_label=tk.Label(Common_details, text="Department: ", padx=5, pady=5, font=("Arial",14), fg="White", bg="Black")
profile_department_label.grid(row=3, column=0)

profile_department_entry=tk.Entry(Common_details, font=("Arial",14), fg='#F0FF00', bg="Black", insertbackground='#F0FF00', disabledforeground="Grey", disabledbackground="Black")
profile_department_entry.grid(row=3, column=1)

profile_age_label=tk.Label(Common_details, text="Age: ", padx=5, pady=5, font=("Arial",14), fg="White", bg="Black")
profile_age_label.grid(row=4, column=0)

profile_age=tk.IntVar(value=18)
profile_age_spinbox=tk.Spinbox(Common_details, from_=0, to=200, textvariable=profile_age, font=("Arial",14), fg='#F0FF00', bg="Black", readonlybackground="Black", disabledbackground="Black")
profile_age_spinbox.grid(row=4, column=1)

#Class specific details for Teacher
Teacher_details=tk.Frame(Profile, bg="Black")
teacher_designation_label=tk.Label(Teacher_details, text="Designation: ", padx=5, pady=5, font=("Arial",14), fg="White", bg="Black")
teacher_designation_label.grid(row=0, column=0)

teacher_designation_list=["Professor", "Assistant Professor", "Associate Professor"]
teacher_designation=tk.StringVar(value=teacher_designation_list[0])
teacher_designation_menu=tk.OptionMenu(Teacher_details, teacher_designation, *teacher_designation_list)
teacher_designation_menu.config(font=("Arial",14), fg='#F0FF00', bg="Black", activeforeground='#F0FF00', activebackground="Black")
teacher_designation_menu.grid(row=0, column=1)

teacher_yearofjoining_label=tk.Label(Teacher_details, text="Year Of Joining: ", padx=5, pady=5, font=("Arial",14), fg="White", bg="Black")
teacher_yearofjoining_label.grid(row=1, column=0)

teacher_yearofjoining=tk.IntVar(value=2024)
teacher_yearofjoining_spinbox=tk.Spinbox(Teacher_details, from_=1900, to=2024, textvariable=teacher_yearofjoining, font=("Arial",14), fg='#F0FF00', bg="Black", readonlybackground="Black", disabledbackground="Black")
teacher_yearofjoining_spinbox.grid(row=1, column=1)

teacher_office_label=tk.Label(Teacher_details, text="Office: ", padx=5, pady=5, font=("Arial",14), fg="White", bg="Black")
teacher_office_label.grid(row=2, column=0)

teacher_office_entry=tk.Entry(Teacher_details, font=("Arial",14), fg='#F0FF00', bg="Black", insertbackground='#F0FF00', disabledforeground="Grey", disabledbackground="Black")
teacher_office_entry.grid(row=2, column=1)

#Class specific details for Student
Student_details=tk.Frame(Profile, bg="Black")
student_rollno_label=tk.Label(Student_details, text="Roll No.: ", padx=5, pady=5, font=("Arial",14), fg="White", bg="Black")
student_rollno_label.grid(row=0, column=0)

student_rollno_entry=tk.Entry(Student_details, font=("Arial",14), fg='#F0FF00', bg="Black", insertbackground='#F0FF00', disabledforeground="Grey", disabledbackground="Black")
student_rollno_entry.grid(row=0, column=1)

student_batchyear_label=tk.Label(Student_details, text="Batch Year: ", padx=5, pady=5, font=("Arial",14), fg="White", bg="Black")
student_batchyear_label.grid(row=1, column=0)

student_batchyear=tk.IntVar(value=2024)
student_batchyear_spinbox=tk.Spinbox(Student_details, from_=2000, to=2024, textvariable=student_batchyear, font=("Arial",14), fg='#F0FF00', bg="Black", readonlybackground="Black", disabledbackground="Black")
student_batchyear_spinbox.grid(row=1, column=1)

#UG specific details
UG_details=tk.Frame(Profile, bg="Black")
ug_degree_label=tk.Label(UG_details, text="Degree: ", padx=5, pady=5, font=("Arial",14), fg="White", bg="Black")
ug_degree_label.grid(row=0, column=0)

ug_degree_list=["BTech", "BSc", "BArch", "Dual Degree"]
ug_degree=tk.StringVar(value=ug_degree_list[0])
ug_degree_menu=tk.OptionMenu(UG_details, ug_degree, *ug_degree_list)
ug_degree_menu.config(font=("Arial",14), fg='#F0FF00', bg="Black", activeforeground='#F0FF00', activebackground="Black")
ug_degree_menu.grid(row=0, column=1)

#PG specific details
PG_details=tk.Frame(Profile, bg="Black")
pg_degree_label=tk.Label(PG_details, text="Degree: ", padx=5, pady=5, font=("Arial",14), fg="White", bg="Black")
pg_degree_label.grid(row=0, column=0)

pg_degree_list=["PhD", "MTech", "MSc", "MBA"]
pg_degree=tk.StringVar(value=pg_degree_list[0])
pg_degree_menu=tk.OptionMenu(PG_details, pg_degree, *pg_degree_list)
pg_degree_menu.config(font=("Arial",14), fg='#F0FF00', bg="Black", activeforeground='#F0FF00', activebackground="Black")
pg_degree_menu.grid(row=0, column=1)

#Edit Profile, Confirm Changes and Cancel buttons
token_classno=tk.IntVar()
token_userid=tk.StringVar()
token_password=tk.StringVar()

Profile_Editing=tk.Frame(Profile, bg="Black")

def edit_profile():      #enable Profile entry fields for input from user
    edit_profile_button.pack_forget()
    Profile_Changes.pack()
    profile_signout_button.config(state='disabled')
    deregister_button.config(state='disabled')

    classno=token_classno.get()
    profile_firstname_entry.config(state='normal')
    profile_lastname_entry.config(state='normal')
    profile_department_entry.config(state='normal')
    profile_age_spinbox.config(state='readonly')
    if classno==0:
        teacher_designation_menu.config(state='normal')
        teacher_yearofjoining_spinbox.config(state='readonly')
        teacher_office_entry.config(state='normal')
    else:
        student_rollno_entry.config(state='normal')
        student_batchyear_spinbox.config(state='readonly')
        if classno==1: ug_degree_menu.config(state='normal')
        else: pg_degree_menu.config(state='normal')

edit_profile_button=tk.Button(Profile_Editing, text="Edit Profile", command=edit_profile, font=("Arial",12), fg='#FFA000', bg="Black")


Profile_Changes=tk.Frame(Profile_Editing, bg="Black")

def confirm_changes():    #create token object and assign Profile entry field values to its parameters, then save token data in database
    Profile_Changes.pack_forget()
    edit_profile_button.pack()
    profile_signout_button.config(state='normal')
    deregister_button.config(state='normal')

    classno=token_classno.get()
    userid=token_userid.get()
    password=token_password.get()

    match classno:
        case 0: token=Teacher(userid, password)
        case 1: token=UG_Student(userid, password)
        case 2: token=PG_Student(userid, password)
    token.classno=classno
    token.FirstName=profile_firstname_entry.get()
    token.LastName=profile_lastname_entry.get()
    token.Department=profile_department_entry.get()
    token.Age=profile_age.get()
    if classno==0:
        token.Designation=teacher_designation.get()
        token.YearOfJoining=teacher_yearofjoining.get()
        token.Office=teacher_office_entry.get()
    else:
        token.RollNo=student_rollno_entry.get()
        token.BatchYear=student_batchyear.get()
        if classno==1: token.Degree=ug_degree.get()
        else: token.Degree=pg_degree.get()
    
    token.Save_Data()
    
    set_profile(token)
    del token

profile_confirm_changes_button=tk.Button(Profile_Changes, text="Confirm Changes", command=confirm_changes, font=("Arial",12), fg='#FFA000', bg="Black")
profile_confirm_changes_button.grid(row=0, column=0)


def cancel_changes():             #reset Profile entry fields to user data taken from database via token object
    Profile_Changes.pack_forget()
    edit_profile_button.pack()
    profile_signout_button.config(state='normal')
    deregister_button.config(state='normal')

    classno=token_classno.get()
    userid=token_userid.get()
    password=token_password.get()

    match classno:
        case 0: token=Teacher(userid, password)
        case 1: token=UG_Student(userid, password)
        case 2: token=PG_Student(userid, password)
    token.classno=classno

    token.Retrieve_Data()

    set_profile(token)
    del token

profile_cancel_changes_button=tk.Button(Profile_Changes, text="Cancel", command=cancel_changes, font=("Arial",12), fg='#FFA000', bg="Black")
profile_cancel_changes_button.grid(row=0, column=1)

#Sign out and Deregister buttons
profile_signout_button=tk.Button(Profile, text="Sign Out", command=switch_to_welcome, font=("Arial",12), fg='#DC00FF', bg="Black")

def deregister():       #send information about user account to be deleted via token 
    confirmation=messagebox.askquestion("Delete Account", "Are You Sure?", icon='warning')
    if confirmation=='no': return
    userid=token_userid.get()
    password=token_password.get()
    token=Person(userid, password)
    token.User_Deregistration()
    switch_to_welcome()
    messagebox.showinfo("Deletion Complete", "Your Account has been Deleted")
    del token

deregister_button=tk.Button(window, text="Delete Account", command=deregister, font=("Arial Bold",12), fg='#FF0000', bg="Black")


Welcome.pack(padx=175, pady=175)
welcome_label.pack()
SignInFrame.pack(padx=30, pady=30)
signup_switch_button.pack()
window.mainloop()