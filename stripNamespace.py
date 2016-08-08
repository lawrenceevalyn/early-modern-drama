# this makes the file into a string without its namespace (so it can be used elsewhere)

import re

def strip(path):
	# open the file and convert it to a string
	with open(path, 'r') as myfile:
		xmlstring=myfile.read()
    
		# use a regex!
		xmlstring = re.sub(' xmlns="[^"]+"', '', xmlstring, count=1)
		
	return xmlstring