# Pseudocode ahoy!

# Get set up with the corpus

Open the directory?
	#TODO: How do I specify the corpus directory?
	# I *definitely* don't want to load the whole corpus at once!

Create a CSV file somewhere else	#TODO: give it a distinctive name -- the date/time?
									
Loop: For each file in the directory,
	#TODO: How do I handle the fact that some plays are split across multiple XML files?
	# Probably write a separate program to run once before this one?
	# Why were they split across multiple files?

# Get set up with the play

	Create a new line in the CSV
	
	Print the TCP number of the play (followed by a comma)
				# relevant XML: <idno type="DLPS">A00456</idno>
				
# Find all the characters within the play
	Loop: for each <speaker> tag,
				
		Identify the speaker's name
					# relevant XML: <speaker><w lemma="Virginius"></w></speaker>
				
		See if that string already exists inside the array 
				
		If not, add it to the array

# Associate each character with their number of words spoken
	Loop: For each string in the array,
			
		Create an int with the name of that string and add it to an array
			# I think if I just name the integer value with the character's actual name,
			# I can keep the character name and the integer value associated for later?
		
		Loop: For each speech in the play tagged with that string,
				
			Count the lemmas within that speech
				
			Add that number to the int named for that string
				
	Order the ints within the array by their values
	#TODO: Can I store ints in an array too...?
	
	Loop: For each int in the array
	
		Print the int name (should be character's name) (followed by a comma)
		
		Print the integer value (followed by a comma)
		
# Do statistics to the characters' words spoken? (value-add)	
	# Now is when I would calculate whatever I am going to calculate, to capture
	# the dispersion / variance within the play.
	#TODO: What metrics should I calculate?
	
# Finish the play
	Delete all the variable names?
				# Whatever I need to to, so it won't cause problems later
				# when characters repeat names.
				
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
		