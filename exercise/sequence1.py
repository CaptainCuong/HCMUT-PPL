class CodeGenVisitor(BaseVisitor):
    def __init__(self, astTree, env):
        #astTree: AST
        #env: List[Symbol]
        #dir_: File

        self.astTree = astTree
        self.env = env
        self.className = "MCClass"
        self.emit = Emitter("./" + self.className + ".j")


    def visitProgram(self, ast, c):
        #ast: Program
        #c: Any

        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        reduce(lambda env,ele: SubBody(env.frame,[self.visit(ele,env)]+env.sym),ast.decl, SubBody(None, self.env))
        # generate default constructor
        self.genMETHOD(FuncDecl(Id("<init>"), list(), None,list()), c, Frame("<init>", VoidType() ))
        self.emit.emitEPILOG()
        return c

    def genMETHOD(self, consdecl, o, frame):
        #consdecl: FuncDecl
        #o: Any
        #frame: Frame

        isInit = consdecl.returnType is None
        isMain = consdecl.name == "main" and len(consdecl.param) == 0 and type(consdecl.returnType) is VoidType
        returnType = VoidType() if isInit else consdecl.returnType
        methodName = "<init>" if isInit else consdecl.name
        intype = [ArrayType(StringType())] if isMain else list(map(lambda x: x.typ,consdecl.param))
        mtype = MType(intype, returnType)

        self.emit.printout(self.emit.emitMETHOD(methodName, mtype, not isInit))

        frame.enterScope(True)

        glenv = o

        # Generate code for parameter declarations
        if isInit:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel()))
        elif isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayType(StringType()), frame.getStartLabel(), frame.getEndLabel()))
        else:
            local = reduce(lambda env,ele: SubBody(frame,[self.visit(ele,env)]+env.sym),consdecl.param,SubBody(frame,[]))
            glenv = local.sym+glenv
        body = consdecl.body
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Generate code for statements
        if isInit:
            self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        list(map(lambda x: self.visit(x, SubBody(frame, glenv)), body))

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if type(returnType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(),  ...snip...  ret = FloatType()
            if ast.op in ['+','-']:
                return e1c + e2c + self.emit.emitADDOP(ast.op,ret,o.frame),ret
            elif ast.op in ['*','/']:
                return e1c + e2c + self.emit.emitMULOP(ast.op,ret,o.frame),ret
            else:
                return e1c + e2c + self.emit.emitREOP(ast.op,ret,o.frame),BoolType()
        else:
            resLabel = o.frame.getNewLabel()
            nextLabel = o.frame.getNewLabel()
            if ast.op == '&&':
                ctlcode = self.emit.emitIFFALSE(resLabel,o.frame)
            else:
                ctlcode = self.emit.emitIFTRUE(resLabel,o.frame)
            e2c,e2t = self.visit(ast.e2,o)
            gotocode = self.emit.emitGOTO(nextLabel,o.frame)
            lcode = self.emit.emitLABEL(resLabel,o.frame)
            if ast.op == '&&':
                rcode = self.emit.emitPUSHICONST("false",o.frame)
            else:
                rcode = self.emit.emitPUSHICONST("true",o.frame)
            ncode = self.emit.emitLABEL(nextLabel,o.frame)

            return e1c+ctlcode+e2c+gotocode+lcode+rcode+ncode, BoolType()
    
    def visitId(self, ast, o):
        sym = next(filter(lambda y: y.name == ast.name,o.sym),False)
        if o.isLeft:
            if type(sym.value) is Index:
                code = self.emit.emitWRITEVAR(sym.name,sym.mtype,sym.value.value,o.frame)
            else:
                code = self.emit.emitPUTSTATIC(sym.value.value+"."+sym.name,sym.mtype,o.frame)
        else:
            if type(sym.value) is Index:
                code = self.emit.emitREADVAR(sym.name,sym.mtype,sym.value.value,o.frame)
            else:
                code = self.emit.emitGETSTATIC(sym.value.value+"."+sym.name,sym.mtype,o.frame)
        typ = sym.mtype
        return code, typ

    def visitVarDecl(self,ast,o):
        if o.frame is None:
            self.emit.printout(self.emit.emitATTRIBUTE(ast.name,ast.typ,False))
            return Symbol(ast.name,ast.typ,CName(self.className))
        else:
            idx = o.frame.getNewIndex()
            self.emit.printout(self.emit.emitVAR(idx,ast.name,ast.typ,o.frame.getStartLabel(),o.frame.getEndLabel()))
            return Symbol(ast.name,ast.typ,Index(idx))
            
    def visitBlock(self,ast,o):
        o.frame.enterScope(False)
        local = reduce(lambda acc,ele: SubBody(o.frame,[self.visit(ele,acc)]+acc.sym),ast.decl,SubBody(o.frame,[]))
        self.emit.printout(self.emit.emitLABEL(o.frame.getStartLabel(),o.frame))
        list(map(lambda ele: self.visit(ele,SubBody(o.frame,local.sym+o.sym)),ast.stmts))
        self.emit.printout(self.emit.emitLABEL(o.frame.getEndLabel(),o.frame))
        o.frame.exitScope()


    # Cau 1
    def lookup(self, query, lst, func):
        for i in range(len(lst)):
            if func(lst[i]) == query:
                return lst[i]
        return None
    
    def visitId(self, ctx, o):
        sym = self.lookup(ctx.name,o.sym,lambda x: x.name)
        txt=''

        if o.isLeft:
            if isinstance(sym.value.value, int):
                txt = self.emit.emitWRITEVAR(ctx.name, sym.mtype, sym.value.value, o.frame)
            else:
                txt = self.emit.emitPUTSTATIC(sym.value.value+'.'+ctx.name, sym.mtype, o.frame)
        elif isinstance(sym.value.value, int):
            txt = self.emit.emitREADVAR(ctx.name,sym.mtype,sym.value.value,o.frame)
        else:
            txt = self.emit.emitGETSTATIC(sym.value.value+'.'+ctx.name,sym.mtype,o.frame)
        
        return txt, sym.mtype
        
    # Cau 2
    def visitAssign(self,ctx,o):
        text = ''
        if type(ctx.rhs) is Id:
            text = self.visitId(ctx.rhs, Access(o.frame, o.sym, False, False))[0]
        else:
            text = self.visitIntLiteral(ctx.rhs, Access(o.frame, o.sym, False, False))[0]
        text1, typ_l = self.visitId(ctx.lhs, Access(o.frame, o.sym, True, False))
        self.emit.printout(text+text1)
        return '', typ_l

    # Cau 3
    def visitIf(self,ctx,o):
        label1 = o.frame.getNewLabel()
        label2 = o.frame.getNewLabel()
        label3 = o.frame.getNewLabel()
        
        txt = self.visit(ctx.expr, Access(o.frame, o.sym, False, False))[0]
        self.emit.printout(txt)
        self.emit.printout(self.emit.emitPUSHICONST(0,o.frame))
        self.emit.printout(self.emit.emitRELOP('==',IntType(),label2,label1,o.frame))
        
        #Label1:
        self.emit.printout(self.emit.emitLABEL(label1,o.frame))
        if ctx.tstmt:
            self.visit(ctx.tstmt, Access(o.frame, o.sym, False, False))
        self.emit.printout(self.emit.emitGOTO(label3,o.frame))
        
        #Label2:
        self.emit.printout(self.emit.emitLABEL(label2,o.frame))
        if ctx.estmt:
            self.visit(ctx.estmt, Access(o.frame, o.sym, False, False))
        
        #Label3:
        self.emit.printout(self.emit.emitLABEL(label3,o.frame))
        return '', IntType()

    # Cau 4
    def visitWhile(self,ctx,o):
        
        o.frame.enterLoop()
        label0 = o.frame.getContinueLabel()
        label2 = o.frame.getBreakLabel()
        label1 = o.frame.getNewLabel()
        
        #Label0:
        self.emit.printout(self.emit.emitLABEL(label0,o.frame))
        
        #Condition expr:
        self.emit.printout(self.visit(ctx.expr,Access(o.frame,o.sym,False,False))[0])
        self.emit.printout(self.emit.emitPUSHICONST(0,o.frame))
        self.emit.printout(self.emit.emitRELOP('==',IntType(),label2,label1,o.frame))
        
        #Label1:
        self.emit.printout(self.emit.emitLABEL(label1,o.frame))
        
        #Statement
        self.visit(ctx.stmt,Access(o.frame,o.sym,False,False))
        
        #goto Condition
        self.emit.printout(self.emit.emitGOTO(label0,o.frame))
        
        #Label2:
        self.emit.printout(self.emit.emitLABEL(label2,o.frame))
        
        o.frame.exitLoop()

    # Cau 5
    def visitFuncDecl(self,ctx,o):
        o.frame = Frame(ctx.name,ctx.returnType)
        o.frame.enterScope(False)
        
        label0 = o.frame.getStartLabel()
        label1 = o.frame.getEndLabel()
        # print(Symbol.__init__.__code__.co_varnames)
        para_typ_lst = list(map(lambda x:x.typ, ctx.param))
        lexeme = ctx.name + '(' + ''.join(map(lambda x:self.emit.getJVMType(x), para_typ_lst)) + ')'
        self.emit.printout(self.emit.emitMETHOD(lexeme=lexeme,inType=ctx.returnType,isStatic=True))
        
        for i in range(len(ctx.param)):
            indx = o.frame.getNewIndex()
            self.emit.printout(self.emit.emitVAR(indx, ctx.param[i].name, ctx.param[i].typ, label0, label1))
        for i in range(len(ctx.body[0])):
            indx = o.frame.getNewIndex()
            self.emit.printout(self.emit.emitVAR(indx, ctx.body[0][i].name, ctx.body[0][i].typ, label0, label1))
        
        #Label0:
        self.emit.printout(self.emit.emitLABEL(label0,o.frame))
        
        #Body
        for stmt in ctx.body[1]:
            self.visit(stmt, Access(o.frame,o.sym,False,False))
        
        #Label1:
        self.emit.printout(self.emit.emitLABEL(label1,o.frame))
        
        #limit
        self.emit.printout(self.emit.emitENDMETHOD(o.frame))

        
        o.frame.exitScope()
        return Symbol(ctx.name, MType(para_typ_lst,ctx.returnType), CName('MCClass'))

    # Cau 6
    def visitBinExpr(self, ast, o):
        e1c,e1t = self.visit(ast.e1,o)
        if ast.op in ['+','-','*','/','>','<','>=','<=','==','!=']:
            e2c,e2t = self.visit(ast.e2,o)
            if type(e1t) is type(e2t):
                ret = e1t
            if type(e1t) is IntType and (type(e2t) is FloatType or ast.op == '/'):
                e1c += self.emit.emitI2F(o.frame)
                ret = FloatType()
            if type(e2t) is IntType and (type(e1t) is FloatType or ast.op == '/'):
                e2c += self.emit.emitI2F(o.frame)
                ret = FloatType()
            if ast.op in ['+','-']:
                return e1c + e2c + self.emit.emitADDOP(ast.op,ret,o.frame),ret
            elif ast.op in ['*','/']:
                return e1c + e2c + self.emit.emitMULOP(ast.op,ret,o.frame),ret
            else:
                return e1c + e2c + self.emit.emitREOP(ast.op,ret,o.frame),BoolType()
        else:
            resLabel = o.frame.getNewLabel()
            nextLabel = o.frame.getNewLabel()
            if ast.op == '&&':
                ctlcode = self.emit.emitIFFALSE(resLabel,o.frame)
            else:
                ctlcode = self.emit.emitIFTRUE(resLabel,o.frame)
            e2c,e2t = self.visit(ast.e2,o)
            gotocode = self.emit.emitGOTO(nextLabel,o.frame)
            lcode = self.emit.emitLABEL(resLabel,o.frame)
            if ast.op == '&&':
                rcode = self.emit.emitPUSHICONST("false",o.frame)
            else:
                rcode = self.emit.emitPUSHICONST("true",o.frame)
            ncode = self.emit.emitLABEL(nextLabel,o.frame)

            return e1c+ctlcode+e2c+gotocode+lcode+rcode+ncode, BoolType()