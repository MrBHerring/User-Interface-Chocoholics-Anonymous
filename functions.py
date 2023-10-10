from tkinter import *
import tkinter
from PIL import Image, ImageTk
from tkinter import messagebox, filedialog
from reportWindows import display_Report, display_Invoice
from Manage_Member import manageMember
from Manage_Provider import manageProvider

#place an image on the grid
def display_logo(url, row, column):
    img = Image.open(url)
    #resize image
    img = img.resize((int(img.size[0]/1.5),int(img.size[1]/1.5)))
    img = ImageTk.PhotoImage(img)
    img_label = Label(image=img, bg="white")
    img_label.image = img
    img_label.grid(column=column, row=row, rowspan=2, sticky=NW, padx=20, pady=40)


def openMemberWindow():
    # Toplevel object which will
    # be treated as a new openNewWindow
    newWindow = Toplevel()
    # sets the title of the Toplevel widget
    newWindow.title("Member Login")

    # sets the geometry of Toplevel
    newWindow.geometry("340x440")
    newWindow.configure(bg='#333333')

    def login():
        username= "Mjin"
        password= "password"
        if username_entry.get()==username and password_entry.get()==password:
            messagebox.showinfo(title="Login Success", message="You successfully logged in.")
            memberWindow = Toplevel()
            memberWindow.title("Hello Member " + username)
            memberWindow.geometry("700x400")
            memberWindow.configure(bg='#333333')
            member_hello = tkinter.Label(memberWindow, text="Hello Member " + username, bg='gray', fg='brown', font=("Arial, 30"))
            member_hello.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
            check_status_button = tkinter.Button(memberWindow, text="Check Status", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=checkStatus)
            check_status_button.grid(row=2, column=1, columnspan=2, pady=30)
            renew_membership_button = tkinter.Button(memberWindow, text="Renew Membership", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=renewMembership)
            renew_membership_button.grid(row=2, column=3, columnspan=2, pady=30)

            invoice_button = tkinter.Button(memberWindow, text="Request Invoice", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=display_Invoice)
            invoice_button.grid(row=3, column=1, columnspan=2, pady=30)
            logout_button = tkinter.Button(memberWindow, text="Logout", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=memberWindow.destroy)
            logout_button.grid(row=3, column=3, columnspan=2,pady=30)


        elif username_entry.get()!=username:
            messagebox.showerror(title="Error", message="Invalid Username.")
        else:
            messagebox.showerror(title="Error", message="Invalid Password.")

    def checkStatus():
        status = "Active"
        #status = "Inactive"
        if status == "Active":
            messagebox.showinfo(title="Member Status", message="Your membership is currently active.")
        else:
            messagebox.showinfo(title="Member Status", message="Your membership is currently inactive.")

    def renewMembership():
        #status = "Active"
        status = "Inactive"
        def submit():
            cardNumber = "123456"
            cardSecurity = "123"
            if card_number_entry.get()==cardNumber and card_security_entry.get()==cardSecurity:
                messagebox.showinfo(title="Payment Successful", message ="Your payment has gone through successfully.")
            else:
                messagebox.showinfo(title="Payment Failed", message ="Your payment did not go through successfully. Please reeenter your payment information or try a different card.")

        if status == "Active":
            messagebox.showinfo(title="Member Status", message="Your membership is currently active. No need to renew membership.")
        else:
            renewMemberWindow = Toplevel()
            renewMemberWindow.title("Renew Membership")
            renewMemberWindow.geometry("400x600")
            renewMemberWindow.configure(bg='#333333')
            renew_label = tkinter.Label(renewMemberWindow, text="Renew Membership", bg='#333333', fg='brown', font=("Arial, 30"))
            card_number_label = tkinter.Label(renewMemberWindow, text="Card Number", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
            card_number_entry = tkinter.Entry(renewMemberWindow, font=("Arial, 16"))
            card_security_label = tkinter.Label(renewMemberWindow, text="Card Security Code", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
            card_security_entry = tkinter.Entry(renewMemberWindow, font=("Arial, 16"))
            submit_button = tkinter.Button(renewMemberWindow, text="Submit Payment", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=submit)

            renew_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
            card_number_label.grid(row=1, column=0)
            card_number_entry.grid(row=1, column=1, pady=20)
            card_security_label.grid(row=2, column=0)
            card_security_entry.grid(row=2, column=1, pady=20)
            submit_button.grid(row=3, column=0, columnspan=2, pady=30)


    # Creating widgets
    login_label = tkinter.Label(newWindow, text="Member Login", bg='#333333', fg='brown', font=("Arial, 30"))
    username_label = tkinter.Label(newWindow, text="Username", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
    username_entry = tkinter.Entry(newWindow,font=("Arial, 16"))
    password_entry = tkinter.Entry(newWindow, show="*",font=("Arial, 16"))
    password_label = tkinter.Label(newWindow, text="Password", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
    login_button = tkinter.Button(newWindow, text="Login", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=login)


    # Placing widgets on the screen
    login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
    username_label.grid(row=1, column=0)
    username_entry.grid(row=1, column=1, pady=20)
    password_label.grid(row=2, column=0)
    password_entry.grid(row=2, column=1, pady=20)
    login_button.grid(row=3, column=0, columnspan=2, pady=30)






def openProviderWindow():
    # Toplevel object which will
    # be treated as a new openNewWindow
    newWindow = Toplevel()
    # sets the title of the Toplevel widget
    newWindow.title("Provider Login")

    # sets the geometry of Toplevel
    newWindow.geometry("340x440")
    newWindow.configure(bg='#333333')

    def login():
        username= "Mjin"
        password= "password"
        if username_entry.get()==username and password_entry.get()==password:
            messagebox.showinfo(title="Login Success", message="You successfully logged in.")

            providerWindow = Toplevel()
            providerWindow.title("Hello Provider " + username)
            providerWindow.geometry("340x440")
            providerWindow.configure(bg='#333333')
            report_button = tkinter.Button(providerWindow, text="Request Report", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=display_Report)
            report_button.grid(row=3, column=0, columnspan=2,padx=(0,250), pady=30)
            logout_button = tkinter.Button(providerWindow, text="Logout", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=providerWindow.destroy)
            logout_button.grid(row=6, column=0, columnspan=2,padx=(0,250), pady=30)
#Edward's part 2
            verify_member = tkinter.Button(providerWindow, text="Verify member", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=verifying_member)
            verify_member.grid(row=4, column=0, columnspan=2,padx=(0,250), pady=30)

#Edward's part 3
            provider_submit = tkinter.Button(providerWindow, text="Submit a Claim", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=Submit_ProviderClaim)
            provider_submit.grid(row=4, column=1, columnspan=2,padx=(0,90), pady=30)
#Edward's part 4
            provider_directory = tkinter.Button(providerWindow, text="Search Directory", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=directory_search)
            provider_directory.grid(row=5, column=0, columnspan=2,padx=(0,220), pady=30)
            
        elif username_entry.get()!=username:
            messagebox.showerror(title="Error", message="Invalid Username.")
        else:
            messagebox.showerror(title="Error", message="Invalid Password.")


#Edward's part 2
    def verifying_member():
        def submit():
            validMemberNumber= "2929"
            expiredNumber= "3636"
            if valid_entry.get()==validMemberNumber:
                messagebox.showinfo(title="Member Status", message ="Valid")
            elif valid_entry.get()==expiredNumber:
                messagebox.showinfo(title="Member Status", message ="Expired")
            else:
                messagebox.showinfo(title="Member Status", message ="Non-existing")
        #status = "Active"
        #status = "Inactive"
        verifyMemberWindow = Toplevel()
        verifyMemberWindow.title("Verify Membership")
        verifyMemberWindow.geometry("400x600")
        verifyMemberWindow.configure(bg='#333333')
        verify_label = tkinter.Label(verifyMemberWindow, text="Verify Member", bg='#333333', fg='brown', font=("Arial, 30"))
        valid_entry = tkinter.Entry(verifyMemberWindow, font=("Arial, 16"))
        verify_btn = tkinter.Button(verifyMemberWindow, text="Verify", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=submit)

        verify_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
        valid_entry.grid(row=2, column=1, pady=20)
        verify_btn.grid(row=3, column=0, columnspan=2, pady=30)

#Edward's part 3
    def Submit_ProviderClaim():
        ServiceCodes = []
        def displayInfo(ServiceCodes, code):
            found = False
            pos = 0
            while pos< len(ServiceCodes) and not found:
                if ServiceCodes[pos][0] == code:
                    found = True
                pos+=1
            if found:
                messagebox.showinfo(message = "Success")

                return ServiceCodes[pos-1][1]
            else:
                messagebox.showerror(message = "Unsuccessful")

        def clickArea():
            dollarFloat.set(displayInfo(ServiceCodes, code.get()))

        def createList():
            codeFile = open ("ServiceCodes.txt", 'r')
            for line in codeFile:
                coding = line.split()
                ServiceCodes.append(coding)
            codeFile.close()
            return ServiceCodes

        #status = "Active"
        #status = "Inactive"
        submitClaimWindow = Toplevel()
        submitClaimWindow.title("Submit a claim")
        #submitClaimWindow.geometry("400x600")
        #submitClaimWindow.configure(bg='#333333')
        #claim_label = tkinter.Label(submitClaimWindow, text="Code", bg='#333333', fg='brown', font=("Arial, 30"))
        #claim_entry = tkinter.Entry(submitClaimWindow, font=("Arial, 16"))
        #claim_btn = tkinter.Button(submitClaimWindow, text="Submit", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=submit)

        #claim_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
        #claim_entry.grid(row=2, column=1, pady=20)
        #claim_btn.grid(row=3, column=0, columnspan=2, pady=30)

        Label(submitClaimWindow, text="Code").grid(row=0, column=0)
        code = StringVar()
        Entry(submitClaimWindow, textvariable=code).grid(row=0, column=1)

        Label(submitClaimWindow, text="Fee $").grid(row=2, column=0)
        dollarFloat = IntVar()
        Entry(submitClaimWindow, textvariable=dollarFloat).grid(row=2, column=1)

        button = Button(submitClaimWindow, text="Submit Claim", command=clickArea)
        button.grid(row=3, column=0, columnspan=2)
        createList()
        print(ServiceCodes)
#Edward's part 4

    def directory_search():
        directWindow = Toplevel()
        # sets the title of the Toplevel widget
        directWindow.title("Search Directory")

        # sets the geometry of Toplevel
        directWindow.geometry("400x200")
        my_dir=''

        def my_fun():
            my_dir=filedialog.askdirectory()
            l1.config(text=my_dir)
        b1=tkinter.Button(directWindow,text='Select Directory',font=22,
                         command=lambda:my_fun(),bg='lightgreen')
        b1.grid(row=0,column=0,padx=10,pady=20)
        l1=tkinter.Label(directWindow,text=my_dir,bg='yellow',font=18)
        l1.grid(row=0,column=1,padx=2)





#        if status == "Active":
#            messagebox.showinfo(title="Member Status", message="Your membership is currently active. No need to renew membership.")
#        else:





    # Creating widgets
    login_label = tkinter.Label(newWindow, text="Provider Login", bg='#333333', fg='brown', font=("Arial, 30"))
    username_label = tkinter.Label(newWindow, text="Username", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
    username_entry = tkinter.Entry(newWindow,font=("Arial, 16"))
    password_entry = tkinter.Entry(newWindow, show="*",font=("Arial, 16"))
    password_label = tkinter.Label(newWindow, text="Password", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
    login_button = tkinter.Button(newWindow, text="Login", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=login)

    # Placing widgets on the screen
    login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
    username_label.grid(row=1, column=0)
    username_entry.grid(row=1, column=1, pady=20)
    password_label.grid(row=2, column=0)
    password_entry.grid(row=2, column=1, pady=20)
    login_button.grid(row=3, column=0, columnspan=2, pady=30)

def openManagerWindow():
    # Toplevel object which will
    # be treated as a new openNewWindow
    newWindow = Toplevel()
    # sets the title of the Toplevel widget
    newWindow.title("Manager Login")

    # sets the geometry of Toplevel
    newWindow.geometry("340x440")
    newWindow.configure(bg='#333333')

    def login():
        username= "Mjin"
        password= "password"
        if username_entry.get()==username and password_entry.get()==password:
            messagebox.showinfo(title="Login Success", message="You successfully logged in.")

            managerWindow = Toplevel()
            managerWindow.title("Hello Manager " + username)
            managerWindow.geometry("700x400")
            managerWindow.configure(bg='#333333')
            report_button = tkinter.Button(managerWindow, text="Request Report", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=display_Report)
            report_button.grid(row=3, column=0, columnspan=2,padx=(0,250), pady=30)
            invoice_button = tkinter.Button(managerWindow, text="Request Invoice", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=display_Invoice)
            invoice_button.grid(row=4, column=0, columnspan=2,padx=(0,250), pady=50)
            logout_button = tkinter.Button(managerWindow, text="Logout", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=managerWindow.destroy)
            logout_button.grid(row=5, column=0, columnspan=2,padx=(0,250), pady=30)

            manageMemberBtn = tkinter.Button(managerWindow, text="Manage Member", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=manageMember)
            manageMemberBtn.grid(row=3, column=1, columnspan=2, pady=30)

            manageProviderBtn = tkinter.Button(managerWindow, text="Manage Provider", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=manageProvider)
            manageProviderBtn.grid(row=4, column=1, columnspan=2, pady=30)

        elif username_entry.get()!=username:
            messagebox.showerror(title="Error", message="Invalid Username.")
        else:
            messagebox.showerror(title="Error", message="Invalid Password.")

    # Creating widgets
    login_label = tkinter.Label(newWindow, text="Manager Login", bg='#333333', fg='brown', font=("Arial, 30"))
    username_label = tkinter.Label(newWindow, text="Username", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
    username_entry = tkinter.Entry(newWindow,font=("Arial, 16"))
    password_entry = tkinter.Entry(newWindow, show="*",font=("Arial, 16"))
    password_label = tkinter.Label(newWindow, text="Password", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
    login_button = tkinter.Button(newWindow, text="Login", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=login)

    # Placing widgets on the screen
    login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
    username_label.grid(row=1, column=0)
    username_entry.grid(row=1, column=1, pady=20)
    password_label.grid(row=2, column=0)
    password_entry.grid(row=2, column=1, pady=20)
    login_button.grid(row=3, column=0, columnspan=2, pady=30)


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Schedule Report
def Schedule_Report():
    # Toplevel object which will
    # be treated as a new openNewWindow
    ScheduleWindow = Toplevel()
    # sets the title of the Toplevel widget
    ScheduleWindow.title("Choose Report")

    # sets the geometry of Toplevel
    ScheduleWindow.geometry("340x440")
    ScheduleWindow.configure(bg='#333333')


    # Creating widgets
    dailyReport_btn = tkinter.Button(ScheduleWindow, text="Daily Report", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=DailyReport)
    weeklyReport_btn = tkinter.Button(ScheduleWindow, text="Weekly Report", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=WeeklyReport)
    monthlyReport_btn = tkinter.Button(ScheduleWindow, text="Monthly Report", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=MonthlyReport)
    dailyMember_btn = tkinter.Button(ScheduleWindow, text="Daily Membership", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=DailyMemberships)



    # Placing widgets on the screen
    dailyReport_btn.grid(row=3, column=0, columnspan=2,padx=(0,250), pady=30)
    weeklyReport_btn.grid(row=4, column=0, columnspan=2,padx=(0,250), pady=30)
    monthlyReport_btn.grid(row=5, column=0, columnspan=2,padx=(0,250), pady=30)
    dailyMember_btn.grid(row=6, column=0, columnspan=2,padx=(0,250), pady=30)



#Daily Service Report
def DailyReport():
    # Toplevel object which will
    # be treated as a new openNewWindow
    writeDaily = Toplevel()
    # sets the title of the Toplevel widget
    writeDaily.title("Daily Request")

    # sets the geometry of Toplevel
    writeDaily.geometry("500x500")
    writeDaily.configure(bg='#333333')

    def save_info():
        date_num = date.get()
        print(date_num)

        file = open("Daily Report.txt", "w")
        file.write("Date: " + date_num + "\n")
        file.close()
        print("Success")

        date_entry.delete(0, END)

    date = StringVar()



           # Creating widgets
    daily_label = tkinter.Label(writeDaily, text="Daily Report", bg='#333333', fg='brown', font=("Arial, 30"))
    date_entry = tkinter.Entry(writeDaily,textvariable = date,font=("Arial, 16"))
    date_label = tkinter.Label(writeDaily, text="Date", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
    submit_button = tkinter.Button(writeDaily, text="Submit", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=save_info)


    # Placing widgets on the screen
    daily_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
    date_label.grid(row=1, column=0)
    date_entry.grid(row=1, column=1, pady=20)
    submit_button.grid(row=3, column=0, columnspan=2, pady=30)


#Weekly Service Report
def WeeklyReport():
    # Toplevel object which will
    # be treated as a new openNewWindow
    writeWeekly = Toplevel()
    # sets the title of the Toplevel widget
    writeWeekly.title("Weekly Report")

    # sets the geometry of Toplevel
    writeWeekly.geometry("500x500")
    writeWeekly.configure(bg='#333333')

    def save_info():
        date_num = date.get()
        print(date_num)

        file = open("Weekly Report.txt", "w")
        file.write("Date: " + date_num + "\n")
        file.close()
        print("Success")

        date_entry.delete(0, END)

    date = StringVar()



           # Creating widgets
    weekly_label = tkinter.Label(writeWeekly, text="Weekly Report", bg='#333333', fg='brown', font=("Arial, 30"))
    date_entry = tkinter.Entry(writeWeekly,textvariable = date,font=("Arial, 16"))
    date_label = tkinter.Label(writeWeekly, text="Date", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
    submit_button = tkinter.Button(writeWeekly, text="Submit", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=save_info)


    # Placing widgets on the screen
    weekly_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
    date_label.grid(row=1, column=0)
    date_entry.grid(row=1, column=1, pady=20)
    submit_button.grid(row=3, column=0, columnspan=2, pady=30)

#Monthly Service Report
def MonthlyReport():
    # Toplevel object which will
    # be treated as a new openNewWindow
    writeMonthly = Toplevel()
    # sets the title of the Toplevel widget
    writeMonthly.title("Monthly Report")

    # sets the geometry of Toplevel
    writeMonthly.geometry("500x500")
    writeMonthly.configure(bg='#333333')

    def save_info():
        date_num = date.get()
        print(date_num)

        file = open("Monthly Report.txt", "w")
        file.write("Date: " + date_num + "\n")
        file.close()
        print("Success")

        date_entry.delete(0, END)

    date = StringVar()



           # Creating widgets
    monthly_label = tkinter.Label(writeMonthly, text="Monthly Report", bg='#333333', fg='brown', font=("Arial, 30"))
    date_entry = tkinter.Entry(writeMonthly,textvariable = date,font=("Arial, 16"))
    date_label = tkinter.Label(writeMonthly, text="Date", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
    submit_button = tkinter.Button(writeMonthly, text="Submit", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=save_info)


    # Placing widgets on the screen
    monthly_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
    date_label.grid(row=1, column=0)
    date_entry.grid(row=1, column=1, pady=20)
    submit_button.grid(row=3, column=0, columnspan=2, pady=30)

#Daily Memberships
def DailyMemberships():
    # Toplevel object which will
    # be treated as a new openNewWindow
    writeMemberships = Toplevel()
    # sets the title of the Toplevel widget
    writeMemberships.title("Daily Memberships")

    # sets the geometry of Toplevel
    writeMemberships.geometry("500x500")
    writeMemberships.configure(bg='#333333')

    def save_info():
        date_num = date.get()
        print(date_num)

        file = open("Daily Memberships.txt", "w")
        file.write("Date: " + date_num + "\n")
        file.close()
        print("Success")

        date_entry.delete(0, END)

    date = StringVar()



           # Creating widgets
    memberships_label = tkinter.Label(writeMemberships, text="Daily Memberships", bg='#333333', fg='brown', font=("Arial, 30"))
    date_entry = tkinter.Entry(writeMemberships,textvariable = date,font=("Arial, 16"))
    date_label = tkinter.Label(writeMemberships, text="Date", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
    submit_button = tkinter.Button(writeMemberships, text="Submit", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=save_info)


    # Placing widgets on the screen
    memberships_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
    date_label.grid(row=1, column=0)
    date_entry.grid(row=1, column=1, pady=20)
    submit_button.grid(row=3, column=0, columnspan=2, pady=30)


def SearchService():
    ServiceCodes = []
    def displayInfo(ServiceCodes, code):
        found = False
        pos = 0
        while pos< len(ServiceCodes) and not found:
            if ServiceCodes[pos][0] == code:
                found = True
            pos+=1
        if found:
            messagebox.showinfo(message = "Success")

            return ServiceCodes[pos-1][1]
        else:
            messagebox.showerror(message = "Unsuccessful")

    def clickArea():
        dollarFloat.set(displayInfo(ServiceCodes, code.get()))

    def createList():
        codeFile = open ("ServiceCodes.txt", 'r')
        for line in codeFile:
            coding = line.split()
            ServiceCodes.append(coding)
        codeFile.close()
        return ServiceCodes

    #status = "Active"
    #status = "Inactive"
    CodeService = Toplevel()
    CodeService.title("Search a code")
    #submitClaimWindow.geometry("400x600")
    #submitClaimWindow.configure(bg='#333333')
    #claim_label = tkinter.Label(submitClaimWindow, text="Code", bg='#333333', fg='brown', font=("Arial, 30"))
    #claim_entry = tkinter.Entry(submitClaimWindow, font=("Arial, 16"))
    #claim_btn = tkinter.Button(submitClaimWindow, text="Submit", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=submit)

    #claim_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
    #claim_entry.grid(row=2, column=1, pady=20)
    #claim_btn.grid(row=3, column=0, columnspan=2, pady=30)

    Label(CodeService, text="Code").grid(row=0, column=0)
    code = StringVar()
    Entry(CodeService, textvariable=code).grid(row=0, column=1)

    Label(CodeService, text="Fee $").grid(row=2, column=0)
    dollarFloat = IntVar()
    Entry(CodeService, textvariable=dollarFloat).grid(row=2, column=1)

    button = Button(CodeService, text="Submit Claim", command=clickArea)
    button.grid(row=3, column=0, columnspan=2)
    createList()
    print(ServiceCodes)
