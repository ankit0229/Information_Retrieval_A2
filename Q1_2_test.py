import pickle
import os
import re
import string
import math
import sys
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

list_all_nt = []
for ac in dict_nt:
    list_all_nt.append(dict_nt[ac])

max_nt_corpus = max(list_all_nt)
#print(f"value max nt = {max_nt_corpus}")

Picklefile4 = open('freq_sums', 'rb')
dict_freq_summation = pickle.load(Picklefile4)

Picklefile5 = open('max_freq', 'rb')
dict_max_freq = pickle.load(Picklefile5)

Picklefile6 = open('max_nt', 'rb')
dict_max_nt = pickle.load(Picklefile6)

#Begins for without
Picklefile18 = open('dict_without_mstr', 'rb')
mstr_dict_without = pickle.load(Picklefile18)

Picklefile19 = open('doc_hits_without', 'rb')
dict_nt_without = pickle.load(Picklefile19)

Picklefile20 = open('freq_sums_without', 'rb')
dict_freq_summation_without = pickle.load(Picklefile20)

Picklefile21 = open('max_freq_without', 'rb')
dict_max_freq_without = pickle.load(Picklefile21)

Picklefile22 = open('max_nt_without', 'rb')
dict_max_nt_without = pickle.load(Picklefile22)

Picklefile23 = open('stories_words_list_without', 'rb')
list_unique_wrds_stories_without = pickle.load(Picklefile23)

list_all_nt = []
for ac in dict_nt_without:
    list_all_nt.append(dict_nt_without[ac])

max_nt_without = max(list_all_nt)
#print(f"value max nt = {max_nt_without}")

#Begins for titles
Picklefile7 = open('title_counts', 'rb')
dict_title_counts = pickle.load(Picklefile7)

Picklefile8 = open('title_hits', 'rb')
dict_title_nt = pickle.load(Picklefile8)

Picklefile9 = open('title_freq_sums', 'rb')
dict_title_freq_summation = pickle.load(Picklefile9)

Picklefile10 = open('title_max_freq', 'rb')
dict_title_max_freq = pickle.load(Picklefile10)

list_all_nt = []
for ac in dict_title_nt:
    list_all_nt.append(dict_title_nt[ac])

max_nt_title = max(list_all_nt)
#print(f"value max nt of titles = {max_nt_corpus}")

N_val = len(dict_max_freq)

#print(dict_max_freq)
def tf_binary(term, doc):
    return 1

def tf_raw_count(term, doc):
    curr = mstr_dict[doc]
    return curr[term]

def tf_term_frequency(term, doc):
    curr = mstr_dict[doc]
    tf_wt = curr[term] / dict_freq_summation[doc]
    return tf_wt

def tf_log_norm(term, doc):
    curr = mstr_dict[doc]
    tf_wt = math.log10(1 + curr[term])
    return tf_wt

def double_norm_point5(term, doc):
    curr = mstr_dict[doc]
    tf_wt = 0.5 + (0.5*(curr[term] / dict_max_freq[doc]))
    return tf_wt

def double_norm_k(k, term, doc):
    curr = mstr_dict[doc]
    tf_wt = k + ((1 - k) * (curr[term] / dict_max_freq[doc]))
    return tf_wt

def idf(term):
    idf_val = math.log10(N_val / dict_nt[term])
    return idf_val

def idf_smooth(term):
    idf_val = math.log10(N_val / (1 + dict_nt[term]))
    return idf_val

def idf_max(term):
    idf_val = math.log10(max_nt_corpus / (1 + dict_nt[term]))
    return idf_val

#Now defining the tf and idf functions for titles
def title_tf_binary(term, doc):
    return 1

def title_tf_raw_count(term, doc):
    curr = dict_title_counts[doc]
    return curr[term]

def title_tf_term_frequency(term, doc):
    curr = dict_title_counts[doc]
    tf_wt = curr[term] / dict_title_freq_summation[doc]
    return tf_wt

def title_tf_log_norm(term, doc):
    curr = dict_title_counts[doc]
    tf_wt = math.log10(1 + curr[term])
    return tf_wt

def title_double_norm_point5(term, doc):
    curr = dict_title_counts[doc]
    tf_wt = 0.5 + (0.5*(curr[term] / dict_title_max_freq[doc]))
    return tf_wt

def title_double_norm_k(k, term, doc):
    curr = dict_title_counts[doc]
    tf_wt = k + ((1 - k) * (curr[term] / dict_title_max_freq[doc]))
    return tf_wt

def title_idf_max(term):
    idf_val = math.log10(max_nt_title / (1 + dict_title_nt[term]))
    return idf_val

#Now defining the tf and idf functions for without case
def tf_binary_without(term, doc):
    return 1

def tf_raw_count_without(term, doc):
    curr = mstr_dict_without[doc]
    return curr[term]

def tf_term_frequency_without(term, doc):
    curr = mstr_dict_without[doc]
    tf_wt = curr[term] / dict_freq_summation_without[doc]
    return tf_wt

def tf_log_norm_without(term, doc):
    curr = mstr_dict_without[doc]
    tf_wt = math.log10(1 + curr[term])
    return tf_wt

def double_norm_point5_without(term, doc):
    curr = mstr_dict_without[doc]
    tf_wt = 0.5 + (0.5*(curr[term] / dict_max_freq_without[doc]))
    return tf_wt

def double_norm_k_without(k, term, doc):
    curr = mstr_dict_without[doc]
    tf_wt = k + ((1 - k) * (curr[term] / dict_max_freq_without[doc]))
    return tf_wt

def idf_max_without(term):
    idf_val = math.log10(max_nt_without / (1 + dict_nt_without[term]))
    return idf_val

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
norm_k_val = 0.3

list_matching_scores_without = [[] for i in range(6)]
list_mt_scores_titles = [[] for i in range(6)]
for dc in mstr_dict:
    curr_doc = mstr_dict[dc]
    curr_doc_title = dict_title_counts[dc]
    curr_doc_without = mstr_dict_without[dc]
    list_ms = [0 for i in range(6)]
    list_ms_title = [0 for i in range(6)]
    list_ms_without = [0 for i in range(6)]
    for q in query_tokens:
        #Handling the case of without
        if curr_doc_without[q] != 0:
            val_tf_bin = tf_binary_without(q, dc)
            val_tf_raw = tf_raw_count_without(q, dc)
            val_tf_tf = tf_term_frequency_without(q, dc)
            val_tf_log = tf_log_norm_without(q, dc)
            val_tf_norm = double_norm_point5_without(q, dc)
            val_tf_norm_k = double_norm_k_without(norm_k_val, q, dc)
            val_idf_max = idf_max_without(q)

            list_ms_without[0] += (val_tf_bin * val_idf_max)
            list_ms_without[1] += (val_tf_raw * val_idf_max)
            list_ms_without[2] += (val_tf_tf * val_idf_max)
            list_ms_without[3] += (val_tf_log * val_idf_max)
            list_ms_without[4] += (val_tf_norm * val_idf_max)
            list_ms_without[5] += (val_tf_norm_k * val_idf_max)

        if curr_doc[q] != 0:
            val_tf_bin = tf_binary(q, dc)
            val_tf_raw = tf_raw_count(q, dc)
            val_tf_tf = tf_term_frequency(q, dc)
            val_tf_log = tf_log_norm(q, dc)
            val_tf_norm = double_norm_point5(q, dc)
            val_tf_norm_k = double_norm_k(norm_k_val, q, dc)
            val_idf_simple = idf(q)
            val_idf_smooth = idf_smooth(q)
            val_idf_max = idf_max(q)

            list_ms[0] += (val_tf_bin * val_idf_max)
            list_ms[1] += (val_tf_raw * val_idf_max)
            list_ms[2] += (val_tf_tf * val_idf_max)
            list_ms[3] += (val_tf_log * val_idf_max)
            list_ms[4] += (val_tf_norm * val_idf_max)
            list_ms[5] += (val_tf_norm_k * val_idf_max)

        #Now finding intersection of query with title and getting score
        if curr_doc_title[q] != 0:
            val_tf_bin = title_tf_binary(q, dc)
            val_tf_raw = title_tf_raw_count(q, dc)
            val_tf_tf = title_tf_term_frequency(q, dc)
            val_tf_log = title_tf_log_norm(q, dc)
            val_tf_norm = title_double_norm_point5(q, dc)
            val_tf_norm_k = title_double_norm_k(norm_k_val, q, dc)
            val_idf_max = title_idf_max(q)

            list_ms_title[0] += (val_tf_bin * val_idf_max)
            list_ms_title[1] += (val_tf_raw * val_idf_max)
            list_ms_title[2] += (val_tf_tf * val_idf_max)
            list_ms_title[3] += (val_tf_log * val_idf_max)
            list_ms_title[4] += (val_tf_norm * val_idf_max)
            list_ms_title[5] += (val_tf_norm_k * val_idf_max)

    for ij in range(6):
        pair = [dc, list_ms_without[ij]]
        list_matching_scores_without[ij].append(pair)

    for ik in range(6):
        combined_score = (0.7*list_ms_title[ik]) + (0.3 * list_ms[ik])
        pair = [dc, combined_score]
        list_mt_scores_titles[ik].append(pair)

#print(f"check val = {len(list_mt_scores_titles[3])}")
list_methods = ['tf_binary and idf_max', 'tf_raw and idf_max', 'tf_tf and idf_max', 'tf_log and idf_max',
                'tf_norm_0.5 and idf_max', 'tf_norm_k and idf_max']

mt_no = 0
print("Without giving special attention to the title the top k documents using different methods are:\n")
for kl in list_matching_scores_without:
    kl.sort(key = lambda x:x[1], reverse=True)
    list_top_docs = []
    for j in range(k):
        list_top_docs.append(kl[j][0])

    print(f"\nThe top k documents by method {list_methods[mt_no]} are: ")
    print(list_top_docs)
    mt_no += 1
    for j in list_top_docs:
        print(dict_titles_doc[j])

#Now giving special attention to the title of the document
mt_no = 0
print("\nGiving special attention to the title the top k documents using different methods are:\n")
for kl in list_mt_scores_titles:
    kl.sort(key = lambda x:x[1], reverse=True)
    list_top_docs = []
    for j in range(k):
        list_top_docs.append(kl[j][0])

    print(f"\nThe top k documents by method {list_methods[mt_no]} are: ")
    print(list_top_docs)
    mt_no += 1
    for j in list_top_docs:
        print(dict_titles_doc[j])