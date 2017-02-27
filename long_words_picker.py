# This program will pick only words with length more than 5 letters

my_words = ['blog', 'Treehouse', 'Python', 'hi']

def long_words(lst):
	words = []
	for word in lst:
		if len(word) > 5:
			words.append(word)
	return words 
my_words = long_words(my_words)
print my_words