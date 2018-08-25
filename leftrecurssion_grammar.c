#include<stdio.h>
#include<ctype.h>
#include<string.h>

void r_leftrec(char grammar[])
{
char alpha[20],beta[20];
int m,h,k=0,l=0;
for(m=0;m<20;m++)
{
alpha[m]='\0';
beta[m]='\0';
}

for(m=4;m<strlen(grammar);m++)
{
if(grammar[m]=='|')
h=m;
if(m<h){
alpha[k]=grammar[m];
k++;}
}

for(m=h+1;m<strlen(grammar);m++)
{
beta[l]=grammar[m];
l++;}
printf("%c->%s%c'\n",grammar[0],beta,grammar[0]);
printf("%c'->%s%c'|\u03B5 \n",grammar[0],alpha,grammar[0]);

}

void main(){
int i,n,m,t=0;
char grammar[10][20];

for(i=0;i<10;i++){
for(m=0;m<20;m++)
{
grammar[i][m]='\0';
}
}
printf("enter no of lines of grammar\n");
scanf("%d",&n);
printf("enter grammar in format of S->S\u03B1|\u03B2\n");
for(i=0;i<n;i++)
{
scanf("%s",grammar[i]); 
}

for(i=0;i<n;i++){
if((grammar[i][0]==grammar[i][3])&&isupper(grammar[i][0])&&isupper(grammar[i][3]))
{
for(m=3;m<strlen(grammar[i]);m++)
{
if((grammar[i][m]=='|')&&m<(strlen(grammar[i])-1))
{
t=1;
r_leftrec(grammar[i]);
}

}

}


}


if(t==1)
printf("grammar left reccursion has been removed\n");
else
printf("no left reccursion is present\n");

}
