# _*_ coding: utf-8 _*_
import nltk
from nltk import CFG

"""
A,E,Ẹ,I,O,Ọ,U
a,à,á,e,è,é,ẹ,ẹ̀,ẹ́,i,ì,í,o,ò,ó,ọ,ọ̀,ọ́,u,ù,ú
"""
noun_file = open('noun_file.txt', encoding="utf8");
noun_list = noun_file.read().split(',')
noun_string = "|". join("'" + str(x.lower()) +
                        "'" for x in noun_list if x is not '')


verb_file = open('verb_file.txt', encoding='utf8')
verb_list = verb_file.read().split(",")
verb_output = "|". join("'" + str(x.lower()) +
                        "'" for x in verb_list if x is not '')


def perform_xbar(sentence):
        gramma_string = (" IP -> Spec IBAR \n"
                        " Spec -> NP \n"
                        " IBAR -> I VP\n"
                        " NP -> NBAR  \n"
                        " NBAR -> N DP| N  \n"
                        " VP -> VBAR \n"
                        " VBAR -> V| V NP \n"
                        " DP -> DBAR \n"
                        " DBAR -> D \n"
                        " N -> "+noun_string + " \n"
                        " V -> "+verb_output+ " \n"
                        " D -> 'náà' \n")
        gramma = CFG.fromstring(gramma_string)
        parser = nltk.ChartParser(gramma)
        try:
                lower_sentence = sentence.lower()
                ans = parser.parse(lower_sentence.split())
                output = " ".join(str(x) for x in list(ans))
        except ValueError as e:
                output = "Error : " + str(e)
        return output

# result = perform_xbar("Tóbi sè oúnje náà")
result = perform_xbar("bísọ́lá  wọ ọkọ̀ náà")
print(str(result).encode("utf-8"))
print(len(list(result)))
print(result[0:5])

