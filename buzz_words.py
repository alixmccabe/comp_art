"""This is a dictionary of facebook terms that I do not want to appear 
in any of the posts I pull from facebook

these terms are profile picture updates, shared links, etc. and indicate that 
the post does not reflect the user's subjectivity
"""
index = ['0','1','2','3','4','5']

words = [['cover photo'],['shared'],['timeline'],['profile picture'],['life event'],['became friends']]


buzz_words = {}

for i in range(len(index)):
    for word in words[i]:
        buzz_words[word] = index[i]

for word in buzz_words:
	print buzz_words

"""
def search_for_status():

	This function searches the newsfeed that we just found for relevant statuses
	it excludes facebook-generated posts such as profile picture changes and life events

	buzz_words = ['cover photo','shared','timeline','profile picture','life event','became friends','going to an event']

	f = open("text_author.pickle",'r')
	lines_in_text = f.readlines()
	print lines_in_text

	status = []

	i = 0

	for line in lines_in_text:
		print line
		print line [for word in buzz_words if word in line]

		else:
			if len(line)>=8:
				status += line
				print status

print search_for_status()
"""
