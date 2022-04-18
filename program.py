


# A library is mainly use to create button.
from tkinter import *
# Import Csv as it contain some details.
import csv
# A library that is use to create button and use messagebox for keeping users information.
from tkinter import messagebox

# create empty list that would handle user input.
contactlist = []

# Function that contain file where user inputs are contains.
def Read_CSVFile():
    # create global variable header which allow it to be use anywhere in a code.
    global header
    # Files that store user input data.
    with open('Phone_Contacts.csv') as csvfile:
        # Read data in a file which are in a separate data streams.
        csv_reader = csv.reader(csvfile ,delimiter=',')
        header = next(csv_reader)
        # Check row data whether they are in a file header.
        for row in csv_reader:
            # Add contacts to contact list.
            contactlist .append(row)
    # To return back the selected contact.
    set_select()
    # print the contact list requested.
    print(contactlist )

# Function that handle a file where input of the user are contain.
def Write_In_CSVFile(phonelist):
    try:
        # File that store contact data
        with open('Phone_Contacts.csv' ,'w' ,newline='') as csv_file:
            # To write in a file
            write = csv.writer(csv_file ,delimiter=',')
            write.writerow(header)
            # check row in a contact list of the user input
            for row in phonelist:
                # write in a row part.
                write.writerow(row)
    except PermissionError:
        print("Please chose within the list of contact.")
# Function that deal with the selection of the name in a stack.
def Select_options():
    try:
        # Determine the length of the selected option
        print("hello" ,len(select.curselection()))
        # check if the selected element is equal to zero
        if len(select.curselection() )==0:
            # Display error in a message box in case a user hasn't select the name.
            messagebox.showerror("Error", "Please Select the Name")
        else:
            # Return the selected part if the first one doesn't work
            return int(select.curselection()[0])
    except ValueError:
        print("select the proper contact details")

# Function to deal for adding more data into an array of the contacts.
def Add_More_Details():
    try:
        # Add on the details of the contact list.
        if E_name.get( )!="" and E_last_name.get( )!="" and E_contact.get( )!="":
            # Add contacts details to array of the contact list.
            contactlist.append([E_name.get( ) +'  ' +E_last_name.get() ,E_contact.get()])
            # Print contact inserted in a list by the user.
            print(contactlist)
            # Allow user to write to a contact list file.
            Write_In_CSVFile(contactlist)
            # To select the option of choice
            set_select()
            # Redo the data inserted.
            Cancel()
            # Show message box for confirming whether the new added contact is added.
            messagebox.showinfo("Confermation", "Succesfully Add New Contact")
        else:
            # Show an error message if the first option is not satisfied.
            messagebox.showerror("Error", "Please fill the information")
    except TypeError:
        print("please put the correct contact details.")


# Function that handling updating contact.
def Contacts_Updated():
    try:
        # Update the details of the contact list.
        if E_name.get() and E_last_name.get() and E_contact.get():
            # Select the the contact which need to be updated from contact list.
            contactlist[Select_options()] = [ E_name.get( ) +'  ' +E_last_name.get(), E_contact.get()]
            # Insert the new contact to the contact list.
            Write_In_CSVFile(contactlist)
            # Show the updated new contact in the message box.
            messagebox.showinfo("Confirmation", "Succesfully Update Contact")
            # Option to cancel the chosen contact details.
            Cancel()
            # Select the contact that need to be updated.
            set_select()
            # check if the user didn't select anything contact from the contact list to update.
        elif not(E_name.get()) and not(E_last_name.get()) and not(E_contact.get()) and not(len(select.curselection() )==0):
            # Prompt the error.
            messagebox.showerror("Error", "Please fill the information")
        else:
            # Evaluate if no contact is selected.
            if len(select.curselection() )==0:
                # Tell the user to select the contact from the contact list.
                messagebox.showerror("Error", "Please Select the Name and \n press Load button")
            else:
                # To return the details of the contact to the screen
                message1 = """To Load the all information of \n selected row press Load button\n."""
                # Show the error that maybe encounter in the process.
                messagebox.showerror("Error", message1)
    except ValueError:
        print("select the proper contact details to update")

# Function that would focus on resetting the selected contact
def Cancel():
    try:
        # reset the name
        E_name_var.set('')
        # reset the last name
        E_last_name_var.set('')
        # reset the phone Number
        E_contact_var.set('')
    except ValueError:
        print("Please select the correct contact you want to cancel.")


# Function that would handle the delete part in the program.
def Delete():
    try:
        # Evaluate if none of the contact is selected.
        if len(select.curselection() )!=0:
            # Asked the user to confirm whether the selected option to delete would be the best choice.
            result =messagebox.askyesno('Confirmation' ,'You Want to Delete Contact\n Which you selected')
            # Evaluate the if the choice of the selected option is the best choice.
            if result==True:
                # Delete the selected contact from the contact list.
                del contactlist[Select_options()]
                # Update the contact list.
                Write_In_CSVFile(contactlist)
                # select the contact that to be selected.
                set_select()
        else:
            # Tell the user to chose the contact if it doesn't do so.
            messagebox.showerror("Error", 'Please select the Contact')
    except TypeError:
        print("Please select the right contact to delete.")

# Function that reprompt the details selected by the user to the screen.
def Display():
    try:
        # Direct the options that should be setected in the contact list.
        name, phone = contactlist[Select_options()]
        print(name.split(' '))
        # Print the first name
        E_name_var.set(name.split()[0])
        # print the last name
        E_last_name_var.set(name.split()[1])
        # print the phone number
        E_contact_var.set(phone)
    except ValueError:
        print("Please try to put numbers or select the contact when trying to load the contacts.")



# Function that monitor the user input into the contact list.
def set_select():
    try:
        # Arrange the inserted contacts in ascending order base on the how the were inserted/recorded.
        contactlist.sort(key=lambda record: record[1])
        # To select the contact to be deleted.
        select.delete(0, END)
        i=0
        # Check name and phone in a contact list.
        for name, phone in contactlist:
            # iterate the number and name.
            i+=1
            # Insert the names and number to the contact list.
            select.insert(END, f"{i}  |    {name}   |   {phone}")
    except IndexError:
        print("please select the number within the program cycle to avoid this the list index out of range")

window = Tk()
# Frame where to tell the user the title of the program
Frame1 = LabelFrame(window, text="Enter the Contact Detail")
Frame1.grid(padx=15, pady=15)

Inside_Frame1 = Frame(Frame1)
Inside_Frame1.grid(row=0, column=0, padx=15, pady=15)

# frame to print the first name
l_name = Label(Inside_Frame1, text="FirstName")
l_name.grid(row=0, column=0, padx=5, pady=5)
E_name_var = StringVar()

E_name = Entry(Inside_Frame1, width=30, textvariable=E_name_var)
E_name.grid(row=0, column=1, padx=5, pady=5)

# frame to print the last name
l_last_name = Label(Inside_Frame1, text="LastName")
l_last_name.grid(row=1, column=0, padx=5, pady=5)
E_last_name_var = StringVar()
E_last_name = Entry(Inside_Frame1, width=30, textvariable=E_last_name_var)
E_last_name.grid(row=1, column=1, padx=5, pady=5)

# frame to print the the phone number
l_contact = Label(Inside_Frame1, text="Phone.No")
l_contact.grid(row=2, column=0, padx=5, pady=5)
E_contact_var = StringVar()
E_contact = Entry(Inside_Frame1, width=30, textvariable=E_contact_var)
E_contact.grid(row=2, column=1, padx=5, pady=5)

Frame2 = Frame(window)
Frame2.grid(row=0, column=1, padx=15, pady=15, sticky=E)

# Giving the color to the window on "Add contact".
Add_button = Button(Frame2, text="Add", width=15, bg="Blue", fg="white", command=Add_More_Details)
Add_button.grid(row=0, column=0, padx=8, pady=8)

# Giving the color to the window on " update the contact".
Update_button = Button(Frame2, text="Update", width=15, bg="Blue", fg="White", command=Contacts_Updated)
Update_button.grid(row=1, column=0, padx=8, pady=8)

# Giving the color to the " Reset".
Reset_button = Button(Frame2, text="Cancel", width=15, bg="Blue", fg="White", command=Cancel)
Reset_button.grid(row=2, column=0, padx=8, pady=8)

DisplayFrame = Frame(window)
DisplayFrame.grid(row=1, column=0, padx=15, pady=15)

scroll = Scrollbar(DisplayFrame, orient=VERTICAL)
select = Listbox(DisplayFrame, yscrollcommand=scroll.set, font=("Arial Bold", 10), bg="#282923", fg="#E7C855", width=40,
                 height=10, borderwidth=3, relief="groove")
scroll.config(command=select.yview)
select.grid(row=0, column=0, sticky=W)
scroll.grid(row=0, column=1, sticky=N + S)

ActionFrame = Frame(window)
ActionFrame.grid(row=1, column=1, padx=15, pady=15, sticky=E)

# Giving the button the color on delete
Delete_button = Button(ActionFrame, text="Delete", width=15, bg="Blue", fg="White", command=Delete)
Delete_button.grid(row=0, column=0, padx=5, pady=5, sticky=S)

# Giving the button the color on load
Loadbutton = Button(ActionFrame, text="Display", width=15, bg="Blue", fg="White", command=Display)
Loadbutton.grid(row=1, column=0, padx=5, pady=5)


# call the read file
Read_CSVFile()
# Call the window main class to the program
window.mainloop()
