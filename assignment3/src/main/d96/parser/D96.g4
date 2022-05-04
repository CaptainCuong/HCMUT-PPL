grammar D96;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}


program: class_dcl+ EOF;

class_dcl : CLASS ID (CL ID)? class_body;

class_body : LP (att_dcl | method_dcl)* RP;

expr_pro : expr_lit | index_ele | index_ele_pro;

// 'att_dcl_list' has ASSIGN_OP
att_dcl : VAL_VAR id_list CL data_type SEMI // not assigned
        | VAL_VAR (ID | DOLLAR_ID) att_dcl_list expr_lit SEMI; // assigned

att_dcl_list : CL data_type ASSIGN_OP
             | CM (ID | DOLLAR_ID) att_dcl_list expr_lit CM;

method_dcl : (DESTRUCTOR | CONSTRUCTOR | ID | DOLLAR_ID) LB para_dcl_list RB method_block;

method_block : LP (stm | block_stm)* RP;

para_dcl_list :
              | para_dcl para_dcl_smcllist;

para_dcl_smcllist :
                  | SEMI para_dcl para_dcl_smcllist;

para_dcl : id_list CL data_type;

stm : (asm_stm | var_dcl | break_stm | continue_stm | return_stm | method_invoke_stm) SEMI
    | if_stm | for_in_stm
    | block_stm;

for_in_stm : FOREACH LB ID IN expr_lit RANGE expr_lit (BY expr_lit)? RB block_stm;

if_stm: IF LB expr_lit RB block_stm (ELSEIF LB expr_lit RB block_stm)* (ELSE block_stm)?;

block_stm : LP mn_stm RP;

mn_stm :
       | stm mn_stm;

continue_stm : CONTINUE;

break_stm : BREAK;

asm_stm : expr_lit ASSIGN_OP expr_lit;

return_stm : RETURN (expr_lit | );

method_invoke_stm : instance_method_invoke | static_mehod_invoke;

var_dcl : VAL_VAR non_static_id_list CL data_type // not assigned
        | VAL_VAR ID var_dcl_list expr_lit; // assigned

var_dcl_list : CL data_type ASSIGN_OP
             | CM ID var_dcl_list expr_lit CM;

expr_pro_list :
          | expr_pro expr_pro_cmlist;

expr_pro_cmlist : | CM expr_pro expr_pro_cmlist;


expr_lit : ID | NULL | lit | index_arr | mul_dim_arr                // literal
         | NEW expr_lit LB expr_lit_list RB                         // object initializing
         | expr_lit LS (expr_lit | int_gen) RS                      // index element(4)
         | expr_lit DOT ID LB para_pass_list RB                     // method invocation(6)
         | expr_lit DOT ID                                          // attribute access(3)
         | expr_lit MEM_ACCESS_OP DOLLAR_ID                         // static attribute access(3)
         | expr_lit MEM_ACCESS_OP DOLLAR_ID LB para_pass_list RB    // static method invocation(6)
         | unary_op expr_lit                                        // unary operator(2)
         | LB expr_lit RB                                           // (expr)(3)
         | expr_lit binary_op expr_lit                              // binary operator(3)
         ;

expr_lit_list : | expr_lit (CM expr_lit)*;

binary_op : ADDOP | LESS_EQUAL | LESS_THAN | GREAT_EQUAL
          | GREAT_THAN | SUBOP | MULOP | LESS_THAN | MODOP
          |DIVOP | NOT_EQUAL | EQUAL | AND | OR | STR_CMP | STR_CONCAT
          ;

unary_op : SUBOP | NEGATE;

instance_method_invoke : expr_lit DOT ID LB para_pass_list RB;

static_mehod_invoke : expr_lit MEM_ACCESS_OP DOLLAR_ID LB para_pass_list RB;

para_pass_list : expr_pro_list;

att_access : instance_att_access | static_att_access;

instance_att_access : expr_lit (DOT expr_lit | MEM_ACCESS_OP DOLLAR_ID)* DOT ID;

static_att_access : expr_lit (DOT expr_lit | MEM_ACCESS_OP DOLLAR_ID)* MEM_ACCESS_OP DOLLAR_ID;

index_ele_pro : ID (LS expr_pro_list RS)+ ;

index_ele : expr_lit (LS expr_lit_list RS)+;

int_object : int_gen | ID | att_access;

float_object : FLOATLIT | ID | att_access;

index_arr_list :
               | index_arr index_arr_cmlist;

index_arr_cmlist :
                 | CM index_arr index_arr_cmlist;

index_arr : ARRAY LB same_type_list RB;

mul_dim_arr : ARRAY LB expr_lit_list RB;




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

non_static_id_list :
        | ID non_static_id_cmlist;

non_static_id_cmlist :
                 | CM ID non_static_id_cmlist;

id_list :
        | (ID | DOLLAR_ID)  id_cmlist;

id_cmlist :
          | CM (ID | DOLLAR_ID) id_cmlist;

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

int_gen : INTLIT_16 | INTLIT_2 | INTLIT_8 | INTLIT_10 | ZERO_2 | ZERO_8 | ZERO_10 | ZERO_16;

data_type : INT_TYPE | FLOAT_TYPE | BOOL_TYPE | STRING_TYPE | array_type | ID;

size : INTLIT_16 | INTLIT_2 | INTLIT_8 | INTLIT_10;

array_type : ARRAY LS data_type CM size RS;


STRINGLIT : ('""' // Case 1: There is no character
          | '"' ('\'"' | '\\' [btnfr'\\] | ~[\r\t\n\\"] )* ('\'"' | '\\' [btnfr'\\] | ~[\r\t\n\\"'] )'"') {self.text = self.text[1:-1]}; // Case 2: There is at least 1 character -> The single quote can not stand at the end of string
          
NULL : 'Null';

MEM_ACCESS_OP : '::';

STRING_TYPE : 'String';

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

FLOATLIT : ((INTLIT_10 | ZERO_10) EXPONENT
		 | (INTLIT_10 | ZERO_10) DECIMAL
		 | DECIMAL EXPONENT
		 | (INTLIT_10 | ZERO_10) DECIMAL EXPONENT)
		 {self.text = self.text.replace("_","")};

fragment DECIMAL : DOT (ZERO_10* (INTLIT_10 | ZERO_10))?;

BY : 'By';

BOOLIT : 'True' | 'False';

VAL_VAR : 'Val' | 'Var';

//STATIC : '$';

ARRAY : 'Array';

INT_TYPE : 'Int';

FLOAT_TYPE : 'Float';

BOOL_TYPE : 'Boolean';

zero : ZERO_2 | ZERO_8 | ZERO_10 | ZERO_16;

ZERO_2 : '0'[bB]'0';

ZERO_8: '00';

ZERO_10 : '0';

ZERO_16 : '0'[xX]'0';

INTLIT_16 : ('0'[xX][1-9A-F]
		  | '0'[xX][1-9A-F][0-9A-F_]*[0-9A-F])
		  {self.text = self.text.replace("_","")};

INTLIT_2 : ('0'[bB]'1'
		 | '0'[bB]'1'[0-1_]*[0-1]) 		 
		 {self.text = self.text.replace("_","")};

INTLIT_8 : ('0'[1-7]
		 | '0'[1-7][0-7_]*[0-7]) 
		 {self.text = self.text.replace("_","")};


INTLIT_10 : ([1-9]'_'?([0-9]'_'?)*[0-9] | [1-9]) {self.text = self.text.replace("_","")};

fragment LIT : [a-zA-Z_];

fragment EXPONENT : ([eE][-+]?'0'* (INTLIT_10 | '0'));

DOLLAR_ID : '$'[0-9a-zA-Z_]+;

ID : [a-zA-Z_] [0-9a-zA-Z_]*;

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
ILLEGAL_ESCAPE: ( '"' ('\\'[bfrnt\\'] | ~[\n\r\\"])* ('\\'(~[bfrnt'\\]))) {self.text = self.text[1:]; raise IllegalEscape(self.text)};
UNCLOSED_STRING: ( '"' ('\'"' | '\\' [btnfr'\\] | ~[\r\t\n\\"] )* ) {self.text = self.text[1:]; raise UncloseString(self.text)};
ERROR_CHAR: . {raise ErrorToken(self.text)};