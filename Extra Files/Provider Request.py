from tkinter import *

def save_info():
    provider_num = provider.get()
    date_num = date.get()
    print(provider_num, date_num)

    file = open("Weekly Payment Report.txt", "w")
    file.write("Provider Number: " + provider_num + "\n")
    file.write("Date: " + date_num + "\n")
    file.close()
    print(" User ", provider_num, " has been registered successfully")

    provider_entry.delete(0, END)
    date_entry.delete(0, END)



screen = Tk()
screen.geometry("500x500")
screen.title("Python Form")
heading = Label(text = "Python Form", bg = "grey", fg = "black", width = "500", height = "3")
heading.pack()


providerNum_text = Label(text = "Provider# * ",)
dateNum_text = Label(text = "Date * ",)
providerNum_text.place(x = 15, y = 70)
dateNum_text.place(x = 15, y = 140)


provider = StringVar()
date = StringVar()


provider_entry = Entry(textvariable = provider, width = "30")
date_entry = Entry(textvariable = date, width = "30")

provider_entry.place(x = 15, y = 100)
date_entry.place(x = 15, y = 180)


report = Button(screen,text = "Submit Report", width = "30", height = "2", command = save_info, bg = "grey")
report.place(x = 15, y = 290)

