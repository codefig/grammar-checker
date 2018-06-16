# _*_ coding: utf-8 _*_
import nltk
from nltk import CFG
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

"""
A,E,Ẹ,I,O,Ọ,U
a,à,á,e,è,é,ẹ,ẹ̀,ẹ́,i,ì,í,o,ò,ó,ọ,ọ̀,ọ́,u,ù,ú
"""


noun_file = open('noun_file.txt', encoding="utf8");
noun_list = noun_file.read().split(',')
noun_string = "|". join("'" +str(x) +"'"  for x in noun_list if x is not '')
# print(noun_string)

verb_file = open('verb_file.txt', encoding='utf8')
verb_list = verb_file.read().split(",")
verb_output = "|". join("'" +str(x) +"'"  for x in verb_list if x is not '')
# print(verb_output)
                        # " N -> " + "'Bísọ́lá' | 'ọkọ̀' | 'Tóbi' | 'oúnje' | 'tọ́pé'| 'owó' | 'Ọmọbìnrin' | 'àga' | 'asọ' | 'igi'| 'Ile' \n"

string_ans = ( " S -> NP VP \n"
                        " NP -> N | N D | N ADJP |N N| N NP\n"
                        " VP -> V NP | V \n"
                        " ADJP -> ADJ D |ADJ \n"
                        " N -> " + noun_string + " \n"
                        " V -> 'wọ' | 'sè' | 'dá' | 'gùn'| 'fọ̀' | 'ra' \n"
                        " D -> 'náà'|'yẹn' \n"
                        " ADJ -> 'dúdú' \n")

gramma = CFG.fromstring(string_ans)
sent1= ['Bísọ́lá']
sent2= ['Ile','Bísọ́lá']
sent3= ['aga','Bísọ́lá','yẹn']      
sent4= ['Bísọ́lá','wọ','ọkọ̀','náà']
sent5= ['Tóbi','sè','oúnje','náà']
sent6= ['tọ́pé','dá','owó']
sent7= ['Ọmọbìnrin','náà','gùn','àga','náà'] 
sent8= ['igi','náà','dá']
sent9= ['Bísọ́lá','fọ̀','asọ','náà']
sent10=['Ọmọbìnrin','náà','ra','ọkọ̀','dúdú','náà']
parser = nltk.ChartParser(gramma)
# print(parser)
for tree in parser.parse(sent6):
        print(tree)
tree.draw()
# parser = nltk.ChartParser(gramma)
# for tree in parser.parse(sent2):
#         print(tree)
# tree.draw()
# for tree in parser.parse(sent3):
#         print(tree)
# tree.draw()
# for tree in parser.parse(sent4):
#         print(tree)
# tree.draw()
# for tree in parser.parse(sent5):
#         print(tree)
# tree.draw()
# for tree in parser.parse(sent6):
#         print(tree)
# tree.draw()
# for tree in parser.parse(sent7):
#         print(tree)
# tree.draw()
