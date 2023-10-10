from tkinter import *
from tkinter import messagebox
import tkinter.simpledialog
import csv

def serviceBoxing():


    #functions associated with the buttons
    def find_member():
        #brings up a dialogue box that asks the user to input a customer id
        customer_id = tkinter.simpledialog.askstring("askstring", "Enter your name")

        found=0
        #Open the results file containing all of the results
        with open('customer.txt','r') as csvfile:
            #All of the data from the file goes into the variable called reader
            reader = csv.reader(csvfile)
            #The for loop goes through each record
            for row in reader:
                #See if the customerID entered matches a record in the csv csv file
                if customer_id == row[0]:
                    found = 1
                    #creates labels on the Window and populates it with the record details
                    blank_firstname_label= Label(root,text=row[1]).grid(row=1,column=2)
                    blank_surname_label= Label(root,text=row[2]).grid(row=2,column=2)
                    #Checks to see if the gender is Male or Female and creates the label with the word Male or Female
                    if row[5]=='1':
                        blank_gender_label=Label(root,text="Male").grid(row=3,column=2)
                    else:
                        blank_gender_label=Label(root,text="Female").grid(row=3,column=2)
                    blank_email_label= Label(root,text=row[3]).grid(row=4,column=2)
                    blank_birthday_label= Label(root,text=row[4]).grid(row=5,column=2)
                    blank_mobile_label= Label(root,text=row[6]).grid(row=6,column=2)
        #close the file
        csvfile.close()
        #error message appears if it is not found in the csv file
        if found ==0:
            messagebox.showerror("error","try again")
            name = row[1]
            print(name)


    def back():
        print('here')

    def help_entry():
        #simple success message
        messagebox.showinfo("Information", "Click on Find button and enter a customer id")


    #Sets up the frame 0 we are using a single frame in this example
    root = Toplevel()
    root.config(background = "white")

    #------------------------------------------------------------------------------------------
    #GUI Components for each row

    #Row 0 Heading - watch the columnspan across 4 columns so that it is centered
    lblHeading = Label(root,text="Find Customer",font=('Arial',24,"bold")).grid(row=0,column=0)
    #Row 1 Components
    lblFirstName = Label(root,text="First Name",font=('Arial',14,"bold")).grid(row=1,column=1)
    #Row 2 Components
    lblLastName = Label(root,text="Last Name",font=('Arial',14,"bold")).grid(row=2,column=1)
    #Row 3 Components
    lblGender = Label(root,text="Gender",font=('Arial',14,"bold")).grid(row=3,column=1)
    #Row 4 Components
    lblemail = Label(root,text="Email",font=('Arial',14,"bold")).grid(row=4,column=1)
    #Row 5 Components
    lblbirthday = Label(root,text="Birthday",font=('Arial',14,"bold")).grid(row=5,column=1)
    #Row 6 Components
    lblmobile = Label(root,text="Mobile: +44",font=('Arial',14,"bold")).grid(row=6,column=1)



    #Row 7 Components
    #Here are all of the buttons
    find_button=Button(root, text="Find",command=find_member,bg='orange',fg='white').grid(row=7,column=0,sticky=E,padx=20,pady=10)
    back_button=Button(root, text="Back",command=back,bg='orange',fg='white').grid(row=7,column=1,sticky=E,padx=20,pady=10)
    help_button=Button(root, text="Help",command=help_entry,bg='orange',fg='white').grid(row=7,column=2,sticky=E,padx=20,pady=10)
    enterorder_button=Button(root, text="Enter Order",command=help_entry,bg='orange',fg='white').grid(row=7,column=3,sticky=E,padx=20,pady=10)

    close_window_button = tkinter.Button(root, text="Close Window", bg='orange',fg='white', command=root.destroy)
    close_window_button.grid(row=8, column=0, columnspan=2,padx=20, pady=10)
 
