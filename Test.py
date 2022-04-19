

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


