import pyperclip

class User:
    '''
    class that allows user to generate user account
    '''
    
    user_list = []
    
    def __init__(self,user_name,password):
        self.user_name = user_name
        self.password = password
        
    def save_user(self):
        '''
        save_user method that saves new user object
        '''
        User.user_list.append(self)

