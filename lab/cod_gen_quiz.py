#1
    def visitIntLiteral(self,ctx,o):
        
        return self.emit.emitPUSHICONST(ctx.value, o.frame), IntType()
#2
    def visitFloatLiteral(self,ctx,o):
        return self.emit.emitPUSHFCONST(ctx.value, o.frame), FloatType()
#3
    def visitBinExpr(self,ctx,o):
        if ctx.op in ['+','-','*','/']:
            if isinstance(ctx.e1, BinExpr):
                self.emit.printout(self.visitBinExpr(ctx.e1, o)[0])
            else: 
                self.emit.printout(self.emit.emitPUSHICONST(ctx.e1.value, o.frame))
            
            if isinstance(ctx.e2, BinExpr):
                self.emit.printout(self.visitBinExpr(ctx.e2, o)[0])
            else:
                self.emit.printout(self.emit.emitPUSHICONST(ctx.e2.value, o.frame))
            
            if ctx.op == '+':
                return self.emit.emitADDOP('+', IntType(), o.frame), IntType()
            if ctx.op == '-':
                return self.emit.emitADDOP('-', IntType(), o.frame), IntType()
            if ctx.op == '*':
                return self.emit.emitMULOP('*', IntType(), o.frame), IntType()
            if ctx.op == '/':
                return self.emit.emitMULOP('/', IntType(), o.frame), IntType()
            
        if ctx.op in ['+.','-.','*.','/.']:
            if isinstance(ctx.e1, BinExpr):
                self.emit.printout(self.visitBinExpr(ctx.e1, o)[0])
            else: 
                self.emit.printout(self.emit.emitPUSHFCONST(ctx.e1.value, o.frame))
            
            if isinstance(ctx.e2, BinExpr):
                self.emit.printout(self.visitBinExpr(ctx.e2, o)[0])
            else:
                self.emit.printout(self.emit.emitPUSHFCONST(ctx.e2.value, o.frame))
                
            if ctx.op == '+.':
                return self.emit.emitADDOP('+', FloatType(), o.frame), FloatType()
            if ctx.op == '-.':
                return self.emit.emitADDOP('-', FloatType(), o.frame), FloatType()
            if ctx.op == '*.':
                return self.emit.emitMULOP('*', FloatType(), o.frame), FloatType()
            if ctx.op == '/.':
                return self.emit.emitMULOP('/', FloatType(), o.frame), FloatType()
#4
    def visitId(self,ctx,o):
        sym = self.lookup(ctx.name,o.sym,lambda x: x.name)
        if isinstance(sym.value.value, int):
            return self.emit.emitREADVAR(ctx.name, sym.mtype, sym.value.value, o.frame), IntType()
        else:
            return self.emit.emitGETSTATIC(sym.value.value + '.' + ctx.name, sym.mtype, o.frame), IntType()
#5
    def visitBinExpr(self,ctx,o):
        type1 = None
        type2 = None
        text = ''
        ret_txt = ''
        ######### e1 #########
        if isinstance(ctx.e1, IntLiteral):
            text, type1 = self.emit.emitPUSHICONST(ctx.e1.value, o.frame), IntType()
            ret_txt += text
            if ctx.op in ['>','<','>=','<=','!=','==','/']: 
                type1 = FloatType()
                ret_txt += self.emit.emitI2F(o.frame)
        elif isinstance(ctx.e1, FloatLiteral):
            text, type1 = self.emit.emitPUSHFCONST(str(ctx.e1.value), o.frame), FloatType()
            ret_txt += text
        else:
            text, type1 = self.visitBinExpr(ctx.e1, o)
            ret_txt += text
            if ctx.op in ['>','<','>=','<=','!=','==','/'] and isinstance(type1, IntType):
                type1 = FloatType()
                ret_txt += self.emit.emitI2F(o.frame)
                
        ######### e2 #########
        if isinstance(ctx.e2, IntLiteral):
            text, type2 = self.emit.emitPUSHICONST(ctx.e2.value, o.frame), IntType()
            ret_txt += text
            if ctx.op in ['>','<','>=','<=','!=','==','/'] or isinstance(type1, FloatType):
                type2 = FloatType()
                text = self.emit.emitI2F(o.frame)
                ret_txt += text
        elif isinstance(ctx.e2, FloatLiteral):
            text, type2 = self.emit.emitPUSHFCONST(str(ctx.e2.value), o.frame), FloatType()
            if isinstance(type1, IntType):
                type1 = FloatType()
                ret_txt += self.emit.emitI2F(o.frame)
            ret_txt += text
        else:
            text, type2 = self.visitBinExpr(ctx.e2, o)
            if ctx.op in ['>','<','>=','<=','!=','==','/'] and isinstance(type2, IntType): ret_txt += text; ret_txt += self.emit.emitI2F(o.frame)
            elif isinstance(type1, FloatType) and isinstance(type2, IntType): ret_txt += text; ret_txt += self.emit.emitI2F(o.frame)
            elif isinstance(type1, IntType) and isinstance(type2, FloatType): ret_txt += self.emit.emitI2F(o.frame); ret_txt += text
            else: ret_txt += text

        ######### op #########
        if ctx.op in ['+','-','*']:
            if isinstance(type1, IntType) and isinstance(type2, IntType):
                if ctx.op in ['+','-']:
                    ret_txt += self.emit.emitADDOP(ctx.op,IntType(),o.frame)
                    return ret_txt, IntType()
                else:
                    ret_txt += self.emit.emitMULOP(ctx.op,IntType(),o.frame)
                    return ret_txt, IntType()
                
            if ctx.op in ['+','-']:
                ret_txt += self.emit.emitADDOP(ctx.op,FloatType(),o.frame)
                return ret_txt, FloatType()
            else:
                ret_txt += self.emit.emitMULOP(ctx.op,FloatType(),o.frame)
                return ret_txt, FloatType()
        if ctx.op == '/': 
            ret_txt += self.emit.emitMULOP(ctx.op,FloatType(),o.frame)
            return ret_txt, FloatType()
        
        
        if ctx.op in ['>','<','>=','<=','!=','==']:
            ret_txt += self.emit.emitREOP(ctx.op,BoolType(),o.frame)
            return ret_txt, BoolType()
#6
    def visitVarDecl(self,ctx,o):
        # if o.frame:
        #     print(ctx.name+':\n\tIndex Local',o.frame.indexLocal)
        #     print('\tCurrent Label: ',o.frame.currentLabel)
        #     print('\tCurrent Label: ',o.frame.currentLabel)
        #     print('\tStart Label: ',o.frame.startLabel)
        #     print('\tEnd Label: ',o.frame.endLabel)
        #     print('\tCurrent Index: ',o.frame.currIndex)
        # else:
        #     print(ctx.name+': No frame')
        #     print(len(o.sym))

        if not o.frame:
            self.emit.printout(self.emit.emitATTRIBUTE(ctx.name,ctx.typ,False))
            return Symbol(ctx.name,ctx.typ,CName('MCClass'))
        else:
            self.emit.printout(self.emit.emitVAR(o.frame.currIndex,ctx.name,ctx.typ,o.frame.startLabel[-1],o.frame.endLabel[-1]))
            o.frame.setCurrIndex(o.frame.getCurrIndex()+1)
            return Symbol(ctx.name,ctx.typ,Index(o.frame.getCurrIndex()-1))

###################################################################################################
