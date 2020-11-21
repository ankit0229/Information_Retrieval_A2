import pickle
import os
import re
import string
import math
import numpy
import sys
import pdb
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import WordNetLemmatizer
from collections import Counter

Picklefile13 = open('vectors_stories', 'rb')
stories_vectors_matrix = pickle.load(Picklefile13)

Picklefile14 = open('vectors_titles', 'rb')
titles_vectors_matrix = pickle.load(Picklefile14)

Picklefile15 = open('docs_list', 'rb')
list_docs = pickle.load(Picklefile15)

Picklefile1 = open('doc_titles', 'rb')
dict_titles_doc = pickle.load(Picklefile1)

Picklefile3 = open('doc_hits', 'rb')
dict_nt = pickle.load(Picklefile3)

Picklefile8 = open('title_hits', 'rb')
dict_title_nt = pickle.load(Picklefile8)

Picklefile11 = open('stories_words_list', 'rb')
list_unique_wrds_stories = pickle.load(Picklefile11)
len_list_unique_wrds_stories = len(list_unique_wrds_stories)

Picklefile12 = open('titles_word_list', 'rb')
list_unique_words_titles = pickle.load(Picklefile12)

Picklefile16 = open('vectors_stories_log', 'rb')
log_stories_vectors_matrix = pickle.load(Picklefile16)

Picklefile17 = open('vectors_titles_log', 'rb')
log_titles_vectors_matrix = pickle.load(Picklefile17)

#Without work begins
Picklefile19 = open('doc_hits_without', 'rb')
dict_nt_without = pickle.load(Picklefile19)

Picklefile23 = open('stories_words_list_without', 'rb')
list_unique_wrds_stories_without = pickle.load(Picklefile23)
len_list_unique_wrds_stories_without = len(list_unique_wrds_stories_without)

Picklefile24 = open('vectors_without', 'rb')
without_vectors_matrix = pickle.load(Picklefile24)

Picklefile25 = open('vectors_without_log', 'rb')
log_without_vectors_matrix = pickle.load(Picklefile25)

len_list_unique_words_titles = len(list_unique_words_titles)

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

def make_vector(tokens_query):
    q_vector = numpy.zeros(len_list_unique_wrds_stories, dtype=float)
    word_counts_query = Counter(tokens_query)
    tmp_list = []
    for j in word_counts_query:
        tmp_list.append(word_counts_query[j])
    max_ftd = max(tmp_list)
    for i in range(len_list_unique_wrds_stories):
        curr_wd = list_unique_wrds_stories[i]
        val_tf_norm_point5 = 0.5 + (0.5 * (word_counts_query[curr_wd] / max_ftd))
        idf_val = math.log10(max_nt_corpus / (1 + dict_nt[curr_wd]))
        prod = val_tf_norm_point5 * idf_val
        q_vector[i] = prod
    return q_vector


def find_similarity(query_vector, doc_vector):
    doc_numpy_vector = numpy.array(doc_vector)
    norm_q_vector = numpy.linalg.norm(query_vector)
    norm_doc_vector = numpy.linalg.norm(doc_numpy_vector)
    cosine_sim = (numpy.dot(query_vector, doc_numpy_vector)) / (norm_q_vector * norm_doc_vector)
    return cosine_sim

def make_vector_log(tokens_query):
    q_vector = numpy.zeros(len_list_unique_wrds_stories, dtype=float)
    word_counts_query = Counter(tokens_query)
    for i in range(len_list_unique_wrds_stories):
        curr_wd = list_unique_wrds_stories[i]
        val_tf_log = math.log10(1 + word_counts_query[curr_wd])
        idf_val = math.log10(max_nt_corpus / (1 + dict_nt[curr_wd]))
        prod = val_tf_log * idf_val
        q_vector[i] = prod
    return q_vector

def make_vector_title(tokens_query):
    q_vector = numpy.zeros(len_list_unique_words_titles, dtype=float)
    word_counts_query = Counter(tokens_query)
    tmp_list = []
    for j in word_counts_query:
        tmp_list.append(word_counts_query[j])
    max_ftd = max(tmp_list)
    for i in range(len_list_unique_words_titles):
        curr_wd = list_unique_words_titles[i]
        val_tf_norm_point5 = 0.5 + (0.5 * (word_counts_query[curr_wd] / max_ftd))
        idf_val = math.log10(max_nt_corpus / (1 + dict_title_nt[curr_wd]))
        prod = val_tf_norm_point5 * idf_val
        q_vector[i] = prod
    return q_vector

def make_vector_title_log(tokens_query):
    q_vector = numpy.zeros(len_list_unique_words_titles, dtype=float)
    word_counts_query = Counter(tokens_query)
    for i in range(len_list_unique_words_titles):
        curr_wd = list_unique_words_titles[i]
        val_tf_log = math.log10(1 + word_counts_query[curr_wd])
        idf_val = math.log10(max_nt_corpus / (1 + dict_title_nt[curr_wd]))
        prod = val_tf_log * idf_val
        q_vector[i] = prod
    return q_vector

#Without work begins
def make_vector_without(tokens_query):
    q_vector = numpy.zeros(len_list_unique_wrds_stories_without, dtype=float)
    word_counts_query = Counter(tokens_query)
    tmp_list = []
    for j in word_counts_query:
        tmp_list.append(word_counts_query[j])
    max_ftd = max(tmp_list)
    for i in range(len_list_unique_wrds_stories_without):
        curr_wd = list_unique_wrds_stories_without[i]
        val_tf_norm_point5 = 0.5 + (0.5 * (word_counts_query[curr_wd] / max_ftd))
        idf_val = math.log10(max_nt_without / (1 + dict_nt_without[curr_wd]))
        prod = val_tf_norm_point5 * idf_val
        q_vector[i] = prod
    return q_vector

def make_vector_log_without(tokens_query):
    q_vector = numpy.zeros(len_list_unique_wrds_stories_without, dtype=float)
    word_counts_query = Counter(tokens_query)
    for i in range(len_list_unique_wrds_stories_without):
        curr_wd = list_unique_wrds_stories_without[i]
        val_tf_log = math.log10(1 + word_counts_query[curr_wd])
        idf_val = math.log10(max_nt_without / (1 + dict_nt_without[curr_wd]))
        prod = val_tf_log * idf_val
        q_vector[i] = prod
    return q_vector

# print("Enter the query:")
# query = input()
# print("Enter the value of k: ")
# top_k = int(input())
list_args = sys.argv
query = list_args[1]
top_k = int(list_args[2])
query = query.lower()
query = re.sub(r'\S+@\S+', '', query)
query = re.sub(r'[a-zA-Z]+[0-9]+', '', query)
query = re.sub(r'[0-9]+[a-zA-Z]+', '', query)
translator = str.maketrans(string.punctuation, ' ' * len(string.punctuation))  # map punctuation to space
query = query.translate(translator)
query_tokens = word_tokenize(query)
vector_query = make_vector(query_tokens)
vector_query_title = make_vector_title(query_tokens)
vector_query_log = make_vector_log(query_tokens)
vector_query_title_log = make_vector_title_log(query_tokens)
vector_query_without = make_vector_without(query_tokens)
vector_query_without_log = make_vector_log_without(query_tokens)

stories_list_scores = []
title_story_list_scores = []
stories_list_scores_log = []
title_story_list_scores_log = []
without_list_scores = []
without_list_scores_log = []
for x in range(len(list_docs)):
    #Work for with title
    vector_curr_doc = stories_vectors_matrix[x]
    score_ret = find_similarity(vector_query, vector_curr_doc)
    pair = [list_docs[x], score_ret]
    stories_list_scores.append(pair)
    #Now finding the sim with title of doc
    vector_curr_title = titles_vectors_matrix[x]
    title_score_ret = find_similarity(vector_query_title, vector_curr_title)
    combined_score = (0.7 * title_score_ret) + (0.3 * score_ret)
    new_pair = [list_docs[x], combined_score]
    title_story_list_scores.append(new_pair)
    #Finding sim using only body with log tf
    vector_curr_doc = log_stories_vectors_matrix[x]
    score_ret = find_similarity(vector_query_log, vector_curr_doc)
    pair = [list_docs[x], score_ret]
    stories_list_scores_log.append(pair)
    #Finding sim considering title also with log
    vector_curr_title = log_titles_vectors_matrix[x]
    title_score_ret = find_similarity(vector_query_title_log, vector_curr_title)
    combined_score = (0.7 * title_score_ret) + (0.3 * score_ret)
    new_pair = [list_docs[x], combined_score]
    title_story_list_scores_log.append(new_pair)
    #Without title work begins
    vector_curr_without = without_vectors_matrix[x]
    #print(len(vector_curr_without))
    score_ret = find_similarity(vector_query_without, vector_curr_without)
    pair = [list_docs[x], score_ret]
    without_list_scores.append(pair)

    vector_curr_without = log_without_vectors_matrix[x]
    score_ret = find_similarity(vector_query_without_log, vector_curr_without)
    pair = [list_docs[x], score_ret]
    without_list_scores_log.append(pair)

#Getting and printing the top documents without considering titles
without_list_scores.sort(key = lambda p:p[1], reverse=True)
list_top_docs = []
for j in range(top_k):
    list_top_docs.append(without_list_scores[j][0])

print("Using double norm 0.5 as tf\n")
print("Without giving special attention to the document title the top documents are:\n")
#print(f"\nThe top k documents by method {list_methods[mt_no]} are: ")
print(list_top_docs)
for j in list_top_docs:
    print(dict_titles_doc[j])

#Getting and printing the top documents while considering titles also
print("Giving special attention to the document titles the top documents are:\n")
title_story_list_scores.sort(key = lambda p:p[1], reverse=True)
list_top_docs = []
for j in range(top_k):
    list_top_docs.append(title_story_list_scores[j][0])

print(list_top_docs)
for j in list_top_docs:
    print(dict_titles_doc[j])

print("\nUsing log norm as tf")
print("Without giving special attention to the document title the top documents are:\n")
without_list_scores_log.sort(key = lambda x:x[1], reverse=True)
list_top_docs = []
for j in range(top_k):
    list_top_docs.append(without_list_scores_log[j][0])

print(list_top_docs)
for j in list_top_docs:
    print(dict_titles_doc[j])

print("\nGiving special attention to the document titles the top documents are:\n")
title_story_list_scores_log.sort(key = lambda p:p[1], reverse=True)
list_top_docs = []
for j in range(top_k):
    list_top_docs.append(title_story_list_scores_log[j][0])

print(list_top_docs)
for j in list_top_docs:
    print(dict_titles_doc[j])
