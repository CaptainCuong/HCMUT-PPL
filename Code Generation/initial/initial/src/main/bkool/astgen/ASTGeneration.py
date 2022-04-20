from BKOOLVisitor import BKOOLVisitor
from BKOOLParser import BKOOLParser
from AST import *

class ASTGeneration(BKOOLVisitor):
    def visitProgram(self,ctx:BKOOLParser.ProgramContext):
        return Program([FuncDecl(Id("main"),
                        [],
                        self.visit(ctx.mptype()),
                        Block([],[self.visit(ctx.body())] if ctx.body() else []))])
        


    def visitMptype(self,ctx:BKOOLParser.MptypeContext):
        if ctx.INTLIT():
            return IntType(str(ctx.getText()))
        elif ctx.FLOATLIT():
            return FloatType()
        else:
            return VoidType()

    def visitBody(self,ctx:BKOOLParser.BodyContext):
        return self.visit(ctx.funcall())
  
  	
    def visitFuncall(self,ctx:BKOOLParser.FuncallContext):
        return CallExpr(Id(ctx.ID().getText()),[self.visit(ctx.exp())] if ctx.exp() else [])

    def visitExp(self,ctx:BKOOLParser.ExpContext):
        if (ctx.funcall()):
            return self.visit(ctx.funcall())
        elif ctx.ADDOP():
            return FloatLiteral(ctx.exp1(0).accept(self).value + ctx.exp1(1).accept(self).value)\
                    if isinstance(ctx.exp1(0).accept(self), float) or isinstance(ctx.exp1(1).accept(self), float)\
                    else IntLiteral(ctx.exp1(0).accept(self).value + ctx.exp1(1).accept(self).value)
        elif ctx.MINOP():
             return FloatLiteral(ctx.exp1(0).accept(self).value - ctx.exp1(1).accept(self).value)\
                    if isinstance(ctx.exp1(0).accept(self), float) or isinstance(ctx.exp1(1).accept(self), float)\
                    else IntLiteral(ctx.exp1(0).accept(self).value - ctx.exp1(1).accept(self).value)

    def visitExp1(self,ctx:BKOOLParser.ExpContext):
        if ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():    
            return FloatLiteral(float(ctx.FLOATTLIT().getText()))
        elif ctx.exp():
            return ctx.exp().accept(self)
        elif ctx.MULOP():
             return FloatLiteral(ctx.exp1(0).accept(self).value * ctx.exp1(1).accept(self).value)\
                    if isinstance(ctx.exp1(0).accept(self), float) or isinstance(ctx.exp1(1).accept(self), float)\
                    else IntLiteral(ctx.exp1(0).accept(self).value * ctx.exp1(1).accept(self).value)
        elif ctx.DIVOP():
            return FloatLiteral(ctx.exp1(self).accept(self).value / ctx.exp1().accept(self).value)\
                    if isinstance(ctx.exp1(0).accept(self), float) or isinstance(ctx.exp1(1).accept(self), float)\
                    else IntLiteral(ctx.exp1(self).accept(self).value / ctx.exp1().accept(self).value)


        
        

