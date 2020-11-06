import nltk
from nltk import sent_tokenize
from mediawiki import MediaWiki
from nltk import ne_chunk, pos_tag, word_tokenize

wikipedia = MediaWiki()

p = wikipedia.page('Bon Jovi')
content= p.content
#print(content)
#sent=content.sents()
sentences=sent_tokenize(content)
#print(sentences)

"""
To Tag Named Entities
1) Word Tokenize a Sentence
2) POS tag the tokens
3) print(nltk.ne_chunk(tagged))
"""

#print(sentences)
def ner(page):
    print(ne_chunk(pos_tag(word_tokenize(page))))

for s in sentences:
    ner(s)

#ne_chunk(pos_tag(word_tokenize(sentences)))

#4
#Calculate Precision, Recall, and F-Measure for Person
#For 56 sentences
def total(tp,fp,fn,tn):
    return tp+fp+fn+tn

def acc(tp,fp,fn,tn):
    return (tp+tn)/(tp+fp+fn+tn)

def pres(tp,fp,fn,tn):
    return tp/(tp+fp)

def rec(tp,fp,fn,tn):
    return tp/(tp+fn)


def f1(tp,fp,fn,tn):
    pre = tp / (tp + fp)
    re = tp / (tp + fn)
    return (2*(pre*re)/(re+pre))
print("Precision for first 56 sentences: ", pres(61,16,3,630))
print("Recall for first 56 sentences: ", rec(61,16,3,630))
print("F-Measure for first 56 sentences: ", f1(61,16,3,630))
