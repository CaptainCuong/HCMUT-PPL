# Generated from C:/Users/ADMIN/Documents/GitHub/HCMUT-PPL/assignment1/src/main/d96/parser\D96.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .D96Parser import D96Parser
else:
    from D96Parser import D96Parser

# This class defines a complete generic visitor for a parse tree produced by D96Parser.

class D96Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by D96Parser#program.
    def visitProgram(self, ctx:D96Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#comment.
    def visitComment(self, ctx:D96Parser.CommentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_dcl.
    def visitClass_dcl(self, ctx:D96Parser.Class_dclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_body.
    def visitClass_body(self, ctx:D96Parser.Class_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#att_dcl.
    def visitAtt_dcl(self, ctx:D96Parser.Att_dclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#att_dcl_list.
    def visitAtt_dcl_list(self, ctx:D96Parser.Att_dcl_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#method_dcl.
    def visitMethod_dcl(self, ctx:D96Parser.Method_dclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#para_dcl_list.
    def visitPara_dcl_list(self, ctx:D96Parser.Para_dcl_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#para_dcl_smcllist.
    def visitPara_dcl_smcllist(self, ctx:D96Parser.Para_dcl_smcllistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#para_dcl.
    def visitPara_dcl(self, ctx:D96Parser.Para_dclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stm.
    def visitStm(self, ctx:D96Parser.StmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#for_in_stm.
    def visitFor_in_stm(self, ctx:D96Parser.For_in_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#if_stm.
    def visitIf_stm(self, ctx:D96Parser.If_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#block_stm.
    def visitBlock_stm(self, ctx:D96Parser.Block_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#mn_stm.
    def visitMn_stm(self, ctx:D96Parser.Mn_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#continue_stm.
    def visitContinue_stm(self, ctx:D96Parser.Continue_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#break_stm.
    def visitBreak_stm(self, ctx:D96Parser.Break_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#asm_stm.
    def visitAsm_stm(self, ctx:D96Parser.Asm_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#return_stm.
    def visitReturn_stm(self, ctx:D96Parser.Return_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#method_invoke_stm.
    def visitMethod_invoke_stm(self, ctx:D96Parser.Method_invoke_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#var_dcl.
    def visitVar_dcl(self, ctx:D96Parser.Var_dclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#var_dcl_list.
    def visitVar_dcl_list(self, ctx:D96Parser.Var_dcl_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr_list.
    def visitExpr_list(self, ctx:D96Parser.Expr_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr_cmlist.
    def visitExpr_cmlist(self, ctx:D96Parser.Expr_cmlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr.
    def visitExpr(self, ctx:D96Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#object_ini.
    def visitObject_ini(self, ctx:D96Parser.Object_iniContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#instance_method_invoke.
    def visitInstance_method_invoke(self, ctx:D96Parser.Instance_method_invokeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#static_mehod_invoke.
    def visitStatic_mehod_invoke(self, ctx:D96Parser.Static_mehod_invokeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#para_pass_list.
    def visitPara_pass_list(self, ctx:D96Parser.Para_pass_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#att_access.
    def visitAtt_access(self, ctx:D96Parser.Att_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#instance_att_access.
    def visitInstance_att_access(self, ctx:D96Parser.Instance_att_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#static_att_access.
    def visitStatic_att_access(self, ctx:D96Parser.Static_att_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#index_ele.
    def visitIndex_ele(self, ctx:D96Parser.Index_eleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#int_object.
    def visitInt_object(self, ctx:D96Parser.Int_objectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#float_object.
    def visitFloat_object(self, ctx:D96Parser.Float_objectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#index_arr_list.
    def visitIndex_arr_list(self, ctx:D96Parser.Index_arr_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#index_arr_cmlist.
    def visitIndex_arr_cmlist(self, ctx:D96Parser.Index_arr_cmlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#index_arr.
    def visitIndex_arr(self, ctx:D96Parser.Index_arrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#mul_dim_arr.
    def visitMul_dim_arr(self, ctx:D96Parser.Mul_dim_arrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#same_type_list.
    def visitSame_type_list(self, ctx:D96Parser.Same_type_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#string_op.
    def visitString_op(self, ctx:D96Parser.String_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#bool_op.
    def visitBool_op(self, ctx:D96Parser.Bool_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#relation_op.
    def visitRelation_op(self, ctx:D96Parser.Relation_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#int_op.
    def visitInt_op(self, ctx:D96Parser.Int_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#float_op.
    def visitFloat_op(self, ctx:D96Parser.Float_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#lit_list.
    def visitLit_list(self, ctx:D96Parser.Lit_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#lit_cmlist.
    def visitLit_cmlist(self, ctx:D96Parser.Lit_cmlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#static_id_list.
    def visitStatic_id_list(self, ctx:D96Parser.Static_id_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#static_id_cmlist.
    def visitStatic_id_cmlist(self, ctx:D96Parser.Static_id_cmlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#id_list.
    def visitId_list(self, ctx:D96Parser.Id_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#id_cmlist.
    def visitId_cmlist(self, ctx:D96Parser.Id_cmlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#int_gen_list.
    def visitInt_gen_list(self, ctx:D96Parser.Int_gen_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#int_gen_cm.
    def visitInt_gen_cm(self, ctx:D96Parser.Int_gen_cmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#bool_list.
    def visitBool_list(self, ctx:D96Parser.Bool_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#bool_list_cm.
    def visitBool_list_cm(self, ctx:D96Parser.Bool_list_cmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#float_list.
    def visitFloat_list(self, ctx:D96Parser.Float_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#float_list_cm.
    def visitFloat_list_cm(self, ctx:D96Parser.Float_list_cmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#string_list.
    def visitString_list(self, ctx:D96Parser.String_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#string_list_cm.
    def visitString_list_cm(self, ctx:D96Parser.String_list_cmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#lit.
    def visitLit(self, ctx:D96Parser.LitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#int_gen.
    def visitInt_gen(self, ctx:D96Parser.Int_genContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#data_type.
    def visitData_type(self, ctx:D96Parser.Data_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#size.
    def visitSize(self, ctx:D96Parser.SizeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#array_type.
    def visitArray_type(self, ctx:D96Parser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#unary_op.
    def visitUnary_op(self, ctx:D96Parser.Unary_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#binary_op.
    def visitBinary_op(self, ctx:D96Parser.Binary_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#floatlit.
    def visitFloatlit(self, ctx:D96Parser.FloatlitContext):
        return self.visitChildren(ctx)



del D96Parser