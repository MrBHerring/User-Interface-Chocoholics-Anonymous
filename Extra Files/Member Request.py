from tkinter import *

def save_info():
    member_num = member.get()
    date_num = date.get()
    print(member_num, date_num)

    file = open("Weekly Invoice.txt", "w")
    file.write("Member Number: " + member_num + "\n")
    file.write("Date: " + date_num + "\n")
    file.close()
    print(" User ", member_num, " has been registered successfully")

    member_entry.delete(0, END)
    date_entry.delete(0, END)



screen = Tk()
screen.geometry("500x500")
screen.title("Python Form")
heading = Label(text = "Python Form", bg = "grey", fg = "black", width = "500", height = "3")
heading.pack()


memberNum_text = Label(text = "Member# * ",)
dateNum_text = Label(text = "Date * ",)
memberNum_text.place(x = 15, y = 70)
dateNum_text.place(x = 15, y = 140)


member = StringVar()
date = StringVar()


member_entry = Entry(textvariable = member, width = "30")
date_entry = Entry(textvariable = date, width = "30")

member_entry.place(x = 15, y = 100)
date_entry.place(x = 15, y = 180)


report = Button(screen,text = "Submit Report", width = "30", height = "2", command = save_info, bg = "grey")
report.place(x = 15, y = 290)

