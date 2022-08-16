from tkinter import *
from PIL import ImageTk, Image
import sqlite3

with sqlite3.connect("studentsdb") as sdb:
    c = sdb.cursor()

homepage = Tk()
homepage.title("Home | Login")
# homepage.geometry("700x600")


# Variable
priclr = "#06283D"
secclr = "#1363DF"
acentclr = "#47B5FF"
offwyt = "#DFF6FF"


mainwidth = 500
mainheight = 500

# Fucntions
def toregister():
    homepage.destroy()
    import register

def toreset():
    homepage.destroy()
    import reset

def todashboard():
    homepage.destroy()
    import dashboard

def login_ok():
    email1 = emailtxb.get()
    password1 = passwordtxb.get()


    if email1 == "" or password1 == "":
        feedback["text"] = "Please fill all fields"
    else:
        c.execute("SELECT * FROM students WHERE email = '"+ email1 +"' AND password = '"+ password1 +"'  ")

        result = c.fetchone()

        print(result)

        if not result:
            feedback["text"] = "Error : wrong details or user does not exists."
        elif result:
            feedback["text"] = "Login successfully "
            homepage.destroy()
            import dashboard

# Sections
main = Frame(homepage, width=mainwidth, height=mainheight, bg="#DFF6FF").pack()

# Add logo
photo = ImageTk.PhotoImage(file='assets/logo50.png')
logolabel = Label(homepage, image=photo)
logolabel.place(x=100,y=50)

titlelabel = Label(text="OHIO ACADEMY", bg="#DFF6FF", fg="#06283D", font=('ariel', 24, 'bold')).place(x=150, y=50)
pagemsg = Label(text="Please enter details below to login", bg="#DFF6FF", fg="#06283D").place(x=150, y=100)
emaillabel = Label(text="Email", bg="#DFF6FF", fg="#06283D", font=(35)).place(x=100, y=150)
passwordlabel = Label(text="Password", bg="#DFF6FF", fg="#06283D", font=(35)).place(x=100, y=220)
footerlabel = Label(text="powered by Pyt2 Technologies", bg="#DFF6FF", fg="#06283D").place(x=mainwidth/2 - 100, y=mainheight-30)

feedback = Message(text="", width=300, fg="red",anchor=CENTER)
feedback.place(x=100,y=120)


# Profile design
# clientname =

# Add textbox
emailtxb = Entry(homepage, width=33, font=24)
emailtxb.place(x=100, y=180)
passwordtxb = Entry(homepage, width=33, font=24, show="*")
passwordtxb.place(x=100, y=250)

# Reg and reset redirect btns
regbtn = Button(homepage, text="Register", bg="#DFF6FF", command=toregister).place(x=100, y=370)
resetbtn = Button(homepage, text="Forget password?", bg="#DFF6FF", command=toreset).place(x=300, y=370)


# Submit button
loginbtn = Button(homepage, text="Login", width=42, bg="#06283D", fg="#DFF6FF", command=login_ok).place(x=100, y=300)


# Add Logo image
# logo = PhotoImage(homepage, file='assets/logo.jpg')
# logolabel = ttk.Label(homepage, image=logo).pack()






homepage.mainloop()