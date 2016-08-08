# import libraries
import xml.etree.ElementTree as ET # imports my XML reading function
import os.path

# import my other code
from find_idno import find_idno
from stripNamespace import strip

# iterate through the directory
for filename in os.listdir("./test_corpus"):

	# define the path to this file
	path = "./test_corpus/" + filename

	# strip the file's namespace
	xmlstring = strip(path)
	
	# call find-idno.py to assign the file's DLPS idno to the string idno
	idno = find_idno(xmlstring)
	print idno

	# call lemmacounter.py to count lemmas