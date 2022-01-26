grammar D96;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}


program: class_dcl+ EOF;
//program : expr EOF;

class_dcl : CLASS ID (CL id_list)? class_body;

class_body : LP (att_dcl | method_dcl)* RP;

//inside_body :
//            | att_dcl inside_body
//            | method_dcl inside_body;

att_dcl : VAL_VAR static_id_list CL data_type SEMI // not assigned
        | VAL_VAR (ID | DOLLAR_ID) att_dcl_list expr SEMI; // assigned

att_dcl_list : CL data_type ASSIGN_OP
             | CM (ID | DOLLAR_ID) att_dcl_list expr CM;

method_dcl : (DESTRUCTOR | CONSTRUCTOR | ID | DOLLAR_ID) LB para_dcl_smcllist RB block_stm;

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

instance_method_invoke : ID DOT ID LB para_pass_list RB;

static_mehod_invoke : ID MEM_ACCESS_OP DOLLAR_ID LB para_pass_list RB;

para_pass_list :
               | lit_list | id_list
               | lit_list CM id_list;

att_access : instance_att_access | static_att_access;

instance_att_access : ID DOT ID;

static_att_access : ID MEM_ACCESS_OP DOLLAR_ID;

index_ele : (ID | att_access) (LS int_object RS)+;

int_object : int_gen | ID | att_access;

float_object : FLOATLIT | ID | att_access;


index_arr_list :
               | index_arr index_arr_cmlist;

index_arr_cmlist :
                 | CM index_arr index_arr_cmlist;

index_arr : ARRAY LB same_type_list RB;

mul_dim_arr : ARRAY LB index_arr_list RB;




same_type_list : int_gen_list | bool_list | float_list | string_list;

string_op : STR_CMP | STR_CONCAT;

bool_op : NEGATE | OR | AND | EQUAL | NOT_EQUAL;

relation_op : LESS_THAN | NOT_EQUAL | EQUAL | GREAT_THAN;

int_op : ADDOP | LESS_EQUAL | GREAT_EQUAL | SUBOP | MULOP | LESS_THAN | MODOP | DIVOP | NOT_EQUAL | EQUAL;

float_op : ADDOP | LESS_EQUAL | GREAT_EQUAL | SUBOP | MULOP | LESS_THAN | NOT_EQUAL;

lit_list :
         | lit lit_cmlist;

lit_cmlist :
           | CM lit lit_cmlist;

static_id_list :
        | DOLLAR_ID static_id_cmlist;

static_id_cmlist :
                 | CM DOLLAR_ID static_id_cmlist;

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
		   | STRINGLIT string_list_cm;

string_list_cm :
			   | CM STRINGLIT string_list_cm;

lit : FLOATLIT | BOOLIT | STRINGLIT | int_gen;

int_gen : INTLIT_16 | INTLIT_2 | INTLIT_8 | INTLIT_10;

data_type : INT_TYPE | FLOAT_TYPE | BOOL_TYPE | array_type;

size : int_gen;

array_type : ARRAY LS data_type CM size RS;

unary_op : SUBOP | NEGATE;

binary_op : ADDOP | LESS_EQUAL | LESS_THAN | GREAT_EQUAL
          | GREAT_THAN | SUBOP | MULOP | LESS_THAN | MODOP
          |DIVOP | NOT_EQUAL | EQUAL | AND | OR | STR_CMP | STR_CONCAT;

STRINGLIT : '""' // Case 1: There is no character
          | '"' ('\'"' | '\\' [btnfr'\\] | ~[\r\t\n\\"] )* ('\'"' | '\\' [btnfr'\\] | ~[\r\t\n\\"'] )'"'; // Case 2: There is at least 1 character -> The single quote can not stand at the end of string

MEM_ACCESS_OP : '::';

NEW : 'New';

RETURN : 'Return';

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

FLOATLIT : (INTLIT_10 EXPONENT
		 | INTLIT_10? DOT (ZERO* INTLIT_10)? EXPONENT?)
		 {self.text = self.text.replace("_","")};

BY : 'By';

BOOLIT : 'True' | 'False';

VAL_VAR : 'Val' | 'Var';

//STATIC : '$';

ARRAY : 'Array';

INT_TYPE : 'Int';

FLOAT_TYPE : 'Float';

BOOL_TYPE : 'Boolean';

INTLIT_16 : ('0'[xX][0-9A-F]
		  | '0'[xX][1-9A-F][0-9A-F_]*[0-9A-F])
		  {self.text = self.text.replace("_","")};

INTLIT_2 : ('0'[bB]'0'
		 | '0'[bB]'1'
		 | '0'[bB]'1'[0-1_]*[0-1]) 		 
		 {self.text = self.text.replace("_","")};

INTLIT_8 : ('0'[0-7]
		 | '0'[1-7][0-7_]*[0-7]) 
		 {self.text = self.text.replace("_","")};


INTLIT_10 : ([1-9]'_'?([0-9]'_'?)*[0-9] | [0-9]) {self.text = self.text.replace("_","")};

fragment LIT : [a-zA-Z_];

fragment EXPONENT : ([eE][-+]?'0'*INTLIT_10);

DOLLAR_ID : '$'[0-9a-zA-Z_]+;

ID : [a-zA-Z_] [0-9a-zA-Z_]*;

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

COMMENT : '##' .*? '##' ->skip ;

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines
ILLEGAL_ESCAPE: ( '"' ('\\'[bfrnt\\'] | ~[\n\r\\"])* ('\\'(~[bfrnt'\\]))) {self.text = self.text.replace('"',''); raise IllegalEscape(self.text)};
UNCLOSED_STRING: ( '"' ('\'"' | '\\' [btnfr'\\] | ~[\r\t\n\\"] )* ) {self.text = self.text.replace('"',''); raise UncloseString(self.text)};
ERROR_CHAR: . {raise ErrorToken(self.text)};