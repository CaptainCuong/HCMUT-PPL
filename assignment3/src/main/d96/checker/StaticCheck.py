
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

class Attribute_Check:
    def __init__(self, name:str, typ:Type, isStatic = False):
        self.name = name
        self.type = typ
        self.isStatic = isStatic

class Variable_Check:
    def __init__(self,name,typ,scope, constant=False):
        self.name = name
        self.typ = typ
        self.scope = scope
        self.constant = constant

    def __eq__(self, other):
        if isinstance(other, Variable_Check):
            return self.name == other.name and self.typ == other.typ and self.scope == other.scope
        return False

    def get_type(self):
        return self.typ

class Type_Handler:
    
    def __init__(self, expr):
        if isinstance(expr, Method_Check) or isinstance(expr, Variable_Check):
            self.type = expr.get_type()
        elif isinstance(expr, BinaryOp):
            type1 = Type_Handler(expr.left).get_type()
            type2 = Type_Handler(expr.right).get_type()
            if expr.op in ['+','-','*','/']:
                if type(type1) not in [IntType, FloatType] or type(type2) not in [IntType, FloatType]:
                    raise TypeMismatchInExpression(expr)
                if type(type1) is IntType and type(type2) is IntType:
                    self.type = IntType()
                self.type = FloatType()

            if expr.op in ['<','<=','>','>=']:
                if type(type1) not in [IntType, FloatType] or type(type2) not in [IntType, FloatType]:
                    raise TypeMismatchInExpression(expr)
                self.type = BoolType()

        elif isinstance(expr, UnaryOp):
            typ = Type_Handler(expr.body).get_type()
            if expr.op in ['-']:
                if type(typ) not in [FloatType,IntType]:
                    raise TypeMismatchInExpression(expr)
                elif:
                    self.type = typ
            elif expr.op in ['!']:
                if type(typ) not in [BoolType]:
                    raise TypeMismatchInExpression(expr)
                elif:
                    self.type = typ

        elif isinstance(expr, CallExpr):


        elif isinstance(expr, NewExpr):

        elif isinstance(expr, IntLiteral):
            self.type = IntType()
        elif isinstance(expr, FloatLiteral):
            self.type = FloatType()
        elif isinstance(expr, StringLiteral):
            self.type = StringType()
        elif isinstance(expr, BooleanLiteral):
            self.type = BoolType()
        elif isinstance(expr, NullLiteral):
            
        elif isinstance(expr, SelfLiteral):

        elif isinstance(expr, ArrayLiteral):


    def get_type(self):
        return self.type



class Method_Check:
    def __init__(self, clsname:str, method_name:str, paratype:List[VarDecl], rettype=None):
        self.clsname = clsname
        self.name = method_name
        self.paratype = list(map(lambda x: x.varType, paratype))
        self.rettype = rettype
        self.scope = 0
        self.variable = {}

    def __eq__(self, other):
        if isinstance(other, Method_Check):
            return self.clsname == other.name and self.name == method_name and self.paratype == other.paratype
        return self.clsname == other.cls

    def _enterScope(self):
        self.scope += 1

    def _exitScope(self):
        self.scope -= 1
        for k, lst in self.id.items():
            if lst[-1][1] > self.currScope:
                self.id[k].pop()

    def _change_ret_type(self, rettype):
        self.rettype = rettype

    def _check_redeclared_variable(self, name):
        if name in self.variable:
            if self.variable[name][-1].scope == self.scope:
                raise Redeclared(Variable(),name)

    def _check_type(self, first_expr, second_expr):
         

    def _checkmain(self):
        return name == 'main'

    def get_type(self):
        return self.rettype

    def var_decl(self, name:str, typ:Type):
        self._check_redeclared_variable(name)
        if name not in self.variable:
            self.variable[name] = [Variable_Check(name,typ,self.scope)]
        else:
            self.variable[name] += [Variable_Check(name,typ,self.scope)]

    def const_decl(self, name:str, typ:Type):
        self._check_redeclared_variable(name)
        if name not in self.variable:
            self.variable[name] = [Variable_Check(name,typ,self.scope,True)]
        else:
            self.variable[name] += [Variable_Check(name,typ,self.scope,True)]

    def assign_stmt(self):


    def if_stmt(self):

    def for_stmt(self):

    def break_stmt(self):

    def continue_stmt(self):

    def return_stmt(self):

    def call_stmt(self):

    def block_stmt(self):



class Class_Check:
    def __init__(self, name:str, inherited:Class_Check = None):
        '''
        name : str
        inherited : Class_Check
        '''
        self.att = []
        self.method = []
        self.mro = []
        self.name = name
        if inherited:
            self.att = inherited.att.copy()
            self.method = inherited.method.copy()
            self.mro = [inherited.name] + inherited.mro.copy()

    def add_attribute(self, name:str, att_type:Type):
        self._check_redeclared_attribute(name)
        self.att.append(Attribute_Check(name),att_type)

    def add_method(self, name:str, paratype:List[VarDecl], rettype=None):
        self._check_redeclared_method(name, typelst)
        self.method.append(Method_Check(self.name,name,paratype,rettype))

    def checkentry(self):
        return any([x.checkmain() for x in self.method] if self.method else [False])

    def _check_redeclared_method(self, name, typelst:List[VarDecl]):
        if any(map(lambda x: x.name == name and x.paratype == list(map(lambda x: x.varType, typelst)), self.method)):
            raise Redeclared(Method(), name)

    def _check_redeclared_attribute(self, name):
        if any(map(lambda x: x.name == name, self.att)):
            raise Redeclared(Attribute(),name)

class ClassManager:
    def __init__(self):
        self.objid = {}
        '''
        'id': Class_Check
        '''

    def add_class(self, cls_name:str, inherited:str):
        self._check_redeclared_class(name)
        self._check_undeclared_class(inherited)
        self.objid = Class_Check(name, self.onjid[inherited])

    def add_method(self, cls_name:str, method_name:str, paratype:List[VarDecl], rettype = None):
        self._check_undeclared_class(cls_name)
        self.objid[cls_name].add_method(method_name, paratype, rettype)

    def add_attribute(self, cls_name:str, att_name:str,att_type:Type):
        self._check_undeclared_class(cls_name)
        self.objid[cls_name].add_attribute(att_name,att_type)

    def checkentry(self):
        if not any([x.checkentry() for x in self.objid.values()]):
            raise NoEntryPoint()

    def _check_redeclared_class(self, name):
        if name in self.objid:
            raise Redeclared(Class(),name)

    def _check_undeclared_class(self, cls_name):
        if cls_name not in self.objid:
            raise Undeclared(Class(),cls_name)


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
        self.idhandler = IdHandler()
        self.classhelper = ClassHelper()
        return self.visit(self.ast,StaticChecker.global_envi)

    def visitProgram(self,ast, c):
        self.classmng = ClassManager()
        [self.visit(x) for x in ast.decl]
        if not self.classmng.checkentry():
            raise NoEntryPoint()

    def visitFuncDecl(self,ast, c) -> ClassHelper:
        return ClassHelper()
    

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
        raise TypeMismatchInExpression()
    def visitUnaryOp(self, ast, c):
        raise TypeMismatchInExpression()
    def visitCallExpr(self, ast, c):
        pass
    def visitNewExpr(self, ast, c):
        pass
    def visitArrayCell(self, ast, c):
        raise IllegalArrayLiteral()
        raise TypeMismatchInExpression()
    def visitFieldAccess(self, ast, c):
        raise IllegalMemberAccess()
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
        raise IllegalArrayLiteral()
    def visitDecl(self, ast, c):
        pass
    def visitStoreDecl(self, ast, c):
        pass
    def visitAssign(self, ast, c):
        raise TypeMismatchInStatement()
        raise CannotAssignToConstant()
    def visitIf(self, ast, c):
        raise TypeMismatchInStatement()
    def visitFor(self, ast, c):

        raise TypeMismatchInStatement()
    def visitBreak(self, ast, c):
        raise MustInLoop()
    def visitContinue(self, ast, c):
        raise MustInLoop()
    def visitReturn(self, ast, c):
        raise TypeMismatchInStatement()
    def visitCallStmt(self, ast, c):
        raise TypeMismatchInExpression()
        raise TypeMismatchInStatement()
        raise Undeclared()
    def visitVarDecl(self, ast, c):
        raise Redeclared()
    def visitBlock(self, ast, c):
        # c : (classname, methodname)
        [self.visit(x,c) for x in ast.inst]

    def visitConstDecl(self, ast, c):
        raise IllegalConstantExpression()
        raise TypeMismatchInConstant(ast)
        raise Redeclared()
    def visitClassDecl(self, ast:ClassDecl, c:None) -> ClassHelper:
        if self.classmng.checkredeclared(ast.classname):
            raise Redeclared(Class(),ast.classname)
        
        self.classmng.addclass(ast.classname,ast.parentname)
        [self.visit(x) for x in ast.memlist]
    def visitSIKind(self, ast, c):
        pass
    def visitInstance(self, ast, c):
        pass
    def visitStatic(self, ast, c):
        pass
    def visitMethodDecl(self, ast, c):
        # c:class name
        self.classmng.add_method(c,ast.param)
        self.visit(ast.block, (c,ast.name))
    def visitAttributeDecl(self, ast, c):
        raise Redeclared()
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
    def visitClassType(self, ast, c):
        pass
    def visitVoidType(self, ast, c):
        pass