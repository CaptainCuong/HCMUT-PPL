# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKOOLParser import BKOOLParser
else:
    from BKOOLParser import BKOOLParser

# This class defines a complete generic visitor for a parse tree produced by BKOOLParser.

class BKOOLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKOOLParser#program.
    def visitProgram(self, ctx:BKOOLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#mndcl.
    def visitMndcl(self, ctx:BKOOLParser.MndclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#dcl.
    def visitDcl(self, ctx:BKOOLParser.DclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#var_dcl.
    def visitVar_dcl(self, ctx:BKOOLParser.Var_dclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#var_list.
    def visitVar_list(self, ctx:BKOOLParser.Var_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#var_list_prime.
    def visitVar_list_prime(self, ctx:BKOOLParser.Var_list_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#func_dcl.
    def visitFunc_dcl(self, ctx:BKOOLParser.Func_dclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#para_dcl.
    def visitPara_dcl(self, ctx:BKOOLParser.Para_dclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#mnvar_dcl.
    def visitMnvar_dcl(self, ctx:BKOOLParser.Mnvar_dclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#dcl_without_semi.
    def visitDcl_without_semi(self, ctx:BKOOLParser.Dcl_without_semiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#body.
    def visitBody(self, ctx:BKOOLParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#stm.
    def visitStm(self, ctx:BKOOLParser.StmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#asm.
    def visitAsm(self, ctx:BKOOLParser.AsmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#call.
    def visitCall(self, ctx:BKOOLParser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#ret.
    def visitRet(self, ctx:BKOOLParser.RetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr.
    def visitExpr(self, ctx:BKOOLParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr_list.
    def visitExpr_list(self, ctx:BKOOLParser.Expr_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr_list_prime.
    def visitExpr_list_prime(self, ctx:BKOOLParser.Expr_list_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#vardecl.
    def visitVardecl(self, ctx:BKOOLParser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#funcdecl.
    def visitFuncdecl(self, ctx:BKOOLParser.FuncdeclContext):
        return self.visitChildren(ctx)



del BKOOLParser