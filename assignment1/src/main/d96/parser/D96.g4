grammar D96;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}


program: class_dcl+ EOF;

comment : DOUB_HASH_MARK .*? DOUB_HASH_MARK;

class_dcl : CLASS ID class_body;

class_body : LP (var_dcl | method_dcl)* RP;

method_dcl : (DESTRUCTOR | CONSTRUCTOR | ID) LB para_dcl_smcllist RB block_stm;

para_dcl_list :
              | para_dcl para_dcl_smcllist;

para_dcl_smcllist :
                  | SEMI para_dcl para_dcl_smcllist;

para_dcl : id_list CL data_type;

stm : (asm_stm | var_dcl | break_stm | continue_stm | return_stm | method_invoke_stm) SEMI
    | if_stm | for_in_stm;

for_in_stm : FOREACH LB ID int_gen RANGE int_gen (BY int_gen)? RB block_stm;

if_stm: IF LB expr RB block_stm (ELSEIF LB expr RB block_stm)* (ELSE block_stm)?;

block_stm : LP mn_stm RP;

mn_stm :
       | stm mn_stm;

continue_stm : CONTINUE;

break_stm : BREAK;

asm_stm : ID ASSIGN_OP expr;

return_stm : RETURN expr;

method_invoke_stm : instance_method_invoke | static_mehod_invoke;

var_dcl : VAL_VAR ID var_dcl_list expr;

var_dcl_list : CL data_type ASSIGN_OP
             | CM ID var_dcl_list expr CM;

expr_list :
          | expr expr_cmlist;

expr_cmlist : | CM expr expr_cmlist;

expr : ID | index_ele | object_ini | lit
     | instance_method_invoke | static_mehod_invoke | instance_att_access | static_att_access
     | expr binary_op expr
     | unary_op expr
     ;

object_ini : NEW ID LB expr_list RB;

instance_method_invoke : ID DOT ID LB expr_list RB;

static_mehod_invoke : ID MEM_ACCESS_OP ID LB expr_list RB;

instance_att_access : ID DOT ID;

static_att_access : ID MEM_ACCESS_OP ID;

index_ele : ID LS int_gen_list RS;



index_arr_list :
               | index_arr index_arr_cmlist;

index_arr_cmlist : CM index_arr index_arr_list | ;

index_arr : ARRAY LB same_type_list RB;

mul_dim_arr : ARRAY LB index_arr_list RB;










same_type_list : int_gen_list | bool_list | float_list | string_list;

string : START_END_STRING (DOUB_QUOTE | ~'"' )*? START_END_STRING;

string_op : STR_CMP | STR_CONCAT;

bool_op : NEGATE | OR | AND | EQUAL | NOT_EQUAL;

relation_op : LESS_THAN | NOT_EQUAL | EQUAL | GREAT_THAN;

int_op : ADDOP | LESS_EQUAL | GREAT_EQUAL | SUBOP | MULOP | LESS_THAN | MODOP | DIVOP | NOT_EQUAL | EQUAL;

float_op : ADDOP | LESS_EQUAL | GREAT_EQUAL | SUBOP | MULOP | LESS_THAN | NOT_EQUAL;



id_list :
        | ID id_cmlist;

id_cmlist :
          | CM ID id_cmlist;

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
		   | string string_list_cm;

string_list_cm :
			   | CM string string_list_cm;

lit : FLOATLIT | BOOLIT | string | int_gen;

int_gen : INTLIT_16 | INTLIT_2 | INTLIT_8 | INTLIT_10;

data_type : INT_TYPE | FLOAT_TYPE | BOOL_TYPE;

size : int_gen;

array_type : ARRAY LS data_type CM size RS;

unary_op : SUBOP | NEGATE;

binary_op : ADDOP | LESS_EQUAL | LESS_THAN | GREAT_EQUAL
          | GREAT_THAN | SUBOP | MULOP LESS_THAN | MODOP
          |DIVOP | NOT_EQUAL | EQUAL | AND | OR | STR_CMP | STR_CONCAT;











MEM_ACCESS_OP : '::';

NEW : 'New';

RETURN : 'Return';

DOUB_HASH_MARK : '##';

ASSIGN_OP : '=';

BREAK : 'Break';

CONTINUE : 'Continue';

IF : 'If';

ELSE : 'Else';

ELSEIF : 'Elseif';

FOREACH : 'Foreach';

IN : 'In';

CONSTRUCTOR : 'Constructor';

DESTRUCTOR : 'Destructor';

CLASS : 'Class';












FLOATLIT : INTLIT_10 DOT (ZERO* INTLIT_10)?
		 | INTLIT_10 EXPONENT;

BOOLIT : 'True' | 'False';

VAL_VAR : 'Val' | 'Var';

STATIC : '$';

ARRAY : 'Array';

INT_TYPE : 'Int';

FLOAT_TYPE : 'Float';

BOOL_TYPE : 'Boolean';

INTLIT_16 : '0'[xX][0-9A-F];

INTLIT_2 : '0b'[0-1]+;

INTLIT_8 : '0'[0-7]+;


INTLIT_10 : [1-9][0-9_]*[0-9] | [0-9];

fragment LIT : [a-zA-Z_];

EXPONENT : [eE][-+]?'0'*INTLIT_10;

START_END_STRING : '"';

DOUB_QUOTE : '\'"';

//ESCAPE_SEQ : [\b\f\r\n\t'\\];

//STRING : START_STRING (DOUB_QUOTE | ESCAPE_SEQ | STRING_CHAR)*? END_STRING;

ID : LIT ([0-9] | LIT)*;

ZERO : '0';

DOT : '.';

CM : ',';

LS : '[';

RS : ']';

LB: '(';

RB: ')';

LP: '{';

RP: '}';

RANGE : '..';

BY : 'By';

CL : ':';

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
//UNCLOSE_STRING: .;
//ILLEGAL_ESCAPE: .;