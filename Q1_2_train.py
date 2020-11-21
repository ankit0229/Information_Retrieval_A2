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

Picklefile2 = open('all_doc_counts', 'rb')
mstr_dict = pickle.load(Picklefile2)

Picklefile7 = open('title_counts', 'rb')
dict_title_counts = pickle.load(Picklefile7)

Picklefile18 = open('dict_without_mstr', 'rb')
mstr_dict_without = pickle.load(Picklefile18)

dict_nt = {}
list_stories_words = []
for k in mstr_dict:
    curr = mstr_dict[k]
    for a in curr:
        list_stories_words.append(a)

dict_stories_words = Counter(list_stories_words)
list_unique_wrds_stories = []
for abc in dict_stories_words:
    list_unique_wrds_stories.append(abc)

print(len(list_unique_wrds_stories))
print(list_unique_wrds_stories)
for w in list_unique_wrds_stories:
    count = 0
    for k in mstr_dict:
        curr_dict = mstr_dict[k]
        if curr_dict[w] != 0:
            count = count + 1
    dict_nt[w] = count

print(len(dict_nt))

dict_freq_summation = {}
dict_max_freq = {}
dict_max_nt = {}
for kk in mstr_dict:
    curr = mstr_dict[kk]
    list_counts = []
    sum_cnts = 0
    list_nt_val = []
    for ab in curr:
        sum_cnts += curr[ab]
        list_counts.append(curr[ab])
        list_nt_val.append(dict_nt[ab])
    max_count = max(list_counts)
    dict_freq_summation[kk] = sum_cnts
    dict_max_freq[kk] = max_count
    mx_nt = max(list_nt_val)
    dict_max_nt[kk] = mx_nt

print(len(dict_freq_summation))
print(len(dict_max_freq))
print(len(dict_max_nt))


#Preparing the dictionaries for titles vocabulary i.e nt dictionary and freqsummation dict and max freq dict
dict_title_nt = {}
list_title_words = []
for kl in dict_title_counts:
    curr = dict_title_counts[kl]
    for a in curr:
        list_title_words.append(a)

dict_titles_words = Counter(list_title_words)
list_unique_words_titles = []
for abc in dict_titles_words:
    list_unique_words_titles.append(abc)

for w in list_unique_words_titles:
    count = 0
    for t in dict_title_counts:
        curr_dict = dict_title_counts[t]
        if curr_dict[w] != 0:
            count += 1
    dict_title_nt[w] = count

dict_title_freq_summation = {}
dict_title_max_freq = {}
for kl in dict_title_counts:
    curr = dict_title_counts[kl]
    list_counts = []
    sum_cnts = 0
    for ab in curr:
        sum_cnts += curr[ab]
        list_counts.append(curr[ab])
    max_count = max(list_counts)
    dict_title_freq_summation[kl] = sum_cnts
    dict_title_max_freq[kl] = max_count

print("************")
print(len(dict_title_counts))
print(len(dict_title_nt))
print(len(dict_title_freq_summation))
print(len(dict_title_max_freq))


#Preparing the dictionaries for without title new case
dict_nt_without = {}
list_stories_words_without = []
for k in mstr_dict_without:
    curr = mstr_dict_without[k]
    for a in curr:
        list_stories_words_without.append(a)

dict_stories_words_without = Counter(list_stories_words_without)
list_unique_wrds_stories_without = []
for abc in dict_stories_words_without:
    list_unique_wrds_stories_without.append(abc)

print(f"length unique without = {len(list_unique_wrds_stories_without)}")
for w in list_unique_wrds_stories_without:
    count = 0
    for k in mstr_dict_without:
        curr_dict = mstr_dict_without[k]
        if curr_dict[w] != 0:
            count = count + 1
    dict_nt_without[w] = count

print(len(dict_nt_without))

dict_freq_summation_without = {}
dict_max_freq_without = {}
dict_max_nt_without = {}
for kk in mstr_dict_without:
    curr = mstr_dict_without[kk]
    list_counts_without = []
    sum_cnts = 0
    list_nt_val_without = []
    for ab in curr:
        sum_cnts += curr[ab]
        list_counts_without.append(curr[ab])
        list_nt_val_without.append(dict_nt_without[ab])
    max_count = max(list_counts_without)
    dict_freq_summation_without[kk] = sum_cnts
    dict_max_freq_without[kk] = max_count
    mx_nt = max(list_nt_val_without)
    dict_max_nt_without[kk] = mx_nt

print("%%%%%%%%%%")
print(dict_nt_without['cliff'])
print(len(dict_nt_without))
print(len(dict_freq_summation_without))
print(len(dict_max_freq_without))
print(len(dict_max_nt_without))
print("@@@@@@@@@@@")

Picklefile3 = open('doc_hits', 'wb')
pickle.dump(dict_nt, Picklefile3)
Picklefile3.close()

Picklefile4 = open('freq_sums', 'wb')
pickle.dump(dict_freq_summation, Picklefile4)
Picklefile4.close()

Picklefile5 = open('max_freq', 'wb')
pickle.dump(dict_max_freq, Picklefile5)
Picklefile5.close()

Picklefile6 = open('max_nt', 'wb')
pickle.dump(dict_max_nt, Picklefile6)
Picklefile6.close()

Picklefile8 = open('title_hits', 'wb')
pickle.dump(dict_title_nt, Picklefile8)
Picklefile8.close()

Picklefile9 = open('title_freq_sums', 'wb')
pickle.dump(dict_title_freq_summation, Picklefile9)
Picklefile9.close()

Picklefile10 = open('title_max_freq', 'wb')
pickle.dump(dict_title_max_freq, Picklefile10)
Picklefile10.close()

Picklefile11 = open('stories_words_list', 'wb')
pickle.dump(list_unique_wrds_stories, Picklefile11)
Picklefile11.close()

Picklefile12 = open('titles_word_list', 'wb')
pickle.dump(list_unique_words_titles, Picklefile12)
Picklefile12.close()

#without begins

Picklefile19 = open('doc_hits_without', 'wb')
pickle.dump(dict_nt_without, Picklefile19)
Picklefile19.close()

Picklefile20 = open('freq_sums_without', 'wb')
pickle.dump(dict_freq_summation_without, Picklefile20)
Picklefile20.close()

Picklefile21 = open('max_freq_without', 'wb')
pickle.dump(dict_max_freq_without, Picklefile21)
Picklefile21.close()

Picklefile22 = open('max_nt_without', 'wb')
pickle.dump(dict_max_nt_without, Picklefile22)
Picklefile22.close()

Picklefile23 = open('stories_words_list_without', 'wb')
pickle.dump(list_unique_wrds_stories_without, Picklefile23)
Picklefile23.close()


print("Pickle done")

