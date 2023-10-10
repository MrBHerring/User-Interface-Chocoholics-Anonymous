from tkinter import *
from tkinter import messagebox

race = []

def displayInfo(race, name):
    found = False
    pos = 0
    while pos< len(race) and not found:
        if race[pos][0] == name:
            found = True
        pos+=1
    if found:
        return race[pos-1][1]
    else:
        messagebox.showerror(message = "Invalid input, please try again. ")

def clickArea():
    fin.set(displayInfo(race, name.get()))
    
def createList():
    raceFile = open ("race.txt", 'r')
    for line in raceFile:
        racer = line.split()
        race.append(racer)
    raceFile.close()
    return race

root = Tk()
root.title("Read From Text File/List GUI")

Label(root, text="Name").grid(row=0, column=0)
name = StringVar()
Entry(root, textvariable=name).grid(row=0, column=1)

Label(root, text="Finish Time").grid(row=2, column=0)
fin = IntVar()
Entry(root, textvariable=fin).grid(row=2, column=1)

button = Button(root, text="Finish Time", command=clickArea)
button.grid(row=3, column=0, columnspan=2)

createList()
print(race)
