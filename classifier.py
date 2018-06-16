infile = open('output.txt')
all_lines = infile.readlines()

noun_count = 0
adj_count = 0
conj_count = 0
verb_count = 0
prep_count = 0;
adv_count  =0
noun_file = open('noun_file.txt', 'a+')
adj_file = open('adj_file.txt', 'a+')
conj_file = open('conj_file.txt', 'a+')
verb_file = open('verb_file.txt', 'a+')
prep_file = open('prep_file.txt', 'a+')
adv_file = open('adv_file.txt', 'a+')

# print(all_lines)
print(all_lines[12].split(','))
print(len(all_lines[12].split(',')))
for lines in all_lines:
	words = lines.split(",")
	text = words[0]
	if(len(words) > 1):
		if words[1] == ' n\n':
			noun_file.write(text + ",")
			noun_count +=1
		elif words[1] == ' adj\n':
			adj_file.write(text + ",")
			adj_count +=1
		elif words[1] == ' conj\n':
			conj_file.write(text +",")
			conj_count +=1
		elif words[1] == ' v\n':
			verb_file.write(text + ",")
			verb_count +=1
		elif words[1] == ' prep\n':
			prep_file.write(text + ",")
			prep_count +=1
		elif words[1] == ' adv\n':
			adv_file.write(text + ",")
			adv_count +=1
		else : 
			pass
print(adj_count)
noun_file.close()
adj_file.close()
conj_file.close()
verb_file.close()
prep_file.close()
adv_file.close()
print("Done !")