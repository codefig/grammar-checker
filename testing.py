import nltk
from nltk import CFG
gramma = CFG.fromstring("\n"
                        " S -> NP VP \n"
                        " NP -> N | D N | ADJP NP | D NP \n"
                        " VP -> V NP | V \n"
                        " ADJP -> ADJ \n"
                        " N -> 'bisola' | 'car' | 'tobi' | 'food' | 'tope'| 'money' | 'girl' | 'chair' | 'clothes' | 'stick'|'girl' \n"
                        " V -> 'boarded' | 'cooked' | 'contributed' | 'broke' | 'climbed'| 'washed'|'bought' \n"
                        " D -> 'the' \n"
                        " ADJ -> 'black' \n")

sent1= ['tobi','cooked','the','food']
sent2= ['bisola','boarded','the','car']
sent3= ['tope','contributed','money']
sent4= ['the','girl','climbed','the','black','chair']
sent5= ['the','stick','broke']
sent6= ['bisola','washed','the','clothes']
sent7= ['the','girl','bought','the','black','car']
parser = nltk.ChartParser(gramma)
for tree in parser.parse(sent1):
        print(tree)
tree.draw()
for tree in parser.parse(sent2):
    print(tree)
tree.draw()
for tree in parser.parse(sent3):
    print(tree)
tree.draw()
for tree in parser.parse(sent4):
   print(tree)
tree.draw()
for tree in parser.parse(sent5):
    print(tree)
tree.draw()
for tree in parser.parse(sent6):
        print(tree)
tree.draw()
for tree in parser.parse(sent7):
        print(tree)
tree.draw()
        





