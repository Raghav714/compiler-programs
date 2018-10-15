def lcs(X, Y,m,n):
    if m == 0 or n == 0:
       return 0;
    elif X[m-1] == Y[n-1]:
       return 1 + lcs(X, Y, m-1, n-1);
    else:
       return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n));
def left_factoring(grammer):
	small_prod = ""
	for key in grammer.copy(): 
		item = grammer[key]
		mi = len(item[0])
		for prod in item:
			if mi >len(prod):
				mi= len(prod)
				small_prod = prod
		for prod in item:
			x = lcs(prod , small_prod,len(prod),len(small_prod))		
			if mi>=x:
				mi = x
		if(x>0):
			c=0
			for p in item:
				fac=p[0:mi]
				grammer[key][c]=p[mi:]
				c=c+1	
			grammer.update({key+"'":[fac]})
	print grammer
grammar = {}
lis = list()
le = input("length")
for i in range(0,le):
	key = raw_input("key")
	l = input("number of production")
	lis = list()
	for i in range(0,l):
		lis.append(raw_input())
	grammar.update({key:lis})
#grammar = {"S":["abAB","abc","abcdA"],"A":["d","psln"],"B":["e","psln"]}
#grammar = {"S":["abAB","abc","abcdA"]}
print "the given grammar grammar\n",grammar
print "removing left factoring free grammer"
left_factoring(grammar)
