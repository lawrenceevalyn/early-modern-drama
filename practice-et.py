import xml.etree.ElementTree as ET
tree = ET.parse('practice.xml')
root = tree.getroot()

for idno in root:
	print "idno"

for sp in root:
	print "sp"