 ###############################################################################
##																			   ##	
## mkprjct is a python script that generates the file structure and key files  ##
## for a new python project													   ##
##                                                                             ##
## Project will be created in the directory that this script is run from.      ##
## INPUT: project name														   ##					
##																			   ##
## Developed by Chloe Dyke - 2017											   ##
##																			   ##
 ###############################################################################

import os
 
# Get the name of the directory from user 
dirname = input("Enter the project name: ")

# Create top-level directory
if not os.path.isdir('./' + dirname + '/'):
    os.mkdir('./' + dirname + '/') 
	
    # Create second-level directories (don't need to check if directories exist as
    # top-level directory has just been created
    os.mkdir('./' + dirname + '/' + dirname + '/')
    os.mkdir('./' + dirname + '/docs/')
    os.mkdir('./' + dirname + '/' + dirname + '/test/')
    os.mkdir('./' + dirname + '/LICENSE')

    # Create top-level files that are standard across projects
    file=open('./' + dirname + '/setup.py','a')
    file=open('./' + dirname + '/README.md','a')
    file=open('./' + dirname + '/requirements.txt','a')

    # Create second-level files that are standard across projects
    file=open('./' + dirname + '/' + dirname + '/__init__.py','a')
    file=open('./' + dirname + '/' + dirname + '/test/__init__.py','a')

    file.close()
else:
    print ("ERROR: Directory already exists.")

