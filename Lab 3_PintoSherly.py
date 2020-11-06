#1 a
from nltk.corpus import brown

sent=len(brown.sents())
print('Number of sentences in the brown Corpus: ', sent)


words=len(brown.raw())
print('Number of words in the brown Corpus: ', words)

avg=words/sent
print('Average words/tokens per sentence:' ,avg)

#2
cat=brown.categories()
m=[]
m_dict={}
for c in cat:
    catsent=len(brown.sents(categories=c))
    m.append(catsent)
    #print(catsent)
    m_dict=dict.fromkeys(cat, m[0])
print('Maximum number of sentences in a category: ',max(m))
print('Minimum number of sentences in a category: ',min(m))

#3
#readlines
import os
filename='book.txt'
file=open(filename, 'r',  encoding='utf8')
text=file.read()
#nltk
from nltk import sent_tokenize
sentences=sent_tokenize(text)

print('The number of sentences in the book',len(sentences))
#readlines
count=0
lines=text.split("\n")
for l in lines:
    count+=1
print('The number of lines in the book',count)


