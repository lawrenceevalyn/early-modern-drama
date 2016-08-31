# As the name suggests, this is the main program that you need to run
# It will 'call' the other sub-programs as needed

# import libraries
try:
    import xml.etree.cElementTree as ET     # this makes it faster
except ImportError:
    import xml.etree.ElementTree as ET
import os.path
import collections
import csv
import operator

# import my other code
from find_idno import find_idno
from stripNamespace import stripNamespace
from lemmacounter import lemmacounter

# things to store stuff in
megaCounter = collections.Counter() #a counter object hash table
countersList = [] #a list of counter objects
threeples = [] #megaCounter converted to tuples (with 3 things) by tokenizing 

#initiate variables
numfiles = 0
allLemmasCount = 0
directory = "corpus"

# make listdir ignore .DS_store (and other hidden files)
def listdir_nohidden(path):
    for f in os.listdir(path):
        if not f.startswith('.'):
            yield f

# iterate through the directory
for filename in listdir_nohidden("./" + directory):

	# define the path to this file
	path = "./" + directory + "/" + filename

	# strip the file's namespace
	try:
		xmlstring = stripNamespace(path)
	except:
		print "error stripping namespace of file %s" % (filename)
	
	# call find-idno.py to print the file's TCP number
	# this is just so you can tell that the program's running,
	# and possibly see how far it got before it crashed (in case of problems)
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

# print some stuff so you know what's going on
print "I read %d files" % (numfiles)
print "total number of keys in list: %d" % (allLemmasCount)

#TODO: merge counters of plays if they have the same idno AND title?

for counter in countersList:
#	print counter
	megaCounter += counter

# compare this to the total number of keys in list to make sure they all made it
print "total number of keys in megaCounter: %d" % (len(megaCounter.keys()))

# time to start writing this stuff to the CSV!
newfilename = "output_%s.csv" % (directory)
with open(newfilename,'w') as csvfile:
	fieldnames=['tcp','speaker','count'] # names the first 3 columns of the CSV
	writer=csv.writer(csvfile)
	writer.writerow(fieldnames)
	
	# go through all the TCPspeaker-count pairs
	for key, value in megaCounter.items():
		if key is None:
			print "why is there nothing here"
			# this means that somehow you have a number without a speaker
			# you need to fix this in the XML but you have no information
			# I'm sorry
		else:
			# split the TCP number from the speaker's name
			keydata = key.split('-', 1)
			# make sure we split it right
			if len(keydata) != 2 :
				print "oooops! malformed XML for speaker: %r" % (keydata)
				# this means the XML didn't follow the format of TCP-speaker
				# usually it's because the who= element doesn't have the TCP
				# you need to fix the XML based on the speaker name
			# if it split properly, carry on with storing the play, speaker, and count
			else:
				rowdata = [keydata[0].encode('utf-8'),keydata[1].encode('utf-8'),value]
				threeples.append(rowdata)
	
	# declares some variables we're gonna need to organize this stuff
	sortedthreeples = sorted(threeples, key=operator.itemgetter(0, 2), reverse=True)
	sortedLongples = [] #empty list
	longple = () #empty tuple
	i = 0
	prevPlay = ''
	
	# loop through the TCP-speaker-count data
	# write each triple down in the right place
	# the goal here is to have one row per play
	while i < len(sortedthreeples):
		[play,speaker,count] = sortedthreeples[i]
		if play == prevPlay:
			# keep appending to our long tuple
			longple += (speaker, count)
		elif prevPlay == '':
			# we found the first play! store its info
			longple = (play, speaker, count)
		else:
			# write the old one
			writer.writerow(longple)
			# make a new one
			longple = (play, speaker, count)
		prevPlay = play
		i += 1
	writer.writerow(longple) # need to write the last one