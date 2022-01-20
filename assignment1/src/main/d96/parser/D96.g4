parser grammar D96;

@lexer::header {
from lexererr import *
}

options {
//	language = Python3;
	tokenVocab= Lexer_helper;
}


program: string EOF;

string : START_STRING (DOUB_QUOTE | ESCAPE_SEQ | STRING_CHAR)*? END_STRING;

string_op : STR_CMP | STR_CONCAT;

bool_op : NEGATE | OR | AND | EQUAL | NOT_EQUAL;

relation_op : LESS_THAN | NOT_EQUAL | EQUAL | GREAT_THAN;

int_op : ADDOP | LESS_EQUAL | GREAT_EQUAL | SUBOP | MULOP | LESS_THAN | MODOP | DIVOP | NOT_EQUAL | EQUAL;

float_op : ADDOP | LESS_EQUAL | GREAT_EQUAL | SUBOP | MULOP | LESS_THAN | NOT_EQUAL;

int_gen_list :
			 | int_gen int_gen_cm;

int_gen_cm :
			   | CM int_gen int_gen_cm;

bool_list :
		  | BOOLIT bool_list_cm;

bool_list_cm :
			 | CM BOOLIT bool_list_cm;

float_list :
		   | FLOATLIT float_list_cm;

float_list_cm :
			  | CM FLOATLIT float_list_cm;

string_list :
		   | STRING string_list_cm;

string_list_cm :
			   | CM STRING string_list_cm;

lit : FLOATLIT | BOOLIT | STRING | int_gen;

//STRING : DOUB_QUOTE (ESC_DOUB_QUOTE | ESCAPE_SEQ | .)*? DOUB_QUOTE;

//FLOATLIT : INTLIT_10 DOT (ZERO* INTLIT_10)?
//		 | INTLIT_10 EXPONENT;

int_gen : INTLIT_16 | INTLIT_2 | INTLIT_8 | INTLIT_10;

//BOOLIT : 'True' | 'False';
//
//ID : LIT ([0-9] | LIT)*;
//
//INTLIT_16 : '0'[xX][0-9A-F];
//
//INTLIT_2 : '0b'[0-1]+;
//
//INTLIT_8 : '0'[0-7]+;
//
//
//INTLIT_10 : [1-9][0-9_]*[0-9] | [0-9];
//
//fragment LIT : [a-zA-Z_];
//
//CLASS : 'Class' ;
//
//EXPONENT : [eE][-+]*;
//
//fragment ESC_DOUB_QUOTE : '\'"';
//
//DOUB_QUOTE : '"' -> mode(STRING);
//
//ESCAPE_SEQ : [\b\f\r\n\t'\\];
//
//ZERO : '0';
//
//DOT : '.';
//
//CM : ',';
//
//LB: '(';
//
//RB: ')';
//
//LP: '{';
//
//RP: '}';
//
//SEMI: ';';
//
//ADDOP : '+';
//
//LESS_EQUAL : '<=';
//
//GREAT_EQUAL : '>=';
//
//SUBOP : '-';
//
//MULOP : '*';
//
//LESS_THAN : '<';
//
//MODOP : '%';
//
//DIVOP : '/';
//
//NOT_EQUAL : '!=';
//
//EQUAL : '==';
//
//GREAT_THAN : '>';
//
//AND : '&&';
//
//OR : '||';
//
//NEGATE : '!';
//
//STR_CMP : '==.';
//
//STR_CONCAT : '+.';
//
//WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines
//
//ERROR_CHAR: . {raise ErrorToken(self.text)};
//UNCLOSE_STRING: .;
//ILLEGAL_ESCAPE: .;

