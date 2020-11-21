import re
from nltk.tokenize import word_tokenize
from collections import Counter

directory = r'D:\M.TECH SEM 2\IR\Assignments\A2\english2\english2.txt'
fp = open(directory, "r")
text = fp.read()
fp.close()
list_words_english2 = word_tokenize(text)
# print(list_words_english2)
# print(len(list_words_english2))
dict_english2 = Counter(list_words_english2)
print(len(dict_english2))

print("Enter the sentence:")
input_sent = input()
print("Enter the value of k in top k:")
top_k = int(input())

input_sent = input_sent.lower()
input_sent = re.sub(r' [0-9]+ ', ' ', input_sent)
input_sent = re.sub(r'[~`!@#$%^&*(){[}|_<,>.?/:;"]', ' ', input_sent)
list_words_input = word_tokenize(input_sent)
dict_unkword_distances = {}
for wrd in list_words_input:
    if dict_english2[wrd] == 0:
        list_distances = []
        len_wrd = len(wrd)
        for curr_word_dict in dict_english2:
            len_curr_word_dict = len(curr_word_dict)
            table_distance = [[0 for i in range(len_curr_word_dict+1)]for j in range(len_wrd+1)]
            for k in range(len_curr_word_dict+1):
                table_distance[0][k] = k * 2
            for l in range(len_wrd+1):
                table_distance[l][0] = l * 1
            for m in range(1, len_curr_word_dict+1):
                for n in range(1, len_wrd+1):
                    list_possib = []
                    list_possib.append(table_distance[n-1][m] + 1)
                    list_possib.append(table_distance[n][m-1] + 2)
                    if wrd[n-1] == curr_word_dict[m-1]:
                        list_possib.append(table_distance[n-1][m-1] + 0)
                    else:
                        list_possib.append(table_distance[n - 1][m - 1] + 3)

                    table_distance[n][m] = min(list_possib)

            edit_distance = table_distance[len_wrd][len_curr_word_dict]
            pair = [curr_word_dict, edit_distance]
            list_distances.append(pair)
        dict_unkword_distances[wrd] = list_distances

if len(dict_unkword_distances) == 0:
    print("No non-dictionary words are present in the sentence")

else:
    for wd in dict_unkword_distances:
        distances_list = dict_unkword_distances[wd]
        distances_list.sort(key = lambda x:x[1])
        print(f"The top {top_k} dictionary words along with the edit distance matching {wd} are: ")
        for i in range(top_k):
            print(f"{distances_list[i][0]}     {distances_list[i][1]}")