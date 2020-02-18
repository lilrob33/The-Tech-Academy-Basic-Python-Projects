#
# Python: 3.8.1
#
# Author: Pedro Suarez
#
# Purpose: The Tech Academy first Python drill. 
# For this drill, you will need to write a script that 
# will check a specific folder on the hard drive, verify whether 
# those files end with a “.txt” file extension and if they do,
# print those qualifying file names and their corresponding modified 
# time-stamps to the console.
#

"""
Requirements:

1. Your script will need to use Python 3 and the OS module.

2. Your script will need to use the listdir() method from the OS module
   to iterate through all files within a specific directory.

3. Your script will need to use the path.join() method from the OS module 
   to concatenate the file name to its file path, forming an absolute path.

4. Your script will need to use the getmtime() method from the OS module to
   find the latest date that each text file has been created or modified.

5. Your script will need to print each file ending with a “.txt” file 
   extension and its corresponding mtime to the console.
"""

# Additional Setup Instructions:

# You will need to create a new directory on your system and then create 10 
# different files within this folder. The files that you create should be a 
# combination of any file types you would like just as long as you include at
# least two that are text documents ending with a “.txt” file extension.

# This directory will be the directory that your script will need to iterate 
# through to complete the drill.







import os

import time


# Set fPath variable
fPath = "C:\\Users\\psuar\\OneDrive\\Desktop\\python_drill\\"

# Set fList Variable
fList = os.listdir(fPath)



for f in fList:
    if f.endswith('.txt'):
        textFiles = os.path.join(fPath,f)
        modTime = time.localtime(os.path.getmtime(fPath))
        fmTime = time.strftime("%m/%d/%Y, %H:%M:%S", modTime)
        print("File Name:", textFiles,"Modified:", fmTime)











