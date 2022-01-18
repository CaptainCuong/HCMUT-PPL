grammar BKOOL;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

/*
program  : ID ;

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
prog : STRING;

STRING : '\'' STR '\'';

fragment STR : ([-.?A-Za-z0-9 ] | DOUBLE_QUOTE)+  ; 
fragment DOUBLE_QUOTE : '\'\'';
*/

/*
program : vardecl
		| funcdecl;
*/




program: mndcl;

mndcl : dcl mndcl | ;

dcl : func_dcl | var_dcl;

var_dcl : VARTYPE var_list SEMI; 



/*     List of variable   */
var_list : ID 
		 | var_list_prime ID
;

var_list_prime : ID CM var_list_prime |;



func_dcl : VARTYPE ID para_dcl body;

para_dcl : '(' mnvar_dcl  ')';

mnvar_dcl : dcl_without_semi
		  | (var_dcl)* dcl_without_semi
		  |
;

dcl_without_semi : VARTYPE var_list; 



body : LP (stm | var_dcl)* RP;

stm : asm SEMI| call SEMI| ret SEMI;

asm : ID EQUAL expr;

call : ID LB expr_list RB;

ret : RET expr;

expr: expr DIVOP expr
	| expr MULOP expr
	| expr MINOP expr
	| expr ADDOP expr
	| call
	| ID
	| INTLIT
	| FLOATLIT
;

expr_list : 
		  | expr
		  | expr expr_list_prime;

expr_list_prime : CM expr expr_list_prime | ;

FLOATLIT : [0-9]+ '.' [0-9]+;

RET : 'return' ;

DIVOP : '/' ;

MULOP : '*' ;

ADDOP : '+' ;

MINOP : '-' ;

EQUAL : '=' ;

LB: '(' ;

RB: ')' ;

LP: '{';

RP: '}';

VARTYPE : 'int' | 'float';

CM : ',';

ID: [a-zA-Z]+;// includes a sequence of alphabetic characters.

INTLIT : [0-9]+ ;

SEMI: ';' ;


vardecl: 'vardecl' ;

funcdecl: 'funcdecl' ;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: . {raise ErrorToken(self.text)};
/*
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
*/