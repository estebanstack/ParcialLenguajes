grammar Fibo;

prog: 'FIBO' '(' INT ')' EOF ;

INT : [0-9]+ ;
WS  : [ \t\r\n]+ -> skip ;
