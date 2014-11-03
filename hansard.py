

def removePunctuation(text):
	newtext = ""
	newtext = text.translate(None, '?!:,."-()') #str.translate(table[, deletechars])
	print 

def readHansard(d, filename):
	#open the file
	readfile = open('PMQs_221014.txt')
	
	#each line should strip off any newline characters, remove punctuation then split the line on spaces into a list of words.
	#use for loop to conert each word to lower case, add each word as a key into the dictionary.
	#if the word is already present increment the value by 1.
	#close the file
	#purpose is to modify the dict, check the 
