from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Ohio Academy | Registration")
# root.title("Ohio Academy | Dashboard")
# root.geometry("700x600")


# Variable
priclr = "#06283D"
secclr = "#1363DF"
acentclr = "#47B5FF"
offwyt = "#DFF6FF"


mainwidth = 500
mainheight = 600

# Fucntions
def backtologin():
    root.destroy()
    import home

# Sections
main = Frame(root, width=mainwidth, height=mainheight, bg="#DFF6FF").pack()

titlelabel = Label(text="OHIO ACADEMY", bg="#DFF6FF", fg="#06283D", font=('ariel', 24, 'bold')).place(x=180, y=20)
pagemsg = Label(text="Please enter details below to register", bg="#DFF6FF", fg="#06283D").place(x=150, y=60)

fullnamelabel = Label(text="Fullname", bg="#DFF6FF", fg="#06283D", font=(35)).place(x=100, y=100)
fullnametxb = Entry(root, width=33, font=24).place(x=100, y=130)

deptlabel = Label(text="Department", bg="#DFF6FF", fg="#06283D", font=(35)).place(x=100, y=160)
depttxb = Entry(root, width=33, font=24).place(x=100, y=190)

levellabel = Label(text="Level", bg="#DFF6FF", fg="#06283D", font=(35)).place(x=100, y=210)
leveltxb = Entry(root, width=33, font=24).place(x=100, y=240)

genderlabel = Label(text="Gender", bg="#DFF6FF", fg="#06283D", font=(35)).place(x=100, y=270)
gendertxb = Entry(root, width=33, font=24).place(x=100, y=300)

emaillabel = Label(text="Email", bg="#DFF6FF", fg="#06283D", font=(35)).place(x=100, y=330)
emailtxb = Entry(root, width=33, font=24).place(x=100, y=360)

passwordlabel = Label(text="Password", bg="#DFF6FF", fg="#06283D", font=(35)).place(x=100, y=390)
passwordtxb = Entry(root, width=33, font=24, show="*").place(x=100, y=420)

# Submit button
loginbtn = Button(root, text="Register", width=42, bg="#06283D", fg="#DFF6FF").place(x=100, y=460)


# Reg and reset redirect btns
backbtn = Button(root, text="<< Back to Login", bg="#DFF6FF", command=backtologin).place(x=300, y=510)

# Footer
footerlabel = Label(text="powered by Pyt2 Technologies", bg="#DFF6FF", fg="#06283D").place(x=mainwidth/2 - 100, y=mainheight-30)



# Add Logo image
# logo = PhotoImage(root, file='assets/logo.jpg')
# logolabel = ttk.Label(root, image=logo).pack()






root.mainloop()