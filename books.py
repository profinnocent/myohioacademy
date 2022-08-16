from tkinter import *
# from tkHyperLinkManager import HyperlinkManager
import webbrowser
from functools import partial

root = Tk()
root.title("Ohio Academy | School Books")
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

# Add books link for download
bkx = 30
bkbx = 400
bky = 120
bkd = 50
book1 = Label(main, text="(1) Linguistics Thoery by J.R Robin", font=('arial',12, 'bold'), bg="#DFF6FF")
book1.place(x=bkx, y=bky)
bk1btn = Button(main, text="Download", bg=priclr,fg=offwyt, padx=10)
bk1btn.place(x=bkbx, y=bky)

book2 = Label(main, text="(2) Advanced Physics  by Dawling Fetchell", font=('arial',12, 'bold'), bg="#DFF6FF")
book2.place(x=bkx, y=bky+bkd)
bk2btn = Button(main, text="Download", bg=priclr,fg=offwyt, padx=10)
bk2btn.place(x=bkbx, y=bky+bkd)

book3 = Label(main, text="(3) Human Psychology by T.Y Edger", font=('arial',12, 'bold'), bg="#DFF6FF")
book3.place(x=bkx, y=bky+(bkd*2))
bk3btn = Button(main, text="Download", bg=priclr,fg=offwyt, padx=10)
bk3btn.place(x=bkbx, y=bky+(bkd*2))

book4 = Label(main, text="(4) Linear Mathematics by C. Campton", font=('arial',12, 'bold'), bg="#DFF6FF")
book4.place(x=30, y=bky+(bkd*3))
bk4btn = Button(main, text="Download", bg=priclr,fg=offwyt, padx=10)
bk4btn.place(x=400, y=bky+(bkd*3))

book5 = Label(main, text="(5) Sociology by R. Janneing & C. Park", font=('arial',12, 'bold'), bg="#DFF6FF")
book5.place(x=30, y=bky+(bkd*4))
bk5btn = Button(main, text="Download", bg=priclr,fg=offwyt, padx=10)
bk5btn.place(x=400, y=bky+(bkd*4))

book6 = Label(main, text="(6) Thermodynamics by Fletcher T.H", font=('arial',12, 'bold'), bg="#DFF6FF")
book6.place(x=30, y=bky+(bkd*5))
bk6btn = Button(main, text="Download", bg=priclr,fg=offwyt, padx=10)
bk6btn.place(x=400, y=bky+(bkd*5))





footer = Frame(width=500, height=50, bg='#06283D').pack()


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
navfeesbtn = Button(navbar, text="Fees", bg="#06283D", fg="white", command=feespage).place(x=260, y=60)
navbooksbtn = Button(navbar, text="Books", fg="#06283D", bg="white").place(x=320, y=60)
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