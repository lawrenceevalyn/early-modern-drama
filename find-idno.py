# this is a function that takes in a file name and returns the idno as an object
# nowhere does it say that it takes in a string and returns a string; it just does

import elementtree.ElementTree as ET

def find-idno(filename):

	fp = open(filename,"r")	#fp stands for file pointer, r stands for read
	tree = ET.parse(fp)
	root = tree.getroot()

	#finds all five idnos!!! but searches whole biblFull
	idnos = root.findall('.//biblFull/publicationStmt/idno') 
	# also valid: root.findall('.//idno')
	# inexplicably not valid: root.findall('.//teiHeader/biblFull/publicationStmt/idno')

	# let's use a loop now because ElementTree can't use XPATH
	for idno in idnos :
		if idno.attrib.get('type') == 'DLPS' :
			print "found DLPS"
			break # this immediately ends the loop and grabs the current value as "idno"
	
		else :
			print "no DLPS"

	# returns the text of the idno element we're holding
	return idno.text

	# IT WORKS! IT WORKS!