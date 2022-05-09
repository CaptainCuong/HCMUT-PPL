from D96Visitor import D96Visitor
from D96Parser import D96Parser
from AST import *
from functools import reduce

class ASTGeneration(D96Visitor):
    def visitProgram(self, ctx):
        return Program(list(map(lambda x: x.accept(self), ctx.class_dcl())))

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
        # print(ctx.parentCtx.ID(0).getText())
        if ctx.getChildCount() > 2:
            memlist = []
            for i in range(1, ctx.getChildCount()-1):
                memlist += ctx.getChild(i).accept(self)
                if isinstance(memlist[-1], MethodDecl) and memlist[-1].name.name == 'main' \
                and memlist[-1].param == [] and ctx.parentCtx.ID(0).getText() == 'Program':
                    memlist[-1].kind = Static()
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
            id_list.append(Id(ctx.getChild(1).getText()))
            id_list += ctx.att_dcl_list().accept(self)['ID']
            value += ctx.att_dcl_list().accept(self)['value']
            value.append(ctx.expr_lit().accept(self))
            data_type = ctx.att_dcl_list().accept(self)['data_type']

        def assigned_att(id_list, data_type, value):
            ret = []
            for ID_set, value in zip(id_list, value):
                if VAL and ID_set.name[0] == '$':
                    ret.append(AttributeDecl(Static(), ConstDecl(ID_set, data_type, value)))
                elif VAL:
                    ret.append(AttributeDecl(Instance(), ConstDecl(ID_set, data_type, value)))
                elif VAR and ID_set.name[0] == '$':
                    ret.append(AttributeDecl(Static(), VarDecl(ID_set, data_type, value)))
                elif VAR:
                    ret.append(AttributeDecl(Instance(), VarDecl(ID_set, data_type, value)))
            return ret

        def no_assigned_att(id_list, data_type):
            ret = []
            for ID_set in id_list:
                if VAL and ID_set.name[0] == '$':
                    ret.append(AttributeDecl(Static(), ConstDecl(ID_set, data_type, None if isinstance(data_type, ClassType) else None)))
                elif VAL:
                    ret.append(AttributeDecl(Instance(), ConstDecl(ID_set, data_type, None if isinstance(data_type, ClassType) else None)))
                elif VAR and ID_set.name[0] == '$':
                    ret.append(AttributeDecl(Static(), VarDecl(ID_set, data_type, NullLiteral() if isinstance(data_type, ClassType) else None)))
                elif VAR:
                    ret.append(AttributeDecl(Instance(), VarDecl(ID_set, data_type, NullLiteral() if isinstance(data_type, ClassType) else None)))
            return ret

        if ASSIGNED:
            return assigned_att(id_list, data_type, value)
        return no_assigned_att(id_list, data_type)


    # Visit a parse tree produced by D96Parser#att_dcl_list.
    def visitAtt_dcl_list(self, ctx):
        if ctx.data_type():
            return {
                    'ID' : [],
                    'data_type' : ctx.data_type().accept(self),
                    'value' : []
                    }
        return {
                'ID' : [Id(ctx.getChild(1).getText())] + ctx.att_dcl_list().accept(self)['ID'],
                'data_type' : ctx.att_dcl_list().accept(self)['data_type'],
                'value' : ctx.att_dcl_list().accept(self)['value'] + [ctx.expr_lit().accept(self)]
                }


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
        return [MethodDecl(Static() if static else Instance(), Id(ID), ctx.para_dcl_list().accept(self), ctx.method_block().accept(self))]


    # Visit a parse tree produced by D96Parser#method_block.
    def visitMethod_block(self, ctx):
        stm_lst = []
        if ctx.getChildCount() > 2:
            for i in range(1, ctx.getChildCount()-1):
                if isinstance(ctx.getChild(i).accept(self), list):
                    stm_lst += ctx.getChild(i).accept(self)
                else:
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
        dtype = ctx.data_type().accept(self)
        return list(map(lambda x: VarDecl(x, dtype, None), ctx.id_list().accept(self)))


    # Visit a parse tree produced by D96Parser#stm.
    def visitStm(self, ctx):
        if ctx.method_invoke_stm():
            call_expr = ctx.getChild(0).accept(self)
            return CallStmt(call_expr.obj, call_expr.method, call_expr.param)
        return ctx.getChild(0).accept(self)


    # Visit a parse tree produced by D96Parser#for_in_stm.
    def visitFor_in_stm(self, ctx):
        ID = ctx.ID().getText()
        expr_lit = ctx.expr_lit()
        block = ctx.block_stm()
        if ctx.BY():
            return For(Id(ID), expr_lit[0].accept(self), expr_lit[1].accept(self), block.accept(self), expr_lit[-1].accept(self))
        return For(Id(ID), expr_lit[0].accept(self), expr_lit[1].accept(self), block.accept(self), None)


    # Visit a parse tree produced by D96Parser#if_stm.
    def visitIf_stm(self, ctx):
        if ctx.ELSE():
            return reduce(lambda x, y: If(y[0].accept(self),y[1].accept(self),x), list(zip(ctx.expr_lit()[-2::-1], ctx.block_stm()[-3::-1])), If(ctx.expr_lit()[-1].accept(self), ctx.block_stm()[-2].accept(self), ctx.block_stm()[-1].accept(self)))
        return reduce(lambda x, y: If(y[0].accept(self),y[1].accept(self),x), list(zip(ctx.expr_lit()[::-1], ctx.block_stm()[::-1])), None)


    # Visit a parse tree produced by D96Parser#block_stm.
    def visitBlock_stm(self, ctx):
        return Block(ctx.mn_stm().accept(self))


    # Visit a parse tree produced by D96Parser#mn_stm.
    def visitMn_stm(self, ctx):
        if ctx.getChildCount() > 0:
            if isinstance(ctx.stm().accept(self), list):
                return ctx.stm().accept(self) + ctx.mn_stm().accept(self)
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
        return Assign(ctx.expr_lit(0).accept(self), ctx.expr_lit(1).accept(self))


    # Visit a parse tree produced by D96Parser#return_stm.
    def visitReturn_stm(self, ctx):
        if ctx.expr_lit():
            return Return(ctx.expr_lit().accept(self))
        return Return(None)


    # Visit a parse tree produced by D96Parser#method_invoke_stm.
    def visitMethod_invoke_stm(self, ctx):
        return ctx.getChild(0).accept(self)


    # Visit a parse tree produced by D96Parser#var_dcl.
    def visitVar_dcl(self, ctx):
        if ctx.non_static_id_list():
            if ctx.VAL_VAR().getText() == 'Var':
                return [VarDecl(x, ctx.data_type().accept(self), NullLiteral() if isinstance(ctx.data_type().accept(self), ClassType) else None) for x in ctx.non_static_id_list().accept(self)]
            return [ConstDecl(x, ctx.data_type().accept(self), None if isinstance(ctx.data_type().accept(self), ClassType) else None) for x in ctx.non_static_id_list().accept(self)]
        
        ids = [Id(ctx.ID().getText())] + ctx.var_dcl_list().accept(self)['ID']
        dtype = ctx.var_dcl_list().accept(self)['dtype']
        expr = ctx.var_dcl_list().accept(self)['expr'] + [ctx.expr_lit().accept(self)]
        if ctx.VAL_VAR().getText() == 'Var':
            return [VarDecl(Id, dtype, Exp) for Id, Exp in zip(ids, expr)]
        return [ConstDecl(Id, dtype, Exp) for Id, Exp in zip(ids, expr)]
        

    # Visit a parse tree produced by D96Parser#var_dcl_list.
    def visitVar_dcl_list(self, ctx):
        if ctx.data_type():
            return {'ID':[], 'dtype':ctx.data_type().accept(self), 'expr': []}
        return {'ID': [Id(ctx.ID().getText())] + ctx.var_dcl_list().accept(self)['ID'],
                'dtype': ctx.var_dcl_list().accept(self)['dtype'],
                'expr': ctx.var_dcl_list().accept(self)['expr'] + [ctx.expr_lit().accept(self)]}


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


    # Visit a parse tree produced by D96Parser#expr_lit.
    def visitExpr_lit(self, ctx):
        precedence = {
                    # 'New':10, 
                    # '::':9, 
                    # '.':8, 
                    # '[,]':7, 
                    '!':6, 
                    '*':5, '/':5, '%':5, 
                    '+':4, '-':4, 
                    '&&':3, '||':3,
                    '==':2, '!=':2, '<':2, '>':2, '<=':2, '>=':2, 
                    '+.':1, '==.':1 }
        '''
        Do not have
        Static Access, Instance Access : FieldAccess
        Index operator :  ArrayCell
        Sign : Unary
        '''
        if ctx.NEW():
            return NewExpr(ctx.expr_lit(0).accept(self), ctx.expr_lit_list().accept(self))
        
        if ctx.ID() and ctx.getChildCount() == 1:
            if ctx.ID().getText() == 'Self':
                return SelfLiteral()
            return Id(ctx.ID().getText())
        
        if ctx.NULL() and ctx.getChildCount() == 1:
            return NullLiteral()
        
        if ctx.getChildCount() == 1:
            return ctx.getChild(0).accept(self)
        
        if ctx.getChildCount() == 4:
            left_ret = ctx.expr_lit(0).accept(self)
            if isinstance(left_ret, ArrayCell):
                return ArrayCell(left_ret.arr, left_ret.idx+[ctx.getChild(2).accept(self)])
            return ArrayCell(ctx.expr_lit(0).accept(self), [ctx.getChild(2).accept(self)])

        if ctx.getChildCount() == 6:
            return CallExpr(ctx.getChild(0).accept(self), Id(ctx.getChild(2).getText()), ctx.para_pass_list().accept(self))

        if ctx.getChildCount() == 3 and (ctx.DOT() or ctx.MEM_ACCESS_OP()):
            return FieldAccess(ctx.expr_lit(0).accept(self), Id(ctx.DOLLAR_ID().getText()) if ctx.DOLLAR_ID() else Id(ctx.ID().getText()))

        # if ctx.getChildCount() == 3 and (ctx.ADDOP() or ctx.SUBOP() or ctx.DIVOP() or ctx.MULOP()):
        #     return BinaryOp(ctx.getChild(1).getText(), ctx.expr_lit(0).accept(self), ctx.expr_lit(1).accept(self))

        if ctx.unary_op():
            return UnaryOp(ctx.unary_op().accept(self), ctx.expr_lit(0).accept(self))

        if ctx.binary_op():
            if isinstance(ctx.expr_lit(0).accept(self), BinaryOp) and \
            isinstance(ctx.expr_lit(1).accept(self), BinaryOp) \
            and not ctx.expr_lit(0).LB() \
            and not ctx.expr_lit(1).LB():
                if precedence[ctx.binary_op().accept(self)] > precedence[ctx.expr_lit(0).accept(self).op] and \
                precedence[ctx.binary_op().accept(self)] > precedence[ctx.expr_lit(1).accept(self).op] and \
                precedence[ctx.binary_op(0).accept(self)] >= precedence[ctx.expr_lit(1).accept(self).op]:
                    return BinaryOp(ctx.expr_lit(1).accept(self).op, BinaryOp(ctx.expr_lit(0).accept(self).op, ctx.expr_lit(0).accept(self).left, BinaryOp(ctx.binary_op().accept(self), ctx.expr_lit(0).accept(self).right, ctx.expr_lit(1).accept(self).left)), ctx.expr_lit(1).accept(self).right)

                if precedence[ctx.binary_op().accept(self)] <= precedence[ctx.expr_lit(0).accept(self).op] and \
                precedence[ctx.binary_op().accept(self)] >= precedence[ctx.expr_lit(1).accept(self).op]:
                    return BinaryOp(ctx.expr_lit(1).accept(self).op, BinaryOp(ctx.binary_op().accept(self), ctx.expr_lit(0).accept(self), ctx.expr_lit(1).accept(self).left),ctx.expr_lit(1).accept(self).right)

                if precedence[ctx.binary_op().accept(self)] > precedence[ctx.expr_lit(0).accept(self).op] and \
                precedence[ctx.binary_op().accept(self)] < precedence[ctx.expr_lit(1).accept(self).op]:
                    return BinaryOp(ctx.expr_lit(0).accept(self).op, ctx.expr_lit(0).accept(self).left, BinaryOp(ctx.binary_op(), ctx.expr_lit(0).accept(self).right, ctx.expr_lit(1).accept(self)))

                if precedence[ctx.binary_op().accept(self)] > precedence[ctx.expr_lit(0).accept(self).op] and \
                precedence[ctx.binary_op().accept(self)] == precedence[ctx.expr_lit(1).accept(self).op] and \
                precedence[ctx.binary_op(0).accept(self)] >= precedence[ctx.expr_lit(1).accept(self).op]:
                    return BinaryOp(ctx.expr_lit(0).op, ctx.expr_lit(0).accept(self).left, BinaryOp(ctx.binary_op().accept(self), BinaryOp(ctx.expr_lit(1).accept(self).op, ctx.expr_lit(0).accept(self).right, ctx.expr_lit(1).accept(self).left),ctx.expr_lit(1).accept(self).right))


            if isinstance(ctx.expr_lit(0).accept(self), BinaryOp) \
            and not ctx.expr_lit(0).LB() and \
            (isinstance(ctx.expr_lit(1).accept(self), BinaryOp) and ctx.expr_lit(1).LB() or\
                not isinstance(ctx.expr_lit(1), BinaryOp)):
                if precedence[ctx.binary_op().accept(self)] > precedence[ctx.expr_lit(0).accept(self).op]:
                    return BinaryOp(ctx.expr_lit(0).accept(self).op, ctx.expr_lit(0).accept(self).left, BinaryOp(ctx.binary_op().accept(self), ctx.expr_lit(0).accept(self).right, ctx.expr_lit(1).accept(self)))




            if isinstance(ctx.expr_lit(1).accept(self), BinaryOp) \
            and not ctx.expr_lit(1).LB() and \
            (isinstance(ctx.expr_lit(0).accept(self), BinaryOp) and ctx.expr_lit(0).LB() or\
                not isinstance(ctx.expr_lit(0), BinaryOp)):
                if precedence[ctx.binary_op().accept(self)] >= precedence[ctx.expr_lit(1).accept(self).op]:
                    return BinaryOp(ctx.expr_lit(1).op, BinaryOp(ctx.binary_op().accept(self), ctx.expr_lit(0).accept(self), ctx.expr_lit(1).accept(self).left), ctx.expr_lit(1).accept(self).right)

            return BinaryOp(ctx.binary_op().accept(self), ctx.expr_lit(0).accept(self), ctx.expr_lit(1).accept(self))

        return ctx.getChild(1).accept(self)


    # Visit a parse tree produced by D96Parser#expr_lit_list.
    def visitExpr_lit_list(self, ctx):
        return [x.accept(self) for x in ctx.expr_lit()]

    # Visit a parse tree produced by D96Parser#instance_method_invoke.
    def visitInstance_method_invoke(self, ctx):
        return CallExpr(ctx.expr_lit().accept(self), Id(ctx.ID().getText()), ctx.para_pass_list().accept(self))


    # Visit a parse tree produced by D96Parser#static_mehod_invoke.
    def visitStatic_mehod_invoke(self, ctx):
        return CallExpr(ctx.expr_lit().accept(self), Id(ctx.DOLLAR_ID().getText()), ctx.para_pass_list().accept(self))


    # Visit a parse tree produced by D96Parser#para_pass_list.
    def visitPara_pass_list(self, ctx):
        return ctx.expr_pro_list().accept(self)


    # Visit a parse tree produced by D96Parser#att_access.
    def visitAtt_access(self, ctx):
        return ctx.getChild(0).accept(self)


    # Visit a parse tree produced by D96Parser#instance_att_access.
    def visitInstance_att_access(self, ctx):
        explst = []
        for i in range(0, ctx.getChildCount(), 2):
            if isinstance(ctx.getChild(i), D96Parser.Expr_litContext):
                explst.append(ctx.getChild(i).accept(self))
            else:
                explst.append(Id(ctx.getChild(i).getText()))
        return reduce(lambda x, y: FieldAccess(x, y), explst)


    # Visit a parse tree produced by D96Parser#static_att_access.
    def visitStatic_att_access(self, ctx):
        explst = []
        for i in range(ctx.getChildCount(), 2):
            if isinstance(ctx.getChild(i), D96Parser.Expr_litContext):
                explst.append(ctx.getChild(i).accept(self))
            else:
                explst.append(Id(ctx.getChild(i).getText()))
        return reduce(lambda x, y: FieldAccess(x, y), explst)


    # Visit a parse tree produced by D96Parser#index_ele_pro.
    def visitIndex_ele_pro(self, ctx):
        return ArrayCell(Id(ctx.ID().getText()), reduce(lambda x, y: x+y,[x.accept(self) for x in ctx.expr_pro_list()]), [])


    # Visit a parse tree produced by D96Parser#index_ele.
    def visitIndex_ele(self, ctx):
        expr = ctx.expr_lit().accept(self)
        if isinstance(expr, ArrayCell):
            return ArrayCell(expr.arr, expr.idx + reduce(lambda x, y: x+y, [x.accept(self) for x in ctx.expr_lit_list()], []))

        return ArrayCell(expr, reduce(lambda x, y: x+y, [x.accept(self) for x in ctx.expr_lit_list()], []))


    # Visit a parse tree produced by D96Parser#expr_list.
    def visitExpr_list(self, ctx):
        if ctx.getChildCount() > 0:
            return list(map(lambda x: x.accept(self), ctx.expr()))
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
            return [ctx.index_arr().accept(self)] + ctx.index_arr_cmlist().accept(self)
        return []


    # Visit a parse tree produced by D96Parser#index_arr_cmlist.
    def visitIndex_arr_cmlist(self, ctx):
        if ctx.getChildCount() > 0:
            return [ctx.index_arr().accept(self)] + ctx.index_arr_cmlist().accept(self)
        return []


    # Visit a parse tree produced by D96Parser#index_arr.
    def visitIndex_arr(self, ctx):
        return ArrayLiteral(ctx.same_type_list().accept(self))


    # Visit a parse tree produced by D96Parser#mul_dim_arr.
    def visitMul_dim_arr(self, ctx):
        return ArrayLiteral(ctx.expr_lit_list().accept(self))


    # Visit a parse tree produced by D96Parser#same_type_list.
    def visitSame_type_list(self, ctx):
        return ctx.getChild(0).accept(self)


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
        return [Id(ctx.getChild(0).getText())] + ctx.id_cmlist().accept(self)


    # Visit a parse tree produced by D96Parser#id_cmlist.
    def visitId_cmlist(self, ctx):
        if ctx.getChildCount() == 0:
            return []
        return [Id(ctx.getChild(1).getText())] + ctx.id_cmlist().accept(self)


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
            floatlit = ctx.FLOATLIT().getText()
            if floatlit[0] == '.':
                floatlit = '0' + floatlit
            elif floatlit[0] == 'e':
                floatlit = '0' + floatlit
            return FloatLiteral(float(floatlit))
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
        return IntLiteral(0)


    # Visit a parse tree produced by D96Parser#data_type.
    def visitData_type(self, ctx):
        dtype = ctx.getChild(0).getText()
        if dtype == 'Int':
            return IntType()
        elif dtype == 'Float':
            return FloatType()
        elif dtype == 'Boolean':
            return BoolType()
        elif dtype == 'String':
            return StringType()
        elif dtype == 'Void':
            return VoidType()
        elif ctx.array_type():
            return ctx.array_type().accept(self)
        return ClassType(Id(dtype))

    # Visit a parse tree produced by D96Parser#size.
    def visitSize(self, ctx):
        if ctx.INTLIT_16():
            return int(ctx.INTLIT_16().getText()[2:], 16)
        if ctx.INTLIT_2():
            return int(ctx.INTLIT_2().getText()[2:], 2)
        if ctx.INTLIT_8():
            return int(ctx.INTLIT_8().getText()[1:], 8)
        if ctx.INTLIT_10():
            return int(ctx.INTLIT_10().getText(), 10)


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
