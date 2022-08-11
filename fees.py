from tkinter import *
from tkinter import ttk


root = Tk()
root.title("Ohio Academy | School Fees")
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
main = Frame(width=500, height=500, bg="#DFF6FF").pack()
footer = Frame(width=500, height=50, bg='#06283D').pack()

# table
my_game = ttk.Treeview(root)

my_game['columns'] = ('SN', 'DEPARTMENT', 'LEVEL', 'PROGRAM', 'FEES')

my_game.column("#0", width=0,  stretch=NO)
my_game.column("SN",anchor=CENTER, width=40)
my_game.column("DEPARTMENT",anchor=CENTER,width=120)
my_game.column("LEVEL",anchor=CENTER,width=60)
my_game.column("PROGRAM",anchor=CENTER,width=100)
my_game.column("FEES",anchor=CENTER,width=100)

my_game.heading("#0",text="",anchor=CENTER)
my_game.heading("SN",text="SN",anchor=CENTER)
my_game.heading("DEPARTMENT",text="DEPARTMENT",anchor=CENTER)
my_game.heading("LEVEL",text="LEVEL",anchor=CENTER)
my_game.heading("PROGRAM",text="PROGRAM",anchor=CENTER)
my_game.heading("FEES",text="FEES",anchor=CENTER)

my_game.insert(parent='',index='end',iid=0,text='',
values=('1','Com Sc','Level 1','Full-time', 'N15,000'))
my_game.insert(parent='',index='end',iid=1,text='',
values=('2','Com Sc','Level 2','Full-time', 'N25,000'))
my_game.insert(parent='',index='end',iid=2,text='',
values=('3','Com Sc','Level 3','Full-time', 'N35,000'))
my_game.insert(parent='',index='end',iid=3,text='',
values=('4','Com Sc','Level 4','Full-time', 'N45,000'))
my_game.insert(parent='',index='end',iid=4,text='',
values=('5','Com Sc','Level 5','Full-time', 'N50,000'))
my_game.insert(parent='',index='end',iid=5,text='',
values=('6','Com Sc','Level 6','Full-time', 'N65,000'))
my_game.insert(parent='',index='end',iid=6,text='',
values=('7','Sociology','Level 1','Full-time', 'N15,000'))
my_game.insert(parent='',index='end',iid=7,text='',
values=('8','Sociology','Level 2','Full-time', 'N25,000'))
my_game.insert(parent='',index='end',iid=8,text='',
values=('9','Sociology','Level 3','Full-time', 'N35,000'))
my_game.insert(parent='',index='end',iid=9,text='',
values=('10','Sociology','Level 4','Full-time', 'N45,000'))
my_game.insert(parent='',index='end',iid=10,text='',
values=('11','Sociology','Level 5','Full-time', 'N50,000'))
my_game.insert(parent='',index='end',iid=11,text='',
values=('12','Sociology','Level 6','Full-time', 'N65,000'))

my_game.place(x=40, y=150)


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


# Labels for the SECTIONS
tblabel = Label(titlebar, text="OHIO ACADEMY", bg="#06283D", fg="white", font=(25)).place(x=20, y=10)
navdashboardbtn = Button(navbar, text="Dashboard", bg="#06283D", fg="white", command=dashboardpage).place(x=20, y=60)
navcoursesbtn = Button(navbar, text="Courses", bg="#06283D", fg="white", command=coursespage).place(x=100, y=60)
navcalendarbtn = Button(navbar, text="Calendar", bg="#06283D", fg="white", command=calendarpage).place(x=180, y=60)
navfeesbtn = Button(navbar, text="Fees", fg="#06283D", bg="white").place(x=260, y=60)
navbooksbtn = Button(navbar, text="Books", bg="#06283D", fg="white", command=bookspage).place(x=320, y=60)
navsettingsbtn = Button(navbar, text="Settings", bg="#06283D", fg="white", command=settingspage).place(x=400, y=60)
footerlabel = Label(footer, text="@ Copyright 2022 || Ohio Academy", bg="#06283D", fg="white").place(x=150, y=610)


#Create logout button
logoutbtn = Button(text="Logout", bg="#1363DF", fg="#DFF6FF", padx=10, command=tohome).place(x=380, y=15)

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