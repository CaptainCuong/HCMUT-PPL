
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
    def __init__(self,name:str,typ:Type,scope:int, constant=False):
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
        self.name = method_name
        self.paratype = list(map(lambda x: x.varType, para))
        self.rettype = rettype
        self.isStatic = static
        self.inLoop = 0
        self.variable = {}
        self.scope = 1
        for var in para:
            self.para_decl(var.variable.name,var.varType)
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
            if lst and lst[-1].scope > self.scope:
                self.variable[k].pop()

    def enterLoop(self):
        self.inLoop += 1

    def exitLoop(self):
        self.inLoop -= 1  

    def _change_ret_type(self, rettype):
        self.rettype = rettype

    def _check_redeclared_parameter(self, name):
        if name in self.variable:
            if self.variable[name][-1].scope == self.scope:
                raise Redeclared(Parameter(),name)

    def _check_redeclared_variable(self, name):
        if name in self.variable:
            if self.variable[name][-1].scope == self.scope:
                raise Redeclared(Variable(),name)

    def _check_redeclared_constant(self, name):
        if name in self.variable:
            if self.variable[name][-1].scope == self.scope:
                raise Redeclared(Constant(),name)

    def _check_undeclared_variable(self, name):
        if name in self.variable:
            if self.variable[name][-1].scope == self.scope:
                raise Undeclared(Variable(),name)

    def _checkmain(self):
        return self.name == 'main'

    def get_type(self):
        return self.rettype

    def para_decl(self, name:str, typ:Type):
        self._check_redeclared_parameter(name)
        if name not in self.variable:
            self.variable[name] = [Variable_Check(name,typ,self.scope)]
        else:
            self.variable[name] += [Variable_Check(name,typ,self.scope)]

    def var_decl(self, name:str, typ:Type):
        self._check_redeclared_variable(name)
        if name not in self.variable:
            self.variable[name] = [Variable_Check(name,typ,self.scope)]
        else:
            self.variable[name] += [Variable_Check(name,typ,self.scope)]

    def const_decl(self, name:str, typ:Type):
        self._check_redeclared_constant(name)
        if name not in self.variable:
            self.variable[name] = [Variable_Check(name,typ,self.scope,True)]
        else:
            self.variable[name] += [Variable_Check(name,typ,self.scope,True)]

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
        self.construct_type = []
        if inherited:
            self.att = inherited.att.copy()
            self.method = inherited.method.copy()
            self.mro = [name] + inherited.mro.copy()
        else:
            self.mro = [name]

    def add_attribute(self, name:str, att_type:Type, isStatic=False, const=False):
        self._check_redeclared_attribute(name)
        self.att[name] = Attribute_Check(name,att_type,isStatic,const)

    def add_method(self, name:str, isStatic=False, paratype:List[VarDecl]=[], rettype=None):
        self._check_redeclared_method(name, paratype)
        self.method[name] = Method_Check(name,isStatic,paratype,rettype)
        if name == 'Constructor':
            self.construct_type = self.method[name].paratype

    def get_method(self, method_name:str):
        if method_name not in self.method.keys(): raise Undeclared(Method(),method_name)
        return self.method[method_name]

    def get_attribute(self, att_name:str):
        if att_name not in self.att.keys(): raise Undeclared(Attribute(),att_name)
        return self.att[att_name]

    def checkentry(self):
        return any([x._checkmain() == 'main' for x in self.method.values()])

    def _check_redeclared_method(self, name:str, typelst:List[VarDecl]):
        # if name in self.method.keys() and self.method[name].paratype == list(map(lambda x: x.varType,typelst)):
        if name in self.method.keys():
            raise Redeclared(Method(), name)

    def _check_redeclared_attribute(self, name:str):
        # if name in self.att:
        if name in self.att.keys():
            raise Redeclared(Attribute(),name)

class ClassManager:
    def __init__(self):
        self.objid = {}
        '''
        'id': Class_Check
        '''

    def add_class(self, cls_name:str, inherited:str = None):
        self._check_redeclared_class(cls_name)
        if inherited:
            self._check_undeclared_class(inherited)
            self.objid[cls_name] = Class_Check(cls_name, self.objid[inherited])
        else:
            self.objid[cls_name] = Class_Check(cls_name)

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

    def compatible_type(self, typ1, typ2):
        
        if type(typ1) is type(typ2) and type(typ1) not in [ClassType, ArrayType]:
            return True
        if type(typ1) is FloatType and type(typ2) is IntType:
            return True
        # if type(typ1) is ClassType and type(typ2) is ClassType and typ1.classname.name in self.get_class(typ2.classname.name).mro:
        if type(typ1) is ClassType and type(typ2) is ClassType and typ1.classname.name == typ2.classname.name:
            return True
        if type(typ1) is ArrayType and type(typ2) is ArrayType:
            return typ1.size == typ2.size and self.compatible_type(typ1.eleType,typ2.eleType)
        return False

    def _check_redeclared_class(self, name:str):
        if name in self.objid.keys():
            raise Redeclared(Class(),name)

    def _check_undeclared_class(self, cls_name):
        if cls_name not in self.objid.keys():
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
            return self.visitId(ast, c)
        elif isinstance(ast, BinaryOp):
            return self.visitBinaryOp(ast, c)
        elif isinstance(ast, UnaryOp):
            return self.visitUnaryOp(ast, c)
        elif isinstance(ast, CallExpr):
            return self.visitCallExpr(ast, c)
        elif isinstance(ast, NewExpr):
            return self.visitNewExpr(ast, c)
        elif isinstance(ast, ArrayCell):
            return self.visitArrayCell(ast, c)
        elif isinstance(ast, FieldAccess):
            return self.visitFieldAccess(ast, c)
        elif isinstance(ast, IntLiteral):
            return self.visitIntLiteral(ast, c)
        elif isinstance(ast, FloatLiteral):
            return self.visitFloatLiteral(ast, c)
        elif isinstance(ast, StringLiteral):
            return self.visitStringLiteral(ast, c)
        elif isinstance(ast, BooleanLiteral):
            return self.visitBooleanLiteral(ast, c)
        elif isinstance(ast, NullLiteral):
            return self.visitNullLiteral(ast, c)
        elif isinstance(ast, SelfLiteral):
            return self.visitSelfLiteral(ast, c)
        elif isinstance(ast, ArrayLiteral):
            return self.visitArrayLiteral(ast, c)
        elif isinstance(ast, Assign):
            return self.visitAssign(ast, c)
        elif isinstance(ast, If):
            return self.visitIf(ast, c)
        elif isinstance(ast, For):
            return self.visitFor(ast, c)
        elif isinstance(ast, Break):
            return self.visitBreak(ast, c)
        elif isinstance(ast, Continue):
            return self.visitContinue(ast, c)
        elif isinstance(ast, Return):
            return self.visitReturn(ast, c)
        elif isinstance(ast, CallStmt):
            return self.visitCallStmt(ast, c)
        elif isinstance(ast, VarDecl):
            return self.visitVarDecl(ast, c)
        elif isinstance(ast, Block):
            return self.visitBlock(ast, c)
        elif isinstance(ast, ConstDecl):
            return self.visitConstDecl(ast, c)
        elif isinstance(ast, ClassDecl):
            return self.visitClassDecl(ast, c)
        elif isinstance(ast, Static):
            return self.visitStatic(ast, c)
        elif isinstance(ast, MethodDecl):
            return self.visitMethodDecl(ast, c)
        elif isinstance(ast, AttributeDecl):
            return self.visitAttributeDecl(ast, c)
        elif isinstance(ast, IntType):
            return self.visitIntType(ast, c)
        elif isinstance(ast, FloatType):
            return self.visitFloatType(ast, c)
        elif isinstance(ast, BoolType):
            return self.visitBoolType(ast, c)
        elif isinstance(ast, StringType):
            return self.visitStringType(ast, c)
        elif isinstance(ast, ArrayType):
            return self.visitArrayType(ast, c)
        elif isinstance(ast, ClassType):
            return self.visitClassType(ast, c)
        elif isinstance(ast, VoidType):
            return self.visitVoidType(ast, c)
        elif isinstance(ast, Program):
            return self.visitProgram(ast, c)

    def check(self):
        return self.visit(self.ast,None)

    def visitProgram(self,ast, c=None):
        self.classmng = ClassManager()
        [self.visit(x,c) for x in ast.decl]
        if not self.classmng.checkentry():
            raise NoEntryPoint()

######################    Decl    ######################

    def visitClassDecl(self, ast:ClassDecl, c=None):
        if ast.parentname:
            self.classmng.add_class(ast.classname.name,ast.parentname.name)
        else:
            self.classmng.add_class(ast.classname.name)
        [self.visit(x,(self.classmng.get_class(ast.classname.name),None)) for x in ast.memlist]

######################    MemDecl    ######################

    def visitAttributeDecl(self, ast, c:Class_Check):
        '''
        c:(Class_Check,None)
        Separating from ConstDecl and VarDecl because
        c[1] is None but ConstDecl and VarDecl use
        c[1] as Method_Check
        '''
        class_ = c[0]
        static = self.visit(ast.kind,c)
        const = type(ast.decl) is ConstDecl
        
        if type(ast.decl) is ConstDecl:
            typ = ast.decl.constType
            att_name = ast.decl.constant.name
            expr_typ = self.visit(ast.decl.value,c)
            if not expr_typ or not expr_typ[1]:
                raise IllegalConstantExpression(ast.decl.value)
        else:
            typ = ast.decl.varType
            att_name = ast.decl.variable.name
            expr_typ = self.visit(ast.decl.varInit,c)

        if type(expr_typ) is ClassType:
            if expr_typ.classname.name not in self.classmng.objid:
                raise Undeclared(Class(),expr_typ.classname.name)

        if expr_typ and not self.classmng.compatible_type(typ,expr_typ[0]):
            if type(ast.decl) is ConstDecl:
                raise TypeMismatchInConstant(ast.decl)
            raise TypeMismatchInStatement(ast.decl)

        class_.add_attribute(att_name,typ,static,const)

    def visitMethodDecl(self,ast, c:Class_Check):
        # c:Class_Check
        '''
        TODO:
        Check:
            + Redeclared(Method(),method_name)
        Store: method name
        '''
        class_ = c[0]
        isStatic = type(ast.kind) is Static
        class_.add_method(ast.name.name,isStatic,ast.param)
        self.visit(ast.body,(c[0],class_.get_method(ast.name.name)))

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
        rhs = self.visit(ast.exp,c)
        if type(lhs[0]) is ClassType and lhs[0].classname.name[-1]==',':
            raise Undeclared(Identifier(),lhs[0].classname.name[:-1])
        if not isinstance(ast.lhs, LHS) or lhs[1]:
            raise CannotAssignToConstant(ast)
        if not self.classmng.compatible_type(lhs[0],rhs[0]):
            raise TypeMismatchInStatement(ast)

    def visitIf(self, ast, c:tuple):
        cond = self.visit(ast.expr,c)
        if cond[0] != BoolType():
            raise TypeMismatchInStatement(ast)
        self.visit(ast.thenStmt,c)
        self.visit(ast.elseStmt,c)

    def visitFor(self, ast, c:tuple):
        class_ = c[0]
        method_ = c[1]
        method_.enterScope()
        method_.enterLoop()
        self.visit(VarDecl(ast.id,IntType()),c)
        expr1 = self.visit(ast.expr1,c)
        expr2 = self.visit(ast.expr2,c)
        if expr1[0] != IntType() or expr2[0] != IntType():
            raise TypeMismatchInStatement(ast)
        # raise CannotAssignToConstant(statement)
        self.visit(ast.loop,c)
        method_.exitLoop()
        method_.exitScope()
    
    def visitBreak(self, ast, c:tuple):
        class_ = c[0]
        method_ = c[1]
        if method_.inLoop == 0: 
            raise MustInLoop(ast)
    
    def visitContinue(self, ast, c:tuple):
        class_ = c[0]
        method_ = c[1]
        if method_.inLoop == 0: 
            raise MustInLoop(ast)

    def visitReturn(self, ast, c:tuple):
        class_ = c[0]
        method_ = c[1]
        method_.rettype = self.visit(ast.expr,c)[0]
        # raise TypeMismatchInStatement()

    def visitCallStmt(self, ast, c=None):
        objtyp = self.visit(ast.obj,c)[0]
        if type(objtyp) is not ClassType:
            raise TypeMismatchInStatement(ast)
        
        class_name = objtyp.classname.name

        instance = True
        if class_name[-1] == ',':
            instance = False
            class_name = class_name[:-1]

        class_ = self.classmng.get_class(class_name)
        method_ = class_.get_method(ast.method.name)
    
        if not instance and not method_.isStatic or instance and method_.isStatic:
            raise IllegalMemberAccess(ast)

        if method_.rettype:
            raise TypeMismatchInStatement(ast)
                    
        paratyp = [self.visit(x,c)[0] for x in ast.param]
        if len(method_.paratype) != len(paratyp):
            raise TypeMismatchInStatement(ast)
        for x in zip(method_.paratype,paratyp):
            if not self.classmng.compatible_type(x[0],x[1]):
                raise TypeMismatchInStatement(ast)

######################    StoreDecl    ######################

    def visitVarDecl(self, ast, c=None):
        class_ = c[0]
        method_ = c[1]
        method_.var_decl(ast.variable.name,ast.varType)
        if type(ast.varType) is ClassType:
            if ast.varType.classname.name not in self.classmng.objid:
                raise Undeclared(Class(),ast.varType.classname.name)
        expr = self.visit(ast.varInit,c)
        if expr and not self.classmng.compatible_type(ast.varType,expr[0]):
            raise TypeMismatchInStatement(ast)


    def visitConstDecl(self, ast, c=None):
        class_ = c[0]
        method_ = c[1]
        method_.const_decl(ast.constant.name,ast.constType)
        if type(ast.constType) is ClassType:
            if ast.constType.classname.name not in self.classmng.objid:
                raise Undeclared(Class(),ast.constType.classname.name)
        expr = self.visit(ast.value,c)
        if (not expr) or (not expr[1]):
            raise IllegalConstantExpression(ast.value)
        if expr and not self.classmng.compatible_type(ast.constType,expr[0]):
            raise TypeMismatchInConstant(ast)


######################    Expr    ######################

    # Expr return (Type, Const)
    def visitBinaryOp(self, ast, c=None):
        typel = self.visit(ast.left,c)
        typer = self.visit(ast.right,c)
        type1 = typel[0]
        type2 = typer[0]
        if ast.op in ['%']:
            if type(type1) is not IntType or type(type2) is not IntType:
                raise TypeMismatchInExpression(ast)
            return (IntType(), typel[1] and typer[1])

        if ast.op in ['+','-','*','/']:
            if type(type1) not in [IntType, FloatType] or type(type2) not in [IntType, FloatType]:
                raise TypeMismatchInExpression(ast)
            if type(type1) is IntType and type(type2) is IntType:
                return (IntType(), typel[1] and typer[1])
            return (FloatType(), typel[1] and typer[1])

        if ast.op in ['<','<=','>','>=']:
            if type(type1) not in [IntType, FloatType] or type(type2) not in [IntType, FloatType]:
                raise TypeMismatchInExpression(ast)
            return (BoolType(), typel[1] and typer[1])

        if ast.op in ['&&','||']:
            if type(type1) is not BoolType or type(type2) is not BoolType:
                raise TypeMismatchInExpression(ast)
            return (BoolType(), typel[1] and typer[1])

        if ast.op in ['+.','==.']:
            if type(type1) is not StringType or type(type2) is not StringType:
                raise TypeMismatchInExpression(ast)
            return (StringType(), typel[1] and typer[1]) if ast.op == '+.' else (BoolType(), typel[1] and typer[1])

        if ast.op in ['!=','==']:
            if not (type(type1) is IntType and type(type2) is IntType or type(type1) is BoolType and type(type2) is BoolType):
                raise TypeMismatchInExpression(ast)
            return (StringType(), typel[1] and typer[1]) if ast.op == '+.' else (BoolType(), typel[1] and typer[1])

    def visitUnaryOp(self, ast, c=None):
        expr = self.visit(ast.body,c)
        if ast.op in ['-'] and type(expr[0]) not in [FloatType,IntType]:
            raise TypeMismatchInExpression(ast)
        elif ast.op in ['!'] and type(expr[0]) not in [BoolType]:
            raise TypeMismatchInExpression(ast)
        return expr


    def visitCallExpr(self, ast, c=None):
        '''
        TODO:
        Check type
        '''
        objtyp = self.visit(ast.obj,c)[0]
        if type(objtyp) is not ClassType:
            raise TypeMismatchInExpression(ast)
        
        instance = True
        if objtyp.classname.name[-1] == ',':
            instance = False
            objtyp.classname.name = objtyp.classname.name[:-1]

        class_name = objtyp.classname.name
        class_ = self.classmng.get_class(class_name)
        method_ = class_.get_method(ast.method.name)

        if not instance and not method_.isStatic or instance and method_.isStatic:
            raise IllegalMemberAccess(ast)

        if not method_.rettype:
            raise TypeMismatchInExpression(ast)
        
        paratyp = [self.visit(x,c)[0] for x in ast.param]
        if len(method_.paratype) != len(paratyp):
            raise TypeMismatchInExpression(ast)
        for x in zip(method_.paratype,paratyp):
            if not self.classmng.compatible_type(x[0],x[1]):
                raise TypeMismatchInExpression(ast)

        return (method_.rettype, False)
    def visitStatic(self,ast,c):
        return True
    def visitInstance(self,ast,c):
        return False
    def visitNewExpr(self, ast:NewExpr, c=None):
        if ast.classname.name not in self.classmng.objid:
            raise Undeclared(Class(),ast.classname.name)
        if ast.param:
            expr_typ = [self.visit(x,c)[0] for x in ast.param]
        else:
            expr_typ = []
        class_ = self.classmng.get_class(ast.classname.name)
        if len(class_.construct_type) != len(expr_typ): 
            raise TypeMismatchInExpression(ast)
        for x in zip(class_.construct_type,expr_typ):
            if not self.classmng.compatible_type(x[0],x[1]):
                raise TypeMismatchInExpression(ast)
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
        return (ClassType(Id(c[0].name)), True)
    def visitArrayLiteral(self, ast:ArrayLiteral, c=None):
        typ = [self.visit(x,c)[0] for x in ast.value]
        if typ:
            typ_ini = typ[0]
            for i in range(len(ast.value)):
                if not self.classmng.compatible_type(typ[i],typ_ini) or type(typ[i]) is not type(typ_ini):
                    raise IllegalArrayLiteral(ast)
        return (ArrayType(len(typ),typ_ini), True)

    # LHS return (Type, Constant)
    def visitId(self, ast, c:tuple):
        '''
        TODO:
        Used to test the declaration of LHS
        '''
        class_ = c[0]
        method_ = c[1]
        if ast.name not in list(method_.variable.keys()) + list(self.classmng.objid.keys()):
            raise Undeclared(Identifier(),ast.name)
        if ast.name in method_.variable:
            return (method_.variable[ast.name][-1].typ, method_.variable[ast.name][-1].constant)
        else:
            return (ClassType(Id(ast.name+',')), False)

    def visitArrayCell(self, ast, c=None):
        array = self.visit(ast.arr,c)
        arrtyp = array[0]
        indtyp = [self.visit(x,c)[0] for x in ast.idx]
        if type(arrtyp) is not ArrayType:
            raise TypeMismatchInExpression(ast)
        rettyp = arrtyp
        for x in indtyp:
            if hasattr(rettyp,'eleType'):
                rettyp = rettyp.eleType
            else:
                raise TypeMismatchInExpression(ast)
            if type(x) is not IntType:
                raise TypeMismatchInExpression(ast)
        
        return (rettyp, array[1])

    def visitFieldAccess(self, ast, c:tuple):
        class_ = c[0]
        method_ = c[1]
        obj = self.visit(ast.obj,c)
        objtyp = obj[0]
        if type(objtyp) is not ClassType:
            if type(ast.obj) is Id and ast.obj.name in self.classmng.objid:
                objtyp = ClassType(Id(ast.obj.name+','))
            else:
                raise IllegalMemberAccess(ast.obj)
        instance = True

        if objtyp.classname.name[-1] == ',':
            instance = False
            objtyp.classname.name = objtyp.classname.name[:-1]
            
        objcls = self.classmng.get_class(objtyp.classname.name)
        if ast.fieldname.name not in objcls.att:
            raise Undeclared(Attribute(),ast.fieldname.name)
        
        if not instance and not objcls.att[ast.fieldname.name].isStatic or instance and objcls.att[ast.fieldname.name].isStatic:
            raise IllegalMemberAccess(ast)
        att = objcls.get_attribute(ast.fieldname.name)

        return (att.type, att.constant and obj[1])