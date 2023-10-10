from tkinter import *
import tkinter
from PIL import Image, ImageTk
from tkinter import messagebox
from datetime import date
import os.path

def manageProvider():

    manageProviderWindow = Toplevel()
    manageProviderWindow.title("Manage Provider")
    manageProviderWindow.geometry("800x800")
    manageProviderWindow.configure(bg='#333333')

    manage_provider_label = tkinter.Label(manageProviderWindow, text="Manage Provider", bg='#333333', fg='brown', font=("Arial, 30"))
    manage_provider_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
    close_window_button = tkinter.Button(manageProviderWindow, text="Close Window", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=manageProviderWindow.destroy)
    close_window_button.grid(row=6, column=4, columnspan=2, pady=30)


    def addProvider():
        addProviderWindow = Toplevel()
        addProviderWindow.title("Add Provider")
        addProviderWindow.geometry("850x850")
        addProviderWindow.configure(bg='#333333')

        def submit():
            today = date.today()
            #create new Provider report for current date
            if str(os.path.isfile(str(today.strftime("%B %d, %Y"))+" Daily Provider Report.txt")) != "True":
                newProviderReport = open(str(today.strftime("%B %d, %Y"))+" Daily Provider Report.txt", "a")
                newProviderReport.close()
                addDateandTitle = open(str(today.strftime("%B %d, %Y"))+" Daily Provider Report.txt", "a")
                addDateandTitle.write("New Provider Report for " + str(today.strftime("%B %d, %Y")))
                addDateandTitle.write('\n')
                addDateandTitle.write('\n')
                addDateandTitle.close()
            #create list of new Provider information and write to new provider report file
            newProviderInfo = ["Provider ID: " + new_provider_id_entry.get(),"Provider ID " + new_provider_id_entry.get() + " Username: " + user_name_entry.get(),"Provider ID " + new_provider_id_entry.get() + " Password: " + user_password_entry.get(),"Provider ID " + new_provider_id_entry.get() + " First Name: " + first_name_entry.get(), "Provider ID " + new_provider_id_entry.get() + " Last Name: " + last_name_entry.get(),"Provider ID " + new_provider_id_entry.get() + " Street Address: " + street_address_entry.get(), "Provider ID " + new_provider_id_entry.get() + " City: " + city_entry.get(), "Provider ID " + new_provider_id_entry.get() + " State: " + state_entry.get(), "Provider ID " + new_provider_id_entry.get() + " ZIP Code: " + zip_code_entry.get(), "Provider ID " + new_provider_id_entry.get() + " Status: Active"]
            with open(str(today.strftime("%B %d, %Y"))+" Daily Provider Report.txt", 'a') as f:
                for line in newProviderInfo:
                    f.write(line)
                    f.write('\n')
                f.write('\n')
            f.close()
            #Create/add to full Provider list
            if str(os.path.isfile("Chocan Provider List.txt")) != "True":
                chocProviderList = open("Chocan Provider List.txt", "a")
                chocProviderList.close()
                providerListTopLine = open("Chocan Provider List.txt", "a")
                providerListTopLine.write("Chocan Provider List")
                providerListTopLine.write('\n')
                providerListTopLine.write('\n')
                providerListTopLine.close()
            providerInfo = ["Provider ID: " + new_provider_id_entry.get(),"Provider ID " + new_provider_id_entry.get() + " Username: " + user_name_entry.get(),"Provider ID " + new_provider_id_entry.get() + " Password: " + user_password_entry.get(),"Provider ID " + new_provider_id_entry.get() + " First Name: " + first_name_entry.get(), "Provider ID " + new_provider_id_entry.get() + " Last Name: " + last_name_entry.get(),"Provider ID " + new_provider_id_entry.get() + " Street Address: " + street_address_entry.get(), "Provider ID " + new_provider_id_entry.get() + " City: " + city_entry.get(), "Provider ID " + new_provider_id_entry.get() + " State: " + state_entry.get(), "Provider ID " + new_provider_id_entry.get() + " ZIP Code: " + zip_code_entry.get(), "Provider ID " + new_provider_id_entry.get() + " Status: Active"]
            with open("Chocan Provider List.txt", "a") as x:
                for line in providerInfo:
                    x.write(line)
                    x.write('\n')
                x.write('\n')
            x.close()
            messagebox.showinfo(title="New Provider Added", message ="You have successfully added provider #"+new_provider_id_entry.get())        
        
        add_provider_label = tkinter.Label(addProviderWindow, text="Add New Provider", bg='#333333', fg='brown', font=("Arial, 30"))
        new_provider_id_label = tkinter.Label(addProviderWindow, text="Enter New Provider ID", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
        new_provider_id_entry = tkinter.Entry(addProviderWindow, font=("Arial, 16"))
        user_name_label = tkinter.Label(addProviderWindow, text="Enter Provider's User Name", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
        user_name_entry = tkinter.Entry(addProviderWindow, font=("Arial, 16"))
        user_password_label = tkinter.Label(addProviderWindow, text="Enter Provider's Password", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
        user_password_entry = tkinter.Entry(addProviderWindow, font=("Arial, 16"))
        first_name_label = tkinter.Label(addProviderWindow, text="First Name", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
        first_name_entry = tkinter.Entry(addProviderWindow, font=("Arial, 16"))
        last_name_label = tkinter.Label(addProviderWindow, text="Last Name", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
        last_name_entry = tkinter.Entry(addProviderWindow, font=("Arial, 16"))
        street_address_label = tkinter.Label(addProviderWindow, text="Street Address", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
        street_address_entry = tkinter.Entry(addProviderWindow, font=("Arial, 16"))
        city_label = tkinter.Label(addProviderWindow, text="City", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
        city_entry = tkinter.Entry(addProviderWindow, font=("Arial, 16"))
        state_label = tkinter.Label(addProviderWindow, text="State", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
        state_entry = tkinter.Entry(addProviderWindow, font=("Arial, 16"))
        zip_code_label = tkinter.Label(addProviderWindow, text="ZIP Code", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
        zip_code_entry = tkinter.Entry(addProviderWindow, font=("Arial, 16")) 
        submit_button = tkinter.Button(addProviderWindow, text="Submit", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=submit)
        close_window_button = tkinter.Button(addProviderWindow, text="Close Window", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=addProviderWindow.destroy)

        add_provider_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
        new_provider_id_label.grid(row=1, column=0)
        new_provider_id_entry.grid(row=1, column=1, pady=20)
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

    def renewProvider():
        renewProviderWindow = Toplevel()
        renewProviderWindow.title("Renew Provider")
        renewProviderWindow.geometry("450x450")
        renewProviderWindow.configure(bg='#333333')

        def submit():
            #open file in read mode
            file = open("Chocan Provider List.txt", "r")
            replaced_content = ""
            #looping through the file
            for line in file:
        
                #stripping line break
                line = line.strip()
                #replacing the texts
                new_line = line.replace( "Provider ID " + provider_ID_entry.get() + " Status: Inactive", "Provider ID " + provider_ID_entry.get() + " Status: Active")
                #concatenate the new string and add an end-line break
                replaced_content = replaced_content + new_line + "\n"
        
            #close the file
            file.close()
            #Open file in write mode
            write_file = open("Chocan Provider List.txt", "w")
            #overwriting the old file contents with the new/replaced content
            write_file.write(replaced_content)
            #close the file
            write_file.close()

            messagebox.showinfo(title="Provider Renewal", message ="You have successfully renewed provider "+ provider_ID_entry.get())

        renew_provider_label = tkinter.Label(renewProviderWindow, text="Renew Provider", bg='#333333', fg='brown', font=("Arial, 30"))
        renew_provider_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
        provider_ID_label = tkinter.Label(renewProviderWindow, text="Provider ID #", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
        provider_ID_label.grid(row=1, column=0)
        provider_ID_entry = tkinter.Entry(renewProviderWindow, font=("Arial, 16"))
        provider_ID_entry.grid(row=2, column=0, pady=20)
        submit_button = tkinter.Button(renewProviderWindow, text="Submit", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=submit)
        submit_button.grid(row=3, column=0, columnspan=2, pady=30)
        close_window_button = tkinter.Button(renewProviderWindow, text="Close Window", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=renewProviderWindow.destroy)
        close_window_button.grid(row=6, column=4, columnspan=2, pady=30)

        
    def modifyProvider():
        modifyProviderWindow = Toplevel()
        modifyProviderWindow.title("Modify Provider")
        modifyProviderWindow.geometry("850x850")
        modifyProviderWindow.configure(bg='#333333')

        #Modify Username
        def modifyUsername():
            modifyUsername = Toplevel()
            modifyUsername.title("Change Username")
            modifyUsername.geometry("600x500")
            modifyUsername.configure(bg='#333333')

            def submit():
                #open file in read mode
                file = open("Chocan Provider List.txt", "r")
                replaced_content = ""
                #looping through the file
                for line in file:
        
                    #stripping line break
                    line = line.strip()
                    #replacing the texts
                    new_username = line.replace( "Provider ID " + provider_ID_entry.get() + " Username: " + old_user_name_entry.get(), "Provider ID " + provider_ID_entry.get() + " Username: " + new_user_name_entry.get())
                    #concatenate the new string and add an end-line break
                    replaced_content = replaced_content + new_username + "\n"
        
                #close the file
                file.close()
                #Open file in write mode
                write_file = open("Chocan Provider List.txt", "w")
                #overwriting the old file contents with the new/replaced content
                write_file.write(replaced_content)
                #close the file
                write_file.close()

                messagebox.showinfo(title="Modify Username", message ="You have successfully changed Provider ID "+ provider_ID_entry.get() +"'s username from " + old_user_name_entry.get() + " to " + new_user_name_entry.get())
            
            modify_username_label = tkinter.Label(modifyUsername, text="Modify Provider", bg='#333333', fg='brown', font=("Arial, 30"))
            provider_ID_label = tkinter.Label(modifyUsername, text="Provider ID", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
            provider_ID_entry = tkinter.Entry(modifyUsername, font=("Arial, 16"))
            old_user_name_label = tkinter.Label(modifyUsername, text="Old User Name", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
            old_user_name_entry = tkinter.Entry(modifyUsername, font=("Arial, 16"))
            new_user_name_label = tkinter.Label(modifyUsername, text="New User Name", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
            new_user_name_entry = tkinter.Entry(modifyUsername, font=("Arial, 16"))
            submit_button = tkinter.Button(modifyUsername, text="Submit", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=submit)
            close_window_button = tkinter.Button(modifyUsername, text="Close Window", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=modifyUsername.destroy)

            modify_username_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
            provider_ID_label.grid(row=1, column=0)
            provider_ID_entry.grid(row=1, column=1, pady=20)
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
                file = open("Chocan Provider List.txt", "r")
                replaced_content = ""
                #looping through the file
                for line in file:
        
                    #stripping line break
                    line = line.strip()
                    #replacing the texts
                    new_password = line.replace( "Provider ID " + provider_ID_entry.get() + " Password: " + old_password_entry.get(), "Provider ID " + provider_ID_entry.get() + " Password: " + new_password_entry.get())
                    #concatenate the new string and add an end-line break
                    replaced_content = replaced_content + new_password + "\n"
        
                #close the file
                file.close()
                #Open file in write mode
                write_file = open("Chocan Provider List.txt", "w")
                #overwriting the old file contents with the new/replaced content
                write_file.write(replaced_content)
                #close the file
                write_file.close()

                messagebox.showinfo(title="Modify Password", message ="You have successfully changed Provider ID "+provider_ID_entry.get() +"'s password from " + old_password_entry.get() + " to " + new_password_entry.get())
            
            modify_password_label = tkinter.Label(modifyPassword, text="Modify Password", bg='#333333', fg='brown', font=("Arial, 30"))
            provider_ID_label = tkinter.Label(modifyPassword, text="Provider ID", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
            provider_ID_entry = tkinter.Entry(modifyPassword, font=("Arial, 16"))
            old_password_label = tkinter.Label(modifyPassword, text="Old Password", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
            old_password_entry = tkinter.Entry(modifyPassword, font=("Arial, 16"))
            new_password_label = tkinter.Label(modifyPassword, text="New Password", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
            new_password_entry = tkinter.Entry(modifyPassword, font=("Arial, 16"))
            submit_button = tkinter.Button(modifyPassword, text="Submit", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=submit)
            close_window_button = tkinter.Button(modifyPassword, text="Close Window", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=modifyPassword.destroy)

            modify_password_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
            provider_ID_label.grid(row=1, column=0)
            provider_ID_entry.grid(row=1, column=1, pady=20)
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
                file = open("Chocan Provider List.txt", "r")
                replaced_content = ""
                #looping through the file
                for line in file:
        
                    #stripping line break
                    line = line.strip()
                    #replacing the texts
                    new_password = line.replace( "Provider ID " + provider_ID_entry.get() + " First Name: " + old_first_name_entry.get(), "Provider ID " + provider_ID_entry.get() + " First Name: " + new_first_name_entry.get())
                    #concatenate the new string and add an end-line break
                    replaced_content = replaced_content + new_password + "\n"
        
                #close the file
                file.close()
                #Open file in write mode
                write_file = open("Chocan Provider List.txt", "w")
                #overwriting the old file contents with the new/replaced content
                write_file.write(replaced_content)
                #close the file
                write_file.close()

                messagebox.showinfo(title="Modify First Name", message ="You have successfully changed Provider ID "+provider_ID_entry.get() +"'s First Name from " + old_first_name_entry.get() + " to " + new_first_name_entry.get())
            
            modify_first_name_label = tkinter.Label(modifyFirstName, text="Modify First Name", bg='#333333', fg='brown', font=("Arial, 30"))
            provider_ID_label = tkinter.Label(modifyFirstName, text="Provider ID", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
            provider_ID_entry = tkinter.Entry(modifyFirstName, font=("Arial, 16"))
            old_first_name_label = tkinter.Label(modifyFirstName, text="Old First Name", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
            old_first_name_entry = tkinter.Entry(modifyFirstName, font=("Arial, 16"))
            new_first_name_label = tkinter.Label(modifyFirstName, text="New First Name", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
            new_first_name_entry = tkinter.Entry(modifyFirstName, font=("Arial, 16"))
            submit_button = tkinter.Button(modifyFirstName, text="Submit", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=submit)
            close_window_button = tkinter.Button(modifyFirstName, text="Close Window", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=modifyFirstName.destroy)

            modify_first_name_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
            provider_ID_label.grid(row=1, column=0)
            provider_ID_entry.grid(row=1, column=1, pady=20)
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
                file = open("Chocan Provider List.txt", "r")
                replaced_content = ""
                #looping through the file
                for line in file:
        
                    #stripping line break
                    line = line.strip()
                    #replacing the texts
                    new_last_name = line.replace( "Provider ID " + provider_ID_entry.get() + " Last Name: " + old_last_name_entry.get(), "Provider ID " + provider_ID_entry.get() + " Last Name: " + new_last_name_entry.get())
                    #concatenate the new string and add an end-line break
                    replaced_content = replaced_content + new_last_name + "\n"
        
                #close the file
                file.close()
                #Open file in write mode
                write_file = open("Chocan Provider List.txt", "w")
                #overwriting the old file contents with the new/replaced content
                write_file.write(replaced_content)
                #close the file
                write_file.close()

                messagebox.showinfo(title="Modify Last Name", message ="You have successfully changed Provider ID "+provider_ID_entry.get() +"'s Last Name from " + old_last_name_entry.get() + " to " + new_last_name_entry.get())
            
            modify_last_name_label = tkinter.Label(modifyLastName, text="Modify Last Name", bg='#333333', fg='brown', font=("Arial, 30"))
            provider_ID_label = tkinter.Label(modifyLastName, text="Provider ID", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
            provider_ID_entry = tkinter.Entry(modifyLastName, font=("Arial, 16"))
            old_last_name_label = tkinter.Label(modifyLastName, text="Old Last Name", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
            old_last_name_entry = tkinter.Entry(modifyLastName, font=("Arial, 16"))
            new_last_name_label = tkinter.Label(modifyLastName, text="New Last Name", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
            new_last_name_entry = tkinter.Entry(modifyLastName, font=("Arial, 16"))
            submit_button = tkinter.Button(modifyLastName, text="Submit", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=submit)
            close_window_button = tkinter.Button(modifyLastName, text="Close Window", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=modifyLastName.destroy)

            modify_last_name_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
            provider_ID_label.grid(row=1, column=0)
            provider_ID_entry.grid(row=1, column=1, pady=20)
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
                file = open("Chocan Provider List.txt", "r")
                replaced_content = ""
                #looping through the file
                for line in file:
            
                    #stripping line break
                    line = line.strip()
                    #replacing the texts
                    new_street_address = line.replace( "Provider ID " + provider_ID_entry.get() + " Street Address: " + old_street_address_entry.get(), "Provider ID " + provider_ID_entry.get() + " Street Address: " + new_street_address_entry.get())
                    #concatenate the new string and add an end-line break
                    replaced_content = replaced_content + new_street_address + "\n"
            
                #close the file
                file.close()
                #Open file in write mode
                write_file = open("Chocan Provider List.txt", "w")
                #overwriting the old file contents with the new/replaced content
                write_file.write(replaced_content)
                #close the file
                write_file.close()

                messagebox.showinfo(title="Modify Street Address", message ="You have successfully changed Provider ID "+provider_ID_entry.get() +"'s Street Address from " + old_street_address_entry.get() + " to " + new_street_address_entry.get())
                
            modify_street_address_label = tkinter.Label(modifyStreetAddress, text="Modify Street Address", bg='#333333', fg='brown', font=("Arial, 30"))
            provider_ID_label = tkinter.Label(modifyStreetAddress, text="Provider ID", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
            provider_ID_entry = tkinter.Entry(modifyStreetAddress, font=("Arial, 16"))
            old_street_address_label = tkinter.Label(modifyStreetAddress, text="Old Street Address", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
            old_street_address_entry = tkinter.Entry(modifyStreetAddress, font=("Arial, 16"))
            new_street_address_label = tkinter.Label(modifyStreetAddress, text="New Street Address", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
            new_street_address_entry = tkinter.Entry(modifyStreetAddress, font=("Arial, 16"))
            submit_button = tkinter.Button(modifyStreetAddress, text="Submit", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=submit)
            close_window_button = tkinter.Button(modifyStreetAddress, text="Close Window", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=modifyStreetAddress.destroy)

            modify_street_address_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
            provider_ID_label.grid(row=1, column=0)
            provider_ID_entry.grid(row=1, column=1, pady=20)
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
                file = open("Chocan Provider List.txt", "r")
                replaced_content = ""
                #looping through the file
                for line in file:
            
                    #stripping line break
                    line = line.strip()
                    #replacing the texts
                    new_city = line.replace( "Provider ID " + provider_ID_entry.get() + " City: " + old_city_entry.get(), "Provider ID " + provider_ID_entry.get() + " City: " + new_city_entry.get())
                    #concatenate the new string and add an end-line break
                    replaced_content = replaced_content + new_city + "\n"
            
                #close the file
                file.close()
                #Open file in write mode
                write_file = open("Chocan Provider List.txt", "w")
                #overwriting the old file contents with the new/replaced content
                write_file.write(replaced_content)
                #close the file
                write_file.close()

                messagebox.showinfo(title="Modify City", message ="You have successfully changed Provider ID "+provider_ID_entry.get() +"'s City from " + old_city_entry.get() + " to " + new_city_entry.get())
                
            modify_city_label = tkinter.Label(modifyCity, text="Modify City", bg='#333333', fg='brown', font=("Arial, 30"))
            provider_ID_label = tkinter.Label(modifyCity, text="Provider ID", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
            provider_ID_entry = tkinter.Entry(modifyCity, font=("Arial, 16"))
            old_city_label = tkinter.Label(modifyCity, text="Old City", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
            old_city_entry = tkinter.Entry(modifyCity, font=("Arial, 16"))
            new_city_label = tkinter.Label(modifyCity, text="New City", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
            new_city_entry = tkinter.Entry(modifyCity, font=("Arial, 16"))
            submit_button = tkinter.Button(modifyCity, text="Submit", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=submit)
            close_window_button = tkinter.Button(modifyCity, text="Close Window", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=modifyCity.destroy)

            modify_city_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
            provider_ID_label.grid(row=1, column=0)
            provider_ID_entry.grid(row=1, column=1, pady=20)
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
                file = open("Chocan Provider List.txt", "r")
                replaced_content = ""
                #looping through the file
                for line in file:
            
                    #stripping line break
                    line = line.strip()
                    #replacing the texts
                    new_state = line.replace( "Provider ID " + provider_ID_entry.get() + " State: " + old_state_entry.get(), "Provider ID " + provider_ID_entry.get() + " State: " + new_state_entry.get())
                    #concatenate the new string and add an end-line break
                    replaced_content = replaced_content + new_state + "\n"
            
                #close the file
                file.close()
                #Open file in write mode
                write_file = open("Chocan Provider List.txt", "w")
                #overwriting the old file contents with the new/replaced content
                write_file.write(replaced_content)
                #close the file
                write_file.close()

                messagebox.showinfo(title="Modify State", message ="You have successfully changed Provider ID "+provider_ID_entry.get() +"'s State from " + old_state_entry.get() + " to " + new_state_entry.get())
                
            modify_state_label = tkinter.Label(modifyState, text="Modify State", bg='#333333', fg='brown', font=("Arial, 30"))
            provider_ID_label = tkinter.Label(modifyState, text="Provider ID", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
            provider_ID_entry = tkinter.Entry(modifyState, font=("Arial, 16"))
            old_state_label = tkinter.Label(modifyState, text="Old State", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
            old_state_entry = tkinter.Entry(modifyState, font=("Arial, 16"))
            new_state_label = tkinter.Label(modifyState, text="New State", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
            new_state_entry = tkinter.Entry(modifyState, font=("Arial, 16"))
            submit_button = tkinter.Button(modifyState, text="Submit", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=submit)
            close_window_button = tkinter.Button(modifyState, text="Close Window", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=modifyState.destroy)

            modify_state_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
            provider_ID_label.grid(row=1, column=0)
            provider_ID_entry.grid(row=1, column=1, pady=20)
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
                file = open("Chocan Provider List.txt", "r")
                replaced_content = ""
                #looping through the file
                for line in file:
            
                    #stripping line break
                    line = line.strip()
                    #replacing the texts
                    new_zip_code = line.replace( "Provider ID " + provider_ID_entry.get() + " ZIP Code: " + old_zip_code_entry.get(), "Provider ID " + provider_ID_entry.get() + " ZIP Code: " + new_zip_code_entry.get())
                    #concatenate the new string and add an end-line break
                    replaced_content = replaced_content + new_zip_code + "\n"
            
                #close the file
                file.close()
                #Open file in write mode
                write_file = open("Chocan Provider List.txt", "w")
                #overwriting the old file contents with the new/replaced content
                write_file.write(replaced_content)
                #close the file
                write_file.close()

                messagebox.showinfo(title="Modify ZIP Code", message ="You have successfully changed Provider ID "+provider_ID_entry.get() +"'s ZIP Code from " + old_zip_code_entry.get() + " to " + new_zip_code_entry.get())
                
            modify_zip_code_label = tkinter.Label(modifyZipCode, text="Modify ZIP Code", bg='#333333', fg='brown', font=("Arial, 30"))
            provider_ID_label = tkinter.Label(modifyZipCode, text="Provider ID", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
            provider_ID_entry = tkinter.Entry(modifyZipCode, font=("Arial, 16"))
            old_zip_code_label = tkinter.Label(modifyZipCode, text="Old ZIP Code", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
            old_zip_code_entry = tkinter.Entry(modifyZipCode, font=("Arial, 16"))
            new_zip_code_label = tkinter.Label(modifyZipCode, text="New ZIP Code", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
            new_zip_code_entry = tkinter.Entry(modifyZipCode, font=("Arial, 16"))
            submit_button = tkinter.Button(modifyZipCode, text="Submit", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=submit)
            close_window_button = tkinter.Button(modifyZipCode, text="Close Window", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=modifyZipCode.destroy)

            modify_zip_code_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
            provider_ID_label.grid(row=1, column=0)
            provider_ID_entry.grid(row=1, column=1, pady=20)
            old_zip_code_label.grid(row=2, column=0)
            old_zip_code_entry.grid(row=2, column=1, pady=20)
            new_zip_code_label.grid(row=3, column=0)
            new_zip_code_entry.grid(row=3, column=1, pady=20)
            submit_button.grid(row=4, column=1, columnspan=2, pady=30)
            close_window_button.grid(row=4, column=4, columnspan=2, pady=30)
        
        #Widgets for Modify Provider Window
        modify_provider_label = tkinter.Label(modifyProviderWindow, text="Modify Provider", bg='#333333', fg='brown', font=("Arial, 30"))
        modify_username_button = tkinter.Button(modifyProviderWindow, text="Modify Provider Username", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=modifyUsername)
        modify_password_button = tkinter.Button(modifyProviderWindow, text="Modify Provider Password", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=modifyPassword)
        modify_first_name_button = tkinter.Button(modifyProviderWindow, text="Modify Provider First Name", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=modifyFirstName)
        modify_last_name_button = tkinter.Button(modifyProviderWindow, text="Modify Provider Last Name", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=modifyLastName)
        modify_street_address_button = tkinter.Button(modifyProviderWindow, text="Modify Provider Street Address", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=modifyStreetAddress)
        modify_city_button = tkinter.Button(modifyProviderWindow, text="Modify Provider City", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=modifyCity)
        modify_state_button = tkinter.Button(modifyProviderWindow, text="Modify Provider State", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=modifyState)
        modify_ZIP_code_button = tkinter.Button(modifyProviderWindow, text="Modify Provider ZIP Code", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=modifyZipCode)
        close_window_button = tkinter.Button(modifyProviderWindow, text="Close Window", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=modifyProviderWindow.destroy)

        modify_provider_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
        modify_username_button.grid(row=1, column=0, columnspan=1, pady=20)
        modify_password_button.grid(row=2, column=0, columnspan=1, pady=20)
        modify_first_name_button.grid(row=3, column=0, columnspan=1, pady=20)
        modify_last_name_button.grid(row=4, column=0, columnspan=1, pady=20)
        modify_street_address_button.grid(row=5, column=0, columnspan=1, pady=20)
        modify_city_button.grid(row=6, column=0, columnspan=1, pady=20)
        modify_state_button.grid(row=7, column=0, columnspan=1, pady=20)
        modify_ZIP_code_button.grid(row=8, column=0, columnspan=1)
        close_window_button.grid(row=8, column=4, columnspan=2, pady=30)
        

    def removeProvider():
        removeProviderWindow = Toplevel()
        removeProviderWindow.title("Remove Provider")
        removeProviderWindow.geometry("500x500")
        removeProviderWindow.configure(bg='#333333')

        def submit():
            #open file in read mode
            file = open("Chocan Provider List.txt", "r")
            replaced_content = ""
            #looping through the file
            for line in file:
        
                #stripping line break
                line = line.strip()
                #replacing the texts
                new_line = line.replace("Provider ID " + provider_ID_entry.get() + " Status: Active", "Provider ID " + provider_ID_entry.get() + " Status: Inactive")
                #concatenate the new string and add an end-line break
                replaced_content = replaced_content + new_line + "\n"
        
            #close the file
            file.close()
            #Open file in write mode
            write_file = open("Chocan Provider List.txt", "w")
            #overwriting the old file contents with the new/replaced content
            write_file.write(replaced_content)
            #close the file
            write_file.close()

            messagebox.showinfo(title="Provider Removed", message ="Provider ID #" + provider_ID_entry.get() + " has been removed.")

        remove_provider_label = tkinter.Label(removeProviderWindow, text="Remove Provider", bg='#333333', fg='brown', font=("Arial, 30"))
        remove_provider_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
        provider_ID_label = tkinter.Label(removeProviderWindow, text="Provider ID #", bg='#333333',fg='#FFFFFF',font=("Arial, 16"))
        provider_ID_label.grid(row=1, column=0)
        provider_ID_entry = tkinter.Entry(removeProviderWindow, font=("Arial, 16"))
        provider_ID_entry.grid(row=2, column=0, pady=20)
        submit_button = tkinter.Button(removeProviderWindow, text="Submit", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=submit)
        submit_button.grid(row=3, column=0, columnspan=2, pady=30)
        close_window_button = tkinter.Button(removeProviderWindow, text="Close Window", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=removeProviderWindow.destroy)
        close_window_button.grid(row=6, column=4, columnspan=2, pady=30)

    # Create widgets for manageProviderWindow
    add_new_provider = tkinter.Button(manageProviderWindow, text="Add Provider", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=addProvider)
    renew_existing = tkinter.Button(manageProviderWindow, text="Renew Provider", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=renewProvider)  
    modify_provider = tkinter.Button(manageProviderWindow, text="Modify Provider", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=modifyProvider)
    remove_provider = tkinter.Button(manageProviderWindow, text="Remove Provider", bg="brown", fg="#FFFFFF",font=("Arial, 16"), command=removeProvider)

    # Place widgets for manageProviderWindow
    add_new_provider.grid(row=2, column=0, columnspan=2, pady=30)
    renew_existing.grid(row=3, column=0, columnspan=2, pady=30)
    modify_provider.grid(row=4, column=0, columnspan=2, pady=30)
    remove_provider.grid(row=5, column=0, columnspan=2, pady=30)
