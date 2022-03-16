from MPVisitor import MPVisitor
from MPParser import MPParser
from AST import *

class ASTGeneration(MPVisitor):
    def toBool(self,x):
        return x == "True"

    def visitProgram(self,ctx:MPParser.ProgramContext):
        return ctx.exp().accept(self)

    def visitExp(self,ctx:MPParser.ExpContext):
        termcount = len(ctx.term())
        ret = None
        if termcount > 1:
            ret = Binary(ctx.ASSIGN(0).getText(), ctx.term(termcount-2).accept(self), ctx.term(termcount-1).accept(self))
            for i in range(3, termcount):
                ret = Binary(ctx.ASSIGN(0).getText(), ctx.term(termcount-3).accept(self), ret)

            return ret
        return ctx.term(0).accept(self)

    def visitTerm(self,ctx:MPParser.TermContext):
        if ctx.COMPARE():
            return Binary(ctx.COMPARE().getText(), ctx.factor(0).accept(self), ctx.factor(1).accept(self))

        return ctx.factor(0).accept(self)

    def visitFactor(self,ctx:MPParser.FactorContext):
        oprcount = ctx.getChildCount()
        ret = None
        if oprcount > 1:
            ret = Binary(ctx.ANDOR(0).getText(), ctx.term(oprcount-2).accept(self), ctx.term(oprcount-1).accept(self))
            for i in range(3, oprcountcount):
                ret = Binary(ctx.ANDOR(0).getText(), ctx.term(i).accept(self), ret)

        return None
  
    def visitOperand(self,ctx:MPParser.OperandContext):
        if ctx.ID():
            return ID(ctx.ID().getText())
        elif ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.BOOLIT():
            return BooleanLiteral(ctx.BOOLIT().getText() == 'True')
        else:
            return ctx.exp().accept(self)
        return None

        

