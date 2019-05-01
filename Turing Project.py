import tkinter

root = tkinter.Tk()
v=tkinter.IntVar()
update = 10

homePage = tkinter.Frame(root, bg="orange", height=600, width=400)
homePage.grid_propagate(False) #lock the home page and others are limited to this size
homePage.grid(row=0, column=0, sticky="nsew")

pageOne = tkinter.Frame(root, bg="yellow")
pageOne.grid(row=0, column=0, sticky="nsew")
pageTwo = tkinter.Frame(root, bg="yellow")
pageTwo.grid(row=0, column=0, sticky="nsew")
pageThree = tkinter.Frame(root, bg="yellow")
pageThree.grid(row=0, column=0, sticky="nsew")
pagePass = tkinter.Frame(root, bg="green")
pagePass.grid(row=0, column=0, sticky="nsew")
pageFail = tkinter.Frame(root, bg="red")
pageFail.grid(row=0, column=0, sticky="nsew")
homePage.tkraise()

def showHome():
    homePage.tkraise()

def showPageOne():
    pageOne.tkraise()


def showPageTwo():
    pageTwo.tkraise()

def showPageThree():
    pageThree.tkraise()

def showPagePass():
    pagePass.tkraise()

def showPageFail():
    pageFail.tkraise()
    
goToOne = tkinter.Button(homePage, text="Go to First Question", fg="red", command=showPageOne)
goToOne.grid(row=0, column=0, sticky="nsew")


nextPage2 = tkinter.Button(pageOne, text="Next Page", fg="black", command=showPageTwo)
nextPage2.grid(row=0, column=0, sticky="nsew")

#Here we can have checkboxes or a series of buttons or and entry field.

label1 = tkinter.Label(pageTwo, text="i am label one")
label1.grid(row=0, column=0)


nextPage3 = tkinter.Button(pageTwo, text="Next Page", fg="black", width=10, command=showPageThree)
nextPage3.grid(row=1, column=0)

Radio_1 = tkinter.Radiobutton(pageThree, text="Option 1", value=1, variable=v)
Radio_1.grid(row=0, column=0, sticky="nsew")
Radio_2 = tkinter.Radiobutton(pageThree, text="Option 2", value=2, variable=v)
Radio_2.grid(row=1, column=0, sticky="nsew")
Radio_3 = tkinter.Radiobutton(pageThree, text="Option 3", value=3, variable=v)
Radio_3.grid(row=2, column=0, sticky="nsew")
selection = v.get()

#This If statement doesn't work correctly yet. The selection is 0 no matter what radio button is pressed.
#Needs more conditions to pass test. Conditions can be set in pages 1 and 2.
Final = ""
if selection == 0:
    Final = showPagePass
elif selection == 1:
    Final = showPageFail
else:
    Final = showPagePass

pageFinal = tkinter.Button(pageThree, text="See Result", fg="black", command=Final)
pageFinal.grid(row=0, column=2, sticky="nsew")
print ("Selection:", selection)
root.mainloop()
