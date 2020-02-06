"""

HandleLogin
~~~~~~~~~~

Has two functions: FindLogin and StoreLogin both have the same arguments of username, password, and database name.

FindLogin will search the database for the username and password inside the given database. This function is used for verifying logins.

StoreLogin will simply encrypt both username and password before inserting the encrypted username and password into the given database

Each function will return True or False

"""

import sqlite3
from bcrypt import hashpw, gensalt, checkpw

def VerifyUser(username, password, db_name):

    if isinstance(username, bytes) is False:
        username = username.encode('utf-8')
    if isinstance(password, bytes) is False:
        password = password.encode('utf-8')

    match = 0
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    
    if cur.fetchone is None:
        print ('DB is empty')
        return False

    print ("Hola, matey")
    # invalid salt will be thrown if db is not hashed
    for row in cur.execute('SELECT * FROM users'):
        print (row)
        if checkpw(username, row[1]):
            if checkpw(password, row[2]):
                print ("MATCH!")
                print (username, "to", row[1])
                print (password, "to", row[2])
                match = 1
                break

    conn.close()
    if match == 1:
        return True
    else:
        return False

def Find_User(username, db_name):

    if isinstance(username, bytes) is False:
        username = username.encode('utf-8')

    conn = sqlite3.connect(db_name)
    cur = conn.cursor()

    if cur.fetchone is None:
        print ('DB is empty')
        return False

    for user in cur.execute("SELECT username FROM users"):
        if checkpw(username, user[0]) is True:
            return True

    # could not find
    return False
        

def StoreLogin(username, password, db_name):

    ''' username and passwords must be encoded utf-8 '''
    if isinstance(username, bytes) is False:
        username = username.encode('utf-8')
    if isinstance(password, bytes) is False:
        password = password.encode('utf-8')

    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    
    # checkpw problem: pretty sure it's because none of the db entries and encrypted yet
    for users in cur.execute('SELECT username FROM users'):
        # print users users is (u'username', )
        if checkpw(username, users[0]):
            print ('login already exists')
            return False

    salt = gensalt()
    hashed_user = hashpw(username, salt)
    hashed_pw = hashpw(password, salt)
    hashed = [hashed_user, hashed_pw]
    #print (hashed)

    cur.execute('INSERT INTO users (username, password) values (?, ?)', hashed)
    conn.commit()
    conn.close()
    return True
#end
