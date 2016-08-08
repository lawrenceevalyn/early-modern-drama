import elementtree.ElementTree as ET

fp = open("practice.xml","r")	#fp stands for file pointer, r stands for read
tree = ET.parse(fp)
root = tree.getroot()

#idnos = root.findall('teiHeader')
# prints "teiHeader"

idnos = root.findall('.//idno') #find all five idnos!!!

#idnos = root.findall('/teiHeader/biblFull/publicationStmt/idno')

print idnos

#print len(idnos)

# for idno in idnos :
#	print "found idno"
	
	
	
# mydoc = ET(file='practice.xml')

#for e in mydoc.findall('/text'):
#    print len (e)
