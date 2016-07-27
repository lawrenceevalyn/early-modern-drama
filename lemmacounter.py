# For now, I'm just trying to get some pseudocode down, to figure out what I need to figure out.

Create a new CSV file

# First just get the plays and characters' word counts down

Loop: For each file in the corpus

	Create a new line in the CSV
	
	Print the TCP number of the play
	
	Get a list of the play's characters?
	
	Loop: For each character in the play
	
		Print the character's name
		
		Create a variable to start counting how many words they say?
		
			Loop: For each speech in the play tagged with that character's name
				
				Count the lemmas within that speech
				
				Add that number to the character's counting variable
				
		Print the character's total words spoken
		
# How can I rearrange the characters in order of most lines to fewest?

# 