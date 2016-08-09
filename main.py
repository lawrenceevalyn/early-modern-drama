# import libraries
import xml.etree.ElementTree as ET # imports my XML reading function
import os.path
import collections
import csv

# import my other code
from find_idno import find_idno
from stripNamespace import stripNamespace
from lemmacounter import lemmacounter

# make a mega-counter
c = collections.Counter()

# iterate through the directory
for filename in os.listdir("./test_corpus"):
# TODO: figure out why this won't run on the real corpus; fix it
# (it looks like there are some malformed files in the corpus --
# try printing the name of each file to spot the bad ones?
# figure out a "try catch" so the program will still run on the good ones?)
# things that might be the issue: 1. stripNamespaces has a problem? compare xmlstring before and after stripNamespaces (see if there's a function to look at the difference)
# 2. something broken with the XML where it doesn't have the idno or the sp or who knows

	# define the path to this file
	path = "./test_corpus/" + filename
		#TODO: don't forget to change the path here too

	# strip the file's namespace
	xmlstring = stripNamespace(path)
	
	# call find-idno.py to print the file's DLPS idno
	idno = find_idno(xmlstring)
	print idno

	# call lemmacounter.py to use a counter on the sp elements
	lemmacounts = lemmacounter(xmlstring)
	c += lemmacounts
	
with open('newfile.csv','w') as csvfile:
	fieldnames=['play DLPS','speaker','count']
	writer=csv.writer(csvfile)
	writer.writerow(fieldnames)
	for key, value in c.items():
		keydata = key.split('-') # makes an array of strings out of the key string
		rowdata = [keydata[0],keydata[1],value] # adds count value to array of strings
		writer.writerow(rowdata) 
	
	#TODO: further refine output of data based on research needs