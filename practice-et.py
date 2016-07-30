import xml.etree.ElementTree as ET
tree = ET.parse('practice.xml')
root = tree.getroot()

for idno in root.findall('idno'):
	print "idno"
	# doesn't print anything at all

for sp in root:
	print "sp"
	# prints "sp" twice, which is correct, but possibly accidental?