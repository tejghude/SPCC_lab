%{
int lines=0, ch=0, words=0, space=0 , uc=0  , sc=0  ,num=0 , sch=0 ,dt=0 ;
%}
digit [0-9]
letter [a-zA-Z]
%%
\n    {lines++;words++;}
[' ']  {space++;words++;}
[A-Z]   {uc++;}
[a-z]   {sc++;}
[0-9]   {dt++;}
{digit}+ {num++;}
.    {sch++;}
%%

int main(){
yyin= fopen("demop.txt", "r");
yylex();
printf("Lines = %d\n", lines);
printf("Words = %d\n", words);
printf("Space = %d\n", space);
printf("Number = %d\n", num);
printf("Uppercase = %d\n", uc);
printf("Smallcase = %d\n", sc);
printf("special character = %d\n", sch);
return 0;
}
int yywrap()
{
return 1;
}