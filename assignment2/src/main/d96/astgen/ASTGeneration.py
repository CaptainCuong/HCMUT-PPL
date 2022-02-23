from D96Visitor import D96Visitor
from D96Parser import D96Parser
from AST import *
from functools import reduce

class ASTGeneration(D96Visitor):
    def visitProgram(self, ctx):
        # return Program([FuncDecl(Id("main"),
        #                          [],
        #                          self.visit(ctx.mptype()),
        #                          Block([], [self.visit(ctx.body())] if ctx.body() else []))])
        res = []
        for i in range(len(ctx.class_dcl())):
            res.append(ctx.class_dcl(i).accept(self))
        return Program(res)

    # Visit a parse tree produced by D96Parser#class_dcl.
    def visitClass_dcl(self, ctx):
        if ctx.getChildCount() > 3:
            return ClassDecl(Id(ctx.ID(0).getText()), ctx.class_body().accept(self), Id(ctx.ID(1).getText()))
        return ClassDecl(Id(ctx.ID(0).getText()), ctx.class_body().accept(self), None)


    # Visit a parse tree produced by D96Parser#class_body.
    def visitClass_body(self, ctx):
        '''
        Return a list of MethodDecl and AttributeDecl
        '''
        if ctx.getChildCount() > 2:
            memlist = []
            for i in range(1, ctx.getChildCount()-1):
                memlist += [ctx.getChild(i).accept(self)]
            return memlist
        return []


    # Visit a parse tree produced by D96Parser#expr_pro.
    def visitExpr_pro(self, ctx):
        return ctx.getChild(0).accept(self)


    # Visit a parse tree produced by D96Parser#att_dcl.
    def visitAtt_dcl(self, ctx):
        '''
        Return a list of AttributeDecl
        '''
        ASSIGNED = False
        VAL = False
        VAR = False
        if ctx.VAL_VAR().getText() == 'Val':
            VAL = True
        else:
            VAR = True

        res = []
        
        # List[(ID, Type, Expr)]
        id_list = []
        data_type = None
        value = []

        if ctx.id_list(): # not assigned
            id_list += ctx.id_list().accept(self)
            data_type = ctx.data_type().accept(self)
        else: # assigned
            ASSIGNED = True
            id_list.append(ctx.getChild(1).getText())
            value.append(ctx.expr_pro().accept(self))
            att_list = ctx.att_dcl_list().accept(self)
            id_list += att_list['ID']
            value += att_list['value']
            data_type = att_list['data_type']

        def assigned_att(id_list, data_type, value):
            ret = []
            for ID_set, value in zip(id_list, value):
                if VAL and ID_set[0] == '$':
                    ret.append(AttributeDecl(Static(), ConstDecl(ID_set, data_type, value)))
                elif VAL:
                    ret.append(AttributeDecl(Instance(), ConstDecl(ID_set, data_type, value)))
                elif VAR and ID_set[0] == '$':
                    ret.append(AttributeDecl(Static(), VarDecl(ID_set, data_type, value)))
                elif VAR:
                    ret.append(AttributeDecl(Instance(), VarDecl(ID_set, data_type, value)))
            return ret

        def no_assigned_att(id_list, data_type):
            ret = []
            for ID_set in id_list:
                if VAL and ID_set[0] == '$':
                    ret.append(AttributeDecl(Static(), ConstDecl(ID_set, data_type, None)))
                elif VAL:
                    ret.append(AttributeDecl(Instance(), ConstDecl(ID_set, data_type, None)))
                elif VAR and ID_set[0] == '$':
                    ret.append(AttributeDecl(Static(), VarDecl(ID_set, data_type, None)))
                elif VAR:
                    ret.append(AttributeDecl(Instance(), VarDecl(ID_set, data_type, None)))
            return ret

        if ASSIGNED:
            return assigned_att(id_list, data_type, value)
        return no_assigned_att(id_list, data_type)

    # Visit a parse tree produced by D96Parser#att_dcl_list.
    def visitAtt_dcl_list(self, ctx):
        ret = {
            'ID' : [],
            'data_type' : None,
            'value' : []
        }

        if ctx.data_type():
            ret['data_type'] = ctx.data_type().accept(self) 
        else:
            ret['ID'] += ctx.getChild(1)
            ret['value'] += ctx.expr_pro().accept(self)
            att_lst = ctx.att_dcl_list().accept(self)
            ret['ID'] += att_lst['ID']
            ret['value'] += att_lst['value']
            ret['data_type'] = att_lst['data_type']
        return ret


    # Visit a parse tree produced by D96Parser#method_dcl.
    def visitMethod_dcl(self, ctx):
        '''
        MethodDecl
        kind: SIKind
        name: Id
        param: List[VarDecl]
        body: Block
        '''
        ID = ctx.getChild(0).getText()
        static = (ID[0] == '$')
        para_lst = ctx.para_dcl_list().accept(self)
        return MethodDecl(Static() if static else Instance(), ID, ctx.para_dcl_list().accept(self), ctx.method_block().accept(self))


    # Visit a parse tree produced by D96Parser#method_block.
    def visitMethod_block(self, ctx):
        stm_lst = []
        if ctx.getChildCount() > 2:
            for i in range(1, ctx.getChildCount()-1):
                stm_lst.append(ctx.getChild(i).accept(self))
        return Block(stm_lst)


    # Visit a parse tree produced by D96Parser#para_dcl_list.
    def visitPara_dcl_list(self, ctx):
        '''
        Return List[VarDecl]
        '''
        if ctx.getChildCount() == 0:
            return []
        else:
            return ctx.para_dcl().accept(self) + ctx.para_dcl_smcllist().accept(self)


    # Visit a parse tree produced by D96Parser#para_dcl_smcllist.
    def visitPara_dcl_smcllist(self, ctx):
        if ctx.getChildCount() > 0:
            return ctx.para_dcl().accept(self) + ctx.para_dcl_smcllist().accept(self)
        return []


    # Visit a parse tree produced by D96Parser#para_dcl.
    def visitPara_dcl(self, ctx):
        ID_lst = ctx.id_list().accept(self)
        data_type = ctx.data_type().accept(self)
        ret = []
        for ID in ID_lst:
            ret.append(VarDecl(ID, data_type, None))
        return ret


    # Visit a parse tree produced by D96Parser#stm.
    def visitStm(self, ctx):
        return ctx.getChild(0).accept(self)


    # Visit a parse tree produced by D96Parser#for_in_stm.
    def visitFor_in_stm(self, ctx):
        ID = ctx.ID().accept(self)
        expr_pro = ctx.expr_pro()
        block = ctx.block_stm().accept(self)
        if ctx.ELSE():
            return For(ID, expr_pro[0].accept(self), expr_pro[1].accept(self), block.accept(self), expr_pro[-1].accept(self))
        return For(ID, expr_pro[0].accept(self), expr_pro[1].accept(self), block.accept(self), None)


    # Visit a parse tree produced by D96Parser#if_stm.
    def visitIf_stm(self, ctx):
        if ctx.ELSE():
            return If(ctx.expr_pro().accept(self), ctx.block_stm(0).accept(self), ctx.block_stm()[-1].accept(self))
        return If(ctx.expr_pro().accept(self), ctx.block_stm(0).accept(self))


    # Visit a parse tree produced by D96Parser#block_stm.
    def visitBlock_stm(self, ctx):
        return Block(ctx.mn_stm().accept(self))


    # Visit a parse tree produced by D96Parser#mn_stm.
    def visitMn_stm(self, ctx):
        if ctx.getChildCount() > 0:
            return [ctx.stm().accept(self)] + ctx.mn_stm().accept(self)
        return []


    # Visit a parse tree produced by D96Parser#continue_stm.
    def visitContinue_stm(self, ctx):
        return Continue()


    # Visit a parse tree produced by D96Parser#break_stm.
    def visitBreak_stm(self, ctx):
        return Break()


    # Visit a parse tree produced by D96Parser#asm_stm.
    def visitAsm_stm(self, ctx):
        if ctx.ID():
            return Assign(Id(ctx.ID().getText()), ctx.expr_pro().accept(self))
        return Assign(ctx.getChild(0).accept(self), ctx.expr_pro().accept(self))


    # Visit a parse tree produced by D96Parser#return_stm.
    def visitReturn_stm(self, ctx):
        return Assign(ctx.getChild(0), ctx.getChild(2))


    # Visit a parse tree produced by D96Parser#method_invoke_stm.
    def visitMethod_invoke_stm(self, ctx):
        return ctx.getChild(0).accept(self)


    # Visit a parse tree produced by D96Parser#var_dcl.
    def visitVar_dcl(self, ctx):
        if ctx.non_static_id_list():
            return [VarDecl(x, ctx.data_type()) for x in ctx.non_static_id_list().accept(self)]
        ids = [Id(ctx.ID().accept(self))] + ctx.var_dcl_list(self).accept(self)['ID']
        dtype = ctx.var_dcl_list(self).accept(self)['dtype']
        expr = ctx.var_dcl_list().accept(self)['expr'] + [ctx.expr_pro().accept(self)]

        ret = []
        for i in range(len(ids)):
            ret += [VarDecl(ids[i], dtype, expr[i])]
        return ret

    # Visit a parse tree produced by D96Parser#var_dcl_list.
    def visitVar_dcl_list(self, ctx):
        if ctx.data_type():
            return {'ID':[], 'dtype':ctx.data_type().accept(self), 'expr': []}
        return {'ID': [Id(ctx.ID().accept(self))] + ctx.var_dcl_list()['ID'],
                'dtype': ctx.var_dcl_list()['dtype'],
                'expr': ctx.var_dcl_list().accept(self) + [ctx.expr_pro().accept(self)]}


    # Visit a parse tree produced by D96Parser#expr_pro_list.
    def visitExpr_pro_list(self, ctx):
        if ctx.getChildCount() > 0:
            return [ctx.expr_pro().accept(self)] + ctx.expr_pro_cmlist().accept(self)
        return []


    # Visit a parse tree produced by D96Parser#expr_pro_cmlist.
    def visitExpr_pro_cmlist(self, ctx):
        if ctx.getChildCount() > 0:
            return [ctx.expr_pro().accept(self)] + ctx.expr_pro_cmlist().accept(self)
        return []


    # Visit a parse tree produced by D96Parser#expr.
    def visitExpr(self, ctx):
        return ctx.getChild(0).accept(self)


    # Visit a parse tree produced by D96Parser#expr_lit.
    def visitExpr_lit(self, ctx):
        if ctx.ID():
            if ctx.ID().getText() == 'Self':
                return SelfLiteral()
            return Id(ctx.ID().getText())
        if ctx.NULL():
            return NullLiteral()
        if ctx.getChildCount() == 1:
            return ctx.getChild(0).accept(self)

        if ctx.getChildCount() == 4:
            return ArrayCell(ctx.expr_lit(0).accept(self), ctx.getChild(2).accept(self))
        
        if ctx.getChildCount() == 6:
            return CallStmt(ctx.getChild(0).accept(self), Id(ctx.getChild(2).getText()), ctx.para_pass_list().accept(self))

        if ctx.getChildCount() == 3 and (ctx.DOT() or ctx.MEM_ACCESS_OP()):
            return FieldAccess(ctx.expr_lit(0).accept(self), Id(ctx.DOLLAR_ID().getText()) if ctx.DOLLAR_ID() else ctx.expr_lit(1).accept(self))

        if ctx.unary_op():
            return UnaryOp(ctx.unary_op().accept(self), ctx.expr_lit(0).accept(self))
        if ctx.binary_op():
            return BinaryOp(ctx.binary_op().accept(self), ctx.expr_lit(0).accept(self), ctx.expr_lit(1).accept(self))
        return ctx.getChild(0).accept(self)


    # Visit a parse tree produced by D96Parser#object_ini.
    def visitObject_ini(self, ctx):
        return NewExpr(Id(ctx.ID().getText()), ctx.expr_pro_list().accept(self))
 

    # Visit a parse tree produced by D96Parser#instance_method_invoke.
    def visitInstance_method_invoke(self, ctx):
        return CallStmt(ctx.expr_lit().accept(self), Id(ctx.ID().getText()), ctx.para_pass_list().accept(self))


    # Visit a parse tree produced by D96Parser#static_mehod_invoke.
    def visitStatic_mehod_invoke(self, ctx):
        return CallStmt(ctx.expr_lit().accept(self), Id(ctx.DOLLAR_ID().getText()), ctx.para_pass_list().accept(self))


    # Visit a parse tree produced by D96Parser#para_pass_list.
    def visitPara_pass_list(self, ctx):
        return ctx.expr_pro_list().accept(self)


    # Visit a parse tree produced by D96Parser#att_access.
    def visitAtt_access(self, ctx):
        return ctx.getChild(0).accept(self)


    # Visit a parse tree produced by D96Parser#instance_att_access.
    def visitInstance_att_access(self, ctx):
        nodecnt = ctx.getChildCount()
        explst = []
        for i in range(0, nodecnt, 2):

            explst.append(ctx.getChild(i).accept(self))
        return reduce(lambda x, y: FieldAccess(x, y), explst)


    # Visit a parse tree produced by D96Parser#static_att_access.
    def visitStatic_att_access(self, ctx):
        nodecnt = ctx.getChildCount()
        explst = []
        for i in range(0, nodecnt, 2):
            explst.append(ctx.getChild(i).accept(self))
        return reduce(lambda x, y: FieldAccess(x, y), explst)


    # Visit a parse tree produced by D96Parser#index_ele_pro.
    def visitIndex_ele_pro(self, ctx):
        return reduce(lambda x, y: ArrayCell(x, y), [Id(ctx.ID().getText())] + ctx.expr_pro_list().accept(self))


    # Visit a parse tree produced by D96Parser#index_ele.
    def visitIndex_ele(self, ctx):
        return reduce(lambda x, y: ArrayCell(x, y), [Id(ctx.ID().getText())] + ctx.expr_list().accept(self))


    # Visit a parse tree produced by D96Parser#expr_list.
    def visitExpr_list(self, ctx):
        if ctx.getChildCount() > 0:
            return map(lambda x: x.accept(self), ctx.expr())
        return []


    # Visit a parse tree produced by D96Parser#int_object.
    def visitInt_object(self, ctx): # Not used
        if ctx.ID():
            return Id(ctx.ID().getText())
        return ctx.getChild(0).accept(self)


    # Visit a parse tree produced by D96Parser#float_object.
    def visitFloat_object(self, ctx): # Not used
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.FLOATLIT():
            return ctx.FloatLiteral(float(ctx.FLOATLIT().getText()))
        return ctx.getChild(0).accept(self)


    # Visit a parse tree produced by D96Parser#index_arr_list.
    def visitIndex_arr_list(self, ctx):
        if ctx.getChildCount() > 0:
            return [ctx.index_arr.accept(self)] + ctx.index_arr_cmlist().accept(self)
        return []


    # Visit a parse tree produced by D96Parser#index_arr_cmlist.
    def visitIndex_arr_cmlist(self, ctx):
        if ctx.getChildCount() > 0:
            return [ctx.index_arr.accept(self)] + ctx.index_arr_cmlist().accept(self)
        return []


    # Visit a parse tree produced by D96Parser#index_arr.
    def visitIndex_arr(self, ctx):
        return ArrayLiteral(ctx.same_type_list().accept(self))


    # Visit a parse tree produced by D96Parser#mul_dim_arr.
    def visitMul_dim_arr(self, ctx):
        return ArrayLiteral(ctx.index_arr_list().accept(self))


    # Visit a parse tree produced by D96Parser#same_type_list.
    def visitSame_type_list(self, ctx):
        return self.getChild(0).accept(self)


    # Visit a parse tree produced by D96Parser#string_op.
    def visitString_op(self, ctx): # Not used
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#bool_op.
    def visitBool_op(self, ctx): # Not used
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#relation_op.
    def visitRelation_op(self, ctx): # Not used
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#int_op.
    def visitInt_op(self, ctx): # Not used
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#float_op.
    def visitFloat_op(self, ctx): # Not used
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#lit_list.
    def visitLit_list(self, ctx): # Not used
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#lit_cmlist.
    def visitLit_cmlist(self, ctx):
        if ctx.getChildCount() > 0:
            return [ctx.lit().accept(self)] + ctx.lit_cmlist().accept(self)
        return []


    # Visit a parse tree produced by D96Parser#non_static_id_list.
    def visitNon_static_id_list(self, ctx):
        if ctx.getChildCount() > 0:
            return [Id(ctx.ID().getText())] + ctx.non_static_id_cmlist().accept(self)
        return []


    # Visit a parse tree produced by D96Parser#non_static_id_cmlist.
    def visitNon_static_id_cmlist(self, ctx):
        if ctx.getChildCount() > 0:
            return [Id(ctx.ID().getText())] + ctx.non_static_id_cmlist().accept(self)
        return []


    # Visit a parse tree produced by D96Parser#id_list.
    def visitId_list(self, ctx):
        '''
        Return List[ID]
        '''
        if ctx.getChildCount() == 0:
            return []
        return [ctx.getChild(0).getText()] + ctx.id_cmlist().accept(self)


    # Visit a parse tree produced by D96Parser#id_cmlist.
    def visitId_cmlist(self, ctx):
        if ctx.getChildCount() == 0:
            return []
        return [ctx.getChild(1).getText()] + ctx.id_cmlist().accept(self)


    # Visit a parse tree produced by D96Parser#int_gen_list.
    def visitInt_gen_list(self, ctx):
        if ctx.getChildCount() > 0:
            return [ctx.int_gen().accept(self)] + ctx.int_gen_cm().accept(self)
        return []


    # Visit a parse tree produced by D96Parser#int_gen_cm.
    def visitInt_gen_cm(self, ctx):
        if ctx.getChildCount() > 0:
            return [ctx.int_gen().accept(self)] + ctx.int_gen_cm().accept(self)
        return []


    # Visit a parse tree produced by D96Parser#bool_list.
    def visitBool_list(self, ctx):
        if ctx.getChildCount() > 0:
            return [BooleanLiteral(ctx.BOOLIT().getText()=='True')] + ctx.bool_list_cm().accept(self)
        return []


    # Visit a parse tree produced by D96Parser#bool_list_cm.
    def visitBool_list_cm(self, ctx):
        if ctx.getChildCount() > 0:
            return [BooleanLiteral(ctx.BOOLIT().getText()=='True')] + ctx.bool_list_cm().accept(self)
        return []


    # Visit a parse tree produced by D96Parser#float_list.
    def visitFloat_list(self, ctx):
        if ctx.getChildCount() > 0:
            return [FloatLiteral(float(ctx.FLOATLIT().getText()))] + ctx.float_list_cm().accept(self)
        return []


    # Visit a parse tree produced by D96Parser#float_list_cm.
    def visitFloat_list_cm(self, ctx):
        if ctx.getChildCount() > 0:
            return [FloatLiteral(float(ctx.FLOATLIT().getText()))] + ctx.float_list_cm().accept(self)
        return []


    # Visit a parse tree produced by D96Parser#string_list.
    def visitString_list(self, ctx):
        if ctx.getChildCount() > 0:
            return [StringLiteral(ctx.STRINGLIT().getText())] + ctx.string_list_cm().accept(self)
        return []


    # Visit a parse tree produced by D96Parser#string_list_cm.
    def visitString_list_cm(self, ctx):
        if ctx.getChildCount() > 0:
            return [StringLiteral(ctx.STRINGLIT().getText())] + ctx.string_list_cm().accept(self)
        return []


    # Visit a parse tree produced by D96Parser#lit.
    def visitLit(self, ctx):
        if ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        if ctx.BOOLIT():
            return BooleanLiteral(ctx.BOOLIT().getText() == 'True')
        if ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())
        return ctx.int_gen().accept(self)


    # Visit a parse tree produced by D96Parser#int_gen.
    def visitInt_gen(self, ctx):
        if ctx.INTLIT_16():
            return IntLiteral(int(ctx.INTLIT_16().getText()[2:], 16))
        if ctx.INTLIT_2():
            return IntLiteral(int(ctx.INTLIT_2().getText()[2:], 2))
        if ctx.INTLIT_8():
            return IntLiteral(int(ctx.INTLIT_8().getText()[1:], 8))
        if ctx.INTLIT_10():
            return IntLiteral(int(ctx.INTLIT_10().getText(), 10))
        if ctx.ZERO_10():
            return IntLiteral(0)


    # Visit a parse tree produced by D96Parser#data_type.
    def visitData_type(self, ctx):
        dtype = ctx.getChild(0).getText()
        if dtype == 'Int':
            return IntType()
        elif dtype == 'Float':
            return FloatType()
        elif dtype == 'Bool':
            return BoolType()
        elif dtype == 'String':
            return StringType()
        elif dtype == 'Void':
            return VoidType()
        elif ctx.array_type():
            return ctx.array_type().accept(self)

    # Visit a parse tree produced by D96Parser#size.
    def visitSize(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#array_type.
    def visitArray_type(self, ctx):
        return ArrayType(ctx.size().accept(self), ctx.data_type().accept(self))


    # Visit a parse tree produced by D96Parser#unary_op.
    def visitUnary_op(self, ctx):
        return ctx.getChild(0).getText()


    # Visit a parse tree produced by D96Parser#binary_op.
    def visitBinary_op(self, ctx):
        return ctx.getChild(0).getText()


    # Visit a parse tree produced by D96Parser#zero.
    def visitZero(self, ctx): # Not used
        return self.visitChildren(ctx)
