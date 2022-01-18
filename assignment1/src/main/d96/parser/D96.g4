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


stm : exp SM;

exp : ID EQUAL exp
	| ID LB exp_list RB
	| 




A program in mC consists of many declarations, which are variable and function declarations.
program -> manydecls EOF
manydecls -> decl decls
decls: decl decls | empty
decl: variable_decl | function_decl;





A variable declaration starts with a type, which is int or float, then a comma-separated list of identifiers and ends with a semicolon
variable_decl -> mctype id_list SM
Id_list -> ID plist
Plist -> CM ID plist | empty		

mctype : INT | FLOAT; 



A function declaration also start with a type and then an identifier, which is the function name, and then parameter declaration and ends with a body.  

function_decl  -> mctype ID param_decl body			



The parameter declaration starts with a left round bracket ’(’ and a null-able semicolon-separated list of parameters and ends with a right round bracket ’)’.  
param_decl -> LP sm_list RP

sm_list -> param sm_plist | empty
sm_plist -> SM param sm_plist | empty				



Each parameter always starts with a type and then a comma-separated list of identifier. 

param → mctype id_list



A body starts with a left curly bracket ’{’, follows by a null-able list of 
variable declarations or statements and ends with a right curly bracket ’}’. 
 
Body -> LB var_stm_list RB
var_stm_list -> var_stm var_stm_plist |empty
var_stm_plist -> var_stm var_stm_plist | empty 	
var_stm -> variable_decl | stm 



There are 3 kinds of statements: assignment, call and return.  

Stm -> assignment SM | call SM | return SM



All statements must end with a semicolon. An assignment statement starts with an identifier, then an equal ’=’, then an expression.

assignment -> ID EQ exp
		











many -> one
Minimum: zero | one
Separator: have | don't have
many -> one manyprime  | Empty
manyprime -> separator one manyprime | empty







many -> one manyprime  | Empty
manyprime -> separator one manyprime | empty
