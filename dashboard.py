from tkinter import *
from utility import *
from PIL import Image, ImageTk
import sqlite3

with sqlite3.connect("studentsdb") as sdb:
    c = sdb.cursor()

root = Tk()
root.title("Ohio Academy | Dashboard")
# root.geometry("700x600")

# Variable
priclr = "#06283D"
secclr = "#1363DF"
acentclr = "#47B5FF"
offwyt = "#DFF6FF"

mainwidth = 500
mainheight = 500


# Sections
titlebar = Frame(width=500, height=50, bg='#06283D').pack()
navbar = Frame(width=500, height=50, bg='#06283D').pack()
main = Frame(root, width=500, height=500, bg="#DFF6FF").pack()
footer = Frame(width=500, height=50, bg='#06283D').pack()

# Dashboard Profile
dp = ImageTk.PhotoImage(file='assets/woman50.png')
dplbl = Label(root, image=dp)
dplbl.place(x=50, y=150)

# Get user details from DB
c.execute("SELECT * FROM sec")
result = c.fetchone()
userid = StringVar()

for x in result:
    userid = str(result[0])

print(userid)

c.execute("SELECT * FROM students where id='"+ userid +"' ")
curruser = c.fetchone()

# Bind user data
fnstr = StringVar()
fnstr = curruser[1]

deptstr = StringVar()
deptstr = curruser[2]

levstr = StringVar()
levstr = curruser[3]

genstr = StringVar()
genstr = curruser[4]

emstr = StringVar()
emstr = curruser[5]

welcomelbl = Label(root, text="Welcome, " + fnstr, font=('arial',20, 'bold'), bg="#DFF6FF")
welcomelbl.place(x=120, y=160)



fnlbl = Label(root, text="Fullname : ", font=('arial',14, 'bold'), bg="#DFF6FF")
fnlbl.place(x=50, y=230)
fnlbl1 = Label(root, text=fnstr, font=('arial',14, 'bold'), bg="#DFF6FF")
fnlbl1.place(x=200, y=230)
fn1str = StringVar()
fn1str = fnlbl1['text']

deptlbl = Label(root, text="Department : ", font=('arial',14, 'bold'), bg="#DFF6FF")
deptlbl.place(x=50, y=260)
deptlbl1 = Label(root, text=deptstr, font=('arial',14, 'bold'), bg="#DFF6FF")
deptlbl1.place(x=200, y=260)
dept1str = StringVar()
dept1str = deptlbl1['text']

levlbl = Label(root, text="Level : ", font=('arial',14, 'bold'), bg="#DFF6FF")
levlbl.place(x=50, y=290)
levlbl1 = Label(root, text=levstr, font=('arial',14, 'bold'), bg="#DFF6FF")
levlbl1.place(x=200, y=290)
lev1str = StringVar()
lev1str = levlbl1['text']

genderlbl = Label(root, text="Gender : ", font=('arial',14, 'bold'), bg="#DFF6FF")
genderlbl.place(x=50, y=320)
genderlbl1 = Label(root, text=genstr, font=('arial',14, 'bold'), bg="#DFF6FF")
genderlbl1.place(x=200, y=320)
gen1str = StringVar()
gen1str = genderlbl1['text']

emaillbl = Label(root, text="Email : ", font=('arial',14, 'bold'), bg="#DFF6FF")
emaillbl.place(x=50, y=350)
emaillbl1 = Label(root, text=emstr, font=('arial',14, 'bold'), bg="#DFF6FF")
emaillbl1.place(x=200, y=350)
em1str = StringVar()
em1str = emaillbl1['text']

pwlbl = Label(root, text="Password : ", font=('arial',14, 'bold'), bg="#DFF6FF")
pwlbl.place(x=50, y=380)
pwlbl1 = Label(root, text=" **********", font=('arial',14, 'bold'), bg="#DFF6FF")
pwlbl1.place(x=200, y=380)

fntxb = Entry(root)
depttxb = Entry(root)
levtxb = Entry(root)
gendertxb = Entry(root)
emailtxb = Entry(root)
pwtxb = Entry(root)


def editsave():
    if button["text"] == "Edit":
        fntxb.insert(0, fn1str )
        fntxb.place(x=350, y=230)

        depttxb.place(x=350, y=260)
        depttxb.insert(0, dept1str )

        levtxb.place(x=350, y=290)
        levtxb.insert(0, lev1str )

        gendertxb.place(x=350, y=320)
        gendertxb.insert(0, gen1str )

        emailtxb.place(x=350, y=350)
        emailtxb.insert(0, em1str )

        # pwtxb.place(x=350, y=380)
        # pwtxb.insert(0, pwlbl1['text'] )


        button["text"] = "Save"
        button["bg"] = "green"

        # Destroy the labels
        fnlbl1.destroy()
        deptlbl1.destroy()
        levlbl1.destroy()
        genderlbl1.destroy()
        emaillbl1.destroy()
        pwlbl1.destroy()

    else:

        # fnlbl1 = Label(root, text=fntxb.get(), font=('arial', 14, 'bold'), bg="#DFF6FF")
        fnlbl1.place(x=200, y=230)
        # deptlbl1 = Label(root, text=depttxb.get(), font=('arial', 14, 'bold'), bg="#DFF6FF")
        deptlbl1.place(x=200, y=260)
        # levlbl1 = Label(root, text=levtxb.get(), font=('arial', 14, 'bold'), bg="#DFF6FF")
        levlbl1.place(x=200, y=290)
        # genderlbl1 = Label(root, text=gendertxb.get(), font=('arial', 14, 'bold'), bg="#DFF6FF")
        genderlbl1.place(x=200, y=320)
        # emaillbl1 = Label(root, text=emailtxb.get(), font=('arial', 14, 'bold'), bg="#DFF6FF")
        emaillbl1.place(x=200, y=350)
        # pwlbl1 = Label(root, text=" **********", font=('arial', 14, 'bold'), bg="#DFF6FF")
        pwlbl1.place(x=200, y=380)

        # Destroy the txbs
        fntxb.destroy()
        depttxb.destroy()
        levtxb.destroy()
        gendertxb.destroy()
        emailtxb.destroy()
        pwtxb.destroy()
        # pass

button = Button(root, text="Edit",fg=offwyt, bg=priclr, width=20, padx=20, pady=5,font=('arial',10, 'bold'), command=editsave)
button.place(x=200, y=430)

# Define button actions
def dashboardpage():
    root.destroy()
    import dashboard

def coursespage():
    root.destroy()
    import courses

def calendarpage():
    root.destroy()
    import calendar

def feespage():
    root.destroy()
    import fees

def bookspage():
    root.destroy()
    import books

def settingspage():
    root.destroy()
    import settings

def tohome():
    root.destroy()
    import home

def logout():
    c.execute("DELETE FROM sec")
    sdb.commit()
    sdb.close()
    tohome()

# Labels for the SECTIONS
tblabel = Label(titlebar, text="OHIO ACADEMY", bg=priclr, fg=offwyt, font=('ariel', 18, 'bold')).place(x=20, y=10)
navdashboardbtn = Button(navbar, text="Dashboard", fg="#06283D", bg=offwyt).place(x=20, y=60)
navcoursesbtn = Button(navbar, text="Courses", bg="#06283D", fg="white", command=coursespage).place(x=100, y=60)
navcalendarbtn = Button(navbar, text="Calendar", bg="#06283D", fg="white", command=calendarpage).place(x=180, y=60)
navfeesbtn = Button(navbar, text="Fees", bg="#06283D", fg="white", command=feespage).place(x=260, y=60)
navbooksbtn = Button(navbar, text="Books", bg="#06283D", fg="white", command=bookspage).place(x=320, y=60)
navsettingsbtn = Button(navbar, text="Settings", bg="#06283D", fg="white", command=settingspage).place(x=400, y=60)
footerlabel = Label(footer, text="@ Copyright 2022 || Ohio Academy", bg="#06283D", fg="white").place(x=150, y=610)


#Create logout button
logoutbtn = Button(text="Logout", bg="#1363DF", fg="#DFF6FF", padx=10, command=logout).place(x=380, y=15)

# Create menubar
menubar = Menu(navbar)

# Add file menu and commands
dashboardmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Dashboard", menu=dashboardmenu)

coursesmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Courses", menu=coursesmenu)

calendarmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Calendar", menu=calendarmenu)

feesmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Fees", menu=feesmenu)

booksmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Books", menu=booksmenu)

settingsmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Settings", menu=settingsmenu)

root.config(menu = menubar)

# Grid the main
# tk.Label(root, ).grid(column=4,row=5)



root.mainloop()