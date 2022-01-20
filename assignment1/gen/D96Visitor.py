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



del D96Parser