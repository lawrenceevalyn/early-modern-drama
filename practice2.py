import xml.etree.ElementTree as ET
tree = ET.parse('practice.xml')
root = tree.getroot()

for comic in root:
	print "comic"