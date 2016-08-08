# Get set up with the corpus

import xml.etree.ElementTree as ET # imports my XML reading function
from find-idno.py import find-idno


Create a CSV file outside the directory
#TODO: give it a distinctive name -- the date/time?


os.listdir("./corpus-xml") #Get a list of all the files in the directory
# https://stackoverflow.com/questions/3207219/how-to-list-all-files-of-a-directory-in-python
									
Loop: For each file in the directory,
#TODO: write a separate program to run once before this one, to concatenate the plays that are split across files
# It's easier / more efficient long-term to make sure the corpus is consistent, rather than making this program more complicated

# Get set up with the play

	
	Delete the file's namespace
	
	Create a new line in the CSV
	
	Print the TCP number of the play (followed by a comma)
	idno = find-idno(INPUTSTRINGGOESHERE)
		# calls find-idno.py to assign the file's DLPS idno to the string idno
				
# Find all the speakers within the play
	Make an array to store all the speaker's names as strings
	#TODO: is this the best way to store this info?
	
	Loop: for each <sp> tag in the file,
				
		Take the speaker's name from "who=" attribute
				# relevant XML: <sp xml:id="A00456-e101340" who="A00456-virginius">
				
		See if a string by that name already exists inside the array 
				
		If not, add it to the array

# Associate each character with their number of words spoken
	Loop: For each string in the array,
			
		Create an int variable named after that string
		# If I  name the integer variable with the character's actual name, I can keep the character name and the integer value associated for later.
		#TODO: What do I need to store the ints in, to order and then loop through them?
		# Do I want to pickle them?
		
		Loop: For each speech in the play tagged with that string,
				
			Count the lemmas within that speech
			#TODO: I assume it's possible to delimit the program based on the <sp></sp> XML tags (otherwise, what is the point of XML?), but how?
			# I could either count the appearance of the word "lemma" itself, or count instances of the <w></w> tag.
				
			Add that number to the int named for that string
				
	Order the ints by their values
	
	Loop: For each int,
	
		Print the int name (followed by a comma)
		# If I've done the rest right, this will be the speaker's name
		
		Print the int value (followed by a comma)
		
# Do statistics to the characters' words spoken? (value-add)	
	# Now is when I would calculate whatever I am going to calculate, to capture the dispersion / variance within the play.
	#TODO: What metrics should I calculate?
	
# Finish the play
	Delete the array of strings and all the ints
	#TODO: Whatever I need to to, so it won't cause confusion with later plays.
				
	End the loop when it's out of files.

# Finish the corpus	
End the program when the loop stops.

# For reference: the XML structure of speeches:
#	<sp xml:id="A00456-e101340" who="A00456-virginius">
#		<l xml:id="A00456-e101350">
#			<w lemma="ah" ana="#uh" xml:id="A00456-013110" facs="3-b-2340">Ah</w>
#		</l>
#	</sp>
		