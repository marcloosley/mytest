import sys

# Function to look up the counts for a list of words
# Does not return anything, just prints out the counts
def compareCounts(d, words):
  for word in words:
    if word in d:
      print(word + " " + str(d[word]))
    else:
      print(word + " 0")

	  
# removePunctuation takes a string parameter and returns
# a copy of the string with the punctuation removed	  
def removePunctuation(text):
	newtext = ""
	newtext = text.translate(None,'?!:,."-()\n') #str.translate(table[, deletechars])
	return newtext 

# Writes out the word frequencies to a file.
def writefrequentWords(d, filename):
  wordcounts = []
  for w in d.keys():
    wordcounts.append ((d[w],w))

  wordcounts.sort(reverse=True)

  outfile = open(filename,"w")
  for (c,w) in wordcounts:
    outfile.write(str(c) +  " " +w + "\n")
    outfile.close

	
	
	
def readHansard(d, filename):
	#open the file
	readfile = open(filename)
	#readfile =  removePunctuation(readfile)
	
	for line in readfile:
		line = line.strip()
		if line != "":
			nopunc = removePunctuation(line)
			words = nopunc.split()
		for word in words:
			lword = word.lower()
			if lword in d:
				d[lword] += 1
			else:
				d[lword] = 1
	readfile.close()



def test():          
  # Make a new dictionary
  wordDict = {}
  # Read in the text
  readHansard(wordDict, "PMQs_221014.txt")

  # Lets compare some words.

  print("Are they referring to gentlemen or ladies?")
  compareCounts(wordDict,["gentleman","lady"])
  
  print("Who asks the questions?")
  compareCounts(wordDict,["con","lab","ld","ukip"])
  
  print("What countries are they talking about?")
  compareCounts(wordDict,["scotland","england","wales"])
  
  print("Who are they talking about?")
  compareCounts(wordDict,["i","we","you","they"])

  # Write the word frequencies to file
  writefrequentWords(wordDict, "hansout.txt")



if __name__ == "__main__":
  test()






