from tkinter import *
from tkinter import ttk

def display_search():
    # Toplevel object which will
    # be treated as a new openNewWindow
    makeSearch = Toplevel()
    # sets the title of the Toplevel widget
    makeSearch.title("Enter Service Code")

    # sets the geometry of Toplevel
    makeSearch.geometry("300x200")





    lst = ['Code10', 'Code20', 'Code30',
           'Code40', 'Code50',
           'Code60', 'Code70', 'Code80','Code90',
           'Code100','Code110']

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




    label = Label(makeSearch,text='Search your favorite code')
    label.pack()
    # creating Combobox
    combo_box = ttk.Combobox(makeSearch,value=lst)

    combo_box.set('Search')
    combo_box.pack()


    combo_box.bind('<KeyRelease>',search)


