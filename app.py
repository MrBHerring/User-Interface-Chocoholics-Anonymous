from tkinter import *
from PIL import Image, ImageTk
from functions import display_logo, openMemberWindow, openProviderWindow, openManagerWindow, Schedule_Report, SearchService
#from ServiceBox import serviceBoxing
#from ServiceBox import display_search

page_contents = []
all_images = []
img_idx = [0]
displayed_img = []


root = Tk()
root.geometry('+%d+%d'%(1250,10)) #place GUI at x=350, y=10

#header area - logo & browse button
header = Frame(root, width=800, height=220, bg="gray")
header.grid(columnspan=3, rowspan=2, row=0)


#main content area - text and image extraction
main_content = Frame(root, width=800, height=250, bg="brown")
main_content.grid(columnspan=3, rowspan=2, row=4)





Member_btn = Button(root, text="Member Login", font=("Raleway", 12), bg="brown",fg="white", height=1, width=15, command=openMemberWindow)
Provider_btn = Button(root, text="Provider Login", font=("Raleway", 12), bg="brown",fg="white", height=1, width=15, command=openProviderWindow)
Manager_btn = Button(root, text="Manager Login", font=("Raleway", 12), bg="brown",fg="white", height=1, width=15, command=openManagerWindow)
Service_btn = Button(root, text="Service Code", font=("Raleway", 12), bg="blue",fg="white", height=1, width=15, command=SearchService)
ScheduleReport_btn = Button(root, text="Schedule Report", font=("Raleway", 12), bg="blue",fg="white", height=1, width=15, command=Schedule_Report)


Member_btn.grid(row=3,column=0,padx=(0,90), pady=5)
Provider_btn.grid(row=3,column=1,padx=(0,150))
Manager_btn.grid(row=3,column=2)
Service_btn.grid(row=4,column=0,padx=(0,90))
ScheduleReport_btn.grid(row=4,column=1,padx=(0,150))

display_logo('logo.png', 0, 0)

#instructions


root.mainloop()
