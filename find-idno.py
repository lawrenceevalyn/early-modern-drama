import elementtree.ElementTree as ET

fp = open("practice.xml","r")	#fp stands for file pointer, r stands for read
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

# prints the text of the idno element we're holding
print idno.text

# IT WORKS! IT WORKS!