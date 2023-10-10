from tkinter import *
import tkinter




def display_Report():
    # Toplevel object which will
    # be treated as a new openNewWindow
    makeReport = Toplevel()
    # sets the title of the Toplevel widget
    makeReport.title("Provider Request")

    # sets the geometry of Toplevel
    makeReport.geometry("500x500")
    makeReport.configure(bg='#333333')

    def save_info():
        provider_num = provider.get()
        date_num = date.get()
        print(provider_num, date_num)

        file = open("Weekly Payment Report.txt", "w")
        file.write("Provider Number: " + provider_num + "\n")
        file.write("Date: " + date_num + "\n")
        file.close()
        print(" Provider ", provider_num, " has been registered successfully")

        provider_entry.delete(0, END)
        date_entry.delete(0, END)

    provider = StringVar()
    date = StringVar()

           # Creating widgets
    report_label = tkinter.Label(makeReport, text="Provider Report", bg='#333333', fg='brown', font=("Arial, 30"))
    provider_label = tkinter.Label(makeReport, text="Provider#", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
    provider_entry = tkinter.Entry(makeReport,textvariable = provider,font=("Arial, 16"))
    date_entry = tkinter.Entry(makeReport,textvariable = date,font=("Arial, 16"))
    date_label = tkinter.Label(makeReport, text="Date", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
    submit_button = tkinter.Button(makeReport, text="Generate Report", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=save_info)
   
    
    # Placing widgets on the screen
    report_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
    provider_label.grid(row=1, column=0)
    provider_entry.grid(row=1, column=1, pady=20)
    date_label.grid(row=2, column=0)
    date_entry.grid(row=2, column=1, pady=20)
    submit_button.grid(row=3, column=0, columnspan=2, pady=30)




def display_Invoice():
    # Toplevel object which will
    # be treated as a new openNewWindow
    makeInvoice = Toplevel()
    # sets the title of the Toplevel widget
    makeInvoice.title("Member Request")

    # sets the geometry of Toplevel
    makeInvoice.geometry("500x500")
    makeInvoice.configure(bg='#333333')

    def save_info():
        member_num = member.get()
        date_num = date.get()
        print(member_num, date_num)

        file = open("Weekly Invoice.txt", "w")
        file.write("Member Number: " + member_num + "\n")
        file.write("Date: " + date_num + "\n")
        file.close()
        print(" Member ", member_num, " has been registered successfully")

        member_entry.delete(0, END)
        date_entry.delete(0, END)

    member = StringVar()
    date = StringVar()



           # Creating widgets
    invoice_label = tkinter.Label(makeInvoice, text="Member Invoice", bg='#333333', fg='brown', font=("Arial, 30"))
    member_label = tkinter.Label(makeInvoice, text="Member#", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
    member_entry = tkinter.Entry(makeInvoice,textvariable = member,font=("Arial, 16"))
    date_entry = tkinter.Entry(makeInvoice,textvariable = date,font=("Arial, 16"))
    date_label = tkinter.Label(makeInvoice, text="Date", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
    submit_button = tkinter.Button(makeInvoice, text="Generate Invoice", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=save_info)
   
    
    # Placing widgets on the screen
    invoice_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
    member_label.grid(row=1, column=0)
    member_entry.grid(row=1, column=1, pady=20)
    date_label.grid(row=2, column=0)
    date_entry.grid(row=2, column=1, pady=20)
    submit_button.grid(row=3, column=0, columnspan=2, pady=30)



    




