#
# Python 3.8.1
#
# Author: Pedro Suarez
#
# Purpose: The Tech Academy Drill. For this drill, you will need to write a 
# script that creates a database and adds new data into that database.
#
# Requirements:
#
# 1. Your script will need to use Python 3 and the sqlite3 module.
#
# 2. Your database will require 2 fields, an auto-increment primary 
#    integer field and a field with the data type of string.
#
# 3. Your script will need to read from the supplied list of file names 
#    at the bottom of this page and determine only the files from the 
#    list which ends with a “.txt” file extension.
#
# 4. Next, your script should add those file names from the list ending 
#    with “.txt” file extension within your database.
#
# 5. Finally, your script should legibly print the qualifying text 
#    files to the console.
#



import sqlite3

import os

def start():
    fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
                'myMovie.mpg', 'World.txt', 'data.pdf','myPhoto.jpg')
    tempList = []


    for file in fileList:
        if file.endswith('.txt'):
            tempList.append(file)


# Database connection
    conn = sqlite3.connect('txtfiles.db') 
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_txtfiles \
        (ID INTEGER PRIMARY KEY AUTOINCREMENT, col_fileName TEXT)")
        for i in tempList:
            cur.execute("INSERT INTO tbl_txtfiles (col_fileName) VALUES (?)",[i])
    query = conn.execute("SELECT (col_fileName) FROM  tbl_txtfiles")
    for row in query:
        print('File Name: {}'.format(row))
        conn.commit()
    conn.close()



if __name__ == "__main__":
    start()
