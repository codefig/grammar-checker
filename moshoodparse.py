# _*_ coding: utf-8 _*_
import nltk
from nltk import CFG
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
"""
A,E,Ẹ,I,O,Ọ,U,
a,à,á,e,è,é,ẹ,ẹ̀,ẹ́,i,ì,í,o,ò,ó,ọ,ọ̀,ọ́,u,ù,ú,&,
'A,À,Á,E,È,É,Ẹ,Ẹ̀,Ẹ́,I,Ì,Í,O,Ò,Ó,Ọ,Ọ̀,Ọ́,U,Ù,Ú,'
"""
# gramma = CFG.fromstring("\n"
#                         " SIGMA -> DELTA\n"
#                         " DELTA -> S P A|S P C|S P C A| S P| S \n"
#                         " A -> p C| Ap \n"
#                         " S -> h |h m| h q| h m q| h e o q d\n"
#                         " C -> h m|h\n"
#                         " P -> n l|a l| l| l PO| a l PO| n a l PO| n l PO| n a l \n"
#                         " h -> 'Tóbi'|'Iná'|'oúnje'| 'Bísọ́lá'|'Tóbi'|'Tólá'|'Ọmọbìnrin'|'Mo'|'àga'|'ọkọ̀'|'bàtà'|'eyinkunle'|'ilé'\n"
#                         " d -> 'náà'| 'yẹn'\n"
#                         " o -> 'méji'\n"
#                         " e -> 'kékeré'\n" 
#                         " l -> 'sè'|'jó'|'wọ'|'gùn'|'ra'|'lọ'| 'múra'\n"
#                         " n -> 'kọ'|'ò'\n"
#                         " q -> 'tí mo kọ́'\n"
#                         " PO -> 'sí'\n"
#                         " p -> 'fún'|'ni'\n"
#                         " Ap -> 'gidigidi'\n"
#                         " a -> 'ń'\n")
# parser = nltk.ChartParser(gramma)

#construct the PSG algorithm
noun_file = open('noun_file.txt');
noun_list = noun_file.read().split(',')
noun_string = "|". join("'" +str(x) +"'"  for x in noun_list)

verb_file = open('verb_file.txt')
verb_list = verb_file.read().split(",")
verb_string = "|". join("'" +str(x) +"'"  for x in verb_list)


grammar_string = '''
                        " S -> NP VP \n"
                        " NP -> N | N D \n"
                        " VP -> V NP | V \n"
                        " N -> 'Man'\n"
                        " V -> 'Woman'\n"
                        " D -> 'Naa'\n"
                  '''
psg_grammar = CFG.fromstring(grammar_string)
# psg_grammar = CFG.fromstring("\n"
#                         " S -> NP VP \n"
#                         " NP -> N | N D \n"
#                         " VP -> V NP | V \n"
#                         " N -> " + noun_string + "\n"
#                         " V -> "+ verb_string + "\n"
#                         " D -> 'Naa'\n")

print(psg_grammar)
# parser = nltk.ChartParser(gramma)
# first =  ['Bísọ́lá','múra','gidigidi']
# try:
      
#       for x in parser.parse(first):
#           print(x)
#       x.draw()
# except ValueError as e:
#       print(e.args)
    
