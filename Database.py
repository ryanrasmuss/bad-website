"""

Database 
~~~~~~~~

Various database commands 

Return various strings or T/F

"""

import sqlite3
import Policies as Pol
import HandleLogin as HL

db_name = 'login.db'

# Check if this is in Usernames (this seems repetetive)
def Username_Exists(username):

    ''' Returns 1 if username is in database, otherwise 0 '''

    print ("TYPE")
    print (type(username))
    
    # Python3 changed unicode to str and str to bytes??

    #XXX test format given

    return HL.Find_User(username, db_name)


# TODO: check if in banned passwords dictionary

# Insert new username and password

def Insert_New_User(username, password):

    # policy checks
    returns = Pol.Username_Policy(username)
    if returns is not Pol.GOOD:
        return returns

    returns = Pol.Password_Policy(password)
    if returns is not Pol.GOOD:
        return returns

    # Check username exists
    ''' going to want check username exists on encrypted logins
    if Username_Exists(username) is True:
        return "Username already exists"
    '''
    if Username_Exists(username) is True:
        return "Username already registered"

    # TODO: Check if bad password
    print ("Encrypting and storing user")

    # should be encrypted before storing
    if HL.StoreLogin(username, password, db_name) is True:
        return Pol.GOOD

    return "Failed to Store information"

def Verify_Login(username, password):

    ''' Unlike the functions above, this functions returns True or False
        True: user has been verified with proper credentials
        False: user has given incorrect credentials
    '''

    return HL.VerifyUser(username, password, db_name)
