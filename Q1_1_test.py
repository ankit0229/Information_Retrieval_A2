import pickle
import os
import re
import string
import sys
import pdb
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import WordNetLemmatizer
from collections import Counter

Picklefile1 = open('doc_titles', 'rb')
dict_titles_doc = pickle.load(Picklefile1)

Picklefile18 = open('dict_without_mstr', 'rb')
mstr_dict_without = pickle.load(Picklefile18)

# print("Enter the query:")
# query = input()
# print("Enter the value of k: ")
# k = int(input())
list_args = sys.argv
query = list_args[1]
k = int(list_args[2])
query = query.lower()
query = re.sub(r'\S+@\S+', '', query)
query = re.sub(r'[a-zA-Z]+[0-9]+', '', query)
query = re.sub(r'[0-9]+[a-zA-Z]+', '', query)
translator = str.maketrans(string.punctuation, ' ' * len(string.punctuation))  # map punctuation to space
query = query.translate(translator)
query_tokens = word_tokenize(query)

list_scores = []
for doc in mstr_dict_without:
    dict_curr_doc = mstr_dict_without[doc]
    num = 0
    for q in query_tokens:
        if dict_curr_doc[q] != 0:
            num += 1
    list_combined = []
    list_combined.extend(dict_curr_doc.keys())
    list_combined.extend(query_tokens)
    dict_union = Counter(list_combined)
    den = len(dict_union)
    jaccard_score = num / den
    pair = [doc, jaccard_score]
    list_scores.append(pair)

#print(len(list_scores))
list_scores.sort(key = lambda x : x[1], reverse = True)
list_top_docs = []
for j in range(k):
    list_top_docs.append(list_scores[j][0])

print(list_top_docs)
print("The top k documents are: ")
for j in list_top_docs:
    print(dict_titles_doc[j])