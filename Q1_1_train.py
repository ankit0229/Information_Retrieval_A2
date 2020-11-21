import pickle
import os
import re
import string
import pdb
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import WordNetLemmatizer
from collections import Counter
Picklefile1 = open('doc_titles', 'rb')
dict_titles_doc = pickle.load(Picklefile1)

dict_doc_title_tokens = {}
dict_title_counts = {}
for ad in dict_titles_doc:
    text = dict_titles_doc[ad]
    text = text.lower()
    text = re.sub(r'\S+@\S+', '', text)
    text = re.sub(r'[a-zA-Z]+[0-9]+', '', text)
    text = re.sub(r'[0-9]+[a-zA-Z]+', '', text)
    translator = str.maketrans(string.punctuation, ' ' * len(string.punctuation))  # map punctuation to space
    text = text.translate(translator)
    title_tokens = word_tokenize(text)
    dict_doc_title_tokens[ad] = title_tokens
    counter_tokens = Counter(title_tokens)
    dict_title_counts[ad] = counter_tokens

print(len(dict_doc_title_tokens))
print(len(dict_title_counts))
mstr_dict = {}
list_docs = dict_titles_doc.keys()
xyz = 1
directory = r'D:\M.TECH SEM 2\IR\Assignments\A2\stories\\'
for doc_name in list_docs:
    list_title_tokens = dict_doc_title_tokens[doc_name]
    doc_path = os.path.join(directory, doc_name)
    fp = open(doc_path, "r", errors='ignore')
    text = fp.read()
    fp.close()
    text = text.lower()
    text = re.sub(r'\S+@\S+', '', text)
    text = re.sub(r'[a-zA-Z]+[0-9]+', '', text)
    text = re.sub(r'[0-9]+[a-zA-Z]+', '', text)
    translator = str.maketrans(string.punctuation, ' ' * len(string.punctuation))  # map punctuation to space
    text = text.translate(translator)
    word_tokens = word_tokenize(text)
    counter_word_counts = Counter(word_tokens)
    for k in list_title_tokens:
        if counter_word_counts[k] != 0:
            counter_word_counts[k] = counter_word_counts[k] - 1
    mstr_dict[doc_name] = counter_word_counts

print(len(mstr_dict))

# Adding changes for without title
mstr_dict_without = {}
list_docs = dict_titles_doc.keys()
xyz = 1
directory = r'D:\M.TECH SEM 2\IR\Assignments\A2\stories\\'
for doc_name in list_docs:
    doc_path = os.path.join(directory, doc_name)
    fp = open(doc_path, "r", errors='ignore')
    text = fp.read()
    fp.close()
    text = text.lower()
    text = re.sub(r'\S+@\S+', '', text)
    text = re.sub(r'[a-zA-Z]+[0-9]+', '', text)
    text = re.sub(r'[0-9]+[a-zA-Z]+', '', text)
    translator = str.maketrans(string.punctuation, ' ' * len(string.punctuation))  # map punctuation to space
    text = text.translate(translator)
    word_tokens = word_tokenize(text)
    counter_word_counts = Counter(word_tokens)
    mstr_dict_without[doc_name] = counter_word_counts

print("$$$")
print(len(mstr_dict_without))
Picklefile2 = open('all_doc_counts', 'wb')
pickle.dump(mstr_dict, Picklefile2)
Picklefile2.close()

Picklefile7 = open('title_counts', 'wb')
pickle.dump(dict_title_counts, Picklefile7)
Picklefile7.close()

Picklefile18 = open('dict_without_mstr', 'wb')
pickle.dump(mstr_dict_without, Picklefile18)
Picklefile18.close()