#THis is for brown and inaugural

from nltk.corpus import brown
print('Number of categories in the brown corpus: ', len(brown.categories()))
#print(brown.raw())
print('Number of sentences in the brown Corpus: ',len(brown.sents()))
#print(brown.fileids())
print(brown.categories())
for c in brown.categories():
    print('Number of sentences in the brown Corpus ', c,  'adventure: ',len(brown.sents(categories=c)))


import nltk
from nltk.corpus import inaugural
#print(inaugural.categories())
#print(inaugural.raw())

import matplotlib as cfd
word1='america'
word2='constitution'
cfd = nltk.ConditionalFreqDist((target, fileid[:4])for fileid in inaugural.fileids()for w in inaugural.words(fileid)for target in [word1, word2] if w.lower().startswith(target))
cfd.plot()
