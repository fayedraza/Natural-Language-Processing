from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

#purpose of this program was to introduce stemming
ps =  PorterStemmer()

example_words = ["python","pythoner","pythoning","pythoned","pythonly"]

##for w in example_words:
  ##  print(ps.stem(w))

new_text = "It is very important to be pythonly when are you pythoning with python."

words = word_tokenize(new_text)

for w in words:
    print(ps.stem(w))