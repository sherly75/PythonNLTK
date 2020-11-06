from textblob import TextBlob
from mediawiki import MediaWiki
wikipedia = MediaWiki()

#Wikipedia pages

p1 = wikipedia.page('Barack Obama')
content= p1.content
politics=content
tb1=TextBlob(politics)
print('Polarity for Barack Obama (Politics)',tb1.sentiment.polarity)

p2 = wikipedia.page('French Revolution')
content= p2.content
history=content
tb2=TextBlob(history)
print('Polarity for French Revolution (History)',tb2.sentiment.polarity)


p3 = wikipedia.page('Black hole')
content= p3.content
science=content
tb3=TextBlob(science)
print('Polarity for Black hole (Science)',tb3.sentiment.polarity)


p4 = wikipedia.page('Taylor Swift')
content= p4.content
celebrity=content
tb4=TextBlob(celebrity)
print('Polarity for Taylor Swift (celebrity)',tb4.sentiment.polarity)

p5 = wikipedia.page('Counter-Strike')
content= p5.content
games=content
tb5=TextBlob(games)
print('Polarity for Counter-Strike (games)',tb5.sentiment.polarity)

#Trying on random sentences
positivetext1="I am very happy and I think everyone should enjoy life and it is beautiful"
pos1=TextBlob(positivetext1)
print('Polarity for the sentence is',pos1.sentiment.polarity)

positivetext2="Because I am glad you came! It is exciting to see such gorgeous faces."
pos2=TextBlob(positivetext2)
print('Polarity for the sentence is',pos2.sentiment.polarity)

positivetext3="The sun is shinning bright and I am excited to go out and have fun."
pos3=TextBlob(positivetext3)
print('Polarity for the sentence is',pos3.sentiment.polarity)

#negative sentences
negativetext1="I want to be alone! Stay away!"
neg1=TextBlob(negativetext1)
print('Polarity for the sentence is',neg1.sentiment.polarity)

negativetext2="That is disgusting! I hope you are not wearing that, eww."
neg2=TextBlob(negativetext2)
print('Polarity for the sentence is',neg2.sentiment.polarity)

negativetext3="I hate you."
neg3=TextBlob(negativetext3)
print('Polarity for the sentence is',neg3.sentiment.polarity)

#I believe, to find polarity it looks for keywords like "hate," "not," "go away!" and "eww" to refer it as negative
# It looks for words like "love," "happy," "excited," and "like" to refer it as positive