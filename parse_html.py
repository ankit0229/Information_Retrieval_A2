import pickle
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
       if data != '\n' and data != '  ':
           list_titles_doc.append(data)

dict_titles_doc = {}
list_titles_doc = []
curr_doc = ''
directory = r'D:\M.TECH SEM 2\IR\Assignments\A2\stories\index.html'
fp = open(directory, "r")
text = fp.read()
fp.close()
#print(text)

parser = MyHTMLParser()
parser.feed(text)
#print(list_titles_doc)

print(list_titles_doc)
list_titles_doc = list_titles_doc[16:]
print(len(list_titles_doc))
ab = len(list_titles_doc)
#list_titles_doc = list_titles_doc[16:1373]
list_titles_doc = list_titles_doc[:ab-2]
print(list_titles_doc)
i = 0
while i < len(list_titles_doc):
    k = list_titles_doc[i]
    v = list_titles_doc[i+2]
    v = v.rstrip()
    dict_titles_doc[k] = v
    i += 3

print(dict_titles_doc)
print(len(dict_titles_doc))

Picklefile1 = open('doc_titles', 'wb')
pickle.dump(dict_titles_doc, Picklefile1)
Picklefile1.close()

print("pickle done")

#print(list_titles_doc.index('Solar Realms Elite: X1 and X2, by Josh Renaud\n'))
#parser = MyHTMLParser()
