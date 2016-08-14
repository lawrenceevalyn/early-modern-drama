import collections
import elementtree.ElementTree as ET

def lemmacounter(xmlstring):
	
	root = ET.fromstring(xmlstring)
	
	c = collections.Counter()
	
	# find all our speech acts
	# we're using the counter so we don't have to know all the speakers before we start
	speeches = root.findall('.//sp')
	
	for sp in speeches:
		speaker = sp.attrib.get('who')
		lines = sp.findall('l')
		for l in lines:
			words = l.findall('w')
			for w in words:
				c[speaker]+=1
	
	return c