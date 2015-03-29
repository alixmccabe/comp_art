from pattern.web import *

def data_search_google(query):
		
	g = Google()
	for result in g.search('Olin College'):
	    print result.url
	    print result.text # print plaintext(result.text) will give you results without HTML

#data_search_google('olin college')

def title_search_wiki(subject):

	w = Wikipedia()
	for article_title in w.index():
		print str(w.index[article_title])
	    if str(article_tile).find(subject, beg=0, end=len(article_tile)):
			print article_title
		


title_search_wiki('Destroy')

def data_search_wiki(title):

	#title = title_search_wiki(subject)

	w = Wikipedia()
	article = w.search(title)
	print article.sections

#data_search_wiki('Olin College')

def twitter():

	s = Twitter().stream('#fail')
	for i in range(10):
	    time.sleep(1)
	    s.update(bytes=1024)
	    print s[-1].text if s else ''

def twitter_trending():
	print Twitter().trends()

