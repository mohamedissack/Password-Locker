import unittest # Importing the unittest 
from credentials import Credentials #importing credential class


class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the Credentials class behaviors.
    '''
    
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        
        self.new_credential = Credentials('Mohamed','Twitter','1234')
        
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credential.user_name,"Mohamed")
        self.assertEqual(self.new_credential.account_name,"Twitter")
        self.assertEqual(self.new_credential.password,"1234")
    
    def test_save_credentials(self):
        '''
        Test to check if the new users info is saved into the user list
        '''
        
        self.new_credential.save_credentials()
        self.assertEqual(len(Credentials.credential_list),7)