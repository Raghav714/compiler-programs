## Left Recursion ##
The left recursion from a grammar is removed in the *left_recursion.py*
to run the program :- $python left_recursion.py<br /> 
length3<br />
keyE<br />
number of production2<br />
E+F<br />
F<br />
keyF<br />
number of production2<br />
F*G<br />
G<br />
keyG<br />
number of production2<br />
(G)<br />
i<br />
{'E': ['E+F', 'F'], 'G': ['(G)', 'i'], 'F': ['F*G', 'G']}<br />
left recursion found<br />
left recursion found<br />
{"E'": ['', "+FE'"], "F'": ['', "*GF'"], 'E': "FE'", 'G': ['(G)', 'i'], 'F': "GF'"}<br />
The obtained output is left recursion free.
## Left Factoring ##
The left factoring is removed in *left_fact.py*<br />
to run the program :- $python left_fact.py <br />
length01<br />
keyE<br />
number of production4<br />
abAB<br />
abCD<br />
abEF<br />
ab<br />
the given grammar grammar<br />
{'E': ['abAB', 'abCD', 'abEF', 'ab']}<br />
removing left factoring free grammer<br />
{"E'": ['ab'], 'E': ['AB', 'CD', 'EF', '']}<br />
The obtained grammar is left factoring free.
## Lexical Analyser ##
lexical analyser is bulid using using PLY python programing language and lex tool.<br />
lexical_lex.py contain python implemented code of lex, it will list out all the token present in sum.c<br />
to run the program :- $python lexical_lex.py <br />
LexToken(INCLUDE,'#include',1,0)<br />
LexToken(LESSER,'<',1,8)<br />
LexToken(ID,'stdio',1,9)<br />
Illegal character '.'<br />
LexToken(ID,'h',1,15)<br />
LexToken(GREATER,'>',1,16)<br />
LexToken(VOID,'void',2,18)<br />
LexToken(FUNCTION,'main(',2,23)<br />
LexToken(RPAREN,')',2,28)<br />
LexToken(LBRAC,'{',3,30)<br />
LexToken(INT,'int',5,43)<br />
LexToken(ID,'a',5,47)<br />
LexToken(COMMA,',',5,48)<br />
LexToken(ID,'b',5,49)<br />
LexToken(COLON,';',5,50)<br />
LexToken(PRINTF,'printf(',6,52)<br />
LexToken(RPAREN,')',6,77)<br />
LexToken(COLON,';',6,78)<br />
LexToken(SCANF,'scanf(',7,80)<br />
LexToken(COMMA,',',7,92)<br />
Illegal character '&'<br />
LexToken(ID,'a',7,94)<br />
LexToken(COMMA,',',7,95)<br /><br />
Illegal character '&'<br />
LexToken(ID,'b',7,97)<br />
LexToken(RPAREN,')',7,98)<br />
LexToken(COLON,';',7,99)<br />
LexToken(INT,'int',8,101)<br />
LexToken(ID,'s',8,105)<br />
LexToken(EQUAL,'=',8,107)<br />
LexToken(ID,'a',8,109)<br />
LexToken(PLUS,'+',8,110)<br />
LexToken(ID,'b',8,111)<br />
LexToken(COLON,';',8,112)<br />
LexToken(PRINTF,'printf(',9,114)<br />
LexToken(COMMA,',',9,132)<br />
LexToken(ID,'s',9,133)<br />
LexToken(RPAREN,')',9,134)<br />
LexToken(COLON,';',9,135)<br />
LexToken(RBRAC,'}',10,137)<br />
## First, Follow and LL1  table ##
The program first.py will calculate first the program will automatically remove all left factoring and left recursion in the grammar.
the ll1table.py contain first, follow and ll1 table in the code.
the code is broken down into the different different function.
## Calculator design using lex and yacc ##
A basic calculator is designed using the grammar.
the calculator perform addition, subtraction, multiplication , divison and negation of the numbers in the equation
cal_lex.l is the lex code lexically analyse the grammar
cal_yac.y is the yacc code to sematically analyse the grammar
command to run the code:-
$lex cal_lex.l<br />
$yacc cal_yac.y<br />
$gcc y.tab.c -ly -lfl -lm<br />
$./a.out<br />
Enter the expression: 2+3+4
Answer: 9 
Enter:

## Other program ##
assignement.l is the lex code written to perform five task:-
1. count the word start with vowel along with position of word.
2. count the word start with consonats along with position of word.
3. count the article along with position.
4. count the numbers along with position.
5. count number of line in file.
