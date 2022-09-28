#!/usr/local/bin/python

import time

userName = "fancypants"
passWord = "catchM3ifYouCan"

complete = False
user = {"some username" : "some password", "more username" : "more password"}

while not complete:
    username = input("What is the username?")
    password = input("What is the password?")
    conf_username = input("Repeat the username?")
    conf_password = input("Repeat the password?")
    # since in your question you said you wanted to ask the user to repeat
    if username != conf_username or password != conf_password:
        print("username or password does not match") # print a message if different inputs
        continue # restarts
    if not username in user: # check to see if user does not exists
        print("Input username again!")
        continue
    if password == user[username]: # check to see if password match
        print("User has been identified, Welcome",username)
        complete = True
    else:
        print("Input password again")
