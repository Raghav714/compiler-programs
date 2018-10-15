from collections import OrderedDict
def find_substr(s, char):
    index = 0

    if char in s:
        c = char[0]
        for ch in s:
            if ch == c:
                if s[index:index+len(char)] == char:
                    return index

            index += 1

    return -1
def change_left(substring,key1,gram):
	return substring.replace(key1,gram)
def left_recursion(grammar):
	flag = 0
	pos = 0
	for key in grammar.copy(): 
		item = grammar[key]
		for prod in item:
			if key == prod[0:1]:
				#print "left recursion found"
				flag = 1
				pos = pos +1
				subfix = prod[1:len(prod)]
		if flag == 1:
			grammar[key] = [item[pos:len(item)][0]+key+"'"]
			grammar.update({key+"'":["epsln",subfix+key+"'"]})
			flag=pos=0
	return grammar

def first(grammar,terminal):
	for key in grammar.copy():
		lis = []
		for string in grammar.copy()[key]:
			for key1 in grammar.copy():
				if key1 in string:
					pos = find_substr(string,key1)
					for i in range(len(grammar[key1])):
						string1 = string[0:pos] + change_left(string[pos:pos+len(key1)],key1,grammar[key1][i]) + string[pos+len(key1):len(string)]
				else:
					string1 = string
			lis.append(string1)
		grammar.update({key:lis})
	first1 = {}
	for key in grammar.copy():
		firlis = []
		for ter in terminal:
			for string in grammar[key]:
				if string.find(ter)==0:
					firlis.append(ter)				
		first1.update({key:firlis})
		
	return first1
grammar = OrderedDict()
'''grammar = {}
le = input("length")
for i in range(le):
	key = raw_input("key")
	l = input("number of production")
	lis = list()
	for i in range(0,l):
		lis.append(raw_input())
	grammar.update({key:lis})'''
#grammar = {"S":["abAB","abc","abcdA"]}
#grammar = {"A":["ABD","Aa","a"],"B":["Bc","b"]}
#grammar = {"S":["SOS1S","01"]}
grammar = {"E":["E+F","F"],"F":["F*G","G"],"G":["(G)","id"]}
terminal = ["(",")","id","epsln","*","+"]
#grammar = {"E":["E+T","T"]}
#grammar = {"E":["TK"],"K":["+TK",""]}
grammar = left_recursion(grammar)
print grammar
print "----------------------------------------------"
x = first(grammar,terminal)
print x
