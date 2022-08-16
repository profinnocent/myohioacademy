from tkinter import *
from PIL import Image, ImageTk
import smtplib, ssl
import sqlite3

with sqlite3.connect("studentsdb") as sdb:
    c = sdb.cursor()




regpage = Tk()
regpage.title("Ohio Academy | Registration")
# regpage.title("Ohio Academy | Dashboard")
# regpage.geometry("700x600")


# Variable
priclr = "#06283D"
secclr = "#1363DF"
acentclr = "#47B5FF"
offwyt = "#DFF6FF"


mainwidth = 500
mainheight = 600

# global ufullname
# global udept
# global uemail
# global ugender
# global ulevel



# Fucntions


def backtologin():
    regpage.destroy()
    import home


def reg_ok():
    idx = 0
    fn1 = fullnametxb.get()
    dept1 = depttxb.get()
    level1 = leveltxb.get()
    gender1 = gendertxb.get()
    email1 = emailtxb.get()
    password1 = passwordtxb.get()


    if email1 == "" or password1 == "":
        feedback["text"] = "Please fill all fields"
    else:
        try:

            c.execute("SELECT COUNT(*) FROM students WHERE email = '"+ email1 +"' ")

            result = c.fetchone()

            if int(result[0]) > 0:
                feedback["text"] = "Error email already exists."
            else:
                c.execute("SELECT * FROM students")
                outcome = c.fetchall()

                if len(outcome) == 0:
                    idx = 1
                else:
                    idx = int(outcome[len(outcome)-1][0]) + int(1)
                    pass

                print(idx)

                feedback["text"] = "New user added successfully."
                c.execute(("INSERT INTO students (id,fullname, department, level, gender, email, password)VALUES(?,?,?,?,?,?,?)"), (idx, fn1, dept1, level1, gender1, email1, password1))
                sdb.commit()

        except Exception as ex:
            print("Error: SQL not executed on Database", ex)





# Sections
main = Frame(regpage, width=mainwidth, height=mainheight, bg="#DFF6FF").pack()

# Add logo
photo = ImageTk.PhotoImage(file='assets/logo50.png')
logolabel = Label(regpage, image=photo)
logolabel.place(x=100, y=20)

titlelabel = Label(regpage,text="OHIO ACADEMY", bg="#DFF6FF", fg="#06283D", font=('ariel', 24, 'bold')).place(x=150, y=20)
pagemsg = Label(regpage, text="Please enter details below to register", bg="#DFF6FF", fg="#06283D").place(x=170, y=60)

feedback = Message(regpage, text="", width=300, fg="red")
feedback.place(x=100, y=80)

fullnamelabel = Label(regpage, text="Fullname", bg="#DFF6FF", fg="#06283D", font=(35)).place(x=100, y=100)
fullnametxb = Entry(regpage, width=33, font=24)
fullnametxb.place(x=100, y=130)

deptlabel = Label(regpage, text="Department", bg="#DFF6FF", fg="#06283D", font=(35)).place(x=100, y=160)
depttxb = Entry(regpage, width=33, font=24)
depttxb.place(x=100, y=190)

levellabel = Label(regpage, text="Level", bg="#DFF6FF", fg="#06283D", font=(35)).place(x=100, y=210)
leveltxb = Entry(regpage, width=33, font=24)
leveltxb.place(x=100, y=240)

genderlabel = Label(regpage, text="Gender", bg="#DFF6FF", fg="#06283D", font=(35)).place(x=100, y=270)
gendertxb = Entry(regpage, width=33, font=24)
gendertxb.place(x=100, y=300)

emaillabel = Label(regpage, text="Email", bg="#DFF6FF", fg="#06283D", font=(35)).place(x=100, y=330)
emailtxb = Entry(regpage, width=33, font=24)
emailtxb.place(x=100, y=360)

passwordlabel = Label(regpage, text="Password", bg="#DFF6FF", fg="#06283D", font=(35)).place(x=100, y=390)
passwordtxb = Entry(regpage, width=33, font=24, show="*")
passwordtxb.place(x=100, y=420)

# Submit button
regbtn = Button(regpage, text="Register", width=42, bg="#06283D", fg="#DFF6FF", command=reg_ok).place(x=100, y=460)


# Reg and reset redirect btns
backbtn = Button(regpage, text="<< Back to Login", bg="#DFF6FF", command=backtologin).place(x=300, y=510)

# Footer
footerlabel = Label(text="powered by Pyt2 Technologies", bg="#DFF6FF", fg="#06283D").place(x=mainwidth/2 - 100, y=mainheight-30)










regpage.mainloop()