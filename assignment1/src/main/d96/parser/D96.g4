grammar D96;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: ('class' ID LP body? RP)* EOF;


body: (funcdef | mem_list)*;


/************************************************/
funcdef: ID LB  RB LP  func_body?  RP;



func_body: ;



/************************************************/
MEM_LIST: INITIALIZER ' ' ID_LIST  ':' mptype '=' EXP_LIST;


ID_LIST : ID ',' ID_LIST
		| ID SEMI
;


EXP_LIST : exp ',' EXP_LIST
		 | exp SEMI
;


/************************************************/
BLOCK_STM : LP MEM_LIST RP 



/************************************************/
ARI_OPRT : '-'
		 | '+'
		 | '-'
		 | '*'
		 | '%'
;

BOOL_OPRT : '!'
		  | '&&'
		  | '||'
		  | '=='
;

STR_OPRT : '+.';

IDX_OPRT : '[' exp ']';








INITIALIZER: 'val' | 'var';

mptype: INTTYPE | VOIDTYPE;

exp: funcall | INTLIT;

funcall: ID LB exp? RB;

INTTYPE: 'Int';

VOIDTYPE: 'void';

ID: '$'? [a-zA-Z]+;

INTLIT: [0-9]+;

LB: '(';

RB: ')';

LP: '{';

RP: '}';

SEMI: ';';

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;

