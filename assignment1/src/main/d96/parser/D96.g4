grammar D96;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}


//program: class_dcl+ EOF;
program : expr EOF;

comment : DOUB_HASH_MARK .*? DOUB_HASH_MARK;

class_dcl : CLASS ID (CL id_list)? class_body;

class_body : LP (att_dcl | method_dcl)* RP;

//inside_body :
//            | att_dcl inside_body
//            | method_dcl inside_body;

att_dcl : VAL_VAR static_id_list CL data_type SEMI // not assigned
        | VAL_VAR STATIC? ID att_dcl_list expr SEMI; // assigned

att_dcl_list : CL data_type ASSIGN_OP
             | CM STATIC? ID att_dcl_list expr CM;

method_dcl : STATIC? (DESTRUCTOR | CONSTRUCTOR | ID) LB para_dcl_smcllist RB block_stm;

para_dcl_list :
              | para_dcl para_dcl_smcllist;

para_dcl_smcllist :
                  | SEMI para_dcl para_dcl_smcllist;

para_dcl : id_list CL data_type;

stm : (asm_stm | var_dcl | break_stm | continue_stm | return_stm | method_invoke_stm) SEMI
    | if_stm | for_in_stm;

for_in_stm : FOREACH LB ID IN expr RANGE expr (BY expr)? RB block_stm;

if_stm: IF LB expr RB block_stm (ELSEIF LB expr RB block_stm)* (ELSE block_stm)?;

block_stm : LP mn_stm RP;

mn_stm :
       | stm mn_stm;

continue_stm : CONTINUE;

break_stm : BREAK;

asm_stm : (ID | att_access | index_ele) ASSIGN_OP expr;

return_stm : RETURN expr;

method_invoke_stm : instance_method_invoke | static_mehod_invoke;

var_dcl : VAL_VAR id_list CL data_type // not assigned
        | VAL_VAR ID var_dcl_list expr; // assigned

var_dcl_list : CL data_type ASSIGN_OP
             | CM ID var_dcl_list expr CM;

expr_list :
          | expr expr_cmlist;

expr_cmlist : | CM expr expr_cmlist;

expr : ID | index_ele | object_ini | lit
     | instance_method_invoke | static_mehod_invoke | instance_att_access | static_att_access
     | expr binary_op expr
     | unary_op expr
     | LB expr RB
     ;

object_ini : NEW ID LB expr_list RB;

instance_method_invoke : ID DOT ID LB expr_list RB;

static_mehod_invoke : ID MEM_ACCESS_OP STATIC ID LB expr_list RB;

att_access : instance_att_access | static_att_access;

instance_att_access : ID DOT ID;

static_att_access : ID MEM_ACCESS_OP STATIC ID;

index_ele : (ID | att_access) (LS int_object RS)+;

int_object : int_gen | ID | att_access;

float_object : floatlit | ID | att_access;


index_arr_list :
               | index_arr index_arr_cmlist;

index_arr_cmlist :
                 | CM index_arr index_arr_cmlist;

index_arr : ARRAY LB same_type_list RB;

mul_dim_arr : ARRAY LB index_arr_list RB;










same_type_list : int_gen_list | bool_list | float_list | string_list;

string : START_END_STRING (DOUB_QUOTE | ~'"' )*? START_END_STRING;

string_op : STR_CMP | STR_CONCAT;

bool_op : NEGATE | OR | AND | EQUAL | NOT_EQUAL;

relation_op : LESS_THAN | NOT_EQUAL | EQUAL | GREAT_THAN;

int_op : ADDOP | LESS_EQUAL | GREAT_EQUAL | SUBOP | MULOP | LESS_THAN | MODOP | DIVOP | NOT_EQUAL | EQUAL;

float_op : ADDOP | LESS_EQUAL | GREAT_EQUAL | SUBOP | MULOP | LESS_THAN | NOT_EQUAL;


static_id_list :
        | STATIC? ID static_id_cmlist;

static_id_cmlist :
                 | CM STATIC? ID static_id_cmlist;

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
		   | floatlit float_list_cm;

float_list_cm :
			  | CM floatlit float_list_cm;

string_list :
		   | string string_list_cm;

string_list_cm :
			   | CM string string_list_cm;

lit : floatlit | BOOLIT | string | int_gen;

int_gen : INTLIT_16 | INTLIT_2 | INTLIT_8 | INTLIT_10;

data_type : INT_TYPE | FLOAT_TYPE | BOOL_TYPE;

size : int_gen;

array_type : ARRAY LS data_type CM size RS;

unary_op : SUBOP | NEGATE;

binary_op : ADDOP | LESS_EQUAL | LESS_THAN | GREAT_EQUAL
          | GREAT_THAN | SUBOP | MULOP | LESS_THAN | MODOP
          |DIVOP | NOT_EQUAL | EQUAL | AND | OR | STR_CMP | STR_CONCAT;


MEM_ACCESS_OP : '::';

NEW : 'New';

RETURN : 'return';

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












floatlit : INTLIT_10 DOT (ZERO* INTLIT_10)?
		 | INTLIT_10 EXPONENT;

BY : 'By';

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


INTLIT_10 : [1-9]'_'?([0-9]'_'?)*[0-9] | [0-9];

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
//UNCLOSE_STRING: . raise ;
//ILLEGAL_ESCAPE: .;