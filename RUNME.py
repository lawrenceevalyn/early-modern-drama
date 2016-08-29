# import libraries
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
import os.path
import collections
import csv

# import my other code
from find_idno import find_idno
from stripNamespace import stripNamespace
from lemmacounter import lemmacounter

# make a mega-counter to shove all the play counts in
megaCounter = collections.Counter()

#make a list for intermediate storage of counters
countersList = []

numfiles = 0
allLemmasCount = 0
directory = "corpus_xml"

# make listdir ignore .DS_store (and other hidden files)
def listdir_nohidden(path):
    for f in os.listdir(path):
        if not f.startswith('.'):
            yield f

# iterate through the directory
for filename in listdir_nohidden("./" + directory):
# TODO: figure out why this won't run on the real corpus; fix it
# things that might be the issue: 1. stripNamespaces has a problem? compare xmlstring
# before and after stripNamespaces (see if there's a function to look at the difference)
# 2. something broken with the XML where it doesn't have the idno or the sp or who knows

	# define the path to this file
	path = "./" + directory + "/" + filename

	# strip the file's namespace
	try:
		xmlstring = stripNamespace(path)
	except:
		print "error stripping namespace of file %s" % (filename)
	
	# call find-idno.py to print the file's DLPS idno
	try:
		idno = find_idno(xmlstring)
		print idno
	except:
		print "error finding IDNO with file %s" % (filename)

	# call lemmacounter.py to use a counter on the w elements
	try:
		lemmacounts = lemmacounter(xmlstring)
		countersList.append(lemmacounts)
		numkeys = len(lemmacounts.keys())
		print numkeys
		allLemmasCount += numkeys	
	except:
		print "error counting lemmas of file %s" % (filename)
		
	# increment a counter to see how many I read
	numfiles += 1

print "I read %d files" % (numfiles)
print "total number of keys in list: %d" % (allLemmasCount)

#TODO: merge counters of plays with the same title (but NOT the same idno)

for counter in countersList:
#	print counter
	megaCounter += counter

print "total number of keys in megaCounter: %d" % (len(megaCounter.keys()))

newfilename = "output_%s.csv" % (directory)
with open(newfilename,'w') as csvfile:
	fieldnames=['tcp','speaker','count']
	writer=csv.writer(csvfile)
	writer.writerow(fieldnames)
	for key, value in megaCounter.items():
		keydata = key.split('-', 1)
		if len(keydata) != 2 :
			print "oooops! bad keydata: %r" % (keydata)
		rowdata = [keydata[0],keydata[1],value]
		writer.writerow(rowdata) 
	
	#TODO: further refine output of data based on research needs