import collections
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

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
#			print l.tag, l.attrib
			words = l.findall('w')
			for w in words:
				c[speaker]+=1
	
		linegroups = sp.findall('lg')
		for lg in linegroups:
#			print lg.tag, lg.attrib
			lines = lg.findall('l')
			for l in lines:
#				print l.tag, l.attrib
				words = l.findall('w')
				for w in words:
					c[speaker]+=1

		paragraphs = sp.findall('p')
		for p in paragraphs:
#			print "found a paragraph"
			words = p.findall('w')
			for w in words:
				c[speaker]+=1

	return c