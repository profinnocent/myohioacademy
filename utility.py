from tkinter import *
# from home import *
# from dashboard import *
from PIL import Image, ImageTk
import sqlite3

with sqlite3.connect("studentsdb") as sdb:
    c = sdb.cursor()

# Variable
priclr = "#06283D"
secclr = "#1363DF"
acentclr = "#47B5FF"
offwyt = "#DFF6FF"

mainwidth = 500
mainheight = 500


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


def logout2():
    c.execute("DELETE FROM sec")
    sdb.commit()
    sdb.close()

