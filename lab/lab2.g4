


/*

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

*/		




/* TEMPLATE

many -> one
Minimum: zero | one
Separator: have | don't have
many -> one manyprime  | Empty
manyprime -> separator one manyprime | empty







many -> one manyprime  | Empty
manyprime -> separator one manyprime | empty

*/