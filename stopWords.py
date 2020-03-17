from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# purpose of this program is to make a set of words and filters the words

#makes a set of all of the words in the language suggested
example_sentence = "This is an example showing off stop word filtiration."
stop_words = set(stopwords.words("english"))

words = word_tokenize(example_sentence)

filtered_setence = []

##for w in words: #used to print the words that we want
 ##   if w not in stop_words:
   ##     filtered_setence.append(w)

filtered_setence = [w for w in words if not w in stop_words]      
print(filtered_setence)  