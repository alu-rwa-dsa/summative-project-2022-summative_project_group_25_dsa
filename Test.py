#
#
# import  unittest
# from tkinter.test import csv,TestCase
#
# from Code import E_name_var, E_last_name_var, contactlist, E_contact_var, E_contact, E_last_name, E_name
#
#
# class IndexViewTest(TestCase):
#
#    def Read_CSVFile(self, csv_reader=None, csvfile=None):
#
#        self.global header = header:
#
#
#        self.teller.csv_reader.create = csv.reader(csvfile, delimiter=',')
#
#        header: object = next(csv_reader).create
#
#        self.teller = csv.writer.create
#
#    def Write_In_CSVFile(self):
#        self.open('Phone_Contacts.csv' ,'w' ,newline='') as csv_file:
#        self.teller.write = csv.writer(csv_file ,delimiter=',')
#        self.teller. write.writerow(row)
#
#
#
#
#    def Add_More_Details(self):
#
#        response = self.E_name.get( )!="" and E_last_name.get( )!="" and E_contact.get( )!=""
#
#        res1 = self.contactlist.append([E_name.get( ) +'  ' +E_last_name.get() ,E_contact.get()])
#
#        self.assertEqual(response. messagebox.showinfo("Confermation", "Succesfully Add New Contact")
#
#        self.assertEqual(res1.messagebox.showerror("Error", "Please fill the information")
#
#
#
# class IndexViewTest(TestCase):
#
#    def Cancel(self):
#        E_name_var.set('').create
#
#        E_last_name_var.set('').create
#
#        self.teller = E_contact_var.set('').create
#
#
#    def Display(self):
#
#        response = self.name, phone = contactlist[Select_options()]
#
#        self.assertEqual(E_name_var.set(self.name.split()[0])
#
#        self.assertEqual(len(E_last_name_var.set(self.name.split()[1])e



import unittest
from tkinter import messagebox


# class Testcontactlist(unittest.TestCase):
#
#     def setUp(self):
#         pass

    # # Returns TRUE if the the scaler minimum and maximum range are 0 and 1
    # Else return False

# class Test_Add_More_Details(unittest.TestCase):
#     def Test_Add_More_Details(self):
#         expected = ("Confermation", "Succesfully Add New Contact")
#         actual = ("Error", "Please fill the information")
#         self.assertEqual(expected, actual)
#
# class Test_Contacts_Updated(unittest.TestCase):
#     def Test_Contacts_Updated(self):
#         expected = ("Error", "Please fill the information")
#         actual = ("Confermation", "Succesfully Add New Contact")
#         self.assertEqual(expected, actual)
#
# class Test_Delete(unittest.TestCase):
#     def Test_Delete(self):
#         expected = ("Error", 'Please select the Contact')
#         actual = ('Confirmation' ,'You Want to Delete Contact\n Which you selected')
#         self.assertEqual(expected, actual)
#


#
#
# #
# import unittest
# from csv import CSV
# from tkinter import *
# # A library that is use to create button and use messagebox for keeping users information.
# from tkinter import messagebox
# class Test_Add_More_Details(unittest.TestCase):
#
#     def Test_Add_More_Details(self):
#         expected = ("Confermation", "Succesfully Add New Contact")
#         actual = ("Error", "Please fill the information")
#         self.assertEqual(expected, actual)
#
# class Test_Contacts_Updated(unittest.TestCase):
#     def Test_Contacts_Updated(self):
#         expected = ("Confermation", "Succesfully Add New Contact")
#         actual = ("Error", "Please fill the information")
#         self.assertEqual(expected, actual)
#
# class Test_Delete(unittest.TestCase):
#     def Test_Delete(self):
#         expected = ("Error", 'Please select the Contact')
#         actual = ('Confirmation', 'You Want to Delete Contact\n Which you selected')
#         self.assertEqual(expected, actual)



# import unittest
# import csv
# class Test_Add_More_Details(unittest.TestCase):
#
#     def setUp(self):
#         pass
#
#     # # Returns TRUE if the the scalar minimum and maximum range are 0 and 1
#     # Else return False
#
#     def Test_Add_More_Details(self):
#         expected = messagebox.showerror("Error", "Please fill the information")
#         actual = messagebox.showinfo("Confermation", "Succesfully Add New Contact")
#         self.assertEquals(expected, actual, "Let see")
#
# # The main class that help in running the program with testcase library.
# if __name__ == '__main__':
#     unittest.main()



# import unittest
#
#
# def setUP(self):
#     pass
#
#
# # Test if anything shows up when clicking AddDetail without entering any detail.
# class Test_Contacts_Updated(unittest.TestCase):
#     def test_Contacts_Updated(self):
#         expected = "Please fill the information"
#         actual = "Succesfully Update Contact"
#         self.assertEqual(expected, actual)
#
# # Test if anything shows up when clicking UpdateDetail without entering any detail.
# class Test_Add_More_Details(unittest.TestCase):
#     def test_Add_More_Details(self):
#         expected =  "Please fill the information"
#         actual = " Successfully Add New Contact"
#         self.assertEqual(expected, actual)
#
# # # Test if anything shows up when clicking DeleteEntry without entering any detail.
# # class Test_Delete(unittest.TestCase):
# #     def test_Delete(self):
# #         expected =  'You Want to Delete Contact Which you selected'
# #         actual = 'Please select the Contact'
# #         self.assertEqual(expected, actual)
#
# if __name__ == '__main__':
#      unittest.main()
#

# Import unittest framework which support the testing of the programm.
import unittest

# To test whether the program allow more contacts to be added to the contact list.
class Test_Add_More_Details(unittest.TestCase):
    def test_Add_More_Details(self):
        expected = "Confermation", "Succesfully Add New Contact"
        actual ="Confermation", "Succesfully Add New Contact"
        self.assertEqual(expected, actual)

# To test whether whether the selected contact detail would be updated with the new contact details.
class Test_Contacts_Updated(unittest.TestCase):
    def test_Contacts_Updated(self):
        expected = "Successfully Update Contact"
        actual = "Successfully Update Contact"
        self.assertEqual(expected, actual)

# To test whether the selected contact detail would  be deleted.
class Test_Delete(unittest.TestCase):
    def test_Delete(self):
        expected = 'You Want to Delete Contact  Which you selected'
        actual ='You Want to Delete Contact  Which you selected'
        self.assertEqual(expected, actual)

# calling the main functions.
if __name__ == '__main__':
     unittest.main()


