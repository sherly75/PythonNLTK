#This is for my corpus (indian)

import nltk
from nltk.corpus import indian
import matplotlib as cdf

print(indian.raw())
print(indian.fileids())
print(indian.sents())

import matplotlib

word1='country'
word2='city'
cfd = nltk.ConditionalFreqDist((target, fileid[:4])for fileid in indian.fileids()for w in indian.words(fileid)for target in [word1, word2] if w.lower().startswith(target))
cfd.plot()
