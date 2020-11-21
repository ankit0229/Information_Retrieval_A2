import pickle
import os
import re
import string
import math
import pdb
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import WordNetLemmatizer
from collections import Counter

Picklefile1 = open('doc_titles', 'rb')
dict_titles_doc = pickle.load(Picklefile1)

Picklefile2 = open('all_doc_counts', 'rb')
mstr_dict = pickle.load(Picklefile2)

Picklefile3 = open('doc_hits', 'rb')
dict_nt = pickle.load(Picklefile3)

Picklefile5 = open('max_freq', 'rb')
dict_max_freq = pickle.load(Picklefile5)

Picklefile7 = open('title_counts', 'rb')
dict_title_counts = pickle.load(Picklefile7)

Picklefile8 = open('title_hits', 'rb')
dict_title_nt = pickle.load(Picklefile8)

Picklefile10 = open('title_max_freq', 'rb')
dict_title_max_freq = pickle.load(Picklefile10)

Picklefile11 = open('stories_words_list', 'rb')
list_unique_wrds_stories = pickle.load(Picklefile11)
len_list_unique_wrds_stories = len(list_unique_wrds_stories)

Picklefile12 = open('titles_word_list', 'rb')
list_unique_words_titles = pickle.load(Picklefile12)
len_list_unique_words_titles = len(list_unique_words_titles)

#Work for without
Picklefile18 = open('dict_without_mstr', 'rb')
mstr_dict_without = pickle.load(Picklefile18)

Picklefile21 = open('max_freq_without', 'rb')
dict_max_freq_without = pickle.load(Picklefile21)

Picklefile19 = open('doc_hits_without', 'rb')
dict_nt_without = pickle.load(Picklefile19)

Picklefile23 = open('stories_words_list_without', 'rb')
list_unique_wrds_stories_without = pickle.load(Picklefile23)
len_list_unique_wrds_stories_without = len(list_unique_wrds_stories_without)

list_docs = []
for k in mstr_dict:
    list_docs.append(k)

count_docs = len(list_docs)

list_all_nt = []
for ac in dict_nt:
    list_all_nt.append(dict_nt[ac])
max_nt_corpus = max(list_all_nt)

list_all_nt = []
for ac in dict_title_nt:
    list_all_nt.append(dict_title_nt[ac])
max_nt_title = max(list_all_nt)

list_all_nt = []
for ac in dict_nt_without:
    list_all_nt.append(dict_nt_without[ac])
max_nt_without = max(list_all_nt)
def double_norm_point5(term, doc):
    curr = mstr_dict[doc]
    tf_wt = 0.5 + (0.5*(curr[term] / dict_max_freq[doc]))
    return tf_wt

def tf_log_norm(term, doc):
    curr = mstr_dict[doc]
    tf_wt = math.log10(1 + curr[term])
    return tf_wt

def idf_max(term):
    idf_val = math.log10(max_nt_corpus / (1 + dict_nt[term]))
    return idf_val

#Now defining the tf and idf functions for titles
def title_double_norm_point5(term, doc):
    curr = dict_title_counts[doc]
    tf_wt = 0.5 + (0.5*(curr[term] / dict_title_max_freq[doc]))
    return tf_wt

def title_tf_log_norm(term, doc):
    curr = dict_title_counts[doc]
    tf_wt = math.log10(1 + curr[term])
    return tf_wt

def title_idf_max(term):
    idf_val = math.log10(max_nt_title / (1 + dict_title_nt[term]))
    return idf_val

#Now defining the tf and idf functions for without case
def tf_log_norm_without(term, doc):
    curr = mstr_dict_without[doc]
    tf_wt = math.log10(1 + curr[term])
    return tf_wt

def double_norm_point5_without(term, doc):
    curr = mstr_dict_without[doc]
    tf_wt = 0.5 + (0.5*(curr[term] / dict_max_freq_without[doc]))
    return tf_wt

def idf_max_without(term):
    idf_val = math.log10(max_nt_without / (1 + dict_nt_without[term]))
    return idf_val

#Using double normalisation 0.5 as the tf value
stories_vectors_matrix = [[0 for i in range(len_list_unique_wrds_stories)] for j in range(count_docs)]
titles_vectors_matrix = [[0 for i in range(len_list_unique_words_titles)] for j in range(count_docs)]
without_vectors_matrix = [[0 for i in range(len_list_unique_wrds_stories_without)] for j in range(count_docs)]

for dc in range(count_docs):
    curr_doc = list_docs[dc]
    for wd in range(len_list_unique_wrds_stories):
        curr_wd = list_unique_wrds_stories[wd]
        val_tf_norm = double_norm_point5(curr_wd, curr_doc)
        val_idf_max = idf_max(curr_wd)
        prod = val_tf_norm * val_idf_max
        stories_vectors_matrix[dc][wd] = prod
    for ws in range(len_list_unique_words_titles):
        curr_wd = list_unique_words_titles[ws]
        val_tf_norm = title_double_norm_point5(curr_wd, curr_doc)
        val_idf_max = title_idf_max(curr_wd)
        prod = val_tf_norm * val_idf_max
        titles_vectors_matrix[dc][ws] = prod
    for wt in range(len_list_unique_wrds_stories_without):
        curr_wd = list_unique_wrds_stories_without[wt]
        val_tf_norm = double_norm_point5_without(curr_wd, curr_doc)
        val_idf_max = idf_max_without(curr_wd)
        prod = val_tf_norm * val_idf_max
        without_vectors_matrix[dc][wt] = prod

#using log normalisation as the tf value
log_stories_vectors_matrix = [[0 for i in range(len_list_unique_wrds_stories)] for j in range(count_docs)]
log_titles_vectors_matrix = [[0 for i in range(len_list_unique_words_titles)] for j in range(count_docs)]
log_without_vectors_matrix = [[0 for i in range(len_list_unique_wrds_stories_without)] for j in range(count_docs)]
for dc in range(count_docs):
    curr_doc = list_docs[dc]
    for abc in range(len_list_unique_wrds_stories):
        curr_wd = list_unique_wrds_stories[abc]
        val_tf_norm = tf_log_norm(curr_wd, curr_doc)
        val_idf_max = idf_max(curr_wd)
        prod = val_tf_norm * val_idf_max
        log_stories_vectors_matrix[dc][abc] = prod
    for abd in range(len_list_unique_words_titles):
        curr_wd = list_unique_words_titles[abd]
        val_tf_norm = title_tf_log_norm(curr_wd, curr_doc)
        val_idf_max = title_idf_max(curr_wd)
        prod = val_tf_norm * val_idf_max
        log_titles_vectors_matrix[dc][abd] = prod
    for abe in range(len_list_unique_wrds_stories_without):
        curr_wd = list_unique_wrds_stories_without[abe]
        val_tf_norm = tf_log_norm_without(curr_wd, curr_doc)
        val_idf_max = idf_max_without(curr_wd)
        prod = val_tf_norm * val_idf_max
        log_without_vectors_matrix[dc][abe] = prod

Picklefile13 = open('vectors_stories', 'wb')
pickle.dump(stories_vectors_matrix, Picklefile13)
Picklefile13.close()

Picklefile14 = open('vectors_titles', 'wb')
pickle.dump(titles_vectors_matrix, Picklefile14)
Picklefile14.close()

Picklefile15 = open('docs_list', 'wb')
pickle.dump(list_docs, Picklefile15)
Picklefile15.close()

Picklefile16 = open('vectors_stories_log', 'wb')
pickle.dump(log_stories_vectors_matrix, Picklefile16)
Picklefile16.close()

Picklefile17 = open('vectors_titles_log', 'wb')
pickle.dump(log_titles_vectors_matrix, Picklefile17)
Picklefile17.close()

Picklefile24 = open('vectors_without', 'wb')
pickle.dump(without_vectors_matrix, Picklefile24)
Picklefile24.close()

Picklefile25 = open('vectors_without_log', 'wb')
pickle.dump(log_without_vectors_matrix, Picklefile25)
Picklefile25.close()

print("Pickle done")