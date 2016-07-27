# Pseudocode ahoy!

# TODO: How do I specify the corpus directory?
# I *definitely* don't want to load the whole corpus at once!

Create a new CSV file	# TODO: give it a distinctive name -- the date/time?
						# I'd rather have a lot of redundant duplicates, than overwrite

Loop: For each file in the directory,
# TODO: How do I handle the fact that some plays are split across multiple XML files?
# Probably write a separate program to run once before this one?
# Why were they split across multiple files?

	Create a new line in the CSV
	
	Print the TCP number of the play
				# relevant XML: <idno type="DLPS">A00456</idno>
	
	Get a list of the play's characters
				# relevant XML: 
	
	Create a variable for each character, named with their name, to store an integer
				# I think if I just name the integer value with their actual name,
				# I can keep the character name and the integer value associated.
	
	Loop: For each character in the play,
		
		Loop: For each speech in the play tagged with that character's name,
				
			Count the lemmas within that speech
				
			Add that number to the character's counting variable
				
	Order the characters by their integer words-spoken values
	
	Loop: For each character in that list
	
		Print their name
		
		Print their integer value
	
	# Now is when I would calculate whatever I am going to calculate, to capture
	# the dispersion / variance within the play
	
	Delete all the variable names?
				# Whatever I need to to, so it won't cause problems later
				# when characters repeat names.
				
	End the loop when it's out of files.
	
End the program when the loop stops.
		