%{
int lines=0,  s_c=0,s_a=0,num=0,sp_c=0,spa=0,word=0;
%}
%%
\n { lines++;}
[' '] {spa++;}
[\t ' ']  {word++;}
[a-z]  { s_c++;}
[A-Z]  { s_a++;}
[0-9] {num++;}
.    {sp_c++; }
%%
int main(){
yyin=fopen("demop.txt", "r"); 
yylex();
if(lines!=0){
printf(" Number of Lines= %d\n", lines+1);}
printf(" Number of Small Case letters= %d\n", s_c);
printf("Number of Upper Case Letters = %d\n",s_a);
printf("Number of digits = %d\n",num);
printf("Number of special characters = %d\n",sp_c);
printf("Number of spaces = %d\n",spa);
printf("Number of characters = %d\n",s_c + s_a + num + sp_c);
printf("Number of words = %d\n",word);
return 0;}
 int yywrap() {
 return 1; }