from tkinter import *
import tkinter
from PIL import Image, ImageTk
from tkinter import messagebox
from datetime import date
import os.path

def manageMember():

    manageMemberWindow = Toplevel()
    manageMemberWindow.title("Manage Member")
    manageMemberWindow.geometry("800x800")
    manageMemberWindow.configure(bg='#333333')

    manage_member_label = tkinter.Label(manageMemberWindow, text="Manage Member", bg='#333333', fg='brown', font=("Arial, 30"))
    manage_member_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
    close_window_button = tkinter.Button(manageMemberWindow, text="Close Window", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=manageMemberWindow.destroy)
    close_window_button.grid(row=6, column=4, columnspan=2, pady=30)


    def addMember():
        addMemberWindow = Toplevel()
        addMemberWindow.title("Add Member")
        addMemberWindow.geometry("850x850")
        addMemberWindow.configure(bg='#333333')

        def submit():
            today = date.today()
            #create new member report for current date
            if str(os.path.isfile(str(today.strftime("%B %d, %Y"))+" Daily Member Report.txt")) != "True":
                newMemberReport = open(str(today.strftime("%B %d, %Y"))+" Daily Member Report.txt", "a")
                newMemberReport.close()
                addDateandTitle = open(str(today.strftime("%B %d, %Y"))+" Daily Member Report.txt", "a")
                addDateandTitle.write("New Member Report for " + str(today.strftime("%B %d, %Y")))
                addDateandTitle.write('\n')
                addDateandTitle.write('\n')
                addDateandTitle.close()
            #create list of new member information and write to new member report file
            newMemberInfo = ["Member ID: " + new_member_id_entry.get(),"Member ID " + new_member_id_entry.get() + " Username: " + user_name_entry.get(),"Member ID " + new_member_id_entry.get() + " Password: " + user_password_entry.get(),"Member ID " + new_member_id_entry.get() + " First Name: " + first_name_entry.get(), "Member ID " + new_member_id_entry.get() + " Last Name: " + last_name_entry.get(),"Member ID " + new_member_id_entry.get() + " Street Address: " + street_address_entry.get(), "Member ID " + new_member_id_entry.get() + " City: " + city_entry.get(), "Member ID " + new_member_id_entry.get() + " State: " + state_entry.get(), "Member ID " + new_member_id_entry.get() + " ZIP Code: " + zip_code_entry.get(), "Member ID " + new_member_id_entry.get() + " Status: Active"]
            with open(str(today.strftime("%B %d, %Y"))+" Daily Member Report.txt", 'a') as f:
                for line in newMemberInfo:
                    f.write(line)
                    f.write('\n')
                f.write('\n')
            f.close()
            #Create/add to full member list
            if str(os.path.isfile("Chocan Member List.txt")) != "True":
                chocMemberList = open("Chocan Member List.txt", "a")
                chocMemberList.close()
                memberListTopLine = open("Chocan Member List.txt", "a")
                memberListTopLine.write("Chocan Member List")
                memberListTopLine.write('\n')
                memberListTopLine.write('\n')
                memberListTopLine.close()
            memberInfo = ["Member ID: " + new_member_id_entry.get(),"Member ID " + new_member_id_entry.get() + " Username: " + user_name_entry.get(),"Member ID " + new_member_id_entry.get() + " Password: " + user_password_entry.get(),"Member ID " + new_member_id_entry.get() + " First Name: " + first_name_entry.get(), "Member ID " + new_member_id_entry.get() + " Last Name: " + last_name_entry.get(),"Member ID " + new_member_id_entry.get() + " Street Address: " + street_address_entry.get(), "Member ID " + new_member_id_entry.get() + " City: " + city_entry.get(), "Member ID " + new_member_id_entry.get() + " State: " + state_entry.get(), "Member ID " + new_member_id_entry.get() + " ZIP Code: " + zip_code_entry.get(), "Member ID " + new_member_id_entry.get() + " Status: Active"]
            with open("Chocan Member List.txt", "a") as x:
                for line in memberInfo:
                    x.write(line)
                    x.write('\n')
                x.write('\n')
            x.close()
            messagebox.showinfo(title="New Member Added", message ="You have successfully added member #"+new_member_id_entry.get())        
        
        add_member_label = tkinter.Label(addMemberWindow, text="Add New Member", bg='#333333', fg='brown', font=("Arial, 30"))
        new_member_id_label = tkinter.Label(addMemberWindow, text="Enter New Member ID", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
        new_member_id_entry = tkinter.Entry(addMemberWindow, font=("Arial, 16"))
        user_name_label = tkinter.Label(addMemberWindow, text="Enter Member's User Name", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
        user_name_entry = tkinter.Entry(addMemberWindow, font=("Arial, 16"))
        user_password_label = tkinter.Label(addMemberWindow, text="Enter Member's Password", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
        user_password_entry = tkinter.Entry(addMemberWindow, font=("Arial, 16"))
        first_name_label = tkinter.Label(addMemberWindow, text="First Name", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
        first_name_entry = tkinter.Entry(addMemberWindow, font=("Arial, 16"))
        last_name_label = tkinter.Label(addMemberWindow, text="Last Name", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
        last_name_entry = tkinter.Entry(addMemberWindow, font=("Arial, 16"))
        street_address_label = tkinter.Label(addMemberWindow, text="Street Address", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
        street_address_entry = tkinter.Entry(addMemberWindow, font=("Arial, 16"))
        city_label = tkinter.Label(addMemberWindow, text="City", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
        city_entry = tkinter.Entry(addMemberWindow, font=("Arial, 16"))
        state_label = tkinter.Label(addMemberWindow, text="State", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
        state_entry = tkinter.Entry(addMemberWindow, font=("Arial, 16"))
        zip_code_label = tkinter.Label(addMemberWindow, text="ZIP Code", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
        zip_code_entry = tkinter.Entry(addMemberWindow, font=("Arial, 16")) 
        submit_button = tkinter.Button(addMemberWindow, text="Submit", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=submit)
        close_window_button = tkinter.Button(addMemberWindow, text="Close Window", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=addMemberWindow.destroy)

        add_member_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
        new_member_id_label.grid(row=1, column=0)
        new_member_id_entry.grid(row=1, column=1, pady=20)
        user_name_label.grid(row=2, column=0)
        user_name_entry.grid(row=2, column=1, pady=20)
        user_password_label.grid(row=3, column=0)
        user_password_entry.grid(row=3, column=1, pady=20)
        first_name_label.grid(row=4, column=0)
        first_name_entry.grid(row=4, column=1, pady=20)
        last_name_label.grid(row=5, column=0)
        last_name_entry.grid(row=5, column=1, pady=20)
        street_address_label.grid(row=6, column=0)
        street_address_entry.grid(row=6, column=1, pady=20)
        city_label.grid(row=7, column=0)
        city_entry.grid(row=7, column=1, pady=20)
        state_label.grid(row=8, column=0)
        state_entry.grid(row=8, column=1, pady=20)
        zip_code_label.grid(row=9, column=0)
        zip_code_entry.grid(row=9, column=1, pady=20)
        submit_button.grid(row=10, column=1, columnspan=2, pady=30)
        close_window_button.grid(row=10, column=4, columnspan=2, pady=30)

    def renewMember():
        renewMemberWindow = Toplevel()
        renewMemberWindow.title("Renew Member")
        renewMemberWindow.geometry("450x450")
        renewMemberWindow.configure(bg='#333333')


        def submit():
            #open file in read mode
            file = open("Chocan Member List.txt", "r")
            replaced_content = ""
            #looping through the file
            for line in file:
        
                #stripping line break
                line = line.strip()
                #replacing the texts
                new_line = line.replace( "Member ID " + member_ID_entry.get() + " Status: Inactive", "Member ID " + member_ID_entry.get() + " Status: Active")
                #concatenate the new string and add an end-line break
                replaced_content = replaced_content + new_line + "\n"
        
            #close the file
            file.close()
            #Open file in write mode
            write_file = open("Chocan Member List.txt", "w")
            #overwriting the old file contents with the new/replaced content
            write_file.write(replaced_content)
            #close the file
            write_file.close()

            messagebox.showinfo(title="Member Renewal", message ="You have successfully renewed member "+member_ID_entry.get())

        renew_member_label = tkinter.Label(renewMemberWindow, text="Renew Member", bg='#333333', fg='brown', font=("Arial, 30"))
        renew_member_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
        member_ID_label = tkinter.Label(renewMemberWindow, text="Member ID #", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
        member_ID_label.grid(row=1, column=0)
        member_ID_entry = tkinter.Entry(renewMemberWindow, font=("Arial, 16"))
        member_ID_entry.grid(row=2, column=0, pady=20)
        submit_button = tkinter.Button(renewMemberWindow, text="Submit", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=submit)
        submit_button.grid(row=3, column=0, columnspan=2, pady=30)
        close_window_button = tkinter.Button(renewMemberWindow, text="Close Window", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=renewMemberWindow.destroy)
        close_window_button.grid(row=4, column=4, columnspan=2, pady=30)

        
    def modifyMember():
        modifyMemberWindow = Toplevel()
        modifyMemberWindow.title("Modify Member")
        modifyMemberWindow.geometry("850x850")
        modifyMemberWindow.configure(bg='#333333')

        #Modify Username
        def modifyUsername():
            modifyUsername = Toplevel()
            modifyUsername.title("Change Username")
            modifyUsername.geometry("600x500")
            modifyUsername.configure(bg='#333333')

            def submit():
                #open file in read mode
                file = open("Chocan Member List.txt", "r")
                replaced_content = ""
                #looping through the file
                for line in file:
        
                    #stripping line break
                    line = line.strip()
                    #replacing the texts
                    new_username = line.replace( "Member ID " + member_ID_entry.get() + " Username: " + old_user_name_entry.get(), "Member ID " + member_ID_entry.get() + " Username: " + new_user_name_entry.get())
                    #concatenate the new string and add an end-line break
                    replaced_content = replaced_content + new_username + "\n"
        
                #close the file
                file.close()
                #Open file in write mode
                write_file = open("Chocan Member List.txt", "w")
                #overwriting the old file contents with the new/replaced content
                write_file.write(replaced_content)
                #close the file
                write_file.close()

                messagebox.showinfo(title="Modify Username", message ="You have successfully changed Member ID "+ member_ID_entry.get() +"'s username from " + old_user_name_entry.get() + " to " + new_user_name_entry.get())
            
            modify_username_label = tkinter.Label(modifyUsername, text="Modify Member", bg='#333333', fg='brown', font=("Arial, 30"))
            member_ID_label = tkinter.Label(modifyUsername, text="Member ID", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
            member_ID_entry = tkinter.Entry(modifyUsername, font=("Arial, 16"))
            old_user_name_label = tkinter.Label(modifyUsername, text="Old User Name", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
            old_user_name_entry = tkinter.Entry(modifyUsername, font=("Arial, 16"))
            new_user_name_label = tkinter.Label(modifyUsername, text="New User Name", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
            new_user_name_entry = tkinter.Entry(modifyUsername, font=("Arial, 16"))
            submit_button = tkinter.Button(modifyUsername, text="Submit", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=submit)
            close_window_button = tkinter.Button(modifyUsername, text="Close Window", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=modifyUsername.destroy)

            modify_username_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
            member_ID_label.grid(row=1, column=0)
            member_ID_entry.grid(row=1, column=1, pady=20)
            old_user_name_label.grid(row=2, column=0)
            old_user_name_entry.grid(row=2, column=1, pady=20)
            new_user_name_label.grid(row=3, column=0)
            new_user_name_entry.grid(row=3, column=1, pady=20)
            submit_button.grid(row=4, column=1, columnspan=2, pady=30)
            close_window_button.grid(row=4, column=4, columnspan=2, pady=30)

        #Modify Password
        def modifyPassword():
            modifyPassword = Toplevel()
            modifyPassword.title("Change Password")
            modifyPassword.geometry("600x500")
            modifyPassword.configure(bg='#333333')

            def submit():
                #open file in read mode
                file = open("Chocan Member List.txt", "r")
                replaced_content = ""
                #looping through the file
                for line in file:
        
                    #stripping line break
                    line = line.strip()
                    #replacing the texts
                    new_password = line.replace( "Member ID " + member_ID_entry.get() + " Password: " + old_password_entry.get(), "Member ID " + member_ID_entry.get() + " Password: " + new_password_entry.get())
                    #concatenate the new string and add an end-line break
                    replaced_content = replaced_content + new_password + "\n"
        
                #close the file
                file.close()
                #Open file in write mode
                write_file = open("Chocan Member List.txt", "w")
                #overwriting the old file contents with the new/replaced content
                write_file.write(replaced_content)
                #close the file
                write_file.close()

                messagebox.showinfo(title="Modify Password", message ="You have successfully changed Member ID "+member_ID_entry.get() +"'s password from " + old_password_entry.get() + " to " + new_password_entry.get())
            
            modify_password_label = tkinter.Label(modifyPassword, text="Modify Password", bg='#333333', fg='brown', font=("Arial, 30"))
            member_ID_label = tkinter.Label(modifyPassword, text="Member ID", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
            member_ID_entry = tkinter.Entry(modifyPassword, font=("Arial, 16"))
            old_password_label = tkinter.Label(modifyPassword, text="Old Password", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
            old_password_entry = tkinter.Entry(modifyPassword, font=("Arial, 16"))
            new_password_label = tkinter.Label(modifyPassword, text="New Password", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
            new_password_entry = tkinter.Entry(modifyPassword, font=("Arial, 16"))
            submit_button = tkinter.Button(modifyPassword, text="Submit", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=submit)
            close_window_button = tkinter.Button(modifyPassword, text="Close Window", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=modifyPassword.destroy)

            modify_password_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
            member_ID_label.grid(row=1, column=0)
            member_ID_entry.grid(row=1, column=1, pady=20)
            old_password_label.grid(row=2, column=0)
            old_password_entry.grid(row=2, column=1, pady=20)
            new_password_label.grid(row=3, column=0)
            new_password_entry.grid(row=3, column=1, pady=20)
            submit_button.grid(row=4, column=1, columnspan=2, pady=30)
            close_window_button.grid(row=4, column=4, columnspan=2, pady=30)

        #Modify First Name
        def modifyFirstName():
            modifyFirstName = Toplevel()
            modifyFirstName.title("Change First Name")
            modifyFirstName.geometry("600x500")
            modifyFirstName.configure(bg='#333333')

            def submit():
                #open file in read mode
                file = open("Chocan Member List.txt", "r")
                replaced_content = ""
                #looping through the file
                for line in file:
        
                    #stripping line break
                    line = line.strip()
                    #replacing the texts
                    new_password = line.replace( "Member ID " + member_ID_entry.get() + " First Name: " + old_first_name_entry.get(), "Member ID " + member_ID_entry.get() + " First Name: " + new_first_name_entry.get())
                    #concatenate the new string and add an end-line break
                    replaced_content = replaced_content + new_password + "\n"
        
                #close the file
                file.close()
                #Open file in write mode
                write_file = open("Chocan Member List.txt", "w")
                #overwriting the old file contents with the new/replaced content
                write_file.write(replaced_content)
                #close the file
                write_file.close()

                messagebox.showinfo(title="Modify First Name", message ="You have successfully changed Member ID "+member_ID_entry.get() +"'s First Name from " + old_first_name_entry.get() + " to " + new_first_name_entry.get())
            
            modify_first_name_label = tkinter.Label(modifyFirstName, text="Modify First Name", bg='#333333', fg='brown', font=("Arial, 30"))
            member_ID_label = tkinter.Label(modifyFirstName, text="Member ID", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
            member_ID_entry = tkinter.Entry(modifyFirstName, font=("Arial, 16"))
            old_first_name_label = tkinter.Label(modifyFirstName, text="Old First Name", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
            old_first_name_entry = tkinter.Entry(modifyFirstName, font=("Arial, 16"))
            new_first_name_label = tkinter.Label(modifyFirstName, text="New First Name", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
            new_first_name_entry = tkinter.Entry(modifyFirstName, font=("Arial, 16"))
            submit_button = tkinter.Button(modifyFirstName, text="Submit", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=submit)
            close_window_button = tkinter.Button(modifyFirstName, text="Close Window", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=modifyFirstName.destroy)

            modify_first_name_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
            member_ID_label.grid(row=1, column=0)
            member_ID_entry.grid(row=1, column=1, pady=20)
            old_first_name_label.grid(row=2, column=0)
            old_first_name_entry.grid(row=2, column=1, pady=20)
            new_first_name_label.grid(row=3, column=0)
            new_first_name_entry.grid(row=3, column=1, pady=20)
            submit_button.grid(row=4, column=1, columnspan=2, pady=30)
            close_window_button.grid(row=4, column=4, columnspan=2, pady=30)

        #Modify Last Name
        def modifyLastName():
            modifyLastName = Toplevel()
            modifyLastName.title("Change First Name")
            modifyLastName.geometry("600x500")
            modifyLastName.configure(bg='#333333')

            def submit():
                #open file in read mode
                file = open("Chocan Member List.txt", "r")
                replaced_content = ""
                #looping through the file
                for line in file:
        
                    #stripping line break
                    line = line.strip()
                    #replacing the texts
                    new_last_name = line.replace( "Member ID " + member_ID_entry.get() + " Last Name: " + old_last_name_entry.get(), "Member ID " + member_ID_entry.get() + " Last Name: " + new_last_name_entry.get())
                    #concatenate the new string and add an end-line break
                    replaced_content = replaced_content + new_last_name + "\n"
        
                #close the file
                file.close()
                #Open file in write mode
                write_file = open("Chocan Member List.txt", "w")
                #overwriting the old file contents with the new/replaced content
                write_file.write(replaced_content)
                #close the file
                write_file.close()

                messagebox.showinfo(title="Modify Last Name", message ="You have successfully changed Member ID "+member_ID_entry.get() +"'s Last Name from " + old_last_name_entry.get() + " to " + new_last_name_entry.get())
            
            modify_last_name_label = tkinter.Label(modifyLastName, text="Modify Last Name", bg='#333333', fg='brown', font=("Arial, 30"))
            member_ID_label = tkinter.Label(modifyLastName, text="Member ID", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
            member_ID_entry = tkinter.Entry(modifyLastName, font=("Arial, 16"))
            old_last_name_label = tkinter.Label(modifyLastName, text="Old Last Name", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
            old_last_name_entry = tkinter.Entry(modifyLastName, font=("Arial, 16"))
            new_last_name_label = tkinter.Label(modifyLastName, text="New Last Name", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
            new_last_name_entry = tkinter.Entry(modifyLastName, font=("Arial, 16"))
            submit_button = tkinter.Button(modifyLastName, text="Submit", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=submit)
            close_window_button = tkinter.Button(modifyLastName, text="Close Window", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=modifyLastName.destroy)

            modify_last_name_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
            member_ID_label.grid(row=1, column=0)
            member_ID_entry.grid(row=1, column=1, pady=20)
            old_last_name_label.grid(row=2, column=0)
            old_last_name_entry.grid(row=2, column=1, pady=20)
            new_last_name_label.grid(row=3, column=0)
            new_last_name_entry.grid(row=3, column=1, pady=20)
            submit_button.grid(row=4, column=1, columnspan=2, pady=30)
            close_window_button.grid(row=4, column=4, columnspan=2, pady=30)

        #Modify Street Address
        def modifyStreetAddress():
            modifyStreetAddress = Toplevel()
            modifyStreetAddress.title("Change Street Address")
            modifyStreetAddress.geometry("600x500")
            modifyStreetAddress.configure(bg='#333333')

            def submit():
                #open file in read mode
                file = open("Chocan Member List.txt", "r")
                replaced_content = ""
                #looping through the file
                for line in file:
            
                    #stripping line break
                    line = line.strip()
                    #replacing the texts
                    new_street_address = line.replace( "Member ID " + member_ID_entry.get() + " Street Address: " + old_street_address_entry.get(), "Member ID " + member_ID_entry.get() + " Street Address: " + new_street_address_entry.get())
                    #concatenate the new string and add an end-line break
                    replaced_content = replaced_content + new_street_address + "\n"
            
                #close the file
                file.close()
                #Open file in write mode
                write_file = open("Chocan Member List.txt", "w")
                #overwriting the old file contents with the new/replaced content
                write_file.write(replaced_content)
                #close the file
                write_file.close()

                messagebox.showinfo(title="Modify Street Address", message ="You have successfully changed Member ID "+member_ID_entry.get() +"'s Street Address from " + old_street_address_entry.get() + " to " + new_street_address_entry.get())
                
            modify_street_address_label = tkinter.Label(modifyStreetAddress, text="Modify Street Address", bg='#333333', fg='brown', font=("Arial, 30"))
            member_ID_label = tkinter.Label(modifyStreetAddress, text="Member ID", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
            member_ID_entry = tkinter.Entry(modifyStreetAddress, font=("Arial, 16"))
            old_street_address_label = tkinter.Label(modifyStreetAddress, text="Old Street Address", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
            old_street_address_entry = tkinter.Entry(modifyStreetAddress, font=("Arial, 16"))
            new_street_address_label = tkinter.Label(modifyStreetAddress, text="New Street Address", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
            new_street_address_entry = tkinter.Entry(modifyStreetAddress, font=("Arial, 16"))
            submit_button = tkinter.Button(modifyStreetAddress, text="Submit", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=submit)
            close_window_button = tkinter.Button(modifyStreetAddress, text="Close Window", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=modifyStreetAddress.destroy)

            modify_street_address_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
            member_ID_label.grid(row=1, column=0)
            member_ID_entry.grid(row=1, column=1, pady=20)
            old_street_address_label.grid(row=2, column=0)
            old_street_address_entry.grid(row=2, column=1, pady=20)
            new_street_address_label.grid(row=3, column=0)
            new_street_address_entry.grid(row=3, column=1, pady=20)
            submit_button.grid(row=4, column=1, columnspan=2, pady=30)
            close_window_button.grid(row=4, column=4, columnspan=2, pady=30)

        #Modify City
        def modifyCity():
            modifyCity = Toplevel()
            modifyCity.title("Change City")
            modifyCity.geometry("600x500")
            modifyCity.configure(bg='#333333')

            def submit():
                #open file in read mode
                file = open("Chocan Member List.txt", "r")
                replaced_content = ""
                #looping through the file
                for line in file:
            
                    #stripping line break
                    line = line.strip()
                    #replacing the texts
                    new_city = line.replace( "Member ID " + member_ID_entry.get() + " City: " + old_city_entry.get(), "Member ID " + member_ID_entry.get() + " City: " + new_city_entry.get())
                    #concatenate the new string and add an end-line break
                    replaced_content = replaced_content + new_city + "\n"
            
                #close the file
                file.close()
                #Open file in write mode
                write_file = open("Chocan Member List.txt", "w")
                #overwriting the old file contents with the new/replaced content
                write_file.write(replaced_content)
                #close the file
                write_file.close()

                messagebox.showinfo(title="Modify City", message ="You have successfully changed Member ID "+member_ID_entry.get() +"'s City from " + old_city_entry.get() + " to " + new_city_entry.get())
                
            modify_city_label = tkinter.Label(modifyCity, text="Modify City", bg='#333333', fg='brown', font=("Arial, 30"))
            member_ID_label = tkinter.Label(modifyCity, text="Member ID", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
            member_ID_entry = tkinter.Entry(modifyCity, font=("Arial, 16"))
            old_city_label = tkinter.Label(modifyCity, text="Old City", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
            old_city_entry = tkinter.Entry(modifyCity, font=("Arial, 16"))
            new_city_label = tkinter.Label(modifyCity, text="New City", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
            new_city_entry = tkinter.Entry(modifyCity, font=("Arial, 16"))
            submit_button = tkinter.Button(modifyCity, text="Submit", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=submit)
            close_window_button = tkinter.Button(modifyCity, text="Close Window", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=modifyCity.destroy)

            modify_city_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
            member_ID_label.grid(row=1, column=0)
            member_ID_entry.grid(row=1, column=1, pady=20)
            old_city_label.grid(row=2, column=0)
            old_city_entry.grid(row=2, column=1, pady=20)
            new_city_label.grid(row=3, column=0)
            new_city_entry.grid(row=3, column=1, pady=20)
            submit_button.grid(row=4, column=1, columnspan=2, pady=30)
            close_window_button.grid(row=4, column=4, columnspan=2, pady=30)

        #Modify State
        def modifyState():
            modifyState = Toplevel()
            modifyState.title("Change City")
            modifyState.geometry("600x500")
            modifyState.configure(bg='#333333')

            def submit():
                #open file in read mode
                file = open("Chocan Member List.txt", "r")
                replaced_content = ""
                #looping through the file
                for line in file:
            
                    #stripping line break
                    line = line.strip()
                    #replacing the texts
                    new_state = line.replace( "Member ID " + member_ID_entry.get() + " State: " + old_state_entry.get(), "Member ID " + member_ID_entry.get() + " State: " + new_state_entry.get())
                    #concatenate the new string and add an end-line break
                    replaced_content = replaced_content + new_state + "\n"
            
                #close the file
                file.close()
                #Open file in write mode
                write_file = open("Chocan Member List.txt", "w")
                #overwriting the old file contents with the new/replaced content
                write_file.write(replaced_content)
                #close the file
                write_file.close()

                messagebox.showinfo(title="Modify State", message ="You have successfully changed Member ID "+member_ID_entry.get() +"'s State from " + old_state_entry.get() + " to " + new_state_entry.get())
                
            modify_state_label = tkinter.Label(modifyState, text="Modify State", bg='#333333', fg='brown', font=("Arial, 30"))
            member_ID_label = tkinter.Label(modifyState, text="Member ID", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
            member_ID_entry = tkinter.Entry(modifyState, font=("Arial, 16"))
            old_state_label = tkinter.Label(modifyState, text="Old State", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
            old_state_entry = tkinter.Entry(modifyState, font=("Arial, 16"))
            new_state_label = tkinter.Label(modifyState, text="New State", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
            new_state_entry = tkinter.Entry(modifyState, font=("Arial, 16"))
            submit_button = tkinter.Button(modifyState, text="Submit", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=submit)
            close_window_button = tkinter.Button(modifyState, text="Close Window", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=modifyState.destroy)

            modify_state_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
            member_ID_label.grid(row=1, column=0)
            member_ID_entry.grid(row=1, column=1, pady=20)
            old_state_label.grid(row=2, column=0)
            old_state_entry.grid(row=2, column=1, pady=20)
            new_state_label.grid(row=3, column=0)
            new_state_entry.grid(row=3, column=1, pady=20)
            submit_button.grid(row=4, column=1, columnspan=2, pady=30)
            close_window_button.grid(row=4, column=4, columnspan=2, pady=30)

        #Modify ZIP Code
        def modifyZipCode():
            modifyZipCode = Toplevel()
            modifyZipCode.title("Change City")
            modifyZipCode.geometry("600x500")
            modifyZipCode.configure(bg='#333333')

            def submit():
                #open file in read mode
                file = open("Chocan Member List.txt", "r")
                replaced_content = ""
                #looping through the file
                for line in file:
            
                    #stripping line break
                    line = line.strip()
                    #replacing the texts
                    new_zip_code = line.replace( "Member ID " + member_ID_entry.get() + " ZIP Code: " + old_zip_code_entry.get(), "Member ID " + member_ID_entry.get() + " ZIP Code: " + new_zip_code_entry.get())
                    #concatenate the new string and add an end-line break
                    replaced_content = replaced_content + new_zip_code + "\n"
            
                #close the file
                file.close()
                #Open file in write mode
                write_file = open("Chocan Member List.txt", "w")
                #overwriting the old file contents with the new/replaced content
                write_file.write(replaced_content)
                #close the file
                write_file.close()

                messagebox.showinfo(title="Modify ZIP Code", message ="You have successfully changed Member ID "+member_ID_entry.get() +"'s ZIP Code from " + old_zip_code_entry.get() + " to " + new_zip_code_entry.get())
                
            modify_zip_code_label = tkinter.Label(modifyZipCode, text="Modify ZIP Code", bg='#333333', fg='brown', font=("Arial, 30"))
            member_ID_label = tkinter.Label(modifyZipCode, text="Member ID", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
            member_ID_entry = tkinter.Entry(modifyZipCode, font=("Arial, 16"))
            old_zip_code_label = tkinter.Label(modifyZipCode, text="Old ZIP Code", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
            old_zip_code_entry = tkinter.Entry(modifyZipCode, font=("Arial, 16"))
            new_zip_code_label = tkinter.Label(modifyZipCode, text="New ZIP Code", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
            new_zip_code_entry = tkinter.Entry(modifyZipCode, font=("Arial, 16"))
            submit_button = tkinter.Button(modifyZipCode, text="Submit", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=submit)
            close_window_button = tkinter.Button(modifyZipCode, text="Close Window", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=modifyZipCode.destroy)

            modify_zip_code_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
            member_ID_label.grid(row=1, column=0)
            member_ID_entry.grid(row=1, column=1, pady=20)
            old_zip_code_label.grid(row=2, column=0)
            old_zip_code_entry.grid(row=2, column=1, pady=20)
            new_zip_code_label.grid(row=3, column=0)
            new_zip_code_entry.grid(row=3, column=1, pady=20)
            submit_button.grid(row=4, column=1, columnspan=2, pady=30)
            close_window_button.grid(row=4, column=4, columnspan=2, pady=30)
        
        #Widgets for Modify Member Window
        modify_member_label = tkinter.Label(modifyMemberWindow, text="Modify Member", bg='#333333', fg='brown', font=("Arial, 30"))
        modify_username_button = tkinter.Button(modifyMemberWindow, text="Modify Member Username", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=modifyUsername)
        modify_password_button = tkinter.Button(modifyMemberWindow, text="Modify Member Password", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=modifyPassword)
        modify_first_name_button = tkinter.Button(modifyMemberWindow, text="Modify Member First Name", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=modifyFirstName)
        modify_last_name_button = tkinter.Button(modifyMemberWindow, text="Modify Member Last Name", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=modifyLastName)
        modify_street_address_button = tkinter.Button(modifyMemberWindow, text="Modify Member Street Address", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=modifyStreetAddress)
        modify_city_button = tkinter.Button(modifyMemberWindow, text="Modify Member City", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=modifyCity)
        modify_state_button = tkinter.Button(modifyMemberWindow, text="Modify Member State", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=modifyState)
        modify_ZIP_code_button = tkinter.Button(modifyMemberWindow, text="Modify Member ZIP Code", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=modifyZipCode)
        close_window_button = tkinter.Button(modifyMemberWindow, text="Close Window", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=modifyMemberWindow.destroy)

        modify_member_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
        modify_username_button.grid(row=1, column=0, columnspan=1, pady=20)
        modify_password_button.grid(row=2, column=0, columnspan=1, pady=20)
        modify_first_name_button.grid(row=3, column=0, columnspan=1, pady=20)
        modify_last_name_button.grid(row=4, column=0, columnspan=1, pady=20)
        modify_street_address_button.grid(row=5, column=0, columnspan=1, pady=20)
        modify_city_button.grid(row=6, column=0, columnspan=1, pady=20)
        modify_state_button.grid(row=7, column=0, columnspan=1, pady=20)
        modify_ZIP_code_button.grid(row=8, column=0, columnspan=1)
        close_window_button.grid(row=8, column=4, columnspan=2, pady=30)
        
    def removeMember():
        removeMemberWindow = Toplevel()
        removeMemberWindow.title("Remove Member")
        removeMemberWindow.geometry("500x500")
        removeMemberWindow.configure(bg='#333333')

        def submit():
            #open file in read mode
            file = open("Chocan Member List.txt", "r")
            replaced_content = ""
            #looping through the file
            for line in file:
        
                #stripping line break
                line = line.strip()
                #replacing the texts
                new_line = line.replace("Member ID " + member_ID_entry.get() + " Status: Active", "Member ID " + member_ID_entry.get() + " Status: Inactive")
                #concatenate the new string and add an end-line break
                replaced_content = replaced_content + new_line + "\n"
        
            #close the file
            file.close()
            #Open file in write mode
            write_file = open("Chocan Member List.txt", "w")
            #overwriting the old file contents with the new/replaced content
            write_file.write(replaced_content)
            #close the file
            write_file.close()

            messagebox.showinfo(title="Member Removed", message ="Member ID #" + member_ID_entry.get() + " has been removed.")

        remove_member_label = tkinter.Label(removeMemberWindow, text="Remove Member", bg='#333333', fg='brown', font=("Arial, 30"))
        remove_member_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
        member_ID_label = tkinter.Label(removeMemberWindow, text="Member ID #", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
        member_ID_label.grid(row=1, column=0)
        member_ID_entry = tkinter.Entry(removeMemberWindow, font=("Arial, 16"))
        member_ID_entry.grid(row=2, column=0, pady=20)
        submit_button = tkinter.Button(removeMemberWindow, text="Submit", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=submit)
        submit_button.grid(row=3, column=0, columnspan=2, pady=30)
        close_window_button = tkinter.Button(removeMemberWindow, text="Close Window", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=removeMemberWindow.destroy)
        close_window_button.grid(row=6, column=4, columnspan=2, pady=30)

    # Create widgets for manageMemberWindow
    add_new_member = tkinter.Button(manageMemberWindow, text="Add Member", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=addMember)
    renew_existing = tkinter.Button(manageMemberWindow, text="Renew Member", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=renewMember)  
    modify_member = tkinter.Button(manageMemberWindow, text="Modify Member", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=modifyMember)
    remove_member = tkinter.Button(manageMemberWindow, text="Remove Member", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=removeMember)

    # Place widgets for manageMemberWindow
    add_new_member.grid(row=2, column=0, columnspan=2, pady=30)
    renew_existing.grid(row=3, column=0, columnspan=2, pady=30)
    modify_member.grid(row=4, column=0, columnspan=2, pady=30)
    remove_member.grid(row=5, column=0, columnspan=2, pady=30)

