from tkinter import *
import sqlite3

with sqlite3.connect("studentsdb") as sdb:
    c = sdb.cursor()

root = Tk()
root.title("Ohio Academy | Settings")
# root.geometry("700x600")

# Variable
priclr = "#06283D"
secclr = "#1363DF"
acentclr = "#47B5FF"
offwyt = "#DFF6FF"

mainwidth = 500
mainheight = 500

# Sections
titlebar = Frame(width=500, height=50, bg=priclr).pack()
navbar = Frame(width=500, height=50, bg=priclr).pack()
main = Frame(width=500, height=500, bg=offwyt).pack()
footer = Frame(width=500, height=50, bg=priclr).pack()


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
    tohome()


# Labels for the SECTIONS
tblabel = Label(titlebar, text="OHIO ACADEMY", bg="#06283D", fg="white", font=(25)).place(x=20, y=10)
navdashboardbtn = Button(navbar, text="Dashboard", bg="#06283D", fg="white", command=dashboardpage).place(x=20, y=60)
navcoursesbtn = Button(navbar, text="Courses", bg="#06283D", fg="white", command=coursespage).place(x=100, y=60)
navcalendarbtn = Button(navbar, text="Calendar", bg="#06283D", fg="white", command=calendarpage).place(x=180, y=60)
navfeesbtn = Button(navbar, text="Fees", bg="#06283D", fg="white", command=feespage).place(x=260, y=60)
navbooksbtn = Button(navbar, text="Books", bg="#06283D", fg="white", command=bookspage).place(x=320, y=60)
navsettingsbtn = Button(navbar, text="Settings", fg="#06283D", bg="white").place(x=400, y=60)
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