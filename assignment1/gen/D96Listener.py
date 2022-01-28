# Generated from C:/Users/ADMIN/Documents/GitHub/HCMUT-PPL/assignment1/src/main/d96/parser\D96.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .D96Parser import D96Parser
else:
    from D96Parser import D96Parser

# This class defines a complete listener for a parse tree produced by D96Parser.
class D96Listener(ParseTreeListener):

    # Enter a parse tree produced by D96Parser#program.
    def enterProgram(self, ctx:D96Parser.ProgramContext):
        pass

    # Exit a parse tree produced by D96Parser#program.
    def exitProgram(self, ctx:D96Parser.ProgramContext):
        pass


    # Enter a parse tree produced by D96Parser#class_dcl.
    def enterClass_dcl(self, ctx:D96Parser.Class_dclContext):
        pass

    # Exit a parse tree produced by D96Parser#class_dcl.
    def exitClass_dcl(self, ctx:D96Parser.Class_dclContext):
        pass


    # Enter a parse tree produced by D96Parser#class_body.
    def enterClass_body(self, ctx:D96Parser.Class_bodyContext):
        pass

    # Exit a parse tree produced by D96Parser#class_body.
    def exitClass_body(self, ctx:D96Parser.Class_bodyContext):
        pass


    # Enter a parse tree produced by D96Parser#expr_pro.
    def enterExpr_pro(self, ctx:D96Parser.Expr_proContext):
        pass

    # Exit a parse tree produced by D96Parser#expr_pro.
    def exitExpr_pro(self, ctx:D96Parser.Expr_proContext):
        pass


    # Enter a parse tree produced by D96Parser#att_dcl.
    def enterAtt_dcl(self, ctx:D96Parser.Att_dclContext):
        pass

    # Exit a parse tree produced by D96Parser#att_dcl.
    def exitAtt_dcl(self, ctx:D96Parser.Att_dclContext):
        pass


    # Enter a parse tree produced by D96Parser#att_dcl_list.
    def enterAtt_dcl_list(self, ctx:D96Parser.Att_dcl_listContext):
        pass

    # Exit a parse tree produced by D96Parser#att_dcl_list.
    def exitAtt_dcl_list(self, ctx:D96Parser.Att_dcl_listContext):
        pass


    # Enter a parse tree produced by D96Parser#method_dcl.
    def enterMethod_dcl(self, ctx:D96Parser.Method_dclContext):
        pass

    # Exit a parse tree produced by D96Parser#method_dcl.
    def exitMethod_dcl(self, ctx:D96Parser.Method_dclContext):
        pass


    # Enter a parse tree produced by D96Parser#para_dcl_list.
    def enterPara_dcl_list(self, ctx:D96Parser.Para_dcl_listContext):
        pass

    # Exit a parse tree produced by D96Parser#para_dcl_list.
    def exitPara_dcl_list(self, ctx:D96Parser.Para_dcl_listContext):
        pass


    # Enter a parse tree produced by D96Parser#para_dcl_smcllist.
    def enterPara_dcl_smcllist(self, ctx:D96Parser.Para_dcl_smcllistContext):
        pass

    # Exit a parse tree produced by D96Parser#para_dcl_smcllist.
    def exitPara_dcl_smcllist(self, ctx:D96Parser.Para_dcl_smcllistContext):
        pass


    # Enter a parse tree produced by D96Parser#para_dcl.
    def enterPara_dcl(self, ctx:D96Parser.Para_dclContext):
        pass

    # Exit a parse tree produced by D96Parser#para_dcl.
    def exitPara_dcl(self, ctx:D96Parser.Para_dclContext):
        pass


    # Enter a parse tree produced by D96Parser#stm.
    def enterStm(self, ctx:D96Parser.StmContext):
        pass

    # Exit a parse tree produced by D96Parser#stm.
    def exitStm(self, ctx:D96Parser.StmContext):
        pass


    # Enter a parse tree produced by D96Parser#for_in_stm.
    def enterFor_in_stm(self, ctx:D96Parser.For_in_stmContext):
        pass

    # Exit a parse tree produced by D96Parser#for_in_stm.
    def exitFor_in_stm(self, ctx:D96Parser.For_in_stmContext):
        pass


    # Enter a parse tree produced by D96Parser#if_stm.
    def enterIf_stm(self, ctx:D96Parser.If_stmContext):
        pass

    # Exit a parse tree produced by D96Parser#if_stm.
    def exitIf_stm(self, ctx:D96Parser.If_stmContext):
        pass


    # Enter a parse tree produced by D96Parser#block_stm.
    def enterBlock_stm(self, ctx:D96Parser.Block_stmContext):
        pass

    # Exit a parse tree produced by D96Parser#block_stm.
    def exitBlock_stm(self, ctx:D96Parser.Block_stmContext):
        pass


    # Enter a parse tree produced by D96Parser#mn_stm.
    def enterMn_stm(self, ctx:D96Parser.Mn_stmContext):
        pass

    # Exit a parse tree produced by D96Parser#mn_stm.
    def exitMn_stm(self, ctx:D96Parser.Mn_stmContext):
        pass


    # Enter a parse tree produced by D96Parser#continue_stm.
    def enterContinue_stm(self, ctx:D96Parser.Continue_stmContext):
        pass

    # Exit a parse tree produced by D96Parser#continue_stm.
    def exitContinue_stm(self, ctx:D96Parser.Continue_stmContext):
        pass


    # Enter a parse tree produced by D96Parser#break_stm.
    def enterBreak_stm(self, ctx:D96Parser.Break_stmContext):
        pass

    # Exit a parse tree produced by D96Parser#break_stm.
    def exitBreak_stm(self, ctx:D96Parser.Break_stmContext):
        pass


    # Enter a parse tree produced by D96Parser#asm_stm.
    def enterAsm_stm(self, ctx:D96Parser.Asm_stmContext):
        pass

    # Exit a parse tree produced by D96Parser#asm_stm.
    def exitAsm_stm(self, ctx:D96Parser.Asm_stmContext):
        pass


    # Enter a parse tree produced by D96Parser#return_stm.
    def enterReturn_stm(self, ctx:D96Parser.Return_stmContext):
        pass

    # Exit a parse tree produced by D96Parser#return_stm.
    def exitReturn_stm(self, ctx:D96Parser.Return_stmContext):
        pass


    # Enter a parse tree produced by D96Parser#method_invoke_stm.
    def enterMethod_invoke_stm(self, ctx:D96Parser.Method_invoke_stmContext):
        pass

    # Exit a parse tree produced by D96Parser#method_invoke_stm.
    def exitMethod_invoke_stm(self, ctx:D96Parser.Method_invoke_stmContext):
        pass


    # Enter a parse tree produced by D96Parser#var_dcl.
    def enterVar_dcl(self, ctx:D96Parser.Var_dclContext):
        pass

    # Exit a parse tree produced by D96Parser#var_dcl.
    def exitVar_dcl(self, ctx:D96Parser.Var_dclContext):
        pass


    # Enter a parse tree produced by D96Parser#var_dcl_list.
    def enterVar_dcl_list(self, ctx:D96Parser.Var_dcl_listContext):
        pass

    # Exit a parse tree produced by D96Parser#var_dcl_list.
    def exitVar_dcl_list(self, ctx:D96Parser.Var_dcl_listContext):
        pass


    # Enter a parse tree produced by D96Parser#expr_pro_list.
    def enterExpr_pro_list(self, ctx:D96Parser.Expr_pro_listContext):
        pass

    # Exit a parse tree produced by D96Parser#expr_pro_list.
    def exitExpr_pro_list(self, ctx:D96Parser.Expr_pro_listContext):
        pass


    # Enter a parse tree produced by D96Parser#expr_pro_cmlist.
    def enterExpr_pro_cmlist(self, ctx:D96Parser.Expr_pro_cmlistContext):
        pass

    # Exit a parse tree produced by D96Parser#expr_pro_cmlist.
    def exitExpr_pro_cmlist(self, ctx:D96Parser.Expr_pro_cmlistContext):
        pass


    # Enter a parse tree produced by D96Parser#expr.
    def enterExpr(self, ctx:D96Parser.ExprContext):
        pass

    # Exit a parse tree produced by D96Parser#expr.
    def exitExpr(self, ctx:D96Parser.ExprContext):
        pass


    # Enter a parse tree produced by D96Parser#expr_lit.
    def enterExpr_lit(self, ctx:D96Parser.Expr_litContext):
        pass

    # Exit a parse tree produced by D96Parser#expr_lit.
    def exitExpr_lit(self, ctx:D96Parser.Expr_litContext):
        pass


    # Enter a parse tree produced by D96Parser#object_ini.
    def enterObject_ini(self, ctx:D96Parser.Object_iniContext):
        pass

    # Exit a parse tree produced by D96Parser#object_ini.
    def exitObject_ini(self, ctx:D96Parser.Object_iniContext):
        pass


    # Enter a parse tree produced by D96Parser#instance_method_invoke.
    def enterInstance_method_invoke(self, ctx:D96Parser.Instance_method_invokeContext):
        pass

    # Exit a parse tree produced by D96Parser#instance_method_invoke.
    def exitInstance_method_invoke(self, ctx:D96Parser.Instance_method_invokeContext):
        pass


    # Enter a parse tree produced by D96Parser#static_mehod_invoke.
    def enterStatic_mehod_invoke(self, ctx:D96Parser.Static_mehod_invokeContext):
        pass

    # Exit a parse tree produced by D96Parser#static_mehod_invoke.
    def exitStatic_mehod_invoke(self, ctx:D96Parser.Static_mehod_invokeContext):
        pass


    # Enter a parse tree produced by D96Parser#para_pass_list.
    def enterPara_pass_list(self, ctx:D96Parser.Para_pass_listContext):
        pass

    # Exit a parse tree produced by D96Parser#para_pass_list.
    def exitPara_pass_list(self, ctx:D96Parser.Para_pass_listContext):
        pass


    # Enter a parse tree produced by D96Parser#att_access.
    def enterAtt_access(self, ctx:D96Parser.Att_accessContext):
        pass

    # Exit a parse tree produced by D96Parser#att_access.
    def exitAtt_access(self, ctx:D96Parser.Att_accessContext):
        pass


    # Enter a parse tree produced by D96Parser#instance_att_access.
    def enterInstance_att_access(self, ctx:D96Parser.Instance_att_accessContext):
        pass

    # Exit a parse tree produced by D96Parser#instance_att_access.
    def exitInstance_att_access(self, ctx:D96Parser.Instance_att_accessContext):
        pass


    # Enter a parse tree produced by D96Parser#static_att_access.
    def enterStatic_att_access(self, ctx:D96Parser.Static_att_accessContext):
        pass

    # Exit a parse tree produced by D96Parser#static_att_access.
    def exitStatic_att_access(self, ctx:D96Parser.Static_att_accessContext):
        pass


    # Enter a parse tree produced by D96Parser#index_ele_pro.
    def enterIndex_ele_pro(self, ctx:D96Parser.Index_ele_proContext):
        pass

    # Exit a parse tree produced by D96Parser#index_ele_pro.
    def exitIndex_ele_pro(self, ctx:D96Parser.Index_ele_proContext):
        pass


    # Enter a parse tree produced by D96Parser#index_ele.
    def enterIndex_ele(self, ctx:D96Parser.Index_eleContext):
        pass

    # Exit a parse tree produced by D96Parser#index_ele.
    def exitIndex_ele(self, ctx:D96Parser.Index_eleContext):
        pass


    # Enter a parse tree produced by D96Parser#int_object.
    def enterInt_object(self, ctx:D96Parser.Int_objectContext):
        pass

    # Exit a parse tree produced by D96Parser#int_object.
    def exitInt_object(self, ctx:D96Parser.Int_objectContext):
        pass


    # Enter a parse tree produced by D96Parser#float_object.
    def enterFloat_object(self, ctx:D96Parser.Float_objectContext):
        pass

    # Exit a parse tree produced by D96Parser#float_object.
    def exitFloat_object(self, ctx:D96Parser.Float_objectContext):
        pass


    # Enter a parse tree produced by D96Parser#index_arr_list.
    def enterIndex_arr_list(self, ctx:D96Parser.Index_arr_listContext):
        pass

    # Exit a parse tree produced by D96Parser#index_arr_list.
    def exitIndex_arr_list(self, ctx:D96Parser.Index_arr_listContext):
        pass


    # Enter a parse tree produced by D96Parser#index_arr_cmlist.
    def enterIndex_arr_cmlist(self, ctx:D96Parser.Index_arr_cmlistContext):
        pass

    # Exit a parse tree produced by D96Parser#index_arr_cmlist.
    def exitIndex_arr_cmlist(self, ctx:D96Parser.Index_arr_cmlistContext):
        pass


    # Enter a parse tree produced by D96Parser#index_arr.
    def enterIndex_arr(self, ctx:D96Parser.Index_arrContext):
        pass

    # Exit a parse tree produced by D96Parser#index_arr.
    def exitIndex_arr(self, ctx:D96Parser.Index_arrContext):
        pass


    # Enter a parse tree produced by D96Parser#mul_dim_arr.
    def enterMul_dim_arr(self, ctx:D96Parser.Mul_dim_arrContext):
        pass

    # Exit a parse tree produced by D96Parser#mul_dim_arr.
    def exitMul_dim_arr(self, ctx:D96Parser.Mul_dim_arrContext):
        pass


    # Enter a parse tree produced by D96Parser#same_type_list.
    def enterSame_type_list(self, ctx:D96Parser.Same_type_listContext):
        pass

    # Exit a parse tree produced by D96Parser#same_type_list.
    def exitSame_type_list(self, ctx:D96Parser.Same_type_listContext):
        pass


    # Enter a parse tree produced by D96Parser#string_op.
    def enterString_op(self, ctx:D96Parser.String_opContext):
        pass

    # Exit a parse tree produced by D96Parser#string_op.
    def exitString_op(self, ctx:D96Parser.String_opContext):
        pass


    # Enter a parse tree produced by D96Parser#bool_op.
    def enterBool_op(self, ctx:D96Parser.Bool_opContext):
        pass

    # Exit a parse tree produced by D96Parser#bool_op.
    def exitBool_op(self, ctx:D96Parser.Bool_opContext):
        pass


    # Enter a parse tree produced by D96Parser#relation_op.
    def enterRelation_op(self, ctx:D96Parser.Relation_opContext):
        pass

    # Exit a parse tree produced by D96Parser#relation_op.
    def exitRelation_op(self, ctx:D96Parser.Relation_opContext):
        pass


    # Enter a parse tree produced by D96Parser#int_op.
    def enterInt_op(self, ctx:D96Parser.Int_opContext):
        pass

    # Exit a parse tree produced by D96Parser#int_op.
    def exitInt_op(self, ctx:D96Parser.Int_opContext):
        pass


    # Enter a parse tree produced by D96Parser#float_op.
    def enterFloat_op(self, ctx:D96Parser.Float_opContext):
        pass

    # Exit a parse tree produced by D96Parser#float_op.
    def exitFloat_op(self, ctx:D96Parser.Float_opContext):
        pass


    # Enter a parse tree produced by D96Parser#lit_list.
    def enterLit_list(self, ctx:D96Parser.Lit_listContext):
        pass

    # Exit a parse tree produced by D96Parser#lit_list.
    def exitLit_list(self, ctx:D96Parser.Lit_listContext):
        pass


    # Enter a parse tree produced by D96Parser#lit_cmlist.
    def enterLit_cmlist(self, ctx:D96Parser.Lit_cmlistContext):
        pass

    # Exit a parse tree produced by D96Parser#lit_cmlist.
    def exitLit_cmlist(self, ctx:D96Parser.Lit_cmlistContext):
        pass


    # Enter a parse tree produced by D96Parser#id_list.
    def enterId_list(self, ctx:D96Parser.Id_listContext):
        pass

    # Exit a parse tree produced by D96Parser#id_list.
    def exitId_list(self, ctx:D96Parser.Id_listContext):
        pass


    # Enter a parse tree produced by D96Parser#id_cmlist.
    def enterId_cmlist(self, ctx:D96Parser.Id_cmlistContext):
        pass

    # Exit a parse tree produced by D96Parser#id_cmlist.
    def exitId_cmlist(self, ctx:D96Parser.Id_cmlistContext):
        pass


    # Enter a parse tree produced by D96Parser#int_gen_list.
    def enterInt_gen_list(self, ctx:D96Parser.Int_gen_listContext):
        pass

    # Exit a parse tree produced by D96Parser#int_gen_list.
    def exitInt_gen_list(self, ctx:D96Parser.Int_gen_listContext):
        pass


    # Enter a parse tree produced by D96Parser#int_gen_cm.
    def enterInt_gen_cm(self, ctx:D96Parser.Int_gen_cmContext):
        pass

    # Exit a parse tree produced by D96Parser#int_gen_cm.
    def exitInt_gen_cm(self, ctx:D96Parser.Int_gen_cmContext):
        pass


    # Enter a parse tree produced by D96Parser#bool_list.
    def enterBool_list(self, ctx:D96Parser.Bool_listContext):
        pass

    # Exit a parse tree produced by D96Parser#bool_list.
    def exitBool_list(self, ctx:D96Parser.Bool_listContext):
        pass


    # Enter a parse tree produced by D96Parser#bool_list_cm.
    def enterBool_list_cm(self, ctx:D96Parser.Bool_list_cmContext):
        pass

    # Exit a parse tree produced by D96Parser#bool_list_cm.
    def exitBool_list_cm(self, ctx:D96Parser.Bool_list_cmContext):
        pass


    # Enter a parse tree produced by D96Parser#float_list.
    def enterFloat_list(self, ctx:D96Parser.Float_listContext):
        pass

    # Exit a parse tree produced by D96Parser#float_list.
    def exitFloat_list(self, ctx:D96Parser.Float_listContext):
        pass


    # Enter a parse tree produced by D96Parser#float_list_cm.
    def enterFloat_list_cm(self, ctx:D96Parser.Float_list_cmContext):
        pass

    # Exit a parse tree produced by D96Parser#float_list_cm.
    def exitFloat_list_cm(self, ctx:D96Parser.Float_list_cmContext):
        pass


    # Enter a parse tree produced by D96Parser#string_list.
    def enterString_list(self, ctx:D96Parser.String_listContext):
        pass

    # Exit a parse tree produced by D96Parser#string_list.
    def exitString_list(self, ctx:D96Parser.String_listContext):
        pass


    # Enter a parse tree produced by D96Parser#string_list_cm.
    def enterString_list_cm(self, ctx:D96Parser.String_list_cmContext):
        pass

    # Exit a parse tree produced by D96Parser#string_list_cm.
    def exitString_list_cm(self, ctx:D96Parser.String_list_cmContext):
        pass


    # Enter a parse tree produced by D96Parser#lit.
    def enterLit(self, ctx:D96Parser.LitContext):
        pass

    # Exit a parse tree produced by D96Parser#lit.
    def exitLit(self, ctx:D96Parser.LitContext):
        pass


    # Enter a parse tree produced by D96Parser#int_gen.
    def enterInt_gen(self, ctx:D96Parser.Int_genContext):
        pass

    # Exit a parse tree produced by D96Parser#int_gen.
    def exitInt_gen(self, ctx:D96Parser.Int_genContext):
        pass


    # Enter a parse tree produced by D96Parser#data_type.
    def enterData_type(self, ctx:D96Parser.Data_typeContext):
        pass

    # Exit a parse tree produced by D96Parser#data_type.
    def exitData_type(self, ctx:D96Parser.Data_typeContext):
        pass


    # Enter a parse tree produced by D96Parser#size.
    def enterSize(self, ctx:D96Parser.SizeContext):
        pass

    # Exit a parse tree produced by D96Parser#size.
    def exitSize(self, ctx:D96Parser.SizeContext):
        pass


    # Enter a parse tree produced by D96Parser#array_type.
    def enterArray_type(self, ctx:D96Parser.Array_typeContext):
        pass

    # Exit a parse tree produced by D96Parser#array_type.
    def exitArray_type(self, ctx:D96Parser.Array_typeContext):
        pass


    # Enter a parse tree produced by D96Parser#unary_op.
    def enterUnary_op(self, ctx:D96Parser.Unary_opContext):
        pass

    # Exit a parse tree produced by D96Parser#unary_op.
    def exitUnary_op(self, ctx:D96Parser.Unary_opContext):
        pass


    # Enter a parse tree produced by D96Parser#binary_op.
    def enterBinary_op(self, ctx:D96Parser.Binary_opContext):
        pass

    # Exit a parse tree produced by D96Parser#binary_op.
    def exitBinary_op(self, ctx:D96Parser.Binary_opContext):
        pass


    # Enter a parse tree produced by D96Parser#zero.
    def enterZero(self, ctx:D96Parser.ZeroContext):
        pass

    # Exit a parse tree produced by D96Parser#zero.
    def exitZero(self, ctx:D96Parser.ZeroContext):
        pass



del D96Parser