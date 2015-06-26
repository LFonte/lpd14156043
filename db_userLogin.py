# -*- coding: utf-8 -*-

"""
Main File

@author Luis Fonte
@date 20150326
"""

import os
import sqlite3
import hashlib

def database():
    """
    Creates db.
    """
    con = sqlite3.connect("users.db")
    cursor = con.cursor()
    cursor.execute("DROP TABLE IF EXISTS users")
    cursor.execute("CREATE TABLE users(id INTEGER PRIMARY KEY,user VARCHAR(30), pass VARCHAR(30))")
    pass

def user_add(username, password):
    """
    Add user to db.
    """
    u = hashlib.md5(username).hexdigest()
    p = hashlib.md5(password).hexdigest()
    con = sqlite3.connect("users.db")
    cursor = con.cursor()
    cursor.execute("INSERT INTO users VALUES (null, ?, ?)", (u,p))
    con.commit()
    pass

def login(username, password):
    """
    Do login.

    @False - returns false if login fails
    @True - returns true if login succeded
    """
    u = hashlib.md5(str.encode(username)).hexdigest()
    p = hashlib.md5(str.encode(password)).hexdigest()
    #print u
    #print p
    con = sqlite3.connect("users.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM users WHERE user=? and pass=?", (u,p))
    user = cursor.fetchone()
    if user == None:
        return False
    else:
        return True
    pass

