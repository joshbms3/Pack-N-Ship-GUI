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
root.geometry('300x380')
root_menu = Menu(root)
root.config(menu=root_menu)
"""This is the root menu, where the main window of the GUI gets its dimensions and title."""

empty_stock = {'Perches': 0, 'Hanging Toys': 0, 'Foot Toys': 0}
check_values = True
"""This is where the default values for empty stock and check values are stored and used for global manipulation.
I now know how to avoid using global variables like these and the ones in the other functions, however I started 
this project before actually learning how to do that effectively, so unfortunately I did not want to mess up
this app design by making any major changes. I will redesign it in the future."""

def menus():
    """This where the toolbar menus are created, currently, none of them actually work, but it would be very
    easy to implement these, all that is missing is a command function for them to call."""
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

def quit_program():
    """This is a quit program function that will terminate the entire application when called,
    specifically for the Quit button on the root window."""
    root.quit()

def close_window():
    """This is the close window function used only to close the top window and/or inventory window
    when called by the button."""
    top.destroy()
    refresh()

def input_verify():
    """This is where inputs are verified, utilizing the global statement to allow the variables
    inputs_checked, check values, and inventory label to be manipulated/initialized globally.
    The reason for the true/false values for check_values is so that if a user enters in an invalid data
    type and is warned to put in a valid number, it would continually flood the screen with errors."""
    global inputs_checked,check_values,inventory_label
    inventory_label = Label(top, text="Please enter a valid number")
    if check_values is True:
        check_values = False
        return inventory_label.pack()

def perches_calc():
    """This is where new perches get calculated by whether the data type in the entry perch_entry.get()
    are actual positive numbers and not characters. If the entry is not a digit the amount of perches
    currently stored in the KJPNSinventory.txt file will remain the appropriate value. After this the
    entry field is cleared with the delete function and then the input is checked with input_verify()."""
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
    """This function is basically the same concept as the previous function, except with the hanging
    toy entry instead."""
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
    """This function is basically the same concept as the previous two functions, except with the foot
        toy entry instead."""
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
    """This is an empty command used to prevent errors from unfinished buttons."""
    pass

def go_to():
    """This is the function that is incharge of popping up the second window that the user requests
    using the navigation frame."""
    choice = selection.get()
    if choice == "Inventory":
        inventory()
    if choice == "Pricing":
        pricing()

def commit():
    """This function is used to update all the values in the KJPNSinventory.txt file, it uses the
    try-except method to generate an error just incase it were to fail, meanwhile the values in the
    entry field are checked, then finally uses a for loop to find the file in the current working
    directory to open and write to it if it exists. And if it were to fail it would generate a
    NameError, lastly print a label with the updated stock, without the brackets and single apostrophes"""
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
    """This is the inventory function where everything in the inventory window from its display resolution, title, and
    its functionality are handled. This is also where the KJPNSinventory.txt file is interpreted as python code using
    the eval function, where it can stored inside a variable 'stock'. This is also where all the 'Submit' buttons get
    there calculation function calls."""
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
    close_button = Button(top, text="Close", command=close_window)
    close_button.pack(side="bottom")
    commit_changes = Button(top, text="Commit changes", command=commit)
    commit_changes.pack(side="bottom")


def pricing():
    """This window currently does not function, it is simply an empty window for now that does not
    do anything other than display a label 'Under construction'"""
    global top
    top = Toplevel()
    top.title("Pricing")
    top.iconbitmap()
    top.geometry('300x300')
    under_construction_label = Label(top, text="Under construction")
    under_construction_label.pack()
    pass

def check_file():
    """This is another function used to check the existence of the KJPNSinventory.txt file, if it does exist
    it is read, assigned to a variable and printed without its curly brackets and single apostrophes. Lastly,
    if the file does not exist it is then opened using 'w' write permissions where the dictionary stored in the
    empty stock variable is written into the file as a string, as later will be evaluated back into a dictionary."""
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
    """This is a refresh function, all it really does it destroy the label and re-display the inventory,
    it doesn't actually need to be called as the program writes to the inventory file immediately, this
    is simply to display proper values on the root window of the app."""
    dashboard_label.destroy()
    check_file().pack()

def clear_inventory():
    """This function is used to write an empty stock to the file when the user requests by clicking the
    'Clear Inventory' button on the root window of the app."""
    inv_file = open("KJPNSinventory.txt", "w")
    inv_file.write(str(empty_stock))
    inv_file.close()
    dashboard_label.destroy()
    check_file().pack()


def welcome():
    """This is where the welcome message is displayed for my app, the image is loaded, buttons, and
    drop down menus are all stored and packed into the root menu, using the side 'bottom', to ensure
    they stay below the welcome msg and photo."""
    welcome_msg = (Label(root, text="\nWelcome to Kaylae and Joshua's Pack 'N Ship Manager!\n"))
    welcome_msg.pack()
    welcome_img = ImageTk.PhotoImage(Image.open("vibrantparrots.png"))
    welcome_img_label = (Label(root, image=welcome_img))
    welcome_img_label.image = welcome_img
    welcome_img_label.pack()
    quit_button = Button(root, text="Quit", command=quit_program)
    quit_button.pack(side="bottom")
    clear_inventory_button = Button(root, text="Clear inventory", command=clear_inventory)
    clear_inventory_button.pack(side="bottom")
    refresh_button = Button(root, text="Refresh", command=refresh)
    refresh_button.pack(side="bottom")
welcome()

def navigation():
    """This is simply where the navigation frame is stored to allow the user to make a choice
    on which window to open / navigate to."""
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
"""This is what first initializes the program, and begins to run it in a consistent loop until terminated
by the end user, using my 'Quit' button or the X in the top right corner."""