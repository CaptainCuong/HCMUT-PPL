grammar MP;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: vardecl+ EOF;

vardecl: mptype ids SEMI;

mptype: INTTYPE | FLOATTYPE;

ids: ID (COMMA ID)*; 

INTTYPE: 'int';

FLOATTYPE: 'float';

SEMI: ';' ;

COMMA: ',' ;

ID: [a-z]+ ;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

ERROR_CHAR: .;
