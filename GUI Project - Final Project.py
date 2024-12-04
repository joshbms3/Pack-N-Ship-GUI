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

empty_stock = {'Perches': 0, 'Hanging Toys': 0, 'Foot Toys': 0}
check_values = True

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

def input_verify():
    global inputs_checked,check_values
    inventory_label = Label(top, text="Please enter a valid number")
    if check_values is True:
        check_values = False
        return inventory_label.pack()

def perches_calc():
    global perches
    if perch_entry.get().isdigit() is False:
        perches = stock['Perches']
        perch_entry.delete(0,END)
        input_verify()
    else:
        new_perches = perch_entry.get()
        perches = int(stock['Perches']) + int(new_perches)
        perch_entry.delete(0,END)

def hanging_toys_calc():
    global hangingToys
    if hanging_toy_entry.get().isdigit() is False:
        hangingToys = stock['Hanging Toys']
        hanging_toy_entry.delete(0,END)
        input_verify()
    else:
        new_hanging_toys = hanging_toy_entry.get()
        hangingToys = int(stock['Hanging Toys']) + int(new_hanging_toys)
        hanging_toy_entry.delete(0,END)

def foot_toys_calc():
    global footToys
    if foot_toy_entry.get().isdigit() is False:
        footToys = stock['Foot Toys']
        foot_toy_entry.delete(0,END)
        input_verify()
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
    global inventory_label
    list_of_files = os.listdir(os.getcwd())
    try:
        stock.update({'Perches': perches,'Hanging Toys': hangingToys,'Foot Toys': footToys})
    except NameError:
        global check_values
        if check_values is True:
            inventory_label = Label(top, text="Please input a value and try again")
            check_values = False
        return inventory_label.pack()

    for filename in list_of_files:
        if "KJPNSinventory" in filename:
            inv_file = open("KJPNSinventory.txt", 'w')
            inv_file.write(str(stock))
    try:
        if inventory_label:
                inventory_label.destroy()
    except NameError:
        pass
    inventory_label = Label(top, text=f"\nYour new updated inventory is:\n{str(stock).strip('{}').replace("'", "")}\n\n")
    inventory_label.pack()
    return

def inventory():
    global top
    top = Toplevel()
    top.title("Inventory")
    top.iconbitmap()
    top.geometry('615x615')
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

def check_file():
    listOfFiles = os.listdir(os.getcwd())
    for filename in listOfFiles:
        if "KJPNSinventory" in filename:
            inv_file = open("KJPNSinventory.txt", 'r')
            read_inv_file = inv_file.read()
            inv_file.close()
            global dashboard_label
            dashboard_label = (Label(text=f"\nAs of today your current inventory is: \n {read_inv_file.strip('{}').replace("'", "")}\n"))
            dashboard_label.pack()
            new_dashboard_label = dashboard_label
            return new_dashboard_label
    else:
        inv_file = open("KJPNSinventory.txt", "w")
        inv_file.write(str(empty_stock))
        inv_file.close()
        inv_file = open("KJPNSinventory.txt", "r")
        read_inv_file = inv_file.read()
        dashboard_label = (Label(text=f"\nAs of today your current inventory is: \n {read_inv_file.strip('{}').replace("'", "")}\n"))
        dashboard_label.pack()
        inv_file.close()
        return read_inv_file



def refresh():
    dashboard_label.destroy()
    check_file().pack()

def clear_inventory():
    inv_file = open("KJPNSinventory.txt", "w")
    inv_file.write(str(empty_stock))
    inv_file.close()
    dashboard_label.destroy()
    check_file().pack()


def welcome():
    welcome_msg = (Label(root, text="\nWelcome to Kaylae and Joshua's Pack 'N Ship Manager!\n"))
    welcome_msg.pack()
    welcome_img = ImageTk.PhotoImage(Image.open("vibrantparrots.png"))
    welcome_img_label = (Label(root, image=welcome_img))
    welcome_img_label.image = welcome_img
    welcome_img_label.pack()
    clear_inventory_button = Button(root, text="Clear inventory", command=clear_inventory)
    clear_inventory_button.pack(side="bottom")
    refresh_button = Button(root, text="Refresh", command=refresh)
    refresh_button.pack(side="bottom")
welcome()

def navigation():
    navFrame = LabelFrame(root, text="Navigation", padx=50)
    navFrame.pack()

    navigation = [
        "Inventory",
            "Pricing",
    ]
    global selection
    selection = StringVar()
    selection.set("Dashboard")

    drop = OptionMenu(navFrame, selection, *navigation)
    drop.grid(row=0, column=0)
    goButton = Button(navFrame, text="Go", command=go_to, pady=2)
    goButton.grid(row=0, column=1)

navigation()

check_file()

root.mainloop()