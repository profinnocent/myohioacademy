from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Ohio Academy | Password Reset")
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
def backtologin():
    root.destroy()
    import home

# Sections

main = Frame(root, width=mainwidth, height=mainheight, bg="#DFF6FF").pack()

titlelabel = Label(text="OHIO ACADEMY", bg="#DFF6FF", fg="#06283D", font=('ariel', 24, 'bold')).place(x=180, y=80)
pagemsg = Label(text="Please enter details below to reset your password", bg="#DFF6FF", fg="#06283D").place(x=120, y=120)

emaillabel = Label(text="Email", bg="#DFF6FF", fg="#06283D", font=(35)).place(x=100, y=mainheight/2 - 80)
emailtxb = Entry(root, width=33, font=24).place(x=100, y=mainheight/2 - 50)

# Submit button
loginbtn = Button(root, text="Reset", width=42, bg="#06283D", fg="#DFF6FF").place(x=100, y=mainheight/2)

# Reg and reset redirect btns
backbtn = Button(root, text="<< Back to Login", bg="#DFF6FF", command=backtologin).place(x=300, y=mainheight/2 + 60)


# Add Logo image
# logo = PhotoImage(root, file='assets/logo.jpg')
# logolabel = ttk.Label(root, image=logo).pack()

footerlabel = Label(text="powered by Pyt2 Technologies", bg="#DFF6FF", fg="#06283D").place(x=mainwidth/2 - 100, y=mainheight-30)





root.mainloop()