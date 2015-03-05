""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg """

import string

def get_word_list(file_name):
	""" Reads the specified project Gutenberg book.  Header comments,
		punctuation, and whitespace are stripped away.  The function
		returns a list of the words used in the book as a list.
		All words are converted to lower case.
	"""
	f = open(file_name,'r')
    	lines_in_text = f.readlines()
    	print lines_in_text
    	lines = list(str(lines_in_text).split())
    
    #to keep track of the line index while using the list of lines
	curr_line = 0

	while lines_in_text[curr_line].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
	    curr_line += 1

	lines = lines[curr_line+1:]
	
	#this for loop strips out all of the whitespace, punctuation, and uppercase letters for the document!
	#it yields a single list for all of the words in the document
	for i in range(len(lines)):
		lines[i] = lines[i].translate(string.maketrans("",""), string.whitespace)
		lines[i] = lines[i].translate(string.maketrans("",""), string.punctuation)
		lines[i] = lines[i].lower()

	#new_lines is a new, empty list that takes all of the values of "lines" that aren't 'n'
	#we need this, because when the whitespace is stripped out, it leaves a null value 'n' in the list
	#this would definitely throw off our word frequency count, so we needed to delete these null values!
	new_lines = [ ]

	#this for loop removes all of the 'n's!
	for i in range(len(lines)):
		if lines[i] != 'n':
			new_lines += [lines[i]]
	
	#the "new_lines" list is a list of all of the words in the document with no capital letters, no whitespace, and no punctuation!
	return new_lines

def get_top_n_words(word_list, n):
	""" Takes a list of words as input and returns a list of the n most frequently
		occurring words ordered from most to least frequently occurring.

		word_list: a list of words (assumed to all be in lower case with no
					punctuation
		n: the number of words to return
		returns: a list of n most frequently occurring words ordered from most
				 frequently to least frequentlyoccurring
	"""

	#with python's built-in "counter" function, it's pretty easy to create a dictionary of all 
	#of the items in a list ordered from most frequent to least frequent!
	from collections import Counter
	order = Counter(word_list)
	#"order" is now a list of all of the words in "word_list" from most to least frequent

	#we process this new dictionary with the following code:
	ordered_by_frequency = sorted(order, key=order.get, reverse=True)
	return ordered_by_frequency[0:n]
	#we return the first "n" indexes of this list according to how many of the most frequent words we want!
	#in this case we want the 100 most frequent words, so n==100


print get_top_n_words(get_word_list("Wizard_of_Oz.txt"),100)