#!/usr/bin/env python3.8
import pyperclip 
from user import User
from credentials import Credentials
import random #import random variable generator
import string  #import string constants

def create_user(user_name,password):
    '''
    Function to create new user
    '''
    new_user = User(user_name,password)
    return new_user

    def save_user(user):
    '''
    Function to save new user account
    '''
    user.save_user()
    def verify_user(user_name,password):
    '''
    Function that verifies the existing user
    
    '''
    check_user = Credentials.check_user(user_name,password)
    return check_user
    
def create_credential(user_name,account_name,password):
    '''
    Function that creates new credential
    '''
    new_credential = Credentials(user_name,account_name,password)
    return new_credential