#Sherly Pinto
import nltk

from nltk.corpus import brown
brown_tagged_sents = brown.tagged_sents(categories='news')

size = int(len(brown_tagged_sents) * 0.9)

train_sents = brown_tagged_sents[:size]
test_sents = brown_tagged_sents[size:]

#train the tagger
unigram_tagger = nltk.UnigramTagger(train_sents)

#calculate the accuracy

print("Results on test set {0}".format(unigram_tagger.evaluate(test_sents)))
print("Results on train set {0}".format(unigram_tagger.evaluate(train_sents)))

#1) Why is the training accuracy higher than the testing accuracy?

"""
The training accuracy is much higher because of the line:
unigram_tagger = nltk.UnigramTagger(train_sents) (Line 12)
The unigram is using "train" as the model to verify if the "test" works accurately.
Since we are using "train" as the model, "test" cannot be more accurate than "train"
"""
#2) Why is the training accuracy not perfect (100%)
"""
For English, the reason for lesser than 100% is ambiguity.
No matter what, accuracy can never reach 100% It will, at maximum, lie very close to 90%

If the model fails, it may consider the token a NN which may not be true.
Even if "train" becomes 100% accurate, while using it on "test" the model may fail 
since "train"=/="test

Also, the higher complexity of the sentences pushes the accuracy to lesser than 100%

"""

def_tagger= nltk.DefaultTagger("NN")
uni_tagger=  nltk.UnigramTagger(train_sents, backoff=def_tagger)
print("\n")
print("Results on train set {0}".format(uni_tagger.evaluate(train_sents)))
print("Results on test set {0}".format(uni_tagger.evaluate(test_sents)))

"""
Backoff model uses a simpler model only when the current model fails or crashes.
For a unigram, the backoff would be NN (noun)
"""
#3 Why does the accuracy score on the training data not go up but it does on the test data?
"""
"Train" is the set that we use for training the n-gram tagger to use on "Test".
Since, the machine is learning from "train", 
it is not testing the accuracy on "train" because it is fixed.
The uni-tagger is used on "Test" by learning from "train"

"Test" changes because of backoff. instead of using uni-gram it is now guessing (mostly as NN).

"""
#4 Create two new taggers, A BigramTagger that has not backoff and a BigramTagger that user a unigram tagger as backoff.
# Report the accuracies. Why is one so much lower than the other?
bigram_tagger = nltk.BigramTagger(train_sents)

print("\n")

print("Results on (Bi) test set {0}".format(bigram_tagger.evaluate(test_sents)))
print("Results on (Bi) train set {0}".format(bigram_tagger.evaluate(train_sents)))

def1_tagger= nltk.UnigramTagger(train_sents)
bigram_tagger=  nltk.BigramTagger(train_sents, backoff=def1_tagger)

print("\n")
print("Results on (Bi-backoff) train set {0}".format(bigram_tagger.evaluate(train_sents)))
print("Results on (Bi-backoff) test set {0}".format(bigram_tagger.evaluate(test_sents)))

# Report the accuracies. Why is one so much lower than the other?

"""
Accuracies before back-off on Bigram:
Test: 0.102
Train: 0.788

Accuracies after back-off on Bigram: (Unigram)
Train: 0.974
Test: 0.821

The accuracy of test is significantly lower because by just using bigram, sometimes certain words may rarely appear next to each other
Some oxymorons are not expected to always be next to each other
Hence using only Bigram model fails.
The higher we go with the n in n-gram model, the less accurate the prediction will be.
By using back-off, we provide scope for unresolved words by using the unigram or the dictionary. Hence accuracy increases.
"""
#5 Repeat #4 with a TrigramTagger using a Bigramtagger as backoff
trigram_tagger = nltk.TrigramTagger(train_sents)

print("\n")

print("Results on (Tri) test set {0}".format(trigram_tagger.evaluate(test_sents)))
print("Results on (Tri) train set {0}".format(trigram_tagger.evaluate(train_sents)))

def2_tagger= nltk.BigramTagger(train_sents)
trigram_tagger=  nltk.BigramTagger(train_sents, backoff=def2_tagger)

print("\n")
print("Results on (Tri-backoff) train set {0}".format(trigram_tagger.evaluate(train_sents)))
print("Results on (Tri-backoff) test set {0}".format(trigram_tagger.evaluate(test_sents)))

"""
The higher we go with the n in n-gram model, the less accurate the prediction will be.
Hence it gets less accurate with tri-gram since 3>2>1.
By using back-off, we provide scope for unresolved words by using the bigram. Hence accuracy increases.

"""

