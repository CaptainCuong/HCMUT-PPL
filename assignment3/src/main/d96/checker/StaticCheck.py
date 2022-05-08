
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
    def __init__(self, name:str, typ:Type, isStatic = False, constant = False):
        self.name = name
        self.type = typ
        self.isStatic = isStatic
        self.constant = constant

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

class Method_Check:
    def __init__(self, method_name:str, static=False, para:List[VarDecl]=[], rettype=None):
        self.clsname = clsname
        self.name = method_name
        self.paratype = list(map(lambda x: x.varType, paratype))
        self.rettype = rettype
        self.isStatic = static
        self.inLoop = 0
        self.variable = {}
        self.scope = 1
        for var in para:
            self.var_decl(var.variable.name,var.varType)
        self.scope = 0

    def __eq__(self, other):
        if isinstance(other, Method_Check):
            return self.clsname == other.name and self.name == method_name and self.paratype == other.paratype
        return self.clsname == other.cls

    def enterScope(self):
        self.scope += 1

    def exitScope(self):
        self.scope -= 1
        for k, lst in self.variable.items():
            if lst[-1].scope > self.scope:
                self.id[k].pop()

    def enterLoop(self):
        self.inLoop += 1

    def exitLoop(self):
        self.inLoop -= 1  

    def _change_ret_type(self, rettype):
        self.rettype = rettype

    def _check_redeclared_variable(self, name):
        if name in self.variable:
            if self.variable[name][-1].scope == self.scope:
                raise Redeclared(Variable(),name)

    def _check_undeclared_variable(self, name):
        if name in self.variable:
            if self.variable[name][-1].scope == self.scope:
                raise Undeclared(Variable(),name)

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

    # def assign_stmt(self, stmt):
    #     if type(stmt.lhs) in [BinaryOp,UnaryOp,NewExpr,IntLiteral,FloatLiteral,StringLiteral,BooleanLiteral]:
    #         tyepl = TypeHandler(stmt.lhs).get_type()
    #     elif type(stmt.lhs) in [CallExpr]:
    #         if type(stmt.lhs.obj) is Id:
    #             if stmt.lhs.obj.name not in self.variable:
    #                 raise Undeclared(Identifier(),stmt.lhs.obj.name)
    #     elif type(stmt.lhs) in [Id,ArrayCell,FieldAccess]:
            
    #     if type(stmt.rhs) in [BinaryOp,UnaryOp,NewExpr,IntLiteral,FloatLiteral,StringLiteral,BooleanLiteral]
    #         tyepr = TypeHandler(stmt.rhs).get_type()

    # def if_stmt(self, stmt):

    # def for_stmt(self, stmt):

    # def break_stmt(self, stmt):

    # def continue_stmt(self, stmt):

    # def return_stmt(self, stmt):

    # def call_stmt(self, stmt):

    # def vardecl_store(self, storedecl):

    # def constdecl_store(self, storedecl):



class Class_Check:
    def __init__(self, name:str, inherited = None):
        '''
        name : str
        inherited : Class_Check
        '''
        self.att = {}
        self.method = {}
        self.mro = []
        self.name = name
        if inherited:
            self.att = inherited.att.copy()
            self.method = inherited.method.copy()
            self.mro = [inherited.name] + inherited.mro.copy()

    def add_attribute(self, name:str, att_type:Type, isStatic=False, const=False):
        self._check_redeclared_attribute(name)
        self.att[name] = Attribute_Check(name,att_type,isStatic,const)

    def add_method(self, name:str, isStatic=False, paratype:List[VarDecl]=[], rettype=None):
        self._check_redeclared_method(name, typelst)
        self.method[name] = Method_Check(name,isStatic,paratype,rettype)

    def get_method(self, method_name:str):
        if method_name not in self.method.keys(): raise Undeclared(Method(),method_name)
        return self.method[method_name]

    def get_attribute(self, att_name:str):
        if att_name not in self.att.keys(): raise Undeclared(Attribute(),att_name)
        return self.att[att_name]

    def checkentry(self):
        return any([x.checkmain() for x in self.method] if self.method else [False])

    def _check_redeclared_method(self, name:str, typelst:List[VarDecl]):
        if name in self.method.keys() and self.method[name].paratype == list(map(lambda x: x.varType,typelst)):
            raise Redeclared(Method(), name)

    def _check_redeclared_attribute(self, name:str):
        if name in self.att:
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
        self.objid[cls_name] = Class_Check(name, self.objid[inherited])

    def add_method(self, cls_name:str, method_name:str, isStatic=False, paratype:List[VarDecl]=[], rettype = None):
        self._check_undeclared_class(cls_name)
        self.objid[cls_name].add_method(method_name, isStatic, paratype, rettype)

    def add_attribute(self, cls_name:str, att_name:str,att_type:Type,isStatic:bool,const:bool):
        self._check_undeclared_class(cls_name)
        self.objid[cls_name].add_attribute(att_name,att_type,isStatic,const)

    def get_class(self, class_name:str):
        return self.objid[class_name]

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

    # global_envi = [
    # Symbol("getInt",MType([],IntType())),
    # Symbol("putIntLn",MType([IntType()],VoidType()))
    # ]
            
    
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
        elif isinstance(ast, ArrayLiteral):
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
        return self.visit(self.ast,None)

    def visitProgram(self,ast, c=None):
        self.classmng = ClassManager()
        [self.visit(x,c) for x in ast.decl]
        if not self.classmng.checkentry():
            raise NoEntryPoint()

######################    Decl    ######################

    def visitClassDecl(self, ast:ClassDecl, c=None):
        self.classmng.add_class(ast.classname,ast.parentname)
        [self.visit(x,self.classmng.get_class(ast.classname)) for x in ast.memlist]

######################    MemDecl    ######################

    def visitAttributeDecl(self, ast, c:Class_Check):
        # c:Class_Check
        class_ = c
        static = self.visit(ast.kind)
        const = type(ast.decl) is ConstDecl
        if type(ast.decl) is ConstDecl:
            typ = ast.decl.constType
            att_name = ast.decl.constant.name
        else:
            typ = ast.decl.varType
            att_name = ast.decl.variable.name
        class_.add_attribute(att_name,ast.typ,static,const)

    def visitMethodDecl(self,ast, c:Class_Check):
        # c:Class_Check
        '''
        TODO:
        Check:
            + Redeclared(Method(),method_name)
        Store: method name
        '''
        class_ = c
        isStatic = type(ast.kind) is Static
        class_.add_method(ast.name,isStatic,ast.param)
        [self.visit(ast.body,(c,class_.get_method(ast.name)))]

######################    Stmt    ######################

    def visitBlock(self, ast, c:tuple):
        # c : (Class_Check,Method_Check)
        class_ = c[0]
        method_ = c[1]
        method_.enterScope()
        [self.visit(x,c) for x in ast.inst]
        method_.exitScope()


    def visitAssign(self, ast, c:tuple):
        lhs = self.visit(ast.lhs,c)
        rhs = self.visit(ast.rhs,c)
        if not isinstance(ast.lhs, LHS) or lhs[1]:
            raise CannotAssignToConstant(ast)
        if lhs[0] != rhs[0]:
            int_float = lhs[0] == FloatType() and rhs[0] == IntType()
            sub_super = type(lhs[0]) is ClassType and type(rhs[0]) is ClassType\
            and rhs[0].classname not in self.classmng.get_class(lhs[0].classname).mro
            if not int_float or not sub_super:
                raise TypeMismatchInStatement(ast)

    def visitIf(self, ast, c:tuple):
        cond = self.visit(ast.expr)
        if cond[0] != BoolType():
            raise TypeMismatchInStatement(ast)
        self.visit(thenStmt,c)
        self.visit(elseStmt,c)

    def visitFor(self, ast, c:tuple):
        class_ = c[0]
        method_ = c[1]
        method_.enterScope()
        method_.enterLoop()
        self.visit(VarDecl(Id(ast.variable),IntType()))
        expr1 = self.visit(ast.expr1)
        expr2 = self.visit(ast.expr2)
        if expr1[0] != IntType() or expr2[0] != IntType():
            raise TypeMismatchInStatement(ast)
        # raise CannotAssignToConstant(statement)
        self.visit(ast.stmt,c)
        method_.exitLoop()
        method_.exitScope()
    
    def visitBreak(self, ast, c:tuple):
        class_ = c[0]
        method_ = c[1]
        if method_.inLoop == 0: 
            raise MustInLoop()
    
    def visitContinue(self, ast, c:tuple):
        class_ = c[0]
        method_ = c[1]
        if method_.inLoop == 0: 
            raise MustInLoop()

    def visitReturn(self, ast, c:tuple):
        class_ = c[0]
        method_ = c[1]
        method_.rettype = self.visit(ast.expr,c)[0]
        # raise TypeMismatchInStatement()

    def visitCallStmt(self, ast, c=None):
        objtyp = self.visit(ast.obj,c)[0]
        if type(objtyp) is not ClassType:
            raise TypeMismatchInStatement(ast)
        
        class_name = objtyp.name
        class_ = self.classmng.get_class(class_name)
        method_ = class_.get_method(ast.method.name)
        if method_.rettype:
            raise TypeMismatchInStatement(ast)
        
        paratyp = [self.visit(x,c)[0] for x in ast.param]
        if method_.paratype != paratyp:
            raise TypeMismatchInStatement(ast)

######################    StoreDecl    ######################

    def visitVarDecl(self, ast, c=None):
        class_ = c[0]
        method_ = c[1]
        method_.var_decl(ast.variable.name,ast.varType)
        expr = self.visit(ast.varInit,c)
        if expr[0] != ast.varType:
            raise TypeMismatchInStatement(ast)


    def visitConstDecl(self, ast, c=None):
        class_ = c[0]
        method_ = c[1]
        method_.const_decl(ast.variable.name,ast.varType)
        expr = self.visit(ast.value)
        if not ast.expr or not expr[1]:
            raise IllegalConstantExpression(ast.value)
        if expr[0] != ast.constType:
            raise TypeMismatchInStatement(ast)


######################    Expr    ######################

    # Expr return (Type, Const)
    def visitBinaryOp(self, ast, c=None):
        typel = self.visit(ast.left,c)
        typer = self.visit(ast.right,c)
        type1 = typel[0]
        type2 = typer[0]
        if expr.op in ['+','-','*','/']:
            if type(type1) not in [IntType, FloatType] or type(type2) not in [IntType, FloatType]:
                raise TypeMismatchInExpression(ast)
            if type(type1) is IntType and type(type2) is IntType:
                return (IntType(), typel[1] and typer[1])
            return (FloatType(), typel[1] and typer[1])

        if expr.op in ['<','<=','>','>=']:
            if type(type1) not in [IntType, FloatType] or type(type2) not in [IntType, FloatType]:
                raise TypeMismatchInExpression(ast)
            return (BoolType(), typel[1] and typer[1])

    def visitUnaryOp(self, ast, c=None):
        typ = self.visit(ast.body,c)[0]
        if ast.op in ['-'] and type(typ) not in [FloatType,IntType]:
            raise TypeMismatchInExpression(ast.body)
        elif ast.op in ['!'] and type(typ) not in [BoolType]:
            raise TypeMismatchInExpression(ast.body)
        return (typ, True)


    def visitCallExpr(self, ast, c=None):
        '''
        TODO:
        Check type
        '''
        objtyp = self.visit(ast.obj,c)[0]
        if type(objtyp) is not ClassType:
            raise TypeMismatchInExpression(ast)
        
        class_name = objtyp.name
        class_ = self.classmng.get_class(class_name)
        method_ = class_.get_method(ast.method.name)
        if not method_.rettype:
            raise TypeMismatchInExpression(ast)
        
        paratyp = [self.visit(x,c)[0] for x in ast.param]
        if method_.paratype != paratyp:
            raise TypeMismatchInExpression(ast)

        if method_.rettype:
            raise TypeMismatchInExpression(ast)
        return (method_rettype, True)

    def visitNewExpr(self, ast:NewExpr, c=None):
        return (ClassType(ast.classname), True)
    def visitIntLiteral(self, ast:IntLiteral, c=None):
        return (IntType(), True)
    def visitFloatLiteral(self, ast:FloatLiteral, c=None):
        return (FloatType(), True)
    def visitStringLiteral(self, ast:StringLiteral, c=None):
        return (StringType(), True)
    def visitBooleanLiteral(self, ast:BooleanLiteral, c=None):
        return (BoolType(), True)
    def visitNullLiteral(self, ast:NullLiteral, c=None):
        return None
    def visitSelfLiteral(self, ast:SelfLiteral, c:tuple):
        return (ClassType(c[0].name), True)
    def visitArrayLiteral(self, ast:ArrayLiteral, c=None):
        typ = [self.visit(x,c)[0] for x in ast.value]
        if typ:
            typ_ini = typ[0]
            for i in range(len(ast.value)):
                if typ[i] != typ_ini:
                    raise IllegalArrayLiteral()
        return (ArrayType(len(typ),typ_ini), True)

    # LHS return (Type, Constant)
    def visitId(self, ast, c:tuple):
        '''
        TODO:
        Return type of Id (if any) else return None
        '''
        class_ = c[0]
        method_ = c[1]
        if ast.name not in method_.variable:
            raise Undeclared(Variable(),ast.name)
        return (method_.variable[ast.name].typ, method_.variable[ast.name].constant)

    def visitArrayCell(self, ast, c=None):
        arrtyp = self.visit(ast.arr,c)
        indtyp = [self.visit(x,c) for x in ast.idx]
        if type(arrtyp) is not ArrayType:
            raise TypeMismatchInExpression(ast)
        for x in indtyp:
            if type(x) is not IntType:
                raise TypeMismatchInExpression(ast)
        return (arrtyp.eleType, False)

    def visitFieldAccess(self, ast, c:tuple):
        class_ = c[0]
        method_ = c[1]
        objtyp = self.visit(ast.obj,c)[0]
        if type(objtyp) is not ClassType:
            raise TypeMismatchInExpression(ast.obj)

        objcls = self.classmng.get_class(objtyp.classname)
        if ast.fieldname.id not in objcls.att:
            raise IllegalMemberAccess(ast.fieldname)
        att = objcls.get_attribute(ast.fieldname.name)
        return (att.type, att.constant)