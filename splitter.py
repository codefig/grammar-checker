infile = open('dictionary.txt')
words = infile.read()
output_file = open('output.txt', 'wb+')

less_words = words.split('.')
# print(less_words[20])
''' 
	This line is for splitting the nouns and part of speech 
'''
print(len(less_words))
for i in range(len(less_words)):
	if(len(less_words[i].split(',')) == 2):
		output_file.write(less_words[i].strip(' ') + "\n")
	else:
		text = less_words[i].split(',')
		for words in text[0:-1]:
			output_file.write(words.strip(' ') + "," + text[-1] + "\n")

output_file.close()
infile.close()

noun_count = 0
adj_count = 0
conj_count = 0
verb_count = 0
prep_count = 0;
adv_count  =0


  