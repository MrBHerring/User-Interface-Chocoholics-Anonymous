from tkinter import *
from tkinter import ttk






lst = ['C', 'C++', 'Java',
       'Python', 'Perl',
       'PHP', 'ASP', 'JS','HTML',
       'Ruby','Machine Learning']

def search(event):
    value = event.widget.get()
    if value == '':
        combo_box['values'] = lst

    else:
        data = []

        for item in lst:
            if value.lower() in item.lower():
                data.append(item)

        combo_box['values'] = data



root = Tk()
root.title("Combobox")
root.geometry("300x200")
label = Label(root,text='Search your favorite language')
label.pack()
# creating Combobox
combo_box = ttk.Combobox(root,value=lst)

combo_box.set('Search')
combo_box.pack()


combo_box.bind('<KeyRelease>',search)

root.mainloop()
