grammar BKOOL;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program  : mptype 'main' LB RB LP body? RP EOF ;


mptype: INTTYPE | VOIDTYPE ;

body: funcall SEMI;

exp: funcall | INTLIT | FLOATLIT
	| expr1 (ADDOP | MINOP) expr1;

expr1: expr1 (MULOP | DIVOP) expr1
	| expr | INTLIT | FLOATLIT;

ADDOP: '+';

MINOP: '-';

MULOP: '*';

DIVOP: '/';


funcall: ID LB exp? RB ;

INTTYPE: 'int' ;

FLOATTYPE: 'float' ;

VOIDTYPE: 'void'  ;

ID: [a-zA-Z]+ ;

FLOATLIT: [0-9]*'.'[0-9]+;

INTLIT: [0-9]+;

LB: '(' ;

RB: ')' ;

LP: '{';

RP: '}';

SEMI: ';' ;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;