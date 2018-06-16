# -*- coding: utf-8 -*-
import nltk
from nltk import CFG

"""
A,E,Ẹ,I,O,Ọ,U,
a,à,á,e,è,é,ẹ,ẹ̀,ẹ́,i,ì,í,o,ò,ó,ọ,ọ̀,ọ́,u,ù,ú,&,
"""
namelist = ['Bisola', 'car', 'food', 'Tobi', 'girl', 'chair', 'car']
name_string = "|". join("'" +str(x) +"'"  for x in namelist)
print(name_string)

# def perform_function(sentence):
#         # print(sentence)
#         output = ""
#         g_string = (" SIGMA -> DELTA\n"
#                                 " DELTA -> S P C|S P C A|S P A | S P \n"
#                                 " A -> Pre Comp \n"
#                                 " S -> h |m h\n"
#                                 " C -> m h|h\n"
#                                 " P -> n l|aux l| l \n"
#                                 " m -> d e| d\n"
#                                 " h -> " +
#                                 name_string + "\n"
#                                 " l -> 'boarded'|'cooked'|'climbed'|'bought'|'gave'\n"
#                                 " Pre -> 'ni'\n"
#                                 " e -> 'black'\n"
#                                 " d -> 'the'|'The'\n"
#                                 " aux -> 'n'")
#         gramma = CFG.fromstring(g_string)
#         parser = nltk.ChartParser(gramma)
#         try:
#                 ans = parser.parse(sentence.split())
#                 output  = " ".join(str(x) for x in list(ans))
#         except ValueError as e:
#                 # print("error : " + str(e))
#                 output = "Error : " + str(e)
#         return output
# def perform_function(sentence):
#         # print(sentence)
#         output = ""
#         g_string = (" SIGMA -> DELTA\n"
#                                 " DELTA -> S P C|S P C A|S P A | S P \n"
#                                 " A -> Pre C\n"
#                                 " S -> h |h m\n"
#                                 " C -> h| h m\n"
#                                 " P -> l|aux l \n"
#                                 " m -> d e| d\n"
#                                 " h -> " +
#                                 name_string + "\n"
#                                 " l -> 'boarded'|'cooked'|'climbed'|'bought'|'gave'\n"
#                                 " Pre -> 'ni'\n"
#                                 " e -> 'black'\n"
#                                 " d -> 'the'|'The'\n"
#                                 " aux -> 'n'")
#         gramma = CFG.fromstring(g_string)
#         parser = nltk.ChartParser(gramma)
#         print(name_string)
        # print(parser.parse(gramma))
        # for tree in parser.parse(sentence.split()):
        #         print(tree)
                # tree.draw()
        # try:
        #         ans = parser.parse(sentence.split())
        #         output  = " ".join(str(x) for x in list(ans))
        # except ValueError as e:
        #         # print("error : " + str(e))
        #         output = "Error : " + str(e)
        # return output
# tree.draw()
# print(g_string)
# gramma = CFG.fromstring(g_string)
# print(perform_function("Bisola boarded the car"))