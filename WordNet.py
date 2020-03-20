from nltk.corpus import wordnet

#introducing useful functions such as finding synonyms and antonyms
syns = wordnet.synsets("program")

#syn set
print(syns[0].name())

#just the word
print(syns[0].lemmas() [0].name())

#defintion
print(syns[0].definition())

#examples
print(syns[0].examples())

synonyms = []
antonynms=[]

for syn in wordnet.synsets("good"):
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonynms.append(l.antonyms() [0].name())

print(set(synonyms))     
print(set(antonynms))

