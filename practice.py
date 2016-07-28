# This program is just for trying out operations before they're added to lemmacounter.py

import xml.sax
from xml.sax import make_parser
from xml.sax import handler
from xml.sax.handler import feature_namespaces

# Define your specialized handler classes

class FindIssue(xml.sax.ContentHandler):
    def __init__(self, title, number):
        self.search_title, self.search_number = title, number
        
    def startElement(self, name, attrs):
        # If it's not a comic element, ignore it
        if name != 'comic': return

        # Look for the title and number attributes (see text)
        title = attrs.get('title', None)
        number = attrs.get('number', None)
        if (title == self.search_title and 
	    number == self.search_number):
            print title, '#' + str(number), 'found'

# Create an instance of the handler classes
dh = FindIssue('Sandman', '62')

if __name__ == '__main__':

	# Create an XML parser
	parser = make_parser()
	
	# Tell the parser we are not interested in XML namespaces (but why??)
	parser.setFeature(feature_namespaces, 0)

	# Tell the parser to use your handler instance
	parser.setContentHandler(dh)

	# Parse the file; your handler's methods will get called
	parser.parse(open('comic.xml'))


# reference: the line of XML that has what I want:
# <idno type="DLPS">A00456</idno>