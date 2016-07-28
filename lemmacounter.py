# Pseudocode ahoy!

# Get set up with the corpus

Open the directory
#TODO: How do I specify the corpus directory?
# I *definitely* don't want to load the whole corpus at once!

Create a CSV file somewhere else
#TODO: give it a distinctive name -- the date/time?
									
Loop: For each file in the directory,
#TODO: How do I handle the fact that some plays are split across multiple XML files?
# Probably write a separate program to run once before this one?
# Why were they split across multiple files?

# Get set up with the play

	Create a new line in the CSV
	
	Print the TCP number of the play (followed by a comma)
				# relevant XML: <idno type="DLPS">A00456</idno>
				# "A00456" is what I want
				
# Find all the speakers within the play
	Make an array to store all the speaker's names as strings
	#TODO: is this the best way to store this info?
	
	Loop: for each <speaker> tag in the file,
	#TODO: this will be really inefficient. Do I care?
				
		Take the speaker's name from the lemma
				# relevant XML: <speaker><w lemma="Virginius"></w></speaker>
				# the lemmas will be human-standardized, so I want those, not the <w>
				
		See if a string by that name already exists inside the array 
				
		If not, add it to the array

# Associate each character with their number of words spoken
	Loop: For each string in the array,
			
		Create an int with the name of that string
		# If I  name the integer value with the character's actual name,
		# I can keep the character name and the integer value associated for later.
		#TODO: What do I need to store the ints in, to order and then loop through them?
		# Do I want to pickle them?
		
		Loop: For each speech in the play tagged with that string,
				
			Count the lemmas within that speech
				
			Add that number to the int named for that string
				
	Order the ints by their values
	
	Loop: For each int,
	
		Print the int name (should be character's name) (followed by a comma)
		
		Print the integer value (followed by a comma)
		
# Do statistics to the characters' words spoken? (value-add)	
	# Now is when I would calculate whatever I am going to calculate, to capture
	# the dispersion / variance within the play.
	#TODO: What metrics should I calculate?
	
# Finish the play
	Delete the array of strings and all the ints
	#TODO: Whatever I need to to, so it won't cause confusion with later plays.
				
	End the loop when it's out of files.

# Finish the corpus	
End the program when the loop stops.

# For reference: the XML structure of speeches:
#	<sp xml:id="A00456-e101340" who="A00456-virginius">
#		<speaker>
#			<w lemma="Virginius" ana="#n1-nn" xml:id="A00456-013080" 
#			facs="3-b-2320">Virginius</w>
#			<pc xml:id="A00456-013090" unit="sentence" facs="3-b-2330">.</pc>
#		</speaker>
#		<l xml:id="A00456-e101350">
#			<w lemma="ah" ana="#uh" xml:id="A00456-013110" facs="3-b-2340">Ah</w>
#		</l>
#	</sp>
		