
"""
 * @author nhphung
"""
from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value

class StaticChecker(BaseVisitor,Utils):

    global_envi = [
    Symbol("getInt",MType([],IntType())),
    Symbol("putIntLn",MType([IntType()],VoidType()))
    ]
            
    
    def __init__(self,ast):
        self.ast = ast

    def lookup(self, qvalue, lst, func):
        for i in range(len(lst)):
            if func(lst[i]) == qvalue:
                return lst[i]
        return None
    
    def visit(self, ast, c):
        if isinstance(ast, Id):
            self.visitId(ast, c)
        elif isinstance(ast, BinaryOp):
            self.visitBinaryOp(ast, c)
        elif isinstance(ast, UnaryOp):
            self.visitUnaryOp(ast, c)
        elif isinstance(ast, CallExpr):
            self.visitCallExpr(ast, c)
        elif isinstance(ast, NewExpr):
            self.visitNewExpr(ast, c)
        elif isinstance(ast, ArrayCell):
            self.visitArrayCell(ast, c)
        elif isinstance(ast, FieldAccess):
            self.visitFieldAccess(ast, c)
        elif isinstance(ast, IntLiteral):
            self.visitIntLiteral(ast, c)
        elif isinstance(ast, FloatLiteral):
            self.visitFloatLiteral(ast, c)
        elif isinstance(ast, StringLiteral):
            self.visitStringLiteral(ast, c)
        elif isinstance(ast, BooleanLiteral):
            self.visitBooleanLiteral(ast, c)
        elif isinstance(ast, NullLiteral):
            self.visitNullLiteral(ast, c)
        elif isinstance(ast, SelfLiteral):
            self.visitSelfLiteral(ast, c)
        elif isinstanceArrayLiteral(ast, ArrayLiteral):
            self.visitArrayLiteral(ast, c)
        elif isinstance(ast, Assign):
            self.visitAssign(ast, c)
        elif isinstance(ast, If):
            self.visitIf(ast, c)
        elif isinstance(ast, For):
            self.visitFor(ast, c)
        elif isinstance(ast, Break):
            self.visitBreak(ast, c)
        elif isinstance(ast, Continue):
            self.visitContinue(ast, c)
        elif isinstance(ast, Return):
            self.visitReturn(ast, c)
        elif isinstance(ast, CallStmt):
            self.visitCallStmt(ast, c)
        elif isinstance(ast, VarDecl):
            self.visitVarDecl(ast, c)
        elif isinstance(ast, Block):
            self.visitBlock(ast, c)
        elif isinstance(ast, ConstDecl):
            self.visitConstDecl(ast, c)
        elif isinstance(ast, ClassDecl):
            self.visitClassDecl(ast, c)
        elif isinstance(ast, Instance):
            self.visitInstance(ast, c)
        elif isinstance(ast, Static):
            self.visitStatic(ast, c)
        elif isinstance(ast, MethodDecl):
            self.visitMethodDecl(ast, c)
        elif isinstance(ast, AttributeDecl):
            self.visitAttributeDecl(ast, c)
        elif isinstance(ast, IntType):
            self.visitIntType(ast, c)
        elif isinstance(ast, FloatType):
            self.visitFloatType(ast, c)
        elif isinstance(ast, BoolType):
            self.visitBoolType(ast, c)
        elif isinstance(ast, StringType):
            self.visitStringType(ast, c)
        elif isinstance(ast, ArrayType):
            self.visitArrayType(ast, c)
        elif isinstance(ast, ClassType):
            self.visitClassType(ast, c)
        elif isinstance(ast, VoidType):
            self.visitVoidType(ast, c)
        elif isinstance(ast, Program):
            self.visitProgram(ast, c)

    def check(self):
        return self.visit(self.ast,StaticChecker.global_envi)

    def visitProgram(self,ast, c): 
        return [self.visit(x,c) for x in ast.decl]

    def visitFuncDecl(self,ast, c): 
        return list(map(lambda x: self.visit(x,(c,True)),ast.body.stmt)) 
    

    def visitCallExpr(self, ast, c): 
        at = [self.visit(x,(c[0],False)) for x in ast.param]
        
        res = self.lookup(ast.method.name,c[0],lambda x: x.name)
        if res is None or not type(res.mtype) is MType:
            raise Undeclared(Function(),ast.method.name)
        elif len(res.mtype.partype) != len(at):
            if c[1]:
                raise TypeMismatchInStatement(ast)
            else:
                raise TypeMismatchInExpression(ast)
        else:
            return res.mtype.rettype

    def visitAST(self, ast, c):
        pass
    def visitInst(self, ast, c):
        pass
    def visitStmt(self, ast, c):
        pass
    def visitExpr(self, ast, c):
        pass
    def visitLHS(self, ast, c):
        pass
    def visitType(self, ast, c):
        pass
    def visitMemDecl(self, ast, c):
        pass
    def visitId(self, ast, c):
        pass
    def visitBinaryOp(self, ast, c):
        pass
    def visitUnaryOp(self, ast, c):
        pass
    def visitCallExpr(self, ast, c):
        pass
    def visitNewExpr(self, ast, c):
        pass
    def visitArrayCell(self, ast, c):
        pass
    def visitFieldAccess(self, ast, c):
        pass
    def visitLiteral(self, ast, c):
        pass
    def visitIntLiteral(self, ast, c):
        pass
    def visitFloatLiteral(self, ast, c):
        pass
    def visitStringLiteral(self, ast, c):
        pass
    def visitBooleanLiteral(self, ast, c):
        pass
    def visitNullLiteral(self, ast, c):
        pass
    def visitSelfLiteral(self, ast, c):
        pass
    def visitArrayLiteral(self, ast, c):
        pass
    def visitDecl(self, ast, c):
        pass
    def visitStoreDecl(self, ast, c):
        pass
    def visitAssign(self, ast, c):
        pass
    def visitIf(self, ast, c):
        pass
    def visitFor(self, ast, c):
        pass
    def visitBreak(self, ast, c):
        pass
    def visitContinue(self, ast, c):
        pass
    def visitReturn(self, ast, c):
        pass
    def visitCallStmt(self, ast, c):
        pass
    def visitVarDecl(self, ast, c):
        pass
    def visitBlock(self, ast, c):
        pass
    def visitConstDecl(self, ast, c):
        pass
    def visitdefDecl(self, ast, c):
        pass
    def visitSIKind(self, ast, c):
        pass
    def visitInstance(self, ast, c):
        pass
    def visitStatic(self, ast, c):
        pass
    def visitMethodDecl(self, ast, c):
        pass
    def visitAttributeDecl(self, ast, c):
        pass
    def visitIntType(self, ast, c):
        pass
    def visitFloatType(self, ast, c):
        pass
    def visitBoolType(self, ast, c):
        pass
    def visitStringType(self, ast, c):
        pass
    def visitArrayType(self, ast, c):
        pass
    def visitdefType(self, ast, c):
        pass
    def visitVoidType(self, ast, c):
        pass
    def visitProgram(self, ast, c):
        pass