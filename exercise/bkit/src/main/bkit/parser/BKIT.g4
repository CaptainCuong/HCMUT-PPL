grammar BKIT;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

/*
program  : mptype 'main' LB RB LP body? RP EOF ;

mptype: INTTYPE | VOIDTYPE ;

body: funcall SEMI;

exp: funcall | INTLIT ;

funcall: ID LB exp? RB ;

INTTYPE: 'int' ;

VOIDTYPE: 'void'  ;

ID: [a-zA-Z]+ ;

INTLIT: [0-9]+;

LB: '(' ;

RB: ')' ;

LP: '{';

RP: '}';

SEMI: ';' ;
*/

/*
prog : SCI_FLOAT;

SCI_FLOAT : REAL
		  | FLOAT 'e' '-'? REAL
		  | REAL 'e' '-'? REAL
;

FLOAT: REAL '.' REAL;

REAL : [0-9]+;
*/

/*
prog : ID;

IDENT1: [1-9][0-9]*;
IDENT2: IDENT1 (('_')[0-9]+)* {self.text = self.text.replace('_', '')};
ID : IDENT1 | IDENT2 |'0';
*/

prog : ADDRS;

ADDRS : NUM '.' NUM '.' NUM '.' NUM; 

fragment NUM : DIGIT 
			 | [1-9] DIGIT 
			 | '1' DIGIT DIGIT 
			 | '2' [0-5] DIGIT 
			 | '25' [0-5];

fragment DIGIT : [0-9];


WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

ERROR_CHAR: . {raise ErrorToken(self.text)};
