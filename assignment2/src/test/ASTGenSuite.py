import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_0(self):
        line = '''Class _X{Constructor (x:Bool){} }Class C:_5{$7(_,d,__:Array [Array [Boolean ,02],0X1E];_ED3_,_:L0;c:_){Continue ; X.a = 5;} }'''
        expect = '''Program([ClassDecl(Id(_X),[MethodDecl(Id(Constructor),Instance,[],Block([],[]))]),ClassDecl(Id(C),Id(_5),[MethodDecl(Id($7),Static,[param(Id(_),ArrayType(30,ArrayType(2,BoolType))),param(Id(d),ArrayType(30,ArrayType(2,BoolType))),param(Id(__),ArrayType(30,ArrayType(2,BoolType))),param(Id(_ED3_),ClassType(Id(L0))),param(Id(_),ClassType(Id(L0))),param(Id(c),ClassType(Id(_)))],Block([],[Continue]))])])'''
        self.assertTrue(TestAST.test(line, expect, 0))

    def test_1(self):
        line = '''Class I{}Class G{Constructor (U:Array [Array [Int ,0x995_6_A],81_4]){}Destructor (){}zF_(){} }'''
        expect = '''Program([ClassDecl(Id(I),[]),ClassDecl(Id(G),[MethodDecl(Id(Constructor),Instance,[param(Id(U),ArrayType(814,ArrayType(628074,IntType)))],Block([],[])),MethodDecl(Id(Destructor),Instance,[],Block([],[])),MethodDecl(Id(zF_),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 1))

    def test_2(self):
        line = '''Class f2:_7_{Var $8_:Boolean ;Var $Jg6:Boolean ;}Class _{Var $_:d;}'''
        expect = '''Program([ClassDecl(Id(f2),Id(_7_),[AttributeDecl(Static,VarDecl(Id($8_),BoolType)),AttributeDecl(Static,VarDecl(Id($Jg6),BoolType))]),ClassDecl(Id(_),[AttributeDecl(Static,VarDecl(Id($_),ClassType(Id(d))))])])'''
        self.assertTrue(TestAST.test(line, expect, 2))

    def test_3(self):
        line = '''Class _:m{}Class u{Constructor (Jc:Array [Array [Array [String ,1],0b1],0B1011000]){} }Class _g1{}Class _:_{}'''
        expect = '''Program([ClassDecl(Id(_),Id(m),[]),ClassDecl(Id(u),[MethodDecl(Id(Constructor),Instance,[param(Id(Jc),ArrayType(88,ArrayType(1,ArrayType(1,StringType))))],Block([],[]))]),ClassDecl(Id(_g1),[]),ClassDecl(Id(_),Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 3))

    def test_4(self):
        line = '''Class ___6:MDO{}Class _:_4{Constructor (__:Array [Boolean ,0B111111]){Continue ;}Destructor (){Break ;{}{} }}Class t{}'''
        expect = '''Program([ClassDecl(Id(___6),Id(MDO),[]),ClassDecl(Id(_),Id(_4),[MethodDecl(Id(Constructor),Instance,[param(Id(__),ArrayType(63,BoolType))],Block([],[Continue])),MethodDecl(Id(Destructor),Instance,[],Block([],[Break,Block([],[]),Block([],[])]))]),ClassDecl(Id(t),[])])'''
        self.assertTrue(TestAST.test(line, expect, 4))

    def test_5(self):
        line = '''Class _:O{}Class _{}Class p3b:__{}Class w09_JC_1{Constructor (_,____,s:Array [Boolean ,0b1010001];Mk,_8,__:_){} }'''
        expect = '''Program([ClassDecl(Id(_),Id(O),[]),ClassDecl(Id(_),[]),ClassDecl(Id(p3b),Id(__),[]),ClassDecl(Id(w09_JC_1),[MethodDecl(Id(Constructor),Instance,[param(Id(_),ArrayType(81,BoolType)),param(Id(____),ArrayType(81,BoolType)),param(Id(s),ArrayType(81,BoolType)),param(Id(Mk),ClassType(Id(_))),param(Id(_8),ClassType(Id(_))),param(Id(__),ClassType(Id(_)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 5))

    def test_6(self):
        line = '''Class _{}Class _{}Class v8:_1{}Class l_:_{}Class u__3:Q__{}'''
        expect = '''Program([ClassDecl(Id(_),[]),ClassDecl(Id(_),[]),ClassDecl(Id(v8),Id(_1),[]),ClassDecl(Id(l_),Id(_),[]),ClassDecl(Id(u__3),Id(Q__),[])])'''
        self.assertTrue(TestAST.test(line, expect, 6))

    def test_7(self):
        line = '''Class _s:__K{}Class _{}Class g0aS:_{}Class _4_{}Class _{}'''
        expect = '''Program([ClassDecl(Id(_s),Id(__K),[]),ClassDecl(Id(_),[]),ClassDecl(Id(g0aS),Id(_),[]),ClassDecl(Id(_4_),[]),ClassDecl(Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 7))

    def test_8(self):
        line = '''Class v:_{}Class gs{Constructor (){}Var _,$_a,$_:String ;}'''
        expect = '''Program([ClassDecl(Id(v),Id(_),[]),ClassDecl(Id(gs),[MethodDecl(Id(Constructor),Instance,[],Block([],[])),AttributeDecl(Instance,VarDecl(Id(_),StringType)),AttributeDecl(Static,VarDecl(Id($_a),StringType)),AttributeDecl(Static,VarDecl(Id($_),StringType))])])'''
        self.assertTrue(TestAST.test(line, expect, 8))

    def test_9(self):
        line = '''Class Z:U{Constructor (l:Array [Array [Float ,0X3],067]){} }'''
        expect = '''Program([ClassDecl(Id(Z),Id(U),[MethodDecl(Id(Constructor),Instance,[param(Id(l),ArrayType(55,ArrayType(3,FloatType)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 9))

    def test_10(self):
        line = '''Class _6_7:_d_3_{Var $g:__rh;Constructor (c6,B:Float ;Nbm,_zi_,_,___:Ffh_8){}Destructor (){} }'''
        expect = '''Program([ClassDecl(Id(_6_7),Id(_d_3_),[AttributeDecl(Static,VarDecl(Id($g),ClassType(Id(__rh)))),MethodDecl(Id(Constructor),Instance,[param(Id(c6),FloatType),param(Id(B),FloatType),param(Id(Nbm),ClassType(Id(Ffh_8))),param(Id(_zi_),ClassType(Id(Ffh_8))),param(Id(_),ClassType(Id(Ffh_8))),param(Id(___),ClassType(Id(Ffh_8)))],Block([],[])),MethodDecl(Id(Destructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 10))

    def test_11(self):
        line = '''Class _:_V{Var t,u:Boolean ;Constructor (){}Constructor (_,ir:Un){}Constructor (){Var _2,_x:Boolean ;}Constructor (__:Boolean ){} }Class _D_:_6_{}Class _:__7{Y(){Continue ;}Constructor (_,F:Array [Array [Array [Boolean ,0x64],48],064_6]){} }'''
        expect = '''Program([ClassDecl(Id(_),Id(_V),[AttributeDecl(Instance,VarDecl(Id(t),BoolType)),AttributeDecl(Instance,VarDecl(Id(u),BoolType)),MethodDecl(Id(Constructor),Instance,[],Block([],[])),MethodDecl(Id(Constructor),Instance,[param(Id(_),ClassType(Id(Un))),param(Id(ir),ClassType(Id(Un)))],Block([],[])),MethodDecl(Id(Constructor),Instance,[],Block([VarDecl(Id(_2),BoolType),VarDecl(Id(_x),BoolType)],[])),MethodDecl(Id(Constructor),Instance,[param(Id(__),BoolType)],Block([],[]))]),ClassDecl(Id(_D_),Id(_6_),[]),ClassDecl(Id(_),Id(__7),[MethodDecl(Id(Y),Instance,[],Block([],[Continue])),MethodDecl(Id(Constructor),Instance,[param(Id(_),ArrayType(422,ArrayType(48,ArrayType(100,BoolType)))),param(Id(F),ArrayType(422,ArrayType(48,ArrayType(100,BoolType))))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 11))

    def test_12(self):
        line = '''Class jk{}Class f4{}Class B:k{Var _,$J565,_,B,$__9:Array [Int ,02];}'''
        expect = '''Program([ClassDecl(Id(jk),[]),ClassDecl(Id(f4),[]),ClassDecl(Id(B),Id(k),[AttributeDecl(Instance,VarDecl(Id(_),ArrayType(2,IntType))),AttributeDecl(Static,VarDecl(Id($J565),ArrayType(2,IntType))),AttributeDecl(Instance,VarDecl(Id(_),ArrayType(2,IntType))),AttributeDecl(Instance,VarDecl(Id(B),ArrayType(2,IntType))),AttributeDecl(Static,VarDecl(Id($__9),ArrayType(2,IntType)))])])'''
        self.assertTrue(TestAST.test(line, expect, 12))

    def test_13(self):
        line = '''Class A{Var $V__a:__;}Class __:j{Constructor (){} }Class _0_:x{}'''
        expect = '''Program([ClassDecl(Id(A),[AttributeDecl(Static,VarDecl(Id($V__a),ClassType(Id(__))))]),ClassDecl(Id(__),Id(j),[MethodDecl(Id(Constructor),Instance,[],Block([],[]))]),ClassDecl(Id(_0_),Id(x),[])])'''
        self.assertTrue(TestAST.test(line, expect, 13))

    def test_14(self):
        line = '''Class __I{}Class _{Var $Ct,_:Array [Boolean ,0x3B];Constructor (){}Var $79,__5_,$V:Boolean ;}Class W_{}Class __:N{}'''
        expect = '''Program([ClassDecl(Id(__I),[]),ClassDecl(Id(_),[AttributeDecl(Static,VarDecl(Id($Ct),ArrayType(59,BoolType))),AttributeDecl(Instance,VarDecl(Id(_),ArrayType(59,BoolType))),MethodDecl(Id(Constructor),Instance,[],Block([],[])),AttributeDecl(Static,VarDecl(Id($79),BoolType)),AttributeDecl(Instance,VarDecl(Id(__5_),BoolType)),AttributeDecl(Static,VarDecl(Id($V),BoolType))]),ClassDecl(Id(W_),[]),ClassDecl(Id(__),Id(N),[])])'''
        self.assertTrue(TestAST.test(line, expect, 14))

    def test_15(self):
        line = '''Class _{Var lR:Array [Array [Array [String ,0XC_1F],0b11_10_0_1],0XC];}'''
        expect = '''Program([ClassDecl(Id(_),[AttributeDecl(Instance,VarDecl(Id(lR),ArrayType(12,ArrayType(57,ArrayType(3103,StringType)))))])])'''
        self.assertTrue(TestAST.test(line, expect, 15))

    def test_16(self):
        line = '''Class TcV:___{}Class __{t6(_:Array [Int ,0x5F];g:_0){} }Class o6P:b_{}'''
        expect = '''Program([ClassDecl(Id(TcV),Id(___),[]),ClassDecl(Id(__),[MethodDecl(Id(t6),Instance,[param(Id(_),ArrayType(95,IntType)),param(Id(g),ClassType(Id(_0)))],Block([],[]))]),ClassDecl(Id(o6P),Id(b_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 16))

    def test_17(self):
        line = '''Class Y{Destructor (){}__(_,_5,_:Array [Boolean ,0X4F]){} }Class _f:_JE{}'''
        expect = '''Program([ClassDecl(Id(Y),[MethodDecl(Id(Destructor),Instance,[],Block([],[])),MethodDecl(Id(__),Instance,[param(Id(_),ArrayType(79,BoolType)),param(Id(_5),ArrayType(79,BoolType)),param(Id(_),ArrayType(79,BoolType))],Block([],[]))]),ClassDecl(Id(_f),Id(_JE),[])])'''
        self.assertTrue(TestAST.test(line, expect, 17))

    def test_18(self):
        line = '''Class A:d__9_A{}Class _4:f_3d{$_(_,_,_h:Array [Array [String ,033_1],0xA];_:_;_,_5:Int ){} }Class Ha{}'''
        expect = '''Program([ClassDecl(Id(A),Id(d__9_A),[]),ClassDecl(Id(_4),Id(f_3d),[MethodDecl(Id($_),Static,[param(Id(_),ArrayType(10,ArrayType(217,StringType))),param(Id(_),ArrayType(10,ArrayType(217,StringType))),param(Id(_h),ArrayType(10,ArrayType(217,StringType))),param(Id(_),ClassType(Id(_))),param(Id(_),IntType),param(Id(_5),IntType)],Block([],[]))]),ClassDecl(Id(Ha),[])])'''
        self.assertTrue(TestAST.test(line, expect, 18))

    def test_19(self):
        line = '''Class N:_N_5{}Class nx:y{Z(u,iDf:Array [String ,0b1]){Continue ;Continue ;}Destructor (){} }'''
        expect = '''Program([ClassDecl(Id(N),Id(_N_5),[]),ClassDecl(Id(nx),Id(y),[MethodDecl(Id(Z),Instance,[param(Id(u),ArrayType(1,StringType)),param(Id(iDf),ArrayType(1,StringType))],Block([],[Continue,Continue])),MethodDecl(Id(Destructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 19))

    def test_20(self):
        line = '''Class _{Constructor (T:r_2h){}$_5(X_g:Array [Array [Array [Float ,0x2D],51],0x2D]){_::$_();}Destructor (){}Destructor (){Return ;} }'''
        expect = '''Program([ClassDecl(Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(T),ClassType(Id(r_2h)))],Block([],[])),MethodDecl(Id($_5),Static,[param(Id(X_g),ArrayType(45,ArrayType(51,ArrayType(45,FloatType))))],Block([],[Call(Id(_),Id($_),[])])),MethodDecl(Id(Destructor),Instance,[],Block([],[])),MethodDecl(Id(Destructor),Instance,[],Block([],[Return(None)]))])])'''
        self.assertTrue(TestAST.test(line, expect, 20))

    def test_21(self):
        line = '''Class F__8{$_230(_1,W,j,_n:O__;D8r_,_,_5_,U,_,T:a__91p918){}Var $58:_;}Class _:_{}'''
        expect = '''Program([ClassDecl(Id(F__8),[MethodDecl(Id($_230),Static,[param(Id(_1),ClassType(Id(O__))),param(Id(W),ClassType(Id(O__))),param(Id(j),ClassType(Id(O__))),param(Id(_n),ClassType(Id(O__))),param(Id(D8r_),ClassType(Id(a__91p918))),param(Id(_),ClassType(Id(a__91p918))),param(Id(_5_),ClassType(Id(a__91p918))),param(Id(U),ClassType(Id(a__91p918))),param(Id(_),ClassType(Id(a__91p918))),param(Id(T),ClassType(Id(a__91p918)))],Block([],[])),AttributeDecl(Static,VarDecl(Id($58),ClassType(Id(_))))]),ClassDecl(Id(_),Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 21))

    def test_22(self):
        line = '''Class T6:_{}Class _:z3_3{Var $4__,_8_m95:c;}Class t:v{}Class _:_9Z{}'''
        expect = '''Program([ClassDecl(Id(T6),Id(_),[]),ClassDecl(Id(_),Id(z3_3),[AttributeDecl(Static,VarDecl(Id($4__),ClassType(Id(c)))),AttributeDecl(Instance,VarDecl(Id(_8_m95),ClassType(Id(c))))]),ClassDecl(Id(t),Id(v),[]),ClassDecl(Id(_),Id(_9Z),[])])'''
        self.assertTrue(TestAST.test(line, expect, 22))

    def test_23(self):
        line = '''Class D:x5Y{$8(m:Boolean ;NT:Int ){Return ;Var ___55o,zi:g;} }'''
        expect = '''Program([ClassDecl(Id(D),Id(x5Y),[MethodDecl(Id($8),Static,[param(Id(m),BoolType),param(Id(NT),IntType)],Block([VarDecl(Id(___55o),ClassType(Id(g))),VarDecl(Id(zi),ClassType(Id(g)))],[Return(None)]))])])'''
        self.assertTrue(TestAST.test(line, expect, 23))

    def test_24(self):
        line = '''Class __{}Class _7H{}Class U:_{Constructor (____v,_,o:Array [Array [String ,0x63],0B1011000]){} }'''
        expect = '''Program([ClassDecl(Id(__),[]),ClassDecl(Id(_7H),[]),ClassDecl(Id(U),Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(____v),ArrayType(88,ArrayType(99,StringType))),param(Id(_),ArrayType(88,ArrayType(99,StringType))),param(Id(o),ArrayType(88,ArrayType(99,StringType)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 24))

    def test_25(self):
        line = '''Class r{Destructor (){} }Class r:_{Destructor (){}$_6(b:Array [Int ,0X3C]){} }'''
        expect = '''Program([ClassDecl(Id(r),[MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(r),Id(_),[MethodDecl(Id(Destructor),Instance,[],Block([],[])),MethodDecl(Id($_6),Static,[param(Id(b),ArrayType(60,IntType))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 25))

    def test_26(self):
        line = '''Class __m9_7rYf:_{Var W:Boolean ;}Class P{Constructor (_,X_L6,_px,R:Array [Array [Array [Array [Boolean ,58],06_0],78],0121]){} }'''
        expect = '''Program([ClassDecl(Id(__m9_7rYf),Id(_),[AttributeDecl(Instance,VarDecl(Id(W),BoolType))]),ClassDecl(Id(P),[MethodDecl(Id(Constructor),Instance,[param(Id(_),ArrayType(81,ArrayType(78,ArrayType(48,ArrayType(58,BoolType))))),param(Id(X_L6),ArrayType(81,ArrayType(78,ArrayType(48,ArrayType(58,BoolType))))),param(Id(_px),ArrayType(81,ArrayType(78,ArrayType(48,ArrayType(58,BoolType))))),param(Id(R),ArrayType(81,ArrayType(78,ArrayType(48,ArrayType(58,BoolType)))))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 26))

    def test_27(self):
        line = '''Class u2___5iv_{Var $D30:Array [Array [Boolean ,0x1_EA],0B1100100];}Class E:_{}'''
        expect = '''Program([ClassDecl(Id(u2___5iv_),[AttributeDecl(Static,VarDecl(Id($D30),ArrayType(100,ArrayType(490,BoolType))))]),ClassDecl(Id(E),Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 27))

    def test_28(self):
        line = '''Class w7:_32{Var _04:Array [Float ,0112];}Class _{Var _86:U;_(Q,WsN_r,_,_:_;ER48_0:Array [String ,0X22];t,E877:String ;_:Boolean ;d,t_,Jjt:p;P:Array [Array [Int ,0X3],0b10_01_10_0111];BY,k:Array [Float ,0x4A]){} }Class T0{}'''
        expect = '''Program([ClassDecl(Id(w7),Id(_32),[AttributeDecl(Instance,VarDecl(Id(_04),ArrayType(74,FloatType)))]),ClassDecl(Id(_),[AttributeDecl(Instance,VarDecl(Id(_86),ClassType(Id(U)))),MethodDecl(Id(_),Instance,[param(Id(Q),ClassType(Id(_))),param(Id(WsN_r),ClassType(Id(_))),param(Id(_),ClassType(Id(_))),param(Id(_),ClassType(Id(_))),param(Id(ER48_0),ArrayType(34,StringType)),param(Id(t),StringType),param(Id(E877),StringType),param(Id(_),BoolType),param(Id(d),ClassType(Id(p))),param(Id(t_),ClassType(Id(p))),param(Id(Jjt),ClassType(Id(p))),param(Id(P),ArrayType(615,ArrayType(3,IntType))),param(Id(BY),ArrayType(74,FloatType)),param(Id(k),ArrayType(74,FloatType))],Block([],[]))]),ClassDecl(Id(T0),[])])'''
        self.assertTrue(TestAST.test(line, expect, 28))

    def test_29(self):
        line = '''Class y__8:__{Var _w:Array [Float ,0107];Var _a,j_8_82:Np_;Var $5_:Array [Array [Boolean ,0107],54];Destructor (){} }'''
        expect = '''Program([ClassDecl(Id(y__8),Id(__),[AttributeDecl(Instance,VarDecl(Id(_w),ArrayType(71,FloatType))),AttributeDecl(Instance,VarDecl(Id(_a),ClassType(Id(Np_)))),AttributeDecl(Instance,VarDecl(Id(j_8_82),ClassType(Id(Np_)))),AttributeDecl(Static,VarDecl(Id($5_),ArrayType(54,ArrayType(71,BoolType)))),MethodDecl(Id(Destructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 29))

    def test_30(self):
        line = '''Class k_9:_kk{}Class _:t9{Var $9Q8_EF1_:Int ;Var $9_:h_2;Var $_:_;}'''
        expect = '''Program([ClassDecl(Id(k_9),Id(_kk),[]),ClassDecl(Id(_),Id(t9),[AttributeDecl(Static,VarDecl(Id($9Q8_EF1_),IntType)),AttributeDecl(Static,VarDecl(Id($9_),ClassType(Id(h_2)))),AttributeDecl(Static,VarDecl(Id($_),ClassType(Id(_))))])])'''
        self.assertTrue(TestAST.test(line, expect, 30))

    def test_31(self):
        line = '''Class _:z{}Class ___B9N_2{Var $w,$__:Array [Array [String ,0x21],11];$2(e3:Boolean ){} }'''
        expect = '''Program([ClassDecl(Id(_),Id(z),[]),ClassDecl(Id(___B9N_2),[AttributeDecl(Static,VarDecl(Id($w),ArrayType(11,ArrayType(33,StringType)))),AttributeDecl(Static,VarDecl(Id($__),ArrayType(11,ArrayType(33,StringType)))),MethodDecl(Id($2),Static,[param(Id(e3),BoolType)],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 31))

    def test_32(self):
        line = '''Class _{Constructor (){}Var $z,$_23,Y5:_;Var _V3,A__2yt__3,_:q_L;Var $3,w6,E,C:Array [Array [String ,0XB33],6_7];Constructor (e:Array [Float ,7];F,_:M4){}Destructor (){} }'''
        expect = '''Program([ClassDecl(Id(_),[MethodDecl(Id(Constructor),Instance,[],Block([],[])),AttributeDecl(Static,VarDecl(Id($z),ClassType(Id(_)))),AttributeDecl(Static,VarDecl(Id($_23),ClassType(Id(_)))),AttributeDecl(Instance,VarDecl(Id(Y5),ClassType(Id(_)))),AttributeDecl(Instance,VarDecl(Id(_V3),ClassType(Id(q_L)))),AttributeDecl(Instance,VarDecl(Id(A__2yt__3),ClassType(Id(q_L)))),AttributeDecl(Instance,VarDecl(Id(_),ClassType(Id(q_L)))),AttributeDecl(Static,VarDecl(Id($3),ArrayType(67,ArrayType(2867,StringType)))),AttributeDecl(Instance,VarDecl(Id(w6),ArrayType(67,ArrayType(2867,StringType)))),AttributeDecl(Instance,VarDecl(Id(E),ArrayType(67,ArrayType(2867,StringType)))),AttributeDecl(Instance,VarDecl(Id(C),ArrayType(67,ArrayType(2867,StringType)))),MethodDecl(Id(Constructor),Instance,[param(Id(e),ArrayType(7,FloatType)),param(Id(F),ClassType(Id(M4))),param(Id(_),ClassType(Id(M4)))],Block([],[])),MethodDecl(Id(Destructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 32))

    def test_33(self):
        line = '''Class Z__{}Class z124:m{Var __:Array [Int ,014_6];}Class K37S2{}'''
        expect = '''Program([ClassDecl(Id(Z__),[]),ClassDecl(Id(z124),Id(m),[AttributeDecl(Instance,VarDecl(Id(__),ArrayType(102,IntType)))]),ClassDecl(Id(K37S2),[])])'''
        self.assertTrue(TestAST.test(line, expect, 33))

    def test_34(self):
        line = '''Class l_4:H{Destructor (){}Destructor (){}z(__,f:Boolean ;n_:j){}___9A(){}Constructor (_,AC,A,_,_,_:Int ;A4X_,B_,a:_;__:String ;_,Ui,m:Array [Array [Int ,95],95]){} }'''
        expect = '''Program([ClassDecl(Id(l_4),Id(H),[MethodDecl(Id(Destructor),Instance,[],Block([],[])),MethodDecl(Id(Destructor),Instance,[],Block([],[])),MethodDecl(Id(z),Instance,[param(Id(__),BoolType),param(Id(f),BoolType),param(Id(n_),ClassType(Id(j)))],Block([],[])),MethodDecl(Id(___9A),Instance,[],Block([],[])),MethodDecl(Id(Constructor),Instance,[param(Id(_),IntType),param(Id(AC),IntType),param(Id(A),IntType),param(Id(_),IntType),param(Id(_),IntType),param(Id(_),IntType),param(Id(A4X_),ClassType(Id(_))),param(Id(B_),ClassType(Id(_))),param(Id(a),ClassType(Id(_))),param(Id(__),StringType),param(Id(_),ArrayType(95,ArrayType(95,IntType))),param(Id(Ui),ArrayType(95,ArrayType(95,IntType))),param(Id(m),ArrayType(95,ArrayType(95,IntType)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 34))

    def test_35(self):
        line = '''Class eD{V(){Continue ;} }Class i{Destructor (){x::$6_();}Var $Q__:String ;}'''
        expect = '''Program([ClassDecl(Id(eD),[MethodDecl(Id(V),Instance,[],Block([],[Continue]))]),ClassDecl(Id(i),[MethodDecl(Id(Destructor),Instance,[],Block([],[Call(Id(x),Id($6_),[])])),AttributeDecl(Static,VarDecl(Id($Q__),StringType))])])'''
        self.assertTrue(TestAST.test(line, expect, 35))

    def test_36(self):
        line = '''Class P__{}Class _{_(_0_9__7,_:Array [Int ,27]){_::$8.i_8o8R();} }'''
        expect = '''Program([ClassDecl(Id(P__),[]),ClassDecl(Id(_),[MethodDecl(Id(_),Instance,[param(Id(_0_9__7),ArrayType(27,IntType)),param(Id(_),ArrayType(27,IntType))],Block([],[Call(FieldAccess(Id(_),Id($8)),Id(i_8o8R),[])]))])])'''
        self.assertTrue(TestAST.test(line, expect, 36))

    def test_37(self):
        line = '''Class H:_{$y4(H_,__,___,_K_,_9,_,__4,s_,q:Float ){Break ;} }'''
        expect = '''Program([ClassDecl(Id(H),Id(_),[MethodDecl(Id($y4),Static,[param(Id(H_),FloatType),param(Id(__),FloatType),param(Id(___),FloatType),param(Id(_K_),FloatType),param(Id(_9),FloatType),param(Id(_),FloatType),param(Id(__4),FloatType),param(Id(s_),FloatType),param(Id(q),FloatType)],Block([],[Break]))])])'''
        self.assertTrue(TestAST.test(line, expect, 37))

    def test_38(self):
        line = '''Class _{}Class g:_{Constructor (x:_;__:Array [Array [Array [Array [Array [Array [Array [Float ,067],067],7],0x39],0x9_14_C_D],182],0xF5_066_9_A_0_E]){}Destructor (){} }Class _:__{}'''
        expect = '''Program([ClassDecl(Id(_),[]),ClassDecl(Id(g),Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(x),ClassType(Id(_))),param(Id(__),ArrayType(65773410830,ArrayType(182,ArrayType(595149,ArrayType(57,ArrayType(7,ArrayType(55,ArrayType(55,FloatType))))))))],Block([],[])),MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(_),Id(__),[])])'''
        self.assertTrue(TestAST.test(line, expect, 38))

    def test_39(self):
        line = '''Class _{Constructor (_:Array [Array [String ,0x3],0x33];yK:__){Var F4,_,_k,_b:_SML;} }'''
        expect = '''Program([ClassDecl(Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(_),ArrayType(51,ArrayType(3,StringType))),param(Id(yK),ClassType(Id(__)))],Block([VarDecl(Id(F4),ClassType(Id(_SML))),VarDecl(Id(_),ClassType(Id(_SML))),VarDecl(Id(_k),ClassType(Id(_SML))),VarDecl(Id(_b),ClassType(Id(_SML)))],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 39))

    def test_40(self):
        line = '''Class R{}Class _{$1(__x:_w;Ml,x,xJ:Boolean ;_1,Z9:_m){} }Class Q{}'''
        expect = '''Program([ClassDecl(Id(R),[]),ClassDecl(Id(_),[MethodDecl(Id($1),Static,[param(Id(__x),ClassType(Id(_w))),param(Id(Ml),BoolType),param(Id(x),BoolType),param(Id(xJ),BoolType),param(Id(_1),ClassType(Id(_m))),param(Id(Z9),ClassType(Id(_m)))],Block([],[]))]),ClassDecl(Id(Q),[])])'''
        self.assertTrue(TestAST.test(line, expect, 40))

    def test_41(self):
        line = '''Class Y:ay{Constructor (g,_G:Array [Array [Array [String ,80],0b1],78]){}b(m,_:e0){Return ;} }'''
        expect = '''Program([ClassDecl(Id(Y),Id(ay),[MethodDecl(Id(Constructor),Instance,[param(Id(g),ArrayType(78,ArrayType(1,ArrayType(80,StringType)))),param(Id(_G),ArrayType(78,ArrayType(1,ArrayType(80,StringType))))],Block([],[])),MethodDecl(Id(b),Instance,[param(Id(m),ClassType(Id(e0))),param(Id(_),ClassType(Id(e0)))],Block([],[Return(None)]))])])'''
        self.assertTrue(TestAST.test(line, expect, 41))

    def test_42(self):
        line = '''Class U{}Class _F_H{Constructor (_,_,U,_:Array [Array [Array [Int ,0b111011],24],064];z:Array [Float ,0x61];n4:Array [Array [String ,0b111011],064];M:q9_){} }Class C{}Class n{}'''
        expect = '''Program([ClassDecl(Id(U),[]),ClassDecl(Id(_F_H),[MethodDecl(Id(Constructor),Instance,[param(Id(_),ArrayType(52,ArrayType(24,ArrayType(59,IntType)))),param(Id(_),ArrayType(52,ArrayType(24,ArrayType(59,IntType)))),param(Id(U),ArrayType(52,ArrayType(24,ArrayType(59,IntType)))),param(Id(_),ArrayType(52,ArrayType(24,ArrayType(59,IntType)))),param(Id(z),ArrayType(97,FloatType)),param(Id(n4),ArrayType(52,ArrayType(59,StringType))),param(Id(M),ClassType(Id(q9_)))],Block([],[]))]),ClassDecl(Id(C),[]),ClassDecl(Id(n),[])])'''
        self.assertTrue(TestAST.test(line, expect, 42))

    def test_43(self):
        line = '''Class f19{_(_:Int ;i:_){}Var $5:_;Var $cQaA_,$o_31:Array [Boolean ,0X8_F];}'''
        expect = '''Program([ClassDecl(Id(f19),[MethodDecl(Id(_),Instance,[param(Id(_),IntType),param(Id(i),ClassType(Id(_)))],Block([],[])),AttributeDecl(Static,VarDecl(Id($5),ClassType(Id(_)))),AttributeDecl(Static,VarDecl(Id($cQaA_),ArrayType(143,BoolType))),AttributeDecl(Static,VarDecl(Id($o_31),ArrayType(143,BoolType)))])])'''
        self.assertTrue(TestAST.test(line, expect, 43))

    def test_44(self):
        line = '''Class s{}Class A4p{Destructor (){} }Class _:_5{Destructor (){}Var $02:_98;}'''
        expect = '''Program([ClassDecl(Id(s),[]),ClassDecl(Id(A4p),[MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(_),Id(_5),[MethodDecl(Id(Destructor),Instance,[],Block([],[])),AttributeDecl(Static,VarDecl(Id($02),ClassType(Id(_98))))])])'''
        self.assertTrue(TestAST.test(line, expect, 44))

    def test_45(self):
        line = '''Class _8:D_{}Class v{}Class _4_n_G_:_{Var $_:Boolean ;Destructor (){} }Class _:_{}'''
        expect = '''Program([ClassDecl(Id(_8),Id(D_),[]),ClassDecl(Id(v),[]),ClassDecl(Id(_4_n_G_),Id(_),[AttributeDecl(Static,VarDecl(Id($_),BoolType)),MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(_),Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 45))

    def test_46(self):
        line = '''Class vsP{Destructor (){ {}Continue ;{ {Break ;} }} }Class ___{Var GZ,$0:Int ;}'''
        expect = '''Program([ClassDecl(Id(vsP),[MethodDecl(Id(Destructor),Instance,[],Block([],[Block([],[]),Continue,Block([],[Block([],[Break])])]))]),ClassDecl(Id(___),[AttributeDecl(Instance,VarDecl(Id(GZ),IntType)),AttributeDecl(Static,VarDecl(Id($0),IntType))])])'''
        self.assertTrue(TestAST.test(line, expect, 46))

    def test_47(self):
        line = '''Class _H:r{}Class _:U{}Class p{}Class u2:_{Constructor (){}e_(){}Destructor (){} }Class u{}'''
        expect = '''Program([ClassDecl(Id(_H),Id(r),[]),ClassDecl(Id(_),Id(U),[]),ClassDecl(Id(p),[]),ClassDecl(Id(u2),Id(_),[MethodDecl(Id(Constructor),Instance,[],Block([],[])),MethodDecl(Id(e_),Instance,[],Block([],[])),MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(u),[])])'''
        self.assertTrue(TestAST.test(line, expect, 47))

    def test_48(self):
        line = '''Class i{Destructor (){Return ;}Constructor (_v:Array [Boolean ,044];_:Boolean ;_U7:Array [Array [Boolean ,0b1],0B1001];_k_,_:_){Break ;Return ;} }Class _q:_l{}'''
        expect = '''Program([ClassDecl(Id(i),[MethodDecl(Id(Destructor),Instance,[],Block([],[Return(None)])),MethodDecl(Id(Constructor),Instance,[param(Id(_v),ArrayType(36,BoolType)),param(Id(_),BoolType),param(Id(_U7),ArrayType(9,ArrayType(1,BoolType))),param(Id(_k_),ClassType(Id(_))),param(Id(_),ClassType(Id(_)))],Block([],[Break,Return(None)]))]),ClassDecl(Id(_q),Id(_l),[])])'''
        self.assertTrue(TestAST.test(line, expect, 48))

    def test_49(self):
        line = '''Class _:i{$4_2(_,D:Array [String ,8]){ {{}Return ;} }}Class a{}Class e{}'''
        expect = '''Program([ClassDecl(Id(_),Id(i),[MethodDecl(Id($4_2),Static,[param(Id(_),ArrayType(8,StringType)),param(Id(D),ArrayType(8,StringType))],Block([],[Block([],[Block([],[]),Return(None)])]))]),ClassDecl(Id(a),[]),ClassDecl(Id(e),[])])'''
        self.assertTrue(TestAST.test(line, expect, 49))

    def test_50(self):
        line = '''Class C{Var I,u,$i3:Array [Array [Array [Boolean ,0x4],0B1010001],0X5F];}'''
        expect = '''Program([ClassDecl(Id(C),[AttributeDecl(Instance,VarDecl(Id(I),ArrayType(95,ArrayType(81,ArrayType(4,BoolType))))),AttributeDecl(Instance,VarDecl(Id(u),ArrayType(95,ArrayType(81,ArrayType(4,BoolType))))),AttributeDecl(Static,VarDecl(Id($i3),ArrayType(95,ArrayType(81,ArrayType(4,BoolType)))))])])'''
        self.assertTrue(TestAST.test(line, expect, 50))

    def test_51(self):
        line = '''Class l{Constructor (_6,_,Q,M,l:Int ;_:String ){} }Class _:z{}'''
        expect = '''Program([ClassDecl(Id(l),[MethodDecl(Id(Constructor),Instance,[param(Id(_6),IntType),param(Id(_),IntType),param(Id(Q),IntType),param(Id(M),IntType),param(Id(l),IntType),param(Id(_),StringType)],Block([],[]))]),ClassDecl(Id(_),Id(z),[])])'''
        self.assertTrue(TestAST.test(line, expect, 51))

    def test_52(self):
        line = '''Class _W{}Class e72:_878{$n(pth,__:Boolean ;_P_f8_,r,G_:_;l_:Array [String ,0113]){} }Class __d:c_n_{Var $__7s,_,__6,___,_:_2Q2;}'''
        expect = '''Program([ClassDecl(Id(_W),[]),ClassDecl(Id(e72),Id(_878),[MethodDecl(Id($n),Static,[param(Id(pth),BoolType),param(Id(__),BoolType),param(Id(_P_f8_),ClassType(Id(_))),param(Id(r),ClassType(Id(_))),param(Id(G_),ClassType(Id(_))),param(Id(l_),ArrayType(75,StringType))],Block([],[]))]),ClassDecl(Id(__d),Id(c_n_),[AttributeDecl(Static,VarDecl(Id($__7s),ClassType(Id(_2Q2)))),AttributeDecl(Instance,VarDecl(Id(_),ClassType(Id(_2Q2)))),AttributeDecl(Instance,VarDecl(Id(__6),ClassType(Id(_2Q2)))),AttributeDecl(Instance,VarDecl(Id(___),ClassType(Id(_2Q2)))),AttributeDecl(Instance,VarDecl(Id(_),ClassType(Id(_2Q2))))])])'''
        self.assertTrue(TestAST.test(line, expect, 52))

    def test_53(self):
        line = '''Class _G:C_{Constructor (k,Lo:String ){Break ;}Constructor (U:String ){} }'''
        expect = '''Program([ClassDecl(Id(_G),Id(C_),[MethodDecl(Id(Constructor),Instance,[param(Id(k),StringType),param(Id(Lo),StringType)],Block([],[Break])),MethodDecl(Id(Constructor),Instance,[param(Id(U),StringType)],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 53))

    def test_54(self):
        line = '''Class _{Constructor (CK,uD:Array [Boolean ,0b1_1_1]){Continue ;} }Class _{}'''
        expect = '''Program([ClassDecl(Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(CK),ArrayType(7,BoolType)),param(Id(uD),ArrayType(7,BoolType))],Block([],[Continue]))]),ClassDecl(Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 54))

    def test_55(self):
        line = '''Class M:I{Constructor (){}Constructor (Q,sV:e8_;_9:Boolean ;_40:Array [Int ,050];R,o,Sb:Int ){} }Class _{Constructor (U:Float ;_:Float ){}Constructor (e,_:Array [Boolean ,0X8_7_9]){} }Class _1L:_{}'''
        expect = '''Program([ClassDecl(Id(M),Id(I),[MethodDecl(Id(Constructor),Instance,[],Block([],[])),MethodDecl(Id(Constructor),Instance,[param(Id(Q),ClassType(Id(e8_))),param(Id(sV),ClassType(Id(e8_))),param(Id(_9),BoolType),param(Id(_40),ArrayType(40,IntType)),param(Id(R),IntType),param(Id(o),IntType),param(Id(Sb),IntType)],Block([],[]))]),ClassDecl(Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(U),FloatType),param(Id(_),FloatType)],Block([],[])),MethodDecl(Id(Constructor),Instance,[param(Id(e),ArrayType(2169,BoolType)),param(Id(_),ArrayType(2169,BoolType))],Block([],[]))]),ClassDecl(Id(_1L),Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 55))

    def test_56(self):
        line = '''Class Zv5y4{}Class _g:l__3{Var $9,B,$Tk:_;Constructor (c_,Ml7:Boolean ;dN:Float ;_,t:Array [Array [Float ,0b1101],0X56]){} }'''
        expect = '''Program([ClassDecl(Id(Zv5y4),[]),ClassDecl(Id(_g),Id(l__3),[AttributeDecl(Static,VarDecl(Id($9),ClassType(Id(_)))),AttributeDecl(Instance,VarDecl(Id(B),ClassType(Id(_)))),AttributeDecl(Static,VarDecl(Id($Tk),ClassType(Id(_)))),MethodDecl(Id(Constructor),Instance,[param(Id(c_),BoolType),param(Id(Ml7),BoolType),param(Id(dN),FloatType),param(Id(_),ArrayType(86,ArrayType(13,FloatType))),param(Id(t),ArrayType(86,ArrayType(13,FloatType)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 56))

    def test_57(self):
        line = '''Class _:s{}Class _{Constructor (_:_;CW,__5:String ;___:_){} }Class ___e:Px{}'''
        expect = '''Program([ClassDecl(Id(_),Id(s),[]),ClassDecl(Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(_),ClassType(Id(_))),param(Id(CW),StringType),param(Id(__5),StringType),param(Id(___),ClassType(Id(_)))],Block([],[]))]),ClassDecl(Id(___e),Id(Px),[])])'''
        self.assertTrue(TestAST.test(line, expect, 57))

    def test_58(self):
        line = '''Class _:G{_(Pu:_;T_:Array [Float ,0b1];f9___,___:Boolean ;h:Boolean ){Continue ;} }Class Q_M:B{Constructor (_x0,o:Boolean ;X6_:Boolean ){} }Class _5_8:o0tL{}'''
        expect = '''Program([ClassDecl(Id(_),Id(G),[MethodDecl(Id(_),Instance,[param(Id(Pu),ClassType(Id(_))),param(Id(T_),ArrayType(1,FloatType)),param(Id(f9___),BoolType),param(Id(___),BoolType),param(Id(h),BoolType)],Block([],[Continue]))]),ClassDecl(Id(Q_M),Id(B),[MethodDecl(Id(Constructor),Instance,[param(Id(_x0),BoolType),param(Id(o),BoolType),param(Id(X6_),BoolType)],Block([],[]))]),ClassDecl(Id(_5_8),Id(o0tL),[])])'''
        self.assertTrue(TestAST.test(line, expect, 58))

    def test_59(self):
        line = '''Class g_2:T{Constructor (u:Array [String ,2];Z,_:String ;G,z:Array [String ,2_2]){} }'''
        expect = '''Program([ClassDecl(Id(g_2),Id(T),[MethodDecl(Id(Constructor),Instance,[param(Id(u),ArrayType(2,StringType)),param(Id(Z),StringType),param(Id(_),StringType),param(Id(G),ArrayType(22,StringType)),param(Id(z),ArrayType(22,StringType))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 59))

    def test_60(self):
        line = '''Class W0{Constructor (__,_,_:Float ){Break ;}Constructor (){}Var $F5,_,_:Array [Float ,0X2A];Var _,l5b:_;Var $_,y8y:String ;}'''
        expect = '''Program([ClassDecl(Id(W0),[MethodDecl(Id(Constructor),Instance,[param(Id(__),FloatType),param(Id(_),FloatType),param(Id(_),FloatType)],Block([],[Break])),MethodDecl(Id(Constructor),Instance,[],Block([],[])),AttributeDecl(Static,VarDecl(Id($F5),ArrayType(42,FloatType))),AttributeDecl(Instance,VarDecl(Id(_),ArrayType(42,FloatType))),AttributeDecl(Instance,VarDecl(Id(_),ArrayType(42,FloatType))),AttributeDecl(Instance,VarDecl(Id(_),ClassType(Id(_)))),AttributeDecl(Instance,VarDecl(Id(l5b),ClassType(Id(_)))),AttributeDecl(Static,VarDecl(Id($_),StringType)),AttributeDecl(Instance,VarDecl(Id(y8y),StringType))])])'''
        self.assertTrue(TestAST.test(line, expect, 60))

    def test_61(self):
        line = '''Class _{Destructor (){New C5_().V_();Break ;} }Class l{}Class z_:X__{Var P,_,_,$_i:Array [Int ,03];}'''
        expect = '''Program([ClassDecl(Id(_),[MethodDecl(Id(Destructor),Instance,[],Block([],[Call(NewExpr(Id(C5_),[]),Id(V_),[]),Break]))]),ClassDecl(Id(l),[]),ClassDecl(Id(z_),Id(X__),[AttributeDecl(Instance,VarDecl(Id(P),ArrayType(3,IntType))),AttributeDecl(Instance,VarDecl(Id(_),ArrayType(3,IntType))),AttributeDecl(Instance,VarDecl(Id(_),ArrayType(3,IntType))),AttributeDecl(Static,VarDecl(Id($_i),ArrayType(3,IntType)))])])'''
        self.assertTrue(TestAST.test(line, expect, 61))

    def test_62(self):
        line = '''Class t7{Destructor (){} }Class _{Destructor (){} }Class F:_{}'''
        expect = '''Program([ClassDecl(Id(t7),[MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(_),[MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(F),Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 62))

    def test_63(self):
        line = '''Class _{Constructor (N,E4:Array [Boolean ,01_7_600_4_4_6]){} }'''
        expect = '''Program([ClassDecl(Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(N),ArrayType(4129062,BoolType)),param(Id(E4),ArrayType(4129062,BoolType))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 63))

    def test_64(self):
        line = '''Class w_84____cv{}Class _{Constructor (){}Constructor (){}$_47(){Continue ;} }'''
        expect = '''Program([ClassDecl(Id(w_84____cv),[]),ClassDecl(Id(_),[MethodDecl(Id(Constructor),Instance,[],Block([],[])),MethodDecl(Id(Constructor),Instance,[],Block([],[])),MethodDecl(Id($_47),Static,[],Block([],[Continue]))])])'''
        self.assertTrue(TestAST.test(line, expect, 64))

    def test_65(self):
        line = '''Class p{Var $_,$_,D3:Array [Float ,34];v_(_,T:N){} }Class dnww:_{}Class V:ZM{}'''
        expect = '''Program([ClassDecl(Id(p),[AttributeDecl(Static,VarDecl(Id($_),ArrayType(34,FloatType))),AttributeDecl(Static,VarDecl(Id($_),ArrayType(34,FloatType))),AttributeDecl(Instance,VarDecl(Id(D3),ArrayType(34,FloatType))),MethodDecl(Id(v_),Instance,[param(Id(_),ClassType(Id(N))),param(Id(T),ClassType(Id(N)))],Block([],[]))]),ClassDecl(Id(dnww),Id(_),[]),ClassDecl(Id(V),Id(ZM),[])])'''
        self.assertTrue(TestAST.test(line, expect, 65))

    def test_66(self):
        line = '''Class _{Var sU:Array [Array [Array [Float ,37],0x16],0B10101];}Class _94_y{Constructor (g,Y,_,_7__:Array [String ,01]){} }'''
        expect = '''Program([ClassDecl(Id(_),[AttributeDecl(Instance,VarDecl(Id(sU),ArrayType(21,ArrayType(22,ArrayType(37,FloatType)))))]),ClassDecl(Id(_94_y),[MethodDecl(Id(Constructor),Instance,[param(Id(g),ArrayType(1,StringType)),param(Id(Y),ArrayType(1,StringType)),param(Id(_),ArrayType(1,StringType)),param(Id(_7__),ArrayType(1,StringType))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 66))

    def test_67(self):
        line = '''Class Qk:_F{L(e:String ;_,c:Array [Array [Array [Boolean ,0B1011101],04],0b110];_s,A:Boolean ){} }'''
        expect = '''Program([ClassDecl(Id(Qk),Id(_F),[MethodDecl(Id(L),Instance,[param(Id(e),StringType),param(Id(_),ArrayType(6,ArrayType(4,ArrayType(93,BoolType)))),param(Id(c),ArrayType(6,ArrayType(4,ArrayType(93,BoolType)))),param(Id(_s),BoolType),param(Id(A),BoolType)],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 67))

    def test_68(self):
        line = '''Class L:U{u(_6:Boolean ;_,O,e7,_:Int ;_,jo65s,_x2,S,O:zw4;_u_,_8,Sf,_s:_x){}B0_Zq7(_Q:j;_8:Array [Array [Float ,0b10110],0B10];V:Boolean ){} }Class _:___8{_(){}Destructor (){Var __e_l,_g____,_:rW;} }'''
        expect = '''Program([ClassDecl(Id(L),Id(U),[MethodDecl(Id(u),Instance,[param(Id(_6),BoolType),param(Id(_),IntType),param(Id(O),IntType),param(Id(e7),IntType),param(Id(_),IntType),param(Id(_),ClassType(Id(zw4))),param(Id(jo65s),ClassType(Id(zw4))),param(Id(_x2),ClassType(Id(zw4))),param(Id(S),ClassType(Id(zw4))),param(Id(O),ClassType(Id(zw4))),param(Id(_u_),ClassType(Id(_x))),param(Id(_8),ClassType(Id(_x))),param(Id(Sf),ClassType(Id(_x))),param(Id(_s),ClassType(Id(_x)))],Block([],[])),MethodDecl(Id(B0_Zq7),Instance,[param(Id(_Q),ClassType(Id(j))),param(Id(_8),ArrayType(2,ArrayType(22,FloatType))),param(Id(V),BoolType)],Block([],[]))]),ClassDecl(Id(_),Id(___8),[MethodDecl(Id(_),Instance,[],Block([],[])),MethodDecl(Id(Destructor),Instance,[],Block([VarDecl(Id(__e_l),ClassType(Id(rW))),VarDecl(Id(_g____),ClassType(Id(rW))),VarDecl(Id(_),ClassType(Id(rW)))],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 68))

    def test_69(self):
        line = '''Class _{Constructor (_,C,rb:Array [Int ,0643]){Break ;} }Class _:v{}'''
        expect = '''Program([ClassDecl(Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(_),ArrayType(419,IntType)),param(Id(C),ArrayType(419,IntType)),param(Id(rb),ArrayType(419,IntType))],Block([],[Break]))]),ClassDecl(Id(_),Id(v),[])])'''
        self.assertTrue(TestAST.test(line, expect, 69))

    def test_70(self):
        line = '''Class U:_{Var _,$_,$d:Array [Array [Float ,3],06];}Class __:_X_m{}'''
        expect = '''Program([ClassDecl(Id(U),Id(_),[AttributeDecl(Instance,VarDecl(Id(_),ArrayType(6,ArrayType(3,FloatType)))),AttributeDecl(Static,VarDecl(Id($_),ArrayType(6,ArrayType(3,FloatType)))),AttributeDecl(Static,VarDecl(Id($d),ArrayType(6,ArrayType(3,FloatType))))]),ClassDecl(Id(__),Id(_X_m),[])])'''
        self.assertTrue(TestAST.test(line, expect, 70))

    def test_71(self):
        line = '''Class r{}Class w:T{Constructor (){} }Class __k{Destructor (){} }'''
        expect = '''Program([ClassDecl(Id(r),[]),ClassDecl(Id(w),Id(T),[MethodDecl(Id(Constructor),Instance,[],Block([],[]))]),ClassDecl(Id(__k),[MethodDecl(Id(Destructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 71))

    def test_72(self):
        line = '''Class _{Var $_,$X_:Array [Float ,5];}Class __m{Constructor (){} }'''
        expect = '''Program([ClassDecl(Id(_),[AttributeDecl(Static,VarDecl(Id($_),ArrayType(5,FloatType))),AttributeDecl(Static,VarDecl(Id($X_),ArrayType(5,FloatType)))]),ClassDecl(Id(__m),[MethodDecl(Id(Constructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 72))

    def test_73(self):
        line = '''Class _:l_{}Class _:_{}Class _{}Class lARB_F{_(){}Var $r_:Boolean ;}'''
        expect = '''Program([ClassDecl(Id(_),Id(l_),[]),ClassDecl(Id(_),Id(_),[]),ClassDecl(Id(_),[]),ClassDecl(Id(lARB_F),[MethodDecl(Id(_),Instance,[],Block([],[])),AttributeDecl(Static,VarDecl(Id($r_),BoolType))])])'''
        self.assertTrue(TestAST.test(line, expect, 73))

    def test_74(self):
        line = '''Class _d_4{}Class __{Destructor (){}tH5(_,Wy:Array [Array [Array [Int ,0XC_2B],0x7],0b1001000];_9GFw,N:Boolean ){} }'''
        expect = '''Program([ClassDecl(Id(_d_4),[]),ClassDecl(Id(__),[MethodDecl(Id(Destructor),Instance,[],Block([],[])),MethodDecl(Id(tH5),Instance,[param(Id(_),ArrayType(72,ArrayType(7,ArrayType(3115,IntType)))),param(Id(Wy),ArrayType(72,ArrayType(7,ArrayType(3115,IntType)))),param(Id(_9GFw),BoolType),param(Id(N),BoolType)],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 74))

    def test_75(self):
        line = '''Class _:__{Constructor (){}Var __d,$4:Array [String ,0b1];}'''
        expect = '''Program([ClassDecl(Id(_),Id(__),[MethodDecl(Id(Constructor),Instance,[],Block([],[])),AttributeDecl(Instance,VarDecl(Id(__d),ArrayType(1,StringType))),AttributeDecl(Static,VarDecl(Id($4),ArrayType(1,StringType)))])])'''
        self.assertTrue(TestAST.test(line, expect, 75))

    def test_76(self):
        line = '''Class _q_{$7i_(){}Destructor (){}Var $T,Q_,$__,$_99,C7_:_P;}'''
        expect = '''Program([ClassDecl(Id(_q_),[MethodDecl(Id($7i_),Static,[],Block([],[])),MethodDecl(Id(Destructor),Instance,[],Block([],[])),AttributeDecl(Static,VarDecl(Id($T),ClassType(Id(_P)))),AttributeDecl(Instance,VarDecl(Id(Q_),ClassType(Id(_P)))),AttributeDecl(Static,VarDecl(Id($__),ClassType(Id(_P)))),AttributeDecl(Static,VarDecl(Id($_99),ClassType(Id(_P)))),AttributeDecl(Instance,VarDecl(Id(C7_),ClassType(Id(_P))))])])'''
        self.assertTrue(TestAST.test(line, expect, 76))

    def test_77(self):
        line = '''Class ___{Destructor (){} }Class _:_W_{}Class n_j4:S_7{}'''
        expect = '''Program([ClassDecl(Id(___),[MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(_),Id(_W_),[]),ClassDecl(Id(n_j4),Id(S_7),[])])'''
        self.assertTrue(TestAST.test(line, expect, 77))

    def test_78(self):
        line = '''Class _:Vf_{}Class _:d{Constructor (_,__89__,d,__c3K:_Z){} }Class i_4:P{$86(){} }'''
        expect = '''Program([ClassDecl(Id(_),Id(Vf_),[]),ClassDecl(Id(_),Id(d),[MethodDecl(Id(Constructor),Instance,[param(Id(_),ClassType(Id(_Z))),param(Id(__89__),ClassType(Id(_Z))),param(Id(d),ClassType(Id(_Z))),param(Id(__c3K),ClassType(Id(_Z)))],Block([],[]))]),ClassDecl(Id(i_4),Id(P),[MethodDecl(Id($86),Static,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 78))

    def test_79(self):
        line = '''Class _:_5x{Var $30SS_1Mk_d,_,_,$_,$__1,$0_,k7_:Float ;}'''
        expect = '''Program([ClassDecl(Id(_),Id(_5x),[AttributeDecl(Static,VarDecl(Id($30SS_1Mk_d),FloatType)),AttributeDecl(Instance,VarDecl(Id(_),FloatType)),AttributeDecl(Instance,VarDecl(Id(_),FloatType)),AttributeDecl(Static,VarDecl(Id($_),FloatType)),AttributeDecl(Static,VarDecl(Id($__1),FloatType)),AttributeDecl(Static,VarDecl(Id($0_),FloatType)),AttributeDecl(Instance,VarDecl(Id(k7_),FloatType))])])'''
        self.assertTrue(TestAST.test(line, expect, 79))

    def test_80(self):
        line = '''Class _3_{Constructor (d,_,_:Array [Array [Boolean ,0b11010],0x47]){} }'''
        expect = '''Program([ClassDecl(Id(_3_),[MethodDecl(Id(Constructor),Instance,[param(Id(d),ArrayType(71,ArrayType(26,BoolType))),param(Id(_),ArrayType(71,ArrayType(26,BoolType))),param(Id(_),ArrayType(71,ArrayType(26,BoolType)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 80))

    def test_81(self):
        line = '''Class z_:_L38{}Class _B:d_0__{Var $4,$5:Array [Float ,0b10];}'''
        expect = '''Program([ClassDecl(Id(z_),Id(_L38),[]),ClassDecl(Id(_B),Id(d_0__),[AttributeDecl(Static,VarDecl(Id($4),ArrayType(2,FloatType))),AttributeDecl(Static,VarDecl(Id($5),ArrayType(2,FloatType)))])])'''
        self.assertTrue(TestAST.test(line, expect, 81))

    def test_82(self):
        line = '''Class t:__{}Class _:_79{Constructor (T,_:Array [Array [Array [Float ,0B1000101],0xD],0x59]){} }'''
        expect = '''Program([ClassDecl(Id(t),Id(__),[]),ClassDecl(Id(_),Id(_79),[MethodDecl(Id(Constructor),Instance,[param(Id(T),ArrayType(89,ArrayType(13,ArrayType(69,FloatType)))),param(Id(_),ArrayType(89,ArrayType(13,ArrayType(69,FloatType))))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 82))

    def test_83(self):
        line = '''Class _{_(_,__5_56,Sy_,_O4:Array [Array [Int ,6],0B1011100]){} }'''
        expect = '''Program([ClassDecl(Id(_),[MethodDecl(Id(_),Instance,[param(Id(_),ArrayType(92,ArrayType(6,IntType))),param(Id(__5_56),ArrayType(92,ArrayType(6,IntType))),param(Id(Sy_),ArrayType(92,ArrayType(6,IntType))),param(Id(_O4),ArrayType(92,ArrayType(6,IntType)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 83))

    def test_84(self):
        line = '''Class nB{}Class wv{$6XE(_64C5__,_,_0ch,_:_){} }Class _:_{}Class __{}'''
        expect = '''Program([ClassDecl(Id(nB),[]),ClassDecl(Id(wv),[MethodDecl(Id($6XE),Static,[param(Id(_64C5__),ClassType(Id(_))),param(Id(_),ClassType(Id(_))),param(Id(_0ch),ClassType(Id(_))),param(Id(_),ClassType(Id(_)))],Block([],[]))]),ClassDecl(Id(_),Id(_),[]),ClassDecl(Id(__),[])])'''
        self.assertTrue(TestAST.test(line, expect, 84))

    def test_85(self):
        line = '''Class W75:dCX{Var _xg22,$_,q1__3:String ;Destructor (){Break ;} }Class tb:T8{}Class _d4:____{}'''
        expect = '''Program([ClassDecl(Id(W75),Id(dCX),[AttributeDecl(Instance,VarDecl(Id(_xg22),StringType)),AttributeDecl(Static,VarDecl(Id($_),StringType)),AttributeDecl(Instance,VarDecl(Id(q1__3),StringType)),MethodDecl(Id(Destructor),Instance,[],Block([],[Break]))]),ClassDecl(Id(tb),Id(T8),[]),ClassDecl(Id(_d4),Id(____),[])])'''
        self.assertTrue(TestAST.test(line, expect, 85))

    def test_86(self):
        line = '''Class L:R{Destructor (){}Destructor (){Break ;Break ;} }Class _{}'''
        expect = '''Program([ClassDecl(Id(L),Id(R),[MethodDecl(Id(Destructor),Instance,[],Block([],[])),MethodDecl(Id(Destructor),Instance,[],Block([],[Break,Break]))]),ClassDecl(Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 86))

    def test_87(self):
        line = '''Class _{}Class _{}Class Z_o6:S{$Y(_,j:Array [Float ,0b1];_zc7:Boolean ){} }'''
        expect = '''Program([ClassDecl(Id(_),[]),ClassDecl(Id(_),[]),ClassDecl(Id(Z_o6),Id(S),[MethodDecl(Id($Y),Static,[param(Id(_),ArrayType(1,FloatType)),param(Id(j),ArrayType(1,FloatType)),param(Id(_zc7),BoolType)],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 87))

    def test_88(self):
        line = '''Class F:v8{Constructor (_:_z8;_,_3_,_:_k6;o3T7:Boolean ){} }'''
        expect = '''Program([ClassDecl(Id(F),Id(v8),[MethodDecl(Id(Constructor),Instance,[param(Id(_),ClassType(Id(_z8))),param(Id(_),ClassType(Id(_k6))),param(Id(_3_),ClassType(Id(_k6))),param(Id(_),ClassType(Id(_k6))),param(Id(o3T7),BoolType)],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 88))

    def test_89(self):
        line = '''Class g7:j{Destructor (){} }Class __{}Class c{}Class _Kp:e1aw{}'''
        expect = '''Program([ClassDecl(Id(g7),Id(j),[MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(__),[]),ClassDecl(Id(c),[]),ClassDecl(Id(_Kp),Id(e1aw),[])])'''
        self.assertTrue(TestAST.test(line, expect, 89))

    def test_90(self):
        line = '''Class _:_{$8(___:__0;rTW:__X_;_1:_Py;_6j:Float ;__0,Kv75_9_,_:__h;__:Array [Array [Float ,80],0140];h,_:Array [Array [String ,03],0140]){} }'''
        expect = '''Program([ClassDecl(Id(_),Id(_),[MethodDecl(Id($8),Static,[param(Id(___),ClassType(Id(__0))),param(Id(rTW),ClassType(Id(__X_))),param(Id(_1),ClassType(Id(_Py))),param(Id(_6j),FloatType),param(Id(__0),ClassType(Id(__h))),param(Id(Kv75_9_),ClassType(Id(__h))),param(Id(_),ClassType(Id(__h))),param(Id(__),ArrayType(96,ArrayType(80,FloatType))),param(Id(h),ArrayType(96,ArrayType(3,StringType))),param(Id(_),ArrayType(96,ArrayType(3,StringType)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 90))

    def test_91(self):
        line = '''Class W31:J__{Constructor (__d__3:Array [Float ,95];__P:String ;_t_:_7;__,_:_;Y,z:Array [Array [Array [Array [Boolean ,01],052_3],15],0B1]){Continue ;{} }}Class M:c{}Class Cq:m{}Class M658F{}Class _:__{Constructor (n0:Array [Array [Float ,0114],95]){}Constructor (){} }'''
        expect = '''Program([ClassDecl(Id(W31),Id(J__),[MethodDecl(Id(Constructor),Instance,[param(Id(__d__3),ArrayType(95,FloatType)),param(Id(__P),StringType),param(Id(_t_),ClassType(Id(_7))),param(Id(__),ClassType(Id(_))),param(Id(_),ClassType(Id(_))),param(Id(Y),ArrayType(1,ArrayType(15,ArrayType(339,ArrayType(1,BoolType))))),param(Id(z),ArrayType(1,ArrayType(15,ArrayType(339,ArrayType(1,BoolType)))))],Block([],[Continue,Block([],[])]))]),ClassDecl(Id(M),Id(c),[]),ClassDecl(Id(Cq),Id(m),[]),ClassDecl(Id(M658F),[]),ClassDecl(Id(_),Id(__),[MethodDecl(Id(Constructor),Instance,[param(Id(n0),ArrayType(95,ArrayType(76,FloatType)))],Block([],[])),MethodDecl(Id(Constructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 91))

    def test_92(self):
        line = '''Class u{Constructor (F22_:_){Break ;}Var $_,$19,$95,$_,$4_:_;}'''
        expect = '''Program([ClassDecl(Id(u),[MethodDecl(Id(Constructor),Instance,[param(Id(F22_),ClassType(Id(_)))],Block([],[Break])),AttributeDecl(Static,VarDecl(Id($_),ClassType(Id(_)))),AttributeDecl(Static,VarDecl(Id($19),ClassType(Id(_)))),AttributeDecl(Static,VarDecl(Id($95),ClassType(Id(_)))),AttributeDecl(Static,VarDecl(Id($_),ClassType(Id(_)))),AttributeDecl(Static,VarDecl(Id($4_),ClassType(Id(_))))])])'''
        self.assertTrue(TestAST.test(line, expect, 92))

    def test_93(self):
        line = '''Class DEz59_4{}Class _:_l{}Class Kdv8_:_{}Class _:s8{}Class u_:_{Var I,K_,$I_,$_,_,Jig,AO4a:Array [Boolean ,074];}Class h:_{}Class _3H:k_40_o{}'''
        expect = '''Program([ClassDecl(Id(DEz59_4),[]),ClassDecl(Id(_),Id(_l),[]),ClassDecl(Id(Kdv8_),Id(_),[]),ClassDecl(Id(_),Id(s8),[]),ClassDecl(Id(u_),Id(_),[AttributeDecl(Instance,VarDecl(Id(I),ArrayType(60,BoolType))),AttributeDecl(Instance,VarDecl(Id(K_),ArrayType(60,BoolType))),AttributeDecl(Static,VarDecl(Id($I_),ArrayType(60,BoolType))),AttributeDecl(Static,VarDecl(Id($_),ArrayType(60,BoolType))),AttributeDecl(Instance,VarDecl(Id(_),ArrayType(60,BoolType))),AttributeDecl(Instance,VarDecl(Id(Jig),ArrayType(60,BoolType))),AttributeDecl(Instance,VarDecl(Id(AO4a),ArrayType(60,BoolType)))]),ClassDecl(Id(h),Id(_),[]),ClassDecl(Id(_3H),Id(k_40_o),[])])'''
        self.assertTrue(TestAST.test(line, expect, 93))

    def test_94(self):
        line = '''Class _z{Destructor (){}Destructor (){}Var U6,$6:Array [Boolean ,0B1001001];}'''
        expect = '''Program([ClassDecl(Id(_z),[MethodDecl(Id(Destructor),Instance,[],Block([],[])),MethodDecl(Id(Destructor),Instance,[],Block([],[])),AttributeDecl(Instance,VarDecl(Id(U6),ArrayType(73,BoolType))),AttributeDecl(Static,VarDecl(Id($6),ArrayType(73,BoolType)))])])'''
        self.assertTrue(TestAST.test(line, expect, 94))

    def test_95(self):
        line = '''Class _:_{}Class _:_P5{Var $_:r08;Var $w:Ak;}Class _{_US(){} }Class Bw:_{}Class _3{}'''
        expect = '''Program([ClassDecl(Id(_),Id(_),[]),ClassDecl(Id(_),Id(_P5),[AttributeDecl(Static,VarDecl(Id($_),ClassType(Id(r08)))),AttributeDecl(Static,VarDecl(Id($w),ClassType(Id(Ak))))]),ClassDecl(Id(_),[MethodDecl(Id(_US),Instance,[],Block([],[]))]),ClassDecl(Id(Bw),Id(_),[]),ClassDecl(Id(_3),[])])'''
        self.assertTrue(TestAST.test(line, expect, 95))

    def test_96(self):
        line = '''Class Hu{Constructor (){}_8FC(_5X4:Array [Boolean ,0B111];Bm,Y_P2,p:Array [Array [String ,3],0b1];x:p){} }'''
        expect = '''Program([ClassDecl(Id(Hu),[MethodDecl(Id(Constructor),Instance,[],Block([],[])),MethodDecl(Id(_8FC),Instance,[param(Id(_5X4),ArrayType(7,BoolType)),param(Id(Bm),ArrayType(1,ArrayType(3,StringType))),param(Id(Y_P2),ArrayType(1,ArrayType(3,StringType))),param(Id(p),ArrayType(1,ArrayType(3,StringType))),param(Id(x),ClassType(Id(p)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 96))

    def test_97(self):
        line = '''Class e:A{}Class _1u:_{_(I:Float ;_,_z35P__:o;V1,_,_:Int ){} }'''
        expect = '''Program([ClassDecl(Id(e),Id(A),[]),ClassDecl(Id(_1u),Id(_),[MethodDecl(Id(_),Instance,[param(Id(I),FloatType),param(Id(_),ClassType(Id(o))),param(Id(_z35P__),ClassType(Id(o))),param(Id(V1),IntType),param(Id(_),IntType),param(Id(_),IntType)],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 97))

    def test_98(self):
        line = '''Class Tf:__u{$v_2_(m4,V9,s64uE_:Array [Array [Int ,0x60],0b111110]){}$0(_e5_l_ON,nZ,g,_S:Array [Array [Float ,9_3],0x15];_C,_E_,R:Array [String ,0x7_B];__,_,_,B:String ){} }'''
        expect = '''Program([ClassDecl(Id(Tf),Id(__u),[MethodDecl(Id($v_2_),Static,[param(Id(m4),ArrayType(62,ArrayType(96,IntType))),param(Id(V9),ArrayType(62,ArrayType(96,IntType))),param(Id(s64uE_),ArrayType(62,ArrayType(96,IntType)))],Block([],[])),MethodDecl(Id($0),Static,[param(Id(_e5_l_ON),ArrayType(21,ArrayType(93,FloatType))),param(Id(nZ),ArrayType(21,ArrayType(93,FloatType))),param(Id(g),ArrayType(21,ArrayType(93,FloatType))),param(Id(_S),ArrayType(21,ArrayType(93,FloatType))),param(Id(_C),ArrayType(123,StringType)),param(Id(_E_),ArrayType(123,StringType)),param(Id(R),ArrayType(123,StringType)),param(Id(__),StringType),param(Id(_),StringType),param(Id(_),StringType),param(Id(B),StringType)],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 98))

    def test_99(self):
        line = '''Class B:_{Constructor (_wt,H:Array [Int ,0B1_0];PN62,U,v,a:Array [String ,0X45];_:Array [Array [String ,458_0],0xEF]){Continue ;}Constructor (_:Boolean ){} }'''
        expect = '''Program([ClassDecl(Id(B),Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(_wt),ArrayType(2,IntType)),param(Id(H),ArrayType(2,IntType)),param(Id(PN62),ArrayType(69,StringType)),param(Id(U),ArrayType(69,StringType)),param(Id(v),ArrayType(69,StringType)),param(Id(a),ArrayType(69,StringType)),param(Id(_),ArrayType(239,ArrayType(4580,StringType)))],Block([],[Continue])),MethodDecl(Id(Constructor),Instance,[param(Id(_),BoolType)],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 99))

    def test_100(self):
        line = '''Class N_:_1{Destructor (){Var _0:_5;Return ;Break ;} }Class j:Q{}'''
        expect = '''Program([ClassDecl(Id(N_),Id(_1),[MethodDecl(Id(Destructor),Instance,[],Block([VarDecl(Id(_0),ClassType(Id(_5)))],[Return(None),Break]))]),ClassDecl(Id(j),Id(Q),[])])'''
        self.assertTrue(TestAST.test(line, expect, 100))

    def test_101(self):
        line = '''Class _1{}Class _o6{}Class x:N{}Class n7Fl{Var $_,$_L,___:Float ;}Class FL:o{}'''
        expect = '''Program([ClassDecl(Id(_1),[]),ClassDecl(Id(_o6),[]),ClassDecl(Id(x),Id(N),[]),ClassDecl(Id(n7Fl),[AttributeDecl(Static,VarDecl(Id($_),FloatType)),AttributeDecl(Static,VarDecl(Id($_L),FloatType)),AttributeDecl(Instance,VarDecl(Id(___),FloatType))]),ClassDecl(Id(FL),Id(o),[])])'''
        self.assertTrue(TestAST.test(line, expect, 101))

    def test_102(self):
        line = '''Class R:L___{}Class _{Constructor (_:Array [Array [Array [Float ,0X8],0b11],07];_S:Array [Array [Int ,7_6],0b1_1];P,_,K,X1j:C){} }Class _{}'''
        expect = '''Program([ClassDecl(Id(R),Id(L___),[]),ClassDecl(Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(_),ArrayType(7,ArrayType(3,ArrayType(8,FloatType)))),param(Id(_S),ArrayType(3,ArrayType(76,IntType))),param(Id(P),ClassType(Id(C))),param(Id(_),ClassType(Id(C))),param(Id(K),ClassType(Id(C))),param(Id(X1j),ClassType(Id(C)))],Block([],[]))]),ClassDecl(Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 102))

    def test_103(self):
        line = '''Class _1:L{Var $9:Array [Array [Array [Array [String ,06],04],0b1],0102];}'''
        expect = '''Program([ClassDecl(Id(_1),Id(L),[AttributeDecl(Static,VarDecl(Id($9),ArrayType(66,ArrayType(1,ArrayType(4,ArrayType(6,StringType))))))])])'''
        self.assertTrue(TestAST.test(line, expect, 103))

    def test_104(self):
        line = '''Class __{eO(m3:Int ;_R,E4:Int ;_,k,S:_6Wl7a;fu,w,Op0:w;_:String ;_:Boolean ){Var R695,_,_,v:Array [Array [Boolean ,0x37],026];{} }}'''
        expect = '''Program([ClassDecl(Id(__),[MethodDecl(Id(eO),Instance,[param(Id(m3),IntType),param(Id(_R),IntType),param(Id(E4),IntType),param(Id(_),ClassType(Id(_6Wl7a))),param(Id(k),ClassType(Id(_6Wl7a))),param(Id(S),ClassType(Id(_6Wl7a))),param(Id(fu),ClassType(Id(w))),param(Id(w),ClassType(Id(w))),param(Id(Op0),ClassType(Id(w))),param(Id(_),StringType),param(Id(_),BoolType)],Block([VarDecl(Id(R695),ArrayType(22,ArrayType(55,BoolType))),VarDecl(Id(_),ArrayType(22,ArrayType(55,BoolType))),VarDecl(Id(_),ArrayType(22,ArrayType(55,BoolType))),VarDecl(Id(v),ArrayType(22,ArrayType(55,BoolType)))],[Block([],[])]))])])'''
        self.assertTrue(TestAST.test(line, expect, 104))

    def test_105(self):
        line = '''Class y3{}Class _{$_(_,_d:Array [Int ,0X4];S,__5_1_,Z,_91:Boolean ){} }'''
        expect = '''Program([ClassDecl(Id(y3),[]),ClassDecl(Id(_),[MethodDecl(Id($_),Static,[param(Id(_),ArrayType(4,IntType)),param(Id(_d),ArrayType(4,IntType)),param(Id(S),BoolType),param(Id(__5_1_),BoolType),param(Id(Z),BoolType),param(Id(_91),BoolType)],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 105))

    def test_106(self):
        line = '''Class _{Var _,_:Array [Array [Array [Array [Boolean ,0X3C],21],0B1_0],0b11];}'''
        expect = '''Program([ClassDecl(Id(_),[AttributeDecl(Instance,VarDecl(Id(_),ArrayType(3,ArrayType(2,ArrayType(21,ArrayType(60,BoolType)))))),AttributeDecl(Instance,VarDecl(Id(_),ArrayType(3,ArrayType(2,ArrayType(21,ArrayType(60,BoolType))))))])])'''
        self.assertTrue(TestAST.test(line, expect, 106))

    def test_107(self):
        line = '''Class X2:_2_{Var $5:_k_;}Class zvS49:d1{}Class _M{}Class _{}'''
        expect = '''Program([ClassDecl(Id(X2),Id(_2_),[AttributeDecl(Static,VarDecl(Id($5),ClassType(Id(_k_))))]),ClassDecl(Id(zvS49),Id(d1),[]),ClassDecl(Id(_M),[]),ClassDecl(Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 107))

    def test_108(self):
        line = '''Class _L:_b__y_3r{Var t:Array [String ,0B1];Constructor (){} }'''
        expect = '''Program([ClassDecl(Id(_L),Id(_b__y_3r),[AttributeDecl(Instance,VarDecl(Id(t),ArrayType(1,StringType))),MethodDecl(Id(Constructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 108))

    def test_109(self):
        line = '''Class A{Var $_7S_:Boolean ;}Class _q2_73:N{}Class _Jm26:W{}'''
        expect = '''Program([ClassDecl(Id(A),[AttributeDecl(Static,VarDecl(Id($_7S_),BoolType))]),ClassDecl(Id(_q2_73),Id(N),[]),ClassDecl(Id(_Jm26),Id(W),[])])'''
        self.assertTrue(TestAST.test(line, expect, 109))

    def test_110(self):
        line = '''Class Tm_HB:_r{}Class _1{Var p,$J,_:Float ;Destructor (){}Constructor (Ol:Int ){}Constructor (_:String ;_,U,G:Array [String ,76]){Continue ;} }'''
        expect = '''Program([ClassDecl(Id(Tm_HB),Id(_r),[]),ClassDecl(Id(_1),[AttributeDecl(Instance,VarDecl(Id(p),FloatType)),AttributeDecl(Static,VarDecl(Id($J),FloatType)),AttributeDecl(Instance,VarDecl(Id(_),FloatType)),MethodDecl(Id(Destructor),Instance,[],Block([],[])),MethodDecl(Id(Constructor),Instance,[param(Id(Ol),IntType)],Block([],[])),MethodDecl(Id(Constructor),Instance,[param(Id(_),StringType),param(Id(_),ArrayType(76,StringType)),param(Id(U),ArrayType(76,StringType)),param(Id(G),ArrayType(76,StringType))],Block([],[Continue]))])])'''
        self.assertTrue(TestAST.test(line, expect, 110))

    def test_111(self):
        line = '''Class _{X1b(){}Constructor (){}Destructor (){}Destructor (){Break ;} }'''
        expect = '''Program([ClassDecl(Id(_),[MethodDecl(Id(X1b),Instance,[],Block([],[])),MethodDecl(Id(Constructor),Instance,[],Block([],[])),MethodDecl(Id(Destructor),Instance,[],Block([],[])),MethodDecl(Id(Destructor),Instance,[],Block([],[Break]))])])'''
        self.assertTrue(TestAST.test(line, expect, 111))

    def test_112(self):
        line = '''Class t:_23_{DL7q(b,_4_:Array [Array [Array [String ,0x37],03],0B11_1]){} }Class __:_i{}'''
        expect = '''Program([ClassDecl(Id(t),Id(_23_),[MethodDecl(Id(DL7q),Instance,[param(Id(b),ArrayType(7,ArrayType(3,ArrayType(55,StringType)))),param(Id(_4_),ArrayType(7,ArrayType(3,ArrayType(55,StringType))))],Block([],[]))]),ClassDecl(Id(__),Id(_i),[])])'''
        self.assertTrue(TestAST.test(line, expect, 112))

    def test_113(self):
        line = '''Class I:_{Var __4:Array [Array [Array [Array [Array [Float ,0X3C],050],0x702],0x3],0B1011];}'''
        expect = '''Program([ClassDecl(Id(I),Id(_),[AttributeDecl(Instance,VarDecl(Id(__4),ArrayType(11,ArrayType(3,ArrayType(1794,ArrayType(40,ArrayType(60,FloatType)))))))])])'''
        self.assertTrue(TestAST.test(line, expect, 113))

    def test_114(self):
        line = '''Class d:_{Var $n:Array [Array [Float ,0145],0b10_00_1];}Class f{}'''
        expect = '''Program([ClassDecl(Id(d),Id(_),[AttributeDecl(Static,VarDecl(Id($n),ArrayType(17,ArrayType(101,FloatType))))]),ClassDecl(Id(f),[])])'''
        self.assertTrue(TestAST.test(line, expect, 114))

    def test_115(self):
        line = '''Class k{}Class _W:_4{_(___0:Array [String ,02];_9e_7H,__2:Int ){} }'''
        expect = '''Program([ClassDecl(Id(k),[]),ClassDecl(Id(_W),Id(_4),[MethodDecl(Id(_),Instance,[param(Id(___0),ArrayType(2,StringType)),param(Id(_9e_7H),IntType),param(Id(__2),IntType)],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 115))

    def test_116(self):
        line = '''Class _f:E{}Class D:m{}Class __8{Var i:Float ;}Class ___:_{}'''
        expect = '''Program([ClassDecl(Id(_f),Id(E),[]),ClassDecl(Id(D),Id(m),[]),ClassDecl(Id(__8),[AttributeDecl(Instance,VarDecl(Id(i),FloatType))]),ClassDecl(Id(___),Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 116))

    def test_117(self):
        line = '''Class _:o{Var tS_,$V_,__:Array [Array [Array [Array [Array [Float ,0b10101],0x4],42],0b10101],0B11];}'''
        expect = '''Program([ClassDecl(Id(_),Id(o),[AttributeDecl(Instance,VarDecl(Id(tS_),ArrayType(3,ArrayType(21,ArrayType(42,ArrayType(4,ArrayType(21,FloatType))))))),AttributeDecl(Static,VarDecl(Id($V_),ArrayType(3,ArrayType(21,ArrayType(42,ArrayType(4,ArrayType(21,FloatType))))))),AttributeDecl(Instance,VarDecl(Id(__),ArrayType(3,ArrayType(21,ArrayType(42,ArrayType(4,ArrayType(21,FloatType)))))))])])'''
        self.assertTrue(TestAST.test(line, expect, 117))

    def test_118(self):
        line = '''Class Y_{_88__(_,P:String ;_,f_:Int ;t,_:Boolean ;_:Array [Boolean ,042];y,_:u_){}_(){} }Class b:_d{_(){}$z93J(_:Array [Array [String ,0b111101],87];V:Float ){} }Class _:g_{}'''
        expect = '''Program([ClassDecl(Id(Y_),[MethodDecl(Id(_88__),Instance,[param(Id(_),StringType),param(Id(P),StringType),param(Id(_),IntType),param(Id(f_),IntType),param(Id(t),BoolType),param(Id(_),BoolType),param(Id(_),ArrayType(34,BoolType)),param(Id(y),ClassType(Id(u_))),param(Id(_),ClassType(Id(u_)))],Block([],[])),MethodDecl(Id(_),Instance,[],Block([],[]))]),ClassDecl(Id(b),Id(_d),[MethodDecl(Id(_),Instance,[],Block([],[])),MethodDecl(Id($z93J),Static,[param(Id(_),ArrayType(87,ArrayType(61,StringType))),param(Id(V),FloatType)],Block([],[]))]),ClassDecl(Id(_),Id(g_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 118))

    def test_119(self):
        line = '''Class _{Constructor (_9_c:_21;_:_;H4m:Array [Array [Array [Array [Float ,024],04],0b111110],100]){}Destructor (){_4::$6();Return ;} }'''
        expect = '''Program([ClassDecl(Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(_9_c),ClassType(Id(_21))),param(Id(_),ClassType(Id(_))),param(Id(H4m),ArrayType(100,ArrayType(62,ArrayType(4,ArrayType(20,FloatType)))))],Block([],[])),MethodDecl(Id(Destructor),Instance,[],Block([],[Call(Id(_4),Id($6),[]),Return(None)]))])])'''
        self.assertTrue(TestAST.test(line, expect, 119))

    def test_120(self):
        line = '''Class g{}Class _:_{}Class b_{}Class _63_5:O52{Var $7_:__X;}'''
        expect = '''Program([ClassDecl(Id(g),[]),ClassDecl(Id(_),Id(_),[]),ClassDecl(Id(b_),[]),ClassDecl(Id(_63_5),Id(O52),[AttributeDecl(Static,VarDecl(Id($7_),ClassType(Id(__X))))])])'''
        self.assertTrue(TestAST.test(line, expect, 120))

    def test_121(self):
        line = '''Class __{$_h3_j(_:String ){}Constructor (){} }Class _z_:_{Var _3:_w2;}'''
        expect = '''Program([ClassDecl(Id(__),[MethodDecl(Id($_h3_j),Static,[param(Id(_),StringType)],Block([],[])),MethodDecl(Id(Constructor),Instance,[],Block([],[]))]),ClassDecl(Id(_z_),Id(_),[AttributeDecl(Instance,VarDecl(Id(_3),ClassType(Id(_w2))))])])'''
        self.assertTrue(TestAST.test(line, expect, 121))

    def test_122(self):
        line = '''Class _0{Var H:n;}Class D_7fe1_{}Class ___:p_{Destructor (){}$6H(j5wF,_:Float ){} }'''
        expect = '''Program([ClassDecl(Id(_0),[AttributeDecl(Instance,VarDecl(Id(H),ClassType(Id(n))))]),ClassDecl(Id(D_7fe1_),[]),ClassDecl(Id(___),Id(p_),[MethodDecl(Id(Destructor),Instance,[],Block([],[])),MethodDecl(Id($6H),Static,[param(Id(j5wF),FloatType),param(Id(_),FloatType)],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 122))

    def test_123(self):
        line = '''Class _P8{}Class _V8:__{Constructor (f_:E;_,W:A;T02_:_){} }'''
        expect = '''Program([ClassDecl(Id(_P8),[]),ClassDecl(Id(_V8),Id(__),[MethodDecl(Id(Constructor),Instance,[param(Id(f_),ClassType(Id(E))),param(Id(_),ClassType(Id(A))),param(Id(W),ClassType(Id(A))),param(Id(T02_),ClassType(Id(_)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 123))

    def test_124(self):
        line = '''Class Y4_{Var $_:Int ;}Class tr:y{Constructor (){Return ;}Constructor (e:_4){} }'''
        expect = '''Program([ClassDecl(Id(Y4_),[AttributeDecl(Static,VarDecl(Id($_),IntType))]),ClassDecl(Id(tr),Id(y),[MethodDecl(Id(Constructor),Instance,[],Block([],[Return(None)])),MethodDecl(Id(Constructor),Instance,[param(Id(e),ClassType(Id(_4)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 124))

    def test_125(self):
        line = '''Class PRo:__{}Class p{}Class j_{}Class _j{Constructor (){} }'''
        expect = '''Program([ClassDecl(Id(PRo),Id(__),[]),ClassDecl(Id(p),[]),ClassDecl(Id(j_),[]),ClassDecl(Id(_j),[MethodDecl(Id(Constructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 125))

    def test_126(self):
        line = '''Class p:i{_q(h_,Ta,_G_:Array [Float ,0B1010110];___,z,_:Array [Boolean ,0x2_3_3_5_8_F];h1:Array [Array [String ,0122],0X59]){} }'''
        expect = '''Program([ClassDecl(Id(p),Id(i),[MethodDecl(Id(_q),Instance,[param(Id(h_),ArrayType(86,FloatType)),param(Id(Ta),ArrayType(86,FloatType)),param(Id(_G_),ArrayType(86,FloatType)),param(Id(___),ArrayType(2307471,BoolType)),param(Id(z),ArrayType(2307471,BoolType)),param(Id(_),ArrayType(2307471,BoolType)),param(Id(h1),ArrayType(89,ArrayType(82,StringType)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 126))

    def test_127(self):
        line = '''Class _7_{}Class j:_0__{Constructor (V,_:Array [Array [Int ,0121],0x6]){Continue ;} }Class d1x_{}Class y__t{}Class sU0:__{}'''
        expect = '''Program([ClassDecl(Id(_7_),[]),ClassDecl(Id(j),Id(_0__),[MethodDecl(Id(Constructor),Instance,[param(Id(V),ArrayType(6,ArrayType(81,IntType))),param(Id(_),ArrayType(6,ArrayType(81,IntType)))],Block([],[Continue]))]),ClassDecl(Id(d1x_),[]),ClassDecl(Id(y__t),[]),ClassDecl(Id(sU0),Id(__),[])])'''
        self.assertTrue(TestAST.test(line, expect, 127))

    def test_128(self):
        line = '''Class __:__9_5V{Var $ni,O69:Array [Int ,3];_(c,_,_h:Float ;hSn:_z__;__:A){} }'''
        expect = '''Program([ClassDecl(Id(__),Id(__9_5V),[AttributeDecl(Static,VarDecl(Id($ni),ArrayType(3,IntType))),AttributeDecl(Instance,VarDecl(Id(O69),ArrayType(3,IntType))),MethodDecl(Id(_),Instance,[param(Id(c),FloatType),param(Id(_),FloatType),param(Id(_h),FloatType),param(Id(hSn),ClassType(Id(_z__))),param(Id(__),ClassType(Id(A)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 128))

    def test_129(self):
        line = '''Class _r{Constructor (N,H_,E,vi_0e_:Int ;W,l:y_1_;_g:Int ;H40P:Array [Boolean ,0XEF];_d:_;_:Float ;__:q;_,_n,_,_,_0:X){} }'''
        expect = '''Program([ClassDecl(Id(_r),[MethodDecl(Id(Constructor),Instance,[param(Id(N),IntType),param(Id(H_),IntType),param(Id(E),IntType),param(Id(vi_0e_),IntType),param(Id(W),ClassType(Id(y_1_))),param(Id(l),ClassType(Id(y_1_))),param(Id(_g),IntType),param(Id(H40P),ArrayType(239,BoolType)),param(Id(_d),ClassType(Id(_))),param(Id(_),FloatType),param(Id(__),ClassType(Id(q))),param(Id(_),ClassType(Id(X))),param(Id(_n),ClassType(Id(X))),param(Id(_),ClassType(Id(X))),param(Id(_),ClassType(Id(X))),param(Id(_0),ClassType(Id(X)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 129))

    def test_130(self):
        line = '''Class m{Var _:CK6_;Var $_zaA2I7,f,$_Hi_5_1:Boolean ;}Class t5:x_{}'''
        expect = '''Program([ClassDecl(Id(m),[AttributeDecl(Instance,VarDecl(Id(_),ClassType(Id(CK6_)))),AttributeDecl(Static,VarDecl(Id($_zaA2I7),BoolType)),AttributeDecl(Instance,VarDecl(Id(f),BoolType)),AttributeDecl(Static,VarDecl(Id($_Hi_5_1),BoolType))]),ClassDecl(Id(t5),Id(x_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 130))

    def test_131(self):
        line = '''Class _{}Class __{_eU_(__93:_){} }Class Z_:_{Constructor (){} }Class _:_{}Class S:_{}'''
        expect = '''Program([ClassDecl(Id(_),[]),ClassDecl(Id(__),[MethodDecl(Id(_eU_),Instance,[param(Id(__93),ClassType(Id(_)))],Block([],[]))]),ClassDecl(Id(Z_),Id(_),[MethodDecl(Id(Constructor),Instance,[],Block([],[]))]),ClassDecl(Id(_),Id(_),[]),ClassDecl(Id(S),Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 131))

    def test_132(self):
        line = '''Class Q31C{Destructor (){Break ;}R(r_8_9_,Q,_:o_Q_;JY2eG,_,_6,Z4:Array [Int ,0X64_0]){}$m_(P2,___,Q:Float ){} }'''
        expect = '''Program([ClassDecl(Id(Q31C),[MethodDecl(Id(Destructor),Instance,[],Block([],[Break])),MethodDecl(Id(R),Instance,[param(Id(r_8_9_),ClassType(Id(o_Q_))),param(Id(Q),ClassType(Id(o_Q_))),param(Id(_),ClassType(Id(o_Q_))),param(Id(JY2eG),ArrayType(1600,IntType)),param(Id(_),ArrayType(1600,IntType)),param(Id(_6),ArrayType(1600,IntType)),param(Id(Z4),ArrayType(1600,IntType))],Block([],[])),MethodDecl(Id($m_),Static,[param(Id(P2),FloatType),param(Id(___),FloatType),param(Id(Q),FloatType)],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 132))

    def test_133(self):
        line = '''Class _6:R{Destructor (){}Destructor (){} }Class s2Xg:Q__{}Class z:_{$bc77_5_vr(_c,W:Array [Array [Array [Array [String ,0x1B_17_E_2],0XF_FE],0xB_C_C],0x2_6];Y:String ;_:Int ){} }'''
        expect = '''Program([ClassDecl(Id(_6),Id(R),[MethodDecl(Id(Destructor),Instance,[],Block([],[])),MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(s2Xg),Id(Q__),[]),ClassDecl(Id(z),Id(_),[MethodDecl(Id($bc77_5_vr),Static,[param(Id(_c),ArrayType(38,ArrayType(3020,ArrayType(4094,ArrayType(1775586,StringType))))),param(Id(W),ArrayType(38,ArrayType(3020,ArrayType(4094,ArrayType(1775586,StringType))))),param(Id(Y),StringType),param(Id(_),IntType)],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 133))

    def test_134(self):
        line = '''Class _fk:D{Var $zn,__,U_:Array [Array [Boolean ,02],0x2A];}'''
        expect = '''Program([ClassDecl(Id(_fk),Id(D),[AttributeDecl(Static,VarDecl(Id($zn),ArrayType(42,ArrayType(2,BoolType)))),AttributeDecl(Instance,VarDecl(Id(__),ArrayType(42,ArrayType(2,BoolType)))),AttributeDecl(Instance,VarDecl(Id(U_),ArrayType(42,ArrayType(2,BoolType))))])])'''
        self.assertTrue(TestAST.test(line, expect, 134))

    def test_135(self):
        line = '''Class _{$_(X:Array [String ,036];kF8:Boolean ;_1,D,_d:_){iL::$_._V();} }'''
        expect = '''Program([ClassDecl(Id(_),[MethodDecl(Id($_),Static,[param(Id(X),ArrayType(30,StringType)),param(Id(kF8),BoolType),param(Id(_1),ClassType(Id(_))),param(Id(D),ClassType(Id(_))),param(Id(_d),ClassType(Id(_)))],Block([],[Call(FieldAccess(Id(iL),Id($_)),Id(_V),[])]))])])'''
        self.assertTrue(TestAST.test(line, expect, 135))

    def test_136(self):
        line = '''Class __:_{c(b:Array [Array [Array [Float ,0X40],0X40],0x3A]){Break ;Break ;} }'''
        expect = '''Program([ClassDecl(Id(__),Id(_),[MethodDecl(Id(c),Instance,[param(Id(b),ArrayType(58,ArrayType(64,ArrayType(64,FloatType))))],Block([],[Break,Break]))])])'''
        self.assertTrue(TestAST.test(line, expect, 136))

    def test_137(self):
        line = '''Class q3:O{}Class a:q{}Class _{}Class N:M{Destructor (){} }Class Hd4o{}Class _{_8(){}_(){} }'''
        expect = '''Program([ClassDecl(Id(q3),Id(O),[]),ClassDecl(Id(a),Id(q),[]),ClassDecl(Id(_),[]),ClassDecl(Id(N),Id(M),[MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(Hd4o),[]),ClassDecl(Id(_),[MethodDecl(Id(_8),Instance,[],Block([],[])),MethodDecl(Id(_),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 137))

    def test_138(self):
        line = '''Class Y6:L{}Class U:_{Var $t:Boolean ;Destructor (){} }Class l:h_{$_(){} }'''
        expect = '''Program([ClassDecl(Id(Y6),Id(L),[]),ClassDecl(Id(U),Id(_),[AttributeDecl(Static,VarDecl(Id($t),BoolType)),MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(l),Id(h_),[MethodDecl(Id($_),Static,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 138))

    def test_139(self):
        line = '''Class X:__3{}Class F6:h{Destructor (){} }Class n_I:_55A0{}Class H{}'''
        expect = '''Program([ClassDecl(Id(X),Id(__3),[]),ClassDecl(Id(F6),Id(h),[MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(n_I),Id(_55A0),[]),ClassDecl(Id(H),[])])'''
        self.assertTrue(TestAST.test(line, expect, 139))

    def test_140(self):
        line = '''Class _Y{Var _,r2,$6:Array [Float ,5_42];Destructor (){} }'''
        expect = '''Program([ClassDecl(Id(_Y),[AttributeDecl(Instance,VarDecl(Id(_),ArrayType(542,FloatType))),AttributeDecl(Instance,VarDecl(Id(r2),ArrayType(542,FloatType))),AttributeDecl(Static,VarDecl(Id($6),ArrayType(542,FloatType))),MethodDecl(Id(Destructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 140))

    def test_141(self):
        line = '''Class T{}Class _:z{Constructor (_:m_ib){ {Return ;} }}Class _{}Class G:O__8{}Class _6:_C{}'''
        expect = '''Program([ClassDecl(Id(T),[]),ClassDecl(Id(_),Id(z),[MethodDecl(Id(Constructor),Instance,[param(Id(_),ClassType(Id(m_ib)))],Block([],[Block([],[Return(None)])]))]),ClassDecl(Id(_),[]),ClassDecl(Id(G),Id(O__8),[]),ClassDecl(Id(_6),Id(_C),[])])'''
        self.assertTrue(TestAST.test(line, expect, 141))

    def test_142(self):
        line = '''Class _:_9{$_D_(t2_C:G_0){} }Class _{}Class T:_{Destructor (){} }Class M:Z{Constructor (){} }'''
        expect = '''Program([ClassDecl(Id(_),Id(_9),[MethodDecl(Id($_D_),Static,[param(Id(t2_C),ClassType(Id(G_0)))],Block([],[]))]),ClassDecl(Id(_),[]),ClassDecl(Id(T),Id(_),[MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(M),Id(Z),[MethodDecl(Id(Constructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 142))

    def test_143(self):
        line = '''Class _:Y_{Var _9,_:Array [Array [Array [Float ,34],34],34];}Class j4{}'''
        expect = '''Program([ClassDecl(Id(_),Id(Y_),[AttributeDecl(Instance,VarDecl(Id(_9),ArrayType(34,ArrayType(34,ArrayType(34,FloatType))))),AttributeDecl(Instance,VarDecl(Id(_),ArrayType(34,ArrayType(34,ArrayType(34,FloatType)))))]),ClassDecl(Id(j4),[])])'''
        self.assertTrue(TestAST.test(line, expect, 143))

    def test_144(self):
        line = '''Class P86{Constructor (T_:Float ;_,_:__;W_:__){Break ;} }'''
        expect = '''Program([ClassDecl(Id(P86),[MethodDecl(Id(Constructor),Instance,[param(Id(T_),FloatType),param(Id(_),ClassType(Id(__))),param(Id(_),ClassType(Id(__))),param(Id(W_),ClassType(Id(__)))],Block([],[Break]))])])'''
        self.assertTrue(TestAST.test(line, expect, 144))

    def test_145(self):
        line = '''Class F{_N(v,i,_,b,__:String ;W:Int ;CJm,y,_:O2_i1_;E_,_S,_,_:Array [Float ,04];_,_:String ;_89,m8_,_4:String ;i:V){}Constructor (_52_h743:String ;X,d,CV1_18:_;_:x;_,u:Int ;_o,KT:Int ){}Constructor (_T_47__,___,_:Float ;_,V,E:Array [Array [Array [String ,0b110],9],04_0]){}Destructor (){} }'''
        expect = '''Program([ClassDecl(Id(F),[MethodDecl(Id(_N),Instance,[param(Id(v),StringType),param(Id(i),StringType),param(Id(_),StringType),param(Id(b),StringType),param(Id(__),StringType),param(Id(W),IntType),param(Id(CJm),ClassType(Id(O2_i1_))),param(Id(y),ClassType(Id(O2_i1_))),param(Id(_),ClassType(Id(O2_i1_))),param(Id(E_),ArrayType(4,FloatType)),param(Id(_S),ArrayType(4,FloatType)),param(Id(_),ArrayType(4,FloatType)),param(Id(_),ArrayType(4,FloatType)),param(Id(_),StringType),param(Id(_),StringType),param(Id(_89),StringType),param(Id(m8_),StringType),param(Id(_4),StringType),param(Id(i),ClassType(Id(V)))],Block([],[])),MethodDecl(Id(Constructor),Instance,[param(Id(_52_h743),StringType),param(Id(X),ClassType(Id(_))),param(Id(d),ClassType(Id(_))),param(Id(CV1_18),ClassType(Id(_))),param(Id(_),ClassType(Id(x))),param(Id(_),IntType),param(Id(u),IntType),param(Id(_o),IntType),param(Id(KT),IntType)],Block([],[])),MethodDecl(Id(Constructor),Instance,[param(Id(_T_47__),FloatType),param(Id(___),FloatType),param(Id(_),FloatType),param(Id(_),ArrayType(32,ArrayType(9,ArrayType(6,StringType)))),param(Id(V),ArrayType(32,ArrayType(9,ArrayType(6,StringType)))),param(Id(E),ArrayType(32,ArrayType(9,ArrayType(6,StringType))))],Block([],[])),MethodDecl(Id(Destructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 145))

    def test_146(self):
        line = '''Class _67p{}Class _:_{h(){}Constructor (){ {} }Constructor (){} }'''
        expect = '''Program([ClassDecl(Id(_67p),[]),ClassDecl(Id(_),Id(_),[MethodDecl(Id(h),Instance,[],Block([],[])),MethodDecl(Id(Constructor),Instance,[],Block([],[Block([],[])])),MethodDecl(Id(Constructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 146))

    def test_147(self):
        line = '''Class _5{Var O,$80_,$I:String ;}Class _:q_{Var _Z,$__,$_,$_:t;}'''
        expect = '''Program([ClassDecl(Id(_5),[AttributeDecl(Instance,VarDecl(Id(O),StringType)),AttributeDecl(Static,VarDecl(Id($80_),StringType)),AttributeDecl(Static,VarDecl(Id($I),StringType))]),ClassDecl(Id(_),Id(q_),[AttributeDecl(Instance,VarDecl(Id(_Z),ClassType(Id(t)))),AttributeDecl(Static,VarDecl(Id($__),ClassType(Id(t)))),AttributeDecl(Static,VarDecl(Id($_),ClassType(Id(t)))),AttributeDecl(Static,VarDecl(Id($_),ClassType(Id(t))))])])'''
        self.assertTrue(TestAST.test(line, expect, 147))

    def test_148(self):
        line = '''Class _1{}Class K{}Class f_{z9KB7j7Ae(_G_G:Boolean ;_:u;_,Z:Int ){} }'''
        expect = '''Program([ClassDecl(Id(_1),[]),ClassDecl(Id(K),[]),ClassDecl(Id(f_),[MethodDecl(Id(z9KB7j7Ae),Instance,[param(Id(_G_G),BoolType),param(Id(_),ClassType(Id(u))),param(Id(_),IntType),param(Id(Z),IntType)],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 148))

    def test_149(self):
        line = '''Class _{Var _:Array [Array [Array [Boolean ,0X3F],23],0XF_4];}Class _{}'''
        expect = '''Program([ClassDecl(Id(_),[AttributeDecl(Instance,VarDecl(Id(_),ArrayType(244,ArrayType(23,ArrayType(63,BoolType)))))]),ClassDecl(Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 149))

    def test_150(self):
        line = '''Class A:j{Var $14_p,_MD,$1Uz:_;Destructor (){} }Class _{}'''
        expect = '''Program([ClassDecl(Id(A),Id(j),[AttributeDecl(Static,VarDecl(Id($14_p),ClassType(Id(_)))),AttributeDecl(Instance,VarDecl(Id(_MD),ClassType(Id(_)))),AttributeDecl(Static,VarDecl(Id($1Uz),ClassType(Id(_)))),MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 150))

    def test_151(self):
        line = '''Class __cO:a_9_{Constructor (_:_8_;Ye9t_:_){} }Class S_2__{}'''
        expect = '''Program([ClassDecl(Id(__cO),Id(a_9_),[MethodDecl(Id(Constructor),Instance,[param(Id(_),ClassType(Id(_8_))),param(Id(Ye9t_),ClassType(Id(_)))],Block([],[]))]),ClassDecl(Id(S_2__),[])])'''
        self.assertTrue(TestAST.test(line, expect, 151))

    def test_152(self):
        line = '''Class p:W{}Class a_{}Class __Qa_{}Class B7{}Class _:_{U(_x_:String ;_,c_,_,_,_:Array [Float ,0b1010011]){_::$_().Z__();} }'''
        expect = '''Program([ClassDecl(Id(p),Id(W),[]),ClassDecl(Id(a_),[]),ClassDecl(Id(__Qa_),[]),ClassDecl(Id(B7),[]),ClassDecl(Id(_),Id(_),[MethodDecl(Id(U),Instance,[param(Id(_x_),StringType),param(Id(_),ArrayType(83,FloatType)),param(Id(c_),ArrayType(83,FloatType)),param(Id(_),ArrayType(83,FloatType)),param(Id(_),ArrayType(83,FloatType)),param(Id(_),ArrayType(83,FloatType))],Block([],[Call(CallExpr(Id(_),Id($_),[]),Id(Z__),[])]))])])'''
        self.assertTrue(TestAST.test(line, expect, 152))

    def test_153(self):
        line = '''Class _{}Class _:s{Var $3:Array [Array [String ,077],0B101101];}Class _0_j{Destructor (){}Var _N,y_,_,v:Array [String ,0X59];Var _2:Array [String ,6_083];}'''
        expect = '''Program([ClassDecl(Id(_),[]),ClassDecl(Id(_),Id(s),[AttributeDecl(Static,VarDecl(Id($3),ArrayType(45,ArrayType(63,StringType))))]),ClassDecl(Id(_0_j),[MethodDecl(Id(Destructor),Instance,[],Block([],[])),AttributeDecl(Instance,VarDecl(Id(_N),ArrayType(89,StringType))),AttributeDecl(Instance,VarDecl(Id(y_),ArrayType(89,StringType))),AttributeDecl(Instance,VarDecl(Id(_),ArrayType(89,StringType))),AttributeDecl(Instance,VarDecl(Id(v),ArrayType(89,StringType))),AttributeDecl(Instance,VarDecl(Id(_2),ArrayType(6083,StringType)))])])'''
        self.assertTrue(TestAST.test(line, expect, 153))

    def test_154(self):
        line = '''Class _9:__{Destructor (){Var w,_,_,_o:Boolean ;} }Class r{}'''
        expect = '''Program([ClassDecl(Id(_9),Id(__),[MethodDecl(Id(Destructor),Instance,[],Block([VarDecl(Id(w),BoolType),VarDecl(Id(_),BoolType),VarDecl(Id(_),BoolType),VarDecl(Id(_o),BoolType)],[]))]),ClassDecl(Id(r),[])])'''
        self.assertTrue(TestAST.test(line, expect, 154))

    def test_155(self):
        line = '''Class _:_{}Class __:_9{$0(){}Var M,$3,__6_u_,U,$_,$k:Array [String ,0B10000];Var $_n,_:Float ;}'''
        expect = '''Program([ClassDecl(Id(_),Id(_),[]),ClassDecl(Id(__),Id(_9),[MethodDecl(Id($0),Static,[],Block([],[])),AttributeDecl(Instance,VarDecl(Id(M),ArrayType(16,StringType))),AttributeDecl(Static,VarDecl(Id($3),ArrayType(16,StringType))),AttributeDecl(Instance,VarDecl(Id(__6_u_),ArrayType(16,StringType))),AttributeDecl(Instance,VarDecl(Id(U),ArrayType(16,StringType))),AttributeDecl(Static,VarDecl(Id($_),ArrayType(16,StringType))),AttributeDecl(Static,VarDecl(Id($k),ArrayType(16,StringType))),AttributeDecl(Static,VarDecl(Id($_n),FloatType)),AttributeDecl(Instance,VarDecl(Id(_),FloatType))])])'''
        self.assertTrue(TestAST.test(line, expect, 155))

    def test_156(self):
        line = '''Class _:_{Var _,$3:Array [Array [Int ,87],0X7_FD2];}Class G_:_8_{}'''
        expect = '''Program([ClassDecl(Id(_),Id(_),[AttributeDecl(Instance,VarDecl(Id(_),ArrayType(32722,ArrayType(87,IntType)))),AttributeDecl(Static,VarDecl(Id($3),ArrayType(32722,ArrayType(87,IntType))))]),ClassDecl(Id(G_),Id(_8_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 156))

    def test_157(self):
        line = '''Class _4w:_{_8(){}$_4(_:Array [Array [Array [Array [Float ,0B1011],0b10001],2],6]){}$W(_:Array [Array [Array [Array [Array [Array [Array [String ,1],0B1011],0B1011],0B1],0b11],036],036];_4n__:Array [Array [Array [Array [Array [Array [Array [Array [Array [Int ,0B1011],0x3F],0xD],0X5C],2],0B111_10],0b1_010],0b10001],2];ja,H:Array [Int ,0x3F]){} }'''
        expect = '''Program([ClassDecl(Id(_4w),Id(_),[MethodDecl(Id(_8),Instance,[],Block([],[])),MethodDecl(Id($_4),Static,[param(Id(_),ArrayType(6,ArrayType(2,ArrayType(17,ArrayType(11,FloatType)))))],Block([],[])),MethodDecl(Id($W),Static,[param(Id(_),ArrayType(30,ArrayType(30,ArrayType(3,ArrayType(1,ArrayType(11,ArrayType(11,ArrayType(1,StringType)))))))),param(Id(_4n__),ArrayType(2,ArrayType(17,ArrayType(10,ArrayType(30,ArrayType(2,ArrayType(92,ArrayType(13,ArrayType(63,ArrayType(11,IntType)))))))))),param(Id(ja),ArrayType(63,IntType)),param(Id(H),ArrayType(63,IntType))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 157))

    def test_158(self):
        line = '''Class _U:_{$R45a(t:String ){}__88(t__,g_AD8:Float ;_,O____s__5:Array [Array [Boolean ,9],0b1000001]){} }'''
        expect = '''Program([ClassDecl(Id(_U),Id(_),[MethodDecl(Id($R45a),Static,[param(Id(t),StringType)],Block([],[])),MethodDecl(Id(__88),Instance,[param(Id(t__),FloatType),param(Id(g_AD8),FloatType),param(Id(_),ArrayType(65,ArrayType(9,BoolType))),param(Id(O____s__5),ArrayType(65,ArrayType(9,BoolType)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 158))

    def test_159(self):
        line = '''Class _{}Class r{}Class _{}Class S{Constructor (){Continue ;} }'''
        expect = '''Program([ClassDecl(Id(_),[]),ClassDecl(Id(r),[]),ClassDecl(Id(_),[]),ClassDecl(Id(S),[MethodDecl(Id(Constructor),Instance,[],Block([],[Continue]))])])'''
        self.assertTrue(TestAST.test(line, expect, 159))

    def test_160(self):
        line = '''Class W:_{$O_(N60c,s1:Array [Boolean ,0X9];J:Array [Int ,0X69];qB_t,T,_5,_,n2E4:Float ){} }'''
        expect = '''Program([ClassDecl(Id(W),Id(_),[MethodDecl(Id($O_),Static,[param(Id(N60c),ArrayType(9,BoolType)),param(Id(s1),ArrayType(9,BoolType)),param(Id(J),ArrayType(105,IntType)),param(Id(qB_t),FloatType),param(Id(T),FloatType),param(Id(_5),FloatType),param(Id(_),FloatType),param(Id(n2E4),FloatType)],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 160))

    def test_161(self):
        line = '''Class _:__{}Class R_5{}Class n_1:_{}Class U_d92E_{}Class u:R_{}'''
        expect = '''Program([ClassDecl(Id(_),Id(__),[]),ClassDecl(Id(R_5),[]),ClassDecl(Id(n_1),Id(_),[]),ClassDecl(Id(U_d92E_),[]),ClassDecl(Id(u),Id(R_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 161))

    def test_162(self):
        line = '''Class A:z{$W(_,_M:Gg6;p59__:Float ;_:_){Continue ;{} }}Class U:___u3{}'''
        expect = '''Program([ClassDecl(Id(A),Id(z),[MethodDecl(Id($W),Static,[param(Id(_),ClassType(Id(Gg6))),param(Id(_M),ClassType(Id(Gg6))),param(Id(p59__),FloatType),param(Id(_),ClassType(Id(_)))],Block([],[Continue,Block([],[])]))]),ClassDecl(Id(U),Id(___u3),[])])'''
        self.assertTrue(TestAST.test(line, expect, 162))

    def test_163(self):
        line = '''Class _:n___{Destructor (){Var _pZ7:Array [Array [Array [Array [Array [Int ,04],0xC],0b1],0x6],066];} }'''
        expect = '''Program([ClassDecl(Id(_),Id(n___),[MethodDecl(Id(Destructor),Instance,[],Block([VarDecl(Id(_pZ7),ArrayType(54,ArrayType(6,ArrayType(1,ArrayType(12,ArrayType(4,IntType))))))],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 163))

    def test_164(self):
        line = '''Class M____7_8{_l5(gD,k7,_,___5_:SWk_2;_,_,c:x){Continue ;Return ;} }'''
        expect = '''Program([ClassDecl(Id(M____7_8),[MethodDecl(Id(_l5),Instance,[param(Id(gD),ClassType(Id(SWk_2))),param(Id(k7),ClassType(Id(SWk_2))),param(Id(_),ClassType(Id(SWk_2))),param(Id(___5_),ClassType(Id(SWk_2))),param(Id(_),ClassType(Id(x))),param(Id(_),ClassType(Id(x))),param(Id(c),ClassType(Id(x)))],Block([],[Continue,Return(None)]))])])'''
        self.assertTrue(TestAST.test(line, expect, 164))

    def test_165(self):
        line = '''Class _7{Var $_2:Array [Array [Array [Float ,96],42],0X5E];}Class yYUZ_:E{}'''
        expect = '''Program([ClassDecl(Id(_7),[AttributeDecl(Static,VarDecl(Id($_2),ArrayType(94,ArrayType(42,ArrayType(96,FloatType)))))]),ClassDecl(Id(yYUZ_),Id(E),[])])'''
        self.assertTrue(TestAST.test(line, expect, 165))

    def test_166(self):
        line = '''Class ry{}Class _{Constructor (){}_1(_vL_71,_2:Array [Array [Array [Boolean ,0x7_9A_9],0b1_0_10_1],07]){} }Class _32{}'''
        expect = '''Program([ClassDecl(Id(ry),[]),ClassDecl(Id(_),[MethodDecl(Id(Constructor),Instance,[],Block([],[])),MethodDecl(Id(_1),Instance,[param(Id(_vL_71),ArrayType(7,ArrayType(21,ArrayType(31145,BoolType)))),param(Id(_2),ArrayType(7,ArrayType(21,ArrayType(31145,BoolType))))],Block([],[]))]),ClassDecl(Id(_32),[])])'''
        self.assertTrue(TestAST.test(line, expect, 166))

    def test_167(self):
        line = '''Class _E:AD{}Class __18N:_{}Class _{D6836(){Var O_8c,_,_O1,s_KRy5d_B_1,__:String ;} }'''
        expect = '''Program([ClassDecl(Id(_E),Id(AD),[]),ClassDecl(Id(__18N),Id(_),[]),ClassDecl(Id(_),[MethodDecl(Id(D6836),Instance,[],Block([VarDecl(Id(O_8c),StringType),VarDecl(Id(_),StringType),VarDecl(Id(_O1),StringType),VarDecl(Id(s_KRy5d_B_1),StringType),VarDecl(Id(__),StringType)],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 167))

    def test_168(self):
        line = '''Class z3__{}Class _{}Class _:__47{}Class G_2:o2ADH__8___R{}'''
        expect = '''Program([ClassDecl(Id(z3__),[]),ClassDecl(Id(_),[]),ClassDecl(Id(_),Id(__47),[]),ClassDecl(Id(G_2),Id(o2ADH__8___R),[])])'''
        self.assertTrue(TestAST.test(line, expect, 168))

    def test_169(self):
        line = '''Class _:z{Destructor (){New _9_()._()._.W();} }Class _Y{Var $8F,_J:Int ;}Class q:_{}'''
        expect = '''Program([ClassDecl(Id(_),Id(z),[MethodDecl(Id(Destructor),Instance,[],Block([],[Call(FieldAccess(CallExpr(NewExpr(Id(_9_),[]),Id(_),[]),Id(_)),Id(W),[])]))]),ClassDecl(Id(_Y),[AttributeDecl(Static,VarDecl(Id($8F),IntType)),AttributeDecl(Instance,VarDecl(Id(_J),IntType))]),ClassDecl(Id(q),Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 169))

    def test_170(self):
        line = '''Class g:__{}Class _:ZHa2{Constructor (){Var _,__,a:_;} }'''
        expect = '''Program([ClassDecl(Id(g),Id(__),[]),ClassDecl(Id(_),Id(ZHa2),[MethodDecl(Id(Constructor),Instance,[],Block([VarDecl(Id(_),ClassType(Id(_))),VarDecl(Id(__),ClassType(Id(_))),VarDecl(Id(a),ClassType(Id(_)))],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 170))

    def test_171(self):
        line = '''Class z_:K0I{}Class aVA:_{}Class z4_{Var _4_O788,$1,__5,__3:_;}Class _:__0{}'''
        expect = '''Program([ClassDecl(Id(z_),Id(K0I),[]),ClassDecl(Id(aVA),Id(_),[]),ClassDecl(Id(z4_),[AttributeDecl(Instance,VarDecl(Id(_4_O788),ClassType(Id(_)))),AttributeDecl(Static,VarDecl(Id($1),ClassType(Id(_)))),AttributeDecl(Instance,VarDecl(Id(__5),ClassType(Id(_)))),AttributeDecl(Instance,VarDecl(Id(__3),ClassType(Id(_))))]),ClassDecl(Id(_),Id(__0),[])])'''
        self.assertTrue(TestAST.test(line, expect, 171))

    def test_172(self):
        line = '''Class _{}Class H1{z(_:fu){}Var $x,$_,$3Y6:Array [Array [Array [String ,31_232],65],65];}Class l:w1{Destructor (){} }Class _{}'''
        expect = '''Program([ClassDecl(Id(_),[]),ClassDecl(Id(H1),[MethodDecl(Id(z),Instance,[param(Id(_),ClassType(Id(fu)))],Block([],[])),AttributeDecl(Static,VarDecl(Id($x),ArrayType(65,ArrayType(65,ArrayType(31232,StringType))))),AttributeDecl(Static,VarDecl(Id($_),ArrayType(65,ArrayType(65,ArrayType(31232,StringType))))),AttributeDecl(Static,VarDecl(Id($3Y6),ArrayType(65,ArrayType(65,ArrayType(31232,StringType)))))]),ClassDecl(Id(l),Id(w1),[MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 172))

    def test_173(self):
        line = '''Class _5:x6{Constructor (_,n:Float ;A:A){}Var $_,$_:Array [Array [Array [Boolean ,0b1_1],0x79_C],056];}'''
        expect = '''Program([ClassDecl(Id(_5),Id(x6),[MethodDecl(Id(Constructor),Instance,[param(Id(_),FloatType),param(Id(n),FloatType),param(Id(A),ClassType(Id(A)))],Block([],[])),AttributeDecl(Static,VarDecl(Id($_),ArrayType(46,ArrayType(1948,ArrayType(3,BoolType))))),AttributeDecl(Static,VarDecl(Id($_),ArrayType(46,ArrayType(1948,ArrayType(3,BoolType)))))])])'''
        self.assertTrue(TestAST.test(line, expect, 173))

    def test_174(self):
        line = '''Class dXm{}Class _:_{$_(){}_M(_:Float ;_8:Array [Array [Array [Array [Array [Array [Float ,0B1],4],6],0x1B],0X2A],06_7_61]){} }'''
        expect = '''Program([ClassDecl(Id(dXm),[]),ClassDecl(Id(_),Id(_),[MethodDecl(Id($_),Static,[],Block([],[])),MethodDecl(Id(_M),Instance,[param(Id(_),FloatType),param(Id(_8),ArrayType(3569,ArrayType(42,ArrayType(27,ArrayType(6,ArrayType(4,ArrayType(1,FloatType)))))))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 174))

    def test_175(self):
        line = '''Class I{Constructor (){}Var s_39,$_:Array [Array [Array [Array [Int ,5],0XB],0157],19];Destructor (){}$S(){} }Class P:D4G_{}'''
        expect = '''Program([ClassDecl(Id(I),[MethodDecl(Id(Constructor),Instance,[],Block([],[])),AttributeDecl(Instance,VarDecl(Id(s_39),ArrayType(19,ArrayType(111,ArrayType(11,ArrayType(5,IntType)))))),AttributeDecl(Static,VarDecl(Id($_),ArrayType(19,ArrayType(111,ArrayType(11,ArrayType(5,IntType)))))),MethodDecl(Id(Destructor),Instance,[],Block([],[])),MethodDecl(Id($S),Static,[],Block([],[]))]),ClassDecl(Id(P),Id(D4G_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 175))

    def test_176(self):
        line = '''Class _{Constructor (g__:Boolean ;I,_:Boolean ;P_,e6,g,i:_7v;_,B:String ;_:Int ;_,_,uV8,_:Int ){Continue ;{} }Constructor (){} }'''
        expect = '''Program([ClassDecl(Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(g__),BoolType),param(Id(I),BoolType),param(Id(_),BoolType),param(Id(P_),ClassType(Id(_7v))),param(Id(e6),ClassType(Id(_7v))),param(Id(g),ClassType(Id(_7v))),param(Id(i),ClassType(Id(_7v))),param(Id(_),StringType),param(Id(B),StringType),param(Id(_),IntType),param(Id(_),IntType),param(Id(_),IntType),param(Id(uV8),IntType),param(Id(_),IntType)],Block([],[Continue,Block([],[])])),MethodDecl(Id(Constructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 176))

    def test_177(self):
        line = '''Class _:Q{Constructor (_1W__,f,d,_1W_:t;n,f5,_:_;J0,__:Array [Float ,036];____:Int ;_d9:w;_,NM,f,F,Y:u;uG,x:Array [Array [Array [String ,58],0b1111],0x5]){} }'''
        expect = '''Program([ClassDecl(Id(_),Id(Q),[MethodDecl(Id(Constructor),Instance,[param(Id(_1W__),ClassType(Id(t))),param(Id(f),ClassType(Id(t))),param(Id(d),ClassType(Id(t))),param(Id(_1W_),ClassType(Id(t))),param(Id(n),ClassType(Id(_))),param(Id(f5),ClassType(Id(_))),param(Id(_),ClassType(Id(_))),param(Id(J0),ArrayType(30,FloatType)),param(Id(__),ArrayType(30,FloatType)),param(Id(____),IntType),param(Id(_d9),ClassType(Id(w))),param(Id(_),ClassType(Id(u))),param(Id(NM),ClassType(Id(u))),param(Id(f),ClassType(Id(u))),param(Id(F),ClassType(Id(u))),param(Id(Y),ClassType(Id(u))),param(Id(uG),ArrayType(5,ArrayType(15,ArrayType(58,StringType)))),param(Id(x),ArrayType(5,ArrayType(15,ArrayType(58,StringType))))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 177))

    def test_178(self):
        line = '''Class o_:a{$_2_9N(){Break ;}Var U,_:W;Var $J58:Array [String ,0x25];}Class __:_{}Class _:F{Destructor (){} }'''
        expect = '''Program([ClassDecl(Id(o_),Id(a),[MethodDecl(Id($_2_9N),Static,[],Block([],[Break])),AttributeDecl(Instance,VarDecl(Id(U),ClassType(Id(W)))),AttributeDecl(Instance,VarDecl(Id(_),ClassType(Id(W)))),AttributeDecl(Static,VarDecl(Id($J58),ArrayType(37,StringType)))]),ClassDecl(Id(__),Id(_),[]),ClassDecl(Id(_),Id(F),[MethodDecl(Id(Destructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 178))

    def test_179(self):
        line = '''Class z2:b{Constructor (){}Var _EjX,_,$W,$_G,s,_:Boolean ;}'''
        expect = '''Program([ClassDecl(Id(z2),Id(b),[MethodDecl(Id(Constructor),Instance,[],Block([],[])),AttributeDecl(Instance,VarDecl(Id(_EjX),BoolType)),AttributeDecl(Instance,VarDecl(Id(_),BoolType)),AttributeDecl(Static,VarDecl(Id($W),BoolType)),AttributeDecl(Static,VarDecl(Id($_G),BoolType)),AttributeDecl(Instance,VarDecl(Id(s),BoolType)),AttributeDecl(Instance,VarDecl(Id(_),BoolType))])])'''
        self.assertTrue(TestAST.test(line, expect, 179))

    def test_180(self):
        line = '''Class _:_{}Class _:_{Var G,__F,__:String ;}Class J4:Y_{}Class y{}'''
        expect = '''Program([ClassDecl(Id(_),Id(_),[]),ClassDecl(Id(_),Id(_),[AttributeDecl(Instance,VarDecl(Id(G),StringType)),AttributeDecl(Instance,VarDecl(Id(__F),StringType)),AttributeDecl(Instance,VarDecl(Id(__),StringType))]),ClassDecl(Id(J4),Id(Y_),[]),ClassDecl(Id(y),[])])'''
        self.assertTrue(TestAST.test(line, expect, 180))

    def test_181(self):
        line = '''Class f:_{}Class Z9_{}Class h0{_(_8,v:_;_:BW0_){} }Class FX:C_G5{Destructor (){} }Class _{}'''
        expect = '''Program([ClassDecl(Id(f),Id(_),[]),ClassDecl(Id(Z9_),[]),ClassDecl(Id(h0),[MethodDecl(Id(_),Instance,[param(Id(_8),ClassType(Id(_))),param(Id(v),ClassType(Id(_))),param(Id(_),ClassType(Id(BW0_)))],Block([],[]))]),ClassDecl(Id(FX),Id(C_G5),[MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 181))

    def test_182(self):
        line = '''Class __:b1{}Class _{}Class c77{}Class _G:_U{}Class L:_{}'''
        expect = '''Program([ClassDecl(Id(__),Id(b1),[]),ClassDecl(Id(_),[]),ClassDecl(Id(c77),[]),ClassDecl(Id(_G),Id(_U),[]),ClassDecl(Id(L),Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 182))

    def test_183(self):
        line = '''Class _9{}Class _:x_{Destructor (){Continue ;}Var $_20v,$_V:_A__b7f;}Class _:VD{}Class _Z{}'''
        expect = '''Program([ClassDecl(Id(_9),[]),ClassDecl(Id(_),Id(x_),[MethodDecl(Id(Destructor),Instance,[],Block([],[Continue])),AttributeDecl(Static,VarDecl(Id($_20v),ClassType(Id(_A__b7f)))),AttributeDecl(Static,VarDecl(Id($_V),ClassType(Id(_A__b7f))))]),ClassDecl(Id(_),Id(VD),[]),ClassDecl(Id(_Z),[])])'''
        self.assertTrue(TestAST.test(line, expect, 183))

    def test_184(self):
        line = '''Class _73_:N{}Class _1{Val Gg:Array [Boolean ,057]=-H::$33._;Destructor (){}Constructor (_,_,d,_,___:E;_:Array [Array [Array [Float ,01_1],0b1_1],87]){} }Class J3{Destructor (){Continue ;Break ;Var O:Array [Array [Int ,0X53],057];} }Class _yJJ1_{}'''
        expect = '''Program([ClassDecl(Id(_73_),Id(N),[]),ClassDecl(Id(_1),[AttributeDecl(Instance,ConstDecl(Id(Gg),ArrayType(47,BoolType),UnaryOp(-,FieldAccess(FieldAccess(Id(H),Id($33)),Id(_))))),MethodDecl(Id(Destructor),Instance,[],Block([],[])),MethodDecl(Id(Constructor),Instance,[param(Id(_),ClassType(Id(E))),param(Id(_),ClassType(Id(E))),param(Id(d),ClassType(Id(E))),param(Id(_),ClassType(Id(E))),param(Id(___),ClassType(Id(E))),param(Id(_),ArrayType(87,ArrayType(3,ArrayType(9,FloatType))))],Block([],[]))]),ClassDecl(Id(J3),[MethodDecl(Id(Destructor),Instance,[],Block([VarDecl(Id(O),ArrayType(47,ArrayType(83,IntType)))],[Continue,Break]))]),ClassDecl(Id(_yJJ1_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 184))

    def test_185(self):
        line = '''Class _:p{Var $7,$__:B;Destructor (){}Constructor (){} }Class s{}Class sZ_{}Class __{}Class _:G{}Class H_:X{}'''
        expect = '''Program([ClassDecl(Id(_),Id(p),[AttributeDecl(Static,VarDecl(Id($7),ClassType(Id(B)))),AttributeDecl(Static,VarDecl(Id($__),ClassType(Id(B)))),MethodDecl(Id(Destructor),Instance,[],Block([],[])),MethodDecl(Id(Constructor),Instance,[],Block([],[]))]),ClassDecl(Id(s),[]),ClassDecl(Id(sZ_),[]),ClassDecl(Id(__),[]),ClassDecl(Id(_),Id(G),[]),ClassDecl(Id(H_),Id(X),[])])'''
        self.assertTrue(TestAST.test(line, expect, 185))

    def test_186(self):
        line = '''Class _:_{}Class _6{_(V64:Array [Int ,0b1];O_eL6,f:Array [Int ,10];J:String ){}Destructor (){Var f2,c,__:String ;} }Class k_4{}'''
        expect = '''Program([ClassDecl(Id(_),Id(_),[]),ClassDecl(Id(_6),[MethodDecl(Id(_),Instance,[param(Id(V64),ArrayType(1,IntType)),param(Id(O_eL6),ArrayType(10,IntType)),param(Id(f),ArrayType(10,IntType)),param(Id(J),StringType)],Block([],[])),MethodDecl(Id(Destructor),Instance,[],Block([VarDecl(Id(f2),StringType),VarDecl(Id(c),StringType),VarDecl(Id(__),StringType)],[]))]),ClassDecl(Id(k_4),[])])'''
        self.assertTrue(TestAST.test(line, expect, 186))

    def test_187(self):
        line = '''Class _{O(_,s1:Array [Array [Float ,80],80];_:Array [Array [Array [Array [Array [Boolean ,0B1_0],0X6],0B101111],0xC_33],055_7];N:Float ;_:X__;_B:__){} }'''
        expect = '''Program([ClassDecl(Id(_),[MethodDecl(Id(O),Instance,[param(Id(_),ArrayType(80,ArrayType(80,FloatType))),param(Id(s1),ArrayType(80,ArrayType(80,FloatType))),param(Id(_),ArrayType(367,ArrayType(3123,ArrayType(47,ArrayType(6,ArrayType(2,BoolType)))))),param(Id(N),FloatType),param(Id(_),ClassType(Id(X__))),param(Id(_B),ClassType(Id(__)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 187))

    def test_188(self):
        line = '''Class _B{}Class _:z{}Class _:_0{}Class _:__1W{}Class _{}Class ___:R_1{}Class W_:w{}'''
        expect = '''Program([ClassDecl(Id(_B),[]),ClassDecl(Id(_),Id(z),[]),ClassDecl(Id(_),Id(_0),[]),ClassDecl(Id(_),Id(__1W),[]),ClassDecl(Id(_),[]),ClassDecl(Id(___),Id(R_1),[]),ClassDecl(Id(W_),Id(w),[])])'''
        self.assertTrue(TestAST.test(line, expect, 188))

    def test_189(self):
        line = '''Class Iw:BP{}Class n{Destructor (){}Destructor (){Break ;} }'''
        expect = '''Program([ClassDecl(Id(Iw),Id(BP),[]),ClassDecl(Id(n),[MethodDecl(Id(Destructor),Instance,[],Block([],[])),MethodDecl(Id(Destructor),Instance,[],Block([],[Break]))])])'''
        self.assertTrue(TestAST.test(line, expect, 189))

    def test_190(self):
        line = '''Class _{Destructor (){}Var $_:String ;Constructor (_,u:String ){} }'''
        expect = '''Program([ClassDecl(Id(_),[MethodDecl(Id(Destructor),Instance,[],Block([],[])),AttributeDecl(Static,VarDecl(Id($_),StringType)),MethodDecl(Id(Constructor),Instance,[param(Id(_),StringType),param(Id(u),StringType)],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 190))

    def test_191(self):
        line = '''Class C:_{__l_b(){}_D6(i1g,e,d_:Boolean ){Var f,m,__8:Int ;} }'''
        expect = '''Program([ClassDecl(Id(C),Id(_),[MethodDecl(Id(__l_b),Instance,[],Block([],[])),MethodDecl(Id(_D6),Instance,[param(Id(i1g),BoolType),param(Id(e),BoolType),param(Id(d_),BoolType)],Block([VarDecl(Id(f),IntType),VarDecl(Id(m),IntType),VarDecl(Id(__8),IntType)],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 191))

    def test_192(self):
        line = '''Class _{}Class _0{Constructor (_q8,_j_25,w,K6:Array [Array [Float ,0B1],0b100111];Ux,__:Array [Float ,3_4];_:Float ){} }Class Q3:_5__{}'''
        expect = '''Program([ClassDecl(Id(_),[]),ClassDecl(Id(_0),[MethodDecl(Id(Constructor),Instance,[param(Id(_q8),ArrayType(39,ArrayType(1,FloatType))),param(Id(_j_25),ArrayType(39,ArrayType(1,FloatType))),param(Id(w),ArrayType(39,ArrayType(1,FloatType))),param(Id(K6),ArrayType(39,ArrayType(1,FloatType))),param(Id(Ux),ArrayType(34,FloatType)),param(Id(__),ArrayType(34,FloatType)),param(Id(_),FloatType)],Block([],[]))]),ClassDecl(Id(Q3),Id(_5__),[])])'''
        self.assertTrue(TestAST.test(line, expect, 192))

    def test_193(self):
        line = '''Class E53_N{}Class _7{$Z(ls,a1,_,hk,U,_,_V:Array [Array [Float ,021],0B1011111];J__M_,_:b9;_:u){} }Class _O{}'''
        expect = '''Program([ClassDecl(Id(E53_N),[]),ClassDecl(Id(_7),[MethodDecl(Id($Z),Static,[param(Id(ls),ArrayType(95,ArrayType(17,FloatType))),param(Id(a1),ArrayType(95,ArrayType(17,FloatType))),param(Id(_),ArrayType(95,ArrayType(17,FloatType))),param(Id(hk),ArrayType(95,ArrayType(17,FloatType))),param(Id(U),ArrayType(95,ArrayType(17,FloatType))),param(Id(_),ArrayType(95,ArrayType(17,FloatType))),param(Id(_V),ArrayType(95,ArrayType(17,FloatType))),param(Id(J__M_),ClassType(Id(b9))),param(Id(_),ClassType(Id(b9))),param(Id(_),ClassType(Id(u)))],Block([],[]))]),ClassDecl(Id(_O),[])])'''
        self.assertTrue(TestAST.test(line, expect, 193))

    def test_194(self):
        line = '''Class _76_:_58{Constructor (){}Var bK:Array [Boolean ,0B100010];Var $G:Array [Array [Int ,0x51],41];}'''
        expect = '''Program([ClassDecl(Id(_76_),Id(_58),[MethodDecl(Id(Constructor),Instance,[],Block([],[])),AttributeDecl(Instance,VarDecl(Id(bK),ArrayType(34,BoolType))),AttributeDecl(Static,VarDecl(Id($G),ArrayType(41,ArrayType(81,IntType))))])])'''
        self.assertTrue(TestAST.test(line, expect, 194))

    def test_195(self):
        line = '''Class _:__{Var _,$6:_4;$_(J_:Array [String ,5];__:String ;_:Boolean ){Break ;}Constructor (_pP___v:Array [Int ,5];_8:String ;____,p2:String ;_,_:Array [Boolean ,5]){} }Class u_:__3{}'''
        expect = '''Program([ClassDecl(Id(_),Id(__),[AttributeDecl(Instance,VarDecl(Id(_),ClassType(Id(_4)))),AttributeDecl(Static,VarDecl(Id($6),ClassType(Id(_4)))),MethodDecl(Id($_),Static,[param(Id(J_),ArrayType(5,StringType)),param(Id(__),StringType),param(Id(_),BoolType)],Block([],[Break])),MethodDecl(Id(Constructor),Instance,[param(Id(_pP___v),ArrayType(5,IntType)),param(Id(_8),StringType),param(Id(____),StringType),param(Id(p2),StringType),param(Id(_),ArrayType(5,BoolType)),param(Id(_),ArrayType(5,BoolType))],Block([],[]))]),ClassDecl(Id(u_),Id(__3),[])])'''
        self.assertTrue(TestAST.test(line, expect, 195))

    def test_196(self):
        line = '''Class H:_{Constructor (_p0:Int ;__,_:Boolean ){} }Class T9_:cW4l{$n(L_a8:Array [Array [Array [Float ,0X51],013],0B1]){Break ;}Constructor (){} }'''
        expect = '''Program([ClassDecl(Id(H),Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(_p0),IntType),param(Id(__),BoolType),param(Id(_),BoolType)],Block([],[]))]),ClassDecl(Id(T9_),Id(cW4l),[MethodDecl(Id($n),Static,[param(Id(L_a8),ArrayType(1,ArrayType(11,ArrayType(81,FloatType))))],Block([],[Break])),MethodDecl(Id(Constructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 196))

    def test_197(self):
        line = '''Class V{}Class _{}Class X:P_C{}Class _37{}Class _{Destructor (){} }'''
        expect = '''Program([ClassDecl(Id(V),[]),ClassDecl(Id(_),[]),ClassDecl(Id(X),Id(P_C),[]),ClassDecl(Id(_37),[]),ClassDecl(Id(_),[MethodDecl(Id(Destructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 197))

    def test_198(self):
        line = '''Class _{}Class _Ewzf:_{}Class R{__9_(){} }Class _Q{}Class _C_Q_:_3{}Class c{}Class _:_c{}Class H{}'''
        expect = '''Program([ClassDecl(Id(_),[]),ClassDecl(Id(_Ewzf),Id(_),[]),ClassDecl(Id(R),[MethodDecl(Id(__9_),Instance,[],Block([],[]))]),ClassDecl(Id(_Q),[]),ClassDecl(Id(_C_Q_),Id(_3),[]),ClassDecl(Id(c),[]),ClassDecl(Id(_),Id(_c),[]),ClassDecl(Id(H),[])])'''
        self.assertTrue(TestAST.test(line, expect, 198))

    def test_199(self):
        line = '''Class V:N84{}Class _:_{}Class _{Var $u:String ;}Class _:__DH_{}Class _063{}'''
        expect = '''Program([ClassDecl(Id(V),Id(N84),[]),ClassDecl(Id(_),Id(_),[]),ClassDecl(Id(_),[AttributeDecl(Static,VarDecl(Id($u),StringType))]),ClassDecl(Id(_),Id(__DH_),[]),ClassDecl(Id(_063),[])])'''
        self.assertTrue(TestAST.test(line, expect, 199))

    def test_200(self):
        line = '''Class F_{Constructor (){}Var _,$yB:Array [Array [Array [Float ,79],0B1],0xC_9];}'''
        expect = '''Program([ClassDecl(Id(F_),[MethodDecl(Id(Constructor),Instance,[],Block([],[])),AttributeDecl(Instance,VarDecl(Id(_),ArrayType(201,ArrayType(1,ArrayType(79,FloatType))))),AttributeDecl(Static,VarDecl(Id($yB),ArrayType(201,ArrayType(1,ArrayType(79,FloatType)))))])])'''
        self.assertTrue(TestAST.test(line, expect, 200))

    def test_201(self):
        line = '''Class _3{Var $1oHw,$_,_b7Z_8xQ:Array [Boolean ,023];}Class _U:R{}'''
        expect = '''Program([ClassDecl(Id(_3),[AttributeDecl(Static,VarDecl(Id($1oHw),ArrayType(19,BoolType))),AttributeDecl(Static,VarDecl(Id($_),ArrayType(19,BoolType))),AttributeDecl(Instance,VarDecl(Id(_b7Z_8xQ),ArrayType(19,BoolType)))]),ClassDecl(Id(_U),Id(R),[])])'''
        self.assertTrue(TestAST.test(line, expect, 201))

    def test_202(self):
        line = '''Class _{Constructor (_:__5F){Continue ;}Var u_,_:Array [Array [Array [Array [Int ,3],46],46],0124];}'''
        expect = '''Program([ClassDecl(Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(_),ClassType(Id(__5F)))],Block([],[Continue])),AttributeDecl(Instance,VarDecl(Id(u_),ArrayType(84,ArrayType(46,ArrayType(46,ArrayType(3,IntType)))))),AttributeDecl(Instance,VarDecl(Id(_),ArrayType(84,ArrayType(46,ArrayType(46,ArrayType(3,IntType))))))])])'''
        self.assertTrue(TestAST.test(line, expect, 202))

    def test_203(self):
        line = '''Class _{}Class _:_{w(){Continue ;}a8(){}Destructor (){}Constructor (_,j2:c_;G,o:G){Break ;Return ;}Var $_:Array [Array [Array [Int ,5],4_3],0X43];}'''
        expect = '''Program([ClassDecl(Id(_),[]),ClassDecl(Id(_),Id(_),[MethodDecl(Id(w),Instance,[],Block([],[Continue])),MethodDecl(Id(a8),Instance,[],Block([],[])),MethodDecl(Id(Destructor),Instance,[],Block([],[])),MethodDecl(Id(Constructor),Instance,[param(Id(_),ClassType(Id(c_))),param(Id(j2),ClassType(Id(c_))),param(Id(G),ClassType(Id(G))),param(Id(o),ClassType(Id(G)))],Block([],[Break,Return(None)])),AttributeDecl(Static,VarDecl(Id($_),ArrayType(67,ArrayType(43,ArrayType(5,IntType)))))])])'''
        self.assertTrue(TestAST.test(line, expect, 203))

    def test_204(self):
        line = '''Class _N6:_{Destructor (){Var _I:_5_;} }Class _hz743:S__k{}'''
        expect = '''Program([ClassDecl(Id(_N6),Id(_),[MethodDecl(Id(Destructor),Instance,[],Block([VarDecl(Id(_I),ClassType(Id(_5_)))],[]))]),ClassDecl(Id(_hz743),Id(S__k),[])])'''
        self.assertTrue(TestAST.test(line, expect, 204))

    def test_205(self):
        line = '''Class q:_{$_n9_(_50c,p,m:_35;d__:Array [Int ,17];_v:Array [String ,22];Y_9__d,__:Array [Boolean ,0b10]){} }'''
        expect = '''Program([ClassDecl(Id(q),Id(_),[MethodDecl(Id($_n9_),Static,[param(Id(_50c),ClassType(Id(_35))),param(Id(p),ClassType(Id(_35))),param(Id(m),ClassType(Id(_35))),param(Id(d__),ArrayType(17,IntType)),param(Id(_v),ArrayType(22,StringType)),param(Id(Y_9__d),ArrayType(2,BoolType)),param(Id(__),ArrayType(2,BoolType))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 205))

    def test_206(self):
        line = '''Class _{Destructor (){} }Class va{Var $_,d_,$7__:Array [Int ,05_7];}'''
        expect = '''Program([ClassDecl(Id(_),[MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(va),[AttributeDecl(Static,VarDecl(Id($_),ArrayType(47,IntType))),AttributeDecl(Instance,VarDecl(Id(d_),ArrayType(47,IntType))),AttributeDecl(Static,VarDecl(Id($7__),ArrayType(47,IntType)))])])'''
        self.assertTrue(TestAST.test(line, expect, 206))

    def test_207(self):
        line = '''Class __t:_R{}Class _:w{}Class _807{}Class V{}Class __{Var sMd:_;Constructor (k:h){}Destructor (){} }Class K:c_{}'''
        expect = '''Program([ClassDecl(Id(__t),Id(_R),[]),ClassDecl(Id(_),Id(w),[]),ClassDecl(Id(_807),[]),ClassDecl(Id(V),[]),ClassDecl(Id(__),[AttributeDecl(Instance,VarDecl(Id(sMd),ClassType(Id(_)))),MethodDecl(Id(Constructor),Instance,[param(Id(k),ClassType(Id(h)))],Block([],[])),MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(K),Id(c_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 207))

    def test_208(self):
        line = '''Class _:_u{Destructor (){} }Class b_{}Class c0{Constructor (){}Destructor (){ {} }}Class _l{}'''
        expect = '''Program([ClassDecl(Id(_),Id(_u),[MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(b_),[]),ClassDecl(Id(c0),[MethodDecl(Id(Constructor),Instance,[],Block([],[])),MethodDecl(Id(Destructor),Instance,[],Block([],[Block([],[])]))]),ClassDecl(Id(_l),[])])'''
        self.assertTrue(TestAST.test(line, expect, 208))

    def test_209(self):
        line = '''Class _:_{Constructor (E_,A,_,_:x;r,_x4__:String ){Continue ;}Var _q:_;}'''
        expect = '''Program([ClassDecl(Id(_),Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(E_),ClassType(Id(x))),param(Id(A),ClassType(Id(x))),param(Id(_),ClassType(Id(x))),param(Id(_),ClassType(Id(x))),param(Id(r),StringType),param(Id(_x4__),StringType)],Block([],[Continue])),AttributeDecl(Instance,VarDecl(Id(_q),ClassType(Id(_))))])])'''
        self.assertTrue(TestAST.test(line, expect, 209))

    def test_210(self):
        line = '''Class _:_{}Class w{Var $3_:String ;Constructor (){} }Class __{j(___5:Array [Array [Array [Array [Float ,26_5],0102],4_0],0X5A];k7:__;__,Io,__,_E:Float ;_f6_:Array [Int ,0102]){ {} }}'''
        expect = '''Program([ClassDecl(Id(_),Id(_),[]),ClassDecl(Id(w),[AttributeDecl(Static,VarDecl(Id($3_),StringType)),MethodDecl(Id(Constructor),Instance,[],Block([],[]))]),ClassDecl(Id(__),[MethodDecl(Id(j),Instance,[param(Id(___5),ArrayType(90,ArrayType(40,ArrayType(66,ArrayType(265,FloatType))))),param(Id(k7),ClassType(Id(__))),param(Id(__),FloatType),param(Id(Io),FloatType),param(Id(__),FloatType),param(Id(_E),FloatType),param(Id(_f6_),ArrayType(66,IntType))],Block([],[Block([],[])]))])])'''
        self.assertTrue(TestAST.test(line, expect, 210))

    def test_211(self):
        line = '''Class _{}Class r__76m_0q{_v_38_K9(M_2_:Array [Array [Array [Boolean ,0101],0X32],684_05];__02:_){} }Class _:n{Var R:T5;}Class _:Z4{Constructor (_:Float ){} }'''
        expect = '''Program([ClassDecl(Id(_),[]),ClassDecl(Id(r__76m_0q),[MethodDecl(Id(_v_38_K9),Instance,[param(Id(M_2_),ArrayType(68405,ArrayType(50,ArrayType(65,BoolType)))),param(Id(__02),ClassType(Id(_)))],Block([],[]))]),ClassDecl(Id(_),Id(n),[AttributeDecl(Instance,VarDecl(Id(R),ClassType(Id(T5))))]),ClassDecl(Id(_),Id(Z4),[MethodDecl(Id(Constructor),Instance,[param(Id(_),FloatType)],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 211))

    def test_212(self):
        line = '''Class O:_{Constructor (__9__h:Array [Int ,0B1]){Return ;Var vJ3,L_0,_G8:_;}Var $_:String ;}'''
        expect = '''Program([ClassDecl(Id(O),Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(__9__h),ArrayType(1,IntType))],Block([VarDecl(Id(vJ3),ClassType(Id(_))),VarDecl(Id(L_0),ClassType(Id(_))),VarDecl(Id(_G8),ClassType(Id(_)))],[Return(None)])),AttributeDecl(Static,VarDecl(Id($_),StringType))])])'''
        self.assertTrue(TestAST.test(line, expect, 212))

    def test_213(self):
        line = '''Class _{$2(__,__76f,_:Array [Array [Array [String ,61],0x1],0x2];_C5g_,L5,RkQ:Array [Boolean ,0b1];__,e:Array [Array [Boolean ,0x21],0xE];_,_,_1S58:Boolean ;_k:Array [Boolean ,05];y_:C;i___:Array [Array [Float ,0B111001],3]){} }'''
        expect = '''Program([ClassDecl(Id(_),[MethodDecl(Id($2),Static,[param(Id(__),ArrayType(2,ArrayType(1,ArrayType(61,StringType)))),param(Id(__76f),ArrayType(2,ArrayType(1,ArrayType(61,StringType)))),param(Id(_),ArrayType(2,ArrayType(1,ArrayType(61,StringType)))),param(Id(_C5g_),ArrayType(1,BoolType)),param(Id(L5),ArrayType(1,BoolType)),param(Id(RkQ),ArrayType(1,BoolType)),param(Id(__),ArrayType(14,ArrayType(33,BoolType))),param(Id(e),ArrayType(14,ArrayType(33,BoolType))),param(Id(_),BoolType),param(Id(_),BoolType),param(Id(_1S58),BoolType),param(Id(_k),ArrayType(5,BoolType)),param(Id(y_),ClassType(Id(C))),param(Id(i___),ArrayType(3,ArrayType(57,FloatType)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 213))

    def test_214(self):
        line = '''Class __:w{}Class __{Destructor (){Continue ;Break ;}$W(){} }'''
        expect = '''Program([ClassDecl(Id(__),Id(w),[]),ClassDecl(Id(__),[MethodDecl(Id(Destructor),Instance,[],Block([],[Continue,Break])),MethodDecl(Id($W),Static,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 214))

    def test_215(self):
        line = '''Class _{Constructor (__:o;j:_){} }Class W:_{}Class _{Constructor (t,_2:Array [Array [String ,0B1011001],0x179_27_A17_B]){} }'''
        expect = '''Program([ClassDecl(Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(__),ClassType(Id(o))),param(Id(j),ClassType(Id(_)))],Block([],[]))]),ClassDecl(Id(W),Id(_),[]),ClassDecl(Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(t),ArrayType(6327607675,ArrayType(89,StringType))),param(Id(_2),ArrayType(6327607675,ArrayType(89,StringType)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 215))

    def test_216(self):
        line = '''Class ga_{}Class ___:P_{}Class feo_{}Class d{}Class _s8:_{}'''
        expect = '''Program([ClassDecl(Id(ga_),[]),ClassDecl(Id(___),Id(P_),[]),ClassDecl(Id(feo_),[]),ClassDecl(Id(d),[]),ClassDecl(Id(_s8),Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 216))

    def test_217(self):
        line = '''Class _{}Class _dN:s{$_7kJ8_9_(_0,_,f37,_:Array [String ,0x55];z:Int ;W_65_,B71,A:P){} }'''
        expect = '''Program([ClassDecl(Id(_),[]),ClassDecl(Id(_dN),Id(s),[MethodDecl(Id($_7kJ8_9_),Static,[param(Id(_0),ArrayType(85,StringType)),param(Id(_),ArrayType(85,StringType)),param(Id(f37),ArrayType(85,StringType)),param(Id(_),ArrayType(85,StringType)),param(Id(z),IntType),param(Id(W_65_),ClassType(Id(P))),param(Id(B71),ClassType(Id(P))),param(Id(A),ClassType(Id(P)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 217))

    def test_218(self):
        line = '''Class _{}Class x:_{Constructor (O,_Km:Array [Array [Array [Array [Array [String ,0x63],0x2E0_F],0B100],0xA],60]){} }'''
        expect = '''Program([ClassDecl(Id(_),[]),ClassDecl(Id(x),Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(O),ArrayType(60,ArrayType(10,ArrayType(4,ArrayType(11791,ArrayType(99,StringType)))))),param(Id(_Km),ArrayType(60,ArrayType(10,ArrayType(4,ArrayType(11791,ArrayType(99,StringType))))))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 218))

    def test_219(self):
        line = '''Class _7E:_X2{Constructor (d_:Int ){} }Class _:e{Var O,l:__;}Class k7:r6{Var $L:Float ;}Class h:r_{}'''
        expect = '''Program([ClassDecl(Id(_7E),Id(_X2),[MethodDecl(Id(Constructor),Instance,[param(Id(d_),IntType)],Block([],[]))]),ClassDecl(Id(_),Id(e),[AttributeDecl(Instance,VarDecl(Id(O),ClassType(Id(__)))),AttributeDecl(Instance,VarDecl(Id(l),ClassType(Id(__))))]),ClassDecl(Id(k7),Id(r6),[AttributeDecl(Static,VarDecl(Id($L),FloatType))]),ClassDecl(Id(h),Id(r_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 219))

    def test_220(self):
        line = '''Class B8_D:X{}Class _3:_5{}Class _{Destructor (){}Destructor (){} }'''
        expect = '''Program([ClassDecl(Id(B8_D),Id(X),[]),ClassDecl(Id(_3),Id(_5),[]),ClassDecl(Id(_),[MethodDecl(Id(Destructor),Instance,[],Block([],[])),MethodDecl(Id(Destructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 220))

    def test_221(self):
        line = '''Class _4{$i_(fg,_3:Array [Array [Array [Array [Array [Array [String ,0x7],0X3],077],0x1C],0X2_62],06];j8,_:Array [String ,0132]){} }Class ir{}Class u:_3{}'''
        expect = '''Program([ClassDecl(Id(_4),[MethodDecl(Id($i_),Static,[param(Id(fg),ArrayType(6,ArrayType(610,ArrayType(28,ArrayType(63,ArrayType(3,ArrayType(7,StringType))))))),param(Id(_3),ArrayType(6,ArrayType(610,ArrayType(28,ArrayType(63,ArrayType(3,ArrayType(7,StringType))))))),param(Id(j8),ArrayType(90,StringType)),param(Id(_),ArrayType(90,StringType))],Block([],[]))]),ClassDecl(Id(ir),[]),ClassDecl(Id(u),Id(_3),[])])'''
        self.assertTrue(TestAST.test(line, expect, 221))

    def test_222(self):
        line = '''Class _{}Class _5_:D3_{}Class bJ31g0_:p{}Class ___Yf{}Class R_{}'''
        expect = '''Program([ClassDecl(Id(_),[]),ClassDecl(Id(_5_),Id(D3_),[]),ClassDecl(Id(bJ31g0_),Id(p),[]),ClassDecl(Id(___Yf),[]),ClassDecl(Id(R_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 222))

    def test_223(self):
        line = '''Class j2{Var _,$_,$0:Array [Array [Array [Array [String ,6],045],82],0b1001101];}'''
        expect = '''Program([ClassDecl(Id(j2),[AttributeDecl(Instance,VarDecl(Id(_),ArrayType(77,ArrayType(82,ArrayType(37,ArrayType(6,StringType)))))),AttributeDecl(Static,VarDecl(Id($_),ArrayType(77,ArrayType(82,ArrayType(37,ArrayType(6,StringType)))))),AttributeDecl(Static,VarDecl(Id($0),ArrayType(77,ArrayType(82,ArrayType(37,ArrayType(6,StringType))))))])])'''
        self.assertTrue(TestAST.test(line, expect, 223))

    def test_224(self):
        line = '''Class r_{}Class A{}Class __:pV{}Class h{}Class y{}Class _5_{}'''
        expect = '''Program([ClassDecl(Id(r_),[]),ClassDecl(Id(A),[]),ClassDecl(Id(__),Id(pV),[]),ClassDecl(Id(h),[]),ClassDecl(Id(y),[]),ClassDecl(Id(_5_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 224))

    def test_225(self):
        line = '''Class _w_:D{Constructor (_L_pW1xk:String ;Lm,_dX:r1){} }'''
        expect = '''Program([ClassDecl(Id(_w_),Id(D),[MethodDecl(Id(Constructor),Instance,[param(Id(_L_pW1xk),StringType),param(Id(Lm),ClassType(Id(r1))),param(Id(_dX),ClassType(Id(r1)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 225))

    def test_226(self):
        line = '''Class __{Var O:Array [Float ,0X25];}Class hk_:_{}Class T{Var __,x:Boolean ;}'''
        expect = '''Program([ClassDecl(Id(__),[AttributeDecl(Instance,VarDecl(Id(O),ArrayType(37,FloatType)))]),ClassDecl(Id(hk_),Id(_),[]),ClassDecl(Id(T),[AttributeDecl(Instance,VarDecl(Id(__),BoolType)),AttributeDecl(Instance,VarDecl(Id(x),BoolType))])])'''
        self.assertTrue(TestAST.test(line, expect, 226))

    def test_227(self):
        line = '''Class M{Constructor (__,Y,_,__,_,_,N:Array [Array [String ,86],051]){}Var $_0:String ;}Class RUZ:_{}Class _{}Class _:_{Destructor (){Break ;}$K(){} }Class _8{}'''
        expect = '''Program([ClassDecl(Id(M),[MethodDecl(Id(Constructor),Instance,[param(Id(__),ArrayType(41,ArrayType(86,StringType))),param(Id(Y),ArrayType(41,ArrayType(86,StringType))),param(Id(_),ArrayType(41,ArrayType(86,StringType))),param(Id(__),ArrayType(41,ArrayType(86,StringType))),param(Id(_),ArrayType(41,ArrayType(86,StringType))),param(Id(_),ArrayType(41,ArrayType(86,StringType))),param(Id(N),ArrayType(41,ArrayType(86,StringType)))],Block([],[])),AttributeDecl(Static,VarDecl(Id($_0),StringType))]),ClassDecl(Id(RUZ),Id(_),[]),ClassDecl(Id(_),[]),ClassDecl(Id(_),Id(_),[MethodDecl(Id(Destructor),Instance,[],Block([],[Break])),MethodDecl(Id($K),Static,[],Block([],[]))]),ClassDecl(Id(_8),[])])'''
        self.assertTrue(TestAST.test(line, expect, 227))

    def test_228(self):
        line = '''Class r_JR_{H_(w__o,__,_D9:_;_pR_776:Float ){_::$__.tI_.___();} }Class q{}Class _2____43:_1{}'''
        expect = '''Program([ClassDecl(Id(r_JR_),[MethodDecl(Id(H_),Instance,[param(Id(w__o),ClassType(Id(_))),param(Id(__),ClassType(Id(_))),param(Id(_D9),ClassType(Id(_))),param(Id(_pR_776),FloatType)],Block([],[Call(FieldAccess(FieldAccess(Id(_),Id($__)),Id(tI_)),Id(___),[])]))]),ClassDecl(Id(q),[]),ClassDecl(Id(_2____43),Id(_1),[])])'''
        self.assertTrue(TestAST.test(line, expect, 228))

    def test_229(self):
        line = '''Class N:N{$_(){ei_::$_();Continue ;Continue ;}Var $_,d,$8Z,i_h_:Array [Float ,035];}'''
        expect = '''Program([ClassDecl(Id(N),Id(N),[MethodDecl(Id($_),Static,[],Block([],[Call(Id(ei_),Id($_),[]),Continue,Continue])),AttributeDecl(Static,VarDecl(Id($_),ArrayType(29,FloatType))),AttributeDecl(Instance,VarDecl(Id(d),ArrayType(29,FloatType))),AttributeDecl(Static,VarDecl(Id($8Z),ArrayType(29,FloatType))),AttributeDecl(Instance,VarDecl(Id(i_h_),ArrayType(29,FloatType)))])])'''
        self.assertTrue(TestAST.test(line, expect, 229))

    def test_230(self):
        line = '''Class e_q:_{}Class h_{}Class V4:z_{}Class _0:_{$T6(){ {}Break ;} }Class b{}'''
        expect = '''Program([ClassDecl(Id(e_q),Id(_),[]),ClassDecl(Id(h_),[]),ClassDecl(Id(V4),Id(z_),[]),ClassDecl(Id(_0),Id(_),[MethodDecl(Id($T6),Static,[],Block([],[Block([],[]),Break]))]),ClassDecl(Id(b),[])])'''
        self.assertTrue(TestAST.test(line, expect, 230))

    def test_231(self):
        line = '''Class T_tR:lO_{}Class _{}Class a{Var __,____M1:Array [Array [Boolean ,0x8],0X26];}Class __m{Var $l:Float ;}'''
        expect = '''Program([ClassDecl(Id(T_tR),Id(lO_),[]),ClassDecl(Id(_),[]),ClassDecl(Id(a),[AttributeDecl(Instance,VarDecl(Id(__),ArrayType(38,ArrayType(8,BoolType)))),AttributeDecl(Instance,VarDecl(Id(____M1),ArrayType(38,ArrayType(8,BoolType))))]),ClassDecl(Id(__m),[AttributeDecl(Static,VarDecl(Id($l),FloatType))])])'''
        self.assertTrue(TestAST.test(line, expect, 231))

    def test_232(self):
        line = '''Class y:E{$7(_0,_7:Float ;m_20,N80,__9:Array [Array [Int ,0x3],21];g,YC,_:String ){} }'''
        expect = '''Program([ClassDecl(Id(y),Id(E),[MethodDecl(Id($7),Static,[param(Id(_0),FloatType),param(Id(_7),FloatType),param(Id(m_20),ArrayType(21,ArrayType(3,IntType))),param(Id(N80),ArrayType(21,ArrayType(3,IntType))),param(Id(__9),ArrayType(21,ArrayType(3,IntType))),param(Id(g),StringType),param(Id(YC),StringType),param(Id(_),StringType)],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 232))

    def test_233(self):
        line = '''Class R:_{}Class _8_:_B{}Class _:_4{Var $b:Array [String ,0B1]=!-Self ;}'''
        expect = '''Program([ClassDecl(Id(R),Id(_),[]),ClassDecl(Id(_8_),Id(_B),[]),ClassDecl(Id(_),Id(_4),[AttributeDecl(Static,VarDecl(Id($7__),ArrayType(1,StringType),UnaryOp(!,UnaryOp(-,Self()))))])])'''
        self.assertTrue(TestAST.test(line, expect, 233))

    def test_234(self):
        line = '''Class r__:_{Constructor (_n:Array [Array [Int ,043],0x50];__,_,_:_;_e,ir,_:y;_,___:Float ){Return ;} }'''
        expect = '''Program([ClassDecl(Id(r__),Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(_n),ArrayType(80,ArrayType(35,IntType))),param(Id(__),ClassType(Id(_))),param(Id(_),ClassType(Id(_))),param(Id(_),ClassType(Id(_))),param(Id(_e),ClassType(Id(y))),param(Id(ir),ClassType(Id(y))),param(Id(_),ClassType(Id(y))),param(Id(_),FloatType),param(Id(___),FloatType)],Block([],[Return(None)]))])])'''
        self.assertTrue(TestAST.test(line, expect, 234))

    def test_235(self):
        line = '''Class __{Destructor (){}Constructor (){} }Class __:_8G_{}'''
        expect = '''Program([ClassDecl(Id(__),[MethodDecl(Id(Destructor),Instance,[],Block([],[])),MethodDecl(Id(Constructor),Instance,[],Block([],[]))]),ClassDecl(Id(__),Id(_8G_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 235))

    def test_236(self):
        line = '''Class B{Constructor (___3U_:D_){_::$9._4().__84.pc.__();} }'''
        expect = '''Program([ClassDecl(Id(B),[MethodDecl(Id(Constructor),Instance,[param(Id(___3U_),ClassType(Id(D_)))],Block([],[Call(FieldAccess(FieldAccess(CallExpr(FieldAccess(Id(_),Id($9)),Id(_4),[]),Id(__84)),Id(pc)),Id(__),[])]))])])'''
        self.assertTrue(TestAST.test(line, expect, 236))

    def test_237(self):
        line = '''Class nB9_{}Class B4g:Fnh5{}Class __{}Class g{Constructor (){} }'''
        expect = '''Program([ClassDecl(Id(nB9_),[]),ClassDecl(Id(B4g),Id(Fnh5),[]),ClassDecl(Id(__),[]),ClassDecl(Id(g),[MethodDecl(Id(Constructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 237))

    def test_238(self):
        line = '''Class q{Constructor (v:Array [Int ,0b1111]){}Constructor (n,_1__:Array [Array [Int ,9_1_360],0xB];_8jg:Int ;_,e,_u__,_,z:W_){} }'''
        expect = '''Program([ClassDecl(Id(q),[MethodDecl(Id(Constructor),Instance,[param(Id(v),ArrayType(15,IntType))],Block([],[])),MethodDecl(Id(Constructor),Instance,[param(Id(n),ArrayType(11,ArrayType(91360,IntType))),param(Id(_1__),ArrayType(11,ArrayType(91360,IntType))),param(Id(_8jg),IntType),param(Id(_),ClassType(Id(W_))),param(Id(e),ClassType(Id(W_))),param(Id(_u__),ClassType(Id(W_))),param(Id(_),ClassType(Id(W_))),param(Id(z),ClassType(Id(W_)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 238))

    def test_239(self):
        line = '''Class F4g9{}Class _:N8{Var $0,$s__,$X_,$__,$_0:Array [Float ,0142];}'''
        expect = '''Program([ClassDecl(Id(F4g9),[]),ClassDecl(Id(_),Id(N8),[AttributeDecl(Static,VarDecl(Id($0),ArrayType(98,FloatType))),AttributeDecl(Static,VarDecl(Id($s__),ArrayType(98,FloatType))),AttributeDecl(Static,VarDecl(Id($X_),ArrayType(98,FloatType))),AttributeDecl(Static,VarDecl(Id($__),ArrayType(98,FloatType))),AttributeDecl(Static,VarDecl(Id($_0),ArrayType(98,FloatType)))])])'''
        self.assertTrue(TestAST.test(line, expect, 239))

    def test_240(self):
        line = '''Class _:_{Constructor (){}Var n,_,$3_,$3__,$7,$_m,b_,$3,$B1:_;Var e:Array [Int ,06_2_3];}Class t5_3M_5{}'''
        expect = '''Program([ClassDecl(Id(_),Id(_),[MethodDecl(Id(Constructor),Instance,[],Block([],[])),AttributeDecl(Instance,VarDecl(Id(n),ClassType(Id(_)))),AttributeDecl(Instance,VarDecl(Id(_),ClassType(Id(_)))),AttributeDecl(Static,VarDecl(Id($3_),ClassType(Id(_)))),AttributeDecl(Static,VarDecl(Id($3__),ClassType(Id(_)))),AttributeDecl(Static,VarDecl(Id($7),ClassType(Id(_)))),AttributeDecl(Static,VarDecl(Id($_m),ClassType(Id(_)))),AttributeDecl(Instance,VarDecl(Id(b_),ClassType(Id(_)))),AttributeDecl(Static,VarDecl(Id($3),ClassType(Id(_)))),AttributeDecl(Static,VarDecl(Id($B1),ClassType(Id(_)))),AttributeDecl(Instance,VarDecl(Id(e),ArrayType(403,IntType)))]),ClassDecl(Id(t5_3M_5),[])])'''
        self.assertTrue(TestAST.test(line, expect, 240))

    def test_241(self):
        line = '''Class _s5_{}Class h_ga:k{}Class O0_:W_S5{Destructor (){Continue ;} }'''
        expect = '''Program([ClassDecl(Id(_s5_),[]),ClassDecl(Id(h_ga),Id(k),[]),ClassDecl(Id(O0_),Id(W_S5),[MethodDecl(Id(Destructor),Instance,[],Block([],[Continue]))])])'''
        self.assertTrue(TestAST.test(line, expect, 241))

    def test_242(self):
        line = '''Class h{}Class _Z9_{Constructor (_7,___:Array [Array [Array [Int ,53],53],0b1010101]){} }Class U_{}'''
        expect = '''Program([ClassDecl(Id(h),[]),ClassDecl(Id(_Z9_),[MethodDecl(Id(Constructor),Instance,[param(Id(_7),ArrayType(85,ArrayType(53,ArrayType(53,IntType)))),param(Id(___),ArrayType(85,ArrayType(53,ArrayType(53,IntType))))],Block([],[]))]),ClassDecl(Id(U_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 242))

    def test_243(self):
        line = '''Class N{}Class dBQ1N_o_7:X19{Var $r:m;}Class X{}Class o{}'''
        expect = '''Program([ClassDecl(Id(N),[]),ClassDecl(Id(dBQ1N_o_7),Id(X19),[AttributeDecl(Static,VarDecl(Id($r),ClassType(Id(m))))]),ClassDecl(Id(X),[]),ClassDecl(Id(o),[])])'''
        self.assertTrue(TestAST.test(line, expect, 243))

    def test_244(self):
        line = '''Class _:at_{}Class X___6U2{Var M_,$U_,p:Boolean ;}Class JE9{}'''
        expect = '''Program([ClassDecl(Id(_),Id(at_),[]),ClassDecl(Id(X___6U2),[AttributeDecl(Instance,VarDecl(Id(M_),BoolType)),AttributeDecl(Static,VarDecl(Id($U_),BoolType)),AttributeDecl(Instance,VarDecl(Id(p),BoolType))]),ClassDecl(Id(JE9),[])])'''
        self.assertTrue(TestAST.test(line, expect, 244))

    def test_245(self):
        line = '''Class m16_:_8{}Class _{Var _,$Al_,$tZ,$4,f,jX__,$_,$3:L5;Constructor (){} }'''
        expect = '''Program([ClassDecl(Id(m16_),Id(_8),[]),ClassDecl(Id(_),[AttributeDecl(Instance,VarDecl(Id(_),ClassType(Id(L5)))),AttributeDecl(Static,VarDecl(Id($Al_),ClassType(Id(L5)))),AttributeDecl(Static,VarDecl(Id($tZ),ClassType(Id(L5)))),AttributeDecl(Static,VarDecl(Id($4),ClassType(Id(L5)))),AttributeDecl(Instance,VarDecl(Id(f),ClassType(Id(L5)))),AttributeDecl(Instance,VarDecl(Id(jX__),ClassType(Id(L5)))),AttributeDecl(Static,VarDecl(Id($_),ClassType(Id(L5)))),AttributeDecl(Static,VarDecl(Id($3),ClassType(Id(L5)))),MethodDecl(Id(Constructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 245))

    def test_246(self):
        line = '''Class _:e{}Class t:_{$T(X:Array [Array [String ,0B1011011],0xB_0];L:Int ){} }Class _6:_7{Var $7,$r0_2G,$q,$U,$_,$3_4X:Float ;}'''
        expect = '''Program([ClassDecl(Id(_),Id(e),[]),ClassDecl(Id(t),Id(_),[MethodDecl(Id($T),Static,[param(Id(X),ArrayType(176,ArrayType(91,StringType))),param(Id(L),IntType)],Block([],[]))]),ClassDecl(Id(_6),Id(_7),[AttributeDecl(Static,VarDecl(Id($7),FloatType)),AttributeDecl(Static,VarDecl(Id($r0_2G),FloatType)),AttributeDecl(Static,VarDecl(Id($q),FloatType)),AttributeDecl(Static,VarDecl(Id($U),FloatType)),AttributeDecl(Static,VarDecl(Id($_),FloatType)),AttributeDecl(Static,VarDecl(Id($3_4X),FloatType))])])'''
        self.assertTrue(TestAST.test(line, expect, 246))

    def test_247(self):
        line = '''Class SjT5:m1{}Class t:_e5{g_h(){Continue ;{} }Constructor (){Continue ;Return ;Var _L73_:Int ;} }'''
        expect = '''Program([ClassDecl(Id(SjT5),Id(m1),[]),ClassDecl(Id(t),Id(_e5),[MethodDecl(Id(g_h),Instance,[],Block([],[Continue,Block([],[])])),MethodDecl(Id(Constructor),Instance,[],Block([VarDecl(Id(_L73_),IntType)],[Continue,Return(None)]))])])'''
        self.assertTrue(TestAST.test(line, expect, 247))

    def test_248(self):
        line = '''Class _:e5{Destructor (){}y(___:String ){} }Class N{}Class _J{}'''
        expect = '''Program([ClassDecl(Id(_),Id(e5),[MethodDecl(Id(Destructor),Instance,[],Block([],[])),MethodDecl(Id(y),Instance,[param(Id(___),StringType)],Block([],[]))]),ClassDecl(Id(N),[]),ClassDecl(Id(_J),[])])'''
        self.assertTrue(TestAST.test(line, expect, 248))

    def test_249(self):
        line = '''Class _862_:_4{}Class _5:__{$G(_8k,w_y0_,_7_9,_:String ;L,Nm,g:Int ;i,D:_4_){} }Class f{}'''
        expect = '''Program([ClassDecl(Id(_862_),Id(_4),[]),ClassDecl(Id(_5),Id(__),[MethodDecl(Id($G),Static,[param(Id(_8k),StringType),param(Id(w_y0_),StringType),param(Id(_7_9),StringType),param(Id(_),StringType),param(Id(L),IntType),param(Id(Nm),IntType),param(Id(g),IntType),param(Id(i),ClassType(Id(_4_))),param(Id(D),ClassType(Id(_4_)))],Block([],[]))]),ClassDecl(Id(f),[])])'''
        self.assertTrue(TestAST.test(line, expect, 249))

    def test_250(self):
        line = '''Class R_N2_:_4{}Class b{}Class _{$02(l:G1){}Destructor (){} }'''
        expect = '''Program([ClassDecl(Id(R_N2_),Id(_4),[]),ClassDecl(Id(b),[]),ClassDecl(Id(_),[MethodDecl(Id($02),Static,[param(Id(l),ClassType(Id(G1)))],Block([],[])),MethodDecl(Id(Destructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 250))

    def test_251(self):
        line = '''Class _Nn46_u27{Destructor (){Break ;{}Break ;}Constructor (dL54_,_:Array [Float ,59]){}Var $g:String ;Var _2_X,q4,_:Array [String ,060];}'''
        expect = '''Program([ClassDecl(Id(_Nn46_u27),[MethodDecl(Id(Destructor),Instance,[],Block([],[Break,Block([],[]),Break])),MethodDecl(Id(Constructor),Instance,[param(Id(dL54_),ArrayType(59,FloatType)),param(Id(_),ArrayType(59,FloatType))],Block([],[])),AttributeDecl(Static,VarDecl(Id($g),StringType)),AttributeDecl(Instance,VarDecl(Id(_2_X),ArrayType(48,StringType))),AttributeDecl(Instance,VarDecl(Id(q4),ArrayType(48,StringType))),AttributeDecl(Instance,VarDecl(Id(_),ArrayType(48,StringType)))])])'''
        self.assertTrue(TestAST.test(line, expect, 251))

    def test_252(self):
        line = '''Class _:_5MO{}Class F{Constructor (__,s,_,_:String ;o0,_:yo_;_:T){Break ;Continue ;{} }}Class e:_m{}'''
        expect = '''Program([ClassDecl(Id(_),Id(_5MO),[]),ClassDecl(Id(F),[MethodDecl(Id(Constructor),Instance,[param(Id(__),StringType),param(Id(s),StringType),param(Id(_),StringType),param(Id(_),StringType),param(Id(o0),ClassType(Id(yo_))),param(Id(_),ClassType(Id(yo_))),param(Id(_),ClassType(Id(T)))],Block([],[Break,Continue,Block([],[])]))]),ClassDecl(Id(e),Id(_m),[])])'''
        self.assertTrue(TestAST.test(line, expect, 252))

    def test_253(self):
        line = '''Class G_{Destructor (){Continue ;}o(){} }Class J0_:T{}Class d:_{}Class R{}Class x{}'''
        expect = '''Program([ClassDecl(Id(G_),[MethodDecl(Id(Destructor),Instance,[],Block([],[Continue])),MethodDecl(Id(o),Instance,[],Block([],[]))]),ClassDecl(Id(J0_),Id(T),[]),ClassDecl(Id(d),Id(_),[]),ClassDecl(Id(R),[]),ClassDecl(Id(x),[])])'''
        self.assertTrue(TestAST.test(line, expect, 253))

    def test_254(self):
        line = '''Class Z:i712P{u__(){}Lw2(_:String ;zy46:Array [String ,0B110110]){} }Class X:D1_{}'''
        expect = '''Program([ClassDecl(Id(Z),Id(i712P),[MethodDecl(Id(u__),Instance,[],Block([],[])),MethodDecl(Id(Lw2),Instance,[param(Id(_),StringType),param(Id(zy46),ArrayType(54,StringType))],Block([],[]))]),ClassDecl(Id(X),Id(D1_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 254))

    def test_255(self):
        line = '''Class __:s{}Class u2s7:U{}Class _{Constructor (){} }Class Mx_{}'''
        expect = '''Program([ClassDecl(Id(__),Id(s),[]),ClassDecl(Id(u2s7),Id(U),[]),ClassDecl(Id(_),[MethodDecl(Id(Constructor),Instance,[],Block([],[]))]),ClassDecl(Id(Mx_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 255))

    def test_256(self):
        line = '''Class I_c7{Constructor (F:Array [String ,0X27];_,_h,_,_,_:_9o9){} }'''
        expect = '''Program([ClassDecl(Id(I_c7),[MethodDecl(Id(Constructor),Instance,[param(Id(F),ArrayType(39,StringType)),param(Id(_),ClassType(Id(_9o9))),param(Id(_h),ClassType(Id(_9o9))),param(Id(_),ClassType(Id(_9o9))),param(Id(_),ClassType(Id(_9o9))),param(Id(_),ClassType(Id(_9o9)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 256))

    def test_257(self):
        line = '''Class _8{}Class __N_{$__(){}Constructor (___4,_J,F,_5:Array [Array [Array [Float ,01],5],0xD];ND_,x,P,_8,q:Array [String ,0B1000001];_9,WI5:Boolean ){} }'''
        expect = '''Program([ClassDecl(Id(_8),[]),ClassDecl(Id(__N_),[MethodDecl(Id($__),Static,[],Block([],[])),MethodDecl(Id(Constructor),Instance,[param(Id(___4),ArrayType(13,ArrayType(5,ArrayType(1,FloatType)))),param(Id(_J),ArrayType(13,ArrayType(5,ArrayType(1,FloatType)))),param(Id(F),ArrayType(13,ArrayType(5,ArrayType(1,FloatType)))),param(Id(_5),ArrayType(13,ArrayType(5,ArrayType(1,FloatType)))),param(Id(ND_),ArrayType(65,StringType)),param(Id(x),ArrayType(65,StringType)),param(Id(P),ArrayType(65,StringType)),param(Id(_8),ArrayType(65,StringType)),param(Id(q),ArrayType(65,StringType)),param(Id(_9),BoolType),param(Id(WI5),BoolType)],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 257))

    def test_258(self):
        line = '''Class wi_:y{}Class __:_{Constructor (k_I,S,_w:_5_){} }Class _4_{}Class ____{Constructor (){} }'''
        expect = '''Program([ClassDecl(Id(wi_),Id(y),[]),ClassDecl(Id(__),Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(k_I),ClassType(Id(_5_))),param(Id(S),ClassType(Id(_5_))),param(Id(_w),ClassType(Id(_5_)))],Block([],[]))]),ClassDecl(Id(_4_),[]),ClassDecl(Id(____),[MethodDecl(Id(Constructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 258))

    def test_259(self):
        line = '''Class F{Constructor (_:q;h,_,_5:Array [Float ,0x4D];_W:Boolean ;V,_d8,__:Array [String ,0B100001];_z_:Array [Array [String ,075],25];D__,r,_,I,Q,_,rA_q_k,_p,_:t5x922_385){} }'''
        expect = '''Program([ClassDecl(Id(F),[MethodDecl(Id(Constructor),Instance,[param(Id(_),ClassType(Id(q))),param(Id(h),ArrayType(77,FloatType)),param(Id(_),ArrayType(77,FloatType)),param(Id(_5),ArrayType(77,FloatType)),param(Id(_W),BoolType),param(Id(V),ArrayType(33,StringType)),param(Id(_d8),ArrayType(33,StringType)),param(Id(__),ArrayType(33,StringType)),param(Id(_z_),ArrayType(25,ArrayType(61,StringType))),param(Id(D__),ClassType(Id(t5x922_385))),param(Id(r),ClassType(Id(t5x922_385))),param(Id(_),ClassType(Id(t5x922_385))),param(Id(I),ClassType(Id(t5x922_385))),param(Id(Q),ClassType(Id(t5x922_385))),param(Id(_),ClassType(Id(t5x922_385))),param(Id(rA_q_k),ClassType(Id(t5x922_385))),param(Id(_p),ClassType(Id(t5x922_385))),param(Id(_),ClassType(Id(t5x922_385)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 259))

    def test_260(self):
        line = '''Class _{Destructor (){}Destructor (){} }Class _9OZ{}Class B:_{}'''
        expect = '''Program([ClassDecl(Id(_),[MethodDecl(Id(Destructor),Instance,[],Block([],[])),MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(_9OZ),[]),ClassDecl(Id(B),Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 260))

    def test_261(self):
        line = '''Class _6:_1_{Constructor (){}Var $827,_:Boolean ;}Class _{}'''
        expect = '''Program([ClassDecl(Id(_6),Id(_1_),[MethodDecl(Id(Constructor),Instance,[],Block([],[])),AttributeDecl(Static,VarDecl(Id($827),BoolType)),AttributeDecl(Instance,VarDecl(Id(_),BoolType))]),ClassDecl(Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 261))

    def test_262(self):
        line = '''Class Z5:_8{}Class H:_F2{Destructor (){ {Continue ;Var q:Array [Boolean ,02];}{} }}'''
        expect = '''Program([ClassDecl(Id(Z5),Id(_8),[]),ClassDecl(Id(H),Id(_F2),[MethodDecl(Id(Destructor),Instance,[],Block([],[Block([VarDecl(Id(q),ArrayType(2,BoolType))],[Continue]),Block([],[])]))])])'''
        self.assertTrue(TestAST.test(line, expect, 262))

    def test_263(self):
        line = '''Class __:u{$_(n:U;j:Array [Array [String ,13],0102];V,K:String ){} }'''
        expect = '''Program([ClassDecl(Id(__),Id(u),[MethodDecl(Id($_),Static,[param(Id(n),ClassType(Id(U))),param(Id(j),ArrayType(66,ArrayType(13,StringType))),param(Id(V),StringType),param(Id(K),StringType)],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 263))

    def test_264(self):
        line = '''Class K5R:_{Var g,_D:Array [Array [Array [String ,0X15],10],0x47];}Class _:_{_(){Var _:O9_;Break ;} }'''
        expect = '''Program([ClassDecl(Id(K5R),Id(_),[AttributeDecl(Instance,VarDecl(Id(g),ArrayType(71,ArrayType(10,ArrayType(21,StringType))))),AttributeDecl(Instance,VarDecl(Id(_D),ArrayType(71,ArrayType(10,ArrayType(21,StringType)))))]),ClassDecl(Id(_),Id(_),[MethodDecl(Id(_),Instance,[],Block([VarDecl(Id(_),ClassType(Id(O9_)))],[Break]))])])'''
        self.assertTrue(TestAST.test(line, expect, 264))

    def test_265(self):
        line = '''Class j:z{}Class Af{}Class Y_0:_{}Class N:qEo{}Class _UKkr:P{Constructor (_4:Array [Float ,0B11];_:String ;SF:Array [String ,0x4B];K0,_,t,v,Z7_8J_7:__gi){}Var y_a,w,$_36D__,_o_4y:Array [Float ,041];}'''
        expect = '''Program([ClassDecl(Id(j),Id(z),[]),ClassDecl(Id(Af),[]),ClassDecl(Id(Y_0),Id(_),[]),ClassDecl(Id(N),Id(qEo),[]),ClassDecl(Id(_UKkr),Id(P),[MethodDecl(Id(Constructor),Instance,[param(Id(_4),ArrayType(3,FloatType)),param(Id(_),StringType),param(Id(SF),ArrayType(75,StringType)),param(Id(K0),ClassType(Id(__gi))),param(Id(_),ClassType(Id(__gi))),param(Id(t),ClassType(Id(__gi))),param(Id(v),ClassType(Id(__gi))),param(Id(Z7_8J_7),ClassType(Id(__gi)))],Block([],[])),AttributeDecl(Instance,VarDecl(Id(y_a),ArrayType(33,FloatType))),AttributeDecl(Instance,VarDecl(Id(w),ArrayType(33,FloatType))),AttributeDecl(Static,VarDecl(Id($_36D__),ArrayType(33,FloatType))),AttributeDecl(Instance,VarDecl(Id(_o_4y),ArrayType(33,FloatType)))])])'''
        self.assertTrue(TestAST.test(line, expect, 265))

    def test_266(self):
        line = '''Class G04_E_:b4{Var $O,s799:Array [Int ,5];}Class _w:rg{}'''
        expect = '''Program([ClassDecl(Id(G04_E_),Id(b4),[AttributeDecl(Static,VarDecl(Id($O),ArrayType(5,IntType))),AttributeDecl(Instance,VarDecl(Id(s799),ArrayType(5,IntType)))]),ClassDecl(Id(_w),Id(rg),[])])'''
        self.assertTrue(TestAST.test(line, expect, 266))

    def test_267(self):
        line = '''Class v8{}Class _{}Class A:Uv{_(_,_,_:Array [Int ,0b11101];_49_,H,j:Array [Float ,13];s:Int ;_:_9){} }Class l{}Class _B:c{}Class c:Z5{}'''
        expect = '''Program([ClassDecl(Id(v8),[]),ClassDecl(Id(_),[]),ClassDecl(Id(A),Id(Uv),[MethodDecl(Id(_),Instance,[param(Id(_),ArrayType(29,IntType)),param(Id(_),ArrayType(29,IntType)),param(Id(_),ArrayType(29,IntType)),param(Id(_49_),ArrayType(13,FloatType)),param(Id(H),ArrayType(13,FloatType)),param(Id(j),ArrayType(13,FloatType)),param(Id(s),IntType),param(Id(_),ClassType(Id(_9)))],Block([],[]))]),ClassDecl(Id(l),[]),ClassDecl(Id(_B),Id(c),[]),ClassDecl(Id(c),Id(Z5),[])])'''
        self.assertTrue(TestAST.test(line, expect, 267))

    def test_268(self):
        line = '''Class E_:_{Var $_,_7ddw7_D8_3m__9_,X,$_2:_;Var $4,_:N;}Class k{Destructor (){} }'''
        expect = '''Program([ClassDecl(Id(E_),Id(_),[AttributeDecl(Static,VarDecl(Id($_),ClassType(Id(_)))),AttributeDecl(Instance,VarDecl(Id(_7ddw7_D8_3m__9_),ClassType(Id(_)))),AttributeDecl(Instance,VarDecl(Id(X),ClassType(Id(_)))),AttributeDecl(Static,VarDecl(Id($_2),ClassType(Id(_)))),AttributeDecl(Static,VarDecl(Id($4),ClassType(Id(N)))),AttributeDecl(Instance,VarDecl(Id(_),ClassType(Id(N))))]),ClassDecl(Id(k),[MethodDecl(Id(Destructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 268))

    def test_269(self):
        line = '''Class _h:_S{}Class R_o:Z_{}Class Ec_:X_0{}Class ___:_k{}Class _{}Class ar__:_2_{}'''
        expect = '''Program([ClassDecl(Id(_h),Id(_S),[]),ClassDecl(Id(R_o),Id(Z_),[]),ClassDecl(Id(Ec_),Id(X_0),[]),ClassDecl(Id(___),Id(_k),[]),ClassDecl(Id(_),[]),ClassDecl(Id(ar__),Id(_2_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 269))

    def test_270(self):
        line = '''Class X{Constructor (_i6,U:Array [Array [Array [Int ,0X1_8_C],6],8]){} }'''
        expect = '''Program([ClassDecl(Id(X),[MethodDecl(Id(Constructor),Instance,[param(Id(_i6),ArrayType(8,ArrayType(6,ArrayType(396,IntType)))),param(Id(U),ArrayType(8,ArrayType(6,ArrayType(396,IntType))))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 270))

    def test_271(self):
        line = '''Class _kt{Destructor (){Break ;_34P::$N._3.X.__();} }Class _sC:q0{Var $_,$7_4U:A;}'''
        expect = '''Program([ClassDecl(Id(_kt),[MethodDecl(Id(Destructor),Instance,[],Block([],[Break,Call(FieldAccess(FieldAccess(FieldAccess(Id(_34P),Id($N)),Id(_3)),Id(X)),Id(__),[])]))]),ClassDecl(Id(_sC),Id(q0),[AttributeDecl(Static,VarDecl(Id($_),ClassType(Id(A)))),AttributeDecl(Static,VarDecl(Id($7_4U),ClassType(Id(A))))])])'''
        self.assertTrue(TestAST.test(line, expect, 271))

    def test_272(self):
        line = '''Class b{}Class q{}Class _:_{_(_,f,d:_;yi5A:Boolean ;_S,E,Xr,_,_:N;_1:Boolean ;R3_,_:Float ;_:Array [Array [Boolean ,0B1001101],0b1001101]){}Var _j:Array [Array [Array [Array [Float ,0b100_0],0x3],0XF_7_F7_3_D],0x24];}'''
        expect = '''Program([ClassDecl(Id(b),[]),ClassDecl(Id(q),[]),ClassDecl(Id(_),Id(_),[MethodDecl(Id(_),Instance,[param(Id(_),ClassType(Id(_))),param(Id(f),ClassType(Id(_))),param(Id(d),ClassType(Id(_))),param(Id(yi5A),BoolType),param(Id(_S),ClassType(Id(N))),param(Id(E),ClassType(Id(N))),param(Id(Xr),ClassType(Id(N))),param(Id(_),ClassType(Id(N))),param(Id(_),ClassType(Id(N))),param(Id(_1),BoolType),param(Id(R3_),FloatType),param(Id(_),FloatType),param(Id(_),ArrayType(77,ArrayType(77,BoolType)))],Block([],[])),AttributeDecl(Instance,VarDecl(Id(_j),ArrayType(36,ArrayType(16250685,ArrayType(3,ArrayType(8,FloatType))))))])])'''
        self.assertTrue(TestAST.test(line, expect, 272))

    def test_273(self):
        line = '''Class t_98011y76{Constructor (){}Destructor (){}$c(){} }'''
        expect = '''Program([ClassDecl(Id(t_98011y76),[MethodDecl(Id(Constructor),Instance,[],Block([],[])),MethodDecl(Id(Destructor),Instance,[],Block([],[])),MethodDecl(Id($c),Static,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 273))

    def test_274(self):
        line = '''Class a_:u{Constructor (_6:Float ){}Var I,$Xi,_D,$7_EQ:Boolean ;}Class u_:_2Z4{}Class x2:i{}Class __7w7{}Class H{}'''
        expect = '''Program([ClassDecl(Id(a_),Id(u),[MethodDecl(Id(Constructor),Instance,[param(Id(_6),FloatType)],Block([],[])),AttributeDecl(Instance,VarDecl(Id(I),BoolType)),AttributeDecl(Static,VarDecl(Id($Xi),BoolType)),AttributeDecl(Instance,VarDecl(Id(_D),BoolType)),AttributeDecl(Static,VarDecl(Id($7_EQ),BoolType))]),ClassDecl(Id(u_),Id(_2Z4),[]),ClassDecl(Id(x2),Id(i),[]),ClassDecl(Id(__7w7),[]),ClassDecl(Id(H),[])])'''
        self.assertTrue(TestAST.test(line, expect, 274))

    def test_275(self):
        line = '''Class R4_:Q{Constructor (){} }Class __:Y__2G___{}Class K:v{}Class r{Var $15x:Boolean ;}'''
        expect = '''Program([ClassDecl(Id(R4_),Id(Q),[MethodDecl(Id(Constructor),Instance,[],Block([],[]))]),ClassDecl(Id(__),Id(Y__2G___),[]),ClassDecl(Id(K),Id(v),[]),ClassDecl(Id(r),[AttributeDecl(Static,VarDecl(Id($15x),BoolType))])])'''
        self.assertTrue(TestAST.test(line, expect, 275))

    def test_276(self):
        line = '''Class _{Var a,H469_j:Boolean ;$Wp1a_6(_L,_,o,t0:String ){} }'''
        expect = '''Program([ClassDecl(Id(_),[AttributeDecl(Instance,VarDecl(Id(a),BoolType)),AttributeDecl(Instance,VarDecl(Id(H469_j),BoolType)),MethodDecl(Id($Wp1a_6),Static,[param(Id(_L),StringType),param(Id(_),StringType),param(Id(o),StringType),param(Id(t0),StringType)],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 276))

    def test_277(self):
        line = '''Class G:c48{Constructor (_:V){Break ;{} }Var _,G__,tK_u:Array [Array [Array [Int ,3_5],0b1000011],077];}'''
        expect = '''Program([ClassDecl(Id(G),Id(c48),[MethodDecl(Id(Constructor),Instance,[param(Id(_),ClassType(Id(V)))],Block([],[Break,Block([],[])])),AttributeDecl(Instance,VarDecl(Id(_),ArrayType(63,ArrayType(67,ArrayType(35,IntType))))),AttributeDecl(Instance,VarDecl(Id(G__),ArrayType(63,ArrayType(67,ArrayType(35,IntType))))),AttributeDecl(Instance,VarDecl(Id(tK_u),ArrayType(63,ArrayType(67,ArrayType(35,IntType)))))])])'''
        self.assertTrue(TestAST.test(line, expect, 277))

    def test_278(self):
        line = '''Class e8:p_99Q{Var $_,T,__:Array [Float ,0b1001010];}Class G7{}Class F{}'''
        expect = '''Program([ClassDecl(Id(e8),Id(p_99Q),[AttributeDecl(Static,VarDecl(Id($_),ArrayType(74,FloatType))),AttributeDecl(Instance,VarDecl(Id(T),ArrayType(74,FloatType))),AttributeDecl(Instance,VarDecl(Id(__),ArrayType(74,FloatType)))]),ClassDecl(Id(G7),[]),ClassDecl(Id(F),[])])'''
        self.assertTrue(TestAST.test(line, expect, 278))

    def test_279(self):
        line = '''Class e{Var $5,$_y:Float ;$D(t85,_A:Int ){}Constructor (W:Array [Array [String ,0114],0b1_1]){} }'''
        expect = '''Program([ClassDecl(Id(e),[AttributeDecl(Static,VarDecl(Id($5),FloatType)),AttributeDecl(Static,VarDecl(Id($_y),FloatType)),MethodDecl(Id($D),Static,[param(Id(t85),IntType),param(Id(_A),IntType)],Block([],[])),MethodDecl(Id(Constructor),Instance,[param(Id(W),ArrayType(3,ArrayType(76,StringType)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 279))

    def test_280(self):
        line = '''Class _{h(){}Constructor (J:_){}Var $_:String ;}Class _{}'''
        expect = '''Program([ClassDecl(Id(_),[MethodDecl(Id(h),Instance,[],Block([],[])),MethodDecl(Id(Constructor),Instance,[param(Id(J),ClassType(Id(_)))],Block([],[])),AttributeDecl(Static,VarDecl(Id($_),StringType))]),ClassDecl(Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 280))

    def test_281(self):
        line = '''Class _{Destructor (){Return ;} }Class IL:n{}Class KP_{}Class Y:Ua8k{}Class _b:_{}Class ___{}'''
        expect = '''Program([ClassDecl(Id(_),[MethodDecl(Id(Destructor),Instance,[],Block([],[Return(None)]))]),ClassDecl(Id(IL),Id(n),[]),ClassDecl(Id(KP_),[]),ClassDecl(Id(Y),Id(Ua8k),[]),ClassDecl(Id(_b),Id(_),[]),ClassDecl(Id(___),[])])'''
        self.assertTrue(TestAST.test(line, expect, 281))

    def test_282(self):
        line = '''Class __:j{Constructor (){_::$_._.__.nK();Break ;} }Class __:d{}'''
        expect = '''Program([ClassDecl(Id(__),Id(j),[MethodDecl(Id(Constructor),Instance,[],Block([],[Call(FieldAccess(FieldAccess(FieldAccess(Id(_),Id($_)),Id(_)),Id(__)),Id(nK),[]),Break]))]),ClassDecl(Id(__),Id(d),[])])'''
        self.assertTrue(TestAST.test(line, expect, 282))

    def test_283(self):
        line = '''Class Z:_{$98l(){}Destructor (){}$V_(_:W;_,_A:Array [Array [Int ,0X30],0B1]){}Var $q,$_6__,$8_:Array [Array [Array [Array [Array [Array [Array [Array [Int ,98],98],7_3_6],7],067],0b1_1_11],0X6],0X30];}'''
        expect = '''Program([ClassDecl(Id(Z),Id(_),[MethodDecl(Id($98l),Static,[],Block([],[])),MethodDecl(Id(Destructor),Instance,[],Block([],[])),MethodDecl(Id($V_),Static,[param(Id(_),ClassType(Id(W))),param(Id(_),ArrayType(1,ArrayType(48,IntType))),param(Id(_A),ArrayType(1,ArrayType(48,IntType)))],Block([],[])),AttributeDecl(Static,VarDecl(Id($q),ArrayType(48,ArrayType(6,ArrayType(15,ArrayType(55,ArrayType(7,ArrayType(736,ArrayType(98,ArrayType(98,IntType)))))))))),AttributeDecl(Static,VarDecl(Id($_6__),ArrayType(48,ArrayType(6,ArrayType(15,ArrayType(55,ArrayType(7,ArrayType(736,ArrayType(98,ArrayType(98,IntType)))))))))),AttributeDecl(Static,VarDecl(Id($8_),ArrayType(48,ArrayType(6,ArrayType(15,ArrayType(55,ArrayType(7,ArrayType(736,ArrayType(98,ArrayType(98,IntType))))))))))])])'''
        self.assertTrue(TestAST.test(line, expect, 283))

    def test_284(self):
        line = '''Class _n46:_{$_9(_:_;l9g_:P;W69NA_k:Boolean ;u_E_,__:Array [Array [Array [Float ,016_7_04],0X29],0b1001010]){}Destructor (){} }'''
        expect = '''Program([ClassDecl(Id(_n46),Id(_),[MethodDecl(Id($_9),Static,[param(Id(_),ClassType(Id(_))),param(Id(l9g_),ClassType(Id(P))),param(Id(W69NA_k),BoolType),param(Id(u_E_),ArrayType(74,ArrayType(41,ArrayType(7620,FloatType)))),param(Id(__),ArrayType(74,ArrayType(41,ArrayType(7620,FloatType))))],Block([],[])),MethodDecl(Id(Destructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 284))

    def test_285(self):
        line = '''Class _:_{}Class C26__{Constructor (K:f){} }Class A_:_{Var A,$_H,$O,f_,$_,zJ:_X_;}Class P:_{}'''
        expect = '''Program([ClassDecl(Id(_),Id(_),[]),ClassDecl(Id(C26__),[MethodDecl(Id(Constructor),Instance,[param(Id(K),ClassType(Id(f)))],Block([],[]))]),ClassDecl(Id(A_),Id(_),[AttributeDecl(Instance,VarDecl(Id(A),ClassType(Id(_X_)))),AttributeDecl(Static,VarDecl(Id($_H),ClassType(Id(_X_)))),AttributeDecl(Static,VarDecl(Id($O),ClassType(Id(_X_)))),AttributeDecl(Instance,VarDecl(Id(f_),ClassType(Id(_X_)))),AttributeDecl(Static,VarDecl(Id($_),ClassType(Id(_X_)))),AttributeDecl(Instance,VarDecl(Id(zJ),ClassType(Id(_X_))))]),ClassDecl(Id(P),Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 285))

    def test_286(self):
        line = '''Class a_{Constructor (_,___3,_N8:Array [Array [Int ,1],02]){}Var th_,$Q8:m;}Class _o_ZW:q{}'''
        expect = '''Program([ClassDecl(Id(a_),[MethodDecl(Id(Constructor),Instance,[param(Id(_),ArrayType(2,ArrayType(1,IntType))),param(Id(___3),ArrayType(2,ArrayType(1,IntType))),param(Id(_N8),ArrayType(2,ArrayType(1,IntType)))],Block([],[])),AttributeDecl(Instance,VarDecl(Id(th_),ClassType(Id(m)))),AttributeDecl(Static,VarDecl(Id($Q8),ClassType(Id(m))))]),ClassDecl(Id(_o_ZW),Id(q),[])])'''
        self.assertTrue(TestAST.test(line, expect, 286))

    def test_287(self):
        line = '''Class _{}Class ___66p_e_:__4n{Constructor (_0,_,_9N_,z:Array [String ,100]){} }'''
        expect = '''Program([ClassDecl(Id(_),[]),ClassDecl(Id(___66p_e_),Id(__4n),[MethodDecl(Id(Constructor),Instance,[param(Id(_0),ArrayType(100,StringType)),param(Id(_),ArrayType(100,StringType)),param(Id(_9N_),ArrayType(100,StringType)),param(Id(z),ArrayType(100,StringType))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 287))

    def test_288(self):
        line = '''Class p{Constructor (H,R:Array [Boolean ,07];_6:j_;v,t,_7,l:Array [Int ,025]){}Constructor (){} }Class o{}'''
        expect = '''Program([ClassDecl(Id(p),[MethodDecl(Id(Constructor),Instance,[param(Id(H),ArrayType(7,BoolType)),param(Id(R),ArrayType(7,BoolType)),param(Id(_6),ClassType(Id(j_))),param(Id(v),ArrayType(21,IntType)),param(Id(t),ArrayType(21,IntType)),param(Id(_7),ArrayType(21,IntType)),param(Id(l),ArrayType(21,IntType))],Block([],[])),MethodDecl(Id(Constructor),Instance,[],Block([],[]))]),ClassDecl(Id(o),[])])'''
        self.assertTrue(TestAST.test(line, expect, 288))

    def test_289(self):
        line = '''Class _5_{Var _f,$t:Array [Array [Array [String ,0X4_8],655],40];}'''
        expect = '''Program([ClassDecl(Id(_5_),[AttributeDecl(Instance,VarDecl(Id(_f),ArrayType(40,ArrayType(655,ArrayType(72,StringType))))),AttributeDecl(Static,VarDecl(Id($t),ArrayType(40,ArrayType(655,ArrayType(72,StringType)))))])])'''
        self.assertTrue(TestAST.test(line, expect, 289))

    def test_290(self):
        line = '''Class _K:___b{}Class p:_9{Var $5M:String ;Destructor (){} }'''
        expect = '''Program([ClassDecl(Id(_K),Id(___b),[]),ClassDecl(Id(p),Id(_9),[AttributeDecl(Static,VarDecl(Id($5M),StringType)),MethodDecl(Id(Destructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 290))

    def test_291(self):
        line = '''Class _2_{}Class _:__q{Var $B:Float ;Var $v7_mx:Array [Array [Array [Int ,0106],0b11010],0b11010];Var $5:ZI_;}'''
        expect = '''Program([ClassDecl(Id(_2_),[]),ClassDecl(Id(_),Id(__q),[AttributeDecl(Static,VarDecl(Id($B),FloatType)),AttributeDecl(Static,VarDecl(Id($v7_mx),ArrayType(26,ArrayType(26,ArrayType(70,IntType))))),AttributeDecl(Static,VarDecl(Id($5),ClassType(Id(ZI_))))])])'''
        self.assertTrue(TestAST.test(line, expect, 291))

    def test_292(self):
        line = '''Class _{Constructor (____WA_,R:_){Continue ;}Var $7J:Array [String ,0XD6];}'''
        expect = '''Program([ClassDecl(Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(____WA_),ClassType(Id(_))),param(Id(R),ClassType(Id(_)))],Block([],[Continue])),AttributeDecl(Static,VarDecl(Id($7J),ArrayType(214,StringType)))])])'''
        self.assertTrue(TestAST.test(line, expect, 292))

    def test_293(self):
        line = '''Class _:r{Var yw:Float ;Destructor (){}Var $f:String ;Var $a__:String ;}'''
        expect = '''Program([ClassDecl(Id(_),Id(r),[AttributeDecl(Instance,VarDecl(Id(yw),FloatType)),MethodDecl(Id(Destructor),Instance,[],Block([],[])),AttributeDecl(Static,VarDecl(Id($f),StringType)),AttributeDecl(Static,VarDecl(Id($a__),StringType))])])'''
        self.assertTrue(TestAST.test(line, expect, 293))

    def test_294(self):
        line = '''Class c_{}Class IL_{}Class G:__3Y{Var $_:Array [Array [Boolean ,6],05];}Class b:_{}'''
        expect = '''Program([ClassDecl(Id(c_),[]),ClassDecl(Id(IL_),[]),ClassDecl(Id(G),Id(__3Y),[AttributeDecl(Static,VarDecl(Id($_),ArrayType(5,ArrayType(6,BoolType))))]),ClassDecl(Id(b),Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 294))

    def test_295(self):
        line = '''Class J3{Destructor (){}Constructor (){}Constructor (){} }'''
        expect = '''Program([ClassDecl(Id(J3),[MethodDecl(Id(Destructor),Instance,[],Block([],[])),MethodDecl(Id(Constructor),Instance,[],Block([],[])),MethodDecl(Id(Constructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 295))

    def test_296(self):
        line = '''Class T:H{}Class M:Q3{Var _,I,$k,$66:Z_;Constructor (){ {}Var __,_5_,__:String ;}Destructor (){}$6__(){}Destructor (){} }'''
        expect = '''Program([ClassDecl(Id(T),Id(H),[]),ClassDecl(Id(M),Id(Q3),[AttributeDecl(Instance,VarDecl(Id(_),ClassType(Id(Z_)))),AttributeDecl(Instance,VarDecl(Id(I),ClassType(Id(Z_)))),AttributeDecl(Static,VarDecl(Id($k),ClassType(Id(Z_)))),AttributeDecl(Static,VarDecl(Id($66),ClassType(Id(Z_)))),MethodDecl(Id(Constructor),Instance,[],Block([VarDecl(Id(__),StringType),VarDecl(Id(_5_),StringType),VarDecl(Id(__),StringType)],[Block([],[])])),MethodDecl(Id(Destructor),Instance,[],Block([],[])),MethodDecl(Id($6__),Static,[],Block([],[])),MethodDecl(Id(Destructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 296))

    def test_297(self):
        line = '''Class __:_N{Var n6,L93,m,$__4:Array [Array [Float ,0B1010000],0B1];}Class ze9:uy{}'''
        expect = '''Program([ClassDecl(Id(__),Id(_N),[AttributeDecl(Instance,VarDecl(Id(n6),ArrayType(1,ArrayType(80,FloatType)))),AttributeDecl(Instance,VarDecl(Id(L93),ArrayType(1,ArrayType(80,FloatType)))),AttributeDecl(Instance,VarDecl(Id(m),ArrayType(1,ArrayType(80,FloatType)))),AttributeDecl(Static,VarDecl(Id($__4),ArrayType(1,ArrayType(80,FloatType))))]),ClassDecl(Id(ze9),Id(uy),[])])'''
        self.assertTrue(TestAST.test(line, expect, 297))

    def test_298(self):
        line = '''Class __:j3{}Class _:xE{}Class U:F{_F_3(_,C8,___:String ;_0_,S__A,_:Array [Array [Int ,04],0X6];W4f,_:String ){} }'''
        expect = '''Program([ClassDecl(Id(__),Id(j3),[]),ClassDecl(Id(_),Id(xE),[]),ClassDecl(Id(U),Id(F),[MethodDecl(Id(_F_3),Instance,[param(Id(_),StringType),param(Id(C8),StringType),param(Id(___),StringType),param(Id(_0_),ArrayType(6,ArrayType(4,IntType))),param(Id(S__A),ArrayType(6,ArrayType(4,IntType))),param(Id(_),ArrayType(6,ArrayType(4,IntType))),param(Id(W4f),StringType),param(Id(_),StringType)],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 298))

    def test_299(self):
        line = '''Class _{Constructor (D3y:Array [Array [Array [Int ,0X1],0B1],0X1];___,tS___,_5j,t:q){} }'''
        expect = '''Program([ClassDecl(Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(D3y),ArrayType(1,ArrayType(1,ArrayType(1,IntType)))),param(Id(___),ClassType(Id(q))),param(Id(tS___),ClassType(Id(q))),param(Id(_5j),ClassType(Id(q))),param(Id(t),ClassType(Id(q)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 299))

    def test_300(self):
        line = '''Class _:TF{Destructor (){Var l,__:_T;}Var $8,Y4:String ;}'''
        expect = '''Program([ClassDecl(Id(_),Id(TF),[MethodDecl(Id(Destructor),Instance,[],Block([VarDecl(Id(l),ClassType(Id(_T))),VarDecl(Id(__),ClassType(Id(_T)))],[])),AttributeDecl(Static,VarDecl(Id($8),StringType)),AttributeDecl(Instance,VarDecl(Id(Y4),StringType))])])'''
        self.assertTrue(TestAST.test(line, expect, 300))

    def test_301(self):
        line = '''Class V{}Class _:_{U90_(__:Array [Boolean ,0X48];__:Array [String ,28];y:String ;_d:String ;K2Q:String ){}$B(){} }Class _76:X3{}Class _M:g{}'''
        expect = '''Program([ClassDecl(Id(V),[]),ClassDecl(Id(_),Id(_),[MethodDecl(Id(U90_),Instance,[param(Id(__),ArrayType(72,BoolType)),param(Id(__),ArrayType(28,StringType)),param(Id(y),StringType),param(Id(_d),StringType),param(Id(K2Q),StringType)],Block([],[])),MethodDecl(Id($B),Static,[],Block([],[]))]),ClassDecl(Id(_76),Id(X3),[]),ClassDecl(Id(_M),Id(g),[])])'''
        self.assertTrue(TestAST.test(line, expect, 301))

    def test_302(self):
        line = '''Class _{Constructor (_,_,Q,P,E45:Array [Int ,01_0_7]){}$G(U_J2_:Array [Array [Array [Array [Array [Array [Array [String ,4],0xF],0b1011001],0xA],0x4_6_2_B_6],0X9],0xB]){}Destructor (){} }'''
        expect = '''Program([ClassDecl(Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(_),ArrayType(71,IntType)),param(Id(_),ArrayType(71,IntType)),param(Id(Q),ArrayType(71,IntType)),param(Id(P),ArrayType(71,IntType)),param(Id(E45),ArrayType(71,IntType))],Block([],[])),MethodDecl(Id($G),Static,[param(Id(U_J2_),ArrayType(11,ArrayType(9,ArrayType(287414,ArrayType(10,ArrayType(89,ArrayType(15,ArrayType(4,StringType))))))))],Block([],[])),MethodDecl(Id(Destructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 302))

    def test_303(self):
        line = '''Class __7:_{Constructor (s:n;D,c,a:__;_2:Array [Int ,41];M,we:_98;G:String ){} }'''
        expect = '''Program([ClassDecl(Id(__7),Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(s),ClassType(Id(n))),param(Id(D),ClassType(Id(__))),param(Id(c),ClassType(Id(__))),param(Id(a),ClassType(Id(__))),param(Id(_2),ArrayType(41,IntType)),param(Id(M),ClassType(Id(_98))),param(Id(we),ClassType(Id(_98))),param(Id(G),StringType)],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 303))

    def test_304(self):
        line = '''Class L9{}Class __{}Class T_{}Class ___:_{}Class __2:eh{}Class u_5:FjE2{}'''
        expect = '''Program([ClassDecl(Id(L9),[]),ClassDecl(Id(__),[]),ClassDecl(Id(T_),[]),ClassDecl(Id(___),Id(_),[]),ClassDecl(Id(__2),Id(eh),[]),ClassDecl(Id(u_5),Id(FjE2),[])])'''
        self.assertTrue(TestAST.test(line, expect, 304))

    def test_305(self):
        line = '''Class Y3{$T_(SY:Array [String ,0X53]){} }Class DU_7_{}Class __{}'''
        expect = '''Program([ClassDecl(Id(Y3),[MethodDecl(Id($T_),Static,[param(Id(SY),ArrayType(83,StringType))],Block([],[]))]),ClassDecl(Id(DU_7_),[]),ClassDecl(Id(__),[])])'''
        self.assertTrue(TestAST.test(line, expect, 305))

    def test_306(self):
        line = '''Class _:_{}Class _{Constructor (){} }Class _0_:SsQ{Var _,$_l6_:Float ;Var $pl:Int ;$_9___(){} }'''
        expect = '''Program([ClassDecl(Id(_),Id(_),[]),ClassDecl(Id(_),[MethodDecl(Id(Constructor),Instance,[],Block([],[]))]),ClassDecl(Id(_0_),Id(SsQ),[AttributeDecl(Instance,VarDecl(Id(_),FloatType)),AttributeDecl(Static,VarDecl(Id($_l6_),FloatType)),AttributeDecl(Static,VarDecl(Id($pl),IntType)),MethodDecl(Id($_9___),Static,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 306))

    def test_307(self):
        line = '''Class nx{Var _,B,$6ebd,u:Int ;}Class _{$_(z2_811N:Array [Array [Array [Array [Array [Array [Array [Array [Array [Array [Int ,0x1D],9],0X28],9],22],02],0X28],4],0x1D],0x1D]){} }'''
        expect = '''Program([ClassDecl(Id(nx),[AttributeDecl(Instance,VarDecl(Id(_),IntType)),AttributeDecl(Instance,VarDecl(Id(B),IntType)),AttributeDecl(Static,VarDecl(Id($6ebd),IntType)),AttributeDecl(Instance,VarDecl(Id(u),IntType))]),ClassDecl(Id(_),[MethodDecl(Id($_),Static,[param(Id(z2_811N),ArrayType(29,ArrayType(29,ArrayType(4,ArrayType(40,ArrayType(2,ArrayType(22,ArrayType(9,ArrayType(40,ArrayType(9,ArrayType(29,IntType)))))))))))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 307))

    def test_308(self):
        line = '''Class z{}Class Y4{Var _T,$f,$_:Array [Array [Int ,0X33],062];}Class _:_0{}'''
        expect = '''Program([ClassDecl(Id(z),[]),ClassDecl(Id(Y4),[AttributeDecl(Instance,VarDecl(Id(_T),ArrayType(50,ArrayType(51,IntType)))),AttributeDecl(Static,VarDecl(Id($f),ArrayType(50,ArrayType(51,IntType)))),AttributeDecl(Static,VarDecl(Id($_),ArrayType(50,ArrayType(51,IntType))))]),ClassDecl(Id(_),Id(_0),[])])'''
        self.assertTrue(TestAST.test(line, expect, 308))

    def test_309(self):
        line = '''Class _:r{Constructor (){}Destructor (){}Var $Rf,$v,v:String ;}'''
        expect = '''Program([ClassDecl(Id(_),Id(r),[MethodDecl(Id(Constructor),Instance,[],Block([],[])),MethodDecl(Id(Destructor),Instance,[],Block([],[])),AttributeDecl(Static,VarDecl(Id($Rf),StringType)),AttributeDecl(Static,VarDecl(Id($v),StringType)),AttributeDecl(Instance,VarDecl(Id(v),StringType))])])'''
        self.assertTrue(TestAST.test(line, expect, 309))

    def test_310(self):
        line = '''Class I:G{__s31(_v,L_:Array [Array [String ,0106],6_57]){} }'''
        expect = '''Program([ClassDecl(Id(I),Id(G),[MethodDecl(Id(__s31),Instance,[param(Id(_v),ArrayType(657,ArrayType(70,StringType))),param(Id(L_),ArrayType(657,ArrayType(70,StringType)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 310))

    def test_311(self):
        line = '''Class _:u471{Var $_4:Array [Array [String ,3],2];Constructor (_:M;i29_4_:Array [Array [Float ,0x8_7],06];o:f){ {} }$_(x:Array [Float ,88]){Return ;Continue ;} }'''
        expect = '''Program([ClassDecl(Id(_),Id(u471),[AttributeDecl(Static,VarDecl(Id($_4),ArrayType(2,ArrayType(3,StringType)))),MethodDecl(Id(Constructor),Instance,[param(Id(_),ClassType(Id(M))),param(Id(i29_4_),ArrayType(6,ArrayType(135,FloatType))),param(Id(o),ClassType(Id(f)))],Block([],[Block([],[])])),MethodDecl(Id($_),Static,[param(Id(x),ArrayType(88,FloatType))],Block([],[Return(None),Continue]))])])'''
        self.assertTrue(TestAST.test(line, expect, 311))

    def test_312(self):
        line = '''Class lP:Wz{}Class _:_3{Destructor (){Continue ;} }Class _L22X:j{}'''
        expect = '''Program([ClassDecl(Id(lP),Id(Wz),[]),ClassDecl(Id(_),Id(_3),[MethodDecl(Id(Destructor),Instance,[],Block([],[Continue]))]),ClassDecl(Id(_L22X),Id(j),[])])'''
        self.assertTrue(TestAST.test(line, expect, 312))

    def test_313(self):
        line = '''Class _:qc0R{}Class E{Var _:E=-New _().kD9.p.F.d().k.h6e71_;}'''
        expect = '''Program([ClassDecl(Id(_),Id(qc0R),[]),ClassDecl(Id(E),[AttributeDecl(Static,VarDecl(Id($b),ClassType(Id(E)),UnaryOp(-,FieldAccess(FieldAccess(CallExpr(FieldAccess(FieldAccess(FieldAccess(NewExpr(Id(_),[]),Id(kD9)),Id(p)),Id(F)),Id(d),[]),Id(k)),Id(h6e71_)))))])])'''
        self.assertTrue(TestAST.test(line, expect, 313))

    def test_314(self):
        line = '''Class s_7:_{Constructor (_2,F4:Array [Boolean ,0445_0];P:Float ){} }Class _2{}'''
        expect = '''Program([ClassDecl(Id(s_7),Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(_2),ArrayType(2344,BoolType)),param(Id(F4),ArrayType(2344,BoolType)),param(Id(P),FloatType)],Block([],[]))]),ClassDecl(Id(_2),[])])'''
        self.assertTrue(TestAST.test(line, expect, 314))

    def test_315(self):
        line = '''Class G{Constructor (_,_7,_F,d,_,A,_x,X:Boolean ;_:Float ){}Var $467,_9:Boolean ;}Class W:_{}'''
        expect = '''Program([ClassDecl(Id(G),[MethodDecl(Id(Constructor),Instance,[param(Id(_),BoolType),param(Id(_7),BoolType),param(Id(_F),BoolType),param(Id(d),BoolType),param(Id(_),BoolType),param(Id(A),BoolType),param(Id(_x),BoolType),param(Id(X),BoolType),param(Id(_),FloatType)],Block([],[])),AttributeDecl(Static,VarDecl(Id($467),BoolType)),AttributeDecl(Instance,VarDecl(Id(_9),BoolType))]),ClassDecl(Id(W),Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 315))

    def test_316(self):
        line = '''Class H{Var _s9,h:_;}Class B5f:H{}Class s_____:_5___{}Class _1_1__H{}'''
        expect = '''Program([ClassDecl(Id(H),[AttributeDecl(Instance,VarDecl(Id(_s9),ClassType(Id(_)))),AttributeDecl(Instance,VarDecl(Id(h),ClassType(Id(_))))]),ClassDecl(Id(B5f),Id(H),[]),ClassDecl(Id(s_____),Id(_5___),[]),ClassDecl(Id(_1_1__H),[])])'''
        self.assertTrue(TestAST.test(line, expect, 316))

    def test_317(self):
        line = '''Class __{Constructor (q,_PM1,X:Array [Float ,0x17];i,N:_4){} }Class _:_{}Class _{}'''
        expect = '''Program([ClassDecl(Id(__),[MethodDecl(Id(Constructor),Instance,[param(Id(q),ArrayType(23,FloatType)),param(Id(_PM1),ArrayType(23,FloatType)),param(Id(X),ArrayType(23,FloatType)),param(Id(i),ClassType(Id(_4))),param(Id(N),ClassType(Id(_4)))],Block([],[]))]),ClassDecl(Id(_),Id(_),[]),ClassDecl(Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 317))

    def test_318(self):
        line = '''Class __{Var $_,_1:Array [Array [Array [Array [Float ,700],0X42],0b1_00_0_10_0],0X9];__(__:Float ;_:c;__,_:v){Var _,F,H,k_4:_s;}Var _0:f;}'''
        expect = '''Program([ClassDecl(Id(__),[AttributeDecl(Static,VarDecl(Id($_),ArrayType(9,ArrayType(68,ArrayType(66,ArrayType(700,FloatType)))))),AttributeDecl(Instance,VarDecl(Id(_1),ArrayType(9,ArrayType(68,ArrayType(66,ArrayType(700,FloatType)))))),MethodDecl(Id(__),Instance,[param(Id(__),FloatType),param(Id(_),ClassType(Id(c))),param(Id(__),ClassType(Id(v))),param(Id(_),ClassType(Id(v)))],Block([VarDecl(Id(_),ClassType(Id(_s))),VarDecl(Id(F),ClassType(Id(_s))),VarDecl(Id(H),ClassType(Id(_s))),VarDecl(Id(k_4),ClassType(Id(_s)))],[])),AttributeDecl(Instance,VarDecl(Id(_0),ClassType(Id(f))))])])'''
        self.assertTrue(TestAST.test(line, expect, 318))

    def test_319(self):
        line = '''Class YW{}Class _6u3:__{Constructor (LZ_,I8:Array [String ,5];_,G:String ;V__6,J:Int ;wP,O,_,f0,_,D__7_23Q8:Boolean ){} }'''
        expect = '''Program([ClassDecl(Id(YW),[]),ClassDecl(Id(_6u3),Id(__),[MethodDecl(Id(Constructor),Instance,[param(Id(LZ_),ArrayType(5,StringType)),param(Id(I8),ArrayType(5,StringType)),param(Id(_),StringType),param(Id(G),StringType),param(Id(V__6),IntType),param(Id(J),IntType),param(Id(wP),BoolType),param(Id(O),BoolType),param(Id(_),BoolType),param(Id(f0),BoolType),param(Id(_),BoolType),param(Id(D__7_23Q8),BoolType)],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 319))

    def test_320(self):
        line = '''Class x{}Class H:U{}Class _:_Q__J_r{}Class E:N{}Class X:_{}'''
        expect = '''Program([ClassDecl(Id(x),[]),ClassDecl(Id(H),Id(U),[]),ClassDecl(Id(_),Id(_Q__J_r),[]),ClassDecl(Id(E),Id(N),[]),ClassDecl(Id(X),Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 320))

    def test_321(self):
        line = '''Class _38{Constructor (T,Wp7:Array [Array [Int ,0B1001001],0b1001001];A_B4__,y_:_;k,i1,I,___:Array [Int ,052]){Break ;Var F,_7:Boolean ;}Constructor (r:String ){} }'''
        expect = '''Program([ClassDecl(Id(_38),[MethodDecl(Id(Constructor),Instance,[param(Id(T),ArrayType(73,ArrayType(73,IntType))),param(Id(Wp7),ArrayType(73,ArrayType(73,IntType))),param(Id(A_B4__),ClassType(Id(_))),param(Id(y_),ClassType(Id(_))),param(Id(k),ArrayType(42,IntType)),param(Id(i1),ArrayType(42,IntType)),param(Id(I),ArrayType(42,IntType)),param(Id(___),ArrayType(42,IntType))],Block([VarDecl(Id(F),BoolType),VarDecl(Id(_7),BoolType)],[Break])),MethodDecl(Id(Constructor),Instance,[param(Id(r),StringType)],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 321))

    def test_322(self):
        line = '''Class Tk{Destructor (){} }Class b{}Class Wm{Destructor (){Var _p,_H0:Array [String ,05];} }Class _{}'''
        expect = '''Program([ClassDecl(Id(Tk),[MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(b),[]),ClassDecl(Id(Wm),[MethodDecl(Id(Destructor),Instance,[],Block([VarDecl(Id(_p),ArrayType(5,StringType)),VarDecl(Id(_H0),ArrayType(5,StringType))],[]))]),ClassDecl(Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 322))

    def test_323(self):
        line = '''Class _5:FW{}Class yc:_{$9(){Var Vt,a,jY,_,c,Y3351d,l9,I6,s,_:Array [Array [Int ,0X48],55];} }'''
        expect = '''Program([ClassDecl(Id(_5),Id(FW),[]),ClassDecl(Id(yc),Id(_),[MethodDecl(Id($9),Static,[],Block([VarDecl(Id(Vt),ArrayType(55,ArrayType(72,IntType))),VarDecl(Id(a),ArrayType(55,ArrayType(72,IntType))),VarDecl(Id(jY),ArrayType(55,ArrayType(72,IntType))),VarDecl(Id(_),ArrayType(55,ArrayType(72,IntType))),VarDecl(Id(c),ArrayType(55,ArrayType(72,IntType))),VarDecl(Id(Y3351d),ArrayType(55,ArrayType(72,IntType))),VarDecl(Id(l9),ArrayType(55,ArrayType(72,IntType))),VarDecl(Id(I6),ArrayType(55,ArrayType(72,IntType))),VarDecl(Id(s),ArrayType(55,ArrayType(72,IntType))),VarDecl(Id(_),ArrayType(55,ArrayType(72,IntType)))],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 323))

    def test_324(self):
        line = '''Class _k{Constructor (i,_dV7,A:Float ;_:Boolean ;_Ra:_;X04:Array [Array [Boolean ,04],0X43]){}Destructor (){}Var $_:Boolean ;}'''
        expect = '''Program([ClassDecl(Id(_k),[MethodDecl(Id(Constructor),Instance,[param(Id(i),FloatType),param(Id(_dV7),FloatType),param(Id(A),FloatType),param(Id(_),BoolType),param(Id(_Ra),ClassType(Id(_))),param(Id(X04),ArrayType(67,ArrayType(4,BoolType)))],Block([],[])),MethodDecl(Id(Destructor),Instance,[],Block([],[])),AttributeDecl(Static,VarDecl(Id($_),BoolType))])])'''
        self.assertTrue(TestAST.test(line, expect, 324))

    def test_325(self):
        line = '''Class __:WR{Constructor (W,_:Array [String ,0xA];__:Array [Array [Array [Array [Boolean ,01],01],01730],0X5D];___:a8){}Destructor (){Break ;} }Class _:uo{}Class __{}'''
        expect = '''Program([ClassDecl(Id(__),Id(WR),[MethodDecl(Id(Constructor),Instance,[param(Id(W),ArrayType(10,StringType)),param(Id(_),ArrayType(10,StringType)),param(Id(__),ArrayType(93,ArrayType(984,ArrayType(1,ArrayType(1,BoolType))))),param(Id(___),ClassType(Id(a8)))],Block([],[])),MethodDecl(Id(Destructor),Instance,[],Block([],[Break]))]),ClassDecl(Id(_),Id(uo),[]),ClassDecl(Id(__),[])])'''
        self.assertTrue(TestAST.test(line, expect, 325))

    def test_326(self):
        line = '''Class N{Constructor (_,_,L:Array [Array [Float ,25],25]){ {} }}Class zEl:K0_{M(_,aLR_Q_:Array [Float ,6]){} }'''
        expect = '''Program([ClassDecl(Id(N),[MethodDecl(Id(Constructor),Instance,[param(Id(_),ArrayType(25,ArrayType(25,FloatType))),param(Id(_),ArrayType(25,ArrayType(25,FloatType))),param(Id(L),ArrayType(25,ArrayType(25,FloatType)))],Block([],[Block([],[])]))]),ClassDecl(Id(zEl),Id(K0_),[MethodDecl(Id(M),Instance,[param(Id(_),ArrayType(6,FloatType)),param(Id(aLR_Q_),ArrayType(6,FloatType))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 326))

    def test_327(self):
        line = '''Class q:R2{$LK_H(I,T:Boolean ;K0:Float ){Break ;}Constructor (_9_:_){}$8(_:m_5;ts,m:s){} }'''
        expect = '''Program([ClassDecl(Id(q),Id(R2),[MethodDecl(Id($LK_H),Static,[param(Id(I),BoolType),param(Id(T),BoolType),param(Id(K0),FloatType)],Block([],[Break])),MethodDecl(Id(Constructor),Instance,[param(Id(_9_),ClassType(Id(_)))],Block([],[])),MethodDecl(Id($8),Static,[param(Id(_),ClassType(Id(m_5))),param(Id(ts),ClassType(Id(s))),param(Id(m),ClassType(Id(s)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 327))

    def test_328(self):
        line = '''Class _{}Class _{Var Z,_,$_:Array [Int ,0B1];Constructor (){} }Class ___:j_he{}Class __cT{}'''
        expect = '''Program([ClassDecl(Id(_),[]),ClassDecl(Id(_),[AttributeDecl(Instance,VarDecl(Id(Z),ArrayType(1,IntType))),AttributeDecl(Instance,VarDecl(Id(_),ArrayType(1,IntType))),AttributeDecl(Static,VarDecl(Id($_),ArrayType(1,IntType))),MethodDecl(Id(Constructor),Instance,[],Block([],[]))]),ClassDecl(Id(___),Id(j_he),[]),ClassDecl(Id(__cT),[])])'''
        self.assertTrue(TestAST.test(line, expect, 328))

    def test_329(self):
        line = '''Class F{}Class _7{}Class B:A{$4_e(___:Float ){}Var _Q:Array [Array [Array [Int ,0B1],07],0b1_0];Vc(zk3Ph:String ){}Var $R_,$_:P;$3(_:_s;_,w,_:Array [Int ,053_2]){} }'''
        expect = '''Program([ClassDecl(Id(F),[]),ClassDecl(Id(_7),[]),ClassDecl(Id(B),Id(A),[MethodDecl(Id($4_e),Static,[param(Id(___),FloatType)],Block([],[])),AttributeDecl(Instance,VarDecl(Id(_Q),ArrayType(2,ArrayType(7,ArrayType(1,IntType))))),MethodDecl(Id(Vc),Instance,[param(Id(zk3Ph),StringType)],Block([],[])),AttributeDecl(Static,VarDecl(Id($R_),ClassType(Id(P)))),AttributeDecl(Static,VarDecl(Id($_),ClassType(Id(P)))),MethodDecl(Id($3),Static,[param(Id(_),ClassType(Id(_s))),param(Id(_),ArrayType(346,IntType)),param(Id(w),ArrayType(346,IntType)),param(Id(_),ArrayType(346,IntType))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 329))

    def test_330(self):
        line = '''Class n8:w7{}Class d5:_b{Var B_:_wiKb6;Destructor (){Break ;} }'''
        expect = '''Program([ClassDecl(Id(n8),Id(w7),[]),ClassDecl(Id(d5),Id(_b),[AttributeDecl(Instance,VarDecl(Id(B_),ClassType(Id(_wiKb6)))),MethodDecl(Id(Destructor),Instance,[],Block([],[Break]))])])'''
        self.assertTrue(TestAST.test(line, expect, 330))

    def test_331(self):
        line = '''Class _:B{Constructor (C0:Array [Array [Array [Array [Array [Array [Array [Array [Array [Boolean ,0b1011001],0b10_00],0x33],0B1001010],0B1],0X45],0127],0X45],65];_:p;_2y,_,o:_){}T(){} }'''
        expect = '''Program([ClassDecl(Id(_),Id(B),[MethodDecl(Id(Constructor),Instance,[param(Id(C0),ArrayType(65,ArrayType(69,ArrayType(87,ArrayType(69,ArrayType(1,ArrayType(74,ArrayType(51,ArrayType(8,ArrayType(89,BoolType)))))))))),param(Id(_),ClassType(Id(p))),param(Id(_2y),ClassType(Id(_))),param(Id(_),ClassType(Id(_))),param(Id(o),ClassType(Id(_)))],Block([],[])),MethodDecl(Id(T),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 331))

    def test_332(self):
        line = '''Class _:_82{Var S_r3:_0;Constructor (C1:Array [Float ,0142]){Continue ;} }'''
        expect = '''Program([ClassDecl(Id(_),Id(_82),[AttributeDecl(Instance,VarDecl(Id(S_r3),ClassType(Id(_0)))),MethodDecl(Id(Constructor),Instance,[param(Id(C1),ArrayType(98,FloatType))],Block([],[Continue]))])])'''
        self.assertTrue(TestAST.test(line, expect, 332))

    def test_333(self):
        line = '''Class h_{}Class UA{}Class H{Var $I,_v,y:Array [Array [Array [Int ,7],0x6_5_2],0b1];}'''
        expect = '''Program([ClassDecl(Id(h_),[]),ClassDecl(Id(UA),[]),ClassDecl(Id(H),[AttributeDecl(Static,VarDecl(Id($I),ArrayType(1,ArrayType(1618,ArrayType(7,IntType))))),AttributeDecl(Instance,VarDecl(Id(_v),ArrayType(1,ArrayType(1618,ArrayType(7,IntType))))),AttributeDecl(Instance,VarDecl(Id(y),ArrayType(1,ArrayType(1618,ArrayType(7,IntType)))))])])'''
        self.assertTrue(TestAST.test(line, expect, 333))

    def test_334(self):
        line = '''Class __3{Var $_,$96,$c,$48y:Array [Array [Array [Array [Array [Array [Int ,0x33],0B111111],052],0xE],82],0X2C];}Class Yx4_2{}'''
        expect = '''Program([ClassDecl(Id(__3),[AttributeDecl(Static,VarDecl(Id($_),ArrayType(44,ArrayType(82,ArrayType(14,ArrayType(42,ArrayType(63,ArrayType(51,IntType)))))))),AttributeDecl(Static,VarDecl(Id($96),ArrayType(44,ArrayType(82,ArrayType(14,ArrayType(42,ArrayType(63,ArrayType(51,IntType)))))))),AttributeDecl(Static,VarDecl(Id($c),ArrayType(44,ArrayType(82,ArrayType(14,ArrayType(42,ArrayType(63,ArrayType(51,IntType)))))))),AttributeDecl(Static,VarDecl(Id($48y),ArrayType(44,ArrayType(82,ArrayType(14,ArrayType(42,ArrayType(63,ArrayType(51,IntType))))))))]),ClassDecl(Id(Yx4_2),[])])'''
        self.assertTrue(TestAST.test(line, expect, 334))

    def test_335(self):
        line = '''Class _:T2_9__{Destructor (){} }Class __1:u{Constructor (t:Array [String ,0X37];_r:Array [String ,06_2_3_5_332]){} }'''
        expect = '''Program([ClassDecl(Id(_),Id(T2_9__),[MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(__1),Id(u),[MethodDecl(Id(Constructor),Instance,[param(Id(t),ArrayType(55,StringType)),param(Id(_r),ArrayType(1653466,StringType))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 335))

    def test_336(self):
        line = '''Class T{Destructor (){} }Class d{Destructor (){}Constructor (_,fp:Array [Array [Array [String ,74],0b1010],07]){} }Class _u:_{}'''
        expect = '''Program([ClassDecl(Id(T),[MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(d),[MethodDecl(Id(Destructor),Instance,[],Block([],[])),MethodDecl(Id(Constructor),Instance,[param(Id(_),ArrayType(7,ArrayType(10,ArrayType(74,StringType)))),param(Id(fp),ArrayType(7,ArrayType(10,ArrayType(74,StringType))))],Block([],[]))]),ClassDecl(Id(_u),Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 336))

    def test_337(self):
        line = '''Class _:X_1{Constructor (_,B,_,y,_170JT:_){}Destructor (){} }'''
        expect = '''Program([ClassDecl(Id(_),Id(X_1),[MethodDecl(Id(Constructor),Instance,[param(Id(_),ClassType(Id(_))),param(Id(B),ClassType(Id(_))),param(Id(_),ClassType(Id(_))),param(Id(y),ClassType(Id(_))),param(Id(_170JT),ClassType(Id(_)))],Block([],[])),MethodDecl(Id(Destructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 337))

    def test_338(self):
        line = '''Class _:___{Var $k7_:o;Destructor (){}K(m,G:Array [Boolean ,06]){} }'''
        expect = '''Program([ClassDecl(Id(_),Id(___),[AttributeDecl(Static,VarDecl(Id($k7_),ClassType(Id(o)))),MethodDecl(Id(Destructor),Instance,[],Block([],[])),MethodDecl(Id(K),Instance,[param(Id(m),ArrayType(6,BoolType)),param(Id(G),ArrayType(6,BoolType))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 338))

    def test_339(self):
        line = '''Class _t0Z0{Destructor (){} }Class _{}Class _{Constructor (){Continue ;} }Class _____:i0y_Q{}'''
        expect = '''Program([ClassDecl(Id(_t0Z0),[MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(_),[]),ClassDecl(Id(_),[MethodDecl(Id(Constructor),Instance,[],Block([],[Continue]))]),ClassDecl(Id(_____),Id(i0y_Q),[])])'''
        self.assertTrue(TestAST.test(line, expect, 339))

    def test_340(self):
        line = '''Class _3_:h{Constructor (O:Array [Array [Array [Array [Array [Array [Array [Float ,0105],03_2_2],0X3],7],6],027],7];l_17,__,z_y,Z1,ln:Int ){} }Class ___{$5_(S5:Array [Array [Boolean ,0B1],0x8];_:_B;_:_){} }'''
        expect = '''Program([ClassDecl(Id(_3_),Id(h),[MethodDecl(Id(Constructor),Instance,[param(Id(O),ArrayType(7,ArrayType(23,ArrayType(6,ArrayType(7,ArrayType(3,ArrayType(210,ArrayType(69,FloatType)))))))),param(Id(l_17),IntType),param(Id(__),IntType),param(Id(z_y),IntType),param(Id(Z1),IntType),param(Id(ln),IntType)],Block([],[]))]),ClassDecl(Id(___),[MethodDecl(Id($5_),Static,[param(Id(S5),ArrayType(8,ArrayType(1,BoolType))),param(Id(_),ClassType(Id(_B))),param(Id(_),ClassType(Id(_)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 340))

    def test_341(self):
        line = '''Class _3_{Constructor (s,S:Array [Array [Array [Array [Float ,0x2],0x5],047_261],0b1];ty0,_S,_,t2d,__:Array [Int ,45];a:Array [Int ,0b1001001];a,_:R27){}Constructor (C8_8,_,_H,_8:Array [String ,0b11_0];E8,X,_:Array [Array [Float ,0B1],0B1]){} }Class K3{}'''
        expect = '''Program([ClassDecl(Id(_3_),[MethodDecl(Id(Constructor),Instance,[param(Id(s),ArrayType(1,ArrayType(20145,ArrayType(5,ArrayType(2,FloatType))))),param(Id(S),ArrayType(1,ArrayType(20145,ArrayType(5,ArrayType(2,FloatType))))),param(Id(ty0),ArrayType(45,IntType)),param(Id(_S),ArrayType(45,IntType)),param(Id(_),ArrayType(45,IntType)),param(Id(t2d),ArrayType(45,IntType)),param(Id(__),ArrayType(45,IntType)),param(Id(a),ArrayType(73,IntType)),param(Id(a),ClassType(Id(R27))),param(Id(_),ClassType(Id(R27)))],Block([],[])),MethodDecl(Id(Constructor),Instance,[param(Id(C8_8),ArrayType(6,StringType)),param(Id(_),ArrayType(6,StringType)),param(Id(_H),ArrayType(6,StringType)),param(Id(_8),ArrayType(6,StringType)),param(Id(E8),ArrayType(1,ArrayType(1,FloatType))),param(Id(X),ArrayType(1,ArrayType(1,FloatType))),param(Id(_),ArrayType(1,ArrayType(1,FloatType)))],Block([],[]))]),ClassDecl(Id(K3),[])])'''
        self.assertTrue(TestAST.test(line, expect, 341))

    def test_342(self):
        line = '''Class b:_{}Class _{Var $E:Array [Array [Array [Float ,0b1011111],0b1],0x36];}'''
        expect = '''Program([ClassDecl(Id(b),Id(_),[]),ClassDecl(Id(_),[AttributeDecl(Static,VarDecl(Id($E),ArrayType(54,ArrayType(1,ArrayType(95,FloatType)))))])])'''
        self.assertTrue(TestAST.test(line, expect, 342))

    def test_343(self):
        line = '''Class _:E_{$9(E,__,_:nS;_,_,_:_;_3F,w:c;q_l_,__y_b,t,j:Array [Float ,0X35]){} }Class ad6mQ{}'''
        expect = '''Program([ClassDecl(Id(_),Id(E_),[MethodDecl(Id($9),Static,[param(Id(E),ClassType(Id(nS))),param(Id(__),ClassType(Id(nS))),param(Id(_),ClassType(Id(nS))),param(Id(_),ClassType(Id(_))),param(Id(_),ClassType(Id(_))),param(Id(_),ClassType(Id(_))),param(Id(_3F),ClassType(Id(c))),param(Id(w),ClassType(Id(c))),param(Id(q_l_),ArrayType(53,FloatType)),param(Id(__y_b),ArrayType(53,FloatType)),param(Id(t),ArrayType(53,FloatType)),param(Id(j),ArrayType(53,FloatType))],Block([],[]))]),ClassDecl(Id(ad6mQ),[])])'''
        self.assertTrue(TestAST.test(line, expect, 343))

    def test_344(self):
        line = '''Class __1:_K2____{S(){} }Class i0J:_6{N_Vo_a(D8_3:_){} }Class d_2:_{}'''
        expect = '''Program([ClassDecl(Id(__1),Id(_K2____),[MethodDecl(Id(S),Instance,[],Block([],[]))]),ClassDecl(Id(i0J),Id(_6),[MethodDecl(Id(N_Vo_a),Instance,[param(Id(D8_3),ClassType(Id(_)))],Block([],[]))]),ClassDecl(Id(d_2),Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 344))

    def test_345(self):
        line = '''Class _6:M{}Class _9:__{}Class _B__5{}Class w_{}Class H_080:Gv{}'''
        expect = '''Program([ClassDecl(Id(_6),Id(M),[]),ClassDecl(Id(_9),Id(__),[]),ClassDecl(Id(_B__5),[]),ClassDecl(Id(w_),[]),ClassDecl(Id(H_080),Id(Gv),[])])'''
        self.assertTrue(TestAST.test(line, expect, 345))

    def test_346(self):
        line = '''Class d:_2{}Class __D{}Class V__:Q{}Class _{}Class W:_W__{}'''
        expect = '''Program([ClassDecl(Id(d),Id(_2),[]),ClassDecl(Id(__D),[]),ClassDecl(Id(V__),Id(Q),[]),ClassDecl(Id(_),[]),ClassDecl(Id(W),Id(_W__),[])])'''
        self.assertTrue(TestAST.test(line, expect, 346))

    def test_347(self):
        line = '''Class C_a_:__9U_R_ay{}Class _:__{}Class _:_{Destructor (){Continue ;} }'''
        expect = '''Program([ClassDecl(Id(C_a_),Id(__9U_R_ay),[]),ClassDecl(Id(_),Id(__),[]),ClassDecl(Id(_),Id(_),[MethodDecl(Id(Destructor),Instance,[],Block([],[Continue]))])])'''
        self.assertTrue(TestAST.test(line, expect, 347))

    def test_348(self):
        line = '''Class _:k{Constructor (){}Var $_:f;}Class a:G{}Class W_{}'''
        expect = '''Program([ClassDecl(Id(_),Id(k),[MethodDecl(Id(Constructor),Instance,[],Block([],[])),AttributeDecl(Static,VarDecl(Id($_),ClassType(Id(f))))]),ClassDecl(Id(a),Id(G),[]),ClassDecl(Id(W_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 348))

    def test_349(self):
        line = '''Class Q{}Class n5{}Class D{Var _,$61:Int ;Var _n_:String ;G(_,_:J;__:_2){} }Class R{Var $__:Array [Boolean ,0b11010];}'''
        expect = '''Program([ClassDecl(Id(Q),[]),ClassDecl(Id(n5),[]),ClassDecl(Id(D),[AttributeDecl(Instance,VarDecl(Id(_),IntType)),AttributeDecl(Static,VarDecl(Id($61),IntType)),AttributeDecl(Instance,VarDecl(Id(_n_),StringType)),MethodDecl(Id(G),Instance,[param(Id(_),ClassType(Id(J))),param(Id(_),ClassType(Id(J))),param(Id(__),ClassType(Id(_2)))],Block([],[]))]),ClassDecl(Id(R),[AttributeDecl(Static,VarDecl(Id($__),ArrayType(26,BoolType)))])])'''
        self.assertTrue(TestAST.test(line, expect, 349))

    def test_350(self):
        line = '''Class pMo_{Var $8B,$k,$7,$0_:Array [Boolean ,4_5_7];Var $m,$M9:Boolean ;Destructor (){} }Class _6{}Class P_:l{Constructor (_q:Array [Boolean ,0xBB];_,_:_){} }Class J:_9{}Class _:K_{}'''
        expect = '''Program([ClassDecl(Id(pMo_),[AttributeDecl(Static,VarDecl(Id($8B),ArrayType(457,BoolType))),AttributeDecl(Static,VarDecl(Id($k),ArrayType(457,BoolType))),AttributeDecl(Static,VarDecl(Id($7),ArrayType(457,BoolType))),AttributeDecl(Static,VarDecl(Id($0_),ArrayType(457,BoolType))),AttributeDecl(Static,VarDecl(Id($m),BoolType)),AttributeDecl(Static,VarDecl(Id($M9),BoolType)),MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(_6),[]),ClassDecl(Id(P_),Id(l),[MethodDecl(Id(Constructor),Instance,[param(Id(_q),ArrayType(187,BoolType)),param(Id(_),ClassType(Id(_))),param(Id(_),ClassType(Id(_)))],Block([],[]))]),ClassDecl(Id(J),Id(_9),[]),ClassDecl(Id(_),Id(K_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 350))

    def test_351(self):
        line = '''Class n{}Class _{Constructor (b:Array [Array [Boolean ,0X5],0122];_N:Array [Array [Array [Array [Array [Boolean ,0x9],0x23],0414_1_15_5],9],0x23]){Continue ;} }'''
        expect = '''Program([ClassDecl(Id(n),[]),ClassDecl(Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(b),ArrayType(82,ArrayType(5,BoolType))),param(Id(_N),ArrayType(35,ArrayType(9,ArrayType(1098349,ArrayType(35,ArrayType(9,BoolType))))))],Block([],[Continue]))])])'''
        self.assertTrue(TestAST.test(line, expect, 351))

    def test_352(self):
        line = '''Class _:O{}Class DqE:TC_{}Class _:_2R0{Var o,$8k1_,_,__,_:Boolean ;Constructor (){} }'''
        expect = '''Program([ClassDecl(Id(_),Id(O),[]),ClassDecl(Id(DqE),Id(TC_),[]),ClassDecl(Id(_),Id(_2R0),[AttributeDecl(Instance,VarDecl(Id(o),BoolType)),AttributeDecl(Static,VarDecl(Id($8k1_),BoolType)),AttributeDecl(Instance,VarDecl(Id(_),BoolType)),AttributeDecl(Instance,VarDecl(Id(__),BoolType)),AttributeDecl(Instance,VarDecl(Id(_),BoolType)),MethodDecl(Id(Constructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 352))

    def test_353(self):
        line = '''Class v:_3__{Constructor (_:String ;_p,n:Int ;Z9:Q;_:y_6;_,H__:Float ;M:_;_,__,_,e:_;o:Array [Array [Int ,0B111],0b10101]){} }'''
        expect = '''Program([ClassDecl(Id(v),Id(_3__),[MethodDecl(Id(Constructor),Instance,[param(Id(_),StringType),param(Id(_p),IntType),param(Id(n),IntType),param(Id(Z9),ClassType(Id(Q))),param(Id(_),ClassType(Id(y_6))),param(Id(_),FloatType),param(Id(H__),FloatType),param(Id(M),ClassType(Id(_))),param(Id(_),ClassType(Id(_))),param(Id(__),ClassType(Id(_))),param(Id(_),ClassType(Id(_))),param(Id(e),ClassType(Id(_))),param(Id(o),ArrayType(21,ArrayType(7,IntType)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 353))

    def test_354(self):
        line = '''Class _{}Class _k4_9_:_{}Class _{}Class y3_{_R(__6h,_,f:Int ){Break ;} }Class J{}'''
        expect = '''Program([ClassDecl(Id(_),[]),ClassDecl(Id(_k4_9_),Id(_),[]),ClassDecl(Id(_),[]),ClassDecl(Id(y3_),[MethodDecl(Id(_R),Instance,[param(Id(__6h),IntType),param(Id(_),IntType),param(Id(f),IntType)],Block([],[Break]))]),ClassDecl(Id(J),[])])'''
        self.assertTrue(TestAST.test(line, expect, 354))

    def test_355(self):
        line = '''Class m{}Class GF:_{Destructor (){}Var $H60:Array [Array [Array [Array [Boolean ,0X9],42],42],0X4F];$_v5(t0:String ;F:O_DB6k){} }'''
        expect = '''Program([ClassDecl(Id(m),[]),ClassDecl(Id(GF),Id(_),[MethodDecl(Id(Destructor),Instance,[],Block([],[])),AttributeDecl(Static,VarDecl(Id($H60),ArrayType(79,ArrayType(42,ArrayType(42,ArrayType(9,BoolType)))))),MethodDecl(Id($_v5),Static,[param(Id(t0),StringType),param(Id(F),ClassType(Id(O_DB6k)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 355))

    def test_356(self):
        line = '''Class j:__{Var $9:Array [Array [Array [Array [Array [Array [Int ,0B1000011],01],0x5F],35],0b111001],041];Destructor (){} }'''
        expect = '''Program([ClassDecl(Id(j),Id(__),[AttributeDecl(Static,VarDecl(Id($9),ArrayType(33,ArrayType(57,ArrayType(35,ArrayType(95,ArrayType(1,ArrayType(67,IntType)))))))),MethodDecl(Id(Destructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 356))

    def test_357(self):
        line = '''Class P:R_{g(_F,_J_7:Boolean ;QJU,F1,O,_09_,IU_:N6;_3:Array [String ,86]){ {} }Constructor (){}Var y,$5mVz:Array [Array [Array [Array [Array [Array [Array [Int ,5847_0],0x4],0b1_000],073],033_0],0X3E],0x4];}'''
        expect = '''Program([ClassDecl(Id(P),Id(R_),[MethodDecl(Id(g),Instance,[param(Id(_F),BoolType),param(Id(_J_7),BoolType),param(Id(QJU),ClassType(Id(N6))),param(Id(F1),ClassType(Id(N6))),param(Id(O),ClassType(Id(N6))),param(Id(_09_),ClassType(Id(N6))),param(Id(IU_),ClassType(Id(N6))),param(Id(_3),ArrayType(86,StringType))],Block([],[Block([],[])])),MethodDecl(Id(Constructor),Instance,[],Block([],[])),AttributeDecl(Instance,VarDecl(Id(y),ArrayType(4,ArrayType(62,ArrayType(216,ArrayType(59,ArrayType(8,ArrayType(4,ArrayType(58470,IntType))))))))),AttributeDecl(Static,VarDecl(Id($5mVz),ArrayType(4,ArrayType(62,ArrayType(216,ArrayType(59,ArrayType(8,ArrayType(4,ArrayType(58470,IntType)))))))))])])'''
        self.assertTrue(TestAST.test(line, expect, 357))

    def test_358(self):
        line = '''Class _:_qz50W__{Var S,X0,$3,__,$C:Boolean ;Constructor (){} }'''
        expect = '''Program([ClassDecl(Id(_),Id(_qz50W__),[AttributeDecl(Instance,VarDecl(Id(S),BoolType)),AttributeDecl(Instance,VarDecl(Id(X0),BoolType)),AttributeDecl(Static,VarDecl(Id($3),BoolType)),AttributeDecl(Instance,VarDecl(Id(__),BoolType)),AttributeDecl(Static,VarDecl(Id($C),BoolType)),MethodDecl(Id(Constructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 358))

    def test_359(self):
        line = '''Class _{$___E2(){}Constructor (O,_:Array [Boolean ,83_25];_76,__i,N,_,M_7,_a__,l1_,X:Int ){} }'''
        expect = '''Program([ClassDecl(Id(_),[MethodDecl(Id($___E2),Static,[],Block([],[])),MethodDecl(Id(Constructor),Instance,[param(Id(O),ArrayType(8325,BoolType)),param(Id(_),ArrayType(8325,BoolType)),param(Id(_76),IntType),param(Id(__i),IntType),param(Id(N),IntType),param(Id(_),IntType),param(Id(M_7),IntType),param(Id(_a__),IntType),param(Id(l1_),IntType),param(Id(X),IntType)],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 359))

    def test_360(self):
        line = '''Class _:_eZ_a_5_{Constructor (__2m8,_8:Array [Int ,1]){} }Class __W_:__9{}'''
        expect = '''Program([ClassDecl(Id(_),Id(_eZ_a_5_),[MethodDecl(Id(Constructor),Instance,[param(Id(__2m8),ArrayType(1,IntType)),param(Id(_8),ArrayType(1,IntType))],Block([],[]))]),ClassDecl(Id(__W_),Id(__9),[])])'''
        self.assertTrue(TestAST.test(line, expect, 360))

    def test_361(self):
        line = '''Class Q__:_{}Class PC_:_b5{}Class _:W7{}Class kJ_95:_M8{}'''
        expect = '''Program([ClassDecl(Id(Q__),Id(_),[]),ClassDecl(Id(PC_),Id(_b5),[]),ClassDecl(Id(_),Id(W7),[]),ClassDecl(Id(kJ_95),Id(_M8),[])])'''
        self.assertTrue(TestAST.test(line, expect, 361))

    def test_362(self):
        line = '''Class __{_(t,___:Array [Int ,0xC2_0];___p_:Array [Array [String ,05],0x51];X:String ;j67h6,_:Boolean ){} }'''
        expect = '''Program([ClassDecl(Id(__),[MethodDecl(Id(_),Instance,[param(Id(t),ArrayType(3104,IntType)),param(Id(___),ArrayType(3104,IntType)),param(Id(___p_),ArrayType(81,ArrayType(5,StringType))),param(Id(X),StringType),param(Id(j67h6),BoolType),param(Id(_),BoolType)],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 362))

    def test_363(self):
        line = '''Class Y{_(_:Int ;_,o5:Array [Float ,6_6]){} }Class dVi:H__{}'''
        expect = '''Program([ClassDecl(Id(Y),[MethodDecl(Id(_),Instance,[param(Id(_),IntType),param(Id(_),ArrayType(66,FloatType)),param(Id(o5),ArrayType(66,FloatType))],Block([],[]))]),ClassDecl(Id(dVi),Id(H__),[])])'''
        self.assertTrue(TestAST.test(line, expect, 363))

    def test_364(self):
        line = '''Class m:__{}Class _zn{}Class __:_1{Constructor (A:Array [Int ,0X23]){} }Class o{}'''
        expect = '''Program([ClassDecl(Id(m),Id(__),[]),ClassDecl(Id(_zn),[]),ClassDecl(Id(__),Id(_1),[MethodDecl(Id(Constructor),Instance,[param(Id(A),ArrayType(35,IntType))],Block([],[]))]),ClassDecl(Id(o),[])])'''
        self.assertTrue(TestAST.test(line, expect, 364))

    def test_365(self):
        line = '''Class s:c7S0{}Class hm:d5{Var $_:Array [Array [Array [Array [Array [String ,3],0b11_0],0x20],0X1A],067];}'''
        expect = '''Program([ClassDecl(Id(s),Id(c7S0),[]),ClassDecl(Id(hm),Id(d5),[AttributeDecl(Static,VarDecl(Id($_),ArrayType(55,ArrayType(26,ArrayType(32,ArrayType(6,ArrayType(3,StringType)))))))])])'''
        self.assertTrue(TestAST.test(line, expect, 365))

    def test_366(self):
        line = '''Class __1:P{Constructor (P:Array [Float ,0B1010]){}Constructor (_S5,i:_8;_q:d;__,_,A,_V1,V:_;Z7,r_:y8x;_6,_,_,_H:Array [Array [Array [Array [Array [Array [Float ,0b1_1_1_101_11],44],7366_30],06_5],05_2],06]){ {Return ;} }}'''
        expect = '''Program([ClassDecl(Id(__1),Id(P),[MethodDecl(Id(Constructor),Instance,[param(Id(P),ArrayType(10,FloatType))],Block([],[])),MethodDecl(Id(Constructor),Instance,[param(Id(_S5),ClassType(Id(_8))),param(Id(i),ClassType(Id(_8))),param(Id(_q),ClassType(Id(d))),param(Id(__),ClassType(Id(_))),param(Id(_),ClassType(Id(_))),param(Id(A),ClassType(Id(_))),param(Id(_V1),ClassType(Id(_))),param(Id(V),ClassType(Id(_))),param(Id(Z7),ClassType(Id(y8x))),param(Id(r_),ClassType(Id(y8x))),param(Id(_6),ArrayType(6,ArrayType(42,ArrayType(53,ArrayType(736630,ArrayType(44,ArrayType(247,FloatType))))))),param(Id(_),ArrayType(6,ArrayType(42,ArrayType(53,ArrayType(736630,ArrayType(44,ArrayType(247,FloatType))))))),param(Id(_),ArrayType(6,ArrayType(42,ArrayType(53,ArrayType(736630,ArrayType(44,ArrayType(247,FloatType))))))),param(Id(_H),ArrayType(6,ArrayType(42,ArrayType(53,ArrayType(736630,ArrayType(44,ArrayType(247,FloatType)))))))],Block([],[Block([],[Return(None)])]))])])'''
        self.assertTrue(TestAST.test(line, expect, 366))

    def test_367(self):
        line = '''Class F:_{E(){}Constructor (_,__:Float ;_v8__,_:String ){}Var $H:Array [Array [String ,07],0X2];}'''
        expect = '''Program([ClassDecl(Id(F),Id(_),[MethodDecl(Id(E),Instance,[],Block([],[])),MethodDecl(Id(Constructor),Instance,[param(Id(_),FloatType),param(Id(__),FloatType),param(Id(_v8__),StringType),param(Id(_),StringType)],Block([],[])),AttributeDecl(Static,VarDecl(Id($H),ArrayType(2,ArrayType(7,StringType))))])])'''
        self.assertTrue(TestAST.test(line, expect, 367))

    def test_368(self):
        line = '''Class _M86{}Class S{$_(){Continue ;Return ;}Var _86:Int ;$p(){} }'''
        expect = '''Program([ClassDecl(Id(_M86),[]),ClassDecl(Id(S),[MethodDecl(Id($_),Static,[],Block([],[Continue,Return(None)])),AttributeDecl(Instance,VarDecl(Id(_86),IntType)),MethodDecl(Id($p),Static,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 368))

    def test_369(self):
        line = '''Class __:M{}Class _U6:O{Constructor (_:Array [Float ,0b1_1];__ce5,_:Array [Int ,0B1_1_1]){} }'''
        expect = '''Program([ClassDecl(Id(__),Id(M),[]),ClassDecl(Id(_U6),Id(O),[MethodDecl(Id(Constructor),Instance,[param(Id(_),ArrayType(3,FloatType)),param(Id(__ce5),ArrayType(7,IntType)),param(Id(_),ArrayType(7,IntType))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 369))

    def test_370(self):
        line = '''Class Py:_T{}Class W6_7{}Class _:_G21{}Class q{$7(){} }Class n6{}Class _7{}'''
        expect = '''Program([ClassDecl(Id(Py),Id(_T),[]),ClassDecl(Id(W6_7),[]),ClassDecl(Id(_),Id(_G21),[]),ClassDecl(Id(q),[MethodDecl(Id($7),Static,[],Block([],[]))]),ClassDecl(Id(n6),[]),ClassDecl(Id(_7),[])])'''
        self.assertTrue(TestAST.test(line, expect, 370))

    def test_371(self):
        line = '''Class _y{f6__(){}$_(z:Array [Array [Array [Array [Array [Float ,0B1],05],56],0X5],0b1100010];df_,_,GF,rP:_n;_9____5e:String ;_:Int ){} }'''
        expect = '''Program([ClassDecl(Id(_y),[MethodDecl(Id(f6__),Instance,[],Block([],[])),MethodDecl(Id($_),Static,[param(Id(z),ArrayType(98,ArrayType(5,ArrayType(56,ArrayType(5,ArrayType(1,FloatType)))))),param(Id(df_),ClassType(Id(_n))),param(Id(_),ClassType(Id(_n))),param(Id(GF),ClassType(Id(_n))),param(Id(rP),ClassType(Id(_n))),param(Id(_9____5e),StringType),param(Id(_),IntType)],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 371))

    def test_372(self):
        line = '''Class _T_K:_8{Destructor (){} }Class W4_9:Ue4Y{}Class __:v{}Class __8_{}'''
        expect = '''Program([ClassDecl(Id(_T_K),Id(_8),[MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(W4_9),Id(Ue4Y),[]),ClassDecl(Id(__),Id(v),[]),ClassDecl(Id(__8_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 372))

    def test_373(self):
        line = '''Class F0:_K{$_4(_3__:Array [Array [Array [String ,94],0B110001],0b1100011]){} }'''
        expect = '''Program([ClassDecl(Id(F0),Id(_K),[MethodDecl(Id($_4),Static,[param(Id(_3__),ArrayType(99,ArrayType(49,ArrayType(94,StringType))))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 373))

    def test_374(self):
        line = '''Class _q_t:Z{Destructor (){ {}Continue ;Return ;}Constructor (){} }'''
        expect = '''Program([ClassDecl(Id(_q_t),Id(Z),[MethodDecl(Id(Destructor),Instance,[],Block([],[Block([],[]),Continue,Return(None)])),MethodDecl(Id(Constructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 374))

    def test_375(self):
        line = '''Class _:k{Var _9_,_4,D,$4_,_:_B;Destructor (){ {}Break ;} }'''
        expect = '''Program([ClassDecl(Id(_),Id(k),[AttributeDecl(Instance,VarDecl(Id(_9_),ClassType(Id(_B)))),AttributeDecl(Instance,VarDecl(Id(_4),ClassType(Id(_B)))),AttributeDecl(Instance,VarDecl(Id(D),ClassType(Id(_B)))),AttributeDecl(Static,VarDecl(Id($4_),ClassType(Id(_B)))),AttributeDecl(Instance,VarDecl(Id(_),ClassType(Id(_B)))),MethodDecl(Id(Destructor),Instance,[],Block([],[Block([],[]),Break]))])])'''
        self.assertTrue(TestAST.test(line, expect, 375))

    def test_376(self):
        line = '''Class ___7{}Class _:dk_{Constructor (b__8:Array [Array [Array [Int ,94],0b11],0b1110];_,X2_:String ;_8:Boolean ;F:Array [Float ,0B1110]){Continue ;} }Class _:p_{}'''
        expect = '''Program([ClassDecl(Id(___7),[]),ClassDecl(Id(_),Id(dk_),[MethodDecl(Id(Constructor),Instance,[param(Id(b__8),ArrayType(14,ArrayType(3,ArrayType(94,IntType)))),param(Id(_),StringType),param(Id(X2_),StringType),param(Id(_8),BoolType),param(Id(F),ArrayType(14,FloatType))],Block([],[Continue]))]),ClassDecl(Id(_),Id(p_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 376))

    def test_377(self):
        line = '''Class _{}Class Z{Constructor (T,m,_:Array [Array [Array [Array [Boolean ,0xA_6],8],0b1],0b1_0]){} }'''
        expect = '''Program([ClassDecl(Id(_),[]),ClassDecl(Id(Z),[MethodDecl(Id(Constructor),Instance,[param(Id(T),ArrayType(2,ArrayType(1,ArrayType(8,ArrayType(166,BoolType))))),param(Id(m),ArrayType(2,ArrayType(1,ArrayType(8,ArrayType(166,BoolType))))),param(Id(_),ArrayType(2,ArrayType(1,ArrayType(8,ArrayType(166,BoolType)))))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 377))

    def test_378(self):
        line = '''Class Sa_{$__3(){} }Class X_z:b{}Class l:t_{Destructor (){} }'''
        expect = '''Program([ClassDecl(Id(Sa_),[MethodDecl(Id($__3),Static,[],Block([],[]))]),ClassDecl(Id(X_z),Id(b),[]),ClassDecl(Id(l),Id(t_),[MethodDecl(Id(Destructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 378))

    def test_379(self):
        line = '''Class _ji_:_{Var N_,$D0:Array [Boolean ,0b1];}Class xI{}'''
        expect = '''Program([ClassDecl(Id(_ji_),Id(_),[AttributeDecl(Instance,VarDecl(Id(N_),ArrayType(1,BoolType))),AttributeDecl(Static,VarDecl(Id($D0),ArrayType(1,BoolType)))]),ClassDecl(Id(xI),[])])'''
        self.assertTrue(TestAST.test(line, expect, 379))

    def test_380(self):
        line = '''Class e88_:_c__j{Var $55_,_:Boolean ;Constructor (V:Array [Array [Array [String ,01],0x1],0B1];_I___,__,X_,c,J_,_:NN5_){} }'''
        expect = '''Program([ClassDecl(Id(e88_),Id(_c__j),[AttributeDecl(Static,VarDecl(Id($55_),BoolType)),AttributeDecl(Instance,VarDecl(Id(_),BoolType)),MethodDecl(Id(Constructor),Instance,[param(Id(V),ArrayType(1,ArrayType(1,ArrayType(1,StringType)))),param(Id(_I___),ClassType(Id(NN5_))),param(Id(__),ClassType(Id(NN5_))),param(Id(X_),ClassType(Id(NN5_))),param(Id(c),ClassType(Id(NN5_))),param(Id(J_),ClassType(Id(NN5_))),param(Id(_),ClassType(Id(NN5_)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 380))

    def test_381(self):
        line = '''Class r3A_P3:__{Destructor (){ {}{}{Var __9:Array [String ,02];Return ;} }_(){} }'''
        expect = '''Program([ClassDecl(Id(r3A_P3),Id(__),[MethodDecl(Id(Destructor),Instance,[],Block([],[Block([],[]),Block([],[]),Block([VarDecl(Id(__9),ArrayType(2,StringType))],[Return(None)])])),MethodDecl(Id(_),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 381))

    def test_382(self):
        line = '''Class L_{Var $9,$v:Array [Array [Array [String ,0x46],0B1],0b110110];}'''
        expect = '''Program([ClassDecl(Id(L_),[AttributeDecl(Static,VarDecl(Id($9),ArrayType(54,ArrayType(1,ArrayType(70,StringType))))),AttributeDecl(Static,VarDecl(Id($v),ArrayType(54,ArrayType(1,ArrayType(70,StringType)))))])])'''
        self.assertTrue(TestAST.test(line, expect, 382))

    def test_383(self):
        line = '''Class E:_{}Class _{Constructor (){} }Class _2:J{}Class j5yb{}Class Q{}'''
        expect = '''Program([ClassDecl(Id(E),Id(_),[]),ClassDecl(Id(_),[MethodDecl(Id(Constructor),Instance,[],Block([],[]))]),ClassDecl(Id(_2),Id(J),[]),ClassDecl(Id(j5yb),[]),ClassDecl(Id(Q),[])])'''
        self.assertTrue(TestAST.test(line, expect, 383))

    def test_384(self):
        line = '''Class _u:_{$W__5I_(){} }Class _{}Class _f{Constructor (n,x6_:Float ){} }'''
        expect = '''Program([ClassDecl(Id(_u),Id(_),[MethodDecl(Id($W__5I_),Static,[],Block([],[]))]),ClassDecl(Id(_),[]),ClassDecl(Id(_f),[MethodDecl(Id(Constructor),Instance,[param(Id(n),FloatType),param(Id(x6_),FloatType)],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 384))

    def test_385(self):
        line = '''Class _Q{}Class __{}Class _D_{Destructor (){} }Class _____7{}'''
        expect = '''Program([ClassDecl(Id(_Q),[]),ClassDecl(Id(__),[]),ClassDecl(Id(_D_),[MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(_____7),[])])'''
        self.assertTrue(TestAST.test(line, expect, 385))

    def test_386(self):
        line = '''Class k:ej_{_(){ {{Continue ;{} }} }}Class C_:_{Var $30:_;_(){} }'''
        expect = '''Program([ClassDecl(Id(k),Id(ej_),[MethodDecl(Id(_),Instance,[],Block([],[Block([],[Block([],[Continue,Block([],[])])])]))]),ClassDecl(Id(C_),Id(_),[AttributeDecl(Static,VarDecl(Id($30),ClassType(Id(_)))),MethodDecl(Id(_),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 386))

    def test_387(self):
        line = '''Class h{Constructor (Z_1__:Array [Array [Int ,0B11],0133];m,u2_,__,V:Boolean ){}Destructor (){} }'''
        expect = '''Program([ClassDecl(Id(h),[MethodDecl(Id(Constructor),Instance,[param(Id(Z_1__),ArrayType(91,ArrayType(3,IntType))),param(Id(m),BoolType),param(Id(u2_),BoolType),param(Id(__),BoolType),param(Id(V),BoolType)],Block([],[])),MethodDecl(Id(Destructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 387))

    def test_388(self):
        line = '''Class pZ:_{}Class _:T_0{$t_8(D:_8;D_46r,P_:Array [Array [Boolean ,0B1],0b1010011]){} }'''
        expect = '''Program([ClassDecl(Id(pZ),Id(_),[]),ClassDecl(Id(_),Id(T_0),[MethodDecl(Id($t_8),Static,[param(Id(D),ClassType(Id(_8))),param(Id(D_46r),ArrayType(83,ArrayType(1,BoolType))),param(Id(P_),ArrayType(83,ArrayType(1,BoolType)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 388))

    def test_389(self):
        line = '''Class _:_x{Constructor (_,_,___1,X:Array [Boolean ,0b101111];y_Y5:yY){} }'''
        expect = '''Program([ClassDecl(Id(_),Id(_x),[MethodDecl(Id(Constructor),Instance,[param(Id(_),ArrayType(47,BoolType)),param(Id(_),ArrayType(47,BoolType)),param(Id(___1),ArrayType(47,BoolType)),param(Id(X),ArrayType(47,BoolType)),param(Id(y_Y5),ClassType(Id(yY)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 389))

    def test_390(self):
        line = '''Class _{}Class _{Constructor (){}Var $2,$8:String ;Constructor (_:Boolean ;r:Int ){Var _7:QLK;} }'''
        expect = '''Program([ClassDecl(Id(_),[]),ClassDecl(Id(_),[MethodDecl(Id(Constructor),Instance,[],Block([],[])),AttributeDecl(Static,VarDecl(Id($2),StringType)),AttributeDecl(Static,VarDecl(Id($8),StringType)),MethodDecl(Id(Constructor),Instance,[param(Id(_),BoolType),param(Id(r),IntType)],Block([VarDecl(Id(_7),ClassType(Id(QLK)))],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 390))

    def test_391(self):
        line = '''Class S1{}Class AOv{}Class S_M0{Constructor (_:_40P;N,__,k,__,w,_4,_J_,P_A,Vb2:Array [String ,032];Y,KAi:Array [Array [Array [Array [Int ,9],18],0x4],0XF]){Break ;} }'''
        expect = '''Program([ClassDecl(Id(S1),[]),ClassDecl(Id(AOv),[]),ClassDecl(Id(S_M0),[MethodDecl(Id(Constructor),Instance,[param(Id(_),ClassType(Id(_40P))),param(Id(N),ArrayType(26,StringType)),param(Id(__),ArrayType(26,StringType)),param(Id(k),ArrayType(26,StringType)),param(Id(__),ArrayType(26,StringType)),param(Id(w),ArrayType(26,StringType)),param(Id(_4),ArrayType(26,StringType)),param(Id(_J_),ArrayType(26,StringType)),param(Id(P_A),ArrayType(26,StringType)),param(Id(Vb2),ArrayType(26,StringType)),param(Id(Y),ArrayType(15,ArrayType(4,ArrayType(18,ArrayType(9,IntType))))),param(Id(KAi),ArrayType(15,ArrayType(4,ArrayType(18,ArrayType(9,IntType)))))],Block([],[Break]))])])'''
        self.assertTrue(TestAST.test(line, expect, 391))

    def test_392(self):
        line = '''Class _m:L{Constructor (_,C__U_:String ;C:Array [String ,0X17_A_1_E6];_T,B2:j;agO8:Int ;_,_,_Ym_,_8:String ;_,g,_:Array [Array [Float ,01],03];_:_3){}Destructor (){} }'''
        expect = '''Program([ClassDecl(Id(_m),Id(L),[MethodDecl(Id(Constructor),Instance,[param(Id(_),StringType),param(Id(C__U_),StringType),param(Id(C),ArrayType(1548774,StringType)),param(Id(_T),ClassType(Id(j))),param(Id(B2),ClassType(Id(j))),param(Id(agO8),IntType),param(Id(_),StringType),param(Id(_),StringType),param(Id(_Ym_),StringType),param(Id(_8),StringType),param(Id(_),ArrayType(3,ArrayType(1,FloatType))),param(Id(g),ArrayType(3,ArrayType(1,FloatType))),param(Id(_),ArrayType(3,ArrayType(1,FloatType))),param(Id(_),ClassType(Id(_3)))],Block([],[])),MethodDecl(Id(Destructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 392))

    def test_393(self):
        line = '''Class b1{Constructor (f:Float ){}Destructor (){} }Class Y:ai9_{}Class L:dD{}'''
        expect = '''Program([ClassDecl(Id(b1),[MethodDecl(Id(Constructor),Instance,[param(Id(f),FloatType)],Block([],[])),MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(Y),Id(ai9_),[]),ClassDecl(Id(L),Id(dD),[])])'''
        self.assertTrue(TestAST.test(line, expect, 393))

    def test_394(self):
        line = '''Class _0{Var _z:Array [Array [Array [String ,01],0B1],070];Destructor (){} }'''
        expect = '''Program([ClassDecl(Id(_0),[AttributeDecl(Instance,VarDecl(Id(_z),ArrayType(56,ArrayType(1,ArrayType(1,StringType))))),MethodDecl(Id(Destructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 394))

    def test_395(self):
        line = '''Class _{Constructor (){} }Class _:ZH0{}Class _9:F_{}Class b_:B{Var bn7,$G_,_,$I:_4TU;}'''
        expect = '''Program([ClassDecl(Id(_),[MethodDecl(Id(Constructor),Instance,[],Block([],[]))]),ClassDecl(Id(_),Id(ZH0),[]),ClassDecl(Id(_9),Id(F_),[]),ClassDecl(Id(b_),Id(B),[AttributeDecl(Instance,VarDecl(Id(bn7),ClassType(Id(_4TU)))),AttributeDecl(Static,VarDecl(Id($G_),ClassType(Id(_4TU)))),AttributeDecl(Instance,VarDecl(Id(_),ClassType(Id(_4TU)))),AttributeDecl(Static,VarDecl(Id($I),ClassType(Id(_4TU))))])])'''
        self.assertTrue(TestAST.test(line, expect, 395))

    def test_396(self):
        line = '''Class _{Var A:String ;Var c,_74:Array [Float ,01];Var _,g_2n:s_Ew_59;}'''
        expect = '''Program([ClassDecl(Id(_),[AttributeDecl(Instance,VarDecl(Id(A),StringType)),AttributeDecl(Instance,VarDecl(Id(c),ArrayType(1,FloatType))),AttributeDecl(Instance,VarDecl(Id(_74),ArrayType(1,FloatType))),AttributeDecl(Instance,VarDecl(Id(_),ClassType(Id(s_Ew_59)))),AttributeDecl(Instance,VarDecl(Id(g_2n),ClassType(Id(s_Ew_59))))])])'''
        self.assertTrue(TestAST.test(line, expect, 396))

    def test_397(self):
        line = '''Class Y:__8{Constructor (f,C:Array [Array [Array [Array [Array [Array [Array [Array [Int ,3_9_0],0B10_0],5],38],0b10001],38],0X7],0B1_01]){} }Class g{}'''
        expect = '''Program([ClassDecl(Id(Y),Id(__8),[MethodDecl(Id(Constructor),Instance,[param(Id(f),ArrayType(5,ArrayType(7,ArrayType(38,ArrayType(17,ArrayType(38,ArrayType(5,ArrayType(4,ArrayType(390,IntType))))))))),param(Id(C),ArrayType(5,ArrayType(7,ArrayType(38,ArrayType(17,ArrayType(38,ArrayType(5,ArrayType(4,ArrayType(390,IntType)))))))))],Block([],[]))]),ClassDecl(Id(g),[])])'''
        self.assertTrue(TestAST.test(line, expect, 397))

    def test_398(self):
        line = '''Class X:m0{}Class iE:EG{Var _0__F,$9:String ;}Class Q21{}'''
        expect = '''Program([ClassDecl(Id(X),Id(m0),[]),ClassDecl(Id(iE),Id(EG),[AttributeDecl(Instance,VarDecl(Id(_0__F),StringType)),AttributeDecl(Static,VarDecl(Id($9),StringType))]),ClassDecl(Id(Q21),[])])'''
        self.assertTrue(TestAST.test(line, expect, 398))

    def test_399(self):
        line = '''Class y_HEW4{_W(){} }Class __8{Var _T,$0,_,_f,$2:Array [Array [Array [Boolean ,1_2],047],0B1010000];}'''
        expect = '''Program([ClassDecl(Id(y_HEW4),[MethodDecl(Id(_W),Instance,[],Block([],[]))]),ClassDecl(Id(__8),[AttributeDecl(Instance,VarDecl(Id(_T),ArrayType(80,ArrayType(39,ArrayType(12,BoolType))))),AttributeDecl(Static,VarDecl(Id($0),ArrayType(80,ArrayType(39,ArrayType(12,BoolType))))),AttributeDecl(Instance,VarDecl(Id(_),ArrayType(80,ArrayType(39,ArrayType(12,BoolType))))),AttributeDecl(Instance,VarDecl(Id(_f),ArrayType(80,ArrayType(39,ArrayType(12,BoolType))))),AttributeDecl(Static,VarDecl(Id($2),ArrayType(80,ArrayType(39,ArrayType(12,BoolType)))))])])'''
        self.assertTrue(TestAST.test(line, expect, 399))

    def test_400(self):
        line = '''Class _7_{}Class b{Constructor (a_,z,_73_,R,__:Array [Array [Array [Array [String ,0x48],49],0X47],49];_u__0j__Kg,_B,_:Kv){} }Class _{}'''
        expect = '''Program([ClassDecl(Id(_7_),[]),ClassDecl(Id(b),[MethodDecl(Id(Constructor),Instance,[param(Id(a_),ArrayType(49,ArrayType(71,ArrayType(49,ArrayType(72,StringType))))),param(Id(z),ArrayType(49,ArrayType(71,ArrayType(49,ArrayType(72,StringType))))),param(Id(_73_),ArrayType(49,ArrayType(71,ArrayType(49,ArrayType(72,StringType))))),param(Id(R),ArrayType(49,ArrayType(71,ArrayType(49,ArrayType(72,StringType))))),param(Id(__),ArrayType(49,ArrayType(71,ArrayType(49,ArrayType(72,StringType))))),param(Id(_u__0j__Kg),ClassType(Id(Kv))),param(Id(_B),ClassType(Id(Kv))),param(Id(_),ClassType(Id(Kv)))],Block([],[]))]),ClassDecl(Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 400))

    def test_401(self):
        line = '''Class _{Constructor (_S:Array [Array [String ,66_7],0x46]){} }Class hTL:C_{}'''
        expect = '''Program([ClassDecl(Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(_S),ArrayType(70,ArrayType(667,StringType)))],Block([],[]))]),ClassDecl(Id(hTL),Id(C_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 401))

    def test_402(self):
        line = '''Class _{Var $8,_:String ;$_(_,_,W__,_8:String ;x94_:Int ;_:Int ;_:t){}Var $F:Array [Int ,0x32];}'''
        expect = '''Program([ClassDecl(Id(_),[AttributeDecl(Static,VarDecl(Id($8),StringType)),AttributeDecl(Instance,VarDecl(Id(_),StringType)),MethodDecl(Id($_),Static,[param(Id(_),StringType),param(Id(_),StringType),param(Id(W__),StringType),param(Id(_8),StringType),param(Id(x94_),IntType),param(Id(_),IntType),param(Id(_),ClassType(Id(t)))],Block([],[])),AttributeDecl(Static,VarDecl(Id($F),ArrayType(50,IntType)))])])'''
        self.assertTrue(TestAST.test(line, expect, 402))

    def test_403(self):
        line = '''Class q{}Class p16{__(){} }Class _{Constructor (_,D:Array [Array [Float ,037],0x9_B]){} }Class _:fKC_5{}Class _:_Ch{}Class _K{}Class l:M4AMx3{}Class _{L(){L::$_7.O()._();} }'''
        expect = '''Program([ClassDecl(Id(q),[]),ClassDecl(Id(p16),[MethodDecl(Id(__),Instance,[],Block([],[]))]),ClassDecl(Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(_),ArrayType(155,ArrayType(31,FloatType))),param(Id(D),ArrayType(155,ArrayType(31,FloatType)))],Block([],[]))]),ClassDecl(Id(_),Id(fKC_5),[]),ClassDecl(Id(_),Id(_Ch),[]),ClassDecl(Id(_K),[]),ClassDecl(Id(l),Id(M4AMx3),[]),ClassDecl(Id(_),[MethodDecl(Id(L),Instance,[],Block([],[Call(CallExpr(FieldAccess(Id(L),Id($_7)),Id(O),[]),Id(_),[])]))])])'''
        self.assertTrue(TestAST.test(line, expect, 403))

    def test_404(self):
        line = '''Class _2:y{$_7_(_oHU:Array [Boolean ,0143];W,_:Array [Array [Array [Array [Array [Boolean ,0X46],0143],0X46],8],0XA4];_,_:Array [Int ,0X46]){} }'''
        expect = '''Program([ClassDecl(Id(_2),Id(y),[MethodDecl(Id($_7_),Static,[param(Id(_oHU),ArrayType(99,BoolType)),param(Id(W),ArrayType(164,ArrayType(8,ArrayType(70,ArrayType(99,ArrayType(70,BoolType)))))),param(Id(_),ArrayType(164,ArrayType(8,ArrayType(70,ArrayType(99,ArrayType(70,BoolType)))))),param(Id(_),ArrayType(70,IntType)),param(Id(_),ArrayType(70,IntType))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 404))

    def test_405(self):
        line = '''Class H5_k:P{}Class Y:_{Constructor (){}Constructor (z2,K46:Array [Array [Int ,0b1],01_6];M_,N,y0,_:D4_){} }'''
        expect = '''Program([ClassDecl(Id(H5_k),Id(P),[]),ClassDecl(Id(Y),Id(_),[MethodDecl(Id(Constructor),Instance,[],Block([],[])),MethodDecl(Id(Constructor),Instance,[param(Id(z2),ArrayType(14,ArrayType(1,IntType))),param(Id(K46),ArrayType(14,ArrayType(1,IntType))),param(Id(M_),ClassType(Id(D4_))),param(Id(N),ClassType(Id(D4_))),param(Id(y0),ClassType(Id(D4_))),param(Id(_),ClassType(Id(D4_)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 405))

    def test_406(self):
        line = '''Class _{r01j(r:Array [String ,0134];l2,lRtdm_1,_,__0K_3,_5___45:Array [Array [Array [Array [Array [String ,0B101_1],0b100010],0134],0134],8];A8:Array [String ,025];_7:String ;_:Array [Int ,0b100010]){} }'''
        expect = '''Program([ClassDecl(Id(_),[MethodDecl(Id(r01j),Instance,[param(Id(r),ArrayType(92,StringType)),param(Id(l2),ArrayType(8,ArrayType(92,ArrayType(92,ArrayType(34,ArrayType(11,StringType)))))),param(Id(lRtdm_1),ArrayType(8,ArrayType(92,ArrayType(92,ArrayType(34,ArrayType(11,StringType)))))),param(Id(_),ArrayType(8,ArrayType(92,ArrayType(92,ArrayType(34,ArrayType(11,StringType)))))),param(Id(__0K_3),ArrayType(8,ArrayType(92,ArrayType(92,ArrayType(34,ArrayType(11,StringType)))))),param(Id(_5___45),ArrayType(8,ArrayType(92,ArrayType(92,ArrayType(34,ArrayType(11,StringType)))))),param(Id(A8),ArrayType(21,StringType)),param(Id(_7),StringType),param(Id(_),ArrayType(34,IntType))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 406))

    def test_407(self):
        line = '''Class T{}Class _D2:TV{Var $_q:Array [Float ,05_5];Var $__,$0_:Boolean ;}'''
        expect = '''Program([ClassDecl(Id(T),[]),ClassDecl(Id(_D2),Id(TV),[AttributeDecl(Static,VarDecl(Id($_q),ArrayType(45,FloatType))),AttributeDecl(Static,VarDecl(Id($__),BoolType)),AttributeDecl(Static,VarDecl(Id($0_),BoolType))])])'''
        self.assertTrue(TestAST.test(line, expect, 407))

    def test_408(self):
        line = '''Class _0:p{}Class U{}Class Q_{Constructor (R:Boolean ;_E:String ){}Constructor (){} }'''
        expect = '''Program([ClassDecl(Id(_0),Id(p),[]),ClassDecl(Id(U),[]),ClassDecl(Id(Q_),[MethodDecl(Id(Constructor),Instance,[param(Id(R),BoolType),param(Id(_E),StringType)],Block([],[])),MethodDecl(Id(Constructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 408))

    def test_409(self):
        line = '''Class w6:_Z1{}Class _:_9_311Cn{}Class __P983_o6{}Class G3{}Class _{}'''
        expect = '''Program([ClassDecl(Id(w6),Id(_Z1),[]),ClassDecl(Id(_),Id(_9_311Cn),[]),ClassDecl(Id(__P983_o6),[]),ClassDecl(Id(G3),[]),ClassDecl(Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 409))

    def test_410(self):
        line = '''Class __{}Class _634:_w{}Class yj{Var _,$s,_:Array [Array [Array [Float ,0x6],2],057];}'''
        expect = '''Program([ClassDecl(Id(__),[]),ClassDecl(Id(_634),Id(_w),[]),ClassDecl(Id(yj),[AttributeDecl(Instance,VarDecl(Id(_),ArrayType(47,ArrayType(2,ArrayType(6,FloatType))))),AttributeDecl(Static,VarDecl(Id($s),ArrayType(47,ArrayType(2,ArrayType(6,FloatType))))),AttributeDecl(Instance,VarDecl(Id(_),ArrayType(47,ArrayType(2,ArrayType(6,FloatType)))))])])'''
        self.assertTrue(TestAST.test(line, expect, 410))

    def test_411(self):
        line = '''Class _101:_i03R{}Class _:cF_{}Class Y:_{Var $s,$7_,$__:Array [Array [Array [Float ,53],0b1011000],0B111001];}'''
        expect = '''Program([ClassDecl(Id(_101),Id(_i03R),[]),ClassDecl(Id(_),Id(cF_),[]),ClassDecl(Id(Y),Id(_),[AttributeDecl(Static,VarDecl(Id($s),ArrayType(57,ArrayType(88,ArrayType(53,FloatType))))),AttributeDecl(Static,VarDecl(Id($7_),ArrayType(57,ArrayType(88,ArrayType(53,FloatType))))),AttributeDecl(Static,VarDecl(Id($__),ArrayType(57,ArrayType(88,ArrayType(53,FloatType)))))])])'''
        self.assertTrue(TestAST.test(line, expect, 411))

    def test_412(self):
        line = '''Class c2{Constructor (){ {Break ;} }}Class S:c__0_a{Constructor (b:C){} }Class E8:y_{}'''
        expect = '''Program([ClassDecl(Id(c2),[MethodDecl(Id(Constructor),Instance,[],Block([],[Block([],[Break])]))]),ClassDecl(Id(S),Id(c__0_a),[MethodDecl(Id(Constructor),Instance,[param(Id(b),ClassType(Id(C)))],Block([],[]))]),ClassDecl(Id(E8),Id(y_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 412))

    def test_413(self):
        line = '''Class _4:__{$1(pn__o_,___9,_:Array [Int ,0x58];_:Array [Boolean ,03_41_7]){New _E()._().h().__.E._();}Var $__,_2APN,$6,$n:Boolean ;}'''
        expect = '''Program([ClassDecl(Id(_4),Id(__),[MethodDecl(Id($1),Static,[param(Id(pn__o_),ArrayType(88,IntType)),param(Id(___9),ArrayType(88,IntType)),param(Id(_),ArrayType(88,IntType)),param(Id(_),ArrayType(1807,BoolType))],Block([],[Call(FieldAccess(FieldAccess(CallExpr(CallExpr(NewExpr(Id(_E),[]),Id(_),[]),Id(h),[]),Id(__)),Id(E)),Id(_),[])])),AttributeDecl(Static,VarDecl(Id($__),BoolType)),AttributeDecl(Instance,VarDecl(Id(_2APN),BoolType)),AttributeDecl(Static,VarDecl(Id($6),BoolType)),AttributeDecl(Static,VarDecl(Id($n),BoolType))])])'''
        self.assertTrue(TestAST.test(line, expect, 413))

    def test_414(self):
        line = '''Class _{}Class k39:_{}Class KwNB_:o_{}Class xoO4{}Class _U{Var $_:kR;}Class ___:F{}'''
        expect = '''Program([ClassDecl(Id(_),[]),ClassDecl(Id(k39),Id(_),[]),ClassDecl(Id(KwNB_),Id(o_),[]),ClassDecl(Id(xoO4),[]),ClassDecl(Id(_U),[AttributeDecl(Static,VarDecl(Id($_),ClassType(Id(kR))))]),ClassDecl(Id(___),Id(F),[])])'''
        self.assertTrue(TestAST.test(line, expect, 414))

    def test_415(self):
        line = '''Class u{Var _d,_:Array [Array [Float ,0XE_4_6_6],011];}Class _{}'''
        expect = '''Program([ClassDecl(Id(u),[AttributeDecl(Instance,VarDecl(Id(_d),ArrayType(9,ArrayType(58470,FloatType)))),AttributeDecl(Instance,VarDecl(Id(_),ArrayType(9,ArrayType(58470,FloatType))))]),ClassDecl(Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 415))

    def test_416(self):
        line = '''Class _6:X_{$83_(___02:Array [Array [Array [Float ,0X9],0xD],96];d,m,__:J;x6_:_9WNV85_o;d:Array [Array [String ,0X1A],0B1];u:r58l){}Constructor (J,e_:String ){} }Class _{}'''
        expect = '''Program([ClassDecl(Id(_6),Id(X_),[MethodDecl(Id($83_),Static,[param(Id(___02),ArrayType(96,ArrayType(13,ArrayType(9,FloatType)))),param(Id(d),ClassType(Id(J))),param(Id(m),ClassType(Id(J))),param(Id(__),ClassType(Id(J))),param(Id(x6_),ClassType(Id(_9WNV85_o))),param(Id(d),ArrayType(1,ArrayType(26,StringType))),param(Id(u),ClassType(Id(r58l)))],Block([],[])),MethodDecl(Id(Constructor),Instance,[param(Id(J),StringType),param(Id(e_),StringType)],Block([],[]))]),ClassDecl(Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 416))

    def test_417(self):
        line = '''Class H_{Constructor (){}Destructor (){} }Class S:m{Constructor (_i105:Int ){} }'''
        expect = '''Program([ClassDecl(Id(H_),[MethodDecl(Id(Constructor),Instance,[],Block([],[])),MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(S),Id(m),[MethodDecl(Id(Constructor),Instance,[param(Id(_i105),IntType)],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 417))

    def test_418(self):
        line = '''Class __{}Class b:_K{Destructor (){Break ;Continue ;}Destructor (){Return ;}$Z_61f10no(){} }'''
        expect = '''Program([ClassDecl(Id(__),[]),ClassDecl(Id(b),Id(_K),[MethodDecl(Id(Destructor),Instance,[],Block([],[Break,Continue])),MethodDecl(Id(Destructor),Instance,[],Block([],[Return(None)])),MethodDecl(Id($Z_61f10no),Static,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 418))

    def test_419(self):
        line = '''Class _1:J_{g1k(_,U,_,M,_:Array [Boolean ,0140];m5_,S_z7:Float ;S:Array [String ,5_8]){} }'''
        expect = '''Program([ClassDecl(Id(_1),Id(J_),[MethodDecl(Id(g1k),Instance,[param(Id(_),ArrayType(96,BoolType)),param(Id(U),ArrayType(96,BoolType)),param(Id(_),ArrayType(96,BoolType)),param(Id(M),ArrayType(96,BoolType)),param(Id(_),ArrayType(96,BoolType)),param(Id(m5_),FloatType),param(Id(S_z7),FloatType),param(Id(S),ArrayType(58,StringType))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 419))

    def test_420(self):
        line = '''Class _{Destructor (){}Constructor (l,c,_0v:q43v){Continue ;} }'''
        expect = '''Program([ClassDecl(Id(_),[MethodDecl(Id(Destructor),Instance,[],Block([],[])),MethodDecl(Id(Constructor),Instance,[param(Id(l),ClassType(Id(q43v))),param(Id(c),ClassType(Id(q43v))),param(Id(_0v),ClassType(Id(q43v)))],Block([],[Continue]))])])'''
        self.assertTrue(TestAST.test(line, expect, 420))

    def test_421(self):
        line = '''Class _7_:__{Constructor (R:Array [Array [String ,5],0XDA]){} }Class z:_{}'''
        expect = '''Program([ClassDecl(Id(_7_),Id(__),[MethodDecl(Id(Constructor),Instance,[param(Id(R),ArrayType(218,ArrayType(5,StringType)))],Block([],[]))]),ClassDecl(Id(z),Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 421))

    def test_422(self):
        line = '''Class _M:_e{}Class _:m{}Class E_8{}Class _:L{}Class _K:oo{}'''
        expect = '''Program([ClassDecl(Id(_M),Id(_e),[]),ClassDecl(Id(_),Id(m),[]),ClassDecl(Id(E_8),[]),ClassDecl(Id(_),Id(L),[]),ClassDecl(Id(_K),Id(oo),[])])'''
        self.assertTrue(TestAST.test(line, expect, 422))

    def test_423(self):
        line = '''Class p{Constructor (){}Destructor (){Continue ;} }Class _{}Class _:_{Var $966,$W,$mX:_;Constructor (){}Var $5,l,$_:Float ;}'''
        expect = '''Program([ClassDecl(Id(p),[MethodDecl(Id(Constructor),Instance,[],Block([],[])),MethodDecl(Id(Destructor),Instance,[],Block([],[Continue]))]),ClassDecl(Id(_),[]),ClassDecl(Id(_),Id(_),[AttributeDecl(Static,VarDecl(Id($966),ClassType(Id(_)))),AttributeDecl(Static,VarDecl(Id($W),ClassType(Id(_)))),AttributeDecl(Static,VarDecl(Id($mX),ClassType(Id(_)))),MethodDecl(Id(Constructor),Instance,[],Block([],[])),AttributeDecl(Static,VarDecl(Id($5),FloatType)),AttributeDecl(Instance,VarDecl(Id(l),FloatType)),AttributeDecl(Static,VarDecl(Id($_),FloatType))])])'''
        self.assertTrue(TestAST.test(line, expect, 423))

    def test_424(self):
        line = '''Class K:i_5{}Class __{Constructor (_vz0_:_){ {Return ;} }}'''
        expect = '''Program([ClassDecl(Id(K),Id(i_5),[]),ClassDecl(Id(__),[MethodDecl(Id(Constructor),Instance,[param(Id(_vz0_),ClassType(Id(_)))],Block([],[Block([],[Return(None)])]))])])'''
        self.assertTrue(TestAST.test(line, expect, 424))

    def test_425(self):
        line = '''Class n:_VZ{__5P(_h9,c_09m_m:B_G3){}Var u:y_;}Class toI__23_:E3{}'''
        expect = '''Program([ClassDecl(Id(n),Id(_VZ),[MethodDecl(Id(__5P),Instance,[param(Id(_h9),ClassType(Id(B_G3))),param(Id(c_09m_m),ClassType(Id(B_G3)))],Block([],[])),AttributeDecl(Instance,VarDecl(Id(u),ClassType(Id(y_))))]),ClassDecl(Id(toI__23_),Id(E3),[])])'''
        self.assertTrue(TestAST.test(line, expect, 425))

    def test_426(self):
        line = '''Class U{$_e8(S:Int ;_:Array [Boolean ,0X60];b:Array [Array [Int ,30],0503]){Continue ;} }'''
        expect = '''Program([ClassDecl(Id(U),[MethodDecl(Id($_e8),Static,[param(Id(S),IntType),param(Id(_),ArrayType(96,BoolType)),param(Id(b),ArrayType(323,ArrayType(30,IntType)))],Block([],[Continue]))])])'''
        self.assertTrue(TestAST.test(line, expect, 426))

    def test_427(self):
        line = '''Class _V5_HN{Destructor (){Var _:Array [Int ,0X6];}Constructor (){} }'''
        expect = '''Program([ClassDecl(Id(_V5_HN),[MethodDecl(Id(Destructor),Instance,[],Block([VarDecl(Id(_),ArrayType(6,IntType))],[])),MethodDecl(Id(Constructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 427))

    def test_428(self):
        line = '''Class _Q3a8{$Vg__(MZ,_:Int ;_,_,C1zk,_,__4,_,__:_){Break ;} }'''
        expect = '''Program([ClassDecl(Id(_Q3a8),[MethodDecl(Id($Vg__),Static,[param(Id(MZ),IntType),param(Id(_),IntType),param(Id(_),ClassType(Id(_))),param(Id(_),ClassType(Id(_))),param(Id(C1zk),ClassType(Id(_))),param(Id(_),ClassType(Id(_))),param(Id(__4),ClassType(Id(_))),param(Id(_),ClassType(Id(_))),param(Id(__),ClassType(Id(_)))],Block([],[Break]))])])'''
        self.assertTrue(TestAST.test(line, expect, 428))

    def test_429(self):
        line = '''Class C__R9_{_C_(_,_5:R_;_33:Int ){}$M(){}Var $_,$_:Array [Float ,0b111010];}'''
        expect = '''Program([ClassDecl(Id(C__R9_),[MethodDecl(Id(_C_),Instance,[param(Id(_),ClassType(Id(R_))),param(Id(_5),ClassType(Id(R_))),param(Id(_33),IntType)],Block([],[])),MethodDecl(Id($M),Static,[],Block([],[])),AttributeDecl(Static,VarDecl(Id($_),ArrayType(58,FloatType))),AttributeDecl(Static,VarDecl(Id($_),ArrayType(58,FloatType)))])])'''
        self.assertTrue(TestAST.test(line, expect, 429))

    def test_430(self):
        line = '''Class ___:_{}Class _:q{Destructor (){}Var $2,__2,$7n1y7_,e__9X9:Array [Array [String ,0b1011110],076];}Class A7{}'''
        expect = '''Program([ClassDecl(Id(___),Id(_),[]),ClassDecl(Id(_),Id(q),[MethodDecl(Id(Destructor),Instance,[],Block([],[])),AttributeDecl(Static,VarDecl(Id($2),ArrayType(62,ArrayType(94,StringType)))),AttributeDecl(Instance,VarDecl(Id(__2),ArrayType(62,ArrayType(94,StringType)))),AttributeDecl(Static,VarDecl(Id($7n1y7_),ArrayType(62,ArrayType(94,StringType)))),AttributeDecl(Instance,VarDecl(Id(e__9X9),ArrayType(62,ArrayType(94,StringType))))]),ClassDecl(Id(A7),[])])'''
        self.assertTrue(TestAST.test(line, expect, 430))

    def test_431(self):
        line = '''Class _:J{Destructor (){}Constructor (){}Constructor (s:Array [Array [Array [Int ,96_0_50],5],0b11001]){} }'''
        expect = '''Program([ClassDecl(Id(_),Id(J),[MethodDecl(Id(Destructor),Instance,[],Block([],[])),MethodDecl(Id(Constructor),Instance,[],Block([],[])),MethodDecl(Id(Constructor),Instance,[param(Id(s),ArrayType(25,ArrayType(5,ArrayType(96050,IntType))))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 431))

    def test_432(self):
        line = '''Class _:q_{Var $7M:_9;g(G_6IWG05_,_:Array [Array [Array [Array [Int ,03_6],0106],1],56]){} }Class l:Q{}'''
        expect = '''Program([ClassDecl(Id(_),Id(q_),[AttributeDecl(Static,VarDecl(Id($7M),ClassType(Id(_9)))),MethodDecl(Id(g),Instance,[param(Id(G_6IWG05_),ArrayType(56,ArrayType(1,ArrayType(70,ArrayType(30,IntType))))),param(Id(_),ArrayType(56,ArrayType(1,ArrayType(70,ArrayType(30,IntType)))))],Block([],[]))]),ClassDecl(Id(l),Id(Q),[])])'''
        self.assertTrue(TestAST.test(line, expect, 432))

    def test_433(self):
        line = '''Class _{Destructor (){} }Class _{}Class _:_6_0_{Var $1,_:Array [Array [Array [Float ,074],0B1],2];}Class j:_A4_{}Class t:z9{}Class _{Constructor (){_::$__._();}Var $6_,$9_F,$20,$_D2,$7,$_N_:hp;}'''
        expect = '''Program([ClassDecl(Id(_),[MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(_),[]),ClassDecl(Id(_),Id(_6_0_),[AttributeDecl(Static,VarDecl(Id($1),ArrayType(2,ArrayType(1,ArrayType(60,FloatType))))),AttributeDecl(Instance,VarDecl(Id(_),ArrayType(2,ArrayType(1,ArrayType(60,FloatType)))))]),ClassDecl(Id(j),Id(_A4_),[]),ClassDecl(Id(t),Id(z9),[]),ClassDecl(Id(_),[MethodDecl(Id(Constructor),Instance,[],Block([],[Call(FieldAccess(Id(_),Id($__)),Id(_),[])])),AttributeDecl(Static,VarDecl(Id($6_),ClassType(Id(hp)))),AttributeDecl(Static,VarDecl(Id($9_F),ClassType(Id(hp)))),AttributeDecl(Static,VarDecl(Id($20),ClassType(Id(hp)))),AttributeDecl(Static,VarDecl(Id($_D2),ClassType(Id(hp)))),AttributeDecl(Static,VarDecl(Id($7),ClassType(Id(hp)))),AttributeDecl(Static,VarDecl(Id($_N_),ClassType(Id(hp))))])])'''
        self.assertTrue(TestAST.test(line, expect, 433))

    def test_434(self):
        line = '''Class _{}Class s{}Class _:u3C{$Q(){} }Class _Pb_72:nDN{Destructor (){} }Class __7:B{}'''
        expect = '''Program([ClassDecl(Id(_),[]),ClassDecl(Id(s),[]),ClassDecl(Id(_),Id(u3C),[MethodDecl(Id($Q),Static,[],Block([],[]))]),ClassDecl(Id(_Pb_72),Id(nDN),[MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(__7),Id(B),[])])'''
        self.assertTrue(TestAST.test(line, expect, 434))

    def test_435(self):
        line = '''Class G_:__{Var $6_u17:Float ;}Class _{}Class _:_{Destructor (){} }Class L:L{Var $_T2:Array [Int ,03];}'''
        expect = '''Program([ClassDecl(Id(G_),Id(__),[AttributeDecl(Static,VarDecl(Id($6_u17),FloatType))]),ClassDecl(Id(_),[]),ClassDecl(Id(_),Id(_),[MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(L),Id(L),[AttributeDecl(Static,VarDecl(Id($_T2),ArrayType(3,IntType)))])])'''
        self.assertTrue(TestAST.test(line, expect, 435))

    def test_436(self):
        line = '''Class _d:_{}Class _14:h7{}Class Yg8X:__{Var $43:Array [Boolean ,0B10_01];}Class _9_0_:s{Destructor (){} }Class N_:_{}'''
        expect = '''Program([ClassDecl(Id(_d),Id(_),[]),ClassDecl(Id(_14),Id(h7),[]),ClassDecl(Id(Yg8X),Id(__),[AttributeDecl(Static,VarDecl(Id($43),ArrayType(9,BoolType)))]),ClassDecl(Id(_9_0_),Id(s),[MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(N_),Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 436))

    def test_437(self):
        line = '''Class _N:C{Var d,$D:Array [Array [Int ,86],0B1001];}Class _86_{Destructor (){} }'''
        expect = '''Program([ClassDecl(Id(_N),Id(C),[AttributeDecl(Instance,VarDecl(Id(d),ArrayType(9,ArrayType(86,IntType)))),AttributeDecl(Static,VarDecl(Id($D),ArrayType(9,ArrayType(86,IntType))))]),ClassDecl(Id(_86_),[MethodDecl(Id(Destructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 437))

    def test_438(self):
        line = '''Class x9_45{}Class _Zd81_:_{}Class v{Var $U,$6:Array [Array [Array [Int ,071],0x7],033];}'''
        expect = '''Program([ClassDecl(Id(x9_45),[]),ClassDecl(Id(_Zd81_),Id(_),[]),ClassDecl(Id(v),[AttributeDecl(Static,VarDecl(Id($U),ArrayType(27,ArrayType(7,ArrayType(57,IntType))))),AttributeDecl(Static,VarDecl(Id($6),ArrayType(27,ArrayType(7,ArrayType(57,IntType)))))])])'''
        self.assertTrue(TestAST.test(line, expect, 438))

    def test_439(self):
        line = '''Class _k:I{_9(_,_v,q1W3_,_5H3:Array [Array [Array [Float ,0XF3],07],06]){} }'''
        expect = '''Program([ClassDecl(Id(_k),Id(I),[MethodDecl(Id(_9),Instance,[param(Id(_),ArrayType(6,ArrayType(7,ArrayType(243,FloatType)))),param(Id(_v),ArrayType(6,ArrayType(7,ArrayType(243,FloatType)))),param(Id(q1W3_),ArrayType(6,ArrayType(7,ArrayType(243,FloatType)))),param(Id(_5H3),ArrayType(6,ArrayType(7,ArrayType(243,FloatType))))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 439))

    def test_440(self):
        line = '''Class _{}Class _:_Az4{Destructor (){} }Class _{}Class y:b___R_{}'''
        expect = '''Program([ClassDecl(Id(_),[]),ClassDecl(Id(_),Id(_Az4),[MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(_),[]),ClassDecl(Id(y),Id(b___R_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 440))

    def test_441(self):
        line = '''Class i{$9(_,o____63:Array [Array [Int ,0XF9],0X6]){Return ;} }'''
        expect = '''Program([ClassDecl(Id(i),[MethodDecl(Id($9),Static,[param(Id(_),ArrayType(6,ArrayType(249,IntType))),param(Id(o____63),ArrayType(6,ArrayType(249,IntType)))],Block([],[Return(None)]))])])'''
        self.assertTrue(TestAST.test(line, expect, 441))

    def test_442(self):
        line = '''Class cm_b8_{Constructor (e_:Array [Int ,034];AZ:Array [Float ,0X3B];_,V4:Array [Array [Float ,034],0x2F]){} }'''
        expect = '''Program([ClassDecl(Id(cm_b8_),[MethodDecl(Id(Constructor),Instance,[param(Id(e_),ArrayType(28,IntType)),param(Id(AZ),ArrayType(59,FloatType)),param(Id(_),ArrayType(47,ArrayType(28,FloatType))),param(Id(V4),ArrayType(47,ArrayType(28,FloatType)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 442))

    def test_443(self):
        line = '''Class h_{$j(xG,q_:_;__:Boolean ;_,UHh:q;C,T:Array [Boolean ,0x1]){} }'''
        expect = '''Program([ClassDecl(Id(h_),[MethodDecl(Id($j),Static,[param(Id(xG),ClassType(Id(_))),param(Id(q_),ClassType(Id(_))),param(Id(__),BoolType),param(Id(_),ClassType(Id(q))),param(Id(UHh),ClassType(Id(q))),param(Id(C),ArrayType(1,BoolType)),param(Id(T),ArrayType(1,BoolType))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 443))

    def test_444(self):
        line = '''Class T61:_{Var $7:Int ;j__(E:String ;_:P;i3o0o:String ){Break ;} }Class K9{}'''
        expect = '''Program([ClassDecl(Id(T61),Id(_),[AttributeDecl(Static,VarDecl(Id($7),IntType)),MethodDecl(Id(j__),Instance,[param(Id(E),StringType),param(Id(_),ClassType(Id(P))),param(Id(i3o0o),StringType)],Block([],[Break]))]),ClassDecl(Id(K9),[])])'''
        self.assertTrue(TestAST.test(line, expect, 444))

    def test_445(self):
        line = '''Class m:_{}Class _4h{Constructor (__S:_;l04:Int ){} }Class _{$_P(){} }Class P:_s_R_{}'''
        expect = '''Program([ClassDecl(Id(m),Id(_),[]),ClassDecl(Id(_4h),[MethodDecl(Id(Constructor),Instance,[param(Id(__S),ClassType(Id(_))),param(Id(l04),IntType)],Block([],[]))]),ClassDecl(Id(_),[MethodDecl(Id($_P),Static,[],Block([],[]))]),ClassDecl(Id(P),Id(_s_R_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 445))

    def test_446(self):
        line = '''Class _r{}Class r3{r(D,_2,K8:Array [Array [Int ,0B1100010],12]){} }Class k4{}'''
        expect = '''Program([ClassDecl(Id(_r),[]),ClassDecl(Id(r3),[MethodDecl(Id(r),Instance,[param(Id(D),ArrayType(12,ArrayType(98,IntType))),param(Id(_2),ArrayType(12,ArrayType(98,IntType))),param(Id(K8),ArrayType(12,ArrayType(98,IntType)))],Block([],[]))]),ClassDecl(Id(k4),[])])'''
        self.assertTrue(TestAST.test(line, expect, 446))

    def test_447(self):
        line = '''Class H{_(_6o11,jq_,_,P6_,G:y){ {} }}Class _0___L_{}Class R1{}'''
        expect = '''Program([ClassDecl(Id(H),[MethodDecl(Id(_),Instance,[param(Id(_6o11),ClassType(Id(y))),param(Id(jq_),ClassType(Id(y))),param(Id(_),ClassType(Id(y))),param(Id(P6_),ClassType(Id(y))),param(Id(G),ClassType(Id(y)))],Block([],[Block([],[])]))]),ClassDecl(Id(_0___L_),[]),ClassDecl(Id(R1),[])])'''
        self.assertTrue(TestAST.test(line, expect, 447))

    def test_448(self):
        line = '''Class _:X{Destructor (){}$M(){Continue ;}Var D,$1,E:_;Destructor (){} }Class e{}Class P:x___{}Class C{}'''
        expect = '''Program([ClassDecl(Id(_),Id(X),[MethodDecl(Id(Destructor),Instance,[],Block([],[])),MethodDecl(Id($M),Static,[],Block([],[Continue])),AttributeDecl(Instance,VarDecl(Id(D),ClassType(Id(_)))),AttributeDecl(Static,VarDecl(Id($1),ClassType(Id(_)))),AttributeDecl(Instance,VarDecl(Id(E),ClassType(Id(_)))),MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(e),[]),ClassDecl(Id(P),Id(x___),[]),ClassDecl(Id(C),[])])'''
        self.assertTrue(TestAST.test(line, expect, 448))

    def test_449(self):
        line = '''Class yf:_{}Class PZ_:n{$y(_:Array [String ,0b10]){} }Class P{}'''
        expect = '''Program([ClassDecl(Id(yf),Id(_),[]),ClassDecl(Id(PZ_),Id(n),[MethodDecl(Id($y),Static,[param(Id(_),ArrayType(2,StringType))],Block([],[]))]),ClassDecl(Id(P),[])])'''
        self.assertTrue(TestAST.test(line, expect, 449))

    def test_450(self):
        line = '''Class y:___{Destructor (){ {} }Constructor (){ {} }}Class _{}Class Q:___R{}'''
        expect = '''Program([ClassDecl(Id(y),Id(___),[MethodDecl(Id(Destructor),Instance,[],Block([],[Block([],[])])),MethodDecl(Id(Constructor),Instance,[],Block([],[Block([],[])]))]),ClassDecl(Id(_),[]),ClassDecl(Id(Q),Id(___R),[])])'''
        self.assertTrue(TestAST.test(line, expect, 450))

    def test_451(self):
        line = '''Class _{}Class h:_{Var _Z:Array [Array [Int ,0b1_00_0],022];}'''
        expect = '''Program([ClassDecl(Id(_),[]),ClassDecl(Id(h),Id(_),[AttributeDecl(Instance,VarDecl(Id(_Z),ArrayType(18,ArrayType(8,IntType))))])])'''
        self.assertTrue(TestAST.test(line, expect, 451))

    def test_452(self):
        line = '''Class _i:_{fQY(tM:Array [Boolean ,0B1_0];_:Array [Array [Array [Float ,0B1],0b11010],0X18]){} }'''
        expect = '''Program([ClassDecl(Id(_i),Id(_),[MethodDecl(Id(fQY),Instance,[param(Id(tM),ArrayType(2,BoolType)),param(Id(_),ArrayType(24,ArrayType(26,ArrayType(1,FloatType))))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 452))

    def test_453(self):
        line = '''Class p_{Destructor (){} }Class _a_P:_7l{}Class X:_{}Class jA{}Class n:_2_{}'''
        expect = '''Program([ClassDecl(Id(p_),[MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(_a_P),Id(_7l),[]),ClassDecl(Id(X),Id(_),[]),ClassDecl(Id(jA),[]),ClassDecl(Id(n),Id(_2_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 453))

    def test_454(self):
        line = '''Class __{}Class R0{}Class _d{}Class _{}Class __1gV_:_RC{}'''
        expect = '''Program([ClassDecl(Id(__),[]),ClassDecl(Id(R0),[]),ClassDecl(Id(_d),[]),ClassDecl(Id(_),[]),ClassDecl(Id(__1gV_),Id(_RC),[])])'''
        self.assertTrue(TestAST.test(line, expect, 454))

    def test_455(self):
        line = '''Class O{}Class z{$1(){}_(_6,_,V7:Array [Array [String ,0B110001],0x7_0];q,__KM0_0,W:Int ){}Destructor (){} }'''
        expect = '''Program([ClassDecl(Id(O),[]),ClassDecl(Id(z),[MethodDecl(Id($1),Static,[],Block([],[])),MethodDecl(Id(_),Instance,[param(Id(_6),ArrayType(112,ArrayType(49,StringType))),param(Id(_),ArrayType(112,ArrayType(49,StringType))),param(Id(V7),ArrayType(112,ArrayType(49,StringType))),param(Id(q),IntType),param(Id(__KM0_0),IntType),param(Id(W),IntType)],Block([],[])),MethodDecl(Id(Destructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 455))

    def test_456(self):
        line = '''Class v:c{}Class _:E_F6_{}Class t:_{Destructor (){} }Class k5{}'''
        expect = '''Program([ClassDecl(Id(v),Id(c),[]),ClassDecl(Id(_),Id(E_F6_),[]),ClassDecl(Id(t),Id(_),[MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(k5),[])])'''
        self.assertTrue(TestAST.test(line, expect, 456))

    def test_457(self):
        line = '''Class D:z33{}Class v2{_(_x__,_8,_JH7__6q,X:Int ){Continue ;} }Class _{}'''
        expect = '''Program([ClassDecl(Id(D),Id(z33),[]),ClassDecl(Id(v2),[MethodDecl(Id(_),Instance,[param(Id(_x__),IntType),param(Id(_8),IntType),param(Id(_JH7__6q),IntType),param(Id(X),IntType)],Block([],[Continue]))]),ClassDecl(Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 457))

    def test_458(self):
        line = '''Class _n:p{}Class S{}Class __{}Class h9{$_k(_7:j;gb:_;_b:Boolean ;_3d:String ){} }'''
        expect = '''Program([ClassDecl(Id(_n),Id(p),[]),ClassDecl(Id(S),[]),ClassDecl(Id(__),[]),ClassDecl(Id(h9),[MethodDecl(Id($_k),Static,[param(Id(_7),ClassType(Id(j))),param(Id(gb),ClassType(Id(_))),param(Id(_b),BoolType),param(Id(_3d),StringType)],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 458))

    def test_459(self):
        line = '''Class Z:z2{b_(Yo,_:Array [Array [String ,0B1010001],7];A,_7:n6;O:Array [String ,7_2];L9_4:_;_2_:Array [Boolean ,07_7_52];vX9_,l,_,b_:F;_,_2,A:Array [Array [Boolean ,02],07200_1]){}Destructor (){} }'''
        expect = '''Program([ClassDecl(Id(Z),Id(z2),[MethodDecl(Id(b_),Instance,[param(Id(Yo),ArrayType(7,ArrayType(81,StringType))),param(Id(_),ArrayType(7,ArrayType(81,StringType))),param(Id(A),ClassType(Id(n6))),param(Id(_7),ClassType(Id(n6))),param(Id(O),ArrayType(72,StringType)),param(Id(L9_4),ClassType(Id(_))),param(Id(_2_),ArrayType(4074,BoolType)),param(Id(vX9_),ClassType(Id(F))),param(Id(l),ClassType(Id(F))),param(Id(_),ClassType(Id(F))),param(Id(b_),ClassType(Id(F))),param(Id(_),ArrayType(29697,ArrayType(2,BoolType))),param(Id(_2),ArrayType(29697,ArrayType(2,BoolType))),param(Id(A),ArrayType(29697,ArrayType(2,BoolType)))],Block([],[])),MethodDecl(Id(Destructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 459))

    def test_460(self):
        line = '''Class V_9_{_(aH:Array [Int ,06_5_3]){Continue ;}Destructor (){}Var $2h:Array [String ,0B1];}'''
        expect = '''Program([ClassDecl(Id(V_9_),[MethodDecl(Id(_),Instance,[param(Id(aH),ArrayType(427,IntType))],Block([],[Continue])),MethodDecl(Id(Destructor),Instance,[],Block([],[])),AttributeDecl(Static,VarDecl(Id($2h),ArrayType(1,StringType)))])])'''
        self.assertTrue(TestAST.test(line, expect, 460))

    def test_461(self):
        line = '''Class _{Destructor (){}Destructor (){} }Class _:r{Var i_5,$9:_;}'''
        expect = '''Program([ClassDecl(Id(_),[MethodDecl(Id(Destructor),Instance,[],Block([],[])),MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(_),Id(r),[AttributeDecl(Instance,VarDecl(Id(i_5),ClassType(Id(_)))),AttributeDecl(Static,VarDecl(Id($9),ClassType(Id(_))))])])'''
        self.assertTrue(TestAST.test(line, expect, 461))

    def test_462(self):
        line = '''Class _:S_{Constructor (_L9:Array [Array [Array [Int ,0b11111],0b11],0133]){} }'''
        expect = '''Program([ClassDecl(Id(_),Id(S_),[MethodDecl(Id(Constructor),Instance,[param(Id(_L9),ArrayType(91,ArrayType(3,ArrayType(31,IntType))))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 462))

    def test_463(self):
        line = '''Class _:q{Var _:Array [Array [Array [Array [Array [String ,0B10],0X12],4_4_6],55],0B1];}'''
        expect = '''Program([ClassDecl(Id(_),Id(q),[AttributeDecl(Instance,VarDecl(Id(_),ArrayType(1,ArrayType(55,ArrayType(446,ArrayType(18,ArrayType(2,StringType)))))))])])'''
        self.assertTrue(TestAST.test(line, expect, 463))

    def test_464(self):
        line = '''Class _{}Class _{Constructor (_:E){Var _0:Float ;} }Class e:_9__{}'''
        expect = '''Program([ClassDecl(Id(_),[]),ClassDecl(Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(_),ClassType(Id(E)))],Block([VarDecl(Id(_0),FloatType)],[]))]),ClassDecl(Id(e),Id(_9__),[])])'''
        self.assertTrue(TestAST.test(line, expect, 464))

    def test_465(self):
        line = '''Class E:___6p__{}Class __7:b{Constructor (){Continue ;New u8o5I_().__._b._()._();} }Class _{}'''
        expect = '''Program([ClassDecl(Id(E),Id(___6p__),[]),ClassDecl(Id(__7),Id(b),[MethodDecl(Id(Constructor),Instance,[],Block([],[Continue,Call(CallExpr(FieldAccess(FieldAccess(NewExpr(Id(u8o5I_),[]),Id(__)),Id(_b)),Id(_),[]),Id(_),[])]))]),ClassDecl(Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 465))

    def test_466(self):
        line = '''Class __{Var $_,$v,$h:Int ;}Class b9i:B{$d2(_7aFt:U){} }'''
        expect = '''Program([ClassDecl(Id(__),[AttributeDecl(Static,VarDecl(Id($_),IntType)),AttributeDecl(Static,VarDecl(Id($v),IntType)),AttributeDecl(Static,VarDecl(Id($h),IntType))]),ClassDecl(Id(b9i),Id(B),[MethodDecl(Id($d2),Static,[param(Id(_7aFt),ClassType(Id(U)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 466))

    def test_467(self):
        line = '''Class c{Constructor (o,_:Array [Array [String ,1],0X99];_x:Array [Array [Array [Boolean ,036],0X9_4A],0X35]){} }'''
        expect = '''Program([ClassDecl(Id(c),[MethodDecl(Id(Constructor),Instance,[param(Id(o),ArrayType(153,ArrayType(1,StringType))),param(Id(_),ArrayType(153,ArrayType(1,StringType))),param(Id(_x),ArrayType(53,ArrayType(2378,ArrayType(30,BoolType))))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 467))

    def test_468(self):
        line = '''Class L{Constructor (__:Int ;_9Pw,_,A_I,_,M:Array [String ,07_1]){}Constructor (_u:_){} }'''
        expect = '''Program([ClassDecl(Id(L),[MethodDecl(Id(Constructor),Instance,[param(Id(__),IntType),param(Id(_9Pw),ArrayType(57,StringType)),param(Id(_),ArrayType(57,StringType)),param(Id(A_I),ArrayType(57,StringType)),param(Id(_),ArrayType(57,StringType)),param(Id(M),ArrayType(57,StringType))],Block([],[])),MethodDecl(Id(Constructor),Instance,[param(Id(_u),ClassType(Id(_)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 468))

    def test_469(self):
        line = '''Class B__{_(j:Array [Float ,5_8_9]){ {} }}Class _{Var $_:c;}'''
        expect = '''Program([ClassDecl(Id(B__),[MethodDecl(Id(_),Instance,[param(Id(j),ArrayType(589,FloatType))],Block([],[Block([],[])]))]),ClassDecl(Id(_),[AttributeDecl(Static,VarDecl(Id($_),ClassType(Id(c))))])])'''
        self.assertTrue(TestAST.test(line, expect, 469))

    def test_470(self):
        line = '''Class _{Var $0,$1,_2_,_D,$__,_:Float ;}Class X__S6{}Class fp1:_{}'''
        expect = '''Program([ClassDecl(Id(_),[AttributeDecl(Static,VarDecl(Id($0),FloatType)),AttributeDecl(Static,VarDecl(Id($1),FloatType)),AttributeDecl(Instance,VarDecl(Id(_2_),FloatType)),AttributeDecl(Instance,VarDecl(Id(_D),FloatType)),AttributeDecl(Static,VarDecl(Id($__),FloatType)),AttributeDecl(Instance,VarDecl(Id(_),FloatType))]),ClassDecl(Id(X__S6),[]),ClassDecl(Id(fp1),Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 470))

    def test_471(self):
        line = '''Class _:F{__(){} }Class _{Constructor (){Break ;Continue ;} }'''
        expect = '''Program([ClassDecl(Id(_),Id(F),[MethodDecl(Id(__),Instance,[],Block([],[]))]),ClassDecl(Id(_),[MethodDecl(Id(Constructor),Instance,[],Block([],[Break,Continue]))])])'''
        self.assertTrue(TestAST.test(line, expect, 471))

    def test_472(self):
        line = '''Class _:_3{Constructor (_2_,cHs,_,F9J_,t:Array [Int ,0x2]){} }Class p:_{}'''
        expect = '''Program([ClassDecl(Id(_),Id(_3),[MethodDecl(Id(Constructor),Instance,[param(Id(_2_),ArrayType(2,IntType)),param(Id(cHs),ArrayType(2,IntType)),param(Id(_),ArrayType(2,IntType)),param(Id(F9J_),ArrayType(2,IntType)),param(Id(t),ArrayType(2,IntType))],Block([],[]))]),ClassDecl(Id(p),Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 472))

    def test_473(self):
        line = '''Class _{Constructor (_i,_x,O__:Boolean ;l:Int ){} }Class lf_{$_(_Jgz_,TA,_,_,_24,r:Int ){} }Class a:_{}'''
        expect = '''Program([ClassDecl(Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(_i),BoolType),param(Id(_x),BoolType),param(Id(O__),BoolType),param(Id(l),IntType)],Block([],[]))]),ClassDecl(Id(lf_),[MethodDecl(Id($_),Static,[param(Id(_Jgz_),IntType),param(Id(TA),IntType),param(Id(_),IntType),param(Id(_),IntType),param(Id(_24),IntType),param(Id(r),IntType)],Block([],[]))]),ClassDecl(Id(a),Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 473))

    def test_474(self):
        line = '''Class b_z:__{}Class _2{}Class _{}Class _6{Destructor (){}Constructor (){} }Class _nV:_{}'''
        expect = '''Program([ClassDecl(Id(b_z),Id(__),[]),ClassDecl(Id(_2),[]),ClassDecl(Id(_),[]),ClassDecl(Id(_6),[MethodDecl(Id(Destructor),Instance,[],Block([],[])),MethodDecl(Id(Constructor),Instance,[],Block([],[]))]),ClassDecl(Id(_nV),Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 474))

    def test_475(self):
        line = '''Class _Gk{yC__(_,x,__,_R:_k){}Constructor (){Break ;}Constructor (_,M,__43,U,_9:Array [Array [Float ,025],6];E,B0:Boolean ){}Destructor (){} }Class _:_{}Class m{}'''
        expect = '''Program([ClassDecl(Id(_Gk),[MethodDecl(Id(yC__),Instance,[param(Id(_),ClassType(Id(_k))),param(Id(x),ClassType(Id(_k))),param(Id(__),ClassType(Id(_k))),param(Id(_R),ClassType(Id(_k)))],Block([],[])),MethodDecl(Id(Constructor),Instance,[],Block([],[Break])),MethodDecl(Id(Constructor),Instance,[param(Id(_),ArrayType(6,ArrayType(21,FloatType))),param(Id(M),ArrayType(6,ArrayType(21,FloatType))),param(Id(__43),ArrayType(6,ArrayType(21,FloatType))),param(Id(U),ArrayType(6,ArrayType(21,FloatType))),param(Id(_9),ArrayType(6,ArrayType(21,FloatType))),param(Id(E),BoolType),param(Id(B0),BoolType)],Block([],[])),MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(_),Id(_),[]),ClassDecl(Id(m),[])])'''
        self.assertTrue(TestAST.test(line, expect, 475))

    def test_476(self):
        line = '''Class K_:_D{Constructor (){}Constructor (q,h,x,u:WOR;_D3_:Int ){} }'''
        expect = '''Program([ClassDecl(Id(K_),Id(_D),[MethodDecl(Id(Constructor),Instance,[],Block([],[])),MethodDecl(Id(Constructor),Instance,[param(Id(q),ClassType(Id(WOR))),param(Id(h),ClassType(Id(WOR))),param(Id(x),ClassType(Id(WOR))),param(Id(u),ClassType(Id(WOR))),param(Id(_D3_),IntType)],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 476))

    def test_477(self):
        line = '''Class _{Destructor (){}Var _,cQ_,$_,_F_,_5A_,BNnQj_0U__:Boolean ;}Class L:z{}Class Ml7:O{}'''
        expect = '''Program([ClassDecl(Id(_),[MethodDecl(Id(Destructor),Instance,[],Block([],[])),AttributeDecl(Instance,VarDecl(Id(_),BoolType)),AttributeDecl(Instance,VarDecl(Id(cQ_),BoolType)),AttributeDecl(Static,VarDecl(Id($_),BoolType)),AttributeDecl(Instance,VarDecl(Id(_F_),BoolType)),AttributeDecl(Instance,VarDecl(Id(_5A_),BoolType)),AttributeDecl(Instance,VarDecl(Id(BNnQj_0U__),BoolType))]),ClassDecl(Id(L),Id(z),[]),ClassDecl(Id(Ml7),Id(O),[])])'''
        self.assertTrue(TestAST.test(line, expect, 477))

    def test_478(self):
        line = '''Class _1B:X6{Var _n9_fc_,$5:Array [Float ,0b11_01_0];a(k,_,__u71gX9:Boolean ){Break ;Break ;} }'''
        expect = '''Program([ClassDecl(Id(_1B),Id(X6),[AttributeDecl(Instance,VarDecl(Id(_n9_fc_),ArrayType(26,FloatType))),AttributeDecl(Static,VarDecl(Id($5),ArrayType(26,FloatType))),MethodDecl(Id(a),Instance,[param(Id(k),BoolType),param(Id(_),BoolType),param(Id(__u71gX9),BoolType)],Block([],[Break,Break]))])])'''
        self.assertTrue(TestAST.test(line, expect, 478))

    def test_479(self):
        line = '''Class _{Var _:_;Var _T,$_,gx:Int ;}Class _FS:x{Var $2l,$9,ds:String ;Destructor (){Continue ;} }Class G:_{}Class r2:BG3{Destructor (){Return ;} }'''
        expect = '''Program([ClassDecl(Id(_),[AttributeDecl(Instance,VarDecl(Id(_),ClassType(Id(_)))),AttributeDecl(Instance,VarDecl(Id(_T),IntType)),AttributeDecl(Static,VarDecl(Id($_),IntType)),AttributeDecl(Instance,VarDecl(Id(gx),IntType))]),ClassDecl(Id(_FS),Id(x),[AttributeDecl(Static,VarDecl(Id($2l),StringType)),AttributeDecl(Static,VarDecl(Id($9),StringType)),AttributeDecl(Instance,VarDecl(Id(ds),StringType)),MethodDecl(Id(Destructor),Instance,[],Block([],[Continue]))]),ClassDecl(Id(G),Id(_),[]),ClassDecl(Id(r2),Id(BG3),[MethodDecl(Id(Destructor),Instance,[],Block([],[Return(None)]))])])'''
        self.assertTrue(TestAST.test(line, expect, 479))

    def test_480(self):
        line = '''Class Q:U{Var __h,_:Array [Array [Array [Boolean ,78],07_301_60_3_67_1],5];Constructor (__3:Array [Boolean ,0x41]){} }'''
        expect = '''Program([ClassDecl(Id(Q),Id(U),[AttributeDecl(Instance,VarDecl(Id(__h),ArrayType(5,ArrayType(990316473,ArrayType(78,BoolType))))),AttributeDecl(Instance,VarDecl(Id(_),ArrayType(5,ArrayType(990316473,ArrayType(78,BoolType))))),MethodDecl(Id(Constructor),Instance,[param(Id(__3),ArrayType(65,BoolType))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 480))

    def test_481(self):
        line = '''Class _{Constructor (_,_m,_:String ){Break ;}Var _,__,$0,_:Array [Boolean ,0X1];}Class __:__{}'''
        expect = '''Program([ClassDecl(Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(_),StringType),param(Id(_m),StringType),param(Id(_),StringType)],Block([],[Break])),AttributeDecl(Instance,VarDecl(Id(_),ArrayType(1,BoolType))),AttributeDecl(Instance,VarDecl(Id(__),ArrayType(1,BoolType))),AttributeDecl(Static,VarDecl(Id($0),ArrayType(1,BoolType))),AttributeDecl(Instance,VarDecl(Id(_),ArrayType(1,BoolType)))]),ClassDecl(Id(__),Id(__),[])])'''
        self.assertTrue(TestAST.test(line, expect, 481))

    def test_482(self):
        line = '''Class _:_82hHH{$_(S,_,W____4:Array [Array [Array [Array [Boolean ,02_73],02],0X3F],0X3F];c:_W){} }'''
        expect = '''Program([ClassDecl(Id(_),Id(_82hHH),[MethodDecl(Id($_),Static,[param(Id(S),ArrayType(63,ArrayType(63,ArrayType(2,ArrayType(187,BoolType))))),param(Id(_),ArrayType(63,ArrayType(63,ArrayType(2,ArrayType(187,BoolType))))),param(Id(W____4),ArrayType(63,ArrayType(63,ArrayType(2,ArrayType(187,BoolType))))),param(Id(c),ClassType(Id(_W)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 482))

    def test_483(self):
        line = '''Class L{}Class Hd{Var V,_6,_,__:Int ;}Class _9:__{}Class p_{}'''
        expect = '''Program([ClassDecl(Id(L),[]),ClassDecl(Id(Hd),[AttributeDecl(Instance,VarDecl(Id(V),IntType)),AttributeDecl(Instance,VarDecl(Id(_6),IntType)),AttributeDecl(Instance,VarDecl(Id(_),IntType)),AttributeDecl(Instance,VarDecl(Id(__),IntType))]),ClassDecl(Id(_9),Id(__),[]),ClassDecl(Id(p_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 483))

    def test_484(self):
        line = '''Class I6__487:Z{Constructor (){} }Class P_:R9dR{Var $7___:Array [Array [String ,93],0x3_B];_(){}$_2_(ok:Array [Float ,93];_,YKed,C0:Float ){} }Class J:_X8m{}'''
        expect = '''Program([ClassDecl(Id(I6__487),Id(Z),[MethodDecl(Id(Constructor),Instance,[],Block([],[]))]),ClassDecl(Id(P_),Id(R9dR),[AttributeDecl(Static,VarDecl(Id($7___),ArrayType(59,ArrayType(93,StringType)))),MethodDecl(Id(_),Instance,[],Block([],[])),MethodDecl(Id($_2_),Static,[param(Id(ok),ArrayType(93,FloatType)),param(Id(_),FloatType),param(Id(YKed),FloatType),param(Id(C0),FloatType)],Block([],[]))]),ClassDecl(Id(J),Id(_X8m),[])])'''
        self.assertTrue(TestAST.test(line, expect, 484))

    def test_485(self):
        line = '''Class M{_(){}Constructor (_:wbm;v_:Array [Array [Int ,9],02_4];PK:H){}_(z,q,__,mc:a){} }'''
        expect = '''Program([ClassDecl(Id(M),[MethodDecl(Id(_),Instance,[],Block([],[])),MethodDecl(Id(Constructor),Instance,[param(Id(_),ClassType(Id(wbm))),param(Id(v_),ArrayType(20,ArrayType(9,IntType))),param(Id(PK),ClassType(Id(H)))],Block([],[])),MethodDecl(Id(_),Instance,[param(Id(z),ClassType(Id(a))),param(Id(q),ClassType(Id(a))),param(Id(__),ClassType(Id(a))),param(Id(mc),ClassType(Id(a)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 485))

    def test_486(self):
        line = '''Class _{_7_t(_,C,P:Array [Array [Array [Array [Array [Array [Int ,0X89],0B1_0],0X7],72],6_7_14],72]){} }'''
        expect = '''Program([ClassDecl(Id(_),[MethodDecl(Id(_7_t),Instance,[param(Id(_),ArrayType(72,ArrayType(6714,ArrayType(72,ArrayType(7,ArrayType(2,ArrayType(137,IntType))))))),param(Id(C),ArrayType(72,ArrayType(6714,ArrayType(72,ArrayType(7,ArrayType(2,ArrayType(137,IntType))))))),param(Id(P),ArrayType(72,ArrayType(6714,ArrayType(72,ArrayType(7,ArrayType(2,ArrayType(137,IntType)))))))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 486))

    def test_487(self):
        line = '''Class yY_{}Class _2fT{Constructor (_:Array [Boolean ,0B100110]){} }Class Qq:_q8{}'''
        expect = '''Program([ClassDecl(Id(yY_),[]),ClassDecl(Id(_2fT),[MethodDecl(Id(Constructor),Instance,[param(Id(_),ArrayType(38,BoolType))],Block([],[]))]),ClassDecl(Id(Qq),Id(_q8),[])])'''
        self.assertTrue(TestAST.test(line, expect, 487))

    def test_488(self):
        line = '''Class _7{}Class F_L:H{}Class _p:_{Var _H_,$FD_:Int ;Var $3,g_o,E9:Array [Boolean ,0X33];}'''
        expect = '''Program([ClassDecl(Id(_7),[]),ClassDecl(Id(F_L),Id(H),[]),ClassDecl(Id(_p),Id(_),[AttributeDecl(Instance,VarDecl(Id(_H_),IntType)),AttributeDecl(Static,VarDecl(Id($FD_),IntType)),AttributeDecl(Static,VarDecl(Id($3),ArrayType(51,BoolType))),AttributeDecl(Instance,VarDecl(Id(g_o),ArrayType(51,BoolType))),AttributeDecl(Instance,VarDecl(Id(E9),ArrayType(51,BoolType)))])])'''
        self.assertTrue(TestAST.test(line, expect, 488))

    def test_489(self):
        line = '''Class _7{Destructor (){Break ;}Var _e6__:Float ;$_(U2:_P){}Var _3:Array [Float ,1_5];}'''
        expect = '''Program([ClassDecl(Id(_7),[MethodDecl(Id(Destructor),Instance,[],Block([],[Break])),AttributeDecl(Instance,VarDecl(Id(_e6__),FloatType)),MethodDecl(Id($_),Static,[param(Id(U2),ClassType(Id(_P)))],Block([],[])),AttributeDecl(Instance,VarDecl(Id(_3),ArrayType(15,FloatType)))])])'''
        self.assertTrue(TestAST.test(line, expect, 489))

    def test_490(self):
        line = '''Class U_ZNi{Var $v8:_;Destructor (){Continue ;} }Class g{_mR(){}Constructor (__,Q:Array [Array [Float ,80],0b1001001]){Break ;}Var v,$S8:Array [Array [String ,0B1_11_0],0XA];}Class t:M_V{}'''
        expect = '''Program([ClassDecl(Id(U_ZNi),[AttributeDecl(Static,VarDecl(Id($v8),ClassType(Id(_)))),MethodDecl(Id(Destructor),Instance,[],Block([],[Continue]))]),ClassDecl(Id(g),[MethodDecl(Id(_mR),Instance,[],Block([],[])),MethodDecl(Id(Constructor),Instance,[param(Id(__),ArrayType(73,ArrayType(80,FloatType))),param(Id(Q),ArrayType(73,ArrayType(80,FloatType)))],Block([],[Break])),AttributeDecl(Instance,VarDecl(Id(v),ArrayType(10,ArrayType(14,StringType)))),AttributeDecl(Static,VarDecl(Id($S8),ArrayType(10,ArrayType(14,StringType))))]),ClassDecl(Id(t),Id(M_V),[])])'''
        self.assertTrue(TestAST.test(line, expect, 490))

    def test_491(self):
        line = '''Class px{Destructor (){}$9(__3__:Array [Boolean ,04];_:Array [Array [Array [String ,86],0X37],0B10001];_:Int ;t,_O_,_12,U7,SN_,W:Array [Array [Array [Boolean ,05],0x46],0x46];M:Float ;_3_T:Array [Array [Float ,0B10001],0x46]){Break ;} }'''
        expect = '''Program([ClassDecl(Id(px),[MethodDecl(Id(Destructor),Instance,[],Block([],[])),MethodDecl(Id($9),Static,[param(Id(__3__),ArrayType(4,BoolType)),param(Id(_),ArrayType(17,ArrayType(55,ArrayType(86,StringType)))),param(Id(_),IntType),param(Id(t),ArrayType(70,ArrayType(70,ArrayType(5,BoolType)))),param(Id(_O_),ArrayType(70,ArrayType(70,ArrayType(5,BoolType)))),param(Id(_12),ArrayType(70,ArrayType(70,ArrayType(5,BoolType)))),param(Id(U7),ArrayType(70,ArrayType(70,ArrayType(5,BoolType)))),param(Id(SN_),ArrayType(70,ArrayType(70,ArrayType(5,BoolType)))),param(Id(W),ArrayType(70,ArrayType(70,ArrayType(5,BoolType)))),param(Id(M),FloatType),param(Id(_3_T),ArrayType(70,ArrayType(17,FloatType)))],Block([],[Break]))])])'''
        self.assertTrue(TestAST.test(line, expect, 491))

    def test_492(self):
        line = '''Class CSl{Destructor (){_::$x();Break ;} }Class _to4:_N{}'''
        expect = '''Program([ClassDecl(Id(CSl),[MethodDecl(Id(Destructor),Instance,[],Block([],[Call(Id(_),Id($x),[]),Break]))]),ClassDecl(Id(_to4),Id(_N),[])])'''
        self.assertTrue(TestAST.test(line, expect, 492))

    def test_493(self):
        line = '''Class cZ_:__C{w(_:_;_Fs_:Float ;_0_:Float ;o:Array [Array [Array [Array [String ,0x20],0b1_1],0XA_6],0x6]){Break ;}Destructor (){} }'''
        expect = '''Program([ClassDecl(Id(cZ_),Id(__C),[MethodDecl(Id(w),Instance,[param(Id(_),ClassType(Id(_))),param(Id(_Fs_),FloatType),param(Id(_0_),FloatType),param(Id(o),ArrayType(6,ArrayType(166,ArrayType(3,ArrayType(32,StringType)))))],Block([],[Break])),MethodDecl(Id(Destructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 493))

    def test_494(self):
        line = '''Class _:_6287{}Class _17eA_:_{}Class z{}Class _e:R_4_{}Class J{}'''
        expect = '''Program([ClassDecl(Id(_),Id(_6287),[]),ClassDecl(Id(_17eA_),Id(_),[]),ClassDecl(Id(z),[]),ClassDecl(Id(_e),Id(R_4_),[]),ClassDecl(Id(J),[])])'''
        self.assertTrue(TestAST.test(line, expect, 494))

    def test_495(self):
        line = '''Class _2_{}Class ___{dS(_:_5;_,_0,c97z2:d0s_;K0_,Y8,_1,_,R_,_m:Int ;_,W:C5){} }'''
        expect = '''Program([ClassDecl(Id(_2_),[]),ClassDecl(Id(___),[MethodDecl(Id(dS),Instance,[param(Id(_),ClassType(Id(_5))),param(Id(_),ClassType(Id(d0s_))),param(Id(_0),ClassType(Id(d0s_))),param(Id(c97z2),ClassType(Id(d0s_))),param(Id(K0_),IntType),param(Id(Y8),IntType),param(Id(_1),IntType),param(Id(_),IntType),param(Id(R_),IntType),param(Id(_m),IntType),param(Id(_),ClassType(Id(C5))),param(Id(W),ClassType(Id(C5)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 495))

    def test_496(self):
        line = '''Class x7:_{Var $_:Array [Array [Array [Array [String ,3],0XA_0],0B10_0],20];}'''
        expect = '''Program([ClassDecl(Id(x7),Id(_),[AttributeDecl(Static,VarDecl(Id($_),ArrayType(20,ArrayType(4,ArrayType(160,ArrayType(3,StringType))))))])])'''
        self.assertTrue(TestAST.test(line, expect, 496))

    def test_497(self):
        line = '''Class V{Constructor (A_:C;o,q9,_,__F:T6;we1_,m7_:Array [Array [Array [Array [Array [Array [Array [Array [String ,3],076],0X64],86],703],0x24],0b1001101],9];H,_6i,_,_,o,QtC,__,_,__0452:Float ;_:Int ){} }'''
        expect = '''Program([ClassDecl(Id(V),[MethodDecl(Id(Constructor),Instance,[param(Id(A_),ClassType(Id(C))),param(Id(o),ClassType(Id(T6))),param(Id(q9),ClassType(Id(T6))),param(Id(_),ClassType(Id(T6))),param(Id(__F),ClassType(Id(T6))),param(Id(we1_),ArrayType(9,ArrayType(77,ArrayType(36,ArrayType(703,ArrayType(86,ArrayType(100,ArrayType(62,ArrayType(3,StringType))))))))),param(Id(m7_),ArrayType(9,ArrayType(77,ArrayType(36,ArrayType(703,ArrayType(86,ArrayType(100,ArrayType(62,ArrayType(3,StringType))))))))),param(Id(H),FloatType),param(Id(_6i),FloatType),param(Id(_),FloatType),param(Id(_),FloatType),param(Id(o),FloatType),param(Id(QtC),FloatType),param(Id(__),FloatType),param(Id(_),FloatType),param(Id(__0452),FloatType),param(Id(_),IntType)],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 497))

    def test_498(self):
        line = '''Class Q:_{}Class G:_{}Class _G16{}Class K8v{}Class __{}Class J5{}Class y{}Class _:E{}'''
        expect = '''Program([ClassDecl(Id(Q),Id(_),[]),ClassDecl(Id(G),Id(_),[]),ClassDecl(Id(_G16),[]),ClassDecl(Id(K8v),[]),ClassDecl(Id(__),[]),ClassDecl(Id(J5),[]),ClassDecl(Id(y),[]),ClassDecl(Id(_),Id(E),[])])'''
        self.assertTrue(TestAST.test(line, expect, 498))

    def test_499(self):
        line = '''Class g{Var $1cB:_;Var $8:Array [Array [String ,0B1000101],0x9];Var $W,$7hh_:Array [Array [Array [Array [Float ,0130],2_0],0B11],0xD];}'''
        expect = '''Program([ClassDecl(Id(g),[AttributeDecl(Static,VarDecl(Id($1cB),ClassType(Id(_)))),AttributeDecl(Static,VarDecl(Id($8),ArrayType(9,ArrayType(69,StringType)))),AttributeDecl(Static,VarDecl(Id($W),ArrayType(13,ArrayType(3,ArrayType(20,ArrayType(88,FloatType)))))),AttributeDecl(Static,VarDecl(Id($7hh_),ArrayType(13,ArrayType(3,ArrayType(20,ArrayType(88,FloatType))))))])])'''
        self.assertTrue(TestAST.test(line, expect, 499))

    def test_500(self):
        line = '''Class __:_{Destructor (){Return ;Continue ;Break ;} }Class a{Constructor (){Continue ;} }Class __{Var $d0,$_,$88:Array [Array [Array [Array [Int ,0x43],65],057],0X15];Var _8u7,$k,u4rw10,$txs7,_,C:O;}'''
        expect = '''Program([ClassDecl(Id(__),Id(_),[MethodDecl(Id(Destructor),Instance,[],Block([],[Return(None),Continue,Break]))]),ClassDecl(Id(a),[MethodDecl(Id(Constructor),Instance,[],Block([],[Continue]))]),ClassDecl(Id(__),[AttributeDecl(Static,VarDecl(Id($d0),ArrayType(21,ArrayType(47,ArrayType(65,ArrayType(67,IntType)))))),AttributeDecl(Static,VarDecl(Id($_),ArrayType(21,ArrayType(47,ArrayType(65,ArrayType(67,IntType)))))),AttributeDecl(Static,VarDecl(Id($88),ArrayType(21,ArrayType(47,ArrayType(65,ArrayType(67,IntType)))))),AttributeDecl(Instance,VarDecl(Id(_8u7),ClassType(Id(O)))),AttributeDecl(Static,VarDecl(Id($k),ClassType(Id(O)))),AttributeDecl(Instance,VarDecl(Id(u4rw10),ClassType(Id(O)))),AttributeDecl(Static,VarDecl(Id($txs7),ClassType(Id(O)))),AttributeDecl(Instance,VarDecl(Id(_),ClassType(Id(O)))),AttributeDecl(Instance,VarDecl(Id(C),ClassType(Id(O))))])])'''
        self.assertTrue(TestAST.test(line, expect, 500))

    def test_501(self):
        line = '''Class TZ_q_{}Class r:_047{Destructor (){} }Class C:_{}Class __8_{Var L:Array [Int ,67];}'''
        expect = '''Program([ClassDecl(Id(TZ_q_),[]),ClassDecl(Id(r),Id(_047),[MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(C),Id(_),[]),ClassDecl(Id(__8_),[AttributeDecl(Instance,VarDecl(Id(L),ArrayType(67,IntType)))])])'''
        self.assertTrue(TestAST.test(line, expect, 501))

    def test_502(self):
        line = '''Class _:D_r{Destructor (){} }Class fy:Du{}Class _{$797(){} }'''
        expect = '''Program([ClassDecl(Id(_),Id(D_r),[MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(fy),Id(Du),[]),ClassDecl(Id(_),[MethodDecl(Id($797),Static,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 502))

    def test_503(self):
        line = '''Class _:__6{}Class _fF5:_{_(_1,_G:___){}Var $_:String ;}Class _:_{}'''
        expect = '''Program([ClassDecl(Id(_),Id(__6),[]),ClassDecl(Id(_fF5),Id(_),[MethodDecl(Id(_),Instance,[param(Id(_1),ClassType(Id(___))),param(Id(_G),ClassType(Id(___)))],Block([],[])),AttributeDecl(Static,VarDecl(Id($_),StringType))]),ClassDecl(Id(_),Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 503))

    def test_504(self):
        line = '''Class _:_{Destructor (){} }Class U_{}Class D_5B:_{Var $z_,$49y,_r_:_;Constructor (){} }'''
        expect = '''Program([ClassDecl(Id(_),Id(_),[MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(U_),[]),ClassDecl(Id(D_5B),Id(_),[AttributeDecl(Static,VarDecl(Id($z_),ClassType(Id(_)))),AttributeDecl(Static,VarDecl(Id($49y),ClassType(Id(_)))),AttributeDecl(Instance,VarDecl(Id(_r_),ClassType(Id(_)))),MethodDecl(Id(Constructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 504))

    def test_505(self):
        line = '''Class __R{Constructor (__:Boolean ;_d,e,_,M,__:Array [Array [String ,1],0B101101]){} }'''
        expect = '''Program([ClassDecl(Id(__R),[MethodDecl(Id(Constructor),Instance,[param(Id(__),BoolType),param(Id(_d),ArrayType(45,ArrayType(1,StringType))),param(Id(e),ArrayType(45,ArrayType(1,StringType))),param(Id(_),ArrayType(45,ArrayType(1,StringType))),param(Id(M),ArrayType(45,ArrayType(1,StringType))),param(Id(__),ArrayType(45,ArrayType(1,StringType)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 505))

    def test_506(self):
        line = '''Class _7__9:__{_(p87,__K,eQ___Tc:Array [Array [Boolean ,7],03];h,Aw,_,__1:n){} }Class t_:_N{}Class _{}'''
        expect = '''Program([ClassDecl(Id(_7__9),Id(__),[MethodDecl(Id(_),Instance,[param(Id(p87),ArrayType(3,ArrayType(7,BoolType))),param(Id(__K),ArrayType(3,ArrayType(7,BoolType))),param(Id(eQ___Tc),ArrayType(3,ArrayType(7,BoolType))),param(Id(h),ClassType(Id(n))),param(Id(Aw),ClassType(Id(n))),param(Id(_),ClassType(Id(n))),param(Id(__1),ClassType(Id(n)))],Block([],[]))]),ClassDecl(Id(t_),Id(_N),[]),ClassDecl(Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 506))

    def test_507(self):
        line = '''Class _{E(){}Var S1_9bC_:__;Constructor (o,B6:l;v7__:Array [Array [Array [String ,9],0x60],59_6];_t__,_:v;_8_:Array [Float ,7]){} }Class _{Constructor (){} }'''
        expect = '''Program([ClassDecl(Id(_),[MethodDecl(Id(E),Instance,[],Block([],[])),AttributeDecl(Instance,VarDecl(Id(S1_9bC_),ClassType(Id(__)))),MethodDecl(Id(Constructor),Instance,[param(Id(o),ClassType(Id(l))),param(Id(B6),ClassType(Id(l))),param(Id(v7__),ArrayType(596,ArrayType(96,ArrayType(9,StringType)))),param(Id(_t__),ClassType(Id(v))),param(Id(_),ClassType(Id(v))),param(Id(_8_),ArrayType(7,FloatType))],Block([],[]))]),ClassDecl(Id(_),[MethodDecl(Id(Constructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 507))

    def test_508(self):
        line = '''Class S{R(W9,g7,nU0,_D64Qd_,_:String ;H0,_5p,_:Float ){} }'''
        expect = '''Program([ClassDecl(Id(S),[MethodDecl(Id(R),Instance,[param(Id(W9),StringType),param(Id(g7),StringType),param(Id(nU0),StringType),param(Id(_D64Qd_),StringType),param(Id(_),StringType),param(Id(H0),FloatType),param(Id(_5p),FloatType),param(Id(_),FloatType)],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 508))

    def test_509(self):
        line = '''Class _:x{}Class sk{Destructor (){}Destructor (){}Destructor (){} }Class _u{}'''
        expect = '''Program([ClassDecl(Id(_),Id(x),[]),ClassDecl(Id(sk),[MethodDecl(Id(Destructor),Instance,[],Block([],[])),MethodDecl(Id(Destructor),Instance,[],Block([],[])),MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(_u),[])])'''
        self.assertTrue(TestAST.test(line, expect, 509))

    def test_510(self):
        line = '''Class _t:B3{Constructor (l6C,FB:_;__,_k05_7:_;B_ss,_G0:String ;w_,_:Array [Float ,0105]){} }'''
        expect = '''Program([ClassDecl(Id(_t),Id(B3),[MethodDecl(Id(Constructor),Instance,[param(Id(l6C),ClassType(Id(_))),param(Id(FB),ClassType(Id(_))),param(Id(__),ClassType(Id(_))),param(Id(_k05_7),ClassType(Id(_))),param(Id(B_ss),StringType),param(Id(_G0),StringType),param(Id(w_),ArrayType(69,FloatType)),param(Id(_),ArrayType(69,FloatType))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 510))

    def test_511(self):
        line = '''Class _o_O:QdZ1Z{}Class a{$6_7382(_6:__){Var r:_0;Return ;}Constructor (y9,W3:Array [String ,0x7_E]){ {} }}Class Q_9{}'''
        expect = '''Program([ClassDecl(Id(_o_O),Id(QdZ1Z),[]),ClassDecl(Id(a),[MethodDecl(Id($6_7382),Static,[param(Id(_6),ClassType(Id(__)))],Block([VarDecl(Id(r),ClassType(Id(_0)))],[Return(None)])),MethodDecl(Id(Constructor),Instance,[param(Id(y9),ArrayType(126,StringType)),param(Id(W3),ArrayType(126,StringType))],Block([],[Block([],[])]))]),ClassDecl(Id(Q_9),[])])'''
        self.assertTrue(TestAST.test(line, expect, 511))

    def test_512(self):
        line = '''Class _m2U9T_:au{Var x,_92,$c,$_R3_r5:Array [Array [Float ,5_86_33],016];Constructor (){} }'''
        expect = '''Program([ClassDecl(Id(_m2U9T_),Id(au),[AttributeDecl(Instance,VarDecl(Id(x),ArrayType(14,ArrayType(58633,FloatType)))),AttributeDecl(Instance,VarDecl(Id(_92),ArrayType(14,ArrayType(58633,FloatType)))),AttributeDecl(Static,VarDecl(Id($c),ArrayType(14,ArrayType(58633,FloatType)))),AttributeDecl(Static,VarDecl(Id($_R3_r5),ArrayType(14,ArrayType(58633,FloatType)))),MethodDecl(Id(Constructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 512))

    def test_513(self):
        line = '''Class L___:_{Constructor (__1K:Array [Float ,0B11];_,_,_,N,__,_,W,_v:Array [Int ,0B1_1]){}Var _:o;}'''
        expect = '''Program([ClassDecl(Id(L___),Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(__1K),ArrayType(3,FloatType)),param(Id(_),ArrayType(3,IntType)),param(Id(_),ArrayType(3,IntType)),param(Id(_),ArrayType(3,IntType)),param(Id(N),ArrayType(3,IntType)),param(Id(__),ArrayType(3,IntType)),param(Id(_),ArrayType(3,IntType)),param(Id(W),ArrayType(3,IntType)),param(Id(_v),ArrayType(3,IntType))],Block([],[])),AttributeDecl(Instance,VarDecl(Id(_),ClassType(Id(o))))])])'''
        self.assertTrue(TestAST.test(line, expect, 513))

    def test_514(self):
        line = '''Class k23:_{Destructor (){} }Class _:_{Var $T,$3:String ;}'''
        expect = '''Program([ClassDecl(Id(k23),Id(_),[MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(_),Id(_),[AttributeDecl(Static,VarDecl(Id($T),StringType)),AttributeDecl(Static,VarDecl(Id($3),StringType))])])'''
        self.assertTrue(TestAST.test(line, expect, 514))

    def test_515(self):
        line = '''Class _d1742K:E4_{$l_X(){ {} }Var Q_,$7:_;Constructor (_GW:Int ;h_,_A_4_,_,Yyl,__:Array [Array [Array [Float ,0B1010101],0B1010101],0X8_7];_,K,_E9,_O,w29_s5,_h7T3N_:Array [Array [String ,0x60],3_4];d_:String ;__:String ){} }'''
        expect = '''Program([ClassDecl(Id(_d1742K),Id(E4_),[MethodDecl(Id($l_X),Static,[],Block([],[Block([],[])])),AttributeDecl(Instance,VarDecl(Id(Q_),ClassType(Id(_)))),AttributeDecl(Static,VarDecl(Id($7),ClassType(Id(_)))),MethodDecl(Id(Constructor),Instance,[param(Id(_GW),IntType),param(Id(h_),ArrayType(135,ArrayType(85,ArrayType(85,FloatType)))),param(Id(_A_4_),ArrayType(135,ArrayType(85,ArrayType(85,FloatType)))),param(Id(_),ArrayType(135,ArrayType(85,ArrayType(85,FloatType)))),param(Id(Yyl),ArrayType(135,ArrayType(85,ArrayType(85,FloatType)))),param(Id(__),ArrayType(135,ArrayType(85,ArrayType(85,FloatType)))),param(Id(_),ArrayType(34,ArrayType(96,StringType))),param(Id(K),ArrayType(34,ArrayType(96,StringType))),param(Id(_E9),ArrayType(34,ArrayType(96,StringType))),param(Id(_O),ArrayType(34,ArrayType(96,StringType))),param(Id(w29_s5),ArrayType(34,ArrayType(96,StringType))),param(Id(_h7T3N_),ArrayType(34,ArrayType(96,StringType))),param(Id(d_),StringType),param(Id(__),StringType)],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 515))

    def test_516(self):
        line = '''Class _{Constructor (_:Float ;c,__3,t,_5U3O22,_,s87,g:_0f;W28:Array [Float ,0x36];A,cJ_2,_9_:Array [Array [Array [Boolean ,062],062],062];u:Boolean ){} }'''
        expect = '''Program([ClassDecl(Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(_),FloatType),param(Id(c),ClassType(Id(_0f))),param(Id(__3),ClassType(Id(_0f))),param(Id(t),ClassType(Id(_0f))),param(Id(_5U3O22),ClassType(Id(_0f))),param(Id(_),ClassType(Id(_0f))),param(Id(s87),ClassType(Id(_0f))),param(Id(g),ClassType(Id(_0f))),param(Id(W28),ArrayType(54,FloatType)),param(Id(A),ArrayType(50,ArrayType(50,ArrayType(50,BoolType)))),param(Id(cJ_2),ArrayType(50,ArrayType(50,ArrayType(50,BoolType)))),param(Id(_9_),ArrayType(50,ArrayType(50,ArrayType(50,BoolType)))),param(Id(u),BoolType)],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 516))

    def test_517(self):
        line = '''Class _:l{Var _jK,$92,$_:String ;Destructor (){Continue ;} }'''
        expect = '''Program([ClassDecl(Id(_),Id(l),[AttributeDecl(Instance,VarDecl(Id(_jK),StringType)),AttributeDecl(Static,VarDecl(Id($92),StringType)),AttributeDecl(Static,VarDecl(Id($_),StringType)),MethodDecl(Id(Destructor),Instance,[],Block([],[Continue]))])])'''
        self.assertTrue(TestAST.test(line, expect, 517))

    def test_518(self):
        line = '''Class Q:D{}Class _{n(_k:_){}Destructor (){0.372.r1()._2()._();} }'''
        expect = '''Program([ClassDecl(Id(Q),Id(D),[]),ClassDecl(Id(_),[MethodDecl(Id(n),Instance,[param(Id(_k),ClassType(Id(_)))],Block([],[])),MethodDecl(Id(Destructor),Instance,[],Block([],[Call(CallExpr(CallExpr(FloatLit(0.372),Id(r1),[]),Id(_2),[]),Id(_),[])]))])])'''
        self.assertTrue(TestAST.test(line, expect, 518))

    def test_519(self):
        line = '''Class F_{Destructor (){}Constructor (__:__;__,_3__:___8){} }'''
        expect = '''Program([ClassDecl(Id(F_),[MethodDecl(Id(Destructor),Instance,[],Block([],[])),MethodDecl(Id(Constructor),Instance,[param(Id(__),ClassType(Id(__))),param(Id(__),ClassType(Id(___8))),param(Id(_3__),ClassType(Id(___8)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 519))

    def test_520(self):
        line = '''Class O{Constructor (T:Array [Int ,02];g_:_;_,_,X:wN;_,Y,y:Array [String ,07]){} }Class _{}'''
        expect = '''Program([ClassDecl(Id(O),[MethodDecl(Id(Constructor),Instance,[param(Id(T),ArrayType(2,IntType)),param(Id(g_),ClassType(Id(_))),param(Id(_),ClassType(Id(wN))),param(Id(_),ClassType(Id(wN))),param(Id(X),ClassType(Id(wN))),param(Id(_),ArrayType(7,StringType)),param(Id(Y),ArrayType(7,StringType)),param(Id(y),ArrayType(7,StringType))],Block([],[]))]),ClassDecl(Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 520))

    def test_521(self):
        line = '''Class _7:__5_{Constructor (N_,_,_3,_5W,_,_8:Array [Array [String ,55],01];S91:_){Return ;} }'''
        expect = '''Program([ClassDecl(Id(_7),Id(__5_),[MethodDecl(Id(Constructor),Instance,[param(Id(N_),ArrayType(1,ArrayType(55,StringType))),param(Id(_),ArrayType(1,ArrayType(55,StringType))),param(Id(_3),ArrayType(1,ArrayType(55,StringType))),param(Id(_5W),ArrayType(1,ArrayType(55,StringType))),param(Id(_),ArrayType(1,ArrayType(55,StringType))),param(Id(_8),ArrayType(1,ArrayType(55,StringType))),param(Id(S91),ClassType(Id(_)))],Block([],[Return(None)]))])])'''
        self.assertTrue(TestAST.test(line, expect, 521))

    def test_522(self):
        line = '''Class _x:_{Var $Ao:Array [Int ,0b10];Constructor (__1:a){} }'''
        expect = '''Program([ClassDecl(Id(_x),Id(_),[AttributeDecl(Static,VarDecl(Id($Ao),ArrayType(2,IntType))),MethodDecl(Id(Constructor),Instance,[param(Id(__1),ClassType(Id(a)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 522))

    def test_523(self):
        line = '''Class _4:_88{Constructor (c2d,_0K7Xv7,_pp:Array [Array [Array [String ,0X30],0b1],1];E_,_E:Array [Int ,15];_,_Vn,_j_N__0_,L:Array [Boolean ,15];_,_:__){} }'''
        expect = '''Program([ClassDecl(Id(_4),Id(_88),[MethodDecl(Id(Constructor),Instance,[param(Id(c2d),ArrayType(1,ArrayType(1,ArrayType(48,StringType)))),param(Id(_0K7Xv7),ArrayType(1,ArrayType(1,ArrayType(48,StringType)))),param(Id(_pp),ArrayType(1,ArrayType(1,ArrayType(48,StringType)))),param(Id(E_),ArrayType(15,IntType)),param(Id(_E),ArrayType(15,IntType)),param(Id(_),ArrayType(15,BoolType)),param(Id(_Vn),ArrayType(15,BoolType)),param(Id(_j_N__0_),ArrayType(15,BoolType)),param(Id(L),ArrayType(15,BoolType)),param(Id(_),ClassType(Id(__))),param(Id(_),ClassType(Id(__)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 523))

    def test_524(self):
        line = '''Class h{}Class g:_{Destructor (){}_(VH:_9m;__:Int ){} }Class I_:q9{Var $5y9:Array [Int ,0B1011111];}Class W{}Class _:x1_{}'''
        expect = '''Program([ClassDecl(Id(h),[]),ClassDecl(Id(g),Id(_),[MethodDecl(Id(Destructor),Instance,[],Block([],[])),MethodDecl(Id(_),Instance,[param(Id(VH),ClassType(Id(_9m))),param(Id(__),IntType)],Block([],[]))]),ClassDecl(Id(I_),Id(q9),[AttributeDecl(Static,VarDecl(Id($5y9),ArrayType(95,IntType)))]),ClassDecl(Id(W),[]),ClassDecl(Id(_),Id(x1_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 524))

    def test_525(self):
        line = '''Class __:A_{Constructor (_Q_v,_,Q8w,___S:String ;_,_:e;O_:fG){} }'''
        expect = '''Program([ClassDecl(Id(__),Id(A_),[MethodDecl(Id(Constructor),Instance,[param(Id(_Q_v),StringType),param(Id(_),StringType),param(Id(Q8w),StringType),param(Id(___S),StringType),param(Id(_),ClassType(Id(e))),param(Id(_),ClassType(Id(e))),param(Id(O_),ClassType(Id(fG)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 525))

    def test_526(self):
        line = '''Class _{}Class ui{Constructor (){Var _:_;}Var $S:String ;}Class _:_{}'''
        expect = '''Program([ClassDecl(Id(_),[]),ClassDecl(Id(ui),[MethodDecl(Id(Constructor),Instance,[],Block([VarDecl(Id(_),ClassType(Id(_)))],[])),AttributeDecl(Static,VarDecl(Id($S),StringType))]),ClassDecl(Id(_),Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 526))

    def test_527(self):
        line = '''Class _Y2:bs{Constructor (b_:_){ {} }}Class _{Destructor (){}Var Q,i,G,$_k,H_,$4H:Array [Float ,18];}'''
        expect = '''Program([ClassDecl(Id(_Y2),Id(bs),[MethodDecl(Id(Constructor),Instance,[param(Id(b_),ClassType(Id(_)))],Block([],[Block([],[])]))]),ClassDecl(Id(_),[MethodDecl(Id(Destructor),Instance,[],Block([],[])),AttributeDecl(Instance,VarDecl(Id(Q),ArrayType(18,FloatType))),AttributeDecl(Instance,VarDecl(Id(i),ArrayType(18,FloatType))),AttributeDecl(Instance,VarDecl(Id(G),ArrayType(18,FloatType))),AttributeDecl(Static,VarDecl(Id($_k),ArrayType(18,FloatType))),AttributeDecl(Instance,VarDecl(Id(H_),ArrayType(18,FloatType))),AttributeDecl(Static,VarDecl(Id($4H),ArrayType(18,FloatType)))])])'''
        self.assertTrue(TestAST.test(line, expect, 527))

    def test_528(self):
        line = '''Class _6{}Class ___{}Class _1L{}Class hknr_0_{Var $M,$3_,$9,$_wMF:Array [Array [String ,0X2],7];Destructor (){Return ;Return ;} }'''
        expect = '''Program([ClassDecl(Id(_6),[]),ClassDecl(Id(___),[]),ClassDecl(Id(_1L),[]),ClassDecl(Id(hknr_0_),[AttributeDecl(Static,VarDecl(Id($M),ArrayType(7,ArrayType(2,StringType)))),AttributeDecl(Static,VarDecl(Id($3_),ArrayType(7,ArrayType(2,StringType)))),AttributeDecl(Static,VarDecl(Id($9),ArrayType(7,ArrayType(2,StringType)))),AttributeDecl(Static,VarDecl(Id($_wMF),ArrayType(7,ArrayType(2,StringType)))),MethodDecl(Id(Destructor),Instance,[],Block([],[Return(None),Return(None)]))])])'''
        self.assertTrue(TestAST.test(line, expect, 528))

    # def test_529(self):
    #     line = '''Class If :__4{H(_hN,y_,_:_g;jU,__3:Int ;_3:Array [String ,41]){ {_L_Es::F();} }}'''
    #     expect = '''Program([ClassDecl(Id(__4),Id(H),[])])'''
    #     self.assertTrue(TestAST.test(line, expect, 529))

    def test_530(self):
        line = '''Class O:U_a_3{wD(z_:Array [String ,0x1];_Z__:Array [Int ,93];u:Boolean ;V:Array [Boolean ,0x5B]){}Constructor (P:Array [Array [Array [Array [Array [Array [Boolean ,0b1100000],0b1000_1_0],07_5],2],03],0b1100000]){}Var $_:Boolean ;w(){Return ;}Var $_:Float ;}'''
        expect = '''Program([ClassDecl(Id(O),Id(U_a_3),[MethodDecl(Id(wD),Instance,[param(Id(z_),ArrayType(1,StringType)),param(Id(_Z__),ArrayType(93,IntType)),param(Id(u),BoolType),param(Id(V),ArrayType(91,BoolType))],Block([],[])),MethodDecl(Id(Constructor),Instance,[param(Id(P),ArrayType(96,ArrayType(3,ArrayType(2,ArrayType(61,ArrayType(34,ArrayType(96,BoolType)))))))],Block([],[])),AttributeDecl(Static,VarDecl(Id($_),BoolType)),MethodDecl(Id(w),Instance,[],Block([],[Return(None)])),AttributeDecl(Static,VarDecl(Id($_),FloatType))])])'''
        self.assertTrue(TestAST.test(line, expect, 530))

    def test_531(self):
        line = '''Class j{}Class C:_{s_(_7,_MZ,__:U_9a;_,e_:Array [Array [Array [Array [String ,5],0111],0x3A],5];t:Int ){} }Class F:_{}'''
        expect = '''Program([ClassDecl(Id(j),[]),ClassDecl(Id(C),Id(_),[MethodDecl(Id(s_),Instance,[param(Id(_7),ClassType(Id(U_9a))),param(Id(_MZ),ClassType(Id(U_9a))),param(Id(__),ClassType(Id(U_9a))),param(Id(_),ArrayType(5,ArrayType(58,ArrayType(73,ArrayType(5,StringType))))),param(Id(e_),ArrayType(5,ArrayType(58,ArrayType(73,ArrayType(5,StringType))))),param(Id(t),IntType)],Block([],[]))]),ClassDecl(Id(F),Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 531))

    def test_532(self):
        line = '''Class _5J{FC_(t_,_8_l,f,__3,I,V:Boolean ;K,W:Boolean ;hn,__5:Boolean ;T,Yv,u69,oW,_0:Array [String ,0xAE]){} }'''
        expect = '''Program([ClassDecl(Id(_5J),[MethodDecl(Id(FC_),Instance,[param(Id(t_),BoolType),param(Id(_8_l),BoolType),param(Id(f),BoolType),param(Id(__3),BoolType),param(Id(I),BoolType),param(Id(V),BoolType),param(Id(K),BoolType),param(Id(W),BoolType),param(Id(hn),BoolType),param(Id(__5),BoolType),param(Id(T),ArrayType(174,StringType)),param(Id(Yv),ArrayType(174,StringType)),param(Id(u69),ArrayType(174,StringType)),param(Id(oW),ArrayType(174,StringType)),param(Id(_0),ArrayType(174,StringType))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 532))

    def test_533(self):
        line = '''Class G{$Z3(p,_:Array [Array [Array [Int ,0B1001100],061],0b1_0];M:Float ;K,v5_:Int ;p,_,t:_){_::$_()._0._EkG();}$0(j9,E_,_:j){}$_(_xy:Array [Boolean ,061]){} }Class _:_AE{}'''
        expect = '''Program([ClassDecl(Id(G),[MethodDecl(Id($Z3),Static,[param(Id(p),ArrayType(2,ArrayType(49,ArrayType(76,IntType)))),param(Id(_),ArrayType(2,ArrayType(49,ArrayType(76,IntType)))),param(Id(M),FloatType),param(Id(K),IntType),param(Id(v5_),IntType),param(Id(p),ClassType(Id(_))),param(Id(_),ClassType(Id(_))),param(Id(t),ClassType(Id(_)))],Block([],[Call(FieldAccess(CallExpr(Id(_),Id($_),[]),Id(_0)),Id(_EkG),[])])),MethodDecl(Id($0),Static,[param(Id(j9),ClassType(Id(j))),param(Id(E_),ClassType(Id(j))),param(Id(_),ClassType(Id(j)))],Block([],[])),MethodDecl(Id($_),Static,[param(Id(_xy),ArrayType(49,BoolType))],Block([],[]))]),ClassDecl(Id(_),Id(_AE),[])])'''
        self.assertTrue(TestAST.test(line, expect, 533))

    def test_534(self):
        line = '''Class __4:X_e{Destructor (){Break ;} }Class _:K5{}Class K{}'''
        expect = '''Program([ClassDecl(Id(__4),Id(X_e),[MethodDecl(Id(Destructor),Instance,[],Block([],[Break]))]),ClassDecl(Id(_),Id(K5),[]),ClassDecl(Id(K),[])])'''
        self.assertTrue(TestAST.test(line, expect, 534))

    def test_535(self):
        line = '''Class _0C{Var $_,$_,I,_,$_:Array [Float ,02463];}Class c1:A{}'''
        expect = '''Program([ClassDecl(Id(_0C),[AttributeDecl(Static,VarDecl(Id($_),ArrayType(1331,FloatType))),AttributeDecl(Static,VarDecl(Id($_),ArrayType(1331,FloatType))),AttributeDecl(Instance,VarDecl(Id(I),ArrayType(1331,FloatType))),AttributeDecl(Instance,VarDecl(Id(_),ArrayType(1331,FloatType))),AttributeDecl(Static,VarDecl(Id($_),ArrayType(1331,FloatType)))]),ClassDecl(Id(c1),Id(A),[])])'''
        self.assertTrue(TestAST.test(line, expect, 535))

    def test_536(self):
        line = '''Class __{_(){} }Class y4{Destructor (){} }Class _{}Class _{}Class __:_{Var _,$8T,_:_;}'''
        expect = '''Program([ClassDecl(Id(__),[MethodDecl(Id(_),Instance,[],Block([],[]))]),ClassDecl(Id(y4),[MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(_),[]),ClassDecl(Id(_),[]),ClassDecl(Id(__),Id(_),[AttributeDecl(Instance,VarDecl(Id(_),ClassType(Id(_)))),AttributeDecl(Static,VarDecl(Id($8T),ClassType(Id(_)))),AttributeDecl(Instance,VarDecl(Id(_),ClassType(Id(_))))])])'''
        self.assertTrue(TestAST.test(line, expect, 536))

    def test_537(self):
        line = '''Class c9_:o7{Var $3,F,g1,m:y_;}Class d__{Constructor (){} }'''
        expect = '''Program([ClassDecl(Id(c9_),Id(o7),[AttributeDecl(Static,VarDecl(Id($3),ClassType(Id(y_)))),AttributeDecl(Instance,VarDecl(Id(F),ClassType(Id(y_)))),AttributeDecl(Instance,VarDecl(Id(g1),ClassType(Id(y_)))),AttributeDecl(Instance,VarDecl(Id(m),ClassType(Id(y_))))]),ClassDecl(Id(d__),[MethodDecl(Id(Constructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 537))

    def test_538(self):
        line = '''Class I:_56__{}Class x{}Class yZs_P:_d{}Class _:_{Constructor (){} }'''
        expect = '''Program([ClassDecl(Id(I),Id(_56__),[]),ClassDecl(Id(x),[]),ClassDecl(Id(yZs_P),Id(_d),[]),ClassDecl(Id(_),Id(_),[MethodDecl(Id(Constructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 538))

    def test_539(self):
        line = '''Class U5M37h_{}Class r_{Var _E,$_,X:Array [Boolean ,0X4E];}Class _N__{}'''
        expect = '''Program([ClassDecl(Id(U5M37h_),[]),ClassDecl(Id(r_),[AttributeDecl(Instance,VarDecl(Id(_E),ArrayType(78,BoolType))),AttributeDecl(Static,VarDecl(Id($_),ArrayType(78,BoolType))),AttributeDecl(Instance,VarDecl(Id(X),ArrayType(78,BoolType)))]),ClassDecl(Id(_N__),[])])'''
        self.assertTrue(TestAST.test(line, expect, 539))

    def test_540(self):
        line = '''Class P{}Class Sb{}Class _0d{$_(G1:Array [Array [Boolean ,0xE_5],0b110001]){} }'''
        expect = '''Program([ClassDecl(Id(P),[]),ClassDecl(Id(Sb),[]),ClassDecl(Id(_0d),[MethodDecl(Id($_),Static,[param(Id(G1),ArrayType(49,ArrayType(229,BoolType)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 540))

    def test_541(self):
        line = '''Class l__:_{Constructor (O_7__,v,eo:N6){} }Class tn5:qW{}'''
        expect = '''Program([ClassDecl(Id(l__),Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(O_7__),ClassType(Id(N6))),param(Id(v),ClassType(Id(N6))),param(Id(eo),ClassType(Id(N6)))],Block([],[]))]),ClassDecl(Id(tn5),Id(qW),[])])'''
        self.assertTrue(TestAST.test(line, expect, 541))

    def test_542(self):
        line = '''Class E0V{Var $_:Array [Array [Array [Array [String ,10],0b1000011],0100],84];}'''
        expect = '''Program([ClassDecl(Id(E0V),[AttributeDecl(Static,VarDecl(Id($_),ArrayType(84,ArrayType(64,ArrayType(67,ArrayType(10,StringType))))))])])'''
        self.assertTrue(TestAST.test(line, expect, 542))

    def test_543(self):
        line = '''Class S:_N{}Class _55_:VV_7{}Class _:Vq{}Class _:Y{}Class _{}'''
        expect = '''Program([ClassDecl(Id(S),Id(_N),[]),ClassDecl(Id(_55_),Id(VV_7),[]),ClassDecl(Id(_),Id(Vq),[]),ClassDecl(Id(_),Id(Y),[]),ClassDecl(Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 543))

    def test_544(self):
        line = '''Class __sj:W7{Var ___r:Int ;}Class y_:_x{}Class _:_{Var _,$_:Array [Array [Boolean ,47],4];}'''
        expect = '''Program([ClassDecl(Id(__sj),Id(W7),[AttributeDecl(Instance,VarDecl(Id(___r),IntType))]),ClassDecl(Id(y_),Id(_x),[]),ClassDecl(Id(_),Id(_),[AttributeDecl(Instance,VarDecl(Id(_),ArrayType(4,ArrayType(47,BoolType)))),AttributeDecl(Static,VarDecl(Id($_),ArrayType(4,ArrayType(47,BoolType))))])])'''
        self.assertTrue(TestAST.test(line, expect, 544))

    def test_545(self):
        line = '''Class ff{}Class fRb{Constructor (){ {}Return ;}Destructor (){} }'''
        expect = '''Program([ClassDecl(Id(ff),[]),ClassDecl(Id(fRb),[MethodDecl(Id(Constructor),Instance,[],Block([],[Block([],[]),Return(None)])),MethodDecl(Id(Destructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 545))

    def test_546(self):
        line = '''Class _:__I{Var _,$o:String ;Constructor (___O1,nt,_4H1:Int ){Break ;} }'''
        expect = '''Program([ClassDecl(Id(_),Id(__I),[AttributeDecl(Instance,VarDecl(Id(_),StringType)),AttributeDecl(Static,VarDecl(Id($o),StringType)),MethodDecl(Id(Constructor),Instance,[param(Id(___O1),IntType),param(Id(nt),IntType),param(Id(_4H1),IntType)],Block([],[Break]))])])'''
        self.assertTrue(TestAST.test(line, expect, 546))

    def test_547(self):
        line = '''Class ___Ex{B6(Ok__,c,_:Array [Float ,2]){}Constructor (){} }'''
        expect = '''Program([ClassDecl(Id(___Ex),[MethodDecl(Id(B6),Instance,[param(Id(Ok__),ArrayType(2,FloatType)),param(Id(c),ArrayType(2,FloatType)),param(Id(_),ArrayType(2,FloatType))],Block([],[])),MethodDecl(Id(Constructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 547))

    def test_548(self):
        line = '''Class _:_783{Constructor (){} }Class t{Constructor (_:Boolean ){} }Class _:n{}'''
        expect = '''Program([ClassDecl(Id(_),Id(_783),[MethodDecl(Id(Constructor),Instance,[],Block([],[]))]),ClassDecl(Id(t),[MethodDecl(Id(Constructor),Instance,[param(Id(_),BoolType)],Block([],[]))]),ClassDecl(Id(_),Id(n),[])])'''
        self.assertTrue(TestAST.test(line, expect, 548))

    def test_549(self):
        line = '''Class D:D{}Class _{Constructor (L,_,_,j,_,a:Array [Array [Array [Array [Array [Array [Array [Array [Boolean ,0136],48],0b1011001],0b1011001],7_6_0_1],0B1],0b1011001],0B1011000]){} }Class C___:__{}'''
        expect = '''Program([ClassDecl(Id(D),Id(D),[]),ClassDecl(Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(L),ArrayType(88,ArrayType(89,ArrayType(1,ArrayType(7601,ArrayType(89,ArrayType(89,ArrayType(48,ArrayType(94,BoolType))))))))),param(Id(_),ArrayType(88,ArrayType(89,ArrayType(1,ArrayType(7601,ArrayType(89,ArrayType(89,ArrayType(48,ArrayType(94,BoolType))))))))),param(Id(_),ArrayType(88,ArrayType(89,ArrayType(1,ArrayType(7601,ArrayType(89,ArrayType(89,ArrayType(48,ArrayType(94,BoolType))))))))),param(Id(j),ArrayType(88,ArrayType(89,ArrayType(1,ArrayType(7601,ArrayType(89,ArrayType(89,ArrayType(48,ArrayType(94,BoolType))))))))),param(Id(_),ArrayType(88,ArrayType(89,ArrayType(1,ArrayType(7601,ArrayType(89,ArrayType(89,ArrayType(48,ArrayType(94,BoolType))))))))),param(Id(a),ArrayType(88,ArrayType(89,ArrayType(1,ArrayType(7601,ArrayType(89,ArrayType(89,ArrayType(48,ArrayType(94,BoolType)))))))))],Block([],[]))]),ClassDecl(Id(C___),Id(__),[])])'''
        self.assertTrue(TestAST.test(line, expect, 549))

    def test_550(self):
        line = '''Class M66_A_{}Class g:E8{_(__F:O;_,_,_,__,v:a){} }Class __:q{Var __:Boolean ;}Class c29:_{}Class __{}'''
        expect = '''Program([ClassDecl(Id(M66_A_),[]),ClassDecl(Id(g),Id(E8),[MethodDecl(Id(_),Instance,[param(Id(__F),ClassType(Id(O))),param(Id(_),ClassType(Id(a))),param(Id(_),ClassType(Id(a))),param(Id(_),ClassType(Id(a))),param(Id(__),ClassType(Id(a))),param(Id(v),ClassType(Id(a)))],Block([],[]))]),ClassDecl(Id(__),Id(q),[AttributeDecl(Instance,VarDecl(Id(__),BoolType))]),ClassDecl(Id(c29),Id(_),[]),ClassDecl(Id(__),[])])'''
        self.assertTrue(TestAST.test(line, expect, 550))

    def test_551(self):
        line = '''Class e__:_{Destructor (){}$__k_jm(){} }Class _6f:zC60{}'''
        expect = '''Program([ClassDecl(Id(e__),Id(_),[MethodDecl(Id(Destructor),Instance,[],Block([],[])),MethodDecl(Id($__k_jm),Static,[],Block([],[]))]),ClassDecl(Id(_6f),Id(zC60),[])])'''
        self.assertTrue(TestAST.test(line, expect, 551))

    def test_552(self):
        line = '''Class b:_F{}Class nk:_{}Class K9:___{}Class wY0:Qs_{$C3j(Y,l_:String ;H:t_zb){}Constructor (){} }'''
        expect = '''Program([ClassDecl(Id(b),Id(_F),[]),ClassDecl(Id(nk),Id(_),[]),ClassDecl(Id(K9),Id(___),[]),ClassDecl(Id(wY0),Id(Qs_),[MethodDecl(Id($C3j),Static,[param(Id(Y),StringType),param(Id(l_),StringType),param(Id(H),ClassType(Id(t_zb)))],Block([],[])),MethodDecl(Id(Constructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 552))

    def test_553(self):
        line = '''Class zL:__81{}Class _:_{Var _D,$_:Int ;Destructor (){} }Class _:_{}'''
        expect = '''Program([ClassDecl(Id(zL),Id(__81),[]),ClassDecl(Id(_),Id(_),[AttributeDecl(Instance,VarDecl(Id(_D),IntType)),AttributeDecl(Static,VarDecl(Id($_),IntType)),MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(_),Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 553))

    def test_554(self):
        line = '''Class L_:_{Constructor (O16:String ;_,_:Array [Float ,0X4_A4_6_4];_,C,_55O,X0,MKm:_){} }'''
        expect = '''Program([ClassDecl(Id(L_),Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(O16),StringType),param(Id(_),ArrayType(304228,FloatType)),param(Id(_),ArrayType(304228,FloatType)),param(Id(_),ClassType(Id(_))),param(Id(C),ClassType(Id(_))),param(Id(_55O),ClassType(Id(_))),param(Id(X0),ClassType(Id(_))),param(Id(MKm),ClassType(Id(_)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 554))

    def test_555(self):
        line = '''Class _jZ:Gj{}Class _:c6{Var $_I:Boolean ;Destructor (){} }Class _:__J{}Class _:_{}Class _2_8:T_{}'''
        expect = '''Program([ClassDecl(Id(_jZ),Id(Gj),[]),ClassDecl(Id(_),Id(c6),[AttributeDecl(Static,VarDecl(Id($_I),BoolType)),MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(_),Id(__J),[]),ClassDecl(Id(_),Id(_),[]),ClassDecl(Id(_2_8),Id(T_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 555))

    def test_556(self):
        line = '''Class i_{}Class _:_o{}Class O_:_{}Class _1{}Class Um:A_8_2m{}Class _W__tC1:_{}Class _:G__i__{}Class _{}Class _{}Class _M:_{$_(){} }'''
        expect = '''Program([ClassDecl(Id(i_),[]),ClassDecl(Id(_),Id(_o),[]),ClassDecl(Id(O_),Id(_),[]),ClassDecl(Id(_1),[]),ClassDecl(Id(Um),Id(A_8_2m),[]),ClassDecl(Id(_W__tC1),Id(_),[]),ClassDecl(Id(_),Id(G__i__),[]),ClassDecl(Id(_),[]),ClassDecl(Id(_),[]),ClassDecl(Id(_M),Id(_),[MethodDecl(Id($_),Static,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 556))

    def test_557(self):
        line = '''Class S4:TD9{}Class l4o:e_{Constructor (){}Var $_j,$_,A28,_i:Array [Array [Boolean ,71],0X97];Constructor (XK_n:String ;Ds,_:Array [Boolean ,04_7_0]){} }'''
        expect = '''Program([ClassDecl(Id(S4),Id(TD9),[]),ClassDecl(Id(l4o),Id(e_),[MethodDecl(Id(Constructor),Instance,[],Block([],[])),AttributeDecl(Static,VarDecl(Id($_j),ArrayType(151,ArrayType(71,BoolType)))),AttributeDecl(Static,VarDecl(Id($_),ArrayType(151,ArrayType(71,BoolType)))),AttributeDecl(Instance,VarDecl(Id(A28),ArrayType(151,ArrayType(71,BoolType)))),AttributeDecl(Instance,VarDecl(Id(_i),ArrayType(151,ArrayType(71,BoolType)))),MethodDecl(Id(Constructor),Instance,[param(Id(XK_n),StringType),param(Id(Ds),ArrayType(312,BoolType)),param(Id(_),ArrayType(312,BoolType))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 557))

    def test_558(self):
        line = '''Class _1J:k{}Class _:_t{_d(V:String ){} }Class __4w:_4p_8{Destructor (){}Destructor (){} }'''
        expect = '''Program([ClassDecl(Id(_1J),Id(k),[]),ClassDecl(Id(_),Id(_t),[MethodDecl(Id(_d),Instance,[param(Id(V),StringType)],Block([],[]))]),ClassDecl(Id(__4w),Id(_4p_8),[MethodDecl(Id(Destructor),Instance,[],Block([],[])),MethodDecl(Id(Destructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 558))

    def test_559(self):
        line = '''Class _{}Class _:_{}Class zC:UMd_{}Class _9{}Class K_9C___:gh_{}'''
        expect = '''Program([ClassDecl(Id(_),[]),ClassDecl(Id(_),Id(_),[]),ClassDecl(Id(zC),Id(UMd_),[]),ClassDecl(Id(_9),[]),ClassDecl(Id(K_9C___),Id(gh_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 559))

    def test_560(self):
        line = '''Class Y{}Class _4:w{Var $_:Boolean ;Destructor (){} }Class s{}Class _3y_:k{}'''
        expect = '''Program([ClassDecl(Id(Y),[]),ClassDecl(Id(_4),Id(w),[AttributeDecl(Static,VarDecl(Id($_),BoolType)),MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(s),[]),ClassDecl(Id(_3y_),Id(k),[])])'''
        self.assertTrue(TestAST.test(line, expect, 560))

    def test_561(self):
        line = '''Class _O{Var _3,_:String ;Var $O0,$6C39B:Array [Array [Boolean ,0446],04_2];}'''
        expect = '''Program([ClassDecl(Id(_O),[AttributeDecl(Instance,VarDecl(Id(_3),StringType)),AttributeDecl(Instance,VarDecl(Id(_),StringType)),AttributeDecl(Static,VarDecl(Id($O0),ArrayType(34,ArrayType(294,BoolType)))),AttributeDecl(Static,VarDecl(Id($6C39B),ArrayType(34,ArrayType(294,BoolType))))])])'''
        self.assertTrue(TestAST.test(line, expect, 561))

    def test_562(self):
        line = '''Class p:_E{}Class _498:T{Var $p:d;Var $pm:Boolean ;Var __6:_;Constructor (_,_:Float ;_,G,p:Boolean ){} }'''
        expect = '''Program([ClassDecl(Id(p),Id(_E),[]),ClassDecl(Id(_498),Id(T),[AttributeDecl(Static,VarDecl(Id($p),ClassType(Id(d)))),AttributeDecl(Static,VarDecl(Id($pm),BoolType)),AttributeDecl(Instance,VarDecl(Id(__6),ClassType(Id(_)))),MethodDecl(Id(Constructor),Instance,[param(Id(_),FloatType),param(Id(_),FloatType),param(Id(_),BoolType),param(Id(G),BoolType),param(Id(p),BoolType)],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 562))

    def test_563(self):
        line = '''Class _7:_{_o_(y3:Array [Array [Array [Float ,0xE_5],05_5],0x4D]){} }'''
        expect = '''Program([ClassDecl(Id(_7),Id(_),[MethodDecl(Id(_o_),Instance,[param(Id(y3),ArrayType(77,ArrayType(45,ArrayType(229,FloatType))))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 563))

    def test_564(self):
        line = '''Class f__{Var e,$_:Float ;}Class v1_u89_{Constructor (){}$8(z,_,_86,oxQ0,o:Array [String ,0123]){} }Class K{}'''
        expect = '''Program([ClassDecl(Id(f__),[AttributeDecl(Instance,VarDecl(Id(e),FloatType)),AttributeDecl(Static,VarDecl(Id($_),FloatType))]),ClassDecl(Id(v1_u89_),[MethodDecl(Id(Constructor),Instance,[],Block([],[])),MethodDecl(Id($8),Static,[param(Id(z),ArrayType(83,StringType)),param(Id(_),ArrayType(83,StringType)),param(Id(_86),ArrayType(83,StringType)),param(Id(oxQ0),ArrayType(83,StringType)),param(Id(o),ArrayType(83,StringType))],Block([],[]))]),ClassDecl(Id(K),[])])'''
        self.assertTrue(TestAST.test(line, expect, 564))

    def test_565(self):
        line = '''Class sh5_{Constructor (___,_:String ;q:m;_,N,ID:Array [Array [Array [Array [Array [Array [Array [String ,0XBB],0xC],0X6],024],88],0X28],024]){} }'''
        expect = '''Program([ClassDecl(Id(sh5_),[MethodDecl(Id(Constructor),Instance,[param(Id(___),StringType),param(Id(_),StringType),param(Id(q),ClassType(Id(m))),param(Id(_),ArrayType(20,ArrayType(40,ArrayType(88,ArrayType(20,ArrayType(6,ArrayType(12,ArrayType(187,StringType)))))))),param(Id(N),ArrayType(20,ArrayType(40,ArrayType(88,ArrayType(20,ArrayType(6,ArrayType(12,ArrayType(187,StringType)))))))),param(Id(ID),ArrayType(20,ArrayType(40,ArrayType(88,ArrayType(20,ArrayType(6,ArrayType(12,ArrayType(187,StringType))))))))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 565))

    def test_566(self):
        line = '''Class _1:Q50{}Class __3_Y{Constructor (_3_0:Float ;Z,_2:Int ){}Destructor (){} }'''
        expect = '''Program([ClassDecl(Id(_1),Id(Q50),[]),ClassDecl(Id(__3_Y),[MethodDecl(Id(Constructor),Instance,[param(Id(_3_0),FloatType),param(Id(Z),IntType),param(Id(_2),IntType)],Block([],[])),MethodDecl(Id(Destructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 566))

    def test_567(self):
        line = '''Class s_{Constructor (__a,_5JIq18_:h){}Constructor (){} }'''
        expect = '''Program([ClassDecl(Id(s_),[MethodDecl(Id(Constructor),Instance,[param(Id(__a),ClassType(Id(h))),param(Id(_5JIq18_),ClassType(Id(h)))],Block([],[])),MethodDecl(Id(Constructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 567))

    def test_568(self):
        line = '''Class a:_{Destructor (){Break ;}$_(_42:Boolean ;___:Boolean ;_20_:Array [Array [String ,0B111101],45]){} }'''
        expect = '''Program([ClassDecl(Id(a),Id(_),[MethodDecl(Id(Destructor),Instance,[],Block([],[Break])),MethodDecl(Id($_),Static,[param(Id(_42),BoolType),param(Id(___),BoolType),param(Id(_20_),ArrayType(45,ArrayType(61,StringType)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 568))

    def test_569(self):
        line = '''Class t:fO83q{Constructor (_0S:Array [Float ,0B1]){}Constructor (){} }'''
        expect = '''Program([ClassDecl(Id(t),Id(fO83q),[MethodDecl(Id(Constructor),Instance,[param(Id(_0S),ArrayType(1,FloatType))],Block([],[])),MethodDecl(Id(Constructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 569))

    def test_570(self):
        line = '''Class _1_2:v{Constructor (Y:Array [Array [Array [String ,0B1100000],0XD],0b111]){}Var _6_h,_s:S6;}'''
        expect = '''Program([ClassDecl(Id(_1_2),Id(v),[MethodDecl(Id(Constructor),Instance,[param(Id(Y),ArrayType(7,ArrayType(13,ArrayType(96,StringType))))],Block([],[])),AttributeDecl(Instance,VarDecl(Id(_6_h),ClassType(Id(S6)))),AttributeDecl(Instance,VarDecl(Id(_s),ClassType(Id(S6))))])])'''
        self.assertTrue(TestAST.test(line, expect, 570))

    def test_571(self):
        line = '''Class P_{j(){} }Class _{Var $__:Array [Array [Boolean ,0x38],390];}'''
        expect = '''Program([ClassDecl(Id(P_),[MethodDecl(Id(j),Instance,[],Block([],[]))]),ClassDecl(Id(_),[AttributeDecl(Static,VarDecl(Id($__),ArrayType(390,ArrayType(56,BoolType))))])])'''
        self.assertTrue(TestAST.test(line, expect, 571))

    def test_572(self):
        line = '''Class M{Constructor (){}$_(){}Var _:Array [Array [String ,0B100110],060];}'''
        expect = '''Program([ClassDecl(Id(M),[MethodDecl(Id(Constructor),Instance,[],Block([],[])),MethodDecl(Id($_),Static,[],Block([],[])),AttributeDecl(Instance,VarDecl(Id(_),ArrayType(48,ArrayType(38,StringType))))])])'''
        self.assertTrue(TestAST.test(line, expect, 572))

    def test_573(self):
        line = '''Class _1:_{Var x_8:Array [Array [Array [Float ,0B111001],0x2],0116];}'''
        expect = '''Program([ClassDecl(Id(_1),Id(_),[AttributeDecl(Instance,VarDecl(Id(x_8),ArrayType(78,ArrayType(2,ArrayType(57,FloatType)))))])])'''
        self.assertTrue(TestAST.test(line, expect, 573))

    def test_574(self):
        line = '''Class _0_{}Class m_:_0{Constructor (){}Var $_:Boolean ;}Class _S{}Class u_Q{}'''
        expect = '''Program([ClassDecl(Id(_0_),[]),ClassDecl(Id(m_),Id(_0),[MethodDecl(Id(Constructor),Instance,[],Block([],[])),AttributeDecl(Static,VarDecl(Id($_),BoolType))]),ClassDecl(Id(_S),[]),ClassDecl(Id(u_Q),[])])'''
        self.assertTrue(TestAST.test(line, expect, 574))

    def test_575(self):
        line = '''Class __5:T_J{}Class _:C{Destructor (){Continue ;{} }}Class m{}Class _n{g(_:Int ){} }Class E_:_8{z97(){} }'''
        expect = '''Program([ClassDecl(Id(__5),Id(T_J),[]),ClassDecl(Id(_),Id(C),[MethodDecl(Id(Destructor),Instance,[],Block([],[Continue,Block([],[])]))]),ClassDecl(Id(m),[]),ClassDecl(Id(_n),[MethodDecl(Id(g),Instance,[param(Id(_),IntType)],Block([],[]))]),ClassDecl(Id(E_),Id(_8),[MethodDecl(Id(z97),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 575))

    def test_576(self):
        line = '''Class __Abv2:_{V_ri(){Var Ps,_:j;Break ;} }Class _{Destructor (){} }'''
        expect = '''Program([ClassDecl(Id(__Abv2),Id(_),[MethodDecl(Id(V_ri),Instance,[],Block([VarDecl(Id(Ps),ClassType(Id(j))),VarDecl(Id(_),ClassType(Id(j)))],[Break]))]),ClassDecl(Id(_),[MethodDecl(Id(Destructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 576))

    def test_577(self):
        line = '''Class _{Var $3311r:Array [Array [String ,0B1_1_1_0],0b110];Constructor (_,ao4:String ){} }Class _{}'''
        expect = '''Program([ClassDecl(Id(_),[AttributeDecl(Static,VarDecl(Id($3311r),ArrayType(6,ArrayType(14,StringType)))),MethodDecl(Id(Constructor),Instance,[param(Id(_),StringType),param(Id(ao4),StringType)],Block([],[]))]),ClassDecl(Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 577))

    def test_578(self):
        line = '''Class F{Var $7_:_;}Class x9xs{_(__:_1){}Constructor (__:___){} }'''
        expect = '''Program([ClassDecl(Id(F),[AttributeDecl(Static,VarDecl(Id($7_),ClassType(Id(_))))]),ClassDecl(Id(x9xs),[MethodDecl(Id(_),Instance,[param(Id(__),ClassType(Id(_1)))],Block([],[])),MethodDecl(Id(Constructor),Instance,[param(Id(__),ClassType(Id(___)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 578))

    def test_579(self):
        line = '''Class _{Constructor (_1:Array [Array [Float ,43],43];_e,SFH_:OQ;Ye3:Array [Array [Boolean ,037],0XB];H,__1:Array [Boolean ,0B1]){Break ;Var l6_:Array [Array [Array [Array [Array [Int ,0b100001],02],032],0B1_011_11_0_1],0X49];} }'''
        expect = '''Program([ClassDecl(Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(_1),ArrayType(43,ArrayType(43,FloatType))),param(Id(_e),ClassType(Id(OQ))),param(Id(SFH_),ClassType(Id(OQ))),param(Id(Ye3),ArrayType(11,ArrayType(31,BoolType))),param(Id(H),ArrayType(1,BoolType)),param(Id(__1),ArrayType(1,BoolType))],Block([VarDecl(Id(l6_),ArrayType(73,ArrayType(189,ArrayType(26,ArrayType(2,ArrayType(33,IntType))))))],[Break]))])])'''
        self.assertTrue(TestAST.test(line, expect, 579))

    def test_580(self):
        line = '''Class _:_6{Destructor (){Break ;Continue ;}Constructor (_:Array [Array [String ,02],69];m_B,Z,_:_;r_Y_,_D4:Array [Float ,0x2C]){} }'''
        expect = '''Program([ClassDecl(Id(_),Id(_6),[MethodDecl(Id(Destructor),Instance,[],Block([],[Break,Continue])),MethodDecl(Id(Constructor),Instance,[param(Id(_),ArrayType(69,ArrayType(2,StringType))),param(Id(m_B),ClassType(Id(_))),param(Id(Z),ClassType(Id(_))),param(Id(_),ClassType(Id(_))),param(Id(r_Y_),ArrayType(44,FloatType)),param(Id(_D4),ArrayType(44,FloatType))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 580))

    def test_581(self):
        line = '''Class _qH{Constructor (_,_w8__:Float ;__:Array [Array [Array [Array [Array [String ,0103],0103],054],0103],0103];t3:Array [String ,01]){}Var $_,$b03_Q,$7__q,$v,h:Array [Array [Boolean ,0b1010110],0B1111];Destructor (){} }'''
        expect = '''Program([ClassDecl(Id(_qH),[MethodDecl(Id(Constructor),Instance,[param(Id(_),FloatType),param(Id(_w8__),FloatType),param(Id(__),ArrayType(67,ArrayType(67,ArrayType(44,ArrayType(67,ArrayType(67,StringType)))))),param(Id(t3),ArrayType(1,StringType))],Block([],[])),AttributeDecl(Static,VarDecl(Id($_),ArrayType(15,ArrayType(86,BoolType)))),AttributeDecl(Static,VarDecl(Id($b03_Q),ArrayType(15,ArrayType(86,BoolType)))),AttributeDecl(Static,VarDecl(Id($7__q),ArrayType(15,ArrayType(86,BoolType)))),AttributeDecl(Static,VarDecl(Id($v),ArrayType(15,ArrayType(86,BoolType)))),AttributeDecl(Instance,VarDecl(Id(h),ArrayType(15,ArrayType(86,BoolType)))),MethodDecl(Id(Destructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 581))

    def test_582(self):
        line = '''Class N:_w_p{snw(n27:Boolean ){} }Class _{Var $__8,$__:Float ;}'''
        expect = '''Program([ClassDecl(Id(N),Id(_w_p),[MethodDecl(Id(snw),Instance,[param(Id(n27),BoolType)],Block([],[]))]),ClassDecl(Id(_),[AttributeDecl(Static,VarDecl(Id($__8),FloatType)),AttributeDecl(Static,VarDecl(Id($__),FloatType))])])'''
        self.assertTrue(TestAST.test(line, expect, 582))

    def test_583(self):
        line = '''Class _3:O_{}Class a0:P{}Class c6h6_R__{}Class g:G{}Class _:K{}'''
        expect = '''Program([ClassDecl(Id(_3),Id(O_),[]),ClassDecl(Id(a0),Id(P),[]),ClassDecl(Id(c6h6_R__),[]),ClassDecl(Id(g),Id(G),[]),ClassDecl(Id(_),Id(K),[])])'''
        self.assertTrue(TestAST.test(line, expect, 583))

    def test_584(self):
        line = '''Class _Q74{Var n,_,$1,p,$1,$w1N,$L_l,_e16,O_k_v_:IM_;}'''
        expect = '''Program([ClassDecl(Id(_Q74),[AttributeDecl(Instance,VarDecl(Id(n),ClassType(Id(IM_)))),AttributeDecl(Instance,VarDecl(Id(_),ClassType(Id(IM_)))),AttributeDecl(Static,VarDecl(Id($1),ClassType(Id(IM_)))),AttributeDecl(Instance,VarDecl(Id(p),ClassType(Id(IM_)))),AttributeDecl(Static,VarDecl(Id($1),ClassType(Id(IM_)))),AttributeDecl(Static,VarDecl(Id($w1N),ClassType(Id(IM_)))),AttributeDecl(Static,VarDecl(Id($L_l),ClassType(Id(IM_)))),AttributeDecl(Instance,VarDecl(Id(_e16),ClassType(Id(IM_)))),AttributeDecl(Instance,VarDecl(Id(O_k_v_),ClassType(Id(IM_))))])])'''
        self.assertTrue(TestAST.test(line, expect, 584))

    def test_585(self):
        line = '''Class _:_{Constructor (){Break ;} }Class _{Var _6Q:String ;}Class _:s{}'''
        expect = '''Program([ClassDecl(Id(_),Id(_),[MethodDecl(Id(Constructor),Instance,[],Block([],[Break]))]),ClassDecl(Id(_),[AttributeDecl(Instance,VarDecl(Id(_6Q),StringType))]),ClassDecl(Id(_),Id(s),[])])'''
        self.assertTrue(TestAST.test(line, expect, 585))

    def test_586(self):
        line = '''Class pF{N_(UvC67:Boolean ){}Destructor (){} }Class _8{Var $__:_;}Class h:j{}'''
        expect = '''Program([ClassDecl(Id(pF),[MethodDecl(Id(N_),Instance,[param(Id(UvC67),BoolType)],Block([],[])),MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(_8),[AttributeDecl(Static,VarDecl(Id($__),ClassType(Id(_))))]),ClassDecl(Id(h),Id(j),[])])'''
        self.assertTrue(TestAST.test(line, expect, 586))

    def test_587(self):
        line = '''Class _:_{Constructor (){__::$3();Break ;}ZJ_K9(){} }Class RZ:j7{_5(){} }'''
        expect = '''Program([ClassDecl(Id(_),Id(_),[MethodDecl(Id(Constructor),Instance,[],Block([],[Call(Id(__),Id($3),[]),Break])),MethodDecl(Id(ZJ_K9),Instance,[],Block([],[]))]),ClassDecl(Id(RZ),Id(j7),[MethodDecl(Id(_5),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 587))

    def test_588(self):
        line = '''Class SS0:A{Destructor (){}Constructor (F_,_,_:Boolean ;d:Float ;_9,_,p,_7,_oD2,_S,__,__:_){} }Class NQ_:_{}'''
        expect = '''Program([ClassDecl(Id(SS0),Id(A),[MethodDecl(Id(Destructor),Instance,[],Block([],[])),MethodDecl(Id(Constructor),Instance,[param(Id(F_),BoolType),param(Id(_),BoolType),param(Id(_),BoolType),param(Id(d),FloatType),param(Id(_9),ClassType(Id(_))),param(Id(_),ClassType(Id(_))),param(Id(p),ClassType(Id(_))),param(Id(_7),ClassType(Id(_))),param(Id(_oD2),ClassType(Id(_))),param(Id(_S),ClassType(Id(_))),param(Id(__),ClassType(Id(_))),param(Id(__),ClassType(Id(_)))],Block([],[]))]),ClassDecl(Id(NQ_),Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 588))

    def test_589(self):
        line = '''Class h:s_1{Constructor (_7,_,G,q_:Array [Array [Array [Array [Array [Array [Array [Array [String ,034_7],0X4A],0x59],0x7_A4],74],03],534],05]){} }'''
        expect = '''Program([ClassDecl(Id(h),Id(s_1),[MethodDecl(Id(Constructor),Instance,[param(Id(_7),ArrayType(5,ArrayType(534,ArrayType(3,ArrayType(74,ArrayType(1956,ArrayType(89,ArrayType(74,ArrayType(231,StringType))))))))),param(Id(_),ArrayType(5,ArrayType(534,ArrayType(3,ArrayType(74,ArrayType(1956,ArrayType(89,ArrayType(74,ArrayType(231,StringType))))))))),param(Id(G),ArrayType(5,ArrayType(534,ArrayType(3,ArrayType(74,ArrayType(1956,ArrayType(89,ArrayType(74,ArrayType(231,StringType))))))))),param(Id(q_),ArrayType(5,ArrayType(534,ArrayType(3,ArrayType(74,ArrayType(1956,ArrayType(89,ArrayType(74,ArrayType(231,StringType)))))))))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 589))

    def test_590(self):
        line = '''Class z_5:_{Constructor (Y:Boolean ){}$_(_9Q:Array [Array [Array [Array [Array [Array [Array [Array [Array [Boolean ,3],033],0XA3],0b10],6],0b10_11],0B1_10],0x30_9A],0B1];_v,w,A,M:Array [Array [Float ,42],0X75_9];j,Vp,g:Boolean ;_,_7,iNr:U;r_:Array [Array [Array [Int ,0B100101],0X3],0b1011011]){} }Class _:M{}Class _{Constructor (iZ__,R,w,_:Boolean ){} }'''
        expect = '''Program([ClassDecl(Id(z_5),Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(Y),BoolType)],Block([],[])),MethodDecl(Id($_),Static,[param(Id(_9Q),ArrayType(1,ArrayType(12442,ArrayType(6,ArrayType(11,ArrayType(6,ArrayType(2,ArrayType(163,ArrayType(27,ArrayType(3,BoolType)))))))))),param(Id(_v),ArrayType(1881,ArrayType(42,FloatType))),param(Id(w),ArrayType(1881,ArrayType(42,FloatType))),param(Id(A),ArrayType(1881,ArrayType(42,FloatType))),param(Id(M),ArrayType(1881,ArrayType(42,FloatType))),param(Id(j),BoolType),param(Id(Vp),BoolType),param(Id(g),BoolType),param(Id(_),ClassType(Id(U))),param(Id(_7),ClassType(Id(U))),param(Id(iNr),ClassType(Id(U))),param(Id(r_),ArrayType(91,ArrayType(3,ArrayType(37,IntType))))],Block([],[]))]),ClassDecl(Id(_),Id(M),[]),ClassDecl(Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(iZ__),BoolType),param(Id(R),BoolType),param(Id(w),BoolType),param(Id(_),BoolType)],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 590))

    def test_591(self):
        line = '''Class U:E{}Class s:S{$L(i69,_,I:S____T){} }Class I:_4{}Class Wp__{}Class _{}'''
        expect = '''Program([ClassDecl(Id(U),Id(E),[]),ClassDecl(Id(s),Id(S),[MethodDecl(Id($L),Static,[param(Id(i69),ClassType(Id(S____T))),param(Id(_),ClassType(Id(S____T))),param(Id(I),ClassType(Id(S____T)))],Block([],[]))]),ClassDecl(Id(I),Id(_4),[]),ClassDecl(Id(Wp__),[]),ClassDecl(Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 591))

    def test_592(self):
        line = '''Class fS:knI_{Destructor (){}Constructor (){}Destructor (){}Destructor (){} }'''
        expect = '''Program([ClassDecl(Id(fS),Id(knI_),[MethodDecl(Id(Destructor),Instance,[],Block([],[])),MethodDecl(Id(Constructor),Instance,[],Block([],[])),MethodDecl(Id(Destructor),Instance,[],Block([],[])),MethodDecl(Id(Destructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 592))

    def test_593(self):
        line = '''Class __5{R(_:Array [Array [Array [String ,0b1100000],0B1],50];y,K,k,J_,z,r,x_:Array [Array [Float ,0b111],0x7];PE:Float ){ {}z::$8m__();}_5m_(D:Array [String ,50]){} }'''
        expect = '''Program([ClassDecl(Id(__5),[MethodDecl(Id(R),Instance,[param(Id(_),ArrayType(50,ArrayType(1,ArrayType(96,StringType)))),param(Id(y),ArrayType(7,ArrayType(7,FloatType))),param(Id(K),ArrayType(7,ArrayType(7,FloatType))),param(Id(k),ArrayType(7,ArrayType(7,FloatType))),param(Id(J_),ArrayType(7,ArrayType(7,FloatType))),param(Id(z),ArrayType(7,ArrayType(7,FloatType))),param(Id(r),ArrayType(7,ArrayType(7,FloatType))),param(Id(x_),ArrayType(7,ArrayType(7,FloatType))),param(Id(PE),FloatType)],Block([],[Block([],[]),Call(Id(z),Id($8m__),[])])),MethodDecl(Id(_5m_),Instance,[param(Id(D),ArrayType(50,StringType))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 593))

    def test_594(self):
        line = '''Class te_82:_a{}Class f_:A2{}Class _{Var $0:Array [String ,0B111];}'''
        expect = '''Program([ClassDecl(Id(te_82),Id(_a),[]),ClassDecl(Id(f_),Id(A2),[]),ClassDecl(Id(_),[AttributeDecl(Static,VarDecl(Id($0),ArrayType(7,StringType)))])])'''
        self.assertTrue(TestAST.test(line, expect, 594))

    def test_595(self):
        line = '''Class s0{}Class _:y{Var $__:Float ;}Class G:K3{}Class dS{}Class t8{}'''
        expect = '''Program([ClassDecl(Id(s0),[]),ClassDecl(Id(_),Id(y),[AttributeDecl(Static,VarDecl(Id($__),FloatType))]),ClassDecl(Id(G),Id(K3),[]),ClassDecl(Id(dS),[]),ClassDecl(Id(t8),[])])'''
        self.assertTrue(TestAST.test(line, expect, 595))

    def test_596(self):
        line = '''Class Wk:_{Constructor (d:Array [Array [Int ,0x3],0x3];_L,V:Boolean ){} }Class _5q8{}Class NF_{}'''
        expect = '''Program([ClassDecl(Id(Wk),Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(d),ArrayType(3,ArrayType(3,IntType))),param(Id(_L),BoolType),param(Id(V),BoolType)],Block([],[]))]),ClassDecl(Id(_5q8),[]),ClassDecl(Id(NF_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 596))

    def test_597(self):
        line = '''Class _j{Constructor (_,_4m_q_R6r:_){}Var $o:String ;Val $3O:H=_::$_;}'''
        expect = '''Program([ClassDecl(Id(_j),[MethodDecl(Id(Constructor),Instance,[param(Id(_),ClassType(Id(_))),param(Id(_4m_q_R6r),ClassType(Id(_)))],Block([],[])),AttributeDecl(Static,VarDecl(Id($o),StringType)),AttributeDecl(Instance,ConstDecl(Id(_),ClassType(Id(H)),FieldAccess(Id(_),Id($_))))])])'''
        self.assertTrue(TestAST.test(line, expect, 597))

    def test_598(self):
        line = '''Class _mJa{$5_(B1,__,F,_C:String ;C:Float ;_,m,_:String ;V,t6:_;_,_,X,_:Float ;_:_){Continue ;} }'''
        expect = '''Program([ClassDecl(Id(_mJa),[MethodDecl(Id($5_),Static,[param(Id(B1),StringType),param(Id(__),StringType),param(Id(F),StringType),param(Id(_C),StringType),param(Id(C),FloatType),param(Id(_),StringType),param(Id(m),StringType),param(Id(_),StringType),param(Id(V),ClassType(Id(_))),param(Id(t6),ClassType(Id(_))),param(Id(_),FloatType),param(Id(_),FloatType),param(Id(X),FloatType),param(Id(_),FloatType),param(Id(_),ClassType(Id(_)))],Block([],[Continue]))])])'''
        self.assertTrue(TestAST.test(line, expect, 598))

    def test_599(self):
        line = '''Class _{}Class _:y_1S{Var $_:Array [Array [Array [Array [Array [Array [Array [String ,55],0x4D],065],0XB],0x4D],0X7],0B111110];Destructor (){Var x8_s,w_:Array [Float ,55];} }'''
        expect = '''Program([ClassDecl(Id(_),[]),ClassDecl(Id(_),Id(y_1S),[AttributeDecl(Static,VarDecl(Id($_),ArrayType(62,ArrayType(7,ArrayType(77,ArrayType(11,ArrayType(53,ArrayType(77,ArrayType(55,StringType))))))))),MethodDecl(Id(Destructor),Instance,[],Block([VarDecl(Id(x8_s),ArrayType(55,FloatType)),VarDecl(Id(w_),ArrayType(55,FloatType))],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 599))

    def test_600(self):
        line = '''Class l:X{Constructor (g_4:Array [Array [Boolean ,0131],9]){} }Class __04:_{Var $P1_,U,$q_,_4:Float ;Destructor (){} }'''
        expect = '''Program([ClassDecl(Id(l),Id(X),[MethodDecl(Id(Constructor),Instance,[param(Id(g_4),ArrayType(9,ArrayType(89,BoolType)))],Block([],[]))]),ClassDecl(Id(__04),Id(_),[AttributeDecl(Static,VarDecl(Id($P1_),FloatType)),AttributeDecl(Instance,VarDecl(Id(U),FloatType)),AttributeDecl(Static,VarDecl(Id($q_),FloatType)),AttributeDecl(Instance,VarDecl(Id(_4),FloatType)),MethodDecl(Id(Destructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 600))

    def test_601(self):
        line = '''Class DS_{Constructor (){ {} }}Class t1_1OK_:v{}Class __5_:_{}'''
        expect = '''Program([ClassDecl(Id(DS_),[MethodDecl(Id(Constructor),Instance,[],Block([],[Block([],[])]))]),ClassDecl(Id(t1_1OK_),Id(v),[]),ClassDecl(Id(__5_),Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 601))

    def test_602(self):
        line = '''Class C_:_{Destructor (){} }Class cV:__7_93{$__(){} }Class _{$_(_:Array [Boolean ,8];_:w_){Continue ;} }Class R:_L{}'''
        expect = '''Program([ClassDecl(Id(C_),Id(_),[MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(cV),Id(__7_93),[MethodDecl(Id($__),Static,[],Block([],[]))]),ClassDecl(Id(_),[MethodDecl(Id($_),Static,[param(Id(_),ArrayType(8,BoolType)),param(Id(_),ClassType(Id(w_)))],Block([],[Continue]))]),ClassDecl(Id(R),Id(_L),[])])'''
        self.assertTrue(TestAST.test(line, expect, 602))

    def test_603(self):
        line = '''Class PT5{Var $_:Array [Int ,0B1];Var $1K_z_,$0,$_X,$Q,$59l_v,q,__7:c;}'''
        expect = '''Program([ClassDecl(Id(PT5),[AttributeDecl(Static,VarDecl(Id($_),ArrayType(1,IntType))),AttributeDecl(Static,VarDecl(Id($1K_z_),ClassType(Id(c)))),AttributeDecl(Static,VarDecl(Id($0),ClassType(Id(c)))),AttributeDecl(Static,VarDecl(Id($_X),ClassType(Id(c)))),AttributeDecl(Static,VarDecl(Id($Q),ClassType(Id(c)))),AttributeDecl(Static,VarDecl(Id($59l_v),ClassType(Id(c)))),AttributeDecl(Instance,VarDecl(Id(q),ClassType(Id(c)))),AttributeDecl(Instance,VarDecl(Id(__7),ClassType(Id(c))))])])'''
        self.assertTrue(TestAST.test(line, expect, 603))

    def test_604(self):
        line = '''Class E_:l41{}Class _3:L_QB{Constructor (e:String ;_jQ14:Boolean ){} }'''
        expect = '''Program([ClassDecl(Id(E_),Id(l41),[]),ClassDecl(Id(_3),Id(L_QB),[MethodDecl(Id(Constructor),Instance,[param(Id(e),StringType),param(Id(_jQ14),BoolType)],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 604))

    def test_605(self):
        line = '''Class _Y:B{}Class _:o{Constructor (s,_5:Boolean ){Break ;} }Class h:__7{}'''
        expect = '''Program([ClassDecl(Id(_Y),Id(B),[]),ClassDecl(Id(_),Id(o),[MethodDecl(Id(Constructor),Instance,[param(Id(s),BoolType),param(Id(_5),BoolType)],Block([],[Break]))]),ClassDecl(Id(h),Id(__7),[])])'''
        self.assertTrue(TestAST.test(line, expect, 605))

    def test_606(self):
        line = '''Class b8_{_(_,j,F_,Uq_7_5,f_A,x:Array [Array [Array [Int ,99],6_1],0B1100100]){}Var K:Float ;}Class _5:_{}'''
        expect = '''Program([ClassDecl(Id(b8_),[MethodDecl(Id(_),Instance,[param(Id(_),ArrayType(100,ArrayType(61,ArrayType(99,IntType)))),param(Id(j),ArrayType(100,ArrayType(61,ArrayType(99,IntType)))),param(Id(F_),ArrayType(100,ArrayType(61,ArrayType(99,IntType)))),param(Id(Uq_7_5),ArrayType(100,ArrayType(61,ArrayType(99,IntType)))),param(Id(f_A),ArrayType(100,ArrayType(61,ArrayType(99,IntType)))),param(Id(x),ArrayType(100,ArrayType(61,ArrayType(99,IntType))))],Block([],[])),AttributeDecl(Instance,VarDecl(Id(K),FloatType))]),ClassDecl(Id(_5),Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 606))

    def test_607(self):
        line = '''Class gG{Var _U:Array [String ,0107];}Class b:__3LT{}Class _4j:_{Var $_:N;}'''
        expect = '''Program([ClassDecl(Id(gG),[AttributeDecl(Instance,VarDecl(Id(_U),ArrayType(71,StringType)))]),ClassDecl(Id(b),Id(__3LT),[]),ClassDecl(Id(_4j),Id(_),[AttributeDecl(Static,VarDecl(Id($_),ClassType(Id(N))))])])'''
        self.assertTrue(TestAST.test(line, expect, 607))

    def test_608(self):
        line = '''Class __:_{Var W,$B,$ED__:Array [Array [Array [Int ,0B1_1],013],0B100100];Destructor (){} }'''
        expect = '''Program([ClassDecl(Id(__),Id(_),[AttributeDecl(Instance,VarDecl(Id(W),ArrayType(36,ArrayType(11,ArrayType(3,IntType))))),AttributeDecl(Static,VarDecl(Id($B),ArrayType(36,ArrayType(11,ArrayType(3,IntType))))),AttributeDecl(Static,VarDecl(Id($ED__),ArrayType(36,ArrayType(11,ArrayType(3,IntType))))),MethodDecl(Id(Destructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 608))

    def test_609(self):
        line = '''Class _6_:v_{}Class q__6:A{Destructor (){}Constructor (){} }'''
        expect = '''Program([ClassDecl(Id(_6_),Id(v_),[]),ClassDecl(Id(q__6),Id(A),[MethodDecl(Id(Destructor),Instance,[],Block([],[])),MethodDecl(Id(Constructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 609))

    def test_610(self):
        line = '''Class _2:_{Constructor (E5,_,r,P_:_E9_e_j_S_;JFW362,_:String ;Y__:Array [Array [Array [Array [Array [Float ,0B101011],0B10_1_10_1],0101],26_3_7],0B1011]){}Constructor (){ {} }}'''
        expect = '''Program([ClassDecl(Id(_2),Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(E5),ClassType(Id(_E9_e_j_S_))),param(Id(_),ClassType(Id(_E9_e_j_S_))),param(Id(r),ClassType(Id(_E9_e_j_S_))),param(Id(P_),ClassType(Id(_E9_e_j_S_))),param(Id(JFW362),StringType),param(Id(_),StringType),param(Id(Y__),ArrayType(11,ArrayType(2637,ArrayType(65,ArrayType(45,ArrayType(43,FloatType))))))],Block([],[])),MethodDecl(Id(Constructor),Instance,[],Block([],[Block([],[])]))])])'''
        self.assertTrue(TestAST.test(line, expect, 610))

    def test_611(self):
        line = '''Class i_0_:V{Constructor (__5,_:Array [Array [Boolean ,0B1],0xD];l:Array [Array [Array [Array [Array [Array [Array [Array [Float ,03_04],0b1_00_0_0],0b1001100],61],61],0B11],2],04]){} }'''
        expect = '''Program([ClassDecl(Id(i_0_),Id(V),[MethodDecl(Id(Constructor),Instance,[param(Id(__5),ArrayType(13,ArrayType(1,BoolType))),param(Id(_),ArrayType(13,ArrayType(1,BoolType))),param(Id(l),ArrayType(4,ArrayType(2,ArrayType(3,ArrayType(61,ArrayType(61,ArrayType(76,ArrayType(16,ArrayType(196,FloatType)))))))))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 611))

    def test_612(self):
        line = '''Class J{Var $E:Array [Array [Boolean ,0xC],0b1];Constructor (_3:Array [String ,0B100100]){} }'''
        expect = '''Program([ClassDecl(Id(J),[AttributeDecl(Static,VarDecl(Id($E),ArrayType(1,ArrayType(12,BoolType)))),MethodDecl(Id(Constructor),Instance,[param(Id(_3),ArrayType(36,StringType))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 612))

    def test_613(self):
        line = '''Class ___:_{}Class __H0{}Class P{Var _:Array [Array [Boolean ,49],0b11];}Class b{}'''
        expect = '''Program([ClassDecl(Id(___),Id(_),[]),ClassDecl(Id(__H0),[]),ClassDecl(Id(P),[AttributeDecl(Instance,VarDecl(Id(_),ArrayType(3,ArrayType(49,BoolType))))]),ClassDecl(Id(b),[])])'''
        self.assertTrue(TestAST.test(line, expect, 613))

    def test_614(self):
        line = '''Class i_{}Class __5_P:wL_9{}Class _s_H:_T1{}Class seC{}'''
        expect = '''Program([ClassDecl(Id(i_),[]),ClassDecl(Id(__5_P),Id(wL_9),[]),ClassDecl(Id(_s_H),Id(_T1),[]),ClassDecl(Id(seC),[])])'''
        self.assertTrue(TestAST.test(line, expect, 614))

    def test_615(self):
        line = '''Class _4:_G{}Class ___4{}Class LhgnGz_:tT{}Class _U3{}Class zM{}'''
        expect = '''Program([ClassDecl(Id(_4),Id(_G),[]),ClassDecl(Id(___4),[]),ClassDecl(Id(LhgnGz_),Id(tT),[]),ClassDecl(Id(_U3),[]),ClassDecl(Id(zM),[])])'''
        self.assertTrue(TestAST.test(line, expect, 615))

    def test_616(self):
        line = '''Class _:K{Constructor (X__:Array [Array [Array [Float ,0X7],0X39],031_675];__V:Array [Array [Array [Array [String ,16],01_6],0x49],0XB];u:xH){Var _506:j;} }Class __7:_w{}Class _I{R(){}Destructor (){} }'''
        expect = '''Program([ClassDecl(Id(_),Id(K),[MethodDecl(Id(Constructor),Instance,[param(Id(X__),ArrayType(13245,ArrayType(57,ArrayType(7,FloatType)))),param(Id(__V),ArrayType(11,ArrayType(73,ArrayType(14,ArrayType(16,StringType))))),param(Id(u),ClassType(Id(xH)))],Block([VarDecl(Id(_506),ClassType(Id(j)))],[]))]),ClassDecl(Id(__7),Id(_w),[]),ClassDecl(Id(_I),[MethodDecl(Id(R),Instance,[],Block([],[])),MethodDecl(Id(Destructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 616))

    def test_617(self):
        line = '''Class _:y9{$yw(_lf:Array [String ,0b1001010];_a:Boolean ;q:Array [Array [String ,06],067]){} }Class __{}Class zn87_:w{}'''
        expect = '''Program([ClassDecl(Id(_),Id(y9),[MethodDecl(Id($yw),Static,[param(Id(_lf),ArrayType(74,StringType)),param(Id(_a),BoolType),param(Id(q),ArrayType(55,ArrayType(6,StringType)))],Block([],[]))]),ClassDecl(Id(__),[]),ClassDecl(Id(zn87_),Id(w),[])])'''
        self.assertTrue(TestAST.test(line, expect, 617))

    def test_618(self):
        line = '''Class _{Destructor (){}Var Z_:Array [Int ,0b1_0];}Class __q0:J{}Class __:_{Constructor (){Continue ;Return ;} }'''
        expect = '''Program([ClassDecl(Id(_),[MethodDecl(Id(Destructor),Instance,[],Block([],[])),AttributeDecl(Instance,VarDecl(Id(Z_),ArrayType(2,IntType)))]),ClassDecl(Id(__q0),Id(J),[]),ClassDecl(Id(__),Id(_),[MethodDecl(Id(Constructor),Instance,[],Block([],[Continue,Return(None)]))])])'''
        self.assertTrue(TestAST.test(line, expect, 618))

    def test_619(self):
        line = '''Class J_:y{Var _,_:Ex6;Var _0M___L:String ;}Class _{Constructor (){} }'''
        expect = '''Program([ClassDecl(Id(J_),Id(y),[AttributeDecl(Instance,VarDecl(Id(_),ClassType(Id(Ex6)))),AttributeDecl(Instance,VarDecl(Id(_),ClassType(Id(Ex6)))),AttributeDecl(Instance,VarDecl(Id(_0M___L),StringType))]),ClassDecl(Id(_),[MethodDecl(Id(Constructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 619))

    def test_620(self):
        line = '''Class _JQ892_75_:Z{}Class ah1h3:h{Constructor (){} }Class _:F_4{}Class c:_{}'''
        expect = '''Program([ClassDecl(Id(_JQ892_75_),Id(Z),[]),ClassDecl(Id(ah1h3),Id(h),[MethodDecl(Id(Constructor),Instance,[],Block([],[]))]),ClassDecl(Id(_),Id(F_4),[]),ClassDecl(Id(c),Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 620))

    def test_621(self):
        line = '''Class x37C4989{}Class a:_{Var $_,Z:_;Var d,$__,$TV_,B0:Array [Int ,0B1_1];}'''
        expect = '''Program([ClassDecl(Id(x37C4989),[]),ClassDecl(Id(a),Id(_),[AttributeDecl(Static,VarDecl(Id($_),ClassType(Id(_)))),AttributeDecl(Instance,VarDecl(Id(Z),ClassType(Id(_)))),AttributeDecl(Instance,VarDecl(Id(d),ArrayType(3,IntType))),AttributeDecl(Static,VarDecl(Id($__),ArrayType(3,IntType))),AttributeDecl(Static,VarDecl(Id($TV_),ArrayType(3,IntType))),AttributeDecl(Instance,VarDecl(Id(B0),ArrayType(3,IntType)))])])'''
        self.assertTrue(TestAST.test(line, expect, 621))

    def test_622(self):
        line = '''Class a{Var $04:a_;a(){} }Class _{}Class _A:f{}Class _y{}'''
        expect = '''Program([ClassDecl(Id(a),[AttributeDecl(Static,VarDecl(Id($04),ClassType(Id(a_)))),MethodDecl(Id(a),Instance,[],Block([],[]))]),ClassDecl(Id(_),[]),ClassDecl(Id(_A),Id(f),[]),ClassDecl(Id(_y),[])])'''
        self.assertTrue(TestAST.test(line, expect, 622))

    def test_623(self):
        line = '''Class __{}Class H_:__K{}Class __:_{$_(_2:_i2p){} }Class A2:__{}'''
        expect = '''Program([ClassDecl(Id(__),[]),ClassDecl(Id(H_),Id(__K),[]),ClassDecl(Id(__),Id(_),[MethodDecl(Id($_),Static,[param(Id(_2),ClassType(Id(_i2p)))],Block([],[]))]),ClassDecl(Id(A2),Id(__),[])])'''
        self.assertTrue(TestAST.test(line, expect, 623))

    def test_624(self):
        line = '''Class t5__:s{Constructor (G,_:Array [Array [Array [Array [Float ,0B1_0],5],0B1],0x49];_E:Int ){Break ;} }Class _I4_o8O5Z__{}'''
        expect = '''Program([ClassDecl(Id(t5__),Id(s),[MethodDecl(Id(Constructor),Instance,[param(Id(G),ArrayType(73,ArrayType(1,ArrayType(5,ArrayType(2,FloatType))))),param(Id(_),ArrayType(73,ArrayType(1,ArrayType(5,ArrayType(2,FloatType))))),param(Id(_E),IntType)],Block([],[Break]))]),ClassDecl(Id(_I4_o8O5Z__),[])])'''
        self.assertTrue(TestAST.test(line, expect, 624))

    def test_625(self):
        line = '''Class _{Var _9K,$_,_,_:Array [Array [Array [Array [Int ,057],6_1_6],3_4],27];}Class n5_:_5{Var r,$__,D,$6:_;Constructor (i,A,W_:P){Break ;} }'''
        expect = '''Program([ClassDecl(Id(_),[AttributeDecl(Instance,VarDecl(Id(_9K),ArrayType(27,ArrayType(34,ArrayType(616,ArrayType(47,IntType)))))),AttributeDecl(Static,VarDecl(Id($_),ArrayType(27,ArrayType(34,ArrayType(616,ArrayType(47,IntType)))))),AttributeDecl(Instance,VarDecl(Id(_),ArrayType(27,ArrayType(34,ArrayType(616,ArrayType(47,IntType)))))),AttributeDecl(Instance,VarDecl(Id(_),ArrayType(27,ArrayType(34,ArrayType(616,ArrayType(47,IntType))))))]),ClassDecl(Id(n5_),Id(_5),[AttributeDecl(Instance,VarDecl(Id(r),ClassType(Id(_)))),AttributeDecl(Static,VarDecl(Id($__),ClassType(Id(_)))),AttributeDecl(Instance,VarDecl(Id(D),ClassType(Id(_)))),AttributeDecl(Static,VarDecl(Id($6),ClassType(Id(_)))),MethodDecl(Id(Constructor),Instance,[param(Id(i),ClassType(Id(P))),param(Id(A),ClassType(Id(P))),param(Id(W_),ClassType(Id(P)))],Block([],[Break]))])])'''
        self.assertTrue(TestAST.test(line, expect, 625))

    def test_626(self):
        line = '''Class _R8:___{Destructor (){} }Class C{}Class __6_5{}Class _:u9o{}'''
        expect = '''Program([ClassDecl(Id(_R8),Id(___),[MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(C),[]),ClassDecl(Id(__6_5),[]),ClassDecl(Id(_),Id(u9o),[])])'''
        self.assertTrue(TestAST.test(line, expect, 626))

    def test_627(self):
        line = '''Class bOC:_0y9{_9Y(Y7,_,k,__:Array [Array [Boolean ,0b1_0],052];_L:String ;U,l___,u,_:Array [Array [Int ,052],0x3C]){} }'''
        expect = '''Program([ClassDecl(Id(bOC),Id(_0y9),[MethodDecl(Id(_9Y),Instance,[param(Id(Y7),ArrayType(42,ArrayType(2,BoolType))),param(Id(_),ArrayType(42,ArrayType(2,BoolType))),param(Id(k),ArrayType(42,ArrayType(2,BoolType))),param(Id(__),ArrayType(42,ArrayType(2,BoolType))),param(Id(_L),StringType),param(Id(U),ArrayType(60,ArrayType(42,IntType))),param(Id(l___),ArrayType(60,ArrayType(42,IntType))),param(Id(u),ArrayType(60,ArrayType(42,IntType))),param(Id(_),ArrayType(60,ArrayType(42,IntType)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 627))

    def test_628(self):
        line = '''Class N_9M{Destructor (){}Var $k,$_0:I;Constructor (){} }Class _{}'''
        expect = '''Program([ClassDecl(Id(N_9M),[MethodDecl(Id(Destructor),Instance,[],Block([],[])),AttributeDecl(Static,VarDecl(Id($k),ClassType(Id(I)))),AttributeDecl(Static,VarDecl(Id($_0),ClassType(Id(I)))),MethodDecl(Id(Constructor),Instance,[],Block([],[]))]),ClassDecl(Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 628))

    def test_629(self):
        line = '''Class z9y:t{Destructor (){} }Class __3Y:L{}Class _{}Class _{Var $1_291_:String ;}'''
        expect = '''Program([ClassDecl(Id(z9y),Id(t),[MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(__3Y),Id(L),[]),ClassDecl(Id(_),[]),ClassDecl(Id(_),[AttributeDecl(Static,VarDecl(Id($1_291_),StringType))])])'''
        self.assertTrue(TestAST.test(line, expect, 629))

    def test_630(self):
        line = '''Class _h:r{Var $L,$6_,$Z,d__O:Array [String ,020];Constructor (){}Constructor (){} }'''
        expect = '''Program([ClassDecl(Id(_h),Id(r),[AttributeDecl(Static,VarDecl(Id($L),ArrayType(16,StringType))),AttributeDecl(Static,VarDecl(Id($6_),ArrayType(16,StringType))),AttributeDecl(Static,VarDecl(Id($Z),ArrayType(16,StringType))),AttributeDecl(Instance,VarDecl(Id(d__O),ArrayType(16,StringType))),MethodDecl(Id(Constructor),Instance,[],Block([],[])),MethodDecl(Id(Constructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 630))

    def test_631(self):
        line = '''Class z2Wp__2{CC(_,a:Float ;_,_:String ;v_,i,__,o0_,p:z_;_2:_){Continue ;Return ;}Destructor (){}Var $_,_c,A:Array [Array [Array [Boolean ,0x9],0b1000111],3_68_8];}'''
        expect = '''Program([ClassDecl(Id(z2Wp__2),[MethodDecl(Id(CC),Instance,[param(Id(_),FloatType),param(Id(a),FloatType),param(Id(_),StringType),param(Id(_),StringType),param(Id(v_),ClassType(Id(z_))),param(Id(i),ClassType(Id(z_))),param(Id(__),ClassType(Id(z_))),param(Id(o0_),ClassType(Id(z_))),param(Id(p),ClassType(Id(z_))),param(Id(_2),ClassType(Id(_)))],Block([],[Continue,Return(None)])),MethodDecl(Id(Destructor),Instance,[],Block([],[])),AttributeDecl(Static,VarDecl(Id($_),ArrayType(3688,ArrayType(71,ArrayType(9,BoolType))))),AttributeDecl(Instance,VarDecl(Id(_c),ArrayType(3688,ArrayType(71,ArrayType(9,BoolType))))),AttributeDecl(Instance,VarDecl(Id(A),ArrayType(3688,ArrayType(71,ArrayType(9,BoolType)))))])])'''
        self.assertTrue(TestAST.test(line, expect, 631))

    def test_632(self):
        line = '''Class __{Destructor (){}Var _,$4,$28:Array [Float ,06_11];}'''
        expect = '''Program([ClassDecl(Id(__),[MethodDecl(Id(Destructor),Instance,[],Block([],[])),AttributeDecl(Instance,VarDecl(Id(_),ArrayType(393,FloatType))),AttributeDecl(Static,VarDecl(Id($4),ArrayType(393,FloatType))),AttributeDecl(Static,VarDecl(Id($28),ArrayType(393,FloatType)))])])'''
        self.assertTrue(TestAST.test(line, expect, 632))

    def test_633(self):
        line = '''Class _:_8{Var $V:Array [Array [Array [Array [Array [String ,0X5],0X8],0B111],0XA],6_25];}Class ZR:fR1__{}'''
        expect = '''Program([ClassDecl(Id(_),Id(_8),[AttributeDecl(Static,VarDecl(Id($V),ArrayType(625,ArrayType(10,ArrayType(7,ArrayType(8,ArrayType(5,StringType)))))))]),ClassDecl(Id(ZR),Id(fR1__),[])])'''
        self.assertTrue(TestAST.test(line, expect, 633))

    def test_634(self):
        line = '''Class _2{Destructor (){}Constructor (K,Z,D,_:Boolean ;y,D_2e:Array [Array [Array [Int ,0B1010011],011],01]){} }Class x{}Class z:_{}'''
        expect = '''Program([ClassDecl(Id(_2),[MethodDecl(Id(Destructor),Instance,[],Block([],[])),MethodDecl(Id(Constructor),Instance,[param(Id(K),BoolType),param(Id(Z),BoolType),param(Id(D),BoolType),param(Id(_),BoolType),param(Id(y),ArrayType(1,ArrayType(9,ArrayType(83,IntType)))),param(Id(D_2e),ArrayType(1,ArrayType(9,ArrayType(83,IntType))))],Block([],[]))]),ClassDecl(Id(x),[]),ClassDecl(Id(z),Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 634))

    def test_635(self):
        line = '''Class _:R{Destructor (){Var _,t,_:Int ;}Destructor (){} }'''
        expect = '''Program([ClassDecl(Id(_),Id(R),[MethodDecl(Id(Destructor),Instance,[],Block([VarDecl(Id(_),IntType),VarDecl(Id(t),IntType),VarDecl(Id(_),IntType)],[])),MethodDecl(Id(Destructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 635))

    def test_636(self):
        line = '''Class __2_:F{_(t,R6K,I,_:_9;_f:String ;a8,_904:Z__e;__5:H7_){}Var $7:a;}Class _:_68_{Var d:Boolean ;}Class x_{}Class _:X_{}'''
        expect = '''Program([ClassDecl(Id(__2_),Id(F),[MethodDecl(Id(_),Instance,[param(Id(t),ClassType(Id(_9))),param(Id(R6K),ClassType(Id(_9))),param(Id(I),ClassType(Id(_9))),param(Id(_),ClassType(Id(_9))),param(Id(_f),StringType),param(Id(a8),ClassType(Id(Z__e))),param(Id(_904),ClassType(Id(Z__e))),param(Id(__5),ClassType(Id(H7_)))],Block([],[])),AttributeDecl(Static,VarDecl(Id($7),ClassType(Id(a))))]),ClassDecl(Id(_),Id(_68_),[AttributeDecl(Instance,VarDecl(Id(d),BoolType))]),ClassDecl(Id(x_),[]),ClassDecl(Id(_),Id(X_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 636))

    def test_637(self):
        line = '''Class VB6_{_8_3(){}Constructor (md,_,__5,_,_,____0,h:Array [Array [Array [Array [Array [Float ,0b10],0x1C],0555],02],4_4]){Break ;} }Class _{}Class NO:z{}'''
        expect = '''Program([ClassDecl(Id(VB6_),[MethodDecl(Id(_8_3),Instance,[],Block([],[])),MethodDecl(Id(Constructor),Instance,[param(Id(md),ArrayType(44,ArrayType(2,ArrayType(365,ArrayType(28,ArrayType(2,FloatType)))))),param(Id(_),ArrayType(44,ArrayType(2,ArrayType(365,ArrayType(28,ArrayType(2,FloatType)))))),param(Id(__5),ArrayType(44,ArrayType(2,ArrayType(365,ArrayType(28,ArrayType(2,FloatType)))))),param(Id(_),ArrayType(44,ArrayType(2,ArrayType(365,ArrayType(28,ArrayType(2,FloatType)))))),param(Id(_),ArrayType(44,ArrayType(2,ArrayType(365,ArrayType(28,ArrayType(2,FloatType)))))),param(Id(____0),ArrayType(44,ArrayType(2,ArrayType(365,ArrayType(28,ArrayType(2,FloatType)))))),param(Id(h),ArrayType(44,ArrayType(2,ArrayType(365,ArrayType(28,ArrayType(2,FloatType))))))],Block([],[Break]))]),ClassDecl(Id(_),[]),ClassDecl(Id(NO),Id(z),[])])'''
        self.assertTrue(TestAST.test(line, expect, 637))

    def test_638(self):
        line = '''Class _5E1:S{Constructor (u:Array [Array [Array [Array [Array [Array [Array [Array [Array [Array [Array [Array [Float ,0XD_1],0B1],0b1],033],041],56],0XC],04],0b101010],0B1],0B11100],0X2C];_,___,_,_,_,_,M988_4_:Array [Boolean ,5_2_06_4];b,__k,V5:Float ){} }'''
        expect = '''Program([ClassDecl(Id(_5E1),Id(S),[MethodDecl(Id(Constructor),Instance,[param(Id(u),ArrayType(44,ArrayType(28,ArrayType(1,ArrayType(42,ArrayType(4,ArrayType(12,ArrayType(56,ArrayType(33,ArrayType(27,ArrayType(1,ArrayType(1,ArrayType(209,FloatType))))))))))))),param(Id(_),ArrayType(52064,BoolType)),param(Id(___),ArrayType(52064,BoolType)),param(Id(_),ArrayType(52064,BoolType)),param(Id(_),ArrayType(52064,BoolType)),param(Id(_),ArrayType(52064,BoolType)),param(Id(_),ArrayType(52064,BoolType)),param(Id(M988_4_),ArrayType(52064,BoolType)),param(Id(b),FloatType),param(Id(__k),FloatType),param(Id(V5),FloatType)],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 638))

    def test_639(self):
        line = '''Class l_:_{Var $Gd,_7_:Array [Boolean ,051];}Class w_{}Class _7{}'''
        expect = '''Program([ClassDecl(Id(l_),Id(_),[AttributeDecl(Static,VarDecl(Id($Gd),ArrayType(41,BoolType))),AttributeDecl(Instance,VarDecl(Id(_7_),ArrayType(41,BoolType)))]),ClassDecl(Id(w_),[]),ClassDecl(Id(_7),[])])'''
        self.assertTrue(TestAST.test(line, expect, 639))

    def test_640(self):
        line = '''Class d:_g_{_w(i,Y7t:Array [Array [String ,0B10001],69];e71:Array [Array [Boolean ,0103],8];D:Array [String ,0B10001];_H3___:String ;_,_497:Array [Array [Array [Boolean ,0b1_1],0X52],01_6];__5s:_g){} }'''
        expect = '''Program([ClassDecl(Id(d),Id(_g_),[MethodDecl(Id(_w),Instance,[param(Id(i),ArrayType(69,ArrayType(17,StringType))),param(Id(Y7t),ArrayType(69,ArrayType(17,StringType))),param(Id(e71),ArrayType(8,ArrayType(67,BoolType))),param(Id(D),ArrayType(17,StringType)),param(Id(_H3___),StringType),param(Id(_),ArrayType(14,ArrayType(82,ArrayType(3,BoolType)))),param(Id(_497),ArrayType(14,ArrayType(82,ArrayType(3,BoolType)))),param(Id(__5s),ClassType(Id(_g)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 640))

    def test_641(self):
        line = '''Class _:A__{}Class _:__L_3{}Class _{Var _:Array [Array [Boolean ,045],0B100];}'''
        expect = '''Program([ClassDecl(Id(_),Id(A__),[]),ClassDecl(Id(_),Id(__L_3),[]),ClassDecl(Id(_),[AttributeDecl(Instance,VarDecl(Id(_),ArrayType(4,ArrayType(37,BoolType))))])])'''
        self.assertTrue(TestAST.test(line, expect, 641))

    def test_642(self):
        line = '''Class v_4:_{Var O:Array [Array [Int ,0b1000011],0x1B];}Class MT:__{Constructor (D:Array [String ,0b1000011]){} }Class O9_:P{Var $6,$F2:Array [Array [Array [Boolean ,0b1000011],03],0X47];}'''
        expect = '''Program([ClassDecl(Id(v_4),Id(_),[AttributeDecl(Instance,VarDecl(Id(O),ArrayType(27,ArrayType(67,IntType))))]),ClassDecl(Id(MT),Id(__),[MethodDecl(Id(Constructor),Instance,[param(Id(D),ArrayType(67,StringType))],Block([],[]))]),ClassDecl(Id(O9_),Id(P),[AttributeDecl(Static,VarDecl(Id($6),ArrayType(71,ArrayType(3,ArrayType(67,BoolType))))),AttributeDecl(Static,VarDecl(Id($F2),ArrayType(71,ArrayType(3,ArrayType(67,BoolType)))))])])'''
        self.assertTrue(TestAST.test(line, expect, 642))

    def test_643(self):
        line = '''Class d:e{}Class _r:_3{Constructor (){} }Class F__{}Class YCaLk{Destructor (){Continue ;}Destructor (){} }Class _:_a_{}'''
        expect = '''Program([ClassDecl(Id(d),Id(e),[]),ClassDecl(Id(_r),Id(_3),[MethodDecl(Id(Constructor),Instance,[],Block([],[]))]),ClassDecl(Id(F__),[]),ClassDecl(Id(YCaLk),[MethodDecl(Id(Destructor),Instance,[],Block([],[Continue])),MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(_),Id(_a_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 643))

    def test_644(self):
        line = '''Class i_4F_{}Class __:t_{Constructor (){___H6::$hwg();} }'''
        expect = '''Program([ClassDecl(Id(i_4F_),[]),ClassDecl(Id(__),Id(t_),[MethodDecl(Id(Constructor),Instance,[],Block([],[Call(Id(___H6),Id($hwg),[])]))])])'''
        self.assertTrue(TestAST.test(line, expect, 644))

    def test_645(self):
        line = '''Class E{Var $q9:Array [Array [Boolean ,075],0b1011101];}Class _L3:M{Destructor (){Break ;Break ;} }'''
        expect = '''Program([ClassDecl(Id(E),[AttributeDecl(Static,VarDecl(Id($q9),ArrayType(93,ArrayType(61,BoolType))))]),ClassDecl(Id(_L3),Id(M),[MethodDecl(Id(Destructor),Instance,[],Block([],[Break,Break]))])])'''
        self.assertTrue(TestAST.test(line, expect, 645))

    def test_646(self):
        line = '''Class _V_7{Var _86:Int =!-New k___()._.j_Z._._s3();Destructor (){} }Class _{Var $_5_,z_:Array [Array [String ,2],80];}'''
        expect = '''Program([ClassDecl(Id(_V_7),[AttributeDecl(Static,VarDecl(Id($25),IntType,UnaryOp(!,UnaryOp(-,CallExpr(FieldAccess(FieldAccess(FieldAccess(NewExpr(Id(k___),[]),Id(_)),Id(j_Z)),Id(_)),Id(_s3),[]))))),MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(_),[AttributeDecl(Static,VarDecl(Id($_5_),ArrayType(80,ArrayType(2,StringType)))),AttributeDecl(Instance,VarDecl(Id(z_),ArrayType(80,ArrayType(2,StringType))))])])'''
        self.assertTrue(TestAST.test(line, expect, 646))

    def test_647(self):
        line = '''Class p_:G8{}Class _g_:_0_{Destructor (){Continue ;} }Class Fu{}'''
        expect = '''Program([ClassDecl(Id(p_),Id(G8),[]),ClassDecl(Id(_g_),Id(_0_),[MethodDecl(Id(Destructor),Instance,[],Block([],[Continue]))]),ClassDecl(Id(Fu),[])])'''
        self.assertTrue(TestAST.test(line, expect, 647))

    def test_648(self):
        line = '''Class i__C:_Nl{}Class _4r9:g{}Class y_:_oID_7l_{Destructor (){} }'''
        expect = '''Program([ClassDecl(Id(i__C),Id(_Nl),[]),ClassDecl(Id(_4r9),Id(g),[]),ClassDecl(Id(y_),Id(_oID_7l_),[MethodDecl(Id(Destructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 648))

    def test_649(self):
        line = '''Class T:_{Destructor (){ {} }Destructor (){}_(_5,_6:Array [Array [Boolean ,0X23],0xB_6_3];mUy:Array [Array [String ,075],0X23]){Break ;}Var _:Array [Array [Boolean ,0X23],0x30];}Class X05C:N_{}'''
        expect = '''Program([ClassDecl(Id(T),Id(_),[MethodDecl(Id(Destructor),Instance,[],Block([],[Block([],[])])),MethodDecl(Id(Destructor),Instance,[],Block([],[])),MethodDecl(Id(_),Instance,[param(Id(_5),ArrayType(2915,ArrayType(35,BoolType))),param(Id(_6),ArrayType(2915,ArrayType(35,BoolType))),param(Id(mUy),ArrayType(35,ArrayType(61,StringType)))],Block([],[Break])),AttributeDecl(Instance,VarDecl(Id(_),ArrayType(48,ArrayType(35,BoolType))))]),ClassDecl(Id(X05C),Id(N_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 649))

    def test_650(self):
        line = '''Class s{Var _0,x_w7,_2,h__,_,_p,$836_:Int ;Destructor (){} }Class T:_{}'''
        expect = '''Program([ClassDecl(Id(s),[AttributeDecl(Instance,VarDecl(Id(_0),IntType)),AttributeDecl(Instance,VarDecl(Id(x_w7),IntType)),AttributeDecl(Instance,VarDecl(Id(_2),IntType)),AttributeDecl(Instance,VarDecl(Id(h__),IntType)),AttributeDecl(Instance,VarDecl(Id(_),IntType)),AttributeDecl(Instance,VarDecl(Id(_p),IntType)),AttributeDecl(Static,VarDecl(Id($836_),IntType)),MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(T),Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 650))

    def test_651(self):
        line = '''Class k{$9_(_570:String ){}Var $h,B0_,_3_,$_G_F0T_,$_,_e2Y:Boolean ;}Class _:__{}'''
        expect = '''Program([ClassDecl(Id(k),[MethodDecl(Id($9_),Static,[param(Id(_570),StringType)],Block([],[])),AttributeDecl(Static,VarDecl(Id($h),BoolType)),AttributeDecl(Instance,VarDecl(Id(B0_),BoolType)),AttributeDecl(Instance,VarDecl(Id(_3_),BoolType)),AttributeDecl(Static,VarDecl(Id($_G_F0T_),BoolType)),AttributeDecl(Static,VarDecl(Id($_),BoolType)),AttributeDecl(Instance,VarDecl(Id(_e2Y),BoolType))]),ClassDecl(Id(_),Id(__),[])])'''
        self.assertTrue(TestAST.test(line, expect, 651))

    def test_652(self):
        line = '''Class _{Constructor (){}Var $Tt,x,_,$J,c,d7:Array [Array [Int ,0x76],0B1010101];}'''
        expect = '''Program([ClassDecl(Id(_),[MethodDecl(Id(Constructor),Instance,[],Block([],[])),AttributeDecl(Static,VarDecl(Id($Tt),ArrayType(85,ArrayType(118,IntType)))),AttributeDecl(Instance,VarDecl(Id(x),ArrayType(85,ArrayType(118,IntType)))),AttributeDecl(Instance,VarDecl(Id(_),ArrayType(85,ArrayType(118,IntType)))),AttributeDecl(Static,VarDecl(Id($J),ArrayType(85,ArrayType(118,IntType)))),AttributeDecl(Instance,VarDecl(Id(c),ArrayType(85,ArrayType(118,IntType)))),AttributeDecl(Instance,VarDecl(Id(d7),ArrayType(85,ArrayType(118,IntType))))])])'''
        self.assertTrue(TestAST.test(line, expect, 652))

    def test_653(self):
        line = '''Class __d{u(){}Constructor (b,Q,e:Array [Array [Int ,0X50],021];r_206:__;_,u8:V){} }Class _{}'''
        expect = '''Program([ClassDecl(Id(__d),[MethodDecl(Id(u),Instance,[],Block([],[])),MethodDecl(Id(Constructor),Instance,[param(Id(b),ArrayType(17,ArrayType(80,IntType))),param(Id(Q),ArrayType(17,ArrayType(80,IntType))),param(Id(e),ArrayType(17,ArrayType(80,IntType))),param(Id(r_206),ClassType(Id(__))),param(Id(_),ClassType(Id(V))),param(Id(u8),ClassType(Id(V)))],Block([],[]))]),ClassDecl(Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 653))

    def test_654(self):
        line = '''Class _6:_m{}Class r_{}Class _8{Constructor (){ {} }Destructor (){} }'''
        expect = '''Program([ClassDecl(Id(_6),Id(_m),[]),ClassDecl(Id(r_),[]),ClassDecl(Id(_8),[MethodDecl(Id(Constructor),Instance,[],Block([],[Block([],[])])),MethodDecl(Id(Destructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 654))

    def test_655(self):
        line = '''Class _2_{}Class _{$10_0(_:Array [String ,0b1];_:m;U:String ;_,_,y_y3:z;_,__:String ){ {} }}Class Hn6:_{}'''
        expect = '''Program([ClassDecl(Id(_2_),[]),ClassDecl(Id(_),[MethodDecl(Id($10_0),Static,[param(Id(_),ArrayType(1,StringType)),param(Id(_),ClassType(Id(m))),param(Id(U),StringType),param(Id(_),ClassType(Id(z))),param(Id(_),ClassType(Id(z))),param(Id(y_y3),ClassType(Id(z))),param(Id(_),StringType),param(Id(__),StringType)],Block([],[Block([],[])]))]),ClassDecl(Id(Hn6),Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 655))

    def test_656(self):
        line = '''Class j_:i{}Class B:_{}Class G__2{Var l_:Boolean ;}Class K:_70{}'''
        expect = '''Program([ClassDecl(Id(j_),Id(i),[]),ClassDecl(Id(B),Id(_),[]),ClassDecl(Id(G__2),[AttributeDecl(Instance,VarDecl(Id(l_),BoolType))]),ClassDecl(Id(K),Id(_70),[])])'''
        self.assertTrue(TestAST.test(line, expect, 656))

    def test_657(self):
        line = '''Class j:Y8{}Class __{Destructor (){}Destructor (){}Constructor (_:t151){Break ;} }Class _{Destructor (){Return ;} }'''
        expect = '''Program([ClassDecl(Id(j),Id(Y8),[]),ClassDecl(Id(__),[MethodDecl(Id(Destructor),Instance,[],Block([],[])),MethodDecl(Id(Destructor),Instance,[],Block([],[])),MethodDecl(Id(Constructor),Instance,[param(Id(_),ClassType(Id(t151)))],Block([],[Break]))]),ClassDecl(Id(_),[MethodDecl(Id(Destructor),Instance,[],Block([],[Return(None)]))])])'''
        self.assertTrue(TestAST.test(line, expect, 657))

    def test_658(self):
        line = '''Class __{$p(){Break ;} }Class _:P6{__(__5_:Int ;tu:W){}Var KO,N:String ;}'''
        expect = '''Program([ClassDecl(Id(__),[MethodDecl(Id($p),Static,[],Block([],[Break]))]),ClassDecl(Id(_),Id(P6),[MethodDecl(Id(__),Instance,[param(Id(__5_),IntType),param(Id(tu),ClassType(Id(W)))],Block([],[])),AttributeDecl(Instance,VarDecl(Id(KO),StringType)),AttributeDecl(Instance,VarDecl(Id(N),StringType))])])'''
        self.assertTrue(TestAST.test(line, expect, 658))

    def test_659(self):
        line = '''Class _D7:B{Var $_5,_,_K9_:Array [Array [String ,0X4],0b1];}'''
        expect = '''Program([ClassDecl(Id(_D7),Id(B),[AttributeDecl(Static,VarDecl(Id($_5),ArrayType(1,ArrayType(4,StringType)))),AttributeDecl(Instance,VarDecl(Id(_),ArrayType(1,ArrayType(4,StringType)))),AttributeDecl(Instance,VarDecl(Id(_K9_),ArrayType(1,ArrayType(4,StringType))))])])'''
        self.assertTrue(TestAST.test(line, expect, 659))

    def test_660(self):
        line = '''Class ___O6P_{Var _7,u:Array [Array [Array [Int ,0B1],074_0],0x2_B2_3];}'''
        expect = '''Program([ClassDecl(Id(___O6P_),[AttributeDecl(Instance,VarDecl(Id(_7),ArrayType(11043,ArrayType(480,ArrayType(1,IntType))))),AttributeDecl(Instance,VarDecl(Id(u),ArrayType(11043,ArrayType(480,ArrayType(1,IntType)))))])])'''
        self.assertTrue(TestAST.test(line, expect, 660))

    def test_661(self):
        line = '''Class _:rM{Constructor (Z_77c,_,q,_Y5,_V9_:Array [Array [Array [Boolean ,0x52],0b1000001],055];y:R){} }'''
        expect = '''Program([ClassDecl(Id(_),Id(rM),[MethodDecl(Id(Constructor),Instance,[param(Id(Z_77c),ArrayType(45,ArrayType(65,ArrayType(82,BoolType)))),param(Id(_),ArrayType(45,ArrayType(65,ArrayType(82,BoolType)))),param(Id(q),ArrayType(45,ArrayType(65,ArrayType(82,BoolType)))),param(Id(_Y5),ArrayType(45,ArrayType(65,ArrayType(82,BoolType)))),param(Id(_V9_),ArrayType(45,ArrayType(65,ArrayType(82,BoolType)))),param(Id(y),ClassType(Id(R)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 661))

    def test_662(self):
        line = '''Class f{}Class _:_z{_(){Break ;}I4(_:Array [Boolean ,18]){} }'''
        expect = '''Program([ClassDecl(Id(f),[]),ClassDecl(Id(_),Id(_z),[MethodDecl(Id(_),Instance,[],Block([],[Break])),MethodDecl(Id(I4),Instance,[param(Id(_),ArrayType(18,BoolType))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 662))

    def test_663(self):
        line = '''Class _1:_y{Var $7T_:Array [Float ,0XB];Var $_8:Array [Int ,0107];Destructor (){}$_(){}Var $X4_,_,$__4_7:Array [Boolean ,0b1_10];$0_(){Continue ;Break ;{} }}Class _65{}'''
        expect = '''Program([ClassDecl(Id(_1),Id(_y),[AttributeDecl(Static,VarDecl(Id($7T_),ArrayType(11,FloatType))),AttributeDecl(Static,VarDecl(Id($_8),ArrayType(71,IntType))),MethodDecl(Id(Destructor),Instance,[],Block([],[])),MethodDecl(Id($_),Static,[],Block([],[])),AttributeDecl(Static,VarDecl(Id($X4_),ArrayType(6,BoolType))),AttributeDecl(Instance,VarDecl(Id(_),ArrayType(6,BoolType))),AttributeDecl(Static,VarDecl(Id($__4_7),ArrayType(6,BoolType))),MethodDecl(Id($0_),Static,[],Block([],[Continue,Break,Block([],[])]))]),ClassDecl(Id(_65),[])])'''
        self.assertTrue(TestAST.test(line, expect, 663))

    def test_664(self):
        line = '''Class _{$_u(_:Array [Array [Array [Float ,0x42],0B110],0b1];_M3,_:_){Break ;} }'''
        expect = '''Program([ClassDecl(Id(_),[MethodDecl(Id($_u),Static,[param(Id(_),ArrayType(1,ArrayType(6,ArrayType(66,FloatType)))),param(Id(_M3),ClassType(Id(_))),param(Id(_),ClassType(Id(_)))],Block([],[Break]))])])'''
        self.assertTrue(TestAST.test(line, expect, 664))

    def test_665(self):
        line = '''Class _{$_(W:Array [Float ,0xA];__:Boolean ;_:String ){} }'''
        expect = '''Program([ClassDecl(Id(_),[MethodDecl(Id($_),Static,[param(Id(W),ArrayType(10,FloatType)),param(Id(__),BoolType),param(Id(_),StringType)],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 665))

    def test_666(self):
        line = '''Class _{}Class I0w{Destructor (){} }Class D9{}Class _u:_79{}'''
        expect = '''Program([ClassDecl(Id(_),[]),ClassDecl(Id(I0w),[MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(D9),[]),ClassDecl(Id(_u),Id(_79),[])])'''
        self.assertTrue(TestAST.test(line, expect, 666))

    def test_667(self):
        line = '''Class E{}Class h{}Class _P9:n{Constructor (){}Constructor (I2H_,V4,s:Array [Boolean ,04_5]){} }'''
        expect = '''Program([ClassDecl(Id(E),[]),ClassDecl(Id(h),[]),ClassDecl(Id(_P9),Id(n),[MethodDecl(Id(Constructor),Instance,[],Block([],[])),MethodDecl(Id(Constructor),Instance,[param(Id(I2H_),ArrayType(37,BoolType)),param(Id(V4),ArrayType(37,BoolType)),param(Id(s),ArrayType(37,BoolType))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 667))

    def test_668(self):
        line = '''Class x:__A_S0Z{}Class j9:y{Constructor (zV:w6X;_,_4U:x){} }Class _:z_lX{}'''
        expect = '''Program([ClassDecl(Id(x),Id(__A_S0Z),[]),ClassDecl(Id(j9),Id(y),[MethodDecl(Id(Constructor),Instance,[param(Id(zV),ClassType(Id(w6X))),param(Id(_),ClassType(Id(x))),param(Id(_4U),ClassType(Id(x)))],Block([],[]))]),ClassDecl(Id(_),Id(z_lX),[])])'''
        self.assertTrue(TestAST.test(line, expect, 668))

    def test_669(self):
        line = '''Class _:C_q{}Class _L_:t{YN(_,__,_09,_e_:Array [Boolean ,77];gAf,_,S,__:_B;_:Array [Boolean ,035]){}$_(d2,E:_){} }'''
        expect = '''Program([ClassDecl(Id(_),Id(C_q),[]),ClassDecl(Id(_L_),Id(t),[MethodDecl(Id(YN),Instance,[param(Id(_),ArrayType(77,BoolType)),param(Id(__),ArrayType(77,BoolType)),param(Id(_09),ArrayType(77,BoolType)),param(Id(_e_),ArrayType(77,BoolType)),param(Id(gAf),ClassType(Id(_B))),param(Id(_),ClassType(Id(_B))),param(Id(S),ClassType(Id(_B))),param(Id(__),ClassType(Id(_B))),param(Id(_),ArrayType(29,BoolType))],Block([],[])),MethodDecl(Id($_),Static,[param(Id(d2),ClassType(Id(_))),param(Id(E),ClassType(Id(_)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 669))

    def test_670(self):
        line = '''Class _Dp{Constructor (R,n9__,_:_;RN9_7_9,o:Array [Array [Boolean ,1],91]){} }Class n_{Var __:Array [Float ,0X51];}Class _g{}'''
        expect = '''Program([ClassDecl(Id(_Dp),[MethodDecl(Id(Constructor),Instance,[param(Id(R),ClassType(Id(_))),param(Id(n9__),ClassType(Id(_))),param(Id(_),ClassType(Id(_))),param(Id(RN9_7_9),ArrayType(91,ArrayType(1,BoolType))),param(Id(o),ArrayType(91,ArrayType(1,BoolType)))],Block([],[]))]),ClassDecl(Id(n_),[AttributeDecl(Instance,VarDecl(Id(__),ArrayType(81,FloatType)))]),ClassDecl(Id(_g),[])])'''
        self.assertTrue(TestAST.test(line, expect, 670))

    def test_671(self):
        line = '''Class _p:b_{Constructor (_:Array [String ,02_6];_:String ){} }'''
        expect = '''Program([ClassDecl(Id(_p),Id(b_),[MethodDecl(Id(Constructor),Instance,[param(Id(_),ArrayType(22,StringType)),param(Id(_),StringType)],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 671))

    def test_672(self):
        line = '''Class _:_{Destructor (){} }Class _:_L{Destructor (){} }Class q8{}Class _{}'''
        expect = '''Program([ClassDecl(Id(_),Id(_),[MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(_),Id(_L),[MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(q8),[]),ClassDecl(Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 672))

    def test_673(self):
        line = '''Class kH{}Class z:o__{}Class _y{}Class _{}Class b{Constructor (){} }'''
        expect = '''Program([ClassDecl(Id(kH),[]),ClassDecl(Id(z),Id(o__),[]),ClassDecl(Id(_y),[]),ClassDecl(Id(_),[]),ClassDecl(Id(b),[MethodDecl(Id(Constructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 673))

    def test_674(self):
        line = '''Class ml30:Vf21{Constructor (P_,__,_D,U:Int ){Var s:J;} }'''
        expect = '''Program([ClassDecl(Id(ml30),Id(Vf21),[MethodDecl(Id(Constructor),Instance,[param(Id(P_),IntType),param(Id(__),IntType),param(Id(_D),IntType),param(Id(U),IntType)],Block([VarDecl(Id(s),ClassType(Id(J)))],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 674))

    def test_675(self):
        line = '''Class _{}Class __:K1{}Class P{}Class _6{Var lC,_9:Array [Array [Int ,0101],28];}Class C_:_{Constructor (_,y3,_A_,Y__:Boolean ){}Var R_,_H,_,I_,$X_9_:R4;}Class _2:J_45dL{}'''
        expect = '''Program([ClassDecl(Id(_),[]),ClassDecl(Id(__),Id(K1),[]),ClassDecl(Id(P),[]),ClassDecl(Id(_6),[AttributeDecl(Instance,VarDecl(Id(lC),ArrayType(28,ArrayType(65,IntType)))),AttributeDecl(Instance,VarDecl(Id(_9),ArrayType(28,ArrayType(65,IntType))))]),ClassDecl(Id(C_),Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(_),BoolType),param(Id(y3),BoolType),param(Id(_A_),BoolType),param(Id(Y__),BoolType)],Block([],[])),AttributeDecl(Instance,VarDecl(Id(R_),ClassType(Id(R4)))),AttributeDecl(Instance,VarDecl(Id(_H),ClassType(Id(R4)))),AttributeDecl(Instance,VarDecl(Id(_),ClassType(Id(R4)))),AttributeDecl(Instance,VarDecl(Id(I_),ClassType(Id(R4)))),AttributeDecl(Static,VarDecl(Id($X_9_),ClassType(Id(R4))))]),ClassDecl(Id(_2),Id(J_45dL),[])])'''
        self.assertTrue(TestAST.test(line, expect, 675))

    def test_676(self):
        line = '''Class e4:___4{Constructor (){ {Break ;} }Constructor (){} }'''
        expect = '''Program([ClassDecl(Id(e4),Id(___4),[MethodDecl(Id(Constructor),Instance,[],Block([],[Block([],[Break])])),MethodDecl(Id(Constructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 676))

    def test_677(self):
        line = '''Class _{}Class x2_:H{$_t(__,_:Array [Array [Array [Float ,066],0B10],5];_6:Int ){}Constructor (){Break ;{} }}'''
        expect = '''Program([ClassDecl(Id(_),[]),ClassDecl(Id(x2_),Id(H),[MethodDecl(Id($_t),Static,[param(Id(__),ArrayType(5,ArrayType(2,ArrayType(54,FloatType)))),param(Id(_),ArrayType(5,ArrayType(2,ArrayType(54,FloatType)))),param(Id(_6),IntType)],Block([],[])),MethodDecl(Id(Constructor),Instance,[],Block([],[Break,Block([],[])]))])])'''
        self.assertTrue(TestAST.test(line, expect, 677))

    def test_678(self):
        line = '''Class y{}Class __{Constructor (__:Array [Int ,01];b4,t,j0,f:Float ;_,_:_;_:Array [Boolean ,0X58]){} }'''
        expect = '''Program([ClassDecl(Id(y),[]),ClassDecl(Id(__),[MethodDecl(Id(Constructor),Instance,[param(Id(__),ArrayType(1,IntType)),param(Id(b4),FloatType),param(Id(t),FloatType),param(Id(j0),FloatType),param(Id(f),FloatType),param(Id(_),ClassType(Id(_))),param(Id(_),ClassType(Id(_))),param(Id(_),ArrayType(88,BoolType))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 678))

    def test_679(self):
        line = '''Class Jjv{Constructor (p1:Array [Array [Array [Array [Boolean ,0b1_1_001_0],0X1_8],92],92]){Continue ;} }'''
        expect = '''Program([ClassDecl(Id(Jjv),[MethodDecl(Id(Constructor),Instance,[param(Id(p1),ArrayType(92,ArrayType(92,ArrayType(24,ArrayType(50,BoolType)))))],Block([],[Continue]))])])'''
        self.assertTrue(TestAST.test(line, expect, 679))

    def test_680(self):
        line = '''Class _m1:_3P{Var $2,i__,$nJ,_29,_6,$6,$h,$S:Array [Array [Boolean ,0B110010],0130];}'''
        expect = '''Program([ClassDecl(Id(_m1),Id(_3P),[AttributeDecl(Static,VarDecl(Id($2),ArrayType(88,ArrayType(50,BoolType)))),AttributeDecl(Instance,VarDecl(Id(i__),ArrayType(88,ArrayType(50,BoolType)))),AttributeDecl(Static,VarDecl(Id($nJ),ArrayType(88,ArrayType(50,BoolType)))),AttributeDecl(Instance,VarDecl(Id(_29),ArrayType(88,ArrayType(50,BoolType)))),AttributeDecl(Instance,VarDecl(Id(_6),ArrayType(88,ArrayType(50,BoolType)))),AttributeDecl(Static,VarDecl(Id($6),ArrayType(88,ArrayType(50,BoolType)))),AttributeDecl(Static,VarDecl(Id($h),ArrayType(88,ArrayType(50,BoolType)))),AttributeDecl(Static,VarDecl(Id($S),ArrayType(88,ArrayType(50,BoolType))))])])'''
        self.assertTrue(TestAST.test(line, expect, 680))

    def test_681(self):
        line = '''Class _:t{Destructor (){Var _7__rH,_,_:Array [Boolean ,73];} }Class _37{}'''
        expect = '''Program([ClassDecl(Id(_),Id(t),[MethodDecl(Id(Destructor),Instance,[],Block([VarDecl(Id(_7__rH),ArrayType(73,BoolType)),VarDecl(Id(_),ArrayType(73,BoolType)),VarDecl(Id(_),ArrayType(73,BoolType))],[]))]),ClassDecl(Id(_37),[])])'''
        self.assertTrue(TestAST.test(line, expect, 681))

    def test_682(self):
        line = '''Class g{Var _8_,b,$_:Float ;Destructor (){Break ;}Var $_:Array [String ,0b10];}'''
        expect = '''Program([ClassDecl(Id(g),[AttributeDecl(Instance,VarDecl(Id(_8_),FloatType)),AttributeDecl(Instance,VarDecl(Id(b),FloatType)),AttributeDecl(Static,VarDecl(Id($_),FloatType)),MethodDecl(Id(Destructor),Instance,[],Block([],[Break])),AttributeDecl(Static,VarDecl(Id($_),ArrayType(2,StringType)))])])'''
        self.assertTrue(TestAST.test(line, expect, 682))

    def test_683(self):
        line = '''Class D{Var _9f1,_:l_;}Class m_:r_{Val $_:Int =---"\t";Var _17_:Int ;}'''
        expect = '''Program([ClassDecl(Id(D),[AttributeDecl(Instance,VarDecl(Id(_9f1),ClassType(Id(l_)))),AttributeDecl(Instance,VarDecl(Id(_),ClassType(Id(l_))))]),ClassDecl(Id(m_),Id(r_),[AttributeDecl(Static,ConstDecl(Id($3O),IntType,UnaryOp(-,UnaryOp(-,UnaryOp(-,StringLit(\t)))))),AttributeDecl(Instance,VarDecl(Id(_17_),IntType))])])'''
        self.assertTrue(TestAST.test(line, expect, 683))

    def test_684(self):
        line = '''Class yLA_:_{}Class Z:_{Constructor (){} }Class _{}Class v{}Class _4d8:_{Destructor (){Continue ;} }'''
        expect = '''Program([ClassDecl(Id(yLA_),Id(_),[]),ClassDecl(Id(Z),Id(_),[MethodDecl(Id(Constructor),Instance,[],Block([],[]))]),ClassDecl(Id(_),[]),ClassDecl(Id(v),[]),ClassDecl(Id(_4d8),Id(_),[MethodDecl(Id(Destructor),Instance,[],Block([],[Continue]))])])'''
        self.assertTrue(TestAST.test(line, expect, 684))

    def test_685(self):
        line = '''Class r:_3_{Constructor (_:Float ;_J:M_;_Bz:Int ){}Destructor (){} }Class s{}'''
        expect = '''Program([ClassDecl(Id(r),Id(_3_),[MethodDecl(Id(Constructor),Instance,[param(Id(_),FloatType),param(Id(_J),ClassType(Id(M_))),param(Id(_Bz),IntType)],Block([],[])),MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(s),[])])'''
        self.assertTrue(TestAST.test(line, expect, 685))

    def test_686(self):
        line = '''Class ew{Var $N_:Array [Array [Array [Boolean ,0B1010000],2],065];$G0(){ {} }Destructor (){} }'''
        expect = '''Program([ClassDecl(Id(ew),[AttributeDecl(Static,VarDecl(Id($N_),ArrayType(53,ArrayType(2,ArrayType(80,BoolType))))),MethodDecl(Id($G0),Static,[],Block([],[Block([],[])])),MethodDecl(Id(Destructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 686))

    def test_687(self):
        line = '''Class y8O_o{D9(w_:Array [String ,0XE];_:Array [Array [String ,0x41],0x41];_:Float ){} }Class ___Y:_{}'''
        expect = '''Program([ClassDecl(Id(y8O_o),[MethodDecl(Id(D9),Instance,[param(Id(w_),ArrayType(14,StringType)),param(Id(_),ArrayType(65,ArrayType(65,StringType))),param(Id(_),FloatType)],Block([],[]))]),ClassDecl(Id(___Y),Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 687))

    def test_688(self):
        line = '''Class _:_{Constructor (){Continue ;}$O_(__B_,C___,_:H){}Constructor (){}_7_2(_t:Array [Array [Array [Float ,3],0b101010],0x15]){} }'''
        expect = '''Program([ClassDecl(Id(_),Id(_),[MethodDecl(Id(Constructor),Instance,[],Block([],[Continue])),MethodDecl(Id($O_),Static,[param(Id(__B_),ClassType(Id(H))),param(Id(C___),ClassType(Id(H))),param(Id(_),ClassType(Id(H)))],Block([],[])),MethodDecl(Id(Constructor),Instance,[],Block([],[])),MethodDecl(Id(_7_2),Instance,[param(Id(_t),ArrayType(21,ArrayType(42,ArrayType(3,FloatType))))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 688))

    def test_689(self):
        line = '''Class _:__{Var I,_7_:Array [Array [Float ,91],0B1001111];}Class G{}Class __{}'''
        expect = '''Program([ClassDecl(Id(_),Id(__),[AttributeDecl(Instance,VarDecl(Id(I),ArrayType(79,ArrayType(91,FloatType)))),AttributeDecl(Instance,VarDecl(Id(_7_),ArrayType(79,ArrayType(91,FloatType))))]),ClassDecl(Id(G),[]),ClassDecl(Id(__),[])])'''
        self.assertTrue(TestAST.test(line, expect, 689))

    def test_690(self):
        line = '''Class hY1W5:I{Constructor (){} }Class W__:_{}Class _06{}Class S{_(_,ceu_F_,_67,_:Boolean ){} }Class ____{}Class __o{}'''
        expect = '''Program([ClassDecl(Id(hY1W5),Id(I),[MethodDecl(Id(Constructor),Instance,[],Block([],[]))]),ClassDecl(Id(W__),Id(_),[]),ClassDecl(Id(_06),[]),ClassDecl(Id(S),[MethodDecl(Id(_),Instance,[param(Id(_),BoolType),param(Id(ceu_F_),BoolType),param(Id(_67),BoolType),param(Id(_),BoolType)],Block([],[]))]),ClassDecl(Id(____),[]),ClassDecl(Id(__o),[])])'''
        self.assertTrue(TestAST.test(line, expect, 690))

    def test_691(self):
        line = '''Class _:t{Destructor (){ {} }Var $N,$7:Boolean ;}Class sDa_{Constructor (_R,zL3_:String ;_,aLp:Array [Float ,6];y1:Int ;_oaq:Array [Array [Array [Array [Float ,0b1001101],1],035],79];w:_m_){} }'''
        expect = '''Program([ClassDecl(Id(_),Id(t),[MethodDecl(Id(Destructor),Instance,[],Block([],[Block([],[])])),AttributeDecl(Static,VarDecl(Id($N),BoolType)),AttributeDecl(Static,VarDecl(Id($7),BoolType))]),ClassDecl(Id(sDa_),[MethodDecl(Id(Constructor),Instance,[param(Id(_R),StringType),param(Id(zL3_),StringType),param(Id(_),ArrayType(6,FloatType)),param(Id(aLp),ArrayType(6,FloatType)),param(Id(y1),IntType),param(Id(_oaq),ArrayType(79,ArrayType(29,ArrayType(1,ArrayType(77,FloatType))))),param(Id(w),ClassType(Id(_m_)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 691))

    def test_692(self):
        line = '''Class _0j{}Class x:B{Var M,$s,$_,mig47,L91Sz_Lt_:Array [Boolean ,0b1];Var $2_d,x:Array [Float ,0x8_5];}'''
        expect = '''Program([ClassDecl(Id(_0j),[]),ClassDecl(Id(x),Id(B),[AttributeDecl(Instance,VarDecl(Id(M),ArrayType(1,BoolType))),AttributeDecl(Static,VarDecl(Id($s),ArrayType(1,BoolType))),AttributeDecl(Static,VarDecl(Id($_),ArrayType(1,BoolType))),AttributeDecl(Instance,VarDecl(Id(mig47),ArrayType(1,BoolType))),AttributeDecl(Instance,VarDecl(Id(L91Sz_Lt_),ArrayType(1,BoolType))),AttributeDecl(Static,VarDecl(Id($2_d),ArrayType(133,FloatType))),AttributeDecl(Instance,VarDecl(Id(x),ArrayType(133,FloatType)))])])'''
        self.assertTrue(TestAST.test(line, expect, 692))

    def test_693(self):
        line = '''Class a6:_{Constructor (x,nh,o_:Array [Float ,41];s8,kx,_A,_j2,S_F:__;_O,_9,c,_:_K;__,X_,_,_:Array [Array [Float ,0123],0x51]){} }'''
        expect = '''Program([ClassDecl(Id(a6),Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(x),ArrayType(41,FloatType)),param(Id(nh),ArrayType(41,FloatType)),param(Id(o_),ArrayType(41,FloatType)),param(Id(s8),ClassType(Id(__))),param(Id(kx),ClassType(Id(__))),param(Id(_A),ClassType(Id(__))),param(Id(_j2),ClassType(Id(__))),param(Id(S_F),ClassType(Id(__))),param(Id(_O),ClassType(Id(_K))),param(Id(_9),ClassType(Id(_K))),param(Id(c),ClassType(Id(_K))),param(Id(_),ClassType(Id(_K))),param(Id(__),ArrayType(81,ArrayType(83,FloatType))),param(Id(X_),ArrayType(81,ArrayType(83,FloatType))),param(Id(_),ArrayType(81,ArrayType(83,FloatType))),param(Id(_),ArrayType(81,ArrayType(83,FloatType)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 693))

    def test_694(self):
        line = '''Class _:r{}Class _:__{Constructor (h,_L:Array [Array [String ,0x2D],037_0_7]){}$0(Z,dh6f:Array [Array [Float ,0x2D],077]){}Constructor (q_:_aIn f_){}Destructor (){} }'''
        expect = '''Program([ClassDecl(Id(_),Id(r),[]),ClassDecl(Id(_),Id(__),[MethodDecl(Id(Constructor),Instance,[param(Id(h),ArrayType(1991,ArrayType(45,StringType))),param(Id(_L),ArrayType(1991,ArrayType(45,StringType)))],Block([],[])),MethodDecl(Id($0),Static,[param(Id(Z),ArrayType(63,ArrayType(45,FloatType))),param(Id(dh6f),ArrayType(63,ArrayType(45,FloatType)))],Block([],[])),MethodDecl(Id(Constructor),Instance,[param(Id(q_),ClassType(Id(_aIn)))],Block([],[])),MethodDecl(Id(Destructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 694))

    def test_695(self):
        line = '''Class m6:__{Var $0:Boolean ;Destructor (){} }Class p:_4_31{Var $_b,$R85,r:Array [Array [Array [String ,0XD],5],0105];}'''
        expect = '''Program([ClassDecl(Id(m6),Id(__),[AttributeDecl(Static,VarDecl(Id($0),BoolType)),MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(p),Id(_4_31),[AttributeDecl(Static,VarDecl(Id($_b),ArrayType(69,ArrayType(5,ArrayType(13,StringType))))),AttributeDecl(Static,VarDecl(Id($R85),ArrayType(69,ArrayType(5,ArrayType(13,StringType))))),AttributeDecl(Instance,VarDecl(Id(r),ArrayType(69,ArrayType(5,ArrayType(13,StringType)))))])])'''
        self.assertTrue(TestAST.test(line, expect, 695))

    def test_696(self):
        line = '''Class _{Destructor (){} }Class V{Var _,_d,_,$Z15_7,$19:Array [Array [Array [Array [Array [Array [Array [Array [Boolean ,0B100],072],0b1000101],06_54],33],0xAC],02_45],01_1_7];}'''
        expect = '''Program([ClassDecl(Id(_),[MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(V),[AttributeDecl(Instance,VarDecl(Id(_),ArrayType(79,ArrayType(165,ArrayType(172,ArrayType(33,ArrayType(428,ArrayType(69,ArrayType(58,ArrayType(4,BoolType)))))))))),AttributeDecl(Instance,VarDecl(Id(_d),ArrayType(79,ArrayType(165,ArrayType(172,ArrayType(33,ArrayType(428,ArrayType(69,ArrayType(58,ArrayType(4,BoolType)))))))))),AttributeDecl(Instance,VarDecl(Id(_),ArrayType(79,ArrayType(165,ArrayType(172,ArrayType(33,ArrayType(428,ArrayType(69,ArrayType(58,ArrayType(4,BoolType)))))))))),AttributeDecl(Static,VarDecl(Id($Z15_7),ArrayType(79,ArrayType(165,ArrayType(172,ArrayType(33,ArrayType(428,ArrayType(69,ArrayType(58,ArrayType(4,BoolType)))))))))),AttributeDecl(Static,VarDecl(Id($19),ArrayType(79,ArrayType(165,ArrayType(172,ArrayType(33,ArrayType(428,ArrayType(69,ArrayType(58,ArrayType(4,BoolType))))))))))])])'''
        self.assertTrue(TestAST.test(line, expect, 696))

    def test_697(self):
        line = '''Class _:_{Constructor (){} }Class W{Var Ur:Array [Array [Boolean ,0B1],0X53];}Class _V:_3{}'''
        expect = '''Program([ClassDecl(Id(_),Id(_),[MethodDecl(Id(Constructor),Instance,[],Block([],[]))]),ClassDecl(Id(W),[AttributeDecl(Instance,VarDecl(Id(Ur),ArrayType(83,ArrayType(1,BoolType))))]),ClassDecl(Id(_V),Id(_3),[])])'''
        self.assertTrue(TestAST.test(line, expect, 697))

    def test_698(self):
        line = '''Class p:_{}Class z_{}Class L_:B1{$z(){Continue ;__4=E9::$_.Kh1___();} }'''
        expect = '''Program([ClassDecl(Id(p),Id(_),[]),ClassDecl(Id(z_),[]),ClassDecl(Id(L_),Id(B1),[MethodDecl(Id($z),Static,[],Block([],[Continue,AssignStmt(Id(__4),CallExpr(FieldAccess(Id(E9),Id($_)),Id(Kh1___),[]))]))])])'''
        self.assertTrue(TestAST.test(line, expect, 698))

    def test_699(self):
        line = '''Class _4_3:x{Var _,$32:Array [Array [String ,5_5_6],05];}'''
        expect = '''Program([ClassDecl(Id(_4_3),Id(x),[AttributeDecl(Instance,VarDecl(Id(_),ArrayType(5,ArrayType(556,StringType)))),AttributeDecl(Static,VarDecl(Id($32),ArrayType(5,ArrayType(556,StringType))))])])'''
        self.assertTrue(TestAST.test(line, expect, 699))

    def test_700(self):
        line = '''Class _x_:k{Destructor (){Break ;}Destructor (){} }Class _{}Class c{Var $3:Float ;}'''
        expect = '''Program([ClassDecl(Id(_x_),Id(k),[MethodDecl(Id(Destructor),Instance,[],Block([],[Break])),MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(_),[]),ClassDecl(Id(c),[AttributeDecl(Static,VarDecl(Id($3),FloatType))])])'''
        self.assertTrue(TestAST.test(line, expect, 700))

    def test_701(self):
        line = '''Class v:l1W1{}Class _0:C2R{Constructor (of:Boolean ){} }'''
        expect = '''Program([ClassDecl(Id(v),Id(l1W1),[]),ClassDecl(Id(_0),Id(C2R),[MethodDecl(Id(Constructor),Instance,[param(Id(of),BoolType)],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 701))

    def test_702(self):
        line = '''Class n{$_9_585(__,qr1,_,_,d:Array [Boolean ,0x2E];IF:Boolean ;S:Boolean ;y,_c1A:Array [Array [Float ,37],0b1000101];a9,_:Array [Array [Array [Int ,053],064],064]){} }'''
        expect = '''Program([ClassDecl(Id(n),[MethodDecl(Id($_9_585),Static,[param(Id(__),ArrayType(46,BoolType)),param(Id(qr1),ArrayType(46,BoolType)),param(Id(_),ArrayType(46,BoolType)),param(Id(_),ArrayType(46,BoolType)),param(Id(d),ArrayType(46,BoolType)),param(Id(IF),BoolType),param(Id(S),BoolType),param(Id(y),ArrayType(69,ArrayType(37,FloatType))),param(Id(_c1A),ArrayType(69,ArrayType(37,FloatType))),param(Id(a9),ArrayType(52,ArrayType(52,ArrayType(43,IntType)))),param(Id(_),ArrayType(52,ArrayType(52,ArrayType(43,IntType))))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 702))

    def test_703(self):
        line = '''Class tg{Destructor (){}Var $eMP__:Array [Array [Array [Int ,50],07],0b1_0];Destructor (){} }'''
        expect = '''Program([ClassDecl(Id(tg),[MethodDecl(Id(Destructor),Instance,[],Block([],[])),AttributeDecl(Static,VarDecl(Id($eMP__),ArrayType(2,ArrayType(7,ArrayType(50,IntType))))),MethodDecl(Id(Destructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 703))

    def test_704(self):
        line = '''Class _{_k(Vd:Boolean ;H:_){} }Class NtoX4{}Class _t:__{}Class _2:l_K9d6_{}'''
        expect = '''Program([ClassDecl(Id(_),[MethodDecl(Id(_k),Instance,[param(Id(Vd),BoolType),param(Id(H),ClassType(Id(_)))],Block([],[]))]),ClassDecl(Id(NtoX4),[]),ClassDecl(Id(_t),Id(__),[]),ClassDecl(Id(_2),Id(l_K9d6_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 704))

    def test_705(self):
        line = '''Class q:__{Constructor (){}Var _h,B:Array [Float ,0x2E];}'''
        expect = '''Program([ClassDecl(Id(q),Id(__),[MethodDecl(Id(Constructor),Instance,[],Block([],[])),AttributeDecl(Instance,VarDecl(Id(_h),ArrayType(46,FloatType))),AttributeDecl(Instance,VarDecl(Id(B),ArrayType(46,FloatType)))])])'''
        self.assertTrue(TestAST.test(line, expect, 705))

    def test_706(self):
        line = '''Class _N3_2__Q7{j0(){}Constructor (_j4,Om,M,Zn:Array [String ,0X25]){}Constructor (){} }'''
        expect = '''Program([ClassDecl(Id(_N3_2__Q7),[MethodDecl(Id(j0),Instance,[],Block([],[])),MethodDecl(Id(Constructor),Instance,[param(Id(_j4),ArrayType(37,StringType)),param(Id(Om),ArrayType(37,StringType)),param(Id(M),ArrayType(37,StringType)),param(Id(Zn),ArrayType(37,StringType))],Block([],[])),MethodDecl(Id(Constructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 706))

    def test_707(self):
        line = '''Class Y_7Q{Constructor (){}Constructor (){}Destructor (){} }'''
        expect = '''Program([ClassDecl(Id(Y_7Q),[MethodDecl(Id(Constructor),Instance,[],Block([],[])),MethodDecl(Id(Constructor),Instance,[],Block([],[])),MethodDecl(Id(Destructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 707))

    def test_708(self):
        line = '''Class _{}Class Ba:_{Constructor (__,_17:Array [Int ,0B101110]){Continue ;} }'''
        expect = '''Program([ClassDecl(Id(_),[]),ClassDecl(Id(Ba),Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(__),ArrayType(46,IntType)),param(Id(_17),ArrayType(46,IntType))],Block([],[Continue]))])])'''
        self.assertTrue(TestAST.test(line, expect, 708))

    def test_709(self):
        line = '''Class f2:k{Var M,d7:Array [Float ,050];Var $j,vR:Boolean ;}'''
        expect = '''Program([ClassDecl(Id(f2),Id(k),[AttributeDecl(Instance,VarDecl(Id(M),ArrayType(40,FloatType))),AttributeDecl(Instance,VarDecl(Id(d7),ArrayType(40,FloatType))),AttributeDecl(Static,VarDecl(Id($j),BoolType)),AttributeDecl(Instance,VarDecl(Id(vR),BoolType))])])'''
        self.assertTrue(TestAST.test(line, expect, 709))

    def test_710(self):
        line = '''Class V6_em{}Class k:j{}Class __:_{}Class Dw:x{Constructor (){} }Class _{Destructor (){} }'''
        expect = '''Program([ClassDecl(Id(V6_em),[]),ClassDecl(Id(k),Id(j),[]),ClassDecl(Id(__),Id(_),[]),ClassDecl(Id(Dw),Id(x),[MethodDecl(Id(Constructor),Instance,[],Block([],[]))]),ClassDecl(Id(_),[MethodDecl(Id(Destructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 710))

    def test_711(self):
        line = '''Class _{}Class _:K8n{FU__3lOS7(_,D_9:Float ){} }Class _{}'''
        expect = '''Program([ClassDecl(Id(_),[]),ClassDecl(Id(_),Id(K8n),[MethodDecl(Id(FU__3lOS7),Instance,[param(Id(_),FloatType),param(Id(D_9),FloatType)],Block([],[]))]),ClassDecl(Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 711))

    def test_712(self):
        line = '''Class h:_{}Class pP:__o9{}Class g5_6:Y{}Class Z2:Q_a{Var _:Array [Array [Array [Float ,0b11011],0X62],0B1];}Class _5{}Class _:_{$a_(B:_){}$a(p,p7:Int ;_:Float ){} }'''
        expect = '''Program([ClassDecl(Id(h),Id(_),[]),ClassDecl(Id(pP),Id(__o9),[]),ClassDecl(Id(g5_6),Id(Y),[]),ClassDecl(Id(Z2),Id(Q_a),[AttributeDecl(Instance,VarDecl(Id(_),ArrayType(1,ArrayType(98,ArrayType(27,FloatType)))))]),ClassDecl(Id(_5),[]),ClassDecl(Id(_),Id(_),[MethodDecl(Id($a_),Static,[param(Id(B),ClassType(Id(_)))],Block([],[])),MethodDecl(Id($a),Static,[param(Id(p),IntType),param(Id(p7),IntType),param(Id(_),FloatType)],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 712))

    def test_713(self):
        line = '''Class _1MOq{Var $D0___,$7,$X:Array [Array [String ,83],40];}'''
        expect = '''Program([ClassDecl(Id(_1MOq),[AttributeDecl(Static,VarDecl(Id($D0___),ArrayType(40,ArrayType(83,StringType)))),AttributeDecl(Static,VarDecl(Id($7),ArrayType(40,ArrayType(83,StringType)))),AttributeDecl(Static,VarDecl(Id($X),ArrayType(40,ArrayType(83,StringType))))])])'''
        self.assertTrue(TestAST.test(line, expect, 713))

    def test_714(self):
        line = '''Class X:Q{Var $7V,$T:Boolean ;}Class E:Rt__9{Var A39,$E,K,$ts_:N_;}'''
        expect = '''Program([ClassDecl(Id(X),Id(Q),[AttributeDecl(Static,VarDecl(Id($7V),BoolType)),AttributeDecl(Static,VarDecl(Id($T),BoolType))]),ClassDecl(Id(E),Id(Rt__9),[AttributeDecl(Instance,VarDecl(Id(A39),ClassType(Id(N_)))),AttributeDecl(Static,VarDecl(Id($E),ClassType(Id(N_)))),AttributeDecl(Instance,VarDecl(Id(K),ClassType(Id(N_)))),AttributeDecl(Static,VarDecl(Id($ts_),ClassType(Id(N_))))])])'''
        self.assertTrue(TestAST.test(line, expect, 714))

    def test_715(self):
        line = '''Class _:D{Destructor (){} }Class Q{Var _U__,$_:Array [Array [Array [Array [Float ,265],3_53],25],06];}'''
        expect = '''Program([ClassDecl(Id(_),Id(D),[MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(Q),[AttributeDecl(Instance,VarDecl(Id(_U__),ArrayType(6,ArrayType(25,ArrayType(353,ArrayType(265,FloatType)))))),AttributeDecl(Static,VarDecl(Id($_),ArrayType(6,ArrayType(25,ArrayType(353,ArrayType(265,FloatType))))))])])'''
        self.assertTrue(TestAST.test(line, expect, 715))

    def test_716(self):
        line = '''Class A_R4{Constructor (){} }Class K:_0{}Class __{}Class W{}Class j__{}'''
        expect = '''Program([ClassDecl(Id(A_R4),[MethodDecl(Id(Constructor),Instance,[],Block([],[]))]),ClassDecl(Id(K),Id(_0),[]),ClassDecl(Id(__),[]),ClassDecl(Id(W),[]),ClassDecl(Id(j__),[])])'''
        self.assertTrue(TestAST.test(line, expect, 716))

    def test_717(self):
        line = '''Class _{}Class _:_V_0{Var $w:Array [Float ,19_24_6_4];}Class _:_{Destructor (){}Constructor (_1T:Array [Int ,01_1_4_6];_,_,b,ntU:_9){} }Class __8I:_8{}'''
        expect = '''Program([ClassDecl(Id(_),[]),ClassDecl(Id(_),Id(_V_0),[AttributeDecl(Static,VarDecl(Id($w),ArrayType(192464,FloatType)))]),ClassDecl(Id(_),Id(_),[MethodDecl(Id(Destructor),Instance,[],Block([],[])),MethodDecl(Id(Constructor),Instance,[param(Id(_1T),ArrayType(614,IntType)),param(Id(_),ClassType(Id(_9))),param(Id(_),ClassType(Id(_9))),param(Id(b),ClassType(Id(_9))),param(Id(ntU),ClassType(Id(_9)))],Block([],[]))]),ClassDecl(Id(__8I),Id(_8),[])])'''
        self.assertTrue(TestAST.test(line, expect, 717))

    def test_718(self):
        line = '''Class __2{Destructor (){}d(){}Var n,$Z:Boolean ;Destructor (){} }'''
        expect = '''Program([ClassDecl(Id(__2),[MethodDecl(Id(Destructor),Instance,[],Block([],[])),MethodDecl(Id(d),Instance,[],Block([],[])),AttributeDecl(Instance,VarDecl(Id(n),BoolType)),AttributeDecl(Static,VarDecl(Id($Z),BoolType)),MethodDecl(Id(Destructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 718))

    def test_719(self):
        line = '''Class W{Destructor (){}Var $____:j;Constructor (){} }Class _3{}'''
        expect = '''Program([ClassDecl(Id(W),[MethodDecl(Id(Destructor),Instance,[],Block([],[])),AttributeDecl(Static,VarDecl(Id($____),ClassType(Id(j)))),MethodDecl(Id(Constructor),Instance,[],Block([],[]))]),ClassDecl(Id(_3),[])])'''
        self.assertTrue(TestAST.test(line, expect, 719))

    def test_720(self):
        line = '''Class __6{Constructor (K,__4_,_M,_13_:Int ;_3,_:String ){}Var I9jb:Int ;}Class _{$s(){Break ;} }'''
        expect = '''Program([ClassDecl(Id(__6),[MethodDecl(Id(Constructor),Instance,[param(Id(K),IntType),param(Id(__4_),IntType),param(Id(_M),IntType),param(Id(_13_),IntType),param(Id(_3),StringType),param(Id(_),StringType)],Block([],[])),AttributeDecl(Instance,VarDecl(Id(I9jb),IntType))]),ClassDecl(Id(_),[MethodDecl(Id($s),Static,[],Block([],[Break]))])])'''
        self.assertTrue(TestAST.test(line, expect, 720))

    def test_721(self):
        line = '''Class hu:_4z{Var $8_P_1O_,$BC:Int ;Var $4,N5:Int ;}Class _a{Destructor (){ {} }}'''
        expect = '''Program([ClassDecl(Id(hu),Id(_4z),[AttributeDecl(Static,VarDecl(Id($8_P_1O_),IntType)),AttributeDecl(Static,VarDecl(Id($BC),IntType)),AttributeDecl(Static,VarDecl(Id($4),IntType)),AttributeDecl(Instance,VarDecl(Id(N5),IntType))]),ClassDecl(Id(_a),[MethodDecl(Id(Destructor),Instance,[],Block([],[Block([],[])]))])])'''
        self.assertTrue(TestAST.test(line, expect, 721))

    def test_722(self):
        line = '''Class CM{Constructor (Y:Boolean ;y,WT3:Float ){ {}v_::$5();} }'''
        expect = '''Program([ClassDecl(Id(CM),[MethodDecl(Id(Constructor),Instance,[param(Id(Y),BoolType),param(Id(y),FloatType),param(Id(WT3),FloatType)],Block([],[Block([],[]),Call(Id(v_),Id($5),[])]))])])'''
        self.assertTrue(TestAST.test(line, expect, 722))

    def test_723(self):
        line = '''Class _7t:pa1{}Class _:__wV{Constructor (_h,L:Int ){}Destructor (){}Constructor (){} }'''
        expect = '''Program([ClassDecl(Id(_7t),Id(pa1),[]),ClassDecl(Id(_),Id(__wV),[MethodDecl(Id(Constructor),Instance,[param(Id(_h),IntType),param(Id(L),IntType)],Block([],[])),MethodDecl(Id(Destructor),Instance,[],Block([],[])),MethodDecl(Id(Constructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 723))

    def test_724(self):
        line = '''Class _:_L6_{Var x_,_40_,__Q:Array [Array [Array [Array [Int ,0X4E],534],0B1],1];}Class _6_a:_{Constructor (){} }'''
        expect = '''Program([ClassDecl(Id(_),Id(_L6_),[AttributeDecl(Instance,VarDecl(Id(x_),ArrayType(1,ArrayType(1,ArrayType(534,ArrayType(78,IntType)))))),AttributeDecl(Instance,VarDecl(Id(_40_),ArrayType(1,ArrayType(1,ArrayType(534,ArrayType(78,IntType)))))),AttributeDecl(Instance,VarDecl(Id(__Q),ArrayType(1,ArrayType(1,ArrayType(534,ArrayType(78,IntType))))))]),ClassDecl(Id(_6_a),Id(_),[MethodDecl(Id(Constructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 724))

    def test_725(self):
        line = '''Class PR__:_{$VL(_,_,f:String ;N4_H,f_0_:String ;x:Int ){} }Class o:v{Constructor (u2___P:String ;_,Z,_O:_){}Constructor (P:_L;l9ui__:Boolean ;_3_:Array [Array [Float ,87],0x7_E];mS1:Int ){} }'''
        expect = '''Program([ClassDecl(Id(PR__),Id(_),[MethodDecl(Id($VL),Static,[param(Id(_),StringType),param(Id(_),StringType),param(Id(f),StringType),param(Id(N4_H),StringType),param(Id(f_0_),StringType),param(Id(x),IntType)],Block([],[]))]),ClassDecl(Id(o),Id(v),[MethodDecl(Id(Constructor),Instance,[param(Id(u2___P),StringType),param(Id(_),ClassType(Id(_))),param(Id(Z),ClassType(Id(_))),param(Id(_O),ClassType(Id(_)))],Block([],[])),MethodDecl(Id(Constructor),Instance,[param(Id(P),ClassType(Id(_L))),param(Id(l9ui__),BoolType),param(Id(_3_),ArrayType(126,ArrayType(87,FloatType))),param(Id(mS1),IntType)],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 725))

    def test_726(self):
        line = '''Class M{}Class _3{Var $3,_,$__,$E:Array [Array [Boolean ,0B11_0_00],0X55];}Class x2{}'''
        expect = '''Program([ClassDecl(Id(M),[]),ClassDecl(Id(_3),[AttributeDecl(Static,VarDecl(Id($3),ArrayType(85,ArrayType(24,BoolType)))),AttributeDecl(Instance,VarDecl(Id(_),ArrayType(85,ArrayType(24,BoolType)))),AttributeDecl(Static,VarDecl(Id($__),ArrayType(85,ArrayType(24,BoolType)))),AttributeDecl(Static,VarDecl(Id($E),ArrayType(85,ArrayType(24,BoolType))))]),ClassDecl(Id(x2),[])])'''
        self.assertTrue(TestAST.test(line, expect, 726))

    def test_727(self):
        line = '''Class Ta:a{Destructor (){} }Class _:x{$____c(){Break ;Continue ;} }Class __w:_{}'''
        expect = '''Program([ClassDecl(Id(Ta),Id(a),[MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(_),Id(x),[MethodDecl(Id($____c),Static,[],Block([],[Break,Continue]))]),ClassDecl(Id(__w),Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 727))

    def test_728(self):
        line = '''Class _4g42:_{Constructor (h:Array [String ,0xF]){} }Class _{}Class g{Var _:_;}'''
        expect = '''Program([ClassDecl(Id(_4g42),Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(h),ArrayType(15,StringType))],Block([],[]))]),ClassDecl(Id(_),[]),ClassDecl(Id(g),[AttributeDecl(Instance,VarDecl(Id(_),ClassType(Id(_))))])])'''
        self.assertTrue(TestAST.test(line, expect, 728))

    def test_729(self):
        line = '''Class L4{Var _z_,d_:Array [Array [Array [Int ,0b1000010],5_6],0B11];_(A:Array [Array [Array [String ,19],1],0B1];p,Fx2:Float ;_:Float ;V,Wy2_,Uk,A:_;r_:Array [Array [Array [Array [Float ,03],04],01],0x7]){}Constructor (){} }'''
        expect = '''Program([ClassDecl(Id(L4),[AttributeDecl(Instance,VarDecl(Id(_z_),ArrayType(3,ArrayType(56,ArrayType(66,IntType))))),AttributeDecl(Instance,VarDecl(Id(d_),ArrayType(3,ArrayType(56,ArrayType(66,IntType))))),MethodDecl(Id(_),Instance,[param(Id(A),ArrayType(1,ArrayType(1,ArrayType(19,StringType)))),param(Id(p),FloatType),param(Id(Fx2),FloatType),param(Id(_),FloatType),param(Id(V),ClassType(Id(_))),param(Id(Wy2_),ClassType(Id(_))),param(Id(Uk),ClassType(Id(_))),param(Id(A),ClassType(Id(_))),param(Id(r_),ArrayType(7,ArrayType(1,ArrayType(4,ArrayType(3,FloatType)))))],Block([],[])),MethodDecl(Id(Constructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 729))

    def test_730(self):
        line = '''Class _{}Class _{}Class _{}Class _:_{Constructor (_:String ){Return ;{} }}Class _:m_{}'''
        expect = '''Program([ClassDecl(Id(_),[]),ClassDecl(Id(_),[]),ClassDecl(Id(_),[]),ClassDecl(Id(_),Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(_),StringType)],Block([],[Return(None),Block([],[])]))]),ClassDecl(Id(_),Id(m_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 730))

    def test_731(self):
        line = '''Class RE{Constructor (){}Constructor (){}k_p(){Break ;Break ;Break ;Break ;} }'''
        expect = '''Program([ClassDecl(Id(RE),[MethodDecl(Id(Constructor),Instance,[],Block([],[])),MethodDecl(Id(Constructor),Instance,[],Block([],[])),MethodDecl(Id(k_p),Instance,[],Block([],[Break,Break,Break,Break]))])])'''
        self.assertTrue(TestAST.test(line, expect, 731))

    def test_732(self):
        line = '''Class _{}Class _48:Xt{}Class mx{Var F,$b,$7,_,$S,$ge_:Int ;}'''
        expect = '''Program([ClassDecl(Id(_),[]),ClassDecl(Id(_48),Id(Xt),[]),ClassDecl(Id(mx),[AttributeDecl(Instance,VarDecl(Id(F),IntType)),AttributeDecl(Static,VarDecl(Id($b),IntType)),AttributeDecl(Static,VarDecl(Id($7),IntType)),AttributeDecl(Instance,VarDecl(Id(_),IntType)),AttributeDecl(Static,VarDecl(Id($S),IntType)),AttributeDecl(Static,VarDecl(Id($ge_),IntType))])])'''
        self.assertTrue(TestAST.test(line, expect, 732))

    def test_733(self):
        line = '''Class ___:___{}Class _:_{}Class i42u:e{$t(___:Array [Float ,98];_:Boolean ;_,_:String ){}Var _:Array [String ,2];}'''
        expect = '''Program([ClassDecl(Id(___),Id(___),[]),ClassDecl(Id(_),Id(_),[]),ClassDecl(Id(i42u),Id(e),[MethodDecl(Id($t),Static,[param(Id(___),ArrayType(98,FloatType)),param(Id(_),BoolType),param(Id(_),StringType),param(Id(_),StringType)],Block([],[])),AttributeDecl(Instance,VarDecl(Id(_),ArrayType(2,StringType)))])])'''
        self.assertTrue(TestAST.test(line, expect, 733))

    def test_734(self):
        line = '''Class _:_{}Class G:_{}Class __8_:R{Var _:String ;}Class _{__(_1:Int ){} }'''
        expect = '''Program([ClassDecl(Id(_),Id(_),[]),ClassDecl(Id(G),Id(_),[]),ClassDecl(Id(__8_),Id(R),[AttributeDecl(Instance,VarDecl(Id(_),StringType))]),ClassDecl(Id(_),[MethodDecl(Id(__),Instance,[param(Id(_1),IntType)],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 734))

    def test_735(self):
        line = '''Class Mq:u6_{Constructor (_6:Y_M;j03,_8:Int ;o6:H_;_,_,_5,m,_,q8:String ){} }Class _:Z{Constructor (_,a:Boolean ;R:Boolean ){s_n_::$Yk_();} }'''
        expect = '''Program([ClassDecl(Id(Mq),Id(u6_),[MethodDecl(Id(Constructor),Instance,[param(Id(_6),ClassType(Id(Y_M))),param(Id(j03),IntType),param(Id(_8),IntType),param(Id(o6),ClassType(Id(H_))),param(Id(_),StringType),param(Id(_),StringType),param(Id(_5),StringType),param(Id(m),StringType),param(Id(_),StringType),param(Id(q8),StringType)],Block([],[]))]),ClassDecl(Id(_),Id(Z),[MethodDecl(Id(Constructor),Instance,[param(Id(_),BoolType),param(Id(a),BoolType),param(Id(R),BoolType)],Block([],[Call(Id(s_n_),Id($Yk_),[])]))])])'''
        self.assertTrue(TestAST.test(line, expect, 735))

    def test_736(self):
        line = '''Class u{Constructor (){}U_u_(WH,_:Boolean ;___9h:Boolean ;__q:v){}Var _,$L:Int ;}'''
        expect = '''Program([ClassDecl(Id(u),[MethodDecl(Id(Constructor),Instance,[],Block([],[])),MethodDecl(Id(U_u_),Instance,[param(Id(WH),BoolType),param(Id(_),BoolType),param(Id(___9h),BoolType),param(Id(__q),ClassType(Id(v)))],Block([],[])),AttributeDecl(Instance,VarDecl(Id(_),IntType)),AttributeDecl(Static,VarDecl(Id($L),IntType))])])'''
        self.assertTrue(TestAST.test(line, expect, 736))

    def test_737(self):
        line = '''Class _{Constructor (g,J6,z,_,a_,O0,D7Y,_JPR,__0l:Array [Int ,06_0];_8,_,_Or_T:Int ){} }Class _i:_{}'''
        expect = '''Program([ClassDecl(Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(g),ArrayType(48,IntType)),param(Id(J6),ArrayType(48,IntType)),param(Id(z),ArrayType(48,IntType)),param(Id(_),ArrayType(48,IntType)),param(Id(a_),ArrayType(48,IntType)),param(Id(O0),ArrayType(48,IntType)),param(Id(D7Y),ArrayType(48,IntType)),param(Id(_JPR),ArrayType(48,IntType)),param(Id(__0l),ArrayType(48,IntType)),param(Id(_8),IntType),param(Id(_),IntType),param(Id(_Or_T),IntType)],Block([],[]))]),ClassDecl(Id(_i),Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 737))

    def test_738(self):
        line = '''Class _7_{Constructor (_A__4Oi_:i;e,h0:Int ;i:Array [Array [Boolean ,80],0B1001011];M:Array [Array [Array [Array [Array [Int ,80],0b1_1],80],0xA],05]){} }'''
        expect = '''Program([ClassDecl(Id(_7_),[MethodDecl(Id(Constructor),Instance,[param(Id(_A__4Oi_),ClassType(Id(i))),param(Id(e),IntType),param(Id(h0),IntType),param(Id(i),ArrayType(75,ArrayType(80,BoolType))),param(Id(M),ArrayType(5,ArrayType(10,ArrayType(80,ArrayType(3,ArrayType(80,IntType))))))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 738))

    def test_739(self):
        line = '''Class t{}Class l_3{$48(_5:Boolean ){Continue ;}Var F,A,cI7,i,$l,H:c__;}'''
        expect = '''Program([ClassDecl(Id(t),[]),ClassDecl(Id(l_3),[MethodDecl(Id($48),Static,[param(Id(_5),BoolType)],Block([],[Continue])),AttributeDecl(Instance,VarDecl(Id(F),ClassType(Id(c__)))),AttributeDecl(Instance,VarDecl(Id(A),ClassType(Id(c__)))),AttributeDecl(Instance,VarDecl(Id(cI7),ClassType(Id(c__)))),AttributeDecl(Instance,VarDecl(Id(i),ClassType(Id(c__)))),AttributeDecl(Static,VarDecl(Id($l),ClassType(Id(c__)))),AttributeDecl(Instance,VarDecl(Id(H),ClassType(Id(c__))))])])'''
        self.assertTrue(TestAST.test(line, expect, 739))

    def test_740(self):
        line = '''Class y_C:O{Constructor (_03_,_:_){} }Class UhX3cj_:N{}'''
        expect = '''Program([ClassDecl(Id(y_C),Id(O),[MethodDecl(Id(Constructor),Instance,[param(Id(_03_),ClassType(Id(_))),param(Id(_),ClassType(Id(_)))],Block([],[]))]),ClassDecl(Id(UhX3cj_),Id(N),[])])'''
        self.assertTrue(TestAST.test(line, expect, 740))

    def test_741(self):
        line = '''Class N____{}Class _V__{Constructor (_76,__:Boolean ;_,O_p31:Int ){} }Class h7:f_{Var $d_l:Boolean ;}'''
        expect = '''Program([ClassDecl(Id(N____),[]),ClassDecl(Id(_V__),[MethodDecl(Id(Constructor),Instance,[param(Id(_76),BoolType),param(Id(__),BoolType),param(Id(_),IntType),param(Id(O_p31),IntType)],Block([],[]))]),ClassDecl(Id(h7),Id(f_),[AttributeDecl(Static,VarDecl(Id($d_l),BoolType))])])'''
        self.assertTrue(TestAST.test(line, expect, 741))

    def test_742(self):
        line = '''Class l3{}Class q_:T{}Class G:_7{}Class _{Destructor (){} }'''
        expect = '''Program([ClassDecl(Id(l3),[]),ClassDecl(Id(q_),Id(T),[]),ClassDecl(Id(G),Id(_7),[]),ClassDecl(Id(_),[MethodDecl(Id(Destructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 742))

    def test_743(self):
        line = '''Class _3{Destructor (){} }Class H6{}Class _:__K{}Class __:_{}Class _{}'''
        expect = '''Program([ClassDecl(Id(_3),[MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(H6),[]),ClassDecl(Id(_),Id(__K),[]),ClassDecl(Id(__),Id(_),[]),ClassDecl(Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 743))

    def test_744(self):
        line = '''Class _{}Class _:_{}Class g_n:UUJ6_{$Q(m,_,aA4,V:O_8;X_3_S:Array [Array [Int ,1_6],0B1]){} }Class _:U{Constructor (){} }Class _{}'''
        expect = '''Program([ClassDecl(Id(_),[]),ClassDecl(Id(_),Id(_),[]),ClassDecl(Id(g_n),Id(UUJ6_),[MethodDecl(Id($Q),Static,[param(Id(m),ClassType(Id(O_8))),param(Id(_),ClassType(Id(O_8))),param(Id(aA4),ClassType(Id(O_8))),param(Id(V),ClassType(Id(O_8))),param(Id(X_3_S),ArrayType(1,ArrayType(16,IntType)))],Block([],[]))]),ClassDecl(Id(_),Id(U),[MethodDecl(Id(Constructor),Instance,[],Block([],[]))]),ClassDecl(Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 744))

    def test_745(self):
        line = '''Class _:x4_{Val _GO:k=!__.F()<=yYF9::$7._()._A_N._.L7K+!tW0::$iw_9();}'''
        expect = '''Program([ClassDecl(Id(_),Id(x4_),[AttributeDecl(Instance,ConstDecl(Id(_86),ClassType(Id(k)),BinaryOp(<=,UnaryOp(!,CallExpr(Id(__),Id(F),[])),BinaryOp(+,FieldAccess(FieldAccess(FieldAccess(CallExpr(FieldAccess(Id(yYF9),Id($7)),Id(_),[]),Id(_A_N)),Id(_)),Id(L7K)),UnaryOp(!,CallExpr(Id(tW0),Id($iw_9),[]))))))])])'''
        self.assertTrue(TestAST.test(line, expect, 745))

    def test_746(self):
        line = '''Class __85{$_(_N,_5,C,Tx,__N:Boolean ;J_,_H:_54;_,__1,B_r5_c:Array [Float ,69]){} }'''
        expect = '''Program([ClassDecl(Id(__85),[MethodDecl(Id($_),Static,[param(Id(_N),BoolType),param(Id(_5),BoolType),param(Id(C),BoolType),param(Id(Tx),BoolType),param(Id(__N),BoolType),param(Id(J_),ClassType(Id(_54))),param(Id(_H),ClassType(Id(_54))),param(Id(_),ArrayType(69,FloatType)),param(Id(__1),ArrayType(69,FloatType)),param(Id(B_r5_c),ArrayType(69,FloatType))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 746))

    def test_747(self):
        line = '''Class __{Var $_,$8,$__,H_a,$_:s;}Class hIz:_F{Var $0,rl_I:Array [Int ,011];}Class __:_{}'''
        expect = '''Program([ClassDecl(Id(__),[AttributeDecl(Static,VarDecl(Id($_),ClassType(Id(s)))),AttributeDecl(Static,VarDecl(Id($8),ClassType(Id(s)))),AttributeDecl(Static,VarDecl(Id($__),ClassType(Id(s)))),AttributeDecl(Instance,VarDecl(Id(H_a),ClassType(Id(s)))),AttributeDecl(Static,VarDecl(Id($_),ClassType(Id(s))))]),ClassDecl(Id(hIz),Id(_F),[AttributeDecl(Static,VarDecl(Id($0),ArrayType(9,IntType))),AttributeDecl(Instance,VarDecl(Id(rl_I),ArrayType(9,IntType)))]),ClassDecl(Id(__),Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 747))

    def test_748(self):
        line = '''Class bv{}Class i:p_{Constructor (){}Var $Y,$2:Float ;}Class l:_t{}'''
        expect = '''Program([ClassDecl(Id(bv),[]),ClassDecl(Id(i),Id(p_),[MethodDecl(Id(Constructor),Instance,[],Block([],[])),AttributeDecl(Static,VarDecl(Id($Y),FloatType)),AttributeDecl(Static,VarDecl(Id($2),FloatType))]),ClassDecl(Id(l),Id(_t),[])])'''
        self.assertTrue(TestAST.test(line, expect, 748))

    def test_749(self):
        line = '''Class O9{Constructor (_2CM_iB:Array [Array [String ,0xB9F],0142];e:Boolean ;_5lI_25:Int ;_,_:j;_S0e:Boolean ){} }'''
        expect = '''Program([ClassDecl(Id(O9),[MethodDecl(Id(Constructor),Instance,[param(Id(_2CM_iB),ArrayType(98,ArrayType(2975,StringType))),param(Id(e),BoolType),param(Id(_5lI_25),IntType),param(Id(_),ClassType(Id(j))),param(Id(_),ClassType(Id(j))),param(Id(_S0e),BoolType)],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 749))

    def test_750(self):
        line = '''Class Ve_0{$_(w4__7U_:Float ;SX:Array [Array [Float ,50],6]){} }Class n:A3{}'''
        expect = '''Program([ClassDecl(Id(Ve_0),[MethodDecl(Id($_),Static,[param(Id(w4__7U_),FloatType),param(Id(SX),ArrayType(6,ArrayType(50,FloatType)))],Block([],[]))]),ClassDecl(Id(n),Id(A3),[])])'''
        self.assertTrue(TestAST.test(line, expect, 750))

    def test_751(self):
        line = '''Class _{}Class _:C1{Constructor (LY_,O,__:Int ){}Destructor (){Break ;Continue ;} }'''
        expect = '''Program([ClassDecl(Id(_),[]),ClassDecl(Id(_),Id(C1),[MethodDecl(Id(Constructor),Instance,[param(Id(LY_),IntType),param(Id(O),IntType),param(Id(__),IntType)],Block([],[])),MethodDecl(Id(Destructor),Instance,[],Block([],[Break,Continue]))])])'''
        self.assertTrue(TestAST.test(line, expect, 751))

    def test_752(self):
        line = '''Class _9_:_{Constructor (){} }Class I:lL{Destructor (){} }'''
        expect = '''Program([ClassDecl(Id(_9_),Id(_),[MethodDecl(Id(Constructor),Instance,[],Block([],[]))]),ClassDecl(Id(I),Id(lL),[MethodDecl(Id(Destructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 752))

    def test_753(self):
        line = '''Class _K1{}Class _:t{Constructor (){If (!-_::$59_745){} }}'''
        expect = '''Program([ClassDecl(Id(_K1),[]),ClassDecl(Id(_),Id(t),[MethodDecl(Id(Constructor),Instance,[],Block([],[If(UnaryOp(!,UnaryOp(-,FieldAccess(Id(_),Id($59_745)))),Block([],[]))]))])])'''
        self.assertTrue(TestAST.test(line, expect, 753))

    def test_754(self):
        line = '''Class o:N4qs{Var S0:Array [Array [Array [Array [Boolean ,0X5E],0724],0X5E],77];$0(b0,L,y6:Boolean ){}$__(){ {} }}'''
        expect = '''Program([ClassDecl(Id(o),Id(N4qs),[AttributeDecl(Instance,VarDecl(Id(S0),ArrayType(77,ArrayType(94,ArrayType(468,ArrayType(94,BoolType)))))),MethodDecl(Id($0),Static,[param(Id(b0),BoolType),param(Id(L),BoolType),param(Id(y6),BoolType)],Block([],[])),MethodDecl(Id($__),Static,[],Block([],[Block([],[])]))])])'''
        self.assertTrue(TestAST.test(line, expect, 754))

    def test_755(self):
        line = '''Class X{Var e,$_,I:Array [Array [Float ,020],0X2E];}Class _{}'''
        expect = '''Program([ClassDecl(Id(X),[AttributeDecl(Instance,VarDecl(Id(e),ArrayType(46,ArrayType(16,FloatType)))),AttributeDecl(Static,VarDecl(Id($_),ArrayType(46,ArrayType(16,FloatType)))),AttributeDecl(Instance,VarDecl(Id(I),ArrayType(46,ArrayType(16,FloatType))))]),ClassDecl(Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 755))

    def test_756(self):
        line = '''Class t_8681:Yn_9o{Constructor (){}Var _:Array [Array [Array [Float ,0B1],51],0XD];}'''
        expect = '''Program([ClassDecl(Id(t_8681),Id(Yn_9o),[MethodDecl(Id(Constructor),Instance,[],Block([],[])),AttributeDecl(Instance,VarDecl(Id(_),ArrayType(13,ArrayType(51,ArrayType(1,FloatType)))))])])'''
        self.assertTrue(TestAST.test(line, expect, 756))

    def test_757(self):
        line = '''Class _:J{Var k,_,$Z_N1,$2:_;Constructor (u86:Array [Boolean ,0x8];M:__a;_,_5:___;l,p,y,_z8,_16:Boolean ;J0:Array [String ,0b1_0];_,__I:Array [Float ,06];N,U_:_){}Constructor (_U__:Array [Boolean ,0B1100100]){Continue ;} }Class D5:_4{}Class R69:_5{}Class _:o_d{}'''
        expect = '''Program([ClassDecl(Id(_),Id(J),[AttributeDecl(Instance,VarDecl(Id(k),ClassType(Id(_)))),AttributeDecl(Instance,VarDecl(Id(_),ClassType(Id(_)))),AttributeDecl(Static,VarDecl(Id($Z_N1),ClassType(Id(_)))),AttributeDecl(Static,VarDecl(Id($2),ClassType(Id(_)))),MethodDecl(Id(Constructor),Instance,[param(Id(u86),ArrayType(8,BoolType)),param(Id(M),ClassType(Id(__a))),param(Id(_),ClassType(Id(___))),param(Id(_5),ClassType(Id(___))),param(Id(l),BoolType),param(Id(p),BoolType),param(Id(y),BoolType),param(Id(_z8),BoolType),param(Id(_16),BoolType),param(Id(J0),ArrayType(2,StringType)),param(Id(_),ArrayType(6,FloatType)),param(Id(__I),ArrayType(6,FloatType)),param(Id(N),ClassType(Id(_))),param(Id(U_),ClassType(Id(_)))],Block([],[])),MethodDecl(Id(Constructor),Instance,[param(Id(_U__),ArrayType(100,BoolType))],Block([],[Continue]))]),ClassDecl(Id(D5),Id(_4),[]),ClassDecl(Id(R69),Id(_5),[]),ClassDecl(Id(_),Id(o_d),[])])'''
        self.assertTrue(TestAST.test(line, expect, 757))

    def test_758(self):
        line = '''Class _{}Class J{}Class __:En{}Class _{Constructor (W2P:U){} }'''
        expect = '''Program([ClassDecl(Id(_),[]),ClassDecl(Id(J),[]),ClassDecl(Id(__),Id(En),[]),ClassDecl(Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(W2P),ClassType(Id(U)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 758))

    def test_759(self):
        line = '''Class _0{Constructor (E:Array [Array [Array [Float ,99],0b1_0_0],0x6];J,e81a,l:Qy){} }Class G_j:I_X_{}Class _:s{}Class M:_{}Class _{}'''
        expect = '''Program([ClassDecl(Id(_0),[MethodDecl(Id(Constructor),Instance,[param(Id(E),ArrayType(6,ArrayType(4,ArrayType(99,FloatType)))),param(Id(J),ClassType(Id(Qy))),param(Id(e81a),ClassType(Id(Qy))),param(Id(l),ClassType(Id(Qy)))],Block([],[]))]),ClassDecl(Id(G_j),Id(I_X_),[]),ClassDecl(Id(_),Id(s),[]),ClassDecl(Id(M),Id(_),[]),ClassDecl(Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 759))

    def test_760(self):
        line = '''Class _{}Class _{Var _P:Array [Boolean ,0xD9];Destructor (){} }'''
        expect = '''Program([ClassDecl(Id(_),[]),ClassDecl(Id(_),[AttributeDecl(Instance,VarDecl(Id(_P),ArrayType(217,BoolType))),MethodDecl(Id(Destructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 760))

    def test_761(self):
        line = '''Class q_{Constructor (vx,__,p,_:F4m;_:Array [Boolean ,050]){} }'''
        expect = '''Program([ClassDecl(Id(q_),[MethodDecl(Id(Constructor),Instance,[param(Id(vx),ClassType(Id(F4m))),param(Id(__),ClassType(Id(F4m))),param(Id(p),ClassType(Id(F4m))),param(Id(_),ClassType(Id(F4m))),param(Id(_),ArrayType(40,BoolType))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 761))

    def test_762(self):
        line = '''Class _{Constructor (_:Array [Boolean ,0x7];__,_,__,n94188IN19:String ){}$_(_,i448,Y:Float ;CEH:Int ;__1:_5_Rn){} }Class _:O6{i_(){} }'''
        expect = '''Program([ClassDecl(Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(_),ArrayType(7,BoolType)),param(Id(__),StringType),param(Id(_),StringType),param(Id(__),StringType),param(Id(n94188IN19),StringType)],Block([],[])),MethodDecl(Id($_),Static,[param(Id(_),FloatType),param(Id(i448),FloatType),param(Id(Y),FloatType),param(Id(CEH),IntType),param(Id(__1),ClassType(Id(_5_Rn)))],Block([],[]))]),ClassDecl(Id(_),Id(O6),[MethodDecl(Id(i_),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 762))

    def test_763(self):
        line = '''Class _:_{$7(U_:Array [Boolean ,0X5];__:Array [Int ,4];_7,F3,l:_0){}Constructor (){} }'''
        expect = '''Program([ClassDecl(Id(_),Id(_),[MethodDecl(Id($7),Static,[param(Id(U_),ArrayType(5,BoolType)),param(Id(__),ArrayType(4,IntType)),param(Id(_7),ClassType(Id(_0))),param(Id(F3),ClassType(Id(_0))),param(Id(l),ClassType(Id(_0)))],Block([],[])),MethodDecl(Id(Constructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 763))

    def test_764(self):
        line = '''Class _:G9{Constructor (e3_68_,x:Array [String ,0B1];c51_3:Int ){} }'''
        expect = '''Program([ClassDecl(Id(_),Id(G9),[MethodDecl(Id(Constructor),Instance,[param(Id(e3_68_),ArrayType(1,StringType)),param(Id(x),ArrayType(1,StringType)),param(Id(c51_3),IntType)],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 764))

    def test_765(self):
        line = '''Class g_J4{}Class n{Constructor (J:Float ;TH,U:String ;s:Boolean ;a3,__:Int ){} }'''
        expect = '''Program([ClassDecl(Id(g_J4),[]),ClassDecl(Id(n),[MethodDecl(Id(Constructor),Instance,[param(Id(J),FloatType),param(Id(TH),StringType),param(Id(U),StringType),param(Id(s),BoolType),param(Id(a3),IntType),param(Id(__),IntType)],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 765))

    def test_766(self):
        line = '''Class _{$X_(_:String ){} }Class _uT:_44{Var $0:String ;}Class __:yx{}'''
        expect = '''Program([ClassDecl(Id(_),[MethodDecl(Id($X_),Static,[param(Id(_),StringType)],Block([],[]))]),ClassDecl(Id(_uT),Id(_44),[AttributeDecl(Static,VarDecl(Id($0),StringType))]),ClassDecl(Id(__),Id(yx),[])])'''
        self.assertTrue(TestAST.test(line, expect, 766))

    def test_767(self):
        line = '''Class _{}Class q_{}Class _{}Class _{Var $3:Array [String ,0x5B];}'''
        expect = '''Program([ClassDecl(Id(_),[]),ClassDecl(Id(q_),[]),ClassDecl(Id(_),[]),ClassDecl(Id(_),[AttributeDecl(Static,VarDecl(Id($3),ArrayType(91,StringType)))])])'''
        self.assertTrue(TestAST.test(line, expect, 767))

    def test_768(self):
        line = '''Class t{}Class _fl:_{Var oTr__F,_6,g,$_W9_,d,s:J;}Class __6:__{}'''
        expect = '''Program([ClassDecl(Id(t),[]),ClassDecl(Id(_fl),Id(_),[AttributeDecl(Instance,VarDecl(Id(oTr__F),ClassType(Id(J)))),AttributeDecl(Instance,VarDecl(Id(_6),ClassType(Id(J)))),AttributeDecl(Instance,VarDecl(Id(g),ClassType(Id(J)))),AttributeDecl(Static,VarDecl(Id($_W9_),ClassType(Id(J)))),AttributeDecl(Instance,VarDecl(Id(d),ClassType(Id(J)))),AttributeDecl(Instance,VarDecl(Id(s),ClassType(Id(J))))]),ClassDecl(Id(__6),Id(__),[])])'''
        self.assertTrue(TestAST.test(line, expect, 768))

    def test_769(self):
        line = '''Class WJ:_K{Constructor (){Break ;Continue ;{}Break ;Return ;}Var _,e,$6qt:Array [Array [Array [Array [Array [Array [String ,0x5],3],66],0X19],58],0B1001010];}Class q2:_{}'''
        expect = '''Program([ClassDecl(Id(WJ),Id(_K),[MethodDecl(Id(Constructor),Instance,[],Block([],[Break,Continue,Block([],[]),Break,Return(None)])),AttributeDecl(Instance,VarDecl(Id(_),ArrayType(74,ArrayType(58,ArrayType(25,ArrayType(66,ArrayType(3,ArrayType(5,StringType)))))))),AttributeDecl(Instance,VarDecl(Id(e),ArrayType(74,ArrayType(58,ArrayType(25,ArrayType(66,ArrayType(3,ArrayType(5,StringType)))))))),AttributeDecl(Static,VarDecl(Id($6qt),ArrayType(74,ArrayType(58,ArrayType(25,ArrayType(66,ArrayType(3,ArrayType(5,StringType))))))))]),ClassDecl(Id(q2),Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 769))

    def test_770(self):
        line = '''Class _85{Constructor (_6,S_:Array [Int ,0XC];__3,_,_j,_:Array [String ,01_73]){} }Class u:__{}Class _:X{}Class _{}'''
        expect = '''Program([ClassDecl(Id(_85),[MethodDecl(Id(Constructor),Instance,[param(Id(_6),ArrayType(12,IntType)),param(Id(S_),ArrayType(12,IntType)),param(Id(__3),ArrayType(123,StringType)),param(Id(_),ArrayType(123,StringType)),param(Id(_j),ArrayType(123,StringType)),param(Id(_),ArrayType(123,StringType))],Block([],[]))]),ClassDecl(Id(u),Id(__),[]),ClassDecl(Id(_),Id(X),[]),ClassDecl(Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 770))

    def test_771(self):
        line = '''Class _:_{Constructor (_:Array [Array [Boolean ,4_7_4],0b1011111];u75:i;m_6,__:Float ;D:Float ){} }Class _:_L__9{}'''
        expect = '''Program([ClassDecl(Id(_),Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(_),ArrayType(95,ArrayType(474,BoolType))),param(Id(u75),ClassType(Id(i))),param(Id(m_6),FloatType),param(Id(__),FloatType),param(Id(D),FloatType)],Block([],[]))]),ClassDecl(Id(_),Id(_L__9),[])])'''
        self.assertTrue(TestAST.test(line, expect, 771))

    def test_772(self):
        line = '''Class _{Constructor (_:Float ){} }Class U:T{Constructor (){} }'''
        expect = '''Program([ClassDecl(Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(_),FloatType)],Block([],[]))]),ClassDecl(Id(U),Id(T),[MethodDecl(Id(Constructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 772))

    def test_773(self):
        line = '''Class gCQ0_d{}Class ___e:z{Constructor (){}_1(I___:Array [String ,0134]){}Var $89:sK;}Class p:_WN__{}'''
        expect = '''Program([ClassDecl(Id(gCQ0_d),[]),ClassDecl(Id(___e),Id(z),[MethodDecl(Id(Constructor),Instance,[],Block([],[])),MethodDecl(Id(_1),Instance,[param(Id(I___),ArrayType(92,StringType))],Block([],[])),AttributeDecl(Static,VarDecl(Id($89),ClassType(Id(sK))))]),ClassDecl(Id(p),Id(_WN__),[])])'''
        self.assertTrue(TestAST.test(line, expect, 773))

    def test_774(self):
        line = '''Class _K:_4f{Destructor (){Continue ;} }Class _:__BbZC{}'''
        expect = '''Program([ClassDecl(Id(_K),Id(_4f),[MethodDecl(Id(Destructor),Instance,[],Block([],[Continue]))]),ClassDecl(Id(_),Id(__BbZC),[])])'''
        self.assertTrue(TestAST.test(line, expect, 774))

    def test_775(self):
        line = '''Class _P__{Var _,_m_:Boolean ;Var b_:Array [Array [String ,0b100111],035];}'''
        expect = '''Program([ClassDecl(Id(_P__),[AttributeDecl(Instance,VarDecl(Id(_),BoolType)),AttributeDecl(Instance,VarDecl(Id(_m_),BoolType)),AttributeDecl(Instance,VarDecl(Id(b_),ArrayType(29,ArrayType(39,StringType))))])])'''
        self.assertTrue(TestAST.test(line, expect, 775))

    def test_776(self):
        line = '''Class ___6:_{Destructor (){Continue ;} }Class K{_(_w,_,l,i,v6s:Array [Array [Float ,04],0B1000100];_,W:_){} }'''
        expect = '''Program([ClassDecl(Id(___6),Id(_),[MethodDecl(Id(Destructor),Instance,[],Block([],[Continue]))]),ClassDecl(Id(K),[MethodDecl(Id(_),Instance,[param(Id(_w),ArrayType(68,ArrayType(4,FloatType))),param(Id(_),ArrayType(68,ArrayType(4,FloatType))),param(Id(l),ArrayType(68,ArrayType(4,FloatType))),param(Id(i),ArrayType(68,ArrayType(4,FloatType))),param(Id(v6s),ArrayType(68,ArrayType(4,FloatType))),param(Id(_),ClassType(Id(_))),param(Id(W),ClassType(Id(_)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 776))

    def test_777(self):
        line = '''Class _:_z_{Destructor (){}Constructor (th12:P){}Constructor (){} }Class nz4:z{}'''
        expect = '''Program([ClassDecl(Id(_),Id(_z_),[MethodDecl(Id(Destructor),Instance,[],Block([],[])),MethodDecl(Id(Constructor),Instance,[param(Id(th12),ClassType(Id(P)))],Block([],[])),MethodDecl(Id(Constructor),Instance,[],Block([],[]))]),ClassDecl(Id(nz4),Id(z),[])])'''
        self.assertTrue(TestAST.test(line, expect, 777))

    def test_778(self):
        line = '''Class _{Var $I,zf,$5,$08:Float ;Constructor (_d,M,_:Array [Array [Boolean ,0B1],0136]){} }'''
        expect = '''Program([ClassDecl(Id(_),[AttributeDecl(Static,VarDecl(Id($I),FloatType)),AttributeDecl(Instance,VarDecl(Id(zf),FloatType)),AttributeDecl(Static,VarDecl(Id($5),FloatType)),AttributeDecl(Static,VarDecl(Id($08),FloatType)),MethodDecl(Id(Constructor),Instance,[param(Id(_d),ArrayType(94,ArrayType(1,BoolType))),param(Id(M),ArrayType(94,ArrayType(1,BoolType))),param(Id(_),ArrayType(94,ArrayType(1,BoolType)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 778))

    def test_779(self):
        line = '''Class _{}Class __{}Class V:S_{}Class h_u6:_24_{Constructor (){} }Class _{}'''
        expect = '''Program([ClassDecl(Id(_),[]),ClassDecl(Id(__),[]),ClassDecl(Id(V),Id(S_),[]),ClassDecl(Id(h_u6),Id(_24_),[MethodDecl(Id(Constructor),Instance,[],Block([],[]))]),ClassDecl(Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 779))

    def test_780(self):
        line = '''Class T{$S_42JD(W:Float ;jF:Float ;_:Array [Int ,29];__L,e:h;c,_7_:Array [Int ,29];G:String ;M93:Boolean ){ {} }}'''
        expect = '''Program([ClassDecl(Id(T),[MethodDecl(Id($S_42JD),Static,[param(Id(W),FloatType),param(Id(jF),FloatType),param(Id(_),ArrayType(29,IntType)),param(Id(__L),ClassType(Id(h))),param(Id(e),ClassType(Id(h))),param(Id(c),ArrayType(29,IntType)),param(Id(_7_),ArrayType(29,IntType)),param(Id(G),StringType),param(Id(M93),BoolType)],Block([],[Block([],[])]))])])'''
        self.assertTrue(TestAST.test(line, expect, 780))

    def test_781(self):
        line = '''Class _{}Class _cQ0{}Class _:_{$K(){}Constructor (kEg_:Array [String ,0b1];G:Array [Array [Int ,0X4B],1];_7_vex1l5,i__n,o,A8,__,_,_:_;OE:Array [String ,0X4B]){}Var $1w_L,$_3X:_;}'''
        expect = '''Program([ClassDecl(Id(_),[]),ClassDecl(Id(_cQ0),[]),ClassDecl(Id(_),Id(_),[MethodDecl(Id($K),Static,[],Block([],[])),MethodDecl(Id(Constructor),Instance,[param(Id(kEg_),ArrayType(1,StringType)),param(Id(G),ArrayType(1,ArrayType(75,IntType))),param(Id(_7_vex1l5),ClassType(Id(_))),param(Id(i__n),ClassType(Id(_))),param(Id(o),ClassType(Id(_))),param(Id(A8),ClassType(Id(_))),param(Id(__),ClassType(Id(_))),param(Id(_),ClassType(Id(_))),param(Id(_),ClassType(Id(_))),param(Id(OE),ArrayType(75,StringType))],Block([],[])),AttributeDecl(Static,VarDecl(Id($1w_L),ClassType(Id(_)))),AttributeDecl(Static,VarDecl(Id($_3X),ClassType(Id(_))))])])'''
        self.assertTrue(TestAST.test(line, expect, 781))

    def test_782(self):
        line = '''Class _:_{}Class _:E0_{Constructor (_D:Boolean ;d,_:Array [Array [Array [Array [Array [Array [String ,12],0xD],0B1000100],04_3],076],076]){} }Class d:_{}'''
        expect = '''Program([ClassDecl(Id(_),Id(_),[]),ClassDecl(Id(_),Id(E0_),[MethodDecl(Id(Constructor),Instance,[param(Id(_D),BoolType),param(Id(d),ArrayType(62,ArrayType(62,ArrayType(35,ArrayType(68,ArrayType(13,ArrayType(12,StringType))))))),param(Id(_),ArrayType(62,ArrayType(62,ArrayType(35,ArrayType(68,ArrayType(13,ArrayType(12,StringType)))))))],Block([],[]))]),ClassDecl(Id(d),Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 782))

    def test_783(self):
        line = '''Class _:XKb_g3{_30(c:Int ){} }Class T7:f_ke4{}Class _:_3{}'''
        expect = '''Program([ClassDecl(Id(_),Id(XKb_g3),[MethodDecl(Id(_30),Instance,[param(Id(c),IntType)],Block([],[]))]),ClassDecl(Id(T7),Id(f_ke4),[]),ClassDecl(Id(_),Id(_3),[])])'''
        self.assertTrue(TestAST.test(line, expect, 783))

    def test_784(self):
        line = '''Class __:Z{}Class K4:m{}Class S19{__(){Var p:__;} }Class _:d5{Destructor (){} }Class _:_{}Class _E7MS5_K{Constructor (__:Mr;_:Q;LK,e,__,_9,_1F_,__Ap:_){} }'''
        expect = '''Program([ClassDecl(Id(__),Id(Z),[]),ClassDecl(Id(K4),Id(m),[]),ClassDecl(Id(S19),[MethodDecl(Id(__),Instance,[],Block([VarDecl(Id(p),ClassType(Id(__)))],[]))]),ClassDecl(Id(_),Id(d5),[MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(_),Id(_),[]),ClassDecl(Id(_E7MS5_K),[MethodDecl(Id(Constructor),Instance,[param(Id(__),ClassType(Id(Mr))),param(Id(_),ClassType(Id(Q))),param(Id(LK),ClassType(Id(_))),param(Id(e),ClassType(Id(_))),param(Id(__),ClassType(Id(_))),param(Id(_9),ClassType(Id(_))),param(Id(_1F_),ClassType(Id(_))),param(Id(__Ap),ClassType(Id(_)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 784))

    def test_785(self):
        line = '''Class _:_42{}Class _:__{_(T,mb37_:_N4;_Ut:Array [Array [Array [Float ,0b1_1],0b1],5]){} }Class _G_M_:_{}'''
        expect = '''Program([ClassDecl(Id(_),Id(_42),[]),ClassDecl(Id(_),Id(__),[MethodDecl(Id(_),Instance,[param(Id(T),ClassType(Id(_N4))),param(Id(mb37_),ClassType(Id(_N4))),param(Id(_Ut),ArrayType(5,ArrayType(1,ArrayType(3,FloatType))))],Block([],[]))]),ClassDecl(Id(_G_M_),Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 785))

    def test_786(self):
        line = '''Class op:_6_c_{}Class ____4_{}Class _3{}Class u:H7{Constructor (r,_,_:Boolean ){}Constructor (){} }'''
        expect = '''Program([ClassDecl(Id(op),Id(_6_c_),[]),ClassDecl(Id(____4_),[]),ClassDecl(Id(_3),[]),ClassDecl(Id(u),Id(H7),[MethodDecl(Id(Constructor),Instance,[param(Id(r),BoolType),param(Id(_),BoolType),param(Id(_),BoolType)],Block([],[])),MethodDecl(Id(Constructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 786))

    def test_787(self):
        line = '''Class Z:zpw_{}Class y{}Class ___h_6P_:_{Var $7P,m:Array [Array [Array [Int ,9],9],06];}Class _9:_Q8_6C{}'''
        expect = '''Program([ClassDecl(Id(Z),Id(zpw_),[]),ClassDecl(Id(y),[]),ClassDecl(Id(___h_6P_),Id(_),[AttributeDecl(Static,VarDecl(Id($7P),ArrayType(6,ArrayType(9,ArrayType(9,IntType))))),AttributeDecl(Instance,VarDecl(Id(m),ArrayType(6,ArrayType(9,ArrayType(9,IntType)))))]),ClassDecl(Id(_9),Id(_Q8_6C),[])])'''
        self.assertTrue(TestAST.test(line, expect, 787))

    def test_788(self):
        line = '''Class Su8x3:Q{$9(____,_:Array [Array [Array [Array [Int ,057],0X63],02],057];__,GT2_,_04,n,_b,__,B_b19,__6CU,C4:Array [String ,06];D:Int ){} }Class _:A{}'''
        expect = '''Program([ClassDecl(Id(Su8x3),Id(Q),[MethodDecl(Id($9),Static,[param(Id(____),ArrayType(47,ArrayType(2,ArrayType(99,ArrayType(47,IntType))))),param(Id(_),ArrayType(47,ArrayType(2,ArrayType(99,ArrayType(47,IntType))))),param(Id(__),ArrayType(6,StringType)),param(Id(GT2_),ArrayType(6,StringType)),param(Id(_04),ArrayType(6,StringType)),param(Id(n),ArrayType(6,StringType)),param(Id(_b),ArrayType(6,StringType)),param(Id(__),ArrayType(6,StringType)),param(Id(B_b19),ArrayType(6,StringType)),param(Id(__6CU),ArrayType(6,StringType)),param(Id(C4),ArrayType(6,StringType)),param(Id(D),IntType)],Block([],[]))]),ClassDecl(Id(_),Id(A),[])])'''
        self.assertTrue(TestAST.test(line, expect, 788))

    def test_789(self):
        line = '''Class j8:n{}Class n:_{Destructor (){}Destructor (){} }Class ___:_{}Class __f:g7{}'''
        expect = '''Program([ClassDecl(Id(j8),Id(n),[]),ClassDecl(Id(n),Id(_),[MethodDecl(Id(Destructor),Instance,[],Block([],[])),MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(___),Id(_),[]),ClassDecl(Id(__f),Id(g7),[])])'''
        self.assertTrue(TestAST.test(line, expect, 789))

    def test_790(self):
        line = '''Class _:O{Constructor (){Continue ;} }Class _{Destructor (){} }Class _{}'''
        expect = '''Program([ClassDecl(Id(_),Id(O),[MethodDecl(Id(Constructor),Instance,[],Block([],[Continue]))]),ClassDecl(Id(_),[MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 790))

    def test_791(self):
        line = '''Class L:_3ZN{}Class _{Constructor (e,m_3:Array [Boolean ,0xE]){} }'''
        expect = '''Program([ClassDecl(Id(L),Id(_3ZN),[]),ClassDecl(Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(e),ArrayType(14,BoolType)),param(Id(m_3),ArrayType(14,BoolType))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 791))

    def test_792(self):
        line = '''Class A{Constructor (C:_2h7){ {} }}Class _M{}Class _7_SG{}Class V_:O{}'''
        expect = '''Program([ClassDecl(Id(A),[MethodDecl(Id(Constructor),Instance,[param(Id(C),ClassType(Id(_2h7)))],Block([],[Block([],[])]))]),ClassDecl(Id(_M),[]),ClassDecl(Id(_7_SG),[]),ClassDecl(Id(V_),Id(O),[])])'''
        self.assertTrue(TestAST.test(line, expect, 792))

    def test_793(self):
        line = '''Class Pd__:H_4R9{Constructor (__,_,c:_;___3sE8,z,_,_:Array [Array [Boolean ,0x22],0X4]){} }Class bS:B{$F7(){Continue ;}Constructor (_,w,h_:Y_K_;r,_,a0:Boolean ;Z,u,_7hP1:Array [String ,03_0_5_1];v:String ;_,SbYD,_9:Array [Array [Float ,0B1001000],9];P,_,_:String ;rb,_:Array [String ,062]){}__(_:Array [Array [Array [Float ,070],0x22],070];_,L7,v:Array [Array [Boolean ,0b1001110],0B1001000]){ {Continue ;} }}Class T:o{}'''
        expect = '''Program([ClassDecl(Id(Pd__),Id(H_4R9),[MethodDecl(Id(Constructor),Instance,[param(Id(__),ClassType(Id(_))),param(Id(_),ClassType(Id(_))),param(Id(c),ClassType(Id(_))),param(Id(___3sE8),ArrayType(4,ArrayType(34,BoolType))),param(Id(z),ArrayType(4,ArrayType(34,BoolType))),param(Id(_),ArrayType(4,ArrayType(34,BoolType))),param(Id(_),ArrayType(4,ArrayType(34,BoolType)))],Block([],[]))]),ClassDecl(Id(bS),Id(B),[MethodDecl(Id($F7),Static,[],Block([],[Continue])),MethodDecl(Id(Constructor),Instance,[param(Id(_),ClassType(Id(Y_K_))),param(Id(w),ClassType(Id(Y_K_))),param(Id(h_),ClassType(Id(Y_K_))),param(Id(r),BoolType),param(Id(_),BoolType),param(Id(a0),BoolType),param(Id(Z),ArrayType(1577,StringType)),param(Id(u),ArrayType(1577,StringType)),param(Id(_7hP1),ArrayType(1577,StringType)),param(Id(v),StringType),param(Id(_),ArrayType(9,ArrayType(72,FloatType))),param(Id(SbYD),ArrayType(9,ArrayType(72,FloatType))),param(Id(_9),ArrayType(9,ArrayType(72,FloatType))),param(Id(P),StringType),param(Id(_),StringType),param(Id(_),StringType),param(Id(rb),ArrayType(50,StringType)),param(Id(_),ArrayType(50,StringType))],Block([],[])),MethodDecl(Id(__),Instance,[param(Id(_),ArrayType(56,ArrayType(34,ArrayType(56,FloatType)))),param(Id(_),ArrayType(72,ArrayType(78,BoolType))),param(Id(L7),ArrayType(72,ArrayType(78,BoolType))),param(Id(v),ArrayType(72,ArrayType(78,BoolType)))],Block([],[Block([],[Continue])]))]),ClassDecl(Id(T),Id(o),[])])'''
        self.assertTrue(TestAST.test(line, expect, 793))

    def test_794(self):
        line = '''Class SM0X9_h__{Constructor (_,__:Boolean ){}Constructor (y:String ){} }'''
        expect = '''Program([ClassDecl(Id(SM0X9_h__),[MethodDecl(Id(Constructor),Instance,[param(Id(_),BoolType),param(Id(__),BoolType)],Block([],[])),MethodDecl(Id(Constructor),Instance,[param(Id(y),StringType)],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 794))

    def test_795(self):
        line = '''Class _{}Class _C:l3T_{}Class R:qK{Destructor (){} }Class D_{}'''
        expect = '''Program([ClassDecl(Id(_),[]),ClassDecl(Id(_C),Id(l3T_),[]),ClassDecl(Id(R),Id(qK),[MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(D_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 795))

    def test_796(self):
        line = '''Class k:h2{Constructor (_,_:String ;n__,g_2,f,o9:Array [Boolean ,6_1874]){ {} }}Class Ae{}'''
        expect = '''Program([ClassDecl(Id(k),Id(h2),[MethodDecl(Id(Constructor),Instance,[param(Id(_),StringType),param(Id(_),StringType),param(Id(n__),ArrayType(61874,BoolType)),param(Id(g_2),ArrayType(61874,BoolType)),param(Id(f),ArrayType(61874,BoolType)),param(Id(o9),ArrayType(61874,BoolType))],Block([],[Block([],[])]))]),ClassDecl(Id(Ae),[])])'''
        self.assertTrue(TestAST.test(line, expect, 796))

    def test_797(self):
        line = '''Class Y:d{}Class t9_{Constructor (_m,_,_:Boolean ;_d,b:_1){}$_S(jP:Array [String ,27];__6:Array [Float ,0B100000];_,J35_,D823,__,_:Array [String ,0XF];_,S:Int ){Continue ;} }Class jLB{}'''
        expect = '''Program([ClassDecl(Id(Y),Id(d),[]),ClassDecl(Id(t9_),[MethodDecl(Id(Constructor),Instance,[param(Id(_m),BoolType),param(Id(_),BoolType),param(Id(_),BoolType),param(Id(_d),ClassType(Id(_1))),param(Id(b),ClassType(Id(_1)))],Block([],[])),MethodDecl(Id($_S),Static,[param(Id(jP),ArrayType(27,StringType)),param(Id(__6),ArrayType(32,FloatType)),param(Id(_),ArrayType(15,StringType)),param(Id(J35_),ArrayType(15,StringType)),param(Id(D823),ArrayType(15,StringType)),param(Id(__),ArrayType(15,StringType)),param(Id(_),ArrayType(15,StringType)),param(Id(_),IntType),param(Id(S),IntType)],Block([],[Continue]))]),ClassDecl(Id(jLB),[])])'''
        self.assertTrue(TestAST.test(line, expect, 797))

    def test_798(self):
        line = '''Class _:t{}Class _{Destructor (){ {} }}Class xR:w{}Class __n5:a{}'''
        expect = '''Program([ClassDecl(Id(_),Id(t),[]),ClassDecl(Id(_),[MethodDecl(Id(Destructor),Instance,[],Block([],[Block([],[])]))]),ClassDecl(Id(xR),Id(w),[]),ClassDecl(Id(__n5),Id(a),[])])'''
        self.assertTrue(TestAST.test(line, expect, 798))

    def test_799(self):
        line = '''Class kl{Var $E:Array [Array [Float ,0X6_1],04];}Class H:C{}'''
        expect = '''Program([ClassDecl(Id(kl),[AttributeDecl(Static,VarDecl(Id($E),ArrayType(4,ArrayType(97,FloatType))))]),ClassDecl(Id(H),Id(C),[])])'''
        self.assertTrue(TestAST.test(line, expect, 799))

    def test_800(self):
        line = '''Class _:_{}Class __0:a65{}Class _o634e:_8{Var G:Array [Boolean ,76];}Class _{Var _,O,$6,$58:Float ;}'''
        expect = '''Program([ClassDecl(Id(_),Id(_),[]),ClassDecl(Id(__0),Id(a65),[]),ClassDecl(Id(_o634e),Id(_8),[AttributeDecl(Instance,VarDecl(Id(G),ArrayType(76,BoolType)))]),ClassDecl(Id(_),[AttributeDecl(Instance,VarDecl(Id(_),FloatType)),AttributeDecl(Instance,VarDecl(Id(O),FloatType)),AttributeDecl(Static,VarDecl(Id($6),FloatType)),AttributeDecl(Static,VarDecl(Id($58),FloatType))])])'''
        self.assertTrue(TestAST.test(line, expect, 800))

    def test_801(self):
        line = '''Class QC:_{}Class E:hv9_{Destructor (){ {} }}Class f:_{}Class y{Constructor (_4c,_:Array [Array [String ,0X5],0xD_8]){Return ;} }Class Y:_{}'''
        expect = '''Program([ClassDecl(Id(QC),Id(_),[]),ClassDecl(Id(E),Id(hv9_),[MethodDecl(Id(Destructor),Instance,[],Block([],[Block([],[])]))]),ClassDecl(Id(f),Id(_),[]),ClassDecl(Id(y),[MethodDecl(Id(Constructor),Instance,[param(Id(_4c),ArrayType(216,ArrayType(5,StringType))),param(Id(_),ArrayType(216,ArrayType(5,StringType)))],Block([],[Return(None)]))]),ClassDecl(Id(Y),Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 801))

    def test_802(self):
        line = '''Class K:_{}Class __:t{Var $i:Array [Array [Array [Float ,041_6],03],0B1];}'''
        expect = '''Program([ClassDecl(Id(K),Id(_),[]),ClassDecl(Id(__),Id(t),[AttributeDecl(Static,VarDecl(Id($i),ArrayType(1,ArrayType(3,ArrayType(270,FloatType)))))])])'''
        self.assertTrue(TestAST.test(line, expect, 802))

    def test_803(self):
        line = '''Class z{$0(_,_14,X95_:lgM_5;_,_9:_;_2:_;B_I,__:x){}Var P,$y,_:tj_;}'''
        expect = '''Program([ClassDecl(Id(z),[MethodDecl(Id($0),Static,[param(Id(_),ClassType(Id(lgM_5))),param(Id(_14),ClassType(Id(lgM_5))),param(Id(X95_),ClassType(Id(lgM_5))),param(Id(_),ClassType(Id(_))),param(Id(_9),ClassType(Id(_))),param(Id(_2),ClassType(Id(_))),param(Id(B_I),ClassType(Id(x))),param(Id(__),ClassType(Id(x)))],Block([],[])),AttributeDecl(Instance,VarDecl(Id(P),ClassType(Id(tj_)))),AttributeDecl(Static,VarDecl(Id($y),ClassType(Id(tj_)))),AttributeDecl(Instance,VarDecl(Id(_),ClassType(Id(tj_))))])])'''
        self.assertTrue(TestAST.test(line, expect, 803))

    def test_804(self):
        line = '''Class _:_{}Class __{}Class _{}Class __:eF2{}Class wBb{}Class __:I9{}'''
        expect = '''Program([ClassDecl(Id(_),Id(_),[]),ClassDecl(Id(__),[]),ClassDecl(Id(_),[]),ClassDecl(Id(__),Id(eF2),[]),ClassDecl(Id(wBb),[]),ClassDecl(Id(__),Id(I9),[])])'''
        self.assertTrue(TestAST.test(line, expect, 804))

    def test_805(self):
        line = '''Class _7{}Class _o2m_4{}Class ew:_{$s(__8,R6,_y,H:R;_w,_r0__W,n_:A6B){}_(t_q:Int ;_:Array [Array [Array [Array [Float ,0b1_01],035],44],02]){}Constructor (){} }Class I__:veN_j7{}Class _:Fl8Lv_{}'''
        expect = '''Program([ClassDecl(Id(_7),[]),ClassDecl(Id(_o2m_4),[]),ClassDecl(Id(ew),Id(_),[MethodDecl(Id($s),Static,[param(Id(__8),ClassType(Id(R))),param(Id(R6),ClassType(Id(R))),param(Id(_y),ClassType(Id(R))),param(Id(H),ClassType(Id(R))),param(Id(_w),ClassType(Id(A6B))),param(Id(_r0__W),ClassType(Id(A6B))),param(Id(n_),ClassType(Id(A6B)))],Block([],[])),MethodDecl(Id(_),Instance,[param(Id(t_q),IntType),param(Id(_),ArrayType(2,ArrayType(44,ArrayType(29,ArrayType(5,FloatType)))))],Block([],[])),MethodDecl(Id(Constructor),Instance,[],Block([],[]))]),ClassDecl(Id(I__),Id(veN_j7),[]),ClassDecl(Id(_),Id(Fl8Lv_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 805))

    def test_806(self):
        line = '''Class _6jV:_{}Class _8s:_LvZPa_3{Destructor (){Var m_:Array [Float ,0b11];}Constructor (){}Constructor (K,b1_7:_9;q:String ){} }'''
        expect = '''Program([ClassDecl(Id(_6jV),Id(_),[]),ClassDecl(Id(_8s),Id(_LvZPa_3),[MethodDecl(Id(Destructor),Instance,[],Block([VarDecl(Id(m_),ArrayType(3,FloatType))],[])),MethodDecl(Id(Constructor),Instance,[],Block([],[])),MethodDecl(Id(Constructor),Instance,[param(Id(K),ClassType(Id(_9))),param(Id(b1_7),ClassType(Id(_9))),param(Id(q),StringType)],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 806))

    def test_807(self):
        line = '''Class O:_{}Class k0:c_7{Constructor (_,yQ,g_h___:R4;D:String ;v,w5PQ,_5:_d_){}P5G_(){} }'''
        expect = '''Program([ClassDecl(Id(O),Id(_),[]),ClassDecl(Id(k0),Id(c_7),[MethodDecl(Id(Constructor),Instance,[param(Id(_),ClassType(Id(R4))),param(Id(yQ),ClassType(Id(R4))),param(Id(g_h___),ClassType(Id(R4))),param(Id(D),StringType),param(Id(v),ClassType(Id(_d_))),param(Id(w5PQ),ClassType(Id(_d_))),param(Id(_5),ClassType(Id(_d_)))],Block([],[])),MethodDecl(Id(P5G_),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 807))

    def test_808(self):
        line = '''Class _O__{Var $f35_:Array [Array [Boolean ,061],44];Constructor (){_::$5_06wx60();} }'''
        expect = '''Program([ClassDecl(Id(_O__),[AttributeDecl(Static,VarDecl(Id($f35_),ArrayType(44,ArrayType(49,BoolType)))),MethodDecl(Id(Constructor),Instance,[],Block([],[Call(Id(_),Id($5_06wx60),[])]))])])'''
        self.assertTrue(TestAST.test(line, expect, 808))

    def test_809(self):
        line = '''Class k:E_5{Constructor (PvF_4_:Boolean ;jvm:Array [Array [Array [Array [Array [Float ,828],52],0b110011],0x2B],3];_aP:Array [Array [Int ,52],07];_:String ){} }Class l:_{}'''
        expect = '''Program([ClassDecl(Id(k),Id(E_5),[MethodDecl(Id(Constructor),Instance,[param(Id(PvF_4_),BoolType),param(Id(jvm),ArrayType(3,ArrayType(43,ArrayType(51,ArrayType(52,ArrayType(828,FloatType)))))),param(Id(_aP),ArrayType(7,ArrayType(52,IntType))),param(Id(_),StringType)],Block([],[]))]),ClassDecl(Id(l),Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 809))

    def test_810(self):
        line = '''Class ct:V{Var _:Array [Array [Boolean ,0156_46],027];Var $6:Boolean ;}Class __{}Class _z{Destructor (){} }'''
        expect = '''Program([ClassDecl(Id(ct),Id(V),[AttributeDecl(Instance,VarDecl(Id(_),ArrayType(23,ArrayType(7078,BoolType)))),AttributeDecl(Static,VarDecl(Id($6),BoolType))]),ClassDecl(Id(__),[]),ClassDecl(Id(_z),[MethodDecl(Id(Destructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 810))

    def test_811(self):
        line = '''Class i_{OM_m_(){} }Class T:m{}Class Wc{Constructor (){}U5(){Continue ;} }'''
        expect = '''Program([ClassDecl(Id(i_),[MethodDecl(Id(OM_m_),Instance,[],Block([],[]))]),ClassDecl(Id(T),Id(m),[]),ClassDecl(Id(Wc),[MethodDecl(Id(Constructor),Instance,[],Block([],[])),MethodDecl(Id(U5),Instance,[],Block([],[Continue]))])])'''
        self.assertTrue(TestAST.test(line, expect, 811))

    def test_812(self):
        line = '''Class l73e_:_{}Class S5_g8{}Class e{i(_8D,_:Array [Int ,0x44];y4,G_H:Boolean ;U0,_,__,_C:Int ;__55g,V,X8k4:Array [Array [Array [Boolean ,67],0x44],0x44];_:Boolean ){} }'''
        expect = '''Program([ClassDecl(Id(l73e_),Id(_),[]),ClassDecl(Id(S5_g8),[]),ClassDecl(Id(e),[MethodDecl(Id(i),Instance,[param(Id(_8D),ArrayType(68,IntType)),param(Id(_),ArrayType(68,IntType)),param(Id(y4),BoolType),param(Id(G_H),BoolType),param(Id(U0),IntType),param(Id(_),IntType),param(Id(__),IntType),param(Id(_C),IntType),param(Id(__55g),ArrayType(68,ArrayType(68,ArrayType(67,BoolType)))),param(Id(V),ArrayType(68,ArrayType(68,ArrayType(67,BoolType)))),param(Id(X8k4),ArrayType(68,ArrayType(68,ArrayType(67,BoolType)))),param(Id(_),BoolType)],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 812))

    def test_813(self):
        line = '''Class VK:_{_(){} }Class _:_e_{}Class _{Constructor (){}Var _:_;}'''
        expect = '''Program([ClassDecl(Id(VK),Id(_),[MethodDecl(Id(_),Instance,[],Block([],[]))]),ClassDecl(Id(_),Id(_e_),[]),ClassDecl(Id(_),[MethodDecl(Id(Constructor),Instance,[],Block([],[])),AttributeDecl(Instance,VarDecl(Id(_),ClassType(Id(_))))])])'''
        self.assertTrue(TestAST.test(line, expect, 813))

    def test_814(self):
        line = '''Class E{}Class p{}Class Mx:S{}Class w:__1{}Class _{}Class b5:Q_{}'''
        expect = '''Program([ClassDecl(Id(E),[]),ClassDecl(Id(p),[]),ClassDecl(Id(Mx),Id(S),[]),ClassDecl(Id(w),Id(__1),[]),ClassDecl(Id(_),[]),ClassDecl(Id(b5),Id(Q_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 814))

    def test_815(self):
        line = '''Class _:_{S(H,_yy:Array [Array [Float ,070],9_4_1_0_9];c,H5,_,hP:Array [Int ,070];_,_,SR:Float ;_g:Float ;_,FK:Array [Array [Boolean ,5],66];n,n,j,De0_:_;_:Int ){}$_(){} }'''
        expect = '''Program([ClassDecl(Id(_),Id(_),[MethodDecl(Id(S),Instance,[param(Id(H),ArrayType(94109,ArrayType(56,FloatType))),param(Id(_yy),ArrayType(94109,ArrayType(56,FloatType))),param(Id(c),ArrayType(56,IntType)),param(Id(H5),ArrayType(56,IntType)),param(Id(_),ArrayType(56,IntType)),param(Id(hP),ArrayType(56,IntType)),param(Id(_),FloatType),param(Id(_),FloatType),param(Id(SR),FloatType),param(Id(_g),FloatType),param(Id(_),ArrayType(66,ArrayType(5,BoolType))),param(Id(FK),ArrayType(66,ArrayType(5,BoolType))),param(Id(n),ClassType(Id(_))),param(Id(n),ClassType(Id(_))),param(Id(j),ClassType(Id(_))),param(Id(De0_),ClassType(Id(_))),param(Id(_),IntType)],Block([],[])),MethodDecl(Id($_),Static,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 815))

    def test_816(self):
        line = '''Class y_____{Destructor (){}Var w9,$_,$S:String ;Constructor (kY9_t:e0;_2:w_0_){} }Class s_WU:P{}'''
        expect = '''Program([ClassDecl(Id(y_____),[MethodDecl(Id(Destructor),Instance,[],Block([],[])),AttributeDecl(Instance,VarDecl(Id(w9),StringType)),AttributeDecl(Static,VarDecl(Id($_),StringType)),AttributeDecl(Static,VarDecl(Id($S),StringType)),MethodDecl(Id(Constructor),Instance,[param(Id(kY9_t),ClassType(Id(e0))),param(Id(_2),ClassType(Id(w_0_)))],Block([],[]))]),ClassDecl(Id(s_WU),Id(P),[])])'''
        self.assertTrue(TestAST.test(line, expect, 816))

    def test_817(self):
        line = '''Class G{Destructor (){} }Class _a8{E1(){Return ;} }Class j3{}'''
        expect = '''Program([ClassDecl(Id(G),[MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(_a8),[MethodDecl(Id(E1),Instance,[],Block([],[Return(None)]))]),ClassDecl(Id(j3),[])])'''
        self.assertTrue(TestAST.test(line, expect, 817))

    def test_818(self):
        line = '''Class y__:_{Constructor (ESm,A,p_,_:_R_;_0:String ;_,F,_,__:Int ;e:String ){} }Class _:__{}'''
        expect = '''Program([ClassDecl(Id(y__),Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(ESm),ClassType(Id(_R_))),param(Id(A),ClassType(Id(_R_))),param(Id(p_),ClassType(Id(_R_))),param(Id(_),ClassType(Id(_R_))),param(Id(_0),StringType),param(Id(_),IntType),param(Id(F),IntType),param(Id(_),IntType),param(Id(__),IntType),param(Id(e),StringType)],Block([],[]))]),ClassDecl(Id(_),Id(__),[])])'''
        self.assertTrue(TestAST.test(line, expect, 818))

    def test_819(self):
        line = '''Class Vp{Var $_J:Array [Array [Float ,0B10100],2_5_0];Constructor (){} }'''
        expect = '''Program([ClassDecl(Id(Vp),[AttributeDecl(Static,VarDecl(Id($_J),ArrayType(250,ArrayType(20,FloatType)))),MethodDecl(Id(Constructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 819))

    def test_820(self):
        line = '''Class oc{}Class _:Z93{}Class _:_{Var _r,$1,$_,$99,_,H,_4q,$g,_,$_:_;Var _,_9,$_:Array [Int ,0B10];}'''
        expect = '''Program([ClassDecl(Id(oc),[]),ClassDecl(Id(_),Id(Z93),[]),ClassDecl(Id(_),Id(_),[AttributeDecl(Instance,VarDecl(Id(_r),ClassType(Id(_)))),AttributeDecl(Static,VarDecl(Id($1),ClassType(Id(_)))),AttributeDecl(Static,VarDecl(Id($_),ClassType(Id(_)))),AttributeDecl(Static,VarDecl(Id($99),ClassType(Id(_)))),AttributeDecl(Instance,VarDecl(Id(_),ClassType(Id(_)))),AttributeDecl(Instance,VarDecl(Id(H),ClassType(Id(_)))),AttributeDecl(Instance,VarDecl(Id(_4q),ClassType(Id(_)))),AttributeDecl(Static,VarDecl(Id($g),ClassType(Id(_)))),AttributeDecl(Instance,VarDecl(Id(_),ClassType(Id(_)))),AttributeDecl(Static,VarDecl(Id($_),ClassType(Id(_)))),AttributeDecl(Instance,VarDecl(Id(_),ArrayType(2,IntType))),AttributeDecl(Instance,VarDecl(Id(_9),ArrayType(2,IntType))),AttributeDecl(Static,VarDecl(Id($_),ArrayType(2,IntType)))])])'''
        self.assertTrue(TestAST.test(line, expect, 820))

    def test_821(self):
        line = '''Class S_{Var $1,b:I_;}Class __q:z___{}Class p_:Pq_{}Class q{}'''
        expect = '''Program([ClassDecl(Id(S_),[AttributeDecl(Static,VarDecl(Id($1),ClassType(Id(I_)))),AttributeDecl(Instance,VarDecl(Id(b),ClassType(Id(I_))))]),ClassDecl(Id(__q),Id(z___),[]),ClassDecl(Id(p_),Id(Pq_),[]),ClassDecl(Id(q),[])])'''
        self.assertTrue(TestAST.test(line, expect, 821))

    def test_822(self):
        line = '''Class y6:Q{Var $42,B,_,_,$3:Array [Array [Array [Array [Float ,41],0b1010010],41],0B1001000];}'''
        expect = '''Program([ClassDecl(Id(y6),Id(Q),[AttributeDecl(Static,VarDecl(Id($42),ArrayType(72,ArrayType(41,ArrayType(82,ArrayType(41,FloatType)))))),AttributeDecl(Instance,VarDecl(Id(B),ArrayType(72,ArrayType(41,ArrayType(82,ArrayType(41,FloatType)))))),AttributeDecl(Instance,VarDecl(Id(_),ArrayType(72,ArrayType(41,ArrayType(82,ArrayType(41,FloatType)))))),AttributeDecl(Instance,VarDecl(Id(_),ArrayType(72,ArrayType(41,ArrayType(82,ArrayType(41,FloatType)))))),AttributeDecl(Static,VarDecl(Id($3),ArrayType(72,ArrayType(41,ArrayType(82,ArrayType(41,FloatType))))))])])'''
        self.assertTrue(TestAST.test(line, expect, 822))

    def test_823(self):
        line = '''Class _{Var _,_:Array [Array [Array [String ,0x5D],0X4],0x5D];}'''
        expect = '''Program([ClassDecl(Id(_),[AttributeDecl(Instance,VarDecl(Id(_),ArrayType(93,ArrayType(4,ArrayType(93,StringType))))),AttributeDecl(Instance,VarDecl(Id(_),ArrayType(93,ArrayType(4,ArrayType(93,StringType)))))])])'''
        self.assertTrue(TestAST.test(line, expect, 823))

    def test_824(self):
        line = '''Class ____{Constructor (){}$88(q__:Boolean ;Y1:Int ){} }Class S_{}'''
        expect = '''Program([ClassDecl(Id(____),[MethodDecl(Id(Constructor),Instance,[],Block([],[])),MethodDecl(Id($88),Static,[param(Id(q__),BoolType),param(Id(Y1),IntType)],Block([],[]))]),ClassDecl(Id(S_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 824))

    def test_825(self):
        line = '''Class __:M{}Class T4_8_08__{$D(__,__1:Array [Int ,014];__T,_,_:Boolean ){Break ;}Constructor (_:Array [Array [Array [Boolean ,0B100000],0B1],0x2];_2_2,_pq:_e72){} }'''
        expect = '''Program([ClassDecl(Id(__),Id(M),[]),ClassDecl(Id(T4_8_08__),[MethodDecl(Id($D),Static,[param(Id(__),ArrayType(12,IntType)),param(Id(__1),ArrayType(12,IntType)),param(Id(__T),BoolType),param(Id(_),BoolType),param(Id(_),BoolType)],Block([],[Break])),MethodDecl(Id(Constructor),Instance,[param(Id(_),ArrayType(2,ArrayType(1,ArrayType(32,BoolType)))),param(Id(_2_2),ClassType(Id(_e72))),param(Id(_pq),ClassType(Id(_e72)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 825))

    def test_826(self):
        line = '''Class j_c5im:bv{__Y8_(_5,___:Array [Array [Float ,0B11],047];n,Z,_j:pP6){} }Class K:Y{}'''
        expect = '''Program([ClassDecl(Id(j_c5im),Id(bv),[MethodDecl(Id(__Y8_),Instance,[param(Id(_5),ArrayType(39,ArrayType(3,FloatType))),param(Id(___),ArrayType(39,ArrayType(3,FloatType))),param(Id(n),ClassType(Id(pP6))),param(Id(Z),ClassType(Id(pP6))),param(Id(_j),ClassType(Id(pP6)))],Block([],[]))]),ClassDecl(Id(K),Id(Y),[])])'''
        self.assertTrue(TestAST.test(line, expect, 826))

    def test_827(self):
        line = '''Class y___56{}Class _:i{}Class A{Destructor (){} }Class N{}'''
        expect = '''Program([ClassDecl(Id(y___56),[]),ClassDecl(Id(_),Id(i),[]),ClassDecl(Id(A),[MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(N),[])])'''
        self.assertTrue(TestAST.test(line, expect, 827))

    def test_828(self):
        line = '''Class _:L11_{}Class g{$9_(_c1,_4u:_;_w_:w){}Destructor (){} }Class _7:__2{}Class b:_{$u(F_Dl:L3;_k,_w,wT_,p:Array [Array [String ,0110],41];_:Int ;__3w:___27;nuF:Boolean ;R,p:Boolean ){ {} }Var __,$D:String ;Constructor (_:Array [Array [Int ,0x9],77]){} }'''
        expect = '''Program([ClassDecl(Id(_),Id(L11_),[]),ClassDecl(Id(g),[MethodDecl(Id($9_),Static,[param(Id(_c1),ClassType(Id(_))),param(Id(_4u),ClassType(Id(_))),param(Id(_w_),ClassType(Id(w)))],Block([],[])),MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(_7),Id(__2),[]),ClassDecl(Id(b),Id(_),[MethodDecl(Id($u),Static,[param(Id(F_Dl),ClassType(Id(L3))),param(Id(_k),ArrayType(41,ArrayType(72,StringType))),param(Id(_w),ArrayType(41,ArrayType(72,StringType))),param(Id(wT_),ArrayType(41,ArrayType(72,StringType))),param(Id(p),ArrayType(41,ArrayType(72,StringType))),param(Id(_),IntType),param(Id(__3w),ClassType(Id(___27))),param(Id(nuF),BoolType),param(Id(R),BoolType),param(Id(p),BoolType)],Block([],[Block([],[])])),AttributeDecl(Instance,VarDecl(Id(__),StringType)),AttributeDecl(Static,VarDecl(Id($D),StringType)),MethodDecl(Id(Constructor),Instance,[param(Id(_),ArrayType(77,ArrayType(9,IntType)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 828))

    def test_829(self):
        line = '''Class H_05{Var _g_I41,_:Boolean ;Destructor (){} }Class _b:__b3{x83(t:Int ;_,_Y28,_:Float ){Break ;} }'''
        expect = '''Program([ClassDecl(Id(H_05),[AttributeDecl(Instance,VarDecl(Id(_g_I41),BoolType)),AttributeDecl(Instance,VarDecl(Id(_),BoolType)),MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(_b),Id(__b3),[MethodDecl(Id(x83),Instance,[param(Id(t),IntType),param(Id(_),FloatType),param(Id(_Y28),FloatType),param(Id(_),FloatType)],Block([],[Break]))])])'''
        self.assertTrue(TestAST.test(line, expect, 829))

    def test_830(self):
        line = '''Class _v__:_n___{Constructor (_,__:Array [Array [Array [Array [Boolean ,0xD],040],4],0xD]){} }'''
        expect = '''Program([ClassDecl(Id(_v__),Id(_n___),[MethodDecl(Id(Constructor),Instance,[param(Id(_),ArrayType(13,ArrayType(4,ArrayType(32,ArrayType(13,BoolType))))),param(Id(__),ArrayType(13,ArrayType(4,ArrayType(32,ArrayType(13,BoolType)))))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 830))

    def test_831(self):
        line = '''Class _{Constructor (){} }Class _q{Var $2p_G4,__,g:String ;}'''
        expect = '''Program([ClassDecl(Id(_),[MethodDecl(Id(Constructor),Instance,[],Block([],[]))]),ClassDecl(Id(_q),[AttributeDecl(Static,VarDecl(Id($2p_G4),StringType)),AttributeDecl(Instance,VarDecl(Id(__),StringType)),AttributeDecl(Instance,VarDecl(Id(g),StringType))])])'''
        self.assertTrue(TestAST.test(line, expect, 831))

    def test_832(self):
        line = '''Class N_:_R{}Class R9J:o7{}Class __97c___N_{}Class S{}Class __{}'''
        expect = '''Program([ClassDecl(Id(N_),Id(_R),[]),ClassDecl(Id(R9J),Id(o7),[]),ClassDecl(Id(__97c___N_),[]),ClassDecl(Id(S),[]),ClassDecl(Id(__),[])])'''
        self.assertTrue(TestAST.test(line, expect, 832))

    def test_833(self):
        line = '''Class _{_8(){}$61(_:Array [Float ,63];O_65:_;_,G5L24_,Y_,_4egG:D;bS:Float ){} }'''
        expect = '''Program([ClassDecl(Id(_),[MethodDecl(Id(_8),Instance,[],Block([],[])),MethodDecl(Id($61),Static,[param(Id(_),ArrayType(63,FloatType)),param(Id(O_65),ClassType(Id(_))),param(Id(_),ClassType(Id(D))),param(Id(G5L24_),ClassType(Id(D))),param(Id(Y_),ClassType(Id(D))),param(Id(_4egG),ClassType(Id(D))),param(Id(bS),FloatType)],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 833))

    def test_834(self):
        line = '''Class _3:B_6_{}Class sN:_{}Class _:__{}Class a3_{}Class n:z{}Class _2{}'''
        expect = '''Program([ClassDecl(Id(_3),Id(B_6_),[]),ClassDecl(Id(sN),Id(_),[]),ClassDecl(Id(_),Id(__),[]),ClassDecl(Id(a3_),[]),ClassDecl(Id(n),Id(z),[]),ClassDecl(Id(_2),[])])'''
        self.assertTrue(TestAST.test(line, expect, 834))

    def test_835(self):
        line = '''Class p16:b_{Constructor (_,d,k_,Y:Array [Float ,06_4]){Continue ;} }Class jn6_{}'''
        expect = '''Program([ClassDecl(Id(p16),Id(b_),[MethodDecl(Id(Constructor),Instance,[param(Id(_),ArrayType(52,FloatType)),param(Id(d),ArrayType(52,FloatType)),param(Id(k_),ArrayType(52,FloatType)),param(Id(Y),ArrayType(52,FloatType))],Block([],[Continue]))]),ClassDecl(Id(jn6_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 835))

    def test_836(self):
        line = '''Class u9u7_:C_{Constructor (){Continue ;Continue ;}_(_,_2P_:Boolean ){Return !!!-----Null ;} }'''
        expect = '''Program([ClassDecl(Id(u9u7_),Id(C_),[MethodDecl(Id(Constructor),Instance,[],Block([],[Continue,Continue])),MethodDecl(Id(_),Instance,[param(Id(_),BoolType),param(Id(_2P_),BoolType)],Block([],[Return(UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,NullLiteral())))))))))]))])])'''
        self.assertTrue(TestAST.test(line, expect, 836))

    def test_837(self):
        line = '''Class _:_d{Var _2,$HTz13,$Fn,j:Float ;$0(){}$_(p:XNut;_,h:String ){} }'''
        expect = '''Program([ClassDecl(Id(_),Id(_d),[AttributeDecl(Instance,VarDecl(Id(_2),FloatType)),AttributeDecl(Static,VarDecl(Id($HTz13),FloatType)),AttributeDecl(Static,VarDecl(Id($Fn),FloatType)),AttributeDecl(Instance,VarDecl(Id(j),FloatType)),MethodDecl(Id($0),Static,[],Block([],[])),MethodDecl(Id($_),Static,[param(Id(p),ClassType(Id(XNut))),param(Id(_),StringType),param(Id(h),StringType)],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 837))

    def test_838(self):
        line = '''Class m:H1{}Class M_l{}Class F{}Class u28:X{Constructor (G__:Array [Float ,62_8]){} }'''
        expect = '''Program([ClassDecl(Id(m),Id(H1),[]),ClassDecl(Id(M_l),[]),ClassDecl(Id(F),[]),ClassDecl(Id(u28),Id(X),[MethodDecl(Id(Constructor),Instance,[param(Id(G__),ArrayType(628,FloatType))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 838))

    def test_839(self):
        line = '''Class i_:_C7P{}Class S:_sy77{Destructor (){} }Class F3:_{}'''
        expect = '''Program([ClassDecl(Id(i_),Id(_C7P),[]),ClassDecl(Id(S),Id(_sy77),[MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(F3),Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 839))

    def test_840(self):
        line = '''Class h{Constructor (L:Int ;_:Array [Int ,0137]){}Constructor (){} }'''
        expect = '''Program([ClassDecl(Id(h),[MethodDecl(Id(Constructor),Instance,[param(Id(L),IntType),param(Id(_),ArrayType(95,IntType))],Block([],[])),MethodDecl(Id(Constructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 840))

    def test_841(self):
        line = '''Class B{}Class __{$h_6_(_,I6:String ;_5,l,v,_:_;___n,d,_:p;_:__1){} }Class _{Var w:Array [String ,02];E(Z,R:_){} }'''
        expect = '''Program([ClassDecl(Id(B),[]),ClassDecl(Id(__),[MethodDecl(Id($h_6_),Static,[param(Id(_),StringType),param(Id(I6),StringType),param(Id(_5),ClassType(Id(_))),param(Id(l),ClassType(Id(_))),param(Id(v),ClassType(Id(_))),param(Id(_),ClassType(Id(_))),param(Id(___n),ClassType(Id(p))),param(Id(d),ClassType(Id(p))),param(Id(_),ClassType(Id(p))),param(Id(_),ClassType(Id(__1)))],Block([],[]))]),ClassDecl(Id(_),[AttributeDecl(Instance,VarDecl(Id(w),ArrayType(2,StringType))),MethodDecl(Id(E),Instance,[param(Id(Z),ClassType(Id(_))),param(Id(R),ClassType(Id(_)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 841))

    def test_842(self):
        line = '''Class e{}Class f__M02{Var $J:Array [Array [String ,74_8],03];}'''
        expect = '''Program([ClassDecl(Id(e),[]),ClassDecl(Id(f__M02),[AttributeDecl(Static,VarDecl(Id($J),ArrayType(3,ArrayType(748,StringType))))])])'''
        self.assertTrue(TestAST.test(line, expect, 842))

    def test_843(self):
        line = '''Class _7:C_{$_(_W,i:Array [Float ,0X18];__76_i,__:_){Break ;}o96kV__l(){}N(_,a:Array [Array [Array [Array [Array [Array [Array [String ,0B10_10_1],035],6_1],0xEB],035],29],0B101100]){}Destructor (){} }'''
        expect = '''Program([ClassDecl(Id(_7),Id(C_),[MethodDecl(Id($_),Static,[param(Id(_W),ArrayType(24,FloatType)),param(Id(i),ArrayType(24,FloatType)),param(Id(__76_i),ClassType(Id(_))),param(Id(__),ClassType(Id(_)))],Block([],[Break])),MethodDecl(Id(o96kV__l),Instance,[],Block([],[])),MethodDecl(Id(N),Instance,[param(Id(_),ArrayType(44,ArrayType(29,ArrayType(29,ArrayType(235,ArrayType(61,ArrayType(29,ArrayType(21,StringType)))))))),param(Id(a),ArrayType(44,ArrayType(29,ArrayType(29,ArrayType(235,ArrayType(61,ArrayType(29,ArrayType(21,StringType))))))))],Block([],[])),MethodDecl(Id(Destructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 843))

    def test_844(self):
        line = '''Class _1{Constructor (__9_,_,W:Array [String ,6];_Ode2_5:Array [String ,0B1];_l:i;c:Array [Int ,0x1]){} }'''
        expect = '''Program([ClassDecl(Id(_1),[MethodDecl(Id(Constructor),Instance,[param(Id(__9_),ArrayType(6,StringType)),param(Id(_),ArrayType(6,StringType)),param(Id(W),ArrayType(6,StringType)),param(Id(_Ode2_5),ArrayType(1,StringType)),param(Id(_l),ClassType(Id(i))),param(Id(c),ArrayType(1,IntType))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 844))

    def test_845(self):
        line = '''Class _{Var $_:Array [Array [Array [Array [String ,0B1000000],0b1000100],070],2_1_4_4];}'''
        expect = '''Program([ClassDecl(Id(_),[AttributeDecl(Static,VarDecl(Id($_),ArrayType(2144,ArrayType(56,ArrayType(68,ArrayType(64,StringType))))))])])'''
        self.assertTrue(TestAST.test(line, expect, 845))

    def test_846(self):
        line = '''Class s7_{}Class CQ{Constructor (){_q_5::$2_();}Var $_,$_:HwV_;}Class _{}'''
        expect = '''Program([ClassDecl(Id(s7_),[]),ClassDecl(Id(CQ),[MethodDecl(Id(Constructor),Instance,[],Block([],[Call(Id(_q_5),Id($2_),[])])),AttributeDecl(Static,VarDecl(Id($_),ClassType(Id(HwV_)))),AttributeDecl(Static,VarDecl(Id($_),ClassType(Id(HwV_))))]),ClassDecl(Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 846))

    def test_847(self):
        line = '''Class fN4_:_6{$4_O29(L,V__1:Array [Int ,4]){Continue ;} }'''
        expect = '''Program([ClassDecl(Id(fN4_),Id(_6),[MethodDecl(Id($4_O29),Static,[param(Id(L),ArrayType(4,IntType)),param(Id(V__1),ArrayType(4,IntType))],Block([],[Continue]))])])'''
        self.assertTrue(TestAST.test(line, expect, 847))

    def test_848(self):
        line = '''Class k_{Constructor (xC1:Array [Int ,0XD];l:vJ){}_(){Continue ;Return ;Break ;} }'''
        expect = '''Program([ClassDecl(Id(k_),[MethodDecl(Id(Constructor),Instance,[param(Id(xC1),ArrayType(13,IntType)),param(Id(l),ClassType(Id(vJ)))],Block([],[])),MethodDecl(Id(_),Instance,[],Block([],[Continue,Return(None),Break]))])])'''
        self.assertTrue(TestAST.test(line, expect, 848))

    def test_849(self):
        line = '''Class __{}Class X{Var _C,_Z,$__:E;}Class _83_J21:__53{}Class v15_:Z{}'''
        expect = '''Program([ClassDecl(Id(__),[]),ClassDecl(Id(X),[AttributeDecl(Instance,VarDecl(Id(_C),ClassType(Id(E)))),AttributeDecl(Instance,VarDecl(Id(_Z),ClassType(Id(E)))),AttributeDecl(Static,VarDecl(Id($__),ClassType(Id(E))))]),ClassDecl(Id(_83_J21),Id(__53),[]),ClassDecl(Id(v15_),Id(Z),[])])'''
        self.assertTrue(TestAST.test(line, expect, 849))

    def test_850(self):
        line = '''Class _{}Class B{}Class b0{}Class B{}Class n:s{Constructor (H87p0,d:Array [Array [Array [Array [Array [Boolean ,33],33],0x40],0x40],0x3];Z:Int ;AN_,z_Z:V){} }'''
        expect = '''Program([ClassDecl(Id(_),[]),ClassDecl(Id(B),[]),ClassDecl(Id(b0),[]),ClassDecl(Id(B),[]),ClassDecl(Id(n),Id(s),[MethodDecl(Id(Constructor),Instance,[param(Id(H87p0),ArrayType(3,ArrayType(64,ArrayType(64,ArrayType(33,ArrayType(33,BoolType)))))),param(Id(d),ArrayType(3,ArrayType(64,ArrayType(64,ArrayType(33,ArrayType(33,BoolType)))))),param(Id(Z),IntType),param(Id(AN_),ClassType(Id(V))),param(Id(z_Z),ClassType(Id(V)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 850))

    def test_851(self):
        line = '''Class v{H(_,L_,h_d,Ln_:Int ;_r1:Float ){}Constructor (){Continue ;Continue ;} }'''
        expect = '''Program([ClassDecl(Id(v),[MethodDecl(Id(H),Instance,[param(Id(_),IntType),param(Id(L_),IntType),param(Id(h_d),IntType),param(Id(Ln_),IntType),param(Id(_r1),FloatType)],Block([],[])),MethodDecl(Id(Constructor),Instance,[],Block([],[Continue,Continue]))])])'''
        self.assertTrue(TestAST.test(line, expect, 851))

    def test_852(self):
        line = '''Class x{}Class _:l{Y(_:Boolean ){ {} }Destructor (){Continue ;} }Class p:_{}'''
        expect = '''Program([ClassDecl(Id(x),[]),ClassDecl(Id(_),Id(l),[MethodDecl(Id(Y),Instance,[param(Id(_),BoolType)],Block([],[Block([],[])])),MethodDecl(Id(Destructor),Instance,[],Block([],[Continue]))]),ClassDecl(Id(p),Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 852))

    def test_853(self):
        line = '''Class E:UG{Destructor (){Return ;}Constructor (__f_3G8_,_,n1:Array [Array [String ,07],0B1_00_0];l,z6,R,_,_,x:String ){Continue ;} }'''
        expect = '''Program([ClassDecl(Id(E),Id(UG),[MethodDecl(Id(Destructor),Instance,[],Block([],[Return(None)])),MethodDecl(Id(Constructor),Instance,[param(Id(__f_3G8_),ArrayType(8,ArrayType(7,StringType))),param(Id(_),ArrayType(8,ArrayType(7,StringType))),param(Id(n1),ArrayType(8,ArrayType(7,StringType))),param(Id(l),StringType),param(Id(z6),StringType),param(Id(R),StringType),param(Id(_),StringType),param(Id(_),StringType),param(Id(x),StringType)],Block([],[Continue]))])])'''
        self.assertTrue(TestAST.test(line, expect, 853))

    def test_854(self):
        line = '''Class Q:QH8{Constructor (__0RI9N,_Y6_,__:String ;c:_h){} }Class c:_9S_{}Class _u:q{}'''
        expect = '''Program([ClassDecl(Id(Q),Id(QH8),[MethodDecl(Id(Constructor),Instance,[param(Id(__0RI9N),StringType),param(Id(_Y6_),StringType),param(Id(__),StringType),param(Id(c),ClassType(Id(_h)))],Block([],[]))]),ClassDecl(Id(c),Id(_9S_),[]),ClassDecl(Id(_u),Id(q),[])])'''
        self.assertTrue(TestAST.test(line, expect, 854))

    def test_855(self):
        line = '''Class _wQ{$R5(G_5:Array [Array [String ,0B101101],40]){} }Class _{}Class _{Constructor (a8,_,_,_:_){} }'''
        expect = '''Program([ClassDecl(Id(_wQ),[MethodDecl(Id($R5),Static,[param(Id(G_5),ArrayType(40,ArrayType(45,StringType)))],Block([],[]))]),ClassDecl(Id(_),[]),ClassDecl(Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(a8),ClassType(Id(_))),param(Id(_),ClassType(Id(_))),param(Id(_),ClassType(Id(_))),param(Id(_),ClassType(Id(_)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 855))

    def test_856(self):
        line = '''Class h:L{Destructor (){ {Continue ;} }}Class _l6:Lzb5{}Class vq:n_{}Class jvsLp4U___:m{}'''
        expect = '''Program([ClassDecl(Id(h),Id(L),[MethodDecl(Id(Destructor),Instance,[],Block([],[Block([],[Continue])]))]),ClassDecl(Id(_l6),Id(Lzb5),[]),ClassDecl(Id(vq),Id(n_),[]),ClassDecl(Id(jvsLp4U___),Id(m),[])])'''
        self.assertTrue(TestAST.test(line, expect, 856))

    def test_857(self):
        line = '''Class __Z_:_{Var _Yhr:_1_;}Class D:__x4408d{}Class _Ii{}'''
        expect = '''Program([ClassDecl(Id(__Z_),Id(_),[AttributeDecl(Instance,VarDecl(Id(_Yhr),ClassType(Id(_1_))))]),ClassDecl(Id(D),Id(__x4408d),[]),ClassDecl(Id(_Ii),[])])'''
        self.assertTrue(TestAST.test(line, expect, 857))

    def test_858(self):
        line = '''Class Le:_{Constructor (){}Constructor (Q:Boolean ;b2,l__,__:Array [Int ,0B1]){} }'''
        expect = '''Program([ClassDecl(Id(Le),Id(_),[MethodDecl(Id(Constructor),Instance,[],Block([],[])),MethodDecl(Id(Constructor),Instance,[param(Id(Q),BoolType),param(Id(b2),ArrayType(1,IntType)),param(Id(l__),ArrayType(1,IntType)),param(Id(__),ArrayType(1,IntType))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 858))

    def test_859(self):
        line = '''Class _i{Var aB6,$Z3_,L,___:Array [Array [Array [Boolean ,0B1_1],0X11],0b1_1_11];}Class _9:_{}Class r_u{Constructor (){} }Class W{}Class C9R{}'''
        expect = '''Program([ClassDecl(Id(_i),[AttributeDecl(Instance,VarDecl(Id(aB6),ArrayType(15,ArrayType(17,ArrayType(3,BoolType))))),AttributeDecl(Static,VarDecl(Id($Z3_),ArrayType(15,ArrayType(17,ArrayType(3,BoolType))))),AttributeDecl(Instance,VarDecl(Id(L),ArrayType(15,ArrayType(17,ArrayType(3,BoolType))))),AttributeDecl(Instance,VarDecl(Id(___),ArrayType(15,ArrayType(17,ArrayType(3,BoolType)))))]),ClassDecl(Id(_9),Id(_),[]),ClassDecl(Id(r_u),[MethodDecl(Id(Constructor),Instance,[],Block([],[]))]),ClassDecl(Id(W),[]),ClassDecl(Id(C9R),[])])'''
        self.assertTrue(TestAST.test(line, expect, 859))

    def test_860(self):
        line = '''Class _:_{}Class x{Destructor (){Return ;}Destructor (){} }'''
        expect = '''Program([ClassDecl(Id(_),Id(_),[]),ClassDecl(Id(x),[MethodDecl(Id(Destructor),Instance,[],Block([],[Return(None)])),MethodDecl(Id(Destructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 860))

    def test_861(self):
        line = '''Class _{}Class __{}Class F:_09J_{Var $z_:OQ_9__;Destructor (){} }'''
        expect = '''Program([ClassDecl(Id(_),[]),ClassDecl(Id(__),[]),ClassDecl(Id(F),Id(_09J_),[AttributeDecl(Static,VarDecl(Id($z_),ClassType(Id(OQ_9__)))),MethodDecl(Id(Destructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 861))

    def test_862(self):
        line = '''Class _h1:_{Constructor (_,_,_:_;Wx:Int ;uc:Int ){} }Class _:_3{Var _,_26_:_;}'''
        expect = '''Program([ClassDecl(Id(_h1),Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(_),ClassType(Id(_))),param(Id(_),ClassType(Id(_))),param(Id(_),ClassType(Id(_))),param(Id(Wx),IntType),param(Id(uc),IntType)],Block([],[]))]),ClassDecl(Id(_),Id(_3),[AttributeDecl(Instance,VarDecl(Id(_),ClassType(Id(_)))),AttributeDecl(Instance,VarDecl(Id(_26_),ClassType(Id(_))))])])'''
        self.assertTrue(TestAST.test(line, expect, 862))

    def test_863(self):
        line = '''Class a{_5(_:Array [Array [Int ,05_7],24];_GH5QZ:Array [Boolean ,69]){} }'''
        expect = '''Program([ClassDecl(Id(a),[MethodDecl(Id(_5),Instance,[param(Id(_),ArrayType(24,ArrayType(47,IntType))),param(Id(_GH5QZ),ArrayType(69,BoolType))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 863))

    def test_864(self):
        line = '''Class V230_4_{Var Hk_,_,$_6:__n;Constructor (){}Var $__,A:Boolean ;}'''
        expect = '''Program([ClassDecl(Id(V230_4_),[AttributeDecl(Instance,VarDecl(Id(Hk_),ClassType(Id(__n)))),AttributeDecl(Instance,VarDecl(Id(_),ClassType(Id(__n)))),AttributeDecl(Static,VarDecl(Id($_6),ClassType(Id(__n)))),MethodDecl(Id(Constructor),Instance,[],Block([],[])),AttributeDecl(Static,VarDecl(Id($__),BoolType)),AttributeDecl(Instance,VarDecl(Id(A),BoolType))])])'''
        self.assertTrue(TestAST.test(line, expect, 864))

    def test_865(self):
        line = '''Class YwZ56_0{Var $4:String ;Constructor (j:Boolean ){} }Class C8_8_1:g{}'''
        expect = '''Program([ClassDecl(Id(YwZ56_0),[AttributeDecl(Static,VarDecl(Id($4),StringType)),MethodDecl(Id(Constructor),Instance,[param(Id(j),BoolType)],Block([],[]))]),ClassDecl(Id(C8_8_1),Id(g),[])])'''
        self.assertTrue(TestAST.test(line, expect, 865))

    def test_866(self):
        line = '''Class __4{Constructor (U,uC0G_K,_:Array [String ,82];j_G,n_:Float ){} }'''
        expect = '''Program([ClassDecl(Id(__4),[MethodDecl(Id(Constructor),Instance,[param(Id(U),ArrayType(82,StringType)),param(Id(uC0G_K),ArrayType(82,StringType)),param(Id(_),ArrayType(82,StringType)),param(Id(j_G),FloatType),param(Id(n_),FloatType)],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 866))

    def test_867(self):
        line = '''Class N:D_{Z(_a5,_:Array [Float ,4_7];__1:Array [Array [Array [Int ,0b101110],1],0b101110]){} }'''
        expect = '''Program([ClassDecl(Id(N),Id(D_),[MethodDecl(Id(Z),Instance,[param(Id(_a5),ArrayType(47,FloatType)),param(Id(_),ArrayType(47,FloatType)),param(Id(__1),ArrayType(46,ArrayType(1,ArrayType(46,IntType))))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 867))

    def test_868(self):
        line = '''Class f_:_{}Class s{}Class Wp_2{$O_1_(){}Constructor (X3,j1KQ:Array [Array [Array [String ,34],0116],0116]){} }Class _6{}'''
        expect = '''Program([ClassDecl(Id(f_),Id(_),[]),ClassDecl(Id(s),[]),ClassDecl(Id(Wp_2),[MethodDecl(Id($O_1_),Static,[],Block([],[])),MethodDecl(Id(Constructor),Instance,[param(Id(X3),ArrayType(78,ArrayType(78,ArrayType(34,StringType)))),param(Id(j1KQ),ArrayType(78,ArrayType(78,ArrayType(34,StringType))))],Block([],[]))]),ClassDecl(Id(_6),[])])'''
        self.assertTrue(TestAST.test(line, expect, 868))

    def test_869(self):
        line = '''Class f:__C{}Class c:G0_3_{}Class O_9{Var $4,$4,A,$_,d,_,__vH,_c:t3_;}'''
        expect = '''Program([ClassDecl(Id(f),Id(__C),[]),ClassDecl(Id(c),Id(G0_3_),[]),ClassDecl(Id(O_9),[AttributeDecl(Static,VarDecl(Id($4),ClassType(Id(t3_)))),AttributeDecl(Static,VarDecl(Id($4),ClassType(Id(t3_)))),AttributeDecl(Instance,VarDecl(Id(A),ClassType(Id(t3_)))),AttributeDecl(Static,VarDecl(Id($_),ClassType(Id(t3_)))),AttributeDecl(Instance,VarDecl(Id(d),ClassType(Id(t3_)))),AttributeDecl(Instance,VarDecl(Id(_),ClassType(Id(t3_)))),AttributeDecl(Instance,VarDecl(Id(__vH),ClassType(Id(t3_)))),AttributeDecl(Instance,VarDecl(Id(_c),ClassType(Id(t3_))))])])'''
        self.assertTrue(TestAST.test(line, expect, 869))

    def test_870(self):
        line = '''Class _:r{}Class _{U(k,_,l,_,___,h:_;I4k_7e,_:Float ){} }'''
        expect = '''Program([ClassDecl(Id(_),Id(r),[]),ClassDecl(Id(_),[MethodDecl(Id(U),Instance,[param(Id(k),ClassType(Id(_))),param(Id(_),ClassType(Id(_))),param(Id(l),ClassType(Id(_))),param(Id(_),ClassType(Id(_))),param(Id(___),ClassType(Id(_))),param(Id(h),ClassType(Id(_))),param(Id(I4k_7e),FloatType),param(Id(_),FloatType)],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 870))

    def test_871(self):
        line = '''Class _e:_{}Class g{}Class J{Var $oX,$_:Array [Int ,0X30];$__(){} }Class _:K_3{}'''
        expect = '''Program([ClassDecl(Id(_e),Id(_),[]),ClassDecl(Id(g),[]),ClassDecl(Id(J),[AttributeDecl(Static,VarDecl(Id($oX),ArrayType(48,IntType))),AttributeDecl(Static,VarDecl(Id($_),ArrayType(48,IntType))),MethodDecl(Id($__),Static,[],Block([],[]))]),ClassDecl(Id(_),Id(K_3),[])])'''
        self.assertTrue(TestAST.test(line, expect, 871))

    def test_872(self):
        line = '''Class _:_{Var _1,$_g_M,$m8:Array [Array [Array [Int ,0b11],0B101100],041];}'''
        expect = '''Program([ClassDecl(Id(_),Id(_),[AttributeDecl(Instance,VarDecl(Id(_1),ArrayType(33,ArrayType(44,ArrayType(3,IntType))))),AttributeDecl(Static,VarDecl(Id($_g_M),ArrayType(33,ArrayType(44,ArrayType(3,IntType))))),AttributeDecl(Static,VarDecl(Id($m8),ArrayType(33,ArrayType(44,ArrayType(3,IntType)))))])])'''
        self.assertTrue(TestAST.test(line, expect, 872))

    def test_873(self):
        line = '''Class _5:W{$_1_(K:Array [Array [Boolean ,04_7],0B1100001];__,_:Array [Array [Array [Array [String ,0b1],63],1],0X1]){} }'''
        expect = '''Program([ClassDecl(Id(_5),Id(W),[MethodDecl(Id($_1_),Static,[param(Id(K),ArrayType(97,ArrayType(39,BoolType))),param(Id(__),ArrayType(1,ArrayType(1,ArrayType(63,ArrayType(1,StringType))))),param(Id(_),ArrayType(1,ArrayType(1,ArrayType(63,ArrayType(1,StringType)))))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 873))

    def test_874(self):
        line = '''Class __:j_{Var _,q:Array [Array [Float ,0X4_4_A],4_0];}Class _:_D8{}Class cU8{}Class __8sn_{}Class f_{}'''
        expect = '''Program([ClassDecl(Id(__),Id(j_),[AttributeDecl(Instance,VarDecl(Id(_),ArrayType(40,ArrayType(1098,FloatType)))),AttributeDecl(Instance,VarDecl(Id(q),ArrayType(40,ArrayType(1098,FloatType))))]),ClassDecl(Id(_),Id(_D8),[]),ClassDecl(Id(cU8),[]),ClassDecl(Id(__8sn_),[]),ClassDecl(Id(f_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 874))

    def test_875(self):
        line = '''Class _n:i{}Class _{Destructor (){}Destructor (){}$_I(_a:_){} }'''
        expect = '''Program([ClassDecl(Id(_n),Id(i),[]),ClassDecl(Id(_),[MethodDecl(Id(Destructor),Instance,[],Block([],[])),MethodDecl(Id(Destructor),Instance,[],Block([],[])),MethodDecl(Id($_I),Static,[param(Id(_a),ClassType(Id(_)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 875))

    def test_876(self):
        line = '''Class B{}Class ps:B{Var $3,r_1,n:Array [Float ,0B1];}Class _{}Class nNc{$f_W__(__,Bx7:GHQJS_;_:Int ;_g3_,y,V:H;_:Float ){} }'''
        expect = '''Program([ClassDecl(Id(B),[]),ClassDecl(Id(ps),Id(B),[AttributeDecl(Static,VarDecl(Id($3),ArrayType(1,FloatType))),AttributeDecl(Instance,VarDecl(Id(r_1),ArrayType(1,FloatType))),AttributeDecl(Instance,VarDecl(Id(n),ArrayType(1,FloatType)))]),ClassDecl(Id(_),[]),ClassDecl(Id(nNc),[MethodDecl(Id($f_W__),Static,[param(Id(__),ClassType(Id(GHQJS_))),param(Id(Bx7),ClassType(Id(GHQJS_))),param(Id(_),IntType),param(Id(_g3_),ClassType(Id(H))),param(Id(y),ClassType(Id(H))),param(Id(V),ClassType(Id(H))),param(Id(_),FloatType)],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 876))

    def test_877(self):
        line = '''Class R:_o{Destructor (){}Var _:Array [Boolean ,13];Constructor (){} }'''
        expect = '''Program([ClassDecl(Id(R),Id(_o),[MethodDecl(Id(Destructor),Instance,[],Block([],[])),AttributeDecl(Instance,VarDecl(Id(_),ArrayType(13,BoolType))),MethodDecl(Id(Constructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 877))

    def test_878(self):
        line = '''Class c8_:c{Constructor (___,x,_:Array [Array [Array [Array [Array [Array [Array [Array [Int ,0142],0B10],040],01],0B1],0b1001100],0B111101],1_7]){} }Class _{Destructor (){Break ;} }Class h{}'''
        expect = '''Program([ClassDecl(Id(c8_),Id(c),[MethodDecl(Id(Constructor),Instance,[param(Id(___),ArrayType(17,ArrayType(61,ArrayType(76,ArrayType(1,ArrayType(1,ArrayType(32,ArrayType(2,ArrayType(98,IntType))))))))),param(Id(x),ArrayType(17,ArrayType(61,ArrayType(76,ArrayType(1,ArrayType(1,ArrayType(32,ArrayType(2,ArrayType(98,IntType))))))))),param(Id(_),ArrayType(17,ArrayType(61,ArrayType(76,ArrayType(1,ArrayType(1,ArrayType(32,ArrayType(2,ArrayType(98,IntType)))))))))],Block([],[]))]),ClassDecl(Id(_),[MethodDecl(Id(Destructor),Instance,[],Block([],[Break]))]),ClassDecl(Id(h),[])])'''
        self.assertTrue(TestAST.test(line, expect, 878))

    def test_879(self):
        line = '''Class _:_{Constructor (H:Array [Float ,0b11_0];_:_NU5ig_){}Constructor (m9,R,Y,b:String ){}Constructor (){}$01z(__9:Float ){} }Class m9:m{}'''
        expect = '''Program([ClassDecl(Id(_),Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(H),ArrayType(6,FloatType)),param(Id(_),ClassType(Id(_NU5ig_)))],Block([],[])),MethodDecl(Id(Constructor),Instance,[param(Id(m9),StringType),param(Id(R),StringType),param(Id(Y),StringType),param(Id(b),StringType)],Block([],[])),MethodDecl(Id(Constructor),Instance,[],Block([],[])),MethodDecl(Id($01z),Static,[param(Id(__9),FloatType)],Block([],[]))]),ClassDecl(Id(m9),Id(m),[])])'''
        self.assertTrue(TestAST.test(line, expect, 879))

    def test_880(self):
        line = '''Class HE6{Var $_,_7N,$_:Array [String ,0b1_0_0];$_99(V,s:_){Continue ;} }'''
        expect = '''Program([ClassDecl(Id(HE6),[AttributeDecl(Static,VarDecl(Id($_),ArrayType(4,StringType))),AttributeDecl(Instance,VarDecl(Id(_7N),ArrayType(4,StringType))),AttributeDecl(Static,VarDecl(Id($_),ArrayType(4,StringType))),MethodDecl(Id($_99),Static,[param(Id(V),ClassType(Id(_))),param(Id(s),ClassType(Id(_)))],Block([],[Continue]))])])'''
        self.assertTrue(TestAST.test(line, expect, 880))

    def test_881(self):
        line = '''Class p:_gy{}Class i{}Class _{}Class _:d{}Class _R:u3_{}'''
        expect = '''Program([ClassDecl(Id(p),Id(_gy),[]),ClassDecl(Id(i),[]),ClassDecl(Id(_),[]),ClassDecl(Id(_),Id(d),[]),ClassDecl(Id(_R),Id(u3_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 881))

    def test_882(self):
        line = '''Class Y7t_C2_oW:g__{Constructor (_,s,AN4_F,__,g,_s:v;_:VZV2_;k_,_k,_4,P:Float ){_::$aJ.HF_.UZ._();} }Class _:__{}'''
        expect = '''Program([ClassDecl(Id(Y7t_C2_oW),Id(g__),[MethodDecl(Id(Constructor),Instance,[param(Id(_),ClassType(Id(v))),param(Id(s),ClassType(Id(v))),param(Id(AN4_F),ClassType(Id(v))),param(Id(__),ClassType(Id(v))),param(Id(g),ClassType(Id(v))),param(Id(_s),ClassType(Id(v))),param(Id(_),ClassType(Id(VZV2_))),param(Id(k_),FloatType),param(Id(_k),FloatType),param(Id(_4),FloatType),param(Id(P),FloatType)],Block([],[Call(FieldAccess(FieldAccess(FieldAccess(Id(_),Id($aJ)),Id(HF_)),Id(UZ)),Id(_),[])]))]),ClassDecl(Id(_),Id(__),[])])'''
        self.assertTrue(TestAST.test(line, expect, 882))

    def test_883(self):
        line = '''Class _la3:_{__(_Q_:z;V8__:Array [Array [Boolean ,0XD_C],037]){} }'''
        expect = '''Program([ClassDecl(Id(_la3),Id(_),[MethodDecl(Id(__),Instance,[param(Id(_Q_),ClassType(Id(z))),param(Id(V8__),ArrayType(31,ArrayType(220,BoolType)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 883))

    def test_884(self):
        line = '''Class x{__(_:Int ){}_(_P1:Boolean ){Break ;} }Class y{bqCVA1W(__:Float ;W9,d:Float ;R:WRg_;_,P,X_kp_7e4:D_;d,Ui_:_;_7:String ){Continue ;} }'''
        expect = '''Program([ClassDecl(Id(x),[MethodDecl(Id(__),Instance,[param(Id(_),IntType)],Block([],[])),MethodDecl(Id(_),Instance,[param(Id(_P1),BoolType)],Block([],[Break]))]),ClassDecl(Id(y),[MethodDecl(Id(bqCVA1W),Instance,[param(Id(__),FloatType),param(Id(W9),FloatType),param(Id(d),FloatType),param(Id(R),ClassType(Id(WRg_))),param(Id(_),ClassType(Id(D_))),param(Id(P),ClassType(Id(D_))),param(Id(X_kp_7e4),ClassType(Id(D_))),param(Id(d),ClassType(Id(_))),param(Id(Ui_),ClassType(Id(_))),param(Id(_7),StringType)],Block([],[Continue]))])])'''
        self.assertTrue(TestAST.test(line, expect, 884))

    def test_885(self):
        line = '''Class M9:_5_{Destructor (){}Var $_,XD,$__F,___,$6,__:Int ;}Class DD:_p{}'''
        expect = '''Program([ClassDecl(Id(M9),Id(_5_),[MethodDecl(Id(Destructor),Instance,[],Block([],[])),AttributeDecl(Static,VarDecl(Id($_),IntType)),AttributeDecl(Instance,VarDecl(Id(XD),IntType)),AttributeDecl(Static,VarDecl(Id($__F),IntType)),AttributeDecl(Instance,VarDecl(Id(___),IntType)),AttributeDecl(Static,VarDecl(Id($6),IntType)),AttributeDecl(Instance,VarDecl(Id(__),IntType))]),ClassDecl(Id(DD),Id(_p),[])])'''
        self.assertTrue(TestAST.test(line, expect, 885))

    def test_886(self):
        line = '''Class _:___3{$z8(_,e,_,_:_){} }Class _{$6(){}Destructor (){Return ;} }'''
        expect = '''Program([ClassDecl(Id(_),Id(___3),[MethodDecl(Id($z8),Static,[param(Id(_),ClassType(Id(_))),param(Id(e),ClassType(Id(_))),param(Id(_),ClassType(Id(_))),param(Id(_),ClassType(Id(_)))],Block([],[]))]),ClassDecl(Id(_),[MethodDecl(Id($6),Static,[],Block([],[])),MethodDecl(Id(Destructor),Instance,[],Block([],[Return(None)]))])])'''
        self.assertTrue(TestAST.test(line, expect, 886))

    def test_887(self):
        line = '''Class w3:_{Var $5_,$j:Array [Array [Array [Array [Array [String ,06],0b1001011],0B10000],02],0B10000];}Class Y66{}'''
        expect = '''Program([ClassDecl(Id(w3),Id(_),[AttributeDecl(Static,VarDecl(Id($5_),ArrayType(16,ArrayType(2,ArrayType(16,ArrayType(75,ArrayType(6,StringType))))))),AttributeDecl(Static,VarDecl(Id($j),ArrayType(16,ArrayType(2,ArrayType(16,ArrayType(75,ArrayType(6,StringType)))))))]),ClassDecl(Id(Y66),[])])'''
        self.assertTrue(TestAST.test(line, expect, 887))

    def test_888(self):
        line = '''Class _J{}Class c{Destructor (){Continue ;} }Class r_5{Destructor (){Var D,w:___;} }Class B{Destructor (){} }'''
        expect = '''Program([ClassDecl(Id(_J),[]),ClassDecl(Id(c),[MethodDecl(Id(Destructor),Instance,[],Block([],[Continue]))]),ClassDecl(Id(r_5),[MethodDecl(Id(Destructor),Instance,[],Block([VarDecl(Id(D),ClassType(Id(___))),VarDecl(Id(w),ClassType(Id(___)))],[]))]),ClassDecl(Id(B),[MethodDecl(Id(Destructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 888))

    def test_889(self):
        line = '''Class _{Var $_y:Boolean ;Constructor (_,_:Array [Array [Float ,2_8_84_1],0B1100011]){}Destructor (){} }'''
        expect = '''Program([ClassDecl(Id(_),[AttributeDecl(Static,VarDecl(Id($_y),BoolType)),MethodDecl(Id(Constructor),Instance,[param(Id(_),ArrayType(99,ArrayType(28841,FloatType))),param(Id(_),ArrayType(99,ArrayType(28841,FloatType)))],Block([],[])),MethodDecl(Id(Destructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 889))

    def test_890(self):
        line = '''Class _:_{}Class __:_L_{Constructor (){} }Class Y_{}Class g{}Class Kza8:_{}'''
        expect = '''Program([ClassDecl(Id(_),Id(_),[]),ClassDecl(Id(__),Id(_L_),[MethodDecl(Id(Constructor),Instance,[],Block([],[]))]),ClassDecl(Id(Y_),[]),ClassDecl(Id(g),[]),ClassDecl(Id(Kza8),Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 890))

    def test_891(self):
        line = '''Class c{Constructor (_:j;_,_8:YG4;_2:Float ){} }Class I6:_{}Class T7_:__{}'''
        expect = '''Program([ClassDecl(Id(c),[MethodDecl(Id(Constructor),Instance,[param(Id(_),ClassType(Id(j))),param(Id(_),ClassType(Id(YG4))),param(Id(_8),ClassType(Id(YG4))),param(Id(_2),FloatType)],Block([],[]))]),ClassDecl(Id(I6),Id(_),[]),ClassDecl(Id(T7_),Id(__),[])])'''
        self.assertTrue(TestAST.test(line, expect, 891))

    def test_892(self):
        line = '''Class _:w{$hXs4(_,__V:Array [Array [Array [Int ,0110],0B1],0110]){Continue ;}Constructor (_,_:String ;D_:Array [String ,0XD_4E_92];_,_M_1_:_;T6,_,v,_yA_:Array [Array [Array [String ,07],0110],6_1]){}Var _m,m_:Array [Array [Float ,0110],0b1010101];}'''
        expect = '''Program([ClassDecl(Id(_),Id(w),[MethodDecl(Id($hXs4),Static,[param(Id(_),ArrayType(72,ArrayType(1,ArrayType(72,IntType)))),param(Id(__V),ArrayType(72,ArrayType(1,ArrayType(72,IntType))))],Block([],[Continue])),MethodDecl(Id(Constructor),Instance,[param(Id(_),StringType),param(Id(_),StringType),param(Id(D_),ArrayType(872082,StringType)),param(Id(_),ClassType(Id(_))),param(Id(_M_1_),ClassType(Id(_))),param(Id(T6),ArrayType(61,ArrayType(72,ArrayType(7,StringType)))),param(Id(_),ArrayType(61,ArrayType(72,ArrayType(7,StringType)))),param(Id(v),ArrayType(61,ArrayType(72,ArrayType(7,StringType)))),param(Id(_yA_),ArrayType(61,ArrayType(72,ArrayType(7,StringType))))],Block([],[])),AttributeDecl(Instance,VarDecl(Id(_m),ArrayType(85,ArrayType(72,FloatType)))),AttributeDecl(Instance,VarDecl(Id(m_),ArrayType(85,ArrayType(72,FloatType))))])])'''
        self.assertTrue(TestAST.test(line, expect, 892))

    def test_893(self):
        line = '''Class s1_:S{}Class g{_(q,B,x:_zo;_0:Boolean ){}_(){} }Class z:U{}Class g:K_60{}'''
        expect = '''Program([ClassDecl(Id(s1_),Id(S),[]),ClassDecl(Id(g),[MethodDecl(Id(_),Instance,[param(Id(q),ClassType(Id(_zo))),param(Id(B),ClassType(Id(_zo))),param(Id(x),ClassType(Id(_zo))),param(Id(_0),BoolType)],Block([],[])),MethodDecl(Id(_),Instance,[],Block([],[]))]),ClassDecl(Id(z),Id(U),[]),ClassDecl(Id(g),Id(K_60),[])])'''
        self.assertTrue(TestAST.test(line, expect, 893))

    def test_894(self):
        line = '''Class T_:_e{$g(G:Array [Array [Boolean ,0b10011],88];_,_:Int ){} }'''
        expect = '''Program([ClassDecl(Id(T_),Id(_e),[MethodDecl(Id($g),Static,[param(Id(G),ArrayType(88,ArrayType(19,BoolType))),param(Id(_),IntType),param(Id(_),IntType)],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 894))

    def test_895(self):
        line = '''Class q_D5{Constructor (_,d0,G,_,__K:K;IQT:String ;_:_;s,a:Float ;S:Boolean ;_:A){} }'''
        expect = '''Program([ClassDecl(Id(q_D5),[MethodDecl(Id(Constructor),Instance,[param(Id(_),ClassType(Id(K))),param(Id(d0),ClassType(Id(K))),param(Id(G),ClassType(Id(K))),param(Id(_),ClassType(Id(K))),param(Id(__K),ClassType(Id(K))),param(Id(IQT),StringType),param(Id(_),ClassType(Id(_))),param(Id(s),FloatType),param(Id(a),FloatType),param(Id(S),BoolType),param(Id(_),ClassType(Id(A)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 895))

    def test_896(self):
        line = '''Class __Q53{Var _,M_Q:Array [Array [Array [Float ,0b1_1],0X3D],0X3D];}Class h{Constructor (a1,J7:Float ){}$33___(){Break ;}$_(__,OYxe_:Float ;_:m;_4:l;L,B8:_294){Return ;}Constructor (_,W:_){} }'''
        expect = '''Program([ClassDecl(Id(__Q53),[AttributeDecl(Instance,VarDecl(Id(_),ArrayType(61,ArrayType(61,ArrayType(3,FloatType))))),AttributeDecl(Instance,VarDecl(Id(M_Q),ArrayType(61,ArrayType(61,ArrayType(3,FloatType)))))]),ClassDecl(Id(h),[MethodDecl(Id(Constructor),Instance,[param(Id(a1),FloatType),param(Id(J7),FloatType)],Block([],[])),MethodDecl(Id($33___),Static,[],Block([],[Break])),MethodDecl(Id($_),Static,[param(Id(__),FloatType),param(Id(OYxe_),FloatType),param(Id(_),ClassType(Id(m))),param(Id(_4),ClassType(Id(l))),param(Id(L),ClassType(Id(_294))),param(Id(B8),ClassType(Id(_294)))],Block([],[Return(None)])),MethodDecl(Id(Constructor),Instance,[param(Id(_),ClassType(Id(_))),param(Id(W),ClassType(Id(_)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 896))

    def test_897(self):
        line = '''Class _d:_{$S__(_:Array [String ,07];_,__b,_:Array [Array [Array [Array [Array [Array [Boolean ,39],016],7_1],0x4E],0X34],0X75D_6]){Var I:Array [String ,0xC5_3_7];Continue ;} }'''
        expect = '''Program([ClassDecl(Id(_d),Id(_),[MethodDecl(Id($S__),Static,[param(Id(_),ArrayType(7,StringType)),param(Id(_),ArrayType(30166,ArrayType(52,ArrayType(78,ArrayType(71,ArrayType(14,ArrayType(39,BoolType))))))),param(Id(__b),ArrayType(30166,ArrayType(52,ArrayType(78,ArrayType(71,ArrayType(14,ArrayType(39,BoolType))))))),param(Id(_),ArrayType(30166,ArrayType(52,ArrayType(78,ArrayType(71,ArrayType(14,ArrayType(39,BoolType)))))))],Block([VarDecl(Id(I),ArrayType(50487,StringType))],[Continue]))])])'''
        self.assertTrue(TestAST.test(line, expect, 897))

    def test_898(self):
        line = '''Class V:_{Var _,$v:q_;}Class D{}Class Zl_5{Var $I,$z3B:String ;Destructor (){} }Class GoMld:l9_qe{}Class _{$r(){} }Class l:__{}'''
        expect = '''Program([ClassDecl(Id(V),Id(_),[AttributeDecl(Instance,VarDecl(Id(_),ClassType(Id(q_)))),AttributeDecl(Static,VarDecl(Id($v),ClassType(Id(q_))))]),ClassDecl(Id(D),[]),ClassDecl(Id(Zl_5),[AttributeDecl(Static,VarDecl(Id($I),StringType)),AttributeDecl(Static,VarDecl(Id($z3B),StringType)),MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(GoMld),Id(l9_qe),[]),ClassDecl(Id(_),[MethodDecl(Id($r),Static,[],Block([],[]))]),ClassDecl(Id(l),Id(__),[])])'''
        self.assertTrue(TestAST.test(line, expect, 898))

    def test_899(self):
        line = '''Class D:__p{}Class c{}Class _73_{}Class I_:C{Destructor (){ {l::$0V4___();} }}'''
        expect = '''Program([ClassDecl(Id(D),Id(__p),[]),ClassDecl(Id(c),[]),ClassDecl(Id(_73_),[]),ClassDecl(Id(I_),Id(C),[MethodDecl(Id(Destructor),Instance,[],Block([],[Block([],[Call(Id(l),Id($0V4___),[])])]))])])'''
        self.assertTrue(TestAST.test(line, expect, 899))

    def test_900(self):
        line = '''Class h:_h8_646{}Class __:_v{Var $7,$_:_;}Class _4U:s{}'''
        expect = '''Program([ClassDecl(Id(h),Id(_h8_646),[]),ClassDecl(Id(__),Id(_v),[AttributeDecl(Static,VarDecl(Id($7),ClassType(Id(_)))),AttributeDecl(Static,VarDecl(Id($_),ClassType(Id(_))))]),ClassDecl(Id(_4U),Id(s),[])])'''
        self.assertTrue(TestAST.test(line, expect, 900))

    def test_901(self):
        line = '''Class a_:_4{Var $_,_2,_V:Int ;}Class __:_{Destructor (){} }'''
        expect = '''Program([ClassDecl(Id(a_),Id(_4),[AttributeDecl(Static,VarDecl(Id($_),IntType)),AttributeDecl(Instance,VarDecl(Id(_2),IntType)),AttributeDecl(Instance,VarDecl(Id(_V),IntType))]),ClassDecl(Id(__),Id(_),[MethodDecl(Id(Destructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 901))

    def test_902(self):
        line = '''Class _:_G{}Class _Q9:r__{}Class _:__V{}Class _0{}Class _m_a54A{}Class c5_9{}Class h7_l_{}Class N:V3{}Class _{}Class N4:_m7{}'''
        expect = '''Program([ClassDecl(Id(_),Id(_G),[]),ClassDecl(Id(_Q9),Id(r__),[]),ClassDecl(Id(_),Id(__V),[]),ClassDecl(Id(_0),[]),ClassDecl(Id(_m_a54A),[]),ClassDecl(Id(c5_9),[]),ClassDecl(Id(h7_l_),[]),ClassDecl(Id(N),Id(V3),[]),ClassDecl(Id(_),[]),ClassDecl(Id(N4),Id(_m7),[])])'''
        self.assertTrue(TestAST.test(line, expect, 902))

    def test_903(self):
        line = '''Class d:__{Var _:Array [Array [Array [Array [Array [Array [Array [Int ,0451],6_2],04],0X29],0B100100],33],6];}'''
        expect = '''Program([ClassDecl(Id(d),Id(__),[AttributeDecl(Instance,VarDecl(Id(_),ArrayType(6,ArrayType(33,ArrayType(36,ArrayType(41,ArrayType(4,ArrayType(62,ArrayType(297,IntType)))))))))])])'''
        self.assertTrue(TestAST.test(line, expect, 903))

    def test_904(self):
        line = '''Class _7:JU49_7{Constructor (__,M:Int ;bZ_o,_3__3:Boolean ;_Ns:Array [Boolean ,0b1000111];Q:U){} }'''
        expect = '''Program([ClassDecl(Id(_7),Id(JU49_7),[MethodDecl(Id(Constructor),Instance,[param(Id(__),IntType),param(Id(M),IntType),param(Id(bZ_o),BoolType),param(Id(_3__3),BoolType),param(Id(_Ns),ArrayType(71,BoolType)),param(Id(Q),ClassType(Id(U)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 904))

    def test_905(self):
        line = '''Class _{}Class l__:_k_6t{}Class W{Val T4:String =!!J_::$__;}'''
        expect = '''Program([ClassDecl(Id(_),[]),ClassDecl(Id(l__),Id(_k_6t),[]),ClassDecl(Id(W),[AttributeDecl(Static,ConstDecl(Id($_),StringType,UnaryOp(!,UnaryOp(!,FieldAccess(Id(J_),Id($__))))))])])'''
        self.assertTrue(TestAST.test(line, expect, 905))

    def test_906(self):
        line = '''Class E{__(_,_V_02Z:Array [Array [Float ,0XF_D5],076];_5_,_Z:Int ){} }'''
        expect = '''Program([ClassDecl(Id(E),[MethodDecl(Id(__),Instance,[param(Id(_),ArrayType(62,ArrayType(4053,FloatType))),param(Id(_V_02Z),ArrayType(62,ArrayType(4053,FloatType))),param(Id(_5_),IntType),param(Id(_Z),IntType)],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 906))

    def test_907(self):
        line = '''Class _MH:_aOHn_{}Class m__:z{}Class n:_Q{}Class _56:q{Var $_P_Al:Float ;}Class aH:y6{}'''
        expect = '''Program([ClassDecl(Id(_MH),Id(_aOHn_),[]),ClassDecl(Id(m__),Id(z),[]),ClassDecl(Id(n),Id(_Q),[]),ClassDecl(Id(_56),Id(q),[AttributeDecl(Static,VarDecl(Id($_P_Al),FloatType))]),ClassDecl(Id(aH),Id(y6),[])])'''
        self.assertTrue(TestAST.test(line, expect, 907))

    def test_908(self):
        line = '''Class V__{$___(G,Fx8_,_:Array [Array [Float ,0xF],06_1_505];B:_X;_,z_:Float ;_,t,Gi1,mu:Float ){Return ;} }'''
        expect = '''Program([ClassDecl(Id(V__),[MethodDecl(Id($___),Static,[param(Id(G),ArrayType(25413,ArrayType(15,FloatType))),param(Id(Fx8_),ArrayType(25413,ArrayType(15,FloatType))),param(Id(_),ArrayType(25413,ArrayType(15,FloatType))),param(Id(B),ClassType(Id(_X))),param(Id(_),FloatType),param(Id(z_),FloatType),param(Id(_),FloatType),param(Id(t),FloatType),param(Id(Gi1),FloatType),param(Id(mu),FloatType)],Block([],[Return(None)]))])])'''
        self.assertTrue(TestAST.test(line, expect, 908))

    def test_909(self):
        line = '''Class a_97__n{}Class R2:i9{_(__,_F,B_l:String ;s,__kQ,e:Array [Array [Array [Array [Int ,0B1],0X1],28],0B1]){} }'''
        expect = '''Program([ClassDecl(Id(a_97__n),[]),ClassDecl(Id(R2),Id(i9),[MethodDecl(Id(_),Instance,[param(Id(__),StringType),param(Id(_F),StringType),param(Id(B_l),StringType),param(Id(s),ArrayType(1,ArrayType(28,ArrayType(1,ArrayType(1,IntType))))),param(Id(__kQ),ArrayType(1,ArrayType(28,ArrayType(1,ArrayType(1,IntType))))),param(Id(e),ArrayType(1,ArrayType(28,ArrayType(1,ArrayType(1,IntType)))))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 909))

    def test_910(self):
        line = '''Class _:t6{Var c:Array [String ,0143];}Class _5{}Class v:R__97582{Var _,$62Q5,$5:Array [Array [Array [Int ,0X3],85],0X5_C];}'''
        expect = '''Program([ClassDecl(Id(_),Id(t6),[AttributeDecl(Instance,VarDecl(Id(c),ArrayType(99,StringType)))]),ClassDecl(Id(_5),[]),ClassDecl(Id(v),Id(R__97582),[AttributeDecl(Instance,VarDecl(Id(_),ArrayType(92,ArrayType(85,ArrayType(3,IntType))))),AttributeDecl(Static,VarDecl(Id($62Q5),ArrayType(92,ArrayType(85,ArrayType(3,IntType))))),AttributeDecl(Static,VarDecl(Id($5),ArrayType(92,ArrayType(85,ArrayType(3,IntType)))))])])'''
        self.assertTrue(TestAST.test(line, expect, 910))

    def test_911(self):
        line = '''Class _:__{}Class _:C7DL{_0(){}Constructor (__,_:Float ;I:Array [Boolean ,0X1B];T:Boolean ){Continue ;Break ;} }'''
        expect = '''Program([ClassDecl(Id(_),Id(__),[]),ClassDecl(Id(_),Id(C7DL),[MethodDecl(Id(_0),Instance,[],Block([],[])),MethodDecl(Id(Constructor),Instance,[param(Id(__),FloatType),param(Id(_),FloatType),param(Id(I),ArrayType(27,BoolType)),param(Id(T),BoolType)],Block([],[Continue,Break]))])])'''
        self.assertTrue(TestAST.test(line, expect, 911))

    def test_912(self):
        line = '''Class _:_6{}Class _:B{Destructor (){} }Class m9{Var h:Array [Array [Boolean ,24],24];}'''
        expect = '''Program([ClassDecl(Id(_),Id(_6),[]),ClassDecl(Id(_),Id(B),[MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(m9),[AttributeDecl(Instance,VarDecl(Id(h),ArrayType(24,ArrayType(24,BoolType))))])])'''
        self.assertTrue(TestAST.test(line, expect, 912))

    def test_913(self):
        line = '''Class _{Var $23,__:Array [Array [Int ,21],0X9];Var $c,$V2,xi,B,V:Array [String ,0130];}Class Cd{Constructor (D,__:Int ;__:_G){} }'''
        expect = '''Program([ClassDecl(Id(_),[AttributeDecl(Static,VarDecl(Id($23),ArrayType(9,ArrayType(21,IntType)))),AttributeDecl(Instance,VarDecl(Id(__),ArrayType(9,ArrayType(21,IntType)))),AttributeDecl(Static,VarDecl(Id($c),ArrayType(88,StringType))),AttributeDecl(Static,VarDecl(Id($V2),ArrayType(88,StringType))),AttributeDecl(Instance,VarDecl(Id(xi),ArrayType(88,StringType))),AttributeDecl(Instance,VarDecl(Id(B),ArrayType(88,StringType))),AttributeDecl(Instance,VarDecl(Id(V),ArrayType(88,StringType)))]),ClassDecl(Id(Cd),[MethodDecl(Id(Constructor),Instance,[param(Id(D),IntType),param(Id(__),IntType),param(Id(__),ClassType(Id(_G)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 913))

    def test_914(self):
        line = '''Class t_4W0:YJ_{__(_2Y:T_;_C:Array [Array [Array [String ,047],0b1001010],0xF];___,e_,_I_,Y,_09,o:String ){} }'''
        expect = '''Program([ClassDecl(Id(t_4W0),Id(YJ_),[MethodDecl(Id(__),Instance,[param(Id(_2Y),ClassType(Id(T_))),param(Id(_C),ArrayType(15,ArrayType(74,ArrayType(39,StringType)))),param(Id(___),StringType),param(Id(e_),StringType),param(Id(_I_),StringType),param(Id(Y),StringType),param(Id(_09),StringType),param(Id(o),StringType)],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 914))

    def test_915(self):
        line = '''Class _{}Class _{Destructor (){}Constructor (_,_,_:Array [Float ,071_3];_:Int ;_:_o;l_e:__){Break ;} }'''
        expect = '''Program([ClassDecl(Id(_),[]),ClassDecl(Id(_),[MethodDecl(Id(Destructor),Instance,[],Block([],[])),MethodDecl(Id(Constructor),Instance,[param(Id(_),ArrayType(459,FloatType)),param(Id(_),ArrayType(459,FloatType)),param(Id(_),ArrayType(459,FloatType)),param(Id(_),IntType),param(Id(_),ClassType(Id(_o))),param(Id(l_e),ClassType(Id(__)))],Block([],[Break]))])])'''
        self.assertTrue(TestAST.test(line, expect, 915))

    def test_916(self):
        line = '''Class _3Q:R{}Class _{}Class _:w_{Var $4G3,__:Array [Int ,5];}'''
        expect = '''Program([ClassDecl(Id(_3Q),Id(R),[]),ClassDecl(Id(_),[]),ClassDecl(Id(_),Id(w_),[AttributeDecl(Static,VarDecl(Id($4G3),ArrayType(5,IntType))),AttributeDecl(Instance,VarDecl(Id(__),ArrayType(5,IntType)))])])'''
        self.assertTrue(TestAST.test(line, expect, 916))

    def test_917(self):
        line = '''Class N:_{$0(x:Float ;_C33:Int ;__:_){} }Class n_{Var _,$n,R:_X;}Class jv_r_{}'''
        expect = '''Program([ClassDecl(Id(N),Id(_),[MethodDecl(Id($0),Static,[param(Id(x),FloatType),param(Id(_C33),IntType),param(Id(__),ClassType(Id(_)))],Block([],[]))]),ClassDecl(Id(n_),[AttributeDecl(Instance,VarDecl(Id(_),ClassType(Id(_X)))),AttributeDecl(Static,VarDecl(Id($n),ClassType(Id(_X)))),AttributeDecl(Instance,VarDecl(Id(R),ClassType(Id(_X))))]),ClassDecl(Id(jv_r_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 917))

    def test_918(self):
        line = '''Class U:g{Constructor (){} }Class _{Var D,wT2,w,$f_l_,w:Int ;}'''
        expect = '''Program([ClassDecl(Id(U),Id(g),[MethodDecl(Id(Constructor),Instance,[],Block([],[]))]),ClassDecl(Id(_),[AttributeDecl(Instance,VarDecl(Id(D),IntType)),AttributeDecl(Instance,VarDecl(Id(wT2),IntType)),AttributeDecl(Instance,VarDecl(Id(w),IntType)),AttributeDecl(Static,VarDecl(Id($f_l_),IntType)),AttributeDecl(Instance,VarDecl(Id(w),IntType))])])'''
        self.assertTrue(TestAST.test(line, expect, 918))

    def test_919(self):
        line = '''Class _{Constructor (){}$9(_,m:String ;f,a,_0_c_:Array [Array [Int ,69],0b11]){} }'''
        expect = '''Program([ClassDecl(Id(_),[MethodDecl(Id(Constructor),Instance,[],Block([],[])),MethodDecl(Id($9),Static,[param(Id(_),StringType),param(Id(m),StringType),param(Id(f),ArrayType(3,ArrayType(69,IntType))),param(Id(a),ArrayType(3,ArrayType(69,IntType))),param(Id(_0_c_),ArrayType(3,ArrayType(69,IntType)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 919))

    def test_920(self):
        line = '''Class _:se{Var _6g,$8,$8_,_2_,__:Array [Boolean ,0B10_1];$6(){} }'''
        expect = '''Program([ClassDecl(Id(_),Id(se),[AttributeDecl(Instance,VarDecl(Id(_6g),ArrayType(5,BoolType))),AttributeDecl(Static,VarDecl(Id($8),ArrayType(5,BoolType))),AttributeDecl(Static,VarDecl(Id($8_),ArrayType(5,BoolType))),AttributeDecl(Instance,VarDecl(Id(_2_),ArrayType(5,BoolType))),AttributeDecl(Instance,VarDecl(Id(__),ArrayType(5,BoolType))),MethodDecl(Id($6),Static,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 920))

    def test_921(self):
        line = '''Class G__X{}Class _e{Constructor (_,h,m,fl1:Array [Int ,07]){} }Class tU{Constructor (){ {} }Constructor (R:_NI){} }Class cV__{}'''
        expect = '''Program([ClassDecl(Id(G__X),[]),ClassDecl(Id(_e),[MethodDecl(Id(Constructor),Instance,[param(Id(_),ArrayType(7,IntType)),param(Id(h),ArrayType(7,IntType)),param(Id(m),ArrayType(7,IntType)),param(Id(fl1),ArrayType(7,IntType))],Block([],[]))]),ClassDecl(Id(tU),[MethodDecl(Id(Constructor),Instance,[],Block([],[Block([],[])])),MethodDecl(Id(Constructor),Instance,[param(Id(R),ClassType(Id(_NI)))],Block([],[]))]),ClassDecl(Id(cV__),[])])'''
        self.assertTrue(TestAST.test(line, expect, 921))

    def test_922(self):
        line = '''Class T7___:SHC{}Class f8{Var $Um_9:Array [Array [Array [Array [Array [Int ,52],0b11],0113],06_1],52];}'''
        expect = '''Program([ClassDecl(Id(T7___),Id(SHC),[]),ClassDecl(Id(f8),[AttributeDecl(Static,VarDecl(Id($Um_9),ArrayType(52,ArrayType(49,ArrayType(75,ArrayType(3,ArrayType(52,IntType)))))))])])'''
        self.assertTrue(TestAST.test(line, expect, 922))

    def test_923(self):
        line = '''Class _{$_(_:Array [Array [Array [Array [Float ,0B101],0xCA],0101],0b1010];c__9,_x:Array [Int ,0101];__:Float ){}Constructor (_f,_:__;_w:Float ){} }'''
        expect = '''Program([ClassDecl(Id(_),[MethodDecl(Id($_),Static,[param(Id(_),ArrayType(10,ArrayType(65,ArrayType(202,ArrayType(5,FloatType))))),param(Id(c__9),ArrayType(65,IntType)),param(Id(_x),ArrayType(65,IntType)),param(Id(__),FloatType)],Block([],[])),MethodDecl(Id(Constructor),Instance,[param(Id(_f),ClassType(Id(__))),param(Id(_),ClassType(Id(__))),param(Id(_w),FloatType)],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 923))

    def test_924(self):
        line = '''Class __9{}Class nR{__Q(d5:Boolean ;_W,_rp1,J,_0,__:Int ;_:Array [Float ,07];K,_,__Y,_:Boolean ;G9,S,R:Array [String ,0X30];__,Z,_,j:_;A:Array [Array [Array [Float ,2],0x4],0b1]){} }Class dD:_3__2g2{}Class P:u{}'''
        expect = '''Program([ClassDecl(Id(__9),[]),ClassDecl(Id(nR),[MethodDecl(Id(__Q),Instance,[param(Id(d5),BoolType),param(Id(_W),IntType),param(Id(_rp1),IntType),param(Id(J),IntType),param(Id(_0),IntType),param(Id(__),IntType),param(Id(_),ArrayType(7,FloatType)),param(Id(K),BoolType),param(Id(_),BoolType),param(Id(__Y),BoolType),param(Id(_),BoolType),param(Id(G9),ArrayType(48,StringType)),param(Id(S),ArrayType(48,StringType)),param(Id(R),ArrayType(48,StringType)),param(Id(__),ClassType(Id(_))),param(Id(Z),ClassType(Id(_))),param(Id(_),ClassType(Id(_))),param(Id(j),ClassType(Id(_))),param(Id(A),ArrayType(1,ArrayType(4,ArrayType(2,FloatType))))],Block([],[]))]),ClassDecl(Id(dD),Id(_3__2g2),[]),ClassDecl(Id(P),Id(u),[])])'''
        self.assertTrue(TestAST.test(line, expect, 924))

    def test_925(self):
        line = '''Class _{}Class _:H{}Class __{}Class _:_{Constructor (){} }'''
        expect = '''Program([ClassDecl(Id(_),[]),ClassDecl(Id(_),Id(H),[]),ClassDecl(Id(__),[]),ClassDecl(Id(_),Id(_),[MethodDecl(Id(Constructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 925))

    def test_926(self):
        line = '''Class _B{Var $A:Array [Float ,067];Var _,S2_,_:Array [Boolean ,0X3F];}'''
        expect = '''Program([ClassDecl(Id(_B),[AttributeDecl(Static,VarDecl(Id($A),ArrayType(55,FloatType))),AttributeDecl(Instance,VarDecl(Id(_),ArrayType(63,BoolType))),AttributeDecl(Instance,VarDecl(Id(S2_),ArrayType(63,BoolType))),AttributeDecl(Instance,VarDecl(Id(_),ArrayType(63,BoolType)))])])'''
        self.assertTrue(TestAST.test(line, expect, 926))

    def test_927(self):
        line = '''Class S:P{Constructor (_v,k,_:Array [Array [Boolean ,219],0b11011];_9_,J,r4,T,__,_Bc63,_L,_9:ZRP_6;t:Array [Float ,0x4E]){} }'''
        expect = '''Program([ClassDecl(Id(S),Id(P),[MethodDecl(Id(Constructor),Instance,[param(Id(_v),ArrayType(27,ArrayType(219,BoolType))),param(Id(k),ArrayType(27,ArrayType(219,BoolType))),param(Id(_),ArrayType(27,ArrayType(219,BoolType))),param(Id(_9_),ClassType(Id(ZRP_6))),param(Id(J),ClassType(Id(ZRP_6))),param(Id(r4),ClassType(Id(ZRP_6))),param(Id(T),ClassType(Id(ZRP_6))),param(Id(__),ClassType(Id(ZRP_6))),param(Id(_Bc63),ClassType(Id(ZRP_6))),param(Id(_L),ClassType(Id(ZRP_6))),param(Id(_9),ClassType(Id(ZRP_6))),param(Id(t),ArrayType(78,FloatType))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 927))

    def test_928(self):
        line = '''Class _60_{}Class h8_n:tr{}Class I_{Destructor (){} }Class _8E{Var r_54:Array [Array [Array [String ,06],04],0b1_0];}Class i:r{}'''
        expect = '''Program([ClassDecl(Id(_60_),[]),ClassDecl(Id(h8_n),Id(tr),[]),ClassDecl(Id(I_),[MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(_8E),[AttributeDecl(Instance,VarDecl(Id(r_54),ArrayType(2,ArrayType(4,ArrayType(6,StringType)))))]),ClassDecl(Id(i),Id(r),[])])'''
        self.assertTrue(TestAST.test(line, expect, 928))

    def test_929(self):
        line = '''Class jR:P{$59(c,B:Array [Array [String ,0b1010000],0B11];_:Int ;o:f;An_,R:Int ;G_9:Array [Int ,0132]){} }'''
        expect = '''Program([ClassDecl(Id(jR),Id(P),[MethodDecl(Id($59),Static,[param(Id(c),ArrayType(3,ArrayType(80,StringType))),param(Id(B),ArrayType(3,ArrayType(80,StringType))),param(Id(_),IntType),param(Id(o),ClassType(Id(f))),param(Id(An_),IntType),param(Id(R),IntType),param(Id(G_9),ArrayType(90,IntType))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 929))

    def test_930(self):
        line = '''Class H_{Constructor (_:Array [Array [Array [Boolean ,0X8_A_9_B63],104_28],0b1_0_0]){} }'''
        expect = '''Program([ClassDecl(Id(H_),[MethodDecl(Id(Constructor),Instance,[param(Id(_),ArrayType(4,ArrayType(10428,ArrayType(9083747,BoolType))))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 930))

    def test_931(self):
        line = '''Class B__k_{Constructor (um,m_:O7MjP;_,z:Float ){Break ;Return ;} }'''
        expect = '''Program([ClassDecl(Id(B__k_),[MethodDecl(Id(Constructor),Instance,[param(Id(um),ClassType(Id(O7MjP))),param(Id(m_),ClassType(Id(O7MjP))),param(Id(_),FloatType),param(Id(z),FloatType)],Block([],[Break,Return(None)]))])])'''
        self.assertTrue(TestAST.test(line, expect, 931))

    def test_932(self):
        line = '''Class _:Z{}Class XVL_{Constructor (__,_:ke;s,_:String ){} }'''
        expect = '''Program([ClassDecl(Id(_),Id(Z),[]),ClassDecl(Id(XVL_),[MethodDecl(Id(Constructor),Instance,[param(Id(__),ClassType(Id(ke))),param(Id(_),ClassType(Id(ke))),param(Id(s),StringType),param(Id(_),StringType)],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 932))

    def test_933(self):
        line = '''Class X:CBt{}Class _:_{$_(Xe63W:Array [Array [Array [String ,0137],044_60_6],0B1];v,_:k){} }'''
        expect = '''Program([ClassDecl(Id(X),Id(CBt),[]),ClassDecl(Id(_),Id(_),[MethodDecl(Id($_),Static,[param(Id(Xe63W),ArrayType(1,ArrayType(18822,ArrayType(95,StringType)))),param(Id(v),ClassType(Id(k))),param(Id(_),ClassType(Id(k)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 933))

    def test_934(self):
        line = '''Class _{Var _:Array [Array [Array [Array [Array [Int ,0X34],0b101111],0X34],82],0x5];}'''
        expect = '''Program([ClassDecl(Id(_),[AttributeDecl(Instance,VarDecl(Id(_),ArrayType(5,ArrayType(82,ArrayType(52,ArrayType(47,ArrayType(52,IntType)))))))])])'''
        self.assertTrue(TestAST.test(line, expect, 934))

    def test_935(self):
        line = '''Class U1_{Var $__,U_:Float ;_o(_:Array [Boolean ,69];_j:R__){}$ZMh(i08:g;Q:Array [Array [Int ,070],070]){} }'''
        expect = '''Program([ClassDecl(Id(U1_),[AttributeDecl(Static,VarDecl(Id($__),FloatType)),AttributeDecl(Instance,VarDecl(Id(U_),FloatType)),MethodDecl(Id(_o),Instance,[param(Id(_),ArrayType(69,BoolType)),param(Id(_j),ClassType(Id(R__)))],Block([],[])),MethodDecl(Id($ZMh),Static,[param(Id(i08),ClassType(Id(g))),param(Id(Q),ArrayType(56,ArrayType(56,IntType)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 935))

    def test_936(self):
        line = '''Class _R8_4v:_{}Class __{Constructor (q_:Array [Float ,01];_E:T;_97:Boolean ){}Constructor (J,D_,_:Int ;Bp:_;_F,_1_4sF:Array [Int ,0B1000101];_,gw,o310q:Array [Array [Int ,7],6]){} }Class N:_8__{}'''
        expect = '''Program([ClassDecl(Id(_R8_4v),Id(_),[]),ClassDecl(Id(__),[MethodDecl(Id(Constructor),Instance,[param(Id(q_),ArrayType(1,FloatType)),param(Id(_E),ClassType(Id(T))),param(Id(_97),BoolType)],Block([],[])),MethodDecl(Id(Constructor),Instance,[param(Id(J),IntType),param(Id(D_),IntType),param(Id(_),IntType),param(Id(Bp),ClassType(Id(_))),param(Id(_F),ArrayType(69,IntType)),param(Id(_1_4sF),ArrayType(69,IntType)),param(Id(_),ArrayType(6,ArrayType(7,IntType))),param(Id(gw),ArrayType(6,ArrayType(7,IntType))),param(Id(o310q),ArrayType(6,ArrayType(7,IntType)))],Block([],[]))]),ClassDecl(Id(N),Id(_8__),[])])'''
        self.assertTrue(TestAST.test(line, expect, 936))

    def test_937(self):
        line = '''Class L__:_Nh_e_{Constructor (__X_m:Int ){} }Class z:_{Destructor (){} }Class _{$COU0(){Continue ;} }'''
        expect = '''Program([ClassDecl(Id(L__),Id(_Nh_e_),[MethodDecl(Id(Constructor),Instance,[param(Id(__X_m),IntType)],Block([],[]))]),ClassDecl(Id(z),Id(_),[MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(_),[MethodDecl(Id($COU0),Static,[],Block([],[Continue]))])])'''
        self.assertTrue(TestAST.test(line, expect, 937))

    def test_938(self):
        line = '''Class _:_{r(bk:y;_:_;_8:L;S,f_6P_,__y:U2;t:_;g1,_:Float ){} }'''
        expect = '''Program([ClassDecl(Id(_),Id(_),[MethodDecl(Id(r),Instance,[param(Id(bk),ClassType(Id(y))),param(Id(_),ClassType(Id(_))),param(Id(_8),ClassType(Id(L))),param(Id(S),ClassType(Id(U2))),param(Id(f_6P_),ClassType(Id(U2))),param(Id(__y),ClassType(Id(U2))),param(Id(t),ClassType(Id(_))),param(Id(g1),FloatType),param(Id(_),FloatType)],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 938))

    def test_939(self):
        line = '''Class t_p{}Class l77m_5{n(){} }Class h:ST{Destructor (){} }'''
        expect = '''Program([ClassDecl(Id(t_p),[]),ClassDecl(Id(l77m_5),[MethodDecl(Id(n),Instance,[],Block([],[]))]),ClassDecl(Id(h),Id(ST),[MethodDecl(Id(Destructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 939))

    def test_940(self):
        line = '''Class _:_5{ks4(){}Var $_7E_9,$d,_:Array [Array [Array [Array [Float ,2],0xA],05],7];}Class ____{}'''
        expect = '''Program([ClassDecl(Id(_),Id(_5),[MethodDecl(Id(ks4),Instance,[],Block([],[])),AttributeDecl(Static,VarDecl(Id($_7E_9),ArrayType(7,ArrayType(5,ArrayType(10,ArrayType(2,FloatType)))))),AttributeDecl(Static,VarDecl(Id($d),ArrayType(7,ArrayType(5,ArrayType(10,ArrayType(2,FloatType)))))),AttributeDecl(Instance,VarDecl(Id(_),ArrayType(7,ArrayType(5,ArrayType(10,ArrayType(2,FloatType))))))]),ClassDecl(Id(____),[])])'''
        self.assertTrue(TestAST.test(line, expect, 940))

    def test_941(self):
        line = '''Class f:_{}Class _:s__{}Class _5__{}Class xJ1_ioi{Constructor (){} }Class _{$5(P:__V){} }'''
        expect = '''Program([ClassDecl(Id(f),Id(_),[]),ClassDecl(Id(_),Id(s__),[]),ClassDecl(Id(_5__),[]),ClassDecl(Id(xJ1_ioi),[MethodDecl(Id(Constructor),Instance,[],Block([],[]))]),ClassDecl(Id(_),[MethodDecl(Id($5),Static,[param(Id(P),ClassType(Id(__V)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 941))

    def test_942(self):
        line = '''Class p:X{}Class c_JtU3{}Class _1{Constructor (_S:Boolean ){ {}Continue ;} }'''
        expect = '''Program([ClassDecl(Id(p),Id(X),[]),ClassDecl(Id(c_JtU3),[]),ClassDecl(Id(_1),[MethodDecl(Id(Constructor),Instance,[param(Id(_S),BoolType)],Block([],[Block([],[]),Continue]))])])'''
        self.assertTrue(TestAST.test(line, expect, 942))

    def test_943(self):
        line = '''Class g_A:b{Constructor (_d,u:_;J,Y,a,zC,M:Array [String ,026];__,_g,_:Array [Float ,0xA_C];_1:B;Z,_,c:Boolean ){Return ;}Var _,$01:Array [Int ,0b10100];}Class __2{}'''
        expect = '''Program([ClassDecl(Id(g_A),Id(b),[MethodDecl(Id(Constructor),Instance,[param(Id(_d),ClassType(Id(_))),param(Id(u),ClassType(Id(_))),param(Id(J),ArrayType(22,StringType)),param(Id(Y),ArrayType(22,StringType)),param(Id(a),ArrayType(22,StringType)),param(Id(zC),ArrayType(22,StringType)),param(Id(M),ArrayType(22,StringType)),param(Id(__),ArrayType(172,FloatType)),param(Id(_g),ArrayType(172,FloatType)),param(Id(_),ArrayType(172,FloatType)),param(Id(_1),ClassType(Id(B))),param(Id(Z),BoolType),param(Id(_),BoolType),param(Id(c),BoolType)],Block([],[Return(None)])),AttributeDecl(Instance,VarDecl(Id(_),ArrayType(20,IntType))),AttributeDecl(Static,VarDecl(Id($01),ArrayType(20,IntType)))]),ClassDecl(Id(__2),[])])'''
        self.assertTrue(TestAST.test(line, expect, 943))

    def test_944(self):
        line = '''Class __m9{}Class WH:_{w9(A:Array [Int ,0b110110];k3,d4:Array [String ,0X19]){}Var _:Array [String ,0X2];}'''
        expect = '''Program([ClassDecl(Id(__m9),[]),ClassDecl(Id(WH),Id(_),[MethodDecl(Id(w9),Instance,[param(Id(A),ArrayType(54,IntType)),param(Id(k3),ArrayType(25,StringType)),param(Id(d4),ArrayType(25,StringType))],Block([],[])),AttributeDecl(Instance,VarDecl(Id(_),ArrayType(2,StringType)))])])'''
        self.assertTrue(TestAST.test(line, expect, 944))

    def test_945(self):
        line = '''Class W0{}Class OYD{}Class _:_h{}Class mH_:h{}Class k6:Gld{}'''
        expect = '''Program([ClassDecl(Id(W0),[]),ClassDecl(Id(OYD),[]),ClassDecl(Id(_),Id(_h),[]),ClassDecl(Id(mH_),Id(h),[]),ClassDecl(Id(k6),Id(Gld),[])])'''
        self.assertTrue(TestAST.test(line, expect, 945))

    def test_946(self):
        line = '''Class hu:_O{}Class j4:m5{Var X,$61,_F_1:Array [String ,0B1];}Class __EOD{}Class _{Destructor (){} }'''
        expect = '''Program([ClassDecl(Id(hu),Id(_O),[]),ClassDecl(Id(j4),Id(m5),[AttributeDecl(Instance,VarDecl(Id(X),ArrayType(1,StringType))),AttributeDecl(Static,VarDecl(Id($61),ArrayType(1,StringType))),AttributeDecl(Instance,VarDecl(Id(_F_1),ArrayType(1,StringType)))]),ClassDecl(Id(__EOD),[]),ClassDecl(Id(_),[MethodDecl(Id(Destructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 946))

    def test_947(self):
        line = '''Class d{Var Mg,_3h,Gv,_,$d27,$_,_9:Array [Array [String ,83],8];}'''
        expect = '''Program([ClassDecl(Id(d),[AttributeDecl(Instance,VarDecl(Id(Mg),ArrayType(8,ArrayType(83,StringType)))),AttributeDecl(Instance,VarDecl(Id(_3h),ArrayType(8,ArrayType(83,StringType)))),AttributeDecl(Instance,VarDecl(Id(Gv),ArrayType(8,ArrayType(83,StringType)))),AttributeDecl(Instance,VarDecl(Id(_),ArrayType(8,ArrayType(83,StringType)))),AttributeDecl(Static,VarDecl(Id($d27),ArrayType(8,ArrayType(83,StringType)))),AttributeDecl(Static,VarDecl(Id($_),ArrayType(8,ArrayType(83,StringType)))),AttributeDecl(Instance,VarDecl(Id(_9),ArrayType(8,ArrayType(83,StringType))))])])'''
        self.assertTrue(TestAST.test(line, expect, 947))

    def test_948(self):
        line = '''Class J:X{$5_(g,_,_,mK,X3,_88,_,_:K;___,m,_,B5_:Array [Array [Array [Float ,0B1001],0X1C],97]){Break ;} }'''
        expect = '''Program([ClassDecl(Id(J),Id(X),[MethodDecl(Id($5_),Static,[param(Id(g),ClassType(Id(K))),param(Id(_),ClassType(Id(K))),param(Id(_),ClassType(Id(K))),param(Id(mK),ClassType(Id(K))),param(Id(X3),ClassType(Id(K))),param(Id(_88),ClassType(Id(K))),param(Id(_),ClassType(Id(K))),param(Id(_),ClassType(Id(K))),param(Id(___),ArrayType(97,ArrayType(28,ArrayType(9,FloatType)))),param(Id(m),ArrayType(97,ArrayType(28,ArrayType(9,FloatType)))),param(Id(_),ArrayType(97,ArrayType(28,ArrayType(9,FloatType)))),param(Id(B5_),ArrayType(97,ArrayType(28,ArrayType(9,FloatType))))],Block([],[Break]))])])'''
        self.assertTrue(TestAST.test(line, expect, 948))

    def test_949(self):
        line = '''Class ___:_7_342{Constructor (){Continue ;}$4(_PG7:Boolean ){} }'''
        expect = '''Program([ClassDecl(Id(___),Id(_7_342),[MethodDecl(Id(Constructor),Instance,[],Block([],[Continue])),MethodDecl(Id($4),Static,[param(Id(_PG7),BoolType)],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 949))

    def test_950(self):
        line = '''Class _:_f_{Constructor (k,__,__rK:Array [Int ,063];_Jx_,_:Array [Int ,69]){Break ;Break ;} }Class _:_m_{}'''
        expect = '''Program([ClassDecl(Id(_),Id(_f_),[MethodDecl(Id(Constructor),Instance,[param(Id(k),ArrayType(51,IntType)),param(Id(__),ArrayType(51,IntType)),param(Id(__rK),ArrayType(51,IntType)),param(Id(_Jx_),ArrayType(69,IntType)),param(Id(_),ArrayType(69,IntType))],Block([],[Break,Break]))]),ClassDecl(Id(_),Id(_m_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 950))

    def test_951(self):
        line = '''Class _{}Class _8:b{_8(c:Int ;_:U9){Continue ;{} }}Class m{}'''
        expect = '''Program([ClassDecl(Id(_),[]),ClassDecl(Id(_8),Id(b),[MethodDecl(Id(_8),Instance,[param(Id(c),IntType),param(Id(_),ClassType(Id(U9)))],Block([],[Continue,Block([],[])]))]),ClassDecl(Id(m),[])])'''
        self.assertTrue(TestAST.test(line, expect, 951))

    def test_952(self):
        line = '''Class _{}Class j4{}Class __55:_{Destructor (){} }Class _{Destructor (){}_(){} }Class _{}'''
        expect = '''Program([ClassDecl(Id(_),[]),ClassDecl(Id(j4),[]),ClassDecl(Id(__55),Id(_),[MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(_),[MethodDecl(Id(Destructor),Instance,[],Block([],[])),MethodDecl(Id(_),Instance,[],Block([],[]))]),ClassDecl(Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 952))

    def test_953(self):
        line = '''Class KD181_:_{Constructor (_,d_5__5:___;W,N6:Array [Array [Array [String ,0B1_0],074],07];J,__,_h5:Array [Float ,0b100100];_:_p){} }'''
        expect = '''Program([ClassDecl(Id(KD181_),Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(_),ClassType(Id(___))),param(Id(d_5__5),ClassType(Id(___))),param(Id(W),ArrayType(7,ArrayType(60,ArrayType(2,StringType)))),param(Id(N6),ArrayType(7,ArrayType(60,ArrayType(2,StringType)))),param(Id(J),ArrayType(36,FloatType)),param(Id(__),ArrayType(36,FloatType)),param(Id(_h5),ArrayType(36,FloatType)),param(Id(_),ClassType(Id(_p)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 953))

    def test_954(self):
        line = '''Class _25__2:_{}Class _j:_3{Var C9:Boolean ;Var $3_c__,v:V;}'''
        expect = '''Program([ClassDecl(Id(_25__2),Id(_),[]),ClassDecl(Id(_j),Id(_3),[AttributeDecl(Instance,VarDecl(Id(C9),BoolType)),AttributeDecl(Static,VarDecl(Id($3_c__),ClassType(Id(V)))),AttributeDecl(Instance,VarDecl(Id(v),ClassType(Id(V))))])])'''
        self.assertTrue(TestAST.test(line, expect, 954))

    def test_955(self):
        line = '''Class _{Var $M_:String ;}Class _{Constructor (l9,V:c;_O_:y){Break ;}Destructor (){}Var AwU,$8niI_,$tU:_;}'''
        expect = '''Program([ClassDecl(Id(_),[AttributeDecl(Static,VarDecl(Id($M_),StringType))]),ClassDecl(Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(l9),ClassType(Id(c))),param(Id(V),ClassType(Id(c))),param(Id(_O_),ClassType(Id(y)))],Block([],[Break])),MethodDecl(Id(Destructor),Instance,[],Block([],[])),AttributeDecl(Instance,VarDecl(Id(AwU),ClassType(Id(_)))),AttributeDecl(Static,VarDecl(Id($8niI_),ClassType(Id(_)))),AttributeDecl(Static,VarDecl(Id($tU),ClassType(Id(_))))])])'''
        self.assertTrue(TestAST.test(line, expect, 955))

    def test_956(self):
        line = '''Class _:_4_{}Class Q{Var _,v9,F_:Array [Boolean ,0B1111];}Class G{_(){} }Class Q15{}Class __7r:_1H_{}'''
        expect = '''Program([ClassDecl(Id(_),Id(_4_),[]),ClassDecl(Id(Q),[AttributeDecl(Instance,VarDecl(Id(_),ArrayType(15,BoolType))),AttributeDecl(Instance,VarDecl(Id(v9),ArrayType(15,BoolType))),AttributeDecl(Instance,VarDecl(Id(F_),ArrayType(15,BoolType)))]),ClassDecl(Id(G),[MethodDecl(Id(_),Instance,[],Block([],[]))]),ClassDecl(Id(Q15),[]),ClassDecl(Id(__7r),Id(_1H_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 956))

    def test_957(self):
        line = '''Class fZy_7_:_{}Class _9{$_(y31:String ){} }Class C{}Class g0:_{}Class _{}'''
        expect = '''Program([ClassDecl(Id(fZy_7_),Id(_),[]),ClassDecl(Id(_9),[MethodDecl(Id($_),Static,[param(Id(y31),StringType)],Block([],[]))]),ClassDecl(Id(C),[]),ClassDecl(Id(g0),Id(_),[]),ClassDecl(Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 957))

    def test_958(self):
        line = '''Class _:_{}Class _:__{Var $7_,_:Array [Array [Array [Array [Array [Array [Array [String ,0b1001110],0B1111],0b1001110],0B1111],0B1111],0B1111],0XF_8_70];}'''
        expect = '''Program([ClassDecl(Id(_),Id(_),[]),ClassDecl(Id(_),Id(__),[AttributeDecl(Static,VarDecl(Id($7_),ArrayType(63600,ArrayType(15,ArrayType(15,ArrayType(15,ArrayType(78,ArrayType(15,ArrayType(78,StringType))))))))),AttributeDecl(Instance,VarDecl(Id(_),ArrayType(63600,ArrayType(15,ArrayType(15,ArrayType(15,ArrayType(78,ArrayType(15,ArrayType(78,StringType)))))))))])])'''
        self.assertTrue(TestAST.test(line, expect, 958))

    def test_959(self):
        line = '''Class _:p{Destructor (){Continue ;}Constructor (_,W,_,KW:R;q:Array [Array [Float ,057],0B1];Gb,q___,_,_0_0:Float ;_:String ;V7:Array [String ,0B111];y:Array [Int ,0B1_0]){ {} }}'''
        expect = '''Program([ClassDecl(Id(_),Id(p),[MethodDecl(Id(Destructor),Instance,[],Block([],[Continue])),MethodDecl(Id(Constructor),Instance,[param(Id(_),ClassType(Id(R))),param(Id(W),ClassType(Id(R))),param(Id(_),ClassType(Id(R))),param(Id(KW),ClassType(Id(R))),param(Id(q),ArrayType(1,ArrayType(47,FloatType))),param(Id(Gb),FloatType),param(Id(q___),FloatType),param(Id(_),FloatType),param(Id(_0_0),FloatType),param(Id(_),StringType),param(Id(V7),ArrayType(7,StringType)),param(Id(y),ArrayType(2,IntType))],Block([],[Block([],[])]))])])'''
        self.assertTrue(TestAST.test(line, expect, 959))

    def test_960(self):
        line = '''Class n6:T_2{Constructor (_,_9q7_25_8,_,OL,_1,_8:_L){} }'''
        expect = '''Program([ClassDecl(Id(n6),Id(T_2),[MethodDecl(Id(Constructor),Instance,[param(Id(_),ClassType(Id(_L))),param(Id(_9q7_25_8),ClassType(Id(_L))),param(Id(_),ClassType(Id(_L))),param(Id(OL),ClassType(Id(_L))),param(Id(_1),ClassType(Id(_L))),param(Id(_8),ClassType(Id(_L)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 960))

    def test_961(self):
        line = '''Class H{Constructor (){} }Class _{}Class A:__Nb{$_1(){} }'''
        expect = '''Program([ClassDecl(Id(H),[MethodDecl(Id(Constructor),Instance,[],Block([],[]))]),ClassDecl(Id(_),[]),ClassDecl(Id(A),Id(__Nb),[MethodDecl(Id($_1),Static,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 961))

    def test_962(self):
        line = '''Class P_:e_8_{Var $_,g__w:Array [Array [Array [Float ,0b1_10],3],0B11];}'''
        expect = '''Program([ClassDecl(Id(P_),Id(e_8_),[AttributeDecl(Static,VarDecl(Id($_),ArrayType(3,ArrayType(3,ArrayType(6,FloatType))))),AttributeDecl(Instance,VarDecl(Id(g__w),ArrayType(3,ArrayType(3,ArrayType(6,FloatType)))))])])'''
        self.assertTrue(TestAST.test(line, expect, 962))

    def test_963(self):
        line = '''Class Z{Constructor (){}Destructor (){} }Class _:_w6_f{}'''
        expect = '''Program([ClassDecl(Id(Z),[MethodDecl(Id(Constructor),Instance,[],Block([],[])),MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(_),Id(_w6_f),[])])'''
        self.assertTrue(TestAST.test(line, expect, 963))

    def test_964(self):
        line = '''Class _7{__(S6_:Array [Int ,100];_B_2_,_:Array [Array [Int ,0xB],0b1];c:Array [Array [Array [Array [Int ,100],0x4],0X9],100]){Break ;} }Class UZQ:HvR{}'''
        expect = '''Program([ClassDecl(Id(_7),[MethodDecl(Id(__),Instance,[param(Id(S6_),ArrayType(100,IntType)),param(Id(_B_2_),ArrayType(1,ArrayType(11,IntType))),param(Id(_),ArrayType(1,ArrayType(11,IntType))),param(Id(c),ArrayType(100,ArrayType(9,ArrayType(4,ArrayType(100,IntType)))))],Block([],[Break]))]),ClassDecl(Id(UZQ),Id(HvR),[])])'''
        self.assertTrue(TestAST.test(line, expect, 964))

    def test_965(self):
        line = '''Class D_{Destructor (){Continue ;{} }}Class _7:A{}Class k9{}'''
        expect = '''Program([ClassDecl(Id(D_),[MethodDecl(Id(Destructor),Instance,[],Block([],[Continue,Block([],[])]))]),ClassDecl(Id(_7),Id(A),[]),ClassDecl(Id(k9),[])])'''
        self.assertTrue(TestAST.test(line, expect, 965))

    def test_966(self):
        line = '''Class _47{Destructor (){Var _,QO:Array [Array [String ,0B111001],0106];} }'''
        expect = '''Program([ClassDecl(Id(_47),[MethodDecl(Id(Destructor),Instance,[],Block([VarDecl(Id(_),ArrayType(70,ArrayType(57,StringType))),VarDecl(Id(QO),ArrayType(70,ArrayType(57,StringType)))],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 966))

    def test_967(self):
        line = '''Class MM_{Var $_,$p,t,$_,$Y_:Boolean ;Constructor (){Return ;} }Class _{}'''
        expect = '''Program([ClassDecl(Id(MM_),[AttributeDecl(Static,VarDecl(Id($_),BoolType)),AttributeDecl(Static,VarDecl(Id($p),BoolType)),AttributeDecl(Instance,VarDecl(Id(t),BoolType)),AttributeDecl(Static,VarDecl(Id($_),BoolType)),AttributeDecl(Static,VarDecl(Id($Y_),BoolType)),MethodDecl(Id(Constructor),Instance,[],Block([],[Return(None)]))]),ClassDecl(Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 967))

    def test_968(self):
        line = '''Class Om4K:_{Constructor (q,_,_5__N:Boolean ;_,b:Int ;i_267,x:Array [Int ,04];m6yO3,_3_,_,H:Array [Array [String ,92],0x8]){} }'''
        expect = '''Program([ClassDecl(Id(Om4K),Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(q),BoolType),param(Id(_),BoolType),param(Id(_5__N),BoolType),param(Id(_),IntType),param(Id(b),IntType),param(Id(i_267),ArrayType(4,IntType)),param(Id(x),ArrayType(4,IntType)),param(Id(m6yO3),ArrayType(8,ArrayType(92,StringType))),param(Id(_3_),ArrayType(8,ArrayType(92,StringType))),param(Id(_),ArrayType(8,ArrayType(92,StringType))),param(Id(H),ArrayType(8,ArrayType(92,StringType)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 968))

    def test_969(self):
        line = '''Class _:_{}Class _{}Class _g:__{}Class _d_{}Class f:T{}Class _{}'''
        expect = '''Program([ClassDecl(Id(_),Id(_),[]),ClassDecl(Id(_),[]),ClassDecl(Id(_g),Id(__),[]),ClassDecl(Id(_d_),[]),ClassDecl(Id(f),Id(T),[]),ClassDecl(Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 969))

    def test_970(self):
        line = '''Class LT_:_{}Class Q___{Var _yU_,$_g:Array [String ,0X64];Var _u,f:k;}'''
        expect = '''Program([ClassDecl(Id(LT_),Id(_),[]),ClassDecl(Id(Q___),[AttributeDecl(Instance,VarDecl(Id(_yU_),ArrayType(100,StringType))),AttributeDecl(Static,VarDecl(Id($_g),ArrayType(100,StringType))),AttributeDecl(Instance,VarDecl(Id(_u),ClassType(Id(k)))),AttributeDecl(Instance,VarDecl(Id(f),ClassType(Id(k))))])])'''
        self.assertTrue(TestAST.test(line, expect, 970))

    def test_971(self):
        line = '''Class G:T_{}Class _:__4{Constructor (){}Var $23_:Boolean ;}'''
        expect = '''Program([ClassDecl(Id(G),Id(T_),[]),ClassDecl(Id(_),Id(__4),[MethodDecl(Id(Constructor),Instance,[],Block([],[])),AttributeDecl(Static,VarDecl(Id($23_),BoolType))])])'''
        self.assertTrue(TestAST.test(line, expect, 971))

    def test_972(self):
        line = '''Class _0{Var q2,Q:Array [Float ,36];Var $_20_,__,S,$_oB__I,_,_:Array [Array [Float ,02],030_2];}Class _r99_:_{}Class _{Var $3_ab_:_p;Destructor (){}Var _yP,$d,a:Array [String ,0X4B];Var f78_ts,$96:n;}'''
        expect = '''Program([ClassDecl(Id(_0),[AttributeDecl(Instance,VarDecl(Id(q2),ArrayType(36,FloatType))),AttributeDecl(Instance,VarDecl(Id(Q),ArrayType(36,FloatType))),AttributeDecl(Static,VarDecl(Id($_20_),ArrayType(194,ArrayType(2,FloatType)))),AttributeDecl(Instance,VarDecl(Id(__),ArrayType(194,ArrayType(2,FloatType)))),AttributeDecl(Instance,VarDecl(Id(S),ArrayType(194,ArrayType(2,FloatType)))),AttributeDecl(Static,VarDecl(Id($_oB__I),ArrayType(194,ArrayType(2,FloatType)))),AttributeDecl(Instance,VarDecl(Id(_),ArrayType(194,ArrayType(2,FloatType)))),AttributeDecl(Instance,VarDecl(Id(_),ArrayType(194,ArrayType(2,FloatType))))]),ClassDecl(Id(_r99_),Id(_),[]),ClassDecl(Id(_),[AttributeDecl(Static,VarDecl(Id($3_ab_),ClassType(Id(_p)))),MethodDecl(Id(Destructor),Instance,[],Block([],[])),AttributeDecl(Instance,VarDecl(Id(_yP),ArrayType(75,StringType))),AttributeDecl(Static,VarDecl(Id($d),ArrayType(75,StringType))),AttributeDecl(Instance,VarDecl(Id(a),ArrayType(75,StringType))),AttributeDecl(Instance,VarDecl(Id(f78_ts),ClassType(Id(n)))),AttributeDecl(Static,VarDecl(Id($96),ClassType(Id(n))))])])'''
        self.assertTrue(TestAST.test(line, expect, 972))

    def test_973(self):
        line = '''Class _:l9{$f(E7,l3,S,W:Array [Array [Boolean ,01_1_1],0B1011100];_3:Array [Float ,0X6C];_N_,_:Boolean ;N,_M,_,A,Zk:__;_6_,I__v_e_:String ;__,_4,_:Array [Array [Array [Boolean ,05],5],01_1_101];_1:Array [Array [Int ,93],062];SVf6:l_g;u:Boolean ;w_,_4,_5g9_,JZ,w:_){} }'''
        expect = '''Program([ClassDecl(Id(_),Id(l9),[MethodDecl(Id($f),Static,[param(Id(E7),ArrayType(92,ArrayType(73,BoolType))),param(Id(l3),ArrayType(92,ArrayType(73,BoolType))),param(Id(S),ArrayType(92,ArrayType(73,BoolType))),param(Id(W),ArrayType(92,ArrayType(73,BoolType))),param(Id(_3),ArrayType(108,FloatType)),param(Id(_N_),BoolType),param(Id(_),BoolType),param(Id(N),ClassType(Id(__))),param(Id(_M),ClassType(Id(__))),param(Id(_),ClassType(Id(__))),param(Id(A),ClassType(Id(__))),param(Id(Zk),ClassType(Id(__))),param(Id(_6_),StringType),param(Id(I__v_e_),StringType),param(Id(__),ArrayType(4673,ArrayType(5,ArrayType(5,BoolType)))),param(Id(_4),ArrayType(4673,ArrayType(5,ArrayType(5,BoolType)))),param(Id(_),ArrayType(4673,ArrayType(5,ArrayType(5,BoolType)))),param(Id(_1),ArrayType(50,ArrayType(93,IntType))),param(Id(SVf6),ClassType(Id(l_g))),param(Id(u),BoolType),param(Id(w_),ClassType(Id(_))),param(Id(_4),ClassType(Id(_))),param(Id(_5g9_),ClassType(Id(_))),param(Id(JZ),ClassType(Id(_))),param(Id(w),ClassType(Id(_)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 973))

    def test_974(self):
        line = '''Class __{Constructor (_2,i__:Array [Array [Int ,0x6],0XE_6_167];H:Int ){} }'''
        expect = '''Program([ClassDecl(Id(__),[MethodDecl(Id(Constructor),Instance,[param(Id(_2),ArrayType(942439,ArrayType(6,IntType))),param(Id(i__),ArrayType(942439,ArrayType(6,IntType))),param(Id(H),IntType)],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 974))

    def test_975(self):
        line = '''Class _:_u_{}Class z3_:_6{}Class u_:H{}Class __:l__B4{}'''
        expect = '''Program([ClassDecl(Id(_),Id(_u_),[]),ClassDecl(Id(z3_),Id(_6),[]),ClassDecl(Id(u_),Id(H),[]),ClassDecl(Id(__),Id(l__B4),[])])'''
        self.assertTrue(TestAST.test(line, expect, 975))

    def test_976(self):
        line = '''Class _6:v8_W{}Class _{}Class _:_{}Class rz:f4{Constructor (){} }Class J_T:s{}'''
        expect = '''Program([ClassDecl(Id(_6),Id(v8_W),[]),ClassDecl(Id(_),[]),ClassDecl(Id(_),Id(_),[]),ClassDecl(Id(rz),Id(f4),[MethodDecl(Id(Constructor),Instance,[],Block([],[]))]),ClassDecl(Id(J_T),Id(s),[])])'''
        self.assertTrue(TestAST.test(line, expect, 976))

    def test_977(self):
        line = '''Class M:j_{}Class _{$_7(x4H37,r,_4:Array [Array [Array [String ,0X67],0X38],0B1001010];_,_,_:Array [Array [Array [Int ,0b11100],0X38],8_81]){} }Class _{}'''
        expect = '''Program([ClassDecl(Id(M),Id(j_),[]),ClassDecl(Id(_),[MethodDecl(Id($_7),Static,[param(Id(x4H37),ArrayType(74,ArrayType(56,ArrayType(103,StringType)))),param(Id(r),ArrayType(74,ArrayType(56,ArrayType(103,StringType)))),param(Id(_4),ArrayType(74,ArrayType(56,ArrayType(103,StringType)))),param(Id(_),ArrayType(881,ArrayType(56,ArrayType(28,IntType)))),param(Id(_),ArrayType(881,ArrayType(56,ArrayType(28,IntType)))),param(Id(_),ArrayType(881,ArrayType(56,ArrayType(28,IntType))))],Block([],[]))]),ClassDecl(Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 977))

    def test_978(self):
        line = '''Class x{Constructor (_M__19:Array [Array [Array [String ,037],070_14],0b1_0_0];____,_i2k5__8,c:String ){} }'''
        expect = '''Program([ClassDecl(Id(x),[MethodDecl(Id(Constructor),Instance,[param(Id(_M__19),ArrayType(4,ArrayType(3596,ArrayType(31,StringType)))),param(Id(____),StringType),param(Id(_i2k5__8),StringType),param(Id(c),StringType)],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 978))

    def test_979(self):
        line = '''Class k:R{Destructor (){}Z4462_(){ {} }Constructor (_F,_331,J_,i_m__2:Array [Boolean ,0X9];__:String ;__:Array [Boolean ,4]){Var _g,E1:Array [String ,054];}$4_3(___0,_,_,__,j__hr_p__:Boolean ;L,_6ye,_:Array [Float ,07]){} }'''
        expect = '''Program([ClassDecl(Id(k),Id(R),[MethodDecl(Id(Destructor),Instance,[],Block([],[])),MethodDecl(Id(Z4462_),Instance,[],Block([],[Block([],[])])),MethodDecl(Id(Constructor),Instance,[param(Id(_F),ArrayType(9,BoolType)),param(Id(_331),ArrayType(9,BoolType)),param(Id(J_),ArrayType(9,BoolType)),param(Id(i_m__2),ArrayType(9,BoolType)),param(Id(__),StringType),param(Id(__),ArrayType(4,BoolType))],Block([VarDecl(Id(_g),ArrayType(44,StringType)),VarDecl(Id(E1),ArrayType(44,StringType))],[])),MethodDecl(Id($4_3),Static,[param(Id(___0),BoolType),param(Id(_),BoolType),param(Id(_),BoolType),param(Id(__),BoolType),param(Id(j__hr_p__),BoolType),param(Id(L),ArrayType(7,FloatType)),param(Id(_6ye),ArrayType(7,FloatType)),param(Id(_),ArrayType(7,FloatType))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 979))

    def test_980(self):
        line = '''Class _{C(_o,I:Array [Float ,0b1001];N,j_:Int ;_,C,_,_:Float ;_:Array [Float ,013]){} }'''
        expect = '''Program([ClassDecl(Id(_),[MethodDecl(Id(C),Instance,[param(Id(_o),ArrayType(9,FloatType)),param(Id(I),ArrayType(9,FloatType)),param(Id(N),IntType),param(Id(j_),IntType),param(Id(_),FloatType),param(Id(C),FloatType),param(Id(_),FloatType),param(Id(_),FloatType),param(Id(_),ArrayType(11,FloatType))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 980))

    def test_981(self):
        line = '''Class _:b_6{Constructor (k,i:String ;Qc:Array [Array [Int ,0B110_1_0],0x14]){} }'''
        expect = '''Program([ClassDecl(Id(_),Id(b_6),[MethodDecl(Id(Constructor),Instance,[param(Id(k),StringType),param(Id(i),StringType),param(Id(Qc),ArrayType(20,ArrayType(26,IntType)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 981))

    def test_982(self):
        line = '''Class _:_F_C{}Class s:g{Constructor (t,_,Y:D;_c,_v3s,_,_,a:Float ;_:String ){} }'''
        expect = '''Program([ClassDecl(Id(_),Id(_F_C),[]),ClassDecl(Id(s),Id(g),[MethodDecl(Id(Constructor),Instance,[param(Id(t),ClassType(Id(D))),param(Id(_),ClassType(Id(D))),param(Id(Y),ClassType(Id(D))),param(Id(_c),FloatType),param(Id(_v3s),FloatType),param(Id(_),FloatType),param(Id(_),FloatType),param(Id(a),FloatType),param(Id(_),StringType)],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 982))

    def test_983(self):
        line = '''Class p{}Class C123{Var $_6jX3,$2_:Boolean ;Var g,z:Array [Int ,6];}'''
        expect = '''Program([ClassDecl(Id(p),[]),ClassDecl(Id(C123),[AttributeDecl(Static,VarDecl(Id($_6jX3),BoolType)),AttributeDecl(Static,VarDecl(Id($2_),BoolType)),AttributeDecl(Instance,VarDecl(Id(g),ArrayType(6,IntType))),AttributeDecl(Instance,VarDecl(Id(z),ArrayType(6,IntType)))])])'''
        self.assertTrue(TestAST.test(line, expect, 983))

    def test_984(self):
        line = '''Class D:q{}Class _8{}Class b4_2:H{Var $Y1:Array [Array [Int ,0x42],53];}'''
        expect = '''Program([ClassDecl(Id(D),Id(q),[]),ClassDecl(Id(_8),[]),ClassDecl(Id(b4_2),Id(H),[AttributeDecl(Static,VarDecl(Id($Y1),ArrayType(53,ArrayType(66,IntType))))])])'''
        self.assertTrue(TestAST.test(line, expect, 984))

    def test_985(self):
        line = '''Class k_2__:KMG{Constructor (M,_,a,_:_l__){} }Class m{$D(){} }'''
        expect = '''Program([ClassDecl(Id(k_2__),Id(KMG),[MethodDecl(Id(Constructor),Instance,[param(Id(M),ClassType(Id(_l__))),param(Id(_),ClassType(Id(_l__))),param(Id(a),ClassType(Id(_l__))),param(Id(_),ClassType(Id(_l__)))],Block([],[]))]),ClassDecl(Id(m),[MethodDecl(Id($D),Static,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 985))

    def test_986(self):
        line = '''Class _:_9j{}Class h:_{Constructor (){}Var S_:String ;}Class _:__43_{}'''
        expect = '''Program([ClassDecl(Id(_),Id(_9j),[]),ClassDecl(Id(h),Id(_),[MethodDecl(Id(Constructor),Instance,[],Block([],[])),AttributeDecl(Instance,VarDecl(Id(S_),StringType))]),ClassDecl(Id(_),Id(__43_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 986))

    def test_987(self):
        line = '''Class X:p1_{Constructor (__:Array [Float ,051];q,_:Array [Array [Array [Array [Array [Int ,75],75],03],75],75];__,fCa:Array [Array [Boolean ,0b111],0X5C];__:Array [Array [Array [Float ,051],01],051];x_,Z_:String ){} }'''
        expect = '''Program([ClassDecl(Id(X),Id(p1_),[MethodDecl(Id(Constructor),Instance,[param(Id(__),ArrayType(41,FloatType)),param(Id(q),ArrayType(75,ArrayType(75,ArrayType(3,ArrayType(75,ArrayType(75,IntType)))))),param(Id(_),ArrayType(75,ArrayType(75,ArrayType(3,ArrayType(75,ArrayType(75,IntType)))))),param(Id(__),ArrayType(92,ArrayType(7,BoolType))),param(Id(fCa),ArrayType(92,ArrayType(7,BoolType))),param(Id(__),ArrayType(41,ArrayType(1,ArrayType(41,FloatType)))),param(Id(x_),StringType),param(Id(Z_),StringType)],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 987))

    def test_988(self):
        line = '''Class _zr5g5:k{Var LB_,_2__:ZJq8;}Class t_:__{}Class _{}'''
        expect = '''Program([ClassDecl(Id(_zr5g5),Id(k),[AttributeDecl(Instance,VarDecl(Id(LB_),ClassType(Id(ZJq8)))),AttributeDecl(Instance,VarDecl(Id(_2__),ClassType(Id(ZJq8))))]),ClassDecl(Id(t_),Id(__),[]),ClassDecl(Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 988))

    def test_989(self):
        line = '''Class _2:f__{vY(_J:Array [Array [Array [Array [Array [Int ,0b1011111],063],063],0x3A],063];G:_){} }Class Ie__5{}'''
        expect = '''Program([ClassDecl(Id(_2),Id(f__),[MethodDecl(Id(vY),Instance,[param(Id(_J),ArrayType(51,ArrayType(58,ArrayType(51,ArrayType(51,ArrayType(95,IntType)))))),param(Id(G),ClassType(Id(_)))],Block([],[]))]),ClassDecl(Id(Ie__5),[])])'''
        self.assertTrue(TestAST.test(line, expect, 989))

    def test_990(self):
        line = '''Class T{}Class v:_{Constructor (F,_3_:Array [Boolean ,75];_,_:Array [Array [Float ,0XC04_C],6_7];_,r,lm,f6__,P5:String ;O,Us_E3,O:String ){} }'''
        expect = '''Program([ClassDecl(Id(T),[]),ClassDecl(Id(v),Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(F),ArrayType(75,BoolType)),param(Id(_3_),ArrayType(75,BoolType)),param(Id(_),ArrayType(67,ArrayType(49228,FloatType))),param(Id(_),ArrayType(67,ArrayType(49228,FloatType))),param(Id(_),StringType),param(Id(r),StringType),param(Id(lm),StringType),param(Id(f6__),StringType),param(Id(P5),StringType),param(Id(O),StringType),param(Id(Us_E3),StringType),param(Id(O),StringType)],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 990))

    def test_991(self):
        line = '''Class _{Var f__:Array [Boolean ,52];}Class _:o_{}Class _:_{}Class U{}'''
        expect = '''Program([ClassDecl(Id(_),[AttributeDecl(Instance,VarDecl(Id(f__),ArrayType(52,BoolType)))]),ClassDecl(Id(_),Id(o_),[]),ClassDecl(Id(_),Id(_),[]),ClassDecl(Id(U),[])])'''
        self.assertTrue(TestAST.test(line, expect, 991))

    def test_992(self):
        line = '''Class _U:_2w3h5v{Var _:Array [Array [Boolean ,0X4],0X4E];}'''
        expect = '''Program([ClassDecl(Id(_U),Id(_2w3h5v),[AttributeDecl(Instance,VarDecl(Id(_),ArrayType(78,ArrayType(4,BoolType))))])])'''
        self.assertTrue(TestAST.test(line, expect, 992))

    def test_993(self):
        line = '''Class __u{$0H(_U:A){}_(_,_a:String ;c,__2_:f2;V,_:Array [Array [Array [Array [Boolean ,37_405_5],0b1],0X2],0b1001110]){ {} }}'''
        expect = '''Program([ClassDecl(Id(__u),[MethodDecl(Id($0H),Static,[param(Id(_U),ClassType(Id(A)))],Block([],[])),MethodDecl(Id(_),Instance,[param(Id(_),StringType),param(Id(_a),StringType),param(Id(c),ClassType(Id(f2))),param(Id(__2_),ClassType(Id(f2))),param(Id(V),ArrayType(78,ArrayType(2,ArrayType(1,ArrayType(374055,BoolType))))),param(Id(_),ArrayType(78,ArrayType(2,ArrayType(1,ArrayType(374055,BoolType)))))],Block([],[Block([],[])]))])])'''
        self.assertTrue(TestAST.test(line, expect, 993))

    def test_994(self):
        line = '''Class __{Constructor (Y7:PV;Sl74:Float ;t3,D,dX:Boolean ;__:e){} }'''
        expect = '''Program([ClassDecl(Id(__),[MethodDecl(Id(Constructor),Instance,[param(Id(Y7),ClassType(Id(PV))),param(Id(Sl74),FloatType),param(Id(t3),BoolType),param(Id(D),BoolType),param(Id(dX),BoolType),param(Id(__),ClassType(Id(e)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 994))

    def test_995(self):
        line = '''Class C13_:_xy{}Class a_:_1j__{}Class ___f:h_{Destructor (){} }Class _:wm{Var $h____,$_,b9k_:Int ;}'''
        expect = '''Program([ClassDecl(Id(C13_),Id(_xy),[]),ClassDecl(Id(a_),Id(_1j__),[]),ClassDecl(Id(___f),Id(h_),[MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(_),Id(wm),[AttributeDecl(Static,VarDecl(Id($h____),IntType)),AttributeDecl(Static,VarDecl(Id($_),IntType)),AttributeDecl(Instance,VarDecl(Id(b9k_),IntType))])])'''
        self.assertTrue(TestAST.test(line, expect, 995))

    def test_996(self):
        line = '''Class F:_{Constructor (_,z:Array [Array [Boolean ,4],72];_:Float ){} }'''
        expect = '''Program([ClassDecl(Id(F),Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(_),ArrayType(72,ArrayType(4,BoolType))),param(Id(z),ArrayType(72,ArrayType(4,BoolType))),param(Id(_),FloatType)],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 996))

    def test_997(self):
        line = '''Class __H:_X1{}Class N___:p{}Class _{}Class p__D{_(){}Var W,$2,$32Y,_:String ;v0_m9(){} }'''
        expect = '''Program([ClassDecl(Id(__H),Id(_X1),[]),ClassDecl(Id(N___),Id(p),[]),ClassDecl(Id(_),[]),ClassDecl(Id(p__D),[MethodDecl(Id(_),Instance,[],Block([],[])),AttributeDecl(Instance,VarDecl(Id(W),StringType)),AttributeDecl(Static,VarDecl(Id($2),StringType)),AttributeDecl(Static,VarDecl(Id($32Y),StringType)),AttributeDecl(Instance,VarDecl(Id(_),StringType)),MethodDecl(Id(v0_m9),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(line, expect, 997))

    def test_998(self):
        line = '''Class W5___{}Class Y8_{Var _1:Array [Array [Int ,4],6_8];$__(){}Destructor (){} }Class j{}'''
        expect = '''Program([ClassDecl(Id(W5___),[]),ClassDecl(Id(Y8_),[AttributeDecl(Instance,VarDecl(Id(_1),ArrayType(68,ArrayType(4,IntType)))),MethodDecl(Id($__),Static,[],Block([],[])),MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(j),[])])'''
        self.assertTrue(TestAST.test(line, expect, 998))

    def test_999(self):
        line = '''Class _H:a052{Constructor (_:p_;_,a_:Array [Array [Float ,0b1],0B10]){}Var _:_;}'''
        expect = '''Program([ClassDecl(Id(_H),Id(a052),[MethodDecl(Id(Constructor),Instance,[param(Id(_),ClassType(Id(p_))),param(Id(_),ArrayType(2,ArrayType(1,FloatType))),param(Id(a_),ArrayType(2,ArrayType(1,FloatType)))],Block([],[])),AttributeDecl(Instance,VarDecl(Id(_),ClassType(Id(_))))])])'''
        self.assertTrue(TestAST.test(line, expect, 999))

    