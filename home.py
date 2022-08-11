from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Home | Login")
# root.title("Ohio Academy | Dashboard")
# root.geometry("700x600")


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

def todashboard():
    root.destroy()
    import dashboard

# Sections
main = Frame(root, width=mainwidth, height=mainheight, bg="#DFF6FF").pack()

titlelabel = Label(text="OHIO ACADEMY", bg="#DFF6FF", fg="#06283D", font=('ariel', 24, 'bold')).place(x=120, y=80)
pagemsg = Label(text="Please enter details below to login", bg="#DFF6FF", fg="#06283D").place(x=150, y=120)
emaillabel = Label(text="Email", bg="#DFF6FF", fg="#06283D", font=(35)).place(x=100, y=150)
passwordlabel = Label(text="Password", bg="#DFF6FF", fg="#06283D", font=(35)).place(x=100, y=220)
footerlabel = Label(text="powered by Pyt2 Technologies", bg="#DFF6FF", fg="#06283D").place(x=mainwidth/2 - 100, y=mainheight-30)

# Add textbox
emailtxb = Entry(root, width=33, font=24).place(x=100, y=180)
passwordtxb = Entry(root, width=33, font=24, show="*").place(x=100, y=250)

# Reg and reset redirect btns
regbtn = Button(root, text="Register", bg="#DFF6FF", command=toregister).place(x=100, y=370)
resetbtn = Button(root, text="Forget password?", bg="#DFF6FF", command=toreset).place(x=300, y=370)


# Submit button
loginbtn = Button(root, text="Login", width=42, bg="#06283D", fg="#DFF6FF", command=todashboard).place(x=100, y=300)


# Add Logo image
# logo = PhotoImage(root, file='assets/logo.jpg')
# logolabel = ttk.Label(root, image=logo).pack()






root.mainloop()