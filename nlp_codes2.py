#REMOVE PUNCTUATION

import string
def remove_punctuation(text):
    return text.translate(str.maketrans('','',string.punctuation))
text = "helloo, world!! let's remove ;the;punctuation."
clean_text=remove_punctuation(text)
print(clean_text)

#BAG OF WORDS

from sklearn.feature_extraction.text import CountVectorizer
documents = [
"I love programming in python",
"python is great for datascience",
"I love learning new programming languages also "
]
vectorizer = CountVectorizer()
x = vectorizer.fit_transform(documents)
feature_names = vectorizer.get_feature_names_out()
print("Feature names:",feature_names)
print("Bag of words model:\n",x.toarray())

#N GRAM

def n_grams(text,n):
    words=text.split()
    return[tuple(words[i:i+n]) for i in range (len(words)-n+1)]

text = " I love programming python"
n =2
print(n_grams(text,n))
