"""
Author:  Joshua Barroso
Date written: 12/2/2024
Assignment:   Module6 exercise1
Short Desc:
The link of the GitHub repository for your final project. 10 points
A working GUI tkinter application with at least two windows.   50 points
Implementing a modular approach in your application. 10 points
Consistent clear navigation throughout the GUI application.   10 points
Use at least two images in your application(images should have alternate text).  10 points
Include at least three labels. 10 points
Include at least three buttons. 10 points
Include at least three call back function with each button, including exit button. 20 points
Implement secure coding best practices, including input validation to check if the user entered
 the correct data type, make sure the entry box is not empty, etc.   10 points
"""

from tkinter import *
from PIL import ImageTk,Image
import os


root = Tk()
root.title("Pack 'N Ship Manager")
root.iconbitmap()
root.geometry('300x350')
root_menu = Menu(root)
root.config(menu=root_menu)

def menus():
    file_menu = Menu(root_menu)
    root_menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="New...")
    file_menu.add_command(label="Open...")
    file_menu.add_command(label="Save")
    file_menu.add_command(label="Save As...")
    file_menu.add_separator()
    file_menu.add_command(label="Import...")
    file_menu.add_command(label="Export...")
    edit_menu = Menu(root_menu)
    root_menu.add_cascade(label="Edit", menu=edit_menu)
    edit_menu.add_command(label="Cut")
    edit_menu.add_command(label="Copy")
    edit_menu.add_command(label="Paste")

    help_menu = Menu(root_menu)
    root_menu.add_cascade(label="Help", menu=help_menu)
    help_menu.add_command(label="(under construction)")
menus()


def check_file():
    listOfFiles = os.listdir(os.getcwd())
    for filename in listOfFiles:
        if "KJPNSinventory" in filename:
            inv_file = open("KJPNSinventory.txt", 'r')
            read_inv_file = inv_file.read()
            return read_inv_file
    else:
        inv_file = open("KJPNSinventory.txt", "w")
        empty_stock = {'Perches':0,'Hanging Toys':0,'Foot Toys':0}
        inv_file.write(str(empty_stock))
        inv_file = open("KJPNSinventory.txt", "r")
        read_inv_file = inv_file.read()
        return read_inv_file

def perches_calc():
    global perches
    if perch_entry.get() == "":
        perches = stock['Perches']
    else:

        new_perches = perch_entry.get()
        perches = int(stock['Perches']) + int(new_perches)
        perch_entry.delete(0,END)

def hanging_toys_calc():
    global hangingToys
    if hanging_toy_entry.get() == "":
        hangingToys = stock['Hanging Toys']
    else:
        new_hanging_toys = hanging_toy_entry.get()
        hangingToys = int(stock['Hanging Toys']) + int(new_hanging_toys)
        hanging_toy_entry.delete(0,END)

def foot_toys_calc():
    global footToys
    if foot_toy_entry.get() == "":
        footToys = stock['Foot Toys']
    else:
        new_foot_toys = foot_toy_entry.get()
        footToys = int(stock['Foot Toys']) + int(new_foot_toys)
        foot_toy_entry.delete(0,END)

def empty_command():
    pass

def go_to():
    choice = selection.get()
    if choice == "Inventory":
        inventory()
    if choice == "Pricing":
        pricing()


def commit():
    list_of_files = os.listdir(os.getcwd())
    stock.update({'Perches': perches})
    stock.update({'Hanging Toys': hangingToys})
    stock.update({'Foot Toys': footToys})
    for filename in list_of_files:
        if "KJPNSinventory" in filename:
            inv_file = open("KJPNSinventory.txt", 'w')
            inv_file.write(str(stock))
            inventory_label = Label(top,text=f"\nYour new updated inventory is:\n{stock}")
            inventory_label.pack()
            return

def inventory():
    global top
    top = Toplevel()
    top.title("Inventory")
    top.iconbitmap()
    top.geometry('615x600')
    global stock
    stock = eval(open("KJPNSinventory.txt", 'r').read())
    inventory_img = ImageTk.PhotoImage(Image.open("warehousewithbirds.png"))
    inventory_img_label = Label(top, image=inventory_img)
    inventory_img_label.image = inventory_img
    inventory_img_label.pack(pady=10)
    perch_label = (Label(top, text="Enter perch amount:"))
    perch_label.pack()
    global perch_entry
    perch_entry = Entry(top, width=5,borderwidth=1)
    perch_entry.pack()
    perch_button = (Button(top, text="Submit",command=perches_calc))
    perch_button.pack()
    hanging_toy_label = Label(top, text="Enter hanging toy amount:")
    hanging_toy_label.pack()
    global hanging_toy_entry
    hanging_toy_entry = Entry(top, width=5, borderwidth=1)
    hanging_toy_entry.pack()
    hanging_toy_button = Button(top, text="Submit", command=hanging_toys_calc)
    hanging_toy_button.pack()
    foot_toy_label = Label(top, text="Enter foot toy amount:")
    foot_toy_label.pack()
    global foot_toy_entry
    foot_toy_entry = Entry(top, width=5, borderwidth=1)
    foot_toy_entry.pack()
    foot_toy_button = Button(top, text="Submit", command=foot_toys_calc)
    foot_toy_button.pack()
    commit_changes = Button(top, text="Commit changes", command=commit)
    commit_changes.pack(side="bottom")


def pricing():
    top = Toplevel()
    top.title("Pricing")
    top.iconbitmap()
    top.geometry('300x300')
    pass

def welcome():
    welcomeMsg = (Label(root, text="\nWelcome to Kaylae and Joshua's Pack 'N Ship Manager!\n"))
    welcomeMsg.pack()
    welcomeImg = ImageTk.PhotoImage(Image.open("vibrantparrots.png"))
    welcomeImgLabel= (Label(root, image=welcomeImg))
    welcomeImgLabel.image = welcomeImg
    welcomeImgLabel.pack()
welcome()

def navigation():
    navFrame = LabelFrame(root, text="Navigation",padx=50)
    navFrame.pack()

    navigation = [
        "Inventory",
        "Pricing",
    ]
    global selection
    selection = StringVar()
    selection.set("Dashboard")

    drop = OptionMenu(navFrame,selection, *navigation)
    drop.grid(row=0,column=0)
    goButton = Button(navFrame, text="Go", command=go_to,pady=2)
    goButton.grid(row=0,column=1)
navigation()

def check_inventory():
    dashboardInvMsg = (Label(text=f"\nAs of today your current inventory is: \n {check_file()}"))
    dashboardInvMsg.pack()
check_inventory()


root.mainloop()