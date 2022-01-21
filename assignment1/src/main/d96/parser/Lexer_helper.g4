lexer grammar Lexer_helper;

FLOATLIT : INTLIT_10 DOT (ZERO* INTLIT_10)?
		 | INTLIT_10 EXPONENT;

BOOLIT : 'True' | 'False';

ID : LIT ([0-9] | LIT)*;

ARRAY : 'Array';

INT_TYPE : 'Int';

FLOAT_TYPE : 'Float';

BOOL_TYPE : 'Boolean';

INTLIT_16 : '0'[xX][0-9A-F];

INTLIT_2 : '0b'[0-1]+;

INTLIT_8 : '0'[0-7]+;


INTLIT_10 : [1-9][0-9_]*[0-9] | [0-9];

fragment LIT : [a-zA-Z_];

CLASS : 'Class' ;

EXPONENT : [eE][-+]*;

START_STRING : '"' -> mode(STRING_INSIDE);

//STRING : START_STRING (DOUB_QUOTE | ESCAPE_SEQ | STRING_CHAR)*? END_STRING;

ZERO : '0';

DOT : '.';

CM : ',';

LS : '[';

RS : ']';

LB: '(';

RB: ')';

LP: '{';

RP: '}';

SEMI: ';';

ADDOP : '+';

LESS_EQUAL : '<=';

GREAT_EQUAL : '>=';

SUBOP : '-';

MULOP : '*';

LESS_THAN : '<';

MODOP : '%';

DIVOP : '/';

NOT_EQUAL : '!=';

EQUAL : '==';

GREAT_THAN : '>';

AND : '&&';

OR : '||';

NEGATE : '!';

STR_CMP : '==.';

STR_CONCAT : '+.';

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;

mode STRING_INSIDE;

DOUB_QUOTE : '\'"';

END_STRING : '"' -> mode(DEFAULT_MODE);

ESCAPE_SEQ : [\b\f\r\n\t'\\];

STRING_CHAR : .;