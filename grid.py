from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Home | Login")
root.geometry("500x500")
# root.grid(row=14, column=3)

# Function
def tohome():
    root.destroy()
    import home

# Create menubar
menubar = Menu(root)

# Add file menu and commands
dashboardmenu = Menu(menubar, tearoff=0, postcommand=tohome)
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



# Variable
priclr = "#06283D"
secclr = "#1363DF"
acentclr = "#47B5FF"
offwyt = "#DFF6FF"


mainwidth = 500
mainheight = 500

# Fucntions
def toregister():
    root.destroy()
    import register

def toreset():
    root.destroy()
    import reset

# Sections
# main = Frame(root, width=mainwidth, height=mainheight, bg="#DFF6FF").grid(row=14, column=3)

titlelabel = Label(root, text="OHIO ACADEMY", bg="#DFF6FF", fg="#06283D", font=(80)).grid(row=0, column=1, columnspan=2)
pagemsg = Label(root, text="Please enter details below to login", bg="#DFF6FF", fg="#06283D").grid(row=1, column=1)

emaillabel = Label(root, text="Email", bg="#DFF6FF", fg="#06283D", font=(35)).grid(row=4, column=1)
emailtxb = Entry(root, width=33, font=24).grid(row=5, column=1)

passwordlabel = Label(root, text="Password", bg="#DFF6FF", fg="#06283D", font=(35)).grid(row=7, column=1)
passwordtxb = Entry(root,width=33, font=24, show="*").grid(row=8, column=1)


# Submit button
loginbtn = Button(root, text="Login", width=42, bg="#06283D", fg="#DFF6FF").grid(row=10, column=1)


# # Reg and reset redirect btns
regbtn = Button(root, text="Register", bg="#DFF6FF", command=toregister).grid(row=12, column=1)
resetbtn = Button(root, text="Forget password?", bg="#DFF6FF", command=toreset).grid(row=12, column=1)




# Add Logo image
# logo = PhotoImage(root, file='assets/logo.jpg')
# logolabel = ttk.Label(root, image=logo).pack()

def drawTable():
    for i in range(3):
        for j in range(10):
            label1 = Label(root, width=20, text=data[i])
            label1.grid(row=i, column=j)



data = [("COR102","Computer science","15"),("COR103","Algorithms","19"),("COR103","Artificial Intelligence","5")]

drawTable()

footerlabel = Label(root, text="powered by Pyt2 Technologies", bg="#DFF6FF", fg="#06283D").grid(row=14, column=1)





root.mainloop()