# tkinter and ttk module
from tkinter import *
from tkinter.ttk import *

# creates a Tk() object
master = Tk()

# sets the geometry of main
# root window
master.geometry("300x300")

# function to open a new window
# on a button click
def openNewWindow():
    # Toplevel object which will
    # be treated as a new openNewWindow
    newWindow = Toplevel(master)
    # sets the title of the Toplevel widget
    newWindow.title("New Window")

    # sets the geometry of Toplevel
    newWindow.geometry("300x300")


    # A Label widget to show in Toplevel

    Label(newWindow, text="new window").pack()

    label = Label(master, text="main window")
    label.pack(pady=10)

# a button widget which will open a new window on button click
btn = Button(master,text="open a new window",command=openNewWindow)
btn.pack(pady=10)

# mainloop, runs infinitely
mainloop()
