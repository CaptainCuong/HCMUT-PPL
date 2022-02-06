import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    def test_0(self):
        self.assertTrue(TestLexer.test('''Class _:n{Constructor (Z_:Boolean ;_8,h:String ){Break ;}Constructor (Z,_:Array [Boolean ,053];_,x6:y){Break ;{} }Var z:PL;}Class r{Val _3:Array [Array [String ,03],0b100000];$_Q(){}Val aAH_2O3,ftYz:Array [Array [Int ,0xD],0X2C];}''','''Class,_,:,n,{,Constructor,(,Z_,:,Boolean,;,_8,,,h,:,String,),{,Break,;,},Constructor,(,Z,,,_,:,Array,[,Boolean,,,053,],;,_,,,x6,:,y,),{,Break,;,{,},},Var,z,:,PL,;,},Class,r,{,Val,_3,:,Array,[,Array,[,String,,,03,],,,0b100000,],;,$_Q,(,),{,},Val,aAH_2O3,,,ftYz,:,Array,[,Array,[,Int,,,0xD,],,,0X2C,],;,},<EOF>''',101))

    def test_1(self):
        self.assertTrue(TestLexer.test('''Class G{_N(_,_:Array [Float ,0117];_3816,L,_,_6,m16e,_:Array [Array [Array [Array [Array [Array [Array [Array [Array [String ,7],0x63],0X59],0117],0X59],0b1000],0b1],0117],0117]){Break ;Return ;} }Class RI77{Val $6,$8,$1l:Boolean ;}''','''Class,G,{,_N,(,_,,,_,:,Array,[,Float,,,0117,],;,_3816,,,L,,,_,,,_6,,,m16e,,,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,7,],,,0x63,],,,0X59,],,,0117,],,,0X59,],,,0b1000,],,,0b1,],,,0117,],,,0117,],),{,Break,;,Return,;,},},Class,RI77,{,Val,$6,,,$8,,,$1l,:,Boolean,;,},<EOF>''',101))

    def test_2(self):
        self.assertTrue(TestLexer.test('''Class C:y_{}Class _o_{M(E:Float ;_,_:Jp){}Val $IX,$__,$V_1,_:Array [Array [Array [Array [Array [Float ,0XE],0X30],0b1_1],0B111111],15];}Class _{$_J(){ {}{Val _:_69V;}{}{}{} }}Class __:H{}Class _c{}Class rw{}''','''Class,C,:,y_,{,},Class,_o_,{,M,(,E,:,Float,;,_,,,_,:,Jp,),{,},Val,$IX,,,$__,,,$V_1,,,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0XE,],,,0X30,],,,0b11,],,,0B111111,],,,15,],;,},Class,_,{,$_J,(,),{,{,},{,Val,_,:,_69V,;,},{,},{,},{,},},},Class,__,:,H,{,},Class,_c,{,},Class,rw,{,},<EOF>''',101))

    def test_3(self):
        self.assertTrue(TestLexer.test('''Class c:by{}Class _{Val $a:Array [Array [Array [Float ,0x97],06],3];}Class Q:ck9{$z(bms,M0_:_;__:Array [Boolean ,0B10000];s_7,_,__1:Int ){}Val v65:Array [Array [String ,0x4],04];}Class u:_{}Class _5:_{Val bu:L___;}''','''Class,c,:,by,{,},Class,_,{,Val,$a,:,Array,[,Array,[,Array,[,Float,,,0x97,],,,06,],,,3,],;,},Class,Q,:,ck9,{,$z,(,bms,,,M0_,:,_,;,__,:,Array,[,Boolean,,,0B10000,],;,s_7,,,_,,,__1,:,Int,),{,},Val,v65,:,Array,[,Array,[,String,,,0x4,],,,04,],;,},Class,u,:,_,{,},Class,_5,:,_,{,Val,bu,:,L___,;,},<EOF>''',101))

    def test_4(self):
        self.assertTrue(TestLexer.test('''Class v:N{}Class k{Var $_2_y:V;}Class _{Destructor (){}Val $_gI,$_V,u_m:Array [Array [Array [Array [Int ,0x8_7_4EB],0b1110],05_51],0b1];}Class dP{}''','''Class,v,:,N,{,},Class,k,{,Var,$_2_y,:,V,;,},Class,_,{,Destructor,(,),{,},Val,$_gI,,,$_V,,,u_m,:,Array,[,Array,[,Array,[,Array,[,Int,,,0x874EB,],,,0b1110,],,,0551,],,,0b1,],;,},Class,dP,{,},<EOF>''',101))

    def test_5(self):
        self.assertTrue(TestLexer.test('''Class _{}Class _R{_A_(_,_:Float ){Break ;} }Class _:_{Constructor (Q:String ){} }Class KC_{}Class _{Constructor (l_4:Float ){} }''','''Class,_,{,},Class,_R,{,_A_,(,_,,,_,:,Float,),{,Break,;,},},Class,_,:,_,{,Constructor,(,Q,:,String,),{,},},Class,KC_,{,},Class,_,{,Constructor,(,l_4,:,Float,),{,},},<EOF>''',101))

    def test_6(self):
        self.assertTrue(TestLexer.test('''Class _:d5{}Class _:_J{}Class _z6M:_{Var $_7Z9_7w:W;Constructor (){Var v:Array [String ,0b1_1];}_(){}Val r___z5_:F;Val O,$_d,_,$_i_1a_:Boolean ;}Class _:_{}Class X{Constructor (){Continue ;}Constructor (X:E9;_8:String ;__:Array [Array [Array [Float ,18],0b11],0b110100]){} }''','''Class,_,:,d5,{,},Class,_,:,_J,{,},Class,_z6M,:,_,{,Var,$_7Z9_7w,:,W,;,Constructor,(,),{,Var,v,:,Array,[,String,,,0b11,],;,},_,(,),{,},Val,r___z5_,:,F,;,Val,O,,,$_d,,,_,,,$_i_1a_,:,Boolean,;,},Class,_,:,_,{,},Class,X,{,Constructor,(,),{,Continue,;,},Constructor,(,X,:,E9,;,_8,:,String,;,__,:,Array,[,Array,[,Array,[,Float,,,18,],,,0b11,],,,0b110100,],),{,},},<EOF>''',101))

    def test_7(self):
        self.assertTrue(TestLexer.test('''Class g2X{$__(_,H,z1__x:Array [Array [Int ,076],0XC];_,Q:Int ;h:_3_;bw7Y:Array [Int ,0b100000];a:Array [Array [Array [Int ,01],34],076];q_:_){}Var _:String ;}''','''Class,g2X,{,$__,(,_,,,H,,,z1__x,:,Array,[,Array,[,Int,,,076,],,,0XC,],;,_,,,Q,:,Int,;,h,:,_3_,;,bw7Y,:,Array,[,Int,,,0b100000,],;,a,:,Array,[,Array,[,Array,[,Int,,,01,],,,34,],,,076,],;,q_,:,_,),{,},Var,_,:,String,;,},<EOF>''',101))

    def test_8(self):
        self.assertTrue(TestLexer.test('''Class __4{Constructor (_67S,zq,g,z:_8____B){Val _,Fe:H;Continue ;Return ;}Var $__:Float ;}Class _:a{L(B:W0){Break ;Continue ;} }Class W3__{}''','''Class,__4,{,Constructor,(,_67S,,,zq,,,g,,,z,:,_8____B,),{,Val,_,,,Fe,:,H,;,Continue,;,Return,;,},Var,$__,:,Float,;,},Class,_,:,a,{,L,(,B,:,W0,),{,Break,;,Continue,;,},},Class,W3__,{,},<EOF>''',101))

    def test_9(self):
        self.assertTrue(TestLexer.test('''Class U:_____7{Val $6,R:Array [Array [Boolean ,0X39_64],0B1110];}Class _2{}Class _J5:_Dqq{Constructor (k_:Array [Array [String ,04],0B1110]){} }''','''Class,U,:,_____7,{,Val,$6,,,R,:,Array,[,Array,[,Boolean,,,0X3964,],,,0B1110,],;,},Class,_2,{,},Class,_J5,:,_Dqq,{,Constructor,(,k_,:,Array,[,Array,[,String,,,04,],,,0B1110,],),{,},},<EOF>''',101))

    def test_10(self):
        self.assertTrue(TestLexer.test('''Class N1{Constructor (_,_6__6:Array [Array [Array [Array [Array [Int ,0B1],7],05],0X1A],18]){} }Class _1{}Class _{}''','''Class,N1,{,Constructor,(,_,,,_6__6,:,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0B1,],,,7,],,,05,],,,0X1A,],,,18,],),{,},},Class,_1,{,},Class,_,{,},<EOF>''',101))

    def test_11(self):
        self.assertTrue(TestLexer.test('''Class T:_6{Constructor (X8,b_:Array [Array [Array [Float ,0x4F],0b1_0],023];LMLgN,_,N:String ;_,_:Boolean ;_i:Array [Array [Array [String ,0b11_0_10_1],023],023]){Break ;Val f:Int ;Break ;}_(Jww,_2__7:String ;_:Array [Float ,0X3]){Break ;}Var $I,$l:Array [Boolean ,0x4F];}''','''Class,T,:,_6,{,Constructor,(,X8,,,b_,:,Array,[,Array,[,Array,[,Float,,,0x4F,],,,0b10,],,,023,],;,LMLgN,,,_,,,N,:,String,;,_,,,_,:,Boolean,;,_i,:,Array,[,Array,[,Array,[,String,,,0b110101,],,,023,],,,023,],),{,Break,;,Val,f,:,Int,;,Break,;,},_,(,Jww,,,_2__7,:,String,;,_,:,Array,[,Float,,,0X3,],),{,Break,;,},Var,$I,,,$l,:,Array,[,Boolean,,,0x4F,],;,},<EOF>''',101))

    def test_12(self):
        self.assertTrue(TestLexer.test('''Class __{$i(_,_,X,_0:Int ;_:Array [Array [Array [Array [Array [Float ,03],0110],81],0b1],0b1000100]){} }Class _:_{Constructor (){} }''','''Class,__,{,$i,(,_,,,_,,,X,,,_0,:,Int,;,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,03,],,,0110,],,,81,],,,0b1,],,,0b1000100,],),{,},},Class,_,:,_,{,Constructor,(,),{,},},<EOF>''',101))

    def test_13(self):
        self.assertTrue(TestLexer.test('''Class _{Constructor (){}$N(_:_g6;____3,_,_,_,_:_R;v,kdl4:Boolean ;O,t,L,l,_0:O;_:_U){} }Class _{_434p(t8,dr,D66i2_m_1Vs_7:Float ;_LrN:J;_,_,K,gf,I_4__,h:Cvu;_R:Array [String ,0x1];J:Array [Array [Float ,0B1010],1]){} }''','''Class,_,{,Constructor,(,),{,},$N,(,_,:,_g6,;,____3,,,_,,,_,,,_,,,_,:,_R,;,v,,,kdl4,:,Boolean,;,O,,,t,,,L,,,l,,,_0,:,O,;,_,:,_U,),{,},},Class,_,{,_434p,(,t8,,,dr,,,D66i2_m_1Vs_7,:,Float,;,_LrN,:,J,;,_,,,_,,,K,,,gf,,,I_4__,,,h,:,Cvu,;,_R,:,Array,[,String,,,0x1,],;,J,:,Array,[,Array,[,Float,,,0B1010,],,,1,],),{,},},<EOF>''',101))

    def test_14(self):
        self.assertTrue(TestLexer.test('''Class _:Ie{Var Dp,H,$3z,$b_88:Array [Array [Boolean ,0B1_0011],01];}Class _:b{Constructor (){}Constructor (){} }Class __{_l1_88(x_,__:__){} }''','''Class,_,:,Ie,{,Var,Dp,,,H,,,$3z,,,$b_88,:,Array,[,Array,[,Boolean,,,0B10011,],,,01,],;,},Class,_,:,b,{,Constructor,(,),{,},Constructor,(,),{,},},Class,__,{,_l1_88,(,x_,,,__,:,__,),{,},},<EOF>''',101))

    def test_15(self):
        self.assertTrue(TestLexer.test('''Class G1_3{Constructor (_,MmC_,D:_;_,__P_,__,_:Y_){Break ;} }Class _{Constructor (OP2h1b:__;N:m_B;_4:_3z;h:Int ){} }''','''Class,G1_3,{,Constructor,(,_,,,MmC_,,,D,:,_,;,_,,,__P_,,,__,,,_,:,Y_,),{,Break,;,},},Class,_,{,Constructor,(,OP2h1b,:,__,;,N,:,m_B,;,_4,:,_3z,;,h,:,Int,),{,},},<EOF>''',101))

    def test_16(self):
        self.assertTrue(TestLexer.test('''Class _:xN{}Class _U:_Q5{Var pi_:Array [Array [Float ,042],0b1];}Class _:__C{_i(e,Ys,k:Array [Array [Int ,042],042];_2_3:Array [Array [Boolean ,29],8]){} }''','''Class,_,:,xN,{,},Class,_U,:,_Q5,{,Var,pi_,:,Array,[,Array,[,Float,,,042,],,,0b1,],;,},Class,_,:,__C,{,_i,(,e,,,Ys,,,k,:,Array,[,Array,[,Int,,,042,],,,042,],;,_2_3,:,Array,[,Array,[,Boolean,,,29,],,,8,],),{,},},<EOF>''',101))

    def test_17(self):
        self.assertTrue(TestLexer.test('''Class e:_9{Val $p:M;__07(){Val __:Array [Array [Array [String ,0b1],032],0x38];}Constructor (){} }Class __{}Class c2u:_7{}''','''Class,e,:,_9,{,Val,$p,:,M,;,__07,(,),{,Val,__,:,Array,[,Array,[,Array,[,String,,,0b1,],,,032,],,,0x38,],;,},Constructor,(,),{,},},Class,__,{,},Class,c2u,:,_7,{,},<EOF>''',101))

    def test_18(self):
        self.assertTrue(TestLexer.test('''Class r{$1(_X25,__O_b:_;_48,_,g1:Int ;_:_4_Hlc){Break ;} }Class _{Var Y_:Float ;Destructor (){ {} }}Class v_{}Class K{}''','''Class,r,{,$1,(,_X25,,,__O_b,:,_,;,_48,,,_,,,g1,:,Int,;,_,:,_4_Hlc,),{,Break,;,},},Class,_,{,Var,Y_,:,Float,;,Destructor,(,),{,{,},},},Class,v_,{,},Class,K,{,},<EOF>''',101))

    def test_19(self):
        self.assertTrue(TestLexer.test('''Class uK{$2(_,_:Boolean ){Break ;}Destructor (){}Destructor (){} }Class _J:N2{Var $yo4:Array [Array [Int ,0B1101],0B1];}''','''Class,uK,{,$2,(,_,,,_,:,Boolean,),{,Break,;,},Destructor,(,),{,},Destructor,(,),{,},},Class,_J,:,N2,{,Var,$yo4,:,Array,[,Array,[,Int,,,0B1101,],,,0B1,],;,},<EOF>''',101))

    def test_20(self):
        self.assertTrue(TestLexer.test('''Class v64_E{}Class _Tj146:_{Constructor (g6I09_:Array [Array [Array [String ,0X21],27],70];J7_:Array [Int ,0B10010]){} }''','''Class,v64_E,{,},Class,_Tj146,:,_,{,Constructor,(,g6I09_,:,Array,[,Array,[,Array,[,String,,,0X21,],,,27,],,,70,],;,J7_,:,Array,[,Int,,,0B10010,],),{,},},<EOF>''',101))

    def test_21(self):
        self.assertTrue(TestLexer.test('''Class C45_:_{}Class FW_{Destructor (){Return ;}Val E_,$H_x,_A,N:Array [Array [Array [Array [Array [Array [Boolean ,0B1110],0x33],6],023],0b110110],023];}Class __:_M{Var $_,Q02wo2b_,D_:Float ;}''','''Class,C45_,:,_,{,},Class,FW_,{,Destructor,(,),{,Return,;,},Val,E_,,,$H_x,,,_A,,,N,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0B1110,],,,0x33,],,,6,],,,023,],,,0b110110,],,,023,],;,},Class,__,:,_M,{,Var,$_,,,Q02wo2b_,,,D_,:,Float,;,},<EOF>''',101))

    def test_22(self):
        self.assertTrue(TestLexer.test('''Class OB{}Class __9__{Val $NuR:Array [Array [Array [Array [Int ,0b1],75],0b1_0],75];Constructor (Q9s,Y,L:Array [Array [Float ,9],0B110];i:Array [Float ,0b1]){} }''','''Class,OB,{,},Class,__9__,{,Val,$NuR,:,Array,[,Array,[,Array,[,Array,[,Int,,,0b1,],,,75,],,,0b10,],,,75,],;,Constructor,(,Q9s,,,Y,,,L,:,Array,[,Array,[,Float,,,9,],,,0B110,],;,i,:,Array,[,Float,,,0b1,],),{,},},<EOF>''',101))

    def test_23(self):
        self.assertTrue(TestLexer.test('''Class __{}Class __{}Class _h{Constructor (){} }Class _s:T{Destructor (){} }Class m_:_{}Class h{Val $2,r,$2:C;Val _,TA:Array [Int ,0B101_11_10];Var l__n:Float ;Var $16,C_0:Array [Int ,0xB9];Destructor (){} }''','''Class,__,{,},Class,__,{,},Class,_h,{,Constructor,(,),{,},},Class,_s,:,T,{,Destructor,(,),{,},},Class,m_,:,_,{,},Class,h,{,Val,$2,,,r,,,$2,:,C,;,Val,_,,,TA,:,Array,[,Int,,,0B1011110,],;,Var,l__n,:,Float,;,Var,$16,,,C_0,:,Array,[,Int,,,0xB9,],;,Destructor,(,),{,},},<EOF>''',101))

    def test_24(self):
        self.assertTrue(TestLexer.test('''Class W__C1:t_Y{}Class _UP_A56{Constructor (q5,us:Boolean ;N_,C_,_,f8,_e,_:e;_L_:Array [Boolean ,0X27];Mv:Array [Array [Float ,03_7],60];VBv,i9__,_u_:a;H_:Di){Break ;} }''','''Class,W__C1,:,t_Y,{,},Class,_UP_A56,{,Constructor,(,q5,,,us,:,Boolean,;,N_,,,C_,,,_,,,f8,,,_e,,,_,:,e,;,_L_,:,Array,[,Boolean,,,0X27,],;,Mv,:,Array,[,Array,[,Float,,,037,],,,60,],;,VBv,,,i9__,,,_u_,:,a,;,H_,:,Di,),{,Break,;,},},<EOF>''',101))

    def test_25(self):
        self.assertTrue(TestLexer.test('''Class _{$T_1(){} }Class _{Val _,n79,q:Array [Array [Int ,0x1E],036];}Class ___4{Var $_,_2_:Array [Int ,036];Destructor (){} }Class B__:_{}Class k:d{}Class i{}''','''Class,_,{,$T_1,(,),{,},},Class,_,{,Val,_,,,n79,,,q,:,Array,[,Array,[,Int,,,0x1E,],,,036,],;,},Class,___4,{,Var,$_,,,_2_,:,Array,[,Int,,,036,],;,Destructor,(,),{,},},Class,B__,:,_,{,},Class,k,:,d,{,},Class,i,{,},<EOF>''',101))

    def test_26(self):
        self.assertTrue(TestLexer.test('''Class _0{Constructor (z:Array [Array [Array [Array [Array [Float ,0X6],0x16],0x7],64],64];_d6t_2,_,_,J_r8,x:_;_:z__24;p_:Boolean ){Break ;}$_(){ {} }}''','''Class,_0,{,Constructor,(,z,:,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0X6,],,,0x16,],,,0x7,],,,64,],,,64,],;,_d6t_2,,,_,,,_,,,J_r8,,,x,:,_,;,_,:,z__24,;,p_,:,Boolean,),{,Break,;,},$_,(,),{,{,},},},<EOF>''',101))

    def test_27(self):
        self.assertTrue(TestLexer.test('''Class d:nY{}Class _02{Val $9,_:_7;Destructor (){_::$___();}Constructor (){} }Class _{}Class W:_{Var $_:Boolean ;Destructor (){} }''','''Class,d,:,nY,{,},Class,_02,{,Val,$9,,,_,:,_7,;,Destructor,(,),{,_,::,$___,(,),;,},Constructor,(,),{,},},Class,_,{,},Class,W,:,_,{,Var,$_,:,Boolean,;,Destructor,(,),{,},},<EOF>''',101))

    def test_28(self):
        self.assertTrue(TestLexer.test('''Class _:_r3Gy8_59YI{Constructor (I:Array [Array [Array [Array [Array [Boolean ,0106],03_6],0B100_1],55],0B1000111]){} }''','''Class,_,:,_r3Gy8_59YI,{,Constructor,(,I,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0106,],,,036,],,,0B1001,],,,55,],,,0B1000111,],),{,},},<EOF>''',101))

    def test_29(self):
        self.assertTrue(TestLexer.test('''Class _:_{}Class T{Q(){}Constructor (){}Var $0:Array [Array [Array [Array [String ,0X2_4],36_7_9],0x27],0X9_D];__(){} }''','''Class,_,:,_,{,},Class,T,{,Q,(,),{,},Constructor,(,),{,},Var,$0,:,Array,[,Array,[,Array,[,Array,[,String,,,0X24,],,,3679,],,,0x27,],,,0X9D,],;,__,(,),{,},},<EOF>''',101))

    def test_30(self):
        self.assertTrue(TestLexer.test('''Class l:_{Var $_,$3:Boolean ;}Class j{Constructor (B,g4y,_:_;x6_,M:_PN5;_,W,_G__m,_9__,o:l83;e5,__4__,_,L,_:A){Var _,WM9:_;} }Class _M__M{}Class B:_2c{}''','''Class,l,:,_,{,Var,$_,,,$3,:,Boolean,;,},Class,j,{,Constructor,(,B,,,g4y,,,_,:,_,;,x6_,,,M,:,_PN5,;,_,,,W,,,_G__m,,,_9__,,,o,:,l83,;,e5,,,__4__,,,_,,,L,,,_,:,A,),{,Var,_,,,WM9,:,_,;,},},Class,_M__M,{,},Class,B,:,_2c,{,},<EOF>''',101))

    def test_31(self):
        self.assertTrue(TestLexer.test('''Class _o:_6{Constructor (){}Val _1_,$a:Array [Array [Array [Boolean ,0b1],0b1_0_0_10],0B1];Val $6,$nu:Float ;}''','''Class,_o,:,_6,{,Constructor,(,),{,},Val,_1_,,,$a,:,Array,[,Array,[,Array,[,Boolean,,,0b1,],,,0b10010,],,,0B1,],;,Val,$6,,,$nu,:,Float,;,},<EOF>''',101))

    def test_32(self):
        self.assertTrue(TestLexer.test('''Class g:Z{__(i:Array [Array [Array [Array [Float ,0B1100000],0B1100000],72],6]){Continue ;Continue ;} }Class R:_{_y(){_::$0_()._1();Continue ;} }''','''Class,g,:,Z,{,__,(,i,:,Array,[,Array,[,Array,[,Array,[,Float,,,0B1100000,],,,0B1100000,],,,72,],,,6,],),{,Continue,;,Continue,;,},},Class,R,:,_,{,_y,(,),{,_,::,$0_,(,),.,_1,(,),;,Continue,;,},},<EOF>''',101))

    def test_33(self):
        self.assertTrue(TestLexer.test('''Class _:_{}Class I__8s:xG{Constructor (Qn9:Array [Array [Array [Array [Array [Array [Array [Array [Boolean ,0X73_E],0x4E],7_516],0120],11],0b1010100],0X8],6]){} }''','''Class,_,:,_,{,},Class,I__8s,:,xG,{,Constructor,(,Qn9,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0X73E,],,,0x4E,],,,7516,],,,0120,],,,11,],,,0b1010100,],,,0X8,],,,6,],),{,},},<EOF>''',101))

    def test_34(self):
        self.assertTrue(TestLexer.test('''Class X6:_9{Constructor (r6z:Float ;g3_G_3V,____,a5_,i,t3,E_:Array [Float ,0B1_0]){}Destructor (){Break ;} }Class _:_{Destructor (){}Destructor (){Break ;} }''','''Class,X6,:,_9,{,Constructor,(,r6z,:,Float,;,g3_G_3V,,,____,,,a5_,,,i,,,t3,,,E_,:,Array,[,Float,,,0B10,],),{,},Destructor,(,),{,Break,;,},},Class,_,:,_,{,Destructor,(,),{,},Destructor,(,),{,Break,;,},},<EOF>''',101))

    def test_35(self):
        self.assertTrue(TestLexer.test('''Class _{Constructor (n,D1,fqg,__,nch,R,t:Array [Array [Array [Boolean ,89],0X5],6];a:String ){Return ;}$1____(qa:Float ;_3_,_:Array [Array [Array [Array [String ,0B1_0],9],0123],89];_:Array [Array [Array [Int ,07],0X7],03]){} }''','''Class,_,{,Constructor,(,n,,,D1,,,fqg,,,__,,,nch,,,R,,,t,:,Array,[,Array,[,Array,[,Boolean,,,89,],,,0X5,],,,6,],;,a,:,String,),{,Return,;,},$1____,(,qa,:,Float,;,_3_,,,_,:,Array,[,Array,[,Array,[,Array,[,String,,,0B10,],,,9,],,,0123,],,,89,],;,_,:,Array,[,Array,[,Array,[,Int,,,07,],,,0X7,],,,03,],),{,},},<EOF>''',101))

    def test_36(self):
        self.assertTrue(TestLexer.test('''Class _1_:_vr{Var v:Array [Array [Array [Array [Array [Array [Array [Array [Boolean ,2_574],0b100001],05_4],0B1_0],1],062],5],062];}''','''Class,_1_,:,_vr,{,Var,v,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,2574,],,,0b100001,],,,054,],,,0B10,],,,1,],,,062,],,,5,],,,062,],;,},<EOF>''',101))

    def test_37(self):
        self.assertTrue(TestLexer.test('''Class ___{Var J,$4,$L:Int ;Constructor (A,b__l1_:Array [Int ,067];m,V_c__,Q4,_,__,_5:String ){}Constructor (_v_:Boolean ){Var _:Array [Array [Array [Array [Array [Int ,16],0B1],0xE],0b1],0B110110];}Var _7,$__:_;}Class _{}''','''Class,___,{,Var,J,,,$4,,,$L,:,Int,;,Constructor,(,A,,,b__l1_,:,Array,[,Int,,,067,],;,m,,,V_c__,,,Q4,,,_,,,__,,,_5,:,String,),{,},Constructor,(,_v_,:,Boolean,),{,Var,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,16,],,,0B1,],,,0xE,],,,0b1,],,,0B110110,],;,},Var,_7,,,$__,:,_,;,},Class,_,{,},<EOF>''',101))

    def test_38(self):
        self.assertTrue(TestLexer.test('''Class _398t{}Class _:_k{Constructor (){Break ;} }Class _2_:__{$s(_R,g1,M___,_o:Array [String ,0B10101]){}Val $v:Array [Float ,0b1];Val $74,$Y:String ;}''','''Class,_398t,{,},Class,_,:,_k,{,Constructor,(,),{,Break,;,},},Class,_2_,:,__,{,$s,(,_R,,,g1,,,M___,,,_o,:,Array,[,String,,,0B10101,],),{,},Val,$v,:,Array,[,Float,,,0b1,],;,Val,$74,,,$Y,:,String,;,},<EOF>''',101))

    def test_39(self):
        self.assertTrue(TestLexer.test('''Class _{Constructor (F,u,V:Int ;_,I,_,q,mi:Array [Float ,04_3_043];_9:_;_:Array [Array [Array [Boolean ,0112],0b1],07_700];Sp__,ku,__:Int ;_,j0_w23,_5D,H:Array [String ,6];G,_A6q,_,O62,_8,_,_K4:Boolean ;_3:_){} }Class u_{$_(t8E_,q,I_,__,_,_:b;NU_E:String ;a_,k_7:_5;O_0,W_:Float ){} }''','''Class,_,{,Constructor,(,F,,,u,,,V,:,Int,;,_,,,I,,,_,,,q,,,mi,:,Array,[,Float,,,043043,],;,_9,:,_,;,_,:,Array,[,Array,[,Array,[,Boolean,,,0112,],,,0b1,],,,07700,],;,Sp__,,,ku,,,__,:,Int,;,_,,,j0_w23,,,_5D,,,H,:,Array,[,String,,,6,],;,G,,,_A6q,,,_,,,O62,,,_8,,,_,,,_K4,:,Boolean,;,_3,:,_,),{,},},Class,u_,{,$_,(,t8E_,,,q,,,I_,,,__,,,_,,,_,:,b,;,NU_E,:,String,;,a_,,,k_7,:,_5,;,O_0,,,W_,:,Float,),{,},},<EOF>''',101))

    def test_40(self):
        self.assertTrue(TestLexer.test('''Class _:G{Val z:Float ;$37_(_:String ;_:Array [Array [Array [Array [Int ,68],041],15],0B1_11]){}Destructor (){}Constructor (_:_C){} }''','''Class,_,:,G,{,Val,z,:,Float,;,$37_,(,_,:,String,;,_,:,Array,[,Array,[,Array,[,Array,[,Int,,,68,],,,041,],,,15,],,,0B111,],),{,},Destructor,(,),{,},Constructor,(,_,:,_C,),{,},},<EOF>''',101))

    def test_41(self):
        self.assertTrue(TestLexer.test('''Class _e:C{Destructor (){} }Class _mwk{}Class NKQ:Rc1{$9(S7:__i;O:Array [Boolean ,0110]){}Val __:_;Destructor (){}Var $_,__1:e;}Class _k{Val $O,D,_:NU1_6_770;}''','''Class,_e,:,C,{,Destructor,(,),{,},},Class,_mwk,{,},Class,NKQ,:,Rc1,{,$9,(,S7,:,__i,;,O,:,Array,[,Boolean,,,0110,],),{,},Val,__,:,_,;,Destructor,(,),{,},Var,$_,,,__1,:,e,;,},Class,_k,{,Val,$O,,,D,,,_,:,NU1_6_770,;,},<EOF>''',101))

    def test_42(self):
        self.assertTrue(TestLexer.test('''Class _{}Class K_O{Val v8,A:_u_;}Class __{Constructor (_T3Z_4:x3H){}Constructor (){}Destructor (){ {} }Destructor (){ {{Break ;}ri::$Y_9();} }}Class _:G{}''','''Class,_,{,},Class,K_O,{,Val,v8,,,A,:,_u_,;,},Class,__,{,Constructor,(,_T3Z_4,:,x3H,),{,},Constructor,(,),{,},Destructor,(,),{,{,},},Destructor,(,),{,{,{,Break,;,},ri,::,$Y_9,(,),;,},},},Class,_,:,G,{,},<EOF>''',101))

    def test_43(self):
        self.assertTrue(TestLexer.test('''Class _{}Class _{__(_H5E_Z_,_,I:Float ;q:Array [Array [Float ,05],9_42];___64_,__p:Boolean ;Z:Array [Array [Float ,7_6_2],03];_,_:Array [Int ,63]){} }Class _{_(){ {} }Destructor (){Continue ;Continue ;} }''','''Class,_,{,},Class,_,{,__,(,_H5E_Z_,,,_,,,I,:,Float,;,q,:,Array,[,Array,[,Float,,,05,],,,942,],;,___64_,,,__p,:,Boolean,;,Z,:,Array,[,Array,[,Float,,,762,],,,03,],;,_,,,_,:,Array,[,Int,,,63,],),{,},},Class,_,{,_,(,),{,{,},},Destructor,(,),{,Continue,;,Continue,;,},},<EOF>''',101))

    def test_44(self):
        self.assertTrue(TestLexer.test('''Class _1__7{}Class zCFi:____{Destructor (){g_::$4_();}Val _1,$T3:Float ;Val W,$_9:Array [Int ,0X34];}Class _:Y{Constructor (_,c9,o_9:J){} }Class N:__{}''','''Class,_1__7,{,},Class,zCFi,:,____,{,Destructor,(,),{,g_,::,$4_,(,),;,},Val,_1,,,$T3,:,Float,;,Val,W,,,$_9,:,Array,[,Int,,,0X34,],;,},Class,_,:,Y,{,Constructor,(,_,,,c9,,,o_9,:,J,),{,},},Class,N,:,__,{,},<EOF>''',101))

    def test_45(self):
        self.assertTrue(TestLexer.test('''Class _4_{Constructor (_,__,_,v__,H,d:__;_,nL19_,mL_,D_u7l,T,_n:Array [Array [Array [Array [Float ,0x5D],013],87],0x1]){} }Class q{_l_(){} }Class _{}Class _:_{Val _:Array [Array [Boolean ,5],0x5D];}Class _8{Constructor (i:Array [Array [Array [Array [Array [Array [String ,047],0B1],047],0xA],0XD9_9D_C_8_0_F],7];jd:Array [Array [Array [Float ,0X5E],87],047];_5:Array [Array [Boolean ,6],0X5E];_T,S,_:String ;_x,E_57:_){} }''','''Class,_4_,{,Constructor,(,_,,,__,,,_,,,v__,,,H,,,d,:,__,;,_,,,nL19_,,,mL_,,,D_u7l,,,T,,,_n,:,Array,[,Array,[,Array,[,Array,[,Float,,,0x5D,],,,013,],,,87,],,,0x1,],),{,},},Class,q,{,_l_,(,),{,},},Class,_,{,},Class,_,:,_,{,Val,_,:,Array,[,Array,[,Boolean,,,5,],,,0x5D,],;,},Class,_8,{,Constructor,(,i,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,047,],,,0B1,],,,047,],,,0xA,],,,0XD99DC80F,],,,7,],;,jd,:,Array,[,Array,[,Array,[,Float,,,0X5E,],,,87,],,,047,],;,_5,:,Array,[,Array,[,Boolean,,,6,],,,0X5E,],;,_T,,,S,,,_,:,String,;,_x,,,E_57,:,_,),{,},},<EOF>''',101))

    def test_46(self):
        self.assertTrue(TestLexer.test('''Class __{Constructor (o_,_,t4N:Boolean ;__,S_:Array [Array [Float ,0X25],62];o__,H,R,i_96_,_,eO,m0:F8;H:Array [Array [Float ,0x3A],0X6B_6]){}Val r:Array [Int ,0x3A];}''','''Class,__,{,Constructor,(,o_,,,_,,,t4N,:,Boolean,;,__,,,S_,:,Array,[,Array,[,Float,,,0X25,],,,62,],;,o__,,,H,,,R,,,i_96_,,,_,,,eO,,,m0,:,F8,;,H,:,Array,[,Array,[,Float,,,0x3A,],,,0X6B6,],),{,},Val,r,:,Array,[,Int,,,0x3A,],;,},<EOF>''',101))

    def test_47(self):
        self.assertTrue(TestLexer.test('''Class s:R{Constructor (n:Float ){}_(){}Constructor (v2,c__7,i2:Int ;_j,v:Array [Array [String ,0x5D],2_67]){} }Class __JmE:y_4_6{Var $Z__5:Array [Array [Float ,55],0X35];}''','''Class,s,:,R,{,Constructor,(,n,:,Float,),{,},_,(,),{,},Constructor,(,v2,,,c__7,,,i2,:,Int,;,_j,,,v,:,Array,[,Array,[,String,,,0x5D,],,,267,],),{,},},Class,__JmE,:,y_4_6,{,Var,$Z__5,:,Array,[,Array,[,Float,,,55,],,,0X35,],;,},<EOF>''',101))

    def test_48(self):
        self.assertTrue(TestLexer.test('''Class _{L_(I6LL:e;__0_,h__,_:__){}Constructor (){}Destructor (){} }Class Oam:_4{}Class _{Val V:c;Destructor (){} }Class _1{}''','''Class,_,{,L_,(,I6LL,:,e,;,__0_,,,h__,,,_,:,__,),{,},Constructor,(,),{,},Destructor,(,),{,},},Class,Oam,:,_4,{,},Class,_,{,Val,V,:,c,;,Destructor,(,),{,},},Class,_1,{,},<EOF>''',101))

    def test_49(self):
        self.assertTrue(TestLexer.test('''Class _:_A{}Class A_{Var L:Array [Array [Array [Float ,40_4],1],6_9];Constructor (){Break ;}Var __,_,_iX:E;$9(){} }''','''Class,_,:,_A,{,},Class,A_,{,Var,L,:,Array,[,Array,[,Array,[,Float,,,404,],,,1,],,,69,],;,Constructor,(,),{,Break,;,},Var,__,,,_,,,_iX,:,E,;,$9,(,),{,},},<EOF>''',101))

    def test_50(self):
        self.assertTrue(TestLexer.test('''Class _8078:__{Destructor (){}Bv9(g,_U,_Vao,Kw,_,_M13B62_,bv:O){} }Class j{}Class _392_78:_35{Var _:_;Destructor (){Return ;} }Class _2:_{$47_b6(){} }''','''Class,_8078,:,__,{,Destructor,(,),{,},Bv9,(,g,,,_U,,,_Vao,,,Kw,,,_,,,_M13B62_,,,bv,:,O,),{,},},Class,j,{,},Class,_392_78,:,_35,{,Var,_,:,_,;,Destructor,(,),{,Return,;,},},Class,_2,:,_,{,$47_b6,(,),{,},},<EOF>''',101))

    def test_51(self):
        self.assertTrue(TestLexer.test('''Class _:G{}Class D9A:_{}Class _H9_2_{Destructor (){}_(){Return ;}Constructor (__P_4,w96,p_8:Int ;dm,O,_Z23Y77Y:_;B,T_:String ){} }''','''Class,_,:,G,{,},Class,D9A,:,_,{,},Class,_H9_2_,{,Destructor,(,),{,},_,(,),{,Return,;,},Constructor,(,__P_4,,,w96,,,p_8,:,Int,;,dm,,,O,,,_Z23Y77Y,:,_,;,B,,,T_,:,String,),{,},},<EOF>''',101))

    def test_52(self):
        self.assertTrue(TestLexer.test('''Class l{}Class S{}Class _{Val $_11__,$d,$X:Array [Array [Array [Array [Array [Array [Float ,0X6],0b11100],05],0B11_11],0B1],0x18];Destructor (){Break ;}Var _02_I_:e;}Class kN{}''','''Class,l,{,},Class,S,{,},Class,_,{,Val,$_11__,,,$d,,,$X,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0X6,],,,0b11100,],,,05,],,,0B1111,],,,0B1,],,,0x18,],;,Destructor,(,),{,Break,;,},Var,_02_I_,:,e,;,},Class,kN,{,},<EOF>''',101))

    def test_53(self):
        self.assertTrue(TestLexer.test('''Class _:t{Constructor (){} }Class _:_{Destructor (){Return ;}$_8(ew,Z:Boolean ;J:e;_5F_8_69_G:Array [Array [String ,0b1],0B1011111]){} }Class gv_:_0{}Class _:d_{}Class e_{}Class _{}Class L:_{}''','''Class,_,:,t,{,Constructor,(,),{,},},Class,_,:,_,{,Destructor,(,),{,Return,;,},$_8,(,ew,,,Z,:,Boolean,;,J,:,e,;,_5F_8_69_G,:,Array,[,Array,[,String,,,0b1,],,,0B1011111,],),{,},},Class,gv_,:,_0,{,},Class,_,:,d_,{,},Class,e_,{,},Class,_,{,},Class,L,:,_,{,},<EOF>''',101))

    def test_54(self):
        self.assertTrue(TestLexer.test('''Class _:_7{Constructor (L:_3g;S__,__:Array [Array [Array [Boolean ,0xD8_F],0b1100000],042]){}Constructor (a:String ){Return ;O::$q();} }''','''Class,_,:,_7,{,Constructor,(,L,:,_3g,;,S__,,,__,:,Array,[,Array,[,Array,[,Boolean,,,0xD8F,],,,0b1100000,],,,042,],),{,},Constructor,(,a,:,String,),{,Return,;,O,::,$q,(,),;,},},<EOF>''',101))

    def test_55(self):
        self.assertTrue(TestLexer.test('''Class _:_{}Class __2{}Class _w:qv{}Class b{}Class _Z{Constructor (_Qb_7:__73_N;_,_0_6,Z:_){}Destructor (){} }''','''Class,_,:,_,{,},Class,__2,{,},Class,_w,:,qv,{,},Class,b,{,},Class,_Z,{,Constructor,(,_Qb_7,:,__73_N,;,_,,,_0_6,,,Z,:,_,),{,},Destructor,(,),{,},},<EOF>''',101))

    def test_56(self):
        self.assertTrue(TestLexer.test('''Class ls___{Constructor (){}Val E:_;Destructor (){}_(A2:Int ;_5:_;_,F,_z,j_:_6;_E_6:Array [Array [String ,0x6_1],0b1001];_u1,_:_){ {} }}Class _D{}Class _{}''','''Class,ls___,{,Constructor,(,),{,},Val,E,:,_,;,Destructor,(,),{,},_,(,A2,:,Int,;,_5,:,_,;,_,,,F,,,_z,,,j_,:,_6,;,_E_6,:,Array,[,Array,[,String,,,0x61,],,,0b1001,],;,_u1,,,_,:,_,),{,{,},},},Class,_D,{,},Class,_,{,},<EOF>''',101))

    def test_57(self):
        self.assertTrue(TestLexer.test('''Class _q{Destructor (){}Var J_9,__:W_3RW;Destructor (){} }Class _V{Var $587:String ;D1(_S:_){Return ;Continue ;} }Class Q{}''','''Class,_q,{,Destructor,(,),{,},Var,J_9,,,__,:,W_3RW,;,Destructor,(,),{,},},Class,_V,{,Var,$587,:,String,;,D1,(,_S,:,_,),{,Return,;,Continue,;,},},Class,Q,{,},<EOF>''',101))

    def test_58(self):
        self.assertTrue(TestLexer.test('''Class _V4{Constructor (){.79E1._75._._h();} }Class m{Var $s,r,$_T,__,_:_;Constructor (){} }Class a:_z5{}Class h_9__z{}Class _751:_{}''','''Class,_V4,{,Constructor,(,),{,.79E1,.,_75,.,_,.,_h,(,),;,},},Class,m,{,Var,$s,,,r,,,$_T,,,__,,,_,:,_,;,Constructor,(,),{,},},Class,a,:,_z5,{,},Class,h_9__z,{,},Class,_751,:,_,{,},<EOF>''',101))

    def test_59(self):
        self.assertTrue(TestLexer.test('''Class _o{Var $_5:Array [Int ,5];Val A:Float ;}Class _:H{Var $__9:_Q;Var $Z3b:Array [Array [Boolean ,0b100_1_1],0b1];Val $6:String ;Var x0:Boolean ;___(z,t:Float ;X,_P,M:Int ){} }''','''Class,_o,{,Var,$_5,:,Array,[,Int,,,5,],;,Val,A,:,Float,;,},Class,_,:,H,{,Var,$__9,:,_Q,;,Var,$Z3b,:,Array,[,Array,[,Boolean,,,0b10011,],,,0b1,],;,Val,$6,:,String,;,Var,x0,:,Boolean,;,___,(,z,,,t,:,Float,;,X,,,_P,,,M,:,Int,),{,},},<EOF>''',101))

    def test_60(self):
        self.assertTrue(TestLexer.test('''Class v{Val $2r,i5,$3_2,$6:Array [Array [String ,1_8],07];$8(_0695,_32_:_){} }Class J_3b0:_{Constructor (){}Constructor (V:Array [Array [String ,0xF_D_5],03];L:Int ;_r,ij,_:O;T:String ){Continue ;}Destructor (){} }''','''Class,v,{,Val,$2r,,,i5,,,$3_2,,,$6,:,Array,[,Array,[,String,,,18,],,,07,],;,$8,(,_0695,,,_32_,:,_,),{,},},Class,J_3b0,:,_,{,Constructor,(,),{,},Constructor,(,V,:,Array,[,Array,[,String,,,0xFD5,],,,03,],;,L,:,Int,;,_r,,,ij,,,_,:,O,;,T,:,String,),{,Continue,;,},Destructor,(,),{,},},<EOF>''',101))

    def test_61(self):
        self.assertTrue(TestLexer.test('''Class _:p{Val _x:Float ;Constructor (){}Var _78,P4020:Boolean ;}Class _:v{Val N,$_:Array [Boolean ,03];}Class B_q:H6_{}''','''Class,_,:,p,{,Val,_x,:,Float,;,Constructor,(,),{,},Var,_78,,,P4020,:,Boolean,;,},Class,_,:,v,{,Val,N,,,$_,:,Array,[,Boolean,,,03,],;,},Class,B_q,:,H6_,{,},<EOF>''',101))

    def test_62(self):
        self.assertTrue(TestLexer.test('''Class _75_{Constructor (){ {} }Constructor (_5_wF:__){}Z(_3,_:Array [Array [Array [Array [Array [Int ,16],03],0x9],0x9F],0x2F];_:_;_g2G,E6_46_T:String ){}Val _:Float ;}Class G8{}''','''Class,_75_,{,Constructor,(,),{,{,},},Constructor,(,_5_wF,:,__,),{,},Z,(,_3,,,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,16,],,,03,],,,0x9,],,,0x9F,],,,0x2F,],;,_,:,_,;,_g2G,,,E6_46_T,:,String,),{,},Val,_,:,Float,;,},Class,G8,{,},<EOF>''',101))

    def test_63(self):
        self.assertTrue(TestLexer.test('''Class __{Constructor (){} }Class c_:Y_n7a{Destructor (){} }Class _:N5__{Val $_,$0_:Int ;Constructor (g,_2mMI,_,i:_9C){}I(){_4::$8();}Val $719e:Float ;}''','''Class,__,{,Constructor,(,),{,},},Class,c_,:,Y_n7a,{,Destructor,(,),{,},},Class,_,:,N5__,{,Val,$_,,,$0_,:,Int,;,Constructor,(,g,,,_2mMI,,,_,,,i,:,_9C,),{,},I,(,),{,_4,::,$8,(,),;,},Val,$719e,:,Float,;,},<EOF>''',101))

    def test_64(self):
        self.assertTrue(TestLexer.test('''Class W{Val $8,_5WZ17,_:Boolean ;d(){} }Class c:h{Constructor (W,_9_,tS__,I:Int ;I,i_9gD,_7_H:Int ;Q:Ef;_,X:Array [Array [Array [Boolean ,0xC0],0x1],48];D0,E,__4,U__5_:Array [Float ,8_9]){}Var _6K_:Float ;}Class NVc{Val $M:Boolean ;}''','''Class,W,{,Val,$8,,,_5WZ17,,,_,:,Boolean,;,d,(,),{,},},Class,c,:,h,{,Constructor,(,W,,,_9_,,,tS__,,,I,:,Int,;,I,,,i_9gD,,,_7_H,:,Int,;,Q,:,Ef,;,_,,,X,:,Array,[,Array,[,Array,[,Boolean,,,0xC0,],,,0x1,],,,48,],;,D0,,,E,,,__4,,,U__5_,:,Array,[,Float,,,89,],),{,},Var,_6K_,:,Float,;,},Class,NVc,{,Val,$M,:,Boolean,;,},<EOF>''',101))

    def test_65(self):
        self.assertTrue(TestLexer.test('''Class __:_e{$0_(y49_4:Array [Array [Array [Array [Boolean ,02],055],0B1001010],0B1_0]){}Var _Z9__:Array [Array [Array [Boolean ,0B1001010],0b10_0],81];}''','''Class,__,:,_e,{,$0_,(,y49_4,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,02,],,,055,],,,0B1001010,],,,0B10,],),{,},Var,_Z9__,:,Array,[,Array,[,Array,[,Boolean,,,0B1001010,],,,0b100,],,,81,],;,},<EOF>''',101))

    def test_66(self):
        self.assertTrue(TestLexer.test('''Class _:_K8{Destructor (){} }Class ji:j{Val $u:Array [Array [Array [Array [Float ,07],0B1],0b1_0],5];}Class _87:E7{}Class X9A{Val _n1E:v_;}''','''Class,_,:,_K8,{,Destructor,(,),{,},},Class,ji,:,j,{,Val,$u,:,Array,[,Array,[,Array,[,Array,[,Float,,,07,],,,0B1,],,,0b10,],,,5,],;,},Class,_87,:,E7,{,},Class,X9A,{,Val,_n1E,:,v_,;,},<EOF>''',101))

    def test_67(self):
        self.assertTrue(TestLexer.test('''Class J_7C:b{Val y333,b,VG_4:Array [Array [Boolean ,0B1010111],0x22];Constructor (___:Array [Array [Boolean ,0xA_A],1_8_7];_S_:_Jp){Val C_1T:Int ;Continue ;} }''','''Class,J_7C,:,b,{,Val,y333,,,b,,,VG_4,:,Array,[,Array,[,Boolean,,,0B1010111,],,,0x22,],;,Constructor,(,___,:,Array,[,Array,[,Boolean,,,0xAA,],,,187,],;,_S_,:,_Jp,),{,Val,C_1T,:,Int,;,Continue,;,},},<EOF>''',101))

    def test_68(self):
        self.assertTrue(TestLexer.test('''Class c_7:_t{Var _JB:_f;Val $4p:_;Var _,$_O8,$Q_,y:String ;}Class _:__{Constructor (iBk:Array [Array [Array [Array [Int ,41],0B11],8],0B111100]){} }Class __:_4{}''','''Class,c_7,:,_t,{,Var,_JB,:,_f,;,Val,$4p,:,_,;,Var,_,,,$_O8,,,$Q_,,,y,:,String,;,},Class,_,:,__,{,Constructor,(,iBk,:,Array,[,Array,[,Array,[,Array,[,Int,,,41,],,,0B11,],,,8,],,,0B111100,],),{,},},Class,__,:,_4,{,},<EOF>''',101))

    def test_69(self):
        self.assertTrue(TestLexer.test('''Class Y99_:y_6{Destructor (){}Constructor (q6Rw:Float ){_K::$6_();}Constructor (J:V8_;_v1_p,X_:String ;___,_Z:Array [Array [Float ,0x16],0X52]){} }Class ___n6{}''','''Class,Y99_,:,y_6,{,Destructor,(,),{,},Constructor,(,q6Rw,:,Float,),{,_K,::,$6_,(,),;,},Constructor,(,J,:,V8_,;,_v1_p,,,X_,:,String,;,___,,,_Z,:,Array,[,Array,[,Float,,,0x16,],,,0X52,],),{,},},Class,___n6,{,},<EOF>''',101))

    def test_70(self):
        self.assertTrue(TestLexer.test('''Class Qk:__{___(_M,_,__t_,n:Int ;_,j:Array [Float ,0b1];g_9m_:Array [Array [Float ,10],0b1];_,B:Float ;__:Float ){Break ;} }''','''Class,Qk,:,__,{,___,(,_M,,,_,,,__t_,,,n,:,Int,;,_,,,j,:,Array,[,Float,,,0b1,],;,g_9m_,:,Array,[,Array,[,Float,,,10,],,,0b1,],;,_,,,B,:,Float,;,__,:,Float,),{,Break,;,},},<EOF>''',101))

    def test_71(self):
        self.assertTrue(TestLexer.test('''Class I{}Class C{X_B4_H(H:_;_,__:Float ){Break ;}Constructor (__:String ;_,ly,_,_,__k__1,Q:_W_47){}Var z_sx_,$_:Float ;}''','''Class,I,{,},Class,C,{,X_B4_H,(,H,:,_,;,_,,,__,:,Float,),{,Break,;,},Constructor,(,__,:,String,;,_,,,ly,,,_,,,_,,,__k__1,,,Q,:,_W_47,),{,},Var,z_sx_,,,$_,:,Float,;,},<EOF>''',101))

    def test_72(self):
        self.assertTrue(TestLexer.test('''Class Z{Var C:Boolean ;}Class _{}Class _Fw_2v:_{Var $t13:Float ;U66_(){}Val $b_,I:_;}Class _8:E{}Class ___T32rZZ:__2{Var __r,$Jv:Array [Int ,0B1100100];}Class R2:d67e{}Class _{___4A(){} }''','''Class,Z,{,Var,C,:,Boolean,;,},Class,_,{,},Class,_Fw_2v,:,_,{,Var,$t13,:,Float,;,U66_,(,),{,},Val,$b_,,,I,:,_,;,},Class,_8,:,E,{,},Class,___T32rZZ,:,__2,{,Var,__r,,,$Jv,:,Array,[,Int,,,0B1100100,],;,},Class,R2,:,d67e,{,},Class,_,{,___4A,(,),{,},},<EOF>''',101))

    def test_73(self):
        self.assertTrue(TestLexer.test('''Class t{Destructor (){}Constructor (_,_,N__,_:Array [Array [Array [Array [Boolean ,03],20],0XC6],067];_8m:_9){}Val $0:Int ;}''','''Class,t,{,Destructor,(,),{,},Constructor,(,_,,,_,,,N__,,,_,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,03,],,,20,],,,0XC6,],,,067,],;,_8m,:,_9,),{,},Val,$0,:,Int,;,},<EOF>''',101))

    def test_74(self):
        self.assertTrue(TestLexer.test('''Class _{Var $__7:Array [Int ,42];Var $628,$_7D:Array [Array [Int ,0x3D],0X57D7B];}Class b{}Class l:z{z7_1(_,p_,K3Y0:Array [Int ,1_7_8_7]){} }Class _2kw{}''','''Class,_,{,Var,$__7,:,Array,[,Int,,,42,],;,Var,$628,,,$_7D,:,Array,[,Array,[,Int,,,0x3D,],,,0X57D7B,],;,},Class,b,{,},Class,l,:,z,{,z7_1,(,_,,,p_,,,K3Y0,:,Array,[,Int,,,1787,],),{,},},Class,_2kw,{,},<EOF>''',101))

    def test_75(self):
        self.assertTrue(TestLexer.test('''Class A_:x{Destructor (){ {_::$68t_();Break ;} }Val $ld,$y,W:Array [Array [Array [Array [Boolean ,4],0X3B],02_5],0B1011000];}Class Pq{}''','''Class,A_,:,x,{,Destructor,(,),{,{,_,::,$68t_,(,),;,Break,;,},},Val,$ld,,,$y,,,W,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,4,],,,0X3B,],,,025,],,,0B1011000,],;,},Class,Pq,{,},<EOF>''',101))

    def test_76(self):
        self.assertTrue(TestLexer.test('''Class _{}Class krD_{Destructor (){}Var $B_,v1_:Array [Array [String ,025],025];}Class _{_5I(){} }Class _0J_B_:o{Constructor (_,_,o_,__:Array [Array [String ,9],0XA]){Continue ;Return ;}Var $_,g,_1,p:Int ;}''','''Class,_,{,},Class,krD_,{,Destructor,(,),{,},Var,$B_,,,v1_,:,Array,[,Array,[,String,,,025,],,,025,],;,},Class,_,{,_5I,(,),{,},},Class,_0J_B_,:,o,{,Constructor,(,_,,,_,,,o_,,,__,:,Array,[,Array,[,String,,,9,],,,0XA,],),{,Continue,;,Return,;,},Var,$_,,,g,,,_1,,,p,:,Int,;,},<EOF>''',101))

    def test_77(self):
        self.assertTrue(TestLexer.test('''Class N_{}Class g:D_Y_{Val $N_Dd,K7:Array [Array [Int ,5_13],36];Destructor (){} }Class Z:__5{Var $NMA_O__:Rjy9BUq;}Class M{}''','''Class,N_,{,},Class,g,:,D_Y_,{,Val,$N_Dd,,,K7,:,Array,[,Array,[,Int,,,513,],,,36,],;,Destructor,(,),{,},},Class,Z,:,__5,{,Var,$NMA_O__,:,Rjy9BUq,;,},Class,M,{,},<EOF>''',101))

    def test_78(self):
        self.assertTrue(TestLexer.test('''Class _:H{Destructor (){} }Class x:_{Constructor (_:w;_,___1,_:T;_:k4;_:Array [Array [Boolean ,0B1000100],0b1_0]){} }''','''Class,_,:,H,{,Destructor,(,),{,},},Class,x,:,_,{,Constructor,(,_,:,w,;,_,,,___1,,,_,:,T,;,_,:,k4,;,_,:,Array,[,Array,[,Boolean,,,0B1000100,],,,0b10,],),{,},},<EOF>''',101))

    def test_79(self):
        self.assertTrue(TestLexer.test('''Class _a_{}Class T{}Class cS:n2{Destructor (){} }Class _{}Class K_{}Class _:__l0_27{}Class x:_6{Val $9:String ;}Class m7{}Class _{}''','''Class,_a_,{,},Class,T,{,},Class,cS,:,n2,{,Destructor,(,),{,},},Class,_,{,},Class,K_,{,},Class,_,:,__l0_27,{,},Class,x,:,_6,{,Val,$9,:,String,;,},Class,m7,{,},Class,_,{,},<EOF>''',101))

    def test_80(self):
        self.assertTrue(TestLexer.test('''Class _:_{Destructor (){} }Class _{}Class __{Val $__:Array [Array [Array [Array [Int ,0b1010010],03],07],0XE];Val $4:Q;}''','''Class,_,:,_,{,Destructor,(,),{,},},Class,_,{,},Class,__,{,Val,$__,:,Array,[,Array,[,Array,[,Array,[,Int,,,0b1010010,],,,03,],,,07,],,,0XE,],;,Val,$4,:,Q,;,},<EOF>''',101))

    def test_81(self):
        self.assertTrue(TestLexer.test('''Class _0{Val $24:Array [Array [String ,34],011];Destructor (){} }Class W_{Val _A:Array [Array [Int ,26],26];}Class _U:__t_{}''','''Class,_0,{,Val,$24,:,Array,[,Array,[,String,,,34,],,,011,],;,Destructor,(,),{,},},Class,W_,{,Val,_A,:,Array,[,Array,[,Int,,,26,],,,26,],;,},Class,_U,:,__t_,{,},<EOF>''',101))

    def test_82(self):
        self.assertTrue(TestLexer.test('''Class b:__{Var U__2,_,$U,_:Array [Array [Array [Array [Array [Array [Array [Array [Array [Boolean ,0B1000010],0X56],39],0x9],90],9],043_2],0XE_F],0X56];}''','''Class,b,:,__,{,Var,U__2,,,_,,,$U,,,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0B1000010,],,,0X56,],,,39,],,,0x9,],,,90,],,,9,],,,0432,],,,0XEF,],,,0X56,],;,},<EOF>''',101))

    def test_83(self):
        self.assertTrue(TestLexer.test('''Class C6{Constructor (_,_,q7__,L,v_,__Q:Array [Array [Array [Float ,0b101111],7_9_5],0b1_1];n73,_:Array [String ,0x48];__4,_,_7,_,v:String ){e::$jg();} }Class a:_Q_{}''','''Class,C6,{,Constructor,(,_,,,_,,,q7__,,,L,,,v_,,,__Q,:,Array,[,Array,[,Array,[,Float,,,0b101111,],,,795,],,,0b11,],;,n73,,,_,:,Array,[,String,,,0x48,],;,__4,,,_,,,_7,,,_,,,v,:,String,),{,e,::,$jg,(,),;,},},Class,a,:,_Q_,{,},<EOF>''',101))

    def test_84(self):
        self.assertTrue(TestLexer.test('''Class _:_7{Constructor (){A_88::$l();} }Class _:_{Constructor (___e,_:_){} }Class __0:k{Destructor (){}Var _:Array [Array [Boolean ,0x69_9],0B1001100];}Class xq{Destructor (){} }Class Q_{}Class _z0_z{Constructor (){} }''','''Class,_,:,_7,{,Constructor,(,),{,A_88,::,$l,(,),;,},},Class,_,:,_,{,Constructor,(,___e,,,_,:,_,),{,},},Class,__0,:,k,{,Destructor,(,),{,},Var,_,:,Array,[,Array,[,Boolean,,,0x699,],,,0B1001100,],;,},Class,xq,{,Destructor,(,),{,},},Class,Q_,{,},Class,_z0_z,{,Constructor,(,),{,},},<EOF>''',101))

    def test_85(self):
        self.assertTrue(TestLexer.test('''Class _3:f{Val _,Nc_3:Array [Array [Array [Array [Array [Array [Array [Int ,0114],0b1],0b1000111],0b11_1],0B1_1],4],0114];}''','''Class,_3,:,f,{,Val,_,,,Nc_3,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0114,],,,0b1,],,,0b1000111,],,,0b111,],,,0B11,],,,4,],,,0114,],;,},<EOF>''',101))

    def test_86(self):
        self.assertTrue(TestLexer.test('''Class X:l2{_9(){}Constructor (){.0E+8._7._.l.a();Break ;}Constructor (E_I37Z:Array [Float ,4];GZ_:Array [Array [Array [Int ,0X61],1],0B100];R:Array [Int ,046];s40__:Int ){}Constructor (){} }''','''Class,X,:,l2,{,_9,(,),{,},Constructor,(,),{,.0E+8,.,_7,.,_,.,l,.,a,(,),;,Break,;,},Constructor,(,E_I37Z,:,Array,[,Float,,,4,],;,GZ_,:,Array,[,Array,[,Array,[,Int,,,0X61,],,,1,],,,0B100,],;,R,:,Array,[,Int,,,046,],;,s40__,:,Int,),{,},Constructor,(,),{,},},<EOF>''',101))

    def test_87(self):
        self.assertTrue(TestLexer.test('''Class Rb_{d(X,l:Array [Array [Array [Array [String ,0X3],0B11100],68],0B11100]){}w6L(){}Constructor (__y:_){}Var v:Int ;}''','''Class,Rb_,{,d,(,X,,,l,:,Array,[,Array,[,Array,[,Array,[,String,,,0X3,],,,0B11100,],,,68,],,,0B11100,],),{,},w6L,(,),{,},Constructor,(,__y,:,_,),{,},Var,v,:,Int,;,},<EOF>''',101))

    def test_88(self):
        self.assertTrue(TestLexer.test('''Class __4{Constructor (P,_0:Array [Array [Array [Array [Int ,0b10001],0X55],4_554_1],02]){_nQ::$__();} }Class A:F{}Class _i:__Z{}''','''Class,__4,{,Constructor,(,P,,,_0,:,Array,[,Array,[,Array,[,Array,[,Int,,,0b10001,],,,0X55,],,,45541,],,,02,],),{,_nQ,::,$__,(,),;,},},Class,A,:,F,{,},Class,_i,:,__Z,{,},<EOF>''',101))

    def test_89(self):
        self.assertTrue(TestLexer.test('''Class P51_{Val $9O,c,_:Array [Boolean ,032];}Class _R_q5_:_{Destructor (){}Val $0__:String ;Constructor (N,_:_5){Return ;} }''','''Class,P51_,{,Val,$9O,,,c,,,_,:,Array,[,Boolean,,,032,],;,},Class,_R_q5_,:,_,{,Destructor,(,),{,},Val,$0__,:,String,;,Constructor,(,N,,,_,:,_5,),{,Return,;,},},<EOF>''',101))

    def test_90(self):
        self.assertTrue(TestLexer.test('''Class R_:A{Constructor (N:O8F){} }Class _W_{Constructor (f,Q_35,g6__:_;A:g;_2_:String ;n_9:v_){Continue ;Break ;} }''','''Class,R_,:,A,{,Constructor,(,N,:,O8F,),{,},},Class,_W_,{,Constructor,(,f,,,Q_35,,,g6__,:,_,;,A,:,g,;,_2_,:,String,;,n_9,:,v_,),{,Continue,;,Break,;,},},<EOF>''',101))

    def test_91(self):
        self.assertTrue(TestLexer.test('''Class _Q_7:G4v{Constructor (_i,_:Array [String ,0X1A];H:Float ;r,x:Array [Array [Boolean ,0134],36];_z:Boolean ){} }''','''Class,_Q_7,:,G4v,{,Constructor,(,_i,,,_,:,Array,[,String,,,0X1A,],;,H,:,Float,;,r,,,x,:,Array,[,Array,[,Boolean,,,0134,],,,36,],;,_z,:,Boolean,),{,},},<EOF>''',101))

    def test_92(self):
        self.assertTrue(TestLexer.test('''Class _:Q6{Constructor (O,_____,_,_0_:Array [Array [Float ,026],0B1000];__:String ;__,O8,swO_:Array [Boolean ,0B1000];T8_9Z:_;S_,U,a3_B_2:Array [Array [Array [Array [Boolean ,6],31],0X23],0x8]){} }''','''Class,_,:,Q6,{,Constructor,(,O,,,_____,,,_,,,_0_,:,Array,[,Array,[,Float,,,026,],,,0B1000,],;,__,:,String,;,__,,,O8,,,swO_,:,Array,[,Boolean,,,0B1000,],;,T8_9Z,:,_,;,S_,,,U,,,a3_B_2,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,6,],,,31,],,,0X23,],,,0x8,],),{,},},<EOF>''',101))

    def test_93(self):
        self.assertTrue(TestLexer.test('''Class _:E{}Class U:Ow__{$8(_9n,k:Int ;__,__H,c:wb){} }Class ____v4_K:w6{Var _,C_:Array [Array [Int ,31],067];Val $Z,$_:Float ;}Class _x:_6{}''','''Class,_,:,E,{,},Class,U,:,Ow__,{,$8,(,_9n,,,k,:,Int,;,__,,,__H,,,c,:,wb,),{,},},Class,____v4_K,:,w6,{,Var,_,,,C_,:,Array,[,Array,[,Int,,,31,],,,067,],;,Val,$Z,,,$_,:,Float,;,},Class,_x,:,_6,{,},<EOF>''',101))

    def test_94(self):
        self.assertTrue(TestLexer.test('''Class _{Var _,U,I4:Array [Array [Array [Boolean ,50],020],0X9];Val $o:Array [String ,0b1];Var $_:K7_o3;Destructor (){}Val Z2_,_,U4a:Array [Float ,06];Constructor (){}Var $53,z_:_7;}''','''Class,_,{,Var,_,,,U,,,I4,:,Array,[,Array,[,Array,[,Boolean,,,50,],,,020,],,,0X9,],;,Val,$o,:,Array,[,String,,,0b1,],;,Var,$_,:,K7_o3,;,Destructor,(,),{,},Val,Z2_,,,_,,,U4a,:,Array,[,Float,,,06,],;,Constructor,(,),{,},Var,$53,,,z_,:,_7,;,},<EOF>''',101))

    def test_95(self):
        self.assertTrue(TestLexer.test('''Class Y{$_(_,__u12_:_;y5:Array [Array [Array [Int ,76],053_1635_2_7],0B110001];__:_;U:_59;_r8,___k:Boolean ){Break ;} }''','''Class,Y,{,$_,(,_,,,__u12_,:,_,;,y5,:,Array,[,Array,[,Array,[,Int,,,76,],,,053163527,],,,0B110001,],;,__,:,_,;,U,:,_59,;,_r8,,,___k,:,Boolean,),{,Break,;,},},<EOF>''',101))

    def test_96(self):
        self.assertTrue(TestLexer.test('''Class _{}Class _:_{Constructor (m,h_,_,f9U:Array [String ,0X4E];_,_Xp:Array [Array [Array [Float ,88],05],0B11_1_0];_,_:__;X,T:String ){}Val $M_:String ;Destructor (){} }''','''Class,_,{,},Class,_,:,_,{,Constructor,(,m,,,h_,,,_,,,f9U,:,Array,[,String,,,0X4E,],;,_,,,_Xp,:,Array,[,Array,[,Array,[,Float,,,88,],,,05,],,,0B1110,],;,_,,,_,:,__,;,X,,,T,:,String,),{,},Val,$M_,:,String,;,Destructor,(,),{,},},<EOF>''',101))

    def test_97(self):
        self.assertTrue(TestLexer.test('''Class X{Constructor (_c:B;Q,_VSc,t1w0,Cx_,m,__iL,wUP,_1,bb,_7__,_a,_:Array [Int ,0B101110];V,__:Array [Array [Float ,05],055];_,_,_j,r:Array [Float ,2_3_8];_c:_){}__(_J2q:Float ;k:Boolean ){} }''','''Class,X,{,Constructor,(,_c,:,B,;,Q,,,_VSc,,,t1w0,,,Cx_,,,m,,,__iL,,,wUP,,,_1,,,bb,,,_7__,,,_a,,,_,:,Array,[,Int,,,0B101110,],;,V,,,__,:,Array,[,Array,[,Float,,,05,],,,055,],;,_,,,_,,,_j,,,r,:,Array,[,Float,,,238,],;,_c,:,_,),{,},__,(,_J2q,:,Float,;,k,:,Boolean,),{,},},<EOF>''',101))

    def test_98(self):
        self.assertTrue(TestLexer.test('''Class j_r{}Class a{Val M__01,$_,s:Array [Array [Boolean ,0XDC_9],070];Var $fx:Array [Int ,010];K9(_1_5:y4D__w){} }Class pW_:VB8{}''','''Class,j_r,{,},Class,a,{,Val,M__01,,,$_,,,s,:,Array,[,Array,[,Boolean,,,0XDC9,],,,070,],;,Var,$fx,:,Array,[,Int,,,010,],;,K9,(,_1_5,:,y4D__w,),{,},},Class,pW_,:,VB8,{,},<EOF>''',101))

    def test_99(self):
        self.assertTrue(TestLexer.test('''Class _:D_{$98_2(_K,_:vI){} }Class __{Destructor (){Return ;__4::$8();}Var a0,$ST:Boolean ;}Class S:f4{}Class V5{}''','''Class,_,:,D_,{,$98_2,(,_K,,,_,:,vI,),{,},},Class,__,{,Destructor,(,),{,Return,;,__4,::,$8,(,),;,},Var,a0,,,$ST,:,Boolean,;,},Class,S,:,f4,{,},Class,V5,{,},<EOF>''',101))

    def test_100(self):
        self.assertTrue(TestLexer.test('''Class BDi:f{r4B(s_,_,__:Array [Array [Int ,025],2];f,_Z:Int ;_Fo_,_,_:Array [Array [Array [Boolean ,025],2],025];__:r){} }''','''Class,BDi,:,f,{,r4B,(,s_,,,_,,,__,:,Array,[,Array,[,Int,,,025,],,,2,],;,f,,,_Z,:,Int,;,_Fo_,,,_,,,_,:,Array,[,Array,[,Array,[,Boolean,,,025,],,,2,],,,025,],;,__,:,r,),{,},},<EOF>''',101))

    def test_101(self):
        self.assertTrue(TestLexer.test('''Class _:Fiw1{Constructor (JMd_:__;__Va:String ;d___:_;_:Boolean ;__GV197L,U8,_:String ;l,O:Array [Boolean ,035];a,s:Boolean ){} }''','''Class,_,:,Fiw1,{,Constructor,(,JMd_,:,__,;,__Va,:,String,;,d___,:,_,;,_,:,Boolean,;,__GV197L,,,U8,,,_,:,String,;,l,,,O,:,Array,[,Boolean,,,035,],;,a,,,s,:,Boolean,),{,},},<EOF>''',101))

    def test_102(self):
        self.assertTrue(TestLexer.test('''Class s{Constructor (_:_;ro:Array [Array [Boolean ,0b1_0],0B100100]){Continue ;}$e(){Var _9_,Y_,j,_,_:_8;} }Class _A:__6_{}Class v{Var $24g_____,$__M:Array [Array [Float ,0B100100],0b110101];}''','''Class,s,{,Constructor,(,_,:,_,;,ro,:,Array,[,Array,[,Boolean,,,0b10,],,,0B100100,],),{,Continue,;,},$e,(,),{,Var,_9_,,,Y_,,,j,,,_,,,_,:,_8,;,},},Class,_A,:,__6_,{,},Class,v,{,Var,$24g_____,,,$__M,:,Array,[,Array,[,Float,,,0B100100,],,,0b110101,],;,},<EOF>''',101))

    def test_103(self):
        self.assertTrue(TestLexer.test('''Class _4i_A:_{Constructor (){}Constructor (Dj6_,_,_:Float ;n5,__X_9g4:Array [String ,0X1D]){Val _:Array [Array [Array [Array [String ,0B1_01],0X8],052],66_54_217];} }Class _{$V46o_D(){} }''','''Class,_4i_A,:,_,{,Constructor,(,),{,},Constructor,(,Dj6_,,,_,,,_,:,Float,;,n5,,,__X_9g4,:,Array,[,String,,,0X1D,],),{,Val,_,:,Array,[,Array,[,Array,[,Array,[,String,,,0B101,],,,0X8,],,,052,],,,6654217,],;,},},Class,_,{,$V46o_D,(,),{,},},<EOF>''',101))

    def test_104(self):
        self.assertTrue(TestLexer.test('''Class XN{}Class W{QS58(W:_C;_hgq:_S){} }Class s_s:_0{Constructor (Y,_p_N_:Array [String ,0B10]){} }Class _6I:_{Val W___:Float ;}''','''Class,XN,{,},Class,W,{,QS58,(,W,:,_C,;,_hgq,:,_S,),{,},},Class,s_s,:,_0,{,Constructor,(,Y,,,_p_N_,:,Array,[,String,,,0B10,],),{,},},Class,_6I,:,_,{,Val,W___,:,Float,;,},<EOF>''',101))

    def test_105(self):
        self.assertTrue(TestLexer.test('''Class S{}Class j_:M_{Val $A8cn5,$4:Array [Array [Array [Array [Float ,0B1_10],36],1],035];Destructor (){} }Class z{}Class x:_{}''','''Class,S,{,},Class,j_,:,M_,{,Val,$A8cn5,,,$4,:,Array,[,Array,[,Array,[,Array,[,Float,,,0B110,],,,36,],,,1,],,,035,],;,Destructor,(,),{,},},Class,z,{,},Class,x,:,_,{,},<EOF>''',101))

    def test_106(self):
        self.assertTrue(TestLexer.test('''Class _{Val $J1_,$Hv2:_;Val _,B,Pf4,_:Boolean ;Constructor (_8U4,_:Boolean ;J,__:Array [Array [Array [Array [String ,040],040],50],0b1011101];_:String ){} }''','''Class,_,{,Val,$J1_,,,$Hv2,:,_,;,Val,_,,,B,,,Pf4,,,_,:,Boolean,;,Constructor,(,_8U4,,,_,:,Boolean,;,J,,,__,:,Array,[,Array,[,Array,[,Array,[,String,,,040,],,,040,],,,50,],,,0b1011101,],;,_,:,String,),{,},},<EOF>''',101))

    def test_107(self):
        self.assertTrue(TestLexer.test('''Class __5{$95(z,tEs,R6:_b){} }Class M:___0{Destructor (){}Constructor (m_XP5,r:_){Return ;}Var $_,_:Float ;}Class __:__{Var _,s_b2_:Float ;}Class _{}''','''Class,__5,{,$95,(,z,,,tEs,,,R6,:,_b,),{,},},Class,M,:,___0,{,Destructor,(,),{,},Constructor,(,m_XP5,,,r,:,_,),{,Return,;,},Var,$_,,,_,:,Float,;,},Class,__,:,__,{,Var,_,,,s_b2_,:,Float,;,},Class,_,{,},<EOF>''',101))

    def test_108(self):
        self.assertTrue(TestLexer.test('''Class VP95__:K1_{}Class d:_0{Constructor (_:e;f3_,_7:Array [Array [Array [Array [Float ,0x4E],3_2],5],07_6]){} }Class _{}Class ___5{Constructor (){} }''','''Class,VP95__,:,K1_,{,},Class,d,:,_0,{,Constructor,(,_,:,e,;,f3_,,,_7,:,Array,[,Array,[,Array,[,Array,[,Float,,,0x4E,],,,32,],,,5,],,,076,],),{,},},Class,_,{,},Class,___5,{,Constructor,(,),{,},},<EOF>''',101))

    def test_109(self):
        self.assertTrue(TestLexer.test('''Class __9:b{_(_7,_4:Array [Array [Array [Float ,37],37],1]){} }Class _:Cx{Var _:Array [Int ,0X1];}Class y_:_4{Destructor (){} }''','''Class,__9,:,b,{,_,(,_7,,,_4,:,Array,[,Array,[,Array,[,Float,,,37,],,,37,],,,1,],),{,},},Class,_,:,Cx,{,Var,_,:,Array,[,Int,,,0X1,],;,},Class,y_,:,_4,{,Destructor,(,),{,},},<EOF>''',101))

    def test_110(self):
        self.assertTrue(TestLexer.test('''Class _k:_{}Class h236R{}Class _1:_x_Zz_{Constructor (){}Destructor (){}Destructor (){Continue ;}Var $m,$_0__,$22:Array [Array [Array [Int ,0x20],0B1],0B111001];Var DG_,$U:Boolean ;}''','''Class,_k,:,_,{,},Class,h236R,{,},Class,_1,:,_x_Zz_,{,Constructor,(,),{,},Destructor,(,),{,},Destructor,(,),{,Continue,;,},Var,$m,,,$_0__,,,$22,:,Array,[,Array,[,Array,[,Int,,,0x20,],,,0B1,],,,0B111001,],;,Var,DG_,,,$U,:,Boolean,;,},<EOF>''',101))

    def test_111(self):
        self.assertTrue(TestLexer.test('''Class _M{Var h:Float ;}Class o:q__{}Class w{Val k_ONM:Array [Boolean ,0x5_1];}Class O_{}Class UF__:_6{Destructor (){} }''','''Class,_M,{,Var,h,:,Float,;,},Class,o,:,q__,{,},Class,w,{,Val,k_ONM,:,Array,[,Boolean,,,0x51,],;,},Class,O_,{,},Class,UF__,:,_6,{,Destructor,(,),{,},},<EOF>''',101))

    def test_112(self):
        self.assertTrue(TestLexer.test('''Class __:N{Constructor (__:Array [Int ,0b1011111]){Continue ;}Val T,$6:Float ;Constructor (o:_;bL,EU,_:_){} }Class _j_3:_r{}Class e:z{}''','''Class,__,:,N,{,Constructor,(,__,:,Array,[,Int,,,0b1011111,],),{,Continue,;,},Val,T,,,$6,:,Float,;,Constructor,(,o,:,_,;,bL,,,EU,,,_,:,_,),{,},},Class,_j_3,:,_r,{,},Class,e,:,z,{,},<EOF>''',101))

    def test_113(self):
        self.assertTrue(TestLexer.test('''Class B0BU_{}Class h_{}Class _:C{}Class _:___4H{$__687(){Continue ;}Val $_h:w;Val $1wP5,_,B_,_:Array [Array [Float ,0X4F],90];}''','''Class,B0BU_,{,},Class,h_,{,},Class,_,:,C,{,},Class,_,:,___4H,{,$__687,(,),{,Continue,;,},Val,$_h,:,w,;,Val,$1wP5,,,_,,,B_,,,_,:,Array,[,Array,[,Float,,,0X4F,],,,90,],;,},<EOF>''',101))

    def test_114(self):
        self.assertTrue(TestLexer.test('''Class U_{}Class Z_{}Class A:H{Var $_,k_,$_,$3q3,$H:Array [String ,0136];}Class _{Constructor (E:W0GE;A,Z8:_2;F9_:b11_t){} }''','''Class,U_,{,},Class,Z_,{,},Class,A,:,H,{,Var,$_,,,k_,,,$_,,,$3q3,,,$H,:,Array,[,String,,,0136,],;,},Class,_,{,Constructor,(,E,:,W0GE,;,A,,,Z8,:,_2,;,F9_,:,b11_t,),{,},},<EOF>''',101))

    def test_115(self):
        self.assertTrue(TestLexer.test('''Class _9_:_{Destructor (){} }Class _{}Class _:qY_{_(){}_L__(){}$3(){}Var __5L7,_N:c_;}Class _P:T{}Class N:__{}''','''Class,_9_,:,_,{,Destructor,(,),{,},},Class,_,{,},Class,_,:,qY_,{,_,(,),{,},_L__,(,),{,},$3,(,),{,},Var,__5L7,,,_N,:,c_,;,},Class,_P,:,T,{,},Class,N,:,__,{,},<EOF>''',101))

    def test_116(self):
        self.assertTrue(TestLexer.test('''Class _:_p{Constructor (yZt3:p_;Z7_:Boolean ;_:Array [Int ,0134];_,tE:Array [Array [Array [String ,07],94],5];__:___;R:String ){Break ;} }''','''Class,_,:,_p,{,Constructor,(,yZt3,:,p_,;,Z7_,:,Boolean,;,_,:,Array,[,Int,,,0134,],;,_,,,tE,:,Array,[,Array,[,Array,[,String,,,07,],,,94,],,,5,],;,__,:,___,;,R,:,String,),{,Break,;,},},<EOF>''',101))

    def test_117(self):
        self.assertTrue(TestLexer.test('''Class m{Val $NF,_S8_,w,A_s_,$_5__5_0o:_;Destructor (){}_59__4(){}Constructor (Q:Array [Boolean ,0X7];_9:String ){} }''','''Class,m,{,Val,$NF,,,_S8_,,,w,,,A_s_,,,$_5__5_0o,:,_,;,Destructor,(,),{,},_59__4,(,),{,},Constructor,(,Q,:,Array,[,Boolean,,,0X7,],;,_9,:,String,),{,},},<EOF>''',101))

    def test_118(self):
        self.assertTrue(TestLexer.test('''Class H_:_3{Val $s,v,$BV_:d;}Class F_{}Class m7{}Class __D62{}Class __{}Class __{}Class __9:_{Var A0,$__:Array [String ,0X6A8F2_D];}Class n__y_:V{}''','''Class,H_,:,_3,{,Val,$s,,,v,,,$BV_,:,d,;,},Class,F_,{,},Class,m7,{,},Class,__D62,{,},Class,__,{,},Class,__,{,},Class,__9,:,_,{,Var,A0,,,$__,:,Array,[,String,,,0X6A8F2D,],;,},Class,n__y_,:,V,{,},<EOF>''',101))

    def test_119(self):
        self.assertTrue(TestLexer.test('''Class _:c{Constructor (V__g_:Float ){Var _,_:Int ;rU::$O()._231();} }Class e{}Class _{Var _7_:Int ;Constructor (){} }Class n{Val DX,$3,j,$__,$d__A3,_:Float ;}''','''Class,_,:,c,{,Constructor,(,V__g_,:,Float,),{,Var,_,,,_,:,Int,;,rU,::,$O,(,),.,_231,(,),;,},},Class,e,{,},Class,_,{,Var,_7_,:,Int,;,Constructor,(,),{,},},Class,n,{,Val,DX,,,$3,,,j,,,$__,,,$d__A3,,,_,:,Float,;,},<EOF>''',101))

    def test_120(self):
        self.assertTrue(TestLexer.test('''Class _:_{Val $_:Array [Array [Array [Boolean ,0b1_0_0],0b1010010],0704];}Class __q3_{Destructor (){}_(_56,_,o_R6:String ;M6_O,w0,_:__;F___2Y5_:Float ;T_,_9,D,u7:lT){} }Class y5:K{}Class I:_{Val Q_e16_s,_:Array [Float ,0x4B];}''','''Class,_,:,_,{,Val,$_,:,Array,[,Array,[,Array,[,Boolean,,,0b100,],,,0b1010010,],,,0704,],;,},Class,__q3_,{,Destructor,(,),{,},_,(,_56,,,_,,,o_R6,:,String,;,M6_O,,,w0,,,_,:,__,;,F___2Y5_,:,Float,;,T_,,,_9,,,D,,,u7,:,lT,),{,},},Class,y5,:,K,{,},Class,I,:,_,{,Val,Q_e16_s,,,_,:,Array,[,Float,,,0x4B,],;,},<EOF>''',101))

    def test_121(self):
        self.assertTrue(TestLexer.test('''Class _{_(O9v4,F:G){} }Class _5I:_{}Class _{R_(M:N;iJ:__;ac9,c:_){}Var $_,$J2Gg_:nC9;H(E9,_,_:Array [Boolean ,7]){}I(){} }Class __b3_{}''','''Class,_,{,_,(,O9v4,,,F,:,G,),{,},},Class,_5I,:,_,{,},Class,_,{,R_,(,M,:,N,;,iJ,:,__,;,ac9,,,c,:,_,),{,},Var,$_,,,$J2Gg_,:,nC9,;,H,(,E9,,,_,,,_,:,Array,[,Boolean,,,7,],),{,},I,(,),{,},},Class,__b3_,{,},<EOF>''',101))

    def test_122(self):
        self.assertTrue(TestLexer.test('''Class __:x{Destructor (){}Constructor (){}$_6(){}$d5(_:_;h,_X,__:Array [Array [Array [Float ,0xD_E],0B1_0_0],0B111111]){}Constructor (_:String ;_67,yp4,_,_,_gX_,O:Float ){}_6G(){} }''','''Class,__,:,x,{,Destructor,(,),{,},Constructor,(,),{,},$_6,(,),{,},$d5,(,_,:,_,;,h,,,_X,,,__,:,Array,[,Array,[,Array,[,Float,,,0xDE,],,,0B100,],,,0B111111,],),{,},Constructor,(,_,:,String,;,_67,,,yp4,,,_,,,_,,,_gX_,,,O,:,Float,),{,},_6G,(,),{,},},<EOF>''',101))

    def test_123(self):
        self.assertTrue(TestLexer.test('''Class _{Destructor (){} }Class _:Y{Constructor (_,__,_63,__:Array [String ,5];q,_:Array [Int ,0X27_8];_:Array [String ,0X34];vrP3,_82,_:w_){} }''','''Class,_,{,Destructor,(,),{,},},Class,_,:,Y,{,Constructor,(,_,,,__,,,_63,,,__,:,Array,[,String,,,5,],;,q,,,_,:,Array,[,Int,,,0X278,],;,_,:,Array,[,String,,,0X34,],;,vrP3,,,_82,,,_,:,w_,),{,},},<EOF>''',101))

    def test_124(self):
        self.assertTrue(TestLexer.test('''Class F_{}Class _:__{Constructor (V_,_,_:Boolean ;_Akd,Q:Array [Array [Float ,0b1],22];_,_b__:String ;u,X2G,I_:Array [Array [Int ,04],0XFF_FD]){} }''','''Class,F_,{,},Class,_,:,__,{,Constructor,(,V_,,,_,,,_,:,Boolean,;,_Akd,,,Q,:,Array,[,Array,[,Float,,,0b1,],,,22,],;,_,,,_b__,:,String,;,u,,,X2G,,,I_,:,Array,[,Array,[,Int,,,04,],,,0XFFFD,],),{,},},<EOF>''',101))

    def test_125(self):
        self.assertTrue(TestLexer.test('''Class Z{Constructor (_,D8v,Hs,Y,_1:Array [String ,83];b1,d_:Float ){}Val $_a,$9F7805I_:Array [Array [Array [Int ,0b1_00_10_0],0B1],0b101110];}''','''Class,Z,{,Constructor,(,_,,,D8v,,,Hs,,,Y,,,_1,:,Array,[,String,,,83,],;,b1,,,d_,:,Float,),{,},Val,$_a,,,$9F7805I_,:,Array,[,Array,[,Array,[,Int,,,0b100100,],,,0B1,],,,0b101110,],;,},<EOF>''',101))

    def test_126(self):
        self.assertTrue(TestLexer.test('''Class _O:o{}Class __:x__{$_(_,P,u_9:Int ;_D,_,_:Array [Float ,53];_l,__:_7;vT,E_:Array [Array [Array [Array [String ,0B100000],53],0b1010100],0x3B];_5,_:Array [Array [Float ,2_73_3],0X39]){} }Class _{}''','''Class,_O,:,o,{,},Class,__,:,x__,{,$_,(,_,,,P,,,u_9,:,Int,;,_D,,,_,,,_,:,Array,[,Float,,,53,],;,_l,,,__,:,_7,;,vT,,,E_,:,Array,[,Array,[,Array,[,Array,[,String,,,0B100000,],,,53,],,,0b1010100,],,,0x3B,],;,_5,,,_,:,Array,[,Array,[,Float,,,2733,],,,0X39,],),{,},},Class,_,{,},<EOF>''',101))

    def test_127(self):
        self.assertTrue(TestLexer.test('''Class _Z{}Class _:h{}Class f:_{}Class _{}Class o{Destructor (){Continue ;} }Class _y:B{Destructor (){}Destructor (){} }Class e8_VF2{Constructor (){} }''','''Class,_Z,{,},Class,_,:,h,{,},Class,f,:,_,{,},Class,_,{,},Class,o,{,Destructor,(,),{,Continue,;,},},Class,_y,:,B,{,Destructor,(,),{,},Destructor,(,),{,},},Class,e8_VF2,{,Constructor,(,),{,},},<EOF>''',101))

    def test_128(self):
        self.assertTrue(TestLexer.test('''Class N_f:H{}Class h:S2_{}Class _:_{Var $_0,$11,$_4,_:Array [Array [String ,0B1],051_4_473_2_3_7];Val $8_,$f:Int ;}''','''Class,N_f,:,H,{,},Class,h,:,S2_,{,},Class,_,:,_,{,Var,$_0,,,$11,,,$_4,,,_,:,Array,[,Array,[,String,,,0B1,],,,0514473237,],;,Val,$8_,,,$f,:,Int,;,},<EOF>''',101))

    def test_129(self):
        self.assertTrue(TestLexer.test('''Class __c:_94r_{}Class _:_vR{}Class H:d_O{Var $8:VY;Constructor (__3:X2;_5:W69;_6_9,C:Array [String ,41]){}Var q55:__;}''','''Class,__c,:,_94r_,{,},Class,_,:,_vR,{,},Class,H,:,d_O,{,Var,$8,:,VY,;,Constructor,(,__3,:,X2,;,_5,:,W69,;,_6_9,,,C,:,Array,[,String,,,41,],),{,},Var,q55,:,__,;,},<EOF>''',101))

    def test_130(self):
        self.assertTrue(TestLexer.test('''Class W__{Var b:Array [Array [Array [Array [Array [Array [Float ,031],0x2D],02],04],5],0b1];Var $_:Boolean ;Val _,_8,_:_;}''','''Class,W__,{,Var,b,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,031,],,,0x2D,],,,02,],,,04,],,,5,],,,0b1,],;,Var,$_,:,Boolean,;,Val,_,,,_8,,,_,:,_,;,},<EOF>''',101))

    def test_131(self):
        self.assertTrue(TestLexer.test('''Class _:X{$v(_,_,l,_:String ;__,_,__o0__,_,L_4_,_:_;i,g1V:Array [Array [String ,05],0126];i:F_V){} }Class sx{}''','''Class,_,:,X,{,$v,(,_,,,_,,,l,,,_,:,String,;,__,,,_,,,__o0__,,,_,,,L_4_,,,_,:,_,;,i,,,g1V,:,Array,[,Array,[,String,,,05,],,,0126,],;,i,:,F_V,),{,},},Class,sx,{,},<EOF>''',101))

    def test_132(self):
        self.assertTrue(TestLexer.test('''Class _{Val $_,__hf,$du,$9,$G,_F,$m,$4,$__:g;Destructor (){Break ;Continue ;}Var at2,_:Float ;Destructor (){} }''','''Class,_,{,Val,$_,,,__hf,,,$du,,,$9,,,$G,,,_F,,,$m,,,$4,,,$__,:,g,;,Destructor,(,),{,Break,;,Continue,;,},Var,at2,,,_,:,Float,;,Destructor,(,),{,},},<EOF>''',101))

    def test_133(self):
        self.assertTrue(TestLexer.test('''Class G_:C{Var $0,N,_,$24,$_J_61:Array [Array [Float ,0XE],0B110010];$N9Hzm(){} }Class _9_{Constructor (__:Boolean ){} }''','''Class,G_,:,C,{,Var,$0,,,N,,,_,,,$24,,,$_J_61,:,Array,[,Array,[,Float,,,0XE,],,,0B110010,],;,$N9Hzm,(,),{,},},Class,_9_,{,Constructor,(,__,:,Boolean,),{,},},<EOF>''',101))

    def test_134(self):
        self.assertTrue(TestLexer.test('''Class I_{Val $8_:Array [Array [Array [Array [Array [Array [String ,0b1010001],0X3A],0XD],0133],65_476],0XE];}Class ___8_:f{}Class _:e2{Destructor (){}F(){} }''','''Class,I_,{,Val,$8_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0b1010001,],,,0X3A,],,,0XD,],,,0133,],,,65476,],,,0XE,],;,},Class,___8_,:,f,{,},Class,_,:,e2,{,Destructor,(,),{,},F,(,),{,},},<EOF>''',101))

    def test_135(self):
        self.assertTrue(TestLexer.test('''Class B_{Constructor (){Val T,_:_;}Val Jb,$_:Int ;Var $P:Array [Array [Array [Array [Array [String ,0B1],04],03],06_6],76];}Class _bs:_5{}''','''Class,B_,{,Constructor,(,),{,Val,T,,,_,:,_,;,},Val,Jb,,,$_,:,Int,;,Var,$P,:,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0B1,],,,04,],,,03,],,,066,],,,76,],;,},Class,_bs,:,_5,{,},<EOF>''',101))

    def test_136(self):
        self.assertTrue(TestLexer.test('''Class YZ2_{}Class yz:k{_(_5Z,H,__,_Q6:Array [Array [Array [Float ,70],0B1010111],70];_:Int ;l,_5:Array [Array [String ,0134],0X52_F28]){} }Class _{}Class Z0N4_{Var _5_,$2,$f00:Q3;}''','''Class,YZ2_,{,},Class,yz,:,k,{,_,(,_5Z,,,H,,,__,,,_Q6,:,Array,[,Array,[,Array,[,Float,,,70,],,,0B1010111,],,,70,],;,_,:,Int,;,l,,,_5,:,Array,[,Array,[,String,,,0134,],,,0X52F28,],),{,},},Class,_,{,},Class,Z0N4_,{,Var,_5_,,,$2,,,$f00,:,Q3,;,},<EOF>''',101))

    def test_137(self):
        self.assertTrue(TestLexer.test('''Class _:E2{Destructor (){Continue ;}Constructor (J:R5___){}$1(_Br64o4Ki,_:__){Continue ;_::$d_U();}Constructor (_i_R,Q:Int ;p54_Z,lK:Array [Array [Boolean ,42],0x787_77]){}Constructor (){} }Class __:_39M{}Class _:R{}''','''Class,_,:,E2,{,Destructor,(,),{,Continue,;,},Constructor,(,J,:,R5___,),{,},$1,(,_Br64o4Ki,,,_,:,__,),{,Continue,;,_,::,$d_U,(,),;,},Constructor,(,_i_R,,,Q,:,Int,;,p54_Z,,,lK,:,Array,[,Array,[,Boolean,,,42,],,,0x78777,],),{,},Constructor,(,),{,},},Class,__,:,_39M,{,},Class,_,:,R,{,},<EOF>''',101))

    def test_138(self):
        self.assertTrue(TestLexer.test('''Class __7:j{$H(_,D,__,_,D__qs,K_,l_e,_:W){}Val $_8t,$7:Array [Array [String ,0x3_9],260_4];Destructor (){}Val _,__,__,_,$_5_,$_:__;}''','''Class,__7,:,j,{,$H,(,_,,,D,,,__,,,_,,,D__qs,,,K_,,,l_e,,,_,:,W,),{,},Val,$_8t,,,$7,:,Array,[,Array,[,String,,,0x39,],,,2604,],;,Destructor,(,),{,},Val,_,,,__,,,__,,,_,,,$_5_,,,$_,:,__,;,},<EOF>''',101))

    def test_139(self):
        self.assertTrue(TestLexer.test('''Class __U_eE:__56Y_{}Class _O:_{Destructor (){}Constructor (){}$__7(_,Hf_7_4_:Array [Int ,0b1_1];L_0___:String ){} }''','''Class,__U_eE,:,__56Y_,{,},Class,_O,:,_,{,Destructor,(,),{,},Constructor,(,),{,},$__7,(,_,,,Hf_7_4_,:,Array,[,Int,,,0b11,],;,L_0___,:,String,),{,},},<EOF>''',101))

    def test_140(self):
        self.assertTrue(TestLexer.test('''Class ____1{}Class y{}Class J{}Class R_{Constructor (HR6:p;l:Float ;K_,ol:A;r,___z0Pg2,_6,M_s_,BK,_:Boolean ;rbg:Boolean ;D_Be,F,e,X_:Array [Float ,2747];w,_:Array [Array [Array [Boolean ,026],0x32],0B110001]){Continue ;} }Class y_D{}Class t_:y{}''','''Class,____1,{,},Class,y,{,},Class,J,{,},Class,R_,{,Constructor,(,HR6,:,p,;,l,:,Float,;,K_,,,ol,:,A,;,r,,,___z0Pg2,,,_6,,,M_s_,,,BK,,,_,:,Boolean,;,rbg,:,Boolean,;,D_Be,,,F,,,e,,,X_,:,Array,[,Float,,,2747,],;,w,,,_,:,Array,[,Array,[,Array,[,Boolean,,,026,],,,0x32,],,,0B110001,],),{,Continue,;,},},Class,y_D,{,},Class,t_,:,y,{,},<EOF>''',101))

    def test_141(self):
        self.assertTrue(TestLexer.test('''Class _{Var $t,_:Array [Array [Array [Array [Float ,29],070],070],070];}Class _:k_{$FH_(){}Val __,$1_6z,$38:String ;}Class o:__{Constructor (){} }''','''Class,_,{,Var,$t,,,_,:,Array,[,Array,[,Array,[,Array,[,Float,,,29,],,,070,],,,070,],,,070,],;,},Class,_,:,k_,{,$FH_,(,),{,},Val,__,,,$1_6z,,,$38,:,String,;,},Class,o,:,__,{,Constructor,(,),{,},},<EOF>''',101))

    def test_142(self):
        self.assertTrue(TestLexer.test('''Class _{Val $0_:B4_;Var $9_,__:D5_;Constructor (_6:h1;_r,_6_:_;__9wt:J){} }Class _{Var $5:x_1;Var $_,t7N:_;$1(){} }''','''Class,_,{,Val,$0_,:,B4_,;,Var,$9_,,,__,:,D5_,;,Constructor,(,_6,:,h1,;,_r,,,_6_,:,_,;,__9wt,:,J,),{,},},Class,_,{,Var,$5,:,x_1,;,Var,$_,,,t7N,:,_,;,$1,(,),{,},},<EOF>''',101))

    def test_143(self):
        self.assertTrue(TestLexer.test('''Class Bj:U{}Class De{}Class s{}Class P:Q{Val y:Array [Array [Array [Array [Array [Boolean ,02_6],0b1],06],032],0B1];Destructor (){} }Class K:_{Val _:Int ;Var H_:String ;}''','''Class,Bj,:,U,{,},Class,De,{,},Class,s,{,},Class,P,:,Q,{,Val,y,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,026,],,,0b1,],,,06,],,,032,],,,0B1,],;,Destructor,(,),{,},},Class,K,:,_,{,Val,_,:,Int,;,Var,H_,:,String,;,},<EOF>''',101))

    def test_144(self):
        self.assertTrue(TestLexer.test('''Class _{Constructor (){Var Z_:Array [Array [Int ,0B1],0B100001];}Destructor (){Break ;} }Class _7S9{}Class _e__:X{Var $lOJ,$45i,__,$6,$267:Float ;}''','''Class,_,{,Constructor,(,),{,Var,Z_,:,Array,[,Array,[,Int,,,0B1,],,,0B100001,],;,},Destructor,(,),{,Break,;,},},Class,_7S9,{,},Class,_e__,:,X,{,Var,$lOJ,,,$45i,,,__,,,$6,,,$267,:,Float,;,},<EOF>''',101))

    def test_145(self):
        self.assertTrue(TestLexer.test('''Class b{}Class Cb_H9:_p7{Val $_5__:Array [Int ,76_1_212];Constructor (_,__744:C){}Destructor (){}Var _,$18_:_M;}''','''Class,b,{,},Class,Cb_H9,:,_p7,{,Val,$_5__,:,Array,[,Int,,,761212,],;,Constructor,(,_,,,__744,:,C,),{,},Destructor,(,),{,},Var,_,,,$18_,:,_M,;,},<EOF>''',101))

    def test_146(self):
        self.assertTrue(TestLexer.test('''Class _:L_Gm8q{}Class _:__{}Class d{Constructor (){}Constructor (_:_;_,ub,_30:Array [Array [String ,27],27]){}Constructor (){} }''','''Class,_,:,L_Gm8q,{,},Class,_,:,__,{,},Class,d,{,Constructor,(,),{,},Constructor,(,_,:,_,;,_,,,ub,,,_30,:,Array,[,Array,[,String,,,27,],,,27,],),{,},Constructor,(,),{,},},<EOF>''',101))

    def test_147(self):
        self.assertTrue(TestLexer.test('''Class _0__ive{Destructor (){} }Class _Dl:__{Val $e:Float ;Val XY:Array [Array [Array [Array [Array [String ,592],0x9],0xEA_5],91],0b100011];_1(){Continue ;} }''','''Class,_0__ive,{,Destructor,(,),{,},},Class,_Dl,:,__,{,Val,$e,:,Float,;,Val,XY,:,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,592,],,,0x9,],,,0xEA5,],,,91,],,,0b100011,],;,_1,(,),{,Continue,;,},},<EOF>''',101))

    def test_148(self):
        self.assertTrue(TestLexer.test('''Class _{Var _P:y;J(){} }Class _{$0(a,Z:Boolean ){ {} }Val $Q6_:Array [Float ,9];}Class _{__(_:Array [Array [Float ,0X22],0B1000010];p,_:Boolean ;_6_F8_,S:Array [Array [Float ,01],0B1]){}Destructor (){} }''','''Class,_,{,Var,_P,:,y,;,J,(,),{,},},Class,_,{,$0,(,a,,,Z,:,Boolean,),{,{,},},Val,$Q6_,:,Array,[,Float,,,9,],;,},Class,_,{,__,(,_,:,Array,[,Array,[,Float,,,0X22,],,,0B1000010,],;,p,,,_,:,Boolean,;,_6_F8_,,,S,:,Array,[,Array,[,Float,,,01,],,,0B1,],),{,},Destructor,(,),{,},},<EOF>''',101))

    def test_149(self):
        self.assertTrue(TestLexer.test('''Class _m{Val $o:Array [Array [Array [Array [Array [Array [Float ,91_4],43],43],0124],0XE],0124];}Class _{}Class _b2_c:e___8k{}''','''Class,_m,{,Val,$o,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,914,],,,43,],,,43,],,,0124,],,,0XE,],,,0124,],;,},Class,_,{,},Class,_b2_c,:,e___8k,{,},<EOF>''',101))

    def test_150(self):
        self.assertTrue(TestLexer.test('''Class _:d{}Class _x{Destructor (){}Destructor (){ {} }}Class _5:L7{Var $__g_:Boolean ;Var $H:Array [Array [Boolean ,0122],07];Destructor (){Val _:__;}Val _,$h3Z_851b_,zo__4_:T;}Class __KK:_{Destructor (){} }''','''Class,_,:,d,{,},Class,_x,{,Destructor,(,),{,},Destructor,(,),{,{,},},},Class,_5,:,L7,{,Var,$__g_,:,Boolean,;,Var,$H,:,Array,[,Array,[,Boolean,,,0122,],,,07,],;,Destructor,(,),{,Val,_,:,__,;,},Val,_,,,$h3Z_851b_,,,zo__4_,:,T,;,},Class,__KK,:,_,{,Destructor,(,),{,},},<EOF>''',101))

    def test_151(self):
        self.assertTrue(TestLexer.test('''Class _{Destructor (){k::$7Q();}Constructor (l:_){ {} }Val r_2,h:Array [Array [Int ,9],35];Destructor (){} }Class K3{}Class z{}Class W{Destructor (){} }''','''Class,_,{,Destructor,(,),{,k,::,$7Q,(,),;,},Constructor,(,l,:,_,),{,{,},},Val,r_2,,,h,:,Array,[,Array,[,Int,,,9,],,,35,],;,Destructor,(,),{,},},Class,K3,{,},Class,z,{,},Class,W,{,Destructor,(,),{,},},<EOF>''',101))

    def test_152(self):
        self.assertTrue(TestLexer.test('''Class P:_KHa_{}Class _w{}Class F3{}Class _{Q2_(Bq:Int ;C,wH:g;___2,__aI,h:Array [Float ,04];_,___:Array [Int ,0x5A];k,__:V){} }''','''Class,P,:,_KHa_,{,},Class,_w,{,},Class,F3,{,},Class,_,{,Q2_,(,Bq,:,Int,;,C,,,wH,:,g,;,___2,,,__aI,,,h,:,Array,[,Float,,,04,],;,_,,,___,:,Array,[,Int,,,0x5A,],;,k,,,__,:,V,),{,},},<EOF>''',101))

    def test_153(self):
        self.assertTrue(TestLexer.test('''Class i:_{Constructor (v,_W,C1_w,_h__,d1:Array [String ,0X58]){} }Class _{}Class JZ_H:x{Var _7,_3,_W1,$_KV:Int ;Constructor (){}Destructor (){} }''','''Class,i,:,_,{,Constructor,(,v,,,_W,,,C1_w,,,_h__,,,d1,:,Array,[,String,,,0X58,],),{,},},Class,_,{,},Class,JZ_H,:,x,{,Var,_7,,,_3,,,_W1,,,$_KV,:,Int,;,Constructor,(,),{,},Destructor,(,),{,},},<EOF>''',101))

    def test_154(self):
        self.assertTrue(TestLexer.test('''Class _{}Class _:_{Var $93,$w:_;Constructor (_:Array [String ,0X2];s_q:Array [String ,54];G,i:Boolean ;_F_4,d:D){} }Class Q_{}Class M{}''','''Class,_,{,},Class,_,:,_,{,Var,$93,,,$w,:,_,;,Constructor,(,_,:,Array,[,String,,,0X2,],;,s_q,:,Array,[,String,,,54,],;,G,,,i,:,Boolean,;,_F_4,,,d,:,D,),{,},},Class,Q_,{,},Class,M,{,},<EOF>''',101))

    def test_155(self):
        self.assertTrue(TestLexer.test('''Class _:V{Var $0:Int ;}Class h:G{Var p,$0,m7C_:Array [Array [Float ,04],0b1_1];Var Qf,_:Array [Int ,4_8_55_7_72];}Class P5{}''','''Class,_,:,V,{,Var,$0,:,Int,;,},Class,h,:,G,{,Var,p,,,$0,,,m7C_,:,Array,[,Array,[,Float,,,04,],,,0b11,],;,Var,Qf,,,_,:,Array,[,Int,,,4855772,],;,},Class,P5,{,},<EOF>''',101))

    def test_156(self):
        self.assertTrue(TestLexer.test('''Class _:_{}Class F:UI{Destructor (){} }Class _1_1:O_{Val $X:N;}Class B7:_{$88(_,_,RS:_8;B,mH_18_,H_H,m7_:_){}Val Hr,$E,$4:Float ;Constructor (_v:_9;P:G;Q:Array [Array [Array [Array [Array [Array [String ,0X4],66],0B100000],0X8],0X32],035];_,P:Array [Array [Array [String ,0b1_0_100],0B100000],0141]){} }''','''Class,_,:,_,{,},Class,F,:,UI,{,Destructor,(,),{,},},Class,_1_1,:,O_,{,Val,$X,:,N,;,},Class,B7,:,_,{,$88,(,_,,,_,,,RS,:,_8,;,B,,,mH_18_,,,H_H,,,m7_,:,_,),{,},Val,Hr,,,$E,,,$4,:,Float,;,Constructor,(,_v,:,_9,;,P,:,G,;,Q,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0X4,],,,66,],,,0B100000,],,,0X8,],,,0X32,],,,035,],;,_,,,P,:,Array,[,Array,[,Array,[,String,,,0b10100,],,,0B100000,],,,0141,],),{,},},<EOF>''',101))

    def test_157(self):
        self.assertTrue(TestLexer.test('''Class _:_0{Constructor (){}Val _6_,$5:Float ;}Class _{Val w:Array [Array [Array [Array [Array [Array [Boolean ,026],0XE],026],0X8],48],026];}''','''Class,_,:,_0,{,Constructor,(,),{,},Val,_6_,,,$5,:,Float,;,},Class,_,{,Val,w,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,026,],,,0XE,],,,026,],,,0X8,],,,48,],,,026,],;,},<EOF>''',101))

    def test_158(self):
        self.assertTrue(TestLexer.test('''Class _{Constructor (){} }Class i:_6{Val b1h:Array [Float ,4];}Class _X:E{Constructor (){Continue ;Break ;G6_::$jT();} }Class Q_0{}''','''Class,_,{,Constructor,(,),{,},},Class,i,:,_6,{,Val,b1h,:,Array,[,Float,,,4,],;,},Class,_X,:,E,{,Constructor,(,),{,Continue,;,Break,;,G6_,::,$jT,(,),;,},},Class,Q_0,{,},<EOF>''',101))

    def test_159(self):
        self.assertTrue(TestLexer.test('''Class ___MhO_507:_4{Constructor (k2:_;_V_D_:Array [Array [Array [Array [Array [String ,3],0X2_7],0X43],0b1000010],7]){ {} }}''','''Class,___MhO_507,:,_4,{,Constructor,(,k2,:,_,;,_V_D_,:,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,3,],,,0X27,],,,0X43,],,,0b1000010,],,,7,],),{,{,},},},<EOF>''',101))

    def test_160(self):
        self.assertTrue(TestLexer.test('''Class _{Constructor (){} }Class v:E{}Class K{}Class _{$__4(){Continue ;}Val _,$Q:ASb_;}Class c_U1H0{}Class Yv{}''','''Class,_,{,Constructor,(,),{,},},Class,v,:,E,{,},Class,K,{,},Class,_,{,$__4,(,),{,Continue,;,},Val,_,,,$Q,:,ASb_,;,},Class,c_U1H0,{,},Class,Yv,{,},<EOF>''',101))

    def test_161(self):
        self.assertTrue(TestLexer.test('''Class _Y{Val C,_,pp,G,$_,$w:Array [Float ,0123];}Class P{}Class _w:D{_(){}__(){}_(M:Array [Array [Array [Array [Array [Boolean ,84],84],03],0123],0x11]){Break ;}Destructor (){} }''','''Class,_Y,{,Val,C,,,_,,,pp,,,G,,,$_,,,$w,:,Array,[,Float,,,0123,],;,},Class,P,{,},Class,_w,:,D,{,_,(,),{,},__,(,),{,},_,(,M,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,84,],,,84,],,,03,],,,0123,],,,0x11,],),{,Break,;,},Destructor,(,),{,},},<EOF>''',101))

    def test_162(self):
        self.assertTrue(TestLexer.test('''Class R{}Class V:pw_{Val $m,$88_:Boolean ;}Class l:__{Destructor (){} }Class r:l{Var $u:Array [Array [Int ,35],0X42];}Class l9{}''','''Class,R,{,},Class,V,:,pw_,{,Val,$m,,,$88_,:,Boolean,;,},Class,l,:,__,{,Destructor,(,),{,},},Class,r,:,l,{,Var,$u,:,Array,[,Array,[,Int,,,35,],,,0X42,],;,},Class,l9,{,},<EOF>''',101))

    def test_163(self):
        self.assertTrue(TestLexer.test('''Class Q:__U{}Class N_4O_:MO{Val em,_,_,$H8,OG,$8:Array [Boolean ,0b111011];Y(){}Val _7d,$32,$_4:Int ;}Class _2:_{}''','''Class,Q,:,__U,{,},Class,N_4O_,:,MO,{,Val,em,,,_,,,_,,,$H8,,,OG,,,$8,:,Array,[,Boolean,,,0b111011,],;,Y,(,),{,},Val,_7d,,,$32,,,$_4,:,Int,;,},Class,_2,:,_,{,},<EOF>''',101))

    def test_164(self):
        self.assertTrue(TestLexer.test('''Class _{Destructor (){}Val _,$7z3_:_w_;Val $6_7F,$0:Array [String ,0x29];Destructor (){}Destructor (){Return ;Break ;}Val _,_KY___,$V:Array [Array [Float ,032],26];}Class b{Val $e,n_f:_u;}Class T{}Class __:Z___{}''','''Class,_,{,Destructor,(,),{,},Val,_,,,$7z3_,:,_w_,;,Val,$6_7F,,,$0,:,Array,[,String,,,0x29,],;,Destructor,(,),{,},Destructor,(,),{,Return,;,Break,;,},Val,_,,,_KY___,,,$V,:,Array,[,Array,[,Float,,,032,],,,26,],;,},Class,b,{,Val,$e,,,n_f,:,_u,;,},Class,T,{,},Class,__,:,Z___,{,},<EOF>''',101))

    def test_165(self):
        self.assertTrue(TestLexer.test('''Class T:br{Constructor (DF_:_;v0__W:c){}$6(m:Array [Array [Float ,01_072_4],0X5_4_3_0];_m,pb4j,_h,_:Array [Array [Array [Array [String ,010],0x7D_8_0_E_A],0XD],1];dz0_3,L__:E_;j:____){ {} }Var z:Array [String ,0675_0];}''','''Class,T,:,br,{,Constructor,(,DF_,:,_,;,v0__W,:,c,),{,},$6,(,m,:,Array,[,Array,[,Float,,,010724,],,,0X5430,],;,_m,,,pb4j,,,_h,,,_,:,Array,[,Array,[,Array,[,Array,[,String,,,010,],,,0x7D80EA,],,,0XD,],,,1,],;,dz0_3,,,L__,:,E_,;,j,:,____,),{,{,},},Var,z,:,Array,[,String,,,06750,],;,},<EOF>''',101))

    def test_166(self):
        self.assertTrue(TestLexer.test('''Class _:_B{Val $Z,_:Array [Array [Array [Array [Array [String ,0X1B],0B111101],0x5B_F],58],047];$4_(wd,f1,o_9_:Int ){Continue ;}Var $__Z,$8_Xe,_:Array [Array [Float ,0X1B],58];}''','''Class,_,:,_B,{,Val,$Z,,,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0X1B,],,,0B111101,],,,0x5BF,],,,58,],,,047,],;,$4_,(,wd,,,f1,,,o_9_,:,Int,),{,Continue,;,},Var,$__Z,,,$8_Xe,,,_,:,Array,[,Array,[,Float,,,0X1B,],,,58,],;,},<EOF>''',101))

    def test_167(self):
        self.assertTrue(TestLexer.test('''Class _cL{}Class _z{}Class fMv{Val $3:_U_;Var v,__:Boolean ;}Class _2:N0O8{E(u:Array [Array [String ,0b10],05];X99W:Array [Boolean ,0x46]){Break ;Continue ;} }''','''Class,_cL,{,},Class,_z,{,},Class,fMv,{,Val,$3,:,_U_,;,Var,v,,,__,:,Boolean,;,},Class,_2,:,N0O8,{,E,(,u,:,Array,[,Array,[,String,,,0b10,],,,05,],;,X99W,:,Array,[,Boolean,,,0x46,],),{,Break,;,Continue,;,},},<EOF>''',101))

    def test_168(self):
        self.assertTrue(TestLexer.test('''Class _{Var $_2_aE__,$6:Array [Float ,0XA];Var Xo3,$6,n,_:Float ;Constructor (_:Array [Array [Array [Int ,67],67],0b1000100];o,_L,b2_:Int ){} }Class T:_U{Val $k,$2:Boolean ;}Class _:Q__{_i(Z4_:Int ){K::$4();}Destructor (){} }''','''Class,_,{,Var,$_2_aE__,,,$6,:,Array,[,Float,,,0XA,],;,Var,Xo3,,,$6,,,n,,,_,:,Float,;,Constructor,(,_,:,Array,[,Array,[,Array,[,Int,,,67,],,,67,],,,0b1000100,],;,o,,,_L,,,b2_,:,Int,),{,},},Class,T,:,_U,{,Val,$k,,,$2,:,Boolean,;,},Class,_,:,Q__,{,_i,(,Z4_,:,Int,),{,K,::,$4,(,),;,},Destructor,(,),{,},},<EOF>''',101))

    def test_169(self):
        self.assertTrue(TestLexer.test('''Class Eg__{Constructor (P3:Array [Array [Array [Array [Array [Array [Array [Array [Float ,81],07_7_42_5],0b1],81],0X7],0X4_4],06_5_3],53];ZvqI8,X,_F:Boolean ){}$c(I:W2;X__,o8:Array [Int ,0X7];b03_,_:Boolean ){} }Class __T1:_{}''','''Class,Eg__,{,Constructor,(,P3,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,81,],,,077425,],,,0b1,],,,81,],,,0X7,],,,0X44,],,,0653,],,,53,],;,ZvqI8,,,X,,,_F,:,Boolean,),{,},$c,(,I,:,W2,;,X__,,,o8,:,Array,[,Int,,,0X7,],;,b03_,,,_,:,Boolean,),{,},},Class,__T1,:,_,{,},<EOF>''',101))

    def test_170(self):
        self.assertTrue(TestLexer.test('''Class F:_iC_{Val $_,$mX,$7:Int ;Destructor (){}$l_(_,_:Int ;F_h4_:_;_:_;I:Array [Array [Array [Float ,0b101_0],0xE_A],0b1100010]){}Val $bb47:y;Destructor (){} }''','''Class,F,:,_iC_,{,Val,$_,,,$mX,,,$7,:,Int,;,Destructor,(,),{,},$l_,(,_,,,_,:,Int,;,F_h4_,:,_,;,_,:,_,;,I,:,Array,[,Array,[,Array,[,Float,,,0b1010,],,,0xEA,],,,0b1100010,],),{,},Val,$bb47,:,y,;,Destructor,(,),{,},},<EOF>''',101))

    def test_171(self):
        self.assertTrue(TestLexer.test('''Class _:I{Constructor (__hpL,__,L,__,_P,_:Array [Boolean ,0x1]){ {} }}Class Wp:_{wo(S_,I_,U:Array [Boolean ,01_46]){} }Class G6i:b{}''','''Class,_,:,I,{,Constructor,(,__hpL,,,__,,,L,,,__,,,_P,,,_,:,Array,[,Boolean,,,0x1,],),{,{,},},},Class,Wp,:,_,{,wo,(,S_,,,I_,,,U,:,Array,[,Boolean,,,0146,],),{,},},Class,G6i,:,b,{,},<EOF>''',101))

    def test_172(self):
        self.assertTrue(TestLexer.test('''Class L__:_{Destructor (){} }Class Z2e:h87{_9(){} }Class g__{}Class W34{_4(z:Array [Boolean ,0B11_0]){Val QsL__8,L,_,Z4_w,_,z_:Array [Array [Int ,050],9];}Var $f4:k;}''','''Class,L__,:,_,{,Destructor,(,),{,},},Class,Z2e,:,h87,{,_9,(,),{,},},Class,g__,{,},Class,W34,{,_4,(,z,:,Array,[,Boolean,,,0B110,],),{,Val,QsL__8,,,L,,,_,,,Z4_w,,,_,,,z_,:,Array,[,Array,[,Int,,,050,],,,9,],;,},Var,$f4,:,k,;,},<EOF>''',101))

    def test_173(self):
        self.assertTrue(TestLexer.test('''Class pdX{Constructor (_,___,cG,P:Array [String ,0b11_1_0]){Continue ;}Val $0,$9_:g;}Class y_:_{}Class ___h:v{}''','''Class,pdX,{,Constructor,(,_,,,___,,,cG,,,P,:,Array,[,String,,,0b1110,],),{,Continue,;,},Val,$0,,,$9_,:,g,;,},Class,y_,:,_,{,},Class,___h,:,v,{,},<EOF>''',101))

    def test_174(self):
        self.assertTrue(TestLexer.test('''Class _{}Class hY:G{}Class _n:__6{Var Q:Array [Array [String ,0X48],0x2_6_B_B_4_E8];Val _,$3:String ;_(W:Float ){Continue ;} }Class _6_Z_:_3{}Class Wa{Val _,$g:Q;Var X,_,DE_K:Array [Boolean ,0XB_9FF];}''','''Class,_,{,},Class,hY,:,G,{,},Class,_n,:,__6,{,Var,Q,:,Array,[,Array,[,String,,,0X48,],,,0x26BB4E8,],;,Val,_,,,$3,:,String,;,_,(,W,:,Float,),{,Continue,;,},},Class,_6_Z_,:,_3,{,},Class,Wa,{,Val,_,,,$g,:,Q,;,Var,X,,,_,,,DE_K,:,Array,[,Boolean,,,0XB9FF,],;,},<EOF>''',101))

    def test_175(self):
        self.assertTrue(TestLexer.test('''Class N_P_{}Class _:_6qi{}Class _:r{Constructor (_D7:String ;_:Array [Array [Array [Array [Array [Array [Array [Array [Array [Float ,0B1011100],19],055],7_7],055],055],43_8],0xED],0b1010001]){} }Class E{}Class T{}''','''Class,N_P_,{,},Class,_,:,_6qi,{,},Class,_,:,r,{,Constructor,(,_D7,:,String,;,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0B1011100,],,,19,],,,055,],,,77,],,,055,],,,055,],,,438,],,,0xED,],,,0b1010001,],),{,},},Class,E,{,},Class,T,{,},<EOF>''',101))

    def test_176(self):
        self.assertTrue(TestLexer.test('''Class C{Val $pnZ:Boolean ;}Class r_:Oc{}Class _{Val l,$9:Array [Array [Array [Array [Array [Float ,0x8_7],88],0131],0X1_3],0B1011011];}''','''Class,C,{,Val,$pnZ,:,Boolean,;,},Class,r_,:,Oc,{,},Class,_,{,Val,l,,,$9,:,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0x87,],,,88,],,,0131,],,,0X13,],,,0B1011011,],;,},<EOF>''',101))

    def test_177(self):
        self.assertTrue(TestLexer.test('''Class Q:A{Val $_:Array [Array [String ,053],61];Var _,$_Q:Array [Int ,0b1];Val DW1pg_e_2_:Boolean ;}Class _Pa:_8{Var _,J9,$0,_f:m;}''','''Class,Q,:,A,{,Val,$_,:,Array,[,Array,[,String,,,053,],,,61,],;,Var,_,,,$_Q,:,Array,[,Int,,,0b1,],;,Val,DW1pg_e_2_,:,Boolean,;,},Class,_Pa,:,_8,{,Var,_,,,J9,,,$0,,,_f,:,m,;,},<EOF>''',101))

    def test_178(self):
        self.assertTrue(TestLexer.test('''Class n_37M_:_9__s{Constructor (){}$__(H,CM_,_:Boolean ;j:Array [Array [Float ,0X3F],01];_:A2;vX:Float ){}Destructor (){} }Class Ok{}''','''Class,n_37M_,:,_9__s,{,Constructor,(,),{,},$__,(,H,,,CM_,,,_,:,Boolean,;,j,:,Array,[,Array,[,Float,,,0X3F,],,,01,],;,_,:,A2,;,vX,:,Float,),{,},Destructor,(,),{,},},Class,Ok,{,},<EOF>''',101))

    def test_179(self):
        self.assertTrue(TestLexer.test('''Class _8:_{}Class __9__:j{Constructor (A,u5:Z_29_;k,S5_26,_1,h,___,qU94,T_:Array [Boolean ,0b10_0_100];F,_,_K_:Array [Float ,4]){} }''','''Class,_8,:,_,{,},Class,__9__,:,j,{,Constructor,(,A,,,u5,:,Z_29_,;,k,,,S5_26,,,_1,,,h,,,___,,,qU94,,,T_,:,Array,[,Boolean,,,0b100100,],;,F,,,_,,,_K_,:,Array,[,Float,,,4,],),{,},},<EOF>''',101))

    def test_180(self):
        self.assertTrue(TestLexer.test('''Class _{Val $_6,$1:Array [Array [Array [Int ,0X9A_4],0B1_0101_1],0B111100];}Class L{Destructor (){Return ;}$4(D5,Y_:Array [Boolean ,045]){} }''','''Class,_,{,Val,$_6,,,$1,:,Array,[,Array,[,Array,[,Int,,,0X9A4,],,,0B101011,],,,0B111100,],;,},Class,L,{,Destructor,(,),{,Return,;,},$4,(,D5,,,Y_,:,Array,[,Boolean,,,045,],),{,},},<EOF>''',101))

    def test_181(self):
        self.assertTrue(TestLexer.test('''Class _:K{$6(_1o,h,__s___I5x__,_e8_:Array [Array [Boolean ,072],0xE]){}Var y1,$0:String ;Val _,$U,$A_,I9_:Float ;}''','''Class,_,:,K,{,$6,(,_1o,,,h,,,__s___I5x__,,,_e8_,:,Array,[,Array,[,Boolean,,,072,],,,0xE,],),{,},Var,y1,,,$0,:,String,;,Val,_,,,$U,,,$A_,,,I9_,:,Float,;,},<EOF>''',101))

    def test_182(self):
        self.assertTrue(TestLexer.test('''Class _:F{Constructor (u1_Ev:F_;__:N__;___,o9_,_:String ){} }Class x{Var _:Boolean ;Constructor (_,_RA,Hrj_:String ){}Constructor (){} }''','''Class,_,:,F,{,Constructor,(,u1_Ev,:,F_,;,__,:,N__,;,___,,,o9_,,,_,:,String,),{,},},Class,x,{,Var,_,:,Boolean,;,Constructor,(,_,,,_RA,,,Hrj_,:,String,),{,},Constructor,(,),{,},},<EOF>''',101))

    def test_183(self):
        self.assertTrue(TestLexer.test('''Class __:_38{}Class C:_{Constructor (_su_:Boolean ;_Y:Array [Array [Array [Array [String ,0xF],1_3_3],031],0x50];_9,_3_o_96F__J:o8){ {_::$k__();} }}''','''Class,__,:,_38,{,},Class,C,:,_,{,Constructor,(,_su_,:,Boolean,;,_Y,:,Array,[,Array,[,Array,[,Array,[,String,,,0xF,],,,133,],,,031,],,,0x50,],;,_9,,,_3_o_96F__J,:,o8,),{,{,_,::,$k__,(,),;,},},},<EOF>''',101))

    def test_184(self):
        self.assertTrue(TestLexer.test('''Class _:__{Constructor (_,Z:Array [Array [Array [Array [Array [String ,0B1],0X8],8],20_7],027];_e,_4,_b8:Array [Boolean ,0x38]){Continue ;} }Class _07_4:_{}Class sla:_{}''','''Class,_,:,__,{,Constructor,(,_,,,Z,:,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0B1,],,,0X8,],,,8,],,,207,],,,027,],;,_e,,,_4,,,_b8,:,Array,[,Boolean,,,0x38,],),{,Continue,;,},},Class,_07_4,:,_,{,},Class,sla,:,_,{,},<EOF>''',101))

    def test_185(self):
        self.assertTrue(TestLexer.test('''Class _{Val IGxt:Array [Boolean ,073];}Class t5:_{Val I53,Jl_,_6_:Int ;Destructor (){} }Class b:e{Val Y:I;Destructor (){} }Class D:KI{}''','''Class,_,{,Val,IGxt,:,Array,[,Boolean,,,073,],;,},Class,t5,:,_,{,Val,I53,,,Jl_,,,_6_,:,Int,;,Destructor,(,),{,},},Class,b,:,e,{,Val,Y,:,I,;,Destructor,(,),{,},},Class,D,:,KI,{,},<EOF>''',101))

    def test_186(self):
        self.assertTrue(TestLexer.test('''Class __{}Class r6p_:_{Constructor (_,_34:Float ;oll,__,_,_4,_T_05V,_:L2;WaFj__h_,b:Float ){}Constructor (o:v9k){}M(_:Array [Array [Boolean ,0x20],0B1_110];m:_){} }Class C:f{}Class _{}''','''Class,__,{,},Class,r6p_,:,_,{,Constructor,(,_,,,_34,:,Float,;,oll,,,__,,,_,,,_4,,,_T_05V,,,_,:,L2,;,WaFj__h_,,,b,:,Float,),{,},Constructor,(,o,:,v9k,),{,},M,(,_,:,Array,[,Array,[,Boolean,,,0x20,],,,0B1110,],;,m,:,_,),{,},},Class,C,:,f,{,},Class,_,{,},<EOF>''',101))

    def test_187(self):
        self.assertTrue(TestLexer.test('''Class E:_O_{}Class __{}Class _Mp_C0:_{Constructor (_2_7BQ_,___N,t3:Int ){}Val y_1_A:Boolean ;}Class _Bg_w0:i{Val $7,Pb_:Array [Float ,62];}''','''Class,E,:,_O_,{,},Class,__,{,},Class,_Mp_C0,:,_,{,Constructor,(,_2_7BQ_,,,___N,,,t3,:,Int,),{,},Val,y_1_A,:,Boolean,;,},Class,_Bg_w0,:,i,{,Val,$7,,,Pb_,:,Array,[,Float,,,62,],;,},<EOF>''',101))

    def test_188(self):
        self.assertTrue(TestLexer.test('''Class _z{Constructor (y:Boolean ;_:Array [Boolean ,6_69];Z:l;_b_16:String ){}$4(b3,_,_:Array [Array [Int ,4],0B1]){} }''','''Class,_z,{,Constructor,(,y,:,Boolean,;,_,:,Array,[,Boolean,,,669,],;,Z,:,l,;,_b_16,:,String,),{,},$4,(,b3,,,_,,,_,:,Array,[,Array,[,Int,,,4,],,,0B1,],),{,},},<EOF>''',101))

    def test_189(self):
        self.assertTrue(TestLexer.test('''Class F{}Class Wh{}Class _Ke{_(_r_:Boolean ;S,_,r1:s){____16::$_7_();Continue ;} }Class Q27:_{}Class Y:Z0{Var oo,$U3,$9,$gV6:Array [Array [Boolean ,0b110110],0B1000110];Constructor (){}Constructor (){} }''','''Class,F,{,},Class,Wh,{,},Class,_Ke,{,_,(,_r_,:,Boolean,;,S,,,_,,,r1,:,s,),{,____16,::,$_7_,(,),;,Continue,;,},},Class,Q27,:,_,{,},Class,Y,:,Z0,{,Var,oo,,,$U3,,,$9,,,$gV6,:,Array,[,Array,[,Boolean,,,0b110110,],,,0B1000110,],;,Constructor,(,),{,},Constructor,(,),{,},},<EOF>''',101))

    def test_190(self):
        self.assertTrue(TestLexer.test('''Class __a:__Qcr{Destructor (){}Destructor (){}u(_,_:Int ;x:W){} }Class _6_{}Class _:c{}Class Gj:__9{Val $88,$_:_r;}''','''Class,__a,:,__Qcr,{,Destructor,(,),{,},Destructor,(,),{,},u,(,_,,,_,:,Int,;,x,:,W,),{,},},Class,_6_,{,},Class,_,:,c,{,},Class,Gj,:,__9,{,Val,$88,,,$_,:,_r,;,},<EOF>''',101))

    def test_191(self):
        self.assertTrue(TestLexer.test('''Class R6:_{}Class _{Val $yMy,$3_,S_,$E7x,$vQv_,$__w:_o_L1T;}Class p{Constructor (){} }Class r6{}Class V4{$9(){}Destructor (){} }''','''Class,R6,:,_,{,},Class,_,{,Val,$yMy,,,$3_,,,S_,,,$E7x,,,$vQv_,,,$__w,:,_o_L1T,;,},Class,p,{,Constructor,(,),{,},},Class,r6,{,},Class,V4,{,$9,(,),{,},Destructor,(,),{,},},<EOF>''',101))

    def test_192(self):
        self.assertTrue(TestLexer.test('''Class q:___s_{Var $_6:Array [String ,0X36];X(L,_,_:H;y:c;a,_,V97_S:Boolean ;_kQ,K:Array [Float ,0x1_C];__1:_2){} }Class Vpj:_6_{}Class r{}Class _:a{}''','''Class,q,:,___s_,{,Var,$_6,:,Array,[,String,,,0X36,],;,X,(,L,,,_,,,_,:,H,;,y,:,c,;,a,,,_,,,V97_S,:,Boolean,;,_kQ,,,K,:,Array,[,Float,,,0x1C,],;,__1,:,_2,),{,},},Class,Vpj,:,_6_,{,},Class,r,{,},Class,_,:,a,{,},<EOF>''',101))

    def test_193(self):
        self.assertTrue(TestLexer.test('''Class A72_{}Class _FS:U{Val $_:Array [Boolean ,05_2_3];}Class _2{}Class vZ{}Class _k_P1W0:r___D{Destructor (){}Destructor (){}Destructor (){} }''','''Class,A72_,{,},Class,_FS,:,U,{,Val,$_,:,Array,[,Boolean,,,0523,],;,},Class,_2,{,},Class,vZ,{,},Class,_k_P1W0,:,r___D,{,Destructor,(,),{,},Destructor,(,),{,},Destructor,(,),{,},},<EOF>''',101))

    def test_194(self):
        self.assertTrue(TestLexer.test('''Class m{}Class f_:xf{Val $1,$_,_3_:__;$_Z28(_,Nbw:Array [Float ,100];t,C_4t_,_y7:String ;w:Array [Float ,100];_,sm_4,k:String ){} }''','''Class,m,{,},Class,f_,:,xf,{,Val,$1,,,$_,,,_3_,:,__,;,$_Z28,(,_,,,Nbw,:,Array,[,Float,,,100,],;,t,,,C_4t_,,,_y7,:,String,;,w,:,Array,[,Float,,,100,],;,_,,,sm_4,,,k,:,String,),{,},},<EOF>''',101))

    def test_195(self):
        self.assertTrue(TestLexer.test('''Class x{L_(M9:Boolean ){}Constructor (_q5_:Array [Array [Array [String ,4],0b110011],0B10010];K:_;Q,_Q,YG_144,__,_2P:Array [String ,0b110011]){} }Class b_5_:n2_{}''','''Class,x,{,L_,(,M9,:,Boolean,),{,},Constructor,(,_q5_,:,Array,[,Array,[,Array,[,String,,,4,],,,0b110011,],,,0B10010,],;,K,:,_,;,Q,,,_Q,,,YG_144,,,__,,,_2P,:,Array,[,String,,,0b110011,],),{,},},Class,b_5_,:,n2_,{,},<EOF>''',101))

    def test_196(self):
        self.assertTrue(TestLexer.test('''Class G{}Class sA_:sI721{}Class _:B{Val $__7C_:Array [Array [Boolean ,7],7_0];Var $_8:Float ;Var r:Int ;}Class w_36_9:P3{}''','''Class,G,{,},Class,sA_,:,sI721,{,},Class,_,:,B,{,Val,$__7C_,:,Array,[,Array,[,Boolean,,,7,],,,70,],;,Var,$_8,:,Float,;,Var,r,:,Int,;,},Class,w_36_9,:,P3,{,},<EOF>''',101))

    def test_197(self):
        self.assertTrue(TestLexer.test('''Class J_:_H7{Constructor (u4l1,_aFe1_9,___:Array [Array [String ,064],064];_,E:Boolean ;R,_:Int ){} }Class __1:_{}''','''Class,J_,:,_H7,{,Constructor,(,u4l1,,,_aFe1_9,,,___,:,Array,[,Array,[,String,,,064,],,,064,],;,_,,,E,:,Boolean,;,R,,,_,:,Int,),{,},},Class,__1,:,_,{,},<EOF>''',101))

    def test_198(self):
        self.assertTrue(TestLexer.test('''Class y:v{}Class __6_:_{$1_(__,_8,_,__,S,_184_,_,_,_,_:Array [Array [Float ,053],025];_,__O:Array [Array [Array [String ,40],31],0B1];f,_x_970,zJR,_O,_:___42){} }''','''Class,y,:,v,{,},Class,__6_,:,_,{,$1_,(,__,,,_8,,,_,,,__,,,S,,,_184_,,,_,,,_,,,_,,,_,:,Array,[,Array,[,Float,,,053,],,,025,],;,_,,,__O,:,Array,[,Array,[,Array,[,String,,,40,],,,31,],,,0B1,],;,f,,,_x_970,,,zJR,,,_O,,,_,:,___42,),{,},},<EOF>''',101))

    def test_199(self):
        self.assertTrue(TestLexer.test('''Class A{Destructor (){} }Class _:r{Destructor (){}$___k__(_:Array [Int ,0X13];_,D:X){Var a8:Array [Int ,0B1_1_11];}Constructor (){} }''','''Class,A,{,Destructor,(,),{,},},Class,_,:,r,{,Destructor,(,),{,},$___k__,(,_,:,Array,[,Int,,,0X13,],;,_,,,D,:,X,),{,Var,a8,:,Array,[,Int,,,0B1111,],;,},Constructor,(,),{,},},<EOF>''',101))

    def test_200(self):
        self.assertTrue(TestLexer.test('''Class _72{Val _,$e1_8:String ;Var b_0,$____,_:_9;$2(__:Float ;a,_j_O,Q,I,L,_,_9W:m;_,__:_;M:Array [Array [Int ,0x7_3],0b110111]){}Destructor (){}Destructor (){} }''','''Class,_72,{,Val,_,,,$e1_8,:,String,;,Var,b_0,,,$____,,,_,:,_9,;,$2,(,__,:,Float,;,a,,,_j_O,,,Q,,,I,,,L,,,_,,,_9W,:,m,;,_,,,__,:,_,;,M,:,Array,[,Array,[,Int,,,0x73,],,,0b110111,],),{,},Destructor,(,),{,},Destructor,(,),{,},},<EOF>''',101))

    def test_201(self):
        self.assertTrue(TestLexer.test('''Class FH3{}Class _:___o_2{Constructor (_:_W;_:Boolean ){} }Class NX{_(nS,A__i:_8;_8C6,d,_7,_3,_:Boolean ){}Var __:Array [Int ,0b10_1_010];}''','''Class,FH3,{,},Class,_,:,___o_2,{,Constructor,(,_,:,_W,;,_,:,Boolean,),{,},},Class,NX,{,_,(,nS,,,A__i,:,_8,;,_8C6,,,d,,,_7,,,_3,,,_,:,Boolean,),{,},Var,__,:,Array,[,Int,,,0b101010,],;,},<EOF>''',101))

    def test_202(self):
        self.assertTrue(TestLexer.test('''Class B{}Class X{z(){} }Class NY0{}Class U:_{}Class _{}Class Z0N:E311{}Class _:_{Val $X7,_,$_:Int ;Constructor (ky:Boolean ;v_j_b:__;r,_:_s;__73,o:L;_:Float ;____93:Q;_,K,_t5:_;_,u:h8_){} }''','''Class,B,{,},Class,X,{,z,(,),{,},},Class,NY0,{,},Class,U,:,_,{,},Class,_,{,},Class,Z0N,:,E311,{,},Class,_,:,_,{,Val,$X7,,,_,,,$_,:,Int,;,Constructor,(,ky,:,Boolean,;,v_j_b,:,__,;,r,,,_,:,_s,;,__73,,,o,:,L,;,_,:,Float,;,____93,:,Q,;,_,,,K,,,_t5,:,_,;,_,,,u,:,h8_,),{,},},<EOF>''',101))

    def test_203(self):
        self.assertTrue(TestLexer.test('''Class X0{}Class _:__1_S3{Constructor (_:Int ){}Constructor (ff44j,_,kd1:Array [Boolean ,0x6]){} }Class _{Val C,$p,z_U12:Boolean ;}''','''Class,X0,{,},Class,_,:,__1_S3,{,Constructor,(,_,:,Int,),{,},Constructor,(,ff44j,,,_,,,kd1,:,Array,[,Boolean,,,0x6,],),{,},},Class,_,{,Val,C,,,$p,,,z_U12,:,Boolean,;,},<EOF>''',101))

    def test_204(self):
        self.assertTrue(TestLexer.test('''Class _vJ:e{Val o0:_;}Class y6:n27c{I(_:String ;_:Array [Array [Int ,0b1_111_0_0],01]){}Constructor (Z_5,_:Array [String ,0b1011000];Pi,_2:Int ){} }Class _5a___:_278{}Class _m_{}''','''Class,_vJ,:,e,{,Val,o0,:,_,;,},Class,y6,:,n27c,{,I,(,_,:,String,;,_,:,Array,[,Array,[,Int,,,0b111100,],,,01,],),{,},Constructor,(,Z_5,,,_,:,Array,[,String,,,0b1011000,],;,Pi,,,_2,:,Int,),{,},},Class,_5a___,:,_278,{,},Class,_m_,{,},<EOF>''',101))

    def test_205(self):
        self.assertTrue(TestLexer.test('''Class _s:U_x{Destructor (){Break ;} }Class _:_{}Class _z{}Class h:v{}Class n:PA{Val $Uu,_:Array [String ,076];}Class K:N{}''','''Class,_s,:,U_x,{,Destructor,(,),{,Break,;,},},Class,_,:,_,{,},Class,_z,{,},Class,h,:,v,{,},Class,n,:,PA,{,Val,$Uu,,,_,:,Array,[,String,,,076,],;,},Class,K,:,N,{,},<EOF>''',101))

    def test_206(self):
        self.assertTrue(TestLexer.test('''Class c{Destructor (){Val S90,k,O_G,q:Int ;I::$l();E::$_.V._M();Val y,C_,C:Array [String ,05];{} }_E(){ {}{} }}Class __{}Class _{}''','''Class,c,{,Destructor,(,),{,Val,S90,,,k,,,O_G,,,q,:,Int,;,I,::,$l,(,),;,E,::,$_,.,V,.,_M,(,),;,Val,y,,,C_,,,C,:,Array,[,String,,,05,],;,{,},},_E,(,),{,{,},{,},},},Class,__,{,},Class,_,{,},<EOF>''',101))

    def test_207(self):
        self.assertTrue(TestLexer.test('''Class v{}Class p:M{}Class __:Q_{R(m:_;C:Array [Array [Float ,06],0XB];_,j,_,G,O1a,H:q){ {}{} }Destructor (){}Val $__,$VY,_m_:TD__8;}''','''Class,v,{,},Class,p,:,M,{,},Class,__,:,Q_,{,R,(,m,:,_,;,C,:,Array,[,Array,[,Float,,,06,],,,0XB,],;,_,,,j,,,_,,,G,,,O1a,,,H,:,q,),{,{,},{,},},Destructor,(,),{,},Val,$__,,,$VY,,,_m_,:,TD__8,;,},<EOF>''',101))

    def test_208(self):
        self.assertTrue(TestLexer.test('''Class _:_{}Class _:sdgf9{}Class _:_1{Var $_t:Array [Array [Array [Array [Array [Array [Array [Array [String ,38],1],0xB],38],0b1],03],2_3_2],38];}''','''Class,_,:,_,{,},Class,_,:,sdgf9,{,},Class,_,:,_1,{,Var,$_t,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,38,],,,1,],,,0xB,],,,38,],,,0b1,],,,03,],,,232,],,,38,],;,},<EOF>''',101))

    def test_209(self):
        self.assertTrue(TestLexer.test('''Class C_0_:Rq{$_66(_X730,_:Array [Array [Array [Boolean ,9],9],020_3_1];_:Boolean ;Y:V0;_M,c41:Array [Array [Array [Boolean ,9],03],0104];u8:e8){}Constructor (o,e,_8,_,X8_8_,i0S,O_,I8_,cE,__:_){}Destructor (){Break ;} }''','''Class,C_0_,:,Rq,{,$_66,(,_X730,,,_,:,Array,[,Array,[,Array,[,Boolean,,,9,],,,9,],,,02031,],;,_,:,Boolean,;,Y,:,V0,;,_M,,,c41,:,Array,[,Array,[,Array,[,Boolean,,,9,],,,03,],,,0104,],;,u8,:,e8,),{,},Constructor,(,o,,,e,,,_8,,,_,,,X8_8_,,,i0S,,,O_,,,I8_,,,cE,,,__,:,_,),{,},Destructor,(,),{,Break,;,},},<EOF>''',101))

    def test_210(self):
        self.assertTrue(TestLexer.test('''Class _4_{}Class _81:__7{Constructor (S,_6,s,D9_:Array [String ,0b1010];_,_:__;_j5,t:Int ){} }Class _{Val ___hv:Array [Float ,0B11111];Destructor (){} }''','''Class,_4_,{,},Class,_81,:,__7,{,Constructor,(,S,,,_6,,,s,,,D9_,:,Array,[,String,,,0b1010,],;,_,,,_,:,__,;,_j5,,,t,:,Int,),{,},},Class,_,{,Val,___hv,:,Array,[,Float,,,0B11111,],;,Destructor,(,),{,},},<EOF>''',101))

    def test_211(self):
        self.assertTrue(TestLexer.test('''Class _:_{Val $X8:Array [Array [Array [Array [Array [Array [Int ,0B10100],0140],3],02],0x3F],0X2E];Val $0,$_,_,$Y5:_;}''','''Class,_,:,_,{,Val,$X8,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0B10100,],,,0140,],,,3,],,,02,],,,0x3F,],,,0X2E,],;,Val,$0,,,$_,,,_,,,$Y5,:,_,;,},<EOF>''',101))

    def test_212(self):
        self.assertTrue(TestLexer.test('''Class v__b0__{Destructor (){}Destructor (){} }Class _T{Var _7y,$d,$_p,_d,w6__:Array [Float ,0X9_1];}Class _6P_{}''','''Class,v__b0__,{,Destructor,(,),{,},Destructor,(,),{,},},Class,_T,{,Var,_7y,,,$d,,,$_p,,,_d,,,w6__,:,Array,[,Float,,,0X91,],;,},Class,_6P_,{,},<EOF>''',101))

    def test_213(self):
        self.assertTrue(TestLexer.test('''Class L{Val _i9:String ;Var $_,_,$y:String ;_I(_:gO;h,_n_,_,_,Z,_t,_,Wc__U:_;_,_,C,_:Array [Int ,8_0421]){} }''','''Class,L,{,Val,_i9,:,String,;,Var,$_,,,_,,,$y,:,String,;,_I,(,_,:,gO,;,h,,,_n_,,,_,,,_,,,Z,,,_t,,,_,,,Wc__U,:,_,;,_,,,_,,,C,,,_,:,Array,[,Int,,,80421,],),{,},},<EOF>''',101))

    def test_214(self):
        self.assertTrue(TestLexer.test('''Class cL_:q_{Var $1XE,_:Int ;_(){}Var __,$7c,$_,__5E,_5,$1,_,$___39:String ;}Class _{Constructor (j:__8_){Return ;} }''','''Class,cL_,:,q_,{,Var,$1XE,,,_,:,Int,;,_,(,),{,},Var,__,,,$7c,,,$_,,,__5E,,,_5,,,$1,,,_,,,$___39,:,String,;,},Class,_,{,Constructor,(,j,:,__8_,),{,Return,;,},},<EOF>''',101))

    def test_215(self):
        self.assertTrue(TestLexer.test('''Class _1:_{}Class __8:_{Constructor (_:Boolean ;_____,NI,_,_,_M1,g__c:Array [Array [Array [Array [Boolean ,0X27],2],0B1],91_56780];UHY6,o,BT:String ){}Constructor (){} }''','''Class,_1,:,_,{,},Class,__8,:,_,{,Constructor,(,_,:,Boolean,;,_____,,,NI,,,_,,,_,,,_M1,,,g__c,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,0X27,],,,2,],,,0B1,],,,9156780,],;,UHY6,,,o,,,BT,:,String,),{,},Constructor,(,),{,},},<EOF>''',101))

    def test_216(self):
        self.assertTrue(TestLexer.test('''Class w:O{Val _j,_25,w_9_7___d_,Y:_;Val $_,$9I_,$t:Array [Array [Array [Array [Int ,017],017],41],0X4];Constructor (__4:t_;f:Int ){}Destructor (){} }''','''Class,w,:,O,{,Val,_j,,,_25,,,w_9_7___d_,,,Y,:,_,;,Val,$_,,,$9I_,,,$t,:,Array,[,Array,[,Array,[,Array,[,Int,,,017,],,,017,],,,41,],,,0X4,],;,Constructor,(,__4,:,t_,;,f,:,Int,),{,},Destructor,(,),{,},},<EOF>''',101))

    def test_217(self):
        self.assertTrue(TestLexer.test('''Class E4{Var _:Array [Array [Array [Boolean ,0XA],25],011];}Class k:G7dd{}Class g{Destructor (){}Val Ld,Q2,_O,La:Array [Array [Float ,0X9_19],0xAAB88];}''','''Class,E4,{,Var,_,:,Array,[,Array,[,Array,[,Boolean,,,0XA,],,,25,],,,011,],;,},Class,k,:,G7dd,{,},Class,g,{,Destructor,(,),{,},Val,Ld,,,Q2,,,_O,,,La,:,Array,[,Array,[,Float,,,0X919,],,,0xAAB88,],;,},<EOF>''',101))

    def test_218(self):
        self.assertTrue(TestLexer.test('''Class _:Cj7{}Class _:X{}Class __{Val $T:Array [Array [Array [Array [Array [Array [Int ,0X10],0b101100],61],0x4],3],6_5];}Class F:M{}Class _{}Class Q:O{}''','''Class,_,:,Cj7,{,},Class,_,:,X,{,},Class,__,{,Val,$T,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0X10,],,,0b101100,],,,61,],,,0x4,],,,3,],,,65,],;,},Class,F,:,M,{,},Class,_,{,},Class,Q,:,O,{,},<EOF>''',101))

    def test_219(self):
        self.assertTrue(TestLexer.test('''Class _:b5o{$H(u5,_,__,_:String ;j:Array [Array [Array [String ,0X3],0B1],0x2B];G:Array [Array [Array [Array [String ,0111],02],0B10],01_7];_,y,_8,lA:Array [Array [Float ,48],48];_:_4;q:Float ;X_,Nb61A,S_D:_7;__,f1:String ;D4,_3z:Array [String ,0B10]){Var _9_r647_:W2_7;} }''','''Class,_,:,b5o,{,$H,(,u5,,,_,,,__,,,_,:,String,;,j,:,Array,[,Array,[,Array,[,String,,,0X3,],,,0B1,],,,0x2B,],;,G,:,Array,[,Array,[,Array,[,Array,[,String,,,0111,],,,02,],,,0B10,],,,017,],;,_,,,y,,,_8,,,lA,:,Array,[,Array,[,Float,,,48,],,,48,],;,_,:,_4,;,q,:,Float,;,X_,,,Nb61A,,,S_D,:,_7,;,__,,,f1,:,String,;,D4,,,_3z,:,Array,[,String,,,0B10,],),{,Var,_9_r647_,:,W2_7,;,},},<EOF>''',101))

    def test_220(self):
        self.assertTrue(TestLexer.test('''Class _:A_{}Class _m4a:__{Val $_2:Int ;Destructor (){}Constructor (y8V,_0:Float ;b_a__:Int ){}Destructor (){} }''','''Class,_,:,A_,{,},Class,_m4a,:,__,{,Val,$_2,:,Int,;,Destructor,(,),{,},Constructor,(,y8V,,,_0,:,Float,;,b_a__,:,Int,),{,},Destructor,(,),{,},},<EOF>''',101))

    def test_221(self):
        self.assertTrue(TestLexer.test('''Class _:y{Constructor (_:Array [Array [Array [String ,90_77],0b1],0B1]){}Var $N:d7_;}Class c:_081Lw{}Class Iz:h_9{}Class _2_2:m{$_(){}Destructor (){} }''','''Class,_,:,y,{,Constructor,(,_,:,Array,[,Array,[,Array,[,String,,,9077,],,,0b1,],,,0B1,],),{,},Var,$N,:,d7_,;,},Class,c,:,_081Lw,{,},Class,Iz,:,h_9,{,},Class,_2_2,:,m,{,$_,(,),{,},Destructor,(,),{,},},<EOF>''',101))

    def test_222(self):
        self.assertTrue(TestLexer.test('''Class _{$x(_:Array [Array [String ,18],5];r__:Nq_){} }Class _8jG:tzq_Ei{Destructor (){}$55(_H_,Q,EU,_:Array [Boolean ,18];__:Array [Array [Array [Int ,18],034],18]){Z::$_X_._();} }Class m:__{}''','''Class,_,{,$x,(,_,:,Array,[,Array,[,String,,,18,],,,5,],;,r__,:,Nq_,),{,},},Class,_8jG,:,tzq_Ei,{,Destructor,(,),{,},$55,(,_H_,,,Q,,,EU,,,_,:,Array,[,Boolean,,,18,],;,__,:,Array,[,Array,[,Array,[,Int,,,18,],,,034,],,,18,],),{,Z,::,$_X_,.,_,(,),;,},},Class,m,:,__,{,},<EOF>''',101))

    def test_223(self):
        self.assertTrue(TestLexer.test('''Class _1Z:r{Constructor (E,J:Array [Array [Array [Int ,04_76],0xE],0b1_0];_f,A_3,_:Float ;___,o,R,x_3_0_:_3){} }''','''Class,_1Z,:,r,{,Constructor,(,E,,,J,:,Array,[,Array,[,Array,[,Int,,,0476,],,,0xE,],,,0b10,],;,_f,,,A_3,,,_,:,Float,;,___,,,o,,,R,,,x_3_0_,:,_3,),{,},},<EOF>''',101))

    def test_224(self):
        self.assertTrue(TestLexer.test('''Class _X{Constructor (){}Destructor (){}Var $_Z,_U,E:F;A6(){}$L_(_,M_,_,___r,M_,__:String ;_,_,R,R_,_M_,_:_){} }Class V{}''','''Class,_X,{,Constructor,(,),{,},Destructor,(,),{,},Var,$_Z,,,_U,,,E,:,F,;,A6,(,),{,},$L_,(,_,,,M_,,,_,,,___r,,,M_,,,__,:,String,;,_,,,_,,,R,,,R_,,,_M_,,,_,:,_,),{,},},Class,V,{,},<EOF>''',101))

    def test_225(self):
        self.assertTrue(TestLexer.test('''Class __:_{Constructor (z:Array [Boolean ,0x6];_:_;_,X,lJ1,__,_,e1,W:_9i;DI_:Boolean ;_,_1:Array [Array [Array [Array [Array [Float ,14],02],0X9],5_64],0XD16_1]){Break ;} }''','''Class,__,:,_,{,Constructor,(,z,:,Array,[,Boolean,,,0x6,],;,_,:,_,;,_,,,X,,,lJ1,,,__,,,_,,,e1,,,W,:,_9i,;,DI_,:,Boolean,;,_,,,_1,:,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,14,],,,02,],,,0X9,],,,564,],,,0XD161,],),{,Break,;,},},<EOF>''',101))

    def test_226(self):
        self.assertTrue(TestLexer.test('''Class _7__H_:_{Constructor (K:Boolean ;E:String ;un_,_:Array [Array [String ,0XB_D],8];_w:Array [String ,0B1_1];__p_Q:Boolean ;_:Boolean ){} }''','''Class,_7__H_,:,_,{,Constructor,(,K,:,Boolean,;,E,:,String,;,un_,,,_,:,Array,[,Array,[,String,,,0XBD,],,,8,],;,_w,:,Array,[,String,,,0B11,],;,__p_Q,:,Boolean,;,_,:,Boolean,),{,},},<EOF>''',101))

    def test_227(self):
        self.assertTrue(TestLexer.test('''Class _s{}Class _:W{$_(_:Float ;r:Array [Float ,1]){} }Class __4:l_{}Class p6V0:j{Destructor (){}Constructor (_7_,_8:Array [Array [Array [Boolean ,0144],0b10_0],0XB]){}Val m8_:Int ;Val $TK_:_;V(){} }Class _R_M_8:__{}''','''Class,_s,{,},Class,_,:,W,{,$_,(,_,:,Float,;,r,:,Array,[,Float,,,1,],),{,},},Class,__4,:,l_,{,},Class,p6V0,:,j,{,Destructor,(,),{,},Constructor,(,_7_,,,_8,:,Array,[,Array,[,Array,[,Boolean,,,0144,],,,0b100,],,,0XB,],),{,},Val,m8_,:,Int,;,Val,$TK_,:,_,;,V,(,),{,},},Class,_R_M_8,:,__,{,},<EOF>''',101))

    def test_228(self):
        self.assertTrue(TestLexer.test('''Class _{__(_,_,_i_,_:Array [Float ,0XF];_:Array [Array [Int ,265],0X20];T,O,a_5:String ;mf_39:Array [Array [Array [String ,0X20],0x1A],063];f34_y:Float ;s:Array [Int ,0xB_69]){}Destructor (){}Constructor (){Break ;}Var $_:Array [Int ,01_6_4_5_2];}''','''Class,_,{,__,(,_,,,_,,,_i_,,,_,:,Array,[,Float,,,0XF,],;,_,:,Array,[,Array,[,Int,,,265,],,,0X20,],;,T,,,O,,,a_5,:,String,;,mf_39,:,Array,[,Array,[,Array,[,String,,,0X20,],,,0x1A,],,,063,],;,f34_y,:,Float,;,s,:,Array,[,Int,,,0xB69,],),{,},Destructor,(,),{,},Constructor,(,),{,Break,;,},Var,$_,:,Array,[,Int,,,016452,],;,},<EOF>''',101))

    def test_229(self):
        self.assertTrue(TestLexer.test('''Class f_{Var $D_:K;}Class _{Constructor (e:Array [Boolean ,027];_:_7u){}Constructor (D7_,d:Int ){}Var $_m,l_b,$b,__:Int ;}''','''Class,f_,{,Var,$D_,:,K,;,},Class,_,{,Constructor,(,e,:,Array,[,Boolean,,,027,],;,_,:,_7u,),{,},Constructor,(,D7_,,,d,:,Int,),{,},Var,$_m,,,l_b,,,$b,,,__,:,Int,;,},<EOF>''',101))

    def test_230(self):
        self.assertTrue(TestLexer.test('''Class _3:k8_{}Class y__5{Var $_B:String ;}Class _{Destructor (){z::$_.h();} }Class v_We9:s5{Val $_:Array [String ,31];}''','''Class,_3,:,k8_,{,},Class,y__5,{,Var,$_B,:,String,;,},Class,_,{,Destructor,(,),{,z,::,$_,.,h,(,),;,},},Class,v_We9,:,s5,{,Val,$_,:,Array,[,String,,,31,],;,},<EOF>''',101))

    def test_231(self):
        self.assertTrue(TestLexer.test('''Class _:_{Constructor (_b:Array [Array [Array [Float ,0b11_011_00],10],07_3];s,_:Array [Array [Int ,3_1],0b1000010];_:Boolean ){Break ;} }''','''Class,_,:,_,{,Constructor,(,_b,:,Array,[,Array,[,Array,[,Float,,,0b1101100,],,,10,],,,073,],;,s,,,_,:,Array,[,Array,[,Int,,,31,],,,0b1000010,],;,_,:,Boolean,),{,Break,;,},},<EOF>''',101))

    def test_232(self):
        self.assertTrue(TestLexer.test('''Class __7__{Constructor (){}Constructor (){}Var _,F5:_Awd;Constructor (_,r,J:Array [Int ,05]){}Var yZ,$y:Float ;Destructor (){} }''','''Class,__7__,{,Constructor,(,),{,},Constructor,(,),{,},Var,_,,,F5,:,_Awd,;,Constructor,(,_,,,r,,,J,:,Array,[,Int,,,05,],),{,},Var,yZ,,,$y,:,Float,;,Destructor,(,),{,},},<EOF>''',101))

    def test_233(self):
        self.assertTrue(TestLexer.test('''Class Wk:_{}Class v{}Class V:__4{$__M(_0u:Array [Int ,0xF];Y,C__3:Int ;____z_fD51q7n_,Xk____:bs_;_:_;_:Float ;_:Array [Int ,0X2]){} }Class W_1:v{}''','''Class,Wk,:,_,{,},Class,v,{,},Class,V,:,__4,{,$__M,(,_0u,:,Array,[,Int,,,0xF,],;,Y,,,C__3,:,Int,;,____z_fD51q7n_,,,Xk____,:,bs_,;,_,:,_,;,_,:,Float,;,_,:,Array,[,Int,,,0X2,],),{,},},Class,W_1,:,v,{,},<EOF>''',101))

    def test_234(self):
        self.assertTrue(TestLexer.test('''Class TM9X:_4{}Class X:__{Val $b:String ;$_(){ {}Return ;} }Class mh:r{_4_(){Continue ;} }Class __:s{Constructor (){} }Class N{}''','''Class,TM9X,:,_4,{,},Class,X,:,__,{,Val,$b,:,String,;,$_,(,),{,{,},Return,;,},},Class,mh,:,r,{,_4_,(,),{,Continue,;,},},Class,__,:,s,{,Constructor,(,),{,},},Class,N,{,},<EOF>''',101))

    def test_235(self):
        self.assertTrue(TestLexer.test('''Class XU5{e5(V:Array [Float ,50];_,_,x,f3,E:Float ){}Constructor (H_cy:_6){} }Class i:M{Constructor (_:String ){} }''','''Class,XU5,{,e5,(,V,:,Array,[,Float,,,50,],;,_,,,_,,,x,,,f3,,,E,:,Float,),{,},Constructor,(,H_cy,:,_6,),{,},},Class,i,:,M,{,Constructor,(,_,:,String,),{,},},<EOF>''',101))

    def test_236(self):
        self.assertTrue(TestLexer.test('''Class _:_{}Class _O{Constructor (_:uF;v,_,_,_c49,_v_,_B,X9:Array [Array [Array [Boolean ,5],59_54],0X2];_,_,_,_y:W;s_F:Array [Array [Int ,6],0B1_01]){}Constructor (){Return ;} }Class bR5{}Class o{}''','''Class,_,:,_,{,},Class,_O,{,Constructor,(,_,:,uF,;,v,,,_,,,_,,,_c49,,,_v_,,,_B,,,X9,:,Array,[,Array,[,Array,[,Boolean,,,5,],,,5954,],,,0X2,],;,_,,,_,,,_,,,_y,:,W,;,s_F,:,Array,[,Array,[,Int,,,6,],,,0B101,],),{,},Constructor,(,),{,Return,;,},},Class,bR5,{,},Class,o,{,},<EOF>''',101))

    def test_237(self):
        self.assertTrue(TestLexer.test('''Class k_{u772(n,_82:Array [String ,0xD]){}__(B__,_,_1,b,_,F,r_65:Boolean ;W:Float ;Y77:_4){}Destructor (){} }''','''Class,k_,{,u772,(,n,,,_82,:,Array,[,String,,,0xD,],),{,},__,(,B__,,,_,,,_1,,,b,,,_,,,F,,,r_65,:,Boolean,;,W,:,Float,;,Y77,:,_4,),{,},Destructor,(,),{,},},<EOF>''',101))

    def test_238(self):
        self.assertTrue(TestLexer.test('''Class __l{Constructor (){}Val $aG:Array [Array [Array [Array [Array [Array [String ,030],0X22],0b1000011],86],0170_6],0b1000011];}Class M__{Destructor (){Var M:String ;}Destructor (){} }''','''Class,__l,{,Constructor,(,),{,},Val,$aG,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,030,],,,0X22,],,,0b1000011,],,,86,],,,01706,],,,0b1000011,],;,},Class,M__,{,Destructor,(,),{,Var,M,:,String,;,},Destructor,(,),{,},},<EOF>''',101))

    def test_239(self):
        self.assertTrue(TestLexer.test('''Class w{Val $s,$_:Array [Float ,0x6];Constructor (j6v,_:String ;_37:Array [Array [Array [String ,6],0x5A],1]){} }Class N{}''','''Class,w,{,Val,$s,,,$_,:,Array,[,Float,,,0x6,],;,Constructor,(,j6v,,,_,:,String,;,_37,:,Array,[,Array,[,Array,[,String,,,6,],,,0x5A,],,,1,],),{,},},Class,N,{,},<EOF>''',101))

    def test_240(self):
        self.assertTrue(TestLexer.test('''Class _t{Var $5:String ;Val qMO_7_v,_6t:Int ;}Class _Q{Destructor (){} }Class K_{Constructor (_0,T4,_,U,O:L_){} }''','''Class,_t,{,Var,$5,:,String,;,Val,qMO_7_v,,,_6t,:,Int,;,},Class,_Q,{,Destructor,(,),{,},},Class,K_,{,Constructor,(,_0,,,T4,,,_,,,U,,,O,:,L_,),{,},},<EOF>''',101))

    def test_241(self):
        self.assertTrue(TestLexer.test('''Class a:s{}Class _3:s{Val q,$8p,V0__lL9__uF,L_:Array [Int ,0157];}Class yZ7{Val $__:Array [Array [Array [Float ,0105],4],23];}''','''Class,a,:,s,{,},Class,_3,:,s,{,Val,q,,,$8p,,,V0__lL9__uF,,,L_,:,Array,[,Int,,,0157,],;,},Class,yZ7,{,Val,$__,:,Array,[,Array,[,Array,[,Float,,,0105,],,,4,],,,23,],;,},<EOF>''',101))

    def test_242(self):
        self.assertTrue(TestLexer.test('''Class f{Val $_,$i_:u;Destructor (){} }Class __y7{Var _2,$__1,$a:Boolean ;Constructor (I0_6_7,J,T,P:Float ;_:Float ){} }Class _{}Class f{}''','''Class,f,{,Val,$_,,,$i_,:,u,;,Destructor,(,),{,},},Class,__y7,{,Var,_2,,,$__1,,,$a,:,Boolean,;,Constructor,(,I0_6_7,,,J,,,T,,,P,:,Float,;,_,:,Float,),{,},},Class,_,{,},Class,f,{,},<EOF>''',101))

    def test_243(self):
        self.assertTrue(TestLexer.test('''Class cH0_{Val $_:String =!_n._RM();Constructor (W__:_){}Constructor (){}Constructor (_:Boolean ;_p,L_,R_,Z7:String ;e_,_:String ;_7:Array [String ,0b1_0]){} }Class R{}''','''Class,cH0_,{,Val,$_,:,String,=,!,_n,.,_RM,(,),;,Constructor,(,W__,:,_,),{,},Constructor,(,),{,},Constructor,(,_,:,Boolean,;,_p,,,L_,,,R_,,,Z7,:,String,;,e_,,,_,:,String,;,_7,:,Array,[,String,,,0b10,],),{,},},Class,R,{,},<EOF>''',101))

    def test_244(self):
        self.assertTrue(TestLexer.test('''Class f:a3_{}Class zt{Destructor (){} }Class _:___{}Class U{Var __rTJi:String ;$_(){Val T94_:J;Val __,m,_:Q7;} }Class p{}Class OK{}''','''Class,f,:,a3_,{,},Class,zt,{,Destructor,(,),{,},},Class,_,:,___,{,},Class,U,{,Var,__rTJi,:,String,;,$_,(,),{,Val,T94_,:,J,;,Val,__,,,m,,,_,:,Q7,;,},},Class,p,{,},Class,OK,{,},<EOF>''',101))

    def test_245(self):
        self.assertTrue(TestLexer.test('''Class _{}Class Zh{Var _:Boolean ;Constructor (_:Array [String ,023_00]){} }Class _:e{}Class _:E{}Class _{Val S__,$D:_n;}''','''Class,_,{,},Class,Zh,{,Var,_,:,Boolean,;,Constructor,(,_,:,Array,[,String,,,02300,],),{,},},Class,_,:,e,{,},Class,_,:,E,{,},Class,_,{,Val,S__,,,$D,:,_n,;,},<EOF>''',101))

    def test_246(self):
        self.assertTrue(TestLexer.test('''Class _Y:__B{$i(){}Var _0CZq,C:Array [String ,10];}Class d{}Class gzX{Constructor (_,P301,_:Float ){}Destructor (){Val E:Boolean ;} }''','''Class,_Y,:,__B,{,$i,(,),{,},Var,_0CZq,,,C,:,Array,[,String,,,10,],;,},Class,d,{,},Class,gzX,{,Constructor,(,_,,,P301,,,_,:,Float,),{,},Destructor,(,),{,Val,E,:,Boolean,;,},},<EOF>''',101))

    def test_247(self):
        self.assertTrue(TestLexer.test('''Class _{Constructor (B5:Array [String ,0XB];_1:Array [Boolean ,06_1];Oh__:V;_3yE,V,_,s_,___90i,o_Kd,_,_:Array [Int ,5]){} }Class _T:X{Var $J_,$_:Array [String ,065];}Class _{}''','''Class,_,{,Constructor,(,B5,:,Array,[,String,,,0XB,],;,_1,:,Array,[,Boolean,,,061,],;,Oh__,:,V,;,_3yE,,,V,,,_,,,s_,,,___90i,,,o_Kd,,,_,,,_,:,Array,[,Int,,,5,],),{,},},Class,_T,:,X,{,Var,$J_,,,$_,:,Array,[,String,,,065,],;,},Class,_,{,},<EOF>''',101))

    def test_248(self):
        self.assertTrue(TestLexer.test('''Class _ta{}Class _{Destructor (){} }Class t_7:U5_R{Var $V:i;Var ___:Array [Array [Array [Array [Array [Array [Array [Boolean ,28_6],0b110001],60],60],0B1000110],0XD],0B1];}''','''Class,_ta,{,},Class,_,{,Destructor,(,),{,},},Class,t_7,:,U5_R,{,Var,$V,:,i,;,Var,___,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,286,],,,0b110001,],,,60,],,,60,],,,0B1000110,],,,0XD,],,,0B1,],;,},<EOF>''',101))

    def test_249(self):
        self.assertTrue(TestLexer.test('''Class _:U{}Class syQ8_:_{}Class V{$_u10(K_509_,_2F,C:_;k,__,GA:Array [Int ,0b1]){}Constructor (_O_,L:_;_6_:Float ;a_,_:_26y;_,_,e,XT:_;_14_,Dy,__v6:Array [String ,0B1111];_,__,_S,W87,t:Array [Array [Array [Array [Boolean ,8],0B1111],036],44];_2,_,_,_,_:Boolean ){Continue ;}T(z_:Int ){} }''','''Class,_,:,U,{,},Class,syQ8_,:,_,{,},Class,V,{,$_u10,(,K_509_,,,_2F,,,C,:,_,;,k,,,__,,,GA,:,Array,[,Int,,,0b1,],),{,},Constructor,(,_O_,,,L,:,_,;,_6_,:,Float,;,a_,,,_,:,_26y,;,_,,,_,,,e,,,XT,:,_,;,_14_,,,Dy,,,__v6,:,Array,[,String,,,0B1111,],;,_,,,__,,,_S,,,W87,,,t,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,8,],,,0B1111,],,,036,],,,44,],;,_2,,,_,,,_,,,_,,,_,:,Boolean,),{,Continue,;,},T,(,z_,:,Int,),{,},},<EOF>''',101))

    def test_250(self):
        self.assertTrue(TestLexer.test('''Class _:_{A(_,NA_:_f__;_,q,q_L:Array [Boolean ,0106];_:Array [Array [String ,0xD],25];Y_,_2__:Array [Int ,0106];U,B7,__i,E73_,H,_:Array [Float ,8];__,u8:_0_4;_I,_:Array [Array [Array [Array [Int ,0xD],0X12],0B1_1],8_5];_B,t,A_:__;_:g;_aX:String ){} }''','''Class,_,:,_,{,A,(,_,,,NA_,:,_f__,;,_,,,q,,,q_L,:,Array,[,Boolean,,,0106,],;,_,:,Array,[,Array,[,String,,,0xD,],,,25,],;,Y_,,,_2__,:,Array,[,Int,,,0106,],;,U,,,B7,,,__i,,,E73_,,,H,,,_,:,Array,[,Float,,,8,],;,__,,,u8,:,_0_4,;,_I,,,_,:,Array,[,Array,[,Array,[,Array,[,Int,,,0xD,],,,0X12,],,,0B11,],,,85,],;,_B,,,t,,,A_,:,__,;,_,:,g,;,_aX,:,String,),{,},},<EOF>''',101))

    def test_251(self):
        self.assertTrue(TestLexer.test('''Class WT_2{$2_(__3:Array [Array [Array [Array [String ,0b1],0x8],0X24],0xCF]){} }Class _a:_{Var $u:Int ;}Class _1{$j_(_:I;V:Boolean ){} }''','''Class,WT_2,{,$2_,(,__3,:,Array,[,Array,[,Array,[,Array,[,String,,,0b1,],,,0x8,],,,0X24,],,,0xCF,],),{,},},Class,_a,:,_,{,Var,$u,:,Int,;,},Class,_1,{,$j_,(,_,:,I,;,V,:,Boolean,),{,},},<EOF>''',101))

    def test_252(self):
        self.assertTrue(TestLexer.test('''Class J{Val b,l:l;}Class _9Lw_:z{Var U,$__,$_,_o,$_r:Array [String ,9_8];}Class t2s1bY1:X9{Val __:Int ;}Class _9{}''','''Class,J,{,Val,b,,,l,:,l,;,},Class,_9Lw_,:,z,{,Var,U,,,$__,,,$_,,,_o,,,$_r,:,Array,[,String,,,98,],;,},Class,t2s1bY1,:,X9,{,Val,__,:,Int,;,},Class,_9,{,},<EOF>''',101))

    def test_253(self):
        self.assertTrue(TestLexer.test('''Class B2W{Constructor (R_A:Array [Boolean ,0b1];Q:Array [Array [Array [Array [Float ,0x6],023_01],0B101000],2];_,__:Float ;l,E:Array [Array [String ,77],0x3_1];__6_6:Boolean ;_3_,_CY,PV9_L_3Z_W,Jy:Array [Array [Array [Float ,246],051],0X5B]){}V(I:Array [Int ,05]){}Constructor (M:Array [Float ,0XDA_D]){} }''','''Class,B2W,{,Constructor,(,R_A,:,Array,[,Boolean,,,0b1,],;,Q,:,Array,[,Array,[,Array,[,Array,[,Float,,,0x6,],,,02301,],,,0B101000,],,,2,],;,_,,,__,:,Float,;,l,,,E,:,Array,[,Array,[,String,,,77,],,,0x31,],;,__6_6,:,Boolean,;,_3_,,,_CY,,,PV9_L_3Z_W,,,Jy,:,Array,[,Array,[,Array,[,Float,,,246,],,,051,],,,0X5B,],),{,},V,(,I,:,Array,[,Int,,,05,],),{,},Constructor,(,M,:,Array,[,Float,,,0XDAD,],),{,},},<EOF>''',101))

    def test_254(self):
        self.assertTrue(TestLexer.test('''Class y{Constructor (u9_2y:Array [Array [Array [Array [Array [Float ,1],071],071],17_6],0X32];Ec_B,_7:Boolean ){} }''','''Class,y,{,Constructor,(,u9_2y,:,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,1,],,,071,],,,071,],,,176,],,,0X32,],;,Ec_B,,,_7,:,Boolean,),{,},},<EOF>''',101))

    def test_255(self):
        self.assertTrue(TestLexer.test('''Class _B1{Var $y,_:__;}Class u:__{Val e1:Array [Array [Boolean ,100],100];Destructor (){}Destructor (){}Destructor (){} }''','''Class,_B1,{,Var,$y,,,_,:,__,;,},Class,u,:,__,{,Val,e1,:,Array,[,Array,[,Boolean,,,100,],,,100,],;,Destructor,(,),{,},Destructor,(,),{,},Destructor,(,),{,},},<EOF>''',101))

    def test_256(self):
        self.assertTrue(TestLexer.test('''Class _:_{Constructor (__:_;_,_:Array [Array [Array [Int ,4],0137],0b1011100];_,y:Array [String ,0B100001];e,n,W:Array [Boolean ,07]){}_(___q:_8){Break ;}Constructor (){} }''','''Class,_,:,_,{,Constructor,(,__,:,_,;,_,,,_,:,Array,[,Array,[,Array,[,Int,,,4,],,,0137,],,,0b1011100,],;,_,,,y,:,Array,[,String,,,0B100001,],;,e,,,n,,,W,:,Array,[,Boolean,,,07,],),{,},_,(,___q,:,_8,),{,Break,;,},Constructor,(,),{,},},<EOF>''',101))

    def test_257(self):
        self.assertTrue(TestLexer.test('''Class Sn{Val _,ekDP3,_,Y_9KlI,$1098,_,$__0:___;Val $1_9,_,_5,_,$_bE,$u5,h:String ;Val $76:Array [Array [Float ,0x43],07_7];}''','''Class,Sn,{,Val,_,,,ekDP3,,,_,,,Y_9KlI,,,$1098,,,_,,,$__0,:,___,;,Val,$1_9,,,_,,,_5,,,_,,,$_bE,,,$u5,,,h,:,String,;,Val,$76,:,Array,[,Array,[,Float,,,0x43,],,,077,],;,},<EOF>''',101))

    def test_258(self):
        self.assertTrue(TestLexer.test('''Class _677{Constructor (Km_,F:Array [Array [Boolean ,0B1],0X57];k:Float ){Continue ;}Var hi:S_;}Class KAu_:p7P_{Val _,$_8_2,l,zXt:String ;}Class _:VL1210{Var _,S,$d____:Array [Float ,0b1];}''','''Class,_677,{,Constructor,(,Km_,,,F,:,Array,[,Array,[,Boolean,,,0B1,],,,0X57,],;,k,:,Float,),{,Continue,;,},Var,hi,:,S_,;,},Class,KAu_,:,p7P_,{,Val,_,,,$_8_2,,,l,,,zXt,:,String,;,},Class,_,:,VL1210,{,Var,_,,,S,,,$d____,:,Array,[,Float,,,0b1,],;,},<EOF>''',101))

    def test_259(self):
        self.assertTrue(TestLexer.test('''Class _7:y{Destructor (){} }Class q:I{Val n__,D,$AJ,$_:Array [Array [Array [Array [String ,0x5B],0B11010],4],5];}Class aj13:mG6_5{}''','''Class,_7,:,y,{,Destructor,(,),{,},},Class,q,:,I,{,Val,n__,,,D,,,$AJ,,,$_,:,Array,[,Array,[,Array,[,Array,[,String,,,0x5B,],,,0B11010,],,,4,],,,5,],;,},Class,aj13,:,mG6_5,{,},<EOF>''',101))

    def test_260(self):
        self.assertTrue(TestLexer.test('''Class J_eL5{}Class N:_3L{}Class ___d:m{$4_(_J:_o;L:Array [Array [Array [Array [Array [String ,076],0B1010001],0B1],0X11],0x44];_R:Array [Float ,0B1]){Break ;Val _:S9_;} }Class _:_{}''','''Class,J_eL5,{,},Class,N,:,_3L,{,},Class,___d,:,m,{,$4_,(,_J,:,_o,;,L,:,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,076,],,,0B1010001,],,,0B1,],,,0X11,],,,0x44,],;,_R,:,Array,[,Float,,,0B1,],),{,Break,;,Val,_,:,S9_,;,},},Class,_,:,_,{,},<EOF>''',101))

    def test_261(self):
        self.assertTrue(TestLexer.test('''Class S:_{Constructor (__:_;z7:Boolean ;g_:Array [Array [Array [Array [Array [Int ,2_5],0704],0105],3],0x21]){} }Class D{Destructor (){} }''','''Class,S,:,_,{,Constructor,(,__,:,_,;,z7,:,Boolean,;,g_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,25,],,,0704,],,,0105,],,,3,],,,0x21,],),{,},},Class,D,{,Destructor,(,),{,},},<EOF>''',101))

    def test_262(self):
        self.assertTrue(TestLexer.test('''Class P:_E3t_{}Class u:_l{p(_9:Array [Array [String ,02],5]){MX1::$5();} }Class Z:_{}Class _:WJ4_{}Class _6{}Class bh0_:V2d{Val $86,$_Nt5,$r_8:GR;}''','''Class,P,:,_E3t_,{,},Class,u,:,_l,{,p,(,_9,:,Array,[,Array,[,String,,,02,],,,5,],),{,MX1,::,$5,(,),;,},},Class,Z,:,_,{,},Class,_,:,WJ4_,{,},Class,_6,{,},Class,bh0_,:,V2d,{,Val,$86,,,$_Nt5,,,$r_8,:,GR,;,},<EOF>''',101))

    def test_263(self):
        self.assertTrue(TestLexer.test('''Class H{}Class T7:_{Var $K,_u1,_,$26o_,_:Array [Array [Array [Array [Array [Boolean ,067],2],0B1001001],0xE_20],9_29_98_1_713];}Class _q_{}''','''Class,H,{,},Class,T7,:,_,{,Var,$K,,,_u1,,,_,,,$26o_,,,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,067,],,,2,],,,0B1001001,],,,0xE20,],,,929981713,],;,},Class,_q_,{,},<EOF>''',101))

    def test_264(self):
        self.assertTrue(TestLexer.test('''Class U{}Class W:b{Var M,_r5M:Array [Array [Array [Array [Array [Array [Float ,7_2_9_5],3],0X22],0xC_3C7_D5_0],0140],22];}Class _q:w___{}Class _{}''','''Class,U,{,},Class,W,:,b,{,Var,M,,,_r5M,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,7295,],,,3,],,,0X22,],,,0xC3C7D50,],,,0140,],,,22,],;,},Class,_q,:,w___,{,},Class,_,{,},<EOF>''',101))

    def test_265(self):
        self.assertTrue(TestLexer.test('''Class yj:V{$_1H(_:String ;_:_y_5B;_,z:Array [Array [String ,0x48],057];G__6,m,Qr,_,__B4:_X;__:Array [Array [Float ,02],017]){} }''','''Class,yj,:,V,{,$_1H,(,_,:,String,;,_,:,_y_5B,;,_,,,z,:,Array,[,Array,[,String,,,0x48,],,,057,],;,G__6,,,m,,,Qr,,,_,,,__B4,:,_X,;,__,:,Array,[,Array,[,Float,,,02,],,,017,],),{,},},<EOF>''',101))

    def test_266(self):
        self.assertTrue(TestLexer.test('''Class q_{}Class _:Z{}Class _:wjjX{Constructor (F60_6_,_,_,F:Boolean ;q:Array [Int ,0X15]){R::$_();}Var $2:s=!!!!!New D();}''','''Class,q_,{,},Class,_,:,Z,{,},Class,_,:,wjjX,{,Constructor,(,F60_6_,,,_,,,_,,,F,:,Boolean,;,q,:,Array,[,Int,,,0X15,],),{,R,::,$_,(,),;,},Var,$2,:,s,=,!,!,!,!,!,New,D,(,),;,},<EOF>''',101))

    def test_267(self):
        self.assertTrue(TestLexer.test('''Class _:_{Constructor (x:_;_:Array [Array [Int ,1_8_21],01];__p7_,V:xN;L:Float ){} }Class wX_37:_a{Destructor (){} }Class __:_{}''','''Class,_,:,_,{,Constructor,(,x,:,_,;,_,:,Array,[,Array,[,Int,,,1821,],,,01,],;,__p7_,,,V,:,xN,;,L,:,Float,),{,},},Class,wX_37,:,_a,{,Destructor,(,),{,},},Class,__,:,_,{,},<EOF>''',101))

    def test_268(self):
        self.assertTrue(TestLexer.test('''Class B:_{Constructor (Vx:Int ;_k,__:_){} }Class _:_N{Destructor (){}Var o:Float ;}Class _O:M{Var E:Int ;}Class __:s{Destructor (){} }''','''Class,B,:,_,{,Constructor,(,Vx,:,Int,;,_k,,,__,:,_,),{,},},Class,_,:,_N,{,Destructor,(,),{,},Var,o,:,Float,;,},Class,_O,:,M,{,Var,E,:,Int,;,},Class,__,:,s,{,Destructor,(,),{,},},<EOF>''',101))

    def test_269(self):
        self.assertTrue(TestLexer.test('''Class aZ44:_{}Class _:___57__i8{}Class dAutk0:Ae{}Class Tm{Val $7,$2N_,U_:String ;Var _:Array [Array [Float ,022],9];}''','''Class,aZ44,:,_,{,},Class,_,:,___57__i8,{,},Class,dAutk0,:,Ae,{,},Class,Tm,{,Val,$7,,,$2N_,,,U_,:,String,;,Var,_,:,Array,[,Array,[,Float,,,022,],,,9,],;,},<EOF>''',101))

    def test_270(self):
        self.assertTrue(TestLexer.test('''Class __1_se{}Class _g:_E2__35__5{}Class _{Constructor (){Break ;} }Class K_{}Class H{}Class _{Constructor (){Continue ;} }''','''Class,__1_se,{,},Class,_g,:,_E2__35__5,{,},Class,_,{,Constructor,(,),{,Break,;,},},Class,K_,{,},Class,H,{,},Class,_,{,Constructor,(,),{,Continue,;,},},<EOF>''',101))

    def test_271(self):
        self.assertTrue(TestLexer.test('''Class _:_G{Var _S,T7_:_;t(O,q,k_,_E:Array [Array [Array [Array [Int ,0X9],0b110110],0x2F_5_8],03];__7_,V:Float ){} }''','''Class,_,:,_G,{,Var,_S,,,T7_,:,_,;,t,(,O,,,q,,,k_,,,_E,:,Array,[,Array,[,Array,[,Array,[,Int,,,0X9,],,,0b110110,],,,0x2F58,],,,03,],;,__7_,,,V,:,Float,),{,},},<EOF>''',101))

    def test_272(self):
        self.assertTrue(TestLexer.test('''Class i_{Var EP1__,$_:Array [Array [Boolean ,05_5],5];}Class _A:_{Constructor (e3_d_Hy:Array [Int ,040]){ {Return ;} }Constructor (){}$1(_n_Xm,Y,q,_:__3;__1_,_p7,_R2_,h_Z:Array [Array [Array [String ,0X59],040],947_71_06]){} }Class _4W{}Class _k_:w{Var f:Array [Array [Array [Boolean ,0b1010],0XB],040]=-J::$098P_60a;}''','''Class,i_,{,Var,EP1__,,,$_,:,Array,[,Array,[,Boolean,,,055,],,,5,],;,},Class,_A,:,_,{,Constructor,(,e3_d_Hy,:,Array,[,Int,,,040,],),{,{,Return,;,},},Constructor,(,),{,},$1,(,_n_Xm,,,Y,,,q,,,_,:,__3,;,__1_,,,_p7,,,_R2_,,,h_Z,:,Array,[,Array,[,Array,[,String,,,0X59,],,,040,],,,9477106,],),{,},},Class,_4W,{,},Class,_k_,:,w,{,Var,f,:,Array,[,Array,[,Array,[,Boolean,,,0b1010,],,,0XB,],,,040,],=,-,J,::,$098P_60a,;,},<EOF>''',101))

    def test_273(self):
        self.assertTrue(TestLexer.test('''Class N4:_{Constructor (){Break ;}Val $__:etf;}Class e6{$_(E:Array [Array [Boolean ,0X5F],0X5F];_m:Array [Array [Array [Array [String ,4_26_2_8_5],33],0x34_A],0B11];_:_;k_,_6JQs,_,_,_2wZ_1:Array [Array [Int ,0X3_B],06_6_101]){} }''','''Class,N4,:,_,{,Constructor,(,),{,Break,;,},Val,$__,:,etf,;,},Class,e6,{,$_,(,E,:,Array,[,Array,[,Boolean,,,0X5F,],,,0X5F,],;,_m,:,Array,[,Array,[,Array,[,Array,[,String,,,426285,],,,33,],,,0x34A,],,,0B11,],;,_,:,_,;,k_,,,_6JQs,,,_,,,_,,,_2wZ_1,:,Array,[,Array,[,Int,,,0X3B,],,,066101,],),{,},},<EOF>''',101))

    def test_274(self):
        self.assertTrue(TestLexer.test('''Class _{Val t__4,$kc:Array [Array [Array [Boolean ,0B10_0],0142],0X9];}Class _RPN3Cw_9_k{}Class g{Val Qj_,$W:Float ;}Class _:__v7{}Class _3{}Class O{}''','''Class,_,{,Val,t__4,,,$kc,:,Array,[,Array,[,Array,[,Boolean,,,0B100,],,,0142,],,,0X9,],;,},Class,_RPN3Cw_9_k,{,},Class,g,{,Val,Qj_,,,$W,:,Float,;,},Class,_,:,__v7,{,},Class,_3,{,},Class,O,{,},<EOF>''',101))

    def test_275(self):
        self.assertTrue(TestLexer.test('''Class R{}Class _5_:YY{Constructor (){}Var $_:Array [Array [Array [Array [Boolean ,07],7],36],0x1_7];Val _2_:String ;}''','''Class,R,{,},Class,_5_,:,YY,{,Constructor,(,),{,},Var,$_,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,07,],,,7,],,,36,],,,0x17,],;,Val,_2_,:,String,;,},<EOF>''',101))

    def test_276(self):
        self.assertTrue(TestLexer.test('''Class A:_5{Var P:TO;Destructor (){Return ;} }Class D{$y(k_:String ;_1,S8w:Int ){_bu::$0();Break ;} }Class h{}Class o:m{}''','''Class,A,:,_5,{,Var,P,:,TO,;,Destructor,(,),{,Return,;,},},Class,D,{,$y,(,k_,:,String,;,_1,,,S8w,:,Int,),{,_bu,::,$0,(,),;,Break,;,},},Class,h,{,},Class,o,:,m,{,},<EOF>''',101))

    def test_277(self):
        self.assertTrue(TestLexer.test('''Class tR:_{}Class d{}Class C_:_{}Class D_:w{}Class _{}Class _s:M11{}Class i:B{T46W9_(__,g,_,_:_JcgW;_:__E;__,f:Array [Float ,0B1];E08:__;_0G:_){Continue ;}Constructor (){}Constructor (){} }''','''Class,tR,:,_,{,},Class,d,{,},Class,C_,:,_,{,},Class,D_,:,w,{,},Class,_,{,},Class,_s,:,M11,{,},Class,i,:,B,{,T46W9_,(,__,,,g,,,_,,,_,:,_JcgW,;,_,:,__E,;,__,,,f,:,Array,[,Float,,,0B1,],;,E08,:,__,;,_0G,:,_,),{,Continue,;,},Constructor,(,),{,},Constructor,(,),{,},},<EOF>''',101))

    def test_278(self):
        self.assertTrue(TestLexer.test('''Class _9{Val r_,$1_:_86;Destructor (){} }Class x:b0b{}Class z{Val V,Vfl5,$i:Array [Array [Boolean ,062_6],0b1];Destructor (){} }''','''Class,_9,{,Val,r_,,,$1_,:,_86,;,Destructor,(,),{,},},Class,x,:,b0b,{,},Class,z,{,Val,V,,,Vfl5,,,$i,:,Array,[,Array,[,Boolean,,,0626,],,,0b1,],;,Destructor,(,),{,},},<EOF>''',101))

    def test_279(self):
        self.assertTrue(TestLexer.test('''Class x:_{Constructor (__:String ;mU:Array [Array [Array [Array [String ,9_3],0x48],0X2B],032_3_0];Q4,_,c,_7:String ){Var v,I_:Array [Array [Array [Float ,0b1010011],02],03_6];} }Class _:U{}''','''Class,x,:,_,{,Constructor,(,__,:,String,;,mU,:,Array,[,Array,[,Array,[,Array,[,String,,,93,],,,0x48,],,,0X2B,],,,03230,],;,Q4,,,_,,,c,,,_7,:,String,),{,Var,v,,,I_,:,Array,[,Array,[,Array,[,Float,,,0b1010011,],,,02,],,,036,],;,},},Class,_,:,U,{,},<EOF>''',101))

    def test_280(self):
        self.assertTrue(TestLexer.test('''Class P{}Class __:f0{Var $_,_u,_:Array [Array [Array [Array [Array [Float ,0XE],0B1011000],06],0xC_B9],0B1];Var $_:Boolean ;}Class SL{}Class u:h{Var $c_,$r:Boolean ;}''','''Class,P,{,},Class,__,:,f0,{,Var,$_,,,_u,,,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0XE,],,,0B1011000,],,,06,],,,0xCB9,],,,0B1,],;,Var,$_,:,Boolean,;,},Class,SL,{,},Class,u,:,h,{,Var,$c_,,,$r,:,Boolean,;,},<EOF>''',101))

    def test_281(self):
        self.assertTrue(TestLexer.test('''Class _:_{}Class g_{Var q_R7:M_;Val hy,f,$B6Q,$G_,$F,__7A,r:Array [Array [Array [Float ,0x5C],0110],0110];}Class m{}''','''Class,_,:,_,{,},Class,g_,{,Var,q_R7,:,M_,;,Val,hy,,,f,,,$B6Q,,,$G_,,,$F,,,__7A,,,r,:,Array,[,Array,[,Array,[,Float,,,0x5C,],,,0110,],,,0110,],;,},Class,m,{,},<EOF>''',101))

    def test_282(self):
        self.assertTrue(TestLexer.test('''Class L_:i{Val $_p,v2_:_;}Class _:J0{r_g(){ {} }}Class _jc:_{Val $J:String ;}Class _3F:_{}Class _{Destructor (){}Var $F:_5;Destructor (){}Constructor (_,hs:String ;ik,aa:Float ;W:Array [Array [Array [Array [Boolean ,062],65],05],0b1]){Continue ;O::$_();} }''','''Class,L_,:,i,{,Val,$_p,,,v2_,:,_,;,},Class,_,:,J0,{,r_g,(,),{,{,},},},Class,_jc,:,_,{,Val,$J,:,String,;,},Class,_3F,:,_,{,},Class,_,{,Destructor,(,),{,},Var,$F,:,_5,;,Destructor,(,),{,},Constructor,(,_,,,hs,:,String,;,ik,,,aa,:,Float,;,W,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,062,],,,65,],,,05,],,,0b1,],),{,Continue,;,O,::,$_,(,),;,},},<EOF>''',101))

    def test_283(self):
        self.assertTrue(TestLexer.test('''Class q:i{Constructor (eA_:I7;x_9Q_26je1__:Float ;__:Array [Int ,0B101011];Ke:Float ){}Val $___:Array [Array [String ,0B101011],0b10];}''','''Class,q,:,i,{,Constructor,(,eA_,:,I7,;,x_9Q_26je1__,:,Float,;,__,:,Array,[,Int,,,0B101011,],;,Ke,:,Float,),{,},Val,$___,:,Array,[,Array,[,String,,,0B101011,],,,0b10,],;,},<EOF>''',101))

    def test_284(self):
        self.assertTrue(TestLexer.test('''Class _r:_{$3(Z,Y7,S_:Array [Float ,037];C,Xv:Array [Array [Float ,03_7_3],05426];__,J,_2,__g_,_,_233:String ){Break ;} }''','''Class,_r,:,_,{,$3,(,Z,,,Y7,,,S_,:,Array,[,Float,,,037,],;,C,,,Xv,:,Array,[,Array,[,Float,,,0373,],,,05426,],;,__,,,J,,,_2,,,__g_,,,_,,,_233,:,String,),{,Break,;,},},<EOF>''',101))

    def test_285(self):
        self.assertTrue(TestLexer.test('''Class _a7_{Var _:Array [Array [Array [Boolean ,80],0B1_0_0],0b1];_(){Break ;Continue ;Var _,_:String ;} }Class __7M:w{Val g_,_,p4:OPB3;}''','''Class,_a7_,{,Var,_,:,Array,[,Array,[,Array,[,Boolean,,,80,],,,0B100,],,,0b1,],;,_,(,),{,Break,;,Continue,;,Var,_,,,_,:,String,;,},},Class,__7M,:,w,{,Val,g_,,,_,,,p4,:,OPB3,;,},<EOF>''',101))

    def test_286(self):
        self.assertTrue(TestLexer.test('''Class _:_5h{}Class _1{}Class P{}Class _g:Z9p{}Class Q2___:d{}Class fx3{}Class _:N_{}Class _F__j:__k{}Class K:D{}''','''Class,_,:,_5h,{,},Class,_1,{,},Class,P,{,},Class,_g,:,Z9p,{,},Class,Q2___,:,d,{,},Class,fx3,{,},Class,_,:,N_,{,},Class,_F__j,:,__k,{,},Class,K,:,D,{,},<EOF>''',101))

    def test_287(self):
        self.assertTrue(TestLexer.test('''Class Zq:L{Constructor (q_5__,_,_,_,_LY_,L2:Array [Array [Boolean ,0b101010],0b101010];p,____,U_,_:Array [Array [Boolean ,07_6_4],02];tz,m7,_,w__l__94:Int ){} }''','''Class,Zq,:,L,{,Constructor,(,q_5__,,,_,,,_,,,_,,,_LY_,,,L2,:,Array,[,Array,[,Boolean,,,0b101010,],,,0b101010,],;,p,,,____,,,U_,,,_,:,Array,[,Array,[,Boolean,,,0764,],,,02,],;,tz,,,m7,,,_,,,w__l__94,:,Int,),{,},},<EOF>''',101))

    def test_288(self):
        self.assertTrue(TestLexer.test('''Class ZrS6:w6{}Class _:t6_{Var z,_:Boolean ;$1_(n:_){} }Class a79{_(_:Array [Array [Array [Array [Array [Array [Int ,0X9],28],0x7],0b100101],2],0XF]){} }Class sp:N{q_(_:Boolean ){ {} }$r8(){Val X:__c;} }Class _:E{}Class _:_R{}''','''Class,ZrS6,:,w6,{,},Class,_,:,t6_,{,Var,z,,,_,:,Boolean,;,$1_,(,n,:,_,),{,},},Class,a79,{,_,(,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0X9,],,,28,],,,0x7,],,,0b100101,],,,2,],,,0XF,],),{,},},Class,sp,:,N,{,q_,(,_,:,Boolean,),{,{,},},$r8,(,),{,Val,X,:,__c,;,},},Class,_,:,E,{,},Class,_,:,_R,{,},<EOF>''',101))

    def test_289(self):
        self.assertTrue(TestLexer.test('''Class f_:_F1_{Var $_,__,$_8b,$_1,w,Q,_1_:Array [Array [Array [Array [Float ,05],47],5_618_56],0xC];$9(X1,C:Boolean ){} }''','''Class,f_,:,_F1_,{,Var,$_,,,__,,,$_8b,,,$_1,,,w,,,Q,,,_1_,:,Array,[,Array,[,Array,[,Array,[,Float,,,05,],,,47,],,,561856,],,,0xC,],;,$9,(,X1,,,C,:,Boolean,),{,},},<EOF>''',101))

    def test_290(self):
        self.assertTrue(TestLexer.test('''Class _:H{Var __:_1_C__;}Class uO{_d_3(l,_,__j,l__:Bi_J8){}Val $__0,b,$_,W:Array [Int ,0XD_8A];}Class _W_:_{Constructor (E,_,_ff,X:Array [Array [Array [Int ,0B11011],02],1]){} }''','''Class,_,:,H,{,Var,__,:,_1_C__,;,},Class,uO,{,_d_3,(,l,,,_,,,__j,,,l__,:,Bi_J8,),{,},Val,$__0,,,b,,,$_,,,W,:,Array,[,Int,,,0XD8A,],;,},Class,_W_,:,_,{,Constructor,(,E,,,_,,,_ff,,,X,:,Array,[,Array,[,Array,[,Int,,,0B11011,],,,02,],,,1,],),{,},},<EOF>''',101))

    def test_291(self):
        self.assertTrue(TestLexer.test('''Class G:_x5{}Class Z:_{Constructor (d:_;_x_05,f,_:Array [Array [Array [String ,0x3],2],87];_4,d,a3K,__,w_u69_:Array [Array [Array [Array [String ,0X5E],87],0x4A],0xFF_4]){} }''','''Class,G,:,_x5,{,},Class,Z,:,_,{,Constructor,(,d,:,_,;,_x_05,,,f,,,_,:,Array,[,Array,[,Array,[,String,,,0x3,],,,2,],,,87,],;,_4,,,d,,,a3K,,,__,,,w_u69_,:,Array,[,Array,[,Array,[,Array,[,String,,,0X5E,],,,87,],,,0x4A,],,,0xFF4,],),{,},},<EOF>''',101))

    def test_292(self):
        self.assertTrue(TestLexer.test('''Class A:Ssk2Y_3_5_{Destructor (){} }Class _:_K{Var RN,_,$dB,$_q,$0_,_B_5R_,$s9,$6,$___2,$W:Array [Array [Float ,0X32],0131];Var _,$____:Int ;}Class rK{Destructor (){} }Class _3{_(__:Float ){__xi7_2::$Z4.v92_()._();} }''','''Class,A,:,Ssk2Y_3_5_,{,Destructor,(,),{,},},Class,_,:,_K,{,Var,RN,,,_,,,$dB,,,$_q,,,$0_,,,_B_5R_,,,$s9,,,$6,,,$___2,,,$W,:,Array,[,Array,[,Float,,,0X32,],,,0131,],;,Var,_,,,$____,:,Int,;,},Class,rK,{,Destructor,(,),{,},},Class,_3,{,_,(,__,:,Float,),{,__xi7_2,::,$Z4,.,v92_,(,),.,_,(,),;,},},<EOF>''',101))

    def test_293(self):
        self.assertTrue(TestLexer.test('''Class _0_82V:f_0{Constructor (_5:Int ){Continue ;}Var $J_:Int ;}Class u3v5V:_{Constructor (){} }Class X5C__:_{}''','''Class,_0_82V,:,f_0,{,Constructor,(,_5,:,Int,),{,Continue,;,},Var,$J_,:,Int,;,},Class,u3v5V,:,_,{,Constructor,(,),{,},},Class,X5C__,:,_,{,},<EOF>''',101))

    def test_294(self):
        self.assertTrue(TestLexer.test('''Class A{Constructor (O,_9,_Z:_;M,f:Float ;_,D,g,_,_cm:Int ;V:QC;_2_:Array [Array [Array [String ,0x4],044_77],50]){Var x3ty,_,_,_,y95,h_:o5214_;} }''','''Class,A,{,Constructor,(,O,,,_9,,,_Z,:,_,;,M,,,f,:,Float,;,_,,,D,,,g,,,_,,,_cm,:,Int,;,V,:,QC,;,_2_,:,Array,[,Array,[,Array,[,String,,,0x4,],,,04477,],,,50,],),{,Var,x3ty,,,_,,,_,,,_,,,y95,,,h_,:,o5214_,;,},},<EOF>''',101))

    def test_295(self):
        self.assertTrue(TestLexer.test('''Class __0__4{Constructor (G_:String ;_79,P,o_y_:Array [Array [Array [Float ,0130],0b1111_1],0xD_C];xm:Int ){}Destructor (){} }Class i3{}''','''Class,__0__4,{,Constructor,(,G_,:,String,;,_79,,,P,,,o_y_,:,Array,[,Array,[,Array,[,Float,,,0130,],,,0b11111,],,,0xDC,],;,xm,:,Int,),{,},Destructor,(,),{,},},Class,i3,{,},<EOF>''',101))

    def test_296(self):
        self.assertTrue(TestLexer.test('''Class QJ:_{Val _,N2,$L__7i,_,N_,$fj:Int ;Constructor (_y0,s0V_,j5,_:Float ;___:Array [Float ,4]){Continue ;} }Class O:X{}''','''Class,QJ,:,_,{,Val,_,,,N2,,,$L__7i,,,_,,,N_,,,$fj,:,Int,;,Constructor,(,_y0,,,s0V_,,,j5,,,_,:,Float,;,___,:,Array,[,Float,,,4,],),{,Continue,;,},},Class,O,:,X,{,},<EOF>''',101))

    def test_297(self):
        self.assertTrue(TestLexer.test('''Class m:_9{}Class _39:y1{}Class f2_{}Class _u_1{Val $46:Boolean ;Var _4qO,$_3:Array [Array [Float ,0X4A],065];}Class _TM:_{}Class H0_{}''','''Class,m,:,_9,{,},Class,_39,:,y1,{,},Class,f2_,{,},Class,_u_1,{,Val,$46,:,Boolean,;,Var,_4qO,,,$_3,:,Array,[,Array,[,Float,,,0X4A,],,,065,],;,},Class,_TM,:,_,{,},Class,H0_,{,},<EOF>''',101))

    def test_298(self):
        self.assertTrue(TestLexer.test('''Class C:_{Constructor (k,_:A5;p,fC8008,_:Array [Array [Array [Int ,0X59],99],0x12];_3_:_;_1W39:Int ){Break ;}$N2A_7_(___3:P_){}Val $E99dk,$_,_:_;}Class pE{}Class G9{Destructor (){} }''','''Class,C,:,_,{,Constructor,(,k,,,_,:,A5,;,p,,,fC8008,,,_,:,Array,[,Array,[,Array,[,Int,,,0X59,],,,99,],,,0x12,],;,_3_,:,_,;,_1W39,:,Int,),{,Break,;,},$N2A_7_,(,___3,:,P_,),{,},Val,$E99dk,,,$_,,,_,:,_,;,},Class,pE,{,},Class,G9,{,Destructor,(,),{,},},<EOF>''',101))

    def test_299(self):
        self.assertTrue(TestLexer.test('''Class _:_{Var _,_R6:Int ;V(){}$_(_3,_,_,W_,L9,_G_q6vf4e3_:Int ;_,_:Array [Array [Array [Float ,0X4D],0X43],0B11010]){} }''','''Class,_,:,_,{,Var,_,,,_R6,:,Int,;,V,(,),{,},$_,(,_3,,,_,,,_,,,W_,,,L9,,,_G_q6vf4e3_,:,Int,;,_,,,_,:,Array,[,Array,[,Array,[,Float,,,0X4D,],,,0X43,],,,0B11010,],),{,},},<EOF>''',101))

    def test_300(self):
        self.assertTrue(TestLexer.test('''Class w{Val K_V,$4:Array [Array [Array [String ,075],6_6],075];}Class _{Constructor (x3Z:Array [Int ,0B1010001];__9,_:_;t__,t0DP,E,_5:Array [Array [Float ,054],0x3A_0_683B];i8_:x){} }Class __{Constructor (_,vK9,_:Array [Array [Int ,0b1_0],0B1010001];u:P3){Break ;Continue ;} }''','''Class,w,{,Val,K_V,,,$4,:,Array,[,Array,[,Array,[,String,,,075,],,,66,],,,075,],;,},Class,_,{,Constructor,(,x3Z,:,Array,[,Int,,,0B1010001,],;,__9,,,_,:,_,;,t__,,,t0DP,,,E,,,_5,:,Array,[,Array,[,Float,,,054,],,,0x3A0683B,],;,i8_,:,x,),{,},},Class,__,{,Constructor,(,_,,,vK9,,,_,:,Array,[,Array,[,Int,,,0b10,],,,0B1010001,],;,u,:,P3,),{,Break,;,Continue,;,},},<EOF>''',101))

    def test_301(self):
        self.assertTrue(TestLexer.test('''Class p2_:r{Constructor (_8_,z,X:Array [Int ,0B10]){} }Class _{Constructor (H_i_1,j:String ;_,_71,l,bh6,_1_,_,P,K_,V:Array [Boolean ,0X2_C]){} }''','''Class,p2_,:,r,{,Constructor,(,_8_,,,z,,,X,:,Array,[,Int,,,0B10,],),{,},},Class,_,{,Constructor,(,H_i_1,,,j,:,String,;,_,,,_71,,,l,,,bh6,,,_1_,,,_,,,P,,,K_,,,V,:,Array,[,Boolean,,,0X2C,],),{,},},<EOF>''',101))

    def test_302(self):
        self.assertTrue(TestLexer.test('''Class _{Destructor (){Continue ;}Constructor (__:_j_p0_01___;fjb:Array [Boolean ,0x8D_7];_:Float ){} }Class VO9{Val $_,t:String ;}''','''Class,_,{,Destructor,(,),{,Continue,;,},Constructor,(,__,:,_j_p0_01___,;,fjb,:,Array,[,Boolean,,,0x8D7,],;,_,:,Float,),{,},},Class,VO9,{,Val,$_,,,t,:,String,;,},<EOF>''',101))

    def test_303(self):
        self.assertTrue(TestLexer.test('''Class g:M{Constructor (){}_p_(){} }Class __:DYD{I(){}_4(){Var A:_R;}Destructor (){}Val $_P:Int ;Destructor (){} }''','''Class,g,:,M,{,Constructor,(,),{,},_p_,(,),{,},},Class,__,:,DYD,{,I,(,),{,},_4,(,),{,Var,A,:,_R,;,},Destructor,(,),{,},Val,$_P,:,Int,;,Destructor,(,),{,},},<EOF>''',101))

    def test_304(self):
        self.assertTrue(TestLexer.test('''Class __5{Var $8:Array [Array [Array [Array [Array [Array [Array [Array [Array [Array [Array [Array [Array [Array [Int ,0B111011],0X2B],44],44],44],44],0b1100010],0132],0X2B],0XBF_B5],0X2B],44],0132],0X2B];Var L,$1_:Array [Array [Boolean ,0b1_101],0B111011];}''','''Class,__5,{,Var,$8,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0B111011,],,,0X2B,],,,44,],,,44,],,,44,],,,44,],,,0b1100010,],,,0132,],,,0X2B,],,,0XBFB5,],,,0X2B,],,,44,],,,0132,],,,0X2B,],;,Var,L,,,$1_,:,Array,[,Array,[,Boolean,,,0b1101,],,,0B111011,],;,},<EOF>''',101))

    def test_305(self):
        self.assertTrue(TestLexer.test('''Class v:_{}Class _{Var $3:Float ;Destructor (){} }Class _{$_(A:Array [Array [Array [Array [String ,88],0b1],0x36],0104];mG:_50;j_:e;k,bE2,___:Array [Array [Array [Array [Float ,4],0X3_8],0b1_0],3];_,c,T:Int ){M::$V._();Var K,_:String ;}Destructor (){}$7(_:Array [Array [Array [Array [String ,0x36],0B11001],12],0x36];_:Boolean ;G3N7,_iGz5:Float ){} }''','''Class,v,:,_,{,},Class,_,{,Var,$3,:,Float,;,Destructor,(,),{,},},Class,_,{,$_,(,A,:,Array,[,Array,[,Array,[,Array,[,String,,,88,],,,0b1,],,,0x36,],,,0104,],;,mG,:,_50,;,j_,:,e,;,k,,,bE2,,,___,:,Array,[,Array,[,Array,[,Array,[,Float,,,4,],,,0X38,],,,0b10,],,,3,],;,_,,,c,,,T,:,Int,),{,M,::,$V,.,_,(,),;,Var,K,,,_,:,String,;,},Destructor,(,),{,},$7,(,_,:,Array,[,Array,[,Array,[,Array,[,String,,,0x36,],,,0B11001,],,,12,],,,0x36,],;,_,:,Boolean,;,G3N7,,,_iGz5,:,Float,),{,},},<EOF>''',101))

    def test_306(self):
        self.assertTrue(TestLexer.test('''Class _:_{Constructor (Hn9:B;R_,_n_:Array [Array [Array [Array [Array [Float ,0b1_0],17],0b1],0X1],0B1001001];e,_,K__,MG5:_Ys_p_0;__C0,G:E){}Destructor (){Break ;} }''','''Class,_,:,_,{,Constructor,(,Hn9,:,B,;,R_,,,_n_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0b10,],,,17,],,,0b1,],,,0X1,],,,0B1001001,],;,e,,,_,,,K__,,,MG5,:,_Ys_p_0,;,__C0,,,G,:,E,),{,},Destructor,(,),{,Break,;,},},<EOF>''',101))

    def test_307(self):
        self.assertTrue(TestLexer.test('''Class F{Val $_,_8,_,$Z_:Float ;Var $s_p_X,B78:String ;}Class L:_{Var _:Array [Float ,78];}Class Y:_6{Var n,$0,$_:Array [Array [Array [Array [Array [Array [Array [Array [Int ,0B1001101],0xB_6],39],0B1001101],0XC],78],0x19],0B1001101];Destructor (){Continue ;}Constructor (_:Boolean ){Continue ;} }''','''Class,F,{,Val,$_,,,_8,,,_,,,$Z_,:,Float,;,Var,$s_p_X,,,B78,:,String,;,},Class,L,:,_,{,Var,_,:,Array,[,Float,,,78,],;,},Class,Y,:,_6,{,Var,n,,,$0,,,$_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0B1001101,],,,0xB6,],,,39,],,,0B1001101,],,,0XC,],,,78,],,,0x19,],,,0B1001101,],;,Destructor,(,),{,Continue,;,},Constructor,(,_,:,Boolean,),{,Continue,;,},},<EOF>''',101))

    def test_308(self):
        self.assertTrue(TestLexer.test('''Class _{}Class Y0:O{Destructor (){} }Class u{Constructor (){}Y(n,I,_:Array [Boolean ,94];_:Float ;_T:Array [Float ,0X58]){} }''','''Class,_,{,},Class,Y0,:,O,{,Destructor,(,),{,},},Class,u,{,Constructor,(,),{,},Y,(,n,,,I,,,_,:,Array,[,Boolean,,,94,],;,_,:,Float,;,_T,:,Array,[,Float,,,0X58,],),{,},},<EOF>''',101))

    def test_309(self):
        self.assertTrue(TestLexer.test('''Class V:H{Constructor (){}Var r,_S,P8_:Array [Boolean ,0x42];}Class _:z{Constructor (H,N7_1t:Array [String ,0107];M8A,g1,_6s5_,d,_1_,k:_;r,_9:C;_T_:H){} }''','''Class,V,:,H,{,Constructor,(,),{,},Var,r,,,_S,,,P8_,:,Array,[,Boolean,,,0x42,],;,},Class,_,:,z,{,Constructor,(,H,,,N7_1t,:,Array,[,String,,,0107,],;,M8A,,,g1,,,_6s5_,,,d,,,_1_,,,k,:,_,;,r,,,_9,:,C,;,_T_,:,H,),{,},},<EOF>''',101))

    def test_310(self):
        self.assertTrue(TestLexer.test('''Class _X:v{}Class _:TM{}Class _{Val b,$_4_,$_7,$_:Array [Array [Boolean ,0X447],2];}Class _:_{Constructor (){Continue ;}$_(l53r:Float ){} }''','''Class,_X,:,v,{,},Class,_,:,TM,{,},Class,_,{,Val,b,,,$_4_,,,$_7,,,$_,:,Array,[,Array,[,Boolean,,,0X447,],,,2,],;,},Class,_,:,_,{,Constructor,(,),{,Continue,;,},$_,(,l53r,:,Float,),{,},},<EOF>''',101))

    def test_311(self):
        self.assertTrue(TestLexer.test('''Class _6R{}Class L_{_(_5,__9:Array [Array [Boolean ,0X7_59_7],0XC5BA8];_,_:Array [Array [Array [Array [Array [String ,2_1_2],051],0x4B],0X32],0b1111]){} }Class _q741:t8{}''','''Class,_6R,{,},Class,L_,{,_,(,_5,,,__9,:,Array,[,Array,[,Boolean,,,0X7597,],,,0XC5BA8,],;,_,,,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,212,],,,051,],,,0x4B,],,,0X32,],,,0b1111,],),{,},},Class,_q741,:,t8,{,},<EOF>''',101))

    def test_312(self):
        self.assertTrue(TestLexer.test('''Class _:z{Val _9m,$1:Array [Array [Array [Array [String ,0B110],2],2],0b1_1_0_0_01];Constructor (h5_s8:Int ;__:Array [String ,0b1001011];o1Uf,__0:Array [Array [Array [Array [Array [Boolean ,0X45],0x3D],87],0b1001011],0b1];n:Float ;_:O;_6,f,M,m__,__bk,M,__6:Array [Boolean ,0141];_,F,O:Int ;zF:String ){Val _:Int ;Val __:Y_;} }''','''Class,_,:,z,{,Val,_9m,,,$1,:,Array,[,Array,[,Array,[,Array,[,String,,,0B110,],,,2,],,,2,],,,0b110001,],;,Constructor,(,h5_s8,:,Int,;,__,:,Array,[,String,,,0b1001011,],;,o1Uf,,,__0,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0X45,],,,0x3D,],,,87,],,,0b1001011,],,,0b1,],;,n,:,Float,;,_,:,O,;,_6,,,f,,,M,,,m__,,,__bk,,,M,,,__6,:,Array,[,Boolean,,,0141,],;,_,,,F,,,O,:,Int,;,zF,:,String,),{,Val,_,:,Int,;,Val,__,:,Y_,;,},},<EOF>''',101))

    def test_313(self):
        self.assertTrue(TestLexer.test('''Class _:_{}Class Y{Constructor (){} }Class L_4l:_1{Constructor (_,R:Array [Boolean ,0x11];_:Int ){}Val X,_,D6_:String ;}''','''Class,_,:,_,{,},Class,Y,{,Constructor,(,),{,},},Class,L_4l,:,_1,{,Constructor,(,_,,,R,:,Array,[,Boolean,,,0x11,],;,_,:,Int,),{,},Val,X,,,_,,,D6_,:,String,;,},<EOF>''',101))

    def test_314(self):
        self.assertTrue(TestLexer.test('''Class j{}Class z_76_{Constructor (_:String ){}Constructor (_4,_,YP__8B,p_0,_,_4:_;_8s,p_6,_:_98C;_8,v89e7T9,kPE,kh,_c,_,y:Array [Array [Boolean ,0b1],0xF_60_C_B]){}Val A45,v:Array [Int ,0b1];Var Y7:String ;}Class dZ:k_{}''','''Class,j,{,},Class,z_76_,{,Constructor,(,_,:,String,),{,},Constructor,(,_4,,,_,,,YP__8B,,,p_0,,,_,,,_4,:,_,;,_8s,,,p_6,,,_,:,_98C,;,_8,,,v89e7T9,,,kPE,,,kh,,,_c,,,_,,,y,:,Array,[,Array,[,Boolean,,,0b1,],,,0xF60CB,],),{,},Val,A45,,,v,:,Array,[,Int,,,0b1,],;,Var,Y7,:,String,;,},Class,dZ,:,k_,{,},<EOF>''',101))

    def test_315(self):
        self.assertTrue(TestLexer.test('''Class _Y2_:__B{}Class oY4:_{Val _,$5:Array [Boolean ,20];}Class _D4_L:oMFd{}Class _:O{}Class _C{$3(){Continue ;} }''','''Class,_Y2_,:,__B,{,},Class,oY4,:,_,{,Val,_,,,$5,:,Array,[,Boolean,,,20,],;,},Class,_D4_L,:,oMFd,{,},Class,_,:,O,{,},Class,_C,{,$3,(,),{,Continue,;,},},<EOF>''',101))

    def test_316(self):
        self.assertTrue(TestLexer.test('''Class _{}Class Hk_DQ:_36_3{_(W_839__Cb,T:Int ;_Q9:Array [Array [String ,06],07];__i__u:Array [Array [Int ,02_5],0X8]){} }''','''Class,_,{,},Class,Hk_DQ,:,_36_3,{,_,(,W_839__Cb,,,T,:,Int,;,_Q9,:,Array,[,Array,[,String,,,06,],,,07,],;,__i__u,:,Array,[,Array,[,Int,,,025,],,,0X8,],),{,},},<EOF>''',101))

    def test_318(self):
        self.assertTrue(TestLexer.test('''Class BU:_9M{$C(){}Val __4nT_,$_,__:Array [Array [Array [Array [Array [String ,61],92],0x21],4],0x89];}Class cF_764:_c_{Val $w:_;}''','''Class,BU,:,_9M,{,$C,(,),{,},Val,__4nT_,,,$_,,,__,:,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,61,],,,92,],,,0x21,],,,4,],,,0x89,],;,},Class,cF_764,:,_c_,{,Val,$w,:,_,;,},<EOF>''',101))

    def test_319(self):
        self.assertTrue(TestLexer.test('''Class V:_{}Class _:_{}Class _S:_{Val $5:Array [Int ,0b1];Constructor (_,_:q;_8:w;D:Int ;_,F:Array [Int ,0B1000001];Vv_:Int ){} }''','''Class,V,:,_,{,},Class,_,:,_,{,},Class,_S,:,_,{,Val,$5,:,Array,[,Int,,,0b1,],;,Constructor,(,_,,,_,:,q,;,_8,:,w,;,D,:,Int,;,_,,,F,:,Array,[,Int,,,0B1000001,],;,Vv_,:,Int,),{,},},<EOF>''',101))

    def test_320(self):
        self.assertTrue(TestLexer.test('''Class _7_{j_(_84:_1;_4,_8,q0n:Array [Array [Float ,0122],0B1];_:Array [Int ,0122];c,_:J){}Var _,$_:Int ;}Class _{}''','''Class,_7_,{,j_,(,_84,:,_1,;,_4,,,_8,,,q0n,:,Array,[,Array,[,Float,,,0122,],,,0B1,],;,_,:,Array,[,Int,,,0122,],;,c,,,_,:,J,),{,},Var,_,,,$_,:,Int,;,},Class,_,{,},<EOF>''',101))

    def test_321(self):
        self.assertTrue(TestLexer.test('''Class w_:m_{_5(_q_:Array [Float ,65_7]){}Constructor (Rhe:Array [String ,0XE];s:U){}Val __,_:Array [Array [Int ,0135],0b10_0_1];Constructor (){} }''','''Class,w_,:,m_,{,_5,(,_q_,:,Array,[,Float,,,657,],),{,},Constructor,(,Rhe,:,Array,[,String,,,0XE,],;,s,:,U,),{,},Val,__,,,_,:,Array,[,Array,[,Int,,,0135,],,,0b1001,],;,Constructor,(,),{,},},<EOF>''',101))

    def test_322(self):
        self.assertTrue(TestLexer.test('''Class hF:_{Constructor (_,__RO6_:Float ;_WV8,T6:Int ;_9:K521;u:__v;_,_,_:S918){}Destructor (){Val _:_;}Constructor (O:Array [Array [Array [Array [Array [Int ,0X32],70],074],0x9],0x5]){} }Class _{}Class a{}Class _{}Class _:__b{}''','''Class,hF,:,_,{,Constructor,(,_,,,__RO6_,:,Float,;,_WV8,,,T6,:,Int,;,_9,:,K521,;,u,:,__v,;,_,,,_,,,_,:,S918,),{,},Destructor,(,),{,Val,_,:,_,;,},Constructor,(,O,:,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0X32,],,,70,],,,074,],,,0x9,],,,0x5,],),{,},},Class,_,{,},Class,a,{,},Class,_,{,},Class,_,:,__b,{,},<EOF>''',101))

    def test_323(self):
        self.assertTrue(TestLexer.test('''Class _v:W{Var V,$E,$39:Array [String ,047];Destructor (){}zx5_Q(_:Int ;Y:_j_;w_0:Array [Array [Array [Array [Boolean ,0X60],03],0b1],047]){} }''','''Class,_v,:,W,{,Var,V,,,$E,,,$39,:,Array,[,String,,,047,],;,Destructor,(,),{,},zx5_Q,(,_,:,Int,;,Y,:,_j_,;,w_0,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,0X60,],,,03,],,,0b1,],,,047,],),{,},},<EOF>''',101))

    def test_324(self):
        self.assertTrue(TestLexer.test('''Class OP:E3{Var $7_,n_,$_:Array [Array [Array [Array [Array [Float ,0B110],073],073],84],0x8];Val $__5:Int ;}Class K:xi05z{Var R4B:Array [Boolean ,03_1];}''','''Class,OP,:,E3,{,Var,$7_,,,n_,,,$_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0B110,],,,073,],,,073,],,,84,],,,0x8,],;,Val,$__5,:,Int,;,},Class,K,:,xi05z,{,Var,R4B,:,Array,[,Boolean,,,031,],;,},<EOF>''',101))

    def test_325(self):
        self.assertTrue(TestLexer.test('''Class _s41ym:bF{Var Z:Array [Array [Array [Array [Array [Array [Array [Array [Array [Array [Float ,13],13],070],0X3F],0xA],0x3F],0b1],654],13],13]=New E()._;Var j7V,$_:Int ;}''','''Class,_s41ym,:,bF,{,Var,Z,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,13,],,,13,],,,070,],,,0X3F,],,,0xA,],,,0x3F,],,,0b1,],,,654,],,,13,],,,13,],=,New,E,(,),.,_,;,Var,j7V,,,$_,:,Int,;,},<EOF>''',101))

    def test_326(self):
        self.assertTrue(TestLexer.test('''Class _G_:_{}Class X__1:n{Var $9,M7:Array [Array [Array [Array [Array [String ,0b10],0XF_5_4_8F],0b11101],0b1],0x17];}Class O:_{}Class Un2{Destructor (){} }''','''Class,_G_,:,_,{,},Class,X__1,:,n,{,Var,$9,,,M7,:,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0b10,],,,0XF548F,],,,0b11101,],,,0b1,],,,0x17,],;,},Class,O,:,_,{,},Class,Un2,{,Destructor,(,),{,},},<EOF>''',101))

    def test_327(self):
        self.assertTrue(TestLexer.test('''Class _{Constructor (){}Val $uG2:m83;}Class __I:NB{Destructor (){} }Class M0_:UQYA{Val _3,$V,x,_0P,v,$4_8_,$8a_,g,$5_,B:Int ;}Class _:P_0{}Class t{}Class _t:_9Y{}''','''Class,_,{,Constructor,(,),{,},Val,$uG2,:,m83,;,},Class,__I,:,NB,{,Destructor,(,),{,},},Class,M0_,:,UQYA,{,Val,_3,,,$V,,,x,,,_0P,,,v,,,$4_8_,,,$8a_,,,g,,,$5_,,,B,:,Int,;,},Class,_,:,P_0,{,},Class,t,{,},Class,_t,:,_9Y,{,},<EOF>''',101))

    def test_328(self):
        self.assertTrue(TestLexer.test('''Class Rj{}Class _S_W:Y{}Class b:C9e{Val X:Array [Array [String ,0X23],0X23];Destructor (){Continue ;}Constructor (_c:String ;_V:Array [Array [String ,0X23],0x14];h1,G,yd,f,Y,l_:Float ;d,_,__,_:u_;g_,_:Float ){} }Class __i:_{}Class __R_4N_{}''','''Class,Rj,{,},Class,_S_W,:,Y,{,},Class,b,:,C9e,{,Val,X,:,Array,[,Array,[,String,,,0X23,],,,0X23,],;,Destructor,(,),{,Continue,;,},Constructor,(,_c,:,String,;,_V,:,Array,[,Array,[,String,,,0X23,],,,0x14,],;,h1,,,G,,,yd,,,f,,,Y,,,l_,:,Float,;,d,,,_,,,__,,,_,:,u_,;,g_,,,_,:,Float,),{,},},Class,__i,:,_,{,},Class,__R_4N_,{,},<EOF>''',101))

    def test_329(self):
        self.assertTrue(TestLexer.test('''Class w:_20{Destructor (){} }Class _R5:O{Var P,$R7B4:C;$N_(){}$_(){}Val $97J,_,F:Array [Array [Int ,0b11101],0X62];Destructor (){} }Class F{}Class _:P8{}''','''Class,w,:,_20,{,Destructor,(,),{,},},Class,_R5,:,O,{,Var,P,,,$R7B4,:,C,;,$N_,(,),{,},$_,(,),{,},Val,$97J,,,_,,,F,:,Array,[,Array,[,Int,,,0b11101,],,,0X62,],;,Destructor,(,),{,},},Class,F,{,},Class,_,:,P8,{,},<EOF>''',101))

    def test_330(self):
        self.assertTrue(TestLexer.test('''Class y:Ho{}Class _M{Constructor (){}Var Bkn_:Array [Boolean ,88];Val $I_,$i27,_J2__m,$_G,$x_:Int ;}Class _:__8{}''','''Class,y,:,Ho,{,},Class,_M,{,Constructor,(,),{,},Var,Bkn_,:,Array,[,Boolean,,,88,],;,Val,$I_,,,$i27,,,_J2__m,,,$_G,,,$x_,:,Int,;,},Class,_,:,__8,{,},<EOF>''',101))

    def test_331(self):
        self.assertTrue(TestLexer.test('''Class I{Destructor (){"'"".D();} }Class s{Val _8,$l_7,$_8,U:Float ;G(){}Constructor (C,_:_;bo,s:Array [Array [Boolean ,01_4],0X62]){}Constructor (W4,_32,__4R,_7,r_7,_,___58,_k:Array [Boolean ,03_7];_Z____d:E){}Val _,p,$__,$Y,_7_r:sl;}Class _D{_M(_,_a79,_Ng1_,m:Float ;_,PL7:Boolean ){} }''','''Class,I,{,Destructor,(,),{,'",.,D,(,),;,},},Class,s,{,Val,_8,,,$l_7,,,$_8,,,U,:,Float,;,G,(,),{,},Constructor,(,C,,,_,:,_,;,bo,,,s,:,Array,[,Array,[,Boolean,,,014,],,,0X62,],),{,},Constructor,(,W4,,,_32,,,__4R,,,_7,,,r_7,,,_,,,___58,,,_k,:,Array,[,Boolean,,,037,],;,_Z____d,:,E,),{,},Val,_,,,p,,,$__,,,$Y,,,_7_r,:,sl,;,},Class,_D,{,_M,(,_,,,_a79,,,_Ng1_,,,m,:,Float,;,_,,,PL7,:,Boolean,),{,},},<EOF>''',101))

    def test_332(self):
        self.assertTrue(TestLexer.test('''Class Y{Constructor (){Break ;}Val $_,$_Ln,_,_92k1_q,$81,h,_,_,$84:String ;}Class LE8_3:U{Destructor (){}Var _t13:nn;}''','''Class,Y,{,Constructor,(,),{,Break,;,},Val,$_,,,$_Ln,,,_,,,_92k1_q,,,$81,,,h,,,_,,,_,,,$84,:,String,;,},Class,LE8_3,:,U,{,Destructor,(,),{,},Var,_t13,:,nn,;,},<EOF>''',101))

    def test_333(self):
        self.assertTrue(TestLexer.test('''Class f_nt_23X:tk5{}Class L{}Class _{}Class SF{}Class Fp{}Class YO{Constructor (G:Boolean ;_x:Int ){L3::$k()._7();} }''','''Class,f_nt_23X,:,tk5,{,},Class,L,{,},Class,_,{,},Class,SF,{,},Class,Fp,{,},Class,YO,{,Constructor,(,G,:,Boolean,;,_x,:,Int,),{,L3,::,$k,(,),.,_7,(,),;,},},<EOF>''',101))

    def test_334(self):
        self.assertTrue(TestLexer.test('''Class _{Constructor (){Break ;}Val $0:Array [Array [Array [Array [Array [Array [Array [Float ,0x42],8_7_78_75_8],0x42],0XD_D],0x8_3],0b110101],052];}''','''Class,_,{,Constructor,(,),{,Break,;,},Val,$0,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0x42,],,,8778758,],,,0x42,],,,0XDD,],,,0x83,],,,0b110101,],,,052,],;,},<EOF>''',101))

    def test_335(self):
        self.assertTrue(TestLexer.test('''Class C{}Class _B{_(_9:Array [Array [String ,0B11],044];V_,H:Array [String ,05];X,O,__:Float ){} }Class WD{Val _5_0_:Boolean ;}''','''Class,C,{,},Class,_B,{,_,(,_9,:,Array,[,Array,[,String,,,0B11,],,,044,],;,V_,,,H,:,Array,[,String,,,05,],;,X,,,O,,,__,:,Float,),{,},},Class,WD,{,Val,_5_0_,:,Boolean,;,},<EOF>''',101))

    def test_336(self):
        self.assertTrue(TestLexer.test('''Class _3{Destructor (){} }Class h:a{Val _n,_,k:Array [Float ,0b101001];Constructor (y9,G:Array [Float ,0B110];_:Array [Boolean ,0B1010100];__Q,_4,O:String ){g_::$f();} }Class g0{}Class h{}Class _{}''','''Class,_3,{,Destructor,(,),{,},},Class,h,:,a,{,Val,_n,,,_,,,k,:,Array,[,Float,,,0b101001,],;,Constructor,(,y9,,,G,:,Array,[,Float,,,0B110,],;,_,:,Array,[,Boolean,,,0B1010100,],;,__Q,,,_4,,,O,:,String,),{,g_,::,$f,(,),;,},},Class,g0,{,},Class,h,{,},Class,_,{,},<EOF>''',101))

    def test_337(self):
        self.assertTrue(TestLexer.test('''Class vd_4_{Constructor (P,_1,CZ5M__,I4:M_;d_,k_:Array [Array [Array [Int ,0xD],0102],66];_u8__d:Array [String ,3];V_5DH:Boolean ;Zb:x;_,iW0,_20X,_70:_){ {Return ;} }Val cf:Array [Float ,0x24];Val _:String ;}''','''Class,vd_4_,{,Constructor,(,P,,,_1,,,CZ5M__,,,I4,:,M_,;,d_,,,k_,:,Array,[,Array,[,Array,[,Int,,,0xD,],,,0102,],,,66,],;,_u8__d,:,Array,[,String,,,3,],;,V_5DH,:,Boolean,;,Zb,:,x,;,_,,,iW0,,,_20X,,,_70,:,_,),{,{,Return,;,},},Val,cf,:,Array,[,Float,,,0x24,],;,Val,_,:,String,;,},<EOF>''',101))

    def test_338(self):
        self.assertTrue(TestLexer.test('''Class _:_Q_8_{}Class _{Constructor (w2,_,_,V1_z,__,_pmE1:_F;_,b,_,q6,G8z,_7:Boolean ;_,_:Array [Array [Int ,021],0B110000]){}Var __,_,_,$__8,$_W1_4_,$_7_,$__,$177:Float ;}''','''Class,_,:,_Q_8_,{,},Class,_,{,Constructor,(,w2,,,_,,,_,,,V1_z,,,__,,,_pmE1,:,_F,;,_,,,b,,,_,,,q6,,,G8z,,,_7,:,Boolean,;,_,,,_,:,Array,[,Array,[,Int,,,021,],,,0B110000,],),{,},Var,__,,,_,,,_,,,$__8,,,$_W1_4_,,,$_7_,,,$__,,,$177,:,Float,;,},<EOF>''',101))

    def test_339(self):
        self.assertTrue(TestLexer.test('''Class _8_{}Class _{}Class J:_2{Constructor (_:__4_;_1:Array [Int ,0x6];D,__:Array [Array [Array [Array [String ,0B101000],0B10],0b10],0x43];___w:Array [Array [Array [Array [Array [Array [Array [Boolean ,0XD],0X2_4BB],0B1],0b1],0B1_0],9],0x43]){Var XMg2,I8k:__;} }''','''Class,_8_,{,},Class,_,{,},Class,J,:,_2,{,Constructor,(,_,:,__4_,;,_1,:,Array,[,Int,,,0x6,],;,D,,,__,:,Array,[,Array,[,Array,[,Array,[,String,,,0B101000,],,,0B10,],,,0b10,],,,0x43,],;,___w,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0XD,],,,0X24BB,],,,0B1,],,,0b1,],,,0B10,],,,9,],,,0x43,],),{,Var,XMg2,,,I8k,:,__,;,},},<EOF>''',101))

    def test_340(self):
        self.assertTrue(TestLexer.test('''Class k:t_{}Class w{__(X,_4_1f,A:Array [Array [Array [Array [Array [Array [Array [Int ,0B1001000],05],0X2],4],0x7],017],0B1]){} }Class _{}Class L:t{}''','''Class,k,:,t_,{,},Class,w,{,__,(,X,,,_4_1f,,,A,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0B1001000,],,,05,],,,0X2,],,,4,],,,0x7,],,,017,],,,0B1,],),{,},},Class,_,{,},Class,L,:,t,{,},<EOF>''',101))

    def test_341(self):
        self.assertTrue(TestLexer.test('''Class V_:_9{Constructor (pW,g_a1r0:Array [Boolean ,0B1];z:Boolean ;__c_:dB;B,de741:Array [Array [Array [String ,5],65],066]){}Val $_:Array [Float ,0x19];}''','''Class,V_,:,_9,{,Constructor,(,pW,,,g_a1r0,:,Array,[,Boolean,,,0B1,],;,z,:,Boolean,;,__c_,:,dB,;,B,,,de741,:,Array,[,Array,[,Array,[,String,,,5,],,,65,],,,066,],),{,},Val,$_,:,Array,[,Float,,,0x19,],;,},<EOF>''',101))

    def test_342(self):
        self.assertTrue(TestLexer.test('''Class _{}Class _9{Constructor (_,l:Array [Array [Array [Array [String ,014],07],014],0B1001011];__e3u:Float ;J,_,_,__:Array [Boolean ,0X51];o,i,_:v3;_f:J;_:String ;_s3:Array [Int ,0b1100];__0t17:Int ;M:Array [Array [String ,7],014];o,_:Int ){} }''','''Class,_,{,},Class,_9,{,Constructor,(,_,,,l,:,Array,[,Array,[,Array,[,Array,[,String,,,014,],,,07,],,,014,],,,0B1001011,],;,__e3u,:,Float,;,J,,,_,,,_,,,__,:,Array,[,Boolean,,,0X51,],;,o,,,i,,,_,:,v3,;,_f,:,J,;,_,:,String,;,_s3,:,Array,[,Int,,,0b1100,],;,__0t17,:,Int,;,M,:,Array,[,Array,[,String,,,7,],,,014,],;,o,,,_,:,Int,),{,},},<EOF>''',101))

    def test_343(self):
        self.assertTrue(TestLexer.test('''Class Q_:Z{}Class _:_{}Class _:_____{LTu(_:Array [Array [Array [Array [String ,0b1],0X5],070],0xE]){}$4t(){} }''','''Class,Q_,:,Z,{,},Class,_,:,_,{,},Class,_,:,_____,{,LTu,(,_,:,Array,[,Array,[,Array,[,Array,[,String,,,0b1,],,,0X5,],,,070,],,,0xE,],),{,},$4t,(,),{,},},<EOF>''',101))

    def test_344(self):
        self.assertTrue(TestLexer.test('''Class __:t{}Class __{Constructor (zfm,B,T,_47_,x:Array [Array [Float ,0b1000100],637];_:Array [Array [Array [Array [String ,06476_3_2],74],0116],07_5];E_,w:Array [String ,7]){} }''','''Class,__,:,t,{,},Class,__,{,Constructor,(,zfm,,,B,,,T,,,_47_,,,x,:,Array,[,Array,[,Float,,,0b1000100,],,,637,],;,_,:,Array,[,Array,[,Array,[,Array,[,String,,,0647632,],,,74,],,,0116,],,,075,],;,E_,,,w,:,Array,[,String,,,7,],),{,},},<EOF>''',101))

    def test_345(self):
        self.assertTrue(TestLexer.test('''Class O_x{}Class q:_{}Class _8:b{R4M(U:Array [Float ,0B10001]){}$S3B(p_6K:Array [Array [Array [Array [Array [Array [Array [Array [Array [Int ,0b1_0_1],05],053],0XA4],03_01],0xC],03],57],0b1];_B_7WLS:e;n:Float ){} }Class e:u{Var F_,_:Float ;}''','''Class,O_x,{,},Class,q,:,_,{,},Class,_8,:,b,{,R4M,(,U,:,Array,[,Float,,,0B10001,],),{,},$S3B,(,p_6K,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0b101,],,,05,],,,053,],,,0XA4,],,,0301,],,,0xC,],,,03,],,,57,],,,0b1,],;,_B_7WLS,:,e,;,n,:,Float,),{,},},Class,e,:,u,{,Var,F_,,,_,:,Float,;,},<EOF>''',101))

    def test_346(self):
        self.assertTrue(TestLexer.test('''Class r:t7pG{Constructor (){}$_(_,_,VT:Boolean ;Zw_:Array [Array [Int ,72],034];q,E,_q,a:Array [Array [Int ,0x7_7_E],0B1]){} }Class y31:_{}''','''Class,r,:,t7pG,{,Constructor,(,),{,},$_,(,_,,,_,,,VT,:,Boolean,;,Zw_,:,Array,[,Array,[,Int,,,72,],,,034,],;,q,,,E,,,_q,,,a,:,Array,[,Array,[,Int,,,0x77E,],,,0B1,],),{,},},Class,y31,:,_,{,},<EOF>''',101))

    def test_347(self):
        self.assertTrue(TestLexer.test('''Class _:_{}Class __42_1{}Class c_{Destructor (){} }Class _q{_z(_:Array [Array [Float ,0X4_8],0x21];_J:_;_,J_0:Boolean ;__S_:Boolean ;S:Boolean ){} }''','''Class,_,:,_,{,},Class,__42_1,{,},Class,c_,{,Destructor,(,),{,},},Class,_q,{,_z,(,_,:,Array,[,Array,[,Float,,,0X48,],,,0x21,],;,_J,:,_,;,_,,,J_0,:,Boolean,;,__S_,:,Boolean,;,S,:,Boolean,),{,},},<EOF>''',101))

    def test_348(self):
        self.assertTrue(TestLexer.test('''Class t{ge_(m,_2,w,C,Q,Q,q,x:_){} }Class _H{Val D:h;Destructor (){}Destructor (){}Var $8,__7:Int ;}Class jj_:_{}Class g7:j{}Class _:_{}''','''Class,t,{,ge_,(,m,,,_2,,,w,,,C,,,Q,,,Q,,,q,,,x,:,_,),{,},},Class,_H,{,Val,D,:,h,;,Destructor,(,),{,},Destructor,(,),{,},Var,$8,,,__7,:,Int,;,},Class,jj_,:,_,{,},Class,g7,:,j,{,},Class,_,:,_,{,},<EOF>''',101))

    def test_349(self):
        self.assertTrue(TestLexer.test('''Class t4__:_{$9(){Return ;} }Class _{}Class _Ag_:_27_0{$3(_,_h,w2,a_G9,_,d,U,_n,Q6:String ;_o,w,A_,x_:_;b_:Boolean ){} }''','''Class,t4__,:,_,{,$9,(,),{,Return,;,},},Class,_,{,},Class,_Ag_,:,_27_0,{,$3,(,_,,,_h,,,w2,,,a_G9,,,_,,,d,,,U,,,_n,,,Q6,:,String,;,_o,,,w,,,A_,,,x_,:,_,;,b_,:,Boolean,),{,},},<EOF>''',101))

    def test_350(self):
        self.assertTrue(TestLexer.test('''Class _s{Var $_,$4:Array [Array [Array [Array [Array [Array [Array [Float ,0b1],04],69],1_4_55_3],73],0X9],4];}Class __:_{}''','''Class,_s,{,Var,$_,,,$4,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0b1,],,,04,],,,69,],,,14553,],,,73,],,,0X9,],,,4,],;,},Class,__,:,_,{,},<EOF>''',101))

    def test_351(self):
        self.assertTrue(TestLexer.test('''Class Bm{}Class l_xOFd2:_8Pq{Constructor (l,_,i3G:String ;_9_j,L_,_,_,____:Array [Array [Array [Int ,33],03],33];K:Float ;_o:Boolean ){} }Class S:_{}''','''Class,Bm,{,},Class,l_xOFd2,:,_8Pq,{,Constructor,(,l,,,_,,,i3G,:,String,;,_9_j,,,L_,,,_,,,_,,,____,:,Array,[,Array,[,Array,[,Int,,,33,],,,03,],,,33,],;,K,:,Float,;,_o,:,Boolean,),{,},},Class,S,:,_,{,},<EOF>''',101))

    def test_352(self):
        self.assertTrue(TestLexer.test('''Class _{$NW_92_PE(u,i:Array [Array [Array [Array [Boolean ,0b1_1],0B1001101],0X4_9],23]){}Val _9B,o:Float ;}Class B{Constructor (___:Array [Array [Float ,0B1001101],060];_V,_5:Array [Boolean ,58];_,_D_V_:Float ){} }''','''Class,_,{,$NW_92_PE,(,u,,,i,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,0b11,],,,0B1001101,],,,0X49,],,,23,],),{,},Val,_9B,,,o,:,Float,;,},Class,B,{,Constructor,(,___,:,Array,[,Array,[,Float,,,0B1001101,],,,060,],;,_V,,,_5,:,Array,[,Boolean,,,58,],;,_,,,_D_V_,:,Float,),{,},},<EOF>''',101))

    def test_353(self):
        self.assertTrue(TestLexer.test('''Class T_:_r2_{Constructor (){}$H(v,_:Int ;__c:_R_){}Var X_:Array [Array [Array [Array [Int ,0xF3_16],59],035],050];Val _,$_:Boolean ;}''','''Class,T_,:,_r2_,{,Constructor,(,),{,},$H,(,v,,,_,:,Int,;,__c,:,_R_,),{,},Var,X_,:,Array,[,Array,[,Array,[,Array,[,Int,,,0xF316,],,,59,],,,035,],,,050,],;,Val,_,,,$_,:,Boolean,;,},<EOF>''',101))

    def test_354(self):
        self.assertTrue(TestLexer.test('''Class _:V{}Class Z:_{Constructor (_:Int ;_c:Array [Array [Array [Boolean ,991_8_2],72],06];gS,e:_;__:Boolean ;i,_a,Y_,_:Int ){}Var $_,$P:Array [Boolean ,05];}''','''Class,_,:,V,{,},Class,Z,:,_,{,Constructor,(,_,:,Int,;,_c,:,Array,[,Array,[,Array,[,Boolean,,,99182,],,,72,],,,06,],;,gS,,,e,:,_,;,__,:,Boolean,;,i,,,_a,,,Y_,,,_,:,Int,),{,},Var,$_,,,$P,:,Array,[,Boolean,,,05,],;,},<EOF>''',101))

    def test_355(self):
        self.assertTrue(TestLexer.test('''Class _{}Class w86:x_m0{Destructor (){Break ;} }Class l_:___{}Class _{Var $_yZ:Array [Array [Array [String ,053_0],04],0x66];}''','''Class,_,{,},Class,w86,:,x_m0,{,Destructor,(,),{,Break,;,},},Class,l_,:,___,{,},Class,_,{,Var,$_yZ,:,Array,[,Array,[,Array,[,String,,,0530,],,,04,],,,0x66,],;,},<EOF>''',101))

    def test_356(self):
        self.assertTrue(TestLexer.test('''Class lU:N{$_0(_h__6:String ;_,_:Array [Array [Array [Boolean ,022],0b1],0X51]){}Constructor (){} }Class _O_:z1{}''','''Class,lU,:,N,{,$_0,(,_h__6,:,String,;,_,,,_,:,Array,[,Array,[,Array,[,Boolean,,,022,],,,0b1,],,,0X51,],),{,},Constructor,(,),{,},},Class,_O_,:,z1,{,},<EOF>''',101))

    def test_357(self):
        self.assertTrue(TestLexer.test('''Class __Z_{}Class _{_3(_T4:Array [Float ,02]){Val _v1,_,d:D_;}Var _7,OAc,$38B,$ft2_:_7_;}Class __{}Class A_8EO:_{}''','''Class,__Z_,{,},Class,_,{,_3,(,_T4,:,Array,[,Float,,,02,],),{,Val,_v1,,,_,,,d,:,D_,;,},Var,_7,,,OAc,,,$38B,,,$ft2_,:,_7_,;,},Class,__,{,},Class,A_8EO,:,_,{,},<EOF>''',101))

    def test_358(self):
        self.assertTrue(TestLexer.test('''Class W_{$__(S,_:Array [Array [Int ,043],70];U,X_:Int ;___6,_:F;x,W__J:Array [Array [Boolean ,70],0X61];_:Array [String ,0x42];_,_:E;F,sb,_2,_,_6:i){} }''','''Class,W_,{,$__,(,S,,,_,:,Array,[,Array,[,Int,,,043,],,,70,],;,U,,,X_,:,Int,;,___6,,,_,:,F,;,x,,,W__J,:,Array,[,Array,[,Boolean,,,70,],,,0X61,],;,_,:,Array,[,String,,,0x42,],;,_,,,_,:,E,;,F,,,sb,,,_2,,,_,,,_6,:,i,),{,},},<EOF>''',101))

    def test_359(self):
        self.assertTrue(TestLexer.test('''Class _:N{Val $6:Array [Array [Boolean ,0X2_7A],0130];}Class p84_m:uN{Constructor (){Continue ;} }Class Q_:__{}Class _v:__4{}Class _{}''','''Class,_,:,N,{,Val,$6,:,Array,[,Array,[,Boolean,,,0X27A,],,,0130,],;,},Class,p84_m,:,uN,{,Constructor,(,),{,Continue,;,},},Class,Q_,:,__,{,},Class,_v,:,__4,{,},Class,_,{,},<EOF>''',101))

    def test_360(self):
        self.assertTrue(TestLexer.test('''Class _9v:DY2{}Class W:__{}Class _:c96{Destructor (){}Var $o7_67_2_,_55_,y,W,$a:Array [Array [Array [String ,040],9],0x23];Constructor (V0,y:Array [String ,64_8];_0bk,pBU7,_,_,x,_,_,_N:m_;c:Array [Float ,0X24];B1,M_:Array [String ,040];x3:Boolean ){}Var _d:Float ;}''','''Class,_9v,:,DY2,{,},Class,W,:,__,{,},Class,_,:,c96,{,Destructor,(,),{,},Var,$o7_67_2_,,,_55_,,,y,,,W,,,$a,:,Array,[,Array,[,Array,[,String,,,040,],,,9,],,,0x23,],;,Constructor,(,V0,,,y,:,Array,[,String,,,648,],;,_0bk,,,pBU7,,,_,,,_,,,x,,,_,,,_,,,_N,:,m_,;,c,:,Array,[,Float,,,0X24,],;,B1,,,M_,:,Array,[,String,,,040,],;,x3,:,Boolean,),{,},Var,_d,:,Float,;,},<EOF>''',101))

    def test_361(self):
        self.assertTrue(TestLexer.test('''Class t:a{$T(){}A(f5,_8C,___:Array [Array [Array [Float ,0X95],0XB],55];_:String ){}Var $V,n:Array [Int ,0B1];}Class _04:_{$T9(_9:Int ;I4x:Boolean ;_7595:_;__,c2D:String ){}Constructor (){} }''','''Class,t,:,a,{,$T,(,),{,},A,(,f5,,,_8C,,,___,:,Array,[,Array,[,Array,[,Float,,,0X95,],,,0XB,],,,55,],;,_,:,String,),{,},Var,$V,,,n,:,Array,[,Int,,,0B1,],;,},Class,_04,:,_,{,$T9,(,_9,:,Int,;,I4x,:,Boolean,;,_7595,:,_,;,__,,,c2D,:,String,),{,},Constructor,(,),{,},},<EOF>''',101))

    def test_362(self):
        self.assertTrue(TestLexer.test('''Class R_:_2{Constructor (){} }Class _{}Class _9P{_V(){Val _9_:Array [Array [Float ,0b1100100],0b1];}Val $_:Int ;Val U_,_,$13:Float ;}Class _{}Class _:_{}''','''Class,R_,:,_2,{,Constructor,(,),{,},},Class,_,{,},Class,_9P,{,_V,(,),{,Val,_9_,:,Array,[,Array,[,Float,,,0b1100100,],,,0b1,],;,},Val,$_,:,Int,;,Val,U_,,,_,,,$13,:,Float,;,},Class,_,{,},Class,_,:,_,{,},<EOF>''',101))

    def test_363(self):
        self.assertTrue(TestLexer.test('''Class _:_{}Class _9BNaM_:B_K{Constructor (e1__e_:_;_:Int ;zt_:Array [Int ,0b111];Gh:Boolean ){}Val $_7G:Boolean ;Destructor (){} }Class _:_3{Constructor (_,L_:String ){} }''','''Class,_,:,_,{,},Class,_9BNaM_,:,B_K,{,Constructor,(,e1__e_,:,_,;,_,:,Int,;,zt_,:,Array,[,Int,,,0b111,],;,Gh,:,Boolean,),{,},Val,$_7G,:,Boolean,;,Destructor,(,),{,},},Class,_,:,_3,{,Constructor,(,_,,,L_,:,String,),{,},},<EOF>''',101))

    def test_364(self):
        self.assertTrue(TestLexer.test('''Class _q{}Class _1:_G{Val $5Z,_,$7_8,$_,_,FB_4a,$8e,$_:A58;}Class l:Q_{_(_:n__9;__jo:Array [Array [Array [Array [String ,0XD_FC],0b1_0_1],0x16],0b1010001];q_:R){Continue ;} }''','''Class,_q,{,},Class,_1,:,_G,{,Val,$5Z,,,_,,,$7_8,,,$_,,,_,,,FB_4a,,,$8e,,,$_,:,A58,;,},Class,l,:,Q_,{,_,(,_,:,n__9,;,__jo,:,Array,[,Array,[,Array,[,Array,[,String,,,0XDFC,],,,0b101,],,,0x16,],,,0b1010001,],;,q_,:,R,),{,Continue,;,},},<EOF>''',101))

    def test_365(self):
        self.assertTrue(TestLexer.test('''Class UI:e_M5{}Class q2{}Class _{Constructor (_Z_:Array [Array [Float ,82],0b1_1_1]){}Destructor (){} }Class _:_l_{}Class D:G{}Class z:_{Constructor (j,_:Boolean ){} }''','''Class,UI,:,e_M5,{,},Class,q2,{,},Class,_,{,Constructor,(,_Z_,:,Array,[,Array,[,Float,,,82,],,,0b111,],),{,},Destructor,(,),{,},},Class,_,:,_l_,{,},Class,D,:,G,{,},Class,z,:,_,{,Constructor,(,j,,,_,:,Boolean,),{,},},<EOF>''',101))

    def test_366(self):
        self.assertTrue(TestLexer.test('''Class _v9{}Class e:_1_{_55do(){}Constructor (__2,G,_,q,n:Array [Array [Float ,0X1_68_9_D7],0X5]){} }Class Z:_{Constructor (){Break ;}Destructor (){Continue ;} }''','''Class,_v9,{,},Class,e,:,_1_,{,_55do,(,),{,},Constructor,(,__2,,,G,,,_,,,q,,,n,:,Array,[,Array,[,Float,,,0X1689D7,],,,0X5,],),{,},},Class,Z,:,_,{,Constructor,(,),{,Break,;,},Destructor,(,),{,Continue,;,},},<EOF>''',101))

    def test_367(self):
        self.assertTrue(TestLexer.test('''Class _:_3_{}Class _8:_{Val $1,$M:Array [Boolean ,046];Constructor (){}Val $0,__:i___;Val $G,$U:Float ;Constructor (F_:Float ;__38,_,_,sF:_;_,_R,_3,j_:_;__:Array [Array [String ,0B1],0B1100]){Var _z__b,w_460:Array [Boolean ,0X7];Continue ;} }''','''Class,_,:,_3_,{,},Class,_8,:,_,{,Val,$1,,,$M,:,Array,[,Boolean,,,046,],;,Constructor,(,),{,},Val,$0,,,__,:,i___,;,Val,$G,,,$U,:,Float,;,Constructor,(,F_,:,Float,;,__38,,,_,,,_,,,sF,:,_,;,_,,,_R,,,_3,,,j_,:,_,;,__,:,Array,[,Array,[,String,,,0B1,],,,0B1100,],),{,Var,_z__b,,,w_460,:,Array,[,Boolean,,,0X7,],;,Continue,;,},},<EOF>''',101))

    def test_368(self):
        self.assertTrue(TestLexer.test('''Class _:Y{}Class p_:__m_l2{Val $8,l1_:I;}Class _:DY{Val __,tj:_;}Class _8____V:F{Val $9c,$J9,$a,$_gt,$_,__3D35,G4_:_;}Class L__{}Class y0_:_{}''','''Class,_,:,Y,{,},Class,p_,:,__m_l2,{,Val,$8,,,l1_,:,I,;,},Class,_,:,DY,{,Val,__,,,tj,:,_,;,},Class,_8____V,:,F,{,Val,$9c,,,$J9,,,$a,,,$_gt,,,$_,,,__3D35,,,G4_,:,_,;,},Class,L__,{,},Class,y0_,:,_,{,},<EOF>''',101))

    def test_369(self):
        self.assertTrue(TestLexer.test('''Class f:_{Destructor (){}Constructor (o,_7:Array [Array [Array [Array [String ,065],0B1_0],03],3];__0_9:Boolean ;_8:Float ;_,c0PH:String ){Break ;{}Return ;} }Class _{}''','''Class,f,:,_,{,Destructor,(,),{,},Constructor,(,o,,,_7,:,Array,[,Array,[,Array,[,Array,[,String,,,065,],,,0B10,],,,03,],,,3,],;,__0_9,:,Boolean,;,_8,:,Float,;,_,,,c0PH,:,String,),{,Break,;,{,},Return,;,},},Class,_,{,},<EOF>''',101))

    def test_370(self):
        self.assertTrue(TestLexer.test('''Class t{Destructor (){}Destructor (){} }Class q{_(i4__g:Float ){}Constructor (_:Array [Array [Array [String ,07],0b1_11],0B1010101]){} }''','''Class,t,{,Destructor,(,),{,},Destructor,(,),{,},},Class,q,{,_,(,i4__g,:,Float,),{,},Constructor,(,_,:,Array,[,Array,[,Array,[,String,,,07,],,,0b111,],,,0B1010101,],),{,},},<EOF>''',101))

    def test_371(self):
        self.assertTrue(TestLexer.test('''Class _:l{Destructor (){} }Class _J{}Class B2_n:O_{}Class ___:w{$_S2Wny(){}Destructor (){}Var x5N_:Array [Float ,62];Val $_:Array [String ,0B1];}''','''Class,_,:,l,{,Destructor,(,),{,},},Class,_J,{,},Class,B2_n,:,O_,{,},Class,___,:,w,{,$_S2Wny,(,),{,},Destructor,(,),{,},Var,x5N_,:,Array,[,Float,,,62,],;,Val,$_,:,Array,[,String,,,0B1,],;,},<EOF>''',101))

    def test_372(self):
        self.assertTrue(TestLexer.test('''Class I{$5_(){z7_h_3::$L();} }Class _:_{Constructor (u:Array [Array [Array [Boolean ,72],4],0B100000];_:_;_l,_mq,_,U6,D_I,l__:Array [Array [Int ,0b10010],0X25]){}Val __I:Array [Boolean ,07];}''','''Class,I,{,$5_,(,),{,z7_h_3,::,$L,(,),;,},},Class,_,:,_,{,Constructor,(,u,:,Array,[,Array,[,Array,[,Boolean,,,72,],,,4,],,,0B100000,],;,_,:,_,;,_l,,,_mq,,,_,,,U6,,,D_I,,,l__,:,Array,[,Array,[,Int,,,0b10010,],,,0X25,],),{,},Val,__I,:,Array,[,Boolean,,,07,],;,},<EOF>''',101))

    def test_373(self):
        self.assertTrue(TestLexer.test('''Class _:O9_{}Class Tq{_(){}$_(_,W_V_W6,E5,_2:_G;_1,___,K_,__,_Qk_r:Boolean ;Mq2,r,_:Array [Int ,63]){} }Class _37_{Constructor (){} }''','''Class,_,:,O9_,{,},Class,Tq,{,_,(,),{,},$_,(,_,,,W_V_W6,,,E5,,,_2,:,_G,;,_1,,,___,,,K_,,,__,,,_Qk_r,:,Boolean,;,Mq2,,,r,,,_,:,Array,[,Int,,,63,],),{,},},Class,_37_,{,Constructor,(,),{,},},<EOF>''',101))

    def test_374(self):
        self.assertTrue(TestLexer.test('''Class Xj{$7(m_,Y,k:Array [Float ,0B1_0];_,B_7:Array [Array [Boolean ,0b10],014];_M,Y,_lI:j_c;__,_:String ){}Destructor (){}Var $49d,$_4_1_8__,__3_,$3:Array [Array [Array [String ,0142],0b10],0XE];}''','''Class,Xj,{,$7,(,m_,,,Y,,,k,:,Array,[,Float,,,0B10,],;,_,,,B_7,:,Array,[,Array,[,Boolean,,,0b10,],,,014,],;,_M,,,Y,,,_lI,:,j_c,;,__,,,_,:,String,),{,},Destructor,(,),{,},Var,$49d,,,$_4_1_8__,,,__3_,,,$3,:,Array,[,Array,[,Array,[,String,,,0142,],,,0b10,],,,0XE,],;,},<EOF>''',101))

    def test_375(self):
        self.assertTrue(TestLexer.test('''Class NT4{J(___T:Array [Array [String ,0X8],0B10_01];_5N:Array [Array [Boolean ,0x6_8_08],0X3A];Q,I:Boolean ){Q0::$_r._2();Break ;{} }}Class G:R8_{}Class o_{}''','''Class,NT4,{,J,(,___T,:,Array,[,Array,[,String,,,0X8,],,,0B1001,],;,_5N,:,Array,[,Array,[,Boolean,,,0x6808,],,,0X3A,],;,Q,,,I,:,Boolean,),{,Q0,::,$_r,.,_2,(,),;,Break,;,{,},},},Class,G,:,R8_,{,},Class,o_,{,},<EOF>''',101))

    def test_376(self):
        self.assertTrue(TestLexer.test('''Class _90:_{$9_(_,_3,_,_:Array [Array [Array [Array [Array [Array [Int ,0B1],3],0X9],9],525],0b1_10];C,Y9:_2){} }''','''Class,_90,:,_,{,$9_,(,_,,,_3,,,_,,,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0B1,],,,3,],,,0X9,],,,9,],,,525,],,,0b110,],;,C,,,Y9,:,_2,),{,},},<EOF>''',101))

    def test_377(self):
        self.assertTrue(TestLexer.test('''Class r:_2{}Class a{Var $P:f72;}Class Y:_{Val _U_:Array [Float ,05_2];Val B:Array [Boolean ,0b1_1];Constructor (_,_D:Array [Array [Boolean ,8],0x35]){} }''','''Class,r,:,_2,{,},Class,a,{,Var,$P,:,f72,;,},Class,Y,:,_,{,Val,_U_,:,Array,[,Float,,,052,],;,Val,B,:,Array,[,Boolean,,,0b11,],;,Constructor,(,_,,,_D,:,Array,[,Array,[,Boolean,,,8,],,,0x35,],),{,},},<EOF>''',101))

    def test_378(self):
        self.assertTrue(TestLexer.test('''Class __{Constructor (){}Var $_s_8:Array [Array [Array [String ,046],0X26],0x1];Constructor (z:v_;_,C:String ;_,_:__){}Var $2,$_X_:Array [Float ,0XF_F_B_8];}Class _:T{}''','''Class,__,{,Constructor,(,),{,},Var,$_s_8,:,Array,[,Array,[,Array,[,String,,,046,],,,0X26,],,,0x1,],;,Constructor,(,z,:,v_,;,_,,,C,:,String,;,_,,,_,:,__,),{,},Var,$2,,,$_X_,:,Array,[,Float,,,0XFFB8,],;,},Class,_,:,T,{,},<EOF>''',101))

    def test_379(self):
        self.assertTrue(TestLexer.test('''Class _I{}Class _2{Constructor (W_9:Float ;_:String ;C0_5,Y,__20,_L,_O:Array [Float ,2];w_,__,_:String ;W2,S2c81,L:Boolean ){} }''','''Class,_I,{,},Class,_2,{,Constructor,(,W_9,:,Float,;,_,:,String,;,C0_5,,,Y,,,__20,,,_L,,,_O,:,Array,[,Float,,,2,],;,w_,,,__,,,_,:,String,;,W2,,,S2c81,,,L,:,Boolean,),{,},},<EOF>''',101))

    def test_380(self):
        self.assertTrue(TestLexer.test('''Class _:d{$d3(){}Constructor (Pd1VDF_9:Array [Array [Array [Int ,0x1],0X4_A],2];q,D7,_7:Array [Array [Boolean ,0XF],0b1001101]){} }''','''Class,_,:,d,{,$d3,(,),{,},Constructor,(,Pd1VDF_9,:,Array,[,Array,[,Array,[,Int,,,0x1,],,,0X4A,],,,2,],;,q,,,D7,,,_7,:,Array,[,Array,[,Boolean,,,0XF,],,,0b1001101,],),{,},},<EOF>''',101))

    def test_381(self):
        self.assertTrue(TestLexer.test('''Class J__{Var $__6ir:F;}Class _2_J:__u__Cz{}Class _{Val u74g,_:Array [Int ,016];}Class bj{Constructor (P_:Array [Float ,031];__:String ){ {} }}''','''Class,J__,{,Var,$__6ir,:,F,;,},Class,_2_J,:,__u__Cz,{,},Class,_,{,Val,u74g,,,_,:,Array,[,Int,,,016,],;,},Class,bj,{,Constructor,(,P_,:,Array,[,Float,,,031,],;,__,:,String,),{,{,},},},<EOF>''',101))

    def test_382(self):
        self.assertTrue(TestLexer.test('''Class A:X{Constructor (_:Array [Array [Array [Float ,07],0110],0X1];m,_,_:String ;x6_5:Array [Array [Boolean ,0110],0110];_5x,_M:_){} }''','''Class,A,:,X,{,Constructor,(,_,:,Array,[,Array,[,Array,[,Float,,,07,],,,0110,],,,0X1,],;,m,,,_,,,_,:,String,;,x6_5,:,Array,[,Array,[,Boolean,,,0110,],,,0110,],;,_5x,,,_M,:,_,),{,},},<EOF>''',101))

    def test_383(self):
        self.assertTrue(TestLexer.test('''Class i:N{}Class C8{Constructor (){Continue ;Break ;}Destructor (){}Var $56,_:Float ;Var c:Array [Int ,0B10_11];}Class jmv{Constructor (){Break ;Var f:Array [Int ,05_4];} }Class _{Var _m_,K,Q,$71c:Int ;Val $9:_;}''','''Class,i,:,N,{,},Class,C8,{,Constructor,(,),{,Continue,;,Break,;,},Destructor,(,),{,},Var,$56,,,_,:,Float,;,Var,c,:,Array,[,Int,,,0B1011,],;,},Class,jmv,{,Constructor,(,),{,Break,;,Var,f,:,Array,[,Int,,,054,],;,},},Class,_,{,Var,_m_,,,K,,,Q,,,$71c,:,Int,;,Val,$9,:,_,;,},<EOF>''',101))

    def test_384(self):
        self.assertTrue(TestLexer.test('''Class _:f_{Val _,$7_:Array [Boolean ,0X17];Destructor (){}Constructor (){Var z,z_36:String ;Break ;Break ;} }Class _:W_{}''','''Class,_,:,f_,{,Val,_,,,$7_,:,Array,[,Boolean,,,0X17,],;,Destructor,(,),{,},Constructor,(,),{,Var,z,,,z_36,:,String,;,Break,;,Break,;,},},Class,_,:,W_,{,},<EOF>''',101))

    def test_385(self):
        self.assertTrue(TestLexer.test('''Class T{Constructor (d4_,__3_,_F:_;_,R_7h_:String ;_:Array [Boolean ,0XA]){} }Class _:_1_w__zy__65__3{}Class _{}''','''Class,T,{,Constructor,(,d4_,,,__3_,,,_F,:,_,;,_,,,R_7h_,:,String,;,_,:,Array,[,Boolean,,,0XA,],),{,},},Class,_,:,_1_w__zy__65__3,{,},Class,_,{,},<EOF>''',101))

    def test_386(self):
        self.assertTrue(TestLexer.test('''Class h{Constructor (_,__V:Array [Float ,0b100011];_0,__17:Array [Array [Array [Int ,0B1_10_1],9_6_9],57_22];n,_6_,_,p,Z3,O:M){} }Class _{}''','''Class,h,{,Constructor,(,_,,,__V,:,Array,[,Float,,,0b100011,],;,_0,,,__17,:,Array,[,Array,[,Array,[,Int,,,0B1101,],,,969,],,,5722,],;,n,,,_6_,,,_,,,p,,,Z3,,,O,:,M,),{,},},Class,_,{,},<EOF>''',101))

    def test_387(self):
        self.assertTrue(TestLexer.test('''Class ___4_{Constructor (__,_NT,_,___:Array [Float ,0x42];_:Array [Array [Array [Int ,0B10],0B1_00],0B1];S:a;_,__L,k3:_;k:Int ){} }''','''Class,___4_,{,Constructor,(,__,,,_NT,,,_,,,___,:,Array,[,Float,,,0x42,],;,_,:,Array,[,Array,[,Array,[,Int,,,0B10,],,,0B100,],,,0B1,],;,S,:,a,;,_,,,__L,,,k3,:,_,;,k,:,Int,),{,},},<EOF>''',101))

    def test_388(self):
        self.assertTrue(TestLexer.test('''Class _{Val $874I_,$7,$_4w,$9m_2:Array [Array [Array [Float ,63],3],0XB];}Class F5__:O{Destructor (){Break ;Return ;}Destructor (){Break ;}Val $l,E:Float ;}Class x81r{A(){}Val _:Array [Array [Int ,0x4B],0X60]=!l::$D/-T0u::$_;}Class E__{Constructor (_:Boolean ;_,N__,IyDA:Int ){Break ;}Val __w4_:_=R::$__l();}Class F_ca{Var $_:Array [String ,5_2];}''','''Class,_,{,Val,$874I_,,,$7,,,$_4w,,,$9m_2,:,Array,[,Array,[,Array,[,Float,,,63,],,,3,],,,0XB,],;,},Class,F5__,:,O,{,Destructor,(,),{,Break,;,Return,;,},Destructor,(,),{,Break,;,},Val,$l,,,E,:,Float,;,},Class,x81r,{,A,(,),{,},Val,_,:,Array,[,Array,[,Int,,,0x4B,],,,0X60,],=,!,l,::,$D,/,-,T0u,::,$_,;,},Class,E__,{,Constructor,(,_,:,Boolean,;,_,,,N__,,,IyDA,:,Int,),{,Break,;,},Val,__w4_,:,_,=,R,::,$__l,(,),;,},Class,F_ca,{,Var,$_,:,Array,[,String,,,52,],;,},<EOF>''',101))

    def test_389(self):
        self.assertTrue(TestLexer.test('''Class H:h{}Class H3__e:J_{Constructor (){} }Class _:_u9a{s(P,Xu5:J){Return ;}Val _:Array [Array [Int ,07_607_1],42];}Class z:X{}Class _{}''','''Class,H,:,h,{,},Class,H3__e,:,J_,{,Constructor,(,),{,},},Class,_,:,_u9a,{,s,(,P,,,Xu5,:,J,),{,Return,;,},Val,_,:,Array,[,Array,[,Int,,,076071,],,,42,],;,},Class,z,:,X,{,},Class,_,{,},<EOF>''',101))

    def test_390(self):
        self.assertTrue(TestLexer.test('''Class x{Var o,$b8K:String ;Constructor (j4_6:Array [Array [Boolean ,82],0b10001];_1,gJ,O6,_,icl,_:String ;W:Boolean ;_:r__){} }Class _:___{}''','''Class,x,{,Var,o,,,$b8K,:,String,;,Constructor,(,j4_6,:,Array,[,Array,[,Boolean,,,82,],,,0b10001,],;,_1,,,gJ,,,O6,,,_,,,icl,,,_,:,String,;,W,:,Boolean,;,_,:,r__,),{,},},Class,_,:,___,{,},<EOF>''',101))

    def test_391(self):
        self.assertTrue(TestLexer.test('''Class _pk_0v:_{}Class l:Y{Constructor (_:_){} }Class kr{}Class _Lf:R_{Val $_:Array [Array [Boolean ,0X63],0X63];}Class _80{_(){} }''','''Class,_pk_0v,:,_,{,},Class,l,:,Y,{,Constructor,(,_,:,_,),{,},},Class,kr,{,},Class,_Lf,:,R_,{,Val,$_,:,Array,[,Array,[,Boolean,,,0X63,],,,0X63,],;,},Class,_80,{,_,(,),{,},},<EOF>''',101))

    def test_392(self):
        self.assertTrue(TestLexer.test('''Class j:E_90u_{}Class K:_19f6{}Class _:T{$D_(n:Array [Int ,0X23];__:_;Om_:Int ;__1_:_C;__:Array [Array [Array [Array [Boolean ,0x18],034],051_4],034];_B,_:Int ;__:i){} }''','''Class,j,:,E_90u_,{,},Class,K,:,_19f6,{,},Class,_,:,T,{,$D_,(,n,:,Array,[,Int,,,0X23,],;,__,:,_,;,Om_,:,Int,;,__1_,:,_C,;,__,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,0x18,],,,034,],,,0514,],,,034,],;,_B,,,_,:,Int,;,__,:,i,),{,},},<EOF>''',101))

    def test_393(self):
        self.assertTrue(TestLexer.test('''Class _:c_{Constructor (__2_:Float ;_r,_:Array [Boolean ,03_5]){Return ;} }Class _:_9U_{Constructor (k27:Array [Array [Array [String ,0xE],21],6]){} }Class _:_{}''','''Class,_,:,c_,{,Constructor,(,__2_,:,Float,;,_r,,,_,:,Array,[,Boolean,,,035,],),{,Return,;,},},Class,_,:,_9U_,{,Constructor,(,k27,:,Array,[,Array,[,Array,[,String,,,0xE,],,,21,],,,6,],),{,},},Class,_,:,_,{,},<EOF>''',101))

    def test_394(self):
        self.assertTrue(TestLexer.test('''Class _{Val _,$3__,d3:Int ;_(){Break ;Break ;}$0(_:__;_,z:_q8_;P:u__7){Return ;}o(t2:Array [Float ,07]){}Val $c,$R_,D0h__1_o:String ;}Class _J83:s_{}''','''Class,_,{,Val,_,,,$3__,,,d3,:,Int,;,_,(,),{,Break,;,Break,;,},$0,(,_,:,__,;,_,,,z,:,_q8_,;,P,:,u__7,),{,Return,;,},o,(,t2,:,Array,[,Float,,,07,],),{,},Val,$c,,,$R_,,,D0h__1_o,:,String,;,},Class,_J83,:,s_,{,},<EOF>''',101))

    def test_395(self):
        self.assertTrue(TestLexer.test('''Class _:_{Var $3l5:_4A;Val $L_n_:b;Constructor (_,_,t:Int ){}Val $5_7__4_,$_,$_,$A_h,_o,$x8:T2;Val _d_g__,_,$8:A5;}''','''Class,_,:,_,{,Var,$3l5,:,_4A,;,Val,$L_n_,:,b,;,Constructor,(,_,,,_,,,t,:,Int,),{,},Val,$5_7__4_,,,$_,,,$_,,,$A_h,,,_o,,,$x8,:,T2,;,Val,_d_g__,,,_,,,$8,:,A5,;,},<EOF>''',101))

    def test_396(self):
        self.assertTrue(TestLexer.test('''Class x:_{$6(j,t8:Array [Int ,0X3A];_,W0_,Nhf,_,_:Array [Array [Float ,0b101010],067]){Return ;Break ;{} }Val $__:_;_(__5Ft:Int ){Return ;} }Class x{}Class hH:_{Destructor (){ {} }}Class _{}Class a{M(){} }Class __{Val M_34_66:_;Val $__,_,$35p,$1,$8_:Array [Float ,5];Constructor (bp:f;Mb8,_re9p,_:String ;B:Array [Boolean ,0B10_0];I45,x:y;_kF_jn6_8_,Q:Array [Int ,46]){Return ;Break ;} }''','''Class,x,:,_,{,$6,(,j,,,t8,:,Array,[,Int,,,0X3A,],;,_,,,W0_,,,Nhf,,,_,,,_,:,Array,[,Array,[,Float,,,0b101010,],,,067,],),{,Return,;,Break,;,{,},},Val,$__,:,_,;,_,(,__5Ft,:,Int,),{,Return,;,},},Class,x,{,},Class,hH,:,_,{,Destructor,(,),{,{,},},},Class,_,{,},Class,a,{,M,(,),{,},},Class,__,{,Val,M_34_66,:,_,;,Val,$__,,,_,,,$35p,,,$1,,,$8_,:,Array,[,Float,,,5,],;,Constructor,(,bp,:,f,;,Mb8,,,_re9p,,,_,:,String,;,B,:,Array,[,Boolean,,,0B100,],;,I45,,,x,:,y,;,_kF_jn6_8_,,,Q,:,Array,[,Int,,,46,],),{,Return,;,Break,;,},},<EOF>''',101))

    def test_397(self):
        self.assertTrue(TestLexer.test('''Class _{Constructor (__,__:Array [Array [Float ,0100],4];e:Array [Array [Array [Boolean ,7_571_9_0],0X5A],0b1_1]){}Destructor (){} }Class G_{}Class O2:i{}''','''Class,_,{,Constructor,(,__,,,__,:,Array,[,Array,[,Float,,,0100,],,,4,],;,e,:,Array,[,Array,[,Array,[,Boolean,,,757190,],,,0X5A,],,,0b11,],),{,},Destructor,(,),{,},},Class,G_,{,},Class,O2,:,i,{,},<EOF>''',101))

    def test_398(self):
        self.assertTrue(TestLexer.test('''Class j{Destructor (){} }Class _:_2{Destructor (){}Destructor (){}Var G_,_,o:Boolean ;}Class _:_G{Constructor (_8_,U3,EXu,_n6,ew,__,_43:Boolean ;_8,_,_:P){} }Class __{}''','''Class,j,{,Destructor,(,),{,},},Class,_,:,_2,{,Destructor,(,),{,},Destructor,(,),{,},Var,G_,,,_,,,o,:,Boolean,;,},Class,_,:,_G,{,Constructor,(,_8_,,,U3,,,EXu,,,_n6,,,ew,,,__,,,_43,:,Boolean,;,_8,,,_,,,_,:,P,),{,},},Class,__,{,},<EOF>''',101))

    def test_399(self):
        self.assertTrue(TestLexer.test('''Class Y:_{Val _7_,_G_:Array [Array [Array [Array [Array [Array [Array [Array [Boolean ,8],0X27],02_2],062],062],0XC_0_6],79],04_5700_42];Var _,h:Float ;Destructor (){ {} }}Class m{}Class m{}Class Z{}Class _:_{}''','''Class,Y,:,_,{,Val,_7_,,,_G_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,8,],,,0X27,],,,022,],,,062,],,,062,],,,0XC06,],,,79,],,,04570042,],;,Var,_,,,h,:,Float,;,Destructor,(,),{,{,},},},Class,m,{,},Class,m,{,},Class,Z,{,},Class,_,:,_,{,},<EOF>''',101))

    def test_400(self):
        self.assertTrue(TestLexer.test('''Class b:_{}Class B7:p{}Class _{}Class _E{Var X8:Array [Array [Int ,0B1],72];Val _,$_:Array [Array [Boolean ,060],060];Destructor (){} }Class U{}''','''Class,b,:,_,{,},Class,B7,:,p,{,},Class,_,{,},Class,_E,{,Var,X8,:,Array,[,Array,[,Int,,,0B1,],,,72,],;,Val,_,,,$_,:,Array,[,Array,[,Boolean,,,060,],,,060,],;,Destructor,(,),{,},},Class,U,{,},<EOF>''',101))

    def test_401(self):
        self.assertTrue(TestLexer.test('''Class U:_c{n(_:Boolean ;q,w,__:Array [Float ,07_6_6_11];_:_z___;_:Array [Array [Boolean ,072],9];H:I_M){}$L_(){} }''','''Class,U,:,_c,{,n,(,_,:,Boolean,;,q,,,w,,,__,:,Array,[,Float,,,076611,],;,_,:,_z___,;,_,:,Array,[,Array,[,Boolean,,,072,],,,9,],;,H,:,I_M,),{,},$L_,(,),{,},},<EOF>''',101))

    def test_402(self):
        self.assertTrue(TestLexer.test('''Class h6Y_{Constructor (_,n,t,__,Wy_:Array [Int ,4_68_9]){Val x,_,_D:Boolean ;}Var $B_u_82,o:Array [Array [Float ,59_3_1],0x5F_B7];Var $2_2,$m_,$_5A:q4y;}Class __977:X{}Class _{Val $__eDX:_r74;}''','''Class,h6Y_,{,Constructor,(,_,,,n,,,t,,,__,,,Wy_,:,Array,[,Int,,,4689,],),{,Val,x,,,_,,,_D,:,Boolean,;,},Var,$B_u_82,,,o,:,Array,[,Array,[,Float,,,5931,],,,0x5FB7,],;,Var,$2_2,,,$m_,,,$_5A,:,q4y,;,},Class,__977,:,X,{,},Class,_,{,Val,$__eDX,:,_r74,;,},<EOF>''',101))

    def test_403(self):
        self.assertTrue(TestLexer.test('''Class o1Y{$l_(__gf:Array [Array [Array [Array [Boolean ,0b1001001],05],033],0X14];_,_:Int ;_,p__E,_:_;_:c3f4Z32J02){} }''','''Class,o1Y,{,$l_,(,__gf,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,0b1001001,],,,05,],,,033,],,,0X14,],;,_,,,_,:,Int,;,_,,,p__E,,,_,:,_,;,_,:,c3f4Z32J02,),{,},},<EOF>''',101))

    def test_404(self):
        self.assertTrue(TestLexer.test('''Class dl:e{Constructor (){ {} }Var _G,$_C3:Array [Array [Boolean ,26],0X52];}Class __{}Class _K{Destructor (){Continue ;h::$H9.a();} }Class UX:jI{Destructor (){} }''','''Class,dl,:,e,{,Constructor,(,),{,{,},},Var,_G,,,$_C3,:,Array,[,Array,[,Boolean,,,26,],,,0X52,],;,},Class,__,{,},Class,_K,{,Destructor,(,),{,Continue,;,h,::,$H9,.,a,(,),;,},},Class,UX,:,jI,{,Destructor,(,),{,},},<EOF>''',101))

    def test_405(self):
        self.assertTrue(TestLexer.test('''Class v:XK__{Val x:Float =!!!!!-New _()._()||-Null ;Constructor (_6_J:Array [Array [Array [Array [Int ,03_4_2_414],025],031],0X56];m:Array [String ,011];K0N,H,XV__F,w_:_A7_){} }''','''Class,v,:,XK__,{,Val,x,:,Float,=,!,!,!,!,!,-,New,_,(,),.,_,(,),||,-,Null,;,Constructor,(,_6_J,:,Array,[,Array,[,Array,[,Array,[,Int,,,0342414,],,,025,],,,031,],,,0X56,],;,m,:,Array,[,String,,,011,],;,K0N,,,H,,,XV__F,,,w_,:,_A7_,),{,},},<EOF>''',101))

    def test_406(self):
        self.assertTrue(TestLexer.test('''Class W{}Class u_0{X61(N,B_H,_w5,_J:String ;_O5,u_y6_,_,_,_v_,h:U4_B_;x:String ;_:u3;t2Q:Array [Int ,0b1011101]){} }''','''Class,W,{,},Class,u_0,{,X61,(,N,,,B_H,,,_w5,,,_J,:,String,;,_O5,,,u_y6_,,,_,,,_,,,_v_,,,h,:,U4_B_,;,x,:,String,;,_,:,u3,;,t2Q,:,Array,[,Int,,,0b1011101,],),{,},},<EOF>''',101))

    def test_407(self):
        self.assertTrue(TestLexer.test('''Class _:_k{Constructor (D_,_:Array [Array [Array [Array [String ,0b101001],0B1],0X16],0xE50_54];_5,_4_:Array [Array [Array [String ,91],0B1_0],0X16]){}Destructor (){} }Class _1{Constructor (){} }Class _a_q__{}''','''Class,_,:,_k,{,Constructor,(,D_,,,_,:,Array,[,Array,[,Array,[,Array,[,String,,,0b101001,],,,0B1,],,,0X16,],,,0xE5054,],;,_5,,,_4_,:,Array,[,Array,[,Array,[,String,,,91,],,,0B10,],,,0X16,],),{,},Destructor,(,),{,},},Class,_1,{,Constructor,(,),{,},},Class,_a_q__,{,},<EOF>''',101))

    def test_408(self):
        self.assertTrue(TestLexer.test('''Class __{Destructor (){Val e5,ak_:Array [Array [Array [Array [Int ,04],74],0B100000],0b11];} }Class Q6M:__1{}Class _56{}''','''Class,__,{,Destructor,(,),{,Val,e5,,,ak_,:,Array,[,Array,[,Array,[,Array,[,Int,,,04,],,,74,],,,0B100000,],,,0b11,],;,},},Class,Q6M,:,__1,{,},Class,_56,{,},<EOF>''',101))

    def test_409(self):
        self.assertTrue(TestLexer.test('''Class m9_:_{}Class UQTP4:M{}Class __{Destructor (){Continue ;}$B(bx,W_Tw92,mN2:Array [Array [Array [Array [Array [Array [Int ,06_64_2],0b1_1_00_01],73],0x2E],8],0B1100]){}$_(q:Float ){} }''','''Class,m9_,:,_,{,},Class,UQTP4,:,M,{,},Class,__,{,Destructor,(,),{,Continue,;,},$B,(,bx,,,W_Tw92,,,mN2,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,06642,],,,0b110001,],,,73,],,,0x2E,],,,8,],,,0B1100,],),{,},$_,(,q,:,Float,),{,},},<EOF>''',101))

    def test_410(self):
        self.assertTrue(TestLexer.test('''Class u{$0E0(){Continue ;}l(){_::$4();}Var _:n6QD;}Class j{}Class n:I{Var M1,a8,u_6:f;Destructor (){}Val O___,_,$_25,wo,Nq:_9T;Destructor (){}Val g:Array [Array [Array [Array [Array [Array [Array [Array [String ,225],0B1000010],04],04],8],0101],15],9];}''','''Class,u,{,$0E0,(,),{,Continue,;,},l,(,),{,_,::,$4,(,),;,},Var,_,:,n6QD,;,},Class,j,{,},Class,n,:,I,{,Var,M1,,,a8,,,u_6,:,f,;,Destructor,(,),{,},Val,O___,,,_,,,$_25,,,wo,,,Nq,:,_9T,;,Destructor,(,),{,},Val,g,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,225,],,,0B1000010,],,,04,],,,04,],,,8,],,,0101,],,,15,],,,9,],;,},<EOF>''',101))

    def test_411(self):
        self.assertTrue(TestLexer.test('''Class e4:L{}Class _{}Class Z_{Val _,$_:Array [Float ,0B110110];Var $nhfS:Array [Array [Boolean ,0B110110],0x20];Val R,BC:Boolean ;}Class _CS{Var __:_;}''','''Class,e4,:,L,{,},Class,_,{,},Class,Z_,{,Val,_,,,$_,:,Array,[,Float,,,0B110110,],;,Var,$nhfS,:,Array,[,Array,[,Boolean,,,0B110110,],,,0x20,],;,Val,R,,,BC,:,Boolean,;,},Class,_CS,{,Var,__,:,_,;,},<EOF>''',101))

    def test_412(self):
        self.assertTrue(TestLexer.test('''Class __:J0{Var $X,$_:M_;}Class _3:mom{}Class U:S{Constructor (_,_:p6;U,_:Array [Array [Int ,0x4],04]){} }Class _:U_QZ__{}''','''Class,__,:,J0,{,Var,$X,,,$_,:,M_,;,},Class,_3,:,mom,{,},Class,U,:,S,{,Constructor,(,_,,,_,:,p6,;,U,,,_,:,Array,[,Array,[,Int,,,0x4,],,,04,],),{,},},Class,_,:,U_QZ__,{,},<EOF>''',101))

    def test_413(self):
        self.assertTrue(TestLexer.test('''Class _:h{A50(){} }Class _:_S_{}Class vp9{Val $_:eL;Destructor (){Break ;Val _FMRg,_:Array [Array [Float ,035],0b1];} }Class _:__0e4a{}Class C{}''','''Class,_,:,h,{,A50,(,),{,},},Class,_,:,_S_,{,},Class,vp9,{,Val,$_,:,eL,;,Destructor,(,),{,Break,;,Val,_FMRg,,,_,:,Array,[,Array,[,Float,,,035,],,,0b1,],;,},},Class,_,:,__0e4a,{,},Class,C,{,},<EOF>''',101))

    def test_414(self):
        self.assertTrue(TestLexer.test('''Class _:S{Constructor (IM_,h_:Float ;K,_,f1__,_L:Array [Array [Boolean ,0b1000000],03_5];r:_;V,t,n:Array [Array [Int ,06],0X23]){} }''','''Class,_,:,S,{,Constructor,(,IM_,,,h_,:,Float,;,K,,,_,,,f1__,,,_L,:,Array,[,Array,[,Boolean,,,0b1000000,],,,035,],;,r,:,_,;,V,,,t,,,n,:,Array,[,Array,[,Int,,,06,],,,0X23,],),{,},},<EOF>''',101))

    def test_415(self):
        self.assertTrue(TestLexer.test('''Class _:_{}Class C:_{$35_g8W(_:Array [Array [String ,0X57],67]){}Var t_C,$_W:o;Constructor (_,_0,_:I__){}Val k:Float ;}''','''Class,_,:,_,{,},Class,C,:,_,{,$35_g8W,(,_,:,Array,[,Array,[,String,,,0X57,],,,67,],),{,},Var,t_C,,,$_W,:,o,;,Constructor,(,_,,,_0,,,_,:,I__,),{,},Val,k,:,Float,;,},<EOF>''',101))

    def test_416(self):
        self.assertTrue(TestLexer.test('''Class __Z:W{}Class _:__9{Destructor (){}Var $K,$Z,$_5HC3,$6:Array [Int ,9];}Class g{Constructor (){}Val J_:T;}Class va_7{_Qj(_,p26,_:Boolean ){ {{} }_Q_::$6__5h();Break ;} }''','''Class,__Z,:,W,{,},Class,_,:,__9,{,Destructor,(,),{,},Var,$K,,,$Z,,,$_5HC3,,,$6,:,Array,[,Int,,,9,],;,},Class,g,{,Constructor,(,),{,},Val,J_,:,T,;,},Class,va_7,{,_Qj,(,_,,,p26,,,_,:,Boolean,),{,{,{,},},_Q_,::,$6__5h,(,),;,Break,;,},},<EOF>''',101))

    def test_417(self):
        self.assertTrue(TestLexer.test('''Class Cw3{}Class _1:__5{}Class _{Constructor (o_:String ;x:_vFX;a,_:Array [Array [Array [String ,30],0b10110],0x39]){} }''','''Class,Cw3,{,},Class,_1,:,__5,{,},Class,_,{,Constructor,(,o_,:,String,;,x,:,_vFX,;,a,,,_,:,Array,[,Array,[,Array,[,String,,,30,],,,0b10110,],,,0x39,],),{,},},<EOF>''',101))

    def test_418(self):
        self.assertTrue(TestLexer.test('''Class __{_(_:Float ;_:Array [Float ,60];__:Array [Int ,0B1001000];CX,GRY_,_m_:Array [Array [Int ,0B1001000],046];D_:String ){} }''','''Class,__,{,_,(,_,:,Float,;,_,:,Array,[,Float,,,60,],;,__,:,Array,[,Int,,,0B1001000,],;,CX,,,GRY_,,,_m_,:,Array,[,Array,[,Int,,,0B1001000,],,,046,],;,D_,:,String,),{,},},<EOF>''',101))

    def test_419(self):
        self.assertTrue(TestLexer.test('''Class J{_(){Var _,_:x;Return ;} }Class K:m{Destructor (){}Val $56:_C;Var _8,$R8_,$_,_,__0_,$5C_1v:String ;Constructor (){ {}Val _:Int ;} }''','''Class,J,{,_,(,),{,Var,_,,,_,:,x,;,Return,;,},},Class,K,:,m,{,Destructor,(,),{,},Val,$56,:,_C,;,Var,_8,,,$R8_,,,$_,,,_,,,__0_,,,$5C_1v,:,String,;,Constructor,(,),{,{,},Val,_,:,Int,;,},},<EOF>''',101))

    def test_420(self):
        self.assertTrue(TestLexer.test('''Class B:v{Val h_z_y_:Float ;}Class _1_{}Class _9{Destructor (){Var _:D;}Destructor (){}Var $L,F_1PR,t:Boolean ;}''','''Class,B,:,v,{,Val,h_z_y_,:,Float,;,},Class,_1_,{,},Class,_9,{,Destructor,(,),{,Var,_,:,D,;,},Destructor,(,),{,},Var,$L,,,F_1PR,,,t,:,Boolean,;,},<EOF>''',101))

    def test_421(self):
        self.assertTrue(TestLexer.test('''Class _:L{Constructor (){ {} }$7(i0F:Array [String ,0x69];_4p,_7_,Wy_,i_,_:Array [Float ,02]){Return ;Val Z__5__v:I;{} }}''','''Class,_,:,L,{,Constructor,(,),{,{,},},$7,(,i0F,:,Array,[,String,,,0x69,],;,_4p,,,_7_,,,Wy_,,,i_,,,_,:,Array,[,Float,,,02,],),{,Return,;,Val,Z__5__v,:,I,;,{,},},},<EOF>''',101))

    def test_422(self):
        self.assertTrue(TestLexer.test('''Class ___:oI{Constructor (){}Val $N7Q070:Array [Float ,0B1000111];fg_(_,A,p,_,l,E:_;R__,_:Int ;A,_,_:Float ;x:Array [Int ,94];C9:Array [Array [Array [Array [Int ,0X64],94],0B11_1],05_25_3];_eec2_1:String ){}_q52m(HQ,R8f:Float ;MS_,s,_7,O_:_){Continue ;o9::$_(!!!--T::$_A);Continue ;}Val p,$53_7_p:_s_;}Class S{}Class S85_7R{}''','''Class,___,:,oI,{,Constructor,(,),{,},Val,$N7Q070,:,Array,[,Float,,,0B1000111,],;,fg_,(,_,,,A,,,p,,,_,,,l,,,E,:,_,;,R__,,,_,:,Int,;,A,,,_,,,_,:,Float,;,x,:,Array,[,Int,,,94,],;,C9,:,Array,[,Array,[,Array,[,Array,[,Int,,,0X64,],,,94,],,,0B111,],,,05253,],;,_eec2_1,:,String,),{,},_q52m,(,HQ,,,R8f,:,Float,;,MS_,,,s,,,_7,,,O_,:,_,),{,Continue,;,o9,::,$_,(,!,!,!,-,-,T,::,$_A,),;,Continue,;,},Val,p,,,$53_7_p,:,_s_,;,},Class,S,{,},Class,S85_7R,{,},<EOF>''',101))

    def test_423(self):
        self.assertTrue(TestLexer.test('''Class sb_:u{Val X,_t:W_;}Class lL_{Constructor (C,_,_6_,_,i38,_0OK3,_,_:_7t){G_O__::$4L();} }Class _:_{Var $c2t2,ZY,$_,_2_,$1:_ya;Val _4,$_,$lw9_5:V;}''','''Class,sb_,:,u,{,Val,X,,,_t,:,W_,;,},Class,lL_,{,Constructor,(,C,,,_,,,_6_,,,_,,,i38,,,_0OK3,,,_,,,_,:,_7t,),{,G_O__,::,$4L,(,),;,},},Class,_,:,_,{,Var,$c2t2,,,ZY,,,$_,,,_2_,,,$1,:,_ya,;,Val,_4,,,$_,,,$lw9_5,:,V,;,},<EOF>''',101))

    def test_424(self):
        self.assertTrue(TestLexer.test('''Class _o{}Class P{Var __:Boolean ;Val KP,_:Array [Int ,0X4B];Var S:Array [Array [Array [Float ,0x44],071],6_0_2_7];}Class _g_{}''','''Class,_o,{,},Class,P,{,Var,__,:,Boolean,;,Val,KP,,,_,:,Array,[,Int,,,0X4B,],;,Var,S,:,Array,[,Array,[,Array,[,Float,,,0x44,],,,071,],,,6027,],;,},Class,_g_,{,},<EOF>''',101))

    def test_425(self):
        self.assertTrue(TestLexer.test('''Class _g3{Val b:String ;}Class _:_{__(Tg:Boolean ;W0,T,_,_,_,m,_,_p,p_1:String ;o,__3u_,h,p:Float ){ {{} }Val g,m7Z,_:Array [Boolean ,54];} }''','''Class,_g3,{,Val,b,:,String,;,},Class,_,:,_,{,__,(,Tg,:,Boolean,;,W0,,,T,,,_,,,_,,,_,,,m,,,_,,,_p,,,p_1,:,String,;,o,,,__3u_,,,h,,,p,:,Float,),{,{,{,},},Val,g,,,m7Z,,,_,:,Array,[,Boolean,,,54,],;,},},<EOF>''',101))

    def test_426(self):
        self.assertTrue(TestLexer.test('''Class _j:_41r{Constructor (_,__:Float ;_3,_G_:Array [Array [Array [Array [Float ,73],7],0B10],0x8];o:Array [Array [Int ,05],0115]){} }Class Mh{}''','''Class,_j,:,_41r,{,Constructor,(,_,,,__,:,Float,;,_3,,,_G_,:,Array,[,Array,[,Array,[,Array,[,Float,,,73,],,,7,],,,0B10,],,,0x8,],;,o,:,Array,[,Array,[,Int,,,05,],,,0115,],),{,},},Class,Mh,{,},<EOF>''',101))

    def test_427(self):
        self.assertTrue(TestLexer.test('''Class s{}Class s:c{Val _2:_6_;}Class s{Var $_:Array [Array [Array [Array [Boolean ,0x10],0B10],04],94];Var f_7_W,$_:i;}''','''Class,s,{,},Class,s,:,c,{,Val,_2,:,_6_,;,},Class,s,{,Var,$_,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,0x10,],,,0B10,],,,04,],,,94,],;,Var,f_7_W,,,$_,:,i,;,},<EOF>''',101))

    def test_428(self):
        self.assertTrue(TestLexer.test('''Class _:_{_8(){}Constructor (_,_b3_:Int ;_:Array [Array [Array [Float ,0b1],0B1],062];_,_,Gb:String ;g,_O4:_o;m8,_a:Float ;__,_:o_;d:__;A,_K,E3,x:Boolean ;_83,h0:String ;f_,X,_i,_:Float ){} }Class j{Var $6_,$_d:KB_x;$T(){Break ;}Destructor (){}Constructor (){}Destructor (){Var _:Array [Array [String ,0b1],0X24];}Val __:Array [Array [Array [Boolean ,0b1001010],0X24],9];Val Jq:String ;Val $_,$_wt6_X:Boolean ;$_(t:Array [Boolean ,0B11_1]){ {} }}Class _{}''','''Class,_,:,_,{,_8,(,),{,},Constructor,(,_,,,_b3_,:,Int,;,_,:,Array,[,Array,[,Array,[,Float,,,0b1,],,,0B1,],,,062,],;,_,,,_,,,Gb,:,String,;,g,,,_O4,:,_o,;,m8,,,_a,:,Float,;,__,,,_,:,o_,;,d,:,__,;,A,,,_K,,,E3,,,x,:,Boolean,;,_83,,,h0,:,String,;,f_,,,X,,,_i,,,_,:,Float,),{,},},Class,j,{,Var,$6_,,,$_d,:,KB_x,;,$T,(,),{,Break,;,},Destructor,(,),{,},Constructor,(,),{,},Destructor,(,),{,Var,_,:,Array,[,Array,[,String,,,0b1,],,,0X24,],;,},Val,__,:,Array,[,Array,[,Array,[,Boolean,,,0b1001010,],,,0X24,],,,9,],;,Val,Jq,:,String,;,Val,$_,,,$_wt6_X,:,Boolean,;,$_,(,t,:,Array,[,Boolean,,,0B111,],),{,{,},},},Class,_,{,},<EOF>''',101))

    def test_429(self):
        self.assertTrue(TestLexer.test('''Class _:t{$___Eh(__:Array [Array [Array [Array [Boolean ,82_3_5],073],6_6],84];sB,Et,_5_6,f88,w:p1C_6_c_32H;O1,_,_:Boolean ;B3:Array [Boolean ,84]){} }Class _1__9{Constructor (){Break ;}Var _:EJ;}''','''Class,_,:,t,{,$___Eh,(,__,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,8235,],,,073,],,,66,],,,84,],;,sB,,,Et,,,_5_6,,,f88,,,w,:,p1C_6_c_32H,;,O1,,,_,,,_,:,Boolean,;,B3,:,Array,[,Boolean,,,84,],),{,},},Class,_1__9,{,Constructor,(,),{,Break,;,},Var,_,:,EJ,;,},<EOF>''',101))

    def test_430(self):
        self.assertTrue(TestLexer.test('''Class ___{Val _7:q;Constructor (){Continue ;}Constructor (){ {{}{} }Break ;T82A::$g();} }Class w:W688{}Class Z8:s_{}Class ___{}''','''Class,___,{,Val,_7,:,q,;,Constructor,(,),{,Continue,;,},Constructor,(,),{,{,{,},{,},},Break,;,T82A,::,$g,(,),;,},},Class,w,:,W688,{,},Class,Z8,:,s_,{,},Class,___,{,},<EOF>''',101))

    def test_431(self):
        self.assertTrue(TestLexer.test('''Class V__96{}Class b:___{Constructor (){} }Class VO9_O{Constructor (_L_33:Int ;J,crt:Int ){}Destructor (){Break ;}Var BkC,$s,$L_2_7:Array [Array [Int ,55],0136];}''','''Class,V__96,{,},Class,b,:,___,{,Constructor,(,),{,},},Class,VO9_O,{,Constructor,(,_L_33,:,Int,;,J,,,crt,:,Int,),{,},Destructor,(,),{,Break,;,},Var,BkC,,,$s,,,$L_2_7,:,Array,[,Array,[,Int,,,55,],,,0136,],;,},<EOF>''',101))

    def test_432(self):
        self.assertTrue(TestLexer.test('''Class JKo_:mz{}Class _BF1{Destructor (){}Var X__,L__:Z;}Class e__:_{Constructor (_,d:Int ;TJ:Array [Array [Array [Array [String ,0b1_0_0],5],76],0b111011];_,_:_8Pn__3){} }''','''Class,JKo_,:,mz,{,},Class,_BF1,{,Destructor,(,),{,},Var,X__,,,L__,:,Z,;,},Class,e__,:,_,{,Constructor,(,_,,,d,:,Int,;,TJ,:,Array,[,Array,[,Array,[,Array,[,String,,,0b100,],,,5,],,,76,],,,0b111011,],;,_,,,_,:,_8Pn__3,),{,},},<EOF>''',101))

    def test_433(self):
        self.assertTrue(TestLexer.test('''Class _:__{Destructor (){}C7(Ma,_,rz:Float ;z:Array [String ,0X1_D6];_,p:Array [Array [Array [String ,03],02],0X55]){} }''','''Class,_,:,__,{,Destructor,(,),{,},C7,(,Ma,,,_,,,rz,:,Float,;,z,:,Array,[,String,,,0X1D6,],;,_,,,p,:,Array,[,Array,[,Array,[,String,,,03,],,,02,],,,0X55,],),{,},},<EOF>''',101))

    def test_434(self):
        self.assertTrue(TestLexer.test('''Class _:X{Constructor (_:Array [Array [String ,0XE5_25],01306];k:b_;m6:String ;U_,__F,_1HTb,v,_,o,fI48,_:_){} }Class _:W{}Class qU:___{Val q__:_;}Class _Op{Var $_:Boolean ;}''','''Class,_,:,X,{,Constructor,(,_,:,Array,[,Array,[,String,,,0XE525,],,,01306,],;,k,:,b_,;,m6,:,String,;,U_,,,__F,,,_1HTb,,,v,,,_,,,o,,,fI48,,,_,:,_,),{,},},Class,_,:,W,{,},Class,qU,:,___,{,Val,q__,:,_,;,},Class,_Op,{,Var,$_,:,Boolean,;,},<EOF>''',101))

    def test_435(self):
        self.assertTrue(TestLexer.test('''Class O:P{Constructor (Y_7:Array [Int ,04]){} }Class _1{Var $6_,$3,$_rN:Array [Array [Array [Array [Boolean ,0107],0x3A],6],1];Constructor (){}Val $8:Array [String ,0b11_1];}Class F{}''','''Class,O,:,P,{,Constructor,(,Y_7,:,Array,[,Int,,,04,],),{,},},Class,_1,{,Var,$6_,,,$3,,,$_rN,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,0107,],,,0x3A,],,,6,],,,1,],;,Constructor,(,),{,},Val,$8,:,Array,[,String,,,0b111,],;,},Class,F,{,},<EOF>''',101))

    def test_436(self):
        self.assertTrue(TestLexer.test('''Class _:_9{}Class _{Constructor (_8k:Boolean ;q6:Array [Array [Array [Float ,74],05],07_11_2_6_11_1];x,_:_){}Val $E:Array [Boolean ,0X6];}''','''Class,_,:,_9,{,},Class,_,{,Constructor,(,_8k,:,Boolean,;,q6,:,Array,[,Array,[,Array,[,Float,,,74,],,,05,],,,071126111,],;,x,,,_,:,_,),{,},Val,$E,:,Array,[,Boolean,,,0X6,],;,},<EOF>''',101))

    def test_437(self):
        self.assertTrue(TestLexer.test('''Class _q_{$_(_:Array [String ,2];TMI7,p8_q:Array [Array [Array [Array [Array [Array [Array [Array [Float ,0B1],0x39],066],066],0b111],0b1_0],0X51],0x39]){} }''','''Class,_q_,{,$_,(,_,:,Array,[,String,,,2,],;,TMI7,,,p8_q,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0B1,],,,0x39,],,,066,],,,066,],,,0b111,],,,0b10,],,,0X51,],,,0x39,],),{,},},<EOF>''',101))

    def test_438(self):
        self.assertTrue(TestLexer.test('''Class _:_{}Class __5:_3_{Constructor (_:Array [Array [Float ,0X10],16];G,ucM_,_:String ;_K,_,_:Array [Array [Array [Array [Array [Boolean ,16],0X10],0b10],3],075]){} }''','''Class,_,:,_,{,},Class,__5,:,_3_,{,Constructor,(,_,:,Array,[,Array,[,Float,,,0X10,],,,16,],;,G,,,ucM_,,,_,:,String,;,_K,,,_,,,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,16,],,,0X10,],,,0b10,],,,3,],,,075,],),{,},},<EOF>''',101))

    def test_439(self):
        self.assertTrue(TestLexer.test('''Class q:o{Constructor (_4,_:B){}K(_p,V,_,A1__5,__:Boolean ;I2M,_,Qz:Float ;H:_61_;_:Array [String ,0B1010010];_1,_,I4:String ){} }Class j:__8{}Class B{}''','''Class,q,:,o,{,Constructor,(,_4,,,_,:,B,),{,},K,(,_p,,,V,,,_,,,A1__5,,,__,:,Boolean,;,I2M,,,_,,,Qz,:,Float,;,H,:,_61_,;,_,:,Array,[,String,,,0B1010010,],;,_1,,,_,,,I4,:,String,),{,},},Class,j,:,__8,{,},Class,B,{,},<EOF>''',101))

    def test_440(self):
        self.assertTrue(TestLexer.test('''Class _{Destructor (){}Val $_d__:Array [Array [Boolean ,03],0B1];Constructor (_,__,_:Array [Array [Boolean ,0X54],0b11];g:Int ;w,e,M8,v,i:Array [Array [Boolean ,03_0],7];pU:_){} }''','''Class,_,{,Destructor,(,),{,},Val,$_d__,:,Array,[,Array,[,Boolean,,,03,],,,0B1,],;,Constructor,(,_,,,__,,,_,:,Array,[,Array,[,Boolean,,,0X54,],,,0b11,],;,g,:,Int,;,w,,,e,,,M8,,,v,,,i,:,Array,[,Array,[,Boolean,,,030,],,,7,],;,pU,:,_,),{,},},<EOF>''',101))

    def test_441(self):
        self.assertTrue(TestLexer.test('''Class _x{Constructor (_d7439s:Boolean ;h1:V0;L_:Int ){} }Class J0_:h{}Class __:C{Constructor (K,_9,_9,Cu:Float ){} }Class ZZ{}''','''Class,_x,{,Constructor,(,_d7439s,:,Boolean,;,h1,:,V0,;,L_,:,Int,),{,},},Class,J0_,:,h,{,},Class,__,:,C,{,Constructor,(,K,,,_9,,,_9,,,Cu,:,Float,),{,},},Class,ZZ,{,},<EOF>''',101))

    def test_442(self):
        self.assertTrue(TestLexer.test('''Class _:_{Var $00:Array [Int ,0b1110];S(_1_2Xc:Array [Boolean ,19]){} }Class _0{Var _:Array [Array [Boolean ,19],063];}Class _:_1{}''','''Class,_,:,_,{,Var,$00,:,Array,[,Int,,,0b1110,],;,S,(,_1_2Xc,:,Array,[,Boolean,,,19,],),{,},},Class,_0,{,Var,_,:,Array,[,Array,[,Boolean,,,19,],,,063,],;,},Class,_,:,_1,{,},<EOF>''',101))

    def test_443(self):
        self.assertTrue(TestLexer.test('''Class y5:N{$tl_(Z83_,_9hm3:Int ;_7_:Float ;_:Z;Ks_2:z;C:Int ;_:q2;_47,OD,_2_G:Float ){Val n:Array [Array [Array [Int ,0x2],0b10001],0x2];}Val KA_,_3R_,V__,_:Array [Boolean ,053];}Class F{}''','''Class,y5,:,N,{,$tl_,(,Z83_,,,_9hm3,:,Int,;,_7_,:,Float,;,_,:,Z,;,Ks_2,:,z,;,C,:,Int,;,_,:,q2,;,_47,,,OD,,,_2_G,:,Float,),{,Val,n,:,Array,[,Array,[,Array,[,Int,,,0x2,],,,0b10001,],,,0x2,],;,},Val,KA_,,,_3R_,,,V__,,,_,:,Array,[,Boolean,,,053,],;,},Class,F,{,},<EOF>''',101))

    def test_444(self):
        self.assertTrue(TestLexer.test('''Class UT{Destructor (){} }Class _:fQ{Destructor (){}Constructor (){} }Class _mu42_:j{}Class I{}Class _Rk:K{Destructor (){} }''','''Class,UT,{,Destructor,(,),{,},},Class,_,:,fQ,{,Destructor,(,),{,},Constructor,(,),{,},},Class,_mu42_,:,j,{,},Class,I,{,},Class,_Rk,:,K,{,Destructor,(,),{,},},<EOF>''',101))

    def test_445(self):
        self.assertTrue(TestLexer.test('''Class __Ri_:V{Val _6,Z4_N7:Array [Array [Array [Array [Array [Array [Array [Int ,1],9_179],0xF],0b10],0X1F],04],8];}''','''Class,__Ri_,:,V,{,Val,_6,,,Z4_N7,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,1,],,,9179,],,,0xF,],,,0b10,],,,0X1F,],,,04,],,,8,],;,},<EOF>''',101))

    def test_446(self):
        self.assertTrue(TestLexer.test('''Class E_:qE7{}Class R:TC{}Class W{Val $_,Q:Array [Array [Array [Array [Array [Array [Array [Array [Float ,0X2],0x31],0B10],0x31],0X2],044],044],06];}''','''Class,E_,:,qE7,{,},Class,R,:,TC,{,},Class,W,{,Val,$_,,,Q,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0X2,],,,0x31,],,,0B10,],,,0x31,],,,0X2,],,,044,],,,044,],,,06,],;,},<EOF>''',101))

    def test_447(self):
        self.assertTrue(TestLexer.test('''Class k7k8:hFW{Val O_Dx:Int ;Destructor (){}Constructor (B:Boolean ){}Destructor (){}Var $4,W,_,$_:Array [Array [Array [Array [Array [Array [Int ,0x20],2],0X4],65],65],0B1];}''','''Class,k7k8,:,hFW,{,Val,O_Dx,:,Int,;,Destructor,(,),{,},Constructor,(,B,:,Boolean,),{,},Destructor,(,),{,},Var,$4,,,W,,,_,,,$_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0x20,],,,2,],,,0X4,],,,65,],,,65,],,,0B1,],;,},<EOF>''',101))

    def test_448(self):
        self.assertTrue(TestLexer.test('''Class bCv{}Class _3{_(M__:Array [Array [Array [Array [Int ,9],0b1001110],0b1001110],0X25]){}Val Ot:_e;Constructor (){}Var _35FC,$_,$_,_9:String ;}Class T_:g_3J{}Class b3{}''','''Class,bCv,{,},Class,_3,{,_,(,M__,:,Array,[,Array,[,Array,[,Array,[,Int,,,9,],,,0b1001110,],,,0b1001110,],,,0X25,],),{,},Val,Ot,:,_e,;,Constructor,(,),{,},Var,_35FC,,,$_,,,$_,,,_9,:,String,;,},Class,T_,:,g_3J,{,},Class,b3,{,},<EOF>''',101))

    def test_449(self):
        self.assertTrue(TestLexer.test('''Class V:_{}Class _{}Class S{$_(_:_;_,Pw:Array [String ,0136];_,I,mJ_,p:Array [Float ,0xF02_9];__M:Float ;_8S,R,M7P1,A,eI,bl3:Boolean ;__:Float ;H:_;_,_:J_1){Return ;} }''','''Class,V,:,_,{,},Class,_,{,},Class,S,{,$_,(,_,:,_,;,_,,,Pw,:,Array,[,String,,,0136,],;,_,,,I,,,mJ_,,,p,:,Array,[,Float,,,0xF029,],;,__M,:,Float,;,_8S,,,R,,,M7P1,,,A,,,eI,,,bl3,:,Boolean,;,__,:,Float,;,H,:,_,;,_,,,_,:,J_1,),{,Return,;,},},<EOF>''',101))

    def test_450(self):
        self.assertTrue(TestLexer.test('''Class __:Jq{Var $_,u:Array [Array [Array [Array [Array [Array [Float ,2],14],1_19],0X39],050],0102];}Class MD:_b_{Var $3m,$4:Array [Array [Array [Array [Array [Array [Array [Array [String ,0XC],0X39],0b1],6],0X88],03],0102],3_7233_0];}Class G{}''','''Class,__,:,Jq,{,Var,$_,,,u,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,2,],,,14,],,,119,],,,0X39,],,,050,],,,0102,],;,},Class,MD,:,_b_,{,Var,$3m,,,$4,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0XC,],,,0X39,],,,0b1,],,,6,],,,0X88,],,,03,],,,0102,],,,372330,],;,},Class,G,{,},<EOF>''',101))

    def test_451(self):
        self.assertTrue(TestLexer.test('''Class _n:z7__R_f2_x{Constructor (){}Constructor (){} }Class M0{Val $_7,$2:Boolean ;}Class _:_{}Class _:s6{Val _z:Int ;}''','''Class,_n,:,z7__R_f2_x,{,Constructor,(,),{,},Constructor,(,),{,},},Class,M0,{,Val,$_7,,,$2,:,Boolean,;,},Class,_,:,_,{,},Class,_,:,s6,{,Val,_z,:,Int,;,},<EOF>''',101))

    def test_452(self):
        self.assertTrue(TestLexer.test('''Class v8e{}Class p7:__{}Class _{Val h,_5,$_:Array [Array [Array [String ,0x7E],024],01];Val $_:String ;Val V1a,$_:Int ;}''','''Class,v8e,{,},Class,p7,:,__,{,},Class,_,{,Val,h,,,_5,,,$_,:,Array,[,Array,[,Array,[,String,,,0x7E,],,,024,],,,01,],;,Val,$_,:,String,;,Val,V1a,,,$_,:,Int,;,},<EOF>''',101))

    def test_453(self):
        self.assertTrue(TestLexer.test('''Class Zi{Destructor (){Var r,uCe7:Float ;Val _k:String ;Break ;}Val V4:Boolean =!-O::$6._._();Constructor (){Val _,FG9_A_,_k_1:Int ;}Destructor (){ {} }Destructor (){} }''','''Class,Zi,{,Destructor,(,),{,Var,r,,,uCe7,:,Float,;,Val,_k,:,String,;,Break,;,},Val,V4,:,Boolean,=,!,-,O,::,$6,.,_,.,_,(,),;,Constructor,(,),{,Val,_,,,FG9_A_,,,_k_1,:,Int,;,},Destructor,(,),{,{,},},Destructor,(,),{,},},<EOF>''',101))

    def test_454(self):
        self.assertTrue(TestLexer.test('''Class m:R{Constructor (EW:Array [Array [Array [Array [Array [Array [Array [Array [Array [String ,0X40],0x5],0X40],017],017],0b1_11111],3_81],0B110011],05535]){} }''','''Class,m,:,R,{,Constructor,(,EW,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0X40,],,,0x5,],,,0X40,],,,017,],,,017,],,,0b111111,],,,381,],,,0B110011,],,,05535,],),{,},},<EOF>''',101))

    def test_455(self):
        self.assertTrue(TestLexer.test('''Class _{}Class cn5:Q{}Class _{Val F__,uCBlp23K:Array [Array [Array [Array [Array [Array [Array [Float ,94245],73],0B1010110],0B1],0x60],022],0x6];Destructor (){}Var _9:String ;Constructor (F_:String ;A,w,_34,_0:A;HK8O5_:_;W:Int ){}Var $_,y_:Boolean ;Var $co8:Array [Array [Array [Float ,0X62],03_2],0x7];}''','''Class,_,{,},Class,cn5,:,Q,{,},Class,_,{,Val,F__,,,uCBlp23K,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,94245,],,,73,],,,0B1010110,],,,0B1,],,,0x60,],,,022,],,,0x6,],;,Destructor,(,),{,},Var,_9,:,String,;,Constructor,(,F_,:,String,;,A,,,w,,,_34,,,_0,:,A,;,HK8O5_,:,_,;,W,:,Int,),{,},Var,$_,,,y_,:,Boolean,;,Var,$co8,:,Array,[,Array,[,Array,[,Float,,,0X62,],,,032,],,,0x7,],;,},<EOF>''',101))

    def test_456(self):
        self.assertTrue(TestLexer.test('''Class M:_{Constructor (Y0,J,_:Array [Int ,0x56];w:Int ;i8:Int ;Y5:_;_:Float ){} }Class cX:_37_{Var $5:Array [Array [Array [String ,0B1],0b1100],0x6_4];}Class _33{Constructor (n,r,_:Array [Array [Int ,0x56],0xD];_,w11_,o:_;__9i,X,___,Z__,m,_:Float ){} }Class _Kr_{Var c,$9:Boolean ;}''','''Class,M,:,_,{,Constructor,(,Y0,,,J,,,_,:,Array,[,Int,,,0x56,],;,w,:,Int,;,i8,:,Int,;,Y5,:,_,;,_,:,Float,),{,},},Class,cX,:,_37_,{,Var,$5,:,Array,[,Array,[,Array,[,String,,,0B1,],,,0b1100,],,,0x64,],;,},Class,_33,{,Constructor,(,n,,,r,,,_,:,Array,[,Array,[,Int,,,0x56,],,,0xD,],;,_,,,w11_,,,o,:,_,;,__9i,,,X,,,___,,,Z__,,,m,,,_,:,Float,),{,},},Class,_Kr_,{,Var,c,,,$9,:,Boolean,;,},<EOF>''',101))

    def test_457(self):
        self.assertTrue(TestLexer.test('''Class g_:__{Constructor (O,__:e;_:Float ;__8:_;Z:R){Break ;Return ;Continue ;} }Class c5:Z{Val XKQ,__7j:String ;$7(_:sT;Q91:String ){} }''','''Class,g_,:,__,{,Constructor,(,O,,,__,:,e,;,_,:,Float,;,__8,:,_,;,Z,:,R,),{,Break,;,Return,;,Continue,;,},},Class,c5,:,Z,{,Val,XKQ,,,__7j,:,String,;,$7,(,_,:,sT,;,Q91,:,String,),{,},},<EOF>''',101))

    def test_458(self):
        self.assertTrue(TestLexer.test('''Class _8:_4{Constructor (_:Int ;_:Array [Array [Int ,0B1],8]){} }Class __f{Val ___R7,$4_,L,_C7:Int ;}Class u__{}Class X____{}Class w{Destructor (){Val Me_:Int ;} }Class y_:d{}Class __5{Constructor (){} }''','''Class,_8,:,_4,{,Constructor,(,_,:,Int,;,_,:,Array,[,Array,[,Int,,,0B1,],,,8,],),{,},},Class,__f,{,Val,___R7,,,$4_,,,L,,,_C7,:,Int,;,},Class,u__,{,},Class,X____,{,},Class,w,{,Destructor,(,),{,Val,Me_,:,Int,;,},},Class,y_,:,d,{,},Class,__5,{,Constructor,(,),{,},},<EOF>''',101))

    def test_459(self):
        self.assertTrue(TestLexer.test('''Class q0h{Constructor (_:Int ;__:Array [Array [Array [Int ,3],057],0X8];C39:Boolean ;_i9,k,_:Array [Array [Float ,85_5_8],03]){} }''','''Class,q0h,{,Constructor,(,_,:,Int,;,__,:,Array,[,Array,[,Array,[,Int,,,3,],,,057,],,,0X8,],;,C39,:,Boolean,;,_i9,,,k,,,_,:,Array,[,Array,[,Float,,,8558,],,,03,],),{,},},<EOF>''',101))

    def test_460(self):
        self.assertTrue(TestLexer.test('''Class __:M_{Val $B_,$_____,_,_NF:Array [Boolean ,05_011];}Class __b{Val $_6:_;Constructor (){}Destructor (){} }''','''Class,__,:,M_,{,Val,$B_,,,$_____,,,_,,,_NF,:,Array,[,Boolean,,,05011,],;,},Class,__b,{,Val,$_6,:,_,;,Constructor,(,),{,},Destructor,(,),{,},},<EOF>''',101))

    def test_461(self):
        self.assertTrue(TestLexer.test('''Class _w{}Class __3{Var $_:Array [Array [Array [Array [String ,0X3],80],5],0xDE_B];Var $297:_;Val $2__M7943,$5Cc:Array [Array [Array [Boolean ,80],80],02];}Class _:oS{}''','''Class,_w,{,},Class,__3,{,Var,$_,:,Array,[,Array,[,Array,[,Array,[,String,,,0X3,],,,80,],,,5,],,,0xDEB,],;,Var,$297,:,_,;,Val,$2__M7943,,,$5Cc,:,Array,[,Array,[,Array,[,Boolean,,,80,],,,80,],,,02,],;,},Class,_,:,oS,{,},<EOF>''',101))

    def test_462(self):
        self.assertTrue(TestLexer.test('''Class A:__{}Class _:a1_0L{Constructor (){Continue ;Continue ;}Var $6,S,$3_8:Array [Boolean ,063];Constructor (){} }''','''Class,A,:,__,{,},Class,_,:,a1_0L,{,Constructor,(,),{,Continue,;,Continue,;,},Var,$6,,,S,,,$3_8,:,Array,[,Boolean,,,063,],;,Constructor,(,),{,},},<EOF>''',101))

    def test_463(self):
        self.assertTrue(TestLexer.test('''Class _m{Destructor (){}Constructor (e,_,_,k:Q;b_,g,j,_,S:Array [Array [Array [Array [Array [Array [String ,07_32],0X2D],0X7_4],0x4A],4],0x3_0];_pW:Array [Array [String ,4],073];_:Array [Array [Array [Array [Boolean ,0X2D],0B1100001],0xE7E],0X2D];_:U5KH;_5,D3,_:I){} }''','''Class,_m,{,Destructor,(,),{,},Constructor,(,e,,,_,,,_,,,k,:,Q,;,b_,,,g,,,j,,,_,,,S,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0732,],,,0X2D,],,,0X74,],,,0x4A,],,,4,],,,0x30,],;,_pW,:,Array,[,Array,[,String,,,4,],,,073,],;,_,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,0X2D,],,,0B1100001,],,,0xE7E,],,,0X2D,],;,_,:,U5KH,;,_5,,,D3,,,_,:,I,),{,},},<EOF>''',101))

    def test_464(self):
        self.assertTrue(TestLexer.test('''Class G_2_:K{}Class d{Constructor (U8,_,_6:g1;I7:Array [Array [Array [Array [String ,7_9],9],9],0b1]){}Var $K:Array [String ,02_1];}''','''Class,G_2_,:,K,{,},Class,d,{,Constructor,(,U8,,,_,,,_6,:,g1,;,I7,:,Array,[,Array,[,Array,[,Array,[,String,,,79,],,,9,],,,9,],,,0b1,],),{,},Var,$K,:,Array,[,String,,,021,],;,},<EOF>''',101))

    def test_465(self):
        self.assertTrue(TestLexer.test('''Class k:S5_{$1q_(U,_5,P,i3,_,_:_;I0:_y;_:_){} }Class __{Destructor (){Var _S__uA,_,A__:Array [Boolean ,052];}Var E,$_:String ;}Class r{}''','''Class,k,:,S5_,{,$1q_,(,U,,,_5,,,P,,,i3,,,_,,,_,:,_,;,I0,:,_y,;,_,:,_,),{,},},Class,__,{,Destructor,(,),{,Var,_S__uA,,,_,,,A__,:,Array,[,Boolean,,,052,],;,},Var,E,,,$_,:,String,;,},Class,r,{,},<EOF>''',101))

    def test_466(self):
        self.assertTrue(TestLexer.test('''Class _EH{Constructor (){}m(u_:a_;_,M:Int ;_:Boolean ){} }Class _:_{}Class _{Val _9_:Array [Array [Array [Float ,052],0X60],0B110];}''','''Class,_EH,{,Constructor,(,),{,},m,(,u_,:,a_,;,_,,,M,:,Int,;,_,:,Boolean,),{,},},Class,_,:,_,{,},Class,_,{,Val,_9_,:,Array,[,Array,[,Array,[,Float,,,052,],,,0X60,],,,0B110,],;,},<EOF>''',101))

    def test_467(self):
        self.assertTrue(TestLexer.test('''Class _V__{Val $A6,_:Array [Array [Array [Array [Float ,0x13],29_1],0B1011101],0B1];Val $__v:Array [Array [Array [Int ,69],07],69];}Class _{Constructor (){} }Class T_{Val $_:Int ;}Class _:q{}''','''Class,_V__,{,Val,$A6,,,_,:,Array,[,Array,[,Array,[,Array,[,Float,,,0x13,],,,291,],,,0B1011101,],,,0B1,],;,Val,$__v,:,Array,[,Array,[,Array,[,Int,,,69,],,,07,],,,69,],;,},Class,_,{,Constructor,(,),{,},},Class,T_,{,Val,$_,:,Int,;,},Class,_,:,q,{,},<EOF>''',101))

    def test_468(self):
        self.assertTrue(TestLexer.test('''Class _A0:E6H_{Var _LI_s,Bw:Array [Array [Array [Array [Int ,0B1010100],0b101],031_3],0b1111];Var U:Array [Array [Boolean ,0b1],030];}''','''Class,_A0,:,E6H_,{,Var,_LI_s,,,Bw,:,Array,[,Array,[,Array,[,Array,[,Int,,,0B1010100,],,,0b101,],,,0313,],,,0b1111,],;,Var,U,:,Array,[,Array,[,Boolean,,,0b1,],,,030,],;,},<EOF>''',101))

    def test_469(self):
        self.assertTrue(TestLexer.test('''Class _9:_9{Var l_,$xU,$v5B,$_q,k:Array [Array [Array [Array [Array [Array [Array [Boolean ,22],0105],1],01],0B1],22],9_6];}Class h_{}''','''Class,_9,:,_9,{,Var,l_,,,$xU,,,$v5B,,,$_q,,,k,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,22,],,,0105,],,,1,],,,01,],,,0B1,],,,22,],,,96,],;,},Class,h_,{,},<EOF>''',101))

    def test_470(self):
        self.assertTrue(TestLexer.test('''Class _4:d__{Constructor (HWI,_:Array [Float ,0B101000];G,C:Array [Boolean ,06];__29:Boolean ;b,m7:Array [Array [Float ,0b1100000],0x19];uC:Array [Array [Int ,070],0b1100000];_1,D:Int ;n60:__;_,_:Float ;_:Float ){Break ;} }''','''Class,_4,:,d__,{,Constructor,(,HWI,,,_,:,Array,[,Float,,,0B101000,],;,G,,,C,:,Array,[,Boolean,,,06,],;,__29,:,Boolean,;,b,,,m7,:,Array,[,Array,[,Float,,,0b1100000,],,,0x19,],;,uC,:,Array,[,Array,[,Int,,,070,],,,0b1100000,],;,_1,,,D,:,Int,;,n60,:,__,;,_,,,_,:,Float,;,_,:,Float,),{,Break,;,},},<EOF>''',101))

    def test_471(self):
        self.assertTrue(TestLexer.test('''Class Qy:__e{Var $x,$_9,$_:Float ;$5(_V,_W,_h8,dI:Float ;G:Array [Array [Boolean ,47_981_7_11],03_7];_a:Int ;O:Array [Array [Int ,52],0B1];_,_2_,__,_,fJ:Array [Array [String ,0B111000],0b1100]){} }''','''Class,Qy,:,__e,{,Var,$x,,,$_9,,,$_,:,Float,;,$5,(,_V,,,_W,,,_h8,,,dI,:,Float,;,G,:,Array,[,Array,[,Boolean,,,47981711,],,,037,],;,_a,:,Int,;,O,:,Array,[,Array,[,Int,,,52,],,,0B1,],;,_,,,_2_,,,__,,,_,,,fJ,:,Array,[,Array,[,String,,,0B111000,],,,0b1100,],),{,},},<EOF>''',101))

    def test_472(self):
        self.assertTrue(TestLexer.test('''Class A{Constructor (__:f;__26,O5:Array [Array [Array [Array [Boolean ,80_4_4],0X48],1_8_78],0xA];_x2Cv,h____,NU,q:jh99_;i,_:Float ;H,l_,_:__h_s){} }''','''Class,A,{,Constructor,(,__,:,f,;,__26,,,O5,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,8044,],,,0X48,],,,1878,],,,0xA,],;,_x2Cv,,,h____,,,NU,,,q,:,jh99_,;,i,,,_,:,Float,;,H,,,l_,,,_,:,__h_s,),{,},},<EOF>''',101))

    def test_473(self):
        self.assertTrue(TestLexer.test('''Class _{Constructor (L,__Hx:__2;__8,G,M:_Vf;_9,_:f;iI,y_6_,w_:Array [Boolean ,07_4];_z__,Q__5d,__,_28,P:Int ;___,y,B:Float ;xX,_,__:Q_){} }''','''Class,_,{,Constructor,(,L,,,__Hx,:,__2,;,__8,,,G,,,M,:,_Vf,;,_9,,,_,:,f,;,iI,,,y_6_,,,w_,:,Array,[,Boolean,,,074,],;,_z__,,,Q__5d,,,__,,,_28,,,P,:,Int,;,___,,,y,,,B,:,Float,;,xX,,,_,,,__,:,Q_,),{,},},<EOF>''',101))

    def test_474(self):
        self.assertTrue(TestLexer.test('''Class h{$1Y(J:th;b:_1_){}Var $_:Array [Array [Array [Array [Array [Boolean ,0XB_8_96],17],0b1_0],07],0b1000011];$I(j98:c){} }''','''Class,h,{,$1Y,(,J,:,th,;,b,:,_1_,),{,},Var,$_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0XB896,],,,17,],,,0b10,],,,07,],,,0b1000011,],;,$I,(,j98,:,c,),{,},},<EOF>''',101))

    def test_475(self):
        self.assertTrue(TestLexer.test('''Class a{}Class _:g{Constructor (t,k,_,__1e,u:Array [String ,0b101110]){Continue ;Continue ;Val d:v_;} }Class _C5:_{Var _:Boolean ;}''','''Class,a,{,},Class,_,:,g,{,Constructor,(,t,,,k,,,_,,,__1e,,,u,:,Array,[,String,,,0b101110,],),{,Continue,;,Continue,;,Val,d,:,v_,;,},},Class,_C5,:,_,{,Var,_,:,Boolean,;,},<EOF>''',101))

    def test_476(self):
        self.assertTrue(TestLexer.test('''Class _:s{}Class _5:_4{}Class rU4_H59:J{Destructor (){Break ;} }Class Gic4A{}Class j1:B2{}Class p{Var C:Boolean ;}Class O:_0{}''','''Class,_,:,s,{,},Class,_5,:,_4,{,},Class,rU4_H59,:,J,{,Destructor,(,),{,Break,;,},},Class,Gic4A,{,},Class,j1,:,B2,{,},Class,p,{,Var,C,:,Boolean,;,},Class,O,:,_0,{,},<EOF>''',101))

    def test_477(self):
        self.assertTrue(TestLexer.test('''Class _E0:Pu_{Constructor (___:_;_0_:Array [Array [Array [String ,0b1],2],070];_7,W,UD_:Int ;_,H3e5:Array [String ,0b1]){} }Class y:f3{}''','''Class,_E0,:,Pu_,{,Constructor,(,___,:,_,;,_0_,:,Array,[,Array,[,Array,[,String,,,0b1,],,,2,],,,070,],;,_7,,,W,,,UD_,:,Int,;,_,,,H3e5,:,Array,[,String,,,0b1,],),{,},},Class,y,:,f3,{,},<EOF>''',101))

    def test_478(self):
        self.assertTrue(TestLexer.test('''Class B:V_{Val $b,H:Array [Int ,33];Constructor (sd,r,_M_C2:Array [Array [Float ,0b11000],0x21]){}Destructor (){ {} }Destructor (){Return ;} }Class _63:_W{}''','''Class,B,:,V_,{,Val,$b,,,H,:,Array,[,Int,,,33,],;,Constructor,(,sd,,,r,,,_M_C2,:,Array,[,Array,[,Float,,,0b11000,],,,0x21,],),{,},Destructor,(,),{,{,},},Destructor,(,),{,Return,;,},},Class,_63,:,_W,{,},<EOF>''',101))

    def test_479(self):
        self.assertTrue(TestLexer.test('''Class _:O5l{Var $G_:zJ;}Class _:_1_I_f{$O7y(_M9_3__:Float ;e,_,F_:Array [Int ,02]){}f(){}Destructor (){ {} }Var $7,_rUbL0:Array [String ,0x33];y(q,_b,___R_,_m__,LB:String ){} }Class _:__{}''','''Class,_,:,O5l,{,Var,$G_,:,zJ,;,},Class,_,:,_1_I_f,{,$O7y,(,_M9_3__,:,Float,;,e,,,_,,,F_,:,Array,[,Int,,,02,],),{,},f,(,),{,},Destructor,(,),{,{,},},Var,$7,,,_rUbL0,:,Array,[,String,,,0x33,],;,y,(,q,,,_b,,,___R_,,,_m__,,,LB,:,String,),{,},},Class,_,:,__,{,},<EOF>''',101))

    def test_480(self):
        self.assertTrue(TestLexer.test('''Class _{Destructor (){ {}{Continue ;}Var _W:Array [Array [Array [Array [Array [Array [Array [String ,1],0b1],0x3],063],2],0b110010],0x1D_0];}Constructor (){} }Class _P:_9{}''','''Class,_,{,Destructor,(,),{,{,},{,Continue,;,},Var,_W,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,1,],,,0b1,],,,0x3,],,,063,],,,2,],,,0b110010,],,,0x1D0,],;,},Constructor,(,),{,},},Class,_P,:,_9,{,},<EOF>''',101))

    def test_481(self):
        self.assertTrue(TestLexer.test('''Class g:_n{Destructor (){_9b_::$9K();Return ;} }Class m:A_{Val $5_u,$C,$_,$3,$1,_P_:Float ;}Class j:_5_{Var $W_,o_o,$_C9,$_J:Vrj;}''','''Class,g,:,_n,{,Destructor,(,),{,_9b_,::,$9K,(,),;,Return,;,},},Class,m,:,A_,{,Val,$5_u,,,$C,,,$_,,,$3,,,$1,,,_P_,:,Float,;,},Class,j,:,_5_,{,Var,$W_,,,o_o,,,$_C9,,,$_J,:,Vrj,;,},<EOF>''',101))

    def test_482(self):
        self.assertTrue(TestLexer.test('''Class T{Var x5,$733V,_,_,u_2__:_;Var $7,$7,x,gO7,_,$__:Array [Int ,19];OJ(){Val a:Array [Boolean ,0B101101];Break ;} }''','''Class,T,{,Var,x5,,,$733V,,,_,,,_,,,u_2__,:,_,;,Var,$7,,,$7,,,x,,,gO7,,,_,,,$__,:,Array,[,Int,,,19,],;,OJ,(,),{,Val,a,:,Array,[,Boolean,,,0B101101,],;,Break,;,},},<EOF>''',101))

    def test_483(self):
        self.assertTrue(TestLexer.test('''Class __{Constructor (_,EH_,_:Array [Array [Boolean ,31],010];W,_7U4,U:nn_8e;I,D,_J,_IE:String ;H9:W_){}Destructor (){Return ;} }''','''Class,__,{,Constructor,(,_,,,EH_,,,_,:,Array,[,Array,[,Boolean,,,31,],,,010,],;,W,,,_7U4,,,U,:,nn_8e,;,I,,,D,,,_J,,,_IE,:,String,;,H9,:,W_,),{,},Destructor,(,),{,Return,;,},},<EOF>''',101))

    def test_484(self):
        self.assertTrue(TestLexer.test('''Class M_:_3{}Class Bi__n{Constructor (__:_){} }Class _{Var LZ,$_b9:Array [Array [Array [Float ,49],4_4_1_5_7_2],0b11];}''','''Class,M_,:,_3,{,},Class,Bi__n,{,Constructor,(,__,:,_,),{,},},Class,_,{,Var,LZ,,,$_b9,:,Array,[,Array,[,Array,[,Float,,,49,],,,441572,],,,0b11,],;,},<EOF>''',101))

    def test_485(self):
        self.assertTrue(TestLexer.test('''Class _YF{Destructor (){Var E:Float ;Break ;}Var $_,$2,_,$1,_Z,$K:Array [Int ,97];Destructor (){} }Class _:_2T6{Destructor (){} }''','''Class,_YF,{,Destructor,(,),{,Var,E,:,Float,;,Break,;,},Var,$_,,,$2,,,_,,,$1,,,_Z,,,$K,:,Array,[,Int,,,97,],;,Destructor,(,),{,},},Class,_,:,_2T6,{,Destructor,(,),{,},},<EOF>''',101))

    def test_486(self):
        self.assertTrue(TestLexer.test('''Class WK:_{Var __,$_1vDh3b8:__;_3(_,_:t;jN:Array [Array [Array [Float ,0b101101],0x55],0b101101]){Continue ;} }Class f{Val $_,_o_XZ82E____,$____:String ;T(kx5:Array [Array [Array [Array [Int ,57],9],051],0X2B];GC:Int ){} }''','''Class,WK,:,_,{,Var,__,,,$_1vDh3b8,:,__,;,_3,(,_,,,_,:,t,;,jN,:,Array,[,Array,[,Array,[,Float,,,0b101101,],,,0x55,],,,0b101101,],),{,Continue,;,},},Class,f,{,Val,$_,,,_o_XZ82E____,,,$____,:,String,;,T,(,kx5,:,Array,[,Array,[,Array,[,Array,[,Int,,,57,],,,9,],,,051,],,,0X2B,],;,GC,:,Int,),{,},},<EOF>''',101))

    def test_487(self):
        self.assertTrue(TestLexer.test('''Class __JvL__8:_e8_{$D(){} }Class dI8:T{u(v:Float ;Q_5T25M____:Array [Int ,0X6];_:Array [Array [Boolean ,0XEC9F],0b110100]){ {Continue ;} }}Class _f{}''','''Class,__JvL__8,:,_e8_,{,$D,(,),{,},},Class,dI8,:,T,{,u,(,v,:,Float,;,Q_5T25M____,:,Array,[,Int,,,0X6,],;,_,:,Array,[,Array,[,Boolean,,,0XEC9F,],,,0b110100,],),{,{,Continue,;,},},},Class,_f,{,},<EOF>''',101))

    def test_488(self):
        self.assertTrue(TestLexer.test('''Class _{}Class _9_{$h(t81,__,_S5_i,_W485,rQ:Float ;M,Q08,_L:_;_,E5,___:_4;_:_;J_:K_;p:Array [String ,06];fk:_28){} }''','''Class,_,{,},Class,_9_,{,$h,(,t81,,,__,,,_S5_i,,,_W485,,,rQ,:,Float,;,M,,,Q08,,,_L,:,_,;,_,,,E5,,,___,:,_4,;,_,:,_,;,J_,:,K_,;,p,:,Array,[,String,,,06,],;,fk,:,_28,),{,},},<EOF>''',101))

    def test_489(self):
        self.assertTrue(TestLexer.test('''Class f:_7_7__{Val $_:Int ;Var $9_,$2__,Vw__4,$J7,_:___r;Var $_,$_,_,_,m_,_,$6_,$3,$2_,G,$x:Array [Array [Array [Array [Array [Array [Float ,0b111110],0B1001100],34],3_4_1],0XE],0b1];}''','''Class,f,:,_7_7__,{,Val,$_,:,Int,;,Var,$9_,,,$2__,,,Vw__4,,,$J7,,,_,:,___r,;,Var,$_,,,$_,,,_,,,_,,,m_,,,_,,,$6_,,,$3,,,$2_,,,G,,,$x,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0b111110,],,,0B1001100,],,,34,],,,341,],,,0XE,],,,0b1,],;,},<EOF>''',101))

    def test_490(self):
        self.assertTrue(TestLexer.test('''Class K{}Class B{Constructor (ZJ,_,f,_,O:Float ;_,_0_:_P5J;_b_:Array [String ,23]){ {}__::$9_m();}Destructor (){} }''','''Class,K,{,},Class,B,{,Constructor,(,ZJ,,,_,,,f,,,_,,,O,:,Float,;,_,,,_0_,:,_P5J,;,_b_,:,Array,[,String,,,23,],),{,{,},__,::,$9_m,(,),;,},Destructor,(,),{,},},<EOF>''',101))

    def test_491(self):
        self.assertTrue(TestLexer.test('''Class __{}Class _H{Val __o_,$_E,_,$Z,_,$_:Array [String ,0X55];}Class L6_{Val $_9X,P,$v:Array [Array [Array [String ,0xE_8A],0b1011010],07];}Class _{Var h322:Boolean ;}Class ZF:_{}Class j:__ci6{}Class jA{}Class __:_{}Class _{}''','''Class,__,{,},Class,_H,{,Val,__o_,,,$_E,,,_,,,$Z,,,_,,,$_,:,Array,[,String,,,0X55,],;,},Class,L6_,{,Val,$_9X,,,P,,,$v,:,Array,[,Array,[,Array,[,String,,,0xE8A,],,,0b1011010,],,,07,],;,},Class,_,{,Var,h322,:,Boolean,;,},Class,ZF,:,_,{,},Class,j,:,__ci6,{,},Class,jA,{,},Class,__,:,_,{,},Class,_,{,},<EOF>''',101))

    def test_492(self):
        self.assertTrue(TestLexer.test('''Class _1_T{Var $99:Float ;Val $_,_f1_Y,_:Array [Array [Array [Array [Float ,04],0x4],02_5_7_1],0143];Val L39_:Array [Array [Float ,0X44],4];Constructor (){}Val $_:_;}''','''Class,_1_T,{,Var,$99,:,Float,;,Val,$_,,,_f1_Y,,,_,:,Array,[,Array,[,Array,[,Array,[,Float,,,04,],,,0x4,],,,02571,],,,0143,],;,Val,L39_,:,Array,[,Array,[,Float,,,0X44,],,,4,],;,Constructor,(,),{,},Val,$_,:,_,;,},<EOF>''',101))

    def test_493(self):
        self.assertTrue(TestLexer.test('''Class _n{Constructor (J,_2,A:Array [Array [Array [Array [Array [String ,7_5_08],29],07_2],0X3D],06];_s:Array [Array [Array [Float ,0X57],6],0x61]){Break ;} }Class _:_{Destructor (){Var _aW:P_;} }Class f{Var $F22:Int ;}''','''Class,_n,{,Constructor,(,J,,,_2,,,A,:,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,7508,],,,29,],,,072,],,,0X3D,],,,06,],;,_s,:,Array,[,Array,[,Array,[,Float,,,0X57,],,,6,],,,0x61,],),{,Break,;,},},Class,_,:,_,{,Destructor,(,),{,Var,_aW,:,P_,;,},},Class,f,{,Var,$F22,:,Int,;,},<EOF>''',101))

    def test_494(self):
        self.assertTrue(TestLexer.test('''Class _:_{Constructor (_S_:_;_:Int ;_5:Array [Float ,0116];_2:H){}Var $xo,w:Int ;Var B6c:V;Constructor (){Break ;} }''','''Class,_,:,_,{,Constructor,(,_S_,:,_,;,_,:,Int,;,_5,:,Array,[,Float,,,0116,],;,_2,:,H,),{,},Var,$xo,,,w,:,Int,;,Var,B6c,:,V,;,Constructor,(,),{,Break,;,},},<EOF>''',101))

    def test_495(self):
        self.assertTrue(TestLexer.test('''Class w:_{Constructor (_Al7,_,k,gm:__L;__67:String ;_,_:Array [Array [Array [Array [Array [Array [Boolean ,03_1],4],0X28],014],0X51_4],0b1010100];_:String ){} }Class _q{}''','''Class,w,:,_,{,Constructor,(,_Al7,,,_,,,k,,,gm,:,__L,;,__67,:,String,;,_,,,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,031,],,,4,],,,0X28,],,,014,],,,0X514,],,,0b1010100,],;,_,:,String,),{,},},Class,_q,{,},<EOF>''',101))

    def test_496(self):
        self.assertTrue(TestLexer.test('''Class _6:_{Constructor (){} }Class W:e_0_{Var $_T0:Array [Boolean ,0B1];}Class __{}Class _{Destructor (){} }Class _5{Var __:Int ;}''','''Class,_6,:,_,{,Constructor,(,),{,},},Class,W,:,e_0_,{,Var,$_T0,:,Array,[,Boolean,,,0B1,],;,},Class,__,{,},Class,_,{,Destructor,(,),{,},},Class,_5,{,Var,__,:,Int,;,},<EOF>''',101))

    def test_497(self):
        self.assertTrue(TestLexer.test('''Class z{}Class Bq:c{Constructor (W:_____;_,_h6,__:Array [Array [Array [Array [Array [Array [Float ,0x9],0XF],0b111011],2_50],0x9],0XB6];_d:m_;W8X:vJ){} }''','''Class,z,{,},Class,Bq,:,c,{,Constructor,(,W,:,_____,;,_,,,_h6,,,__,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0x9,],,,0XF,],,,0b111011,],,,250,],,,0x9,],,,0XB6,],;,_d,:,m_,;,W8X,:,vJ,),{,},},<EOF>''',101))

    def test_498(self):
        self.assertTrue(TestLexer.test('''Class _{Val $_:_kP_e2;}Class mzKl{Constructor (_,s:_;E,M:g;_2_,z,_i,___,Z,_,D:Array [Array [Float ,5],0X43]){} }''','''Class,_,{,Val,$_,:,_kP_e2,;,},Class,mzKl,{,Constructor,(,_,,,s,:,_,;,E,,,M,:,g,;,_2_,,,z,,,_i,,,___,,,Z,,,_,,,D,:,Array,[,Array,[,Float,,,5,],,,0X43,],),{,},},<EOF>''',101))

    def test_499(self):
        self.assertTrue(TestLexer.test('''Class __{$0(XZ:Int ;_a:String ;a_,W:_12_;_:r_){Var h6_,Jr:Boolean ;} }Class b{fA(){}Destructor (){}Val $C_,_,q,_:Array [Array [Boolean ,48],04];}Class __:_l_{}''','''Class,__,{,$0,(,XZ,:,Int,;,_a,:,String,;,a_,,,W,:,_12_,;,_,:,r_,),{,Var,h6_,,,Jr,:,Boolean,;,},},Class,b,{,fA,(,),{,},Destructor,(,),{,},Val,$C_,,,_,,,q,,,_,:,Array,[,Array,[,Boolean,,,48,],,,04,],;,},Class,__,:,_l_,{,},<EOF>''',101))

    def test_500(self):
        self.assertTrue(TestLexer.test('''Class g_{}Class _{Constructor (O:Array [Int ,0x9];_,_:aU00;P,_f,w:Array [Array [Array [Array [Array [Array [Array [Array [Boolean ,0B1011010],7_0],0X51],03_5],05],84],0124_5],05]){}Var $v,$3:__;}''','''Class,g_,{,},Class,_,{,Constructor,(,O,:,Array,[,Int,,,0x9,],;,_,,,_,:,aU00,;,P,,,_f,,,w,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0B1011010,],,,70,],,,0X51,],,,035,],,,05,],,,84,],,,01245,],,,05,],),{,},Var,$v,,,$3,:,__,;,},<EOF>''',101))

    def test_501(self):
        self.assertTrue(TestLexer.test('''Class _7{$_(_,_:String ;Q8W_,R_O:b2){}Constructor (_x_:Array [Array [String ,0X11],0B1010100]){Break ;Continue ;}_(K_:_){Return ;}_(wO,L:a){Break ;} }''','''Class,_7,{,$_,(,_,,,_,:,String,;,Q8W_,,,R_O,:,b2,),{,},Constructor,(,_x_,:,Array,[,Array,[,String,,,0X11,],,,0B1010100,],),{,Break,;,Continue,;,},_,(,K_,:,_,),{,Return,;,},_,(,wO,,,L,:,a,),{,Break,;,},},<EOF>''',101))

    def test_502(self):
        self.assertTrue(TestLexer.test('''Class f1u38{Val __:Array [Array [Array [Array [String ,02_6_5],0b1],0120],0b1];Destructor (){} }Class _{}Class n_v:_mkL8K_2A6_{}''','''Class,f1u38,{,Val,__,:,Array,[,Array,[,Array,[,Array,[,String,,,0265,],,,0b1,],,,0120,],,,0b1,],;,Destructor,(,),{,},},Class,_,{,},Class,n_v,:,_mkL8K_2A6_,{,},<EOF>''',101))

    def test_503(self):
        self.assertTrue(TestLexer.test('''Class P:_i0{}Class a5{Var $__4N:Float ;}Class _:_{_4oGU(j_:Array [Array [Array [Array [String ,4],0B1],0b1001100],6]){Break ;} }''','''Class,P,:,_i0,{,},Class,a5,{,Var,$__4N,:,Float,;,},Class,_,:,_,{,_4oGU,(,j_,:,Array,[,Array,[,Array,[,Array,[,String,,,4,],,,0B1,],,,0b1001100,],,,6,],),{,Break,;,},},<EOF>''',101))

    def test_504(self):
        self.assertTrue(TestLexer.test('''Class sC:e_{}Class X:_o{Val D_,U:Array [Array [Array [Array [Array [Array [Array [Array [Array [Float ,45],0X13],6],45],0x4A],0B1011111],053],0X13],0B1];}''','''Class,sC,:,e_,{,},Class,X,:,_o,{,Val,D_,,,U,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,45,],,,0X13,],,,6,],,,45,],,,0x4A,],,,0B1011111,],,,053,],,,0X13,],,,0B1,],;,},<EOF>''',101))

    def test_505(self):
        self.assertTrue(TestLexer.test('''Class _{$k(_,_:Array [Boolean ,0B1];_mhO_17:Boolean ;o5,nE7:gy;K,__h,n_:Array [Float ,0X3A]){} }Class _{}Class _v0_{Val $5,$7r___,We01Q_t_9,X:Array [Float ,41];}''','''Class,_,{,$k,(,_,,,_,:,Array,[,Boolean,,,0B1,],;,_mhO_17,:,Boolean,;,o5,,,nE7,:,gy,;,K,,,__h,,,n_,:,Array,[,Float,,,0X3A,],),{,},},Class,_,{,},Class,_v0_,{,Val,$5,,,$7r___,,,We01Q_t_9,,,X,:,Array,[,Float,,,41,],;,},<EOF>''',101))

    def test_506(self):
        self.assertTrue(TestLexer.test('''Class _2_:V5__R{}Class _:_2{Var _,I81u3P,d,____,$T4L,_,$8:Array [Boolean ,74];$K(k:Array [Array [Array [Boolean ,0X19],2],0B1_1011];_:Float ){} }''','''Class,_2_,:,V5__R,{,},Class,_,:,_2,{,Var,_,,,I81u3P,,,d,,,____,,,$T4L,,,_,,,$8,:,Array,[,Boolean,,,74,],;,$K,(,k,:,Array,[,Array,[,Array,[,Boolean,,,0X19,],,,2,],,,0B11011,],;,_,:,Float,),{,},},<EOF>''',101))

    def test_507(self):
        self.assertTrue(TestLexer.test('''Class n{}Class x_s:C_2{}Class Y58__C:E{lj(s1_2_F83,_:Array [Array [Array [Array [String ,0b110],0B1],0B11],0X47];__:Int ;_q,__VT,wu:_6){}Constructor (_:Array [Array [Array [String ,0x7],0X47],06]){Break ;} }Class _q:CV7_{}''','''Class,n,{,},Class,x_s,:,C_2,{,},Class,Y58__C,:,E,{,lj,(,s1_2_F83,,,_,:,Array,[,Array,[,Array,[,Array,[,String,,,0b110,],,,0B1,],,,0B11,],,,0X47,],;,__,:,Int,;,_q,,,__VT,,,wu,:,_6,),{,},Constructor,(,_,:,Array,[,Array,[,Array,[,String,,,0x7,],,,0X47,],,,06,],),{,Break,;,},},Class,_q,:,CV7_,{,},<EOF>''',101))

    def test_508(self):
        self.assertTrue(TestLexer.test('''Class _:_{Var $_,_:Float ;Constructor (){}Var _9,v:Array [Float ,6_4];Var U_3Q:Int ;Val n6,pg:String ;Var C:String ;}''','''Class,_,:,_,{,Var,$_,,,_,:,Float,;,Constructor,(,),{,},Var,_9,,,v,:,Array,[,Float,,,64,],;,Var,U_3Q,:,Int,;,Val,n6,,,pg,:,String,;,Var,C,:,String,;,},<EOF>''',101))

    def test_509(self):
        self.assertTrue(TestLexer.test('''Class _{Val $8:F;Constructor (v:R){}Constructor (e_Qp,_6Q_:Boolean ;_6,v:Int ){} }Class S:f3e{Var $8w:Int ;}Class t2:R{}''','''Class,_,{,Val,$8,:,F,;,Constructor,(,v,:,R,),{,},Constructor,(,e_Qp,,,_6Q_,:,Boolean,;,_6,,,v,:,Int,),{,},},Class,S,:,f3e,{,Var,$8w,:,Int,;,},Class,t2,:,R,{,},<EOF>''',101))

    def test_510(self):
        self.assertTrue(TestLexer.test('''Class _{_n9M(z:x___;__:Array [Int ,0b10];_3,Z:n7__){_::$8_();}Var _2c,$__:_;Val $__7:String ;}Class b{Destructor (){} }''','''Class,_,{,_n9M,(,z,:,x___,;,__,:,Array,[,Int,,,0b10,],;,_3,,,Z,:,n7__,),{,_,::,$8_,(,),;,},Var,_2c,,,$__,:,_,;,Val,$__7,:,String,;,},Class,b,{,Destructor,(,),{,},},<EOF>''',101))

    def test_511(self):
        self.assertTrue(TestLexer.test('''Class B_{$_H(_:U;_:Array [Array [Float ,070],1]){} }Class _7D{_4(P:Array [Int ,1];_A:Array [Array [Int ,070],070];e:Boolean ){} }Class b4{}Class __my:_h_{}''','''Class,B_,{,$_H,(,_,:,U,;,_,:,Array,[,Array,[,Float,,,070,],,,1,],),{,},},Class,_7D,{,_4,(,P,:,Array,[,Int,,,1,],;,_A,:,Array,[,Array,[,Int,,,070,],,,070,],;,e,:,Boolean,),{,},},Class,b4,{,},Class,__my,:,_h_,{,},<EOF>''',101))

    def test_512(self):
        self.assertTrue(TestLexer.test('''Class o:_{Destructor (){}__0(__6l_61:Array [String ,0b10];N,l:Array [Int ,28]){Return ;}$_(_D,_:Float ;_,_,_,m5,_,__:Array [Array [Int ,0xF],0b1]){} }''','''Class,o,:,_,{,Destructor,(,),{,},__0,(,__6l_61,:,Array,[,String,,,0b10,],;,N,,,l,:,Array,[,Int,,,28,],),{,Return,;,},$_,(,_D,,,_,:,Float,;,_,,,_,,,_,,,m5,,,_,,,__,:,Array,[,Array,[,Int,,,0xF,],,,0b1,],),{,},},<EOF>''',101))

    def test_513(self):
        self.assertTrue(TestLexer.test('''Class A{Constructor (__,_3,z,I:Int ;_,C7,E:l){}Val $_44s2v:Boolean ;Val $6,$0n,$8:_;Val r:w1_;}Class g{$P1(){} }Class _{}Class li{}Class h:_3_{}Class q:_{Destructor (){} }''','''Class,A,{,Constructor,(,__,,,_3,,,z,,,I,:,Int,;,_,,,C7,,,E,:,l,),{,},Val,$_44s2v,:,Boolean,;,Val,$6,,,$0n,,,$8,:,_,;,Val,r,:,w1_,;,},Class,g,{,$P1,(,),{,},},Class,_,{,},Class,li,{,},Class,h,:,_3_,{,},Class,q,:,_,{,Destructor,(,),{,},},<EOF>''',101))

    def test_514(self):
        self.assertTrue(TestLexer.test('''Class e:_h{}Class h4tS17{Constructor (J,Q,_2_,_,c__,_:Array [Array [Int ,0X3_8],0b1_00];s_N,__,h5,uOi:Array [Float ,0x37]){} }Class m{_(){} }''','''Class,e,:,_h,{,},Class,h4tS17,{,Constructor,(,J,,,Q,,,_2_,,,_,,,c__,,,_,:,Array,[,Array,[,Int,,,0X38,],,,0b100,],;,s_N,,,__,,,h5,,,uOi,:,Array,[,Float,,,0x37,],),{,},},Class,m,{,_,(,),{,},},<EOF>''',101))

    def test_515(self):
        self.assertTrue(TestLexer.test('''Class c04_J{Constructor (mn,__j61_,j:String ;_,_:Array [String ,14];Fi,f,K_IQ6sE,p:Float ){}Destructor (){}Constructor (R,N_:Array [Array [Array [Array [String ,0x7],0656],0b1010101],034]){}$2_(h2:String ;_:Array [Array [String ,01_1_4],05_4]){} }''','''Class,c04_J,{,Constructor,(,mn,,,__j61_,,,j,:,String,;,_,,,_,:,Array,[,String,,,14,],;,Fi,,,f,,,K_IQ6sE,,,p,:,Float,),{,},Destructor,(,),{,},Constructor,(,R,,,N_,:,Array,[,Array,[,Array,[,Array,[,String,,,0x7,],,,0656,],,,0b1010101,],,,034,],),{,},$2_,(,h2,:,String,;,_,:,Array,[,Array,[,String,,,0114,],,,054,],),{,},},<EOF>''',101))

    def test_516(self):
        self.assertTrue(TestLexer.test('''Class _:_1{$2_Y_U(_i:P;_:Boolean ;c_h,d_E,l_,_:_;G_:I7___rxN;__8,_1,gV5_,n,_6:Int ;u:Float ;K_3_,__9,O,__r,_b:_9;h:hh_6_;_c_8,z:Float ){} }''','''Class,_,:,_1,{,$2_Y_U,(,_i,:,P,;,_,:,Boolean,;,c_h,,,d_E,,,l_,,,_,:,_,;,G_,:,I7___rxN,;,__8,,,_1,,,gV5_,,,n,,,_6,:,Int,;,u,:,Float,;,K_3_,,,__9,,,O,,,__r,,,_b,:,_9,;,h,:,hh_6_,;,_c_8,,,z,:,Float,),{,},},<EOF>''',101))

    def test_517(self):
        self.assertTrue(TestLexer.test('''Class _b{Destructor (){Return ;}Constructor (){Continue ;Break ;Val w,C:F4;}Var _2:Array [String ,56];Val $__:Array [Array [Boolean ,04],9];Val $_,d,$8_:Array [Boolean ,56];_(_L,x9,n:Float ;j:__7;M_,__x_,S,q:Array [Array [Array [String ,0XB],2_707],0b1001111]){ {} }}Class _p{Destructor (){} }''','''Class,_b,{,Destructor,(,),{,Return,;,},Constructor,(,),{,Continue,;,Break,;,Val,w,,,C,:,F4,;,},Var,_2,:,Array,[,String,,,56,],;,Val,$__,:,Array,[,Array,[,Boolean,,,04,],,,9,],;,Val,$_,,,d,,,$8_,:,Array,[,Boolean,,,56,],;,_,(,_L,,,x9,,,n,:,Float,;,j,:,__7,;,M_,,,__x_,,,S,,,q,:,Array,[,Array,[,Array,[,String,,,0XB,],,,2707,],,,0b1001111,],),{,{,},},},Class,_p,{,Destructor,(,),{,},},<EOF>''',101))

    def test_518(self):
        self.assertTrue(TestLexer.test('''Class S:w_29{}Class z3:Rf{Destructor (){} }Class J:X{Destructor (){ {} }$__(_,O5_z5,_X,zf:P;_:Boolean ;_,A,__8M:Array [Float ,0B11_0_11_1_00]){}on(m4,_9_:Array [Array [Array [Array [Array [Int ,0B10],28],0X25],28],05];I___:Array [Array [Int ,0B1_0_0],0B100000];o_G,g___,_01T0,fH_4_:Array [String ,4_921]){} }Class l{$8(){} }''','''Class,S,:,w_29,{,},Class,z3,:,Rf,{,Destructor,(,),{,},},Class,J,:,X,{,Destructor,(,),{,{,},},$__,(,_,,,O5_z5,,,_X,,,zf,:,P,;,_,:,Boolean,;,_,,,A,,,__8M,:,Array,[,Float,,,0B11011100,],),{,},on,(,m4,,,_9_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0B10,],,,28,],,,0X25,],,,28,],,,05,],;,I___,:,Array,[,Array,[,Int,,,0B100,],,,0B100000,],;,o_G,,,g___,,,_01T0,,,fH_4_,:,Array,[,String,,,4921,],),{,},},Class,l,{,$8,(,),{,},},<EOF>''',101))

    def test_519(self):
        self.assertTrue(TestLexer.test('''Class _P5_6:k{_(__,gG:String ;A8,J__8___t5,__:String ){Return ;Return ;} }Class P{}Class _:u9{Destructor (){} }''','''Class,_P5_6,:,k,{,_,(,__,,,gG,:,String,;,A8,,,J__8___t5,,,__,:,String,),{,Return,;,Return,;,},},Class,P,{,},Class,_,:,u9,{,Destructor,(,),{,},},<EOF>''',101))

    def test_520(self):
        self.assertTrue(TestLexer.test('''Class o83:___6{Constructor (V_:String ;t6H2P32F,_:Array [Array [Boolean ,0b1011101],0b1011101]){}Var $_4,$_,_TS:_232;_(R6G,m:Array [Array [Array [Boolean ,9_3],0xD],0B10111]){_::$80();} }''','''Class,o83,:,___6,{,Constructor,(,V_,:,String,;,t6H2P32F,,,_,:,Array,[,Array,[,Boolean,,,0b1011101,],,,0b1011101,],),{,},Var,$_4,,,$_,,,_TS,:,_232,;,_,(,R6G,,,m,:,Array,[,Array,[,Array,[,Boolean,,,93,],,,0xD,],,,0B10111,],),{,_,::,$80,(,),;,},},<EOF>''',101))

    def test_521(self):
        self.assertTrue(TestLexer.test('''Class O{Val $__wN,$o:Array [Array [Array [Array [String ,0141],5],0XF6],0B10_10];Constructor (){}Destructor (){} }''','''Class,O,{,Val,$__wN,,,$o,:,Array,[,Array,[,Array,[,Array,[,String,,,0141,],,,5,],,,0XF6,],,,0B1010,],;,Constructor,(,),{,},Destructor,(,),{,},},<EOF>''',101))

    def test_522(self):
        self.assertTrue(TestLexer.test('''Class __:_48{Destructor (){}Val $__,__:String ;}Class I{$_r1n(){Var m_s:Boolean ;}$1h(){Continue ;} }Class _:h{}Class _{}Class N__9:_{}Class L816:T_{}Class _:_{Var $_:_;_(){ {} }}''','''Class,__,:,_48,{,Destructor,(,),{,},Val,$__,,,__,:,String,;,},Class,I,{,$_r1n,(,),{,Var,m_s,:,Boolean,;,},$1h,(,),{,Continue,;,},},Class,_,:,h,{,},Class,_,{,},Class,N__9,:,_,{,},Class,L816,:,T_,{,},Class,_,:,_,{,Var,$_,:,_,;,_,(,),{,{,},},},<EOF>''',101))

    def test_523(self):
        self.assertTrue(TestLexer.test('''Class _:_{___L(_,Vu,Auw8h:o){}Constructor (){}Constructor (V05_l,__9:Boolean ;_n,___,OE_,o_:Array [Array [Array [Array [Array [Array [Array [Array [Array [Array [Float ,13],0b1001100],13],1],036],036],0X4_5],036],013_5],0X7]){} }Class _:__7{}Class _1w3_{}Class A{$8(){} }Class _:C{Val _U3,__,$k,$_,_h,__Mo_:_;}''','''Class,_,:,_,{,___L,(,_,,,Vu,,,Auw8h,:,o,),{,},Constructor,(,),{,},Constructor,(,V05_l,,,__9,:,Boolean,;,_n,,,___,,,OE_,,,o_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,13,],,,0b1001100,],,,13,],,,1,],,,036,],,,036,],,,0X45,],,,036,],,,0135,],,,0X7,],),{,},},Class,_,:,__7,{,},Class,_1w3_,{,},Class,A,{,$8,(,),{,},},Class,_,:,C,{,Val,_U3,,,__,,,$k,,,$_,,,_h,,,__Mo_,:,_,;,},<EOF>''',101))

    def test_524(self):
        self.assertTrue(TestLexer.test('''Class M2_p_{Constructor (_:Array [Array [Array [Array [Array [Array [String ,02],0X46],0X46],03],0X9AB],056_1];o6,d:w;_,m_:Boolean ){}$e0(){ {Return ;{} }} }Class __{Constructor (){} }Class a3_0:_b{}''','''Class,M2_p_,{,Constructor,(,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,02,],,,0X46,],,,0X46,],,,03,],,,0X9AB,],,,0561,],;,o6,,,d,:,w,;,_,,,m_,:,Boolean,),{,},$e0,(,),{,{,Return,;,{,},},},},Class,__,{,Constructor,(,),{,},},Class,a3_0,:,_b,{,},<EOF>''',101))

    def test_525(self):
        self.assertTrue(TestLexer.test('''Class B{}Class _7{Var j3_6_:Array [Array [Array [Array [Array [Int ,8_4_735_5_7_3],0x18],10],04_350],03_1];}Class __{}''','''Class,B,{,},Class,_7,{,Var,j3_6_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,84735573,],,,0x18,],,,10,],,,04350,],,,031,],;,},Class,__,{,},<EOF>''',101))

    def test_526(self):
        self.assertTrue(TestLexer.test('''Class H{$_87(_j:Array [Int ,0xB_2_4]){} }Class u{}Class ___{}Class _ek{Val Bp0,E:Array [Float ,02];}Class p{}Class J{}Class _{}''','''Class,H,{,$_87,(,_j,:,Array,[,Int,,,0xB24,],),{,},},Class,u,{,},Class,___,{,},Class,_ek,{,Val,Bp0,,,E,:,Array,[,Float,,,02,],;,},Class,p,{,},Class,J,{,},Class,_,{,},<EOF>''',101))

    def test_527(self):
        self.assertTrue(TestLexer.test('''Class A_R{Var PJd,_D:t;Constructor (Sq_:L4;g:Array [Float ,0X28];_C,_9H50:Int ;O_3K_,_,N_K:Boolean ;b:m7){} }Class Z46:T{}''','''Class,A_R,{,Var,PJd,,,_D,:,t,;,Constructor,(,Sq_,:,L4,;,g,:,Array,[,Float,,,0X28,],;,_C,,,_9H50,:,Int,;,O_3K_,,,_,,,N_K,:,Boolean,;,b,:,m7,),{,},},Class,Z46,:,T,{,},<EOF>''',101))

    def test_528(self):
        self.assertTrue(TestLexer.test('''Class _4S:S{}Class u2:V{Constructor (c,a,_,x0:Boolean ;_,G9g,_IJ25_,B2_,g__:Array [Int ,0X22];_,_l:String ;_7,_0G,z,_4p:M;R__4,_Qw3:w){} }''','''Class,_4S,:,S,{,},Class,u2,:,V,{,Constructor,(,c,,,a,,,_,,,x0,:,Boolean,;,_,,,G9g,,,_IJ25_,,,B2_,,,g__,:,Array,[,Int,,,0X22,],;,_,,,_l,:,String,;,_7,,,_0G,,,z,,,_4p,:,M,;,R__4,,,_Qw3,:,w,),{,},},<EOF>''',101))

    def test_529(self):
        self.assertTrue(TestLexer.test('''Class E{Var $o:String ;}Class _6r{Var U:k_;Var UL,$__,$u_3,$_,$0,$p6:Array [Array [String ,0b1000101],0b1_0];}Class __:_{}''','''Class,E,{,Var,$o,:,String,;,},Class,_6r,{,Var,U,:,k_,;,Var,UL,,,$__,,,$u_3,,,$_,,,$0,,,$p6,:,Array,[,Array,[,String,,,0b1000101,],,,0b10,],;,},Class,__,:,_,{,},<EOF>''',101))

    def test_530(self):
        self.assertTrue(TestLexer.test('''Class w_u50{$57_8(){} }Class _{}Class Z:__{}Class P:_{Constructor (v1_:_;n:Array [String ,0X41];V:Array [Array [Array [Array [String ,07],0X4E8_D],0B10],0X41];_O_d_,d1,P:__TE;B_9:Boolean ;_:String ;__,_t1,M,f,_,_0,___2,_yw0:q){} }''','''Class,w_u50,{,$57_8,(,),{,},},Class,_,{,},Class,Z,:,__,{,},Class,P,:,_,{,Constructor,(,v1_,:,_,;,n,:,Array,[,String,,,0X41,],;,V,:,Array,[,Array,[,Array,[,Array,[,String,,,07,],,,0X4E8D,],,,0B10,],,,0X41,],;,_O_d_,,,d1,,,P,:,__TE,;,B_9,:,Boolean,;,_,:,String,;,__,,,_t1,,,M,,,f,,,_,,,_0,,,___2,,,_yw0,:,q,),{,},},<EOF>''',101))

    def test_531(self):
        self.assertTrue(TestLexer.test('''Class _:_{}Class w{Val N:_;_(___,_:String ;x:Array [Int ,48_93];_6G,_8:m_1;S_,_:String ;s,W,K,_s:j_t_;Y:Array [Int ,0b1_0];R:Int ;k__,_:Array [Array [Int ,0XDE_EE],0B1];__,W:Int ;L,_:R_){}$___X0(){}Val $3,$C:_;Var ll:_03;}''','''Class,_,:,_,{,},Class,w,{,Val,N,:,_,;,_,(,___,,,_,:,String,;,x,:,Array,[,Int,,,4893,],;,_6G,,,_8,:,m_1,;,S_,,,_,:,String,;,s,,,W,,,K,,,_s,:,j_t_,;,Y,:,Array,[,Int,,,0b10,],;,R,:,Int,;,k__,,,_,:,Array,[,Array,[,Int,,,0XDEEE,],,,0B1,],;,__,,,W,:,Int,;,L,,,_,:,R_,),{,},$___X0,(,),{,},Val,$3,,,$C,:,_,;,Var,ll,:,_03,;,},<EOF>''',101))

    def test_532(self):
        self.assertTrue(TestLexer.test('''Class _7_{$_(ILVM6__I,v,_7:_x;_,__,_:String ;_:Int ;_,j:Array [Array [Array [Array [Array [Array [Array [Boolean ,0b100111],057],04],30],0x40],0x40],30];_eN4:U_7;_4,a_gwA:__){} }''','''Class,_7_,{,$_,(,ILVM6__I,,,v,,,_7,:,_x,;,_,,,__,,,_,:,String,;,_,:,Int,;,_,,,j,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0b100111,],,,057,],,,04,],,,30,],,,0x40,],,,0x40,],,,30,],;,_eN4,:,U_7,;,_4,,,a_gwA,:,__,),{,},},<EOF>''',101))

    def test_533(self):
        self.assertTrue(TestLexer.test('''Class r9{$X(_1__,_u,_e_6,mt_,U_:Vz_8;_:Array [Int ,065];_:Boolean ;_7_rL:Array [Float ,01_2];_3:Boolean ){Continue ;}Var $_:Boolean ;}Class C:GQ{Constructor (){K::$c.C._Y();Continue ;}Constructor (_,JL:Float ){}Destructor (){} }''','''Class,r9,{,$X,(,_1__,,,_u,,,_e_6,,,mt_,,,U_,:,Vz_8,;,_,:,Array,[,Int,,,065,],;,_,:,Boolean,;,_7_rL,:,Array,[,Float,,,012,],;,_3,:,Boolean,),{,Continue,;,},Var,$_,:,Boolean,;,},Class,C,:,GQ,{,Constructor,(,),{,K,::,$c,.,C,.,_Y,(,),;,Continue,;,},Constructor,(,_,,,JL,:,Float,),{,},Destructor,(,),{,},},<EOF>''',101))

    def test_534(self):
        self.assertTrue(TestLexer.test('''Class U{}Class T{Val p_,W,$7:v;U(){}Val NA:Float ;$_(){Break ;Val _R:Array [Array [Array [Array [Float ,0x59],0b11_0_0],4],0B1010011];}Val $L,$_,Jn,j,gI6,__,$_,$_:Array [String ,0x3];}Class bW{}''','''Class,U,{,},Class,T,{,Val,p_,,,W,,,$7,:,v,;,U,(,),{,},Val,NA,:,Float,;,$_,(,),{,Break,;,Val,_R,:,Array,[,Array,[,Array,[,Array,[,Float,,,0x59,],,,0b1100,],,,4,],,,0B1010011,],;,},Val,$L,,,$_,,,Jn,,,j,,,gI6,,,__,,,$_,,,$_,:,Array,[,String,,,0x3,],;,},Class,bW,{,},<EOF>''',101))

    def test_535(self):
        self.assertTrue(TestLexer.test('''Class _4{Constructor (p,_:Z;m,_FG:Array [String ,9_872];_z:Int ;E,d_F8____,h3Cf53:Boolean ;n:h_A00u1_){} }Class _{}''','''Class,_4,{,Constructor,(,p,,,_,:,Z,;,m,,,_FG,:,Array,[,String,,,9872,],;,_z,:,Int,;,E,,,d_F8____,,,h3Cf53,:,Boolean,;,n,:,h_A00u1_,),{,},},Class,_,{,},<EOF>''',101))

    def test_536(self):
        self.assertTrue(TestLexer.test('''Class _i{Constructor (_0:Array [String ,0x9];_,_,m:String ;_B_j,S9,_:_;b_:Array [Array [Array [Array [Array [Array [Float ,14],4_8],9_9],0X14],0b1000010],062]){Continue ;} }''','''Class,_i,{,Constructor,(,_0,:,Array,[,String,,,0x9,],;,_,,,_,,,m,:,String,;,_B_j,,,S9,,,_,:,_,;,b_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,14,],,,48,],,,99,],,,0X14,],,,0b1000010,],,,062,],),{,Continue,;,},},<EOF>''',101))

    def test_537(self):
        self.assertTrue(TestLexer.test('''Class __L2Jm0_:q8{}Class _{}Class J_:__I{Destructor (){Var _:Int ;} }Class _:__{Val $_,$eJ,_,_:Array [Array [Float ,02],0xD0];}''','''Class,__L2Jm0_,:,q8,{,},Class,_,{,},Class,J_,:,__I,{,Destructor,(,),{,Var,_,:,Int,;,},},Class,_,:,__,{,Val,$_,,,$eJ,,,_,,,_,:,Array,[,Array,[,Float,,,02,],,,0xD0,],;,},<EOF>''',101))

    def test_538(self):
        self.assertTrue(TestLexer.test('''Class jB{}Class F60i:WxmM{Constructor (__:_k){} }Class n_3c{$_f_6C(z,f,___G_,_e,_5,Uf_,y_38__:String ;ik:String ){Continue ;}Constructor (_:_;p,___:String ){Break ;} }''','''Class,jB,{,},Class,F60i,:,WxmM,{,Constructor,(,__,:,_k,),{,},},Class,n_3c,{,$_f_6C,(,z,,,f,,,___G_,,,_e,,,_5,,,Uf_,,,y_38__,:,String,;,ik,:,String,),{,Continue,;,},Constructor,(,_,:,_,;,p,,,___,:,String,),{,Break,;,},},<EOF>''',101))

    def test_539(self):
        self.assertTrue(TestLexer.test('''Class T:js_1892{Var $G:aS;}Class n7:a_{}Class vK_{$3v(_,___5:Int ;_,J_:Array [Array [Array [String ,21],0x28],0X3]){Var _n,_w,h:_;Break ;} }''','''Class,T,:,js_1892,{,Var,$G,:,aS,;,},Class,n7,:,a_,{,},Class,vK_,{,$3v,(,_,,,___5,:,Int,;,_,,,J_,:,Array,[,Array,[,Array,[,String,,,21,],,,0x28,],,,0X3,],),{,Var,_n,,,_w,,,h,:,_,;,Break,;,},},<EOF>''',101))

    def test_540(self):
        self.assertTrue(TestLexer.test('''Class u2w7I:_y{$7_0_(_44D,_:Float ){Break ;}$___u(){} }Class _{}Class __:U{Var $71:String ;Var _H,$g__05:Array [Array [Boolean ,0x3],0b1000010];Val $__:Int ;}''','''Class,u2w7I,:,_y,{,$7_0_,(,_44D,,,_,:,Float,),{,Break,;,},$___u,(,),{,},},Class,_,{,},Class,__,:,U,{,Var,$71,:,String,;,Var,_H,,,$g__05,:,Array,[,Array,[,Boolean,,,0x3,],,,0b1000010,],;,Val,$__,:,Int,;,},<EOF>''',101))

    def test_541(self):
        self.assertTrue(TestLexer.test('''Class x080__:f{}Class _2{Destructor (){} }Class _C:S{}Class b7_{Var $TF_,$84_,_I,D:String ;}Class _:__Y_{Constructor (_,_3:Array [Float ,53];w_:String ){ {Val K,__,x1:Int ;} }}''','''Class,x080__,:,f,{,},Class,_2,{,Destructor,(,),{,},},Class,_C,:,S,{,},Class,b7_,{,Var,$TF_,,,$84_,,,_I,,,D,:,String,;,},Class,_,:,__Y_,{,Constructor,(,_,,,_3,:,Array,[,Float,,,53,],;,w_,:,String,),{,{,Val,K,,,__,,,x1,:,Int,;,},},},<EOF>''',101))

    def test_542(self):
        self.assertTrue(TestLexer.test('''Class _:s{}Class aIL:H{Val $e:Array [String ,0104];}Class H:c{}Class C{}Class f:k_{Constructor (){Break ;}Val $_:r_;}''','''Class,_,:,s,{,},Class,aIL,:,H,{,Val,$e,:,Array,[,String,,,0104,],;,},Class,H,:,c,{,},Class,C,{,},Class,f,:,k_,{,Constructor,(,),{,Break,;,},Val,$_,:,r_,;,},<EOF>''',101))

    def test_543(self):
        self.assertTrue(TestLexer.test('''Class _{Constructor (_C:Array [Array [Array [Array [Array [Float ,3],02],0B10],3],0X24]){}Var h,v:Array [Array [Float ,0x57],25_25_7];}''','''Class,_,{,Constructor,(,_C,:,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,3,],,,02,],,,0B10,],,,3,],,,0X24,],),{,},Var,h,,,v,:,Array,[,Array,[,Float,,,0x57,],,,25257,],;,},<EOF>''',101))

    def test_544(self):
        self.assertTrue(TestLexer.test('''Class z8t4_{g__3_(S:n;_:Array [Array [String ,077],0x3];A,Y:String ;_9D_G,s:Array [String ,0b1000101];_:Array [String ,03];m,_,I,d9,pA3o,n7,_:Array [String ,0x6_E];_:Array [Array [Array [Int ,0X7],01_0_72],1]){} }''','''Class,z8t4_,{,g__3_,(,S,:,n,;,_,:,Array,[,Array,[,String,,,077,],,,0x3,],;,A,,,Y,:,String,;,_9D_G,,,s,:,Array,[,String,,,0b1000101,],;,_,:,Array,[,String,,,03,],;,m,,,_,,,I,,,d9,,,pA3o,,,n7,,,_,:,Array,[,String,,,0x6E,],;,_,:,Array,[,Array,[,Array,[,Int,,,0X7,],,,01072,],,,1,],),{,},},<EOF>''',101))

    def test_545(self):
        self.assertTrue(TestLexer.test('''Class x:Z{}Class f:P__{}Class m5:__{$_x(X,G,pt,_,v,i5,e,udM0,c7,_9_:Array [Array [Array [Array [Array [String ,0B1],0b11_01],03376_76],9],0B1]){} }''','''Class,x,:,Z,{,},Class,f,:,P__,{,},Class,m5,:,__,{,$_x,(,X,,,G,,,pt,,,_,,,v,,,i5,,,e,,,udM0,,,c7,,,_9_,:,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0B1,],,,0b1101,],,,0337676,],,,9,],,,0B1,],),{,},},<EOF>''',101))

    def test_546(self):
        self.assertTrue(TestLexer.test('''Class __5d:i_{Val $8f,$___1,$4,_B:Array [Array [Array [Array [Array [String ,5_726],0B1],01_7_13],0X9],0B1_11];}Class S5:R{}Class s:E{}Class xy:_23{Destructor (){} }''','''Class,__5d,:,i_,{,Val,$8f,,,$___1,,,$4,,,_B,:,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,5726,],,,0B1,],,,01713,],,,0X9,],,,0B111,],;,},Class,S5,:,R,{,},Class,s,:,E,{,},Class,xy,:,_23,{,Destructor,(,),{,},},<EOF>''',101))

    def test_547(self):
        self.assertTrue(TestLexer.test('''Class M{}Class _p850J:_3s{}Class Y{}Class _:_5g0X{Tp(__:Array [Array [Array [Boolean ,81],0B1100010],81];B,_gN:Array [Int ,05];Af_,_:Int ;_4_:q2){Continue ;} }''','''Class,M,{,},Class,_p850J,:,_3s,{,},Class,Y,{,},Class,_,:,_5g0X,{,Tp,(,__,:,Array,[,Array,[,Array,[,Boolean,,,81,],,,0B1100010,],,,81,],;,B,,,_gN,:,Array,[,Int,,,05,],;,Af_,,,_,:,Int,;,_4_,:,q2,),{,Continue,;,},},<EOF>''',101))

    def test_548(self):
        self.assertTrue(TestLexer.test('''Class _:e{Var $9,$YT5:Array [Array [Array [Array [Array [Array [Array [String ,0B10110],0B1],0B10110],0X9],0x88],58],0x4E];}Class H_:bm{}Class y_0i{Constructor (){}Val $_W:Array [Boolean ,58];}''','''Class,_,:,e,{,Var,$9,,,$YT5,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0B10110,],,,0B1,],,,0B10110,],,,0X9,],,,0x88,],,,58,],,,0x4E,],;,},Class,H_,:,bm,{,},Class,y_0i,{,Constructor,(,),{,},Val,$_W,:,Array,[,Boolean,,,58,],;,},<EOF>''',101))

    def test_549(self):
        self.assertTrue(TestLexer.test('''Class i_{$__4(_62,_,y9,l_:_1L;_,_C_:Array [String ,02];_:_8;_:bs;gh:Array [String ,01];J:Array [String ,63_1_04]){}K_o7_(p04_,_5o,_8__:a_;b_,n:Array [String ,0X18]){} }''','''Class,i_,{,$__4,(,_62,,,_,,,y9,,,l_,:,_1L,;,_,,,_C_,:,Array,[,String,,,02,],;,_,:,_8,;,_,:,bs,;,gh,:,Array,[,String,,,01,],;,J,:,Array,[,String,,,63104,],),{,},K_o7_,(,p04_,,,_5o,,,_8__,:,a_,;,b_,,,n,:,Array,[,String,,,0X18,],),{,},},<EOF>''',101))

    def test_550(self):
        self.assertTrue(TestLexer.test('''Class _p744{Destructor (){} }Class V{Var l9:Array [String ,0B1];}Class g_6:_A{}Class _y_:_{Var $q7_:i;}Class _:el5{Var _:I;Var $Q_,$_8,$_:Array [Array [Boolean ,0132],0x16];}''','''Class,_p744,{,Destructor,(,),{,},},Class,V,{,Var,l9,:,Array,[,String,,,0B1,],;,},Class,g_6,:,_A,{,},Class,_y_,:,_,{,Var,$q7_,:,i,;,},Class,_,:,el5,{,Var,_,:,I,;,Var,$Q_,,,$_8,,,$_,:,Array,[,Array,[,Boolean,,,0132,],,,0x16,],;,},<EOF>''',101))

    def test_551(self):
        self.assertTrue(TestLexer.test('''Class N23T{}Class l4S9:__{Val $3,$_:Array [Array [Boolean ,0XC_E],1];}Class __:g_{Val $8:String ;Val _1,$_,_:v_E4l;Val _:String ;}''','''Class,N23T,{,},Class,l4S9,:,__,{,Val,$3,,,$_,:,Array,[,Array,[,Boolean,,,0XCE,],,,1,],;,},Class,__,:,g_,{,Val,$8,:,String,;,Val,_1,,,$_,,,_,:,v_E4l,;,Val,_,:,String,;,},<EOF>''',101))

    def test_552(self):
        self.assertTrue(TestLexer.test('''Class q_{Val $5:String ;Val b:Array [Array [String ,0B1],0x2_6];}Class p8_c1{Var $ZLr5:Array [Array [String ,13],0b11];}''','''Class,q_,{,Val,$5,:,String,;,Val,b,:,Array,[,Array,[,String,,,0B1,],,,0x26,],;,},Class,p8_c1,{,Var,$ZLr5,:,Array,[,Array,[,String,,,13,],,,0b11,],;,},<EOF>''',101))

    def test_553(self):
        self.assertTrue(TestLexer.test('''Class J:_76Q8_{$_V(f,_,_0,__:Int ;wl__3g,T,i4_s,_:Array [Boolean ,0B1_0];_,q6Y_7:Int ;T,_5L71:Array [Array [Float ,054_6_4],81]){} }Class _97{}''','''Class,J,:,_76Q8_,{,$_V,(,f,,,_,,,_0,,,__,:,Int,;,wl__3g,,,T,,,i4_s,,,_,:,Array,[,Boolean,,,0B10,],;,_,,,q6Y_7,:,Int,;,T,,,_5L71,:,Array,[,Array,[,Float,,,05464,],,,81,],),{,},},Class,_97,{,},<EOF>''',101))

    def test_554(self):
        self.assertTrue(TestLexer.test('''Class _:F{}Class j{Constructor (_j_:Int ;V:Boolean ;g,_40_y_:ek6;W,Zv_:Array [Array [Int ,24],42]){}Val $1N,$_:Array [Boolean ,42];}''','''Class,_,:,F,{,},Class,j,{,Constructor,(,_j_,:,Int,;,V,:,Boolean,;,g,,,_40_y_,:,ek6,;,W,,,Zv_,:,Array,[,Array,[,Int,,,24,],,,42,],),{,},Val,$1N,,,$_,:,Array,[,Boolean,,,42,],;,},<EOF>''',101))

    def test_555(self):
        self.assertTrue(TestLexer.test('''Class Rs:Oy{Destructor (){} }Class XB_{}Class N:_B9__{Val $__,$74W:Boolean ;}Class G_TI:__{Constructor (__:String ;_,E,__,G0:Array [Array [Float ,0x4],433];L:Array [Boolean ,01_1_1];_Px,_:Array [Array [Array [Array [Float ,0b1],78],0B1],0126]){} }Class L{}Class __:s8{}''','''Class,Rs,:,Oy,{,Destructor,(,),{,},},Class,XB_,{,},Class,N,:,_B9__,{,Val,$__,,,$74W,:,Boolean,;,},Class,G_TI,:,__,{,Constructor,(,__,:,String,;,_,,,E,,,__,,,G0,:,Array,[,Array,[,Float,,,0x4,],,,433,],;,L,:,Array,[,Boolean,,,0111,],;,_Px,,,_,:,Array,[,Array,[,Array,[,Array,[,Float,,,0b1,],,,78,],,,0B1,],,,0126,],),{,},},Class,L,{,},Class,__,:,s8,{,},<EOF>''',101))

    def test_556(self):
        self.assertTrue(TestLexer.test('''Class _:X{}Class K:A{Destructor (){}Constructor (y,_6_8,_,A__0:Array [Int ,5];_G,_:_4L){} }Class _:G7{}Class _t{Var i,_0,__:Int ;}Class F{Constructor (_a:Boolean ){Val _:String ;_::$7._.Er.Y_._().h_();} }''','''Class,_,:,X,{,},Class,K,:,A,{,Destructor,(,),{,},Constructor,(,y,,,_6_8,,,_,,,A__0,:,Array,[,Int,,,5,],;,_G,,,_,:,_4L,),{,},},Class,_,:,G7,{,},Class,_t,{,Var,i,,,_0,,,__,:,Int,;,},Class,F,{,Constructor,(,_a,:,Boolean,),{,Val,_,:,String,;,_,::,$7,.,_,.,Er,.,Y_,.,_,(,),.,h_,(,),;,},},<EOF>''',101))

    def test_557(self):
        self.assertTrue(TestLexer.test('''Class a_{Constructor (_,__i8_,_U_9Q:String ){}Var $_,$2E_,$bYl:Array [Array [Array [String ,3_07_5_9],77],7];}''','''Class,a_,{,Constructor,(,_,,,__i8_,,,_U_9Q,:,String,),{,},Var,$_,,,$2E_,,,$bYl,:,Array,[,Array,[,Array,[,String,,,30759,],,,77,],,,7,],;,},<EOF>''',101))

    def test_558(self):
        self.assertTrue(TestLexer.test('''Class _Y0_7:_{Var $9_,_315_u9,$80Ts,_l:Array [Array [Boolean ,0B1],0x38];$3(b6,A_,stc,B:Array [String ,36]){}Val _B____:Int ;Val __:x_CsP;Destructor (){} }Class _{}''','''Class,_Y0_7,:,_,{,Var,$9_,,,_315_u9,,,$80Ts,,,_l,:,Array,[,Array,[,Boolean,,,0B1,],,,0x38,],;,$3,(,b6,,,A_,,,stc,,,B,:,Array,[,String,,,36,],),{,},Val,_B____,:,Int,;,Val,__,:,x_CsP,;,Destructor,(,),{,},},Class,_,{,},<EOF>''',101))

    def test_559(self):
        self.assertTrue(TestLexer.test('''Class C:_{Val f,_,__j:Array [Int ,5];Destructor (){} }Class _:Vq{}Class l{}Class B:r{Val g,___:Boolean ;Val ulV__aj,nu8:c4_;}Class _8__1E_n70_{}''','''Class,C,:,_,{,Val,f,,,_,,,__j,:,Array,[,Int,,,5,],;,Destructor,(,),{,},},Class,_,:,Vq,{,},Class,l,{,},Class,B,:,r,{,Val,g,,,___,:,Boolean,;,Val,ulV__aj,,,nu8,:,c4_,;,},Class,_8__1E_n70_,{,},<EOF>''',101))

    def test_560(self):
        self.assertTrue(TestLexer.test('''Class _37{}Class aT{Constructor (__,_,P:Boolean ;L_,x,_6C:Boolean ){Break ;}$1(_,_,_l:Array [String ,1];_:Array [Boolean ,0x1E]){} }''','''Class,_37,{,},Class,aT,{,Constructor,(,__,,,_,,,P,:,Boolean,;,L_,,,x,,,_6C,:,Boolean,),{,Break,;,},$1,(,_,,,_,,,_l,:,Array,[,String,,,1,],;,_,:,Array,[,Boolean,,,0x1E,],),{,},},<EOF>''',101))

    def test_561(self):
        self.assertTrue(TestLexer.test('''Class _{Val _b8:Array [Array [Array [Float ,0X2E],0B1100000],0x56];Constructor (l6Q,y,__1Q_,_:Boolean ;_:U){} }Class o71{}''','''Class,_,{,Val,_b8,:,Array,[,Array,[,Array,[,Float,,,0X2E,],,,0B1100000,],,,0x56,],;,Constructor,(,l6Q,,,y,,,__1Q_,,,_,:,Boolean,;,_,:,U,),{,},},Class,o71,{,},<EOF>''',101))

    def test_562(self):
        self.assertTrue(TestLexer.test('''Class k:_{F(Q8_,B:Boolean ;S,_6_,d:_;Sg7_6D:Array [Array [Array [Array [Array [Boolean ,050],85],0x10],0x55],03_0_6];_0,_WI,_,__,W,X__G1:Array [Array [Boolean ,9],037];_,K_:X6;E,S,E,_1F:Array [Array [Array [Float ,0x55],0X9_D],0b1000101]){} }Class KW{}''','''Class,k,:,_,{,F,(,Q8_,,,B,:,Boolean,;,S,,,_6_,,,d,:,_,;,Sg7_6D,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,050,],,,85,],,,0x10,],,,0x55,],,,0306,],;,_0,,,_WI,,,_,,,__,,,W,,,X__G1,:,Array,[,Array,[,Boolean,,,9,],,,037,],;,_,,,K_,:,X6,;,E,,,S,,,E,,,_1F,:,Array,[,Array,[,Array,[,Float,,,0x55,],,,0X9D,],,,0b1000101,],),{,},},Class,KW,{,},<EOF>''',101))

    def test_563(self):
        self.assertTrue(TestLexer.test('''Class _{}Class vF:_e{}Class rbzRRq91:R0_0{Constructor (_9n8S,c__:Array [Boolean ,0X3_A_7B];_:Array [Array [String ,0B111011],0B1];C,__,M,_i:Float ;F_:Array [Array [Array [Array [Array [Boolean ,67],67],0b1101],0X43],67]){} }Class _{}''','''Class,_,{,},Class,vF,:,_e,{,},Class,rbzRRq91,:,R0_0,{,Constructor,(,_9n8S,,,c__,:,Array,[,Boolean,,,0X3A7B,],;,_,:,Array,[,Array,[,String,,,0B111011,],,,0B1,],;,C,,,__,,,M,,,_i,:,Float,;,F_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,67,],,,67,],,,0b1101,],,,0X43,],,,67,],),{,},},Class,_,{,},<EOF>''',101))

    def test_564(self):
        self.assertTrue(TestLexer.test('''Class M{Constructor (a:Boolean ){Continue ;} }Class ACh{Val $_,$1,w__,e24,__:Array [Array [Array [Array [Float ,0XE],29],29],0XDE];}''','''Class,M,{,Constructor,(,a,:,Boolean,),{,Continue,;,},},Class,ACh,{,Val,$_,,,$1,,,w__,,,e24,,,__,:,Array,[,Array,[,Array,[,Array,[,Float,,,0XE,],,,29,],,,29,],,,0XDE,],;,},<EOF>''',101))

    def test_565(self):
        self.assertTrue(TestLexer.test('''Class _5{Destructor (){}Var $38:Array [Array [String ,9_88],0X2];Var $36,$_,ge:Array [Array [Boolean ,0B10_1],0B1010000];}''','''Class,_5,{,Destructor,(,),{,},Var,$38,:,Array,[,Array,[,String,,,988,],,,0X2,],;,Var,$36,,,$_,,,ge,:,Array,[,Array,[,Boolean,,,0B101,],,,0B1010000,],;,},<EOF>''',101))

    def test_566(self):
        self.assertTrue(TestLexer.test('''Class _:T{Constructor (ha5yn_:Array [Int ,72];__,P4:Array [Array [Array [Int ,0b1],0B10_1_1_1],010]){Continue ;}Val _,$c,PM1:Array [String ,0xF_3F];Val H:Array [Array [String ,72],0b1011100];}''','''Class,_,:,T,{,Constructor,(,ha5yn_,:,Array,[,Int,,,72,],;,__,,,P4,:,Array,[,Array,[,Array,[,Int,,,0b1,],,,0B10111,],,,010,],),{,Continue,;,},Val,_,,,$c,,,PM1,:,Array,[,String,,,0xF3F,],;,Val,H,:,Array,[,Array,[,String,,,72,],,,0b1011100,],;,},<EOF>''',101))

    def test_567(self):
        self.assertTrue(TestLexer.test('''Class yZp428p{_(){} }Class A:C{}Class _:_L{}Class c_:_{Var $_:Array [String ,021_524];}Class pj:m{}Class R_s_{}Class o:S{}''','''Class,yZp428p,{,_,(,),{,},},Class,A,:,C,{,},Class,_,:,_L,{,},Class,c_,:,_,{,Var,$_,:,Array,[,String,,,021524,],;,},Class,pj,:,m,{,},Class,R_s_,{,},Class,o,:,S,{,},<EOF>''',101))

    def test_568(self):
        self.assertTrue(TestLexer.test('''Class _k{S1(X,_,SmH,_:Array [String ,0b1]){Break ;Break ;}Val $5XdD,C__,$PI:_N;}Class V45lw_{Destructor (){}Val Om:Array [Float ,55];Val c:Boolean ;}''','''Class,_k,{,S1,(,X,,,_,,,SmH,,,_,:,Array,[,String,,,0b1,],),{,Break,;,Break,;,},Val,$5XdD,,,C__,,,$PI,:,_N,;,},Class,V45lw_,{,Destructor,(,),{,},Val,Om,:,Array,[,Float,,,55,],;,Val,c,:,Boolean,;,},<EOF>''',101))

    def test_569(self):
        self.assertTrue(TestLexer.test('''Class _:_9{$42v8_(s:Array [Array [Array [Float ,0X43],0b111100],72]){} }Class V:__{}Class __{_____4(){_::$0_2_8q_();Break ;Continue ;} }Class Q4{Var $5_:P0;}Class _M8_{Var eb,$9,$9_,$A__,HV5:Float ;Constructor (_,Z:Float ){} }''','''Class,_,:,_9,{,$42v8_,(,s,:,Array,[,Array,[,Array,[,Float,,,0X43,],,,0b111100,],,,72,],),{,},},Class,V,:,__,{,},Class,__,{,_____4,(,),{,_,::,$0_2_8q_,(,),;,Break,;,Continue,;,},},Class,Q4,{,Var,$5_,:,P0,;,},Class,_M8_,{,Var,eb,,,$9,,,$9_,,,$A__,,,HV5,:,Float,;,Constructor,(,_,,,Z,:,Float,),{,},},<EOF>''',101))

    def test_570(self):
        self.assertTrue(TestLexer.test('''Class m:_r__{}Class _7__:_{}Class _:_Y{}Class A{}Class _G:__5a_8{Constructor (_:_){}f1_(y:K){} }Class _{}Class d{}''','''Class,m,:,_r__,{,},Class,_7__,:,_,{,},Class,_,:,_Y,{,},Class,A,{,},Class,_G,:,__5a_8,{,Constructor,(,_,:,_,),{,},f1_,(,y,:,K,),{,},},Class,_,{,},Class,d,{,},<EOF>''',101))

    def test_571(self):
        self.assertTrue(TestLexer.test('''Class s{}Class L{n(_,_,CC:Boolean ;_,E:Array [Array [Boolean ,0X53],0132]){Continue ;}$1(){Break ;} }Class c:_{Constructor (U,R,L74,JH3,C:_5k){}Destructor (){Break ;} }''','''Class,s,{,},Class,L,{,n,(,_,,,_,,,CC,:,Boolean,;,_,,,E,:,Array,[,Array,[,Boolean,,,0X53,],,,0132,],),{,Continue,;,},$1,(,),{,Break,;,},},Class,c,:,_,{,Constructor,(,U,,,R,,,L74,,,JH3,,,C,:,_5k,),{,},Destructor,(,),{,Break,;,},},<EOF>''',101))

    def test_572(self):
        self.assertTrue(TestLexer.test('''Class _{}Class _{Constructor (t,C2i,V,m,_630:Array [Array [Array [Array [Int ,0X49],0b10101],026],0B10110];__,_:Boolean ;__,G,r:Array [String ,8_7];b:h;_z:Array [Array [Array [Boolean ,0b10101],07_1_0],5_48];J:V){}$_G(){Break ;} }Class _62_{}Class _{}''','''Class,_,{,},Class,_,{,Constructor,(,t,,,C2i,,,V,,,m,,,_630,:,Array,[,Array,[,Array,[,Array,[,Int,,,0X49,],,,0b10101,],,,026,],,,0B10110,],;,__,,,_,:,Boolean,;,__,,,G,,,r,:,Array,[,String,,,87,],;,b,:,h,;,_z,:,Array,[,Array,[,Array,[,Boolean,,,0b10101,],,,0710,],,,548,],;,J,:,V,),{,},$_G,(,),{,Break,;,},},Class,_62_,{,},Class,_,{,},<EOF>''',101))

    def test_573(self):
        self.assertTrue(TestLexer.test('''Class _6_{}Class kn_:WS{$B(){} }Class _:_5{Var I_3c,jb:Array [Array [Array [Float ,0B100100],7],03];Var $_t,$5,$8eP:m_2;}Class Q{}''','''Class,_6_,{,},Class,kn_,:,WS,{,$B,(,),{,},},Class,_,:,_5,{,Var,I_3c,,,jb,:,Array,[,Array,[,Array,[,Float,,,0B100100,],,,7,],,,03,],;,Var,$_t,,,$5,,,$8eP,:,m_2,;,},Class,Q,{,},<EOF>''',101))

    def test_574(self):
        self.assertTrue(TestLexer.test('''Class _Ni{Destructor (){}_(_:__){} }Class _:B{}Class _:_4{}Class _:y{Var P:U;$6d3(){Var _C0Q:Array [Int ,0x4];}Var $g4,_o3e:C_;}Class _4:_{Var _,$Va:Array [String ,0X1];}''','''Class,_Ni,{,Destructor,(,),{,},_,(,_,:,__,),{,},},Class,_,:,B,{,},Class,_,:,_4,{,},Class,_,:,y,{,Var,P,:,U,;,$6d3,(,),{,Var,_C0Q,:,Array,[,Int,,,0x4,],;,},Var,$g4,,,_o3e,:,C_,;,},Class,_4,:,_,{,Var,_,,,$Va,:,Array,[,String,,,0X1,],;,},<EOF>''',101))

    def test_575(self):
        self.assertTrue(TestLexer.test('''Class N7851f{Var p_3:_;Val $96,b,$N,N,M:String ;$_32F61(h,Hc,U:Y;p,_,fm,N__:Array [Array [Float ,0b1_1],0b1111];_1,It_Q,_,O:Int ;_DD:_;_4hX:String ;_,e:_a8_;__M:Array [Float ,07]){Continue ;Continue ;}Val $_Eqt,_,$1_v_P:Boolean ;Var _d4:_;}''','''Class,N7851f,{,Var,p_3,:,_,;,Val,$96,,,b,,,$N,,,N,,,M,:,String,;,$_32F61,(,h,,,Hc,,,U,:,Y,;,p,,,_,,,fm,,,N__,:,Array,[,Array,[,Float,,,0b11,],,,0b1111,],;,_1,,,It_Q,,,_,,,O,:,Int,;,_DD,:,_,;,_4hX,:,String,;,_,,,e,:,_a8_,;,__M,:,Array,[,Float,,,07,],),{,Continue,;,Continue,;,},Val,$_Eqt,,,_,,,$1_v_P,:,Boolean,;,Var,_d4,:,_,;,},<EOF>''',101))

    def test_576(self):
        self.assertTrue(TestLexer.test('''Class Zb{_4__1(_H1o_P:Array [Array [Array [Int ,6_6],0x7_0],0xD]){} }Class _8{Destructor (){ {Continue ;} }Destructor (){Var _,_O9U:z;}Var $_84:Array [Boolean ,0X6_0];Var $4J9___,uV1_,$L:Array [Array [Array [String ,0B101111],0b11_0],70];__(){Break ;} }''','''Class,Zb,{,_4__1,(,_H1o_P,:,Array,[,Array,[,Array,[,Int,,,66,],,,0x70,],,,0xD,],),{,},},Class,_8,{,Destructor,(,),{,{,Continue,;,},},Destructor,(,),{,Var,_,,,_O9U,:,z,;,},Var,$_84,:,Array,[,Boolean,,,0X60,],;,Var,$4J9___,,,uV1_,,,$L,:,Array,[,Array,[,Array,[,String,,,0B101111,],,,0b110,],,,70,],;,__,(,),{,Break,;,},},<EOF>''',101))

    def test_577(self):
        self.assertTrue(TestLexer.test('''Class _{Destructor (){Break ;Break ;}w(){}Var $C7:Float ;Val k:D_;Val _2W_X_,_6_2,Q,$0i,G42_,__:Array [Array [Int ,0x54],42];}Class ___:_sv{}''','''Class,_,{,Destructor,(,),{,Break,;,Break,;,},w,(,),{,},Var,$C7,:,Float,;,Val,k,:,D_,;,Val,_2W_X_,,,_6_2,,,Q,,,$0i,,,G42_,,,__,:,Array,[,Array,[,Int,,,0x54,],,,42,],;,},Class,___,:,_sv,{,},<EOF>''',101))

    def test_578(self):
        self.assertTrue(TestLexer.test('''Class KT{}Class d{}Class T:D4{}Class _{}Class _:_Q_{$03(O:_;_,eS,C_:Array [Boolean ,0B1];yl,_50_5:Int ){}Destructor (){Return ;} }''','''Class,KT,{,},Class,d,{,},Class,T,:,D4,{,},Class,_,{,},Class,_,:,_Q_,{,$03,(,O,:,_,;,_,,,eS,,,C_,:,Array,[,Boolean,,,0B1,],;,yl,,,_50_5,:,Int,),{,},Destructor,(,),{,Return,;,},},<EOF>''',101))

    def test_579(self):
        self.assertTrue(TestLexer.test('''Class _A{dz(_,_:Int ;e__,_:Array [Array [Array [Float ,87],07],041]){Val ij,_:Array [Array [Array [Array [String ,3],0X4F],0b111110],02];H9::$3();Break ;Return ;Continue ;} }Class h6{Constructor (Q6,__56:Array [Array [Boolean ,0X1_7B8_6],0b10];_k4,___:V;k:Tf){Return ;} }''','''Class,_A,{,dz,(,_,,,_,:,Int,;,e__,,,_,:,Array,[,Array,[,Array,[,Float,,,87,],,,07,],,,041,],),{,Val,ij,,,_,:,Array,[,Array,[,Array,[,Array,[,String,,,3,],,,0X4F,],,,0b111110,],,,02,],;,H9,::,$3,(,),;,Break,;,Return,;,Continue,;,},},Class,h6,{,Constructor,(,Q6,,,__56,:,Array,[,Array,[,Boolean,,,0X17B86,],,,0b10,],;,_k4,,,___,:,V,;,k,:,Tf,),{,Return,;,},},<EOF>''',101))

    def test_580(self):
        self.assertTrue(TestLexer.test('''Class __{Constructor (_0_:Array [Array [Array [Array [Array [Float ,0X61],0B110010],6],0x50],36]){Var P,_,l:Array [Array [Int ,5],36];}Destructor (){}$_(te:q03_8){} }''','''Class,__,{,Constructor,(,_0_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0X61,],,,0B110010,],,,6,],,,0x50,],,,36,],),{,Var,P,,,_,,,l,:,Array,[,Array,[,Int,,,5,],,,36,],;,},Destructor,(,),{,},$_,(,te,:,q03_8,),{,},},<EOF>''',101))

    def test_581(self):
        self.assertTrue(TestLexer.test('''Class _{Var $1:String ;Destructor (){}Var $tkD5:Array [Array [Array [Array [Array [Array [Array [Float ,0B1_0_0],0114],0b1],9_3],0b110101],45],94];}''','''Class,_,{,Var,$1,:,String,;,Destructor,(,),{,},Var,$tkD5,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0B100,],,,0114,],,,0b1,],,,93,],,,0b110101,],,,45,],,,94,],;,},<EOF>''',101))

    def test_582(self):
        self.assertTrue(TestLexer.test('''Class _{}Class _{Constructor (){}Var _,uL62:String ;}Class _:_dm{Constructor (_:Array [Float ,4];_o,T:Array [Array [Boolean ,74],3_1];V,B:_;R_8w8:Array [String ,0X5];___m:_){}Var $D:_;}Class XI{}''','''Class,_,{,},Class,_,{,Constructor,(,),{,},Var,_,,,uL62,:,String,;,},Class,_,:,_dm,{,Constructor,(,_,:,Array,[,Float,,,4,],;,_o,,,T,:,Array,[,Array,[,Boolean,,,74,],,,31,],;,V,,,B,:,_,;,R_8w8,:,Array,[,String,,,0X5,],;,___m,:,_,),{,},Var,$D,:,_,;,},Class,XI,{,},<EOF>''',101))

    def test_583(self):
        self.assertTrue(TestLexer.test('''Class d:_{}Class xL:__{}Class O3{Destructor (){}Destructor (){}Var _,$2,k,$v,$Zs:Array [Int ,0b1];Destructor (){}Val J7:Array [Array [Array [Array [Array [Array [Array [String ,06],0b1],0b1],39],0X5B],026],0B100001];}''','''Class,d,:,_,{,},Class,xL,:,__,{,},Class,O3,{,Destructor,(,),{,},Destructor,(,),{,},Var,_,,,$2,,,k,,,$v,,,$Zs,:,Array,[,Int,,,0b1,],;,Destructor,(,),{,},Val,J7,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,06,],,,0b1,],,,0b1,],,,39,],,,0X5B,],,,026,],,,0B100001,],;,},<EOF>''',101))

    def test_584(self):
        self.assertTrue(TestLexer.test('''Class _{Constructor (sLr_:B_;U_3,c7,n,_r,e,m,S,n_,r:Int ;_Y,f_:String ;k4,Z8,Q__5:Array [Int ,05_11];_:Array [Array [Array [Float ,8],0b110001],0B1000101]){} }''','''Class,_,{,Constructor,(,sLr_,:,B_,;,U_3,,,c7,,,n,,,_r,,,e,,,m,,,S,,,n_,,,r,:,Int,;,_Y,,,f_,:,String,;,k4,,,Z8,,,Q__5,:,Array,[,Int,,,0511,],;,_,:,Array,[,Array,[,Array,[,Float,,,8,],,,0b110001,],,,0B1000101,],),{,},},<EOF>''',101))

    def test_585(self):
        self.assertTrue(TestLexer.test('''Class V_{}Class _:K_{Val _D:Array [Array [Boolean ,0X14],0b101];_(V2,aGL,X:Array [Array [Array [Array [Array [Array [Boolean ,94],045],0X14],045],0B1_0],0x30];__,_,a7,_:Array [Array [Boolean ,5],0x30]){ {}Val Tv,_R,b,H_,_:L3x;{} }Val __,$9_:String ;b_Z(B__,W,zT__:Int ){}Destructor (){}Destructor (){}Destructor (){} }''','''Class,V_,{,},Class,_,:,K_,{,Val,_D,:,Array,[,Array,[,Boolean,,,0X14,],,,0b101,],;,_,(,V2,,,aGL,,,X,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,94,],,,045,],,,0X14,],,,045,],,,0B10,],,,0x30,],;,__,,,_,,,a7,,,_,:,Array,[,Array,[,Boolean,,,5,],,,0x30,],),{,{,},Val,Tv,,,_R,,,b,,,H_,,,_,:,L3x,;,{,},},Val,__,,,$9_,:,String,;,b_Z,(,B__,,,W,,,zT__,:,Int,),{,},Destructor,(,),{,},Destructor,(,),{,},Destructor,(,),{,},},<EOF>''',101))

    def test_586(self):
        self.assertTrue(TestLexer.test('''Class __{Val xn,_2:_;}Class m___8Z_{}Class j:T{}Class h_9{Constructor (_:Array [Array [Boolean ,0X33],0b1];Y:Array [Float ,0X9]){Val _,_6:_D;} }Class cV:_{Val Bvo,j,n_:_;Var _:Array [Boolean ,0XC];H_(_,HSVg4:Array [Float ,03];_,As_:Array [Boolean ,0B1001100]){} }''','''Class,__,{,Val,xn,,,_2,:,_,;,},Class,m___8Z_,{,},Class,j,:,T,{,},Class,h_9,{,Constructor,(,_,:,Array,[,Array,[,Boolean,,,0X33,],,,0b1,],;,Y,:,Array,[,Float,,,0X9,],),{,Val,_,,,_6,:,_D,;,},},Class,cV,:,_,{,Val,Bvo,,,j,,,n_,:,_,;,Var,_,:,Array,[,Boolean,,,0XC,],;,H_,(,_,,,HSVg4,:,Array,[,Float,,,03,],;,_,,,As_,:,Array,[,Boolean,,,0B1001100,],),{,},},<EOF>''',101))

    def test_587(self):
        self.assertTrue(TestLexer.test('''Class _8_:Y9r{Destructor (){}Destructor (){Break ;}Var $__,_,$_,_,$MV___6N4Q,_l,$_,$q,b,$__:su2_;}Class kl{}''','''Class,_8_,:,Y9r,{,Destructor,(,),{,},Destructor,(,),{,Break,;,},Var,$__,,,_,,,$_,,,_,,,$MV___6N4Q,,,_l,,,$_,,,$q,,,b,,,$__,:,su2_,;,},Class,kl,{,},<EOF>''',101))

    def test_588(self):
        self.assertTrue(TestLexer.test('''Class _6Mv18__:_2{Val _,$_:Array [Int ,03];}Class D4:N{Val J:Array [Float ,179];Val _:Array [Array [Array [Boolean ,044],0B1],03];}Class _5_:M{}''','''Class,_6Mv18__,:,_2,{,Val,_,,,$_,:,Array,[,Int,,,03,],;,},Class,D4,:,N,{,Val,J,:,Array,[,Float,,,179,],;,Val,_,:,Array,[,Array,[,Array,[,Boolean,,,044,],,,0B1,],,,03,],;,},Class,_5_,:,M,{,},<EOF>''',101))

    def test_589(self):
        self.assertTrue(TestLexer.test('''Class _{Fv(_:Array [Int ,037];__9,j:Array [Array [Array [Array [Array [Array [String ,0x40],0B1_1_1],4],57],0b1],0B11100];_F:Array [Array [Array [Array [Boolean ,6_7_99_7],57],0b1011],05_5]){Var _73_:Z;}Destructor (){ {}d::$04()._()._e0_();} }''','''Class,_,{,Fv,(,_,:,Array,[,Int,,,037,],;,__9,,,j,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0x40,],,,0B111,],,,4,],,,57,],,,0b1,],,,0B11100,],;,_F,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,67997,],,,57,],,,0b1011,],,,055,],),{,Var,_73_,:,Z,;,},Destructor,(,),{,{,},d,::,$04,(,),.,_,(,),.,_e0_,(,),;,},},<EOF>''',101))

    def test_590(self):
        self.assertTrue(TestLexer.test('''Class _8:p4861_C{Destructor (){}___(E01,V47,Z,_4,_:String ;P_,e__j_k_,yc:Array [Array [Int ,0B110011],31]){}Var $5:T_9q;}''','''Class,_8,:,p4861_C,{,Destructor,(,),{,},___,(,E01,,,V47,,,Z,,,_4,,,_,:,String,;,P_,,,e__j_k_,,,yc,:,Array,[,Array,[,Int,,,0B110011,],,,31,],),{,},Var,$5,:,T_9q,;,},<EOF>''',101))

    def test_591(self):
        self.assertTrue(TestLexer.test('''Class b1_{}Class w{}Class _:r{}Class T:W{__0(C,_:Array [Array [Boolean ,2_7],0X40];Nb__,bk,_:Array [Int ,92]){} }''','''Class,b1_,{,},Class,w,{,},Class,_,:,r,{,},Class,T,:,W,{,__0,(,C,,,_,:,Array,[,Array,[,Boolean,,,27,],,,0X40,],;,Nb__,,,bk,,,_,:,Array,[,Int,,,92,],),{,},},<EOF>''',101))

    def test_592(self):
        self.assertTrue(TestLexer.test('''Class _O0_S__D_:t1_8_{Destructor (){}Destructor (){}K8(){Break ;} }Class l{Var _6,$R:Boolean ;}Class S:_{}Class Q{}''','''Class,_O0_S__D_,:,t1_8_,{,Destructor,(,),{,},Destructor,(,),{,},K8,(,),{,Break,;,},},Class,l,{,Var,_6,,,$R,:,Boolean,;,},Class,S,:,_,{,},Class,Q,{,},<EOF>''',101))

    def test_593(self):
        self.assertTrue(TestLexer.test('''Class S94A{}Class _O{}Class _V{$_2s(n,_cSA7_6:_1F_;c:Int ){Return ;}_K(B,_:j__){ {} }Constructor (){Return ;} }''','''Class,S94A,{,},Class,_O,{,},Class,_V,{,$_2s,(,n,,,_cSA7_6,:,_1F_,;,c,:,Int,),{,Return,;,},_K,(,B,,,_,:,j__,),{,{,},},Constructor,(,),{,Return,;,},},<EOF>''',101))

    def test_594(self):
        self.assertTrue(TestLexer.test('''Class VA{$_(g,_,_:X_;_:_;k:AW_d;_:Array [String ,014];x,_:Array [Array [String ,0B10001],7_8];_,_tM1_,_,_34,s_N,_:__;K7:Array [String ,0x1]){} }Class ___{}''','''Class,VA,{,$_,(,g,,,_,,,_,:,X_,;,_,:,_,;,k,:,AW_d,;,_,:,Array,[,String,,,014,],;,x,,,_,:,Array,[,Array,[,String,,,0B10001,],,,78,],;,_,,,_tM1_,,,_,,,_34,,,s_N,,,_,:,__,;,K7,:,Array,[,String,,,0x1,],),{,},},Class,___,{,},<EOF>''',101))

    def test_595(self):
        self.assertTrue(TestLexer.test('''Class _B{Constructor (_,_:__W){Val A,_,u:Int ;}Destructor (){} }Class __:_{Destructor (){}$e(){Var O07,s1:Array [String ,0xA80];}Val O__:Int ;}Class _:_liU{Constructor (_:Boolean ){Break ;}Val __0:Array [Array [Array [Array [Array [String ,07],0x17_5],8],0B111111],4_6];}''','''Class,_B,{,Constructor,(,_,,,_,:,__W,),{,Val,A,,,_,,,u,:,Int,;,},Destructor,(,),{,},},Class,__,:,_,{,Destructor,(,),{,},$e,(,),{,Var,O07,,,s1,:,Array,[,String,,,0xA80,],;,},Val,O__,:,Int,;,},Class,_,:,_liU,{,Constructor,(,_,:,Boolean,),{,Break,;,},Val,__0,:,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,07,],,,0x175,],,,8,],,,0B111111,],,,46,],;,},<EOF>''',101))

    def test_596(self):
        self.assertTrue(TestLexer.test('''Class Z{Val _U:Array [Array [Array [Array [Array [Array [Float ,0X1_1F],8_6],0xF],042_50_3],0b1110],46];Var $U_:Array [Float ,9];}''','''Class,Z,{,Val,_U,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0X11F,],,,86,],,,0xF,],,,042503,],,,0b1110,],,,46,],;,Var,$U_,:,Array,[,Float,,,9,],;,},<EOF>''',101))

    def test_597(self):
        self.assertTrue(TestLexer.test('''Class __{Destructor (){}Constructor (a:Array [Boolean ,0B1];_,_O9G:Boolean ;_7:Boolean ){Return ;}va(){} }Class ycj:aH{}''','''Class,__,{,Destructor,(,),{,},Constructor,(,a,:,Array,[,Boolean,,,0B1,],;,_,,,_O9G,:,Boolean,;,_7,:,Boolean,),{,Return,;,},va,(,),{,},},Class,ycj,:,aH,{,},<EOF>''',101))

    def test_598(self):
        self.assertTrue(TestLexer.test('''Class _{Constructor (_,a:Int ;V3L:Array [Array [Array [Array [Array [Array [Array [Array [String ,0X37],85],0xC],0b1011001],0B1],0B1],0113],0b11_0]){Val G,_,_:Boolean ;Continue ;} }''','''Class,_,{,Constructor,(,_,,,a,:,Int,;,V3L,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0X37,],,,85,],,,0xC,],,,0b1011001,],,,0B1,],,,0B1,],,,0113,],,,0b110,],),{,Val,G,,,_,,,_,:,Boolean,;,Continue,;,},},<EOF>''',101))

    def test_599(self):
        self.assertTrue(TestLexer.test('''Class _:q{Val $0,y:C;f1(_,_U,y:Int ;u_gP,a_:Float ;_EP,mV_,D7:Array [Int ,0b10011];_3,_:String ;d:Array [Array [Int ,06],0xE9]){} }''','''Class,_,:,q,{,Val,$0,,,y,:,C,;,f1,(,_,,,_U,,,y,:,Int,;,u_gP,,,a_,:,Float,;,_EP,,,mV_,,,D7,:,Array,[,Int,,,0b10011,],;,_3,,,_,:,String,;,d,:,Array,[,Array,[,Int,,,06,],,,0xE9,],),{,},},<EOF>''',101))

    def test_600(self):
        self.assertTrue(TestLexer.test('''Class l{$6(Iq_:Float ){}Var e,$m_7W,$052d__,_:Boolean ;$4(s__:Int ;q:v;hxM:_;_29_rK_c__,O_,_2,_,_,U:_q___){} }''','''Class,l,{,$6,(,Iq_,:,Float,),{,},Var,e,,,$m_7W,,,$052d__,,,_,:,Boolean,;,$4,(,s__,:,Int,;,q,:,v,;,hxM,:,_,;,_29_rK_c__,,,O_,,,_2,,,_,,,_,,,U,:,_q___,),{,},},<EOF>''',101))

    def test_601(self):
        self.assertTrue(TestLexer.test('''Class q{B(T,S:Array [String ,035];X0fY:Boolean ;_:Array [Boolean ,077];N__X4:Array [String ,5];_:Array [Array [Array [Array [Int ,0B1],0B110000],77],77]){}Var _,$U06,$1:Array [Array [Array [Array [String ,117],0b1],27_2],0b1010011];A29tH__(){Break ;} }''','''Class,q,{,B,(,T,,,S,:,Array,[,String,,,035,],;,X0fY,:,Boolean,;,_,:,Array,[,Boolean,,,077,],;,N__X4,:,Array,[,String,,,5,],;,_,:,Array,[,Array,[,Array,[,Array,[,Int,,,0B1,],,,0B110000,],,,77,],,,77,],),{,},Var,_,,,$U06,,,$1,:,Array,[,Array,[,Array,[,Array,[,String,,,117,],,,0b1,],,,272,],,,0b1010011,],;,A29tH__,(,),{,Break,;,},},<EOF>''',101))

    def test_602(self):
        self.assertTrue(TestLexer.test('''Class E:_{}Class I5g{Val k0__:Float ;}Class ___Q{}Class Z_{Constructor (r,_:Int ;R,_:Array [Boolean ,6];t6_c_,_t,E26_Er_0,M:T){Continue ;}Val B,$u,$6,_M,A:Array [Array [Array [Int ,0x8],0b110000],04];}''','''Class,E,:,_,{,},Class,I5g,{,Val,k0__,:,Float,;,},Class,___Q,{,},Class,Z_,{,Constructor,(,r,,,_,:,Int,;,R,,,_,:,Array,[,Boolean,,,6,],;,t6_c_,,,_t,,,E26_Er_0,,,M,:,T,),{,Continue,;,},Val,B,,,$u,,,$6,,,_M,,,A,:,Array,[,Array,[,Array,[,Int,,,0x8,],,,0b110000,],,,04,],;,},<EOF>''',101))

    def test_603(self):
        self.assertTrue(TestLexer.test('''Class T{}Class e:q8{Destructor (){}Var K,C,$_7mU,$_D:_9;Constructor (){ {Break ;}{} }Constructor (){}Val _,Z_,d8:_a;}''','''Class,T,{,},Class,e,:,q8,{,Destructor,(,),{,},Var,K,,,C,,,$_7mU,,,$_D,:,_9,;,Constructor,(,),{,{,Break,;,},{,},},Constructor,(,),{,},Val,_,,,Z_,,,d8,:,_a,;,},<EOF>''',101))

    def test_604(self):
        self.assertTrue(TestLexer.test('''Class f{}Class Mo:_{Val u1:Int ;}Class _9ep_z:___{Var $D8,l43U,$xh:_U;Val G_,$5Y_D__j,_1J:Boolean ;Constructor (M_x,_,Y,_:G66_lYU;f_6,u_:Int ){} }Class d1{}Class D:q_{}''','''Class,f,{,},Class,Mo,:,_,{,Val,u1,:,Int,;,},Class,_9ep_z,:,___,{,Var,$D8,,,l43U,,,$xh,:,_U,;,Val,G_,,,$5Y_D__j,,,_1J,:,Boolean,;,Constructor,(,M_x,,,_,,,Y,,,_,:,G66_lYU,;,f_6,,,u_,:,Int,),{,},},Class,d1,{,},Class,D,:,q_,{,},<EOF>''',101))

    def test_605(self):
        self.assertTrue(TestLexer.test('''Class D{$_(_,p,S:Array [String ,0X4D];Y9,_,C:Array [String ,44];r:l;_vQ0,_,_,_:Array [String ,0B1];I5_4Zt,_kFv:J2m;i__:Int ){Break ;{} }}Class _:B6_{}Class _:_{Destructor (){Continue ;} }Class K26{}''','''Class,D,{,$_,(,_,,,p,,,S,:,Array,[,String,,,0X4D,],;,Y9,,,_,,,C,:,Array,[,String,,,44,],;,r,:,l,;,_vQ0,,,_,,,_,,,_,:,Array,[,String,,,0B1,],;,I5_4Zt,,,_kFv,:,J2m,;,i__,:,Int,),{,Break,;,{,},},},Class,_,:,B6_,{,},Class,_,:,_,{,Destructor,(,),{,Continue,;,},},Class,K26,{,},<EOF>''',101))

    def test_606(self):
        self.assertTrue(TestLexer.test('''Class JZ{$8_(){}Val l,_,$W_,V1Ya,$38c,$0,_:Q5;Constructor (q,_0_C6,_:__8){}Var _5,_Ez_:Array [String ,0B1001];}''','''Class,JZ,{,$8_,(,),{,},Val,l,,,_,,,$W_,,,V1Ya,,,$38c,,,$0,,,_,:,Q5,;,Constructor,(,q,,,_0_C6,,,_,:,__8,),{,},Var,_5,,,_Ez_,:,Array,[,String,,,0B1001,],;,},<EOF>''',101))

    def test_607(self):
        self.assertTrue(TestLexer.test('''Class wQ_{Constructor (s:Array [String ,0B10111];_:Boolean ;h,_,b,_:Array [Array [Array [Array [Array [Float ,35],04],35],0X27],35]){} }Class _2:_3c{}''','''Class,wQ_,{,Constructor,(,s,:,Array,[,String,,,0B10111,],;,_,:,Boolean,;,h,,,_,,,b,,,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,35,],,,04,],,,35,],,,0X27,],,,35,],),{,},},Class,_2,:,_3c,{,},<EOF>''',101))

    def test_608(self):
        self.assertTrue(TestLexer.test('''Class ___2{Val s,t:Array [Array [Int ,04_5],0b11_0];Var $_,vv,$3,$_,$_44PY:Array [Array [Array [String ,0b11_000_01],50],0b1_00];$2(_,F,_:Array [Array [Int ,0B110010],4_3];YS,c0,f_,_:e;zw_:Array [Array [Int ,6_8],50]){} }Class Hz0{Destructor (){} }Class _{}''','''Class,___2,{,Val,s,,,t,:,Array,[,Array,[,Int,,,045,],,,0b110,],;,Var,$_,,,vv,,,$3,,,$_,,,$_44PY,:,Array,[,Array,[,Array,[,String,,,0b1100001,],,,50,],,,0b100,],;,$2,(,_,,,F,,,_,:,Array,[,Array,[,Int,,,0B110010,],,,43,],;,YS,,,c0,,,f_,,,_,:,e,;,zw_,:,Array,[,Array,[,Int,,,68,],,,50,],),{,},},Class,Hz0,{,Destructor,(,),{,},},Class,_,{,},<EOF>''',101))

    def test_609(self):
        self.assertTrue(TestLexer.test('''Class _24__{Constructor (_R,_,s7:Array [Array [Boolean ,0XA_4_3],33];F:Array [Array [Boolean ,33],0X6_203_A];_,I,_i_m,__:Boolean ){} }Class J{}''','''Class,_24__,{,Constructor,(,_R,,,_,,,s7,:,Array,[,Array,[,Boolean,,,0XA43,],,,33,],;,F,:,Array,[,Array,[,Boolean,,,33,],,,0X6203A,],;,_,,,I,,,_i_m,,,__,:,Boolean,),{,},},Class,J,{,},<EOF>''',101))

    def test_610(self):
        self.assertTrue(TestLexer.test('''Class _R_:G{Constructor (l8,_,_9,l,g,_33,K,_:Array [Array [Array [Array [String ,0x1B],04_25],0126],0b1_0_0]){} }Class D8{Destructor (){Return ;} }''','''Class,_R_,:,G,{,Constructor,(,l8,,,_,,,_9,,,l,,,g,,,_33,,,K,,,_,:,Array,[,Array,[,Array,[,Array,[,String,,,0x1B,],,,0425,],,,0126,],,,0b100,],),{,},},Class,D8,{,Destructor,(,),{,Return,;,},},<EOF>''',101))

    def test_611(self):
        self.assertTrue(TestLexer.test('''Class Uv:_{Var $CW,$x7,___E_0F_:_eO;}Class c:J__{}Class _H___X_:q{Constructor (){ {Val D,__:Float ;} }Destructor (){}$82Z7(){}Destructor (){} }''','''Class,Uv,:,_,{,Var,$CW,,,$x7,,,___E_0F_,:,_eO,;,},Class,c,:,J__,{,},Class,_H___X_,:,q,{,Constructor,(,),{,{,Val,D,,,__,:,Float,;,},},Destructor,(,),{,},$82Z7,(,),{,},Destructor,(,),{,},},<EOF>''',101))

    def test_612(self):
        self.assertTrue(TestLexer.test('''Class __65X:Kt9w{Var D:Array [Array [Array [Int ,031],04],67];}Class __b:h{Constructor (_y:Int ;___3,U,Yq_:Int ){} }''','''Class,__65X,:,Kt9w,{,Var,D,:,Array,[,Array,[,Array,[,Int,,,031,],,,04,],,,67,],;,},Class,__b,:,h,{,Constructor,(,_y,:,Int,;,___3,,,U,,,Yq_,:,Int,),{,},},<EOF>''',101))

    def test_613(self):
        self.assertTrue(TestLexer.test('''Class _:__{$E(k:Array [Array [Int ,2],94];I:Array [Array [Array [Array [Array [Float ,8],0b1_1_1],0B1],011],06];e,s:Float ;D,F:Array [Array [Float ,1],0b1_1_0_111]){}Constructor (){}Destructor (){Break ;}Destructor (){_::$G2oM();}Val _I,$_bO43____:b;}''','''Class,_,:,__,{,$E,(,k,:,Array,[,Array,[,Int,,,2,],,,94,],;,I,:,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,8,],,,0b111,],,,0B1,],,,011,],,,06,],;,e,,,s,:,Float,;,D,,,F,:,Array,[,Array,[,Float,,,1,],,,0b110111,],),{,},Constructor,(,),{,},Destructor,(,),{,Break,;,},Destructor,(,),{,_,::,$G2oM,(,),;,},Val,_I,,,$_bO43____,:,b,;,},<EOF>''',101))

    def test_614(self):
        self.assertTrue(TestLexer.test('''Class _2{Val $_,$e_,$AT_:_76Q;Var _:Float ;O776(_,_77:Array [Array [Array [String ,0X5F],013],0XE]){Var __5_:Array [Int ,0B1010110];} }''','''Class,_2,{,Val,$_,,,$e_,,,$AT_,:,_76Q,;,Var,_,:,Float,;,O776,(,_,,,_77,:,Array,[,Array,[,Array,[,String,,,0X5F,],,,013,],,,0XE,],),{,Var,__5_,:,Array,[,Int,,,0B1010110,],;,},},<EOF>''',101))

    def test_615(self):
        self.assertTrue(TestLexer.test('''Class u{Val _,R,b_56:_;Constructor (O2V3l:Array [Array [Array [String ,0X19],53],8];Q,_,L:q___){}Constructor (){}Val z7:Array [Array [Array [Array [Array [Array [Array [Float ,53],0B1_1_01_1],0X19],9_7],53],8],07];}''','''Class,u,{,Val,_,,,R,,,b_56,:,_,;,Constructor,(,O2V3l,:,Array,[,Array,[,Array,[,String,,,0X19,],,,53,],,,8,],;,Q,,,_,,,L,:,q___,),{,},Constructor,(,),{,},Val,z7,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,53,],,,0B11011,],,,0X19,],,,97,],,,53,],,,8,],,,07,],;,},<EOF>''',101))

    def test_616(self):
        self.assertTrue(TestLexer.test('''Class _:fZ_{J(x,_:String ){Break ;}Var y:Boolean ;Destructor (){}$q8T(_z3,__8,F52,n:A;_,Q:D){}Destructor (){} }''','''Class,_,:,fZ_,{,J,(,x,,,_,:,String,),{,Break,;,},Var,y,:,Boolean,;,Destructor,(,),{,},$q8T,(,_z3,,,__8,,,F52,,,n,:,A,;,_,,,Q,:,D,),{,},Destructor,(,),{,},},<EOF>''',101))

    def test_617(self):
        self.assertTrue(TestLexer.test('''Class _{B_(_,j,c_F,w,i0mg12:_){} }Class f{$_v(_,e79W,_:String ){}Constructor (b:_Zh_o;_t:_;_:Float ;_:Array [Int ,0X47_A_8]){} }''','''Class,_,{,B_,(,_,,,j,,,c_F,,,w,,,i0mg12,:,_,),{,},},Class,f,{,$_v,(,_,,,e79W,,,_,:,String,),{,},Constructor,(,b,:,_Zh_o,;,_t,:,_,;,_,:,Float,;,_,:,Array,[,Int,,,0X47A8,],),{,},},<EOF>''',101))

    def test_618(self):
        self.assertTrue(TestLexer.test('''Class qsI{}Class _:__{}Class _:A_{Constructor (I,_:String ;_2p:Boolean ){Return ;Var l_:Array [String ,28];} }Class ___:_T{}''','''Class,qsI,{,},Class,_,:,__,{,},Class,_,:,A_,{,Constructor,(,I,,,_,:,String,;,_2p,:,Boolean,),{,Return,;,Var,l_,:,Array,[,String,,,28,],;,},},Class,___,:,_T,{,},<EOF>''',101))

    def test_619(self):
        self.assertTrue(TestLexer.test('''Class __3{Constructor (_j,M,_E,d:_;P:_d;__:__;_:Array [Array [Boolean ,0b110001],8_9636]){} }Class _:_{Constructor (YH_t,_:String ){}Destructor (){} }''','''Class,__3,{,Constructor,(,_j,,,M,,,_E,,,d,:,_,;,P,:,_d,;,__,:,__,;,_,:,Array,[,Array,[,Boolean,,,0b110001,],,,89636,],),{,},},Class,_,:,_,{,Constructor,(,YH_t,,,_,:,String,),{,},Destructor,(,),{,},},<EOF>''',101))

    def test_620(self):
        self.assertTrue(TestLexer.test('''Class _{}Class _:w{}Class _:ZT1_{}Class S4{}Class c9:v{}Class _3{Val M,$r:Array [Array [Array [Int ,0b1000000],020],02];Var $4_,$P_:_;Val Z:_;Var $_5,$0__C,P:__;}Class L_:K{}Class Aq{$5_(z,_:_){} }''','''Class,_,{,},Class,_,:,w,{,},Class,_,:,ZT1_,{,},Class,S4,{,},Class,c9,:,v,{,},Class,_3,{,Val,M,,,$r,:,Array,[,Array,[,Array,[,Int,,,0b1000000,],,,020,],,,02,],;,Var,$4_,,,$P_,:,_,;,Val,Z,:,_,;,Var,$_5,,,$0__C,,,P,:,__,;,},Class,L_,:,K,{,},Class,Aq,{,$5_,(,z,,,_,:,_,),{,},},<EOF>''',101))

    def test_621(self):
        self.assertTrue(TestLexer.test('''Class w_A_:_E{}Class i:_l{$_(_1,J:Boolean ;A45_:kl7;_3_Y__75Q9,K,_,_7_9k__:_x;z_4:Array [Int ,0x2];E,_,P,____:Array [String ,0b1_11_0];f5Y_M,J,x,_:Float ;c,X,_,i:Array [Float ,0X6F_C]){} }Class _:Z{}Class _X:_{$7G_1(){Break ;} }Class _Q:_{}''','''Class,w_A_,:,_E,{,},Class,i,:,_l,{,$_,(,_1,,,J,:,Boolean,;,A45_,:,kl7,;,_3_Y__75Q9,,,K,,,_,,,_7_9k__,:,_x,;,z_4,:,Array,[,Int,,,0x2,],;,E,,,_,,,P,,,____,:,Array,[,String,,,0b1110,],;,f5Y_M,,,J,,,x,,,_,:,Float,;,c,,,X,,,_,,,i,:,Array,[,Float,,,0X6FC,],),{,},},Class,_,:,Z,{,},Class,_X,:,_,{,$7G_1,(,),{,Break,;,},},Class,_Q,:,_,{,},<EOF>''',101))

    def test_622(self):
        self.assertTrue(TestLexer.test('''Class _:y{}Class P{Constructor (__:Array [Array [Array [Int ,3_3],9],0143]){}di(_,t,_59_T_____40_gY__,_4E_,_X,X:Array [Array [Boolean ,0x43],9]){Return ;}Constructor (k_,V5:p){}Val i,$0,_,_,h,__,$b___,_:Array [Array [Array [Array [Float ,01_1],0B10111],97],8_53];Val $3o6_,Syk:_;}''','''Class,_,:,y,{,},Class,P,{,Constructor,(,__,:,Array,[,Array,[,Array,[,Int,,,33,],,,9,],,,0143,],),{,},di,(,_,,,t,,,_59_T_____40_gY__,,,_4E_,,,_X,,,X,:,Array,[,Array,[,Boolean,,,0x43,],,,9,],),{,Return,;,},Constructor,(,k_,,,V5,:,p,),{,},Val,i,,,$0,,,_,,,_,,,h,,,__,,,$b___,,,_,:,Array,[,Array,[,Array,[,Array,[,Float,,,011,],,,0B10111,],,,97,],,,853,],;,Val,$3o6_,,,Syk,:,_,;,},<EOF>''',101))

    def test_623(self):
        self.assertTrue(TestLexer.test('''Class Lz{Constructor (r,_,_,Y_,bt_:Array [Array [String ,29],0X3B];_:Int ){}Var x,_:Array [Array [Int ,29],327];}Class __:_{}Class _044:c__{}''','''Class,Lz,{,Constructor,(,r,,,_,,,_,,,Y_,,,bt_,:,Array,[,Array,[,String,,,29,],,,0X3B,],;,_,:,Int,),{,},Var,x,,,_,:,Array,[,Array,[,Int,,,29,],,,327,],;,},Class,__,:,_,{,},Class,_044,:,c__,{,},<EOF>''',101))

    def test_624(self):
        self.assertTrue(TestLexer.test('''Class _{Val ErvV:Boolean ;_(_,LC,_:Array [Array [Array [String ,0B1000011],62],1];B5,tO:String ;_j4:String ;c__7,_,_,_8,P7,K_,k3Z_:_;Z:Float ){Val _____,D,z,T_:w1;}Destructor (){Break ;} }''','''Class,_,{,Val,ErvV,:,Boolean,;,_,(,_,,,LC,,,_,:,Array,[,Array,[,Array,[,String,,,0B1000011,],,,62,],,,1,],;,B5,,,tO,:,String,;,_j4,:,String,;,c__7,,,_,,,_,,,_8,,,P7,,,K_,,,k3Z_,:,_,;,Z,:,Float,),{,Val,_____,,,D,,,z,,,T_,:,w1,;,},Destructor,(,),{,Break,;,},},<EOF>''',101))

    def test_625(self):
        self.assertTrue(TestLexer.test('''Class A{f_3(j4,a:Boolean ;_:Array [Float ,0X7];___0,__:Float ;_,j:Array [Int ,41];_,_,__,_,_:Float ){} }Class G:_{}''','''Class,A,{,f_3,(,j4,,,a,:,Boolean,;,_,:,Array,[,Float,,,0X7,],;,___0,,,__,:,Float,;,_,,,j,:,Array,[,Int,,,41,],;,_,,,_,,,__,,,_,,,_,:,Float,),{,},},Class,G,:,_,{,},<EOF>''',101))

    def test_626(self):
        self.assertTrue(TestLexer.test('''Class _:_P{Constructor (__,p_A,Q21_,d0__,B:Array [Array [Array [Array [Array [Array [Array [String ,95],0xAD_9],0X9A],0b1],0b101001],32],95]){} }''','''Class,_,:,_P,{,Constructor,(,__,,,p_A,,,Q21_,,,d0__,,,B,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,95,],,,0xAD9,],,,0X9A,],,,0b1,],,,0b101001,],,,32,],,,95,],),{,},},<EOF>''',101))

    def test_627(self):
        self.assertTrue(TestLexer.test('''Class _1:_{Constructor (_H_3:Int ;C2__:Array [Array [Float ,032],0x41];_X:Array [Array [Array [Float ,5],7],0B101110]){} }''','''Class,_1,:,_,{,Constructor,(,_H_3,:,Int,;,C2__,:,Array,[,Array,[,Float,,,032,],,,0x41,],;,_X,:,Array,[,Array,[,Array,[,Float,,,5,],,,7,],,,0B101110,],),{,},},<EOF>''',101))

    def test_628(self):
        self.assertTrue(TestLexer.test('''Class _{Constructor (_,_:Array [Float ,0x1]){Break ;} }Class __:FA{$4(){Continue ;}Val _,$3,bO,$j,zsF2:_;}Class __M{}''','''Class,_,{,Constructor,(,_,,,_,:,Array,[,Float,,,0x1,],),{,Break,;,},},Class,__,:,FA,{,$4,(,),{,Continue,;,},Val,_,,,$3,,,bO,,,$j,,,zsF2,:,_,;,},Class,__M,{,},<EOF>''',101))

    def test_629(self):
        self.assertTrue(TestLexer.test('''Class _6__{Destructor (){k::$__();__U2::$_();}Var _:V;Destructor (){} }Class __p0_{Var _3:i_4;Constructor (){Break ;}Destructor (){} }''','''Class,_6__,{,Destructor,(,),{,k,::,$__,(,),;,__U2,::,$_,(,),;,},Var,_,:,V,;,Destructor,(,),{,},},Class,__p0_,{,Var,_3,:,i_4,;,Constructor,(,),{,Break,;,},Destructor,(,),{,},},<EOF>''',101))

    def test_630(self):
        self.assertTrue(TestLexer.test('''Class _:__{}Class __{Destructor (){Break ;}Constructor (__5,_,W,Z6,_,p_:Array [Array [Float ,19],0B1001101]){Break ;Return ;} }Class EC{}Class sN_p{}''','''Class,_,:,__,{,},Class,__,{,Destructor,(,),{,Break,;,},Constructor,(,__5,,,_,,,W,,,Z6,,,_,,,p_,:,Array,[,Array,[,Float,,,19,],,,0B1001101,],),{,Break,;,Return,;,},},Class,EC,{,},Class,sN_p,{,},<EOF>''',101))

    def test_631(self):
        self.assertTrue(TestLexer.test('''Class _{}Class P58:V{Val $_,$03:Array [String ,07];}Class _{Destructor (){}Val _,Rn_T:Int ;Destructor (){}Constructor (){} }Class __{}''','''Class,_,{,},Class,P58,:,V,{,Val,$_,,,$03,:,Array,[,String,,,07,],;,},Class,_,{,Destructor,(,),{,},Val,_,,,Rn_T,:,Int,;,Destructor,(,),{,},Constructor,(,),{,},},Class,__,{,},<EOF>''',101))

    def test_632(self):
        self.assertTrue(TestLexer.test('''Class e_QQ_M:Z{Var $_:Array [Array [Array [Array [Array [Int ,0x4],03_3],5_7_58],0b10],18];}Class _E:sl{}Class Q{}Class _{}''','''Class,e_QQ_M,:,Z,{,Var,$_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0x4,],,,033,],,,5758,],,,0b10,],,,18,],;,},Class,_E,:,sl,{,},Class,Q,{,},Class,_,{,},<EOF>''',101))

    def test_633(self):
        self.assertTrue(TestLexer.test('''Class n{Constructor (){Continue ;} }Class _u{Destructor (){}Var $4:Boolean ;}Class ki:F{Destructor (){} }Class s1{}''','''Class,n,{,Constructor,(,),{,Continue,;,},},Class,_u,{,Destructor,(,),{,},Var,$4,:,Boolean,;,},Class,ki,:,F,{,Destructor,(,),{,},},Class,s1,{,},<EOF>''',101))

    def test_634(self):
        self.assertTrue(TestLexer.test('''Class _{}Class k{Val $_:Array [Array [Array [Array [Array [Float ,071463],0x2_F],8],0X2],071];Val ___:String ;}Class G:_{}Class e{}''','''Class,_,{,},Class,k,{,Val,$_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,071463,],,,0x2F,],,,8,],,,0X2,],,,071,],;,Val,___,:,String,;,},Class,G,:,_,{,},Class,e,{,},<EOF>''',101))

    def test_635(self):
        self.assertTrue(TestLexer.test('''Class _{_(){}Destructor (){}Constructor (_4w3_:o_;_4,_C6i:Array [Boolean ,0xE_65];_5i_:Array [Array [Array [Array [Int ,0xE_0],0XB5787],0107],0x5]){} }Class _K:__5U5_0{}''','''Class,_,{,_,(,),{,},Destructor,(,),{,},Constructor,(,_4w3_,:,o_,;,_4,,,_C6i,:,Array,[,Boolean,,,0xE65,],;,_5i_,:,Array,[,Array,[,Array,[,Array,[,Int,,,0xE0,],,,0XB5787,],,,0107,],,,0x5,],),{,},},Class,_K,:,__5U5_0,{,},<EOF>''',101))

    def test_636(self):
        self.assertTrue(TestLexer.test('''Class b:q{Var $_c_,_09_P:Array [Int ,64_9_8];Val Q93,$y,$_,$78_,J,$8,$_:String ;Val $13,e,$J3_m,_4:Boolean ;Destructor (){} }''','''Class,b,:,q,{,Var,$_c_,,,_09_P,:,Array,[,Int,,,6498,],;,Val,Q93,,,$y,,,$_,,,$78_,,,J,,,$8,,,$_,:,String,;,Val,$13,,,e,,,$J3_m,,,_4,:,Boolean,;,Destructor,(,),{,},},<EOF>''',101))

    def test_637(self):
        self.assertTrue(TestLexer.test('''Class _h:_5_{Val $8_:String ;Var $5:String ;Constructor (u_,_:_;_:Boolean ){}Val $ny:Boolean ;$__(z:Boolean ;h:Array [Int ,021];_,LB:Array [Array [Boolean ,5_2_45],0x21]){_S::$3();} }''','''Class,_h,:,_5_,{,Val,$8_,:,String,;,Var,$5,:,String,;,Constructor,(,u_,,,_,:,_,;,_,:,Boolean,),{,},Val,$ny,:,Boolean,;,$__,(,z,:,Boolean,;,h,:,Array,[,Int,,,021,],;,_,,,LB,:,Array,[,Array,[,Boolean,,,5245,],,,0x21,],),{,_S,::,$3,(,),;,},},<EOF>''',101))

    def test_638(self):
        self.assertTrue(TestLexer.test('''Class _{_(_,y,E,m:_;n:Array [Boolean ,6]){} }Class _{}Class l{}Class _0:_z{}Class _{Val _Q,$7:Array [Boolean ,9];}''','''Class,_,{,_,(,_,,,y,,,E,,,m,:,_,;,n,:,Array,[,Boolean,,,6,],),{,},},Class,_,{,},Class,l,{,},Class,_0,:,_z,{,},Class,_,{,Val,_Q,,,$7,:,Array,[,Boolean,,,9,],;,},<EOF>''',101))

    def test_639(self):
        self.assertTrue(TestLexer.test('''Class __{Ow_6(f:_;A_,YN_:Int ){} }Class Y{$_(){} }Class _:_5u1__{Var tP:Array [String ,0B1_1];}Class L{Destructor (){} }''','''Class,__,{,Ow_6,(,f,:,_,;,A_,,,YN_,:,Int,),{,},},Class,Y,{,$_,(,),{,},},Class,_,:,_5u1__,{,Var,tP,:,Array,[,String,,,0B11,],;,},Class,L,{,Destructor,(,),{,},},<EOF>''',101))

    def test_640(self):
        self.assertTrue(TestLexer.test('''Class _9___7:r1_F__{Val M,U,_,$29_,i,$0:Array [Array [Array [Array [Array [Int ,0x55],0b1011],05_6_6],0X1],0X9];}Class _S{}''','''Class,_9___7,:,r1_F__,{,Val,M,,,U,,,_,,,$29_,,,i,,,$0,:,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0x55,],,,0b1011,],,,0566,],,,0X1,],,,0X9,],;,},Class,_S,{,},<EOF>''',101))

    def test_641(self):
        self.assertTrue(TestLexer.test('''Class B:_m2U{Constructor (O1:Array [Int ,0x4D];_,l5__k:Array [Array [Array [Float ,0x4D],04],0137]){} }Class F{Var H:Float ;}''','''Class,B,:,_m2U,{,Constructor,(,O1,:,Array,[,Int,,,0x4D,],;,_,,,l5__k,:,Array,[,Array,[,Array,[,Float,,,0x4D,],,,04,],,,0137,],),{,},},Class,F,{,Var,H,:,Float,;,},<EOF>''',101))

    def test_642(self):
        self.assertTrue(TestLexer.test('''Class v{Val _,$5jex6383_:Int ;$q_4(_10__,T:Int ;n0:Array [Array [Array [Boolean ,90],0B111100],0X24]){}Constructor (_9B_r_,Sq_W,_3:_T;Y,a:Array [Boolean ,03];qEd:wP){}Val T,$nC5,_,$_:H;}Class _:ty_{}''','''Class,v,{,Val,_,,,$5jex6383_,:,Int,;,$q_4,(,_10__,,,T,:,Int,;,n0,:,Array,[,Array,[,Array,[,Boolean,,,90,],,,0B111100,],,,0X24,],),{,},Constructor,(,_9B_r_,,,Sq_W,,,_3,:,_T,;,Y,,,a,:,Array,[,Boolean,,,03,],;,qEd,:,wP,),{,},Val,T,,,$nC5,,,_,,,$_,:,H,;,},Class,_,:,ty_,{,},<EOF>''',101))

    def test_643(self):
        self.assertTrue(TestLexer.test('''Class R4:_2{Var $_o:Array [Array [Array [String ,0x3],0X34],0X34];}Class S1_:b_9m{$__(t_,M:Array [Boolean ,01];_c0N,q:f){Var _34_U,_zW3,_,_lM8,JE_67J4q,K9:Float ;} }Class y{}''','''Class,R4,:,_2,{,Var,$_o,:,Array,[,Array,[,Array,[,String,,,0x3,],,,0X34,],,,0X34,],;,},Class,S1_,:,b_9m,{,$__,(,t_,,,M,:,Array,[,Boolean,,,01,],;,_c0N,,,q,:,f,),{,Var,_34_U,,,_zW3,,,_,,,_lM8,,,JE_67J4q,,,K9,:,Float,;,},},Class,y,{,},<EOF>''',101))

    def test_644(self):
        self.assertTrue(TestLexer.test('''Class S8{}Class _3:b{Val $q:_U;Val _3:A;}Class p4O_{Constructor (n5,_,_,N6W___:String ;_,G9,LCUD,q9,g__:Boolean ){Return ;} }''','''Class,S8,{,},Class,_3,:,b,{,Val,$q,:,_U,;,Val,_3,:,A,;,},Class,p4O_,{,Constructor,(,n5,,,_,,,_,,,N6W___,:,String,;,_,,,G9,,,LCUD,,,q9,,,g__,:,Boolean,),{,Return,;,},},<EOF>''',101))

    def test_645(self):
        self.assertTrue(TestLexer.test('''Class uZ_:__Q_5{Destructor (){}Constructor (B:Array [Float ,065]){}Var $_8h:Array [Array [Array [Array [Array [Boolean ,06],3],83],0X1_8],0xE9];Val $6,_:Array [Boolean ,0X1];}''','''Class,uZ_,:,__Q_5,{,Destructor,(,),{,},Constructor,(,B,:,Array,[,Float,,,065,],),{,},Var,$_8h,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,06,],,,3,],,,83,],,,0X18,],,,0xE9,],;,Val,$6,,,_,:,Array,[,Boolean,,,0X1,],;,},<EOF>''',101))

    def test_646(self):
        self.assertTrue(TestLexer.test('''Class F_:_6F{Constructor (_1T_:Array [Array [Float ,0XB],0x6];WP:Int ){}__(U,__,B,_:Array [String ,06]){}Destructor (){ {} }$__P16(_,_,_,C72X4,Z,_U0f3:_){} }Class _:m{}''','''Class,F_,:,_6F,{,Constructor,(,_1T_,:,Array,[,Array,[,Float,,,0XB,],,,0x6,],;,WP,:,Int,),{,},__,(,U,,,__,,,B,,,_,:,Array,[,String,,,06,],),{,},Destructor,(,),{,{,},},$__P16,(,_,,,_,,,_,,,C72X4,,,Z,,,_U0f3,:,_,),{,},},Class,_,:,m,{,},<EOF>''',101))

    def test_647(self):
        self.assertTrue(TestLexer.test('''Class GN:J0{Val $_:Array [Array [Array [Array [String ,0x6],0x7],4_6_67_9],0x40];}Class u:k{}Class _{Destructor (){} }Class gNv1{}''','''Class,GN,:,J0,{,Val,$_,:,Array,[,Array,[,Array,[,Array,[,String,,,0x6,],,,0x7,],,,46679,],,,0x40,],;,},Class,u,:,k,{,},Class,_,{,Destructor,(,),{,},},Class,gNv1,{,},<EOF>''',101))

    def test_648(self):
        self.assertTrue(TestLexer.test('''Class j_:n_5{Var $_i,$_r__ms_8O,a,$_:Float ;Var $_J,$x:Array [Array [Array [Array [Array [Array [Int ,02_4_77757],0B1001001],0X3A],0b101110],02],7];Destructor (){}Constructor (){}Var $v,g:Float ;}Class j{}Class l{Val $__3_:Array [Array [Float ,53],0x2];}''','''Class,j_,:,n_5,{,Var,$_i,,,$_r__ms_8O,,,a,,,$_,:,Float,;,Var,$_J,,,$x,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,02477757,],,,0B1001001,],,,0X3A,],,,0b101110,],,,02,],,,7,],;,Destructor,(,),{,},Constructor,(,),{,},Var,$v,,,g,:,Float,;,},Class,j,{,},Class,l,{,Val,$__3_,:,Array,[,Array,[,Float,,,53,],,,0x2,],;,},<EOF>''',101))

    def test_649(self):
        self.assertTrue(TestLexer.test('''Class _{Var _,$M_,EU4_,$_i_,$u:Boolean ;Constructor (Wh,_:Array [Boolean ,0X49];___,c_:c;_2K6:Float ;_,_,_V:String ){} }''','''Class,_,{,Var,_,,,$M_,,,EU4_,,,$_i_,,,$u,:,Boolean,;,Constructor,(,Wh,,,_,:,Array,[,Boolean,,,0X49,],;,___,,,c_,:,c,;,_2K6,:,Float,;,_,,,_,,,_V,:,String,),{,},},<EOF>''',101))

    def test_650(self):
        self.assertTrue(TestLexer.test('''Class _:DX{Val w:Array [Array [Float ,57],0x64];}Class _:q_2_{}Class _28:I3_1s{}Class __{}Class Ym_{Val I:Array [Array [Float ,07],79];}''','''Class,_,:,DX,{,Val,w,:,Array,[,Array,[,Float,,,57,],,,0x64,],;,},Class,_,:,q_2_,{,},Class,_28,:,I3_1s,{,},Class,__,{,},Class,Ym_,{,Val,I,:,Array,[,Array,[,Float,,,07,],,,79,],;,},<EOF>''',101))

    def test_651(self):
        self.assertTrue(TestLexer.test('''Class B_9_{Val _Z:ca;Destructor (){Break ;}Destructor (){}Val $4:Array [Array [Array [Array [Array [Array [Array [Boolean ,0b11],01],0XE],56],01],0B10],0B11100];}''','''Class,B_9_,{,Val,_Z,:,ca,;,Destructor,(,),{,Break,;,},Destructor,(,),{,},Val,$4,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0b11,],,,01,],,,0XE,],,,56,],,,01,],,,0B10,],,,0B11100,],;,},<EOF>''',101))

    def test_652(self):
        self.assertTrue(TestLexer.test('''Class _b{Constructor (___,_:Array [Array [Array [Array [Array [Boolean ,0x7],7_4],0B1_1],070],89]){} }Class _T:r_q_{}Class s:_M{}''','''Class,_b,{,Constructor,(,___,,,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0x7,],,,74,],,,0B11,],,,070,],,,89,],),{,},},Class,_T,:,r_q_,{,},Class,s,:,_M,{,},<EOF>''',101))

    def test_653(self):
        self.assertTrue(TestLexer.test('''Class y{}Class _X5{Destructor (){}Destructor (){Break ;}Constructor (_:Nc){}Var $6__5W:Array [String ,06_6_71_1];}Class V_{Destructor (){ {}Continue ;}Var $5QC:Boolean ;}''','''Class,y,{,},Class,_X5,{,Destructor,(,),{,},Destructor,(,),{,Break,;,},Constructor,(,_,:,Nc,),{,},Var,$6__5W,:,Array,[,String,,,066711,],;,},Class,V_,{,Destructor,(,),{,{,},Continue,;,},Var,$5QC,:,Boolean,;,},<EOF>''',101))

    def test_654(self):
        self.assertTrue(TestLexer.test('''Class _{O(C,l,_,k4u5_:Float ){Var y,_d37:Array [Array [String ,022_0],0XA5];Continue ;}Val _,$4,$_,Q,$3:String ;}Class q4M:q{Var ___26t,$_:Array [Int ,0B100];}Class Ql{}Class _W9_5:H1{}''','''Class,_,{,O,(,C,,,l,,,_,,,k4u5_,:,Float,),{,Var,y,,,_d37,:,Array,[,Array,[,String,,,0220,],,,0XA5,],;,Continue,;,},Val,_,,,$4,,,$_,,,Q,,,$3,:,String,;,},Class,q4M,:,q,{,Var,___26t,,,$_,:,Array,[,Int,,,0B100,],;,},Class,Ql,{,},Class,_W9_5,:,H1,{,},<EOF>''',101))

    def test_655(self):
        self.assertTrue(TestLexer.test('''Class o_P6z{$__(J:Array [Array [Boolean ,06],430_8];v_3_ks_,BI:b){Continue ;} }Class _A:C_{}Class _:_{}Class Cj_V:v{}Class _{}''','''Class,o_P6z,{,$__,(,J,:,Array,[,Array,[,Boolean,,,06,],,,4308,],;,v_3_ks_,,,BI,:,b,),{,Continue,;,},},Class,_A,:,C_,{,},Class,_,:,_,{,},Class,Cj_V,:,v,{,},Class,_,{,},<EOF>''',101))

    def test_656(self):
        self.assertTrue(TestLexer.test('''Class I{}Class _{Val _:v_;Val $_:Array [Int ,0B1_1];}Class u1_8q_5_O{Var $a_,$3b_:Boolean ;Var yz1:Array [Array [Boolean ,0b1],03];}''','''Class,I,{,},Class,_,{,Val,_,:,v_,;,Val,$_,:,Array,[,Int,,,0B11,],;,},Class,u1_8q_5_O,{,Var,$a_,,,$3b_,:,Boolean,;,Var,yz1,:,Array,[,Array,[,Boolean,,,0b1,],,,03,],;,},<EOF>''',101))

    def test_657(self):
        self.assertTrue(TestLexer.test('''Class Kp_:ZF78{}Class _{}Class __Z{Var $Si2,$_3,$c:Array [String ,0X1B];Val $B:W;Val $I,$M1:Array [Boolean ,0114];}Class _4S:gQ4{}''','''Class,Kp_,:,ZF78,{,},Class,_,{,},Class,__Z,{,Var,$Si2,,,$_3,,,$c,:,Array,[,String,,,0X1B,],;,Val,$B,:,W,;,Val,$I,,,$M1,:,Array,[,Boolean,,,0114,],;,},Class,_4S,:,gQ4,{,},<EOF>''',101))

    def test_658(self):
        self.assertTrue(TestLexer.test('''Class __{}Class AZ_h_:_{B4(_i,r,zq:Array [Int ,7_2]){}Var $_T:Boolean ;Constructor (S,I8,_,W,_,g,_,V1,_,__,N_,s,v,c:Array [Float ,052];A:Array [Array [Array [String ,0B11],13],0x5F];_,_:String ;_0:Array [Array [Float ,0x5F],0x6_4];N3:_;h__5R:V){Continue ;} }''','''Class,__,{,},Class,AZ_h_,:,_,{,B4,(,_i,,,r,,,zq,:,Array,[,Int,,,72,],),{,},Var,$_T,:,Boolean,;,Constructor,(,S,,,I8,,,_,,,W,,,_,,,g,,,_,,,V1,,,_,,,__,,,N_,,,s,,,v,,,c,:,Array,[,Float,,,052,],;,A,:,Array,[,Array,[,Array,[,String,,,0B11,],,,13,],,,0x5F,],;,_,,,_,:,String,;,_0,:,Array,[,Array,[,Float,,,0x5F,],,,0x64,],;,N3,:,_,;,h__5R,:,V,),{,Continue,;,},},<EOF>''',101))

    def test_659(self):
        self.assertTrue(TestLexer.test('''Class q{}Class _:_{Constructor (_,___,_8:Array [Array [String ,0B111001],0b1_011_1];c,q_,jf,_:Array [Array [Boolean ,0x40],7]){}Destructor (){} }''','''Class,q,{,},Class,_,:,_,{,Constructor,(,_,,,___,,,_8,:,Array,[,Array,[,String,,,0B111001,],,,0b10111,],;,c,,,q_,,,jf,,,_,:,Array,[,Array,[,Boolean,,,0x40,],,,7,],),{,},Destructor,(,),{,},},<EOF>''',101))

    def test_660(self):
        self.assertTrue(TestLexer.test('''Class _{Constructor (_:Array [Array [String ,69],0XA_3_B];_:Array [Int ,0X8];____7:e;_:Array [Array [Array [String ,69],0B110100],0B110100];X1:Array [Float ,4_8];M_:x;__R:_;w:String ;__:Array [Array [Int ,027],5];_r:Array [Array [Array [Array [Array [Float ,0X30],0B110100],69],3_6_041],0b1100011]){} }''','''Class,_,{,Constructor,(,_,:,Array,[,Array,[,String,,,69,],,,0XA3B,],;,_,:,Array,[,Int,,,0X8,],;,____7,:,e,;,_,:,Array,[,Array,[,Array,[,String,,,69,],,,0B110100,],,,0B110100,],;,X1,:,Array,[,Float,,,48,],;,M_,:,x,;,__R,:,_,;,w,:,String,;,__,:,Array,[,Array,[,Int,,,027,],,,5,],;,_r,:,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0X30,],,,0B110100,],,,69,],,,36041,],,,0b1100011,],),{,},},<EOF>''',101))

    def test_661(self):
        self.assertTrue(TestLexer.test('''Class _h:b{Var $_5_:Array [Int ,0x2];}Class _:ky_4o{Constructor (K,_:String ){}Destructor (){Continue ;}Val L__410:Array [Array [Array [String ,0B11000],017],0x2];}''','''Class,_h,:,b,{,Var,$_5_,:,Array,[,Int,,,0x2,],;,},Class,_,:,ky_4o,{,Constructor,(,K,,,_,:,String,),{,},Destructor,(,),{,Continue,;,},Val,L__410,:,Array,[,Array,[,Array,[,String,,,0B11000,],,,017,],,,0x2,],;,},<EOF>''',101))

    def test_662(self):
        self.assertTrue(TestLexer.test('''Class _:kx{}Class A2:J__{Constructor (){Break ;} }Class F{Destructor (){ {} }Constructor (__,x,_Q_:_){}Constructor (){} }''','''Class,_,:,kx,{,},Class,A2,:,J__,{,Constructor,(,),{,Break,;,},},Class,F,{,Destructor,(,),{,{,},},Constructor,(,__,,,x,,,_Q_,:,_,),{,},Constructor,(,),{,},},<EOF>''',101))

    def test_663(self):
        self.assertTrue(TestLexer.test('''Class _Z7F__x:_{}Class y_L_:_9{Val $w:Array [Array [Array [Array [Array [Array [Array [Array [Array [Array [Array [Array [Array [Int ,0B10010],82],0b111000],5],0x8],0X2E],82],01],0b111000],0101],07],0x9],0101];}''','''Class,_Z7F__x,:,_,{,},Class,y_L_,:,_9,{,Val,$w,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0B10010,],,,82,],,,0b111000,],,,5,],,,0x8,],,,0X2E,],,,82,],,,01,],,,0b111000,],,,0101,],,,07,],,,0x9,],,,0101,],;,},<EOF>''',101))

    def test_664(self):
        self.assertTrue(TestLexer.test('''Class s{}Class N__:_{Ax(_:Array [Array [Int ,50],0727_1]){} }Class p_:_{}Class ___I{Var u0H___R,__:Array [Array [Array [Array [Array [Int ,031_6],0X2],0x5],0b1011],9];}''','''Class,s,{,},Class,N__,:,_,{,Ax,(,_,:,Array,[,Array,[,Int,,,50,],,,07271,],),{,},},Class,p_,:,_,{,},Class,___I,{,Var,u0H___R,,,__,:,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0316,],,,0X2,],,,0x5,],,,0b1011,],,,9,],;,},<EOF>''',101))

    def test_665(self):
        self.assertTrue(TestLexer.test('''Class y__{Constructor (__O:Array [Int ,2_0_1];_i,h:_;__3:Array [Array [Array [Float ,0b1011011],0x5E],0xADE_9];mp9:Int ;_:_1_h7;_9O8_P_,q:_){} }''','''Class,y__,{,Constructor,(,__O,:,Array,[,Int,,,201,],;,_i,,,h,:,_,;,__3,:,Array,[,Array,[,Array,[,Float,,,0b1011011,],,,0x5E,],,,0xADE9,],;,mp9,:,Int,;,_,:,_1_h7,;,_9O8_P_,,,q,:,_,),{,},},<EOF>''',101))

    def test_666(self):
        self.assertTrue(TestLexer.test('''Class _:m{Destructor (){Val Ki,_h:Array [Array [Array [Array [Boolean ,0b11],0121],0121],7];}Val $5_:Int ;$_(V:Array [Boolean ,0B1]){} }''','''Class,_,:,m,{,Destructor,(,),{,Val,Ki,,,_h,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,0b11,],,,0121,],,,0121,],,,7,],;,},Val,$5_,:,Int,;,$_,(,V,:,Array,[,Boolean,,,0B1,],),{,},},<EOF>''',101))

    def test_667(self):
        self.assertTrue(TestLexer.test('''Class c{}Class yNt0:_{}Class X{Var __,v,$_7:Boolean ;}Class m4R:Gl{Var X6:Boolean ;}Class _:SA{$_(_1,_,_:Array [Array [Int ,0XB],0B10]){} }Class tj_:D7Pv1{$5(){New Cq()._();Break ;Continue ;} }''','''Class,c,{,},Class,yNt0,:,_,{,},Class,X,{,Var,__,,,v,,,$_7,:,Boolean,;,},Class,m4R,:,Gl,{,Var,X6,:,Boolean,;,},Class,_,:,SA,{,$_,(,_1,,,_,,,_,:,Array,[,Array,[,Int,,,0XB,],,,0B10,],),{,},},Class,tj_,:,D7Pv1,{,$5,(,),{,New,Cq,(,),.,_,(,),;,Break,;,Continue,;,},},<EOF>''',101))

    def test_668(self):
        self.assertTrue(TestLexer.test('''Class d:u{Val r,$O,_7u8,$_zn_1,_,$_,_4F,$_:Array [Array [Array [Array [Array [Array [Float ,1],0x2F],97],0x2F],0b1101],0B1001000];}Class i0:__1_{}''','''Class,d,:,u,{,Val,r,,,$O,,,_7u8,,,$_zn_1,,,_,,,$_,,,_4F,,,$_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,1,],,,0x2F,],,,97,],,,0x2F,],,,0b1101,],,,0B1001000,],;,},Class,i0,:,__1_,{,},<EOF>''',101))

    def test_669(self):
        self.assertTrue(TestLexer.test('''Class _{Destructor (){Continue ;} }Class _{__(){} }Class q{Var $_,nn64_1,$D8_X,i,Q,$6,$0,$_:X;Destructor (){}Destructor (){Break ;}Constructor (_Py_48,B91:T___7;cq,r,D8d:String ){} }''','''Class,_,{,Destructor,(,),{,Continue,;,},},Class,_,{,__,(,),{,},},Class,q,{,Var,$_,,,nn64_1,,,$D8_X,,,i,,,Q,,,$6,,,$0,,,$_,:,X,;,Destructor,(,),{,},Destructor,(,),{,Break,;,},Constructor,(,_Py_48,,,B91,:,T___7,;,cq,,,r,,,D8d,:,String,),{,},},<EOF>''',101))

    def test_670(self):
        self.assertTrue(TestLexer.test('''Class R{__(_X_:Array [Array [Array [Array [Array [String ,0B101],0X2A],0X2A],05],0B100000];_K,D,M31,u:MU_;t5,e:String ;_:o;X:w27;g,__H,_:R;F,_:Float ){Break ;} }''','''Class,R,{,__,(,_X_,:,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0B101,],,,0X2A,],,,0X2A,],,,05,],,,0B100000,],;,_K,,,D,,,M31,,,u,:,MU_,;,t5,,,e,:,String,;,_,:,o,;,X,:,w27,;,g,,,__H,,,_,:,R,;,F,,,_,:,Float,),{,Break,;,},},<EOF>''',101))

    def test_671(self):
        self.assertTrue(TestLexer.test('''Class _1:F{Var __mC_,_:_;}Class p75{Val $__,O,Bp:Array [Array [Array [Array [String ,0B11101],2],0B11101],07_3_06];}Class f48:M{}Class k_QL1:_{}Class _:_9{}''','''Class,_1,:,F,{,Var,__mC_,,,_,:,_,;,},Class,p75,{,Val,$__,,,O,,,Bp,:,Array,[,Array,[,Array,[,Array,[,String,,,0B11101,],,,2,],,,0B11101,],,,07306,],;,},Class,f48,:,M,{,},Class,k_QL1,:,_,{,},Class,_,:,_9,{,},<EOF>''',101))

    def test_672(self):
        self.assertTrue(TestLexer.test('''Class J0:w{$A1(__:_;u:Array [Boolean ,0B1010000]){Continue ;}Constructor (Z:Float ;_3e,D,_6:Array [Array [String ,0x7E],0X8_1_8];M_,c:Int ){} }''','''Class,J0,:,w,{,$A1,(,__,:,_,;,u,:,Array,[,Boolean,,,0B1010000,],),{,Continue,;,},Constructor,(,Z,:,Float,;,_3e,,,D,,,_6,:,Array,[,Array,[,String,,,0x7E,],,,0X818,],;,M_,,,c,:,Int,),{,},},<EOF>''',101))

    def test_673(self):
        self.assertTrue(TestLexer.test('''Class G{}Class H8{Destructor (){Var _:_;Continue ;}Var $H3_:Array [Array [Array [Array [Int ,015_3],27_4_8],0X39],03_7];Var __,$v,_vGai,_5_r_8W82Q_:_;}''','''Class,G,{,},Class,H8,{,Destructor,(,),{,Var,_,:,_,;,Continue,;,},Var,$H3_,:,Array,[,Array,[,Array,[,Array,[,Int,,,0153,],,,2748,],,,0X39,],,,037,],;,Var,__,,,$v,,,_vGai,,,_5_r_8W82Q_,:,_,;,},<EOF>''',101))

    def test_674(self):
        self.assertTrue(TestLexer.test('''Class _95:z{_(){Return ;}xNN2(){} }Class _:R_{Val S:Array [Int ,22];Var $7:Float ;}Class Be5{}Class _:_s8283{Destructor (){} }Class fh{}''','''Class,_95,:,z,{,_,(,),{,Return,;,},xNN2,(,),{,},},Class,_,:,R_,{,Val,S,:,Array,[,Int,,,22,],;,Var,$7,:,Float,;,},Class,Be5,{,},Class,_,:,_s8283,{,Destructor,(,),{,},},Class,fh,{,},<EOF>''',101))

    def test_675(self):
        self.assertTrue(TestLexer.test('''Class _:_{}Class _:_{}Class _{}Class _j{Val _62:_;Val __:Array [Array [String ,01],97];}Class __1___9HA002:U2__{}''','''Class,_,:,_,{,},Class,_,:,_,{,},Class,_,{,},Class,_j,{,Val,_62,:,_,;,Val,__,:,Array,[,Array,[,String,,,01,],,,97,],;,},Class,__1___9HA002,:,U2__,{,},<EOF>''',101))

    def test_676(self):
        self.assertTrue(TestLexer.test('''Class _{}Class _:R{}Class P:K{$t2_(fMp,o_,_,_,S74:Array [Array [Array [Array [Boolean ,19],0b10000],19],8];_5:m){} }Class ___{Var _aY:_;Val $_:Array [Array [Array [Array [Array [Array [Float ,19],3],0X1E0_5],9],0x9],0x3A];}Class gy:e{}''','''Class,_,{,},Class,_,:,R,{,},Class,P,:,K,{,$t2_,(,fMp,,,o_,,,_,,,_,,,S74,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,19,],,,0b10000,],,,19,],,,8,],;,_5,:,m,),{,},},Class,___,{,Var,_aY,:,_,;,Val,$_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,19,],,,3,],,,0X1E05,],,,9,],,,0x9,],,,0x3A,],;,},Class,gy,:,e,{,},<EOF>''',101))

    def test_677(self):
        self.assertTrue(TestLexer.test('''Class n:m6{}Class Z{}Class X_2{Constructor (){} }Class d_T:M{_(){}Var CkG3,$O:Array [Array [Array [Boolean ,0X3D],041],0B1000101];Constructor (_,_:b_5){} }''','''Class,n,:,m6,{,},Class,Z,{,},Class,X_2,{,Constructor,(,),{,},},Class,d_T,:,M,{,_,(,),{,},Var,CkG3,,,$O,:,Array,[,Array,[,Array,[,Boolean,,,0X3D,],,,041,],,,0B1000101,],;,Constructor,(,_,,,_,:,b_5,),{,},},<EOF>''',101))

    def test_678(self):
        self.assertTrue(TestLexer.test('''Class AA{Constructor (_:k;__:Array [Array [Array [Array [Int ,074],0X65B],0B111010],0B111010];R,_,_:Array [Int ,0X18E];_:String ){ {Val _,c:Int ;Continue ;}{} }Val _:Array [Float ,0x63];Constructor (uD__:__;A,_61:Array [Boolean ,074];E__3__C_2:Array [Float ,19];v_,w7:Array [Boolean ,074];Q,Y79,a_1,_:Array [Boolean ,074];__:_){} }Class H9k_{Destructor (){} }''','''Class,AA,{,Constructor,(,_,:,k,;,__,:,Array,[,Array,[,Array,[,Array,[,Int,,,074,],,,0X65B,],,,0B111010,],,,0B111010,],;,R,,,_,,,_,:,Array,[,Int,,,0X18E,],;,_,:,String,),{,{,Val,_,,,c,:,Int,;,Continue,;,},{,},},Val,_,:,Array,[,Float,,,0x63,],;,Constructor,(,uD__,:,__,;,A,,,_61,:,Array,[,Boolean,,,074,],;,E__3__C_2,:,Array,[,Float,,,19,],;,v_,,,w7,:,Array,[,Boolean,,,074,],;,Q,,,Y79,,,a_1,,,_,:,Array,[,Boolean,,,074,],;,__,:,_,),{,},},Class,H9k_,{,Destructor,(,),{,},},<EOF>''',101))

    def test_679(self):
        self.assertTrue(TestLexer.test('''Class _fK3:_{Val _a,w4d3:Array [Float ,0136];Var $E_,$__,$_:Int ;}Class y_1{}Class _:k0{}Class _O:_{Constructor (){}$C_(_:Array [Array [Float ,0XA5F],69];s,_,__6_lY:Array [Array [Int ,0b1],4]){}_(){ {}Var z,j:Boolean ;Break ;} }Class w:_O{Val $s:Float ;}''','''Class,_fK3,:,_,{,Val,_a,,,w4d3,:,Array,[,Float,,,0136,],;,Var,$E_,,,$__,,,$_,:,Int,;,},Class,y_1,{,},Class,_,:,k0,{,},Class,_O,:,_,{,Constructor,(,),{,},$C_,(,_,:,Array,[,Array,[,Float,,,0XA5F,],,,69,],;,s,,,_,,,__6_lY,:,Array,[,Array,[,Int,,,0b1,],,,4,],),{,},_,(,),{,{,},Var,z,,,j,:,Boolean,;,Break,;,},},Class,w,:,_O,{,Val,$s,:,Float,;,},<EOF>''',101))

    def test_680(self):
        self.assertTrue(TestLexer.test('''Class L_{Var b_:y_4;Constructor (D9_,X8:Int ;E:Array [Boolean ,0B111001];__,_:_;a:Boolean ;_,_8:Float ;G:Array [Array [Int ,0b1011],8]){} }Class _{Val _:Array [Array [Int ,06],0115];}''','''Class,L_,{,Var,b_,:,y_4,;,Constructor,(,D9_,,,X8,:,Int,;,E,:,Array,[,Boolean,,,0B111001,],;,__,,,_,:,_,;,a,:,Boolean,;,_,,,_8,:,Float,;,G,:,Array,[,Array,[,Int,,,0b1011,],,,8,],),{,},},Class,_,{,Val,_,:,Array,[,Array,[,Int,,,06,],,,0115,],;,},<EOF>''',101))

    def test_681(self):
        self.assertTrue(TestLexer.test('''Class _:_{Var w_,$N05,$3:_7_t;y_5(__0:Float ;_:Array [Array [Float ,0B1],0X9];__,R_:_){}Val a,$m__,$H:J;$i6_(T:Array [Array [Array [Array [String ,97],06],0b1],02];_,_L:Boolean ;_:p1){_e8E0j::$3();} }''','''Class,_,:,_,{,Var,w_,,,$N05,,,$3,:,_7_t,;,y_5,(,__0,:,Float,;,_,:,Array,[,Array,[,Float,,,0B1,],,,0X9,],;,__,,,R_,:,_,),{,},Val,a,,,$m__,,,$H,:,J,;,$i6_,(,T,:,Array,[,Array,[,Array,[,Array,[,String,,,97,],,,06,],,,0b1,],,,02,],;,_,,,_L,:,Boolean,;,_,:,p1,),{,_e8E0j,::,$3,(,),;,},},<EOF>''',101))

    def test_682(self):
        self.assertTrue(TestLexer.test('''Class o{Destructor (){}Destructor (){Var F0:_;Val _:Int ;}Constructor (_,_:Float ;_7___,c:Boolean ;___,_1_3:Array [Array [Array [Array [Boolean ,1],0B1011101],037],026];z7f_8,m_,_M_4__7:String ){ {Continue ;} }}''','''Class,o,{,Destructor,(,),{,},Destructor,(,),{,Var,F0,:,_,;,Val,_,:,Int,;,},Constructor,(,_,,,_,:,Float,;,_7___,,,c,:,Boolean,;,___,,,_1_3,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,1,],,,0B1011101,],,,037,],,,026,],;,z7f_8,,,m_,,,_M_4__7,:,String,),{,{,Continue,;,},},},<EOF>''',101))

    def test_683(self):
        self.assertTrue(TestLexer.test('''Class N{Constructor (){}Var Q:Array [Array [Boolean ,0X46],05];Constructor (_,v5,b98_1,__37,HDj__c,_F2:O_;x:Boolean ){} }''','''Class,N,{,Constructor,(,),{,},Var,Q,:,Array,[,Array,[,Boolean,,,0X46,],,,05,],;,Constructor,(,_,,,v5,,,b98_1,,,__37,,,HDj__c,,,_F2,:,O_,;,x,:,Boolean,),{,},},<EOF>''',101))

    def test_684(self):
        self.assertTrue(TestLexer.test('''Class R_h_:s{Constructor (x5:Boolean ;_pN9_8x:Array [Array [String ,0X2_C_7],0x18]){}$3d(jM:Boolean ){}Destructor (){} }''','''Class,R_h_,:,s,{,Constructor,(,x5,:,Boolean,;,_pN9_8x,:,Array,[,Array,[,String,,,0X2C7,],,,0x18,],),{,},$3d,(,jM,:,Boolean,),{,},Destructor,(,),{,},},<EOF>''',101))

    def test_685(self):
        self.assertTrue(TestLexer.test('''Class n{Var $G_2,$_8,_81:Array [Array [Array [Float ,0XBB_5_2_F],0B1100100],0X54];Destructor (){} }Class _{}Class _SK:N3M{}''','''Class,n,{,Var,$G_2,,,$_8,,,_81,:,Array,[,Array,[,Array,[,Float,,,0XBB52F,],,,0B1100100,],,,0X54,],;,Destructor,(,),{,},},Class,_,{,},Class,_SK,:,N3M,{,},<EOF>''',101))

    def test_686(self):
        self.assertTrue(TestLexer.test('''Class n{Constructor (n:Boolean ;_,N:Array [String ,0b1];r_7,_R:String ;_9:_;_,_:Array [Boolean ,0B1];_:_;gM:Array [Array [Int ,022],0B101101]){}z(_:Float ){}Constructor (){} }''','''Class,n,{,Constructor,(,n,:,Boolean,;,_,,,N,:,Array,[,String,,,0b1,],;,r_7,,,_R,:,String,;,_9,:,_,;,_,,,_,:,Array,[,Boolean,,,0B1,],;,_,:,_,;,gM,:,Array,[,Array,[,Int,,,022,],,,0B101101,],),{,},z,(,_,:,Float,),{,},Constructor,(,),{,},},<EOF>''',101))

    def test_687(self):
        self.assertTrue(TestLexer.test('''Class ___{Constructor (_1N,R,_6j:String ;S1__:Float ;_:_p;_2,J:Int ;a_c,_:String ){Break ;}Var $4:Float ;Var I:Array [String ,0x8];}Class r:_{}Class __:_Dw3_{Destructor (){} }''','''Class,___,{,Constructor,(,_1N,,,R,,,_6j,:,String,;,S1__,:,Float,;,_,:,_p,;,_2,,,J,:,Int,;,a_c,,,_,:,String,),{,Break,;,},Var,$4,:,Float,;,Var,I,:,Array,[,String,,,0x8,],;,},Class,r,:,_,{,},Class,__,:,_Dw3_,{,Destructor,(,),{,},},<EOF>''',101))

    def test_688(self):
        self.assertTrue(TestLexer.test('''Class d4:_8hZ_3{Constructor (_:Array [Array [Int ,0XB_C],0x62];_:Array [Array [Int ,0B1],01];My9174:Array [Array [Array [Array [Int ,041],0105],0x62],0b10010];_iX:Array [Array [Int ,41],0xB]){} }Class _:_7{}''','''Class,d4,:,_8hZ_3,{,Constructor,(,_,:,Array,[,Array,[,Int,,,0XBC,],,,0x62,],;,_,:,Array,[,Array,[,Int,,,0B1,],,,01,],;,My9174,:,Array,[,Array,[,Array,[,Array,[,Int,,,041,],,,0105,],,,0x62,],,,0b10010,],;,_iX,:,Array,[,Array,[,Int,,,41,],,,0xB,],),{,},},Class,_,:,_7,{,},<EOF>''',101))

    def test_689(self):
        self.assertTrue(TestLexer.test('''Class _:a{}Class _1_Q:_{Val $1,$_fj_,_:Array [Array [Array [Int ,01],01],0XF];}Class _4_{}Class _:w{}Class _{}Class _:_{}''','''Class,_,:,a,{,},Class,_1_Q,:,_,{,Val,$1,,,$_fj_,,,_,:,Array,[,Array,[,Array,[,Int,,,01,],,,01,],,,0XF,],;,},Class,_4_,{,},Class,_,:,w,{,},Class,_,{,},Class,_,:,_,{,},<EOF>''',101))

    def test_690(self):
        self.assertTrue(TestLexer.test('''Class SI:r2H{_YY__(K:Array [Float ,47];_:Array [Array [String ,0XD],0X2_E_0_5];_,a:Array [Array [Int ,0x4],0XD]){} }''','''Class,SI,:,r2H,{,_YY__,(,K,:,Array,[,Float,,,47,],;,_,:,Array,[,Array,[,String,,,0XD,],,,0X2E05,],;,_,,,a,:,Array,[,Array,[,Int,,,0x4,],,,0XD,],),{,},},<EOF>''',101))

    def test_691(self):
        self.assertTrue(TestLexer.test('''Class Q_:oMn_{$M(e7_,_yH,Q,K_,_:_;G,e,a,_,_4_:Array [Array [Float ,5],89];_:Array [Boolean ,0143];_4:d_9_d;__,E_r4_04__2,C:_a6){}$_6(y:_;_,__2,_:String ){} }''','''Class,Q_,:,oMn_,{,$M,(,e7_,,,_yH,,,Q,,,K_,,,_,:,_,;,G,,,e,,,a,,,_,,,_4_,:,Array,[,Array,[,Float,,,5,],,,89,],;,_,:,Array,[,Boolean,,,0143,],;,_4,:,d_9_d,;,__,,,E_r4_04__2,,,C,:,_a6,),{,},$_6,(,y,:,_,;,_,,,__2,,,_,:,String,),{,},},<EOF>''',101))

    def test_692(self):
        self.assertTrue(TestLexer.test('''Class T1W{Val _3:_;Destructor (){}Destructor (){Continue ;}Destructor (){} }Class II{}Class dr:_{}Class _:c___{Var $_:u;Var _,_:String ;}Class ____:_{}Class _61me:p{}''','''Class,T1W,{,Val,_3,:,_,;,Destructor,(,),{,},Destructor,(,),{,Continue,;,},Destructor,(,),{,},},Class,II,{,},Class,dr,:,_,{,},Class,_,:,c___,{,Var,$_,:,u,;,Var,_,,,_,:,String,;,},Class,____,:,_,{,},Class,_61me,:,p,{,},<EOF>''',101))

    def test_693(self):
        self.assertTrue(TestLexer.test('''Class yY{mq0_M(___,_,__,S,_2:Array [Array [Boolean ,04],0B1_0_1_1];s,aq:String ){} }Class _74{Var $_:Array [Int ,05_7];}''','''Class,yY,{,mq0_M,(,___,,,_,,,__,,,S,,,_2,:,Array,[,Array,[,Boolean,,,04,],,,0B1011,],;,s,,,aq,:,String,),{,},},Class,_74,{,Var,$_,:,Array,[,Int,,,057,],;,},<EOF>''',101))

    def test_694(self):
        self.assertTrue(TestLexer.test('''Class O{Constructor (){}$1(___:Array [Array [Array [Float ,99],07_1],0X9_1_4E];S_1431:Array [Boolean ,4];_:tl){}Constructor (){} }''','''Class,O,{,Constructor,(,),{,},$1,(,___,:,Array,[,Array,[,Array,[,Float,,,99,],,,071,],,,0X914E,],;,S_1431,:,Array,[,Boolean,,,4,],;,_,:,tl,),{,},Constructor,(,),{,},},<EOF>''',101))

    def test_695(self):
        self.assertTrue(TestLexer.test('''Class s9{Constructor (_I_:D_;L_,_:Array [Array [Array [Float ,0b11],1821],0B1010110]){Val _1T_:Array [Int ,0B1_1];} }''','''Class,s9,{,Constructor,(,_I_,:,D_,;,L_,,,_,:,Array,[,Array,[,Array,[,Float,,,0b11,],,,1821,],,,0B1010110,],),{,Val,_1T_,:,Array,[,Int,,,0B11,],;,},},<EOF>''',101))

    def test_696(self):
        self.assertTrue(TestLexer.test('''Class h:Y_{$D(H_:Array [Float ,0b1];_,_,f_,Y,_,q,a,_:Array [Float ,48];__P_:Array [String ,0106];zX:Array [Boolean ,994_85_4]){} }''','''Class,h,:,Y_,{,$D,(,H_,:,Array,[,Float,,,0b1,],;,_,,,_,,,f_,,,Y,,,_,,,q,,,a,,,_,:,Array,[,Float,,,48,],;,__P_,:,Array,[,String,,,0106,],;,zX,:,Array,[,Boolean,,,994854,],),{,},},<EOF>''',101))

    def test_697(self):
        self.assertTrue(TestLexer.test('''Class F:g__9{}Class n:__{Val $_2,$7:Array [Array [Float ,0X2FA],40];Destructor (){}$V86_(r_v0_849,E3:Int ;___5:String ){} }Class Z{V__(){} }''','''Class,F,:,g__9,{,},Class,n,:,__,{,Val,$_2,,,$7,:,Array,[,Array,[,Float,,,0X2FA,],,,40,],;,Destructor,(,),{,},$V86_,(,r_v0_849,,,E3,:,Int,;,___5,:,String,),{,},},Class,Z,{,V__,(,),{,},},<EOF>''',101))

    def test_698(self):
        self.assertTrue(TestLexer.test('''Class _K_{}Class _{Var $s7_:Float ;Destructor (){}B(h,l:g1b){Var _,_:_;}Var NcKd,_3_,F,j_,$K,V:String ;Var $_X_:Array [Array [Int ,05],14];}''','''Class,_K_,{,},Class,_,{,Var,$s7_,:,Float,;,Destructor,(,),{,},B,(,h,,,l,:,g1b,),{,Var,_,,,_,:,_,;,},Var,NcKd,,,_3_,,,F,,,j_,,,$K,,,V,:,String,;,Var,$_X_,:,Array,[,Array,[,Int,,,05,],,,14,],;,},<EOF>''',101))

    def test_699(self):
        self.assertTrue(TestLexer.test('''Class _{}Class x{Constructor (v:Array [Array [Array [Array [Boolean ,0B110],24],24],0114];___p,X_TD,l,_t_:Int ;_8,J_i,M,n5,_2:String ){} }''','''Class,_,{,},Class,x,{,Constructor,(,v,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,0B110,],,,24,],,,24,],,,0114,],;,___p,,,X_TD,,,l,,,_t_,:,Int,;,_8,,,J_i,,,M,,,n5,,,_2,:,String,),{,},},<EOF>''',101))

    def test_700(self):
        self.assertTrue(TestLexer.test('''Class x:U{$_(kDZ,_:Array [String ,030];_:Array [String ,031_72];B,__PW:Int ;w_3_:Int ;v,U,_:String ;_:String ){} }''','''Class,x,:,U,{,$_,(,kDZ,,,_,:,Array,[,String,,,030,],;,_,:,Array,[,String,,,03172,],;,B,,,__PW,:,Int,;,w_3_,:,Int,;,v,,,U,,,_,:,String,;,_,:,String,),{,},},<EOF>''',101))

    def test_701(self):
        self.assertTrue(TestLexer.test('''Class om{Destructor (){Break ;{} }}Class _{Destructor (){Break ;}_(){}M(r,i,ll:Array [Array [Array [Int ,0120],92],0x62]){Return ;}Val _,_:_;}Class D_:b0{Constructor (){} }Class __6_:_pj__{}''','''Class,om,{,Destructor,(,),{,Break,;,{,},},},Class,_,{,Destructor,(,),{,Break,;,},_,(,),{,},M,(,r,,,i,,,ll,:,Array,[,Array,[,Array,[,Int,,,0120,],,,92,],,,0x62,],),{,Return,;,},Val,_,,,_,:,_,;,},Class,D_,:,b0,{,Constructor,(,),{,},},Class,__6_,:,_pj__,{,},<EOF>''',101))

    def test_702(self):
        self.assertTrue(TestLexer.test('''Class S:_{}Class LH2__:v{Var _,_oq,$Oz:Boolean ;}Class A{$T(_706,_,u_,_:Array [Array [Array [Array [Array [Array [Array [Array [Boolean ,0127],0XC],14],07_45_42],89],0XB],0b111011],0127];bJh_0q:Array [Boolean ,14]){Break ;} }''','''Class,S,:,_,{,},Class,LH2__,:,v,{,Var,_,,,_oq,,,$Oz,:,Boolean,;,},Class,A,{,$T,(,_706,,,_,,,u_,,,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0127,],,,0XC,],,,14,],,,074542,],,,89,],,,0XB,],,,0b111011,],,,0127,],;,bJh_0q,:,Array,[,Boolean,,,14,],),{,Break,;,},},<EOF>''',101))

    def test_703(self):
        self.assertTrue(TestLexer.test('''Class M_:hT9{}Class T{Destructor (){}Constructor (X:___;Z,V9:Float ;_U:String ;q:I){}Var A,$LCEk_,$_1:Array [Array [Boolean ,0xA],04];}''','''Class,M_,:,hT9,{,},Class,T,{,Destructor,(,),{,},Constructor,(,X,:,___,;,Z,,,V9,:,Float,;,_U,:,String,;,q,:,I,),{,},Var,A,,,$LCEk_,,,$_1,:,Array,[,Array,[,Boolean,,,0xA,],,,04,],;,},<EOF>''',101))

    def test_704(self):
        self.assertTrue(TestLexer.test('''Class _{Constructor (L,m2:Int ;_3,_,_,_,_:Array [Array [Float ,76],0X4];_p,w,B,_:Array [Array [Float ,064],712];iH,m_:Int ){}Var f:Array [Array [Array [String ,63_8],0B110001],2];}Class _7:x{Val _,$_H2:Array [Array [Float ,0X55],8];}Class _4:jz{Destructor (){}Constructor (){}Destructor (){} }''','''Class,_,{,Constructor,(,L,,,m2,:,Int,;,_3,,,_,,,_,,,_,,,_,:,Array,[,Array,[,Float,,,76,],,,0X4,],;,_p,,,w,,,B,,,_,:,Array,[,Array,[,Float,,,064,],,,712,],;,iH,,,m_,:,Int,),{,},Var,f,:,Array,[,Array,[,Array,[,String,,,638,],,,0B110001,],,,2,],;,},Class,_7,:,x,{,Val,_,,,$_H2,:,Array,[,Array,[,Float,,,0X55,],,,8,],;,},Class,_4,:,jz,{,Destructor,(,),{,},Constructor,(,),{,},Destructor,(,),{,},},<EOF>''',101))

    def test_705(self):
        self.assertTrue(TestLexer.test('''Class __8a:_{Constructor (_,F:Array [String ,100];vE_,K43:_;Eq:Int ;__5K,q:Int ){} }Class o256:c{Val _,_,$5:Array [Int ,0B1_0];}Class V:_{}Class __:EI2{}Class I_{}''','''Class,__8a,:,_,{,Constructor,(,_,,,F,:,Array,[,String,,,100,],;,vE_,,,K43,:,_,;,Eq,:,Int,;,__5K,,,q,:,Int,),{,},},Class,o256,:,c,{,Val,_,,,_,,,$5,:,Array,[,Int,,,0B10,],;,},Class,V,:,_,{,},Class,__,:,EI2,{,},Class,I_,{,},<EOF>''',101))

    def test_706(self):
        self.assertTrue(TestLexer.test('''Class X{}Class _{Destructor (){} }Class j_:H{}Class _{Var T:_;}Class q:__4r{Val A,$_o,YI,$1,$_X,_:Array [Array [Float ,063],61];}Class z3_{Var $v:Float ;}''','''Class,X,{,},Class,_,{,Destructor,(,),{,},},Class,j_,:,H,{,},Class,_,{,Var,T,:,_,;,},Class,q,:,__4r,{,Val,A,,,$_o,,,YI,,,$1,,,$_X,,,_,:,Array,[,Array,[,Float,,,063,],,,61,],;,},Class,z3_,{,Var,$v,:,Float,;,},<EOF>''',101))

    def test_707(self):
        self.assertTrue(TestLexer.test('''Class _{}Class e4_K_{}Class __{Constructor (_,U_G,x6_68,_,V:Boolean ;_,pn5:_W;H,b_5_S:e;_7q_:Float ){}Val $_:_;Destructor (){}Var _:Float ;}''','''Class,_,{,},Class,e4_K_,{,},Class,__,{,Constructor,(,_,,,U_G,,,x6_68,,,_,,,V,:,Boolean,;,_,,,pn5,:,_W,;,H,,,b_5_S,:,e,;,_7q_,:,Float,),{,},Val,$_,:,_,;,Destructor,(,),{,},Var,_,:,Float,;,},<EOF>''',101))

    def test_708(self):
        self.assertTrue(TestLexer.test('''Class _9{_(){} }Class W979{}Class i_3k2_X{a(_8571_:Int ;sbm_,_:Array [Int ,0X4_A]){Continue ;}$5(){Break ;} }Class M:q1{Var $_:Qv;}''','''Class,_9,{,_,(,),{,},},Class,W979,{,},Class,i_3k2_X,{,a,(,_8571_,:,Int,;,sbm_,,,_,:,Array,[,Int,,,0X4A,],),{,Continue,;,},$5,(,),{,Break,;,},},Class,M,:,q1,{,Var,$_,:,Qv,;,},<EOF>''',101))

    def test_709(self):
        self.assertTrue(TestLexer.test('''Class __7{Val $7_4:Int ;}Class __p_9nb8{Constructor (_:Array [Array [Array [Array [Float ,92],0X21],0X7],590]){ {} }}''','''Class,__7,{,Val,$7_4,:,Int,;,},Class,__p_9nb8,{,Constructor,(,_,:,Array,[,Array,[,Array,[,Array,[,Float,,,92,],,,0X21,],,,0X7,],,,590,],),{,{,},},},<EOF>''',101))

    def test_710(self):
        self.assertTrue(TestLexer.test('''Class _:_{}Class D:_{Val Th_:_T_;Var $S,_:Array [Array [Array [Array [Array [Array [Array [String ,0xE],0XAE32],0xA],02],06_1],0b101000],3_99_422];Destructor (){} }''','''Class,_,:,_,{,},Class,D,:,_,{,Val,Th_,:,_T_,;,Var,$S,,,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0xE,],,,0XAE32,],,,0xA,],,,02,],,,061,],,,0b101000,],,,399422,],;,Destructor,(,),{,},},<EOF>''',101))

    def test_711(self):
        self.assertTrue(TestLexer.test('''Class G:_W{}Class Bv:_{}Class _0M_:X4{Constructor (____1v:E69;M,_6:String ){Var h:Array [Array [Array [Int ,0X4],9_7_6],0B100111];} }Class _6{Val $_:Boolean ;}Class _796_{}''','''Class,G,:,_W,{,},Class,Bv,:,_,{,},Class,_0M_,:,X4,{,Constructor,(,____1v,:,E69,;,M,,,_6,:,String,),{,Var,h,:,Array,[,Array,[,Array,[,Int,,,0X4,],,,976,],,,0B100111,],;,},},Class,_6,{,Val,$_,:,Boolean,;,},Class,_796_,{,},<EOF>''',101))

    def test_712(self):
        self.assertTrue(TestLexer.test('''Class e{}Class h52c{Val pW,$C,_7:Array [Float ,05_2_3];l(_:__4;n:Array [Array [Array [Float ,0x1],61],0X57];nP1:Float ;v,h80,_:eq_k_){} }Class _:T{}Class I1:__{}''','''Class,e,{,},Class,h52c,{,Val,pW,,,$C,,,_7,:,Array,[,Float,,,0523,],;,l,(,_,:,__4,;,n,:,Array,[,Array,[,Array,[,Float,,,0x1,],,,61,],,,0X57,],;,nP1,:,Float,;,v,,,h80,,,_,:,eq_k_,),{,},},Class,_,:,T,{,},Class,I1,:,__,{,},<EOF>''',101))

    def test_713(self):
        self.assertTrue(TestLexer.test('''Class ktwC:____K{$4t_(_m:Array [Array [Array [Array [Array [Float ,0XA],0b1011101],065],0b1],84];MX,Ry,UQ__w4,k_m,_:Array [Array [Array [Array [Int ,0x5B],0b1],06_33],84];_L42,o22_:Array [Float ,0b1011101];_,j_:Float ;_,D,_,mr_b_:Array [Boolean ,0B1000000]){} }''','''Class,ktwC,:,____K,{,$4t_,(,_m,:,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0XA,],,,0b1011101,],,,065,],,,0b1,],,,84,],;,MX,,,Ry,,,UQ__w4,,,k_m,,,_,:,Array,[,Array,[,Array,[,Array,[,Int,,,0x5B,],,,0b1,],,,0633,],,,84,],;,_L42,,,o22_,:,Array,[,Float,,,0b1011101,],;,_,,,j_,:,Float,;,_,,,D,,,_,,,mr_b_,:,Array,[,Boolean,,,0B1000000,],),{,},},<EOF>''',101))

    def test_714(self):
        self.assertTrue(TestLexer.test('''Class _h{Var r,_,_0,$r:Array [Array [Int ,0B1000],0X1F];}Class vk_RO{Destructor (){} }Class s7U{}Class k:Qr_{Val o__:Array [Array [Boolean ,5],100];}''','''Class,_h,{,Var,r,,,_,,,_0,,,$r,:,Array,[,Array,[,Int,,,0B1000,],,,0X1F,],;,},Class,vk_RO,{,Destructor,(,),{,},},Class,s7U,{,},Class,k,:,Qr_,{,Val,o__,:,Array,[,Array,[,Boolean,,,5,],,,100,],;,},<EOF>''',101))

    def test_715(self):
        self.assertTrue(TestLexer.test('''Class _X{$32J6(_V,V:Array [Array [Int ,41],0X34]){}Val $7,$Z,X_,$_,$B7n3_,$_9hf_5:_4_;Val f_,_:Array [Int ,0X34];}Class P___{}Class m:__{Var _J4_p6h,$bp,_:Array [Int ,0137];Var K,Z,_:Array [Array [Array [Float ,0B1],0b1],0B1110];}''','''Class,_X,{,$32J6,(,_V,,,V,:,Array,[,Array,[,Int,,,41,],,,0X34,],),{,},Val,$7,,,$Z,,,X_,,,$_,,,$B7n3_,,,$_9hf_5,:,_4_,;,Val,f_,,,_,:,Array,[,Int,,,0X34,],;,},Class,P___,{,},Class,m,:,__,{,Var,_J4_p6h,,,$bp,,,_,:,Array,[,Int,,,0137,],;,Var,K,,,Z,,,_,:,Array,[,Array,[,Array,[,Float,,,0B1,],,,0b1,],,,0B1110,],;,},<EOF>''',101))

    def test_716(self):
        self.assertTrue(TestLexer.test('''Class ETC:J{}Class l{Constructor (){}Destructor (){}Constructor (_,D_:Float ){ {{}Continue ;Continue ;}Return ;Continue ;} }''','''Class,ETC,:,J,{,},Class,l,{,Constructor,(,),{,},Destructor,(,),{,},Constructor,(,_,,,D_,:,Float,),{,{,{,},Continue,;,Continue,;,},Return,;,Continue,;,},},<EOF>''',101))

    def test_717(self):
        self.assertTrue(TestLexer.test('''Class N:_{Constructor (_o_7:Z;_,B,f,n6,Y,p0,_:Array [Float ,0b1]){Continue ;}Val __4_w,A:Array [Float ,07];Destructor (){ {} }Destructor (){} }''','''Class,N,:,_,{,Constructor,(,_o_7,:,Z,;,_,,,B,,,f,,,n6,,,Y,,,p0,,,_,:,Array,[,Float,,,0b1,],),{,Continue,;,},Val,__4_w,,,A,:,Array,[,Float,,,07,],;,Destructor,(,),{,{,},},Destructor,(,),{,},},<EOF>''',101))

    def test_718(self):
        self.assertTrue(TestLexer.test('''Class B6l:_{}Class _:_{}Class _EX{$3(){Var z87_,PP,A,_61,H:l_;}Constructor (pt:Int ){}_8_(Q_E28,_:String ;x:Array [Array [Float ,1_6],21];jOC,i_Q:String ;T:Float ){Continue ;} }''','''Class,B6l,:,_,{,},Class,_,:,_,{,},Class,_EX,{,$3,(,),{,Var,z87_,,,PP,,,A,,,_61,,,H,:,l_,;,},Constructor,(,pt,:,Int,),{,},_8_,(,Q_E28,,,_,:,String,;,x,:,Array,[,Array,[,Float,,,16,],,,21,],;,jOC,,,i_Q,:,String,;,T,:,Float,),{,Continue,;,},},<EOF>''',101))

    def test_719(self):
        self.assertTrue(TestLexer.test('''Class __N{}Class _{}Class _{Var R6,N:__;Var _5o3w,$_:_g;Constructor (_Z4u_:Array [Array [Float ,0x5F],8_5_6];E:__;U,__,wDF_,R_:Array [Array [Boolean ,0x5_D],07];z8:Int ;S:__Y){}_(_,A:Array [Float ,0B110_01_0_0_1_00_1];_O:Array [Array [Array [Array [Boolean ,0b1100010],07],02],0X24]){}Var $d:Array [Array [Array [Boolean ,0X24],07],07];}''','''Class,__N,{,},Class,_,{,},Class,_,{,Var,R6,,,N,:,__,;,Var,_5o3w,,,$_,:,_g,;,Constructor,(,_Z4u_,:,Array,[,Array,[,Float,,,0x5F,],,,856,],;,E,:,__,;,U,,,__,,,wDF_,,,R_,:,Array,[,Array,[,Boolean,,,0x5D,],,,07,],;,z8,:,Int,;,S,:,__Y,),{,},_,(,_,,,A,:,Array,[,Float,,,0B11001001001,],;,_O,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,0b1100010,],,,07,],,,02,],,,0X24,],),{,},Var,$d,:,Array,[,Array,[,Array,[,Boolean,,,0X24,],,,07,],,,07,],;,},<EOF>''',101))

    def test_720(self):
        self.assertTrue(TestLexer.test('''Class l{Destructor (){} }Class BgF:_F{Val n_l,z:Array [Array [Float ,1],8_6];Var $3,$rH_:Boolean ;}Class Pc__6:_5A5{Constructor (Rf8:Boolean ){}Constructor (){}$4c69V(){}$l2N(){} }''','''Class,l,{,Destructor,(,),{,},},Class,BgF,:,_F,{,Val,n_l,,,z,:,Array,[,Array,[,Float,,,1,],,,86,],;,Var,$3,,,$rH_,:,Boolean,;,},Class,Pc__6,:,_5A5,{,Constructor,(,Rf8,:,Boolean,),{,},Constructor,(,),{,},$4c69V,(,),{,},$l2N,(,),{,},},<EOF>''',101))

    def test_721(self):
        self.assertTrue(TestLexer.test('''Class HY4W{$_(L:Array [Float ,0B1001000];_:String ;_,qtX,x:Array [Boolean ,94]){}Val $or:Boolean ;$9(h,_9,C,_:String ;ot,_V__,_:Float ){} }Class K{Val _,_k:B;}Class _{Destructor (){}Destructor (){} }''','''Class,HY4W,{,$_,(,L,:,Array,[,Float,,,0B1001000,],;,_,:,String,;,_,,,qtX,,,x,:,Array,[,Boolean,,,94,],),{,},Val,$or,:,Boolean,;,$9,(,h,,,_9,,,C,,,_,:,String,;,ot,,,_V__,,,_,:,Float,),{,},},Class,K,{,Val,_,,,_k,:,B,;,},Class,_,{,Destructor,(,),{,},Destructor,(,),{,},},<EOF>''',101))

    def test_722(self):
        self.assertTrue(TestLexer.test('''Class ___S3{T(){}Constructor (rf,A___qU__:Array [Array [Boolean ,0XC],0b1];_f:Array [Float ,010]){}Var _U90,$z,$__,C0_,$_:Array [Array [Array [Array [String ,0xB],98],0X9_D],98];Var $x:c7;R(){} }''','''Class,___S3,{,T,(,),{,},Constructor,(,rf,,,A___qU__,:,Array,[,Array,[,Boolean,,,0XC,],,,0b1,],;,_f,:,Array,[,Float,,,010,],),{,},Var,_U90,,,$z,,,$__,,,C0_,,,$_,:,Array,[,Array,[,Array,[,Array,[,String,,,0xB,],,,98,],,,0X9D,],,,98,],;,Var,$x,:,c7,;,R,(,),{,},},<EOF>''',101))

    def test_723(self):
        self.assertTrue(TestLexer.test('''Class __:B{Destructor (){Continue ;Return ;}Constructor (m,S,I1074ho:String ;__x:Array [Array [Array [Float ,0X7_0],81],0b11]){} }Class P:m{}''','''Class,__,:,B,{,Destructor,(,),{,Continue,;,Return,;,},Constructor,(,m,,,S,,,I1074ho,:,String,;,__x,:,Array,[,Array,[,Array,[,Float,,,0X70,],,,81,],,,0b11,],),{,},},Class,P,:,m,{,},<EOF>''',101))

    def test_724(self):
        self.assertTrue(TestLexer.test('''Class _{Constructor (S,Q,__1,_:Float ){} }Class dT{Var _d_,$1K,_:Array [String ,212];}Class U{Destructor (){} }Class _{}''','''Class,_,{,Constructor,(,S,,,Q,,,__1,,,_,:,Float,),{,},},Class,dT,{,Var,_d_,,,$1K,,,_,:,Array,[,String,,,212,],;,},Class,U,{,Destructor,(,),{,},},Class,_,{,},<EOF>''',101))

    def test_725(self):
        self.assertTrue(TestLexer.test('''Class _N9Uc:__{Constructor (Z:Boolean ;_3,eR_6P,_,_:Array [Array [Array [String ,71_6_4],0x31],0X25C8_4ADB];we:Array [Int ,0b11001]){Continue ;Return ;Break ;Continue ;} }Class _T:x5{_9p(_:f;Y:b){} }''','''Class,_N9Uc,:,__,{,Constructor,(,Z,:,Boolean,;,_3,,,eR_6P,,,_,,,_,:,Array,[,Array,[,Array,[,String,,,7164,],,,0x31,],,,0X25C84ADB,],;,we,:,Array,[,Int,,,0b11001,],),{,Continue,;,Return,;,Break,;,Continue,;,},},Class,_T,:,x5,{,_9p,(,_,:,f,;,Y,:,b,),{,},},<EOF>''',101))

    def test_726(self):
        self.assertTrue(TestLexer.test('''Class __6m{Constructor (_,_:Boolean ;_:Array [Array [Array [Array [Array [Boolean ,0B1000110],0XA1D3_A],05_7],05],0B1000110];H4,_,_,_:Int ){} }Class a:b{}''','''Class,__6m,{,Constructor,(,_,,,_,:,Boolean,;,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0B1000110,],,,0XA1D3A,],,,057,],,,05,],,,0B1000110,],;,H4,,,_,,,_,,,_,:,Int,),{,},},Class,a,:,b,{,},<EOF>''',101))

    def test_727(self):
        self.assertTrue(TestLexer.test('''Class _{Constructor (_,f:Boolean ;j2,_p:_O8_X0_;_,__,C,U,p,_1_:Array [Array [Array [Float ,0X6],0xD],0XF];r_,u__:Boolean ){} }Class OJ_{}Class X5_:_{Destructor (){} }''','''Class,_,{,Constructor,(,_,,,f,:,Boolean,;,j2,,,_p,:,_O8_X0_,;,_,,,__,,,C,,,U,,,p,,,_1_,:,Array,[,Array,[,Array,[,Float,,,0X6,],,,0xD,],,,0XF,],;,r_,,,u__,:,Boolean,),{,},},Class,OJ_,{,},Class,X5_,:,_,{,Destructor,(,),{,},},<EOF>''',101))

    def test_728(self):
        self.assertTrue(TestLexer.test('''Class _4:_{Val $15_,_,$_:_;}Class K2_{Var $_2:_;Ty1n_(_7Ye,_23_2:String ;_:___;Y,_:Array [String ,80]){} }Class _:_7{}''','''Class,_4,:,_,{,Val,$15_,,,_,,,$_,:,_,;,},Class,K2_,{,Var,$_2,:,_,;,Ty1n_,(,_7Ye,,,_23_2,:,String,;,_,:,___,;,Y,,,_,:,Array,[,String,,,80,],),{,},},Class,_,:,_7,{,},<EOF>''',101))

    def test_729(self):
        self.assertTrue(TestLexer.test('''Class __:_2_{}Class _3{Destructor (){Continue ;}Constructor (){New W1().r().X.W9v();}Destructor (){Continue ;} }''','''Class,__,:,_2_,{,},Class,_3,{,Destructor,(,),{,Continue,;,},Constructor,(,),{,New,W1,(,),.,r,(,),.,X,.,W9v,(,),;,},Destructor,(,),{,Continue,;,},},<EOF>''',101))

    def test_730(self):
        self.assertTrue(TestLexer.test('''Class __:__{Constructor (_,_9V_:Int ){Return ;} }Class _{}Class _2T_v:_{Var $V:Array [Array [Array [Array [String ,0b100_1_1_1_1],035],0B1_11],75_7];}''','''Class,__,:,__,{,Constructor,(,_,,,_9V_,:,Int,),{,Return,;,},},Class,_,{,},Class,_2T_v,:,_,{,Var,$V,:,Array,[,Array,[,Array,[,Array,[,String,,,0b1001111,],,,035,],,,0B111,],,,757,],;,},<EOF>''',101))

    def test_731(self):
        self.assertTrue(TestLexer.test('''Class _co1_:Hh__8{Var $9,_5:Array [Int ,0B101];}Class c:_{Constructor (_4b_5w,_:Array [Float ,0x6_4_7]){}Var $9:_;Val j:_4pXS;}''','''Class,_co1_,:,Hh__8,{,Var,$9,,,_5,:,Array,[,Int,,,0B101,],;,},Class,c,:,_,{,Constructor,(,_4b_5w,,,_,:,Array,[,Float,,,0x647,],),{,},Var,$9,:,_,;,Val,j,:,_4pXS,;,},<EOF>''',101))

    def test_732(self):
        self.assertTrue(TestLexer.test('''Class JSR56:t__5_0{}Class _:z{$4(_Q,_qp,_:Array [Boolean ,0b1100100];_,_:Boolean ;p,_,fI:_Nl){Continue ;_::$_7__IT_();}$l(_:B){} }''','''Class,JSR56,:,t__5_0,{,},Class,_,:,z,{,$4,(,_Q,,,_qp,,,_,:,Array,[,Boolean,,,0b1100100,],;,_,,,_,:,Boolean,;,p,,,_,,,fI,:,_Nl,),{,Continue,;,_,::,$_7__IT_,(,),;,},$l,(,_,:,B,),{,},},<EOF>''',101))

    def test_733(self):
        self.assertTrue(TestLexer.test('''Class l_:Npp8{}Class __xb{}Class b_:__0{}Class c_O:i7{Val $_P9__:Array [Boolean ,043];Var $5,$Yx:_;Constructor (O:_4;_:_7__7;WC3q_K__:String ;al,_x,_,_,_:Array [Array [Array [Int ,78],5],0b1];vu,__,_:String ;_,j____s:Array [Int ,78]){} }Class _9:_8F{}Class f:w{}Class _:_{}Class y:_{Destructor (){} }''','''Class,l_,:,Npp8,{,},Class,__xb,{,},Class,b_,:,__0,{,},Class,c_O,:,i7,{,Val,$_P9__,:,Array,[,Boolean,,,043,],;,Var,$5,,,$Yx,:,_,;,Constructor,(,O,:,_4,;,_,:,_7__7,;,WC3q_K__,:,String,;,al,,,_x,,,_,,,_,,,_,:,Array,[,Array,[,Array,[,Int,,,78,],,,5,],,,0b1,],;,vu,,,__,,,_,:,String,;,_,,,j____s,:,Array,[,Int,,,78,],),{,},},Class,_9,:,_8F,{,},Class,f,:,w,{,},Class,_,:,_,{,},Class,y,:,_,{,Destructor,(,),{,},},<EOF>''',101))

    def test_734(self):
        self.assertTrue(TestLexer.test('''Class J{}Class _7_0_6:X_{Destructor (){Break ;} }Class _h{}Class K:x{Val _,$8_,V_:Array [Float ,040];}Class J{Val c:Float ;}''','''Class,J,{,},Class,_7_0_6,:,X_,{,Destructor,(,),{,Break,;,},},Class,_h,{,},Class,K,:,x,{,Val,_,,,$8_,,,V_,:,Array,[,Float,,,040,],;,},Class,J,{,Val,c,:,Float,;,},<EOF>''',101))

    def test_735(self):
        self.assertTrue(TestLexer.test('''Class e{Constructor (r:Boolean ;_:String ;_:Array [Boolean ,9_2];_7,_c_9:String ;_,_E48,U,__gr,L7_:Int ;O:C;___I5_9_r,_w,Gn7__2_S2q,f_,_,_:Array [Array [Array [Array [Array [Array [Array [Array [Array [Boolean ,01],07],0B100011],1],0xB],0b1],01],0B100011],0b111110];j,_,ni,__:String ;U__,_:_72n){} }''','''Class,e,{,Constructor,(,r,:,Boolean,;,_,:,String,;,_,:,Array,[,Boolean,,,92,],;,_7,,,_c_9,:,String,;,_,,,_E48,,,U,,,__gr,,,L7_,:,Int,;,O,:,C,;,___I5_9_r,,,_w,,,Gn7__2_S2q,,,f_,,,_,,,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,01,],,,07,],,,0B100011,],,,1,],,,0xB,],,,0b1,],,,01,],,,0B100011,],,,0b111110,],;,j,,,_,,,ni,,,__,:,String,;,U__,,,_,:,_72n,),{,},},<EOF>''',101))

    def test_736(self):
        self.assertTrue(TestLexer.test('''Class __{}Class y_{Destructor (){Continue ;}$6_(){Var mki_:Array [Array [Array [Array [Int ,9],043],0X3C],0x3F];} }''','''Class,__,{,},Class,y_,{,Destructor,(,),{,Continue,;,},$6_,(,),{,Var,mki_,:,Array,[,Array,[,Array,[,Array,[,Int,,,9,],,,043,],,,0X3C,],,,0x3F,],;,},},<EOF>''',101))

    def test_737(self):
        self.assertTrue(TestLexer.test('''Class _8{Val _:_3;BF_1_n5_ic(q,g,s_:Array [Float ,076]){} }Class Y___:s{Constructor (__E7,_qU51,_7:String ){s::$0();}Val _7,_H:_;Val n,_4_I_WRQ6,l:Int ;Val $7_:_;}''','''Class,_8,{,Val,_,:,_3,;,BF_1_n5_ic,(,q,,,g,,,s_,:,Array,[,Float,,,076,],),{,},},Class,Y___,:,s,{,Constructor,(,__E7,,,_qU51,,,_7,:,String,),{,s,::,$0,(,),;,},Val,_7,,,_H,:,_,;,Val,n,,,_4_I_WRQ6,,,l,:,Int,;,Val,$7_,:,_,;,},<EOF>''',101))

    def test_738(self):
        self.assertTrue(TestLexer.test('''Class _Z:Q__{}Class _OR_{Var _:Boolean ;}Class G:t{Constructor (){} }Class X{Constructor (){} }Class _R_{}Class h_1l_{}Class __p{$X(){Continue ;} }''','''Class,_Z,:,Q__,{,},Class,_OR_,{,Var,_,:,Boolean,;,},Class,G,:,t,{,Constructor,(,),{,},},Class,X,{,Constructor,(,),{,},},Class,_R_,{,},Class,h_1l_,{,},Class,__p,{,$X,(,),{,Continue,;,},},<EOF>''',101))

    def test_739(self):
        self.assertTrue(TestLexer.test('''Class _5D:l_{Var $_,$3,$P,$F,c,$7,__C,ss1,$c1,N:Array [Array [Int ,0b1010_0],0x1];Val mQ,$Y:S9;}Class d0g_0N3_:M{}''','''Class,_5D,:,l_,{,Var,$_,,,$3,,,$P,,,$F,,,c,,,$7,,,__C,,,ss1,,,$c1,,,N,:,Array,[,Array,[,Int,,,0b10100,],,,0x1,],;,Val,mQ,,,$Y,:,S9,;,},Class,d0g_0N3_,:,M,{,},<EOF>''',101))

    def test_740(self):
        self.assertTrue(TestLexer.test('''Class _{Var v7:Array [Array [Array [Array [Array [Array [Array [Array [Int ,73],0B1000000],0B1],0X3],0X2C],0X48],0B1000000],0XD];}Class f_{$7_(){} }''','''Class,_,{,Var,v7,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,73,],,,0B1000000,],,,0B1,],,,0X3,],,,0X2C,],,,0X48,],,,0B1000000,],,,0XD,],;,},Class,f_,{,$7_,(,),{,},},<EOF>''',101))

    def test_741(self):
        self.assertTrue(TestLexer.test('''Class URK:_G{Val $__z_P:Array [String ,0B1];I_Fw(u_:Array [Int ,0b1];___:Array [Array [Boolean ,41],0136];a950J40e8g_7:L;K_,_,K,e,Y8Q_t_7E_5X,_,C,Q,_8_:_X){} }''','''Class,URK,:,_G,{,Val,$__z_P,:,Array,[,String,,,0B1,],;,I_Fw,(,u_,:,Array,[,Int,,,0b1,],;,___,:,Array,[,Array,[,Boolean,,,41,],,,0136,],;,a950J40e8g_7,:,L,;,K_,,,_,,,K,,,e,,,Y8Q_t_7E_5X,,,_,,,C,,,Q,,,_8_,:,_X,),{,},},<EOF>''',101))

    def test_742(self):
        self.assertTrue(TestLexer.test('''Class _8:__n8Gp{$7(Ll_,P:Array [Array [String ,0115],9]){} }Class _{Val b:Array [Boolean ,0xA4];Destructor (){} }Class k{Destructor (){} }''','''Class,_8,:,__n8Gp,{,$7,(,Ll_,,,P,:,Array,[,Array,[,String,,,0115,],,,9,],),{,},},Class,_,{,Val,b,:,Array,[,Boolean,,,0xA4,],;,Destructor,(,),{,},},Class,k,{,Destructor,(,),{,},},<EOF>''',101))

    def test_743(self):
        self.assertTrue(TestLexer.test('''Class r{Var $_:_2;}Class O{Var $___:Array [Array [Array [Array [Float ,05_16_2],0x6_7],82],074];}Class U4__:_5{}''','''Class,r,{,Var,$_,:,_2,;,},Class,O,{,Var,$___,:,Array,[,Array,[,Array,[,Array,[,Float,,,05162,],,,0x67,],,,82,],,,074,],;,},Class,U4__,:,_5,{,},<EOF>''',101))

    def test_744(self):
        self.assertTrue(TestLexer.test('''Class _{}Class L0:l{l_(_:_4;M_:Array [Array [Float ,0B1],0X43];_,I:Boolean ;OW:Array [Array [Array [Array [Array [Float ,04],87],0b1],073],0X5];_:_){} }''','''Class,_,{,},Class,L0,:,l,{,l_,(,_,:,_4,;,M_,:,Array,[,Array,[,Float,,,0B1,],,,0X43,],;,_,,,I,:,Boolean,;,OW,:,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,04,],,,87,],,,0b1,],,,073,],,,0X5,],;,_,:,_,),{,},},<EOF>''',101))

    def test_745(self):
        self.assertTrue(TestLexer.test('''Class _:__{}Class b8_qk{}Class Xj{}Class _dz0:V_{Val $_N_F8,E6,B,$9,_,z,Q4Ip:Array [Array [Boolean ,4],0b1];Destructor (){ {} }Var $0:Array [Array [String ,70],036];}''','''Class,_,:,__,{,},Class,b8_qk,{,},Class,Xj,{,},Class,_dz0,:,V_,{,Val,$_N_F8,,,E6,,,B,,,$9,,,_,,,z,,,Q4Ip,:,Array,[,Array,[,Boolean,,,4,],,,0b1,],;,Destructor,(,),{,{,},},Var,$0,:,Array,[,Array,[,String,,,70,],,,036,],;,},<EOF>''',101))

    def test_746(self):
        self.assertTrue(TestLexer.test('''Class F{Constructor (__3:Array [Array [Float ,91],0xE_3_F];_,X5,R_,_5,m_P5:_;_:_s;w,_:Array [Array [Int ,91],91];B:Float ;aM1,z2:HF7;Im1,_:Boolean ){} }''','''Class,F,{,Constructor,(,__3,:,Array,[,Array,[,Float,,,91,],,,0xE3F,],;,_,,,X5,,,R_,,,_5,,,m_P5,:,_,;,_,:,_s,;,w,,,_,:,Array,[,Array,[,Int,,,91,],,,91,],;,B,:,Float,;,aM1,,,z2,:,HF7,;,Im1,,,_,:,Boolean,),{,},},<EOF>''',101))

    def test_747(self):
        self.assertTrue(TestLexer.test('''Class _795{Destructor (){}Constructor (s:String ;_,_,u_:__4Z465b2_;_w_m,__,x,_j,_:Boolean ;__:Array [Array [Array [Array [Float ,0X30],52],0X30],0X5_6];_0dH,w,k,_,_:Float ){} }''','''Class,_795,{,Destructor,(,),{,},Constructor,(,s,:,String,;,_,,,_,,,u_,:,__4Z465b2_,;,_w_m,,,__,,,x,,,_j,,,_,:,Boolean,;,__,:,Array,[,Array,[,Array,[,Array,[,Float,,,0X30,],,,52,],,,0X30,],,,0X56,],;,_0dH,,,w,,,k,,,_,,,_,:,Float,),{,},},<EOF>''',101))

    def test_748(self):
        self.assertTrue(TestLexer.test('''Class s8:Fe{Destructor (){Continue ;}Val _2:Array [Array [Array [Float ,0b100111],0x37],0B1];Destructor (){}Var $P:F_2;}''','''Class,s8,:,Fe,{,Destructor,(,),{,Continue,;,},Val,_2,:,Array,[,Array,[,Array,[,Float,,,0b100111,],,,0x37,],,,0B1,],;,Destructor,(,),{,},Var,$P,:,F_2,;,},<EOF>''',101))

    def test_749(self):
        self.assertTrue(TestLexer.test('''Class l{}Class MTn:d{__(V,_Lj,i7:r;__x6,qT__:Array [Array [Array [Array [Array [Float ,5],0XDF_08D_8],0x51],063],07];_,b6_s:Float ){}Val S,_3:Int ;Var Z____,q____:Array [Float ,0x324_0];}''','''Class,l,{,},Class,MTn,:,d,{,__,(,V,,,_Lj,,,i7,:,r,;,__x6,,,qT__,:,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,5,],,,0XDF08D8,],,,0x51,],,,063,],,,07,],;,_,,,b6_s,:,Float,),{,},Val,S,,,_3,:,Int,;,Var,Z____,,,q____,:,Array,[,Float,,,0x3240,],;,},<EOF>''',101))

    def test_750(self):
        self.assertTrue(TestLexer.test('''Class JR{Var _:O;Val $_:Array [Array [Int ,0120],0120];}Class p:_{}Class _{}Class S{Constructor (k8,V_,_3H3,r,K:d;J:_){Return ;Continue ;Return ;Break ;} }Class D_{}Class __{Constructor (U_7,_:z){} }''','''Class,JR,{,Var,_,:,O,;,Val,$_,:,Array,[,Array,[,Int,,,0120,],,,0120,],;,},Class,p,:,_,{,},Class,_,{,},Class,S,{,Constructor,(,k8,,,V_,,,_3H3,,,r,,,K,:,d,;,J,:,_,),{,Return,;,Continue,;,Return,;,Break,;,},},Class,D_,{,},Class,__,{,Constructor,(,U_7,,,_,:,z,),{,},},<EOF>''',101))

    def test_751(self):
        self.assertTrue(TestLexer.test('''Class k:h70{}Class _{}Class _Ey9:_{$4(O0,c9:Int ){}Val $0,$1:Array [String ,0X25];Destructor (){}Val $8_Oig:H;}''','''Class,k,:,h70,{,},Class,_,{,},Class,_Ey9,:,_,{,$4,(,O0,,,c9,:,Int,),{,},Val,$0,,,$1,:,Array,[,String,,,0X25,],;,Destructor,(,),{,},Val,$8_Oig,:,H,;,},<EOF>''',101))

    def test_752(self):
        self.assertTrue(TestLexer.test('''Class Z{Var _:s;}Class p{Var $5qT0:Boolean ;Val h,$_:Array [Array [Array [Boolean ,7_19],0b1],0b10001];$sZW_4(pf,_1:Boolean ;B3:Z_w8Y_){} }''','''Class,Z,{,Var,_,:,s,;,},Class,p,{,Var,$5qT0,:,Boolean,;,Val,h,,,$_,:,Array,[,Array,[,Array,[,Boolean,,,719,],,,0b1,],,,0b10001,],;,$sZW_4,(,pf,,,_1,:,Boolean,;,B3,:,Z_w8Y_,),{,},},<EOF>''',101))

    def test_753(self):
        self.assertTrue(TestLexer.test('''Class JI:_31{Destructor (){} }Class _:_{Destructor (){} }Class _{$_C1(g:_d__r6017K;_1_:_nT){}Val _7:Array [Int ,6_35];Val K,g1:Float ;}''','''Class,JI,:,_31,{,Destructor,(,),{,},},Class,_,:,_,{,Destructor,(,),{,},},Class,_,{,$_C1,(,g,:,_d__r6017K,;,_1_,:,_nT,),{,},Val,_7,:,Array,[,Int,,,635,],;,Val,K,,,g1,:,Float,;,},<EOF>''',101))

    def test_754(self):
        self.assertTrue(TestLexer.test('''Class l8m0_{}Class IGr{M(){} }Class _{}Class B:_{Var $im6:Array [Boolean ,9_4];Constructor (){Return ;} }Class _:__A_1B{}''','''Class,l8m0_,{,},Class,IGr,{,M,(,),{,},},Class,_,{,},Class,B,:,_,{,Var,$im6,:,Array,[,Boolean,,,94,],;,Constructor,(,),{,Return,;,},},Class,_,:,__A_1B,{,},<EOF>''',101))

    def test_755(self):
        self.assertTrue(TestLexer.test('''Class n0{Constructor (_2,D_O,__:g;_s,_:Array [Boolean ,0x9];R,H,_v,C68,_,_,__:Array [Array [Array [String ,5],0b1001011],0b1]){} }''','''Class,n0,{,Constructor,(,_2,,,D_O,,,__,:,g,;,_s,,,_,:,Array,[,Boolean,,,0x9,],;,R,,,H,,,_v,,,C68,,,_,,,_,,,__,:,Array,[,Array,[,Array,[,String,,,5,],,,0b1001011,],,,0b1,],),{,},},<EOF>''',101))

    def test_756(self):
        self.assertTrue(TestLexer.test('''Class Q:G{}Class _N_{}Class _{Constructor (){} }Class _:_{b(OK_5vy9,mn_m3:Int ;_,_,_j,H9_6:Array [Array [Float ,1],1];_,V9ks1:Int ;k:Array [Array [Boolean ,0X34],51]){}Var $k,$7:_;}''','''Class,Q,:,G,{,},Class,_N_,{,},Class,_,{,Constructor,(,),{,},},Class,_,:,_,{,b,(,OK_5vy9,,,mn_m3,:,Int,;,_,,,_,,,_j,,,H9_6,:,Array,[,Array,[,Float,,,1,],,,1,],;,_,,,V9ks1,:,Int,;,k,:,Array,[,Array,[,Boolean,,,0X34,],,,51,],),{,},Var,$k,,,$7,:,_,;,},<EOF>''',101))

    def test_757(self):
        self.assertTrue(TestLexer.test('''Class mAm_{J(__544,_:__28;OA,Mf_:K9){}Destructor (){}Constructor (Z,n:K___){}Destructor (){_::$r1._();}Val _0:_;}''','''Class,mAm_,{,J,(,__544,,,_,:,__28,;,OA,,,Mf_,:,K9,),{,},Destructor,(,),{,},Constructor,(,Z,,,n,:,K___,),{,},Destructor,(,),{,_,::,$r1,.,_,(,),;,},Val,_0,:,_,;,},<EOF>''',101))

    def test_758(self):
        self.assertTrue(TestLexer.test('''Class __{$1Tb(_:Array [Int ,0b110111];Q,_,_:Boolean ;_h____,_M,C,__3:Array [Float ,0b1];J,_9_,__:_;___nK:T___){} }''','''Class,__,{,$1Tb,(,_,:,Array,[,Int,,,0b110111,],;,Q,,,_,,,_,:,Boolean,;,_h____,,,_M,,,C,,,__3,:,Array,[,Float,,,0b1,],;,J,,,_9_,,,__,:,_,;,___nK,:,T___,),{,},},<EOF>''',101))

    def test_759(self):
        self.assertTrue(TestLexer.test('''Class _{}Class Qd{Var $_,$E,$__15427_kQZ2:_;Destructor (){}Constructor (){}Val $_1,$m,O__,$5,E:Array [Array [Array [String ,013],0x6],0b1010100];}''','''Class,_,{,},Class,Qd,{,Var,$_,,,$E,,,$__15427_kQZ2,:,_,;,Destructor,(,),{,},Constructor,(,),{,},Val,$_1,,,$m,,,O__,,,$5,,,E,:,Array,[,Array,[,Array,[,String,,,013,],,,0x6,],,,0b1010100,],;,},<EOF>''',101))

    def test_760(self):
        self.assertTrue(TestLexer.test('''Class _:c{_(){ {}Return ;}Var _GHWI_:Array [Array [Boolean ,0126],0x2];Val $w:_;Constructor (){Continue ;}Val _3,__,_,$6,$1:Array [Array [String ,03_5],0xF_8F];}Class _:Y{Destructor (){} }''','''Class,_,:,c,{,_,(,),{,{,},Return,;,},Var,_GHWI_,:,Array,[,Array,[,Boolean,,,0126,],,,0x2,],;,Val,$w,:,_,;,Constructor,(,),{,Continue,;,},Val,_3,,,__,,,_,,,$6,,,$1,:,Array,[,Array,[,String,,,035,],,,0xF8F,],;,},Class,_,:,Y,{,Destructor,(,),{,},},<EOF>''',101))

    def test_761(self):
        self.assertTrue(TestLexer.test('''Class ix_L0:x_2{Var $c_F_,$X16:Array [String ,6];Constructor (P:Array [Array [Array [Array [Array [Array [Array [Array [String ,041],0b1],0b1010000],64],0x8],0b10],0b1],05];_:Array [Boolean ,0x3C]){}Var v,p_:Float ;}''','''Class,ix_L0,:,x_2,{,Var,$c_F_,,,$X16,:,Array,[,String,,,6,],;,Constructor,(,P,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,041,],,,0b1,],,,0b1010000,],,,64,],,,0x8,],,,0b10,],,,0b1,],,,05,],;,_,:,Array,[,Boolean,,,0x3C,],),{,},Var,v,,,p_,:,Float,;,},<EOF>''',101))

    def test_762(self):
        self.assertTrue(TestLexer.test('''Class _8G:_{}Class __{}Class _2_:w{}Class SO:_5{Destructor (){} }Class A:K{b(T:_;_88:Float ;_9:Array [String ,0x3]){}Destructor (){} }Class WZ:t{}Class _{}''','''Class,_8G,:,_,{,},Class,__,{,},Class,_2_,:,w,{,},Class,SO,:,_5,{,Destructor,(,),{,},},Class,A,:,K,{,b,(,T,:,_,;,_88,:,Float,;,_9,:,Array,[,String,,,0x3,],),{,},Destructor,(,),{,},},Class,WZ,:,t,{,},Class,_,{,},<EOF>''',101))

    def test_763(self):
        self.assertTrue(TestLexer.test('''Class s_{Constructor (u:Array [Array [Boolean ,0b111011],0XA];dK_7,HQ_62,dW:String ){} }Class _N{Val $4bA,$a,$9,x:_;Constructor (){}Constructor (_0El:String ){} }''','''Class,s_,{,Constructor,(,u,:,Array,[,Array,[,Boolean,,,0b111011,],,,0XA,],;,dK_7,,,HQ_62,,,dW,:,String,),{,},},Class,_N,{,Val,$4bA,,,$a,,,$9,,,x,:,_,;,Constructor,(,),{,},Constructor,(,_0El,:,String,),{,},},<EOF>''',101))

    def test_764(self):
        self.assertTrue(TestLexer.test('''Class V:_1{Var x8,_:Array [Int ,06];Destructor (){}Constructor (_,S_w924,WA__a,_,__,Cn5,___,m,G4,x,_:Array [Array [Int ,0X7],8_7]){Break ;}Val R:Float ;}Class v6{$1(_E,_5T:Float ;_,_:_){} }Class T:Q1{}''','''Class,V,:,_1,{,Var,x8,,,_,:,Array,[,Int,,,06,],;,Destructor,(,),{,},Constructor,(,_,,,S_w924,,,WA__a,,,_,,,__,,,Cn5,,,___,,,m,,,G4,,,x,,,_,:,Array,[,Array,[,Int,,,0X7,],,,87,],),{,Break,;,},Val,R,:,Float,;,},Class,v6,{,$1,(,_E,,,_5T,:,Float,;,_,,,_,:,_,),{,},},Class,T,:,Q1,{,},<EOF>''',101))

    def test_765(self):
        self.assertTrue(TestLexer.test('''Class _:p{Val $_M:Array [Array [Array [Array [Float ,9],01],0B111011],50];_(_,H:Gy){}__(h7:Array [String ,0B111011]){}Var $8_:Array [Array [Float ,07],0x62];}''','''Class,_,:,p,{,Val,$_M,:,Array,[,Array,[,Array,[,Array,[,Float,,,9,],,,01,],,,0B111011,],,,50,],;,_,(,_,,,H,:,Gy,),{,},__,(,h7,:,Array,[,String,,,0B111011,],),{,},Var,$8_,:,Array,[,Array,[,Float,,,07,],,,0x62,],;,},<EOF>''',101))

    def test_766(self):
        self.assertTrue(TestLexer.test('''Class S6{}Class _:_N2{Var $qX0,_:Array [Int ,86];U(I,m:G4;__:Array [Int ,0X13];T:__;D1:l;Y:BK;q,S2:Boolean ){} }Class o{}Class _:_Q{}Class ___{}Class LW2:_{Constructor (_:Int ){} }''','''Class,S6,{,},Class,_,:,_N2,{,Var,$qX0,,,_,:,Array,[,Int,,,86,],;,U,(,I,,,m,:,G4,;,__,:,Array,[,Int,,,0X13,],;,T,:,__,;,D1,:,l,;,Y,:,BK,;,q,,,S2,:,Boolean,),{,},},Class,o,{,},Class,_,:,_Q,{,},Class,___,{,},Class,LW2,:,_,{,Constructor,(,_,:,Int,),{,},},<EOF>''',101))

    def test_767(self):
        self.assertTrue(TestLexer.test('''Class _5:U_k2{Destructor (){} }Class _:____0__{$b(){Break ;} }Class Q:fW{Destructor (){Break ;Break ;} }Class _:Ny_{Constructor (){} }''','''Class,_5,:,U_k2,{,Destructor,(,),{,},},Class,_,:,____0__,{,$b,(,),{,Break,;,},},Class,Q,:,fW,{,Destructor,(,),{,Break,;,Break,;,},},Class,_,:,Ny_,{,Constructor,(,),{,},},<EOF>''',101))

    def test_768(self):
        self.assertTrue(TestLexer.test('''Class ox_o:Q{$_o(_er0_,e_,_:Array [Array [Array [Array [Array [Float ,79],0b1],0XB_80],0b1010],0B1];j,M:Float ){} }Class x2:q{}Class W{}Class F:u3{}Class e_:O7{}''','''Class,ox_o,:,Q,{,$_o,(,_er0_,,,e_,,,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,79,],,,0b1,],,,0XB80,],,,0b1010,],,,0B1,],;,j,,,M,:,Float,),{,},},Class,x2,:,q,{,},Class,W,{,},Class,F,:,u3,{,},Class,e_,:,O7,{,},<EOF>''',101))

    def test_769(self):
        self.assertTrue(TestLexer.test('''Class _:p9{Constructor (){Break ;}$_(H,_:String ;c:wi3_5){}Destructor (){Val _3M9___0,U,iY_0_11_:Array [Array [String ,0B1],0X17];} }''','''Class,_,:,p9,{,Constructor,(,),{,Break,;,},$_,(,H,,,_,:,String,;,c,:,wi3_5,),{,},Destructor,(,),{,Val,_3M9___0,,,U,,,iY_0_11_,:,Array,[,Array,[,String,,,0B1,],,,0X17,],;,},},<EOF>''',101))

    def test_770(self):
        self.assertTrue(TestLexer.test('''Class _:V00_d{}Class _F:w1{Destructor (){ {} }}Class S:j{}Class _{}Class _:U_{Var F,R,dS_:Boolean ;Constructor (){} }Class N371{Var U8:_;}Class _87{Val $7:Q42_;}''','''Class,_,:,V00_d,{,},Class,_F,:,w1,{,Destructor,(,),{,{,},},},Class,S,:,j,{,},Class,_,{,},Class,_,:,U_,{,Var,F,,,R,,,dS_,:,Boolean,;,Constructor,(,),{,},},Class,N371,{,Var,U8,:,_,;,},Class,_87,{,Val,$7,:,Q42_,;,},<EOF>''',101))

    def test_771(self):
        self.assertTrue(TestLexer.test('''Class _{}Class _:G{Constructor (J:Boolean ;_:Array [Float ,0X3];x:Array [Array [Array [Int ,0b1000],35],0X3]){} }''','''Class,_,{,},Class,_,:,G,{,Constructor,(,J,:,Boolean,;,_,:,Array,[,Float,,,0X3,],;,x,:,Array,[,Array,[,Array,[,Int,,,0b1000,],,,35,],,,0X3,],),{,},},<EOF>''',101))

    def test_772(self):
        self.assertTrue(TestLexer.test('''Class P:g97{}Class _:__{$Q(_,__:Array [Int ,0B1000];_34C,Y:Boolean ;F_:Boolean ;_:Boolean ;__:Int ){}$0_(o:Float ;M6,l:Float ;_,__8____G,_,s__pPS,__F1_:h_;_:Boolean ){Continue ;Return ;{} }_(){}Var _25Vw6:Float ;}''','''Class,P,:,g97,{,},Class,_,:,__,{,$Q,(,_,,,__,:,Array,[,Int,,,0B1000,],;,_34C,,,Y,:,Boolean,;,F_,:,Boolean,;,_,:,Boolean,;,__,:,Int,),{,},$0_,(,o,:,Float,;,M6,,,l,:,Float,;,_,,,__8____G,,,_,,,s__pPS,,,__F1_,:,h_,;,_,:,Boolean,),{,Continue,;,Return,;,{,},},_,(,),{,},Var,_25Vw6,:,Float,;,},<EOF>''',101))

    def test_773(self):
        self.assertTrue(TestLexer.test('''Class _W_99{Constructor (__,h:Array [Array [Int ,0XF],65];_,___,Iu__a,_,_81:Array [Float ,0b11100];Y6:_;_:Array [Float ,97_9];V_,_:Float ){} }''','''Class,_W_99,{,Constructor,(,__,,,h,:,Array,[,Array,[,Int,,,0XF,],,,65,],;,_,,,___,,,Iu__a,,,_,,,_81,:,Array,[,Float,,,0b11100,],;,Y6,:,_,;,_,:,Array,[,Float,,,979,],;,V_,,,_,:,Float,),{,},},<EOF>''',101))

    def test_774(self):
        self.assertTrue(TestLexer.test('''Class ej:_{Val $Z,___b,$vm3,jI4ro,_,_:String ;Val _86,_,$0_r,$_,Gm,d,$_,$1__6_,$_:Array [Array [Array [Int ,0B1_0],060],8];}''','''Class,ej,:,_,{,Val,$Z,,,___b,,,$vm3,,,jI4ro,,,_,,,_,:,String,;,Val,_86,,,_,,,$0_r,,,$_,,,Gm,,,d,,,$_,,,$1__6_,,,$_,:,Array,[,Array,[,Array,[,Int,,,0B10,],,,060,],,,8,],;,},<EOF>''',101))

    def test_775(self):
        self.assertTrue(TestLexer.test('''Class _{}Class W:_{}Class vW:H{$7(_,_z,_:Array [Array [Array [Array [Int ,0X5D],0B111010],7260_1],0B1_10];Z:_43;YL2,_,C:Float ){Continue ;} }''','''Class,_,{,},Class,W,:,_,{,},Class,vW,:,H,{,$7,(,_,,,_z,,,_,:,Array,[,Array,[,Array,[,Array,[,Int,,,0X5D,],,,0B111010,],,,72601,],,,0B110,],;,Z,:,_43,;,YL2,,,_,,,C,:,Float,),{,Continue,;,},},<EOF>''',101))

    def test_776(self):
        self.assertTrue(TestLexer.test('''Class _E{Val Y:Array [Array [Array [Array [Boolean ,80],0263],010],0B1];}Class _:I{$_b(){} }Class _{}Class _{$6(w:d){} }''','''Class,_E,{,Val,Y,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,80,],,,0263,],,,010,],,,0B1,],;,},Class,_,:,I,{,$_b,(,),{,},},Class,_,{,},Class,_,{,$6,(,w,:,d,),{,},},<EOF>''',101))

    def test_777(self):
        self.assertTrue(TestLexer.test('''Class T_:g82{Var $Uhk_:Array [Int ,0X6];$v(){}Var t,$_,$227__,_p:_8_;}Class fRr{_(){Val V,e,_:Array [String ,01];}Var $_:F;}''','''Class,T_,:,g82,{,Var,$Uhk_,:,Array,[,Int,,,0X6,],;,$v,(,),{,},Var,t,,,$_,,,$227__,,,_p,:,_8_,;,},Class,fRr,{,_,(,),{,Val,V,,,e,,,_,:,Array,[,String,,,01,],;,},Var,$_,:,F,;,},<EOF>''',101))

    def test_778(self):
        self.assertTrue(TestLexer.test('''Class _:EB{Var _,_24,XW,$_,$5,$_,_,l:Array [Int ,0X3E];Destructor (){}Constructor (__,_vB:String ;f_:Array [Array [Float ,0X3E],0740];_O:Int ;__,b:Array [Int ,1];j:Array [Array [Boolean ,03],0x3];S_:d_K){Return ;} }''','''Class,_,:,EB,{,Var,_,,,_24,,,XW,,,$_,,,$5,,,$_,,,_,,,l,:,Array,[,Int,,,0X3E,],;,Destructor,(,),{,},Constructor,(,__,,,_vB,:,String,;,f_,:,Array,[,Array,[,Float,,,0X3E,],,,0740,],;,_O,:,Int,;,__,,,b,:,Array,[,Int,,,1,],;,j,:,Array,[,Array,[,Boolean,,,03,],,,0x3,],;,S_,:,d_K,),{,Return,;,},},<EOF>''',101))

    def test_779(self):
        self.assertTrue(TestLexer.test('''Class __38__42_:_{$q(__6,_K,ZB,__:Array [Int ,84];_:Boolean ;Q_o9:Array [Array [Array [String ,5],0x61],0X2];V__T:_6;_:Array [Array [Array [Int ,84],0B1001001],0135];L,E,_:Y;__T__7,_,_:Array [String ,0X2]){Continue ;} }''','''Class,__38__42_,:,_,{,$q,(,__6,,,_K,,,ZB,,,__,:,Array,[,Int,,,84,],;,_,:,Boolean,;,Q_o9,:,Array,[,Array,[,Array,[,String,,,5,],,,0x61,],,,0X2,],;,V__T,:,_6,;,_,:,Array,[,Array,[,Array,[,Int,,,84,],,,0B1001001,],,,0135,],;,L,,,E,,,_,:,Y,;,__T__7,,,_,,,_,:,Array,[,String,,,0X2,],),{,Continue,;,},},<EOF>''',101))

    def test_780(self):
        self.assertTrue(TestLexer.test('''Class w_4B:__{Destructor (){Var _:Array [Array [Array [Array [Array [String ,035],4],0B101],0X5C],062];} }Class H0_{}''','''Class,w_4B,:,__,{,Destructor,(,),{,Var,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,035,],,,4,],,,0B101,],,,0X5C,],,,062,],;,},},Class,H0_,{,},<EOF>''',101))

    def test_781(self):
        self.assertTrue(TestLexer.test('''Class G{Constructor (pK:Array [Array [Boolean ,05_411],79];vt:Array [Array [Float ,0b1010001],0B101110];_:Boolean ;c8H,_R,___7,_,e:JG34){}Constructor (){Var _:w6;Break ;} }''','''Class,G,{,Constructor,(,pK,:,Array,[,Array,[,Boolean,,,05411,],,,79,],;,vt,:,Array,[,Array,[,Float,,,0b1010001,],,,0B101110,],;,_,:,Boolean,;,c8H,,,_R,,,___7,,,_,,,e,:,JG34,),{,},Constructor,(,),{,Var,_,:,w6,;,Break,;,},},<EOF>''',101))

    def test_782(self):
        self.assertTrue(TestLexer.test('''Class n{Var $_:Array [Int ,03];Val _Y,k:Array [Array [Array [Array [Array [Array [Int ,06],0b1],0X33],05723_2_6_7_2],9_479],0b10_1];}Class y{}Class _8:_{_X(k0:T_7;__:Int ){} }''','''Class,n,{,Var,$_,:,Array,[,Int,,,03,],;,Val,_Y,,,k,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,06,],,,0b1,],,,0X33,],,,057232672,],,,9479,],,,0b101,],;,},Class,y,{,},Class,_8,:,_,{,_X,(,k0,:,T_7,;,__,:,Int,),{,},},<EOF>''',101))

    def test_783(self):
        self.assertTrue(TestLexer.test('''Class _{Var X,$_,_H,$E,$_:n;Constructor (Y,n7,N:Array [Array [Array [Array [Array [Boolean ,067],0B100101],014_3_566],067],5];_9,_:Array [String ,0X9]){} }''','''Class,_,{,Var,X,,,$_,,,_H,,,$E,,,$_,:,n,;,Constructor,(,Y,,,n7,,,N,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,067,],,,0B100101,],,,0143566,],,,067,],,,5,],;,_9,,,_,:,Array,[,String,,,0X9,],),{,},},<EOF>''',101))

    def test_784(self):
        self.assertTrue(TestLexer.test('''Class _:_{}Class __{Constructor (_,__,AnX,_,K,__r_,_,_:Array [Array [Array [Array [Array [Float ,0B1010011],39],0B10_10_01_00],31],4];k:Array [Int ,0B1]){} }''','''Class,_,:,_,{,},Class,__,{,Constructor,(,_,,,__,,,AnX,,,_,,,K,,,__r_,,,_,,,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0B1010011,],,,39,],,,0B10100100,],,,31,],,,4,],;,k,:,Array,[,Int,,,0B1,],),{,},},<EOF>''',101))

    def test_785(self):
        self.assertTrue(TestLexer.test('''Class _:_{}Class T_:_{__6(__b,F3U,N_,_,_,S:Array [Array [Array [String ,0xF],9],9];o,_,x9:Float ){Break ;}Destructor (){Break ;Continue ;}Val _:_;}''','''Class,_,:,_,{,},Class,T_,:,_,{,__6,(,__b,,,F3U,,,N_,,,_,,,_,,,S,:,Array,[,Array,[,Array,[,String,,,0xF,],,,9,],,,9,],;,o,,,_,,,x9,:,Float,),{,Break,;,},Destructor,(,),{,Break,;,Continue,;,},Val,_,:,_,;,},<EOF>''',101))

    def test_786(self):
        self.assertTrue(TestLexer.test('''Class _5:L_{Var zH1,$_:Float ;Val _,b,_F_,R_,$3:Array [Array [Boolean ,0b1],8_2];Var P,$_26_i_,$714:Array [Array [Array [String ,0b1_11],066],0X8];Destructor (){ {} }}''','''Class,_5,:,L_,{,Var,zH1,,,$_,:,Float,;,Val,_,,,b,,,_F_,,,R_,,,$3,:,Array,[,Array,[,Boolean,,,0b1,],,,82,],;,Var,P,,,$_26_i_,,,$714,:,Array,[,Array,[,Array,[,String,,,0b111,],,,066,],,,0X8,],;,Destructor,(,),{,{,},},},<EOF>''',101))

    def test_787(self):
        self.assertTrue(TestLexer.test('''Class Q:_{Var $5_:Array [Int ,29];Constructor (_q2:Boolean ;_D3,W,_,k2,_:Array [Array [Array [Array [Array [Array [Array [Array [String ,06550_1],0X1],29],0xE_5_D],29],0b101110],0XD],0b1];Y:Array [Array [Array [Array [Float ,52],20],0B111001],040]){}Val $v9l:Boolean ;}''','''Class,Q,:,_,{,Var,$5_,:,Array,[,Int,,,29,],;,Constructor,(,_q2,:,Boolean,;,_D3,,,W,,,_,,,k2,,,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,065501,],,,0X1,],,,29,],,,0xE5D,],,,29,],,,0b101110,],,,0XD,],,,0b1,],;,Y,:,Array,[,Array,[,Array,[,Array,[,Float,,,52,],,,20,],,,0B111001,],,,040,],),{,},Val,$v9l,:,Boolean,;,},<EOF>''',101))

    def test_788(self):
        self.assertTrue(TestLexer.test('''Class _3:_{Var $_4xd,$S,_0_v5RN:Float ;_LM(_,i_,_S,H_,_,_,AvM2,S_5b9_,l7:Int ;__:b;P:Array [Array [Array [Array [Array [Float ,01],0X5F],0xC_C2],0B1001101],0720]){} }Class o_UR{}Class _z:a{}''','''Class,_3,:,_,{,Var,$_4xd,,,$S,,,_0_v5RN,:,Float,;,_LM,(,_,,,i_,,,_S,,,H_,,,_,,,_,,,AvM2,,,S_5b9_,,,l7,:,Int,;,__,:,b,;,P,:,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,01,],,,0X5F,],,,0xCC2,],,,0B1001101,],,,0720,],),{,},},Class,o_UR,{,},Class,_z,:,a,{,},<EOF>''',101))

    def test_789(self):
        self.assertTrue(TestLexer.test('''Class _4:__r{Constructor (S,Re:Array [Array [Float ,0x57],017044];r_,_r:Float ;_,I__,_,__,__5,g_,oA:String ;_u,__:wy;Z,_,_,q,oD:g2_){Val pf:g6;} }Class _:_V__{Val C:Array [Float ,035];}''','''Class,_4,:,__r,{,Constructor,(,S,,,Re,:,Array,[,Array,[,Float,,,0x57,],,,017044,],;,r_,,,_r,:,Float,;,_,,,I__,,,_,,,__,,,__5,,,g_,,,oA,:,String,;,_u,,,__,:,wy,;,Z,,,_,,,_,,,q,,,oD,:,g2_,),{,Val,pf,:,g6,;,},},Class,_,:,_V__,{,Val,C,:,Array,[,Float,,,035,],;,},<EOF>''',101))

    def test_790(self):
        self.assertTrue(TestLexer.test('''Class T:P_{Destructor (){Val _2r,_:Array [Array [Array [Float ,0B110101],76],0B1_1];}Destructor (){Var __,M_:f_4;Continue ;}Var $p,$_70_:_;Var $9:Array [Array [Array [Boolean ,0x2],0xF],0x32];Constructor (){}Val $_xK,_,_:_;}''','''Class,T,:,P_,{,Destructor,(,),{,Val,_2r,,,_,:,Array,[,Array,[,Array,[,Float,,,0B110101,],,,76,],,,0B11,],;,},Destructor,(,),{,Var,__,,,M_,:,f_4,;,Continue,;,},Var,$p,,,$_70_,:,_,;,Var,$9,:,Array,[,Array,[,Array,[,Boolean,,,0x2,],,,0xF,],,,0x32,],;,Constructor,(,),{,},Val,$_xK,,,_,,,_,:,_,;,},<EOF>''',101))

    def test_791(self):
        self.assertTrue(TestLexer.test('''Class _7_:_{Constructor (_:Int ;_,j_I:Array [Float ,0x3];vC,_:_;_08:m){Break ;} }Class F:e{Val l__,$_,$_:Array [Int ,49_9];}''','''Class,_7_,:,_,{,Constructor,(,_,:,Int,;,_,,,j_I,:,Array,[,Float,,,0x3,],;,vC,,,_,:,_,;,_08,:,m,),{,Break,;,},},Class,F,:,e,{,Val,l__,,,$_,,,$_,:,Array,[,Int,,,499,],;,},<EOF>''',101))

    def test_792(self):
        self.assertTrue(TestLexer.test('''Class _:qC{_J(_,i,ea85h_:Array [Int ,0b1001011]){}Val _5:_;}Class u3{Destructor (){Break ;Return ;{}Return ;Continue ;} }''','''Class,_,:,qC,{,_J,(,_,,,i,,,ea85h_,:,Array,[,Int,,,0b1001011,],),{,},Val,_5,:,_,;,},Class,u3,{,Destructor,(,),{,Break,;,Return,;,{,},Return,;,Continue,;,},},<EOF>''',101))

    def test_793(self):
        self.assertTrue(TestLexer.test('''Class _{}Class _{Val $2,A,j1:Array [Array [Array [Array [Array [String ,0B1_0],2_3_8_2],06],0B1],0x1];Var $_,__,P:p_;}''','''Class,_,{,},Class,_,{,Val,$2,,,A,,,j1,:,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0B10,],,,2382,],,,06,],,,0B1,],,,0x1,],;,Var,$_,,,__,,,P,:,p_,;,},<EOF>''',101))

    def test_794(self):
        self.assertTrue(TestLexer.test('''Class _:G2_{}Class _3{Val $P8_8F_1,_6:Array [Array [Array [Int ,0b1000000],0xE_5A],0X4C];$_E6_(){}Constructor (J,__,l65:Int ){}Destructor (){} }''','''Class,_,:,G2_,{,},Class,_3,{,Val,$P8_8F_1,,,_6,:,Array,[,Array,[,Array,[,Int,,,0b1000000,],,,0xE5A,],,,0X4C,],;,$_E6_,(,),{,},Constructor,(,J,,,__,,,l65,:,Int,),{,},Destructor,(,),{,},},<EOF>''',101))

    def test_795(self):
        self.assertTrue(TestLexer.test('''Class S1_r{Constructor (){}Constructor (N:Float ;q:Boolean ;H:D3;CN,g2:Int ;_:Array [Array [Int ,7536],0X7];_:q){} }Class r65{}Class SC{}''','''Class,S1_r,{,Constructor,(,),{,},Constructor,(,N,:,Float,;,q,:,Boolean,;,H,:,D3,;,CN,,,g2,:,Int,;,_,:,Array,[,Array,[,Int,,,7536,],,,0X7,],;,_,:,q,),{,},},Class,r65,{,},Class,SC,{,},<EOF>''',101))

    def test_796(self):
        self.assertTrue(TestLexer.test('''Class _n45:_{}Class q:_P{Constructor (){Break ;}Var _uKX3q:_7;}Class __:__1____G{}Class Ih_5{Constructor (){}Var $05_:String ;}''','''Class,_n45,:,_,{,},Class,q,:,_P,{,Constructor,(,),{,Break,;,},Var,_uKX3q,:,_7,;,},Class,__,:,__1____G,{,},Class,Ih_5,{,Constructor,(,),{,},Var,$05_,:,String,;,},<EOF>''',101))

    def test_797(self):
        self.assertTrue(TestLexer.test('''Class Y6q:E_{}Class _{Val $7:Int ;Val N:Array [Array [Array [Boolean ,0130],0b101101],0130];}Class _q__:f{Val $_3:Array [Array [Array [Array [Array [Array [Array [Array [Array [Array [Float ,0b101101],0X58],52],0130],0130],0B1010],0B1010],0B1010],52],9_3];}''','''Class,Y6q,:,E_,{,},Class,_,{,Val,$7,:,Int,;,Val,N,:,Array,[,Array,[,Array,[,Boolean,,,0130,],,,0b101101,],,,0130,],;,},Class,_q__,:,f,{,Val,$_3,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0b101101,],,,0X58,],,,52,],,,0130,],,,0130,],,,0B1010,],,,0B1010,],,,0B1010,],,,52,],,,93,],;,},<EOF>''',101))

    def test_798(self):
        self.assertTrue(TestLexer.test('''Class _X3:_46{}Class L8V{Val $_,$_:Array [Array [Array [Array [Array [Float ,0b1000010],9],0171],0x13],0B111];}Class n9De_:F{Destructor (){}Var $_6_I1:Float ;}Class _c5:_{d8(){} }Class _{Var $V:Array [Array [Array [Array [String ,0B1_1],0b1000010],0B1001100],5];Destructor (){} }''','''Class,_X3,:,_46,{,},Class,L8V,{,Val,$_,,,$_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0b1000010,],,,9,],,,0171,],,,0x13,],,,0B111,],;,},Class,n9De_,:,F,{,Destructor,(,),{,},Var,$_6_I1,:,Float,;,},Class,_c5,:,_,{,d8,(,),{,},},Class,_,{,Var,$V,:,Array,[,Array,[,Array,[,Array,[,String,,,0B11,],,,0b1000010,],,,0B1001100,],,,5,],;,Destructor,(,),{,},},<EOF>''',101))

    def test_799(self):
        self.assertTrue(TestLexer.test('''Class _:_9{}Class _7:_{Destructor (){}Constructor (_:Array [Array [Array [Boolean ,3],8],0X1F];_:Boolean ){} }Class C:i{}''','''Class,_,:,_9,{,},Class,_7,:,_,{,Destructor,(,),{,},Constructor,(,_,:,Array,[,Array,[,Array,[,Boolean,,,3,],,,8,],,,0X1F,],;,_,:,Boolean,),{,},},Class,C,:,i,{,},<EOF>''',101))

    def test_800(self):
        self.assertTrue(TestLexer.test('''Class q82_1__:o{}Class __{$3_V_(j,_c,YR_:Array [String ,9];FR,_,Q:Int ;_E___m_,_:__;c8_3:Array [Array [Array [Float ,3],070],3]){} }''','''Class,q82_1__,:,o,{,},Class,__,{,$3_V_,(,j,,,_c,,,YR_,:,Array,[,String,,,9,],;,FR,,,_,,,Q,:,Int,;,_E___m_,,,_,:,__,;,c8_3,:,Array,[,Array,[,Array,[,Float,,,3,],,,070,],,,3,],),{,},},<EOF>''',101))

    def test_801(self):
        self.assertTrue(TestLexer.test('''Class _:_{}Class T:i{Val $2_6,_,_:bN;}Class ___{}Class P{Destructor (){}Constructor (_N,_n09_:String ;c,qf_:String ){}Destructor (){ {} }}''','''Class,_,:,_,{,},Class,T,:,i,{,Val,$2_6,,,_,,,_,:,bN,;,},Class,___,{,},Class,P,{,Destructor,(,),{,},Constructor,(,_N,,,_n09_,:,String,;,c,,,qf_,:,String,),{,},Destructor,(,),{,{,},},},<EOF>''',101))

    def test_802(self):
        self.assertTrue(TestLexer.test('''Class n:O{Val $9__,$T_P:Array [Boolean ,0b10100];Var S:Array [Boolean ,7];Destructor (){ {Break ;}{ {} }}Var $_3:Array [Array [String ,47],0b10100];}''','''Class,n,:,O,{,Val,$9__,,,$T_P,:,Array,[,Boolean,,,0b10100,],;,Var,S,:,Array,[,Boolean,,,7,],;,Destructor,(,),{,{,Break,;,},{,{,},},},Var,$_3,:,Array,[,Array,[,String,,,47,],,,0b10100,],;,},<EOF>''',101))

    def test_803(self):
        self.assertTrue(TestLexer.test('''Class _{}Class _9{$__(_Y,_,_,q,By 5V8G5,c7_9:Array [Array [Boolean ,0105],34];_,_:_sH;rw,_72,_a,V:Array [Array [Array [Array [String ,0105],100],0b100011],9]){} }''','''Class,_,{,},Class,_9,{,$__,(,_Y,,,_,,,_,,,q,,,By,5,V8G5,,,c7_9,:,Array,[,Array,[,Boolean,,,0105,],,,34,],;,_,,,_,:,_sH,;,rw,,,_72,,,_a,,,V,:,Array,[,Array,[,Array,[,Array,[,String,,,0105,],,,100,],,,0b100011,],,,9,],),{,},},<EOF>''',101))

    def test_804(self):
        self.assertTrue(TestLexer.test('''Class _E{Constructor (_,P,__0:Array [Array [Array [Float ,07],0B1010011],0b1011101]){}$W(){}Constructor (X8_,FC:Array [Array [Array [Array [Boolean ,025],0b10],0XE],0x4C]){Return ;}Constructor (r,Wg,F_IC,T:_;N:_;_,J:Array [Array [Int ,0B1010011],34];_:P_){} }''','''Class,_E,{,Constructor,(,_,,,P,,,__0,:,Array,[,Array,[,Array,[,Float,,,07,],,,0B1010011,],,,0b1011101,],),{,},$W,(,),{,},Constructor,(,X8_,,,FC,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,025,],,,0b10,],,,0XE,],,,0x4C,],),{,Return,;,},Constructor,(,r,,,Wg,,,F_IC,,,T,:,_,;,N,:,_,;,_,,,J,:,Array,[,Array,[,Int,,,0B1010011,],,,34,],;,_,:,P_,),{,},},<EOF>''',101))

    def test_805(self):
        self.assertTrue(TestLexer.test('''Class C_{Destructor (){N::$L();}Var _,$423Y,$_:Array [Array [Boolean ,68],04_2_5];}Class o7BZ{}Class d{Constructor (){Return ;}$q_Q9(_:A5t_){} }Class B1UF63:F1{}''','''Class,C_,{,Destructor,(,),{,N,::,$L,(,),;,},Var,_,,,$423Y,,,$_,:,Array,[,Array,[,Boolean,,,68,],,,0425,],;,},Class,o7BZ,{,},Class,d,{,Constructor,(,),{,Return,;,},$q_Q9,(,_,:,A5t_,),{,},},Class,B1UF63,:,F1,{,},<EOF>''',101))

    def test_806(self):
        self.assertTrue(TestLexer.test('''Class r_{}Class _{Val y,$0:__;Val $6,c:__;}Class z{B_(_:String ;M_8:String ){}Var E:Float ;Destructor (){Return ;} }''','''Class,r_,{,},Class,_,{,Val,y,,,$0,:,__,;,Val,$6,,,c,:,__,;,},Class,z,{,B_,(,_,:,String,;,M_8,:,String,),{,},Var,E,:,Float,;,Destructor,(,),{,Return,;,},},<EOF>''',101))

    def test_807(self):
        self.assertTrue(TestLexer.test('''Class v:j1v{Constructor (_:Array [String ,0B1_001];L,i1:String ;_,_:Array [Array [Array [Boolean ,1],0b1],7];z_:Array [Array [Int ,0XF],0B111100];E,_k,m:_){Break ;} }''','''Class,v,:,j1v,{,Constructor,(,_,:,Array,[,String,,,0B1001,],;,L,,,i1,:,String,;,_,,,_,:,Array,[,Array,[,Array,[,Boolean,,,1,],,,0b1,],,,7,],;,z_,:,Array,[,Array,[,Int,,,0XF,],,,0B111100,],;,E,,,_k,,,m,:,_,),{,Break,;,},},<EOF>''',101))

    def test_808(self):
        self.assertTrue(TestLexer.test('''Class _929___m2_:e{Var N,$c:Array [Array [String ,4],0x1B];Val R_,$H9M,E0,jS:Array [Array [Array [Array [Boolean ,0B1],7_9_7_49],0B10_1_1],04_0];}''','''Class,_929___m2_,:,e,{,Var,N,,,$c,:,Array,[,Array,[,String,,,4,],,,0x1B,],;,Val,R_,,,$H9M,,,E0,,,jS,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,0B1,],,,79749,],,,0B1011,],,,040,],;,},<EOF>''',101))

    def test_809(self):
        self.assertTrue(TestLexer.test('''Class _29:al{}Class d3{Constructor (){}Destructor (){} }Class __{Val $OZ6_:q;Destructor (){Val _80,_X,__x,_A_,dh9W9,_:Array [Array [Array [Boolean ,0XBC],0b1],0X2];} }''','''Class,_29,:,al,{,},Class,d3,{,Constructor,(,),{,},Destructor,(,),{,},},Class,__,{,Val,$OZ6_,:,q,;,Destructor,(,),{,Val,_80,,,_X,,,__x,,,_A_,,,dh9W9,,,_,:,Array,[,Array,[,Array,[,Boolean,,,0XBC,],,,0b1,],,,0X2,],;,},},<EOF>''',101))

    def test_810(self):
        self.assertTrue(TestLexer.test('''Class c8DD{}Class b_{Val $P_,_,$_:Array [Array [Array [Array [Array [Array [Float ,30_9_2],0X84_6],0XB],01],0b101111],0b101111];}''','''Class,c8DD,{,},Class,b_,{,Val,$P_,,,_,,,$_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,3092,],,,0X846,],,,0XB,],,,01,],,,0b101111,],,,0b101111,],;,},<EOF>''',101))

    def test_811(self):
        self.assertTrue(TestLexer.test('''Class Z:_1{}Class _{_(p:Array [Int ,0142]){} }Class _Z__P_3{Val _,_:A;Val $p,__3_,_:F;Constructor (){}Var $K:Array [Array [Boolean ,0XD51],0X2F];}Class n{Destructor (){} }Class O4:_{}Class _G_7{Constructor (_,_4H,D_Ct7__:A;s:Array [Float ,0b100];j:Float ;_:Array [Array [Float ,0B1100011],0x14];e_n_2,o,__:Boolean ;mF,_:I0){} }''','''Class,Z,:,_1,{,},Class,_,{,_,(,p,:,Array,[,Int,,,0142,],),{,},},Class,_Z__P_3,{,Val,_,,,_,:,A,;,Val,$p,,,__3_,,,_,:,F,;,Constructor,(,),{,},Var,$K,:,Array,[,Array,[,Boolean,,,0XD51,],,,0X2F,],;,},Class,n,{,Destructor,(,),{,},},Class,O4,:,_,{,},Class,_G_7,{,Constructor,(,_,,,_4H,,,D_Ct7__,:,A,;,s,:,Array,[,Float,,,0b100,],;,j,:,Float,;,_,:,Array,[,Array,[,Float,,,0B1100011,],,,0x14,],;,e_n_2,,,o,,,__,:,Boolean,;,mF,,,_,:,I0,),{,},},<EOF>''',101))

    def test_812(self):
        self.assertTrue(TestLexer.test('''Class F:_{}Class g8:n_a{}Class sL{Constructor (m,__0:Int ;_hk,B:Float ;P,___5:Array [Float ,8_9_0_47];H:Float ;Sl,h99_:Array [Int ,2_1_2_7];A1,y1,v,_,_,_:Array [Float ,010];_sT,z_f_,_8,Y,s,Lz21:Int ;cW:_v;n_,Z3:_;_:_x){Break ;} }''','''Class,F,:,_,{,},Class,g8,:,n_a,{,},Class,sL,{,Constructor,(,m,,,__0,:,Int,;,_hk,,,B,:,Float,;,P,,,___5,:,Array,[,Float,,,89047,],;,H,:,Float,;,Sl,,,h99_,:,Array,[,Int,,,2127,],;,A1,,,y1,,,v,,,_,,,_,,,_,:,Array,[,Float,,,010,],;,_sT,,,z_f_,,,_8,,,Y,,,s,,,Lz21,:,Int,;,cW,:,_v,;,n_,,,Z3,:,_,;,_,:,_x,),{,Break,;,},},<EOF>''',101))

    def test_813(self):
        self.assertTrue(TestLexer.test('''Class __8__:_{Destructor (){}Constructor (jj_:__;q4,_A,___,e,_,B__E,_:Int ;_:Array [Array [Int ,046],046]){} }Class V{}''','''Class,__8__,:,_,{,Destructor,(,),{,},Constructor,(,jj_,:,__,;,q4,,,_A,,,___,,,e,,,_,,,B__E,,,_,:,Int,;,_,:,Array,[,Array,[,Int,,,046,],,,046,],),{,},},Class,V,{,},<EOF>''',101))

    def test_814(self):
        self.assertTrue(TestLexer.test('''Class _b{}Class P_:_{Constructor (_:Array [Array [Array [Array [Array [Array [Array [String ,30],0X48],0X4_B],016],0x45],0b1000001],30]){Break ;}C2_(O:R;j8:Array [Boolean ,0B111010];P_,__,_:Array [String ,0b1000001];e,k4:Array [Array [Int ,0x45],0B1_0_0];_,_2:Array [Array [String ,016],0b1000001]){} }Class l:h{}''','''Class,_b,{,},Class,P_,:,_,{,Constructor,(,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,30,],,,0X48,],,,0X4B,],,,016,],,,0x45,],,,0b1000001,],,,30,],),{,Break,;,},C2_,(,O,:,R,;,j8,:,Array,[,Boolean,,,0B111010,],;,P_,,,__,,,_,:,Array,[,String,,,0b1000001,],;,e,,,k4,:,Array,[,Array,[,Int,,,0x45,],,,0B100,],;,_,,,_2,:,Array,[,Array,[,String,,,016,],,,0b1000001,],),{,},},Class,l,:,h,{,},<EOF>''',101))

    def test_815(self):
        self.assertTrue(TestLexer.test('''Class _{}Class mZ:L_1{}Class u:_{Constructor (_,_,X,w:String ;_:Xm){_e::$6();}_(s0,kvs,sE,yn9,_,_,_p1:_Q){} }''','''Class,_,{,},Class,mZ,:,L_1,{,},Class,u,:,_,{,Constructor,(,_,,,_,,,X,,,w,:,String,;,_,:,Xm,),{,_e,::,$6,(,),;,},_,(,s0,,,kvs,,,sE,,,yn9,,,_,,,_,,,_p1,:,_Q,),{,},},<EOF>''',101))

    def test_816(self):
        self.assertTrue(TestLexer.test('''Class _:_4{Val P:Array [Float ,0b10];}Class _Z947:_{}Class C_:GF{Constructor (_,q:Boolean ;x:String ){}Destructor (){} }Class v{}Class vL{Val $CG:n;}''','''Class,_,:,_4,{,Val,P,:,Array,[,Float,,,0b10,],;,},Class,_Z947,:,_,{,},Class,C_,:,GF,{,Constructor,(,_,,,q,:,Boolean,;,x,:,String,),{,},Destructor,(,),{,},},Class,v,{,},Class,vL,{,Val,$CG,:,n,;,},<EOF>''',101))

    def test_817(self):
        self.assertTrue(TestLexer.test('''Class Nh{v__(){} }Class U{$7(b_:Array [Int ,0XA];b9:Array [Float ,0B1100100];x85,_2,_,B:_;B__,___6v:Array [Array [Int ,0B1100100],49]){} }''','''Class,Nh,{,v__,(,),{,},},Class,U,{,$7,(,b_,:,Array,[,Int,,,0XA,],;,b9,:,Array,[,Float,,,0B1100100,],;,x85,,,_2,,,_,,,B,:,_,;,B__,,,___6v,:,Array,[,Array,[,Int,,,0B1100100,],,,49,],),{,},},<EOF>''',101))

    def test_818(self):
        self.assertTrue(TestLexer.test('''Class qYA_u:uX_Y5_2{}Class Qw{}Class A_:_x5{}Class _{}Class h_6N:C{Val OHdz,$y_,v,_:Array [Array [Array [Array [String ,73],0B1_1],0103],0103];}''','''Class,qYA_u,:,uX_Y5_2,{,},Class,Qw,{,},Class,A_,:,_x5,{,},Class,_,{,},Class,h_6N,:,C,{,Val,OHdz,,,$y_,,,v,,,_,:,Array,[,Array,[,Array,[,Array,[,String,,,73,],,,0B11,],,,0103,],,,0103,],;,},<EOF>''',101))

    def test_819(self):
        self.assertTrue(TestLexer.test('''Class X:_{Destructor (){_fj9_::$C();} }Class _{Constructor (){Break ;}$_(E9,_1,__W:Float ){}$44(xx,__,_,__:Array [String ,0X57]){Continue ;} }''','''Class,X,:,_,{,Destructor,(,),{,_fj9_,::,$C,(,),;,},},Class,_,{,Constructor,(,),{,Break,;,},$_,(,E9,,,_1,,,__W,:,Float,),{,},$44,(,xx,,,__,,,_,,,__,:,Array,[,String,,,0X57,],),{,Continue,;,},},<EOF>''',101))

    def test_820(self):
        self.assertTrue(TestLexer.test('''Class c6:_{}Class _{Constructor (_9J,___g,__9,Q,X_83__7:_57){} }Class Hn_:C{}Class _{Destructor (){} }Class _:_{}''','''Class,c6,:,_,{,},Class,_,{,Constructor,(,_9J,,,___g,,,__9,,,Q,,,X_83__7,:,_57,),{,},},Class,Hn_,:,C,{,},Class,_,{,Destructor,(,),{,},},Class,_,:,_,{,},<EOF>''',101))

    def test_821(self):
        self.assertTrue(TestLexer.test('''Class _{Val _X:_;Val $_W:String ;}Class _{Destructor (){}Constructor (){Break ;} }Class a{Var $0:E_Rlc_F;Val wd6:String ;Val E5_,$_2,$3_1,$_b:Array [Array [Array [Int ,91],0b1],91];}Class D_6{}''','''Class,_,{,Val,_X,:,_,;,Val,$_W,:,String,;,},Class,_,{,Destructor,(,),{,},Constructor,(,),{,Break,;,},},Class,a,{,Var,$0,:,E_Rlc_F,;,Val,wd6,:,String,;,Val,E5_,,,$_2,,,$3_1,,,$_b,:,Array,[,Array,[,Array,[,Int,,,91,],,,0b1,],,,91,],;,},Class,D_6,{,},<EOF>''',101))

    def test_822(self):
        self.assertTrue(TestLexer.test('''Class _{}Class C_{}Class E{}Class X:__{Val Y:Array [Boolean ,33];}Class h{Constructor (k_N:Array [Array [Array [Array [Int ,0B1001010],0x4],0X58],33]){} }''','''Class,_,{,},Class,C_,{,},Class,E,{,},Class,X,:,__,{,Val,Y,:,Array,[,Boolean,,,33,],;,},Class,h,{,Constructor,(,k_N,:,Array,[,Array,[,Array,[,Array,[,Int,,,0B1001010,],,,0x4,],,,0X58,],,,33,],),{,},},<EOF>''',101))

    def test_823(self):
        self.assertTrue(TestLexer.test('''Class N6:__{Var $_:C9g_;Constructor (_,h,_6:_D){ {} }Val s1:Array [Array [Array [Array [Array [Array [Float ,0101],0101],0b1_0],04],0xC_E_E],0b111];}Class BY6:__{Constructor (A:Array [Int ,0x3D7AF0];_Z,P:Array [Array [Int ,0x41],0x41]){} }Class _{Constructor (){} }''','''Class,N6,:,__,{,Var,$_,:,C9g_,;,Constructor,(,_,,,h,,,_6,:,_D,),{,{,},},Val,s1,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0101,],,,0101,],,,0b10,],,,04,],,,0xCEE,],,,0b111,],;,},Class,BY6,:,__,{,Constructor,(,A,:,Array,[,Int,,,0x3D7AF0,],;,_Z,,,P,:,Array,[,Array,[,Int,,,0x41,],,,0x41,],),{,},},Class,_,{,Constructor,(,),{,},},<EOF>''',101))

    def test_824(self):
        self.assertTrue(TestLexer.test('''Class _:z_{}Class V:z{Constructor (nHA8_,y,q,Zo_,_,_e0_h,M,_,_:Float ;P,lS,__:Y;l,_,b_k1,_:Boolean ;C:Boolean ;_,_:Array [Float ,0X43];N:h){}Destructor (){} }Class s:_{Val $u7_,$0_:_C_;Val $_P,$W:p;}''','''Class,_,:,z_,{,},Class,V,:,z,{,Constructor,(,nHA8_,,,y,,,q,,,Zo_,,,_,,,_e0_h,,,M,,,_,,,_,:,Float,;,P,,,lS,,,__,:,Y,;,l,,,_,,,b_k1,,,_,:,Boolean,;,C,:,Boolean,;,_,,,_,:,Array,[,Float,,,0X43,],;,N,:,h,),{,},Destructor,(,),{,},},Class,s,:,_,{,Val,$u7_,,,$0_,:,_C_,;,Val,$_P,,,$W,:,p,;,},<EOF>''',101))

    def test_825(self):
        self.assertTrue(TestLexer.test('''Class __np{Var s5pc_,$277,$2:Array [String ,65];Constructor (){} }Class F:Qbv8{Val __n4,q:Array [Array [String ,0b1],0xA_0];}Class _I5{Val $4,n,$_,_:Array [Int ,06_3_52];Constructor (){} }Class b8_{}''','''Class,__np,{,Var,s5pc_,,,$277,,,$2,:,Array,[,String,,,65,],;,Constructor,(,),{,},},Class,F,:,Qbv8,{,Val,__n4,,,q,:,Array,[,Array,[,String,,,0b1,],,,0xA0,],;,},Class,_I5,{,Val,$4,,,n,,,$_,,,_,:,Array,[,Int,,,06352,],;,Constructor,(,),{,},},Class,b8_,{,},<EOF>''',101))

    def test_826(self):
        self.assertTrue(TestLexer.test('''Class __{Var $48i2,_,_,ct2,$f,qs,$_A1_:_;}Class t:F0_{}Class a{$YAG_9m(_2_dl,d:_5;S_:_y){} }Class __8{Var _J165,a_oV:_21;}Class _{Destructor (){} }''','''Class,__,{,Var,$48i2,,,_,,,_,,,ct2,,,$f,,,qs,,,$_A1_,:,_,;,},Class,t,:,F0_,{,},Class,a,{,$YAG_9m,(,_2_dl,,,d,:,_5,;,S_,:,_y,),{,},},Class,__8,{,Var,_J165,,,a_oV,:,_21,;,},Class,_,{,Destructor,(,),{,},},<EOF>''',101))

    def test_827(self):
        self.assertTrue(TestLexer.test('''Class _2ac__:UMZY{}Class t:_4_{Val $_N,f:Array [Array [Array [Array [Array [Array [Array [Array [String ,31],060],6_2],060],0b10111],40],0b10111],0B1_0110_110];Val $__X_9:Float ;}''','''Class,_2ac__,:,UMZY,{,},Class,t,:,_4_,{,Val,$_N,,,f,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,31,],,,060,],,,62,],,,060,],,,0b10111,],,,40,],,,0b10111,],,,0B10110110,],;,Val,$__X_9,:,Float,;,},<EOF>''',101))

    def test_828(self):
        self.assertTrue(TestLexer.test('''Class _1{}Class q{}Class J:_{Destructor (){}Constructor (_k:_;_C,__:Array [Boolean ,0B1_1_1_1]){} }Class Pu_nQ__:_{}''','''Class,_1,{,},Class,q,{,},Class,J,:,_,{,Destructor,(,),{,},Constructor,(,_k,:,_,;,_C,,,__,:,Array,[,Boolean,,,0B1111,],),{,},},Class,Pu_nQ__,:,_,{,},<EOF>''',101))

    def test_829(self):
        self.assertTrue(TestLexer.test('''Class _:_{Destructor (){}Constructor (_J5,_4lD1,_:Array [Array [Float ,012],012];___:Array [Array [String ,0X3],0b1_000];_U27TP,_L:_){} }Class _:_{}Class hJ4{}''','''Class,_,:,_,{,Destructor,(,),{,},Constructor,(,_J5,,,_4lD1,,,_,:,Array,[,Array,[,Float,,,012,],,,012,],;,___,:,Array,[,Array,[,String,,,0X3,],,,0b1000,],;,_U27TP,,,_L,:,_,),{,},},Class,_,:,_,{,},Class,hJ4,{,},<EOF>''',101))

    def test_830(self):
        self.assertTrue(TestLexer.test('''Class T:u{Val U3,$41__:Array [Array [Array [Array [Int ,0B1_1],0XA_5],0x63],0113];}Class l5:_41{}Class L:___{Var _:s;}Class J_:_2{}''','''Class,T,:,u,{,Val,U3,,,$41__,:,Array,[,Array,[,Array,[,Array,[,Int,,,0B11,],,,0XA5,],,,0x63,],,,0113,],;,},Class,l5,:,_41,{,},Class,L,:,___,{,Var,_,:,s,;,},Class,J_,:,_2,{,},<EOF>''',101))

    def test_831(self):
        self.assertTrue(TestLexer.test('''Class SP939{Constructor (){}Destructor (){}Destructor (){} }Class _L:P3C{Destructor (){Return ;}Destructor (){Break ;} }''','''Class,SP939,{,Constructor,(,),{,},Destructor,(,),{,},Destructor,(,),{,},},Class,_L,:,P3C,{,Destructor,(,),{,Return,;,},Destructor,(,),{,Break,;,},},<EOF>''',101))

    def test_832(self):
        self.assertTrue(TestLexer.test('''Class E{Val k,g,$9a,Le,_D:String ;Var T80,_:Int ;}Class _:y_{}Class _s{Constructor (P_9,Ec:Array [Float ,0x14];_8:_g;_Z,_J84,_4,IA,_,r,_,_:_){}Var __e,$_:String ;}''','''Class,E,{,Val,k,,,g,,,$9a,,,Le,,,_D,:,String,;,Var,T80,,,_,:,Int,;,},Class,_,:,y_,{,},Class,_s,{,Constructor,(,P_9,,,Ec,:,Array,[,Float,,,0x14,],;,_8,:,_g,;,_Z,,,_J84,,,_4,,,IA,,,_,,,r,,,_,,,_,:,_,),{,},Var,__e,,,$_,:,String,;,},<EOF>''',101))

    def test_833(self):
        self.assertTrue(TestLexer.test('''Class S:_f{f_V(rix,_,__02:String ;sLiC,T,_K:Array [String ,0b1011011];q:Boolean ;_:Array [Boolean ,0401];_X:Array [Int ,96]){} }''','''Class,S,:,_f,{,f_V,(,rix,,,_,,,__02,:,String,;,sLiC,,,T,,,_K,:,Array,[,String,,,0b1011011,],;,q,:,Boolean,;,_,:,Array,[,Boolean,,,0401,],;,_X,:,Array,[,Int,,,96,],),{,},},<EOF>''',101))

    def test_834(self):
        self.assertTrue(TestLexer.test('''Class __{Constructor (vF__1,_L4,__p:Array [Array [Array [Array [Array [Int ,0B1],0X2],9_4_598],0b1],05_6]){} }''','''Class,__,{,Constructor,(,vF__1,,,_L4,,,__p,:,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0B1,],,,0X2,],,,94598,],,,0b1,],,,056,],),{,},},<EOF>''',101))

    def test_835(self):
        self.assertTrue(TestLexer.test('''Class _{Val $2:L;}Class E{Constructor (R,Y:Array [Array [Float ,03],0XE1];cMZ:Array [Float ,0XB];__,_,_6_:_9){} }''','''Class,_,{,Val,$2,:,L,;,},Class,E,{,Constructor,(,R,,,Y,:,Array,[,Array,[,Float,,,03,],,,0XE1,],;,cMZ,:,Array,[,Float,,,0XB,],;,__,,,_,,,_6_,:,_9,),{,},},<EOF>''',101))

    def test_836(self):
        self.assertTrue(TestLexer.test('''Class iw{$_7___(__2_,_528puDE____1,_,zI3,gA__0:Array [Boolean ,057];_,jr:Array [String ,61]){Break ;Break ;}Val $_:Float ;Var m:T;}''','''Class,iw,{,$_7___,(,__2_,,,_528puDE____1,,,_,,,zI3,,,gA__0,:,Array,[,Boolean,,,057,],;,_,,,jr,:,Array,[,String,,,61,],),{,Break,;,Break,;,},Val,$_,:,Float,;,Var,m,:,T,;,},<EOF>''',101))

    def test_837(self):
        self.assertTrue(TestLexer.test('''Class K{Var t,Ot,$4_10,_,$e9:Array [Array [Int ,0b1],0x5F];Destructor (){}Val _CjS,_7_t_a,$2,_,$d:Array [String ,6_3];}Class gm{Constructor (){}$4(){}Val $5,$_,__:w_;}''','''Class,K,{,Var,t,,,Ot,,,$4_10,,,_,,,$e9,:,Array,[,Array,[,Int,,,0b1,],,,0x5F,],;,Destructor,(,),{,},Val,_CjS,,,_7_t_a,,,$2,,,_,,,$d,:,Array,[,String,,,63,],;,},Class,gm,{,Constructor,(,),{,},$4,(,),{,},Val,$5,,,$_,,,__,:,w_,;,},<EOF>''',101))

    def test_838(self):
        self.assertTrue(TestLexer.test('''Class _0b7:O_9N{}Class M4:j{}Class _7:__{}Class _{$Q(a,_2:Array [Array [Array [Boolean ,0B110],0b1101],0xD];_,_:Float ){}Var $54s,$5,$_U_,$iU:a__;}Class _{}Class t_:_X{Val _:_;}Class A____4N:W4{Constructor (){} }Class __7:__5__{}''','''Class,_0b7,:,O_9N,{,},Class,M4,:,j,{,},Class,_7,:,__,{,},Class,_,{,$Q,(,a,,,_2,:,Array,[,Array,[,Array,[,Boolean,,,0B110,],,,0b1101,],,,0xD,],;,_,,,_,:,Float,),{,},Var,$54s,,,$5,,,$_U_,,,$iU,:,a__,;,},Class,_,{,},Class,t_,:,_X,{,Val,_,:,_,;,},Class,A____4N,:,W4,{,Constructor,(,),{,},},Class,__7,:,__5__,{,},<EOF>''',101))

    def test_839(self):
        self.assertTrue(TestLexer.test('''Class _76:__Z{Constructor (_,S,_:_){}Destructor (){}__0Y(_:Yw){Continue ;}Constructor (_:Array [Array [Array [String ,0x41],0104],2];__:__R){}Var U:Array [Float ,04];}Class _959__20kU:_2{}Class h{Val X_05,z_C1,_:Float ;Val _7,__,U,$23g,_,_,P_:Array [String ,020];}''','''Class,_76,:,__Z,{,Constructor,(,_,,,S,,,_,:,_,),{,},Destructor,(,),{,},__0Y,(,_,:,Yw,),{,Continue,;,},Constructor,(,_,:,Array,[,Array,[,Array,[,String,,,0x41,],,,0104,],,,2,],;,__,:,__R,),{,},Var,U,:,Array,[,Float,,,04,],;,},Class,_959__20kU,:,_2,{,},Class,h,{,Val,X_05,,,z_C1,,,_,:,Float,;,Val,_7,,,__,,,U,,,$23g,,,_,,,_,,,P_,:,Array,[,String,,,020,],;,},<EOF>''',101))

    def test_840(self):
        self.assertTrue(TestLexer.test('''Class Z{Constructor (____,_:Array [Boolean ,0b1];_f,s__2,_:Array [Float ,25];o:_r6;__9E,_,_j:Q;j,P,l:Boolean ;t:Float ){} }Class S{Val $y:_;}''','''Class,Z,{,Constructor,(,____,,,_,:,Array,[,Boolean,,,0b1,],;,_f,,,s__2,,,_,:,Array,[,Float,,,25,],;,o,:,_r6,;,__9E,,,_,,,_j,:,Q,;,j,,,P,,,l,:,Boolean,;,t,:,Float,),{,},},Class,S,{,Val,$y,:,_,;,},<EOF>''',101))

    def test_841(self):
        self.assertTrue(TestLexer.test('''Class o_{}Class _9_{}Class _9{_i(_IP:Array [String ,0b110110];a,_,_:Int ;l_,_T,_I,_NW,_:Int ;_,_1:_4_){}Destructor (){}Val _l23:Float ;}Class h{}''','''Class,o_,{,},Class,_9_,{,},Class,_9,{,_i,(,_IP,:,Array,[,String,,,0b110110,],;,a,,,_,,,_,:,Int,;,l_,,,_T,,,_I,,,_NW,,,_,:,Int,;,_,,,_1,:,_4_,),{,},Destructor,(,),{,},Val,_l23,:,Float,;,},Class,h,{,},<EOF>''',101))

    def test_842(self):
        self.assertTrue(TestLexer.test('''Class y_G_:_{}Class _h28:__{Val _,$I,_,_,$_:_;Var $YEj:Array [Array [String ,0XD],88];}Class _1:b_5{Constructor (){}$D__(){}Constructor (__,y,c5_E_,_:_A;F,_X69_0F,fQ,O5a_F3,_u:Int ;w,__g_9t_,U5,_:Int ;_8:_3;_:h6;tJ__,J,hp:Array [Array [Boolean ,0B1100010],065]){} }Class _:_{}Class _{Destructor (){Return ;} }''','''Class,y_G_,:,_,{,},Class,_h28,:,__,{,Val,_,,,$I,,,_,,,_,,,$_,:,_,;,Var,$YEj,:,Array,[,Array,[,String,,,0XD,],,,88,],;,},Class,_1,:,b_5,{,Constructor,(,),{,},$D__,(,),{,},Constructor,(,__,,,y,,,c5_E_,,,_,:,_A,;,F,,,_X69_0F,,,fQ,,,O5a_F3,,,_u,:,Int,;,w,,,__g_9t_,,,U5,,,_,:,Int,;,_8,:,_3,;,_,:,h6,;,tJ__,,,J,,,hp,:,Array,[,Array,[,Boolean,,,0B1100010,],,,065,],),{,},},Class,_,:,_,{,},Class,_,{,Destructor,(,),{,Return,;,},},<EOF>''',101))

    def test_843(self):
        self.assertTrue(TestLexer.test('''Class k{Val $B,U,e_v,$0:Float ;}Class K:_{$6U(_,w__d,O_,_,FnR,_,V3:___;__,_:Array [Array [Float ,0b11],1_5]){}__(){Break ;} }''','''Class,k,{,Val,$B,,,U,,,e_v,,,$0,:,Float,;,},Class,K,:,_,{,$6U,(,_,,,w__d,,,O_,,,_,,,FnR,,,_,,,V3,:,___,;,__,,,_,:,Array,[,Array,[,Float,,,0b11,],,,15,],),{,},__,(,),{,Break,;,},},<EOF>''',101))

    def test_844(self):
        self.assertTrue(TestLexer.test('''Class _{$7uU3(z:Array [String ,1_11];_:Array [String ,14_4];_j:Array [Int ,02]){} }Class _5{}Class _{Var $_Cy:Int ;Constructor (){} }''','''Class,_,{,$7uU3,(,z,:,Array,[,String,,,111,],;,_,:,Array,[,String,,,144,],;,_j,:,Array,[,Int,,,02,],),{,},},Class,_5,{,},Class,_,{,Var,$_Cy,:,Int,;,Constructor,(,),{,},},<EOF>''',101))

    def test_845(self):
        self.assertTrue(TestLexer.test('''Class x_{Constructor (__U38f,Y9,_:Array [Boolean ,0X15];_3:Int ;_39:Int ;_,M,_1,__,_1:Array [Int ,0b11]){}Destructor (){}Constructor (_d4,a:_wS6__){Continue ;{} }}''','''Class,x_,{,Constructor,(,__U38f,,,Y9,,,_,:,Array,[,Boolean,,,0X15,],;,_3,:,Int,;,_39,:,Int,;,_,,,M,,,_1,,,__,,,_1,:,Array,[,Int,,,0b11,],),{,},Destructor,(,),{,},Constructor,(,_d4,,,a,:,_wS6__,),{,Continue,;,{,},},},<EOF>''',101))

    def test_846(self):
        self.assertTrue(TestLexer.test('''Class _Ei3__F3kQ_:K5_A{Constructor (T2:String ;P,B_,_EW8_:W;a:Int ;fj76l,pY,A:Array [Array [Array [Float ,0B111011],0B1],83]){Val I,UN,p0,P,_6:Array [Boolean ,83];} }''','''Class,_Ei3__F3kQ_,:,K5_A,{,Constructor,(,T2,:,String,;,P,,,B_,,,_EW8_,:,W,;,a,:,Int,;,fj76l,,,pY,,,A,:,Array,[,Array,[,Array,[,Float,,,0B111011,],,,0B1,],,,83,],),{,Val,I,,,UN,,,p0,,,P,,,_6,:,Array,[,Boolean,,,83,],;,},},<EOF>''',101))

    def test_847(self):
        self.assertTrue(TestLexer.test('''Class d__:qY_{}Class c{}Class H3{}Class _3s6_mXU0:_{Constructor (U,_,u,_,rx,h:_){Return ;}Constructor (_,x:Array [Array [Float ,7_0],0B1_010_10]){Continue ;} }''','''Class,d__,:,qY_,{,},Class,c,{,},Class,H3,{,},Class,_3s6_mXU0,:,_,{,Constructor,(,U,,,_,,,u,,,_,,,rx,,,h,:,_,),{,Return,;,},Constructor,(,_,,,x,:,Array,[,Array,[,Float,,,70,],,,0B101010,],),{,Continue,;,},},<EOF>''',101))

    def test_848(self):
        self.assertTrue(TestLexer.test('''Class _4{Val _:Array [Array [Array [Float ,50],03],50];$_(){}Var B,$w659i_,$_,$4,g,T:_s;Destructor (){}Destructor (){Break ;} }''','''Class,_4,{,Val,_,:,Array,[,Array,[,Array,[,Float,,,50,],,,03,],,,50,],;,$_,(,),{,},Var,B,,,$w659i_,,,$_,,,$4,,,g,,,T,:,_s,;,Destructor,(,),{,},Destructor,(,),{,Break,;,},},<EOF>''',101))

    def test_849(self):
        self.assertTrue(TestLexer.test('''Class Z8:____4{Val n,$_742,_,$2g,$X:h6;Constructor (){} }Class __t7:A{Var x0,___,_,S,$80,L:v6a;Var r:Array [Boolean ,047];Constructor (){}Val mw,$67:Int ;}''','''Class,Z8,:,____4,{,Val,n,,,$_742,,,_,,,$2g,,,$X,:,h6,;,Constructor,(,),{,},},Class,__t7,:,A,{,Var,x0,,,___,,,_,,,S,,,$80,,,L,:,v6a,;,Var,r,:,Array,[,Boolean,,,047,],;,Constructor,(,),{,},Val,mw,,,$67,:,Int,;,},<EOF>''',101))

    def test_850(self):
        self.assertTrue(TestLexer.test('''Class N:FYV{Var $u,_,$_93,_,__,_49:Array [Array [Float ,85_1],0x64];}Class _iY:_{$_(){} }Class S:X{}Class A:A7h{}''','''Class,N,:,FYV,{,Var,$u,,,_,,,$_93,,,_,,,__,,,_49,:,Array,[,Array,[,Float,,,851,],,,0x64,],;,},Class,_iY,:,_,{,$_,(,),{,},},Class,S,:,X,{,},Class,A,:,A7h,{,},<EOF>''',101))

    def test_851(self):
        self.assertTrue(TestLexer.test('''Class n{Constructor (){}Constructor (R:_j;_3E_:Float ;_3_,_39V:Float ;_:r;a_:Array [Array [Boolean ,9],04];_:g;P3_8:Array [Array [Array [Array [Array [Int ,0B1010010],0B1_10],0X4],047],06]){}Constructor (x:Array [Float ,047];d48K_v,_h:tp;_:f){ {} }}''','''Class,n,{,Constructor,(,),{,},Constructor,(,R,:,_j,;,_3E_,:,Float,;,_3_,,,_39V,:,Float,;,_,:,r,;,a_,:,Array,[,Array,[,Boolean,,,9,],,,04,],;,_,:,g,;,P3_8,:,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0B1010010,],,,0B110,],,,0X4,],,,047,],,,06,],),{,},Constructor,(,x,:,Array,[,Float,,,047,],;,d48K_v,,,_h,:,tp,;,_,:,f,),{,{,},},},<EOF>''',101))

    def test_852(self):
        self.assertTrue(TestLexer.test('''Class __:x__{Constructor (){} }Class _{Var $P_:Array [Array [Float ,2],0XA]=!!-----Null ;}Class T:a{}Class _{_(){}_(){} }Class _:k{}Class __{}''','''Class,__,:,x__,{,Constructor,(,),{,},},Class,_,{,Var,$P_,:,Array,[,Array,[,Float,,,2,],,,0XA,],=,!,!,-,-,-,-,-,Null,;,},Class,T,:,a,{,},Class,_,{,_,(,),{,},_,(,),{,},},Class,_,:,k,{,},Class,__,{,},<EOF>''',101))

    def test_853(self):
        self.assertTrue(TestLexer.test('''Class LG:l{Destructor (){}Constructor (FW8:a1;G_:N;E__,_:Array [Array [Array [Array [Array [Array [Array [Float ,0B1001100],6],0XD],6],0x10],0X53],94]){} }''','''Class,LG,:,l,{,Destructor,(,),{,},Constructor,(,FW8,:,a1,;,G_,:,N,;,E__,,,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0B1001100,],,,6,],,,0XD,],,,6,],,,0x10,],,,0X53,],,,94,],),{,},},<EOF>''',101))

    def test_854(self):
        self.assertTrue(TestLexer.test('''Class _{}Class y50i:dK{}Class t:J_2{$U(__,k:Array [Array [Float ,0B1001011],0b1];O__4:Array [Array [Array [String ,0X3B],0B1001011],0132];__1:Array [Array [Array [Boolean ,3_2_1],04],39];nh,_3,_:aO_h){} }Class m_:_6j_8{}''','''Class,_,{,},Class,y50i,:,dK,{,},Class,t,:,J_2,{,$U,(,__,,,k,:,Array,[,Array,[,Float,,,0B1001011,],,,0b1,],;,O__4,:,Array,[,Array,[,Array,[,String,,,0X3B,],,,0B1001011,],,,0132,],;,__1,:,Array,[,Array,[,Array,[,Boolean,,,321,],,,04,],,,39,],;,nh,,,_3,,,_,:,aO_h,),{,},},Class,m_,:,_6j_8,{,},<EOF>''',101))

    def test_855(self):
        self.assertTrue(TestLexer.test('''Class _l:F2yt{}Class _E9a:_8{Val w:_;}Class _7D1:K{Constructor (){} }Class U{Var $6:Array [Array [Boolean ,0xE],0XB];}''','''Class,_l,:,F2yt,{,},Class,_E9a,:,_8,{,Val,w,:,_,;,},Class,_7D1,:,K,{,Constructor,(,),{,},},Class,U,{,Var,$6,:,Array,[,Array,[,Boolean,,,0xE,],,,0XB,],;,},<EOF>''',101))

    def test_856(self):
        self.assertTrue(TestLexer.test('''Class _:r{Constructor (){}Destructor (){} }Class Q3:__{v(R0,C,_4:Array [Int ,0137];_:Array [Array [Array [Float ,0B1],0x5B],9];_H:Array [Float ,0XF];WT_N:B){} }''','''Class,_,:,r,{,Constructor,(,),{,},Destructor,(,),{,},},Class,Q3,:,__,{,v,(,R0,,,C,,,_4,:,Array,[,Int,,,0137,],;,_,:,Array,[,Array,[,Array,[,Float,,,0B1,],,,0x5B,],,,9,],;,_H,:,Array,[,Float,,,0XF,],;,WT_N,:,B,),{,},},<EOF>''',101))

    def test_857(self):
        self.assertTrue(TestLexer.test('''Class L_:_{M(_:Array [String ,0107]){Var _g,f,_Qc34:Array [Array [Array [Float ,81],0X17],05_1];Continue ;Return ;} }Class w{}''','''Class,L_,:,_,{,M,(,_,:,Array,[,String,,,0107,],),{,Var,_g,,,f,,,_Qc34,:,Array,[,Array,[,Array,[,Float,,,81,],,,0X17,],,,051,],;,Continue,;,Return,;,},},Class,w,{,},<EOF>''',101))

    def test_858(self):
        self.assertTrue(TestLexer.test('''Class zHE{Var _,$_H,E9b,_D,$N,j,$_,k_l,$Y_,$_,$_:Array [Boolean ,0B1];}Class _4_9:_{Constructor (_:Array [Boolean ,031];_,_,r_2:_;H_yz,_:String ){}Val $y8:Int ;Var $hi,__:Array [Boolean ,83];Val $M4:_6;}''','''Class,zHE,{,Var,_,,,$_H,,,E9b,,,_D,,,$N,,,j,,,$_,,,k_l,,,$Y_,,,$_,,,$_,:,Array,[,Boolean,,,0B1,],;,},Class,_4_9,:,_,{,Constructor,(,_,:,Array,[,Boolean,,,031,],;,_,,,_,,,r_2,:,_,;,H_yz,,,_,:,String,),{,},Val,$y8,:,Int,;,Var,$hi,,,__,:,Array,[,Boolean,,,83,],;,Val,$M4,:,_6,;,},<EOF>''',101))

    def test_859(self):
        self.assertTrue(TestLexer.test('''Class I5{}Class G{Constructor (O:Array [Array [String ,0x1],031];_:Array [Float ,0x5A9];_:Array [Array [Array [Array [Array [Boolean ,0b10000],1_5],7],0x2B],14_5_33_10];G:Array [Int ,8]){} }Class i{Val $e_kY_:Boolean ;}''','''Class,I5,{,},Class,G,{,Constructor,(,O,:,Array,[,Array,[,String,,,0x1,],,,031,],;,_,:,Array,[,Float,,,0x5A9,],;,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0b10000,],,,15,],,,7,],,,0x2B,],,,1453310,],;,G,:,Array,[,Int,,,8,],),{,},},Class,i,{,Val,$e_kY_,:,Boolean,;,},<EOF>''',101))

    def test_860(self):
        self.assertTrue(TestLexer.test('''Class _:zP{Val X7:Array [String ,24];}Class OF{}Class l23P73_{Constructor (_,_:Array [Array [String ,5_787],0xB_4];c_1:Int ){} }''','''Class,_,:,zP,{,Val,X7,:,Array,[,String,,,24,],;,},Class,OF,{,},Class,l23P73_,{,Constructor,(,_,,,_,:,Array,[,Array,[,String,,,5787,],,,0xB4,],;,c_1,:,Int,),{,},},<EOF>''',101))

    def test_861(self):
        self.assertTrue(TestLexer.test('''Class _:o{Destructor (){Continue ;Val w,_:Array [Int ,33];__Q::$_U3_7();_::$_O();} }Class Y:A54{Destructor (){Break ;} }''','''Class,_,:,o,{,Destructor,(,),{,Continue,;,Val,w,,,_,:,Array,[,Int,,,33,],;,__Q,::,$_U3_7,(,),;,_,::,$_O,(,),;,},},Class,Y,:,A54,{,Destructor,(,),{,Break,;,},},<EOF>''',101))

    def test_862(self):
        self.assertTrue(TestLexer.test('''Class __:QO{Var t:String ;Destructor (){Break ;Break ;}Val $13l_5_5S__:_R;}Class _:aC{}Class _{}Class _C8:_91{}''','''Class,__,:,QO,{,Var,t,:,String,;,Destructor,(,),{,Break,;,Break,;,},Val,$13l_5_5S__,:,_R,;,},Class,_,:,aC,{,},Class,_,{,},Class,_C8,:,_91,{,},<EOF>''',101))

    def test_863(self):
        self.assertTrue(TestLexer.test('''Class s{}Class _92:_D7_{$A_(I:Array [Array [Float ,0X64],47];g_:Int ;_,T,B_1sQ6y_,v9:_;h7,Dx6w:_;a,G_:Float ){Break ;} }Class ZN{}''','''Class,s,{,},Class,_92,:,_D7_,{,$A_,(,I,:,Array,[,Array,[,Float,,,0X64,],,,47,],;,g_,:,Int,;,_,,,T,,,B_1sQ6y_,,,v9,:,_,;,h7,,,Dx6w,:,_,;,a,,,G_,:,Float,),{,Break,;,},},Class,ZN,{,},<EOF>''',101))

    def test_864(self):
        self.assertTrue(TestLexer.test('''Class n7:_{}Class _:w{Constructor (_:Array [Array [Int ,8],0B101101];z:Array [Array [Array [Array [Array [String ,0141],01],0B11],0B1],2];N:Boolean ;V2,___:String ){} }''','''Class,n7,:,_,{,},Class,_,:,w,{,Constructor,(,_,:,Array,[,Array,[,Int,,,8,],,,0B101101,],;,z,:,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0141,],,,01,],,,0B11,],,,0B1,],,,2,],;,N,:,Boolean,;,V2,,,___,:,String,),{,},},<EOF>''',101))

    def test_865(self):
        self.assertTrue(TestLexer.test('''Class V1I{Var D4_,$z,_:Boolean ;$4(_1:Y84;_,l:Float ){} }Class j{Var $_,$5:Float ;a_(){} }Class NG:P{Val HX6:A54M7;}''','''Class,V1I,{,Var,D4_,,,$z,,,_,:,Boolean,;,$4,(,_1,:,Y84,;,_,,,l,:,Float,),{,},},Class,j,{,Var,$_,,,$5,:,Float,;,a_,(,),{,},},Class,NG,:,P,{,Val,HX6,:,A54M7,;,},<EOF>''',101))

    def test_866(self):
        self.assertTrue(TestLexer.test('''Class u:B{}Class _931_:_{Var $72L8:v;Constructor (_b,A:String ;t,Ny:Array [String ,98]){Continue ;} }Class _75:s4_XL0_mq_{}''','''Class,u,:,B,{,},Class,_931_,:,_,{,Var,$72L8,:,v,;,Constructor,(,_b,,,A,:,String,;,t,,,Ny,:,Array,[,String,,,98,],),{,Continue,;,},},Class,_75,:,s4_XL0_mq_,{,},<EOF>''',101))

    def test_867(self):
        self.assertTrue(TestLexer.test('''Class MW{Var _h:Array [Array [Array [Array [Float ,0xF],0X1A],074],0x7];$7W_oG(hk,_O,_,_356l:Array [Float ,0x53];Z_:Array [Array [Array [Array [Boolean ,0x53],21],21],074]){} }Class t{}Class k7{Constructor (_:__){} }''','''Class,MW,{,Var,_h,:,Array,[,Array,[,Array,[,Array,[,Float,,,0xF,],,,0X1A,],,,074,],,,0x7,],;,$7W_oG,(,hk,,,_O,,,_,,,_356l,:,Array,[,Float,,,0x53,],;,Z_,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,0x53,],,,21,],,,21,],,,074,],),{,},},Class,t,{,},Class,k7,{,Constructor,(,_,:,__,),{,},},<EOF>''',101))

    def test_868(self):
        self.assertTrue(TestLexer.test('''Class _:g_{$_5(__r,__,_3,i:Array [Array [Int ,0X5],0X5B];L,___c:String ;_:j;ls,_:Array [Array [Int ,0X5B],0B10_0];y,L,_q,OK:Boolean ){ {} }}''','''Class,_,:,g_,{,$_5,(,__r,,,__,,,_3,,,i,:,Array,[,Array,[,Int,,,0X5,],,,0X5B,],;,L,,,___c,:,String,;,_,:,j,;,ls,,,_,:,Array,[,Array,[,Int,,,0X5B,],,,0B100,],;,y,,,L,,,_q,,,OK,:,Boolean,),{,{,},},},<EOF>''',101))

    def test_869(self):
        self.assertTrue(TestLexer.test('''Class vb{}Class _:O{}Class H___{Destructor (){}Constructor (_,E,_,_:Float ;s,v,D12:Array [String ,0X51];Mt:vy7;u:Float ;l6,Q:F0;_:Array [Array [Array [Array [Boolean ,0x5_F],0B1],0627],70]){} }Class _{}''','''Class,vb,{,},Class,_,:,O,{,},Class,H___,{,Destructor,(,),{,},Constructor,(,_,,,E,,,_,,,_,:,Float,;,s,,,v,,,D12,:,Array,[,String,,,0X51,],;,Mt,:,vy7,;,u,:,Float,;,l6,,,Q,:,F0,;,_,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,0x5F,],,,0B1,],,,0627,],,,70,],),{,},},Class,_,{,},<EOF>''',101))

    def test_870(self):
        self.assertTrue(TestLexer.test('''Class J:s7M{Constructor (_,d,_,_6sp:Boolean ;_:Array [Array [Int ,0x5F],0b100]){}Constructor (){}Constructor (){} }''','''Class,J,:,s7M,{,Constructor,(,_,,,d,,,_,,,_6sp,:,Boolean,;,_,:,Array,[,Array,[,Int,,,0x5F,],,,0b100,],),{,},Constructor,(,),{,},Constructor,(,),{,},},<EOF>''',101))

    def test_871(self):
        self.assertTrue(TestLexer.test('''Class z2_:u{$61(_Q9:_;_,o_:_3Z){Break ;} }Class o__73{Val $A4:Array [Array [Boolean ,85],0x6];}Class _1{Var $1_8:Array [Array [Array [Array [Float ,01_6],0B1110],0103],0103];}''','''Class,z2_,:,u,{,$61,(,_Q9,:,_,;,_,,,o_,:,_3Z,),{,Break,;,},},Class,o__73,{,Val,$A4,:,Array,[,Array,[,Boolean,,,85,],,,0x6,],;,},Class,_1,{,Var,$1_8,:,Array,[,Array,[,Array,[,Array,[,Float,,,016,],,,0B1110,],,,0103,],,,0103,],;,},<EOF>''',101))

    def test_872(self):
        self.assertTrue(TestLexer.test('''Class _{Constructor (W:Int ;t_,m:Array [String ,0b110011];t0,_b:String ){} }Class p:Z{Var $5D,$2,_,sRs7,$Z_,$_,tF_,q:Array [Array [Int ,0x1F5_1],0x94];}''','''Class,_,{,Constructor,(,W,:,Int,;,t_,,,m,:,Array,[,String,,,0b110011,],;,t0,,,_b,:,String,),{,},},Class,p,:,Z,{,Var,$5D,,,$2,,,_,,,sRs7,,,$Z_,,,$_,,,tF_,,,q,:,Array,[,Array,[,Int,,,0x1F51,],,,0x94,],;,},<EOF>''',101))

    def test_873(self):
        self.assertTrue(TestLexer.test('''Class _{}Class _:m_{Constructor (){}Constructor (R_4j,P:B;_:Array [Array [String ,050],10];o6,T:Int ;gP,Q_,R:_){}Destructor (){} }''','''Class,_,{,},Class,_,:,m_,{,Constructor,(,),{,},Constructor,(,R_4j,,,P,:,B,;,_,:,Array,[,Array,[,String,,,050,],,,10,],;,o6,,,T,:,Int,;,gP,,,Q_,,,R,:,_,),{,},Destructor,(,),{,},},<EOF>''',101))

    def test_874(self):
        self.assertTrue(TestLexer.test('''Class Z{}Class _:_{Var $3,uP_1FT3,$7,$_:Boolean ;}Class _:_q{Val $_D:Array [Array [Array [Array [String ,9],73],03],0b100101];}Class Xs{}''','''Class,Z,{,},Class,_,:,_,{,Var,$3,,,uP_1FT3,,,$7,,,$_,:,Boolean,;,},Class,_,:,_q,{,Val,$_D,:,Array,[,Array,[,Array,[,Array,[,String,,,9,],,,73,],,,03,],,,0b100101,],;,},Class,Xs,{,},<EOF>''',101))

    def test_875(self):
        self.assertTrue(TestLexer.test('''Class L{Constructor (_U_,E,i:Boolean ){}Val $6_67,$M2i8y,_:O_;i(_5_M,__0c_,u__o_:Array [Array [Int ,6],84];S5_,UC:Array [Array [String ,0x8_A_D1_63],84]){} }''','''Class,L,{,Constructor,(,_U_,,,E,,,i,:,Boolean,),{,},Val,$6_67,,,$M2i8y,,,_,:,O_,;,i,(,_5_M,,,__0c_,,,u__o_,:,Array,[,Array,[,Int,,,6,],,,84,],;,S5_,,,UC,:,Array,[,Array,[,String,,,0x8AD163,],,,84,],),{,},},<EOF>''',101))

    def test_876(self):
        self.assertTrue(TestLexer.test('''Class __:_CG{}Class _{$_m(){}Val $P_3,$i_:g_;Constructor (){}$D(z8,b_,A__,C,__,_Y,_:Array [Float ,0335_1_2];c4:Float ){}Var _,l:Float ;}Class h:_{}''','''Class,__,:,_CG,{,},Class,_,{,$_m,(,),{,},Val,$P_3,,,$i_,:,g_,;,Constructor,(,),{,},$D,(,z8,,,b_,,,A__,,,C,,,__,,,_Y,,,_,:,Array,[,Float,,,033512,],;,c4,:,Float,),{,},Var,_,,,l,:,Float,;,},Class,h,:,_,{,},<EOF>''',101))

    def test_877(self):
        self.assertTrue(TestLexer.test('''Class __{Var _Zf,$y_:String ;Constructor (P,f__I,D_0_N,SQ6,p_,u_,_h__d:_w_2__F;_:_635;L:Array [Float ,2];_:Boolean ;__:c){} }Class _:_{}Class g{Constructor (){}Var R1:Float ;}Class _:H{}Class L_{}''','''Class,__,{,Var,_Zf,,,$y_,:,String,;,Constructor,(,P,,,f__I,,,D_0_N,,,SQ6,,,p_,,,u_,,,_h__d,:,_w_2__F,;,_,:,_635,;,L,:,Array,[,Float,,,2,],;,_,:,Boolean,;,__,:,c,),{,},},Class,_,:,_,{,},Class,g,{,Constructor,(,),{,},Var,R1,:,Float,;,},Class,_,:,H,{,},Class,L_,{,},<EOF>''',101))

    def test_878(self):
        self.assertTrue(TestLexer.test('''Class Y:I{$p6(_:Boolean ){_2_3R::$5_();}Constructor (){Continue ;Return ;}Var _:Int ;}Class u:G_{}Class _:_{}Class V:_{}''','''Class,Y,:,I,{,$p6,(,_,:,Boolean,),{,_2_3R,::,$5_,(,),;,},Constructor,(,),{,Continue,;,Return,;,},Var,_,:,Int,;,},Class,u,:,G_,{,},Class,_,:,_,{,},Class,V,:,_,{,},<EOF>''',101))

    def test_879(self):
        self.assertTrue(TestLexer.test('''Class bC:s{Constructor (W,_41rr4,I:q8){}$M__(N:_490;C:String ;_r,t:Array [String ,0B11011];_:Array [Array [String ,040],0x47];_:Int ;__1,_a,I1LI_,n:_l){} }''','''Class,bC,:,s,{,Constructor,(,W,,,_41rr4,,,I,:,q8,),{,},$M__,(,N,:,_490,;,C,:,String,;,_r,,,t,:,Array,[,String,,,0B11011,],;,_,:,Array,[,Array,[,String,,,040,],,,0x47,],;,_,:,Int,;,__1,,,_a,,,I1LI_,,,n,:,_l,),{,},},<EOF>''',101))

    def test_880(self):
        self.assertTrue(TestLexer.test('''Class L:_{}Class Q_1{Constructor (_N6689,_:Array [String ,0x32];_0,h_m,_:Array [Array [Array [Boolean ,0x32],0x2],012]){} }''','''Class,L,:,_,{,},Class,Q_1,{,Constructor,(,_N6689,,,_,:,Array,[,String,,,0x32,],;,_0,,,h_m,,,_,:,Array,[,Array,[,Array,[,Boolean,,,0x32,],,,0x2,],,,012,],),{,},},<EOF>''',101))

    def test_881(self):
        self.assertTrue(TestLexer.test('''Class Iz{_(_:_3_s;___A:G_){}Constructor (uK:Array [Array [Array [Array [Int ,0X1B],0143],0X19],64];_:_m){Return ;} }Class _B5___NTy{Var Pa_,cZ:String ;}Class __4:_m{}Class _{}Class a:__Z5{}''','''Class,Iz,{,_,(,_,:,_3_s,;,___A,:,G_,),{,},Constructor,(,uK,:,Array,[,Array,[,Array,[,Array,[,Int,,,0X1B,],,,0143,],,,0X19,],,,64,],;,_,:,_m,),{,Return,;,},},Class,_B5___NTy,{,Var,Pa_,,,cZ,:,String,;,},Class,__4,:,_m,{,},Class,_,{,},Class,a,:,__Z5,{,},<EOF>''',101))

    def test_882(self):
        self.assertTrue(TestLexer.test('''Class g_z5{Var _:Array [Array [Array [Array [Array [Boolean ,015],0X3D],0X3D],015],4];Var $m_D_,_t4:String ;}Class U:S{}''','''Class,g_z5,{,Var,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,015,],,,0X3D,],,,0X3D,],,,015,],,,4,],;,Var,$m_D_,,,_t4,:,String,;,},Class,U,:,S,{,},<EOF>''',101))

    def test_883(self):
        self.assertTrue(TestLexer.test('''Class _{Constructor (_1,_3_:Array [Array [String ,1],0xD];eT7_:Array [Array [String ,0B111001],0X9]){Var y6,_3a9,_:String ;} }''','''Class,_,{,Constructor,(,_1,,,_3_,:,Array,[,Array,[,String,,,1,],,,0xD,],;,eT7_,:,Array,[,Array,[,String,,,0B111001,],,,0X9,],),{,Var,y6,,,_3a9,,,_,:,String,;,},},<EOF>''',101))

    def test_884(self):
        self.assertTrue(TestLexer.test('''Class w{Var $eW:Boolean ;}Class X_k:B35{Val $_:Array [Array [Float ,075],13];Val $8:Array [Array [Array [Boolean ,01],13],0b1_1];}''','''Class,w,{,Var,$eW,:,Boolean,;,},Class,X_k,:,B35,{,Val,$_,:,Array,[,Array,[,Float,,,075,],,,13,],;,Val,$8,:,Array,[,Array,[,Array,[,Boolean,,,01,],,,13,],,,0b11,],;,},<EOF>''',101))

    def test_885(self):
        self.assertTrue(TestLexer.test('''Class _x{}Class S:jy{}Class _Pw_0_{}Class q{Destructor (){Return ;Return ;}Constructor (aY___,M5:Array [String ,0110];_:Array [Array [Int ,0110],0110];r,_7:String ;g,_:Array [Array [Array [Boolean ,06],07_4_3],0x10]){} }''','''Class,_x,{,},Class,S,:,jy,{,},Class,_Pw_0_,{,},Class,q,{,Destructor,(,),{,Return,;,Return,;,},Constructor,(,aY___,,,M5,:,Array,[,String,,,0110,],;,_,:,Array,[,Array,[,Int,,,0110,],,,0110,],;,r,,,_7,:,String,;,g,,,_,:,Array,[,Array,[,Array,[,Boolean,,,06,],,,0743,],,,0x10,],),{,},},<EOF>''',101))

    def test_886(self):
        self.assertTrue(TestLexer.test('''Class Q6I:z{}Class _{Ln__j(fQ6,_,_,_,_0,A_Q,i:Array [Array [Array [Int ,0X5B],0x3],0X5B];_:String ){} }Class _6_z6{}''','''Class,Q6I,:,z,{,},Class,_,{,Ln__j,(,fQ6,,,_,,,_,,,_,,,_0,,,A_Q,,,i,:,Array,[,Array,[,Array,[,Int,,,0X5B,],,,0x3,],,,0X5B,],;,_,:,String,),{,},},Class,_6_z6,{,},<EOF>''',101))

    def test_887(self):
        self.assertTrue(TestLexer.test('''Class R_:__X2{}Class _{}Class _2:_{}Class _91{Constructor (_7s_29A0_Qa7U,Hl:Array [Int ,39]){Val _:Boolean ;{} }Var X,$_q77_:w_4;Var $Ug:Float ;}''','''Class,R_,:,__X2,{,},Class,_,{,},Class,_2,:,_,{,},Class,_91,{,Constructor,(,_7s_29A0_Qa7U,,,Hl,:,Array,[,Int,,,39,],),{,Val,_,:,Boolean,;,{,},},Var,X,,,$_q77_,:,w_4,;,Var,$Ug,:,Float,;,},<EOF>''',101))

    def test_888(self):
        self.assertTrue(TestLexer.test('''Class _:_{}Class __XQ:_Z_0{$_(_,_:Array [Array [Array [Array [Array [Float ,7],047],02],98],0X1D];_3,_4:_){}t(){Var B,w5:Array [String ,0b1];} }Class T:Jx{}''','''Class,_,:,_,{,},Class,__XQ,:,_Z_0,{,$_,(,_,,,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,7,],,,047,],,,02,],,,98,],,,0X1D,],;,_3,,,_4,:,_,),{,},t,(,),{,Var,B,,,w5,:,Array,[,String,,,0b1,],;,},},Class,T,:,Jx,{,},<EOF>''',101))

    def test_889(self):
        self.assertTrue(TestLexer.test('''Class e{Destructor (){}Val u_87:Array [Array [Int ,21],032_1_2_4_3_1];Val _,$1,$2_bez:Float ;}Class _:b{}Class _:_{}Class _0{}Class _{Constructor (_:P7_;j:Array [Array [Array [Int ,0x34],0B1001],7];r,_1:Float ){} }Class _:_zv0{Var $_:_g__;}Class __{Var $L__,_:Boolean ;}''','''Class,e,{,Destructor,(,),{,},Val,u_87,:,Array,[,Array,[,Int,,,21,],,,03212431,],;,Val,_,,,$1,,,$2_bez,:,Float,;,},Class,_,:,b,{,},Class,_,:,_,{,},Class,_0,{,},Class,_,{,Constructor,(,_,:,P7_,;,j,:,Array,[,Array,[,Array,[,Int,,,0x34,],,,0B1001,],,,7,],;,r,,,_1,:,Float,),{,},},Class,_,:,_zv0,{,Var,$_,:,_g__,;,},Class,__,{,Var,$L__,,,_,:,Boolean,;,},<EOF>''',101))

    def test_890(self):
        self.assertTrue(TestLexer.test('''Class b45__7{$_2(){} }Class sB:_{Constructor (){}Val G:Array [Float ,0B1001100];Var $_5R,$_g:Array [Array [Float ,0X4_8_5],0b111001];}''','''Class,b45__7,{,$_2,(,),{,},},Class,sB,:,_,{,Constructor,(,),{,},Val,G,:,Array,[,Float,,,0B1001100,],;,Var,$_5R,,,$_g,:,Array,[,Array,[,Float,,,0X485,],,,0b111001,],;,},<EOF>''',101))

    def test_891(self):
        self.assertTrue(TestLexer.test('''Class _:It6Ej{Val cq____:Int ;Var s,$7,m_,$x:Array [Boolean ,0x71];Val _g:Array [Float ,0XA];_A2_5(_,_,_3,_0K,I_:Int ;_:Int ;H6,V8:Array [Array [Array [String ,042],0x31],5_4];_:Int ;_:Array [String ,042];_,k,z_,_:Boolean ;__:K_){} }Class B:__{}Class w_:_2_h0{}Class _:J8{}Class _{}''','''Class,_,:,It6Ej,{,Val,cq____,:,Int,;,Var,s,,,$7,,,m_,,,$x,:,Array,[,Boolean,,,0x71,],;,Val,_g,:,Array,[,Float,,,0XA,],;,_A2_5,(,_,,,_,,,_3,,,_0K,,,I_,:,Int,;,_,:,Int,;,H6,,,V8,:,Array,[,Array,[,Array,[,String,,,042,],,,0x31,],,,54,],;,_,:,Int,;,_,:,Array,[,String,,,042,],;,_,,,k,,,z_,,,_,:,Boolean,;,__,:,K_,),{,},},Class,B,:,__,{,},Class,w_,:,_2_h0,{,},Class,_,:,J8,{,},Class,_,{,},<EOF>''',101))

    def test_892(self):
        self.assertTrue(TestLexer.test('''Class __1:dBYS{Var $_,$9S0:Array [Array [Array [Array [Array [Int ,0B1_0],03],0b110110],2],4_17_6];}Class w_{}Class J8_rd6g1Z:___GM{}''','''Class,__1,:,dBYS,{,Var,$_,,,$9S0,:,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0B10,],,,03,],,,0b110110,],,,2,],,,4176,],;,},Class,w_,{,},Class,J8_rd6g1Z,:,___GM,{,},<EOF>''',101))

    def test_893(self):
        self.assertTrue(TestLexer.test('''Class p:_{}Class f{}Class G_{}Class _41:__{}Class _:_Yn{}Class _:_59K{}Class i:_{}Class _:__5_{}Class _{Var $A:String ;Val $_:Array [String ,0X1F];}Class O:_{Destructor (){ {}{Return ;} }}Class _:_{}''','''Class,p,:,_,{,},Class,f,{,},Class,G_,{,},Class,_41,:,__,{,},Class,_,:,_Yn,{,},Class,_,:,_59K,{,},Class,i,:,_,{,},Class,_,:,__5_,{,},Class,_,{,Var,$A,:,String,;,Val,$_,:,Array,[,String,,,0X1F,],;,},Class,O,:,_,{,Destructor,(,),{,{,},{,Return,;,},},},Class,_,:,_,{,},<EOF>''',101))

    def test_894(self):
        self.assertTrue(TestLexer.test('''Class _:X{$f(){ {}Val H,_,At09:Array [Array [Array [Array [Array [Array [Array [Float ,0b10_10],0X58],0B1011010],0X58],0B11],0b1011111],4];}Constructor (){} }''','''Class,_,:,X,{,$f,(,),{,{,},Val,H,,,_,,,At09,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0b1010,],,,0X58,],,,0B1011010,],,,0X58,],,,0B11,],,,0b1011111,],,,4,],;,},Constructor,(,),{,},},<EOF>''',101))

    def test_895(self):
        self.assertTrue(TestLexer.test('''Class _:V{}Class b:L3_{Var j,$4:Boolean ;Val $ZC:D;Var $_l_:Array [String ,2];}Class B_2R9h{Var bp:String ;}Class S{}''','''Class,_,:,V,{,},Class,b,:,L3_,{,Var,j,,,$4,:,Boolean,;,Val,$ZC,:,D,;,Var,$_l_,:,Array,[,String,,,2,],;,},Class,B_2R9h,{,Var,bp,:,String,;,},Class,S,{,},<EOF>''',101))

    def test_896(self):
        self.assertTrue(TestLexer.test('''Class _60{}Class bs8:_{$1__WV5(_7_2f,H,_,_0:Array [Boolean ,79_8];v_,ZA,_8,_0:Array [Array [Int ,78],5_1_4_8]){} }''','''Class,_60,{,},Class,bs8,:,_,{,$1__WV5,(,_7_2f,,,H,,,_,,,_0,:,Array,[,Boolean,,,798,],;,v_,,,ZA,,,_8,,,_0,:,Array,[,Array,[,Int,,,78,],,,5148,],),{,},},<EOF>''',101))

    def test_897(self):
        self.assertTrue(TestLexer.test('''Class ey7:_U_829Y0__o{}Class _{}Class mf3_P{}Class __:_{$_(___3:Boolean ;__8:String ){Break ;}Val X:Array [Float ,06];}Class YB1z_6eC_W{Var $7:L;}''','''Class,ey7,:,_U_829Y0__o,{,},Class,_,{,},Class,mf3_P,{,},Class,__,:,_,{,$_,(,___3,:,Boolean,;,__8,:,String,),{,Break,;,},Val,X,:,Array,[,Float,,,06,],;,},Class,YB1z_6eC_W,{,Var,$7,:,L,;,},<EOF>''',101))

    def test_898(self):
        self.assertTrue(TestLexer.test('''Class _xF_99{Val $H_:Boolean ;}Class hW_:O{$9(_7:Boolean ){}Var SM:Int ;Destructor (){} }Class w:_K{Destructor (){_::$_();} }''','''Class,_xF_99,{,Val,$H_,:,Boolean,;,},Class,hW_,:,O,{,$9,(,_7,:,Boolean,),{,},Var,SM,:,Int,;,Destructor,(,),{,},},Class,w,:,_K,{,Destructor,(,),{,_,::,$_,(,),;,},},<EOF>''',101))

    def test_899(self):
        self.assertTrue(TestLexer.test('''Class D_D__E0_{}Class _57_:__{}Class _v{Constructor (T_:Int ){}Val $H0,$__:Array [Boolean ,3_7_3_5];Constructor (W:_;e75:Boolean ){} }''','''Class,D_D__E0_,{,},Class,_57_,:,__,{,},Class,_v,{,Constructor,(,T_,:,Int,),{,},Val,$H0,,,$__,:,Array,[,Boolean,,,3735,],;,Constructor,(,W,:,_,;,e75,:,Boolean,),{,},},<EOF>''',101))

    def test_900(self):
        self.assertTrue(TestLexer.test('''Class Hw:w8__zc{}Class _0:_7{_(){}Var $S,$V_:Array [Array [Array [Array [Float ,8_3658_8],0xB_8_E_EA],053],0b100011];}''','''Class,Hw,:,w8__zc,{,},Class,_0,:,_7,{,_,(,),{,},Var,$S,,,$V_,:,Array,[,Array,[,Array,[,Array,[,Float,,,836588,],,,0xB8EEA,],,,053,],,,0b100011,],;,},<EOF>''',101))

    def test_901(self):
        self.assertTrue(TestLexer.test('''Class zK_{Constructor (w:Array [String ,0X55];_99,G0rHX_71:Float ){}Val $g8y4_,$_,$A,_r,$_:Array [Boolean ,0XF6];Val v89:Int ;}''','''Class,zK_,{,Constructor,(,w,:,Array,[,String,,,0X55,],;,_99,,,G0rHX_71,:,Float,),{,},Val,$g8y4_,,,$_,,,$A,,,_r,,,$_,:,Array,[,Boolean,,,0XF6,],;,Val,v89,:,Int,;,},<EOF>''',101))

    def test_902(self):
        self.assertTrue(TestLexer.test('''Class lc:__v__{}Class o5_1_:_6{Val $b__:Array [Array [Array [Float ,0XA05_7A],0X9_F],0X64];Val $j,$_LO1_e_yr,$k:v;Val _5:Boolean ;Val _f:Array [Boolean ,4];}Class __{}''','''Class,lc,:,__v__,{,},Class,o5_1_,:,_6,{,Val,$b__,:,Array,[,Array,[,Array,[,Float,,,0XA057A,],,,0X9F,],,,0X64,],;,Val,$j,,,$_LO1_e_yr,,,$k,:,v,;,Val,_5,:,Boolean,;,Val,_f,:,Array,[,Boolean,,,4,],;,},Class,__,{,},<EOF>''',101))

    def test_903(self):
        self.assertTrue(TestLexer.test('''Class d{Val _5,$K,$_:Array [Array [Array [Array [Array [Array [Array [Boolean ,0B1],0b1],93],0x2A],0b1],01],0xF_8];Constructor (_:String ;_:Array [String ,0b1]){ {{Break ;} }Break ;}Val v:Array [Array [String ,93],23];}''','''Class,d,{,Val,_5,,,$K,,,$_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0B1,],,,0b1,],,,93,],,,0x2A,],,,0b1,],,,01,],,,0xF8,],;,Constructor,(,_,:,String,;,_,:,Array,[,String,,,0b1,],),{,{,{,Break,;,},},Break,;,},Val,v,:,Array,[,Array,[,String,,,93,],,,23,],;,},<EOF>''',101))

    def test_904(self):
        self.assertTrue(TestLexer.test('''Class b{Var Z,hI:Array [Float ,6];Val $2k_,z:Array [Int ,0107];$____P_(_,_,p6P5:Int ){__7q55j3::$P();}Destructor (){}Destructor (){} }''','''Class,b,{,Var,Z,,,hI,:,Array,[,Float,,,6,],;,Val,$2k_,,,z,:,Array,[,Int,,,0107,],;,$____P_,(,_,,,_,,,p6P5,:,Int,),{,__7q55j3,::,$P,(,),;,},Destructor,(,),{,},Destructor,(,),{,},},<EOF>''',101))

    def test_905(self):
        self.assertTrue(TestLexer.test('''Class wN:_{Constructor (_:___6;n,G_:Float ;S__T8S5:Array [Boolean ,0X15];_,_,_,X8:k){}Val _4:R_;}Class __:_3n93{Var $9:h_4;}''','''Class,wN,:,_,{,Constructor,(,_,:,___6,;,n,,,G_,:,Float,;,S__T8S5,:,Array,[,Boolean,,,0X15,],;,_,,,_,,,_,,,X8,:,k,),{,},Val,_4,:,R_,;,},Class,__,:,_3n93,{,Var,$9,:,h_4,;,},<EOF>''',101))

    def test_906(self):
        self.assertTrue(TestLexer.test('''Class u20_:_{}Class Ew_5:__v6_{Var _,$___,$_,BQ1:Array [Array [Array [Float ,040],02],0b1011100];}Class _{Var $6:Array [Boolean ,0B1_0100_1]=_c::$Q1h0.N;Destructor (){}Constructor (){}Var $_,$47:String ;}Class _:_{}Class d{Destructor (){} }Class _5:W4__{}''','''Class,u20_,:,_,{,},Class,Ew_5,:,__v6_,{,Var,_,,,$___,,,$_,,,BQ1,:,Array,[,Array,[,Array,[,Float,,,040,],,,02,],,,0b1011100,],;,},Class,_,{,Var,$6,:,Array,[,Boolean,,,0B101001,],=,_c,::,$Q1h0,.,N,;,Destructor,(,),{,},Constructor,(,),{,},Var,$_,,,$47,:,String,;,},Class,_,:,_,{,},Class,d,{,Destructor,(,),{,},},Class,_5,:,W4__,{,},<EOF>''',101))

    def test_907(self):
        self.assertTrue(TestLexer.test('''Class kK:k{Destructor (){}Constructor (__:Array [Array [Array [Int ,0131],0B1010101],66]){ {} }}Class a:x{Var _5I8,$_Q:n3;}''','''Class,kK,:,k,{,Destructor,(,),{,},Constructor,(,__,:,Array,[,Array,[,Array,[,Int,,,0131,],,,0B1010101,],,,66,],),{,{,},},},Class,a,:,x,{,Var,_5I8,,,$_Q,:,n3,;,},<EOF>''',101))

    def test_908(self):
        self.assertTrue(TestLexer.test('''Class p{}Class _95{}Class _{Constructor (X,E__,_c:Array [Array [String ,0x4_8_5_9],024]){} }Class T{Val $_LU_,d,_Z:e;}''','''Class,p,{,},Class,_95,{,},Class,_,{,Constructor,(,X,,,E__,,,_c,:,Array,[,Array,[,String,,,0x4859,],,,024,],),{,},},Class,T,{,Val,$_LU_,,,d,,,_Z,:,e,;,},<EOF>''',101))

    def test_909(self):
        self.assertTrue(TestLexer.test('''Class c_{Constructor (){Val _,_6:_3_;}$__(_5,_9__7,_681:Array [Array [String ,03],25];__,_D2,B,_0:Array [Float ,0b1100001];P:Boolean ;_9:D;h5c3:T;K_,_:Array [Array [Array [String ,25],0xC],06_34]){} }''','''Class,c_,{,Constructor,(,),{,Val,_,,,_6,:,_3_,;,},$__,(,_5,,,_9__7,,,_681,:,Array,[,Array,[,String,,,03,],,,25,],;,__,,,_D2,,,B,,,_0,:,Array,[,Float,,,0b1100001,],;,P,:,Boolean,;,_9,:,D,;,h5c3,:,T,;,K_,,,_,:,Array,[,Array,[,Array,[,String,,,25,],,,0xC,],,,0634,],),{,},},<EOF>''',101))

    def test_910(self):
        self.assertTrue(TestLexer.test('''Class __{}Class BE:_{Constructor (__,_:Float ){} }Class d:_c_{}Class _d:L{}Class _:_{Destructor (){Continue ;}Val j,__,_S1_1_:_;}''','''Class,__,{,},Class,BE,:,_,{,Constructor,(,__,,,_,:,Float,),{,},},Class,d,:,_c_,{,},Class,_d,:,L,{,},Class,_,:,_,{,Destructor,(,),{,Continue,;,},Val,j,,,__,,,_S1_1_,:,_,;,},<EOF>''',101))

    def test_911(self):
        self.assertTrue(TestLexer.test('''Class _:_{Var _1g__8:Array [Array [Array [Float ,1],0x7E],0B1011001]=!Null *!!!-_05L::$_().v9L;Destructor (){} }Class oD{}Class _{}''','''Class,_,:,_,{,Var,_1g__8,:,Array,[,Array,[,Array,[,Float,,,1,],,,0x7E,],,,0B1011001,],=,!,Null,*,!,!,!,-,_05L,::,$_,(,),.,v9L,;,Destructor,(,),{,},},Class,oD,{,},Class,_,{,},<EOF>''',101))

    def test_912(self):
        self.assertTrue(TestLexer.test('''Class c{Val _0,d:e;Val e_,t:Array [Float ,0XE];}Class _k79{}Class z:xy{Val $0_,$i_,a7_:Array [Array [Array [Array [Boolean ,0x5_F],06],0X2_28],07];Destructor (){Continue ;} }''','''Class,c,{,Val,_0,,,d,:,e,;,Val,e_,,,t,:,Array,[,Float,,,0XE,],;,},Class,_k79,{,},Class,z,:,xy,{,Val,$0_,,,$i_,,,a7_,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,0x5F,],,,06,],,,0X228,],,,07,],;,Destructor,(,),{,Continue,;,},},<EOF>''',101))

    def test_913(self):
        self.assertTrue(TestLexer.test('''Class __K__{Constructor (_:_;_x,_f:_;_,d,_:_;__1:Array [String ,0b10101];_,_:Float ;m6:__p;_,x,TN,__c_,yC:T){} }Class _:z_{}Class Q:_{}''','''Class,__K__,{,Constructor,(,_,:,_,;,_x,,,_f,:,_,;,_,,,d,,,_,:,_,;,__1,:,Array,[,String,,,0b10101,],;,_,,,_,:,Float,;,m6,:,__p,;,_,,,x,,,TN,,,__c_,,,yC,:,T,),{,},},Class,_,:,z_,{,},Class,Q,:,_,{,},<EOF>''',101))

    def test_914(self):
        self.assertTrue(TestLexer.test('''Class _:__G_{$8(){}Var _6,A71:Array [Array [Array [String ,0B1_0_1_1],055],6];Constructor (_4,_3D7F_,u:Array [String ,47_7]){Break ;}Destructor (){} }Class q{}Class _:__D3{$6(T:Array [Array [Array [String ,0XE5],8],055];_,_u:M;_6_,k,bo:Array [Array [Array [Array [Array [Int ,07_14_6_2],07],0X46],036],0B101101]){} }Class _{}''','''Class,_,:,__G_,{,$8,(,),{,},Var,_6,,,A71,:,Array,[,Array,[,Array,[,String,,,0B1011,],,,055,],,,6,],;,Constructor,(,_4,,,_3D7F_,,,u,:,Array,[,String,,,477,],),{,Break,;,},Destructor,(,),{,},},Class,q,{,},Class,_,:,__D3,{,$6,(,T,:,Array,[,Array,[,Array,[,String,,,0XE5,],,,8,],,,055,],;,_,,,_u,:,M,;,_6_,,,k,,,bo,:,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,071462,],,,07,],,,0X46,],,,036,],,,0B101101,],),{,},},Class,_,{,},<EOF>''',101))

    def test_915(self):
        self.assertTrue(TestLexer.test('''Class _{Var __,_s,$3,$_7:Array [Int ,84];Constructor (_R2__4:__08Lk;_4:Array [Array [Array [Int ,84],0b11],0141]){}Var _,_,_,$_:Array [Array [Array [String ,0b1],0x5_6],3];}''','''Class,_,{,Var,__,,,_s,,,$3,,,$_7,:,Array,[,Int,,,84,],;,Constructor,(,_R2__4,:,__08Lk,;,_4,:,Array,[,Array,[,Array,[,Int,,,84,],,,0b11,],,,0141,],),{,},Var,_,,,_,,,_,,,$_,:,Array,[,Array,[,Array,[,String,,,0b1,],,,0x56,],,,3,],;,},<EOF>''',101))

    def test_916(self):
        self.assertTrue(TestLexer.test('''Class Ejeb7_2:K{}Class f:_{Val U,Q7H_f:Boolean ;}Class _:_{Constructor (s,_,__7:F_;u:Array [Array [Array [Array [Array [Boolean ,0100],0x11],9],0100],05_6]){Var f_:Array [Float ,0100];} }''','''Class,Ejeb7_2,:,K,{,},Class,f,:,_,{,Val,U,,,Q7H_f,:,Boolean,;,},Class,_,:,_,{,Constructor,(,s,,,_,,,__7,:,F_,;,u,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0100,],,,0x11,],,,9,],,,0100,],,,056,],),{,Var,f_,:,Array,[,Float,,,0100,],;,},},<EOF>''',101))

    def test_917(self):
        self.assertTrue(TestLexer.test('''Class x:_{}Class r__{Val $5,f,_1567,$M:Array [Int ,81];}Class _:F{}Class _1:vD{}Class O4_:d{Constructor (_:Int ){} }''','''Class,x,:,_,{,},Class,r__,{,Val,$5,,,f,,,_1567,,,$M,:,Array,[,Int,,,81,],;,},Class,_,:,F,{,},Class,_1,:,vD,{,},Class,O4_,:,d,{,Constructor,(,_,:,Int,),{,},},<EOF>''',101))

    def test_918(self):
        self.assertTrue(TestLexer.test('''Class _4{Constructor (_,_,_:Array [Array [Array [Array [Array [Array [Float ,0X2C],0B1_1],0B1],2],0xA],1];tW_,Dk,Y:e;ltnl:Boolean ){Break ;} }''','''Class,_4,{,Constructor,(,_,,,_,,,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0X2C,],,,0B11,],,,0B1,],,,2,],,,0xA,],,,1,],;,tW_,,,Dk,,,Y,:,e,;,ltnl,:,Boolean,),{,Break,;,},},<EOF>''',101))

    def test_919(self):
        self.assertTrue(TestLexer.test('''Class _u_58{}Class w{Constructor (_6H:Array [String ,072];zS978:Float ;_K:Array [Array [Boolean ,0X6_B_E_E6],39];Tv1T_7n:Array [Boolean ,0B10];C_:Array [Array [Float ,0XF],02]){} }Class _:D64{Val _1,$0:ca;}Class _8{}''','''Class,_u_58,{,},Class,w,{,Constructor,(,_6H,:,Array,[,String,,,072,],;,zS978,:,Float,;,_K,:,Array,[,Array,[,Boolean,,,0X6BEE6,],,,39,],;,Tv1T_7n,:,Array,[,Boolean,,,0B10,],;,C_,:,Array,[,Array,[,Float,,,0XF,],,,02,],),{,},},Class,_,:,D64,{,Val,_1,,,$0,:,ca,;,},Class,_8,{,},<EOF>''',101))

    def test_920(self):
        self.assertTrue(TestLexer.test('''Class P:_x{}Class ad{}Class _7:D{Var o_U,$_w08__:_O98_T;}Class _9_8_32:p2{}Class J_O:L{Val $_b:Array [String ,0X5F];Constructor (){ {Continue ;} }}''','''Class,P,:,_x,{,},Class,ad,{,},Class,_7,:,D,{,Var,o_U,,,$_w08__,:,_O98_T,;,},Class,_9_8_32,:,p2,{,},Class,J_O,:,L,{,Val,$_b,:,Array,[,String,,,0X5F,],;,Constructor,(,),{,{,Continue,;,},},},<EOF>''',101))

    def test_921(self):
        self.assertTrue(TestLexer.test('''Class _{Constructor (h_,px:Array [Array [String ,33],0X926_7_E];O2,R___:_;e4V,RiP,__,b,__,_5w:Array [String ,0b1]){} }''','''Class,_,{,Constructor,(,h_,,,px,:,Array,[,Array,[,String,,,33,],,,0X9267E,],;,O2,,,R___,:,_,;,e4V,,,RiP,,,__,,,b,,,__,,,_5w,:,Array,[,String,,,0b1,],),{,},},<EOF>''',101))

    def test_922(self):
        self.assertTrue(TestLexer.test('''Class _6_y_1_{Constructor (){u::$kY7__3n().Lfa();Val _:Array [Array [Array [Array [Array [Float ,0B1],010],0b1000],0b1],0X3B];} }Class O0{}''','''Class,_6_y_1_,{,Constructor,(,),{,u,::,$kY7__3n,(,),.,Lfa,(,),;,Val,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0B1,],,,010,],,,0b1000,],,,0b1,],,,0X3B,],;,},},Class,O0,{,},<EOF>''',101))

    def test_923(self):
        self.assertTrue(TestLexer.test('''Class _4{Destructor (){Break ;{} }Val _5__X,_,Q_:String ;}Class __{}Class _O:b_0_6U3{$_(_:_;I_0:String ){}Constructor (){}__(){}Destructor (){}Constructor (){} }''','''Class,_4,{,Destructor,(,),{,Break,;,{,},},Val,_5__X,,,_,,,Q_,:,String,;,},Class,__,{,},Class,_O,:,b_0_6U3,{,$_,(,_,:,_,;,I_0,:,String,),{,},Constructor,(,),{,},__,(,),{,},Destructor,(,),{,},Constructor,(,),{,},},<EOF>''',101))

    def test_924(self):
        self.assertTrue(TestLexer.test('''Class q{Constructor (_,_,_,_,x,y,IOKJA:Array [Boolean ,045_4];l_V:Int ;_7:Array [Array [Array [Array [Array [Array [Int ,0B11011],0x35],0xC6],0b1],0X30],0262_0]){ {Val _:Array [Int ,0X30];} }}Class X{}Class _h{}''','''Class,q,{,Constructor,(,_,,,_,,,_,,,_,,,x,,,y,,,IOKJA,:,Array,[,Boolean,,,0454,],;,l_V,:,Int,;,_7,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0B11011,],,,0x35,],,,0xC6,],,,0b1,],,,0X30,],,,02620,],),{,{,Val,_,:,Array,[,Int,,,0X30,],;,},},},Class,X,{,},Class,_h,{,},<EOF>''',101))

    def test_925(self):
        self.assertTrue(TestLexer.test('''Class U0__2{}Class p{}Class c:f{Val n7,__1u,_70l5,G:Array [String ,03];B_(X,_J:Array [Boolean ,0B1];vgl_,_4:_7;W,k2:_;n,_,__V2WG269,_,X:___6_){} }Class v_m3_{Constructor (){} }Class G{Val $0_8z:f8;}Class _9_{Val c:Float ;}Class _:Lw{}Class b{Val _4:Boolean ;Var r,Ps:Array [Array [Array [String ,0xA0],0B1],0B10_1];Val $d,E___,X1_,_J7:Int ;}''','''Class,U0__2,{,},Class,p,{,},Class,c,:,f,{,Val,n7,,,__1u,,,_70l5,,,G,:,Array,[,String,,,03,],;,B_,(,X,,,_J,:,Array,[,Boolean,,,0B1,],;,vgl_,,,_4,:,_7,;,W,,,k2,:,_,;,n,,,_,,,__V2WG269,,,_,,,X,:,___6_,),{,},},Class,v_m3_,{,Constructor,(,),{,},},Class,G,{,Val,$0_8z,:,f8,;,},Class,_9_,{,Val,c,:,Float,;,},Class,_,:,Lw,{,},Class,b,{,Val,_4,:,Boolean,;,Var,r,,,Ps,:,Array,[,Array,[,Array,[,String,,,0xA0,],,,0B1,],,,0B101,],;,Val,$d,,,E___,,,X1_,,,_J7,:,Int,;,},<EOF>''',101))

    def test_926(self):
        self.assertTrue(TestLexer.test('''Class r{}Class _Aq_{}Class N:n60{Var $i_,_8_9,$_t:Boolean ;Constructor (S:Array [Array [Array [Float ,3],0b1_0],061]){Continue ;} }''','''Class,r,{,},Class,_Aq_,{,},Class,N,:,n60,{,Var,$i_,,,_8_9,,,$_t,:,Boolean,;,Constructor,(,S,:,Array,[,Array,[,Array,[,Float,,,3,],,,0b10,],,,061,],),{,Continue,;,},},<EOF>''',101))

    def test_927(self):
        self.assertTrue(TestLexer.test('''Class _:_J{$0g8(sv,X_:_;_:KlW40_02;_,__2pC1_T:Array [Array [Array [String ,0X5F],48],07_2_0_6];_,___,Q,_6__:Array [String ,0141];___:String ){}Var $_140n,$8_,w_8:Array [Float ,0141];Destructor (){} }''','''Class,_,:,_J,{,$0g8,(,sv,,,X_,:,_,;,_,:,KlW40_02,;,_,,,__2pC1_T,:,Array,[,Array,[,Array,[,String,,,0X5F,],,,48,],,,07206,],;,_,,,___,,,Q,,,_6__,:,Array,[,String,,,0141,],;,___,:,String,),{,},Var,$_140n,,,$8_,,,w_8,:,Array,[,Float,,,0141,],;,Destructor,(,),{,},},<EOF>''',101))

    def test_928(self):
        self.assertTrue(TestLexer.test('''Class _{}Class _W{P67_(_,__1:Array [String ,7];S,__:String ){} }Class a:__{Val $P,$A,C:_;}Class _:G{Constructor (){} }Class _Kz{}Class j{}Class __{Destructor (){} }Class _9{}Class y:A{}''','''Class,_,{,},Class,_W,{,P67_,(,_,,,__1,:,Array,[,String,,,7,],;,S,,,__,:,String,),{,},},Class,a,:,__,{,Val,$P,,,$A,,,C,:,_,;,},Class,_,:,G,{,Constructor,(,),{,},},Class,_Kz,{,},Class,j,{,},Class,__,{,Destructor,(,),{,},},Class,_9,{,},Class,y,:,A,{,},<EOF>''',101))

    def test_929(self):
        self.assertTrue(TestLexer.test('''Class Qao5{}Class p:KP{}Class _:_{Constructor (U,a_0G:_){Return ;Return ;}Constructor (){} }Class _{}Class _:O{Constructor (){} }''','''Class,Qao5,{,},Class,p,:,KP,{,},Class,_,:,_,{,Constructor,(,U,,,a_0G,:,_,),{,Return,;,Return,;,},Constructor,(,),{,},},Class,_,{,},Class,_,:,O,{,Constructor,(,),{,},},<EOF>''',101))

    def test_930(self):
        self.assertTrue(TestLexer.test('''Class x2:_{_(c,K_,_z:Array [Array [Boolean ,55],020];W,f:q;_,Z_:E;E:n){}Var $___,J:String ;}Class rx:_{Destructor (){} }Class _r:__64gP{}Class __:_O{}''','''Class,x2,:,_,{,_,(,c,,,K_,,,_z,:,Array,[,Array,[,Boolean,,,55,],,,020,],;,W,,,f,:,q,;,_,,,Z_,:,E,;,E,:,n,),{,},Var,$___,,,J,:,String,;,},Class,rx,:,_,{,Destructor,(,),{,},},Class,_r,:,__64gP,{,},Class,__,:,_O,{,},<EOF>''',101))

    def test_931(self):
        self.assertTrue(TestLexer.test('''Class F{$K7i(){} }Class Z{Val P_,F_9_:s;}Class _{Destructor (){Break ;} }Class __:L___{Val $o:Array [Array [String ,0x5],14];}Class _:_{}''','''Class,F,{,$K7i,(,),{,},},Class,Z,{,Val,P_,,,F_9_,:,s,;,},Class,_,{,Destructor,(,),{,Break,;,},},Class,__,:,L___,{,Val,$o,:,Array,[,Array,[,String,,,0x5,],,,14,],;,},Class,_,:,_,{,},<EOF>''',101))

    def test_932(self):
        self.assertTrue(TestLexer.test('''Class W:i{Var $q1_V_j2z_:String ;}Class _1:Y{}Class N{Var $X8_,_i,$O8,_2:Array [Int ,91];}Class __{}Class _:__3_{}''','''Class,W,:,i,{,Var,$q1_V_j2z_,:,String,;,},Class,_1,:,Y,{,},Class,N,{,Var,$X8_,,,_i,,,$O8,,,_2,:,Array,[,Int,,,91,],;,},Class,__,{,},Class,_,:,__3_,{,},<EOF>''',101))

    def test_933(self):
        self.assertTrue(TestLexer.test('''Class __{Val ___:G_FF;$vL_(_,_:String ;__:Float ;_,d:V_;P_7,_:Array [Array [Array [Array [Int ,82],0x60],0103],0b11]){} }Class wuU{Destructor (){} }''','''Class,__,{,Val,___,:,G_FF,;,$vL_,(,_,,,_,:,String,;,__,:,Float,;,_,,,d,:,V_,;,P_7,,,_,:,Array,[,Array,[,Array,[,Array,[,Int,,,82,],,,0x60,],,,0103,],,,0b11,],),{,},},Class,wuU,{,Destructor,(,),{,},},<EOF>''',101))

    def test_934(self):
        self.assertTrue(TestLexer.test('''Class r{$_(h:Array [Array [Array [Array [Array [Array [Boolean ,0617_55],0b1111],0b1_11],0B11010],6],0b1];_N7i,A_:Boolean ){} }Class _{}Class ___:_{}''','''Class,r,{,$_,(,h,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,061755,],,,0b1111,],,,0b111,],,,0B11010,],,,6,],,,0b1,],;,_N7i,,,A_,:,Boolean,),{,},},Class,_,{,},Class,___,:,_,{,},<EOF>''',101))

    def test_935(self):
        self.assertTrue(TestLexer.test('''Class u2P:_8{Destructor (){} }Class __D:e4{}Class _{Var g,$1U1f_,$h_:_;Var X,u_:Int ;}Class K:_{}Class d85__1{}Class ___2:_{}Class m_2:g{Var $__S,P:Int ;}''','''Class,u2P,:,_8,{,Destructor,(,),{,},},Class,__D,:,e4,{,},Class,_,{,Var,g,,,$1U1f_,,,$h_,:,_,;,Var,X,,,u_,:,Int,;,},Class,K,:,_,{,},Class,d85__1,{,},Class,___2,:,_,{,},Class,m_2,:,g,{,Var,$__S,,,P,:,Int,;,},<EOF>''',101))

    def test_936(self):
        self.assertTrue(TestLexer.test('''Class D:_{Constructor (_Xk,_,____e__at,H4x3_M,__:String ){ {Val r,i:Array [Array [Array [Boolean ,0130],02_21_3_74],55];Break ;Continue ;} }Val R_:Array [Array [String ,0130],0B1];}''','''Class,D,:,_,{,Constructor,(,_Xk,,,_,,,____e__at,,,H4x3_M,,,__,:,String,),{,{,Val,r,,,i,:,Array,[,Array,[,Array,[,Boolean,,,0130,],,,0221374,],,,55,],;,Break,;,Continue,;,},},Val,R_,:,Array,[,Array,[,String,,,0130,],,,0B1,],;,},<EOF>''',101))

    def test_937(self):
        self.assertTrue(TestLexer.test('''Class uw{Val $B_4:Array [Array [Array [Array [Array [Boolean ,04],07],0X3],88],0b1];Val __9:Array [String ,04];$_u(C6_6k,__6Y_:Int ){} }Class J{Destructor (){}Val $_t14,T_79_2B__5,_s29k,_,$r:x;Constructor (){} }''','''Class,uw,{,Val,$B_4,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,04,],,,07,],,,0X3,],,,88,],,,0b1,],;,Val,__9,:,Array,[,String,,,04,],;,$_u,(,C6_6k,,,__6Y_,:,Int,),{,},},Class,J,{,Destructor,(,),{,},Val,$_t14,,,T_79_2B__5,,,_s29k,,,_,,,$r,:,x,;,Constructor,(,),{,},},<EOF>''',101))

    def test_938(self):
        self.assertTrue(TestLexer.test('''Class _:s{}Class F_{Var $A5,$J_:Array [Int ,0x19];}Class _5:_{Constructor (){}$2(_,C0,G:Boolean ){}Var _v,m39_,$X,$__m:Float ;}''','''Class,_,:,s,{,},Class,F_,{,Var,$A5,,,$J_,:,Array,[,Int,,,0x19,],;,},Class,_5,:,_,{,Constructor,(,),{,},$2,(,_,,,C0,,,G,:,Boolean,),{,},Var,_v,,,m39_,,,$X,,,$__m,:,Float,;,},<EOF>''',101))

    def test_939(self):
        self.assertTrue(TestLexer.test('''Class _3:_{Constructor (j1k,a8__:Array [Boolean ,0x5];a:Array [Array [Array [Array [Boolean ,0b1000111],0X7D],0x3],0b1000111];X,_6:_3;y,L5:Float ;m_:Boolean ){} }Class q{}''','''Class,_3,:,_,{,Constructor,(,j1k,,,a8__,:,Array,[,Boolean,,,0x5,],;,a,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,0b1000111,],,,0X7D,],,,0x3,],,,0b1000111,],;,X,,,_6,:,_3,;,y,,,L5,:,Float,;,m_,:,Boolean,),{,},},Class,q,{,},<EOF>''',101))

    def test_940(self):
        self.assertTrue(TestLexer.test('''Class _:Z__{Destructor (){}Val $__,$_9,P5:D;Val $_Y,$9_1_:Array [Float ,07_3];Constructor (_,_,_:Array [String ,0B1010101]){}Constructor (){} }Class _0_{}''','''Class,_,:,Z__,{,Destructor,(,),{,},Val,$__,,,$_9,,,P5,:,D,;,Val,$_Y,,,$9_1_,:,Array,[,Float,,,073,],;,Constructor,(,_,,,_,,,_,:,Array,[,String,,,0B1010101,],),{,},Constructor,(,),{,},},Class,_0_,{,},<EOF>''',101))

    def test_941(self):
        self.assertTrue(TestLexer.test('''Class Y0:_{Constructor (d95,Am:Array [Array [Array [Array [Array [Boolean ,0b1001000],0b1],0X4],037],0X18];_:t;_,c:Boolean ;__:Boolean ){} }''','''Class,Y0,:,_,{,Constructor,(,d95,,,Am,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0b1001000,],,,0b1,],,,0X4,],,,037,],,,0X18,],;,_,:,t,;,_,,,c,:,Boolean,;,__,:,Boolean,),{,},},<EOF>''',101))

    def test_942(self):
        self.assertTrue(TestLexer.test('''Class c:dX4{Val _:Int ;$__Z(bk:Int ;W:Array [Array [Float ,05],0B1_1];_1:Boolean ;m,_:Array [Array [Array [Array [Array [Array [Array [Array [Float ,01],01],01],0B101001],01],0X719],7],055]){} }Class _V{}''','''Class,c,:,dX4,{,Val,_,:,Int,;,$__Z,(,bk,:,Int,;,W,:,Array,[,Array,[,Float,,,05,],,,0B11,],;,_1,:,Boolean,;,m,,,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,01,],,,01,],,,01,],,,0B101001,],,,01,],,,0X719,],,,7,],,,055,],),{,},},Class,_V,{,},<EOF>''',101))

    def test_943(self):
        self.assertTrue(TestLexer.test('''Class _{Var _,$_6:String ;}Class J{Var $Nd_:Array [Array [Array [String ,05_3],0X5D],0x62];}Class u{}Class q{}Class I:_{}Class _{}Class __V{Destructor (){} }''','''Class,_,{,Var,_,,,$_6,:,String,;,},Class,J,{,Var,$Nd_,:,Array,[,Array,[,Array,[,String,,,053,],,,0X5D,],,,0x62,],;,},Class,u,{,},Class,q,{,},Class,I,:,_,{,},Class,_,{,},Class,__V,{,Destructor,(,),{,},},<EOF>''',101))

    def test_944(self):
        self.assertTrue(TestLexer.test('''Class _l3:Re{Constructor (_:Array [Float ,2];_,m,__:Array [Array [Array [Array [Array [Boolean ,04_1],0X27],8_21],0X27],59]){Break ;} }Class _m:m_{}''','''Class,_l3,:,Re,{,Constructor,(,_,:,Array,[,Float,,,2,],;,_,,,m,,,__,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,041,],,,0X27,],,,821,],,,0X27,],,,59,],),{,Break,;,},},Class,_m,:,m_,{,},<EOF>''',101))

    def test_945(self):
        self.assertTrue(TestLexer.test('''Class _{Destructor (){Break ;}Var CH,K_T2:a;_xq_(){}Var $7,$M:Array [Array [Int ,49],8_4_61];}Class _{}Class _4{}''','''Class,_,{,Destructor,(,),{,Break,;,},Var,CH,,,K_T2,:,a,;,_xq_,(,),{,},Var,$7,,,$M,:,Array,[,Array,[,Int,,,49,],,,8461,],;,},Class,_,{,},Class,_4,{,},<EOF>''',101))

    def test_946(self):
        self.assertTrue(TestLexer.test('''Class a{Var G:Boolean ;$3(){}Destructor (){Var _j,K__:Boolean ;}Val $Z4J,__38:Array [Array [Float ,052767_31],48];Var m:_;}''','''Class,a,{,Var,G,:,Boolean,;,$3,(,),{,},Destructor,(,),{,Var,_j,,,K__,:,Boolean,;,},Val,$Z4J,,,__38,:,Array,[,Array,[,Float,,,05276731,],,,48,],;,Var,m,:,_,;,},<EOF>''',101))

    def test_947(self):
        self.assertTrue(TestLexer.test('''Class x___:_3{}Class _V:_{Val _:Array [Array [Array [Int ,0124],0b1],0b1];}Class _:_2{Destructor (){}Destructor (){} }''','''Class,x___,:,_3,{,},Class,_V,:,_,{,Val,_,:,Array,[,Array,[,Array,[,Int,,,0124,],,,0b1,],,,0b1,],;,},Class,_,:,_2,{,Destructor,(,),{,},Destructor,(,),{,},},<EOF>''',101))

    def test_948(self):
        self.assertTrue(TestLexer.test('''Class _3{$9(N,_V__,_:Int ;_P,_M:Array [Array [Array [Array [Array [Boolean ,03],0122],0b1011000],0B1],0B101111]){ {}Continue ;Break ;} }''','''Class,_3,{,$9,(,N,,,_V__,,,_,:,Int,;,_P,,,_M,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,03,],,,0122,],,,0b1011000,],,,0B1,],,,0B101111,],),{,{,},Continue,;,Break,;,},},<EOF>''',101))

    def test_949(self):
        self.assertTrue(TestLexer.test('''Class __a:q{}Class d_P1g8Q{Val $3,$oI,_,$_0,r:Array [Array [String ,0X40],0x8];Destructor (){Continue ;{Break ;} }}''','''Class,__a,:,q,{,},Class,d_P1g8Q,{,Val,$3,,,$oI,,,_,,,$_0,,,r,:,Array,[,Array,[,String,,,0X40,],,,0x8,],;,Destructor,(,),{,Continue,;,{,Break,;,},},},<EOF>''',101))

    def test_950(self):
        self.assertTrue(TestLexer.test('''Class i{Val $Z8__X,$a_7_q,$___3:Array [Array [Array [Array [Array [Array [Boolean ,0xC],0b1010001],8_2],5],0B1010111],48];}''','''Class,i,{,Val,$Z8__X,,,$a_7_q,,,$___3,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0xC,],,,0b1010001,],,,82,],,,5,],,,0B1010111,],,,48,],;,},<EOF>''',101))

    def test_951(self):
        self.assertTrue(TestLexer.test('''Class __:L{}Class __41i{Destructor (){}Val _:Boolean ;$5(w,u1,_,sk,_EQ,_9,_,_3_:Array [String ,0b1]){Continue ;Continue ;} }Class _:_{$4(){} }''','''Class,__,:,L,{,},Class,__41i,{,Destructor,(,),{,},Val,_,:,Boolean,;,$5,(,w,,,u1,,,_,,,sk,,,_EQ,,,_9,,,_,,,_3_,:,Array,[,String,,,0b1,],),{,Continue,;,Continue,;,},},Class,_,:,_,{,$4,(,),{,},},<EOF>''',101))

    def test_952(self):
        self.assertTrue(TestLexer.test('''Class __:_66{Constructor (_:Boolean ;____:Array [Array [Array [Array [Float ,0b1110],0B110011],020],0X55];x3_oD,M:Q0R;_r:Float ){}Destructor (){} }Class _:p{}''','''Class,__,:,_66,{,Constructor,(,_,:,Boolean,;,____,:,Array,[,Array,[,Array,[,Array,[,Float,,,0b1110,],,,0B110011,],,,020,],,,0X55,],;,x3_oD,,,M,:,Q0R,;,_r,:,Float,),{,},Destructor,(,),{,},},Class,_,:,p,{,},<EOF>''',101))

    def test_953(self):
        self.assertTrue(TestLexer.test('''Class bH:_{}Class _:RE5_{_5(){}F7_(){}Val $_QG,$8:Array [Array [Array [String ,01],05],0B1001101];Var $P,_:Boolean ;Val _:Array [Array [Array [Float ,0XF_D_F],6_5],0x5D];Constructor (_:String ){} }Class d:w_7_{Val K:__j;Destructor (){Break ;} }Class m{Val HS:Array [Array [Int ,0B1001101],0b1];Val _m:Float ;}Class _{}Class _{}Class __9:N{}Class Z{}Class DF1:l{}''','''Class,bH,:,_,{,},Class,_,:,RE5_,{,_5,(,),{,},F7_,(,),{,},Val,$_QG,,,$8,:,Array,[,Array,[,Array,[,String,,,01,],,,05,],,,0B1001101,],;,Var,$P,,,_,:,Boolean,;,Val,_,:,Array,[,Array,[,Array,[,Float,,,0XFDF,],,,65,],,,0x5D,],;,Constructor,(,_,:,String,),{,},},Class,d,:,w_7_,{,Val,K,:,__j,;,Destructor,(,),{,Break,;,},},Class,m,{,Val,HS,:,Array,[,Array,[,Int,,,0B1001101,],,,0b1,],;,Val,_m,:,Float,;,},Class,_,{,},Class,_,{,},Class,__9,:,N,{,},Class,Z,{,},Class,DF1,:,l,{,},<EOF>''',101))

    def test_954(self):
        self.assertTrue(TestLexer.test('''Class G_7pA_5{Constructor (){}Destructor (){}Val wg_,$C,_,S,$_p_:Array [Array [Array [String ,0X15],1],0xA];}''','''Class,G_7pA_5,{,Constructor,(,),{,},Destructor,(,),{,},Val,wg_,,,$C,,,_,,,S,,,$_p_,:,Array,[,Array,[,Array,[,String,,,0X15,],,,1,],,,0xA,],;,},<EOF>''',101))

    def test_955(self):
        self.assertTrue(TestLexer.test('''Class _:_{Constructor (){}Val $__,$_57:Float ;Constructor (){ {} }Constructor (c__,O:Float ;_7Pt_,_,C8_,a:Array [Array [Boolean ,0X2A],0b1001];J:Array [Array [Float ,0B1010],0X2A];_:Array [Boolean ,0b1011011];v_,m0:Array [Array [Array [Array [Int ,0x36],0xDF],0x36],0B1_01_0]){} }''','''Class,_,:,_,{,Constructor,(,),{,},Val,$__,,,$_57,:,Float,;,Constructor,(,),{,{,},},Constructor,(,c__,,,O,:,Float,;,_7Pt_,,,_,,,C8_,,,a,:,Array,[,Array,[,Boolean,,,0X2A,],,,0b1001,],;,J,:,Array,[,Array,[,Float,,,0B1010,],,,0X2A,],;,_,:,Array,[,Boolean,,,0b1011011,],;,v_,,,m0,:,Array,[,Array,[,Array,[,Array,[,Int,,,0x36,],,,0xDF,],,,0x36,],,,0B1010,],),{,},},<EOF>''',101))

    def test_956(self):
        self.assertTrue(TestLexer.test('''Class i_3:Y{}Class __:_{Var $_:Array [Float ,075];c__(s4F,_J:l_;M:Array [Array [Array [Array [Array [String ,3_85],075],0b110100],99],0b110100]){} }Class e_l:_{}Class A9{}Class _2{}Class F7_6n:___G{Val R,V:K;}''','''Class,i_3,:,Y,{,},Class,__,:,_,{,Var,$_,:,Array,[,Float,,,075,],;,c__,(,s4F,,,_J,:,l_,;,M,:,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,385,],,,075,],,,0b110100,],,,99,],,,0b110100,],),{,},},Class,e_l,:,_,{,},Class,A9,{,},Class,_2,{,},Class,F7_6n,:,___G,{,Val,R,,,V,:,K,;,},<EOF>''',101))

    def test_957(self):
        self.assertTrue(TestLexer.test('''Class P_{Destructor (){} }Class Dh:j3{Var $V,_2,A,$4,$H:Array [Array [String ,0121],0b111];Var $9:Array [Int ,0X6];}''','''Class,P_,{,Destructor,(,),{,},},Class,Dh,:,j3,{,Var,$V,,,_2,,,A,,,$4,,,$H,:,Array,[,Array,[,String,,,0121,],,,0b111,],;,Var,$9,:,Array,[,Int,,,0X6,],;,},<EOF>''',101))

    def test_958(self):
        self.assertTrue(TestLexer.test('''Class C_{Val __:Array [Array [Array [String ,072],0b1],3];}Class _8:d{Val $10,$4,W:Array [Array [Int ,4_90_8],0b1_0];}''','''Class,C_,{,Val,__,:,Array,[,Array,[,Array,[,String,,,072,],,,0b1,],,,3,],;,},Class,_8,:,d,{,Val,$10,,,$4,,,W,:,Array,[,Array,[,Int,,,4908,],,,0b10,],;,},<EOF>''',101))

    def test_959(self):
        self.assertTrue(TestLexer.test('''Class OD{j_5xv1aW_0(_:Int ;ui83K:Array [Array [Array [Array [Array [Array [Boolean ,0X57],07],0b111_0],041],0x9],0X57];G00:Array [Array [Array [Array [String ,041],071_4],0B1],7];i:Array [Array [Array [Array [Array [Array [Array [Int ,041],0b10100],02_7],0B1010010],041],0B1010010],0X57]){} }''','''Class,OD,{,j_5xv1aW_0,(,_,:,Int,;,ui83K,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0X57,],,,07,],,,0b1110,],,,041,],,,0x9,],,,0X57,],;,G00,:,Array,[,Array,[,Array,[,Array,[,String,,,041,],,,0714,],,,0B1,],,,7,],;,i,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,041,],,,0b10100,],,,027,],,,0B1010010,],,,041,],,,0B1010010,],,,0X57,],),{,},},<EOF>''',101))

    def test_960(self):
        self.assertTrue(TestLexer.test('''Class _iu_:I_{Var $_:Array [Array [Array [Array [Array [Array [Array [Array [Boolean ,0x58],062],05_6],0XB],48],0XB],0XB],0B101101];}''','''Class,_iu_,:,I_,{,Var,$_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0x58,],,,062,],,,056,],,,0XB,],,,48,],,,0XB,],,,0XB,],,,0B101101,],;,},<EOF>''',101))

    def test_961(self):
        self.assertTrue(TestLexer.test('''Class dT{}Class oT{Var u,$H:_25_;y(_m5,o64,E:Array [Boolean ,0X5B];_,_:Array [Array [String ,8_7],0x6];_:Float ){Break ;}Destructor (){Break ;} }''','''Class,dT,{,},Class,oT,{,Var,u,,,$H,:,_25_,;,y,(,_m5,,,o64,,,E,:,Array,[,Boolean,,,0X5B,],;,_,,,_,:,Array,[,Array,[,String,,,87,],,,0x6,],;,_,:,Float,),{,Break,;,},Destructor,(,),{,Break,;,},},<EOF>''',101))

    def test_962(self):
        self.assertTrue(TestLexer.test('''Class Q_{}Class _{}Class o_:__{Constructor (_,p:Float ;_l,h,o,W:Float ;_,F,Z:Array [Boolean ,0B111100];_6:Array [Array [String ,70],07]){Break ;} }''','''Class,Q_,{,},Class,_,{,},Class,o_,:,__,{,Constructor,(,_,,,p,:,Float,;,_l,,,h,,,o,,,W,:,Float,;,_,,,F,,,Z,:,Array,[,Boolean,,,0B111100,],;,_6,:,Array,[,Array,[,String,,,70,],,,07,],),{,Break,;,},},<EOF>''',101))

    def test_963(self):
        self.assertTrue(TestLexer.test('''Class _{}Class C_:_{}Class _{Val __3,G:Float ;Var $_:Boolean ;}Class __:Q{}Class _{_(v:Array [Array [Int ,0B10_01_11],0116]){} }''','''Class,_,{,},Class,C_,:,_,{,},Class,_,{,Val,__3,,,G,:,Float,;,Var,$_,:,Boolean,;,},Class,__,:,Q,{,},Class,_,{,_,(,v,:,Array,[,Array,[,Int,,,0B100111,],,,0116,],),{,},},<EOF>''',101))

    def test_964(self):
        self.assertTrue(TestLexer.test('''Class Ma_4{}Class __hQ__g_7{Constructor (U:Boolean ;A_h,_6,_ys6o:Array [Array [Float ,0X5B],30]){_::$4_();Break ;}Constructor (){} }''','''Class,Ma_4,{,},Class,__hQ__g_7,{,Constructor,(,U,:,Boolean,;,A_h,,,_6,,,_ys6o,:,Array,[,Array,[,Float,,,0X5B,],,,30,],),{,_,::,$4_,(,),;,Break,;,},Constructor,(,),{,},},<EOF>''',101))

    def test_965(self):
        self.assertTrue(TestLexer.test('''Class m9_:b___{}Class _5{Constructor (){}Constructor (__:Boolean ;_5:Float ;N1_192,b:Array [Array [Int ,0B101101],01]){} }Class _6r0{}Class _:___{}Class OiA46:_{}''','''Class,m9_,:,b___,{,},Class,_5,{,Constructor,(,),{,},Constructor,(,__,:,Boolean,;,_5,:,Float,;,N1_192,,,b,:,Array,[,Array,[,Int,,,0B101101,],,,01,],),{,},},Class,_6r0,{,},Class,_,:,___,{,},Class,OiA46,:,_,{,},<EOF>''',101))

    def test_966(self):
        self.assertTrue(TestLexer.test('''Class __:_{Destructor (){} }Class __:_4{}Class i{}Class _{Destructor (){}Destructor (){}Destructor (){}$__8(){}Var L_:f;}''','''Class,__,:,_,{,Destructor,(,),{,},},Class,__,:,_4,{,},Class,i,{,},Class,_,{,Destructor,(,),{,},Destructor,(,),{,},Destructor,(,),{,},$__8,(,),{,},Var,L_,:,f,;,},<EOF>''',101))

    def test_967(self):
        self.assertTrue(TestLexer.test('''Class _C:_{Var $O,$8,G,F,_,$3_G:Array [Boolean ,4_6];Var e,$3__GRO,_:Array [Array [Int ,0XD],0XC];}Class c_:e_{}''','''Class,_C,:,_,{,Var,$O,,,$8,,,G,,,F,,,_,,,$3_G,:,Array,[,Boolean,,,46,],;,Var,e,,,$3__GRO,,,_,:,Array,[,Array,[,Int,,,0XD,],,,0XC,],;,},Class,c_,:,e_,{,},<EOF>''',101))

    def test_968(self):
        self.assertTrue(TestLexer.test('''Class _{Destructor (){ {} }}Class u{$N(){} }Class __2a:_{}Class _z4_:_{_(OX6,H_N_,_1o,b:Array [Array [String ,0b100010],07];W,K:l){} }''','''Class,_,{,Destructor,(,),{,{,},},},Class,u,{,$N,(,),{,},},Class,__2a,:,_,{,},Class,_z4_,:,_,{,_,(,OX6,,,H_N_,,,_1o,,,b,:,Array,[,Array,[,String,,,0b100010,],,,07,],;,W,,,K,:,l,),{,},},<EOF>''',101))

    def test_969(self):
        self.assertTrue(TestLexer.test('''Class _3__774:__5_{Constructor (G,M2,_:K;_9_,_Rv,_:Array [Int ,88];_:Array [Array [Array [Float ,0102],07],0x1A];UE:_C){Break ;} }Class Ug{}''','''Class,_3__774,:,__5_,{,Constructor,(,G,,,M2,,,_,:,K,;,_9_,,,_Rv,,,_,:,Array,[,Int,,,88,],;,_,:,Array,[,Array,[,Array,[,Float,,,0102,],,,07,],,,0x1A,],;,UE,:,_C,),{,Break,;,},},Class,Ug,{,},<EOF>''',101))

    def test_970(self):
        self.assertTrue(TestLexer.test('''Class F5{b_(dNm,l,d:Array [Array [Array [Boolean ,0B1100001],8],0XD];_,j_:Array [Boolean ,0b1]){Return ;Continue ;} }''','''Class,F5,{,b_,(,dNm,,,l,,,d,:,Array,[,Array,[,Array,[,Boolean,,,0B1100001,],,,8,],,,0XD,],;,_,,,j_,:,Array,[,Boolean,,,0b1,],),{,Return,;,Continue,;,},},<EOF>''',101))

    def test_971(self):
        self.assertTrue(TestLexer.test('''Class _:B5xXj_{_(_:L2){}Constructor (I,_n,_:String ;J:Array [Array [Array [Array [Int ,78],4_70_6],070],0x44];_,Z:Boolean ){} }''','''Class,_,:,B5xXj_,{,_,(,_,:,L2,),{,},Constructor,(,I,,,_n,,,_,:,String,;,J,:,Array,[,Array,[,Array,[,Array,[,Int,,,78,],,,4706,],,,070,],,,0x44,],;,_,,,Z,:,Boolean,),{,},},<EOF>''',101))

    def test_972(self):
        self.assertTrue(TestLexer.test('''Class n6_G{_8d_(G,E,V:Array [Array [Array [Float ,6_08],6355_3],0B1];_:String ;p5,_,i,n2,m_,Z_:Array [Boolean ,0B1_1]){} }Class ShRt_:_5{Var $_,$96:_85;Val $O:Array [Array [Float ,39],74];Destructor (){} }''','''Class,n6_G,{,_8d_,(,G,,,E,,,V,:,Array,[,Array,[,Array,[,Float,,,608,],,,63553,],,,0B1,],;,_,:,String,;,p5,,,_,,,i,,,n2,,,m_,,,Z_,:,Array,[,Boolean,,,0B11,],),{,},},Class,ShRt_,:,_5,{,Var,$_,,,$96,:,_85,;,Val,$O,:,Array,[,Array,[,Float,,,39,],,,74,],;,Destructor,(,),{,},},<EOF>''',101))

    def test_973(self):
        self.assertTrue(TestLexer.test('''Class X:J_76{Constructor (V:T){} }Class _{Val $_,__x5:_c6_;I(){}Var $38:Array [String ,0114];Destructor (){Continue ;} }Class _tZ:tG_7_R{}''','''Class,X,:,J_76,{,Constructor,(,V,:,T,),{,},},Class,_,{,Val,$_,,,__x5,:,_c6_,;,I,(,),{,},Var,$38,:,Array,[,String,,,0114,],;,Destructor,(,),{,Continue,;,},},Class,_tZ,:,tG_7_R,{,},<EOF>''',101))

    def test_974(self):
        self.assertTrue(TestLexer.test('''Class J:y{Val $B9_,Z,$0,Pj:Int ;Val _6:Array [Array [Array [Array [Array [String ,0xDD],72],7],0B1000001],0b1];}Class a{}''','''Class,J,:,y,{,Val,$B9_,,,Z,,,$0,,,Pj,:,Int,;,Val,_6,:,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0xDD,],,,72,],,,7,],,,0B1000001,],,,0b1,],;,},Class,a,{,},<EOF>''',101))

    def test_975(self):
        self.assertTrue(TestLexer.test('''Class __398{Constructor (R,Y2,__,P:Array [Array [String ,4_9],15];K5,_CWKlx2:z;Y___hD_A,__,_:Boolean ;f0:Array [Boolean ,33]){} }Class _29u_:Z1{r(_,Y_F0s_:Array [Array [Float ,0X8],33]){} }Class _5__F__Y_2041:_sH{Destructor (){} }''','''Class,__398,{,Constructor,(,R,,,Y2,,,__,,,P,:,Array,[,Array,[,String,,,49,],,,15,],;,K5,,,_CWKlx2,:,z,;,Y___hD_A,,,__,,,_,:,Boolean,;,f0,:,Array,[,Boolean,,,33,],),{,},},Class,_29u_,:,Z1,{,r,(,_,,,Y_F0s_,:,Array,[,Array,[,Float,,,0X8,],,,33,],),{,},},Class,_5__F__Y_2041,:,_sH,{,Destructor,(,),{,},},<EOF>''',101))

    def test_976(self):
        self.assertTrue(TestLexer.test('''Class _G5{}Class n_{}Class Q{B(E85_,Z:Int ;z_:Array [String ,032]){}Val $_,$e:Int ;Val $__7Q,$r,T:Float ;Q(){} }''','''Class,_G5,{,},Class,n_,{,},Class,Q,{,B,(,E85_,,,Z,:,Int,;,z_,:,Array,[,String,,,032,],),{,},Val,$_,,,$e,:,Int,;,Val,$__7Q,,,$r,,,T,:,Float,;,Q,(,),{,},},<EOF>''',101))

    def test_977(self):
        self.assertTrue(TestLexer.test('''Class t{Constructor (){}Destructor (){}$7(t_,_6F_,O7:Array [Array [Array [Int ,0x5A1],04],0B1];_,_:g2_){} }Class G:__r{}Class _{}''','''Class,t,{,Constructor,(,),{,},Destructor,(,),{,},$7,(,t_,,,_6F_,,,O7,:,Array,[,Array,[,Array,[,Int,,,0x5A1,],,,04,],,,0B1,],;,_,,,_,:,g2_,),{,},},Class,G,:,__r,{,},Class,_,{,},<EOF>''',101))

    def test_978(self):
        self.assertTrue(TestLexer.test('''Class _3{Var __:Int ;}Class y{}Class K{}Class Z_{Constructor (_,zQ02_:Array [Array [Array [Array [Boolean ,88],0X7],01],0x7_EB]){} }''','''Class,_3,{,Var,__,:,Int,;,},Class,y,{,},Class,K,{,},Class,Z_,{,Constructor,(,_,,,zQ02_,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,88,],,,0X7,],,,01,],,,0x7EB,],),{,},},<EOF>''',101))

    def test_979(self):
        self.assertTrue(TestLexer.test('''Class uU3{Var Y_,$7,j:Array [Float ,0x8];Var F7:Array [String ,0XF];Constructor (_,_,G5,_,___,_:wmX__6;h_4,_:Y){} }Class _R0_6{}''','''Class,uU3,{,Var,Y_,,,$7,,,j,:,Array,[,Float,,,0x8,],;,Var,F7,:,Array,[,String,,,0XF,],;,Constructor,(,_,,,_,,,G5,,,_,,,___,,,_,:,wmX__6,;,h_4,,,_,:,Y,),{,},},Class,_R0_6,{,},<EOF>''',101))

    def test_980(self):
        self.assertTrue(TestLexer.test('''Class _:_{Constructor (_,_,___:Array [Array [String ,0136],0b1]){}$_z1(la,_W_:Array [Array [String ,0x40],0b1]){} }''','''Class,_,:,_,{,Constructor,(,_,,,_,,,___,:,Array,[,Array,[,String,,,0136,],,,0b1,],),{,},$_z1,(,la,,,_W_,:,Array,[,Array,[,String,,,0x40,],,,0b1,],),{,},},<EOF>''',101))

    def test_981(self):
        self.assertTrue(TestLexer.test('''Class g_{}Class _y{}Class t{Constructor (_,a_Eo:Array [Array [Array [Array [String ,0X1B],0B1_1],0b110101],0b1_0]){} }''','''Class,g_,{,},Class,_y,{,},Class,t,{,Constructor,(,_,,,a_Eo,:,Array,[,Array,[,Array,[,Array,[,String,,,0X1B,],,,0B11,],,,0b110101,],,,0b10,],),{,},},<EOF>''',101))

    def test_982(self):
        self.assertTrue(TestLexer.test('''Class m9_{}Class _7{Val _:String ;Var $9f,Pm_:Array [Array [Boolean ,04],04_7];}Class _{}Class _A_:_{Destructor (){} }Class W:B{}''','''Class,m9_,{,},Class,_7,{,Val,_,:,String,;,Var,$9f,,,Pm_,:,Array,[,Array,[,Boolean,,,04,],,,047,],;,},Class,_,{,},Class,_A_,:,_,{,Destructor,(,),{,},},Class,W,:,B,{,},<EOF>''',101))

    def test_983(self):
        self.assertTrue(TestLexer.test('''Class g_{}Class w_{Destructor (){}Constructor (_,_,_74:Array [Int ,36];n:Array [String ,025];W,X,h08,_,Q,D4:Int ){} }''','''Class,g_,{,},Class,w_,{,Destructor,(,),{,},Constructor,(,_,,,_,,,_74,:,Array,[,Int,,,36,],;,n,:,Array,[,String,,,025,],;,W,,,X,,,h08,,,_,,,Q,,,D4,:,Int,),{,},},<EOF>''',101))

    def test_984(self):
        self.assertTrue(TestLexer.test('''Class b9_G{}Class LD{}Class _E_:j{}Class __:_{Constructor (__22,_0:_;_:Array [Float ,0x12];O:Array [Array [Array [Array [Array [Int ,0b11010_11_110],36],36],0b1],0B10011]){}Val _:Array [Int ,8_3];Destructor (){} }''','''Class,b9_G,{,},Class,LD,{,},Class,_E_,:,j,{,},Class,__,:,_,{,Constructor,(,__22,,,_0,:,_,;,_,:,Array,[,Float,,,0x12,],;,O,:,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0b1101011110,],,,36,],,,36,],,,0b1,],,,0B10011,],),{,},Val,_,:,Array,[,Int,,,83,],;,Destructor,(,),{,},},<EOF>''',101))

    def test_985(self):
        self.assertTrue(TestLexer.test('''Class _a2:_{Val $q:Array [Array [Boolean ,0141],0X24];Destructor (){}Destructor (){} }Class Q:_{}Class s{Destructor (){} }''','''Class,_a2,:,_,{,Val,$q,:,Array,[,Array,[,Boolean,,,0141,],,,0X24,],;,Destructor,(,),{,},Destructor,(,),{,},},Class,Q,:,_,{,},Class,s,{,Destructor,(,),{,},},<EOF>''',101))

    def test_986(self):
        self.assertTrue(TestLexer.test('''Class _3e{$_(N:Int ;f:d;m,r8:Array [Array [Int ,0XE3D_2_32B],01_65_4_2];J:Array [Array [Array [Boolean ,39],0b1],0xA]){Var _w,_,_P_:Array [Array [Array [Array [Array [String ,0133],0x1D],06_6],037_772],0x2];}Val $_k:Array [Boolean ,34];}Class ___:R__{}''','''Class,_3e,{,$_,(,N,:,Int,;,f,:,d,;,m,,,r8,:,Array,[,Array,[,Int,,,0XE3D232B,],,,016542,],;,J,:,Array,[,Array,[,Array,[,Boolean,,,39,],,,0b1,],,,0xA,],),{,Var,_w,,,_,,,_P_,:,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0133,],,,0x1D,],,,066,],,,037772,],,,0x2,],;,},Val,$_k,:,Array,[,Boolean,,,34,],;,},Class,___,:,R__,{,},<EOF>''',101))

    def test_987(self):
        self.assertTrue(TestLexer.test('''Class F{Val $wM26:String ;}Class _{Destructor (){Continue ;} }Class _:U__{Constructor (_,_:Array [Float ,0x23];u:Array [Int ,0114];P:Array [Array [Array [Array [Boolean ,0170],0X37],0114],04]){}Var p_G:Float ;}Class m:Dp{}Class _{}''','''Class,F,{,Val,$wM26,:,String,;,},Class,_,{,Destructor,(,),{,Continue,;,},},Class,_,:,U__,{,Constructor,(,_,,,_,:,Array,[,Float,,,0x23,],;,u,:,Array,[,Int,,,0114,],;,P,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,0170,],,,0X37,],,,0114,],,,04,],),{,},Var,p_G,:,Float,;,},Class,m,:,Dp,{,},Class,_,{,},<EOF>''',101))

    def test_988(self):
        self.assertTrue(TestLexer.test('''Class R_y{}Class pX3:_2{}Class __:_{}Class _{Val Y_,$1,$_,_l:Y_;Var $sFa,C_,$_P:Array [Boolean ,06];_(_3,_8j,aJ:Array [Array [Array [String ,1],020],0b1]){} }Class i{Val _vM_:String ;Var $L:Boolean ;}''','''Class,R_y,{,},Class,pX3,:,_2,{,},Class,__,:,_,{,},Class,_,{,Val,Y_,,,$1,,,$_,,,_l,:,Y_,;,Var,$sFa,,,C_,,,$_P,:,Array,[,Boolean,,,06,],;,_,(,_3,,,_8j,,,aJ,:,Array,[,Array,[,Array,[,String,,,1,],,,020,],,,0b1,],),{,},},Class,i,{,Val,_vM_,:,String,;,Var,$L,:,Boolean,;,},<EOF>''',101))

    def test_989(self):
        self.assertTrue(TestLexer.test('''Class Z:l{Val _9_,$Q_,$7_,__:Array [Array [Array [Array [Int ,012],0X3C],0xE],04_5_1_35_2];Val $___p:Array [Array [Array [Boolean ,012],0x2_7_8],05_4];}''','''Class,Z,:,l,{,Val,_9_,,,$Q_,,,$7_,,,__,:,Array,[,Array,[,Array,[,Array,[,Int,,,012,],,,0X3C,],,,0xE,],,,0451352,],;,Val,$___p,:,Array,[,Array,[,Array,[,Boolean,,,012,],,,0x278,],,,054,],;,},<EOF>''',101))

    def test_990(self):
        self.assertTrue(TestLexer.test('''Class _{}Class _{}Class X:_Z{W(_f:g1){}Var $676,$q:Array [Array [Array [Array [Array [Boolean ,0b111001],26],0b111001],69],69];}Class _:_{}''','''Class,_,{,},Class,_,{,},Class,X,:,_Z,{,W,(,_f,:,g1,),{,},Var,$676,,,$q,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0b111001,],,,26,],,,0b111001,],,,69,],,,69,],;,},Class,_,:,_,{,},<EOF>''',101))

    def test_991(self):
        self.assertTrue(TestLexer.test('''Class _O{Constructor (_t43,Db,_,_,_,_:Int ;_5,h211,_,Rc:_;_,D_:Boolean ;L:Array [Array [String ,47],47];u:Array [Boolean ,0X26]){} }''','''Class,_O,{,Constructor,(,_t43,,,Db,,,_,,,_,,,_,,,_,:,Int,;,_5,,,h211,,,_,,,Rc,:,_,;,_,,,D_,:,Boolean,;,L,:,Array,[,Array,[,String,,,47,],,,47,],;,u,:,Array,[,Boolean,,,0X26,],),{,},},<EOF>''',101))

    def test_992(self):
        self.assertTrue(TestLexer.test('''Class _:_{Constructor (_,_:_){} }Class _t{Val K,e,$6S61,_E_,$r_,$85__,$2:Array [Array [Array [Array [Array [Array [Array [String ,0B11_0_0],052],4_6],052],86],9],0x54];}Class Z{}''','''Class,_,:,_,{,Constructor,(,_,,,_,:,_,),{,},},Class,_t,{,Val,K,,,e,,,$6S61,,,_E_,,,$r_,,,$85__,,,$2,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0B1100,],,,052,],,,46,],,,052,],,,86,],,,9,],,,0x54,],;,},Class,Z,{,},<EOF>''',101))

    def test_993(self):
        self.assertTrue(TestLexer.test('''Class c_{Var _:String ;Constructor (X:String ;_,Z7:Array [Float ,0X16];_:Array [Array [Boolean ,0xC],0B1_0_1_1]){} }Class v1_p9:y{}''','''Class,c_,{,Var,_,:,String,;,Constructor,(,X,:,String,;,_,,,Z7,:,Array,[,Float,,,0X16,],;,_,:,Array,[,Array,[,Boolean,,,0xC,],,,0B1011,],),{,},},Class,v1_p9,:,y,{,},<EOF>''',101))

    def test_994(self):
        self.assertTrue(TestLexer.test('''Class Y{}Class e5_:a{Destructor (){}Var $g8I:Array [Array [Int ,6],06_6];}Class _h:V22{Var _u_,$h,_T,_,_1:Array [Boolean ,0x1A];}''','''Class,Y,{,},Class,e5_,:,a,{,Destructor,(,),{,},Var,$g8I,:,Array,[,Array,[,Int,,,6,],,,066,],;,},Class,_h,:,V22,{,Var,_u_,,,$h,,,_T,,,_,,,_1,:,Array,[,Boolean,,,0x1A,],;,},<EOF>''',101))

    def test_995(self):
        self.assertTrue(TestLexer.test('''Class _A:f_{}Class t:_{Val $J,$8,_,$1,$i:_;_(_,_:Int ){Break ;}Var $_L,$U1_,$E,N_,p_,$w__SM,$78_45:Array [Array [Array [String ,89],0b1_010_0_0],0B1000100];}''','''Class,_A,:,f_,{,},Class,t,:,_,{,Val,$J,,,$8,,,_,,,$1,,,$i,:,_,;,_,(,_,,,_,:,Int,),{,Break,;,},Var,$_L,,,$U1_,,,$E,,,N_,,,p_,,,$w__SM,,,$78_45,:,Array,[,Array,[,Array,[,String,,,89,],,,0b101000,],,,0B1000100,],;,},<EOF>''',101))

    def test_996(self):
        self.assertTrue(TestLexer.test('''Class _:Q{}Class __{d(jQ,I:String ;__f_68o,sk__,MI:tE__;g2:Array [String ,0x85]){Return ;}Destructor (){}Val R:Int ;}''','''Class,_,:,Q,{,},Class,__,{,d,(,jQ,,,I,:,String,;,__f_68o,,,sk__,,,MI,:,tE__,;,g2,:,Array,[,String,,,0x85,],),{,Return,;,},Destructor,(,),{,},Val,R,:,Int,;,},<EOF>''',101))

    def test_997(self):
        self.assertTrue(TestLexer.test('''Class J{Var _,$_1:String ;Nv(_b:String ;_:String ){Break ;}b_m__(D4:Array [Array [Array [Array [Array [Array [Array [Float ,0136],0136],0xAB],0x3E],05],70],0b1000010]){}Constructor (_:Array [String ,0B1001011];__48_4,_Z_:Array [Array [Array [Int ,0b1_1_1_0],0136],0x7];__nh:Array [Int ,0X3]){Continue ;Break ;} }''','''Class,J,{,Var,_,,,$_1,:,String,;,Nv,(,_b,:,String,;,_,:,String,),{,Break,;,},b_m__,(,D4,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0136,],,,0136,],,,0xAB,],,,0x3E,],,,05,],,,70,],,,0b1000010,],),{,},Constructor,(,_,:,Array,[,String,,,0B1001011,],;,__48_4,,,_Z_,:,Array,[,Array,[,Array,[,Int,,,0b1110,],,,0136,],,,0x7,],;,__nh,:,Array,[,Int,,,0X3,],),{,Continue,;,Break,;,},},<EOF>''',101))

    def test_998(self):
        self.assertTrue(TestLexer.test('''Class _:_VT{$c52(){} }Class __:_{}Class dp{Var $29_J_:Boolean ;}Class p{}Class A3_{Constructor (__,_:Array [Boolean ,0X28];_,o,_:_){Break ;} }Class IX:j{}''','''Class,_,:,_VT,{,$c52,(,),{,},},Class,__,:,_,{,},Class,dp,{,Var,$29_J_,:,Boolean,;,},Class,p,{,},Class,A3_,{,Constructor,(,__,,,_,:,Array,[,Boolean,,,0X28,],;,_,,,o,,,_,:,_,),{,Break,;,},},Class,IX,:,j,{,},<EOF>''',101))

    def test_999(self):
        self.assertTrue(TestLexer.test('''Class a:vr{_(___:Array [Boolean ,50]){} }Class _{}Class __x0R{Constructor (){ {}Return ;}Constructor (i,_,bX:Array [Array [Float ,0125],0b1]){}Constructor (){Break ;} }Class V2:_L4{Var __:Array [Int ,014];}''','''Class,a,:,vr,{,_,(,___,:,Array,[,Boolean,,,50,],),{,},},Class,_,{,},Class,__x0R,{,Constructor,(,),{,{,},Return,;,},Constructor,(,i,,,_,,,bX,:,Array,[,Array,[,Float,,,0125,],,,0b1,],),{,},Constructor,(,),{,Break,;,},},Class,V2,:,_L4,{,Var,__,:,Array,[,Int,,,014,],;,},<EOF>''',101))

    def test_1000(self):
        self.assertTrue(TestLexer.test('''Class M9U:_oZm{Constructor (_:s63){} }Class _5:Q{Constructor (Co_9,_4,_7,X:B;_,_:Array [Array [Array [Array [Array [Array [Int ,0X6],0b111010],33],0B1000011],33],052]){}Val $_:_;}Class _{}''','''Class,M9U,:,_oZm,{,Constructor,(,_,:,s63,),{,},},Class,_5,:,Q,{,Constructor,(,Co_9,,,_4,,,_7,,,X,:,B,;,_,,,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0X6,],,,0b111010,],,,33,],,,0B1000011,],,,33,],,,052,],),{,},Val,$_,:,_,;,},Class,_,{,},<EOF>''',101))

    def test_1001(self):
        self.assertTrue(TestLexer.test('''Class _{$v2(__1,_,_:Array [Array [Array [Array [Array [Boolean ,06],6],06],0b1100],0b1100]){}$_p(_,f:u){Aka::$7();}Constructor (){Break ;} }''','''Class,_,{,$v2,(,__1,,,_,,,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,06,],,,6,],,,06,],,,0b1100,],,,0b1100,],),{,},$_p,(,_,,,f,:,u,),{,Aka,::,$7,(,),;,},Constructor,(,),{,Break,;,},},<EOF>''',101))

    def test_1002(self):
        self.assertTrue(TestLexer.test('''Class o_:_{}Class jq{}Class Zx{}Class h:z{}Class _{$4f_h(){}Val $7_51:U;Val $_h__72,e2i,V_,p_,_3_6,_:Array [String ,0xE];Val $7:Array [Array [Int ,54],0xE];}''','''Class,o_,:,_,{,},Class,jq,{,},Class,Zx,{,},Class,h,:,z,{,},Class,_,{,$4f_h,(,),{,},Val,$7_51,:,U,;,Val,$_h__72,,,e2i,,,V_,,,p_,,,_3_6,,,_,:,Array,[,String,,,0xE,],;,Val,$7,:,Array,[,Array,[,Int,,,54,],,,0xE,],;,},<EOF>''',101))

    def test_1003(self):
        self.assertTrue(TestLexer.test('''Class _m:_{}Class _{Constructor (_5,__o:Array [Array [Int ,0X1],031]){}v(){Continue ;} }Class _{$7_(){}$4(_,W:_Ul_;___,_Dy:Array [Float ,0B11100];__N3:Array [String ,0x28];_1w_,EN:Array [Float ,0x28];_Y7,y,_k:_4W4_7_){}Constructor (){Continue ;} }Class I__51aa_h4S:b{}''','''Class,_m,:,_,{,},Class,_,{,Constructor,(,_5,,,__o,:,Array,[,Array,[,Int,,,0X1,],,,031,],),{,},v,(,),{,Continue,;,},},Class,_,{,$7_,(,),{,},$4,(,_,,,W,:,_Ul_,;,___,,,_Dy,:,Array,[,Float,,,0B11100,],;,__N3,:,Array,[,String,,,0x28,],;,_1w_,,,EN,:,Array,[,Float,,,0x28,],;,_Y7,,,y,,,_k,:,_4W4_7_,),{,},Constructor,(,),{,Continue,;,},},Class,I__51aa_h4S,:,b,{,},<EOF>''',101))

    def test_1004(self):
        self.assertTrue(TestLexer.test('''Class _{Destructor (){Continue ;}Constructor (___,_,_,_5:String ;W,v_,_:Array [String ,06];A,_,_2,K_E_5,_4:_8__;__,P:Float ;_,_9_:_g3;m:Float ;_:M){} }''','''Class,_,{,Destructor,(,),{,Continue,;,},Constructor,(,___,,,_,,,_,,,_5,:,String,;,W,,,v_,,,_,:,Array,[,String,,,06,],;,A,,,_,,,_2,,,K_E_5,,,_4,:,_8__,;,__,,,P,:,Float,;,_,,,_9_,:,_g3,;,m,:,Float,;,_,:,M,),{,},},<EOF>''',101))

    def test_1005(self):
        self.assertTrue(TestLexer.test('''Class f{Var ze,kG:c;}Class G{$5(e,WM_9,_F,_,_:d7_Y;b__,_,W:_0;_,_:Boolean ;_RH0_,_:_;_,y:Array [Int ,0b111]){Break ;} }''','''Class,f,{,Var,ze,,,kG,:,c,;,},Class,G,{,$5,(,e,,,WM_9,,,_F,,,_,,,_,:,d7_Y,;,b__,,,_,,,W,:,_0,;,_,,,_,:,Boolean,;,_RH0_,,,_,:,_,;,_,,,y,:,Array,[,Int,,,0b111,],),{,Break,;,},},<EOF>''',101))

    def test_1006(self):
        self.assertTrue(TestLexer.test('''Class b6f{Destructor (){}Destructor (){} }Class _{$_(_,J:Boolean ;_,__r__,__l,C:Float ;x:Array [Array [Array [Array [Array [String ,04_1_0],0x3D],054],0XE],4]){}Val $y_:Boolean ;}Class A5_tF6_:T{Var $r,$21_,$x:Array [Array [Array [Array [Array [Boolean ,054],45],45],040_7_61],1_1_6];}Class e{}Class y{Destructor (){}Val $8,$806,_,R:T;}Class t{}''','''Class,b6f,{,Destructor,(,),{,},Destructor,(,),{,},},Class,_,{,$_,(,_,,,J,:,Boolean,;,_,,,__r__,,,__l,,,C,:,Float,;,x,:,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0410,],,,0x3D,],,,054,],,,0XE,],,,4,],),{,},Val,$y_,:,Boolean,;,},Class,A5_tF6_,:,T,{,Var,$r,,,$21_,,,$x,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,054,],,,45,],,,45,],,,040761,],,,116,],;,},Class,e,{,},Class,y,{,Destructor,(,),{,},Val,$8,,,$806,,,_,,,R,:,T,;,},Class,t,{,},<EOF>''',101))

    def test_1007(self):
        self.assertTrue(TestLexer.test('''Class _f_144_S8{}Class L:Q{Val $8C_2oc10,$_,H:_;$9(){}i(V3ZX_Pq_:Array [Float ,0372]){Break ;}Constructor (b:Array [String ,0b10];pq,_,_:_W;___:Array [Array [Array [String ,0b101],0x34],0B11];W,__,K,_,D6:Array [Int ,0b1_11]){} }''','''Class,_f_144_S8,{,},Class,L,:,Q,{,Val,$8C_2oc10,,,$_,,,H,:,_,;,$9,(,),{,},i,(,V3ZX_Pq_,:,Array,[,Float,,,0372,],),{,Break,;,},Constructor,(,b,:,Array,[,String,,,0b10,],;,pq,,,_,,,_,:,_W,;,___,:,Array,[,Array,[,Array,[,String,,,0b101,],,,0x34,],,,0B11,],;,W,,,__,,,K,,,_,,,D6,:,Array,[,Int,,,0b111,],),{,},},<EOF>''',101))

    def test_1008(self):
        self.assertTrue(TestLexer.test('''Class _{Var $_:Array [Array [Array [Array [Array [Int ,32],056],0B11],015],0X1C_4_5];Var $_:Array [Array [Array [Array [String ,015],7],0B11],06];}''','''Class,_,{,Var,$_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,32,],,,056,],,,0B11,],,,015,],,,0X1C45,],;,Var,$_,:,Array,[,Array,[,Array,[,Array,[,String,,,015,],,,7,],,,0B11,],,,06,],;,},<EOF>''',101))

    def test_1009(self):
        self.assertTrue(TestLexer.test('''Class v{$4(){} }Class z:_{}Class Gt_:__{}Class _:___{B08___(Ob,__,_,__,Rr:Boolean ){T::$JY().D().a();Continue ;}Var C6AV,B:String ;}Class __gebD:p{}''','''Class,v,{,$4,(,),{,},},Class,z,:,_,{,},Class,Gt_,:,__,{,},Class,_,:,___,{,B08___,(,Ob,,,__,,,_,,,__,,,Rr,:,Boolean,),{,T,::,$JY,(,),.,D,(,),.,a,(,),;,Continue,;,},Var,C6AV,,,B,:,String,;,},Class,__gebD,:,p,{,},<EOF>''',101))

    def test_1010(self):
        self.assertTrue(TestLexer.test('''Class ZJ:h4{}Class MI:_{Var $rX,_I,c43,$_,_,$4,__T,v3A,_:Array [Array [Array [Int ,0b10010],0B101001],0b1];th(__:Boolean ;_nv,X,_0_6,_0:g_){} }''','''Class,ZJ,:,h4,{,},Class,MI,:,_,{,Var,$rX,,,_I,,,c43,,,$_,,,_,,,$4,,,__T,,,v3A,,,_,:,Array,[,Array,[,Array,[,Int,,,0b10010,],,,0B101001,],,,0b1,],;,th,(,__,:,Boolean,;,_nv,,,X,,,_0_6,,,_0,:,g_,),{,},},<EOF>''',101))

    def test_1011(self):
        self.assertTrue(TestLexer.test('''Class _{R(W,rI,We:Array [Array [Array [Array [Boolean ,0XA],0104],0X44],9_4]){Continue ;Continue ;}Var _97:Array [Array [Float ,4],0X6];}''','''Class,_,{,R,(,W,,,rI,,,We,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,0XA,],,,0104,],,,0X44,],,,94,],),{,Continue,;,Continue,;,},Var,_97,:,Array,[,Array,[,Float,,,4,],,,0X6,],;,},<EOF>''',101))

    def test_1012(self):
        self.assertTrue(TestLexer.test('''Class f{}Class __:_{Destructor (){} }Class __A2__v_:_sj_Z{Constructor (VGn,_,_:Array [Array [Boolean ,07],37]){} }''','''Class,f,{,},Class,__,:,_,{,Destructor,(,),{,},},Class,__A2__v_,:,_sj_Z,{,Constructor,(,VGn,,,_,,,_,:,Array,[,Array,[,Boolean,,,07,],,,37,],),{,},},<EOF>''',101))

    def test_1013(self):
        self.assertTrue(TestLexer.test('''Class _{}Class S{Destructor (){}Destructor (){}Val $__:Array [Array [Boolean ,06],0B110111];}Class _{Destructor (){}Var $_:Array [Array [Array [String ,06],4],0X1C];}Class c:F{Destructor (){}$8(){Return ;} }''','''Class,_,{,},Class,S,{,Destructor,(,),{,},Destructor,(,),{,},Val,$__,:,Array,[,Array,[,Boolean,,,06,],,,0B110111,],;,},Class,_,{,Destructor,(,),{,},Var,$_,:,Array,[,Array,[,Array,[,String,,,06,],,,4,],,,0X1C,],;,},Class,c,:,F,{,Destructor,(,),{,},$8,(,),{,Return,;,},},<EOF>''',101))

    def test_1014(self):
        self.assertTrue(TestLexer.test('''Class Q:_1{Constructor (_XNAgAg,__w:Array [Array [Array [Boolean ,065],0B1_1_0_1_0],065]){B::$1_();}Val _,_9,_,h_S:Boolean ;}Class _{}Class ___4:ya{}Class _j__p:j{Var Tu:String ;Destructor (){}Destructor (){} }''','''Class,Q,:,_1,{,Constructor,(,_XNAgAg,,,__w,:,Array,[,Array,[,Array,[,Boolean,,,065,],,,0B11010,],,,065,],),{,B,::,$1_,(,),;,},Val,_,,,_9,,,_,,,h_S,:,Boolean,;,},Class,_,{,},Class,___4,:,ya,{,},Class,_j__p,:,j,{,Var,Tu,:,String,;,Destructor,(,),{,},Destructor,(,),{,},},<EOF>''',101))

    def test_1015(self):
        self.assertTrue(TestLexer.test('''Class lO{}Class h:_7{Destructor (){Continue ;}Constructor (____pE:Array [Int ,8]){} }Class d_781{Var $5,$9_:Int ;}Class _q__{Var L,_,kXf0_,Y1:_f;}''','''Class,lO,{,},Class,h,:,_7,{,Destructor,(,),{,Continue,;,},Constructor,(,____pE,:,Array,[,Int,,,8,],),{,},},Class,d_781,{,Var,$5,,,$9_,:,Int,;,},Class,_q__,{,Var,L,,,_,,,kXf0_,,,Y1,:,_f,;,},<EOF>''',101))

    def test_1016(self):
        self.assertTrue(TestLexer.test('''Class G{Destructor (){Break ;} }Class _{}Class RuEe:_{}Class _:_{Constructor (_,_,___4__i2,_,LI_,_:Array [Array [Float ,0B11_0],5_79]){Continue ;} }Class m_{}''','''Class,G,{,Destructor,(,),{,Break,;,},},Class,_,{,},Class,RuEe,:,_,{,},Class,_,:,_,{,Constructor,(,_,,,_,,,___4__i2,,,_,,,LI_,,,_,:,Array,[,Array,[,Float,,,0B110,],,,579,],),{,Continue,;,},},Class,m_,{,},<EOF>''',101))

    def test_1017(self):
        self.assertTrue(TestLexer.test('''Class TY{$_w426T__(){Var W,_4,_D74,m6,_0,_,__7:Array [Array [Int ,0XB4],0x33];} }Class O:wGS{Constructor (){} }''','''Class,TY,{,$_w426T__,(,),{,Var,W,,,_4,,,_D74,,,m6,,,_0,,,_,,,__7,:,Array,[,Array,[,Int,,,0XB4,],,,0x33,],;,},},Class,O,:,wGS,{,Constructor,(,),{,},},<EOF>''',101))

    def test_1018(self):
        self.assertTrue(TestLexer.test('''Class _:_{Constructor (_,Z,_8NZ,d2:Array [Array [Array [Int ,0XD1],0b1100000],0B110110];_h,_,q:Array [Array [String ,69],030_5];T:_;_,_,_7,_,_:L0_F;m_,g_x01:Array [Array [String ,0x1B],0B11]){}_(_:Array [Array [Array [Array [Array [String ,69],0X2],0x1B],69],0136];_UW__:_){} }''','''Class,_,:,_,{,Constructor,(,_,,,Z,,,_8NZ,,,d2,:,Array,[,Array,[,Array,[,Int,,,0XD1,],,,0b1100000,],,,0B110110,],;,_h,,,_,,,q,:,Array,[,Array,[,String,,,69,],,,0305,],;,T,:,_,;,_,,,_,,,_7,,,_,,,_,:,L0_F,;,m_,,,g_x01,:,Array,[,Array,[,String,,,0x1B,],,,0B11,],),{,},_,(,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,69,],,,0X2,],,,0x1B,],,,69,],,,0136,],;,_UW__,:,_,),{,},},<EOF>''',101))

    def test_1019(self):
        self.assertTrue(TestLexer.test('''Class j:Cz{Val $7_1,$Oo__4,$77,$_,$2,h_9W:Array [Array [Array [Boolean ,70],05],35];Var D,$8c_80A:Array [Array [Array [Array [Int ,0b11111],0XC_8_5],0B1],076_4];}Class a:w{}''','''Class,j,:,Cz,{,Val,$7_1,,,$Oo__4,,,$77,,,$_,,,$2,,,h_9W,:,Array,[,Array,[,Array,[,Boolean,,,70,],,,05,],,,35,],;,Var,D,,,$8c_80A,:,Array,[,Array,[,Array,[,Array,[,Int,,,0b11111,],,,0XC85,],,,0B1,],,,0764,],;,},Class,a,:,w,{,},<EOF>''',101))

    def test_1020(self):
        self.assertTrue(TestLexer.test('''Class B4{}Class ___{R8(b71:String ;_:Array [Array [Float ,0XD],0b1];_,_:Float ;_5,p__x,dq_:b;N2M,j_:Array [Array [Float ,14],0B1011011];_:Boolean ;_,_a:Array [Float ,0b100000]){} }''','''Class,B4,{,},Class,___,{,R8,(,b71,:,String,;,_,:,Array,[,Array,[,Float,,,0XD,],,,0b1,],;,_,,,_,:,Float,;,_5,,,p__x,,,dq_,:,b,;,N2M,,,j_,:,Array,[,Array,[,Float,,,14,],,,0B1011011,],;,_,:,Boolean,;,_,,,_a,:,Array,[,Float,,,0b100000,],),{,},},<EOF>''',101))

    def test_1021(self):
        self.assertTrue(TestLexer.test('''Class I:__0{}Class W__z:u_{Val __,$_,_:t___QR2;Var $M,$_,$Z,_,_0_,__:A4M_;$M(){} }Class _4:_4{Constructor (Qq__t_5,_,_:Array [Float ,0B11101];s4:_;E:Array [Boolean ,02]){} }''','''Class,I,:,__0,{,},Class,W__z,:,u_,{,Val,__,,,$_,,,_,:,t___QR2,;,Var,$M,,,$_,,,$Z,,,_,,,_0_,,,__,:,A4M_,;,$M,(,),{,},},Class,_4,:,_4,{,Constructor,(,Qq__t_5,,,_,,,_,:,Array,[,Float,,,0B11101,],;,s4,:,_,;,E,:,Array,[,Boolean,,,02,],),{,},},<EOF>''',101))

    def test_1022(self):
        self.assertTrue(TestLexer.test('''Class ____{$_(x:_;J___1TP,o6_,_,T_,_5:L2;h__:String ){}Val $d0,$5_,_:Array [Array [Int ,063],7_14_7];}Class _s_{}Class D_:_{}''','''Class,____,{,$_,(,x,:,_,;,J___1TP,,,o6_,,,_,,,T_,,,_5,:,L2,;,h__,:,String,),{,},Val,$d0,,,$5_,,,_,:,Array,[,Array,[,Int,,,063,],,,7147,],;,},Class,_s_,{,},Class,D_,:,_,{,},<EOF>''',101))

    def test_1023(self):
        self.assertTrue(TestLexer.test('''Class _:L{Destructor (){} }Class __g8{}Class U12_0{}Class _:A{Var _:Array [Array [Array [Boolean ,0b111010],0b111010],01];}Class Ns6_43:p_6Dh{}''','''Class,_,:,L,{,Destructor,(,),{,},},Class,__g8,{,},Class,U12_0,{,},Class,_,:,A,{,Var,_,:,Array,[,Array,[,Array,[,Boolean,,,0b111010,],,,0b111010,],,,01,],;,},Class,Ns6_43,:,p_6Dh,{,},<EOF>''',101))

    def test_1024(self):
        self.assertTrue(TestLexer.test('''Class _76_i{R(n_e02,lA38:Array [Float ,03_5_01];_V,e0,__,y,_b_t6:String ){} }Class y{Destructor (){}Constructor (_:String ){} }''','''Class,_76_i,{,R,(,n_e02,,,lA38,:,Array,[,Float,,,03501,],;,_V,,,e0,,,__,,,y,,,_b_t6,:,String,),{,},},Class,y,{,Destructor,(,),{,},Constructor,(,_,:,String,),{,},},<EOF>''',101))

    def test_1025(self):
        self.assertTrue(TestLexer.test('''Class Z{Constructor (_,HN_0,N__0:n_;_t_78,NJ__:__;n:q1;_9,ni:Array [Array [Array [String ,0xE],0B110000],16];w,S_,_0:String ){} }''','''Class,Z,{,Constructor,(,_,,,HN_0,,,N__0,:,n_,;,_t_78,,,NJ__,:,__,;,n,:,q1,;,_9,,,ni,:,Array,[,Array,[,Array,[,String,,,0xE,],,,0B110000,],,,16,],;,w,,,S_,,,_0,:,String,),{,},},<EOF>''',101))

    def test_1026(self):
        self.assertTrue(TestLexer.test('''Class q{$2O3(_g0,q3_,_S:Int ;_,C,__:Int ;B_:Array [Array [Array [Array [Array [Int ,7],0x25],64],64],0b1];_:r5;x_:n){} }''','''Class,q,{,$2O3,(,_g0,,,q3_,,,_S,:,Int,;,_,,,C,,,__,:,Int,;,B_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,7,],,,0x25,],,,64,],,,64,],,,0b1,],;,_,:,r5,;,x_,:,n,),{,},},<EOF>''',101))

    def test_1027(self):
        self.assertTrue(TestLexer.test('''Class _{}Class _:__c3{$_96(__:Array [Int ,5]){}$f(_4:Array [Array [Array [Int ,34],34],0b100110]){} }Class Nou{}Class xL{}''','''Class,_,{,},Class,_,:,__c3,{,$_96,(,__,:,Array,[,Int,,,5,],),{,},$f,(,_4,:,Array,[,Array,[,Array,[,Int,,,34,],,,34,],,,0b100110,],),{,},},Class,Nou,{,},Class,xL,{,},<EOF>''',101))

    def test_1028(self):
        self.assertTrue(TestLexer.test('''Class __2fe3{Var $__K_,$0_60,$4f:Array [Array [Array [Array [Array [Array [String ,0B1],0XBC],50],06],0b10],0B101110];a(){ {}U2::$12();Continue ;} }''','''Class,__2fe3,{,Var,$__K_,,,$0_60,,,$4f,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0B1,],,,0XBC,],,,50,],,,06,],,,0b10,],,,0B101110,],;,a,(,),{,{,},U2,::,$12,(,),;,Continue,;,},},<EOF>''',101))

    def test_1029(self):
        self.assertTrue(TestLexer.test('''Class _3{}Class B:k{Destructor (){Return ;{} }Var b:Array [Array [Int ,0B1_1_0],0X4];}Class Z{}Class o0_:_q{Var $X,$8,$_7:__;}Class _541{Destructor (){} }''','''Class,_3,{,},Class,B,:,k,{,Destructor,(,),{,Return,;,{,},},Var,b,:,Array,[,Array,[,Int,,,0B110,],,,0X4,],;,},Class,Z,{,},Class,o0_,:,_q,{,Var,$X,,,$8,,,$_7,:,__,;,},Class,_541,{,Destructor,(,),{,},},<EOF>''',101))

    def test_1030(self):
        self.assertTrue(TestLexer.test('''Class a_:M0_{Val $C,$C,df:_p;$__bM_r(m3U:_I_8;_,i:Array [Array [Boolean ,026],0b1];M5,y,g,_,I_:_;t018:_8k){} }Class _:U{}''','''Class,a_,:,M0_,{,Val,$C,,,$C,,,df,:,_p,;,$__bM_r,(,m3U,:,_I_8,;,_,,,i,:,Array,[,Array,[,Boolean,,,026,],,,0b1,],;,M5,,,y,,,g,,,_,,,I_,:,_,;,t018,:,_8k,),{,},},Class,_,:,U,{,},<EOF>''',101))

    def test_1031(self):
        self.assertTrue(TestLexer.test('''Class _{Constructor (p:U){}$__(W_,_8,c_s_3,y,_V6,_z,j,_:Array [String ,36];_:J;j___,k:_b__;r_7,d:_;J:U){}Val A,__9,$L,$__:n26;}Class _:Z_i8_{}''','''Class,_,{,Constructor,(,p,:,U,),{,},$__,(,W_,,,_8,,,c_s_3,,,y,,,_V6,,,_z,,,j,,,_,:,Array,[,String,,,36,],;,_,:,J,;,j___,,,k,:,_b__,;,r_7,,,d,:,_,;,J,:,U,),{,},Val,A,,,__9,,,$L,,,$__,:,n26,;,},Class,_,:,Z_i8_,{,},<EOF>''',101))

    def test_1032(self):
        self.assertTrue(TestLexer.test('''Class _{Val $_,$_9Qg:Boolean ;Var $9,B3A3,__D:Array [Array [String ,7],0116];}Class ___F7{Destructor (){Break ;} }Class _{}''','''Class,_,{,Val,$_,,,$_9Qg,:,Boolean,;,Var,$9,,,B3A3,,,__D,:,Array,[,Array,[,String,,,7,],,,0116,],;,},Class,___F7,{,Destructor,(,),{,Break,;,},},Class,_,{,},<EOF>''',101))

    def test_1033(self):
        self.assertTrue(TestLexer.test('''Class Z_{}Class R{Destructor (){}$0(dE:Float ;p:Array [Boolean ,044];S6,____1:Float ;F,f1,e:__){}Constructor (){}Constructor (_,___,x6:String ){}Destructor (){} }''','''Class,Z_,{,},Class,R,{,Destructor,(,),{,},$0,(,dE,:,Float,;,p,:,Array,[,Boolean,,,044,],;,S6,,,____1,:,Float,;,F,,,f1,,,e,:,__,),{,},Constructor,(,),{,},Constructor,(,_,,,___,,,x6,:,String,),{,},Destructor,(,),{,},},<EOF>''',101))

    def test_1034(self):
        self.assertTrue(TestLexer.test('''Class R_61:_28{}Class S:Esq{$3cjR(__,_C,z658_304:Array [Array [Boolean ,02],37];n,_6___83:Q;X,_,e:Boolean ;_9,D,W:Array [Int ,02]){}Destructor (){Val _,_1,lL_GY_:Float ;} }Class _:a{}''','''Class,R_61,:,_28,{,},Class,S,:,Esq,{,$3cjR,(,__,,,_C,,,z658_304,:,Array,[,Array,[,Boolean,,,02,],,,37,],;,n,,,_6___83,:,Q,;,X,,,_,,,e,:,Boolean,;,_9,,,D,,,W,:,Array,[,Int,,,02,],),{,},Destructor,(,),{,Val,_,,,_1,,,lL_GY_,:,Float,;,},},Class,_,:,a,{,},<EOF>''',101))

    def test_1035(self):
        self.assertTrue(TestLexer.test('''Class _:v{}Class _:T{}Class b:er{Constructor (W:Array [Array [Array [String ,54],0x4A],0xC_2];q:Array [Array [Int ,0X2A_3],2];D:__){} }''','''Class,_,:,v,{,},Class,_,:,T,{,},Class,b,:,er,{,Constructor,(,W,:,Array,[,Array,[,Array,[,String,,,54,],,,0x4A,],,,0xC2,],;,q,:,Array,[,Array,[,Int,,,0X2A3,],,,2,],;,D,:,__,),{,},},<EOF>''',101))

    def test_1036(self):
        self.assertTrue(TestLexer.test('''Class B_:V_{}Class __d_{$_(G,kS_:Array [Array [Array [Array [Array [Array [String ,0B1],0b1_0],0b1_0],0B1000],5_3],06_2_4]){} }Class s_8{}Class Y{}''','''Class,B_,:,V_,{,},Class,__d_,{,$_,(,G,,,kS_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0B1,],,,0b10,],,,0b10,],,,0B1000,],,,53,],,,0624,],),{,},},Class,s_8,{,},Class,Y,{,},<EOF>''',101))

    def test_1037(self):
        self.assertTrue(TestLexer.test('''Class w0{$eGp_(d:Array [Array [Array [Array [Boolean ,28],0X23],28],0X23];Q,_3_N_,i_ZN_D_,nm,T__t,n:Boolean ){Break ;} }Class _:_{Destructor (){Break ;}Destructor (){Continue ;} }''','''Class,w0,{,$eGp_,(,d,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,28,],,,0X23,],,,28,],,,0X23,],;,Q,,,_3_N_,,,i_ZN_D_,,,nm,,,T__t,,,n,:,Boolean,),{,Break,;,},},Class,_,:,_,{,Destructor,(,),{,Break,;,},Destructor,(,),{,Continue,;,},},<EOF>''',101))

    def test_1038(self):
        self.assertTrue(TestLexer.test('''Class _:N9{Destructor (){Return ;}Var _,_22,F:Array [Array [Array [Float ,0B1010],0b10],04];}Class L:_{Constructor (){} }''','''Class,_,:,N9,{,Destructor,(,),{,Return,;,},Var,_,,,_22,,,F,:,Array,[,Array,[,Array,[,Float,,,0B1010,],,,0b10,],,,04,],;,},Class,L,:,_,{,Constructor,(,),{,},},<EOF>''',101))

    def test_1039(self):
        self.assertTrue(TestLexer.test('''Class _Kj:_{Var $0,$_,_c__:_4_;Val _:Array [Int ,0143];}Class t_{}Class _1:Z{Var $W,$__57_,_G1:Array [Array [Boolean ,05],0B101101];Val $__X,M,$___,Z:String ;}''','''Class,_Kj,:,_,{,Var,$0,,,$_,,,_c__,:,_4_,;,Val,_,:,Array,[,Int,,,0143,],;,},Class,t_,{,},Class,_1,:,Z,{,Var,$W,,,$__57_,,,_G1,:,Array,[,Array,[,Boolean,,,05,],,,0B101101,],;,Val,$__X,,,M,,,$___,,,Z,:,String,;,},<EOF>''',101))

    def test_1040(self):
        self.assertTrue(TestLexer.test('''Class O{}Class _:_M_1Ww{Constructor (_,y,t:Float ;C,Y:Array [Array [Array [String ,6],0103],0B110100];_:Float ){Break ;}Val $J_:_;}''','''Class,O,{,},Class,_,:,_M_1Ww,{,Constructor,(,_,,,y,,,t,:,Float,;,C,,,Y,:,Array,[,Array,[,Array,[,String,,,6,],,,0103,],,,0B110100,],;,_,:,Float,),{,Break,;,},Val,$J_,:,_,;,},<EOF>''',101))

    def test_1041(self):
        self.assertTrue(TestLexer.test('''Class WKb0_0:_{Var $z,__DA,$E_4,$_:i;Constructor (B3,_s__p,l,_g5_km_,N:Float ;I:D__;_9:Array [Array [Array [Array [Array [Array [Array [Array [Array [Array [String ,02_4_4],4_2_06],023],03],0B100],0X28],057],0x6_41_9],0b1_1],15]){} }''','''Class,WKb0_0,:,_,{,Var,$z,,,__DA,,,$E_4,,,$_,:,i,;,Constructor,(,B3,,,_s__p,,,l,,,_g5_km_,,,N,:,Float,;,I,:,D__,;,_9,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0244,],,,4206,],,,023,],,,03,],,,0B100,],,,0X28,],,,057,],,,0x6419,],,,0b11,],,,15,],),{,},},<EOF>''',101))

    def test_1042(self):
        self.assertTrue(TestLexer.test('''Class _{$1(d:Array [Array [Array [Array [Array [Array [Int ,0XAFB],0b1001100],022],0X3],067],0B100]){Break ;} }Class _:_{}''','''Class,_,{,$1,(,d,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0XAFB,],,,0b1001100,],,,022,],,,0X3,],,,067,],,,0B100,],),{,Break,;,},},Class,_,:,_,{,},<EOF>''',101))

    def test_1043(self):
        self.assertTrue(TestLexer.test('''Class X{Val $_902KI,$m:Array [Int ,33];Var $8_2,_:o;Destructor (){}Constructor (__8_:wj_s_S__9;_w,_p:Array [Array [Int ,07_3],017];g9___4:q__d;__:Boolean ;_,b:Int ;S:Array [Array [Array [Int ,017],02_27_1],0b1011011];_:Array [Boolean ,02]){} }''','''Class,X,{,Val,$_902KI,,,$m,:,Array,[,Int,,,33,],;,Var,$8_2,,,_,:,o,;,Destructor,(,),{,},Constructor,(,__8_,:,wj_s_S__9,;,_w,,,_p,:,Array,[,Array,[,Int,,,073,],,,017,],;,g9___4,:,q__d,;,__,:,Boolean,;,_,,,b,:,Int,;,S,:,Array,[,Array,[,Array,[,Int,,,017,],,,02271,],,,0b1011011,],;,_,:,Array,[,Boolean,,,02,],),{,},},<EOF>''',101))

    def test_1044(self):
        self.assertTrue(TestLexer.test('''Class y:_T{}Class U{Destructor (){} }Class __{}Class _{Constructor (n,F,xm_,_,Ca:Array [Array [String ,60_7],0x1]){Continue ;Break ;} }''','''Class,y,:,_T,{,},Class,U,{,Destructor,(,),{,},},Class,__,{,},Class,_,{,Constructor,(,n,,,F,,,xm_,,,_,,,Ca,:,Array,[,Array,[,String,,,607,],,,0x1,],),{,Continue,;,Break,;,},},<EOF>''',101))

    def test_1045(self):
        self.assertTrue(TestLexer.test('''Class __5{Var _,$7:Boolean ;Var _:Array [Array [Array [Array [Array [Array [Int ,0B11],0X58_D],0b1111],0B1],0B1],0140];}Class d_2{}Class O{}''','''Class,__5,{,Var,_,,,$7,:,Boolean,;,Var,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0B11,],,,0X58D,],,,0b1111,],,,0B1,],,,0B1,],,,0140,],;,},Class,d_2,{,},Class,O,{,},<EOF>''',101))

    def test_1046(self):
        self.assertTrue(TestLexer.test('''Class __D{Constructor (Nku,_,r_,z,_,_Nu:Array [Array [Array [Array [Int ,98],98],0X688_03_35],0144]){Return ;}Destructor (){}Val _,_,$SG:H;F(__,_:Float ){}Destructor (){Continue ;} }Class _4M7__2:_{$1_(_:String ){} }''','''Class,__D,{,Constructor,(,Nku,,,_,,,r_,,,z,,,_,,,_Nu,:,Array,[,Array,[,Array,[,Array,[,Int,,,98,],,,98,],,,0X6880335,],,,0144,],),{,Return,;,},Destructor,(,),{,},Val,_,,,_,,,$SG,:,H,;,F,(,__,,,_,:,Float,),{,},Destructor,(,),{,Continue,;,},},Class,_4M7__2,:,_,{,$1_,(,_,:,String,),{,},},<EOF>''',101))

    def test_1047(self):
        self.assertTrue(TestLexer.test('''Class Rw{}Class xOx{Destructor (){Break ;}Constructor (Oo:j0){ {{Break ;}Break ;} }Constructor (e76_,C:Array [Int ,0xB];__6:Fb___){} }''','''Class,Rw,{,},Class,xOx,{,Destructor,(,),{,Break,;,},Constructor,(,Oo,:,j0,),{,{,{,Break,;,},Break,;,},},Constructor,(,e76_,,,C,:,Array,[,Int,,,0xB,],;,__6,:,Fb___,),{,},},<EOF>''',101))

    def test_1048(self):
        self.assertTrue(TestLexer.test('''Class _{Val F,$D:Float ;Destructor (){} }Class _:_9__1{}Class s5_:__X2{}Class __{$5(F,_X:R){Continue ;}Destructor (){Return ;} }''','''Class,_,{,Val,F,,,$D,:,Float,;,Destructor,(,),{,},},Class,_,:,_9__1,{,},Class,s5_,:,__X2,{,},Class,__,{,$5,(,F,,,_X,:,R,),{,Continue,;,},Destructor,(,),{,Return,;,},},<EOF>''',101))

    def test_1049(self):
        self.assertTrue(TestLexer.test('''Class _{$N_(_W:Array [Array [Array [Array [String ,9],015],0b101110],032];b_3:Boolean ;T,B_20G6:Float ){Continue ;Continue ;} }Class W_1_:FS_52oG{}''','''Class,_,{,$N_,(,_W,:,Array,[,Array,[,Array,[,Array,[,String,,,9,],,,015,],,,0b101110,],,,032,],;,b_3,:,Boolean,;,T,,,B_20G6,:,Float,),{,Continue,;,Continue,;,},},Class,W_1_,:,FS_52oG,{,},<EOF>''',101))

    def test_1050(self):
        self.assertTrue(TestLexer.test('''Class _6:_0{}Class _8_{}Class O:_w7{Var $A,$6,$_s,$7,xRc:Array [Array [Array [String ,0b111011],0x8_E],014];}Class _TUq{Destructor (){} }''','''Class,_6,:,_0,{,},Class,_8_,{,},Class,O,:,_w7,{,Var,$A,,,$6,,,$_s,,,$7,,,xRc,:,Array,[,Array,[,Array,[,String,,,0b111011,],,,0x8E,],,,014,],;,},Class,_TUq,{,Destructor,(,),{,},},<EOF>''',101))

    def test_1051(self):
        self.assertTrue(TestLexer.test('''Class n__X_p{}Class _:_{_(){} }Class _i____:_{}Class _{Constructor (_,_,_,_3,_,_4_:d;t,o:Float ;_,TS4,_:_2_){ {Break ;{} }Break ;} }Class _{}Class _:k{}''','''Class,n__X_p,{,},Class,_,:,_,{,_,(,),{,},},Class,_i____,:,_,{,},Class,_,{,Constructor,(,_,,,_,,,_,,,_3,,,_,,,_4_,:,d,;,t,,,o,:,Float,;,_,,,TS4,,,_,:,_2_,),{,{,Break,;,{,},},Break,;,},},Class,_,{,},Class,_,:,k,{,},<EOF>''',101))

    def test_1052(self):
        self.assertTrue(TestLexer.test('''Class r__HE:_j_6{Var _:Array [Array [String ,037],22];Constructor (_1MCX:_;_:Array [Array [Array [Int ,7],0B1011011],0x4B];_D,x:Int ;_,o:Boolean ;Q9:String ;_,x6:_6){Val s:Boolean ;Return ;Break ;} }''','''Class,r__HE,:,_j_6,{,Var,_,:,Array,[,Array,[,String,,,037,],,,22,],;,Constructor,(,_1MCX,:,_,;,_,:,Array,[,Array,[,Array,[,Int,,,7,],,,0B1011011,],,,0x4B,],;,_D,,,x,:,Int,;,_,,,o,:,Boolean,;,Q9,:,String,;,_,,,x6,:,_6,),{,Val,s,:,Boolean,;,Return,;,Break,;,},},<EOF>''',101))

    def test_1053(self):
        self.assertTrue(TestLexer.test('''Class _{Constructor (){} }Class _n:Nu{_Vp(_8_H3_V:Array [Boolean ,0XCF9_2_D8];_1_:Array [String ,0B101111];_:Array [Boolean ,0B101111];N,_8,_w_:v4;___:Array [Int ,0b1]){} }''','''Class,_,{,Constructor,(,),{,},},Class,_n,:,Nu,{,_Vp,(,_8_H3_V,:,Array,[,Boolean,,,0XCF92D8,],;,_1_,:,Array,[,String,,,0B101111,],;,_,:,Array,[,Boolean,,,0B101111,],;,N,,,_8,,,_w_,:,v4,;,___,:,Array,[,Int,,,0b1,],),{,},},<EOF>''',101))

    def test_1054(self):
        self.assertTrue(TestLexer.test('''Class _X{zQ_(){}Constructor (){} }Class _:_{Constructor (_50H:Array [String ,3];_n2,L:v4n){}Constructor (){} }''','''Class,_X,{,zQ_,(,),{,},Constructor,(,),{,},},Class,_,:,_,{,Constructor,(,_50H,:,Array,[,String,,,3,],;,_n2,,,L,:,v4n,),{,},Constructor,(,),{,},},<EOF>''',101))

    def test_1055(self):
        self.assertTrue(TestLexer.test('''Class _H:_01e_n{$e(){}Constructor (o0_e_u:Array [Array [Array [Array [Boolean ,0XBD2],0b1011],12],0b10_1];U_O,q8:Boolean ;_3_,__,_,XJ,z:String ){} }''','''Class,_H,:,_01e_n,{,$e,(,),{,},Constructor,(,o0_e_u,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,0XBD2,],,,0b1011,],,,12,],,,0b101,],;,U_O,,,q8,:,Boolean,;,_3_,,,__,,,_,,,XJ,,,z,:,String,),{,},},<EOF>''',101))

    def test_1056(self):
        self.assertTrue(TestLexer.test('''Class S_3{}Class _:D{}Class _:_{}Class _:xT9{Var $__,$J,$L,m,_:Float ;}Class K{Var k_:I;Destructor (){Continue ;Continue ;} }Class _{}Class o{}''','''Class,S_3,{,},Class,_,:,D,{,},Class,_,:,_,{,},Class,_,:,xT9,{,Var,$__,,,$J,,,$L,,,m,,,_,:,Float,;,},Class,K,{,Var,k_,:,I,;,Destructor,(,),{,Continue,;,Continue,;,},},Class,_,{,},Class,o,{,},<EOF>''',101))

    def test_1057(self):
        self.assertTrue(TestLexer.test('''Class P:_{}Class _9:i1__m{ok(){}Var $_3:_;Constructor (r,_:_D_;_,J,x,_:Array [Array [Array [Boolean ,1_2_3_9_6_778],0B10],0114]){Break ;} }Class _{}Class _:O_{}Class n5:_l{}Class _{}''','''Class,P,:,_,{,},Class,_9,:,i1__m,{,ok,(,),{,},Var,$_3,:,_,;,Constructor,(,r,,,_,:,_D_,;,_,,,J,,,x,,,_,:,Array,[,Array,[,Array,[,Boolean,,,12396778,],,,0B10,],,,0114,],),{,Break,;,},},Class,_,{,},Class,_,:,O_,{,},Class,n5,:,_l,{,},Class,_,{,},<EOF>''',101))

    def test_1058(self):
        self.assertTrue(TestLexer.test('''Class X__:V95_{Constructor (___,g,_tn:Boolean ){} }Class X:_e{}Class W{Val F2,$_:Float ;$_X_(qu6,_,a,aPa,_,___:Array [Array [Array [String ,0b1001010],4_2],05_4_13];_:Boolean ;e___:Boolean ){} }''','''Class,X__,:,V95_,{,Constructor,(,___,,,g,,,_tn,:,Boolean,),{,},},Class,X,:,_e,{,},Class,W,{,Val,F2,,,$_,:,Float,;,$_X_,(,qu6,,,_,,,a,,,aPa,,,_,,,___,:,Array,[,Array,[,Array,[,String,,,0b1001010,],,,42,],,,05413,],;,_,:,Boolean,;,e___,:,Boolean,),{,},},<EOF>''',101))

    def test_1059(self):
        self.assertTrue(TestLexer.test('''Class oF7L{Var _,_6:String ;Constructor (_,M,_:__;JA2:_c;DJ:Array [Array [Int ,0X8C],0102];d:_0;sAq:Array [Array [Array [Boolean ,6],0XA],06];_:_;ttq64:Array [Array [Array [Boolean ,65],65],65]){Continue ;}Destructor (){} }Class O_18{}Class __{}Class _{}''','''Class,oF7L,{,Var,_,,,_6,:,String,;,Constructor,(,_,,,M,,,_,:,__,;,JA2,:,_c,;,DJ,:,Array,[,Array,[,Int,,,0X8C,],,,0102,],;,d,:,_0,;,sAq,:,Array,[,Array,[,Array,[,Boolean,,,6,],,,0XA,],,,06,],;,_,:,_,;,ttq64,:,Array,[,Array,[,Array,[,Boolean,,,65,],,,65,],,,65,],),{,Continue,;,},Destructor,(,),{,},},Class,O_18,{,},Class,__,{,},Class,_,{,},<EOF>''',101))

    def test_1060(self):
        self.assertTrue(TestLexer.test('''Class A_{Val $GZ:Boolean ;Val $_Q_,$o:_b095_K_u;Constructor (Xx,_:Array [Boolean ,0B111111]){}Var qq:Array [Array [Array [Array [Array [String ,0x58],0B111111],0B10],2],0b1100100];}Class __{}Class _{Constructor (_,Q:Array [Boolean ,0b1100100]){} }''','''Class,A_,{,Val,$GZ,:,Boolean,;,Val,$_Q_,,,$o,:,_b095_K_u,;,Constructor,(,Xx,,,_,:,Array,[,Boolean,,,0B111111,],),{,},Var,qq,:,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0x58,],,,0B111111,],,,0B10,],,,2,],,,0b1100100,],;,},Class,__,{,},Class,_,{,Constructor,(,_,,,Q,:,Array,[,Boolean,,,0b1100100,],),{,},},<EOF>''',101))

    def test_1061(self):
        self.assertTrue(TestLexer.test('''Class F{Constructor (){} }Class D:b{Constructor (_:X;CGv9,B4:Array [Array [Array [Array [Array [Float ,98],0b1],3],0X27],053];_2__,_V,R:String ;C4:Array [Array [Array [String ,0X27],0B1_1],0x22]){} }Class v78_7:Z3o_{}''','''Class,F,{,Constructor,(,),{,},},Class,D,:,b,{,Constructor,(,_,:,X,;,CGv9,,,B4,:,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,98,],,,0b1,],,,3,],,,0X27,],,,053,],;,_2__,,,_V,,,R,:,String,;,C4,:,Array,[,Array,[,Array,[,String,,,0X27,],,,0B11,],,,0x22,],),{,},},Class,v78_7,:,Z3o_,{,},<EOF>''',101))

    def test_1062(self):
        self.assertTrue(TestLexer.test('''Class E:o5n_{$9H(_:Boolean ;e_,_,_3_:_;AC_M:Array [Int ,02];k,u:Array [Array [Array [String ,0XA6A],0100],0X3]){} }''','''Class,E,:,o5n_,{,$9H,(,_,:,Boolean,;,e_,,,_,,,_3_,:,_,;,AC_M,:,Array,[,Int,,,02,],;,k,,,u,:,Array,[,Array,[,Array,[,String,,,0XA6A,],,,0100,],,,0X3,],),{,},},<EOF>''',101))

    def test_1063(self):
        self.assertTrue(TestLexer.test('''Class Z6:_{Val $004M___G,$p_:Array [Boolean ,04_04_67];Var $P:Array [Array [String ,30],0b1];Z__(R:Array [Array [Array [String ,30],0B1_1_0_1_0],02_5_77]){} }Class _{}Class u:__v_v{}''','''Class,Z6,:,_,{,Val,$004M___G,,,$p_,:,Array,[,Boolean,,,040467,],;,Var,$P,:,Array,[,Array,[,String,,,30,],,,0b1,],;,Z__,(,R,:,Array,[,Array,[,Array,[,String,,,30,],,,0B11010,],,,02577,],),{,},},Class,_,{,},Class,u,:,__v_v,{,},<EOF>''',101))

    def test_1064(self):
        self.assertTrue(TestLexer.test('''Class ____{_(G,g,_,_:_;_,f9:String ;_,_6_:Array [Array [String ,047],42];K,_,N0:Array [Array [Array [Array [Array [Float ,0b1000001],42],047],0b1],0B10]){}Var $314_:Array [Boolean ,42];Constructor (){p::$_l();} }Class R3a:V{}Class _s37_:_{}''','''Class,____,{,_,(,G,,,g,,,_,,,_,:,_,;,_,,,f9,:,String,;,_,,,_6_,:,Array,[,Array,[,String,,,047,],,,42,],;,K,,,_,,,N0,:,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0b1000001,],,,42,],,,047,],,,0b1,],,,0B10,],),{,},Var,$314_,:,Array,[,Boolean,,,42,],;,Constructor,(,),{,p,::,$_l,(,),;,},},Class,R3a,:,V,{,},Class,_s37_,:,_,{,},<EOF>''',101))

    def test_1065(self):
        self.assertTrue(TestLexer.test('''Class T{c1(E2_0Y1_6:o_3_4_0;_J:Array [Array [Array [Array [Int ,0B1010000],04],074],05]){} }Class i1{}Class f_47:__{}''','''Class,T,{,c1,(,E2_0Y1_6,:,o_3_4_0,;,_J,:,Array,[,Array,[,Array,[,Array,[,Int,,,0B1010000,],,,04,],,,074,],,,05,],),{,},},Class,i1,{,},Class,f_47,:,__,{,},<EOF>''',101))

    def test_1066(self):
        self.assertTrue(TestLexer.test('''Class _:p_{}Class _u{Constructor (E320q_,gf3T,K:h3;d:Array [Array [Array [Array [Array [Float ,0b100000],025],50],8],06]){} }Class _:R711W{}''','''Class,_,:,p_,{,},Class,_u,{,Constructor,(,E320q_,,,gf3T,,,K,:,h3,;,d,:,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0b100000,],,,025,],,,50,],,,8,],,,06,],),{,},},Class,_,:,R711W,{,},<EOF>''',101))

    def test_1067(self):
        self.assertTrue(TestLexer.test('''Class _:Mh{}Class D{Constructor (_L_,__,fk,v,vQ__28F_,C2:String ;b,A,_H1:eV_){} }Class _L{}Class q_{}Class _{}''','''Class,_,:,Mh,{,},Class,D,{,Constructor,(,_L_,,,__,,,fk,,,v,,,vQ__28F_,,,C2,:,String,;,b,,,A,,,_H1,:,eV_,),{,},},Class,_L,{,},Class,q_,{,},Class,_,{,},<EOF>''',101))

    def test_1068(self):
        self.assertTrue(TestLexer.test('''Class __:U{Val B00D,$_,$N1,$_q_:Array [Boolean ,032];Val $DM__1_3,$_:Int ;Var $48:String ;}Class _{Destructor (){ {} }}''','''Class,__,:,U,{,Val,B00D,,,$_,,,$N1,,,$_q_,:,Array,[,Boolean,,,032,],;,Val,$DM__1_3,,,$_,:,Int,;,Var,$48,:,String,;,},Class,_,{,Destructor,(,),{,{,},},},<EOF>''',101))

    def test_1069(self):
        self.assertTrue(TestLexer.test('''Class A:e8_{Destructor (){Val S6:Array [Array [Array [String ,0B10_0],0b1_01],39];Break ;}Val $7,$w,$_:String ;}''','''Class,A,:,e8_,{,Destructor,(,),{,Val,S6,:,Array,[,Array,[,Array,[,String,,,0B100,],,,0b101,],,,39,],;,Break,;,},Val,$7,,,$w,,,$_,:,String,;,},<EOF>''',101))

    def test_1070(self):
        self.assertTrue(TestLexer.test('''Class _3:L2{Constructor (T,_:Array [Float ,72];_,yg:Array [Boolean ,0B11];__,__,_665,___:Array [Float ,72];_,_4_:Array [Array [Array [Array [String ,0x1C],72],0XD],248]){}Var $_b_,$z5:Boolean ;}''','''Class,_3,:,L2,{,Constructor,(,T,,,_,:,Array,[,Float,,,72,],;,_,,,yg,:,Array,[,Boolean,,,0B11,],;,__,,,__,,,_665,,,___,:,Array,[,Float,,,72,],;,_,,,_4_,:,Array,[,Array,[,Array,[,Array,[,String,,,0x1C,],,,72,],,,0XD,],,,248,],),{,},Var,$_b_,,,$z5,:,Boolean,;,},<EOF>''',101))

    def test_1071(self):
        self.assertTrue(TestLexer.test('''Class _9{Constructor (_3_,_8,SA,_,__0:Array [String ,84];c_,_P,_2_Z,sM:D2;_:Float ;_,I:Boolean ){}Var E,___M_:Array [Float ,0B1110];}''','''Class,_9,{,Constructor,(,_3_,,,_8,,,SA,,,_,,,__0,:,Array,[,String,,,84,],;,c_,,,_P,,,_2_Z,,,sM,:,D2,;,_,:,Float,;,_,,,I,:,Boolean,),{,},Var,E,,,___M_,:,Array,[,Float,,,0B1110,],;,},<EOF>''',101))

    def test_1072(self):
        self.assertTrue(TestLexer.test('''Class __{Val C_2F,$B:Int ;Constructor (_,L:Float ;o_,HToK:Array [Array [Float ,030],030]){}Var $9,$6:Float ;}Class s_:e_Y{}''','''Class,__,{,Val,C_2F,,,$B,:,Int,;,Constructor,(,_,,,L,:,Float,;,o_,,,HToK,:,Array,[,Array,[,Float,,,030,],,,030,],),{,},Var,$9,,,$6,:,Float,;,},Class,s_,:,e_Y,{,},<EOF>''',101))

    def test_1073(self):
        self.assertTrue(TestLexer.test('''Class dD:__{Var _2,y,$_q:Array [Array [Array [Array [Boolean ,06],91],0B10],0b110];}Class __5C{Val $_j:String ;}Class _10:_{}''','''Class,dD,:,__,{,Var,_2,,,y,,,$_q,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,06,],,,91,],,,0B10,],,,0b110,],;,},Class,__5C,{,Val,$_j,:,String,;,},Class,_10,:,_,{,},<EOF>''',101))

    def test_1074(self):
        self.assertTrue(TestLexer.test('''Class E{$08(_,__,kC2:M1d;M:Array [Float ,0b1000000]){} }Class _w{}Class O_wr_:D{$C__(){ {} }Constructor (){}Val _,_:Array [String ,0b1_1_1_1];}Class _{}''','''Class,E,{,$08,(,_,,,__,,,kC2,:,M1d,;,M,:,Array,[,Float,,,0b1000000,],),{,},},Class,_w,{,},Class,O_wr_,:,D,{,$C__,(,),{,{,},},Constructor,(,),{,},Val,_,,,_,:,Array,[,String,,,0b1111,],;,},Class,_,{,},<EOF>''',101))

    def test_1075(self):
        self.assertTrue(TestLexer.test('''Class __3_{Constructor (_x:String ;_:Array [Int ,0b100011];_,H,_:Array [Array [Int ,0B1],21];_,_,_,M1:Array [Array [Boolean ,07],07];p,o:Float ){} }Class _:_{}''','''Class,__3_,{,Constructor,(,_x,:,String,;,_,:,Array,[,Int,,,0b100011,],;,_,,,H,,,_,:,Array,[,Array,[,Int,,,0B1,],,,21,],;,_,,,_,,,_,,,M1,:,Array,[,Array,[,Boolean,,,07,],,,07,],;,p,,,o,:,Float,),{,},},Class,_,:,_,{,},<EOF>''',101))

    def test_1076(self):
        self.assertTrue(TestLexer.test('''Class _:_V{$5(g,h,J:Array [String ,0xF]){}$_(j,J:Array [Float ,07];B:Boolean ;_:Array [String ,0130]){}Val $_,$_:String ;Destructor (){}Destructor (){Continue ;} }Class i__{}''','''Class,_,:,_V,{,$5,(,g,,,h,,,J,:,Array,[,String,,,0xF,],),{,},$_,(,j,,,J,:,Array,[,Float,,,07,],;,B,:,Boolean,;,_,:,Array,[,String,,,0130,],),{,},Val,$_,,,$_,:,String,;,Destructor,(,),{,},Destructor,(,),{,Continue,;,},},Class,i__,{,},<EOF>''',101))

    def test_1077(self):
        self.assertTrue(TestLexer.test('''Class _{Constructor (){} }Class h{Val $x:C;}Class i_{Val $_,$I_:Array [Array [String ,69],05];Var A,S:Array [Array [Boolean ,0106],7];}''','''Class,_,{,Constructor,(,),{,},},Class,h,{,Val,$x,:,C,;,},Class,i_,{,Val,$_,,,$I_,:,Array,[,Array,[,String,,,69,],,,05,],;,Var,A,,,S,:,Array,[,Array,[,Boolean,,,0106,],,,7,],;,},<EOF>''',101))

    def test_1078(self):
        self.assertTrue(TestLexer.test('''Class _{}Class E8:_{}Class _32__{Var $__a:_9;Destructor (){} }Class _8__7o{Val $_,e,$X,__:Array [Array [Array [Boolean ,0B100010],49],032];Val e,AL,J:_k6_4;Destructor (){}Constructor (){} }''','''Class,_,{,},Class,E8,:,_,{,},Class,_32__,{,Var,$__a,:,_9,;,Destructor,(,),{,},},Class,_8__7o,{,Val,$_,,,e,,,$X,,,__,:,Array,[,Array,[,Array,[,Boolean,,,0B100010,],,,49,],,,032,],;,Val,e,,,AL,,,J,:,_k6_4,;,Destructor,(,),{,},Constructor,(,),{,},},<EOF>''',101))

    def test_1079(self):
        self.assertTrue(TestLexer.test('''Class c38{Destructor (){Val C,P:Array [String ,0xC];}Var $_1:Array [Array [Array [Float ,044],0B1_11],0XF];}Class _:__{Val FT,$9_,$N_,_,_,f,GhQz,$_,_28,$_:b;}Class D{}''','''Class,c38,{,Destructor,(,),{,Val,C,,,P,:,Array,[,String,,,0xC,],;,},Var,$_1,:,Array,[,Array,[,Array,[,Float,,,044,],,,0B111,],,,0XF,],;,},Class,_,:,__,{,Val,FT,,,$9_,,,$N_,,,_,,,_,,,f,,,GhQz,,,$_,,,_28,,,$_,:,b,;,},Class,D,{,},<EOF>''',101))

    def test_1080(self):
        self.assertTrue(TestLexer.test('''Class i_{}Class D_{Constructor (){}$27C5_1(){}Destructor (){Val _,_m2,h9,_q,__2,e:O4;Break ;_T::$K_();}Destructor (){}Constructor (__v:Int ;a:Array [Boolean ,072]){} }''','''Class,i_,{,},Class,D_,{,Constructor,(,),{,},$27C5_1,(,),{,},Destructor,(,),{,Val,_,,,_m2,,,h9,,,_q,,,__2,,,e,:,O4,;,Break,;,_T,::,$K_,(,),;,},Destructor,(,),{,},Constructor,(,__v,:,Int,;,a,:,Array,[,Boolean,,,072,],),{,},},<EOF>''',101))

    def test_1081(self):
        self.assertTrue(TestLexer.test('''Class _:M{$i(){}Val i_Z__,__:String ;}Class __{}Class wP{Var h_,_,$Bq__:Array [Array [String ,0B1],5];}Class T{}''','''Class,_,:,M,{,$i,(,),{,},Val,i_Z__,,,__,:,String,;,},Class,__,{,},Class,wP,{,Var,h_,,,_,,,$Bq__,:,Array,[,Array,[,String,,,0B1,],,,5,],;,},Class,T,{,},<EOF>''',101))

    def test_1082(self):
        self.assertTrue(TestLexer.test('''Class __:__{Var $_5_:Array [Array [Array [String ,011],047],0XB];}Class o:_{Val _8,$7:Array [Array [Array [Array [String ,0x3A],074],01],011];}''','''Class,__,:,__,{,Var,$_5_,:,Array,[,Array,[,Array,[,String,,,011,],,,047,],,,0XB,],;,},Class,o,:,_,{,Val,_8,,,$7,:,Array,[,Array,[,Array,[,Array,[,String,,,0x3A,],,,074,],,,01,],,,011,],;,},<EOF>''',101))

    def test_1083(self):
        self.assertTrue(TestLexer.test('''Class g:__3{$T(){}Constructor (){} }Class _1_:_1{Constructor (j,_,__,_:Boolean ;VX,oD_:Array [Array [Array [Array [String ,0b1100],0x2_2],0x36],0XF];Y_T3,g_:Boolean ){Var _,YXL,R:Xc1;} }''','''Class,g,:,__3,{,$T,(,),{,},Constructor,(,),{,},},Class,_1_,:,_1,{,Constructor,(,j,,,_,,,__,,,_,:,Boolean,;,VX,,,oD_,:,Array,[,Array,[,Array,[,Array,[,String,,,0b1100,],,,0x22,],,,0x36,],,,0XF,],;,Y_T3,,,g_,:,Boolean,),{,Var,_,,,YXL,,,R,:,Xc1,;,},},<EOF>''',101))

    def test_1084(self):
        self.assertTrue(TestLexer.test('''Class S2{$9(_v:J_;Eh_,C_:Array [Array [Float ,50],50];_aJ,G_H_DS_L,I_:_){}$6k(e:Array [Array [Array [String ,3],0127],0X971];B,c:Array [Boolean ,50];F,_B,_:Array [Float ,0B1000100];_4,E,SN_r,z,QIa,p3:Array [String ,0b1010010]){Continue ;}Val _5,$_2:String ;}''','''Class,S2,{,$9,(,_v,:,J_,;,Eh_,,,C_,:,Array,[,Array,[,Float,,,50,],,,50,],;,_aJ,,,G_H_DS_L,,,I_,:,_,),{,},$6k,(,e,:,Array,[,Array,[,Array,[,String,,,3,],,,0127,],,,0X971,],;,B,,,c,:,Array,[,Boolean,,,50,],;,F,,,_B,,,_,:,Array,[,Float,,,0B1000100,],;,_4,,,E,,,SN_r,,,z,,,QIa,,,p3,:,Array,[,String,,,0b1010010,],),{,Continue,;,},Val,_5,,,$_2,:,String,;,},<EOF>''',101))

    def test_1085(self):
        self.assertTrue(TestLexer.test('''Class _9g__:Y{}Class W{Constructor (_:_;_h,_,__,f,__w_6___,_,Ga7,_6,_w:Int ;_B:f6;_,NQ,_s_:v){ {}Continue ;} }Class _{}''','''Class,_9g__,:,Y,{,},Class,W,{,Constructor,(,_,:,_,;,_h,,,_,,,__,,,f,,,__w_6___,,,_,,,Ga7,,,_6,,,_w,:,Int,;,_B,:,f6,;,_,,,NQ,,,_s_,:,v,),{,{,},Continue,;,},},Class,_,{,},<EOF>''',101))

    def test_1086(self):
        self.assertTrue(TestLexer.test('''Class _{}Class n{Var $_l:F=0.UP().t_().__;Destructor (){Return ;} }Class _1:_6M8F{}Class _Fj63_{Val $_:_;Val _J:Array [Array [Int ,66],0B1011];}''','''Class,_,{,},Class,n,{,Var,$_l,:,F,=,0.,UP,(,),.,t_,(,),.,__,;,Destructor,(,),{,Return,;,},},Class,_1,:,_6M8F,{,},Class,_Fj63_,{,Val,$_,:,_,;,Val,_J,:,Array,[,Array,[,Int,,,66,],,,0B1011,],;,},<EOF>''',101))

    def test_1087(self):
        self.assertTrue(TestLexer.test('''Class b{}Class J_:___W_{Var $i5V,$5n6:Array [Array [Array [Array [Array [Array [Array [Float ,045],10],0X39],045],0B1],045],0B1_0];}''','''Class,b,{,},Class,J_,:,___W_,{,Var,$i5V,,,$5n6,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,045,],,,10,],,,0X39,],,,045,],,,0B1,],,,045,],,,0B10,],;,},<EOF>''',101))

    def test_1088(self):
        self.assertTrue(TestLexer.test('''Class _2{Destructor (){Break ;Continue ;} }Class iX{Val ____,___,J2Q,__I:Array [Int ,18];}Class _:__{Constructor (P,_wS:Float ){ {} }}Class O{}''','''Class,_2,{,Destructor,(,),{,Break,;,Continue,;,},},Class,iX,{,Val,____,,,___,,,J2Q,,,__I,:,Array,[,Int,,,18,],;,},Class,_,:,__,{,Constructor,(,P,,,_wS,:,Float,),{,{,},},},Class,O,{,},<EOF>''',101))

    def test_1089(self):
        self.assertTrue(TestLexer.test('''Class _:K0{}Class __:Lt{Var $_0_:Array [Float ,037];Var _,Q:q_;}Class J:_9{Val ___:Array [Array [String ,0b101010],47];Constructor (){}Constructor (_,_:Array [String ,0b101010];_9_R:c;__9:Float ;P:m5a3H){} }''','''Class,_,:,K0,{,},Class,__,:,Lt,{,Var,$_0_,:,Array,[,Float,,,037,],;,Var,_,,,Q,:,q_,;,},Class,J,:,_9,{,Val,___,:,Array,[,Array,[,String,,,0b101010,],,,47,],;,Constructor,(,),{,},Constructor,(,_,,,_,:,Array,[,String,,,0b101010,],;,_9_R,:,c,;,__9,:,Float,;,P,:,m5a3H,),{,},},<EOF>''',101))

    def test_1090(self):
        self.assertTrue(TestLexer.test('''Class t{Val $l,_:String ;_nA_sS(){}Val $__:Array [Boolean ,0x8];Constructor (y,_8,Z,E,q_09:String ){} }Class ___uo:e{}Class Mh_{}Class x{}Class _{Constructor (){}Destructor (){}Var $31:Boolean ;}''','''Class,t,{,Val,$l,,,_,:,String,;,_nA_sS,(,),{,},Val,$__,:,Array,[,Boolean,,,0x8,],;,Constructor,(,y,,,_8,,,Z,,,E,,,q_09,:,String,),{,},},Class,___uo,:,e,{,},Class,Mh_,{,},Class,x,{,},Class,_,{,Constructor,(,),{,},Destructor,(,),{,},Var,$31,:,Boolean,;,},<EOF>''',101))

    def test_1091(self):
        self.assertTrue(TestLexer.test('''Class e:h{Constructor (_A:Array [String ,0b1100];__:Array [String ,0B1_1];B,_3:Array [Int ,0b1];__2:Array [Array [Array [Array [Boolean ,0X62],021],9_9],13];__,y:Qq){} }Class Vq6_:_{}''','''Class,e,:,h,{,Constructor,(,_A,:,Array,[,String,,,0b1100,],;,__,:,Array,[,String,,,0B11,],;,B,,,_3,:,Array,[,Int,,,0b1,],;,__2,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,0X62,],,,021,],,,99,],,,13,],;,__,,,y,:,Qq,),{,},},Class,Vq6_,:,_,{,},<EOF>''',101))

    def test_1092(self):
        self.assertTrue(TestLexer.test('''Class _7:N{}Class _2x{$d(E_:Array [String ,0b1]){}Var _1,$Sq,$WF_:Array [Int ,0X3E];}Class __7:n_{$p(){}Var $0d_:_;}''','''Class,_7,:,N,{,},Class,_2x,{,$d,(,E_,:,Array,[,String,,,0b1,],),{,},Var,_1,,,$Sq,,,$WF_,:,Array,[,Int,,,0X3E,],;,},Class,__7,:,n_,{,$p,(,),{,},Var,$0d_,:,_,;,},<EOF>''',101))

    def test_1093(self):
        self.assertTrue(TestLexer.test('''Class kT{Constructor (){}Destructor (){}Destructor (){}Val h:o9;Constructor (H:String ;_,g,_,E,c,B,k_,_h,M_81,_:Float ){Break ;W::$N_();Break ;} }''','''Class,kT,{,Constructor,(,),{,},Destructor,(,),{,},Destructor,(,),{,},Val,h,:,o9,;,Constructor,(,H,:,String,;,_,,,g,,,_,,,E,,,c,,,B,,,k_,,,_h,,,M_81,,,_,:,Float,),{,Break,;,W,::,$N_,(,),;,Break,;,},},<EOF>''',101))

    def test_1094(self):
        self.assertTrue(TestLexer.test('''Class _6:W{Constructor (f:_319;__:Array [String ,0XE];_:Array [Float ,0X1];_:Array [Array [Array [Array [Float ,38],0110],0B1001100],0110]){} }Class L4:_a5{Constructor (B,_,_,T:Float ;_4:Array [Array [Boolean ,02_15],0110]){}Val r,HY,c_:Array [Array [Array [String ,02],0b1010110],0X2_66];}''','''Class,_6,:,W,{,Constructor,(,f,:,_319,;,__,:,Array,[,String,,,0XE,],;,_,:,Array,[,Float,,,0X1,],;,_,:,Array,[,Array,[,Array,[,Array,[,Float,,,38,],,,0110,],,,0B1001100,],,,0110,],),{,},},Class,L4,:,_a5,{,Constructor,(,B,,,_,,,_,,,T,:,Float,;,_4,:,Array,[,Array,[,Boolean,,,0215,],,,0110,],),{,},Val,r,,,HY,,,c_,:,Array,[,Array,[,Array,[,String,,,02,],,,0b1010110,],,,0X266,],;,},<EOF>''',101))

    def test_1095(self):
        self.assertTrue(TestLexer.test('''Class _{Constructor (_xX:String ){Break ;} }Class _:T_{Destructor (){ {}{}Var _3:Array [Array [Array [Int ,0b10],0b1],0X30_E];Return ;} }''','''Class,_,{,Constructor,(,_xX,:,String,),{,Break,;,},},Class,_,:,T_,{,Destructor,(,),{,{,},{,},Var,_3,:,Array,[,Array,[,Array,[,Int,,,0b10,],,,0b1,],,,0X30E,],;,Return,;,},},<EOF>''',101))

    def test_1096(self):
        self.assertTrue(TestLexer.test('''Class t{OZh___(__0__:Int ){}Var $6E00:Array [Array [Array [Array [String ,0b1010011],0xC],03],0X44];Val $_3t,e_:Array [Boolean ,32];}Class _:_{Val $K_:Array [Boolean ,05];}''','''Class,t,{,OZh___,(,__0__,:,Int,),{,},Var,$6E00,:,Array,[,Array,[,Array,[,Array,[,String,,,0b1010011,],,,0xC,],,,03,],,,0X44,],;,Val,$_3t,,,e_,:,Array,[,Boolean,,,32,],;,},Class,_,:,_,{,Val,$K_,:,Array,[,Boolean,,,05,],;,},<EOF>''',101))

    def test_1097(self):
        self.assertTrue(TestLexer.test('''Class ___:_{Var $M:Array [Int ,05_5];Constructor (_:Array [Array [Float ,25],0x4]){ {}E::$_();} }Class _QR8:Q{}Class Q:_{}''','''Class,___,:,_,{,Var,$M,:,Array,[,Int,,,055,],;,Constructor,(,_,:,Array,[,Array,[,Float,,,25,],,,0x4,],),{,{,},E,::,$_,(,),;,},},Class,_QR8,:,Q,{,},Class,Q,:,_,{,},<EOF>''',101))

    def test_1098(self):
        self.assertTrue(TestLexer.test('''Class _d:_{}Class rf{}Class Xe{}Class _H{$57(Q:Array [Array [Array [Float ,0X12],0b1010],2_58];_0,__:Int ){}Var yO:Array [Array [String ,0X963],03];Constructor (){}Destructor (){} }''','''Class,_d,:,_,{,},Class,rf,{,},Class,Xe,{,},Class,_H,{,$57,(,Q,:,Array,[,Array,[,Array,[,Float,,,0X12,],,,0b1010,],,,258,],;,_0,,,__,:,Int,),{,},Var,yO,:,Array,[,Array,[,String,,,0X963,],,,03,],;,Constructor,(,),{,},Destructor,(,),{,},},<EOF>''',101))

    def test_1099(self):
        self.assertTrue(TestLexer.test('''Class W:U{Constructor (){}Constructor (){}Val $18kGc6:Array [Int ,051];}Class _{Val _,_,$_,$0:Array [Float ,1];}Class _5L:h_{}''','''Class,W,:,U,{,Constructor,(,),{,},Constructor,(,),{,},Val,$18kGc6,:,Array,[,Int,,,051,],;,},Class,_,{,Val,_,,,_,,,$_,,,$0,:,Array,[,Float,,,1,],;,},Class,_5L,:,h_,{,},<EOF>''',101))

    def test_1100(self):
        self.assertTrue(TestLexer.test('''Class i{Val s608,$_:_9;Val __,$l:z4;}Class __:_{Var y_:Array [Array [Array [Array [Array [Array [Boolean ,0X9],033],0x5A],033],63],0X15];Var $__:_;}''','''Class,i,{,Val,s608,,,$_,:,_9,;,Val,__,,,$l,:,z4,;,},Class,__,:,_,{,Var,y_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0X9,],,,033,],,,0x5A,],,,033,],,,63,],,,0X15,],;,Var,$__,:,_,;,},<EOF>''',101))

    def test_1101(self):
        self.assertTrue(TestLexer.test('''Class _:A{_(_0,_,_,a,__,___,__R2:Array [Array [Array [Array [Array [String ,2],0b11110],0b11110],7_3],034];_:_){}Destructor (){}Destructor (){} }''','''Class,_,:,A,{,_,(,_0,,,_,,,_,,,a,,,__,,,___,,,__R2,:,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,2,],,,0b11110,],,,0b11110,],,,73,],,,034,],;,_,:,_,),{,},Destructor,(,),{,},Destructor,(,),{,},},<EOF>''',101))

    def test_1102(self):
        self.assertTrue(TestLexer.test('''Class _{Constructor (D:_;KT:Array [Array [Array [Int ,0314_1_0_7_1],0113],0113];_6_,G,_7:Array [Int ,0113];__5:M){Continue ;Continue ;Break ;} }''','''Class,_,{,Constructor,(,D,:,_,;,KT,:,Array,[,Array,[,Array,[,Int,,,03141071,],,,0113,],,,0113,],;,_6_,,,G,,,_7,:,Array,[,Int,,,0113,],;,__5,:,M,),{,Continue,;,Continue,;,Break,;,},},<EOF>''',101))

    def test_1103(self):
        self.assertTrue(TestLexer.test('''Class __L{dG_Un_5(____,_K_:Array [Array [Array [Array [Array [Array [Array [Array [Array [Float ,01],0b1_0],2_5],0XE],0X9],052],7],0x8],29]){}Destructor (){Break ;{} }Var $c39_z_:Array [Array [String ,0b1011101],32_8]=bQ_o___::$c.D9_6._q;}''','''Class,__L,{,dG_Un_5,(,____,,,_K_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,01,],,,0b10,],,,25,],,,0XE,],,,0X9,],,,052,],,,7,],,,0x8,],,,29,],),{,},Destructor,(,),{,Break,;,{,},},Var,$c39_z_,:,Array,[,Array,[,String,,,0b1011101,],,,328,],=,bQ_o___,::,$c,.,D9_6,.,_q,;,},<EOF>''',101))

    def test_1104(self):
        self.assertTrue(TestLexer.test('''Class n__{Constructor (i_6_:Array [Array [Array [Int ,0X6_B9],7],062_0_73]){}Constructor (A:m;_,K6y,__,_4,_2l0,__6,J0,O5,_:Float ;_,G:Array [Boolean ,0XB]){} }''','''Class,n__,{,Constructor,(,i_6_,:,Array,[,Array,[,Array,[,Int,,,0X6B9,],,,7,],,,062073,],),{,},Constructor,(,A,:,m,;,_,,,K6y,,,__,,,_4,,,_2l0,,,__6,,,J0,,,O5,,,_,:,Float,;,_,,,G,:,Array,[,Boolean,,,0XB,],),{,},},<EOF>''',101))

    def test_1105(self):
        self.assertTrue(TestLexer.test('''Class Q__6_:d{}Class e{}Class _{Val $y_:Boolean ;Constructor (_,K,t1,___7_:Array [String ,0X3D_C_1];Vcx,c,_d,E3,h___,__:Array [Array [Array [Array [Float ,23],8],0b100000],0B1];CO:_P77){Return ;}Val _,_Y_2,_:Array [Array [String ,23],1];Val _:Array [String ,0131];Var _Z5:Array [String ,0b100000];}''','''Class,Q__6_,:,d,{,},Class,e,{,},Class,_,{,Val,$y_,:,Boolean,;,Constructor,(,_,,,K,,,t1,,,___7_,:,Array,[,String,,,0X3DC1,],;,Vcx,,,c,,,_d,,,E3,,,h___,,,__,:,Array,[,Array,[,Array,[,Array,[,Float,,,23,],,,8,],,,0b100000,],,,0B1,],;,CO,:,_P77,),{,Return,;,},Val,_,,,_Y_2,,,_,:,Array,[,Array,[,String,,,23,],,,1,],;,Val,_,:,Array,[,String,,,0131,],;,Var,_Z5,:,Array,[,String,,,0b100000,],;,},<EOF>''',101))

    def test_1106(self):
        self.assertTrue(TestLexer.test('''Class _E:R{Constructor (__,w:Int ;nn5_L59:Array [Array [Array [Array [String ,0X61],5],07],0b1001110]){}Destructor (){} }Class y{Constructor (O,_:Array [Array [String ,0b1_0_1],0x13]){}Val _0_5:Pw=!-"'""<=-_Ad4::$0.__f.__D;}''','''Class,_E,:,R,{,Constructor,(,__,,,w,:,Int,;,nn5_L59,:,Array,[,Array,[,Array,[,Array,[,String,,,0X61,],,,5,],,,07,],,,0b1001110,],),{,},Destructor,(,),{,},},Class,y,{,Constructor,(,O,,,_,:,Array,[,Array,[,String,,,0b101,],,,0x13,],),{,},Val,_0_5,:,Pw,=,!,-,'",<=,-,_Ad4,::,$0,.,__f,.,__D,;,},<EOF>''',101))

    def test_1107(self):
        self.assertTrue(TestLexer.test('''Class __6:a_{Var U:Array [Array [Array [Array [Array [Boolean ,0b10_1],01_5],87],0B1],024];Var $1:Array [Boolean ,012];}Class Gb:K14l2{}Class d6:O{}Class P:_1{}''','''Class,__6,:,a_,{,Var,U,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0b101,],,,015,],,,87,],,,0B1,],,,024,],;,Var,$1,:,Array,[,Boolean,,,012,],;,},Class,Gb,:,K14l2,{,},Class,d6,:,O,{,},Class,P,:,_1,{,},<EOF>''',101))

    def test_1108(self):
        self.assertTrue(TestLexer.test('''Class _Y2:U{Val $_,_:Int ;Constructor (__6,_:t;W_:I){} }Class ___e:_{}Class q_9{Var _27_a43:Array [Array [String ,04_0],0X22];}Class H:Dv_{}''','''Class,_Y2,:,U,{,Val,$_,,,_,:,Int,;,Constructor,(,__6,,,_,:,t,;,W_,:,I,),{,},},Class,___e,:,_,{,},Class,q_9,{,Var,_27_a43,:,Array,[,Array,[,String,,,040,],,,0X22,],;,},Class,H,:,Dv_,{,},<EOF>''',101))

    def test_1109(self):
        self.assertTrue(TestLexer.test('''Class _F:dw{Var s,m_:Float ;$_3(_,E:z){ {} }Destructor (){}Destructor (){} }Class N_fGl{Val $f_2,$59_3,_:Array [Array [Array [Array [Array [Int ,0XB_6],4],03_5],0x57],0b101];$1(){}Destructor (){}Val I:Boolean ;}Class _2{_(c67,__9_:Array [Float ,0XC]){} }Class M8{Val $_Bi__3,$s:Array [Array [String ,027],41];Val q_:KM2j_=!_0::$_._9V()._2a._7z_.__;}''','''Class,_F,:,dw,{,Var,s,,,m_,:,Float,;,$_3,(,_,,,E,:,z,),{,{,},},Destructor,(,),{,},Destructor,(,),{,},},Class,N_fGl,{,Val,$f_2,,,$59_3,,,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0XB6,],,,4,],,,035,],,,0x57,],,,0b101,],;,$1,(,),{,},Destructor,(,),{,},Val,I,:,Boolean,;,},Class,_2,{,_,(,c67,,,__9_,:,Array,[,Float,,,0XC,],),{,},},Class,M8,{,Val,$_Bi__3,,,$s,:,Array,[,Array,[,String,,,027,],,,41,],;,Val,q_,:,KM2j_,=,!,_0,::,$_,.,_9V,(,),.,_2a,.,_7z_,.,__,;,},<EOF>''',101))

    def test_1110(self):
        self.assertTrue(TestLexer.test('''Class _6{}Class u{Var $_:Array [Boolean ,0b1_1];_V(z,_,Mr:p_;n03:Q5_;_1,y_,_w5_:f;D,_P_1:Int ){Break ;Break ;} }''','''Class,_6,{,},Class,u,{,Var,$_,:,Array,[,Boolean,,,0b11,],;,_V,(,z,,,_,,,Mr,:,p_,;,n03,:,Q5_,;,_1,,,y_,,,_w5_,:,f,;,D,,,_P_1,:,Int,),{,Break,;,Break,;,},},<EOF>''',101))

    def test_1111(self):
        self.assertTrue(TestLexer.test('''Class _{$_(_,_:_K_3){}Constructor (aT:Array [Array [Array [Int ,0x18],0272052_45],0x50];_6:Array [Boolean ,05];i_,B_,_,_U:Array [String ,07];_,_o_m_L48_e,J:Int ){} }''','''Class,_,{,$_,(,_,,,_,:,_K_3,),{,},Constructor,(,aT,:,Array,[,Array,[,Array,[,Int,,,0x18,],,,027205245,],,,0x50,],;,_6,:,Array,[,Boolean,,,05,],;,i_,,,B_,,,_,,,_U,:,Array,[,String,,,07,],;,_,,,_o_m_L48_e,,,J,:,Int,),{,},},<EOF>''',101))

    def test_1112(self):
        self.assertTrue(TestLexer.test('''Class _S2:_{Destructor (){} }Class G_6:E{}Class _:c{}Class iA{L_9k_(_p,d:Boolean ;_:_P;i6:n;D:Int ;Q,_j3K_,_:Int ){} }''','''Class,_S2,:,_,{,Destructor,(,),{,},},Class,G_6,:,E,{,},Class,_,:,c,{,},Class,iA,{,L_9k_,(,_p,,,d,:,Boolean,;,_,:,_P,;,i6,:,n,;,D,:,Int,;,Q,,,_j3K_,,,_,:,Int,),{,},},<EOF>''',101))

    def test_1113(self):
        self.assertTrue(TestLexer.test('''Class sC4{Constructor (__3:w;b_:_3_;_:Array [Array [Array [Array [Array [Array [String ,0b11011],016],0b11011],0x55],0b1],0B1];D,G:Array [String ,7];il,X__Z:_m9){} }Class L_{}Class _s_2{}''','''Class,sC4,{,Constructor,(,__3,:,w,;,b_,:,_3_,;,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0b11011,],,,016,],,,0b11011,],,,0x55,],,,0b1,],,,0B1,],;,D,,,G,:,Array,[,String,,,7,],;,il,,,X__Z,:,_m9,),{,},},Class,L_,{,},Class,_s_2,{,},<EOF>''',101))

    def test_1114(self):
        self.assertTrue(TestLexer.test('''Class __:__0{_(n6_M7A:Array [Array [Boolean ,05],65];Wt,fd,_,_:Array [Int ,65];k:String ;_90:Boolean ;E,_:__;_:Boolean ;c,k:__5){}Val $N,n,$__,h99_:Array [Array [Array [Array [Float ,65],0B1],05_444],053];}''','''Class,__,:,__0,{,_,(,n6_M7A,:,Array,[,Array,[,Boolean,,,05,],,,65,],;,Wt,,,fd,,,_,,,_,:,Array,[,Int,,,65,],;,k,:,String,;,_90,:,Boolean,;,E,,,_,:,__,;,_,:,Boolean,;,c,,,k,:,__5,),{,},Val,$N,,,n,,,$__,,,h99_,:,Array,[,Array,[,Array,[,Array,[,Float,,,65,],,,0B1,],,,05444,],,,053,],;,},<EOF>''',101))

    def test_1115(self):
        self.assertTrue(TestLexer.test('''Class z{Constructor (__1_5:bt_;_8,_:Array [Array [Array [Int ,1],0x28],0b1];__,__M:_){Var Qgt:Int ;}Val sk:Int ;Constructor (h,_i_:___3__;Q:Float ){}Var $_H21:String ;}Class _:____95{}Class __:___C{Var Z:_H8P__;}''','''Class,z,{,Constructor,(,__1_5,:,bt_,;,_8,,,_,:,Array,[,Array,[,Array,[,Int,,,1,],,,0x28,],,,0b1,],;,__,,,__M,:,_,),{,Var,Qgt,:,Int,;,},Val,sk,:,Int,;,Constructor,(,h,,,_i_,:,___3__,;,Q,:,Float,),{,},Var,$_H21,:,String,;,},Class,_,:,____95,{,},Class,__,:,___C,{,Var,Z,:,_H8P__,;,},<EOF>''',101))

    def test_1116(self):
        self.assertTrue(TestLexer.test('''Class E{Val y5_6i:Boolean ;}Class vVu_W{}Class _{Constructor (){}Destructor (){} }Class L:t{}Class T798{}Class U_{}''','''Class,E,{,Val,y5_6i,:,Boolean,;,},Class,vVu_W,{,},Class,_,{,Constructor,(,),{,},Destructor,(,),{,},},Class,L,:,t,{,},Class,T798,{,},Class,U_,{,},<EOF>''',101))

    def test_1117(self):
        self.assertTrue(TestLexer.test('''Class b{Destructor (){}Val $6,R,$_,I,_4_,T3,$_q___S,$7,__:mn;}Class h:_{Var $3:Boolean ;Constructor (_W9,M:Array [Int ,03];_,__:Float ;_,oc,H:_;U,_:e27xn1;_,M:Array [Array [Array [Int ,0B1],834],69];__,r,_,_:li){} }''','''Class,b,{,Destructor,(,),{,},Val,$6,,,R,,,$_,,,I,,,_4_,,,T3,,,$_q___S,,,$7,,,__,:,mn,;,},Class,h,:,_,{,Var,$3,:,Boolean,;,Constructor,(,_W9,,,M,:,Array,[,Int,,,03,],;,_,,,__,:,Float,;,_,,,oc,,,H,:,_,;,U,,,_,:,e27xn1,;,_,,,M,:,Array,[,Array,[,Array,[,Int,,,0B1,],,,834,],,,69,],;,__,,,r,,,_,,,_,:,li,),{,},},<EOF>''',101))

    def test_1118(self):
        self.assertTrue(TestLexer.test('''Class _15:q{Destructor (){Return ;Break ;Break ;} }Class A5v__6{_L(cU,_i:s;s_j_:Boolean ){} }Class __d:i33__{Var D:Array [Array [Float ,0B10100],0x8];}Class _:t_{Constructor (){} }''','''Class,_15,:,q,{,Destructor,(,),{,Return,;,Break,;,Break,;,},},Class,A5v__6,{,_L,(,cU,,,_i,:,s,;,s_j_,:,Boolean,),{,},},Class,__d,:,i33__,{,Var,D,:,Array,[,Array,[,Float,,,0B10100,],,,0x8,],;,},Class,_,:,t_,{,Constructor,(,),{,},},<EOF>''',101))

    def test_1119(self):
        self.assertTrue(TestLexer.test('''Class _{}Class D{Constructor (){}Constructor (){} }Class _7__:W{Constructor (sk_9,OR:Array [Array [Array [Float ,0b11010],026_727],0xBA_AD];_,_,Q,ux_:Float ){Return ;Break ;} }''','''Class,_,{,},Class,D,{,Constructor,(,),{,},Constructor,(,),{,},},Class,_7__,:,W,{,Constructor,(,sk_9,,,OR,:,Array,[,Array,[,Array,[,Float,,,0b11010,],,,026727,],,,0xBAAD,],;,_,,,_,,,Q,,,ux_,:,Float,),{,Return,;,Break,;,},},<EOF>''',101))

    def test_1120(self):
        self.assertTrue(TestLexer.test('''Class a33_e_{Var $_f,$_,_,$_,__:Int ;Val $4068_:Array [Boolean ,022];_(_,_J:_;_e,I:Array [Array [Array [Array [Int ,011_5],0X58],0X58],20]){} }''','''Class,a33_e_,{,Var,$_f,,,$_,,,_,,,$_,,,__,:,Int,;,Val,$4068_,:,Array,[,Boolean,,,022,],;,_,(,_,,,_J,:,_,;,_e,,,I,:,Array,[,Array,[,Array,[,Array,[,Int,,,0115,],,,0X58,],,,0X58,],,,20,],),{,},},<EOF>''',101))

    def test_1121(self):
        self.assertTrue(TestLexer.test('''Class _:__{Destructor (){Break ;}$1(){Break ;Var P,_Y9zi,c_:E;} }Class JK{Destructor (){} }Class _C{}Class Z:Hvk{}''','''Class,_,:,__,{,Destructor,(,),{,Break,;,},$1,(,),{,Break,;,Var,P,,,_Y9zi,,,c_,:,E,;,},},Class,JK,{,Destructor,(,),{,},},Class,_C,{,},Class,Z,:,Hvk,{,},<EOF>''',101))

    def test_1122(self):
        self.assertTrue(TestLexer.test('''Class _J:E{Constructor (){}$V_(Z,_:String ;_:Array [Array [Array [Array [Array [Array [Float ,87],076],016],0B110110],87],87]){} }Class _8m5{}Class _{}Class EMdl{}''','''Class,_J,:,E,{,Constructor,(,),{,},$V_,(,Z,,,_,:,String,;,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,87,],,,076,],,,016,],,,0B110110,],,,87,],,,87,],),{,},},Class,_8m5,{,},Class,_,{,},Class,EMdl,{,},<EOF>''',101))

    def test_1123(self):
        self.assertTrue(TestLexer.test('''Class s_3V8_6T173:__69c{Var __:_q;}Class VH{$0_(){Break ;}Var b0_:Array [Array [Array [Int ,35],35],0X27];}Class _B_lu7{}''','''Class,s_3V8_6T173,:,__69c,{,Var,__,:,_q,;,},Class,VH,{,$0_,(,),{,Break,;,},Var,b0_,:,Array,[,Array,[,Array,[,Int,,,35,],,,35,],,,0X27,],;,},Class,_B_lu7,{,},<EOF>''',101))

    def test_1124(self):
        self.assertTrue(TestLexer.test('''Class _Xu_9L1_8__O8{Constructor (o0,_:_;c,_A:Float ;_,t,_7,L:Array [Array [Array [Array [Array [Array [Array [Array [String ,0X3C],1_3],056],0b1001001],03_1_6_7],04],0X5],072_1];__90,_,_Z:Float ;_3:Array [Array [String ,0X6],0b1001001];__:Int ;c:String ;g:Float ;ae_I1:Array [String ,0B1000110];_,_,_W:String ){} }''','''Class,_Xu_9L1_8__O8,{,Constructor,(,o0,,,_,:,_,;,c,,,_A,:,Float,;,_,,,t,,,_7,,,L,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0X3C,],,,13,],,,056,],,,0b1001001,],,,03167,],,,04,],,,0X5,],,,0721,],;,__90,,,_,,,_Z,:,Float,;,_3,:,Array,[,Array,[,String,,,0X6,],,,0b1001001,],;,__,:,Int,;,c,:,String,;,g,:,Float,;,ae_I1,:,Array,[,String,,,0B1000110,],;,_,,,_,,,_W,:,String,),{,},},<EOF>''',101))

    def test_1125(self):
        self.assertTrue(TestLexer.test('''Class _:c{Constructor (_,e:Array [Array [Array [Array [Boolean ,0b1],0b1],0b101000],0b101000];_d:_4_){d_::$__.O2iH.X9();} }Class _5:E{}''','''Class,_,:,c,{,Constructor,(,_,,,e,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,0b1,],,,0b1,],,,0b101000,],,,0b101000,],;,_d,:,_4_,),{,d_,::,$__,.,O2iH,.,X9,(,),;,},},Class,_5,:,E,{,},<EOF>''',101))

    def test_1126(self):
        self.assertTrue(TestLexer.test('''Class _{Val $_,$V:c6;Val $Y:_;Var _p4h,$8:Array [Boolean ,06];Y_(_2:Boolean ){Break ;} }Class J8:_{}Class _b__14J:o{}Class ___6{Var $0:String ;Destructor (){Break ;} }''','''Class,_,{,Val,$_,,,$V,:,c6,;,Val,$Y,:,_,;,Var,_p4h,,,$8,:,Array,[,Boolean,,,06,],;,Y_,(,_2,:,Boolean,),{,Break,;,},},Class,J8,:,_,{,},Class,_b__14J,:,o,{,},Class,___6,{,Var,$0,:,String,;,Destructor,(,),{,Break,;,},},<EOF>''',101))

    def test_1127(self):
        self.assertTrue(TestLexer.test('''Class j{Constructor (y:String ;_:Array [Array [Array [Boolean ,52_392_1],72],34_4];v_7__,_,uG,PG:Int ;_,G_Kx50,KP,q_9_e1,_4,_,g:Array [Array [Array [Array [Float ,0xD],0102],052_635_6],06];K1_j:Array [Float ,0102];_:Array [Int ,07]){} }Class I:y4{}''','''Class,j,{,Constructor,(,y,:,String,;,_,:,Array,[,Array,[,Array,[,Boolean,,,523921,],,,72,],,,344,],;,v_7__,,,_,,,uG,,,PG,:,Int,;,_,,,G_Kx50,,,KP,,,q_9_e1,,,_4,,,_,,,g,:,Array,[,Array,[,Array,[,Array,[,Float,,,0xD,],,,0102,],,,0526356,],,,06,],;,K1_j,:,Array,[,Float,,,0102,],;,_,:,Array,[,Int,,,07,],),{,},},Class,I,:,y4,{,},<EOF>''',101))

    def test_1128(self):
        self.assertTrue(TestLexer.test('''Class o{}Class E6{__2(z,_2:r;D,A:String ){}V3(_,cx:Int ){}_(_:Array [Array [Array [Array [Array [Boolean ,0b100110],22],0x1],0X3],0130];O_x,_:Array [Array [Array [Array [Boolean ,0130],0B111],0130],22]){} }''','''Class,o,{,},Class,E6,{,__2,(,z,,,_2,:,r,;,D,,,A,:,String,),{,},V3,(,_,,,cx,:,Int,),{,},_,(,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0b100110,],,,22,],,,0x1,],,,0X3,],,,0130,],;,O_x,,,_,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,0130,],,,0B111,],,,0130,],,,22,],),{,},},<EOF>''',101))

    def test_1129(self):
        self.assertTrue(TestLexer.test('''Class _1:g{Var _28,xT,x,_5,$c__:_Wg;$qEp_(a_0,zY,_:Float ;z__,_,_,_,_sE,_6,_,_,k,J_:Boolean ){ {} }$____(M,_5:String ;_D_:l_u_1;_9,pE:_){}Constructor (){} }''','''Class,_1,:,g,{,Var,_28,,,xT,,,x,,,_5,,,$c__,:,_Wg,;,$qEp_,(,a_0,,,zY,,,_,:,Float,;,z__,,,_,,,_,,,_,,,_sE,,,_6,,,_,,,_,,,k,,,J_,:,Boolean,),{,{,},},$____,(,M,,,_5,:,String,;,_D_,:,l_u_1,;,_9,,,pE,:,_,),{,},Constructor,(,),{,},},<EOF>''',101))

    def test_1130(self):
        self.assertTrue(TestLexer.test('''Class Gn{Constructor (_,_b:Array [Array [Boolean ,0b1_1],60];w_152M:Array [Array [Array [Array [Array [Boolean ,0xF_6_E_8B1E],075],60],0X1_A_7],0XD]){}Var __:Boolean ;}''','''Class,Gn,{,Constructor,(,_,,,_b,:,Array,[,Array,[,Boolean,,,0b11,],,,60,],;,w_152M,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0xF6E8B1E,],,,075,],,,60,],,,0X1A7,],,,0XD,],),{,},Var,__,:,Boolean,;,},<EOF>''',101))

    def test_1131(self):
        self.assertTrue(TestLexer.test('''Class __{Var $Z:E_;Val $_i,$_e:Eo5;Val $ycn,$9HC,$_y,O,$g:Float ;Var R,_,$3:Array [Array [Array [Array [Boolean ,0B1],0X4E],0XFD],0113];}Class E3:N{}Class _{}''','''Class,__,{,Var,$Z,:,E_,;,Val,$_i,,,$_e,:,Eo5,;,Val,$ycn,,,$9HC,,,$_y,,,O,,,$g,:,Float,;,Var,R,,,_,,,$3,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,0B1,],,,0X4E,],,,0XFD,],,,0113,],;,},Class,E3,:,N,{,},Class,_,{,},<EOF>''',101))

    def test_1132(self):
        self.assertTrue(TestLexer.test('''Class _2_{}Class e:_{Var _6_c_,X5,k:Array [Array [Float ,0X28],0X28];Destructor (){}Constructor (){}Var $_,$_,I_9,$6:Float ;w_(){} }Class N{}Class T6:z9{}Class b{}''','''Class,_2_,{,},Class,e,:,_,{,Var,_6_c_,,,X5,,,k,:,Array,[,Array,[,Float,,,0X28,],,,0X28,],;,Destructor,(,),{,},Constructor,(,),{,},Var,$_,,,$_,,,I_9,,,$6,:,Float,;,w_,(,),{,},},Class,N,{,},Class,T6,:,z9,{,},Class,b,{,},<EOF>''',101))

    def test_1133(self):
        self.assertTrue(TestLexer.test('''Class k:_{Constructor (X0h:Int ;o45_c,h,_9:String ;__zO,_:Array [Array [String ,0B10],05_6_05_5]){}Constructor (DP:Array [Array [Array [Array [Array [Array [Array [Array [Boolean ,0b1],0X2B],0B101011],777_3_42],1],0B101011],0B101011],0353]){} }''','''Class,k,:,_,{,Constructor,(,X0h,:,Int,;,o45_c,,,h,,,_9,:,String,;,__zO,,,_,:,Array,[,Array,[,String,,,0B10,],,,056055,],),{,},Constructor,(,DP,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0b1,],,,0X2B,],,,0B101011,],,,777342,],,,1,],,,0B101011,],,,0B101011,],,,0353,],),{,},},<EOF>''',101))

    def test_1134(self):
        self.assertTrue(TestLexer.test('''Class _x_90h{Destructor (){}Var __,$_:Array [Int ,023];}Class c{Val a:Array [Array [Array [Float ,0x5],0X4A],0x7_0];Val $_:_0;}''','''Class,_x_90h,{,Destructor,(,),{,},Var,__,,,$_,:,Array,[,Int,,,023,],;,},Class,c,{,Val,a,:,Array,[,Array,[,Array,[,Float,,,0x5,],,,0X4A,],,,0x70,],;,Val,$_,:,_0,;,},<EOF>''',101))

    def test_1135(self):
        self.assertTrue(TestLexer.test('''Class __12{}Class _:C2{}Class y:_{Constructor (_U:Array [String ,0x2B];M:Array [Array [Array [Array [Int ,0b1100001],0437],0X14],7_5];wA,_:Float ){} }Class _:E___94{Val _,$_:Jik__;}''','''Class,__12,{,},Class,_,:,C2,{,},Class,y,:,_,{,Constructor,(,_U,:,Array,[,String,,,0x2B,],;,M,:,Array,[,Array,[,Array,[,Array,[,Int,,,0b1100001,],,,0437,],,,0X14,],,,75,],;,wA,,,_,:,Float,),{,},},Class,_,:,E___94,{,Val,_,,,$_,:,Jik__,;,},<EOF>''',101))

    def test_1136(self):
        self.assertTrue(TestLexer.test('''Class f:_A1j{}Class ___{}Class r_:w_7___4___{Val _L537,$54_:Float ;}Class wxwN:v{}Class _Q_:m5{Constructor (){} }Class K47:l{$e(H,S,s:u;t,_e_,_:Boolean ){}Destructor (){} }Class _{}Class vU_:c4{Val _4:Array [String ,0B1];Constructor (){}Constructor (Q,_,__:Array [Array [Array [String ,4],61_0],043]){}Constructor (f,f_,_D7b,OV_hw9:Float ){Break ;} }''','''Class,f,:,_A1j,{,},Class,___,{,},Class,r_,:,w_7___4___,{,Val,_L537,,,$54_,:,Float,;,},Class,wxwN,:,v,{,},Class,_Q_,:,m5,{,Constructor,(,),{,},},Class,K47,:,l,{,$e,(,H,,,S,,,s,:,u,;,t,,,_e_,,,_,:,Boolean,),{,},Destructor,(,),{,},},Class,_,{,},Class,vU_,:,c4,{,Val,_4,:,Array,[,String,,,0B1,],;,Constructor,(,),{,},Constructor,(,Q,,,_,,,__,:,Array,[,Array,[,Array,[,String,,,4,],,,610,],,,043,],),{,},Constructor,(,f,,,f_,,,_D7b,,,OV_hw9,:,Float,),{,Break,;,},},<EOF>''',101))

    def test_1137(self):
        self.assertTrue(TestLexer.test('''Class _:i_{Constructor (j5rl,_,m6,_,h_P_G,I_,_,__:Array [Array [Array [Float ,33],20],33];m:Array [Array [Array [Boolean ,01],0b1],0117];_,iwS_,u:Boolean ){} }Class _:y{}''','''Class,_,:,i_,{,Constructor,(,j5rl,,,_,,,m6,,,_,,,h_P_G,,,I_,,,_,,,__,:,Array,[,Array,[,Array,[,Float,,,33,],,,20,],,,33,],;,m,:,Array,[,Array,[,Array,[,Boolean,,,01,],,,0b1,],,,0117,],;,_,,,iwS_,,,u,:,Boolean,),{,},},Class,_,:,y,{,},<EOF>''',101))

    def test_1138(self):
        self.assertTrue(TestLexer.test('''Class V:P{}Class _:_M{Var $29,_g6:Array [Int ,0B1];Var p53_:Array [Array [Float ,01],8];}Class _2:_{Var $_,__:Boolean ;Var Aj9,_4,$b2:Boolean ;}Class _{Constructor (_K_:Boolean ){} }''','''Class,V,:,P,{,},Class,_,:,_M,{,Var,$29,,,_g6,:,Array,[,Int,,,0B1,],;,Var,p53_,:,Array,[,Array,[,Float,,,01,],,,8,],;,},Class,_2,:,_,{,Var,$_,,,__,:,Boolean,;,Var,Aj9,,,_4,,,$b2,:,Boolean,;,},Class,_,{,Constructor,(,_K_,:,Boolean,),{,},},<EOF>''',101))

    def test_1139(self):
        self.assertTrue(TestLexer.test('''Class n{Destructor (){}Var y,$_W_:Array [Boolean ,8_914];Destructor (){}Val R,$_j:Array [Array [Float ,0B1_0],024_6_3];}''','''Class,n,{,Destructor,(,),{,},Var,y,,,$_W_,:,Array,[,Boolean,,,8914,],;,Destructor,(,),{,},Val,R,,,$_j,:,Array,[,Array,[,Float,,,0B10,],,,02463,],;,},<EOF>''',101))

    def test_1140(self):
        self.assertTrue(TestLexer.test('''Class O:i__{}Class _6M{Var _y,$U,q:Array [Boolean ,6];Destructor (){Break ;}Constructor (____:Array [Array [Boolean ,2],80]){} }Class x_0:s_L{}''','''Class,O,:,i__,{,},Class,_6M,{,Var,_y,,,$U,,,q,:,Array,[,Boolean,,,6,],;,Destructor,(,),{,Break,;,},Constructor,(,____,:,Array,[,Array,[,Boolean,,,2,],,,80,],),{,},},Class,x_0,:,s_L,{,},<EOF>''',101))

    def test_1141(self):
        self.assertTrue(TestLexer.test('''Class _5ay0{_(_,___:Array [Int ,34];A_,_0101_,o,vD,_D1:Array [Array [Float ,0XD_B9],0x4]){}Var d_:Array [Array [Array [String ,017],0xD4],0X9_B_C];Destructor (){} }''','''Class,_5ay0,{,_,(,_,,,___,:,Array,[,Int,,,34,],;,A_,,,_0101_,,,o,,,vD,,,_D1,:,Array,[,Array,[,Float,,,0XDB9,],,,0x4,],),{,},Var,d_,:,Array,[,Array,[,Array,[,String,,,017,],,,0xD4,],,,0X9BC,],;,Destructor,(,),{,},},<EOF>''',101))

    def test_1142(self):
        self.assertTrue(TestLexer.test('''Class _:u{Destructor (){}_C(_7,_,pd_N8_:Array [Int ,0X8];f_:Int ;O,E:Array [Array [Array [Float ,05],042],4_6]){}Var $9_,$s,dA_,LT:Array [Float ,0x53];}Class t_:r{$WI(f:I6d_;E_s96,m,X,_,h,_:String ){} }Class T_{Destructor (){} }''','''Class,_,:,u,{,Destructor,(,),{,},_C,(,_7,,,_,,,pd_N8_,:,Array,[,Int,,,0X8,],;,f_,:,Int,;,O,,,E,:,Array,[,Array,[,Array,[,Float,,,05,],,,042,],,,46,],),{,},Var,$9_,,,$s,,,dA_,,,LT,:,Array,[,Float,,,0x53,],;,},Class,t_,:,r,{,$WI,(,f,:,I6d_,;,E_s96,,,m,,,X,,,_,,,h,,,_,:,String,),{,},},Class,T_,{,Destructor,(,),{,},},<EOF>''',101))

    def test_1143(self):
        self.assertTrue(TestLexer.test('''Class j21{}Class ____:i{Var _b,$_6S:ME_R_Ee__;Var _,$7F:Array [Array [Array [String ,0705_3],72],0x27];}Class __{Val $_:Array [Boolean ,63];}''','''Class,j21,{,},Class,____,:,i,{,Var,_b,,,$_6S,:,ME_R_Ee__,;,Var,_,,,$7F,:,Array,[,Array,[,Array,[,String,,,07053,],,,72,],,,0x27,],;,},Class,__,{,Val,$_,:,Array,[,Boolean,,,63,],;,},<EOF>''',101))

    def test_1144(self):
        self.assertTrue(TestLexer.test('''Class _{}Class k{Constructor (_,__z,C,_N_:Boolean ){Val _:Array [Array [Array [String ,89],0B101000],0B1];}Constructor (w,Z_,_,_xx,D__L,_w_g9079,_F1:Array [Float ,070];r:Pp;x_:Array [Boolean ,070];_,_,__C:Array [Boolean ,0x8F];q:nx){Return ;}Val _:_;_n74(){} }''','''Class,_,{,},Class,k,{,Constructor,(,_,,,__z,,,C,,,_N_,:,Boolean,),{,Val,_,:,Array,[,Array,[,Array,[,String,,,89,],,,0B101000,],,,0B1,],;,},Constructor,(,w,,,Z_,,,_,,,_xx,,,D__L,,,_w_g9079,,,_F1,:,Array,[,Float,,,070,],;,r,:,Pp,;,x_,:,Array,[,Boolean,,,070,],;,_,,,_,,,__C,:,Array,[,Boolean,,,0x8F,],;,q,:,nx,),{,Return,;,},Val,_,:,_,;,_n74,(,),{,},},<EOF>''',101))

    def test_1145(self):
        self.assertTrue(TestLexer.test('''Class _:_71_{Constructor (_,_,_so9:_){Continue ;} }Class _:_o{j(_2:cm;o:__;_,_:_Y;_:Array [Boolean ,0X6_D_C_F]){ {} }}''','''Class,_,:,_71_,{,Constructor,(,_,,,_,,,_so9,:,_,),{,Continue,;,},},Class,_,:,_o,{,j,(,_2,:,cm,;,o,:,__,;,_,,,_,:,_Y,;,_,:,Array,[,Boolean,,,0X6DCF,],),{,{,},},},<EOF>''',101))

    def test_1146(self):
        self.assertTrue(TestLexer.test('''Class x:l{Constructor (){} }Class K{}Class _re:v{Var _:String ;Destructor (){}Var g,$A,___,_,_:Array [Boolean ,0X3];}''','''Class,x,:,l,{,Constructor,(,),{,},},Class,K,{,},Class,_re,:,v,{,Var,_,:,String,;,Destructor,(,),{,},Var,g,,,$A,,,___,,,_,,,_,:,Array,[,Boolean,,,0X3,],;,},<EOF>''',101))

    def test_1147(self):
        self.assertTrue(TestLexer.test('''Class zW:tCf2{}Class _d___0:_0{$__44_9D(M_21,d:Array [Array [Float ,39],0122];_a,_5:O;V,_:Int ;I6K:_){}Val $3:Float ;_(){} }''','''Class,zW,:,tCf2,{,},Class,_d___0,:,_0,{,$__44_9D,(,M_21,,,d,:,Array,[,Array,[,Float,,,39,],,,0122,],;,_a,,,_5,:,O,;,V,,,_,:,Int,;,I6K,:,_,),{,},Val,$3,:,Float,;,_,(,),{,},},<EOF>''',101))

    def test_1148(self):
        self.assertTrue(TestLexer.test('''Class _:__{}Class _H:_4_8{Destructor (){}Constructor (_8h,b,Rx,__:Array [String ,0b1];U,_v3,_,_,_,__H1:_;v,e:String ;j:M;u815:Array [Boolean ,37]){}$_(){ {}Return ;}Destructor (){} }''','''Class,_,:,__,{,},Class,_H,:,_4_8,{,Destructor,(,),{,},Constructor,(,_8h,,,b,,,Rx,,,__,:,Array,[,String,,,0b1,],;,U,,,_v3,,,_,,,_,,,_,,,__H1,:,_,;,v,,,e,:,String,;,j,:,M,;,u815,:,Array,[,Boolean,,,37,],),{,},$_,(,),{,{,},Return,;,},Destructor,(,),{,},},<EOF>''',101))

    def test_1149(self):
        self.assertTrue(TestLexer.test('''Class e{Constructor (R:String ;_,J,_8:Boolean ;_:G89E_;e,_5_,__:___;tD,__,H,D,u__,Di9:String ){} }Class Vc:_{}''','''Class,e,{,Constructor,(,R,:,String,;,_,,,J,,,_8,:,Boolean,;,_,:,G89E_,;,e,,,_5_,,,__,:,___,;,tD,,,__,,,H,,,D,,,u__,,,Di9,:,String,),{,},},Class,Vc,:,_,{,},<EOF>''',101))

    def test_1150(self):
        self.assertTrue(TestLexer.test('''Class _:J{Var $_z:String ;Val $6:Array [Array [Array [Float ,0X6_D],73],0B1];Constructor (___,_:Boolean ){Return ;} }''','''Class,_,:,J,{,Var,$_z,:,String,;,Val,$6,:,Array,[,Array,[,Array,[,Float,,,0X6D,],,,73,],,,0B1,],;,Constructor,(,___,,,_,:,Boolean,),{,Return,;,},},<EOF>''',101))

    def test_1151(self):
        self.assertTrue(TestLexer.test('''Class _{Val $p:Array [Float ,44];Val $5,$Q,v:Boolean ;}Class F{}Class __{$q(IF_,l:Array [Boolean ,0B1];_e8:Int ;U:G;_:Array [Boolean ,94]){}S(uw:_){Continue ;}Var $_:Array [Array [Float ,0xA],1];}Class _X:_{}''','''Class,_,{,Val,$p,:,Array,[,Float,,,44,],;,Val,$5,,,$Q,,,v,:,Boolean,;,},Class,F,{,},Class,__,{,$q,(,IF_,,,l,:,Array,[,Boolean,,,0B1,],;,_e8,:,Int,;,U,:,G,;,_,:,Array,[,Boolean,,,94,],),{,},S,(,uw,:,_,),{,Continue,;,},Var,$_,:,Array,[,Array,[,Float,,,0xA,],,,1,],;,},Class,_X,:,_,{,},<EOF>''',101))

    def test_1152(self):
        self.assertTrue(TestLexer.test('''Class J:_{Val $S_0,$6B__6x:_3;}Class _:p{Val _,$5,o,i7:__3_;Destructor (){} }Class Y:_{}Class _ZW{Var $a:Float ;}''','''Class,J,:,_,{,Val,$S_0,,,$6B__6x,:,_3,;,},Class,_,:,p,{,Val,_,,,$5,,,o,,,i7,:,__3_,;,Destructor,(,),{,},},Class,Y,:,_,{,},Class,_ZW,{,Var,$a,:,Float,;,},<EOF>''',101))

    def test_1153(self):
        self.assertTrue(TestLexer.test('''Class g__:x{$J(_,_,__dNE:Array [Array [Array [Int ,03],8],0116];_:Int ){Break ;} }Class _0w{Var $_,xd_,vA2,$3__7:String ;Val _:v;Val _6,$3:Array [Array [Array [Array [Int ,0X76_95_5],2],5],05];}''','''Class,g__,:,x,{,$J,(,_,,,_,,,__dNE,:,Array,[,Array,[,Array,[,Int,,,03,],,,8,],,,0116,],;,_,:,Int,),{,Break,;,},},Class,_0w,{,Var,$_,,,xd_,,,vA2,,,$3__7,:,String,;,Val,_,:,v,;,Val,_6,,,$3,:,Array,[,Array,[,Array,[,Array,[,Int,,,0X76955,],,,2,],,,5,],,,05,],;,},<EOF>''',101))

    def test_1154(self):
        self.assertTrue(TestLexer.test('''Class _4Wb4:t{Constructor (){} }Class M_2_{Destructor (){Break ;Continue ;} }Class s:fF_Y{__(){}Var $C:Array [Array [Array [Boolean ,041],0B11],05];Destructor (){} }''','''Class,_4Wb4,:,t,{,Constructor,(,),{,},},Class,M_2_,{,Destructor,(,),{,Break,;,Continue,;,},},Class,s,:,fF_Y,{,__,(,),{,},Var,$C,:,Array,[,Array,[,Array,[,Boolean,,,041,],,,0B11,],,,05,],;,Destructor,(,),{,},},<EOF>''',101))

    def test_1155(self):
        self.assertTrue(TestLexer.test('''Class P_:__v{Var $_,o__:_;q(_Z1,F6,_,s___,H:p){}Val $4_:Boolean ;}Class h{Constructor (n,_01Ew:Array [Int ,016];__3_:Array [Array [Float ,0x3D],3];_,m:Int ;t:Array [String ,0xE];_PW_:Int ){}Constructor (Z,__:k;oq:Boolean ;rL:Int ;L____0,F:_FuF){} }''','''Class,P_,:,__v,{,Var,$_,,,o__,:,_,;,q,(,_Z1,,,F6,,,_,,,s___,,,H,:,p,),{,},Val,$4_,:,Boolean,;,},Class,h,{,Constructor,(,n,,,_01Ew,:,Array,[,Int,,,016,],;,__3_,:,Array,[,Array,[,Float,,,0x3D,],,,3,],;,_,,,m,:,Int,;,t,:,Array,[,String,,,0xE,],;,_PW_,:,Int,),{,},Constructor,(,Z,,,__,:,k,;,oq,:,Boolean,;,rL,:,Int,;,L____0,,,F,:,_FuF,),{,},},<EOF>''',101))

    def test_1156(self):
        self.assertTrue(TestLexer.test('''Class _:c_i{Destructor (){}Constructor (_,D_0:Array [Array [Array [Array [Array [Int ,030],0B11001],030],0B11001],0xD];A_:String ){}$V(){} }''','''Class,_,:,c_i,{,Destructor,(,),{,},Constructor,(,_,,,D_0,:,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,030,],,,0B11001,],,,030,],,,0B11001,],,,0xD,],;,A_,:,String,),{,},$V,(,),{,},},<EOF>''',101))

    def test_1157(self):
        self.assertTrue(TestLexer.test('''Class _S:q{Val eR95,Fb,_,$s_,$1:Array [Array [Array [String ,04_3],0b1001111],02];Constructor (l__9:String ){Return ;}__(){}Val _,$_y,$FN,_3,$p:_;}''','''Class,_S,:,q,{,Val,eR95,,,Fb,,,_,,,$s_,,,$1,:,Array,[,Array,[,Array,[,String,,,043,],,,0b1001111,],,,02,],;,Constructor,(,l__9,:,String,),{,Return,;,},__,(,),{,},Val,_,,,$_y,,,$FN,,,_3,,,$p,:,_,;,},<EOF>''',101))

    def test_1158(self):
        self.assertTrue(TestLexer.test('''Class n:N{$9_9_0_(){Break ;} }Class n{Constructor (s:Boolean ;X,__,v_:a;E4:Array [Array [Boolean ,94],0x5F];L:Boolean ){Continue ;} }Class _UF_j{Val _0,$o_,_:Ht79;Var X9,N,_,H:Array [Array [Array [Boolean ,6],0B110010],06_5];$t7(){}Destructor (){} }''','''Class,n,:,N,{,$9_9_0_,(,),{,Break,;,},},Class,n,{,Constructor,(,s,:,Boolean,;,X,,,__,,,v_,:,a,;,E4,:,Array,[,Array,[,Boolean,,,94,],,,0x5F,],;,L,:,Boolean,),{,Continue,;,},},Class,_UF_j,{,Val,_0,,,$o_,,,_,:,Ht79,;,Var,X9,,,N,,,_,,,H,:,Array,[,Array,[,Array,[,Boolean,,,6,],,,0B110010,],,,065,],;,$t7,(,),{,},Destructor,(,),{,},},<EOF>''',101))

    def test_1159(self):
        self.assertTrue(TestLexer.test('''Class w:zZ__{}Class X2_2e:_EE__{Val ku,_,_5,_YC,_,$4K0,$_9,m1Wi3:Float ;Val $_,$w,$R,$_0:Array [String ,040];}''','''Class,w,:,zZ__,{,},Class,X2_2e,:,_EE__,{,Val,ku,,,_,,,_5,,,_YC,,,_,,,$4K0,,,$_9,,,m1Wi3,:,Float,;,Val,$_,,,$w,,,$R,,,$_0,:,Array,[,String,,,040,],;,},<EOF>''',101))

    def test_1160(self):
        self.assertTrue(TestLexer.test('''Class _jm:_{Val $2:_;Val $7:Array [String ,0b10];Constructor (jR:Array [Array [String ,01_2_72],0b10];u:Float ){} }''','''Class,_jm,:,_,{,Val,$2,:,_,;,Val,$7,:,Array,[,String,,,0b10,],;,Constructor,(,jR,:,Array,[,Array,[,String,,,01272,],,,0b10,],;,u,:,Float,),{,},},<EOF>''',101))

    def test_1161(self):
        self.assertTrue(TestLexer.test('''Class _:p{__3(NM:l2;_12_:Int ){} }Class Z{Val $N,_94nP0P:_6__7;_(q__:J;C:Array [Array [Boolean ,063],67];oj6,__:Int ;_10,_,Y_3Z,_:_){} }Class E{}''','''Class,_,:,p,{,__3,(,NM,:,l2,;,_12_,:,Int,),{,},},Class,Z,{,Val,$N,,,_94nP0P,:,_6__7,;,_,(,q__,:,J,;,C,:,Array,[,Array,[,Boolean,,,063,],,,67,],;,oj6,,,__,:,Int,;,_10,,,_,,,Y_3Z,,,_,:,_,),{,},},Class,E,{,},<EOF>''',101))

    def test_1162(self):
        self.assertTrue(TestLexer.test('''Class NR:D48{Destructor (){_::$5._();Var ___,_,__,_R5_:Array [Array [Array [Boolean ,0b1],0B1_0_11],0B1100000];}Val T,$_:String ;}Class _:_{Destructor (){}Val $4,$13,$p:Array [Array [Array [Array [Float ,0B11],0B1100000],0X6],6_7];}Class _4:X_{}Class K:_{Constructor (){}Constructor (){}Val _:String ;}''','''Class,NR,:,D48,{,Destructor,(,),{,_,::,$5,.,_,(,),;,Var,___,,,_,,,__,,,_R5_,:,Array,[,Array,[,Array,[,Boolean,,,0b1,],,,0B1011,],,,0B1100000,],;,},Val,T,,,$_,:,String,;,},Class,_,:,_,{,Destructor,(,),{,},Val,$4,,,$13,,,$p,:,Array,[,Array,[,Array,[,Array,[,Float,,,0B11,],,,0B1100000,],,,0X6,],,,67,],;,},Class,_4,:,X_,{,},Class,K,:,_,{,Constructor,(,),{,},Constructor,(,),{,},Val,_,:,String,;,},<EOF>''',101))

    def test_1163(self):
        self.assertTrue(TestLexer.test('''Class _:__{_ez7__1(_:Array [Array [Array [Array [Array [Array [Array [Array [Array [Array [Int ,2],015],077],0b1111],2],0X63],0XC],2],2],077];_,_:eM_i;Q,_,B:_5__;__,n_:_;M9:_;_5T_O,t7099_B5:Int ){} }''','''Class,_,:,__,{,_ez7__1,(,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,2,],,,015,],,,077,],,,0b1111,],,,2,],,,0X63,],,,0XC,],,,2,],,,2,],,,077,],;,_,,,_,:,eM_i,;,Q,,,_,,,B,:,_5__,;,__,,,n_,:,_,;,M9,:,_,;,_5T_O,,,t7099_B5,:,Int,),{,},},<EOF>''',101))

    def test_1164(self):
        self.assertTrue(TestLexer.test('''Class q{Constructor (k7,K4_,y:Array [Array [Array [Int ,8_1],0X2A],016];v:Array [Boolean ,0x5F];V_,_,_,f:Boolean ;F_:Array [Float ,06_05]){} }''','''Class,q,{,Constructor,(,k7,,,K4_,,,y,:,Array,[,Array,[,Array,[,Int,,,81,],,,0X2A,],,,016,],;,v,:,Array,[,Boolean,,,0x5F,],;,V_,,,_,,,_,,,f,:,Boolean,;,F_,:,Array,[,Float,,,0605,],),{,},},<EOF>''',101))

    def test_1165(self):
        self.assertTrue(TestLexer.test('''Class E{Constructor (){}Destructor (){}Val n:Array [Array [Int ,0b1],010];_5(c:Array [Array [Array [Int ,061],0B100100],84];_7:Array [String ,010];_15,__59p73:Array [Float ,02];A_1:H){} }''','''Class,E,{,Constructor,(,),{,},Destructor,(,),{,},Val,n,:,Array,[,Array,[,Int,,,0b1,],,,010,],;,_5,(,c,:,Array,[,Array,[,Array,[,Int,,,061,],,,0B100100,],,,84,],;,_7,:,Array,[,String,,,010,],;,_15,,,__59p73,:,Array,[,Float,,,02,],;,A_1,:,H,),{,},},<EOF>''',101))

    def test_1166(self):
        self.assertTrue(TestLexer.test('''Class Nq5{Destructor (){} }Class M{}Class I{Constructor (_,S1:Array [Float ,0B10001];_1a_1,_,G5J:Float ){} }Class __y1{}Class _2:__{}''','''Class,Nq5,{,Destructor,(,),{,},},Class,M,{,},Class,I,{,Constructor,(,_,,,S1,:,Array,[,Float,,,0B10001,],;,_1a_1,,,_,,,G5J,:,Float,),{,},},Class,__y1,{,},Class,_2,:,__,{,},<EOF>''',101))

    def test_1167(self):
        self.assertTrue(TestLexer.test('''Class _S{Constructor (_:Array [Array [Array [Array [Float ,0b1011001],0134],1_55],040_3]){}Constructor (e,I:Array [String ,64];_B__,W_,_,_:Int ;o:Array [Int ,0134];_:K_r;z,_1_:_B;_J33,nk:Array [Array [Array [Array [Int ,64],0b1_1],05_3],64];j,_:Array [Array [Array [Array [Array [Boolean ,0xA],05],8091],07],5];_1_4l0,_,_j:P){} }''','''Class,_S,{,Constructor,(,_,:,Array,[,Array,[,Array,[,Array,[,Float,,,0b1011001,],,,0134,],,,155,],,,0403,],),{,},Constructor,(,e,,,I,:,Array,[,String,,,64,],;,_B__,,,W_,,,_,,,_,:,Int,;,o,:,Array,[,Int,,,0134,],;,_,:,K_r,;,z,,,_1_,:,_B,;,_J33,,,nk,:,Array,[,Array,[,Array,[,Array,[,Int,,,64,],,,0b11,],,,053,],,,64,],;,j,,,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0xA,],,,05,],,,8091,],,,07,],,,5,],;,_1_4l0,,,_,,,_j,:,P,),{,},},<EOF>''',101))

    def test_1168(self):
        self.assertTrue(TestLexer.test('''Class _:_7_{$_(){}Constructor (_6m___:_;_:Array [Int ,9];__odt_,_:Int ){} }Class _9:_a1{Destructor (){} }Class _1:y{Constructor (){} }''','''Class,_,:,_7_,{,$_,(,),{,},Constructor,(,_6m___,:,_,;,_,:,Array,[,Int,,,9,],;,__odt_,,,_,:,Int,),{,},},Class,_9,:,_a1,{,Destructor,(,),{,},},Class,_1,:,y,{,Constructor,(,),{,},},<EOF>''',101))

    def test_1169(self):
        self.assertTrue(TestLexer.test('''Class b{Constructor (S,F_,__,D4VU,_9_:Float ;h,__,A2vOU__1,q6,P9,In :Int ;xX1,cl:Int ;_,U_1M3:__;x__GO,_5gV,T:Array [Boolean ,8];_5qf:_){} }''','''Class,b,{,Constructor,(,S,,,F_,,,__,,,D4VU,,,_9_,:,Float,;,h,,,__,,,A2vOU__1,,,q6,,,P9,,,In,:,Int,;,xX1,,,cl,:,Int,;,_,,,U_1M3,:,__,;,x__GO,,,_5gV,,,T,:,Array,[,Boolean,,,8,],;,_5qf,:,_,),{,},},<EOF>''',101))

    def test_1170(self):
        self.assertTrue(TestLexer.test('''Class b:_{}Class t_{}Class _5:__D{F(T:Int ;_,M__2607:Array [Array [Array [Array [Int ,0B1_1],7_15],52],0x2A];pj_:Float ;_m:Int ;_5_w:Array [Array [Array [Array [Array [Array [Float ,0X5],0X38],0B101],0b1010100],015],57]){} }''','''Class,b,:,_,{,},Class,t_,{,},Class,_5,:,__D,{,F,(,T,:,Int,;,_,,,M__2607,:,Array,[,Array,[,Array,[,Array,[,Int,,,0B11,],,,715,],,,52,],,,0x2A,],;,pj_,:,Float,;,_m,:,Int,;,_5_w,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0X5,],,,0X38,],,,0B101,],,,0b1010100,],,,015,],,,57,],),{,},},<EOF>''',101))

    def test_1171(self):
        self.assertTrue(TestLexer.test('''Class _ot_:h{}Class qv{Constructor (_:A9){Var x1,B7m:L;}R(K7L0:Float ;_K,q_00:Float ){}Var wUm2Y1:__;Constructor (Q,XV,VM,_h_:_;_,C18___l:Array [Float ,040]){Continue ;} }Class q:j{}''','''Class,_ot_,:,h,{,},Class,qv,{,Constructor,(,_,:,A9,),{,Var,x1,,,B7m,:,L,;,},R,(,K7L0,:,Float,;,_K,,,q_00,:,Float,),{,},Var,wUm2Y1,:,__,;,Constructor,(,Q,,,XV,,,VM,,,_h_,:,_,;,_,,,C18___l,:,Array,[,Float,,,040,],),{,Continue,;,},},Class,q,:,j,{,},<EOF>''',101))

    def test_1172(self):
        self.assertTrue(TestLexer.test('''Class g479_{}Class _:l4V_{Val $9:Array [Boolean ,86];Constructor (){Break ;}Constructor (Wi_:__;__:Array [Array [String ,0140],0X877];_,__:Int ;n,H__,_C_,_1,__:Array [Array [Int ,0B1],0140]){}Constructor (d7:_;_q:Float ){} }''','''Class,g479_,{,},Class,_,:,l4V_,{,Val,$9,:,Array,[,Boolean,,,86,],;,Constructor,(,),{,Break,;,},Constructor,(,Wi_,:,__,;,__,:,Array,[,Array,[,String,,,0140,],,,0X877,],;,_,,,__,:,Int,;,n,,,H__,,,_C_,,,_1,,,__,:,Array,[,Array,[,Int,,,0B1,],,,0140,],),{,},Constructor,(,d7,:,_,;,_q,:,Float,),{,},},<EOF>''',101))

    def test_1173(self):
        self.assertTrue(TestLexer.test('''Class _:ZZ{Constructor (l:Array [Array [Array [Int ,53],0xC],0X99];z_,_,zQN:Float ;_:Boolean ;_1:B;K,U_:Array [String ,0B1_1];O:__){Continue ;}Destructor (){} }Class d:R2{}''','''Class,_,:,ZZ,{,Constructor,(,l,:,Array,[,Array,[,Array,[,Int,,,53,],,,0xC,],,,0X99,],;,z_,,,_,,,zQN,:,Float,;,_,:,Boolean,;,_1,:,B,;,K,,,U_,:,Array,[,String,,,0B11,],;,O,:,__,),{,Continue,;,},Destructor,(,),{,},},Class,d,:,R2,{,},<EOF>''',101))

    def test_1174(self):
        self.assertTrue(TestLexer.test('''Class H5{Constructor (){} }Class _:qsK{Var $C:Array [Array [Boolean ,3],0B1];Destructor (){ {} }_(_1,_,A,zy,o__,_K,_:_){} }Class _{}''','''Class,H5,{,Constructor,(,),{,},},Class,_,:,qsK,{,Var,$C,:,Array,[,Array,[,Boolean,,,3,],,,0B1,],;,Destructor,(,),{,{,},},_,(,_1,,,_,,,A,,,zy,,,o__,,,_K,,,_,:,_,),{,},},Class,_,{,},<EOF>''',101))

    def test_1175(self):
        self.assertTrue(TestLexer.test('''Class _u{Destructor (){} }Class _h25{w_(_4,r5E_9__4,_2o,_9__jb,D7,__:Int ;_:Boolean ;__:_){}Constructor (){} }Class QSN_:__9{}''','''Class,_u,{,Destructor,(,),{,},},Class,_h25,{,w_,(,_4,,,r5E_9__4,,,_2o,,,_9__jb,,,D7,,,__,:,Int,;,_,:,Boolean,;,__,:,_,),{,},Constructor,(,),{,},},Class,QSN_,:,__9,{,},<EOF>''',101))

    def test_1176(self):
        self.assertTrue(TestLexer.test('''Class __{Var _3__h:_;wv(_2_,Sb,j521n8U:Array [Array [Array [Array [String ,0X23],0115],0X23],0x2F];_:m4Y){}Val $1U,$_9,$9:A;}Class _{}Class y:__{}''','''Class,__,{,Var,_3__h,:,_,;,wv,(,_2_,,,Sb,,,j521n8U,:,Array,[,Array,[,Array,[,Array,[,String,,,0X23,],,,0115,],,,0X23,],,,0x2F,],;,_,:,m4Y,),{,},Val,$1U,,,$_9,,,$9,:,A,;,},Class,_,{,},Class,y,:,__,{,},<EOF>''',101))

    def test_1177(self):
        self.assertTrue(TestLexer.test('''Class _{}Class _{}Class F{Constructor (){} }Class _0:_{Constructor (b:_y6U;_:Array [Array [Float ,0x23],011]){p_::$g();} }''','''Class,_,{,},Class,_,{,},Class,F,{,Constructor,(,),{,},},Class,_0,:,_,{,Constructor,(,b,:,_y6U,;,_,:,Array,[,Array,[,Float,,,0x23,],,,011,],),{,p_,::,$g,(,),;,},},<EOF>''',101))

    def test_1178(self):
        self.assertTrue(TestLexer.test('''Class S3_{Val $4_,A6_:Array [Boolean ,0132];}Class _98U_H7_6{Var $4Er,$__I_,_,i85O,$R8_97,_,N:Array [Int ,0B11];}Class O_:rD{u(){} }Class g_C6{}''','''Class,S3_,{,Val,$4_,,,A6_,:,Array,[,Boolean,,,0132,],;,},Class,_98U_H7_6,{,Var,$4Er,,,$__I_,,,_,,,i85O,,,$R8_97,,,_,,,N,:,Array,[,Int,,,0B11,],;,},Class,O_,:,rD,{,u,(,),{,},},Class,g_C6,{,},<EOF>''',101))

    def test_1179(self):
        self.assertTrue(TestLexer.test('''Class _{_(c3,_:Boolean ;J:_n__2;_B,cD4M:_;_,b8,s,Yz:_){ {} }Constructor (_l,_,_,__TF8,w,v:Array [String ,06]){} }Class v_{Val w,_:Array [Array [Int ,05],0X55];}Class J__:_{}Class _:_{Constructor (){} }''','''Class,_,{,_,(,c3,,,_,:,Boolean,;,J,:,_n__2,;,_B,,,cD4M,:,_,;,_,,,b8,,,s,,,Yz,:,_,),{,{,},},Constructor,(,_l,,,_,,,_,,,__TF8,,,w,,,v,:,Array,[,String,,,06,],),{,},},Class,v_,{,Val,w,,,_,:,Array,[,Array,[,Int,,,05,],,,0X55,],;,},Class,J__,:,_,{,},Class,_,:,_,{,Constructor,(,),{,},},<EOF>''',101))

    def test_1180(self):
        self.assertTrue(TestLexer.test('''Class Zsl:_{Destructor (){}Var $S:Array [Array [Int ,0XB],5_9];}Class U{$_(_:Array [String ,0x3];_,__,__6:Int ;s,_,__,_6njY_e7_,__:_E;e_ee6r:Int ){} }''','''Class,Zsl,:,_,{,Destructor,(,),{,},Var,$S,:,Array,[,Array,[,Int,,,0XB,],,,59,],;,},Class,U,{,$_,(,_,:,Array,[,String,,,0x3,],;,_,,,__,,,__6,:,Int,;,s,,,_,,,__,,,_6njY_e7_,,,__,:,_E,;,e_ee6r,:,Int,),{,},},<EOF>''',101))

    def test_1181(self):
        self.assertTrue(TestLexer.test('''Class C{Val $_g:Array [Boolean ,0x50];Constructor (_,_w,l__,N:Int ;dU2,V_:k_uJ9;e,k8_5pqu:Boolean ){}$2g(){} }Class _2:_{w(){} }Class _vfT_D:Y__M{}''','''Class,C,{,Val,$_g,:,Array,[,Boolean,,,0x50,],;,Constructor,(,_,,,_w,,,l__,,,N,:,Int,;,dU2,,,V_,:,k_uJ9,;,e,,,k8_5pqu,:,Boolean,),{,},$2g,(,),{,},},Class,_2,:,_,{,w,(,),{,},},Class,_vfT_D,:,Y__M,{,},<EOF>''',101))

    def test_1182(self):
        self.assertTrue(TestLexer.test('''Class a_{}Class S8J08_{}Class L7{Var $47:Array [Array [Float ,0b11],05];}Class _:_L{Val $_k:Array [Int ,0B1100011];Val $r_5F,$C_O:E2_5;Val _2:Array [String ,0x7];Var A6_I,_,_,_883:Array [Int ,0B1];$_3_(_:String ;yY,_:Boolean ){} }''','''Class,a_,{,},Class,S8J08_,{,},Class,L7,{,Var,$47,:,Array,[,Array,[,Float,,,0b11,],,,05,],;,},Class,_,:,_L,{,Val,$_k,:,Array,[,Int,,,0B1100011,],;,Val,$r_5F,,,$C_O,:,E2_5,;,Val,_2,:,Array,[,String,,,0x7,],;,Var,A6_I,,,_,,,_,,,_883,:,Array,[,Int,,,0B1,],;,$_3_,(,_,:,String,;,yY,,,_,:,Boolean,),{,},},<EOF>''',101))

    def test_1183(self):
        self.assertTrue(TestLexer.test('''Class I_{O_(){} }Class _61:f228{}Class _{Constructor (B2,e,_8:Array [Array [Array [Array [Int ,0b11],0112],0X16],0B10_0];O5:Array [Array [String ,0B1100100],0112];p,s_,_:Array [Float ,0112]){} }Class u{Val _3,$_:X;}''','''Class,I_,{,O_,(,),{,},},Class,_61,:,f228,{,},Class,_,{,Constructor,(,B2,,,e,,,_8,:,Array,[,Array,[,Array,[,Array,[,Int,,,0b11,],,,0112,],,,0X16,],,,0B100,],;,O5,:,Array,[,Array,[,String,,,0B1100100,],,,0112,],;,p,,,s_,,,_,:,Array,[,Float,,,0112,],),{,},},Class,u,{,Val,_3,,,$_,:,X,;,},<EOF>''',101))

    def test_1184(self):
        self.assertTrue(TestLexer.test('''Class zp__{Var $T7,$_Fh_,Z,FHQ,$U,u,_:__;Constructor (_:Array [Array [Array [Float ,0b101010],52],03];_,c7,_H,j,_:Array [Array [Int ,01],041];_d,W,m,LN:Float ;O:Array [Float ,0b101010]){} }''','''Class,zp__,{,Var,$T7,,,$_Fh_,,,Z,,,FHQ,,,$U,,,u,,,_,:,__,;,Constructor,(,_,:,Array,[,Array,[,Array,[,Float,,,0b101010,],,,52,],,,03,],;,_,,,c7,,,_H,,,j,,,_,:,Array,[,Array,[,Int,,,01,],,,041,],;,_d,,,W,,,m,,,LN,:,Float,;,O,:,Array,[,Float,,,0b101010,],),{,},},<EOF>''',101))

    def test_1185(self):
        self.assertTrue(TestLexer.test('''Class Gl{}Class or{$__(_0,t:Float ;_t,_,_,_:s_4;_:_i;E1:Array [Array [Float ,5],5];___B_ya1:Array [Float ,06];z:ug){} }Class _2_V68:N{Val _:String ;}''','''Class,Gl,{,},Class,or,{,$__,(,_0,,,t,:,Float,;,_t,,,_,,,_,,,_,:,s_4,;,_,:,_i,;,E1,:,Array,[,Array,[,Float,,,5,],,,5,],;,___B_ya1,:,Array,[,Float,,,06,],;,z,:,ug,),{,},},Class,_2_V68,:,N,{,Val,_,:,String,;,},<EOF>''',101))

    def test_1186(self):
        self.assertTrue(TestLexer.test('''Class _43:_{}Class q:_{Constructor (_2:Int ){} }Class Np:e7{_(W:Array [Array [Boolean ,0x5_5],04]){Continue ;} }Class j2:j{Destructor (){ {} }}''','''Class,_43,:,_,{,},Class,q,:,_,{,Constructor,(,_2,:,Int,),{,},},Class,Np,:,e7,{,_,(,W,:,Array,[,Array,[,Boolean,,,0x55,],,,04,],),{,Continue,;,},},Class,j2,:,j,{,Destructor,(,),{,{,},},},<EOF>''',101))

    def test_1187(self):
        self.assertTrue(TestLexer.test('''Class w:_A{Val ov,_29:Int ;}Class __26{Val _,x,P,$0_b___8,$__:Array [Int ,0B110101];Constructor (){ {Continue ;}Z96u::$_._();} }''','''Class,w,:,_A,{,Val,ov,,,_29,:,Int,;,},Class,__26,{,Val,_,,,x,,,P,,,$0_b___8,,,$__,:,Array,[,Int,,,0B110101,],;,Constructor,(,),{,{,Continue,;,},Z96u,::,$_,.,_,(,),;,},},<EOF>''',101))

    def test_1188(self):
        self.assertTrue(TestLexer.test('''Class _6_{Constructor (_,_N,i,_D_0:_;P61k:Array [Array [String ,0b11_1_1_0_1],0b111010];_t:Array [String ,0b111010];m2rB_:Boolean ){} }''','''Class,_6_,{,Constructor,(,_,,,_N,,,i,,,_D_0,:,_,;,P61k,:,Array,[,Array,[,String,,,0b111101,],,,0b111010,],;,_t,:,Array,[,String,,,0b111010,],;,m2rB_,:,Boolean,),{,},},<EOF>''',101))

    def test_1189(self):
        self.assertTrue(TestLexer.test('''Class N{$7(){Continue ;}Constructor (){}Constructor (b:Array [Array [Array [Array [Array [Array [String ,0X2C],4],047],5_3],0b1010101],3];_:Float ;I,_,H,_:___73360xE){} }''','''Class,N,{,$7,(,),{,Continue,;,},Constructor,(,),{,},Constructor,(,b,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0X2C,],,,4,],,,047,],,,53,],,,0b1010101,],,,3,],;,_,:,Float,;,I,,,_,,,H,,,_,:,___73360xE,),{,},},<EOF>''',101))

    def test_1190(self):
        self.assertTrue(TestLexer.test('''Class Z6{Destructor (){Continue ;} }Class b6_:_8{Destructor (){Break ;}Val $_:Array [Array [Int ,8],0143]=--_::$2.A_01a;Destructor (){} }''','''Class,Z6,{,Destructor,(,),{,Continue,;,},},Class,b6_,:,_8,{,Destructor,(,),{,Break,;,},Val,$_,:,Array,[,Array,[,Int,,,8,],,,0143,],=,-,-,_,::,$2,.,A_01a,;,Destructor,(,),{,},},<EOF>''',101))

    def test_1191(self):
        self.assertTrue(TestLexer.test('''Class _{Val N,$96e:Array [String ,3];Val a,_:Array [Float ,0xA];}Class ___:i{}Class u{}Class __:S7N_Z{_k_6__0W(E,B:__;_:Array [Boolean ,0X47];did,_C:__){} }Class _B{}''','''Class,_,{,Val,N,,,$96e,:,Array,[,String,,,3,],;,Val,a,,,_,:,Array,[,Float,,,0xA,],;,},Class,___,:,i,{,},Class,u,{,},Class,__,:,S7N_Z,{,_k_6__0W,(,E,,,B,:,__,;,_,:,Array,[,Boolean,,,0X47,],;,did,,,_C,:,__,),{,},},Class,_B,{,},<EOF>''',101))

    def test_1192(self):
        self.assertTrue(TestLexer.test('''Class A{Constructor (){Continue ;Break ;} }Class _0{}Class K_:_{Var $b,_9_7I:Array [Float ,0x1];}Class _81:_{Destructor (){} }''','''Class,A,{,Constructor,(,),{,Continue,;,Break,;,},},Class,_0,{,},Class,K_,:,_,{,Var,$b,,,_9_7I,:,Array,[,Float,,,0x1,],;,},Class,_81,:,_,{,Destructor,(,),{,},},<EOF>''',101))

    def test_1193(self):
        self.assertTrue(TestLexer.test('''Class __2:_{$B(_n:Array [Array [Array [Int ,0b1_1],06],0X63]){Continue ;Break ;Break ;{} }}Class _:_{$___(V6_:Array [Array [Boolean ,7],3]){} }Class W__:_96{Var $__y7,_,__,LVs:Array [Int ,07_6];Val v6M:Array [String ,03];}Class _:L{f(_1__:Float ){}$M(){} }Class _:_H2_245{Destructor (){}Var $S_,$8,$P,$t85_:String ;Constructor (){Continue ;} }Class _:_{}''','''Class,__2,:,_,{,$B,(,_n,:,Array,[,Array,[,Array,[,Int,,,0b11,],,,06,],,,0X63,],),{,Continue,;,Break,;,Break,;,{,},},},Class,_,:,_,{,$___,(,V6_,:,Array,[,Array,[,Boolean,,,7,],,,3,],),{,},},Class,W__,:,_96,{,Var,$__y7,,,_,,,__,,,LVs,:,Array,[,Int,,,076,],;,Val,v6M,:,Array,[,String,,,03,],;,},Class,_,:,L,{,f,(,_1__,:,Float,),{,},$M,(,),{,},},Class,_,:,_H2_245,{,Destructor,(,),{,},Var,$S_,,,$8,,,$P,,,$t85_,:,String,;,Constructor,(,),{,Continue,;,},},Class,_,:,_,{,},<EOF>''',101))

    def test_1194(self):
        self.assertTrue(TestLexer.test('''Class M0_:cd_sgx{Var $_,$_iy,$42___,$4h7,_9,$_:Array [Array [Array [Float ,8],0x64],0x64];Destructor (){} }Class _{Val t3_,R,J:Array [Array [String ,0b1],72];v_(_:_r;_:Int ;NYd7:J;_t:Array [Array [String ,6],0X4];q:Array [Array [Array [Array [Boolean ,0x503_660],0xD],0b111100],0x64]){} }''','''Class,M0_,:,cd_sgx,{,Var,$_,,,$_iy,,,$42___,,,$4h7,,,_9,,,$_,:,Array,[,Array,[,Array,[,Float,,,8,],,,0x64,],,,0x64,],;,Destructor,(,),{,},},Class,_,{,Val,t3_,,,R,,,J,:,Array,[,Array,[,String,,,0b1,],,,72,],;,v_,(,_,:,_r,;,_,:,Int,;,NYd7,:,J,;,_t,:,Array,[,Array,[,String,,,6,],,,0X4,],;,q,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,0x503660,],,,0xD,],,,0b111100,],,,0x64,],),{,},},<EOF>''',101))

    def test_1195(self):
        self.assertTrue(TestLexer.test('''Class _:F{Var $_q_,_b9:Float ;Var _:_15_;Constructor (SD,H,o,_71L__T_,O,___5,_,_,_:Array [Array [String ,0X7],0134];e9,_,P:L6;_:Int ;P,_,_u_,__T__:Float ;_zX,_G,I,V:Boolean ;D,_99:Float ;B_,__:Array [Int ,30]){} }Class _{}''','''Class,_,:,F,{,Var,$_q_,,,_b9,:,Float,;,Var,_,:,_15_,;,Constructor,(,SD,,,H,,,o,,,_71L__T_,,,O,,,___5,,,_,,,_,,,_,:,Array,[,Array,[,String,,,0X7,],,,0134,],;,e9,,,_,,,P,:,L6,;,_,:,Int,;,P,,,_,,,_u_,,,__T__,:,Float,;,_zX,,,_G,,,I,,,V,:,Boolean,;,D,,,_99,:,Float,;,B_,,,__,:,Array,[,Int,,,30,],),{,},},Class,_,{,},<EOF>''',101))

    def test_1196(self):
        self.assertTrue(TestLexer.test('''Class _:_V{Val _g,b:Array [Array [String ,034],034];Constructor (m:Array [Array [Boolean ,0X26],0XD2];__,_:Array [Float ,06_1]){Continue ;}Var p,$6N_3W_,$17,d3l5,_k,$72Cx_r_:Array [Float ,05_05];_(U1ajg,__,Y:Array [Array [Array [Array [Float ,05],5_7],0b1000011],0xF90];c:Array [Array [String ,034],3];j,_,r,_:Array [Array [Array [Array [Array [Array [Boolean ,8],0b1000011],8],0X4],8],0b1000011];i,_:Float ;M,_:Array [Float ,8_90_0]){} }Class a{}''','''Class,_,:,_V,{,Val,_g,,,b,:,Array,[,Array,[,String,,,034,],,,034,],;,Constructor,(,m,:,Array,[,Array,[,Boolean,,,0X26,],,,0XD2,],;,__,,,_,:,Array,[,Float,,,061,],),{,Continue,;,},Var,p,,,$6N_3W_,,,$17,,,d3l5,,,_k,,,$72Cx_r_,:,Array,[,Float,,,0505,],;,_,(,U1ajg,,,__,,,Y,:,Array,[,Array,[,Array,[,Array,[,Float,,,05,],,,57,],,,0b1000011,],,,0xF90,],;,c,:,Array,[,Array,[,String,,,034,],,,3,],;,j,,,_,,,r,,,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,8,],,,0b1000011,],,,8,],,,0X4,],,,8,],,,0b1000011,],;,i,,,_,:,Float,;,M,,,_,:,Array,[,Float,,,8900,],),{,},},Class,a,{,},<EOF>''',101))

    def test_1197(self):
        self.assertTrue(TestLexer.test('''Class f:f__{}Class _d6___7{}Class _g{}Class _:_pl_{Var C:bG0_;}Class __:__{Var w1:Array [Int ,0XB_E];}Class o{}Class _ZMR{}''','''Class,f,:,f__,{,},Class,_d6___7,{,},Class,_g,{,},Class,_,:,_pl_,{,Var,C,:,bG0_,;,},Class,__,:,__,{,Var,w1,:,Array,[,Int,,,0XBE,],;,},Class,o,{,},Class,_ZMR,{,},<EOF>''',101))

    def test_1198(self):
        self.assertTrue(TestLexer.test('''Class R:b{Var __5:Array [Array [Array [Array [Boolean ,032],0x43],74],91];Var $8K8,$4,I__4x22,_:Int ;}Class _{Var __:String ;}''','''Class,R,:,b,{,Var,__5,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,032,],,,0x43,],,,74,],,,91,],;,Var,$8K8,,,$4,,,I__4x22,,,_,:,Int,;,},Class,_,{,Var,__,:,String,;,},<EOF>''',101))

    def test_1199(self):
        self.assertTrue(TestLexer.test('''Class Y:___j{}Class v{}Class ____{}Class I_eH2b{}Class s3A_76_{Constructor (){Continue ;}Val Mxl:Array [Array [Array [Boolean ,0B100000],0X2],0B1];}''','''Class,Y,:,___j,{,},Class,v,{,},Class,____,{,},Class,I_eH2b,{,},Class,s3A_76_,{,Constructor,(,),{,Continue,;,},Val,Mxl,:,Array,[,Array,[,Array,[,Boolean,,,0B100000,],,,0X2,],,,0B1,],;,},<EOF>''',101))

    def test_1200(self):
        self.assertTrue(TestLexer.test('''Class ___7:_6{Constructor (){Continue ;}Constructor (J6:Int ;V2_:Array [Boolean ,0100]){} }Class _S{}Class m4:_{}''','''Class,___7,:,_6,{,Constructor,(,),{,Continue,;,},Constructor,(,J6,:,Int,;,V2_,:,Array,[,Boolean,,,0100,],),{,},},Class,_S,{,},Class,m4,:,_,{,},<EOF>''',101))

    def test_1201(self):
        self.assertTrue(TestLexer.test('''Class j_2_r:_{Var K,ySl61_:_;Constructor (___4:Int ){} }Class _:G{}Class z2{}Class p_{Destructor (){}Constructor (){}Var $9,$_,hqMf,C:M___;}Class _O__i{Var K__:Boolean ;}''','''Class,j_2_r,:,_,{,Var,K,,,ySl61_,:,_,;,Constructor,(,___4,:,Int,),{,},},Class,_,:,G,{,},Class,z2,{,},Class,p_,{,Destructor,(,),{,},Constructor,(,),{,},Var,$9,,,$_,,,hqMf,,,C,:,M___,;,},Class,_O__i,{,Var,K__,:,Boolean,;,},<EOF>''',101))

    def test_1202(self):
        self.assertTrue(TestLexer.test('''Class _{$__5(n,_1,_V:Array [Array [Array [Array [Array [Array [Boolean ,055],01],0xF0],055],80],80];__:Array [Array [Int ,0B1],8651];_,_,_89o:_a_;J:nf3BE;g50m:Boolean ){} }''','''Class,_,{,$__5,(,n,,,_1,,,_V,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,055,],,,01,],,,0xF0,],,,055,],,,80,],,,80,],;,__,:,Array,[,Array,[,Int,,,0B1,],,,8651,],;,_,,,_,,,_89o,:,_a_,;,J,:,nf3BE,;,g50m,:,Boolean,),{,},},<EOF>''',101))

    def test_1203(self):
        self.assertTrue(TestLexer.test('''Class ae:f_N0Z{Constructor (_,L,a1,_1:Array [Float ,065];_,c:String ;_,_5,_,I,_2,rf_:_9;eL,R,Y:Array [Int ,0B1];pZ:_7){} }Class __{Val $______6:Float ;xZ(){}Destructor (){} }''','''Class,ae,:,f_N0Z,{,Constructor,(,_,,,L,,,a1,,,_1,:,Array,[,Float,,,065,],;,_,,,c,:,String,;,_,,,_5,,,_,,,I,,,_2,,,rf_,:,_9,;,eL,,,R,,,Y,:,Array,[,Int,,,0B1,],;,pZ,:,_7,),{,},},Class,__,{,Val,$______6,:,Float,;,xZ,(,),{,},Destructor,(,),{,},},<EOF>''',101))

    def test_1204(self):
        self.assertTrue(TestLexer.test('''Class f:g{Destructor (){} }Class b{Constructor (N43:Array [Boolean ,0b1011111]){}Var $3y:Array [Float ,0112];Constructor (A46_,_2:Float ){}$8(_,__,m,u2,i_DP7,K:Float ){} }Class _:T6{}Class Vn:B{}''','''Class,f,:,g,{,Destructor,(,),{,},},Class,b,{,Constructor,(,N43,:,Array,[,Boolean,,,0b1011111,],),{,},Var,$3y,:,Array,[,Float,,,0112,],;,Constructor,(,A46_,,,_2,:,Float,),{,},$8,(,_,,,__,,,m,,,u2,,,i_DP7,,,K,:,Float,),{,},},Class,_,:,T6,{,},Class,Vn,:,B,{,},<EOF>''',101))

    def test_1205(self):
        self.assertTrue(TestLexer.test('''Class Y{}Class a{Val $57_,$6:_Lq;}Class __{}Class N{Var _A:Y;}Class o{}Class v_:_{Val _:Array [Array [Int ,0B1_00],0x58];}Class _:_{Destructor (){}H(){} }''','''Class,Y,{,},Class,a,{,Val,$57_,,,$6,:,_Lq,;,},Class,__,{,},Class,N,{,Var,_A,:,Y,;,},Class,o,{,},Class,v_,:,_,{,Val,_,:,Array,[,Array,[,Int,,,0B100,],,,0x58,],;,},Class,_,:,_,{,Destructor,(,),{,},H,(,),{,},},<EOF>''',101))

    def test_1206(self):
        self.assertTrue(TestLexer.test('''Class _:tV{}Class ___t__4_:E2P{Val _2:n=True .U()*_::$19see_().s_&&!----O_u::$7.D().b_5.__;Val _:Float ;Val _,_:String ;}Class c{Val $8_:X;}Class _o:_{$_(_:String ;l2g,__:Array [Array [Float ,6],0x57];_:_){Return ;} }Class _:_c_{Destructor (){Continue ;} }Class w{}''','''Class,_,:,tV,{,},Class,___t__4_,:,E2P,{,Val,_2,:,n,=,True,.,U,(,),*,_,::,$19see_,(,),.,s_,&&,!,-,-,-,-,O_u,::,$7,.,D,(,),.,b_5,.,__,;,Val,_,:,Float,;,Val,_,,,_,:,String,;,},Class,c,{,Val,$8_,:,X,;,},Class,_o,:,_,{,$_,(,_,:,String,;,l2g,,,__,:,Array,[,Array,[,Float,,,6,],,,0x57,],;,_,:,_,),{,Return,;,},},Class,_,:,_c_,{,Destructor,(,),{,Continue,;,},},Class,w,{,},<EOF>''',101))

    def test_1207(self):
        self.assertTrue(TestLexer.test('''Class m0_:_K{Destructor (){} }Class uYi{Constructor (){} }Class F:c_v_o7{Var r63,K9:Float ;}Class J7:_1{Val _:Int ;}Class C:h{E___4(_7SG_,_R,_7,L:String ;u_356:D){}Constructor (){}Var _:Array [Array [Array [Int ,33],0b100],0B11000];}''','''Class,m0_,:,_K,{,Destructor,(,),{,},},Class,uYi,{,Constructor,(,),{,},},Class,F,:,c_v_o7,{,Var,r63,,,K9,:,Float,;,},Class,J7,:,_1,{,Val,_,:,Int,;,},Class,C,:,h,{,E___4,(,_7SG_,,,_R,,,_7,,,L,:,String,;,u_356,:,D,),{,},Constructor,(,),{,},Var,_,:,Array,[,Array,[,Array,[,Int,,,33,],,,0b100,],,,0B11000,],;,},<EOF>''',101))

    def test_1208(self):
        self.assertTrue(TestLexer.test('''Class R:t_6{Val _:Fb;Constructor (_,h,_5:Array [Array [Array [Array [Float ,0x2],7],04_5_736],1]){} }Class _{}Class _:Y_7J_{}''','''Class,R,:,t_6,{,Val,_,:,Fb,;,Constructor,(,_,,,h,,,_5,:,Array,[,Array,[,Array,[,Array,[,Float,,,0x2,],,,7,],,,045736,],,,1,],),{,},},Class,_,{,},Class,_,:,Y_7J_,{,},<EOF>''',101))

    def test_1209(self):
        self.assertTrue(TestLexer.test('''Class H{Val e:Int ;}Class m:M4{}Class __{}Class _0080p{Constructor (){Break ;}Val $86,RYn,$a8k:Boolean ;}Class _{}''','''Class,H,{,Val,e,:,Int,;,},Class,m,:,M4,{,},Class,__,{,},Class,_0080p,{,Constructor,(,),{,Break,;,},Val,$86,,,RYn,,,$a8k,:,Boolean,;,},Class,_,{,},<EOF>''',101))

    def test_1210(self):
        self.assertTrue(TestLexer.test('''Class _{}Class _3_:R_{}Class n8{}Class _{}Class Vc:_{mf_(_8m:Boolean ;p:Boolean ){} }Class e4k6{Destructor (){} }''','''Class,_,{,},Class,_3_,:,R_,{,},Class,n8,{,},Class,_,{,},Class,Vc,:,_,{,mf_,(,_8m,:,Boolean,;,p,:,Boolean,),{,},},Class,e4k6,{,Destructor,(,),{,},},<EOF>''',101))

    def test_1211(self):
        self.assertTrue(TestLexer.test('''Class _z{Destructor (){Val p_Y:Array [Array [Int ,0B1_1_1010],0b1010001];}Val XhC,$K5kg,S,_ga__:_;Destructor (){Return ;Return ;Continue ;} }Class uc1:P{}''','''Class,_z,{,Destructor,(,),{,Val,p_Y,:,Array,[,Array,[,Int,,,0B111010,],,,0b1010001,],;,},Val,XhC,,,$K5kg,,,S,,,_ga__,:,_,;,Destructor,(,),{,Return,;,Return,;,Continue,;,},},Class,uc1,:,P,{,},<EOF>''',101))

    def test_1212(self):
        self.assertTrue(TestLexer.test('''Class _{Val $_5:Array [Array [Array [Float ,0130],032_7],0X11];_Y6(){}Val $_:Array [Array [Array [Array [String ,04_6],0B11000],98_4],0x9];}Class U:O_H__SY{}Class _5{}''','''Class,_,{,Val,$_5,:,Array,[,Array,[,Array,[,Float,,,0130,],,,0327,],,,0X11,],;,_Y6,(,),{,},Val,$_,:,Array,[,Array,[,Array,[,Array,[,String,,,046,],,,0B11000,],,,984,],,,0x9,],;,},Class,U,:,O_H__SY,{,},Class,_5,{,},<EOF>''',101))

    def test_1213(self):
        self.assertTrue(TestLexer.test('''Class _:D{Var $2,$0_g,_m0,l,_:Array [String ,0B11_1];Destructor (){Continue ;}Q(){Break ;Return ;} }Class q_{}Class f00:ZP{}''','''Class,_,:,D,{,Var,$2,,,$0_g,,,_m0,,,l,,,_,:,Array,[,String,,,0B111,],;,Destructor,(,),{,Continue,;,},Q,(,),{,Break,;,Return,;,},},Class,q_,{,},Class,f00,:,ZP,{,},<EOF>''',101))

    def test_1214(self):
        self.assertTrue(TestLexer.test('''Class r_:_{Val _A:_;Val __V:Array [String ,0B110];}Class _{}Class _n:s{Constructor (){} }Class BW:_0{Val $cB,$_x78vJ25Y,_,_H:_;}''','''Class,r_,:,_,{,Val,_A,:,_,;,Val,__V,:,Array,[,String,,,0B110,],;,},Class,_,{,},Class,_n,:,s,{,Constructor,(,),{,},},Class,BW,:,_0,{,Val,$cB,,,$_x78vJ25Y,,,_,,,_H,:,_,;,},<EOF>''',101))

    def test_1215(self):
        self.assertTrue(TestLexer.test('''Class _l{_62(_5_O,l,P,g:_;_,T,_,_:Array [Array [Array [Array [Array [Array [Float ,010],50],010],061],0B10],015_6]){} }Class B:Cy62{}Class x_{}Class _6:_{Var $2J_:lr;}''','''Class,_l,{,_62,(,_5_O,,,l,,,P,,,g,:,_,;,_,,,T,,,_,,,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,010,],,,50,],,,010,],,,061,],,,0B10,],,,0156,],),{,},},Class,B,:,Cy62,{,},Class,x_,{,},Class,_6,:,_,{,Var,$2J_,:,lr,;,},<EOF>''',101))

    def test_1216(self):
        self.assertTrue(TestLexer.test('''Class nF__:_7{Constructor (){}W(_,_:__){ {} }Constructor (U_,__8Y,Z,p,_,_0:_;_,__5:Array [Boolean ,07_427]){}Var $RV:__g;}''','''Class,nF__,:,_7,{,Constructor,(,),{,},W,(,_,,,_,:,__,),{,{,},},Constructor,(,U_,,,__8Y,,,Z,,,p,,,_,,,_0,:,_,;,_,,,__5,:,Array,[,Boolean,,,07427,],),{,},Var,$RV,:,__g,;,},<EOF>''',101))

    def test_1217(self):
        self.assertTrue(TestLexer.test('''Class _:___{Var N:Array [Array [Array [Array [Array [Int ,0b1010000],0104],0X43],0b1010000],0xB];$M(_86:Array [Boolean ,0x26];R_,_:M;_5f4,_,_:o1c){} }Class _4z{Destructor (){} }''','''Class,_,:,___,{,Var,N,:,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0b1010000,],,,0104,],,,0X43,],,,0b1010000,],,,0xB,],;,$M,(,_86,:,Array,[,Boolean,,,0x26,],;,R_,,,_,:,M,;,_5f4,,,_,,,_,:,o1c,),{,},},Class,_4z,{,Destructor,(,),{,},},<EOF>''',101))

    def test_1218(self):
        self.assertTrue(TestLexer.test('''Class X:_iA{}Class pk{Val $0,$_,_,_,$_:Array [Array [Array [Array [Array [Array [Float ,0B1001],0B11],9_9],86],86],0X3D];}''','''Class,X,:,_iA,{,},Class,pk,{,Val,$0,,,$_,,,_,,,_,,,$_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0B1001,],,,0B11,],,,99,],,,86,],,,86,],,,0X3D,],;,},<EOF>''',101))

    def test_1219(self):
        self.assertTrue(TestLexer.test('''Class F:_{Constructor (_8:Array [String ,0X28];v,_Z93t,s:s_;_g,i9,P_:Int ;L0,Z7:Boolean ){Var _,_,n:Array [Array [Boolean ,0X28],9];} }''','''Class,F,:,_,{,Constructor,(,_8,:,Array,[,String,,,0X28,],;,v,,,_Z93t,,,s,:,s_,;,_g,,,i9,,,P_,:,Int,;,L0,,,Z7,:,Boolean,),{,Var,_,,,_,,,n,:,Array,[,Array,[,Boolean,,,0X28,],,,9,],;,},},<EOF>''',101))

    def test_1220(self):
        self.assertTrue(TestLexer.test('''Class z8D5_:La96{Val $__5__8,_Y_1c:Array [String ,07];Val Z_3,$_i:h;}Class _:k{}Class _:_{Destructor (){} }Class I06:_Q{}Class m:_{}''','''Class,z8D5_,:,La96,{,Val,$__5__8,,,_Y_1c,:,Array,[,String,,,07,],;,Val,Z_3,,,$_i,:,h,;,},Class,_,:,k,{,},Class,_,:,_,{,Destructor,(,),{,},},Class,I06,:,_Q,{,},Class,m,:,_,{,},<EOF>''',101))

    def test_1221(self):
        self.assertTrue(TestLexer.test('''Class D_:m_{}Class _{Var $_:Array [Array [Array [Array [Array [Array [Array [Boolean ,0b11],70],6298_5_6],0b110100],70],8],1];}''','''Class,D_,:,m_,{,},Class,_,{,Var,$_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0b11,],,,70,],,,629856,],,,0b110100,],,,70,],,,8,],,,1,],;,},<EOF>''',101))

    def test_1222(self):
        self.assertTrue(TestLexer.test('''Class s{Constructor (){}Var $_,_D,$8C,$2:Array [Array [Array [Array [Array [String ,0106],0106],0B1001111],30],0b1100000];Var tK_:Boolean ;}''','''Class,s,{,Constructor,(,),{,},Var,$_,,,_D,,,$8C,,,$2,:,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0106,],,,0106,],,,0B1001111,],,,30,],,,0b1100000,],;,Var,tK_,:,Boolean,;,},<EOF>''',101))

    def test_1223(self):
        self.assertTrue(TestLexer.test('''Class _9t{Constructor (n:Boolean ;_7Ie:_){}$9_(_9,y,R,_:Array [Array [Int ,0b101100],0XBA_4]){} }Class t_i95:g{}Class g{Destructor (){} }Class _{Destructor (){}Constructor (){ {} }}Class B:_E{}''','''Class,_9t,{,Constructor,(,n,:,Boolean,;,_7Ie,:,_,),{,},$9_,(,_9,,,y,,,R,,,_,:,Array,[,Array,[,Int,,,0b101100,],,,0XBA4,],),{,},},Class,t_i95,:,g,{,},Class,g,{,Destructor,(,),{,},},Class,_,{,Destructor,(,),{,},Constructor,(,),{,{,},},},Class,B,:,_E,{,},<EOF>''',101))

    def test_1224(self):
        self.assertTrue(TestLexer.test('''Class a{}Class L0b_{Constructor (_:Array [String ,49];k:Array [Array [Array [Float ,0X9],0XA],1];_:_){} }Class _h0_:_I_{}Class _oyVr_{Val n,_,_Y,E_,$H,__:P__;}''','''Class,a,{,},Class,L0b_,{,Constructor,(,_,:,Array,[,String,,,49,],;,k,:,Array,[,Array,[,Array,[,Float,,,0X9,],,,0XA,],,,1,],;,_,:,_,),{,},},Class,_h0_,:,_I_,{,},Class,_oyVr_,{,Val,n,,,_,,,_Y,,,E_,,,$H,,,__,:,P__,;,},<EOF>''',101))

    def test_1225(self):
        self.assertTrue(TestLexer.test('''Class x:R{}Class __:e{Val $C,IS:Array [Array [Array [Array [Array [Boolean ,01],0X5D],01],0X5D],0X91_7_3];}Class _ki:ZQ__{S(){Return ;}$e(){}Var _J,_:Array [Array [Int ,0x3A],0X5D];}''','''Class,x,:,R,{,},Class,__,:,e,{,Val,$C,,,IS,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,01,],,,0X5D,],,,01,],,,0X5D,],,,0X9173,],;,},Class,_ki,:,ZQ__,{,S,(,),{,Return,;,},$e,(,),{,},Var,_J,,,_,:,Array,[,Array,[,Int,,,0x3A,],,,0X5D,],;,},<EOF>''',101))

    def test_1226(self):
        self.assertTrue(TestLexer.test('''Class T0_{Var $r,_h_:Boolean ;}Class __{_2H(e:_7;s:_;p98,p,RXS5c:Float ;F_d,_G4,_,_:Array [Array [Boolean ,25],06_2_6];_5O,Hw,_,_,V,Yq:Boolean ){}Destructor (){Break ;Return ;Continue ;{} }Var Q:Array [Float ,0x5C];Constructor (_1:_){}Val f,_4,____,__:_8T;Constructor (){} }''','''Class,T0_,{,Var,$r,,,_h_,:,Boolean,;,},Class,__,{,_2H,(,e,:,_7,;,s,:,_,;,p98,,,p,,,RXS5c,:,Float,;,F_d,,,_G4,,,_,,,_,:,Array,[,Array,[,Boolean,,,25,],,,0626,],;,_5O,,,Hw,,,_,,,_,,,V,,,Yq,:,Boolean,),{,},Destructor,(,),{,Break,;,Return,;,Continue,;,{,},},Var,Q,:,Array,[,Float,,,0x5C,],;,Constructor,(,_1,:,_,),{,},Val,f,,,_4,,,____,,,__,:,_8T,;,Constructor,(,),{,},},<EOF>''',101))

    def test_1227(self):
        self.assertTrue(TestLexer.test('''Class D:u{Var _f_:String ;}Class _{Constructor (){}_(D,_b:String ;_,l,_Qc7_,_,e,_h,_,y2:__){}Destructor (){} }Class _{}Class _2vO{}''','''Class,D,:,u,{,Var,_f_,:,String,;,},Class,_,{,Constructor,(,),{,},_,(,D,,,_b,:,String,;,_,,,l,,,_Qc7_,,,_,,,e,,,_h,,,_,,,y2,:,__,),{,},Destructor,(,),{,},},Class,_,{,},Class,_2vO,{,},<EOF>''',101))

    def test_1228(self):
        self.assertTrue(TestLexer.test('''Class _:A{}Class _{}Class _:l{Destructor (){ {} }Constructor (u:Array [Float ,04];_,C_,_gK,ezF,xC,u:Float ;_dE:s;xE,j_,_PU,_,TW1,_:Float ){_4b_ok::$7__6();} }''','''Class,_,:,A,{,},Class,_,{,},Class,_,:,l,{,Destructor,(,),{,{,},},Constructor,(,u,:,Array,[,Float,,,04,],;,_,,,C_,,,_gK,,,ezF,,,xC,,,u,:,Float,;,_dE,:,s,;,xE,,,j_,,,_PU,,,_,,,TW1,,,_,:,Float,),{,_4b_ok,::,$7__6,(,),;,},},<EOF>''',101))

    def test_1229(self):
        self.assertTrue(TestLexer.test('''Class _VUn:_b{Val _,$M_:String ;Var ___t,$9:Array [Int ,0b111110];}Class _:c{Constructor (_:Array [Float ,01_51];_,h_:hm){_::$c9.t2();} }Class b_{}''','''Class,_VUn,:,_b,{,Val,_,,,$M_,:,String,;,Var,___t,,,$9,:,Array,[,Int,,,0b111110,],;,},Class,_,:,c,{,Constructor,(,_,:,Array,[,Float,,,0151,],;,_,,,h_,:,hm,),{,_,::,$c9,.,t2,(,),;,},},Class,b_,{,},<EOF>''',101))

    def test_1230(self):
        self.assertTrue(TestLexer.test('''Class _{Var $2_,$8_7bN_,$9_:Array [Array [Boolean ,0X97_F],9];Var U:Array [Array [Int ,0b1001110],0X95B];Var $5,_:String ;}Class _T:_h{}''','''Class,_,{,Var,$2_,,,$8_7bN_,,,$9_,:,Array,[,Array,[,Boolean,,,0X97F,],,,9,],;,Var,U,:,Array,[,Array,[,Int,,,0b1001110,],,,0X95B,],;,Var,$5,,,_,:,String,;,},Class,_T,:,_h,{,},<EOF>''',101))

    def test_1231(self):
        self.assertTrue(TestLexer.test('''Class _2P_{Constructor (_,__,q6:Array [Array [Boolean ,0136],0136];m:A2;UwE9:Array [Array [Array [Array [Array [Array [Int ,06],0B1],0B1],49],06_51_55],0B1];_5,u,_:Int ;n,B_:String ;S7U9,N___,O,J_,_,_5:Array [Array [Array [Boolean ,0X21],7],01]){}Constructor (){}Var $6e,_2:_;}''','''Class,_2P_,{,Constructor,(,_,,,__,,,q6,:,Array,[,Array,[,Boolean,,,0136,],,,0136,],;,m,:,A2,;,UwE9,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,06,],,,0B1,],,,0B1,],,,49,],,,065155,],,,0B1,],;,_5,,,u,,,_,:,Int,;,n,,,B_,:,String,;,S7U9,,,N___,,,O,,,J_,,,_,,,_5,:,Array,[,Array,[,Array,[,Boolean,,,0X21,],,,7,],,,01,],),{,},Constructor,(,),{,},Var,$6e,,,_2,:,_,;,},<EOF>''',101))

    def test_1232(self):
        self.assertTrue(TestLexer.test('''Class _Ti:_{Val _T,$7,$T6:Boolean ;Destructor (){Break ;}Val $_,$_NXC:Array [Array [Boolean ,15],0B1];Constructor (_5,xr:Float ){} }''','''Class,_Ti,:,_,{,Val,_T,,,$7,,,$T6,:,Boolean,;,Destructor,(,),{,Break,;,},Val,$_,,,$_NXC,:,Array,[,Array,[,Boolean,,,15,],,,0B1,],;,Constructor,(,_5,,,xr,:,Float,),{,},},<EOF>''',101))

    def test_1233(self):
        self.assertTrue(TestLexer.test('''Class _:D71{}Class D{_p(OV:Array [Array [Boolean ,71],6_2];_571:String ;__:Array [Int ,71];RL:W){}Destructor (){Continue ;} }Class _{}''','''Class,_,:,D71,{,},Class,D,{,_p,(,OV,:,Array,[,Array,[,Boolean,,,71,],,,62,],;,_571,:,String,;,__,:,Array,[,Int,,,71,],;,RL,:,W,),{,},Destructor,(,),{,Continue,;,},},Class,_,{,},<EOF>''',101))

    def test_1234(self):
        self.assertTrue(TestLexer.test('''Class _{Constructor (){}Constructor (_:String ;tI1x:Boolean ;c,E_y_,_:Int ;T:Int ;c9lO0n,_,E_,z9,_,_:Float ){} }''','''Class,_,{,Constructor,(,),{,},Constructor,(,_,:,String,;,tI1x,:,Boolean,;,c,,,E_y_,,,_,:,Int,;,T,:,Int,;,c9lO0n,,,_,,,E_,,,z9,,,_,,,_,:,Float,),{,},},<EOF>''',101))

    def test_1235(self):
        self.assertTrue(TestLexer.test('''Class p:_{Constructor (O,K_0:String ;_:JH8;_,J_60,_6,_,p_:_;D8_,t,Fr__n,L67,k97:Array [Boolean ,37_1];I_T_:String ){}Constructor (){Break ;} }Class U_Eq2:_{}Class tW62_{}''','''Class,p,:,_,{,Constructor,(,O,,,K_0,:,String,;,_,:,JH8,;,_,,,J_60,,,_6,,,_,,,p_,:,_,;,D8_,,,t,,,Fr__n,,,L67,,,k97,:,Array,[,Boolean,,,371,],;,I_T_,:,String,),{,},Constructor,(,),{,Break,;,},},Class,U_Eq2,:,_,{,},Class,tW62_,{,},<EOF>''',101))

    def test_1236(self):
        self.assertTrue(TestLexer.test('''Class t{}Class L{}Class _:d{Var O,_,S:Boolean ;Val $3,_1_:Array [Array [Boolean ,66],0b11];$5(){Break ;} }Class d1:a{Var $_s_k:_;}Class Jz:M0__{}''','''Class,t,{,},Class,L,{,},Class,_,:,d,{,Var,O,,,_,,,S,:,Boolean,;,Val,$3,,,_1_,:,Array,[,Array,[,Boolean,,,66,],,,0b11,],;,$5,(,),{,Break,;,},},Class,d1,:,a,{,Var,$_s_k,:,_,;,},Class,Jz,:,M0__,{,},<EOF>''',101))

    def test_1237(self):
        self.assertTrue(TestLexer.test('''Class __2:_6{}Class b:q{$8_(_:_rJ_;_,p_,_4A,_,J,_:Array [Int ,0XA];yb4_:Array [Array [Array [Boolean ,0b11],02],0XA_E]){} }''','''Class,__2,:,_6,{,},Class,b,:,q,{,$8_,(,_,:,_rJ_,;,_,,,p_,,,_4A,,,_,,,J,,,_,:,Array,[,Int,,,0XA,],;,yb4_,:,Array,[,Array,[,Array,[,Boolean,,,0b11,],,,02,],,,0XAE,],),{,},},<EOF>''',101))

    def test_1238(self):
        self.assertTrue(TestLexer.test('''Class P{}Class _1{Var $_:Boolean ;}Class _{}Class _{Constructor (d8XPZc_4d46F:Array [Int ,043];f,_e,_:Array [Boolean ,7]){} }Class n3:c_{$_8(G6,Sw43:String ){} }''','''Class,P,{,},Class,_1,{,Var,$_,:,Boolean,;,},Class,_,{,},Class,_,{,Constructor,(,d8XPZc_4d46F,:,Array,[,Int,,,043,],;,f,,,_e,,,_,:,Array,[,Boolean,,,7,],),{,},},Class,n3,:,c_,{,$_8,(,G6,,,Sw43,:,String,),{,},},<EOF>''',101))

    def test_1239(self):
        self.assertTrue(TestLexer.test('''Class _y:Dq{_(__6_:Array [Array [Array [Array [Array [Boolean ,6],0x5F],050],0B110010],7_0]){} }Class R{Constructor (){} }''','''Class,_y,:,Dq,{,_,(,__6_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,6,],,,0x5F,],,,050,],,,0B110010,],,,70,],),{,},},Class,R,{,Constructor,(,),{,},},<EOF>''',101))

    def test_1240(self):
        self.assertTrue(TestLexer.test('''Class _K{}Class w{}Class _Z78o{Constructor (spO,t,_y,ShY3,Ri7,d_:String ;_,_,_T,q_5:_J89_X;C__u:String ;t0_s_2b:Float ;L5_:Float ;_,k,_4,_,iz,sz_I:Array [Boolean ,0b11_0];_h3_,Z6,R_3_F_,b:Array [Array [Float ,0X4F],5]){Continue ;}Val $_,O,$_:J;Var _:Array [String ,0b1_10_1];}Class UM{}''','''Class,_K,{,},Class,w,{,},Class,_Z78o,{,Constructor,(,spO,,,t,,,_y,,,ShY3,,,Ri7,,,d_,:,String,;,_,,,_,,,_T,,,q_5,:,_J89_X,;,C__u,:,String,;,t0_s_2b,:,Float,;,L5_,:,Float,;,_,,,k,,,_4,,,_,,,iz,,,sz_I,:,Array,[,Boolean,,,0b110,],;,_h3_,,,Z6,,,R_3_F_,,,b,:,Array,[,Array,[,Float,,,0X4F,],,,5,],),{,Continue,;,},Val,$_,,,O,,,$_,:,J,;,Var,_,:,Array,[,String,,,0b1101,],;,},Class,UM,{,},<EOF>''',101))

    def test_1241(self):
        self.assertTrue(TestLexer.test('''Class c9{$S(u6:Array [Boolean ,041];_:String ){}Var $_2,$1_:Boolean ;Val $3,$a7,$k:Array [Array [Array [Int ,0XC3],50],041];Val $_9,$B,$0SQ:Float ;Destructor (){} }''','''Class,c9,{,$S,(,u6,:,Array,[,Boolean,,,041,],;,_,:,String,),{,},Var,$_2,,,$1_,:,Boolean,;,Val,$3,,,$a7,,,$k,:,Array,[,Array,[,Array,[,Int,,,0XC3,],,,50,],,,041,],;,Val,$_9,,,$B,,,$0SQ,:,Float,;,Destructor,(,),{,},},<EOF>''',101))

    def test_1242(self):
        self.assertTrue(TestLexer.test('''Class K:bDH_6{Constructor (){} }Class o{$u0_(_:Array [Array [Array [Array [Array [Array [String ,0B1],3],0x3_E27],72],0b1001010],03]){} }Class r_:_{}Class v4_:j5{Val $7_,$F:Float ;}''','''Class,K,:,bDH_6,{,Constructor,(,),{,},},Class,o,{,$u0_,(,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0B1,],,,3,],,,0x3E27,],,,72,],,,0b1001010,],,,03,],),{,},},Class,r_,:,_,{,},Class,v4_,:,j5,{,Val,$7_,,,$F,:,Float,;,},<EOF>''',101))

    def test_1243(self):
        self.assertTrue(TestLexer.test('''Class v84:_{Val n0_M:Array [Int ,0b1011001];}Class _:_{Constructor (){}Var $zs__B,I_:Array [Array [Array [Int ,0b1],0X40],0x4E];}''','''Class,v84,:,_,{,Val,n0_M,:,Array,[,Int,,,0b1011001,],;,},Class,_,:,_,{,Constructor,(,),{,},Var,$zs__B,,,I_,:,Array,[,Array,[,Array,[,Int,,,0b1,],,,0X40,],,,0x4E,],;,},<EOF>''',101))

    def test_1244(self):
        self.assertTrue(TestLexer.test('''Class _4:_j{}Class v5_{Val g:Gl9nwR;}Class k:_P{Constructor (j_,gQ,__J,by:Array [Array [Array [Array [String ,0x3B],0b10],0B1000],07]){}Destructor (){} }Class SB2o_{}Class _5:H{Val $F_,$ma9_0a:Array [Float ,0b11011];Var $h4,h:String ;}''','''Class,_4,:,_j,{,},Class,v5_,{,Val,g,:,Gl9nwR,;,},Class,k,:,_P,{,Constructor,(,j_,,,gQ,,,__J,,,by,:,Array,[,Array,[,Array,[,Array,[,String,,,0x3B,],,,0b10,],,,0B1000,],,,07,],),{,},Destructor,(,),{,},},Class,SB2o_,{,},Class,_5,:,H,{,Val,$F_,,,$ma9_0a,:,Array,[,Float,,,0b11011,],;,Var,$h4,,,h,:,String,;,},<EOF>''',101))

    def test_1245(self):
        self.assertTrue(TestLexer.test('''Class _7_{Var _,$3__7,$n_,$YG,$j74_:Array [Array [Array [Array [Array [Array [Array [Array [Float ,0x2D],0b1],0b11],07_6_4_4],2],0130],0x2D],42];}''','''Class,_7_,{,Var,_,,,$3__7,,,$n_,,,$YG,,,$j74_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0x2D,],,,0b1,],,,0b11,],,,07644,],,,2,],,,0130,],,,0x2D,],,,42,],;,},<EOF>''',101))

    def test_1246(self):
        self.assertTrue(TestLexer.test('''Class w_9:_2{__(_,f_,Q,e,T_:h;_,x,E_,_46_:Array [Array [Array [Array [Array [Array [String ,75],01],22_4],0XDA],0x1],0B101100];a,LJ,_5Cb_9,p60X,dS8,_,o,_,CU_:Array [Array [Boolean ,0X47],0b1];_:Boolean ){} }''','''Class,w_9,:,_2,{,__,(,_,,,f_,,,Q,,,e,,,T_,:,h,;,_,,,x,,,E_,,,_46_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,75,],,,01,],,,224,],,,0XDA,],,,0x1,],,,0B101100,],;,a,,,LJ,,,_5Cb_9,,,p60X,,,dS8,,,_,,,o,,,_,,,CU_,:,Array,[,Array,[,Boolean,,,0X47,],,,0b1,],;,_,:,Boolean,),{,},},<EOF>''',101))

    def test_1247(self):
        self.assertTrue(TestLexer.test('''Class o_t:_{Val $l:d5;Constructor (_2,W,m,C:_;Vt:Array [Float ,0b10110];g,j:T;_Fa,_,_,__:Array [Array [Float ,0x58],0b10110]){}Val _:FX__4G;Val p,$94,w6_9j:Array [Array [Array [Boolean ,0B11000],052],0B11000];}Class c6N{}''','''Class,o_t,:,_,{,Val,$l,:,d5,;,Constructor,(,_2,,,W,,,m,,,C,:,_,;,Vt,:,Array,[,Float,,,0b10110,],;,g,,,j,:,T,;,_Fa,,,_,,,_,,,__,:,Array,[,Array,[,Float,,,0x58,],,,0b10110,],),{,},Val,_,:,FX__4G,;,Val,p,,,$94,,,w6_9j,:,Array,[,Array,[,Array,[,Boolean,,,0B11000,],,,052,],,,0B11000,],;,},Class,c6N,{,},<EOF>''',101))

    def test_1248(self):
        self.assertTrue(TestLexer.test('''Class v_G{}Class x2__m{$G(_9c,K,_g__:Array [Array [Array [Array [Array [Float ,0xD],0b1011100],7_6],0X64],0b1];_:String ){} }''','''Class,v_G,{,},Class,x2__m,{,$G,(,_9c,,,K,,,_g__,:,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0xD,],,,0b1011100,],,,76,],,,0X64,],,,0b1,],;,_,:,String,),{,},},<EOF>''',101))

    def test_1249(self):
        self.assertTrue(TestLexer.test('''Class _2b:t{}Class f_:_9{Val _k7:String ;Constructor (L,nF_N,J5,_:Array [Array [Float ,43],0132];_____,c:Int ;p_,_,G:w){} }Class c:_6{}Class _g_:_{}''','''Class,_2b,:,t,{,},Class,f_,:,_9,{,Val,_k7,:,String,;,Constructor,(,L,,,nF_N,,,J5,,,_,:,Array,[,Array,[,Float,,,43,],,,0132,],;,_____,,,c,:,Int,;,p_,,,_,,,G,:,w,),{,},},Class,c,:,_6,{,},Class,_g_,:,_,{,},<EOF>''',101))

    def test_1250(self):
        self.assertTrue(TestLexer.test('''Class g{Constructor (_,H_2_,_V,__GE_N,_,_:Int ;D4_w:Array [Float ,0X24];P,_6:Array [Array [Array [Int ,03],0X28],0X8];_r,__,__q,CD_:Float ){} }''','''Class,g,{,Constructor,(,_,,,H_2_,,,_V,,,__GE_N,,,_,,,_,:,Int,;,D4_w,:,Array,[,Float,,,0X24,],;,P,,,_6,:,Array,[,Array,[,Array,[,Int,,,03,],,,0X28,],,,0X8,],;,_r,,,__,,,__q,,,CD_,:,Float,),{,},},<EOF>''',101))

    def test_1251(self):
        self.assertTrue(TestLexer.test('''Class H_:Y{Val $1,$_:Array [Float ,0b1];Var M,$_,Z,$_:_;Var $_:_7_;$__(_2:Array [Int ,0b11111];_,_,_:hW54_7;_:_4){Val m,P,_9_:Float ;} }''','''Class,H_,:,Y,{,Val,$1,,,$_,:,Array,[,Float,,,0b1,],;,Var,M,,,$_,,,Z,,,$_,:,_,;,Var,$_,:,_7_,;,$__,(,_2,:,Array,[,Int,,,0b11111,],;,_,,,_,,,_,:,hW54_7,;,_,:,_4,),{,Val,m,,,P,,,_9_,:,Float,;,},},<EOF>''',101))

    def test_1252(self):
        self.assertTrue(TestLexer.test('''Class __n{qV(){Continue ;}Constructor (){}Constructor (_1,M:Int ;_:_3;S35:Array [Int ,0XC];G,_3:Array [String ,055]){Val d:Boolean ;} }''','''Class,__n,{,qV,(,),{,Continue,;,},Constructor,(,),{,},Constructor,(,_1,,,M,:,Int,;,_,:,_3,;,S35,:,Array,[,Int,,,0XC,],;,G,,,_3,:,Array,[,String,,,055,],),{,Val,d,:,Boolean,;,},},<EOF>''',101))

    def test_1253(self):
        self.assertTrue(TestLexer.test('''Class __9_:__{Var $Mh:Array [Array [Array [Array [Float ,0x5D],23],03_5_0],0B1];Var U:P;Destructor (){} }Class oV:_{Var $__i29__u,$_14,$_:Array [Int ,0b101_0_0];}Class h:_6{Destructor (){ {}{} }}''','''Class,__9_,:,__,{,Var,$Mh,:,Array,[,Array,[,Array,[,Array,[,Float,,,0x5D,],,,23,],,,0350,],,,0B1,],;,Var,U,:,P,;,Destructor,(,),{,},},Class,oV,:,_,{,Var,$__i29__u,,,$_14,,,$_,:,Array,[,Int,,,0b10100,],;,},Class,h,:,_6,{,Destructor,(,),{,{,},{,},},},<EOF>''',101))

    def test_1254(self):
        self.assertTrue(TestLexer.test('''Class g:_{Constructor (_,__,_,g,_,kX4:Array [Int ,18];_E,K,T:__;d,D:String ){Continue ;} }Class O_CYT{}Class Zb:MA{Destructor (){} }''','''Class,g,:,_,{,Constructor,(,_,,,__,,,_,,,g,,,_,,,kX4,:,Array,[,Int,,,18,],;,_E,,,K,,,T,:,__,;,d,,,D,:,String,),{,Continue,;,},},Class,O_CYT,{,},Class,Zb,:,MA,{,Destructor,(,),{,},},<EOF>''',101))

    def test_1255(self):
        self.assertTrue(TestLexer.test('''Class _YUa:v{Val $_,e_,$__,z,$n__9,c6,$YF:Array [Array [Array [Array [Array [Boolean ,0117],0B1],1],0X9],043];Constructor (){Continue ;} }Class ___:a{}Class r{}''','''Class,_YUa,:,v,{,Val,$_,,,e_,,,$__,,,z,,,$n__9,,,c6,,,$YF,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0117,],,,0B1,],,,1,],,,0X9,],,,043,],;,Constructor,(,),{,Continue,;,},},Class,___,:,a,{,},Class,r,{,},<EOF>''',101))

    def test_1256(self):
        self.assertTrue(TestLexer.test('''Class _:_{}Class _:_H{Constructor (_:Boolean ;_,_:_0;Nj3_,b:Array [String ,0x22]){}Val $0:Int ;Destructor (){} }''','''Class,_,:,_,{,},Class,_,:,_H,{,Constructor,(,_,:,Boolean,;,_,,,_,:,_0,;,Nj3_,,,b,:,Array,[,String,,,0x22,],),{,},Val,$0,:,Int,;,Destructor,(,),{,},},<EOF>''',101))

    def test_1257(self):
        self.assertTrue(TestLexer.test('''Class _:__{Var _,$_,z_B_:Array [Float ,0x6];Val $F:_2__;Var $Q_,$01:Array [Array [Array [Float ,0b10],9],0x6];}''','''Class,_,:,__,{,Var,_,,,$_,,,z_B_,:,Array,[,Float,,,0x6,],;,Val,$F,:,_2__,;,Var,$Q_,,,$01,:,Array,[,Array,[,Array,[,Float,,,0b10,],,,9,],,,0x6,],;,},<EOF>''',101))

    def test_1258(self):
        self.assertTrue(TestLexer.test('''Class _9{Val m,$__,k:Array [Array [Array [Boolean ,022_75],0b111110],49];}Class l_:_{Destructor (){}Constructor (){} }''','''Class,_9,{,Val,m,,,$__,,,k,:,Array,[,Array,[,Array,[,Boolean,,,02275,],,,0b111110,],,,49,],;,},Class,l_,:,_,{,Destructor,(,),{,},Constructor,(,),{,},},<EOF>''',101))

    def test_1259(self):
        self.assertTrue(TestLexer.test('''Class zm{g(Y,o_,_7_C:Array [Float ,0B1110];a:L){Val _:_k;}_(Z,g:Array [Array [Int ,0303],2]){Break ;Return ;} }Class _:_{}Class x:d4{}Class K:_{}''','''Class,zm,{,g,(,Y,,,o_,,,_7_C,:,Array,[,Float,,,0B1110,],;,a,:,L,),{,Val,_,:,_k,;,},_,(,Z,,,g,:,Array,[,Array,[,Int,,,0303,],,,2,],),{,Break,;,Return,;,},},Class,_,:,_,{,},Class,x,:,d4,{,},Class,K,:,_,{,},<EOF>''',101))

    def test_1260(self):
        self.assertTrue(TestLexer.test('''Class __{Val n4:Float ;}Class _{Var $_,_,$411Y3p,$u,A4t:Float ;}Class E{}Class F:__8{}Class __:V7_{}Class E:M{}''','''Class,__,{,Val,n4,:,Float,;,},Class,_,{,Var,$_,,,_,,,$411Y3p,,,$u,,,A4t,:,Float,;,},Class,E,{,},Class,F,:,__8,{,},Class,__,:,V7_,{,},Class,E,:,M,{,},<EOF>''',101))

    def test_1261(self):
        self.assertTrue(TestLexer.test('''Class _5d9_77{Constructor (i2:Array [Boolean ,0x65E];e,_e01,_:_;_5:Array [Array [Float ,6],44];x,_:Array [Int ,0x1CA];q:Boolean ){ {} }}''','''Class,_5d9_77,{,Constructor,(,i2,:,Array,[,Boolean,,,0x65E,],;,e,,,_e01,,,_,:,_,;,_5,:,Array,[,Array,[,Float,,,6,],,,44,],;,x,,,_,:,Array,[,Int,,,0x1CA,],;,q,:,Boolean,),{,{,},},},<EOF>''',101))

    def test_1262(self):
        self.assertTrue(TestLexer.test('''Class _:EL{Constructor (_:Array [Array [Array [Array [Float ,047],74],63],0x1];Y_,Q_4m:Array [Float ,0B1010]){} }Class zr{}''','''Class,_,:,EL,{,Constructor,(,_,:,Array,[,Array,[,Array,[,Array,[,Float,,,047,],,,74,],,,63,],,,0x1,],;,Y_,,,Q_4m,:,Array,[,Float,,,0B1010,],),{,},},Class,zr,{,},<EOF>''',101))

    def test_1263(self):
        self.assertTrue(TestLexer.test('''Class j718{}Class _:___{Var _4_8_9:D1;Destructor (){} }Class s6_:_{Var $A,$U___Q_:E;}Class _:t{Destructor (){} }Class _:__{}''','''Class,j718,{,},Class,_,:,___,{,Var,_4_8_9,:,D1,;,Destructor,(,),{,},},Class,s6_,:,_,{,Var,$A,,,$U___Q_,:,E,;,},Class,_,:,t,{,Destructor,(,),{,},},Class,_,:,__,{,},<EOF>''',101))

    def test_1264(self):
        self.assertTrue(TestLexer.test('''Class E9_8X2__:_{Constructor (){}Constructor (__5_0xC:String ){Continue ;Val y:Array [Array [Array [Array [Int ,89],0X89_F],02],0b1010000];}Val $_n_:String ;}Class _:w5{}''','''Class,E9_8X2__,:,_,{,Constructor,(,),{,},Constructor,(,__5_0xC,:,String,),{,Continue,;,Val,y,:,Array,[,Array,[,Array,[,Array,[,Int,,,89,],,,0X89F,],,,02,],,,0b1010000,],;,},Val,$_n_,:,String,;,},Class,_,:,w5,{,},<EOF>''',101))

    def test_1265(self):
        self.assertTrue(TestLexer.test('''Class u:_g_{Constructor (q,_:B;nX:Float ;r_,cv:Array [Float ,016]){} }Class qQ4{Destructor (){} }Class S_{}Class __q_7Bp{}Class H:_{}Class N6_G_:_{L(){} }''','''Class,u,:,_g_,{,Constructor,(,q,,,_,:,B,;,nX,:,Float,;,r_,,,cv,:,Array,[,Float,,,016,],),{,},},Class,qQ4,{,Destructor,(,),{,},},Class,S_,{,},Class,__q_7Bp,{,},Class,H,:,_,{,},Class,N6_G_,:,_,{,L,(,),{,},},<EOF>''',101))

    def test_1266(self):
        self.assertTrue(TestLexer.test('''Class w8:_{$_2(_,_,p1_:Array [Array [Array [Boolean ,0b1_0],0b1],0B1011010]){}Destructor (){}Val $_1,$1:sG;Val $_,_1:Float ;}''','''Class,w8,:,_,{,$_2,(,_,,,_,,,p1_,:,Array,[,Array,[,Array,[,Boolean,,,0b10,],,,0b1,],,,0B1011010,],),{,},Destructor,(,),{,},Val,$_1,,,$1,:,sG,;,Val,$_,,,_1,:,Float,;,},<EOF>''',101))

    def test_1267(self):
        self.assertTrue(TestLexer.test('''Class __:k{Destructor (){}Constructor (j9:Float ;_,DGj:Float ){} }Class w{}Class _z6_V_:__o_{}Class _{}Class u{}''','''Class,__,:,k,{,Destructor,(,),{,},Constructor,(,j9,:,Float,;,_,,,DGj,:,Float,),{,},},Class,w,{,},Class,_z6_V_,:,__o_,{,},Class,_,{,},Class,u,{,},<EOF>''',101))

    def test_1268(self):
        self.assertTrue(TestLexer.test('''Class _2{Constructor (v:Array [Array [Float ,0b11],80];Z,U,_:Array [String ,0X7_39];X9,T0,X6,_cS,p_oc,B9A:_;n:Int ;_n1u,__,_3,___,_6:Float ){} }Class _:q{Destructor (){}Var $A:_;Var v,$_krF,qo:Array [Array [String ,80],0121];}''','''Class,_2,{,Constructor,(,v,:,Array,[,Array,[,Float,,,0b11,],,,80,],;,Z,,,U,,,_,:,Array,[,String,,,0X739,],;,X9,,,T0,,,X6,,,_cS,,,p_oc,,,B9A,:,_,;,n,:,Int,;,_n1u,,,__,,,_3,,,___,,,_6,:,Float,),{,},},Class,_,:,q,{,Destructor,(,),{,},Var,$A,:,_,;,Var,v,,,$_krF,,,qo,:,Array,[,Array,[,String,,,80,],,,0121,],;,},<EOF>''',101))

    def test_1269(self):
        self.assertTrue(TestLexer.test('''Class _:_lj{}Class _vU_Wg50_:L{Destructor (){Var _:Array [Array [Array [Array [Array [Boolean ,82],0x992],03],72],01];} }''','''Class,_,:,_lj,{,},Class,_vU_Wg50_,:,L,{,Destructor,(,),{,Var,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,82,],,,0x992,],,,03,],,,72,],,,01,],;,},},<EOF>''',101))

    def test_1270(self):
        self.assertTrue(TestLexer.test('''Class Y:u35m0{}Class _k:a{Destructor (){}Val $65,$SjM_,$_jJ:Array [Array [Array [Int ,0b1_10_0],60],070];Destructor (){}Destructor (){} }''','''Class,Y,:,u35m0,{,},Class,_k,:,a,{,Destructor,(,),{,},Val,$65,,,$SjM_,,,$_jJ,:,Array,[,Array,[,Array,[,Int,,,0b1100,],,,60,],,,070,],;,Destructor,(,),{,},Destructor,(,),{,},},<EOF>''',101))

    def test_1271(self):
        self.assertTrue(TestLexer.test('''Class A5_Q:D{Var $8:String ;}Class ___{Val t,$_jPS,_:Float ;Val $w,_,$Ae_,__97_:Array [Array [Array [Float ,78],78],0b111100];}''','''Class,A5_Q,:,D,{,Var,$8,:,String,;,},Class,___,{,Val,t,,,$_jPS,,,_,:,Float,;,Val,$w,,,_,,,$Ae_,,,__97_,:,Array,[,Array,[,Array,[,Float,,,78,],,,78,],,,0b111100,],;,},<EOF>''',101))

    def test_1272(self):
        self.assertTrue(TestLexer.test('''Class _{Destructor (){} }Class Ep__:_v{Constructor (){}Destructor (){ {} }}Class M:_{}Class _:kQ{}Class A:_{Destructor (){} }Class _{}Class b{}''','''Class,_,{,Destructor,(,),{,},},Class,Ep__,:,_v,{,Constructor,(,),{,},Destructor,(,),{,{,},},},Class,M,:,_,{,},Class,_,:,kQ,{,},Class,A,:,_,{,Destructor,(,),{,},},Class,_,{,},Class,b,{,},<EOF>''',101))

    def test_1273(self):
        self.assertTrue(TestLexer.test('''Class _{H_(_,R,_,_58:Array [Array [Array [String ,0b11010],6],0XE];_3_9:Boolean ;i,q8,C,z47_M,_,_9:String ;P,VT70z:M_){} }Class _{}''','''Class,_,{,H_,(,_,,,R,,,_,,,_58,:,Array,[,Array,[,Array,[,String,,,0b11010,],,,6,],,,0XE,],;,_3_9,:,Boolean,;,i,,,q8,,,C,,,z47_M,,,_,,,_9,:,String,;,P,,,VT70z,:,M_,),{,},},Class,_,{,},<EOF>''',101))

    def test_1274(self):
        self.assertTrue(TestLexer.test('''Class __L_z:__{Val _,_,$_,vL__,$_,$9_4:Array [Array [Array [Float ,80],05],07_446_7];Var $9,v___Tv:Array [Boolean ,07];}''','''Class,__L_z,:,__,{,Val,_,,,_,,,$_,,,vL__,,,$_,,,$9_4,:,Array,[,Array,[,Array,[,Float,,,80,],,,05,],,,074467,],;,Var,$9,,,v___Tv,:,Array,[,Boolean,,,07,],;,},<EOF>''',101))

    def test_1275(self):
        self.assertTrue(TestLexer.test('''Class D:s_{}Class _:__{Constructor (){}Constructor (___,E:_;_7:Array [Array [Array [Array [String ,2],0123],0X3A],0X4_A]){} }''','''Class,D,:,s_,{,},Class,_,:,__,{,Constructor,(,),{,},Constructor,(,___,,,E,:,_,;,_7,:,Array,[,Array,[,Array,[,Array,[,String,,,2,],,,0123,],,,0X3A,],,,0X4A,],),{,},},<EOF>''',101))

    def test_1276(self):
        self.assertTrue(TestLexer.test('''Class _Q{}Class _{}Class _1_TY{}Class _k0{Val _,_,_:Array [Boolean ,0b1];$w(S35,i,z:__){}Constructor (){Val j,Y_4x:_x;} }''','''Class,_Q,{,},Class,_,{,},Class,_1_TY,{,},Class,_k0,{,Val,_,,,_,,,_,:,Array,[,Boolean,,,0b1,],;,$w,(,S35,,,i,,,z,:,__,),{,},Constructor,(,),{,Val,j,,,Y_4x,:,_x,;,},},<EOF>''',101))

    def test_1277(self):
        self.assertTrue(TestLexer.test('''Class __:P5_6{}Class h5_:__{Var _,$EO_,$O_,_9:Array [Array [Int ,0X6_C],0B1000001];$p(_:_){Val _:Float ;}Var $E_,$_f_,_:String ;}''','''Class,__,:,P5_6,{,},Class,h5_,:,__,{,Var,_,,,$EO_,,,$O_,,,_9,:,Array,[,Array,[,Int,,,0X6C,],,,0B1000001,],;,$p,(,_,:,_,),{,Val,_,:,Float,;,},Var,$E_,,,$_f_,,,_,:,String,;,},<EOF>''',101))

    def test_1278(self):
        self.assertTrue(TestLexer.test('''Class _:_e7QY477_{Var d64,$1:Array [String ,0B1];Var p67:q;$_1o(){ {} }}Class _:_{$_5_(_218:Boolean ;_:Float ){} }''','''Class,_,:,_e7QY477_,{,Var,d64,,,$1,:,Array,[,String,,,0B1,],;,Var,p67,:,q,;,$_1o,(,),{,{,},},},Class,_,:,_,{,$_5_,(,_218,:,Boolean,;,_,:,Float,),{,},},<EOF>''',101))

    def test_1279(self):
        self.assertTrue(TestLexer.test('''Class _:_08_{Constructor (_J3,ww1,L,g_:Array [Array [Int ,021],0B1_0];p__1,R,_K9:Int ){}p768(_:_8;_T,_,u:Float ){Break ;} }''','''Class,_,:,_08_,{,Constructor,(,_J3,,,ww1,,,L,,,g_,:,Array,[,Array,[,Int,,,021,],,,0B10,],;,p__1,,,R,,,_K9,:,Int,),{,},p768,(,_,:,_8,;,_T,,,_,,,u,:,Float,),{,Break,;,},},<EOF>''',101))

    def test_1280(self):
        self.assertTrue(TestLexer.test('''Class H__f:W_{Val $_:Boolean ;}Class __{Constructor (s:String ;___8,P5,f,_K:Boolean ;_i:Array [Array [Int ,88_52],0b1]){} }''','''Class,H__f,:,W_,{,Val,$_,:,Boolean,;,},Class,__,{,Constructor,(,s,:,String,;,___8,,,P5,,,f,,,_K,:,Boolean,;,_i,:,Array,[,Array,[,Int,,,8852,],,,0b1,],),{,},},<EOF>''',101))

    def test_1281(self):
        self.assertTrue(TestLexer.test('''Class WD_{$8(_:Float ;K8_:Array [Float ,4];B,f,__,Tp,J_1WB_m,_,f,_L:Int ;t0ZA,wb,_0:Boolean ;k_9,_,_:Array [Int ,0B1001000];_:Array [Array [Int ,4],0b1000001];m59_4,_VO:_;T,_v,V:___H_k4){} }Class S5_:_{}''','''Class,WD_,{,$8,(,_,:,Float,;,K8_,:,Array,[,Float,,,4,],;,B,,,f,,,__,,,Tp,,,J_1WB_m,,,_,,,f,,,_L,:,Int,;,t0ZA,,,wb,,,_0,:,Boolean,;,k_9,,,_,,,_,:,Array,[,Int,,,0B1001000,],;,_,:,Array,[,Array,[,Int,,,4,],,,0b1000001,],;,m59_4,,,_VO,:,_,;,T,,,_v,,,V,:,___H_k4,),{,},},Class,S5_,:,_,{,},<EOF>''',101))

    def test_1282(self):
        self.assertTrue(TestLexer.test('''Class _:_s{$5__(){}$8(K:Array [Float ,0115];_q,W,N,_:Int ;_:Array [Array [String ,0115],0B10110]){}Val $5i_K_3,$_:_25;_(_o,_,Q9_:_;o:Int ;__,_6:Array [Array [Array [Array [Int ,01],0b10],0b1010100],0X4_4_1]){} }Class _{}Class a_1_:_S{}''','''Class,_,:,_s,{,$5__,(,),{,},$8,(,K,:,Array,[,Float,,,0115,],;,_q,,,W,,,N,,,_,:,Int,;,_,:,Array,[,Array,[,String,,,0115,],,,0B10110,],),{,},Val,$5i_K_3,,,$_,:,_25,;,_,(,_o,,,_,,,Q9_,:,_,;,o,:,Int,;,__,,,_6,:,Array,[,Array,[,Array,[,Array,[,Int,,,01,],,,0b10,],,,0b1010100,],,,0X441,],),{,},},Class,_,{,},Class,a_1_,:,_S,{,},<EOF>''',101))

    def test_1283(self):
        self.assertTrue(TestLexer.test('''Class __g:_y0_{Var $j,$1:h;Var F,M8K_6,_6,__:Float ;Val $4_,R,e6,$0:Array [String ,6];Constructor (___:_F;_:_82_){} }''','''Class,__g,:,_y0_,{,Var,$j,,,$1,:,h,;,Var,F,,,M8K_6,,,_6,,,__,:,Float,;,Val,$4_,,,R,,,e6,,,$0,:,Array,[,String,,,6,],;,Constructor,(,___,:,_F,;,_,:,_82_,),{,},},<EOF>''',101))

    def test_1284(self):
        self.assertTrue(TestLexer.test('''Class E1_Je0:M__{$r(_:Boolean ;_1,__g,d7_M,_:String ){} }Class _:_{}Class _8{}Class _:__u_{}Class n{Var $C:_;}''','''Class,E1_Je0,:,M__,{,$r,(,_,:,Boolean,;,_1,,,__g,,,d7_M,,,_,:,String,),{,},},Class,_,:,_,{,},Class,_8,{,},Class,_,:,__u_,{,},Class,n,{,Var,$C,:,_,;,},<EOF>''',101))

    def test_1285(self):
        self.assertTrue(TestLexer.test('''Class gJ:__R0{Constructor (){Continue ;yd_::$4_();}Var _8_:___8;Var $5,X_:Array [String ,065];Constructor (){} }''','''Class,gJ,:,__R0,{,Constructor,(,),{,Continue,;,yd_,::,$4_,(,),;,},Var,_8_,:,___8,;,Var,$5,,,X_,:,Array,[,String,,,065,],;,Constructor,(,),{,},},<EOF>''',101))

    def test_1286(self):
        self.assertTrue(TestLexer.test('''Class w:KH{Constructor (US7,t,_8ul_,t,_:kc;__:_3;_,_3:Boolean ;_:Array [Array [Array [String ,0B1_10_1],02],06]){} }''','''Class,w,:,KH,{,Constructor,(,US7,,,t,,,_8ul_,,,t,,,_,:,kc,;,__,:,_3,;,_,,,_3,:,Boolean,;,_,:,Array,[,Array,[,Array,[,String,,,0B1101,],,,02,],,,06,],),{,},},<EOF>''',101))

    def test_1287(self):
        self.assertTrue(TestLexer.test('''Class Elx:r{Var T_2,$5_:Float ;Constructor (w7,P:Array [String ,0x14]){} }Class _:D_3{}Class _f__G{Destructor (){}Destructor (){} }''','''Class,Elx,:,r,{,Var,T_2,,,$5_,:,Float,;,Constructor,(,w7,,,P,:,Array,[,String,,,0x14,],),{,},},Class,_,:,D_3,{,},Class,_f__G,{,Destructor,(,),{,},Destructor,(,),{,},},<EOF>''',101))

    def test_1288(self):
        self.assertTrue(TestLexer.test('''Class Z:U{Constructor (_0,m,_3:Float ;__:Float ;ZB:Array [Array [Array [Float ,0b110101],0b10_0_01],06131544]){} }Class C63:xv_G{Val $6414ZB:_;Constructor (){} }''','''Class,Z,:,U,{,Constructor,(,_0,,,m,,,_3,:,Float,;,__,:,Float,;,ZB,:,Array,[,Array,[,Array,[,Float,,,0b110101,],,,0b10001,],,,06131544,],),{,},},Class,C63,:,xv_G,{,Val,$6414ZB,:,_,;,Constructor,(,),{,},},<EOF>''',101))

    def test_1289(self):
        self.assertTrue(TestLexer.test('''Class _:_{}Class F_:_{}Class dH:_{Val Ze:Array [Array [String ,0B1],43];Destructor (){}Destructor (){} }Class _a{}''','''Class,_,:,_,{,},Class,F_,:,_,{,},Class,dH,:,_,{,Val,Ze,:,Array,[,Array,[,String,,,0B1,],,,43,],;,Destructor,(,),{,},Destructor,(,),{,},},Class,_a,{,},<EOF>''',101))

    def test_1290(self):
        self.assertTrue(TestLexer.test('''Class _:_75_{Var D2:Boolean ;Constructor (D__Z,_,j_F,W_:Array [Array [Int ,0X15],55_1];f,_:Array [Boolean ,0B1];w_,f:_){ {} }Destructor (){}$___(){Continue ;} }Class _:T95_9{Val _Fb1,_28,_s,h,$_9,$___1:Array [Int ,44_8_6];Val _:Oj;Val $254:String ;}''','''Class,_,:,_75_,{,Var,D2,:,Boolean,;,Constructor,(,D__Z,,,_,,,j_F,,,W_,:,Array,[,Array,[,Int,,,0X15,],,,551,],;,f,,,_,:,Array,[,Boolean,,,0B1,],;,w_,,,f,:,_,),{,{,},},Destructor,(,),{,},$___,(,),{,Continue,;,},},Class,_,:,T95_9,{,Val,_Fb1,,,_28,,,_s,,,h,,,$_9,,,$___1,:,Array,[,Int,,,4486,],;,Val,_,:,Oj,;,Val,$254,:,String,;,},<EOF>''',101))

    def test_1291(self):
        self.assertTrue(TestLexer.test('''Class Og{}Class _{Var _R__E,$_,$_P:Array [Array [Int ,0X2E],0X31E];MV(_:Array [Array [Array [Array [Float ,0x63],0X2],5],03_1_1126]){}Var $7z:Boolean ;}''','''Class,Og,{,},Class,_,{,Var,_R__E,,,$_,,,$_P,:,Array,[,Array,[,Int,,,0X2E,],,,0X31E,],;,MV,(,_,:,Array,[,Array,[,Array,[,Array,[,Float,,,0x63,],,,0X2,],,,5,],,,0311126,],),{,},Var,$7z,:,Boolean,;,},<EOF>''',101))

    def test_1292(self):
        self.assertTrue(TestLexer.test('''Class fA:V{}Class Q:L{Destructor (){}Val kS,$m_,f_5,__2_ltMN:Array [Int ,0x35];Var $cS:Array [Float ,0X10];Var VR81:_1;Constructor (m,_:Y1_;_,_i,_:Array [Array [Array [Array [Array [Int ,0X10],0563_3],48],05_5],7_4_2];hh,_S:Array [Array [Array [Array [Array [String ,3],0122],48],0B111111],34_2_7];_k6:Array [Int ,48];M,_5R:String ;p_,_:Array [Array [Array [Int ,0122],5_60],0b1];Rk:zJU6){}Val $o210:Array [Array [Float ,0xD_D],0B111111];Constructor (X_:Boolean ){}Constructor (){Var _St27_7:_;} }''','''Class,fA,:,V,{,},Class,Q,:,L,{,Destructor,(,),{,},Val,kS,,,$m_,,,f_5,,,__2_ltMN,:,Array,[,Int,,,0x35,],;,Var,$cS,:,Array,[,Float,,,0X10,],;,Var,VR81,:,_1,;,Constructor,(,m,,,_,:,Y1_,;,_,,,_i,,,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0X10,],,,05633,],,,48,],,,055,],,,742,],;,hh,,,_S,:,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,3,],,,0122,],,,48,],,,0B111111,],,,3427,],;,_k6,:,Array,[,Int,,,48,],;,M,,,_5R,:,String,;,p_,,,_,:,Array,[,Array,[,Array,[,Int,,,0122,],,,560,],,,0b1,],;,Rk,:,zJU6,),{,},Val,$o210,:,Array,[,Array,[,Float,,,0xDD,],,,0B111111,],;,Constructor,(,X_,:,Boolean,),{,},Constructor,(,),{,Var,_St27_7,:,_,;,},},<EOF>''',101))

    def test_1293(self):
        self.assertTrue(TestLexer.test('''Class _{$6_(_:Int ;_6:Array [Array [Array [Array [Array [Array [Int ,015],0B101],81],5],0x52],90]){}$3_4(){} }Class _:_7_56d_Jf___{$8(){} }Class _5_0:_6_R{Constructor (){} }''','''Class,_,{,$6_,(,_,:,Int,;,_6,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,015,],,,0B101,],,,81,],,,5,],,,0x52,],,,90,],),{,},$3_4,(,),{,},},Class,_,:,_7_56d_Jf___,{,$8,(,),{,},},Class,_5_0,:,_6_R,{,Constructor,(,),{,},},<EOF>''',101))

    def test_1294(self):
        self.assertTrue(TestLexer.test('''Class y_:_{}Class i4_{_Sw(a,_,_T,mz,f_,_:Array [String ,017];_,_y_:Float ;l:T;k,_,L,_B2_W,_hiW,V_,f_,Z_3_9,___:l;W1:w2){} }Class _:_{}''','''Class,y_,:,_,{,},Class,i4_,{,_Sw,(,a,,,_,,,_T,,,mz,,,f_,,,_,:,Array,[,String,,,017,],;,_,,,_y_,:,Float,;,l,:,T,;,k,,,_,,,L,,,_B2_W,,,_hiW,,,V_,,,f_,,,Z_3_9,,,___,:,l,;,W1,:,w2,),{,},},Class,_,:,_,{,},<EOF>''',101))

    def test_1295(self):
        self.assertTrue(TestLexer.test('''Class b:_q2{Constructor (){}Var $_,_e,j,V3,$_,_x4:Float ;_7(_:Boolean ){Continue ;}Var $09,$_e,_,$gni,O,_,$_:Array [Float ,0b10];Var C6Yi,h_,$_c,_:Array [Boolean ,0B1];Constructor (_:Array [Array [Float ,0X1B],0B1]){}Destructor (){}Destructor (){_S50704::$_8.f.R_()._5();}Constructor (Myo,N:Array [Boolean ,0b101_0_011_0010];c:Int ){} }Class _8_{Constructor (__:Array [Int ,0B1010100];_f,_3eZ___:Array [Float ,8_3]){__::$1();} }''','''Class,b,:,_q2,{,Constructor,(,),{,},Var,$_,,,_e,,,j,,,V3,,,$_,,,_x4,:,Float,;,_7,(,_,:,Boolean,),{,Continue,;,},Var,$09,,,$_e,,,_,,,$gni,,,O,,,_,,,$_,:,Array,[,Float,,,0b10,],;,Var,C6Yi,,,h_,,,$_c,,,_,:,Array,[,Boolean,,,0B1,],;,Constructor,(,_,:,Array,[,Array,[,Float,,,0X1B,],,,0B1,],),{,},Destructor,(,),{,},Destructor,(,),{,_S50704,::,$_8,.,f,.,R_,(,),.,_5,(,),;,},Constructor,(,Myo,,,N,:,Array,[,Boolean,,,0b10100110010,],;,c,:,Int,),{,},},Class,_8_,{,Constructor,(,__,:,Array,[,Int,,,0B1010100,],;,_f,,,_3eZ___,:,Array,[,Float,,,83,],),{,__,::,$1,(,),;,},},<EOF>''',101))

    def test_1296(self):
        self.assertTrue(TestLexer.test('''Class Q{Constructor (_:_;P,_8,C:Int ){Continue ;}Val $90,_:_;Constructor (__,_,X:z_){} }Class __X_:_{}Class _:_{}Class u{}''','''Class,Q,{,Constructor,(,_,:,_,;,P,,,_8,,,C,:,Int,),{,Continue,;,},Val,$90,,,_,:,_,;,Constructor,(,__,,,_,,,X,:,z_,),{,},},Class,__X_,:,_,{,},Class,_,:,_,{,},Class,u,{,},<EOF>''',101))

    def test_1297(self):
        self.assertTrue(TestLexer.test('''Class Voq{Val P,$av,t,_Bu_V,$82,__:Array [Array [Array [Array [Array [Boolean ,0xC],7_4_7],0b11111],0B1011101],6];Var $j:Array [Boolean ,0xB];}''','''Class,Voq,{,Val,P,,,$av,,,t,,,_Bu_V,,,$82,,,__,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0xC,],,,747,],,,0b11111,],,,0B1011101,],,,6,],;,Var,$j,:,Array,[,Boolean,,,0xB,],;,},<EOF>''',101))

    def test_1298(self):
        self.assertTrue(TestLexer.test('''Class Nn{}Class HQ{Constructor (){}Var $__s:Array [Array [Array [Array [Array [Array [Int ,0X29],0X1],0x94C],0B1111],0x5],052];}''','''Class,Nn,{,},Class,HQ,{,Constructor,(,),{,},Var,$__s,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0X29,],,,0X1,],,,0x94C,],,,0B1111,],,,0x5,],,,052,],;,},<EOF>''',101))

    def test_1299(self):
        self.assertTrue(TestLexer.test('''Class _7{Var $_C:Boolean ;Constructor (_:Array [Boolean ,0xB];_,_,_V:Boolean ){Break ;Return ;}Constructor (){}Destructor (){Break ;} }''','''Class,_7,{,Var,$_C,:,Boolean,;,Constructor,(,_,:,Array,[,Boolean,,,0xB,],;,_,,,_,,,_V,:,Boolean,),{,Break,;,Return,;,},Constructor,(,),{,},Destructor,(,),{,Break,;,},},<EOF>''',101))

    def test_1300(self):
        self.assertTrue(TestLexer.test('''Class E91y8R:x_{Constructor (Q_:A8_;_:Array [Array [Array [Array [Array [Float ,0x1],06],07_525_53],052],1]){} }Class op{Val u:Array [Array [Array [Array [String ,0b110],0b1010001],052],05];}Class N{}Class _{}''','''Class,E91y8R,:,x_,{,Constructor,(,Q_,:,A8_,;,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0x1,],,,06,],,,0752553,],,,052,],,,1,],),{,},},Class,op,{,Val,u,:,Array,[,Array,[,Array,[,Array,[,String,,,0b110,],,,0b1010001,],,,052,],,,05,],;,},Class,N,{,},Class,_,{,},<EOF>''',101))

    def test_1301(self):
        self.assertTrue(TestLexer.test('''Class _{}Class H{}Class _:Q1_{Val __:Array [Array [Boolean ,0B1110_0],01_1_6];Constructor (_,_L:Array [Boolean ,0B1011];_____:Array [Float ,0B1]){}Val q:eh33;}''','''Class,_,{,},Class,H,{,},Class,_,:,Q1_,{,Val,__,:,Array,[,Array,[,Boolean,,,0B11100,],,,0116,],;,Constructor,(,_,,,_L,:,Array,[,Boolean,,,0B1011,],;,_____,:,Array,[,Float,,,0B1,],),{,},Val,q,:,eh33,;,},<EOF>''',101))

    def test_1302(self):
        self.assertTrue(TestLexer.test('''Class BU{Val y,$_:Oj81;Var $d3_,$Tf,X28,_:Array [Array [Array [Boolean ,053],11],7_3];$_(g,_,X,__,U:g3A1;_c,_,ZL1,_:B_g){} }Class _88{}Class _:_{}Class b:u_{}''','''Class,BU,{,Val,y,,,$_,:,Oj81,;,Var,$d3_,,,$Tf,,,X28,,,_,:,Array,[,Array,[,Array,[,Boolean,,,053,],,,11,],,,73,],;,$_,(,g,,,_,,,X,,,__,,,U,:,g3A1,;,_c,,,_,,,ZL1,,,_,:,B_g,),{,},},Class,_88,{,},Class,_,:,_,{,},Class,b,:,u_,{,},<EOF>''',101))

    def test_1303(self):
        self.assertTrue(TestLexer.test('''Class t{Var $42a69,_,z_:Array [Boolean ,0X4_D];_(f__M1Z:k;_HB,_:S){}Constructor (){} }Class _:v1{Val _iX__5y6__M___R1F:Float ;Constructor (y9_:_){} }''','''Class,t,{,Var,$42a69,,,_,,,z_,:,Array,[,Boolean,,,0X4D,],;,_,(,f__M1Z,:,k,;,_HB,,,_,:,S,),{,},Constructor,(,),{,},},Class,_,:,v1,{,Val,_iX__5y6__M___R1F,:,Float,;,Constructor,(,y9_,:,_,),{,},},<EOF>''',101))

    def test_1304(self):
        self.assertTrue(TestLexer.test('''Class J{}Class _:u0{Constructor (_,c5,Tk:b6C_;_,L:w_0;q__,_,E:Int ;B1,_,a,_f:Array [String ,0b11101]){} }Class I_{}''','''Class,J,{,},Class,_,:,u0,{,Constructor,(,_,,,c5,,,Tk,:,b6C_,;,_,,,L,:,w_0,;,q__,,,_,,,E,:,Int,;,B1,,,_,,,a,,,_f,:,Array,[,String,,,0b11101,],),{,},},Class,I_,{,},<EOF>''',101))

    def test_1305(self):
        self.assertTrue(TestLexer.test('''Class _:_{}Class _p_k_:_{Destructor (){}Constructor (c:Array [Array [Boolean ,2],0xE];r7:Array [Boolean ,0B1]){} }''','''Class,_,:,_,{,},Class,_p_k_,:,_,{,Destructor,(,),{,},Constructor,(,c,:,Array,[,Array,[,Boolean,,,2,],,,0xE,],;,r7,:,Array,[,Boolean,,,0B1,],),{,},},<EOF>''',101))

    def test_1306(self):
        self.assertTrue(TestLexer.test('''Class _H88{Constructor (){}Constructor (M:String ;_j:Array [Int ,0XD_55_8_8]){}Constructor (){D::$5_();} }Class _:m{Var _:d;}''','''Class,_H88,{,Constructor,(,),{,},Constructor,(,M,:,String,;,_j,:,Array,[,Int,,,0XD5588,],),{,},Constructor,(,),{,D,::,$5_,(,),;,},},Class,_,:,m,{,Var,_,:,d,;,},<EOF>''',101))

    def test_1307(self):
        self.assertTrue(TestLexer.test('''Class A:_{Destructor (){} }Class J{Constructor (_:String ;_v,_:Array [Array [Array [Int ,0X1],032],0X596];_:_T){} }Class _:u_{}Class B9_j6{Constructor (){} }''','''Class,A,:,_,{,Destructor,(,),{,},},Class,J,{,Constructor,(,_,:,String,;,_v,,,_,:,Array,[,Array,[,Array,[,Int,,,0X1,],,,032,],,,0X596,],;,_,:,_T,),{,},},Class,_,:,u_,{,},Class,B9_j6,{,Constructor,(,),{,},},<EOF>''',101))

    def test_1308(self):
        self.assertTrue(TestLexer.test('''Class _:Uy{h(BI:Array [Array [Array [Array [Array [Boolean ,85227_0],2],45],0XE],0b1010];P_:CG){}Val c_5H,M_:Array [Array [Array [String ,0664],0B1],0X5D];$_F2(_:d_){New X()._().gY();{Return ;} }}Class _:D6{}''','''Class,_,:,Uy,{,h,(,BI,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,852270,],,,2,],,,45,],,,0XE,],,,0b1010,],;,P_,:,CG,),{,},Val,c_5H,,,M_,:,Array,[,Array,[,Array,[,String,,,0664,],,,0B1,],,,0X5D,],;,$_F2,(,_,:,d_,),{,New,X,(,),.,_,(,),.,gY,(,),;,{,Return,;,},},},Class,_,:,D6,{,},<EOF>''',101))

    def test_1309(self):
        self.assertTrue(TestLexer.test('''Class _:L{$M(Sd,e,_,_672P:Float ;_,C3_:_;e:Int ;_h,_:Array [Boolean ,8_1];a:Boolean ;_:T_p;J,R,_:Int ;t,_:Array [Array [Boolean ,40],0x5F]){} }''','''Class,_,:,L,{,$M,(,Sd,,,e,,,_,,,_672P,:,Float,;,_,,,C3_,:,_,;,e,:,Int,;,_h,,,_,:,Array,[,Boolean,,,81,],;,a,:,Boolean,;,_,:,T_p,;,J,,,R,,,_,:,Int,;,t,,,_,:,Array,[,Array,[,Boolean,,,40,],,,0x5F,],),{,},},<EOF>''',101))

    def test_1310(self):
        self.assertTrue(TestLexer.test('''Class _{}Class _:__{Constructor (_Jh,yKZ92,_8K1w:__zT7e){}Destructor (){Continue ;Break ;Var _,E6E1,CF:Boolean ;} }Class o8{}Class Od:L{}''','''Class,_,{,},Class,_,:,__,{,Constructor,(,_Jh,,,yKZ92,,,_8K1w,:,__zT7e,),{,},Destructor,(,),{,Continue,;,Break,;,Var,_,,,E6E1,,,CF,:,Boolean,;,},},Class,o8,{,},Class,Od,:,L,{,},<EOF>''',101))

    def test_1311(self):
        self.assertTrue(TestLexer.test('''Class _6jx:_{Constructor (_,__,bF:Array [Array [String ,0b101100],051];_:Boolean ;bQ52,F,_:Array [Array [Array [Boolean ,0b1_1_0],0741_4],80]){} }''','''Class,_6jx,:,_,{,Constructor,(,_,,,__,,,bF,:,Array,[,Array,[,String,,,0b101100,],,,051,],;,_,:,Boolean,;,bQ52,,,F,,,_,:,Array,[,Array,[,Array,[,Boolean,,,0b110,],,,07414,],,,80,],),{,},},<EOF>''',101))

    def test_1312(self):
        self.assertTrue(TestLexer.test('''Class _:_{__(l,__w___:Array [Array [String ,8],014]){} }Class G:V5{Constructor (){Break ;} }Class _{Var $n:String ;}Class C{}Class __N{}Class s_:k{}Class _3:_{}Class D{_1(G,_G,_4z,X9_e:Array [Array [Int ,0x88E_40],59]){} }Class N:_s{}''','''Class,_,:,_,{,__,(,l,,,__w___,:,Array,[,Array,[,String,,,8,],,,014,],),{,},},Class,G,:,V5,{,Constructor,(,),{,Break,;,},},Class,_,{,Var,$n,:,String,;,},Class,C,{,},Class,__N,{,},Class,s_,:,k,{,},Class,_3,:,_,{,},Class,D,{,_1,(,G,,,_G,,,_4z,,,X9_e,:,Array,[,Array,[,Int,,,0x88E40,],,,59,],),{,},},Class,N,:,_s,{,},<EOF>''',101))

    def test_1313(self):
        self.assertTrue(TestLexer.test('''Class _CgX4X:kN{Constructor (){} }Class __{}Class P2_:_y{}Class __:__{}Class _:J{}Class l{}Class _:_{}Class _:O_{a(h:Float ;_F:Array [Float ,0b1]){Continue ;_l9::$J();} }''','''Class,_CgX4X,:,kN,{,Constructor,(,),{,},},Class,__,{,},Class,P2_,:,_y,{,},Class,__,:,__,{,},Class,_,:,J,{,},Class,l,{,},Class,_,:,_,{,},Class,_,:,O_,{,a,(,h,:,Float,;,_F,:,Array,[,Float,,,0b1,],),{,Continue,;,_l9,::,$J,(,),;,},},<EOF>''',101))

    def test_1314(self):
        self.assertTrue(TestLexer.test('''Class y:_{}Class _d:k_{}Class v1q6___:N{X_(_8x_,W6:Boolean ;__,u,_:v){Var _:Int ;{} }}Class A{Val $1,$_,$J:Int ;}Class _:P_6{}Class ____:_45v_s7{}Class _{}''','''Class,y,:,_,{,},Class,_d,:,k_,{,},Class,v1q6___,:,N,{,X_,(,_8x_,,,W6,:,Boolean,;,__,,,u,,,_,:,v,),{,Var,_,:,Int,;,{,},},},Class,A,{,Val,$1,,,$_,,,$J,:,Int,;,},Class,_,:,P_6,{,},Class,____,:,_45v_s7,{,},Class,_,{,},<EOF>''',101))

    def test_1315(self):
        self.assertTrue(TestLexer.test('''Class U52Vt:__uw_S{$Q3H(J__8C,p7C,C__6_,__:Int ;I,R_:Array [Array [Boolean ,0b1],0B100001];S:_i){L_::$S();Continue ;} }''','''Class,U52Vt,:,__uw_S,{,$Q3H,(,J__8C,,,p7C,,,C__6_,,,__,:,Int,;,I,,,R_,:,Array,[,Array,[,Boolean,,,0b1,],,,0B100001,],;,S,:,_i,),{,L_,::,$S,(,),;,Continue,;,},},<EOF>''',101))

    def test_1316(self):
        self.assertTrue(TestLexer.test('''Class __{}Class _3a6{D(I,A:f___5_;_719F4,r,_,_z,_,y:Array [Boolean ,074]){Continue ;Var k:Array [Array [String ,52],0x24];Val l:Array [Array [Boolean ,52],0X4];}Constructor (){} }Class L{}''','''Class,__,{,},Class,_3a6,{,D,(,I,,,A,:,f___5_,;,_719F4,,,r,,,_,,,_z,,,_,,,y,:,Array,[,Boolean,,,074,],),{,Continue,;,Var,k,:,Array,[,Array,[,String,,,52,],,,0x24,],;,Val,l,:,Array,[,Array,[,Boolean,,,52,],,,0X4,],;,},Constructor,(,),{,},},Class,L,{,},<EOF>''',101))

    def test_1317(self):
        self.assertTrue(TestLexer.test('''Class S:A{a(_,_:__;N:Boolean ;K,S_o:_K;vzS72R,Hse,__L_:Float ;f:v;_2__3:___;_,_MD_,_u:Array [Array [String ,01_2],0127];P,A,_:Array [Array [Boolean ,4],44]){} }Class g8874{}''','''Class,S,:,A,{,a,(,_,,,_,:,__,;,N,:,Boolean,;,K,,,S_o,:,_K,;,vzS72R,,,Hse,,,__L_,:,Float,;,f,:,v,;,_2__3,:,___,;,_,,,_MD_,,,_u,:,Array,[,Array,[,String,,,012,],,,0127,],;,P,,,A,,,_,:,Array,[,Array,[,Boolean,,,4,],,,44,],),{,},},Class,g8874,{,},<EOF>''',101))

    def test_1318(self):
        self.assertTrue(TestLexer.test('''Class KC__{}Class _150a_{Constructor (I,T_:Int ;q,_soK,D:Float ;G5,_:Float ;_:o;h0773_5y,n:Array [Boolean ,01_0];_:Array [Array [Int ,0104],0104];_z4_,Y6,_:Boolean ;_:Z){} }''','''Class,KC__,{,},Class,_150a_,{,Constructor,(,I,,,T_,:,Int,;,q,,,_soK,,,D,:,Float,;,G5,,,_,:,Float,;,_,:,o,;,h0773_5y,,,n,:,Array,[,Boolean,,,010,],;,_,:,Array,[,Array,[,Int,,,0104,],,,0104,],;,_z4_,,,Y6,,,_,:,Boolean,;,_,:,Z,),{,},},<EOF>''',101))

    def test_1319(self):
        self.assertTrue(TestLexer.test('''Class _{Val v_,__:Array [Boolean ,0X3F];Constructor (_,_,r,_:Int ;m:__;f:Array [String ,0X3F]){} }Class _{}Class _:_{}Class _:m_9_{}''','''Class,_,{,Val,v_,,,__,:,Array,[,Boolean,,,0X3F,],;,Constructor,(,_,,,_,,,r,,,_,:,Int,;,m,:,__,;,f,:,Array,[,String,,,0X3F,],),{,},},Class,_,{,},Class,_,:,_,{,},Class,_,:,m_9_,{,},<EOF>''',101))

    def test_1320(self):
        self.assertTrue(TestLexer.test('''Class __r:_{}Class G_:__{Var $_,_:e;Val NB:Array [Boolean ,0X5C];}Class _:rI{}Class y_{}Class _7_V{Destructor (){} }''','''Class,__r,:,_,{,},Class,G_,:,__,{,Var,$_,,,_,:,e,;,Val,NB,:,Array,[,Boolean,,,0X5C,],;,},Class,_,:,rI,{,},Class,y_,{,},Class,_7_V,{,Destructor,(,),{,},},<EOF>''',101))

    def test_1321(self):
        self.assertTrue(TestLexer.test('''Class _{Var _1,$418,$_1d1Z:Array [Array [Array [Array [Int ,0b1_0],38],0x4],06];}Class _:L{}Class _OK:W5{}Class _1_{}''','''Class,_,{,Var,_1,,,$418,,,$_1d1Z,:,Array,[,Array,[,Array,[,Array,[,Int,,,0b10,],,,38,],,,0x4,],,,06,],;,},Class,_,:,L,{,},Class,_OK,:,W5,{,},Class,_1_,{,},<EOF>''',101))

    def test_1322(self):
        self.assertTrue(TestLexer.test('''Class b3aX_2_{Var $3,_u5o:Float ;Constructor (J_:Float ;Ss,_6:Array [Array [Array [Boolean ,01],3_8],1];_bi81:Array [Int ,0xB];_V:Int ){}Constructor (vT_L,_:Array [Array [Array [Int ,0101],0B1001011],0XA_1]){Return ;} }''','''Class,b3aX_2_,{,Var,$3,,,_u5o,:,Float,;,Constructor,(,J_,:,Float,;,Ss,,,_6,:,Array,[,Array,[,Array,[,Boolean,,,01,],,,38,],,,1,],;,_bi81,:,Array,[,Int,,,0xB,],;,_V,:,Int,),{,},Constructor,(,vT_L,,,_,:,Array,[,Array,[,Array,[,Int,,,0101,],,,0B1001011,],,,0XA1,],),{,Return,;,},},<EOF>''',101))

    def test_1323(self):
        self.assertTrue(TestLexer.test('''Class p:i4_{Destructor (){Continue ;} }Class f:_{Var $_,_,u:Array [Array [Array [Array [Array [Array [String ,71],0X51],0b1],9_5],0x2C],3_8];}Class V:_{}''','''Class,p,:,i4_,{,Destructor,(,),{,Continue,;,},},Class,f,:,_,{,Var,$_,,,_,,,u,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,71,],,,0X51,],,,0b1,],,,95,],,,0x2C,],,,38,],;,},Class,V,:,_,{,},<EOF>''',101))

    def test_1324(self):
        self.assertTrue(TestLexer.test('''Class hY:_{}Class w{}Class x{}Class n651b_:___{$0(Y_:Array [Boolean ,17];_,_,_:_50;_,c6:Array [Boolean ,0B100110]){}Val $_:Array [Array [Int ,17],17];}''','''Class,hY,:,_,{,},Class,w,{,},Class,x,{,},Class,n651b_,:,___,{,$0,(,Y_,:,Array,[,Boolean,,,17,],;,_,,,_,,,_,:,_50,;,_,,,c6,:,Array,[,Boolean,,,0B100110,],),{,},Val,$_,:,Array,[,Array,[,Int,,,17,],,,17,],;,},<EOF>''',101))

    def test_1325(self):
        self.assertTrue(TestLexer.test('''Class cH_:o{U_(){}_(Q,_0_0:_3;_B:Float ;_4_9,z:String ){}Var $8Fl7_6,_:q;Constructor (v_,f:_0){Return ;}Constructor (_iP5__,C,U:Boolean ;mj,_l_4Hvr,_,x3,__0z_:m_;_,_83,__jz,g:Boolean ;N2o_,i_:Array [Array [Array [Array [Array [Float ,89],051],0B1_0_0],0116],89];z_5:Array [Boolean ,6]){Var N:F;{} }}''','''Class,cH_,:,o,{,U_,(,),{,},_,(,Q,,,_0_0,:,_3,;,_B,:,Float,;,_4_9,,,z,:,String,),{,},Var,$8Fl7_6,,,_,:,q,;,Constructor,(,v_,,,f,:,_0,),{,Return,;,},Constructor,(,_iP5__,,,C,,,U,:,Boolean,;,mj,,,_l_4Hvr,,,_,,,x3,,,__0z_,:,m_,;,_,,,_83,,,__jz,,,g,:,Boolean,;,N2o_,,,i_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,89,],,,051,],,,0B100,],,,0116,],,,89,],;,z_5,:,Array,[,Boolean,,,6,],),{,Var,N,:,F,;,{,},},},<EOF>''',101))

    def test_1326(self):
        self.assertTrue(TestLexer.test('''Class U{Var $_:Array [Array [Array [Array [Int ,0b10],0B1_1_1111],86],0B1];Val $9___J:Array [Int ,0b110101];_z(){Break ;} }''','''Class,U,{,Var,$_,:,Array,[,Array,[,Array,[,Array,[,Int,,,0b10,],,,0B111111,],,,86,],,,0B1,],;,Val,$9___J,:,Array,[,Int,,,0b110101,],;,_z,(,),{,Break,;,},},<EOF>''',101))

    def test_1327(self):
        self.assertTrue(TestLexer.test('''Class F:_{$_3(_,O_659_4:_i){Break ;} }Class d:o{_(){}$1(M5,__,_Ga:_;_,hx1,_2E,_,_,h:Array [Boolean ,02]){} }Class _:_{}''','''Class,F,:,_,{,$_3,(,_,,,O_659_4,:,_i,),{,Break,;,},},Class,d,:,o,{,_,(,),{,},$1,(,M5,,,__,,,_Ga,:,_,;,_,,,hx1,,,_2E,,,_,,,_,,,h,:,Array,[,Boolean,,,02,],),{,},},Class,_,:,_,{,},<EOF>''',101))

    def test_1328(self):
        self.assertTrue(TestLexer.test('''Class l4__I:z{__46_(_,q,XX_t3_,__4,_l:_;_6,_:Array [Array [Float ,0B110111],0125];e,__350,Tf,Y:Array [Array [Array [Array [Array [Int ,0XD],67],0125],0X2],4_1_9];_E:Int ){} }''','''Class,l4__I,:,z,{,__46_,(,_,,,q,,,XX_t3_,,,__4,,,_l,:,_,;,_6,,,_,:,Array,[,Array,[,Float,,,0B110111,],,,0125,],;,e,,,__350,,,Tf,,,Y,:,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0XD,],,,67,],,,0125,],,,0X2,],,,419,],;,_E,:,Int,),{,},},<EOF>''',101))

    def test_1329(self):
        self.assertTrue(TestLexer.test('''Class ___9:_{}Class __{Var $_6i,_,$_:Float ;$v(){Continue ;} }Class HN{}Class ps{Destructor (){} }Class _:_{Constructor (){} }''','''Class,___9,:,_,{,},Class,__,{,Var,$_6i,,,_,,,$_,:,Float,;,$v,(,),{,Continue,;,},},Class,HN,{,},Class,ps,{,Destructor,(,),{,},},Class,_,:,_,{,Constructor,(,),{,},},<EOF>''',101))

    def test_1330(self):
        self.assertTrue(TestLexer.test('''Class _7:_{$628w(c0_s_:Array [Array [Boolean ,0XF1],6_92];m_:Boolean ;e,_5,V:u_d;Iv8,_:Array [Float ,0xCB9];__,A:Int ){} }''','''Class,_7,:,_,{,$628w,(,c0_s_,:,Array,[,Array,[,Boolean,,,0XF1,],,,692,],;,m_,:,Boolean,;,e,,,_5,,,V,:,u_d,;,Iv8,,,_,:,Array,[,Float,,,0xCB9,],;,__,,,A,:,Int,),{,},},<EOF>''',101))

    def test_1331(self):
        self.assertTrue(TestLexer.test('''Class FE_{Destructor (){}Var C,$v8:Array [String ,06];Constructor (A:_6__;g2,_4q_:Array [Array [Boolean ,0b10000],0B10100];N:Float ;_:Float ){} }''','''Class,FE_,{,Destructor,(,),{,},Var,C,,,$v8,:,Array,[,String,,,06,],;,Constructor,(,A,:,_6__,;,g2,,,_4q_,:,Array,[,Array,[,Boolean,,,0b10000,],,,0B10100,],;,N,:,Float,;,_,:,Float,),{,},},<EOF>''',101))

    def test_1332(self):
        self.assertTrue(TestLexer.test('''Class _{Var _969D_,$__1,_4_:Array [Array [Boolean ,0b10000],0132];Constructor (_,_:Boolean ;tk,_8n0,_Iq,_,p7,Q,_3_,_:_){} }''','''Class,_,{,Var,_969D_,,,$__1,,,_4_,:,Array,[,Array,[,Boolean,,,0b10000,],,,0132,],;,Constructor,(,_,,,_,:,Boolean,;,tk,,,_8n0,,,_Iq,,,_,,,p7,,,Q,,,_3_,,,_,:,_,),{,},},<EOF>''',101))

    def test_1333(self):
        self.assertTrue(TestLexer.test('''Class _{T(){Continue ;Break ;l7w_f::$YF();} }Class n3k1:g_{E(_8LO,_:Int ){ {} }Val $S,$_4Q_,$w73r_A:_2E;V(){} }''','''Class,_,{,T,(,),{,Continue,;,Break,;,l7w_f,::,$YF,(,),;,},},Class,n3k1,:,g_,{,E,(,_8LO,,,_,:,Int,),{,{,},},Val,$S,,,$_4Q_,,,$w73r_A,:,_2E,;,V,(,),{,},},<EOF>''',101))

    def test_1334(self):
        self.assertTrue(TestLexer.test('''Class zn{_m_9(_:Array [Array [Array [Array [Float ,0X32],0B1001000],037],0b111110]){} }Class wB:y{Constructor (e:Boolean ){} }Class _{}''','''Class,zn,{,_m_9,(,_,:,Array,[,Array,[,Array,[,Array,[,Float,,,0X32,],,,0B1001000,],,,037,],,,0b111110,],),{,},},Class,wB,:,y,{,Constructor,(,e,:,Boolean,),{,},},Class,_,{,},<EOF>''',101))

    def test_1335(self):
        self.assertTrue(TestLexer.test('''Class r:_NM{}Class Q:_Q{Destructor (){Break ;}Var R9F,$_7,Vc:_3U;}Class H014{Constructor (__m0:c2_9;_0:Array [Array [Boolean ,067],067];Y_:Float ){_A5::$L();}Destructor (){} }''','''Class,r,:,_NM,{,},Class,Q,:,_Q,{,Destructor,(,),{,Break,;,},Var,R9F,,,$_7,,,Vc,:,_3U,;,},Class,H014,{,Constructor,(,__m0,:,c2_9,;,_0,:,Array,[,Array,[,Boolean,,,067,],,,067,],;,Y_,:,Float,),{,_A5,::,$L,(,),;,},Destructor,(,),{,},},<EOF>''',101))

    def test_1336(self):
        self.assertTrue(TestLexer.test('''Class qA3:_4{Val _,_W_m:_0;}Class j9{_7(p:Array [Array [Int ,4],4]){} }Class W:v{}Class Ahl:_{Var $Y:_qW_;Var X:String ;}''','''Class,qA3,:,_4,{,Val,_,,,_W_m,:,_0,;,},Class,j9,{,_7,(,p,:,Array,[,Array,[,Int,,,4,],,,4,],),{,},},Class,W,:,v,{,},Class,Ahl,:,_,{,Var,$Y,:,_qW_,;,Var,X,:,String,;,},<EOF>''',101))

    def test_1337(self):
        self.assertTrue(TestLexer.test('''Class _:_R5v2{Val $v:Array [String ,02_07];}Class _{}Class _{Val ___,z8__,$_,u,$_,__U71,$k_:_;Var $2,$J0:Array [Array [Array [Int ,0B10],0b1_1_1],0B1_010];}''','''Class,_,:,_R5v2,{,Val,$v,:,Array,[,String,,,0207,],;,},Class,_,{,},Class,_,{,Val,___,,,z8__,,,$_,,,u,,,$_,,,__U71,,,$k_,:,_,;,Var,$2,,,$J0,:,Array,[,Array,[,Array,[,Int,,,0B10,],,,0b111,],,,0B1010,],;,},<EOF>''',101))

    def test_1338(self):
        self.assertTrue(TestLexer.test('''Class AU:_{Destructor (){} }Class _f6:q_03{Constructor (C0,d_:P_1){Break ;}Var $_Yy,$5ZW2_,$_d_:Array [Array [Array [Boolean ,0100],0b11],03];Val E_442_:String ;Var $_G,c,$9:P;}''','''Class,AU,:,_,{,Destructor,(,),{,},},Class,_f6,:,q_03,{,Constructor,(,C0,,,d_,:,P_1,),{,Break,;,},Var,$_Yy,,,$5ZW2_,,,$_d_,:,Array,[,Array,[,Array,[,Boolean,,,0100,],,,0b11,],,,03,],;,Val,E_442_,:,String,;,Var,$_G,,,c,,,$9,:,P,;,},<EOF>''',101))

    def test_1339(self):
        self.assertTrue(TestLexer.test('''Class I:eX_{Constructor (K:Array [Float ,78];_pxb8:Array [Array [Array [Array [Array [Boolean ,062],0B101101],0x6],0xB16_8_C],0b1_10]){}Destructor (){} }Class q:K{Var a9:Float ;Destructor (){} }Class _u:_{}''','''Class,I,:,eX_,{,Constructor,(,K,:,Array,[,Float,,,78,],;,_pxb8,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,062,],,,0B101101,],,,0x6,],,,0xB168C,],,,0b110,],),{,},Destructor,(,),{,},},Class,q,:,K,{,Var,a9,:,Float,;,Destructor,(,),{,},},Class,_u,:,_,{,},<EOF>''',101))

    def test_1340(self):
        self.assertTrue(TestLexer.test('''Class _0{Val $4,$4,$W8,_:Array [Array [Array [Array [Array [Array [Array [Int ,0b1_0_01],0X948],0XC_9],0B1],0x25],0x25],224_8];}Class _:Irm{Val $0__p,$5:Array [Float ,24];}''','''Class,_0,{,Val,$4,,,$4,,,$W8,,,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0b1001,],,,0X948,],,,0XC9,],,,0B1,],,,0x25,],,,0x25,],,,2248,],;,},Class,_,:,Irm,{,Val,$0__p,,,$5,:,Array,[,Float,,,24,],;,},<EOF>''',101))

    def test_1341(self):
        self.assertTrue(TestLexer.test('''Class r__:y{_(_:String ;_,L_:Boolean ;K:Array [Array [Array [Array [String ,5229],49],0b1],0x32]){}Constructor (_0:Float ){} }''','''Class,r__,:,y,{,_,(,_,:,String,;,_,,,L_,:,Boolean,;,K,:,Array,[,Array,[,Array,[,Array,[,String,,,5229,],,,49,],,,0b1,],,,0x32,],),{,},Constructor,(,_0,:,Float,),{,},},<EOF>''',101))

    def test_1342(self):
        self.assertTrue(TestLexer.test('''Class Zw:_{}Class q_9:zH{}Class _S:__2{Constructor (__,_,y_:Array [Array [Boolean ,0b101001],037_3];_:Array [Array [Float ,0x1],0xBE_1];C_:Fnf9F;uU:Array [String ,03];_l:_U;_,__Mv_:v;__qV:Array [String ,0x3F];_2_j:Float ;f,E:Array [Array [Float ,6],0143];__:Array [Boolean ,0143]){} }''','''Class,Zw,:,_,{,},Class,q_9,:,zH,{,},Class,_S,:,__2,{,Constructor,(,__,,,_,,,y_,:,Array,[,Array,[,Boolean,,,0b101001,],,,0373,],;,_,:,Array,[,Array,[,Float,,,0x1,],,,0xBE1,],;,C_,:,Fnf9F,;,uU,:,Array,[,String,,,03,],;,_l,:,_U,;,_,,,__Mv_,:,v,;,__qV,:,Array,[,String,,,0x3F,],;,_2_j,:,Float,;,f,,,E,:,Array,[,Array,[,Float,,,6,],,,0143,],;,__,:,Array,[,Boolean,,,0143,],),{,},},<EOF>''',101))

    def test_1343(self):
        self.assertTrue(TestLexer.test('''Class S{Destructor (){Val _:Array [String ,055];}Var _382,z:Array [String ,0X715];Val __:B;}Class __{}Class __u:_{Constructor (_C:__;S,U:Array [Array [String ,30],055];l:_;C5,Z:Float ;r_:String ;__10,Sb:Array [Float ,0b1010001];_w,XO_x:String ){} }''','''Class,S,{,Destructor,(,),{,Val,_,:,Array,[,String,,,055,],;,},Var,_382,,,z,:,Array,[,String,,,0X715,],;,Val,__,:,B,;,},Class,__,{,},Class,__u,:,_,{,Constructor,(,_C,:,__,;,S,,,U,:,Array,[,Array,[,String,,,30,],,,055,],;,l,:,_,;,C5,,,Z,:,Float,;,r_,:,String,;,__10,,,Sb,:,Array,[,Float,,,0b1010001,],;,_w,,,XO_x,:,String,),{,},},<EOF>''',101))

    def test_1344(self):
        self.assertTrue(TestLexer.test('''Class _{Var $X_v6z:Boolean ;Destructor (){Break ;} }Class _4:_{}Class Y0{}Class _6:O{Constructor (y_g,__c:Int ;_,L4:Int ;s:Int ){} }Class _{}''','''Class,_,{,Var,$X_v6z,:,Boolean,;,Destructor,(,),{,Break,;,},},Class,_4,:,_,{,},Class,Y0,{,},Class,_6,:,O,{,Constructor,(,y_g,,,__c,:,Int,;,_,,,L4,:,Int,;,s,:,Int,),{,},},Class,_,{,},<EOF>''',101))

    def test_1345(self):
        self.assertTrue(TestLexer.test('''Class _1:E0375{}Class U__:_{Val _,D4___:Array [Array [Array [Array [Array [Array [Array [Float ,91],0x8],0x33],015],0b1],0X61],91];$5(){} }Class _:__P{}Class _9__MFr0N_I{}''','''Class,_1,:,E0375,{,},Class,U__,:,_,{,Val,_,,,D4___,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,91,],,,0x8,],,,0x33,],,,015,],,,0b1,],,,0X61,],,,91,],;,$5,(,),{,},},Class,_,:,__P,{,},Class,_9__MFr0N_I,{,},<EOF>''',101))

    def test_1346(self):
        self.assertTrue(TestLexer.test('''Class _v02_9{$_3Y(X,__X_,_:Int ){}Var _X:Array [Array [Array [Array [Array [Array [Array [Array [Array [Int ,0B1],0X2F],01],0x3],0xF_6],0135],0x3A],0XA],0135];$1(Wm:Boolean ;_F_,_5P:Int ){Break ;}Val $___:Float ;}''','''Class,_v02_9,{,$_3Y,(,X,,,__X_,,,_,:,Int,),{,},Var,_X,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0B1,],,,0X2F,],,,01,],,,0x3,],,,0xF6,],,,0135,],,,0x3A,],,,0XA,],,,0135,],;,$1,(,Wm,:,Boolean,;,_F_,,,_5P,:,Int,),{,Break,;,},Val,$___,:,Float,;,},<EOF>''',101))

    def test_1347(self):
        self.assertTrue(TestLexer.test('''Class Q:q{Var $_,__Y,$6_,__,$t:l_2na;Var $U,_g,_2:Array [Array [Int ,06],025];Constructor (_7:Array [Array [Boolean ,0b100000],0b1]){Break ;Continue ;} }Class T{}''','''Class,Q,:,q,{,Var,$_,,,__Y,,,$6_,,,__,,,$t,:,l_2na,;,Var,$U,,,_g,,,_2,:,Array,[,Array,[,Int,,,06,],,,025,],;,Constructor,(,_7,:,Array,[,Array,[,Boolean,,,0b100000,],,,0b1,],),{,Break,;,Continue,;,},},Class,T,{,},<EOF>''',101))

    def test_1348(self):
        self.assertTrue(TestLexer.test('''Class N5:E{Constructor (q_9_,X,_,_p,r:_;n:__){Var cn,W_,s6,u,_:Array [Array [Array [Array [String ,0B11_1_011_01],0x2],0b111010],032];}Var $N,A___5_,_,$6,$_,$6,_1v,__,$8S___6_,$p:Float ;Var $7:Boolean ;}Class q{}''','''Class,N5,:,E,{,Constructor,(,q_9_,,,X,,,_,,,_p,,,r,:,_,;,n,:,__,),{,Var,cn,,,W_,,,s6,,,u,,,_,:,Array,[,Array,[,Array,[,Array,[,String,,,0B11101101,],,,0x2,],,,0b111010,],,,032,],;,},Var,$N,,,A___5_,,,_,,,$6,,,$_,,,$6,,,_1v,,,__,,,$8S___6_,,,$p,:,Float,;,Var,$7,:,Boolean,;,},Class,q,{,},<EOF>''',101))

    def test_1349(self):
        self.assertTrue(TestLexer.test('''Class A2{Constructor (){ {} }Destructor (){} }Class c{Constructor (n__,T,_,R:xN_p6;__,D,f11E,_6,_:Int ;_:x4f;___H__,_08,_,_,n_:Array [Array [Array [Array [String ,027],027],0x7],44];_:___3;_:u){}Val $J:p;}''','''Class,A2,{,Constructor,(,),{,{,},},Destructor,(,),{,},},Class,c,{,Constructor,(,n__,,,T,,,_,,,R,:,xN_p6,;,__,,,D,,,f11E,,,_6,,,_,:,Int,;,_,:,x4f,;,___H__,,,_08,,,_,,,_,,,n_,:,Array,[,Array,[,Array,[,Array,[,String,,,027,],,,027,],,,0x7,],,,44,],;,_,:,___3,;,_,:,u,),{,},Val,$J,:,p,;,},<EOF>''',101))

    def test_1350(self):
        self.assertTrue(TestLexer.test('''Class V{Var $0,_8:Array [Array [Int ,71],3];Val $_:Float ;Val _,_4,l:Array [Array [Array [Array [Float ,0B1_1_0],0b1],0b1011001],05];Var e:S_;Val _4,$__A5:Int ;}Class _:Z{}''','''Class,V,{,Var,$0,,,_8,:,Array,[,Array,[,Int,,,71,],,,3,],;,Val,$_,:,Float,;,Val,_,,,_4,,,l,:,Array,[,Array,[,Array,[,Array,[,Float,,,0B110,],,,0b1,],,,0b1011001,],,,05,],;,Var,e,:,S_,;,Val,_4,,,$__A5,:,Int,;,},Class,_,:,Z,{,},<EOF>''',101))

    def test_1351(self):
        self.assertTrue(TestLexer.test('''Class O_n{}Class _:_5{}Class K__{Var cG3,_:r;$3M(){}Constructor (){}Destructor (){Return ;}Constructor (r,o:L71){} }''','''Class,O_n,{,},Class,_,:,_5,{,},Class,K__,{,Var,cG3,,,_,:,r,;,$3M,(,),{,},Constructor,(,),{,},Destructor,(,),{,Return,;,},Constructor,(,r,,,o,:,L71,),{,},},<EOF>''',101))

    def test_1352(self):
        self.assertTrue(TestLexer.test('''Class _9E{$7(_9,Y66:Int ;r,_J_5,c7__14,_m58_3I_,__8I_,_:Array [Boolean ,02_3];D,_,_t:Array [Array [Array [Array [Array [Array [Float ,0x4F],0B1],0X5_D],0b1100100],0b1_1],0X9_A0_A]){} }''','''Class,_9E,{,$7,(,_9,,,Y66,:,Int,;,r,,,_J_5,,,c7__14,,,_m58_3I_,,,__8I_,,,_,:,Array,[,Boolean,,,023,],;,D,,,_,,,_t,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0x4F,],,,0B1,],,,0X5D,],,,0b1100100,],,,0b11,],,,0X9A0A,],),{,},},<EOF>''',101))

    def test_1353(self):
        self.assertTrue(TestLexer.test('''Class _{Constructor (D:Array [Array [Array [Array [Float ,0xE],7],8_12],93];S:Array [Array [Array [Array [Array [Int ,0X50],93],4],0B10110],4];X_,nQ:String ;K_,r_:Float ){Return ;} }Class _V{}Class G5_{}Class U:y{}''','''Class,_,{,Constructor,(,D,:,Array,[,Array,[,Array,[,Array,[,Float,,,0xE,],,,7,],,,812,],,,93,],;,S,:,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0X50,],,,93,],,,4,],,,0B10110,],,,4,],;,X_,,,nQ,:,String,;,K_,,,r_,:,Float,),{,Return,;,},},Class,_V,{,},Class,G5_,{,},Class,U,:,y,{,},<EOF>''',101))

    def test_1354(self):
        self.assertTrue(TestLexer.test('''Class o:l{}Class MF300I_{}Class r:_h{$B(r8,A,_9,_,_,q,N:k;_Rf:_){}Constructor (_:Boolean ;K,r__,Q:Array [Int ,0xCD_8D]){} }''','''Class,o,:,l,{,},Class,MF300I_,{,},Class,r,:,_h,{,$B,(,r8,,,A,,,_9,,,_,,,_,,,q,,,N,:,k,;,_Rf,:,_,),{,},Constructor,(,_,:,Boolean,;,K,,,r__,,,Q,:,Array,[,Int,,,0xCD8D,],),{,},},<EOF>''',101))

    def test_1355(self):
        self.assertTrue(TestLexer.test('''Class U7_:___{Val $d_:A;}Class _:U{Sj2(){} }Class z{Var $_,_:__;Constructor (){}Constructor (){}Var $_:Array [Float ,0141];}Class O{}Class _:d4{}''','''Class,U7_,:,___,{,Val,$d_,:,A,;,},Class,_,:,U,{,Sj2,(,),{,},},Class,z,{,Var,$_,,,_,:,__,;,Constructor,(,),{,},Constructor,(,),{,},Var,$_,:,Array,[,Float,,,0141,],;,},Class,O,{,},Class,_,:,d4,{,},<EOF>''',101))

    def test_1356(self):
        self.assertTrue(TestLexer.test('''Class L:_Y{Z(){07_5._();}Val JR8x:Array [Array [Boolean ,0b1],0b1];}Class R:_h3_{}Class _{Val $__:Array [String ,98];}Class p{Constructor (M18,N:String ){}Var C:String ;Val E__,_:Boolean ;Var _P:Array [Array [Array [Float ,05_4],1],0X12];}''','''Class,L,:,_Y,{,Z,(,),{,075,.,_,(,),;,},Val,JR8x,:,Array,[,Array,[,Boolean,,,0b1,],,,0b1,],;,},Class,R,:,_h3_,{,},Class,_,{,Val,$__,:,Array,[,String,,,98,],;,},Class,p,{,Constructor,(,M18,,,N,:,String,),{,},Var,C,:,String,;,Val,E__,,,_,:,Boolean,;,Var,_P,:,Array,[,Array,[,Array,[,Float,,,054,],,,1,],,,0X12,],;,},<EOF>''',101))

    def test_1357(self):
        self.assertTrue(TestLexer.test('''Class _9{Constructor (n:_){}_(h:P9;q_5l,__,_9:Boolean ;s_,Fm6_4_:Float ){} }Class _:r_{$494(){}Destructor (){Break ;}Destructor (){} }''','''Class,_9,{,Constructor,(,n,:,_,),{,},_,(,h,:,P9,;,q_5l,,,__,,,_9,:,Boolean,;,s_,,,Fm6_4_,:,Float,),{,},},Class,_,:,r_,{,$494,(,),{,},Destructor,(,),{,Break,;,},Destructor,(,),{,},},<EOF>''',101))

    def test_1358(self):
        self.assertTrue(TestLexer.test('''Class _{}Class ____:_{}Class _mb:B{Val $___:Pmw_13_;}Class _37{Val $9,OZ5,$M__,_,$8i8,$9F:Array [Array [Int ,0b1],021];Val $3:Float ;Val $0:_;}''','''Class,_,{,},Class,____,:,_,{,},Class,_mb,:,B,{,Val,$___,:,Pmw_13_,;,},Class,_37,{,Val,$9,,,OZ5,,,$M__,,,_,,,$8i8,,,$9F,:,Array,[,Array,[,Int,,,0b1,],,,021,],;,Val,$3,:,Float,;,Val,$0,:,_,;,},<EOF>''',101))

    def test_1359(self):
        self.assertTrue(TestLexer.test('''Class _{Destructor (){Continue ;} }Class __q{Val $Z9_Cj:Array [Array [Array [Int ,53],53],0B1010010];$_8_9(_v:Array [Array [String ,8],0x9];r_v:Array [Boolean ,53];k,_:Array [Array [Array [Int ,0X24],0B1010010],0X24];_5,rA,w_:_){}Val $b:Array [Array [Array [String ,0B1_01_0],0B1_1_0],53];Constructor (M_:Int ){} }Class _:F_4{}''','''Class,_,{,Destructor,(,),{,Continue,;,},},Class,__q,{,Val,$Z9_Cj,:,Array,[,Array,[,Array,[,Int,,,53,],,,53,],,,0B1010010,],;,$_8_9,(,_v,:,Array,[,Array,[,String,,,8,],,,0x9,],;,r_v,:,Array,[,Boolean,,,53,],;,k,,,_,:,Array,[,Array,[,Array,[,Int,,,0X24,],,,0B1010010,],,,0X24,],;,_5,,,rA,,,w_,:,_,),{,},Val,$b,:,Array,[,Array,[,Array,[,String,,,0B1010,],,,0B110,],,,53,],;,Constructor,(,M_,:,Int,),{,},},Class,_,:,F_4,{,},<EOF>''',101))

    def test_1360(self):
        self.assertTrue(TestLexer.test('''Class _{_(W:Array [Boolean ,02_37_2_6];T:Array [Array [Array [Int ,03_3],0XC],0b1_1]){}Val $k:_6aFnL__W;}Class w{$_(){} }''','''Class,_,{,_,(,W,:,Array,[,Boolean,,,023726,],;,T,:,Array,[,Array,[,Array,[,Int,,,033,],,,0XC,],,,0b11,],),{,},Val,$k,:,_6aFnL__W,;,},Class,w,{,$_,(,),{,},},<EOF>''',101))

    def test_1361(self):
        self.assertTrue(TestLexer.test('''Class _{Var $3:L;}Class H{Constructor (_r,F_:Int ;S,____,_,_:k7;__0,Y,_,_,_,_5__:Array [Array [Int ,03],0B10_1_1];R_,df:e_I7){} }Class _:_N__{}Class _{}Class y2w7u{}Class __:_{Val $8:String ;Var s1,fB,$0_N,$__,_:Array [Array [Float ,7],0X6];Var $d,$2:String ;Constructor (){Return ;} }Class _{Z9_(j:b7;_0:x){} }Class B{}Class _2o:Q{}''','''Class,_,{,Var,$3,:,L,;,},Class,H,{,Constructor,(,_r,,,F_,:,Int,;,S,,,____,,,_,,,_,:,k7,;,__0,,,Y,,,_,,,_,,,_,,,_5__,:,Array,[,Array,[,Int,,,03,],,,0B1011,],;,R_,,,df,:,e_I7,),{,},},Class,_,:,_N__,{,},Class,_,{,},Class,y2w7u,{,},Class,__,:,_,{,Val,$8,:,String,;,Var,s1,,,fB,,,$0_N,,,$__,,,_,:,Array,[,Array,[,Float,,,7,],,,0X6,],;,Var,$d,,,$2,:,String,;,Constructor,(,),{,Return,;,},},Class,_,{,Z9_,(,j,:,b7,;,_0,:,x,),{,},},Class,B,{,},Class,_2o,:,Q,{,},<EOF>''',101))

    def test_1362(self):
        self.assertTrue(TestLexer.test('''Class _f{Constructor (I_,_:Array [Boolean ,36];KEq:Array [Array [Array [Array [Float ,0X5],3],1_8],0X9]){}Var _44:I4;}Class _{}''','''Class,_f,{,Constructor,(,I_,,,_,:,Array,[,Boolean,,,36,],;,KEq,:,Array,[,Array,[,Array,[,Array,[,Float,,,0X5,],,,3,],,,18,],,,0X9,],),{,},Var,_44,:,I4,;,},Class,_,{,},<EOF>''',101))

    def test_1363(self):
        self.assertTrue(TestLexer.test('''Class x_:_{Val b:Array [Array [Array [Boolean ,0X36],0X1],0B1];}Class Xo:_{}Class __:_l0_6_{_0__(){} }Class o_u_____{}''','''Class,x_,:,_,{,Val,b,:,Array,[,Array,[,Array,[,Boolean,,,0X36,],,,0X1,],,,0B1,],;,},Class,Xo,:,_,{,},Class,__,:,_l0_6_,{,_0__,(,),{,},},Class,o_u_____,{,},<EOF>''',101))

    def test_1364(self):
        self.assertTrue(TestLexer.test('''Class _{}Class S:_{M(_,_6_,r,_,__34X:Float ){} }Class agp_:v{}Class _lX:_5q5__j__{Var $2__a9_BAI,T:J;Val N,$_,$_8,_1,$p:String ;Constructor (){Val _fLWh:I;Var _,_S6:String ;} }Class j{}''','''Class,_,{,},Class,S,:,_,{,M,(,_,,,_6_,,,r,,,_,,,__34X,:,Float,),{,},},Class,agp_,:,v,{,},Class,_lX,:,_5q5__j__,{,Var,$2__a9_BAI,,,T,:,J,;,Val,N,,,$_,,,$_8,,,_1,,,$p,:,String,;,Constructor,(,),{,Val,_fLWh,:,I,;,Var,_,,,_S6,:,String,;,},},Class,j,{,},<EOF>''',101))

    def test_1365(self):
        self.assertTrue(TestLexer.test('''Class P:s_c_{__(_924_,__:f;N__,_,rJ__E,GK,h,_,Z,_,E0:Array [Array [Array [String ,0X8],0X2B],93];A_:Array [Boolean ,0b1011111];__H,a,_:Float ){} }Class __C:_{}''','''Class,P,:,s_c_,{,__,(,_924_,,,__,:,f,;,N__,,,_,,,rJ__E,,,GK,,,h,,,_,,,Z,,,_,,,E0,:,Array,[,Array,[,Array,[,String,,,0X8,],,,0X2B,],,,93,],;,A_,:,Array,[,Boolean,,,0b1011111,],;,__H,,,a,,,_,:,Float,),{,},},Class,__C,:,_,{,},<EOF>''',101))

    def test_1366(self):
        self.assertTrue(TestLexer.test('''Class _{}Class o{Destructor (){Break ;}Val $7,$_,$4_65_:Array [Array [String ,0B1000111],0b1000011];Destructor (){} }Class L_1:L_{}''','''Class,_,{,},Class,o,{,Destructor,(,),{,Break,;,},Val,$7,,,$_,,,$4_65_,:,Array,[,Array,[,String,,,0B1000111,],,,0b1000011,],;,Destructor,(,),{,},},Class,L_1,:,L_,{,},<EOF>''',101))

    def test_1367(self):
        self.assertTrue(TestLexer.test('''Class __4:S{Q(Un,o,I3:__;_,_,u__:Array [Array [Array [Array [Array [Int ,0x9],0b1_1],02_7_5],0B11_0],0X4]){}Constructor (){ {} }}Class _:_S{}''','''Class,__4,:,S,{,Q,(,Un,,,o,,,I3,:,__,;,_,,,_,,,u__,:,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0x9,],,,0b11,],,,0275,],,,0B110,],,,0X4,],),{,},Constructor,(,),{,{,},},},Class,_,:,_S,{,},<EOF>''',101))

    def test_1368(self):
        self.assertTrue(TestLexer.test('''Class i:__{Var w,n,$_2_,V,$A,_6_:String ;Destructor (){}_(WXw3,eY_6:String ;_,O_e:_;M35___:N_){Break ;}Constructor (E:vX4){} }''','''Class,i,:,__,{,Var,w,,,n,,,$_2_,,,V,,,$A,,,_6_,:,String,;,Destructor,(,),{,},_,(,WXw3,,,eY_6,:,String,;,_,,,O_e,:,_,;,M35___,:,N_,),{,Break,;,},Constructor,(,E,:,vX4,),{,},},<EOF>''',101))

    def test_1369(self):
        self.assertTrue(TestLexer.test('''Class y{_(F:_92_;_do4Q:Array [Array [Array [Int ,0x56],0x56],8];_,f:ay;_,_kg_,I7:Boolean ;_:_;y,_5_:Boolean ){} }Class _{}''','''Class,y,{,_,(,F,:,_92_,;,_do4Q,:,Array,[,Array,[,Array,[,Int,,,0x56,],,,0x56,],,,8,],;,_,,,f,:,ay,;,_,,,_kg_,,,I7,:,Boolean,;,_,:,_,;,y,,,_5_,:,Boolean,),{,},},Class,_,{,},<EOF>''',101))

    def test_1370(self):
        self.assertTrue(TestLexer.test('''Class _{}Class q_0{Var $_:Boolean ;}Class N{}Class _{Constructor (){ {} }Val $_52,_:String ;Val $_,$75,Sf,_8,_:Array [Boolean ,0X5];}''','''Class,_,{,},Class,q_0,{,Var,$_,:,Boolean,;,},Class,N,{,},Class,_,{,Constructor,(,),{,{,},},Val,$_52,,,_,:,String,;,Val,$_,,,$75,,,Sf,,,_8,,,_,:,Array,[,Boolean,,,0X5,],;,},<EOF>''',101))

    def test_1371(self):
        self.assertTrue(TestLexer.test('''Class _6d:l7H7{Destructor (){}Var $2,$66:Array [Int ,062];Var _O:Float ;Constructor (nA,x,z_3lt2_,_Qt765:L9_){} }''','''Class,_6d,:,l7H7,{,Destructor,(,),{,},Var,$2,,,$66,:,Array,[,Int,,,062,],;,Var,_O,:,Float,;,Constructor,(,nA,,,x,,,z_3lt2_,,,_Qt765,:,L9_,),{,},},<EOF>''',101))

    def test_1372(self):
        self.assertTrue(TestLexer.test('''Class X:__{Val $6:String ;}Class D9:_{Destructor (){}Constructor (){}$n(__:String ){Continue ;M::$18q57_();} }''','''Class,X,:,__,{,Val,$6,:,String,;,},Class,D9,:,_,{,Destructor,(,),{,},Constructor,(,),{,},$n,(,__,:,String,),{,Continue,;,M,::,$18q57_,(,),;,},},<EOF>''',101))

    def test_1373(self):
        self.assertTrue(TestLexer.test('''Class _:gX{Val _,_b:Array [Array [Array [Array [Array [Array [Boolean ,0b1001101],05],037],037],18],0B1001];Var y_:Array [Array [Array [Array [String ,0B1],037],18],6];}''','''Class,_,:,gX,{,Val,_,,,_b,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0b1001101,],,,05,],,,037,],,,037,],,,18,],,,0B1001,],;,Var,y_,:,Array,[,Array,[,Array,[,Array,[,String,,,0B1,],,,037,],,,18,],,,6,],;,},<EOF>''',101))

    def test_1374(self):
        self.assertTrue(TestLexer.test('''Class g4y___{}Class _v:_{Val $__:Array [Array [Array [Array [Array [Int ,0B1000],073],0b10011],0B1],44];}Class __{}Class w:_8{_(){} }Class l4_8{}''','''Class,g4y___,{,},Class,_v,:,_,{,Val,$__,:,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0B1000,],,,073,],,,0b10011,],,,0B1,],,,44,],;,},Class,__,{,},Class,w,:,_8,{,_,(,),{,},},Class,l4_8,{,},<EOF>''',101))

    def test_1375(self):
        self.assertTrue(TestLexer.test('''Class P:_{$O(__:Int ;_:Array [Boolean ,0B1000100]){Break ;Break ;}Var _dy,__E662:Array [Array [Array [Int ,0X82_8D6],0X15],2];$V(){}Val _g:Int ;}Class _10:_5{}''','''Class,P,:,_,{,$O,(,__,:,Int,;,_,:,Array,[,Boolean,,,0B1000100,],),{,Break,;,Break,;,},Var,_dy,,,__E662,:,Array,[,Array,[,Array,[,Int,,,0X828D6,],,,0X15,],,,2,],;,$V,(,),{,},Val,_g,:,Int,;,},Class,_10,:,_5,{,},<EOF>''',101))

    def test_1376(self):
        self.assertTrue(TestLexer.test('''Class __6:_{Constructor (d,__z5,_,_e,Z_w:Array [Array [Array [Array [Array [Array [Boolean ,10],0b1001111],0112],06],0112],0112]){} }''','''Class,__6,:,_,{,Constructor,(,d,,,__z5,,,_,,,_e,,,Z_w,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,10,],,,0b1001111,],,,0112,],,,06,],,,0112,],,,0112,],),{,},},<EOF>''',101))

    def test_1377(self):
        self.assertTrue(TestLexer.test('''Class _O1:_Xw{Val _,h_5,_s,_,s:_5;}Class R{Val ak,$p:Array [String ,0B1];_(_:Array [Array [String ,0x7_9_E],0113];__:_;_9:Array [Array [Boolean ,0113],0x6]){} }Class _{Var $_2pK_iB,$FR:Boolean ;Constructor (E,ac:String ){} }Class e_:S_3o{}''','''Class,_O1,:,_Xw,{,Val,_,,,h_5,,,_s,,,_,,,s,:,_5,;,},Class,R,{,Val,ak,,,$p,:,Array,[,String,,,0B1,],;,_,(,_,:,Array,[,Array,[,String,,,0x79E,],,,0113,],;,__,:,_,;,_9,:,Array,[,Array,[,Boolean,,,0113,],,,0x6,],),{,},},Class,_,{,Var,$_2pK_iB,,,$FR,:,Boolean,;,Constructor,(,E,,,ac,:,String,),{,},},Class,e_,:,S_3o,{,},<EOF>''',101))

    def test_1378(self):
        self.assertTrue(TestLexer.test('''Class S{$_(_:Array [Float ,0B1001001];__Wi,_P5_j,C7v2,kV_,Z_27ZH,__:Boolean ;_3E,i_q5_3l,d:C){} }Class w:J72lL704{}Class z_1:_6c{}Class _yqzRp{Val Z2UZ1:Int ;}''','''Class,S,{,$_,(,_,:,Array,[,Float,,,0B1001001,],;,__Wi,,,_P5_j,,,C7v2,,,kV_,,,Z_27ZH,,,__,:,Boolean,;,_3E,,,i_q5_3l,,,d,:,C,),{,},},Class,w,:,J72lL704,{,},Class,z_1,:,_6c,{,},Class,_yqzRp,{,Val,Z2UZ1,:,Int,;,},<EOF>''',101))

    def test_1379(self):
        self.assertTrue(TestLexer.test('''Class e{Val _:Array [Array [Boolean ,0xF426_4_2F],052];Destructor (){Return ;} }Class gq__u:z{}Class _6iB__{}Class _{Constructor (){} }Class i:S_p2n{}''','''Class,e,{,Val,_,:,Array,[,Array,[,Boolean,,,0xF42642F,],,,052,],;,Destructor,(,),{,Return,;,},},Class,gq__u,:,z,{,},Class,_6iB__,{,},Class,_,{,Constructor,(,),{,},},Class,i,:,S_p2n,{,},<EOF>''',101))

    def test_1380(self):
        self.assertTrue(TestLexer.test('''Class __:_{}Class nN:_T{Val $_:Array [Boolean ,0X25];Val KoC,_:Array [String ,0B1];Constructor (_:Int ;i:Float ){} }Class l:_828{}''','''Class,__,:,_,{,},Class,nN,:,_T,{,Val,$_,:,Array,[,Boolean,,,0X25,],;,Val,KoC,,,_,:,Array,[,String,,,0B1,],;,Constructor,(,_,:,Int,;,i,:,Float,),{,},},Class,l,:,_828,{,},<EOF>''',101))

    def test_1381(self):
        self.assertTrue(TestLexer.test('''Class _:NS{Var f:Array [Array [Array [Array [Array [Array [Array [Float ,0B11],037],0b1],0x2_1],0x2C],89],03_640_0]=!!!!_::$2;}Class _8{Val _9,$X,$U:_;Constructor (__,__:Array [Int ,06];_Dby,O,H,_2Y:__){} }''','''Class,_,:,NS,{,Var,f,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0B11,],,,037,],,,0b1,],,,0x21,],,,0x2C,],,,89,],,,036400,],=,!,!,!,!,_,::,$2,;,},Class,_8,{,Val,_9,,,$X,,,$U,:,_,;,Constructor,(,__,,,__,:,Array,[,Int,,,06,],;,_Dby,,,O,,,H,,,_2Y,:,__,),{,},},<EOF>''',101))

    def test_1382(self):
        self.assertTrue(TestLexer.test('''Class c:z0eZ___{Val $_:_;$__(P:__;_,T6b,Nd_:Array [Int ,05]){}Constructor (x_,_,_8:z_;C4:_;_FQ_,__8,_0b,_,_,A:C;__,_,bcY:Array [Array [Array [Array [Int ,0b1001110],58],07],0B1011101];_,GI:String ;H_:_;_6,_G_:Boolean ){}Val _,$j:Array [Array [Boolean ,4_2],0x9];}Class _{}''','''Class,c,:,z0eZ___,{,Val,$_,:,_,;,$__,(,P,:,__,;,_,,,T6b,,,Nd_,:,Array,[,Int,,,05,],),{,},Constructor,(,x_,,,_,,,_8,:,z_,;,C4,:,_,;,_FQ_,,,__8,,,_0b,,,_,,,_,,,A,:,C,;,__,,,_,,,bcY,:,Array,[,Array,[,Array,[,Array,[,Int,,,0b1001110,],,,58,],,,07,],,,0B1011101,],;,_,,,GI,:,String,;,H_,:,_,;,_6,,,_G_,:,Boolean,),{,},Val,_,,,$j,:,Array,[,Array,[,Boolean,,,42,],,,0x9,],;,},Class,_,{,},<EOF>''',101))

    def test_1383(self):
        self.assertTrue(TestLexer.test('''Class W_:ua{Destructor (){Break ;} }Class _{Constructor (_:Array [Float ,033];i,b,Q6,t_,_:Array [Array [Array [Array [Array [String ,0X9E],13],0X1],0B1],0b1010]){}Destructor (){Break ;} }''','''Class,W_,:,ua,{,Destructor,(,),{,Break,;,},},Class,_,{,Constructor,(,_,:,Array,[,Float,,,033,],;,i,,,b,,,Q6,,,t_,,,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0X9E,],,,13,],,,0X1,],,,0B1,],,,0b1010,],),{,},Destructor,(,),{,Break,;,},},<EOF>''',101))

    def test_1384(self):
        self.assertTrue(TestLexer.test('''Class h{Val _:String ;_J3M(){}$2__1(q,_6,_,_kJ,N,_:Array [Array [Float ,011],0x2D];_7,_,_7_W1,o:Float ;_,x_w,j:Array [Array [String ,0b1_1],025]){} }''','''Class,h,{,Val,_,:,String,;,_J3M,(,),{,},$2__1,(,q,,,_6,,,_,,,_kJ,,,N,,,_,:,Array,[,Array,[,Float,,,011,],,,0x2D,],;,_7,,,_,,,_7_W1,,,o,:,Float,;,_,,,x_w,,,j,:,Array,[,Array,[,String,,,0b11,],,,025,],),{,},},<EOF>''',101))

    def test_1385(self):
        self.assertTrue(TestLexer.test('''Class _:sO3_{Var _,_jC,$q_aGD_,$7,_S,$o_Y_k:g;Destructor (){Self .V_();} }Class pw3{Bp(_,_85:Array [String ,04_5]){}Var $_:Array [Array [Float ,0B1_1],0B1];}Class j6__:V73p7{}''','''Class,_,:,sO3_,{,Var,_,,,_jC,,,$q_aGD_,,,$7,,,_S,,,$o_Y_k,:,g,;,Destructor,(,),{,Self,.,V_,(,),;,},},Class,pw3,{,Bp,(,_,,,_85,:,Array,[,String,,,045,],),{,},Var,$_,:,Array,[,Array,[,Float,,,0B11,],,,0B1,],;,},Class,j6__,:,V73p7,{,},<EOF>''',101))

    def test_1386(self):
        self.assertTrue(TestLexer.test('''Class _{Var z:Array [Int ,0X37];Constructor (GZ_,U_,_:_5;m,T,_,N9lL__4x:Array [Array [Boolean ,0x11],89]){Break ;}Var $2:___;}''','''Class,_,{,Var,z,:,Array,[,Int,,,0X37,],;,Constructor,(,GZ_,,,U_,,,_,:,_5,;,m,,,T,,,_,,,N9lL__4x,:,Array,[,Array,[,Boolean,,,0x11,],,,89,],),{,Break,;,},Var,$2,:,___,;,},<EOF>''',101))

    def test_1387(self):
        self.assertTrue(TestLexer.test('''Class m{Constructor (__1,_z,M,W:Int ){}Val L:Boolean ;Val H,$9_B:Boolean ;}Class _{}Class _8{Val J_,f:Boolean ;}''','''Class,m,{,Constructor,(,__1,,,_z,,,M,,,W,:,Int,),{,},Val,L,:,Boolean,;,Val,H,,,$9_B,:,Boolean,;,},Class,_,{,},Class,_8,{,Val,J_,,,f,:,Boolean,;,},<EOF>''',101))

    def test_1388(self):
        self.assertTrue(TestLexer.test('''Class P5E9_:A{Val $_Ph_:Array [Array [Array [Array [Float ,04],0B11101],0b110100],0X15];Destructor (){} }Class N{Destructor (){} }''','''Class,P5E9_,:,A,{,Val,$_Ph_,:,Array,[,Array,[,Array,[,Array,[,Float,,,04,],,,0B11101,],,,0b110100,],,,0X15,],;,Destructor,(,),{,},},Class,N,{,Destructor,(,),{,},},<EOF>''',101))

    def test_1389(self):
        self.assertTrue(TestLexer.test('''Class ___:vz{_q(l:Array [Array [Boolean ,62],0x5D];_:Array [Int ,0B1000000];Re:sy;M_s,U,JO,tC:l){} }Class _{Destructor (){} }Class u_w:__{}Class _c_:___{__J(y3v24s_2:Float ;d_,_94,Z,l:Array [Array [Int ,0B1000000],07_5_322];_:h){Continue ;}Var _,$t,$_:D;}''','''Class,___,:,vz,{,_q,(,l,:,Array,[,Array,[,Boolean,,,62,],,,0x5D,],;,_,:,Array,[,Int,,,0B1000000,],;,Re,:,sy,;,M_s,,,U,,,JO,,,tC,:,l,),{,},},Class,_,{,Destructor,(,),{,},},Class,u_w,:,__,{,},Class,_c_,:,___,{,__J,(,y3v24s_2,:,Float,;,d_,,,_94,,,Z,,,l,:,Array,[,Array,[,Int,,,0B1000000,],,,075322,],;,_,:,h,),{,Continue,;,},Var,_,,,$t,,,$_,:,D,;,},<EOF>''',101))

    def test_1390(self):
        self.assertTrue(TestLexer.test('''Class ___Y6{Constructor (_E:__7;_2,_:Float ;__61_,_:Array [Int ,03];_u:_;t_T_:Array [Float ,01]){}Destructor (){} }Class E{Val $6B2_,$1:String ;}Class _0F:_{}''','''Class,___Y6,{,Constructor,(,_E,:,__7,;,_2,,,_,:,Float,;,__61_,,,_,:,Array,[,Int,,,03,],;,_u,:,_,;,t_T_,:,Array,[,Float,,,01,],),{,},Destructor,(,),{,},},Class,E,{,Val,$6B2_,,,$1,:,String,;,},Class,_0F,:,_,{,},<EOF>''',101))

    def test_1391(self):
        self.assertTrue(TestLexer.test('''Class _{e_XW(_,_8N:_;V_I,F,_:Array [Float ,0x57];_,f,_:Array [String ,0b10];An3_d04,_,_7s,_,K:Array [Array [String ,0b1_0_1],0B1_1_1];_E,_C_:Array [Float ,6];H,_:String ;BCe,u:B;n:Array [Float ,0b1100001]){} }''','''Class,_,{,e_XW,(,_,,,_8N,:,_,;,V_I,,,F,,,_,:,Array,[,Float,,,0x57,],;,_,,,f,,,_,:,Array,[,String,,,0b10,],;,An3_d04,,,_,,,_7s,,,_,,,K,:,Array,[,Array,[,String,,,0b101,],,,0B111,],;,_E,,,_C_,:,Array,[,Float,,,6,],;,H,,,_,:,String,;,BCe,,,u,:,B,;,n,:,Array,[,Float,,,0b1100001,],),{,},},<EOF>''',101))

    def test_1392(self):
        self.assertTrue(TestLexer.test('''Class G{Constructor (O,_:Int ;C,y_:__;_8c3,lJ:Array [Float ,7_8]){}$_(_,_:LK;_:_Ci225;Bo,l_:V5;_:String ;_:__6){} }''','''Class,G,{,Constructor,(,O,,,_,:,Int,;,C,,,y_,:,__,;,_8c3,,,lJ,:,Array,[,Float,,,78,],),{,},$_,(,_,,,_,:,LK,;,_,:,_Ci225,;,Bo,,,l_,:,V5,;,_,:,String,;,_,:,__6,),{,},},<EOF>''',101))

    def test_1393(self):
        self.assertTrue(TestLexer.test('''Class _{Var $Ql:Array [String ,053];Var b,$22,__0,$G,$_03,$1:String ;Val P,u4,$_3:_;}Class _{Val $_,$8,$1Vj:Int ;}''','''Class,_,{,Var,$Ql,:,Array,[,String,,,053,],;,Var,b,,,$22,,,__0,,,$G,,,$_03,,,$1,:,String,;,Val,P,,,u4,,,$_3,:,_,;,},Class,_,{,Val,$_,,,$8,,,$1Vj,:,Int,;,},<EOF>''',101))

    def test_1394(self):
        self.assertTrue(TestLexer.test('''Class _{Destructor (){} }Class _{AuB459(_:String ;K54,_,_:_;W,__1:Array [Array [Array [Array [Boolean ,0B1001111],37],37],2];f_R,tQ:Boolean ;k:Int ){}Constructor (R_4R,_:Boolean ;_,r6:Array [Array [Array [Array [Array [Array [Array [Array [String ,0B1],0114],0114],0x9_6],157],06_5],04],02]){ {}Return ;} }''','''Class,_,{,Destructor,(,),{,},},Class,_,{,AuB459,(,_,:,String,;,K54,,,_,,,_,:,_,;,W,,,__1,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,0B1001111,],,,37,],,,37,],,,2,],;,f_R,,,tQ,:,Boolean,;,k,:,Int,),{,},Constructor,(,R_4R,,,_,:,Boolean,;,_,,,r6,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0B1,],,,0114,],,,0114,],,,0x96,],,,157,],,,065,],,,04,],,,02,],),{,{,},Return,;,},},<EOF>''',101))

    def test_1395(self):
        self.assertTrue(TestLexer.test('''Class _{}Class X_{Constructor (jh:Float ;C:Int ;l:l;_EG:_l){ {Continue ;} }Destructor (){__::$Y();Var _81_0:Array [Array [Float ,1_0],0B1_0];Break ;Continue ;} }Class u_58_:_{Val $C,$u:Int ;}''','''Class,_,{,},Class,X_,{,Constructor,(,jh,:,Float,;,C,:,Int,;,l,:,l,;,_EG,:,_l,),{,{,Continue,;,},},Destructor,(,),{,__,::,$Y,(,),;,Var,_81_0,:,Array,[,Array,[,Float,,,10,],,,0B10,],;,Break,;,Continue,;,},},Class,u_58_,:,_,{,Val,$C,,,$u,:,Int,;,},<EOF>''',101))

    def test_1396(self):
        self.assertTrue(TestLexer.test('''Class __2u:_{Val ___:String ;Var L,___7_c:is5;Val __4_X_9,$0T:Array [Array [Array [Array [String ,63],0517_1],03],0x3C];Var $2,_5E:String ;}Class _7F3{}''','''Class,__2u,:,_,{,Val,___,:,String,;,Var,L,,,___7_c,:,is5,;,Val,__4_X_9,,,$0T,:,Array,[,Array,[,Array,[,Array,[,String,,,63,],,,05171,],,,03,],,,0x3C,],;,Var,$2,,,_5E,:,String,;,},Class,_7F3,{,},<EOF>''',101))

    def test_1397(self):
        self.assertTrue(TestLexer.test('''Class __:M_i__{}Class _{Var _N6,_,uC8,_,x__,$8_pQi4:Float ;Constructor (_k,__z,_,_Nv,f,T,sY:String ;b8:G){} }Class _{Val _3,v__9,_:u;}''','''Class,__,:,M_i__,{,},Class,_,{,Var,_N6,,,_,,,uC8,,,_,,,x__,,,$8_pQi4,:,Float,;,Constructor,(,_k,,,__z,,,_,,,_Nv,,,f,,,T,,,sY,:,String,;,b8,:,G,),{,},},Class,_,{,Val,_3,,,v__9,,,_,:,u,;,},<EOF>''',101))

    def test_1398(self):
        self.assertTrue(TestLexer.test('''Class Uv{Constructor (){}Var $9,$z,gV6_:Array [Array [Array [Array [String ,0XE],5],0xD],076];Constructor (){} }Class P_5{Var F:_;}''','''Class,Uv,{,Constructor,(,),{,},Var,$9,,,$z,,,gV6_,:,Array,[,Array,[,Array,[,Array,[,String,,,0XE,],,,5,],,,0xD,],,,076,],;,Constructor,(,),{,},},Class,P_5,{,Var,F,:,_,;,},<EOF>''',101))

    def test_1399(self):
        self.assertTrue(TestLexer.test('''Class _P_{_A_5(){Val _Um65:Int ;}Val z:Int ;Var u,$_:Array [Array [Array [Array [Array [Array [Array [String ,0b1],0b1],010],0B110001],0B110001],67],0x1];}Class I:__F{Var $_,$1:Array [Array [Boolean ,06_1_4_0],0x1];}''','''Class,_P_,{,_A_5,(,),{,Val,_Um65,:,Int,;,},Val,z,:,Int,;,Var,u,,,$_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0b1,],,,0b1,],,,010,],,,0B110001,],,,0B110001,],,,67,],,,0x1,],;,},Class,I,:,__F,{,Var,$_,,,$1,:,Array,[,Array,[,Boolean,,,06140,],,,0x1,],;,},<EOF>''',101))

    def test_1400(self):
        self.assertTrue(TestLexer.test('''Class p__:w0{Destructor (){}_(u,_,p,_,w:eG__){}$_(_:Int ){}Constructor (_,_:__P;L_qP,_,_7,s,v,_50,ZX,u:Float ){} }''','''Class,p__,:,w0,{,Destructor,(,),{,},_,(,u,,,_,,,p,,,_,,,w,:,eG__,),{,},$_,(,_,:,Int,),{,},Constructor,(,_,,,_,:,__P,;,L_qP,,,_,,,_7,,,s,,,v,,,_50,,,ZX,,,u,:,Float,),{,},},<EOF>''',101))

    def test_1401(self):
        self.assertTrue(TestLexer.test('''Class g{Constructor (){Var p:Array [Array [Array [Array [Array [String ,43],0B10110],0x42],43],0b110101];}Val Z,$_,$6:Array [Array [Int ,0x8_B],6];Destructor (){} }Class t_:__{Val q:String ;}''','''Class,g,{,Constructor,(,),{,Var,p,:,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,43,],,,0B10110,],,,0x42,],,,43,],,,0b110101,],;,},Val,Z,,,$_,,,$6,:,Array,[,Array,[,Int,,,0x8B,],,,6,],;,Destructor,(,),{,},},Class,t_,:,__,{,Val,q,:,String,;,},<EOF>''',101))

    def test_1402(self):
        self.assertTrue(TestLexer.test('''Class x:_8{}Class k{Constructor (k,_B,_2:Array [Array [Int ,0b1],0B1_10];_E:String ){} }Class _HV:t{}Class _:z5{}Class M{Destructor (){} }Class E8{Var J:Boolean ;}Class _{Var $f:String ;}''','''Class,x,:,_8,{,},Class,k,{,Constructor,(,k,,,_B,,,_2,:,Array,[,Array,[,Int,,,0b1,],,,0B110,],;,_E,:,String,),{,},},Class,_HV,:,t,{,},Class,_,:,z5,{,},Class,M,{,Destructor,(,),{,},},Class,E8,{,Var,J,:,Boolean,;,},Class,_,{,Var,$f,:,String,;,},<EOF>''',101))

    def test_1403(self):
        self.assertTrue(TestLexer.test('''Class _Xp:_01ck3{$0p(){} }Class _:__6_t{Destructor (){}$_m(){}Val $__,$_j,wdb_J,_,L:Int ;Var $8__,_:Boolean ;}''','''Class,_Xp,:,_01ck3,{,$0p,(,),{,},},Class,_,:,__6_t,{,Destructor,(,),{,},$_m,(,),{,},Val,$__,,,$_j,,,wdb_J,,,_,,,L,:,Int,;,Var,$8__,,,_,:,Boolean,;,},<EOF>''',101))

    def test_1404(self):
        self.assertTrue(TestLexer.test('''Class _:__{$x(z_56,_2:Array [Array [Array [Array [Array [Array [Array [Float ,4],0137],8_7],0137],0B1001001],7_5],10]){}U7(K3B,__n_:_;A:String ;_,b,L,_:Array [Array [String ,0x8C],07];k:m1){} }''','''Class,_,:,__,{,$x,(,z_56,,,_2,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,4,],,,0137,],,,87,],,,0137,],,,0B1001001,],,,75,],,,10,],),{,},U7,(,K3B,,,__n_,:,_,;,A,:,String,;,_,,,b,,,L,,,_,:,Array,[,Array,[,String,,,0x8C,],,,07,],;,k,:,m1,),{,},},<EOF>''',101))

    def test_1405(self):
        self.assertTrue(TestLexer.test('''Class __:_{$_(K,g,_,po_:Array [Boolean ,0x32]){Break ;} }Class P06:O{$_g_(D:Float ){}Var _8,_V__0k6:Boolean ;}Class t:_{Var $Ur_,y6:Array [Array [Array [Boolean ,9],0x29C],0X6];}''','''Class,__,:,_,{,$_,(,K,,,g,,,_,,,po_,:,Array,[,Boolean,,,0x32,],),{,Break,;,},},Class,P06,:,O,{,$_g_,(,D,:,Float,),{,},Var,_8,,,_V__0k6,:,Boolean,;,},Class,t,:,_,{,Var,$Ur_,,,y6,:,Array,[,Array,[,Array,[,Boolean,,,9,],,,0x29C,],,,0X6,],;,},<EOF>''',101))

    def test_1406(self):
        self.assertTrue(TestLexer.test('''Class _:Y___QH_{}Class _{_(){}Constructor (v,_,h__0:t;t:Array [String ,0130]){}Destructor (){}Var $zs:Array [Float ,0X1];}''','''Class,_,:,Y___QH_,{,},Class,_,{,_,(,),{,},Constructor,(,v,,,_,,,h__0,:,t,;,t,:,Array,[,String,,,0130,],),{,},Destructor,(,),{,},Var,$zs,:,Array,[,Float,,,0X1,],;,},<EOF>''',101))

    def test_1407(self):
        self.assertTrue(TestLexer.test('''Class H:_A_X{}Class _5:u{}Class _v:j_{Constructor (_,D_,Fj__j5:_;L7_v:Array [Array [String ,04],0X23];_:Array [Array [Boolean ,011],0b1_0]){}Destructor (){ {_::$3();} }}Class a0D:_{}''','''Class,H,:,_A_X,{,},Class,_5,:,u,{,},Class,_v,:,j_,{,Constructor,(,_,,,D_,,,Fj__j5,:,_,;,L7_v,:,Array,[,Array,[,String,,,04,],,,0X23,],;,_,:,Array,[,Array,[,Boolean,,,011,],,,0b10,],),{,},Destructor,(,),{,{,_,::,$3,(,),;,},},},Class,a0D,:,_,{,},<EOF>''',101))

    def test_1408(self):
        self.assertTrue(TestLexer.test('''Class _:_{Val _,o_,T:Array [Array [Int ,0B1001110],0B1001110];Constructor (K_0,R:Array [Boolean ,0X1_3B3]){} }Class _Tm6{Var $_,$_w,Y_x_,$1669,$IZ,Cs_A6,$_:_0I;}''','''Class,_,:,_,{,Val,_,,,o_,,,T,:,Array,[,Array,[,Int,,,0B1001110,],,,0B1001110,],;,Constructor,(,K_0,,,R,:,Array,[,Boolean,,,0X13B3,],),{,},},Class,_Tm6,{,Var,$_,,,$_w,,,Y_x_,,,$1669,,,$IZ,,,Cs_A6,,,$_,:,_0I,;,},<EOF>''',101))

    def test_1409(self):
        self.assertTrue(TestLexer.test('''Class _:x__2{Val _T,$E:Array [Array [Array [Int ,0X59],1],0B10];}Class _{}Class l{Val Ba,$6_:Array [Array [Array [Int ,0B1_01_1],37],0X4];$_9(){Continue ;}$73j(){}Val $_:Int ;}Class Tv__31M3:_{a(Zbt:_02){} }''','''Class,_,:,x__2,{,Val,_T,,,$E,:,Array,[,Array,[,Array,[,Int,,,0X59,],,,1,],,,0B10,],;,},Class,_,{,},Class,l,{,Val,Ba,,,$6_,:,Array,[,Array,[,Array,[,Int,,,0B1011,],,,37,],,,0X4,],;,$_9,(,),{,Continue,;,},$73j,(,),{,},Val,$_,:,Int,;,},Class,Tv__31M3,:,_,{,a,(,Zbt,:,_02,),{,},},<EOF>''',101))

    def test_1410(self):
        self.assertTrue(TestLexer.test('''Class _:_j_{Constructor (){} }Class __d_:t{Val $69_:Array [Array [Boolean ,0b1_01],02];Destructor (){}Var $___W:Int ;}''','''Class,_,:,_j_,{,Constructor,(,),{,},},Class,__d_,:,t,{,Val,$69_,:,Array,[,Array,[,Boolean,,,0b101,],,,02,],;,Destructor,(,),{,},Var,$___W,:,Int,;,},<EOF>''',101))

    def test_1411(self):
        self.assertTrue(TestLexer.test('''Class ___3:__{}Class _:y{}Class _0_{Var $z,_0,x_3_,z_f16,$__,$_8,$U8053,_N,$k:Array [Int ,06];}Class MH{Var $_9:Int ;}''','''Class,___3,:,__,{,},Class,_,:,y,{,},Class,_0_,{,Var,$z,,,_0,,,x_3_,,,z_f16,,,$__,,,$_8,,,$U8053,,,_N,,,$k,:,Array,[,Int,,,06,],;,},Class,MH,{,Var,$_9,:,Int,;,},<EOF>''',101))

    def test_1412(self):
        self.assertTrue(TestLexer.test('''Class _e{Constructor (_D:String ){}Var $6_:Int ;Constructor (__0,_:Float ;__,_75,_,c:Array [String ,064]){Return ;}Var $8j,$JC5_,$28:__;}''','''Class,_e,{,Constructor,(,_D,:,String,),{,},Var,$6_,:,Int,;,Constructor,(,__0,,,_,:,Float,;,__,,,_75,,,_,,,c,:,Array,[,String,,,064,],),{,Return,;,},Var,$8j,,,$JC5_,,,$28,:,__,;,},<EOF>''',101))

    def test_1413(self):
        self.assertTrue(TestLexer.test('''Class _:q_A5{Var _cg4:Array [String ,0b11];Constructor (_:__VU;_,_J5:String ;e,g3:_8d;c_2,O,_X,q,Y:Array [String ,05_4_3];H_H,__,N2II,_:Array [Array [Array [Array [Array [Array [Array [Int ,0b1_0],0X4],19],0b101000],7_3],0XB],060]){} }Class _:_{}Class e__:_{Var J,_0:Z7__;}''','''Class,_,:,q_A5,{,Var,_cg4,:,Array,[,String,,,0b11,],;,Constructor,(,_,:,__VU,;,_,,,_J5,:,String,;,e,,,g3,:,_8d,;,c_2,,,O,,,_X,,,q,,,Y,:,Array,[,String,,,0543,],;,H_H,,,__,,,N2II,,,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0b10,],,,0X4,],,,19,],,,0b101000,],,,73,],,,0XB,],,,060,],),{,},},Class,_,:,_,{,},Class,e__,:,_,{,Var,J,,,_0,:,Z7__,;,},<EOF>''',101))

    def test_1414(self):
        self.assertTrue(TestLexer.test('''Class g_:_3G{Val $_,$i:Array [Array [Boolean ,80],56];Destructor (){}Constructor (){} }Class A:_7{$I(){} }Class q_:W{Val $5_:R;}Class w____2X:sh4s{}''','''Class,g_,:,_3G,{,Val,$_,,,$i,:,Array,[,Array,[,Boolean,,,80,],,,56,],;,Destructor,(,),{,},Constructor,(,),{,},},Class,A,:,_7,{,$I,(,),{,},},Class,q_,:,W,{,Val,$5_,:,R,;,},Class,w____2X,:,sh4s,{,},<EOF>''',101))

    def test_1415(self):
        self.assertTrue(TestLexer.test('''Class _{}Class _{Var Y:String ;Var $44,_8,$_a5,$i9:Float ;Val $_2__,_5rV:Array [Array [String ,06066242],0b11110];}''','''Class,_,{,},Class,_,{,Var,Y,:,String,;,Var,$44,,,_8,,,$_a5,,,$i9,:,Float,;,Val,$_2__,,,_5rV,:,Array,[,Array,[,String,,,06066242,],,,0b11110,],;,},<EOF>''',101))

    def test_1416(self):
        self.assertTrue(TestLexer.test('''Class __9{}Class _T:oS_{Destructor (){}Destructor (){Break ;} }Class K{Constructor (_,_,_:Array [Array [Array [Float ,0B1_1],30],053]){} }''','''Class,__9,{,},Class,_T,:,oS_,{,Destructor,(,),{,},Destructor,(,),{,Break,;,},},Class,K,{,Constructor,(,_,,,_,,,_,:,Array,[,Array,[,Array,[,Float,,,0B11,],,,30,],,,053,],),{,},},<EOF>''',101))

    def test_1417(self):
        self.assertTrue(TestLexer.test('''Class _:_{$_(){}Constructor (U_:_;u9_Yv,_,_0:_;x_0a,_:Array [String ,75];_nR,_,_,F:_;_0,_:_o){} }Class _{}Class _{}''','''Class,_,:,_,{,$_,(,),{,},Constructor,(,U_,:,_,;,u9_Yv,,,_,,,_0,:,_,;,x_0a,,,_,:,Array,[,String,,,75,],;,_nR,,,_,,,_,,,F,:,_,;,_0,,,_,:,_o,),{,},},Class,_,{,},Class,_,{,},<EOF>''',101))

    def test_1418(self):
        self.assertTrue(TestLexer.test('''Class _7{}Class _:c{Destructor (){c_X::$_();}Val $k:Array [Int ,0B1010000];}Class v:_{}Class j:H{}Class _:_J{}Class _M{}''','''Class,_7,{,},Class,_,:,c,{,Destructor,(,),{,c_X,::,$_,(,),;,},Val,$k,:,Array,[,Int,,,0B1010000,],;,},Class,v,:,_,{,},Class,j,:,H,{,},Class,_,:,_J,{,},Class,_M,{,},<EOF>''',101))

    def test_1419(self):
        self.assertTrue(TestLexer.test('''Class u{Val $4_:String ;Destructor (){Val j2:String ;Val _,_9,_lVE:Array [Float ,0b1011000];}Destructor (){} }Class rr{}''','''Class,u,{,Val,$4_,:,String,;,Destructor,(,),{,Val,j2,:,String,;,Val,_,,,_9,,,_lVE,:,Array,[,Float,,,0b1011000,],;,},Destructor,(,),{,},},Class,rr,{,},<EOF>''',101))

    def test_1420(self):
        self.assertTrue(TestLexer.test('''Class _D:D_3F6{Constructor (I:jF;i:Array [Float ,0x3D]){Continue ;} }Class _:E{}Class R_{Constructor (__:Array [Int ,0B10111];_,_j3,l:String ){}_8(){} }''','''Class,_D,:,D_3F6,{,Constructor,(,I,:,jF,;,i,:,Array,[,Float,,,0x3D,],),{,Continue,;,},},Class,_,:,E,{,},Class,R_,{,Constructor,(,__,:,Array,[,Int,,,0B10111,],;,_,,,_j3,,,l,:,String,),{,},_8,(,),{,},},<EOF>''',101))

    def test_1421(self):
        self.assertTrue(TestLexer.test('''Class _395_e4:OFY4___{Constructor (u___F31,o2:Array [Array [Float ,055],0B1];_k,l,x_,__,__y,I___,_0,y:Float ;_:Boolean ;__,_,n,_3E:Boolean ){} }''','''Class,_395_e4,:,OFY4___,{,Constructor,(,u___F31,,,o2,:,Array,[,Array,[,Float,,,055,],,,0B1,],;,_k,,,l,,,x_,,,__,,,__y,,,I___,,,_0,,,y,:,Float,;,_,:,Boolean,;,__,,,_,,,n,,,_3E,:,Boolean,),{,},},<EOF>''',101))

    def test_1422(self):
        self.assertTrue(TestLexer.test('''Class D{Val $M_,$Y,_j8:Float ;Constructor (__,_M,x:Array [Array [String ,0B11101],06]){} }Class g{Var $0_,$Jq75,_:Boolean ;}''','''Class,D,{,Val,$M_,,,$Y,,,_j8,:,Float,;,Constructor,(,__,,,_M,,,x,:,Array,[,Array,[,String,,,0B11101,],,,06,],),{,},},Class,g,{,Var,$0_,,,$Jq75,,,_,:,Boolean,;,},<EOF>''',101))

    def test_1423(self):
        self.assertTrue(TestLexer.test('''Class d3hk_:N{_4H_3_(I:Array [Array [Boolean ,0B10],07];_:Array [Boolean ,0B110101];_:L;_,Y97,y,M:Int ;___,__:___){}Constructor (){} }''','''Class,d3hk_,:,N,{,_4H_3_,(,I,:,Array,[,Array,[,Boolean,,,0B10,],,,07,],;,_,:,Array,[,Boolean,,,0B110101,],;,_,:,L,;,_,,,Y97,,,y,,,M,:,Int,;,___,,,__,:,___,),{,},Constructor,(,),{,},},<EOF>''',101))

    def test_1424(self):
        self.assertTrue(TestLexer.test('''Class _{}Class B_6:Y726_{Constructor (){}_2J__(P:Array [String ,05];__H8,_:Array [Array [String ,98],0b110_1]){Break ;}Destructor (){} }''','''Class,_,{,},Class,B_6,:,Y726_,{,Constructor,(,),{,},_2J__,(,P,:,Array,[,String,,,05,],;,__H8,,,_,:,Array,[,Array,[,String,,,98,],,,0b1101,],),{,Break,;,},Destructor,(,),{,},},<EOF>''',101))

    def test_1425(self):
        self.assertTrue(TestLexer.test('''Class X:U{$1(B,r:__;_,m_,G,_:f4_;_6:Array [Int ,0x4B];eT1,_,_7,_,K_X_99N8,_T,wf,W6:_){Continue ;Break ;Break ;}Var $7_:T;}Class Cy_L:_{}''','''Class,X,:,U,{,$1,(,B,,,r,:,__,;,_,,,m_,,,G,,,_,:,f4_,;,_6,:,Array,[,Int,,,0x4B,],;,eT1,,,_,,,_7,,,_,,,K_X_99N8,,,_T,,,wf,,,W6,:,_,),{,Continue,;,Break,;,Break,;,},Var,$7_,:,T,;,},Class,Cy_L,:,_,{,},<EOF>''',101))

    def test_1426(self):
        self.assertTrue(TestLexer.test('''Class N:_{Constructor (_,ApB:_7;y:Array [Array [Array [Array [Array [String ,0141],0xB],7],0141],040];b:Array [Int ,0141]){Break ;} }''','''Class,N,:,_,{,Constructor,(,_,,,ApB,:,_7,;,y,:,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0141,],,,0xB,],,,7,],,,0141,],,,040,],;,b,:,Array,[,Int,,,0141,],),{,Break,;,},},<EOF>''',101))

    def test_1427(self):
        self.assertTrue(TestLexer.test('''Class _{}Class FH_{}Class __{Destructor (){}Var $_,$9x_:Uy;Constructor (__,___:_;l:_;rQ:Array [Float ,0x7]){} }''','''Class,_,{,},Class,FH_,{,},Class,__,{,Destructor,(,),{,},Var,$_,,,$9x_,:,Uy,;,Constructor,(,__,,,___,:,_,;,l,:,_,;,rQ,:,Array,[,Float,,,0x7,],),{,},},<EOF>''',101))

    def test_1428(self):
        self.assertTrue(TestLexer.test('''Class _5_{Var _:Array [Boolean ,0B1];Constructor (){Break ;} }Class T:Ny{Val $0m:Int ;Constructor (_o:Array [String ,0B1];b:Float ;Mb_,cV2,__:y7L;Z,c7,__R_1:Float ){ {} }}''','''Class,_5_,{,Var,_,:,Array,[,Boolean,,,0B1,],;,Constructor,(,),{,Break,;,},},Class,T,:,Ny,{,Val,$0m,:,Int,;,Constructor,(,_o,:,Array,[,String,,,0B1,],;,b,:,Float,;,Mb_,,,cV2,,,__,:,y7L,;,Z,,,c7,,,__R_1,:,Float,),{,{,},},},<EOF>''',101))

    def test_1429(self):
        self.assertTrue(TestLexer.test('''Class _{}Class _{}Class _{}Class M:_{Constructor (){}$_(){}_(){}Var $_:Int ;Constructor (a,_Lb_,__:_){} }Class h81:I{}''','''Class,_,{,},Class,_,{,},Class,_,{,},Class,M,:,_,{,Constructor,(,),{,},$_,(,),{,},_,(,),{,},Var,$_,:,Int,;,Constructor,(,a,,,_Lb_,,,__,:,_,),{,},},Class,h81,:,I,{,},<EOF>''',101))

    def test_1430(self):
        self.assertTrue(TestLexer.test('''Class p_6:LF_{}Class T{}Class _:L_{}Class _:__D9{Constructor (s8,__k_2hx_H:s_;_,p_5M_,F_:Array [Int ,0xE];Jt472_:Boolean ;__,_M:Array [String ,0xDFB];g:Array [Boolean ,6]){Val _:String ;} }''','''Class,p_6,:,LF_,{,},Class,T,{,},Class,_,:,L_,{,},Class,_,:,__D9,{,Constructor,(,s8,,,__k_2hx_H,:,s_,;,_,,,p_5M_,,,F_,:,Array,[,Int,,,0xE,],;,Jt472_,:,Boolean,;,__,,,_M,:,Array,[,String,,,0xDFB,],;,g,:,Array,[,Boolean,,,6,],),{,Val,_,:,String,;,},},<EOF>''',101))

    def test_1431(self):
        self.assertTrue(TestLexer.test('''Class _:__{}Class V:D{$9_6(M:Array [Array [Boolean ,0B100111],0x54];H,s_,_8:Int ){Break ;} }Class _:a{Val $W_,$Jy_y,$7Z,_,_,g:Array [String ,0X33];$A(__,_,_,l,z2_:Int ;_M___:_GYH){}Var e:Array [Boolean ,0117];}''','''Class,_,:,__,{,},Class,V,:,D,{,$9_6,(,M,:,Array,[,Array,[,Boolean,,,0B100111,],,,0x54,],;,H,,,s_,,,_8,:,Int,),{,Break,;,},},Class,_,:,a,{,Val,$W_,,,$Jy_y,,,$7Z,,,_,,,_,,,g,:,Array,[,String,,,0X33,],;,$A,(,__,,,_,,,_,,,l,,,z2_,:,Int,;,_M___,:,_GYH,),{,},Var,e,:,Array,[,Boolean,,,0117,],;,},<EOF>''',101))

    def test_1432(self):
        self.assertTrue(TestLexer.test('''Class t{Val Pq_:Array [Boolean ,02];Var $7_:String ;$_(_:String ;_:Int ){ {} }Destructor (){} }Class J:_{o(__:Boolean ){Break ;} }Class _:b{Constructor (_A:Array [Array [Array [Float ,0X8],39],0XC]){}Var _,$NA,N,K:Array [Array [Boolean ,0B1010000],0b1_1];}Class E61{}Class IQ:tj_K{}''','''Class,t,{,Val,Pq_,:,Array,[,Boolean,,,02,],;,Var,$7_,:,String,;,$_,(,_,:,String,;,_,:,Int,),{,{,},},Destructor,(,),{,},},Class,J,:,_,{,o,(,__,:,Boolean,),{,Break,;,},},Class,_,:,b,{,Constructor,(,_A,:,Array,[,Array,[,Array,[,Float,,,0X8,],,,39,],,,0XC,],),{,},Var,_,,,$NA,,,N,,,K,:,Array,[,Array,[,Boolean,,,0B1010000,],,,0b11,],;,},Class,E61,{,},Class,IQ,:,tj_K,{,},<EOF>''',101))

    def test_1433(self):
        self.assertTrue(TestLexer.test('''Class _:B_{}Class l{L(v:Array [Float ,0X5E];LJ:Array [Array [Int ,0b1],69];_,nc_:Array [Array [Array [Array [Boolean ,0b1],0x2],69],0B11100];_1A:Array [Boolean ,0B11100]){Val ___I7,t:_6__I;}Var $4:Array [Int ,0b1_1_1_1_0_00];}''','''Class,_,:,B_,{,},Class,l,{,L,(,v,:,Array,[,Float,,,0X5E,],;,LJ,:,Array,[,Array,[,Int,,,0b1,],,,69,],;,_,,,nc_,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,0b1,],,,0x2,],,,69,],,,0B11100,],;,_1A,:,Array,[,Boolean,,,0B11100,],),{,Val,___I7,,,t,:,_6__I,;,},Var,$4,:,Array,[,Int,,,0b1111000,],;,},<EOF>''',101))

    def test_1434(self):
        self.assertTrue(TestLexer.test('''Class __:_{}Class N5Ad:U{Val $0,_,$4:Array [Float ,030];}Class _:_j7{Constructor (){ {} }Val _,$7_:Array [Array [Array [Array [Array [String ,1],0B101010],030],0b10001],0x58];}''','''Class,__,:,_,{,},Class,N5Ad,:,U,{,Val,$0,,,_,,,$4,:,Array,[,Float,,,030,],;,},Class,_,:,_j7,{,Constructor,(,),{,{,},},Val,_,,,$7_,:,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,1,],,,0B101010,],,,030,],,,0b10001,],,,0x58,],;,},<EOF>''',101))

    def test_1435(self):
        self.assertTrue(TestLexer.test('''Class Rr{}Class xe{$8(K,_,___:Array [Int ,0X28];_:Array [Array [Array [Array [Int ,02],7_65_5],04_1_26_36_2],58]){}Destructor (){}Constructor (_,Y:_;m,_:Array [Array [Array [Array [Array [Boolean ,06],05],79],01],0X28]){Break ;} }Class P:__{}Class _{}Class p:_5M_0{}''','''Class,Rr,{,},Class,xe,{,$8,(,K,,,_,,,___,:,Array,[,Int,,,0X28,],;,_,:,Array,[,Array,[,Array,[,Array,[,Int,,,02,],,,7655,],,,04126362,],,,58,],),{,},Destructor,(,),{,},Constructor,(,_,,,Y,:,_,;,m,,,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,06,],,,05,],,,79,],,,01,],,,0X28,],),{,Break,;,},},Class,P,:,__,{,},Class,_,{,},Class,p,:,_5M_0,{,},<EOF>''',101))

    def test_1436(self):
        self.assertTrue(TestLexer.test('''Class cu{}Class _0_585{F(_0,____5,_:_2){} }Class cU598:u{Val _:Array [Array [Boolean ,04],55_7];}Class F1:_N{Val $__:_;Val $8_:_S;}''','''Class,cu,{,},Class,_0_585,{,F,(,_0,,,____5,,,_,:,_2,),{,},},Class,cU598,:,u,{,Val,_,:,Array,[,Array,[,Boolean,,,04,],,,557,],;,},Class,F1,:,_N,{,Val,$__,:,_,;,Val,$8_,:,_S,;,},<EOF>''',101))

    def test_1437(self):
        self.assertTrue(TestLexer.test('''Class _:_X___8_{Val $Ja_D,$_3_:UPZe8__8;Val $r,m7_,V,$33,$9:q;Var _O,_,$8_,$5:oP;Var $M,I__:Array [Float ,0X2];}Class c0_:_9_7{Destructor (){} }Class x{}''','''Class,_,:,_X___8_,{,Val,$Ja_D,,,$_3_,:,UPZe8__8,;,Val,$r,,,m7_,,,V,,,$33,,,$9,:,q,;,Var,_O,,,_,,,$8_,,,$5,:,oP,;,Var,$M,,,I__,:,Array,[,Float,,,0X2,],;,},Class,c0_,:,_9_7,{,Destructor,(,),{,},},Class,x,{,},<EOF>''',101))

    def test_1438(self):
        self.assertTrue(TestLexer.test('''Class __:__n_y_Y{Val aH9,_j,__,$5gT,$HLr,$_:Q25__8;$Ap(__i8v:Array [Array [Array [Array [Array [Array [Int ,0xD],19],0X9],0xC_F],0x3D],045];__:M;t_:Array [Int ,0B1111_0_1];c,_:Float ){} }''','''Class,__,:,__n_y_Y,{,Val,aH9,,,_j,,,__,,,$5gT,,,$HLr,,,$_,:,Q25__8,;,$Ap,(,__i8v,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0xD,],,,19,],,,0X9,],,,0xCF,],,,0x3D,],,,045,],;,__,:,M,;,t_,:,Array,[,Int,,,0B111101,],;,c,,,_,:,Float,),{,},},<EOF>''',101))

    def test_1439(self):
        self.assertTrue(TestLexer.test('''Class fo38_3{Val $3:Array [Array [Array [Array [Float ,0B100001],0123],0b1_10],0x24];}Class q{}Class __9:s6{Val $o:M;Var _4_962:String ;}''','''Class,fo38_3,{,Val,$3,:,Array,[,Array,[,Array,[,Array,[,Float,,,0B100001,],,,0123,],,,0b110,],,,0x24,],;,},Class,q,{,},Class,__9,:,s6,{,Val,$o,:,M,;,Var,_4_962,:,String,;,},<EOF>''',101))

    def test_1440(self):
        self.assertTrue(TestLexer.test('''Class _:i{Constructor (){} }Class _7{Constructor (){} }Class m_{Destructor (){}Constructor (Kj:String ;_:String ;___,s7:String ;v_YY:Int ){} }Class __1{}''','''Class,_,:,i,{,Constructor,(,),{,},},Class,_7,{,Constructor,(,),{,},},Class,m_,{,Destructor,(,),{,},Constructor,(,Kj,:,String,;,_,:,String,;,___,,,s7,:,String,;,v_YY,:,Int,),{,},},Class,__1,{,},<EOF>''',101))

    def test_1441(self):
        self.assertTrue(TestLexer.test('''Class PyT{_(u_:A_){} }Class _a:q{Val B,$_62:Array [Array [Array [Float ,06_3_3],0x29_C_5],0x62];Var _,$JS:Array [Boolean ,0X15];}''','''Class,PyT,{,_,(,u_,:,A_,),{,},},Class,_a,:,q,{,Val,B,,,$_62,:,Array,[,Array,[,Array,[,Float,,,0633,],,,0x29C5,],,,0x62,],;,Var,_,,,$JS,:,Array,[,Boolean,,,0X15,],;,},<EOF>''',101))

    def test_1442(self):
        self.assertTrue(TestLexer.test('''Class zW8sw2{Constructor (_q,_:f2;L:String ;_43,o_,b_:_;O:Array [String ,0X37]){ {}o_::$_F._3._.o00_ZP2._();} }Class _:_{}''','''Class,zW8sw2,{,Constructor,(,_q,,,_,:,f2,;,L,:,String,;,_43,,,o_,,,b_,:,_,;,O,:,Array,[,String,,,0X37,],),{,{,},o_,::,$_F,.,_3,.,_,.,o00_ZP2,.,_,(,),;,},},Class,_,:,_,{,},<EOF>''',101))

    def test_1443(self):
        self.assertTrue(TestLexer.test('''Class S:V8{_(_o,irX__86:Int ;__6e_:Int ;Y:String ;x:Int ;V10C44Mb:Float ;m_:String ;b:Int ;O:Array [Int ,0X83_1]){} }Class _:g{}''','''Class,S,:,V8,{,_,(,_o,,,irX__86,:,Int,;,__6e_,:,Int,;,Y,:,String,;,x,:,Int,;,V10C44Mb,:,Float,;,m_,:,String,;,b,:,Int,;,O,:,Array,[,Int,,,0X831,],),{,},},Class,_,:,g,{,},<EOF>''',101))

    def test_1444(self):
        self.assertTrue(TestLexer.test('''Class l:G__Z{Constructor (_G:String ;_:Float ;e__9_N:Float ){} }Class _{Destructor (){} }Class a__:H{Val $P_F,_:Int ;}''','''Class,l,:,G__Z,{,Constructor,(,_G,:,String,;,_,:,Float,;,e__9_N,:,Float,),{,},},Class,_,{,Destructor,(,),{,},},Class,a__,:,H,{,Val,$P_F,,,_,:,Int,;,},<EOF>''',101))

    def test_1445(self):
        self.assertTrue(TestLexer.test('''Class _:__{_3(){}Constructor (F,H,g:c;Z,ro:Float ;O,_,hM,_,d:__;WPz:_6y){}m(){}r(__N,w:Array [Array [Array [Array [Int ,4_327],2],1_4],01];h,to_0,o,CS:A3){Continue ;} }Class __ad:_Oo8_{Var $_:Array [Int ,0X1C];}''','''Class,_,:,__,{,_3,(,),{,},Constructor,(,F,,,H,,,g,:,c,;,Z,,,ro,:,Float,;,O,,,_,,,hM,,,_,,,d,:,__,;,WPz,:,_6y,),{,},m,(,),{,},r,(,__N,,,w,:,Array,[,Array,[,Array,[,Array,[,Int,,,4327,],,,2,],,,14,],,,01,],;,h,,,to_0,,,o,,,CS,:,A3,),{,Continue,;,},},Class,__ad,:,_Oo8_,{,Var,$_,:,Array,[,Int,,,0X1C,],;,},<EOF>''',101))

    def test_1446(self):
        self.assertTrue(TestLexer.test('''Class E5{Constructor (_T2,_:Float ;__,qh,L:String ;__:Array [Array [Array [String ,57],0X10],5_1];h_Y_b:Array [Boolean ,0b1]){} }''','''Class,E5,{,Constructor,(,_T2,,,_,:,Float,;,__,,,qh,,,L,:,String,;,__,:,Array,[,Array,[,Array,[,String,,,57,],,,0X10,],,,51,],;,h_Y_b,:,Array,[,Boolean,,,0b1,],),{,},},<EOF>''',101))

    def test_1447(self):
        self.assertTrue(TestLexer.test('''Class _{Constructor (_Vi,_,___:Array [Array [Array [String ,0x3_8],0103],0103]){}Val C,$2_u:Boolean ;}Class ___{}Class F{}''','''Class,_,{,Constructor,(,_Vi,,,_,,,___,:,Array,[,Array,[,Array,[,String,,,0x38,],,,0103,],,,0103,],),{,},Val,C,,,$2_u,:,Boolean,;,},Class,___,{,},Class,F,{,},<EOF>''',101))

    def test_1448(self):
        self.assertTrue(TestLexer.test('''Class _B{}Class X{_(izR23:Array [Array [Array [Boolean ,062],0x8_3],05];_87:Array [Array [String ,0B10010],0B10010]){} }''','''Class,_B,{,},Class,X,{,_,(,izR23,:,Array,[,Array,[,Array,[,Boolean,,,062,],,,0x83,],,,05,],;,_87,:,Array,[,Array,[,String,,,0B10010,],,,0B10010,],),{,},},<EOF>''',101))

    def test_1449(self):
        self.assertTrue(TestLexer.test('''Class r{}Class m:k_{}Class I7{Var $_T,$1Y:Float ;Val $__8,$_,$7_6,i_,$3D8:Array [Boolean ,0b11];}Class _:_G3{Var $sK_:Int ;Var $8:w_98;}''','''Class,r,{,},Class,m,:,k_,{,},Class,I7,{,Var,$_T,,,$1Y,:,Float,;,Val,$__8,,,$_,,,$7_6,,,i_,,,$3D8,:,Array,[,Boolean,,,0b11,],;,},Class,_,:,_G3,{,Var,$sK_,:,Int,;,Var,$8,:,w_98,;,},<EOF>''',101))

    def test_1450(self):
        self.assertTrue(TestLexer.test('''Class _E_0_{Destructor (){} }Class Z{Constructor (__,_,_:String ;_8_4__:Array [Boolean ,0b1010100];_o20:Int ;_:O){}Destructor (){} }''','''Class,_E_0_,{,Destructor,(,),{,},},Class,Z,{,Constructor,(,__,,,_,,,_,:,String,;,_8_4__,:,Array,[,Boolean,,,0b1010100,],;,_o20,:,Int,;,_,:,O,),{,},Destructor,(,),{,},},<EOF>''',101))

    def test_1451(self):
        self.assertTrue(TestLexer.test('''Class _GC_{Val $_,_,_8OwAa:Array [Array [Array [String ,0b1],0X6],0X8];Val O_V5_:V;}Class __o{}Class K2{}Class r{Var _7_:Boolean ;}''','''Class,_GC_,{,Val,$_,,,_,,,_8OwAa,:,Array,[,Array,[,Array,[,String,,,0b1,],,,0X6,],,,0X8,],;,Val,O_V5_,:,V,;,},Class,__o,{,},Class,K2,{,},Class,r,{,Var,_7_,:,Boolean,;,},<EOF>''',101))

    def test_1452(self):
        self.assertTrue(TestLexer.test('''Class _:T{q_(X,___c6,a_:Array [Int ,11];O,n_j7:_E;p:String ;_:String ;__8_:String ){} }Class ___:d{Val g_:Array [Float ,05];Var R:_;}''','''Class,_,:,T,{,q_,(,X,,,___c6,,,a_,:,Array,[,Int,,,11,],;,O,,,n_j7,:,_E,;,p,:,String,;,_,:,String,;,__8_,:,String,),{,},},Class,___,:,d,{,Val,g_,:,Array,[,Float,,,05,],;,Var,R,:,_,;,},<EOF>''',101))

    def test_1453(self):
        self.assertTrue(TestLexer.test('''Class __:n166E{_(_:Array [Boolean ,0131]){}G(I:Array [Int ,03];_:Array [Boolean ,0X9];D:_m;g:Array [Array [Boolean ,8_9],0b10];V_:__5I_){Break ;} }''','''Class,__,:,n166E,{,_,(,_,:,Array,[,Boolean,,,0131,],),{,},G,(,I,:,Array,[,Int,,,03,],;,_,:,Array,[,Boolean,,,0X9,],;,D,:,_m,;,g,:,Array,[,Array,[,Boolean,,,89,],,,0b10,],;,V_,:,__5I_,),{,Break,;,},},<EOF>''',101))

    def test_1454(self):
        self.assertTrue(TestLexer.test('''Class r{}Class _q_9:g{}Class p_{}Class s6__h{Var _,$5M,___H:String ;Var V4o1_5:dz;Val l,__6,_3:Array [String ,0B110001];}''','''Class,r,{,},Class,_q_9,:,g,{,},Class,p_,{,},Class,s6__h,{,Var,_,,,$5M,,,___H,:,String,;,Var,V4o1_5,:,dz,;,Val,l,,,__6,,,_3,:,Array,[,String,,,0B110001,],;,},<EOF>''',101))

    def test_1455(self):
        self.assertTrue(TestLexer.test('''Class DWc:_3{$1(c,_j,_,_,fz056:Array [Array [Array [Array [Int ,0b1],0X5],0X59],0x38];__,f:S_;rT:Int ){Break ;} }Class _{}''','''Class,DWc,:,_3,{,$1,(,c,,,_j,,,_,,,_,,,fz056,:,Array,[,Array,[,Array,[,Array,[,Int,,,0b1,],,,0X5,],,,0X59,],,,0x38,],;,__,,,f,:,S_,;,rT,:,Int,),{,Break,;,},},Class,_,{,},<EOF>''',101))

    def test_1456(self):
        self.assertTrue(TestLexer.test('''Class Q_ma{___4(_,y_H:Array [Array [Array [Array [Array [Array [Array [Float ,055],0x5E],055],15],055],0X7],0X7]){} }''','''Class,Q_ma,{,___4,(,_,,,y_H,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,055,],,,0x5E,],,,055,],,,15,],,,055,],,,0X7,],,,0X7,],),{,},},<EOF>''',101))

    def test_1457(self):
        self.assertTrue(TestLexer.test('''Class _:h{Val $R,_,U__5,VG0__:Float ;$pe(){Break ;Return ;} }Class _:__9f5G0__{}Class n:_T2_{}Class e:_{Val _:_;Destructor (){}Var $I:Array [Array [Array [Boolean ,0b1010011],037],2];}Class _:q{}''','''Class,_,:,h,{,Val,$R,,,_,,,U__5,,,VG0__,:,Float,;,$pe,(,),{,Break,;,Return,;,},},Class,_,:,__9f5G0__,{,},Class,n,:,_T2_,{,},Class,e,:,_,{,Val,_,:,_,;,Destructor,(,),{,},Var,$I,:,Array,[,Array,[,Array,[,Boolean,,,0b1010011,],,,037,],,,2,],;,},Class,_,:,q,{,},<EOF>''',101))

    def test_1458(self):
        self.assertTrue(TestLexer.test('''Class _{}Class H7:T{}Class _:Nt{}Class Z{Val _,_:Array [Boolean ,0b10_1];Var $34,$1:Array [Array [Int ,0132],0B1];Var $95_,FT,_:Array [Array [String ,0b1],0x9];Val $9:_;}Class _{}''','''Class,_,{,},Class,H7,:,T,{,},Class,_,:,Nt,{,},Class,Z,{,Val,_,,,_,:,Array,[,Boolean,,,0b101,],;,Var,$34,,,$1,:,Array,[,Array,[,Int,,,0132,],,,0B1,],;,Var,$95_,,,FT,,,_,:,Array,[,Array,[,String,,,0b1,],,,0x9,],;,Val,$9,:,_,;,},Class,_,{,},<EOF>''',101))

    def test_1459(self):
        self.assertTrue(TestLexer.test('''Class _{}Class _:B{}Class _:_{Constructor (_N:_;_:oz;k:_Rf_m){m::$g._();} }Class d_:_{Destructor (){} }Class e:a5{}''','''Class,_,{,},Class,_,:,B,{,},Class,_,:,_,{,Constructor,(,_N,:,_,;,_,:,oz,;,k,:,_Rf_m,),{,m,::,$g,.,_,(,),;,},},Class,d_,:,_,{,Destructor,(,),{,},},Class,e,:,a5,{,},<EOF>''',101))

    def test_1460(self):
        self.assertTrue(TestLexer.test('''Class E:_940_2p{Destructor (){Continue ;{} }}Class i_{Val $_3__2,$9:Array [Array [Array [String ,43],0B1],0x24];Val _:Boolean ;}''','''Class,E,:,_940_2p,{,Destructor,(,),{,Continue,;,{,},},},Class,i_,{,Val,$_3__2,,,$9,:,Array,[,Array,[,Array,[,String,,,43,],,,0B1,],,,0x24,],;,Val,_,:,Boolean,;,},<EOF>''',101))

    def test_1461(self):
        self.assertTrue(TestLexer.test('''Class U:C{Constructor (__,_co,_o_:String ;B:Array [Array [Array [Boolean ,0b1],0b1],0130];_:Float ;_,k8,_,_:String ){}Destructor (){}Var $k,$p_,$Y_9,$_:Float ;}''','''Class,U,:,C,{,Constructor,(,__,,,_co,,,_o_,:,String,;,B,:,Array,[,Array,[,Array,[,Boolean,,,0b1,],,,0b1,],,,0130,],;,_,:,Float,;,_,,,k8,,,_,,,_,:,String,),{,},Destructor,(,),{,},Var,$k,,,$p_,,,$Y_9,,,$_,:,Float,;,},<EOF>''',101))

    def test_1462(self):
        self.assertTrue(TestLexer.test('''Class J{Destructor (){Break ;}Var $_:Array [String ,0b110101];Constructor (_:String ;_oMZ:_){ {} }Constructor (){Var _,y:_;}Destructor (){}Destructor (){}P3(K:String ;_,k:Array [Array [Array [Int ,7],0x5A],0x1]){}Destructor (){}Destructor (){} }''','''Class,J,{,Destructor,(,),{,Break,;,},Var,$_,:,Array,[,String,,,0b110101,],;,Constructor,(,_,:,String,;,_oMZ,:,_,),{,{,},},Constructor,(,),{,Var,_,,,y,:,_,;,},Destructor,(,),{,},Destructor,(,),{,},P3,(,K,:,String,;,_,,,k,:,Array,[,Array,[,Array,[,Int,,,7,],,,0x5A,],,,0x1,],),{,},Destructor,(,),{,},Destructor,(,),{,},},<EOF>''',101))

    def test_1463(self):
        self.assertTrue(TestLexer.test('''Class P_{Constructor (W,_,_,nK3K,_,__m:_V;_,_,H:Float ;__:Boolean ;F_2,_2:Array [Boolean ,067]){ {} }}Class _:v{}Class f:__{}''','''Class,P_,{,Constructor,(,W,,,_,,,_,,,nK3K,,,_,,,__m,:,_V,;,_,,,_,,,H,:,Float,;,__,:,Boolean,;,F_2,,,_2,:,Array,[,Boolean,,,067,],),{,{,},},},Class,_,:,v,{,},Class,f,:,__,{,},<EOF>''',101))

    def test_1464(self):
        self.assertTrue(TestLexer.test('''Class m:J{Constructor (Xh,h3_l,x_6_,_,w:Int ;___S:Array [Int ,0b100001];_84a:Float ;_0h,Z,_1,y,_34_,z,_:Array [Array [Float ,44],0b100001]){} }''','''Class,m,:,J,{,Constructor,(,Xh,,,h3_l,,,x_6_,,,_,,,w,:,Int,;,___S,:,Array,[,Int,,,0b100001,],;,_84a,:,Float,;,_0h,,,Z,,,_1,,,y,,,_34_,,,z,,,_,:,Array,[,Array,[,Float,,,44,],,,0b100001,],),{,},},<EOF>''',101))

    def test_1465(self):
        self.assertTrue(TestLexer.test('''Class _F_:T49{}Class ___:_5{}Class a_:_{Var B6:Float ;Destructor (){} }Class _{Val _:_;Destructor (){}Val J,$0:A;$P(___1p:Boolean ){} }Class __A_n_:q{Destructor (){} }''','''Class,_F_,:,T49,{,},Class,___,:,_5,{,},Class,a_,:,_,{,Var,B6,:,Float,;,Destructor,(,),{,},},Class,_,{,Val,_,:,_,;,Destructor,(,),{,},Val,J,,,$0,:,A,;,$P,(,___1p,:,Boolean,),{,},},Class,__A_n_,:,q,{,Destructor,(,),{,},},<EOF>''',101))

    def test_1466(self):
        self.assertTrue(TestLexer.test('''Class R8{Val i,$r:Boolean ;Constructor (){}Val $o__s85,g:Array [Float ,0b1];}Class z{Constructor (_,_:String ;_6_:Array [Array [String ,0B10],5];_0N:Int ;Gdg9_Mi4:Array [Boolean ,34]){} }''','''Class,R8,{,Val,i,,,$r,:,Boolean,;,Constructor,(,),{,},Val,$o__s85,,,g,:,Array,[,Float,,,0b1,],;,},Class,z,{,Constructor,(,_,,,_,:,String,;,_6_,:,Array,[,Array,[,String,,,0B10,],,,5,],;,_0N,:,Int,;,Gdg9_Mi4,:,Array,[,Boolean,,,34,],),{,},},<EOF>''',101))

    def test_1467(self):
        self.assertTrue(TestLexer.test('''Class _:_I{h_e(_:__;SB:B){} }Class _:uX1{}Class S{}Class a_1n_{Val $___,$28,_:_zem;Val _,m,A:hT5;_(){} }Class _5{}Class h{}''','''Class,_,:,_I,{,h_e,(,_,:,__,;,SB,:,B,),{,},},Class,_,:,uX1,{,},Class,S,{,},Class,a_1n_,{,Val,$___,,,$28,,,_,:,_zem,;,Val,_,,,m,,,A,:,hT5,;,_,(,),{,},},Class,_5,{,},Class,h,{,},<EOF>''',101))

    def test_1468(self):
        self.assertTrue(TestLexer.test('''Class __:_{$9_(){} }Class _9p:__Q_aq{Var _:Int ;Constructor (){} }Class A_{}Class I{_2(){Break ;}Var $V1D,$1_I3,l:Boolean ;_8(k:__;_:Array [Array [Int ,77],0b1000]){} }''','''Class,__,:,_,{,$9_,(,),{,},},Class,_9p,:,__Q_aq,{,Var,_,:,Int,;,Constructor,(,),{,},},Class,A_,{,},Class,I,{,_2,(,),{,Break,;,},Var,$V1D,,,$1_I3,,,l,:,Boolean,;,_8,(,k,:,__,;,_,:,Array,[,Array,[,Int,,,77,],,,0b1000,],),{,},},<EOF>''',101))

    def test_1469(self):
        self.assertTrue(TestLexer.test('''Class _{Val ____:Float ;Val P,_,_0:F;Constructor (_,_S,_,_,I,_,_,_ew,L,G,O:Array [Array [String ,0B1_0],0B1010000]){} }Class T__Gh{Destructor (){}$__5(Y,A_,__:Array [Int ,0x14];_8:Float ){Break ;}Var $8VM:e1;}Class H{}Class s:B{Destructor (){} }Class __8{Val $xJ:__;}Class _w:x{}Class P:t{}Class __t_:_7{z_0_m(){}Constructor (){Return ;} }Class Z:_{r_M(){} }Class _gc:Q{}Class g__:_{Constructor (){} }Class iQ:__9{}''','''Class,_,{,Val,____,:,Float,;,Val,P,,,_,,,_0,:,F,;,Constructor,(,_,,,_S,,,_,,,_,,,I,,,_,,,_,,,_ew,,,L,,,G,,,O,:,Array,[,Array,[,String,,,0B10,],,,0B1010000,],),{,},},Class,T__Gh,{,Destructor,(,),{,},$__5,(,Y,,,A_,,,__,:,Array,[,Int,,,0x14,],;,_8,:,Float,),{,Break,;,},Var,$8VM,:,e1,;,},Class,H,{,},Class,s,:,B,{,Destructor,(,),{,},},Class,__8,{,Val,$xJ,:,__,;,},Class,_w,:,x,{,},Class,P,:,t,{,},Class,__t_,:,_7,{,z_0_m,(,),{,},Constructor,(,),{,Return,;,},},Class,Z,:,_,{,r_M,(,),{,},},Class,_gc,:,Q,{,},Class,g__,:,_,{,Constructor,(,),{,},},Class,iQ,:,__9,{,},<EOF>''',101))

    def test_1470(self):
        self.assertTrue(TestLexer.test('''Class _:hZ{Constructor (_u,_,_:Array [Array [Array [Int ,0xD],077],033]){Continue ;}Constructor (__:Array [Float ,5_80]){} }Class _:E{}''','''Class,_,:,hZ,{,Constructor,(,_u,,,_,,,_,:,Array,[,Array,[,Array,[,Int,,,0xD,],,,077,],,,033,],),{,Continue,;,},Constructor,(,__,:,Array,[,Float,,,580,],),{,},},Class,_,:,E,{,},<EOF>''',101))

    def test_1471(self):
        self.assertTrue(TestLexer.test('''Class B:_{Var $3_e_35_,$J,_Q,_:Int ;}Class _{Destructor (){Return ;}$_(_:Array [String ,0X58];yl:Array [Array [Float ,90],0b1_11];_:Array [Float ,0120]){} }''','''Class,B,:,_,{,Var,$3_e_35_,,,$J,,,_Q,,,_,:,Int,;,},Class,_,{,Destructor,(,),{,Return,;,},$_,(,_,:,Array,[,String,,,0X58,],;,yl,:,Array,[,Array,[,Float,,,90,],,,0b111,],;,_,:,Array,[,Float,,,0120,],),{,},},<EOF>''',101))

    def test_1472(self):
        self.assertTrue(TestLexer.test('''Class v:_8{$_3(U_:Int ;_h,W_,_562l:BE;_YAhy16:Array [Float ,0B1];d_,b:Array [Float ,0B11_01];d_u_0:a;__,_:_){} }''','''Class,v,:,_8,{,$_3,(,U_,:,Int,;,_h,,,W_,,,_562l,:,BE,;,_YAhy16,:,Array,[,Float,,,0B1,],;,d_,,,b,:,Array,[,Float,,,0B1101,],;,d_u_0,:,a,;,__,,,_,:,_,),{,},},<EOF>''',101))

    def test_1473(self):
        self.assertTrue(TestLexer.test('''Class _{Constructor (_,_,Z9p:P;_6,__:Int ){} }Class n{}Class A_:_3{}Class t_a:_{Val Xi:Array [Array [Boolean ,0B1100001],45];Var v,$___:Float ;}''','''Class,_,{,Constructor,(,_,,,_,,,Z9p,:,P,;,_6,,,__,:,Int,),{,},},Class,n,{,},Class,A_,:,_3,{,},Class,t_a,:,_,{,Val,Xi,:,Array,[,Array,[,Boolean,,,0B1100001,],,,45,],;,Var,v,,,$___,:,Float,;,},<EOF>''',101))

    def test_1474(self):
        self.assertTrue(TestLexer.test('''Class _H:_{Destructor (){} }Class Z:_{$_(){Var z,h:Array [Array [Array [Array [Float ,5_14_7],0b10_011_1],0x9C],0B1011110];} }Class Nx5:E2{}''','''Class,_H,:,_,{,Destructor,(,),{,},},Class,Z,:,_,{,$_,(,),{,Var,z,,,h,:,Array,[,Array,[,Array,[,Array,[,Float,,,5147,],,,0b100111,],,,0x9C,],,,0B1011110,],;,},},Class,Nx5,:,E2,{,},<EOF>''',101))

    def test_1475(self):
        self.assertTrue(TestLexer.test('''Class tN:u{}Class N{Constructor (_E:Boolean ;D,_E66:o){}Destructor (){}$_(b_5:Array [Array [Array [Float ,03],0B1],0B10]){} }Class SW_{}''','''Class,tN,:,u,{,},Class,N,{,Constructor,(,_E,:,Boolean,;,D,,,_E66,:,o,),{,},Destructor,(,),{,},$_,(,b_5,:,Array,[,Array,[,Array,[,Float,,,03,],,,0B1,],,,0B10,],),{,},},Class,SW_,{,},<EOF>''',101))

    def test_1476(self):
        self.assertTrue(TestLexer.test('''Class __:__1Jm5_{$_1NM(_:Array [Array [Int ,0B1000],1];_,___,AmX:_;Y_:Array [Int ,02];Z:_e____SH;_:Array [Array [Array [Boolean ,37],04_3],5];_i8,o3:M){} }Class N{}''','''Class,__,:,__1Jm5_,{,$_1NM,(,_,:,Array,[,Array,[,Int,,,0B1000,],,,1,],;,_,,,___,,,AmX,:,_,;,Y_,:,Array,[,Int,,,02,],;,Z,:,_e____SH,;,_,:,Array,[,Array,[,Array,[,Boolean,,,37,],,,043,],,,5,],;,_i8,,,o3,:,M,),{,},},Class,N,{,},<EOF>''',101))

    def test_1477(self):
        self.assertTrue(TestLexer.test('''Class __407_5_qK_{}Class S_:_g_5{Val _05_,$_WB1,h_X0__:String ;s(A7p:_A__){} }Class _:J{}Class e{}Class W:__6mw{}''','''Class,__407_5_qK_,{,},Class,S_,:,_g_5,{,Val,_05_,,,$_WB1,,,h_X0__,:,String,;,s,(,A7p,:,_A__,),{,},},Class,_,:,J,{,},Class,e,{,},Class,W,:,__6mw,{,},<EOF>''',101))

    def test_1478(self):
        self.assertTrue(TestLexer.test('''Class _2:Z{Var $2:_F_y;}Class O4:x{}Class _g540C38__{Constructor (){}Constructor (Y,h,w:Array [Int ,6];_,_:Boolean ;_,d:Array [String ,06];h_R:__;_,i0:Int ){} }''','''Class,_2,:,Z,{,Var,$2,:,_F_y,;,},Class,O4,:,x,{,},Class,_g540C38__,{,Constructor,(,),{,},Constructor,(,Y,,,h,,,w,:,Array,[,Int,,,6,],;,_,,,_,:,Boolean,;,_,,,d,:,Array,[,String,,,06,],;,h_R,:,__,;,_,,,i0,:,Int,),{,},},<EOF>''',101))

    def test_1479(self):
        self.assertTrue(TestLexer.test('''Class _:_____{}Class ___{Val $x:Array [Array [Boolean ,18],10];Val $4,r,$P_,_Z:Array [Array [Array [Float ,0x15],0xA],18];Val $0,$0:Boolean ;Var $90_A__ei,$0_U_:z;}''','''Class,_,:,_____,{,},Class,___,{,Val,$x,:,Array,[,Array,[,Boolean,,,18,],,,10,],;,Val,$4,,,r,,,$P_,,,_Z,:,Array,[,Array,[,Array,[,Float,,,0x15,],,,0xA,],,,18,],;,Val,$0,,,$0,:,Boolean,;,Var,$90_A__ei,,,$0_U_,:,z,;,},<EOF>''',101))

    def test_1480(self):
        self.assertTrue(TestLexer.test('''Class _:_{na7_8_1(){C7::$T.e__();}_(wj93:Array [Array [Int ,0143],4];mp_o5K_,_:vU;iL,_6,_:Z3q__;y,_08:String ){} }''','''Class,_,:,_,{,na7_8_1,(,),{,C7,::,$T,.,e__,(,),;,},_,(,wj93,:,Array,[,Array,[,Int,,,0143,],,,4,],;,mp_o5K_,,,_,:,vU,;,iL,,,_6,,,_,:,Z3q__,;,y,,,_08,:,String,),{,},},<EOF>''',101))

    def test_1481(self):
        self.assertTrue(TestLexer.test('''Class z{Destructor (){} }Class __yqp_g{Var a:Array [Array [Boolean ,0b1],033];}Class Q{Destructor (){} }Class l6WOH_k{}Class g4:K_16V{}''','''Class,z,{,Destructor,(,),{,},},Class,__yqp_g,{,Var,a,:,Array,[,Array,[,Boolean,,,0b1,],,,033,],;,},Class,Q,{,Destructor,(,),{,},},Class,l6WOH_k,{,},Class,g4,:,K_16V,{,},<EOF>''',101))

    def test_1482(self):
        self.assertTrue(TestLexer.test('''Class _L{Constructor (v:j;t,_,_7w1_,tL,B_Qp,_:Array [Array [Array [Boolean ,0X42],8_7],0b1];__,_,x,M,_:_;Z:Boolean ;_7,_,_2,__:Float ;Bh,W:Array [Boolean ,5];g,Z:String ;_d,k,_:Boolean ){Continue ;} }''','''Class,_L,{,Constructor,(,v,:,j,;,t,,,_,,,_7w1_,,,tL,,,B_Qp,,,_,:,Array,[,Array,[,Array,[,Boolean,,,0X42,],,,87,],,,0b1,],;,__,,,_,,,x,,,M,,,_,:,_,;,Z,:,Boolean,;,_7,,,_,,,_2,,,__,:,Float,;,Bh,,,W,:,Array,[,Boolean,,,5,],;,g,,,Z,:,String,;,_d,,,k,,,_,:,Boolean,),{,Continue,;,},},<EOF>''',101))

    def test_1483(self):
        self.assertTrue(TestLexer.test('''Class f_:__3A_{Val $_:Array [Array [Array [Boolean ,074_3_51214_3],7],0XF];}Class s3__w:__{$3_r(){} }Class _J__:S{}''','''Class,f_,:,__3A_,{,Val,$_,:,Array,[,Array,[,Array,[,Boolean,,,0743512143,],,,7,],,,0XF,],;,},Class,s3__w,:,__,{,$3_r,(,),{,},},Class,_J__,:,S,{,},<EOF>''',101))

    def test_1484(self):
        self.assertTrue(TestLexer.test('''Class N_:z{}Class _{Val u_:Array [Array [Array [String ,30],0B1_0],0B1101];Constructor (_Q___,Fv:String ;b_76:_;_2_,G,_:Array [Float ,040]){} }''','''Class,N_,:,z,{,},Class,_,{,Val,u_,:,Array,[,Array,[,Array,[,String,,,30,],,,0B10,],,,0B1101,],;,Constructor,(,_Q___,,,Fv,:,String,;,b_76,:,_,;,_2_,,,G,,,_,:,Array,[,Float,,,040,],),{,},},<EOF>''',101))

    def test_1485(self):
        self.assertTrue(TestLexer.test('''Class _0D:__l108{}Class Ci{Constructor (E,_I8,_2h_,__,_,_,A:U8838){}Val $VE,_i9:Array [Int ,0X4];}Class __:L{}Class R:Hu{}''','''Class,_0D,:,__l108,{,},Class,Ci,{,Constructor,(,E,,,_I8,,,_2h_,,,__,,,_,,,_,,,A,:,U8838,),{,},Val,$VE,,,_i9,:,Array,[,Int,,,0X4,],;,},Class,__,:,L,{,},Class,R,:,Hu,{,},<EOF>''',101))

    def test_1486(self):
        self.assertTrue(TestLexer.test('''Class l:_{Constructor (){} }Class _:_{$_(____A3O46:Array [Array [Float ,074],0b101010];_5_2:Array [Float ,074];_3__6:Array [Boolean ,0x1_8];M:Int ){} }''','''Class,l,:,_,{,Constructor,(,),{,},},Class,_,:,_,{,$_,(,____A3O46,:,Array,[,Array,[,Float,,,074,],,,0b101010,],;,_5_2,:,Array,[,Float,,,074,],;,_3__6,:,Array,[,Boolean,,,0x18,],;,M,:,Int,),{,},},<EOF>''',101))

    def test_1487(self):
        self.assertTrue(TestLexer.test('''Class z{}Class _{Constructor (D:__){}$P_(S_6,_1:_0F){}Destructor (){}Constructor (P:Boolean ;oZ,T_985_w_:vu;Q:Float ){} }''','''Class,z,{,},Class,_,{,Constructor,(,D,:,__,),{,},$P_,(,S_6,,,_1,:,_0F,),{,},Destructor,(,),{,},Constructor,(,P,:,Boolean,;,oZ,,,T_985_w_,:,vu,;,Q,:,Float,),{,},},<EOF>''',101))

    def test_1488(self):
        self.assertTrue(TestLexer.test('''Class _{}Class _7:_t{$S054(){} }Class _{Destructor (){}Destructor (){i::$K._.mn._5();Continue ;} }Class _0_42:i{}''','''Class,_,{,},Class,_7,:,_t,{,$S054,(,),{,},},Class,_,{,Destructor,(,),{,},Destructor,(,),{,i,::,$K,.,_,.,mn,.,_5,(,),;,Continue,;,},},Class,_0_42,:,i,{,},<EOF>''',101))

    def test_1489(self):
        self.assertTrue(TestLexer.test('''Class m{$_l(U_y,_9___,__i2_,_,F_,S,H:Array [Array [Float ,023],0XF_2C];_:t5){Return ;}Var $__,$_:Array [Boolean ,0b1001111];Constructor (){}Destructor (){} }Class _:____66{}''','''Class,m,{,$_l,(,U_y,,,_9___,,,__i2_,,,_,,,F_,,,S,,,H,:,Array,[,Array,[,Float,,,023,],,,0XF2C,],;,_,:,t5,),{,Return,;,},Var,$__,,,$_,:,Array,[,Boolean,,,0b1001111,],;,Constructor,(,),{,},Destructor,(,),{,},},Class,_,:,____66,{,},<EOF>''',101))

    def test_1490(self):
        self.assertTrue(TestLexer.test('''Class i{Val $741:Array [Array [Int ,051],17];}Class _:__V{Var $9,b7,y:t48;}Class L{}Class M{}Class _B{}Class __:f73{}Class _{}''','''Class,i,{,Val,$741,:,Array,[,Array,[,Int,,,051,],,,17,],;,},Class,_,:,__V,{,Var,$9,,,b7,,,y,:,t48,;,},Class,L,{,},Class,M,{,},Class,_B,{,},Class,__,:,f73,{,},Class,_,{,},<EOF>''',101))

    def test_1491(self):
        self.assertTrue(TestLexer.test('''Class T:w1{}Class _:rHL{$X8(r:_;_M8,A6d0_:Array [Array [Array [Boolean ,0b110010],0xA],0b1_0_0]){} }Class _:_z{Val $gc,__O:v;}Class _:yG_{}Class _13__:Xld{}''','''Class,T,:,w1,{,},Class,_,:,rHL,{,$X8,(,r,:,_,;,_M8,,,A6d0_,:,Array,[,Array,[,Array,[,Boolean,,,0b110010,],,,0xA,],,,0b100,],),{,},},Class,_,:,_z,{,Val,$gc,,,__O,:,v,;,},Class,_,:,yG_,{,},Class,_13__,:,Xld,{,},<EOF>''',101))

    def test_1492(self):
        self.assertTrue(TestLexer.test('''Class j{$9(z9:b){Break ;} }Class _{}Class VZ_3_:S{}Class _:_{Var ___:Array [Array [Array [Boolean ,05],05],0B1001111];}''','''Class,j,{,$9,(,z9,:,b,),{,Break,;,},},Class,_,{,},Class,VZ_3_,:,S,{,},Class,_,:,_,{,Var,___,:,Array,[,Array,[,Array,[,Boolean,,,05,],,,05,],,,0B1001111,],;,},<EOF>''',101))

    def test_1493(self):
        self.assertTrue(TestLexer.test('''Class h_:_9{}Class _{Constructor (_,_:Array [Int ,0x4];_,_,_:_;Q5_,_Q:Boolean ;W_I,Q:Hi4){ {} }$_5(){}Val m,$_,_5_8:Array [Boolean ,0b11_0];}''','''Class,h_,:,_9,{,},Class,_,{,Constructor,(,_,,,_,:,Array,[,Int,,,0x4,],;,_,,,_,,,_,:,_,;,Q5_,,,_Q,:,Boolean,;,W_I,,,Q,:,Hi4,),{,{,},},$_5,(,),{,},Val,m,,,$_,,,_5_8,:,Array,[,Boolean,,,0b110,],;,},<EOF>''',101))

    def test_1494(self):
        self.assertTrue(TestLexer.test('''Class p:_cE{}Class _:_{Constructor (__:Array [Array [Int ,54],0b1011010];T5,__p,A__:Array [Array [Array [Int ,0x6],54],0x10]){}Constructor (){} }Class a7_:w{}Class lW_c{Destructor (){Break ;} }''','''Class,p,:,_cE,{,},Class,_,:,_,{,Constructor,(,__,:,Array,[,Array,[,Int,,,54,],,,0b1011010,],;,T5,,,__p,,,A__,:,Array,[,Array,[,Array,[,Int,,,0x6,],,,54,],,,0x10,],),{,},Constructor,(,),{,},},Class,a7_,:,w,{,},Class,lW_c,{,Destructor,(,),{,Break,;,},},<EOF>''',101))

    def test_1495(self):
        self.assertTrue(TestLexer.test('''Class tt_:J{Constructor (k7:Boolean ;x0:_4;w_,gvf7v,t,_,_1F,R1_6_,_,__,P:s;_89__5_,q:Int ;_:Float ){} }Class F8{}''','''Class,tt_,:,J,{,Constructor,(,k7,:,Boolean,;,x0,:,_4,;,w_,,,gvf7v,,,t,,,_,,,_1F,,,R1_6_,,,_,,,__,,,P,:,s,;,_89__5_,,,q,:,Int,;,_,:,Float,),{,},},Class,F8,{,},<EOF>''',101))

    def test_1496(self):
        self.assertTrue(TestLexer.test('''Class _:pF_1{Var $_,e:Int ;}Class gOg8{}Class aj{$7(_,__vd,_9,_,___,_0,_6:Array [Boolean ,0x45];AN_t:String ;P0,r___:_7I;V_:E){}Val _,$Aa:Int ;}Class _:__{}''','''Class,_,:,pF_1,{,Var,$_,,,e,:,Int,;,},Class,gOg8,{,},Class,aj,{,$7,(,_,,,__vd,,,_9,,,_,,,___,,,_0,,,_6,:,Array,[,Boolean,,,0x45,],;,AN_t,:,String,;,P0,,,r___,:,_7I,;,V_,:,E,),{,},Val,_,,,$Aa,:,Int,;,},Class,_,:,__,{,},<EOF>''',101))

    def test_1497(self):
        self.assertTrue(TestLexer.test('''Class _:_{Constructor (X,_,S,_:Array [String ,024]){}Val _0w__:String ;Constructor (O:Boolean ;_ht:Array [Array [Array [String ,0b1],0B1_01_0_100],04]){} }''','''Class,_,:,_,{,Constructor,(,X,,,_,,,S,,,_,:,Array,[,String,,,024,],),{,},Val,_0w__,:,String,;,Constructor,(,O,:,Boolean,;,_ht,:,Array,[,Array,[,Array,[,String,,,0b1,],,,0B1010100,],,,04,],),{,},},<EOF>''',101))

    def test_1498(self):
        self.assertTrue(TestLexer.test('''Class G{}Class G_l_Q:Z{Var $87kk:Array [Array [String ,0B100100],06_1];Constructor (){}mt(){}$_(_j_:Int ;I,__:Float ;_O_:r_){} }''','''Class,G,{,},Class,G_l_Q,:,Z,{,Var,$87kk,:,Array,[,Array,[,String,,,0B100100,],,,061,],;,Constructor,(,),{,},mt,(,),{,},$_,(,_j_,:,Int,;,I,,,__,:,Float,;,_O_,:,r_,),{,},},<EOF>''',101))

    def test_1499(self):
        self.assertTrue(TestLexer.test('''Class r:r{}Class Oc94__ow{Constructor (__A,_S_:Int ;_0r,V,Q,__:Array [Array [Array [Array [Array [Array [Array [Int ,3_1],0b11000],0x9],0X5A],8],4_2_8_9],0x9];_,_:_2;_:Array [Boolean ,4_01]){} }''','''Class,r,:,r,{,},Class,Oc94__ow,{,Constructor,(,__A,,,_S_,:,Int,;,_0r,,,V,,,Q,,,__,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,31,],,,0b11000,],,,0x9,],,,0X5A,],,,8,],,,4289,],,,0x9,],;,_,,,_,:,_2,;,_,:,Array,[,Boolean,,,401,],),{,},},<EOF>''',101))

    def test_1500(self):
        self.assertTrue(TestLexer.test('''Class _{Var $8:__mq_9;$_(k,_,__:e;_:Array [Array [Array [String ,0xA_5],0XF_5],94];_6,e_:e_t_968_){Return ;} }''','''Class,_,{,Var,$8,:,__mq_9,;,$_,(,k,,,_,,,__,:,e,;,_,:,Array,[,Array,[,Array,[,String,,,0xA5,],,,0XF5,],,,94,],;,_6,,,e_,:,e_t_968_,),{,Return,;,},},<EOF>''',101))

    def test_1501(self):
        self.assertTrue(TestLexer.test('''Class cH:c{Constructor (){}Constructor (){}Val K9:fd2_3_;Var c_,$_,cE5,__LX:Int ;}Class h{Destructor (){}Val cc,$26,_K27y,$4:Boolean ;_(_:Array [Int ,0b11010_0]){}Constructor (){}Val d_:Array [Array [Array [Float ,0x2C],01],0B1];}Class _9_Y{}Class _:Z{}''','''Class,cH,:,c,{,Constructor,(,),{,},Constructor,(,),{,},Val,K9,:,fd2_3_,;,Var,c_,,,$_,,,cE5,,,__LX,:,Int,;,},Class,h,{,Destructor,(,),{,},Val,cc,,,$26,,,_K27y,,,$4,:,Boolean,;,_,(,_,:,Array,[,Int,,,0b110100,],),{,},Constructor,(,),{,},Val,d_,:,Array,[,Array,[,Array,[,Float,,,0x2C,],,,01,],,,0B1,],;,},Class,_9_Y,{,},Class,_,:,Z,{,},<EOF>''',101))

    def test_1502(self):
        self.assertTrue(TestLexer.test('''Class F8:_K2_{Constructor (){Var a,Z:Boolean ;Continue ;Break ;}Val $H,$D:Array [Array [Array [Array [Array [Boolean ,0X6],0b111],55],53],1_6];Val $0_,$X,_:_;}''','''Class,F8,:,_K2_,{,Constructor,(,),{,Var,a,,,Z,:,Boolean,;,Continue,;,Break,;,},Val,$H,,,$D,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0X6,],,,0b111,],,,55,],,,53,],,,16,],;,Val,$0_,,,$X,,,_,:,_,;,},<EOF>''',101))

    def test_1503(self):
        self.assertTrue(TestLexer.test('''Class _D{}Class A:_{$_(_U_,HU,_3:Int ;_:Boolean ;_:_;d1:L9;_,u4e,_8__g,F_:_){ {Continue ;} }}Class X{Var $1SQ:Array [Array [String ,2_6],0XC];}Class _nk1:_{}''','''Class,_D,{,},Class,A,:,_,{,$_,(,_U_,,,HU,,,_3,:,Int,;,_,:,Boolean,;,_,:,_,;,d1,:,L9,;,_,,,u4e,,,_8__g,,,F_,:,_,),{,{,Continue,;,},},},Class,X,{,Var,$1SQ,:,Array,[,Array,[,String,,,26,],,,0XC,],;,},Class,_nk1,:,_,{,},<EOF>''',101))

    def test_1504(self):
        self.assertTrue(TestLexer.test('''Class _70I:_8{Constructor (){}Destructor (){}Val $1:Array [Array [Boolean ,0b1],1_8_4];Constructor (w:G){} }Class z5:nT_3a{}''','''Class,_70I,:,_8,{,Constructor,(,),{,},Destructor,(,),{,},Val,$1,:,Array,[,Array,[,Boolean,,,0b1,],,,184,],;,Constructor,(,w,:,G,),{,},},Class,z5,:,nT_3a,{,},<EOF>''',101))

    def test_1505(self):
        self.assertTrue(TestLexer.test('''Class _{Constructor (Q:Array [Array [Float ,9],27];t:Boolean ;iu,_7:Array [Array [Array [Array [Array [Float ,71],0B1],047],0B10_00],2];_2C:Boolean ;r,c8,q:Float ){Break ;} }''','''Class,_,{,Constructor,(,Q,:,Array,[,Array,[,Float,,,9,],,,27,],;,t,:,Boolean,;,iu,,,_7,:,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,71,],,,0B1,],,,047,],,,0B1000,],,,2,],;,_2C,:,Boolean,;,r,,,c8,,,q,:,Float,),{,Break,;,},},<EOF>''',101))

    def test_1506(self):
        self.assertTrue(TestLexer.test('''Class F{Val _:Boolean ;}Class M9Xy:_V{Val $C,$66:Int ;$Z(__:Float ;ra,_3_:Array [Int ,4];_,_,c,bQ:Float ;_,q,Q:Array [Boolean ,38];u,h_:Array [String ,0X3A];a:Int ){Continue ;} }''','''Class,F,{,Val,_,:,Boolean,;,},Class,M9Xy,:,_V,{,Val,$C,,,$66,:,Int,;,$Z,(,__,:,Float,;,ra,,,_3_,:,Array,[,Int,,,4,],;,_,,,_,,,c,,,bQ,:,Float,;,_,,,q,,,Q,:,Array,[,Boolean,,,38,],;,u,,,h_,:,Array,[,String,,,0X3A,],;,a,:,Int,),{,Continue,;,},},<EOF>''',101))

    def test_1507(self):
        self.assertTrue(TestLexer.test('''Class M{Constructor (k,G:A){}Destructor (){}Destructor (){ {}Return ;Continue ;} }Class _:_{Constructor (){ {} }}''','''Class,M,{,Constructor,(,k,,,G,:,A,),{,},Destructor,(,),{,},Destructor,(,),{,{,},Return,;,Continue,;,},},Class,_,:,_,{,Constructor,(,),{,{,},},},<EOF>''',101))

    def test_1508(self):
        self.assertTrue(TestLexer.test('''Class _:_9u{}Class __:_5_J{Val i3,$T:Y8;Constructor (){}Destructor (){Continue ;K::$k_();__::$RG();Continue ;} }Class _w2:r{Val _92,_,$Z_:_3;}''','''Class,_,:,_9u,{,},Class,__,:,_5_J,{,Val,i3,,,$T,:,Y8,;,Constructor,(,),{,},Destructor,(,),{,Continue,;,K,::,$k_,(,),;,__,::,$RG,(,),;,Continue,;,},},Class,_w2,:,r,{,Val,_92,,,_,,,$Z_,:,_3,;,},<EOF>''',101))

    def test_1509(self):
        self.assertTrue(TestLexer.test('''Class p__{Constructor (H,zcG:_K;d_00,_:Array [Boolean ,0X29];l,D,Kn:String ){}$G(__:Array [Array [Boolean ,5],0B1];_6_,U_:__){} }Class q1W:__t_{Constructor (){} }''','''Class,p__,{,Constructor,(,H,,,zcG,:,_K,;,d_00,,,_,:,Array,[,Boolean,,,0X29,],;,l,,,D,,,Kn,:,String,),{,},$G,(,__,:,Array,[,Array,[,Boolean,,,5,],,,0B1,],;,_6_,,,U_,:,__,),{,},},Class,q1W,:,__t_,{,Constructor,(,),{,},},<EOF>''',101))

    def test_1510(self):
        self.assertTrue(TestLexer.test('''Class a:_6__{}Class _:V{}Class _{Destructor (){} }Class k{}Class _:H{Destructor (){} }Class __{}Class AK_:_z{}Class __k__K:_{}''','''Class,a,:,_6__,{,},Class,_,:,V,{,},Class,_,{,Destructor,(,),{,},},Class,k,{,},Class,_,:,H,{,Destructor,(,),{,},},Class,__,{,},Class,AK_,:,_z,{,},Class,__k__K,:,_,{,},<EOF>''',101))

    def test_1511(self):
        self.assertTrue(TestLexer.test('''Class zBs2:_{}Class X6fW{Var $_:_;Val $3d:C;Val $w:Array [Array [String ,6_0],8_6_92];}Class _7:I_9I_{}Class _06:U{}''','''Class,zBs2,:,_,{,},Class,X6fW,{,Var,$_,:,_,;,Val,$3d,:,C,;,Val,$w,:,Array,[,Array,[,String,,,60,],,,8692,],;,},Class,_7,:,I_9I_,{,},Class,_06,:,U,{,},<EOF>''',101))

    def test_1512(self):
        self.assertTrue(TestLexer.test('''Class __:v_50{}Class _:eA{Constructor (){}Var V:Array [Array [Array [Array [Array [Int ,0B10_1],0b1100001],0XD],03],0X58];}''','''Class,__,:,v_50,{,},Class,_,:,eA,{,Constructor,(,),{,},Var,V,:,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0B101,],,,0b1100001,],,,0XD,],,,03,],,,0X58,],;,},<EOF>''',101))

    def test_1513(self):
        self.assertTrue(TestLexer.test('''Class _{Constructor (){}Constructor (P,l9:Array [Array [Array [Int ,01],05],0b1_0_1]){Continue ;}Constructor (V1__:Float ){}Constructor (b_6,bI,G__d,q,_3,_g_:T;_6_,WI1O,d0:S_d_){Continue ;} }Class _{Val $0,$f:Array [Int ,0X2_B];}Class c_O{}Class _7:__{}''','''Class,_,{,Constructor,(,),{,},Constructor,(,P,,,l9,:,Array,[,Array,[,Array,[,Int,,,01,],,,05,],,,0b101,],),{,Continue,;,},Constructor,(,V1__,:,Float,),{,},Constructor,(,b_6,,,bI,,,G__d,,,q,,,_3,,,_g_,:,T,;,_6_,,,WI1O,,,d0,:,S_d_,),{,Continue,;,},},Class,_,{,Val,$0,,,$f,:,Array,[,Int,,,0X2B,],;,},Class,c_O,{,},Class,_7,:,__,{,},<EOF>''',101))

    def test_1514(self):
        self.assertTrue(TestLexer.test('''Class d{}Class _6_{Constructor (_,_,_,i:Float ){}Var $2_:Array [Int ,0116];kI5(){ {} }}Class H_:b{Var $7:String ;Var Ro_y,$7,d,$R,$S9:Boolean ;}''','''Class,d,{,},Class,_6_,{,Constructor,(,_,,,_,,,_,,,i,:,Float,),{,},Var,$2_,:,Array,[,Int,,,0116,],;,kI5,(,),{,{,},},},Class,H_,:,b,{,Var,$7,:,String,;,Var,Ro_y,,,$7,,,d,,,$R,,,$S9,:,Boolean,;,},<EOF>''',101))

    def test_1515(self):
        self.assertTrue(TestLexer.test('''Class M{}Class j2_{_(E:Array [Int ,28];_,___,_,_,z7,_9_,Y4,h,_2_:Array [Boolean ,0b1]){Continue ;} }Class o___{}''','''Class,M,{,},Class,j2_,{,_,(,E,:,Array,[,Int,,,28,],;,_,,,___,,,_,,,_,,,z7,,,_9_,,,Y4,,,h,,,_2_,:,Array,[,Boolean,,,0b1,],),{,Continue,;,},},Class,o___,{,},<EOF>''',101))

    def test_1516(self):
        self.assertTrue(TestLexer.test('''Class _{Val $Qn:R_;Var _w:Array [Array [Array [Boolean ,71],060],060];_(__:T){Break ;} }Class K{Constructor (){} }Class x:__{$51(G:Array [Array [Float ,0X21],04]){} }''','''Class,_,{,Val,$Qn,:,R_,;,Var,_w,:,Array,[,Array,[,Array,[,Boolean,,,71,],,,060,],,,060,],;,_,(,__,:,T,),{,Break,;,},},Class,K,{,Constructor,(,),{,},},Class,x,:,__,{,$51,(,G,:,Array,[,Array,[,Float,,,0X21,],,,04,],),{,},},<EOF>''',101))

    def test_1517(self):
        self.assertTrue(TestLexer.test('''Class _5I2FDq85R:jI_{Constructor (_IU___,_,Z_,_,d:Array [Boolean ,0177];_1__,E,O,_,k05,wc8:Array [Array [String ,85],0B1]){_::$B();}Constructor (F:Array [Array [Array [Array [Boolean ,0XD64],0B101000],0B1_0],0x17]){} }''','''Class,_5I2FDq85R,:,jI_,{,Constructor,(,_IU___,,,_,,,Z_,,,_,,,d,:,Array,[,Boolean,,,0177,],;,_1__,,,E,,,O,,,_,,,k05,,,wc8,:,Array,[,Array,[,String,,,85,],,,0B1,],),{,_,::,$B,(,),;,},Constructor,(,F,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,0XD64,],,,0B101000,],,,0B10,],,,0x17,],),{,},},<EOF>''',101))

    def test_1518(self):
        self.assertTrue(TestLexer.test('''Class f:_{Destructor (){Return ;}Val R_6:Array [Boolean ,0B110];}Class _5{}Class _l{Constructor (){} }Class N:__{}''','''Class,f,:,_,{,Destructor,(,),{,Return,;,},Val,R_6,:,Array,[,Boolean,,,0B110,],;,},Class,_5,{,},Class,_l,{,Constructor,(,),{,},},Class,N,:,__,{,},<EOF>''',101))

    def test_1519(self):
        self.assertTrue(TestLexer.test('''Class _{a(D,r_,_,_d,__,_,_,k:Array [Array [Array [Array [Float ,021],8],73],0b1]){} }Class R:x{Val $_L0x,$d,$_,_:Int ;}''','''Class,_,{,a,(,D,,,r_,,,_,,,_d,,,__,,,_,,,_,,,k,:,Array,[,Array,[,Array,[,Array,[,Float,,,021,],,,8,],,,73,],,,0b1,],),{,},},Class,R,:,x,{,Val,$_L0x,,,$d,,,$_,,,_,:,Int,;,},<EOF>''',101))

    def test_1520(self):
        self.assertTrue(TestLexer.test('''Class X0:__{}Class b{}Class vC_{}Class w{Constructor (b,Q8___B,u,_v:Int ;V:String ;N,L,F3_t21:String ;_,Z:h){} }''','''Class,X0,:,__,{,},Class,b,{,},Class,vC_,{,},Class,w,{,Constructor,(,b,,,Q8___B,,,u,,,_v,:,Int,;,V,:,String,;,N,,,L,,,F3_t21,:,String,;,_,,,Z,:,h,),{,},},<EOF>''',101))

    def test_1521(self):
        self.assertTrue(TestLexer.test('''Class o3:D{$1__(o6fG,_:__y1;u,_,S_2lWi393:Array [Array [Boolean ,0503],033];D_:Array [Array [Array [Float ,06],7],0XFC5]){} }Class Fu{}''','''Class,o3,:,D,{,$1__,(,o6fG,,,_,:,__y1,;,u,,,_,,,S_2lWi393,:,Array,[,Array,[,Boolean,,,0503,],,,033,],;,D_,:,Array,[,Array,[,Array,[,Float,,,06,],,,7,],,,0XFC5,],),{,},},Class,Fu,{,},<EOF>''',101))

    def test_1522(self):
        self.assertTrue(TestLexer.test('''Class yq{}Class _:dyD{Constructor (_0,_k,O_5:Float ;R_5,L7:Array [Array [Array [Array [Int ,0b100],0b100],0142],0x2];f:I){} }''','''Class,yq,{,},Class,_,:,dyD,{,Constructor,(,_0,,,_k,,,O_5,:,Float,;,R_5,,,L7,:,Array,[,Array,[,Array,[,Array,[,Int,,,0b100,],,,0b100,],,,0142,],,,0x2,],;,f,:,I,),{,},},<EOF>''',101))

    def test_1523(self):
        self.assertTrue(TestLexer.test('''Class m:_4{Constructor (_2:_K;h:String ;_9nz_:Array [String ,0X46];yG:Float ;_:Int ){Val _:v;}Constructor (_g_5,q:Array [String ,0134];d:_P_){} }''','''Class,m,:,_4,{,Constructor,(,_2,:,_K,;,h,:,String,;,_9nz_,:,Array,[,String,,,0X46,],;,yG,:,Float,;,_,:,Int,),{,Val,_,:,v,;,},Constructor,(,_g_5,,,q,:,Array,[,String,,,0134,],;,d,:,_P_,),{,},},<EOF>''',101))

    def test_1524(self):
        self.assertTrue(TestLexer.test('''Class _:_D{_(_,_y3,_:w;_9,T,piL_vc2I:Array [Array [Array [Array [Boolean ,3_7],24],04],0B1];h3:Float ;_,Rj5:Array [Boolean ,6]){} }Class l{}''','''Class,_,:,_D,{,_,(,_,,,_y3,,,_,:,w,;,_9,,,T,,,piL_vc2I,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,37,],,,24,],,,04,],,,0B1,],;,h3,:,Float,;,_,,,Rj5,:,Array,[,Boolean,,,6,],),{,},},Class,l,{,},<EOF>''',101))

    def test_1525(self):
        self.assertTrue(TestLexer.test('''Class g{}Class cw031_5:A{Var $I,$__:Array [Array [Float ,0B1000001],656];Var $_4_2,$__:_34T;Val $3F_12,$mQK:Array [Int ,0XB];}''','''Class,g,{,},Class,cw031_5,:,A,{,Var,$I,,,$__,:,Array,[,Array,[,Float,,,0B1000001,],,,656,],;,Var,$_4_2,,,$__,:,_34T,;,Val,$3F_12,,,$mQK,:,Array,[,Int,,,0XB,],;,},<EOF>''',101))

    def test_1526(self):
        self.assertTrue(TestLexer.test('''Class a{Constructor (){}b(_26,g:Array [Array [Float ,030_5_0],022];L:String ;i3:Array [Array [Array [Array [Array [Array [Int ,0x7],0133],0133],0133],0x3A],0b11_01];_3,_,_i_7I,_2L_:Boolean ;_,t6Vy4__:Boolean ){}Constructor (_,_,znl:Array [Int ,39]){}Var $Z,$674:p9;}''','''Class,a,{,Constructor,(,),{,},b,(,_26,,,g,:,Array,[,Array,[,Float,,,03050,],,,022,],;,L,:,String,;,i3,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0x7,],,,0133,],,,0133,],,,0133,],,,0x3A,],,,0b1101,],;,_3,,,_,,,_i_7I,,,_2L_,:,Boolean,;,_,,,t6Vy4__,:,Boolean,),{,},Constructor,(,_,,,_,,,znl,:,Array,[,Int,,,39,],),{,},Var,$Z,,,$674,:,p9,;,},<EOF>''',101))

    def test_1527(self):
        self.assertTrue(TestLexer.test('''Class R{$n__(){}Destructor (){}Destructor (){}_(_:Int ;_0__:Array [Array [Array [Array [String ,05],067],03_6],0X46]){Break ;} }Class _:_{}''','''Class,R,{,$n__,(,),{,},Destructor,(,),{,},Destructor,(,),{,},_,(,_,:,Int,;,_0__,:,Array,[,Array,[,Array,[,Array,[,String,,,05,],,,067,],,,036,],,,0X46,],),{,Break,;,},},Class,_,:,_,{,},<EOF>''',101))

    def test_1528(self):
        self.assertTrue(TestLexer.test('''Class _{Val $2IC:_;Destructor (){}Destructor (){ {} }Var $q41R:Array [Array [Array [Float ,0107],0107],0X7];Constructor (){} }''','''Class,_,{,Val,$2IC,:,_,;,Destructor,(,),{,},Destructor,(,),{,{,},},Var,$q41R,:,Array,[,Array,[,Array,[,Float,,,0107,],,,0107,],,,0X7,],;,Constructor,(,),{,},},<EOF>''',101))

    def test_1529(self):
        self.assertTrue(TestLexer.test('''Class _{r5(L,FN__,_,F:E;_b:_;_:Array [Float ,4_513]){Val s,i:Array [String ,0b110010];}$_(h,U0:Array [Int ,0B100000];l:Int ){Return ;Break ;} }''','''Class,_,{,r5,(,L,,,FN__,,,_,,,F,:,E,;,_b,:,_,;,_,:,Array,[,Float,,,4513,],),{,Val,s,,,i,:,Array,[,String,,,0b110010,],;,},$_,(,h,,,U0,:,Array,[,Int,,,0B100000,],;,l,:,Int,),{,Return,;,Break,;,},},<EOF>''',101))

    def test_1530(self):
        self.assertTrue(TestLexer.test('''Class e{Val $_:_5EA1__;$7(_0:_;__i,__:Int ;F_,x,O4__m,n9gF,U,L5:Array [Int ,0B1000];_z_:E7h;Z,_h_,_:_1;_:Int ){Var V1,__,W:String ;{} }}''','''Class,e,{,Val,$_,:,_5EA1__,;,$7,(,_0,:,_,;,__i,,,__,:,Int,;,F_,,,x,,,O4__m,,,n9gF,,,U,,,L5,:,Array,[,Int,,,0B1000,],;,_z_,:,E7h,;,Z,,,_h_,,,_,:,_1,;,_,:,Int,),{,Var,V1,,,__,,,W,:,String,;,{,},},},<EOF>''',101))

    def test_1531(self):
        self.assertTrue(TestLexer.test('''Class W{Destructor (){}Q_H(__,_c0:Int ;V,_T8,_3C:Array [Array [Int ,0b101],0B11];___:Array [Array [String ,0B1011111],03_0];M_Vt,U_,z:W){} }Class A57:b{}''','''Class,W,{,Destructor,(,),{,},Q_H,(,__,,,_c0,:,Int,;,V,,,_T8,,,_3C,:,Array,[,Array,[,Int,,,0b101,],,,0B11,],;,___,:,Array,[,Array,[,String,,,0B1011111,],,,030,],;,M_Vt,,,U_,,,z,:,W,),{,},},Class,A57,:,b,{,},<EOF>''',101))

    def test_1532(self):
        self.assertTrue(TestLexer.test('''Class _T:x{Val $u6__oq:Array [Array [Float ,2],15];}Class MV_:_T1_{Constructor (_:Float ){}Destructor (){}N_t(){Var v,q0_q:Array [Array [String ,0b11010],0B10];} }''','''Class,_T,:,x,{,Val,$u6__oq,:,Array,[,Array,[,Float,,,2,],,,15,],;,},Class,MV_,:,_T1_,{,Constructor,(,_,:,Float,),{,},Destructor,(,),{,},N_t,(,),{,Var,v,,,q0_q,:,Array,[,Array,[,String,,,0b11010,],,,0B10,],;,},},<EOF>''',101))

    def test_1533(self):
        self.assertTrue(TestLexer.test('''Class _{}Class y{}Class _{}Class b_:R{Do(_j84m:_){}u(_3,_9,_:__2;A:Array [String ,0x54]){ {} }Val D2:Int ;R9Z_(){}Var $4:J_;}''','''Class,_,{,},Class,y,{,},Class,_,{,},Class,b_,:,R,{,Do,(,_j84m,:,_,),{,},u,(,_3,,,_9,,,_,:,__2,;,A,:,Array,[,String,,,0x54,],),{,{,},},Val,D2,:,Int,;,R9Z_,(,),{,},Var,$4,:,J_,;,},<EOF>''',101))

    def test_1534(self):
        self.assertTrue(TestLexer.test('''Class g:_1{}Class __24_{}Class _{Constructor (_,V_4,_,_,J,X:_;V:_){Break ;} }Class K8{$0_(){} }Class __iR32i:Z{}Class Q_:_{}''','''Class,g,:,_1,{,},Class,__24_,{,},Class,_,{,Constructor,(,_,,,V_4,,,_,,,_,,,J,,,X,:,_,;,V,:,_,),{,Break,;,},},Class,K8,{,$0_,(,),{,},},Class,__iR32i,:,Z,{,},Class,Q_,:,_,{,},<EOF>''',101))

    def test_1535(self):
        self.assertTrue(TestLexer.test('''Class _{}Class _{}Class b{}Class _i_:Iv{Constructor (_,_,i_9:Int ;_,HHJ:Array [Array [Array [Int ,8],041],0b1]){} }''','''Class,_,{,},Class,_,{,},Class,b,{,},Class,_i_,:,Iv,{,Constructor,(,_,,,_,,,i_9,:,Int,;,_,,,HHJ,:,Array,[,Array,[,Array,[,Int,,,8,],,,041,],,,0b1,],),{,},},<EOF>''',101))

    def test_1536(self):
        self.assertTrue(TestLexer.test('''Class _{Constructor (){}pa_6(_,G_06,_,s_:Boolean ;UaC:Array [Array [Array [Boolean ,0B1001011],0X3_31_D],077_3];_,e:Array [String ,02]){} }''','''Class,_,{,Constructor,(,),{,},pa_6,(,_,,,G_06,,,_,,,s_,:,Boolean,;,UaC,:,Array,[,Array,[,Array,[,Boolean,,,0B1001011,],,,0X331D,],,,0773,],;,_,,,e,:,Array,[,String,,,02,],),{,},},<EOF>''',101))

    def test_1537(self):
        self.assertTrue(TestLexer.test('''Class s:X{Constructor (__g_5,xD,jm4:Int ;h,___w:_J_9_E;_z:Int ;_R6,P5:Array [Array [Boolean ,78],4];_,_,iS:Float ){}Constructor (_:String ;p:Array [Int ,0b10001];U_:Int ;_60:Array [Boolean ,0b10001];B_:_e){}Var $q:V7;}Class _{}''','''Class,s,:,X,{,Constructor,(,__g_5,,,xD,,,jm4,:,Int,;,h,,,___w,:,_J_9_E,;,_z,:,Int,;,_R6,,,P5,:,Array,[,Array,[,Boolean,,,78,],,,4,],;,_,,,_,,,iS,:,Float,),{,},Constructor,(,_,:,String,;,p,:,Array,[,Int,,,0b10001,],;,U_,:,Int,;,_60,:,Array,[,Boolean,,,0b10001,],;,B_,:,_e,),{,},Var,$q,:,V7,;,},Class,_,{,},<EOF>''',101))

    def test_1538(self):
        self.assertTrue(TestLexer.test('''Class Y{Constructor (___:_;T_,_:Array [Array [Array [Array [Array [Array [Array [Boolean ,0X60],1],0B1_0_10],0b1000011],052],051],03];_5,_v,hg6:P5L){}Destructor (){} }''','''Class,Y,{,Constructor,(,___,:,_,;,T_,,,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0X60,],,,1,],,,0B1010,],,,0b1000011,],,,052,],,,051,],,,03,],;,_5,,,_v,,,hg6,:,P5L,),{,},Destructor,(,),{,},},<EOF>''',101))

    def test_1539(self):
        self.assertTrue(TestLexer.test('''Class _tV{Var _8_9_:Array [Int ,067];Destructor (){Continue ;Break ;Continue ;}Var $7,_8:Float ;}Class k_:i9{}Class A6_P:_{}''','''Class,_tV,{,Var,_8_9_,:,Array,[,Int,,,067,],;,Destructor,(,),{,Continue,;,Break,;,Continue,;,},Var,$7,,,_8,:,Float,;,},Class,k_,:,i9,{,},Class,A6_P,:,_,{,},<EOF>''',101))

    def test_1540(self):
        self.assertTrue(TestLexer.test('''Class _:__0c_J{Constructor (){}Constructor (){Continue ;} }Class _{}Class m_{$_(_8:Int ){}Destructor (){ {} }}Class j{}''','''Class,_,:,__0c_J,{,Constructor,(,),{,},Constructor,(,),{,Continue,;,},},Class,_,{,},Class,m_,{,$_,(,_8,:,Int,),{,},Destructor,(,),{,{,},},},Class,j,{,},<EOF>''',101))

    def test_1541(self):
        self.assertTrue(TestLexer.test('''Class L:_9W5_{}Class _{Constructor (T:f_;_,H,K,yk7:Array [Float ,0X2C]){} }Class _:_{Val v,$m:Array [Array [Array [Array [Array [Boolean ,0121],0B1010001],27],0X8],27];$18__(){}Val s:E;Constructor (){} }''','''Class,L,:,_9W5_,{,},Class,_,{,Constructor,(,T,:,f_,;,_,,,H,,,K,,,yk7,:,Array,[,Float,,,0X2C,],),{,},},Class,_,:,_,{,Val,v,,,$m,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0121,],,,0B1010001,],,,27,],,,0X8,],,,27,],;,$18__,(,),{,},Val,s,:,E,;,Constructor,(,),{,},},<EOF>''',101))

    def test_1542(self):
        self.assertTrue(TestLexer.test('''Class _:f_{}Class _068{Destructor (){}Destructor (){}Constructor (){}Constructor (_1,_9:Array [Float ,075]){}$X(A:Boolean ;X:Array [Array [Int ,0X20],7]){} }Class _{Val $L_9_19,$7_,$E:Float ;}''','''Class,_,:,f_,{,},Class,_068,{,Destructor,(,),{,},Destructor,(,),{,},Constructor,(,),{,},Constructor,(,_1,,,_9,:,Array,[,Float,,,075,],),{,},$X,(,A,:,Boolean,;,X,:,Array,[,Array,[,Int,,,0X20,],,,7,],),{,},},Class,_,{,Val,$L_9_19,,,$7_,,,$E,:,Float,;,},<EOF>''',101))

    def test_1543(self):
        self.assertTrue(TestLexer.test('''Class _:e2R{Constructor (D,E4:String ;Y,____n_:String ){} }Class ___{F_(t,N1_o,_,w:String ){ {} }}Class _1{}Class s{}Class v_{Constructor (n:Array [Array [Array [Array [String ,0b1],7],05],0b1]){Return ;}Var d4_5,Pc:__8a;}''','''Class,_,:,e2R,{,Constructor,(,D,,,E4,:,String,;,Y,,,____n_,:,String,),{,},},Class,___,{,F_,(,t,,,N1_o,,,_,,,w,:,String,),{,{,},},},Class,_1,{,},Class,s,{,},Class,v_,{,Constructor,(,n,:,Array,[,Array,[,Array,[,Array,[,String,,,0b1,],,,7,],,,05,],,,0b1,],),{,Return,;,},Var,d4_5,,,Pc,:,__8a,;,},<EOF>''',101))

    def test_1544(self):
        self.assertTrue(TestLexer.test('''Class _{Constructor (){}Var $eX:Array [Int ,037];Val _8p_,$__:Array [Float ,07_5];}Class __:r_9{Constructor (_:wT4O_;_0666P_,r__J_2,_5:W5;_:Float ){} }Class _:_h_{}Class _:xW{}''','''Class,_,{,Constructor,(,),{,},Var,$eX,:,Array,[,Int,,,037,],;,Val,_8p_,,,$__,:,Array,[,Float,,,075,],;,},Class,__,:,r_9,{,Constructor,(,_,:,wT4O_,;,_0666P_,,,r__J_2,,,_5,:,W5,;,_,:,Float,),{,},},Class,_,:,_h_,{,},Class,_,:,xW,{,},<EOF>''',101))

    def test_1545(self):
        self.assertTrue(TestLexer.test('''Class Q:uL{}Class V46021:c{}Class TC:_{Constructor (__0,PAm_3,vX,_,_:Array [Array [Array [Array [Array [Array [Array [Int ,9],0100],0x5],0X8],01_7],0xE],0xD]){}N_(){Return ;Break ;} }Class l:PC{Constructor (){Continue ;}d(){} }''','''Class,Q,:,uL,{,},Class,V46021,:,c,{,},Class,TC,:,_,{,Constructor,(,__0,,,PAm_3,,,vX,,,_,,,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,9,],,,0100,],,,0x5,],,,0X8,],,,017,],,,0xE,],,,0xD,],),{,},N_,(,),{,Return,;,Break,;,},},Class,l,:,PC,{,Constructor,(,),{,Continue,;,},d,(,),{,},},<EOF>''',101))

    def test_1546(self):
        self.assertTrue(TestLexer.test('''Class __{$F(Q9h5,_9,_9,a:Boolean ;_H,U:Boolean ;Wu:Array [String ,66];_:Array [String ,0X15];Rv,lW:_;u9_,__o,_:L__R){} }Class __:d_{Val $6:_;Var $d1A,_E:Array [Array [Array [Array [Array [Int ,0xC],66],0X4],011],0b1_00];}Class A:K5_26{Destructor (){} }Class G:_W_{$__(_,__,ATy,Y,GW,_,_4:Array [String ,011]){} }''','''Class,__,{,$F,(,Q9h5,,,_9,,,_9,,,a,:,Boolean,;,_H,,,U,:,Boolean,;,Wu,:,Array,[,String,,,66,],;,_,:,Array,[,String,,,0X15,],;,Rv,,,lW,:,_,;,u9_,,,__o,,,_,:,L__R,),{,},},Class,__,:,d_,{,Val,$6,:,_,;,Var,$d1A,,,_E,:,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0xC,],,,66,],,,0X4,],,,011,],,,0b100,],;,},Class,A,:,K5_26,{,Destructor,(,),{,},},Class,G,:,_W_,{,$__,(,_,,,__,,,ATy,,,Y,,,GW,,,_,,,_4,:,Array,[,String,,,011,],),{,},},<EOF>''',101))

    def test_1547(self):
        self.assertTrue(TestLexer.test('''Class _3B4{Var a:Array [Array [Array [Array [Array [Array [Array [Array [Array [Int ,04_351],05],8],05],6],05],4],0665],0X24];}''','''Class,_3B4,{,Var,a,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,04351,],,,05,],,,8,],,,05,],,,6,],,,05,],,,4,],,,0665,],,,0X24,],;,},<EOF>''',101))

    def test_1548(self):
        self.assertTrue(TestLexer.test('''Class E:_{}Class _{}Class _{Var _:_S;}Class _{Val $4:o;Var d_,_:String ;}Class y6d:F_9{E(J,_,_6:Float ){Continue ;} }Class g3{}''','''Class,E,:,_,{,},Class,_,{,},Class,_,{,Var,_,:,_S,;,},Class,_,{,Val,$4,:,o,;,Var,d_,,,_,:,String,;,},Class,y6d,:,F_9,{,E,(,J,,,_,,,_6,:,Float,),{,Continue,;,},},Class,g3,{,},<EOF>''',101))

    def test_1549(self):
        self.assertTrue(TestLexer.test('''Class _:__S{Var __aMZ:Array [Array [Array [Array [Array [Array [Boolean ,27],0xA],0b11],53],7623],53];}Class _{Val n,_:Boolean ;}''','''Class,_,:,__S,{,Var,__aMZ,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,27,],,,0xA,],,,0b11,],,,53,],,,7623,],,,53,],;,},Class,_,{,Val,n,,,_,:,Boolean,;,},<EOF>''',101))

    def test_1550(self):
        self.assertTrue(TestLexer.test('''Class Q{}Class _RV:_{}Class _1:_{Var $3,$L1:Array [Array [Array [Int ,022],0X3_E],40];Constructor (S1:_){Break ;}Var $_:Array [Int ,0X5B];}Class a8{$_V(_,_9u:__9){} }Class _{}Class _{}''','''Class,Q,{,},Class,_RV,:,_,{,},Class,_1,:,_,{,Var,$3,,,$L1,:,Array,[,Array,[,Array,[,Int,,,022,],,,0X3E,],,,40,],;,Constructor,(,S1,:,_,),{,Break,;,},Var,$_,:,Array,[,Int,,,0X5B,],;,},Class,a8,{,$_V,(,_,,,_9u,:,__9,),{,},},Class,_,{,},Class,_,{,},<EOF>''',101))

    def test_1551(self):
        self.assertTrue(TestLexer.test('''Class _:k{}Class O:X{Constructor (E_P__,_:String ;_n:h;M,__L,_2N:_;o7T,_,Y:w_;_:String ;_:Float ;__,_:Boolean ;_:Float ){ {Val _:Array [Boolean ,0b1];} }}''','''Class,_,:,k,{,},Class,O,:,X,{,Constructor,(,E_P__,,,_,:,String,;,_n,:,h,;,M,,,__L,,,_2N,:,_,;,o7T,,,_,,,Y,:,w_,;,_,:,String,;,_,:,Float,;,__,,,_,:,Boolean,;,_,:,Float,),{,{,Val,_,:,Array,[,Boolean,,,0b1,],;,},},},<EOF>''',101))

    def test_1552(self):
        self.assertTrue(TestLexer.test('''Class _{}Class RS:_{$___E(c,Rc_8:f85;k:String ;___:Array [Array [Boolean ,0x3C],0XC6D_A]){Break ;} }Class _o_5:___{}Class o19{}Class _:_{}Class _Es{Var $2,$sA_pi:s;Val $i2,$J:Array [Array [Int ,063],0x3C];Val $6:Int ;}''','''Class,_,{,},Class,RS,:,_,{,$___E,(,c,,,Rc_8,:,f85,;,k,:,String,;,___,:,Array,[,Array,[,Boolean,,,0x3C,],,,0XC6DA,],),{,Break,;,},},Class,_o_5,:,___,{,},Class,o19,{,},Class,_,:,_,{,},Class,_Es,{,Var,$2,,,$sA_pi,:,s,;,Val,$i2,,,$J,:,Array,[,Array,[,Int,,,063,],,,0x3C,],;,Val,$6,:,Int,;,},<EOF>''',101))

    def test_1553(self):
        self.assertTrue(TestLexer.test('''Class v{}Class _75__M:d{}Class _T{}Class Et4U:XtP{}Class _4r{}Class j9y:_{Var _,x7X77T:Array [Boolean ,96];Destructor (){}Destructor (){New T()._y();} }''','''Class,v,{,},Class,_75__M,:,d,{,},Class,_T,{,},Class,Et4U,:,XtP,{,},Class,_4r,{,},Class,j9y,:,_,{,Var,_,,,x7X77T,:,Array,[,Boolean,,,96,],;,Destructor,(,),{,},Destructor,(,),{,New,T,(,),.,_y,(,),;,},},<EOF>''',101))

    def test_1554(self):
        self.assertTrue(TestLexer.test('''Class _559:Q{Destructor (){Continue ;} }Class _:Q_4_{}Class k5:X__86_{_H8(_,H,hO,k_:e_v_){} }Class _:l0Z4I_{}Class Z{}''','''Class,_559,:,Q,{,Destructor,(,),{,Continue,;,},},Class,_,:,Q_4_,{,},Class,k5,:,X__86_,{,_H8,(,_,,,H,,,hO,,,k_,:,e_v_,),{,},},Class,_,:,l0Z4I_,{,},Class,Z,{,},<EOF>''',101))

    def test_1555(self):
        self.assertTrue(TestLexer.test('''Class Th_{}Class _6e:_{Constructor (l7:_;__,_,v:n7_;Dq,_:Array [Array [Float ,0x9],0b101000];_5,_:Int ;_:I;_,u4:Array [Boolean ,0B1];_7P,_i:B){} }Class __:P{}''','''Class,Th_,{,},Class,_6e,:,_,{,Constructor,(,l7,:,_,;,__,,,_,,,v,:,n7_,;,Dq,,,_,:,Array,[,Array,[,Float,,,0x9,],,,0b101000,],;,_5,,,_,:,Int,;,_,:,I,;,_,,,u4,:,Array,[,Boolean,,,0B1,],;,_7P,,,_i,:,B,),{,},},Class,__,:,P,{,},<EOF>''',101))

    def test_1556(self):
        self.assertTrue(TestLexer.test('''Class _{}Class _:_Z{}Class v_:YL65j{Var $__2,_:Array [Boolean ,85];Constructor (__:Array [Array [Array [String ,04],02],0x7];t5Z,_,_E_:mFY){} }''','''Class,_,{,},Class,_,:,_Z,{,},Class,v_,:,YL65j,{,Var,$__2,,,_,:,Array,[,Boolean,,,85,],;,Constructor,(,__,:,Array,[,Array,[,Array,[,String,,,04,],,,02,],,,0x7,],;,t5Z,,,_,,,_E_,:,mFY,),{,},},<EOF>''',101))

    def test_1557(self):
        self.assertTrue(TestLexer.test('''Class __Z{}Class pK{Val $C,$_6a,$9_A1M,_9_b_,__,____,nII,$__,H:Array [Array [Array [Array [String ,0b10001],0x26],0132],0b10001];Val $_o:Array [Array [Array [Boolean ,07],0B1010001],0132];Destructor (){} }Class _:YI_bN6{Destructor (){} }''','''Class,__Z,{,},Class,pK,{,Val,$C,,,$_6a,,,$9_A1M,,,_9_b_,,,__,,,____,,,nII,,,$__,,,H,:,Array,[,Array,[,Array,[,Array,[,String,,,0b10001,],,,0x26,],,,0132,],,,0b10001,],;,Val,$_o,:,Array,[,Array,[,Array,[,Boolean,,,07,],,,0B1010001,],,,0132,],;,Destructor,(,),{,},},Class,_,:,YI_bN6,{,Destructor,(,),{,},},<EOF>''',101))

    def test_1558(self):
        self.assertTrue(TestLexer.test('''Class _{Var kt:Array [Array [Array [Array [Array [Array [Float ,0b1001100],0XD_B_6],0B1110],0b1],066],0X3D];_(){_::$59_();} }Class v:_8J{}''','''Class,_,{,Var,kt,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0b1001100,],,,0XDB6,],,,0B1110,],,,0b1,],,,066,],,,0X3D,],;,_,(,),{,_,::,$59_,(,),;,},},Class,v,:,_8J,{,},<EOF>''',101))

    def test_1559(self):
        self.assertTrue(TestLexer.test('''Class _w6{Constructor (_:Boolean ;Y__,y:Float ;M:Float ;On__00c,I6:String ;_:String ;_:Array [Array [Array [String ,5_4],031],0B110101];_:Array [Array [Float ,031],0X9];_,y3,_:Int ;_6E:Int ;N,d6:Array [Array [Int ,7_5_8],4];z:String ;_u_d,_4:BC;J___d:Array [Int ,52]){} }''','''Class,_w6,{,Constructor,(,_,:,Boolean,;,Y__,,,y,:,Float,;,M,:,Float,;,On__00c,,,I6,:,String,;,_,:,String,;,_,:,Array,[,Array,[,Array,[,String,,,54,],,,031,],,,0B110101,],;,_,:,Array,[,Array,[,Float,,,031,],,,0X9,],;,_,,,y3,,,_,:,Int,;,_6E,:,Int,;,N,,,d6,:,Array,[,Array,[,Int,,,758,],,,4,],;,z,:,String,;,_u_d,,,_4,:,BC,;,J___d,:,Array,[,Int,,,52,],),{,},},<EOF>''',101))

    def test_1560(self):
        self.assertTrue(TestLexer.test('''Class q__{$v(A:Array [Boolean ,0x1A0];R,_7:Int ;Y,_:Boolean ;V5_,_:N){} }Class _:__{}Class T{}Class _6_{}Class y:_{}''','''Class,q__,{,$v,(,A,:,Array,[,Boolean,,,0x1A0,],;,R,,,_7,:,Int,;,Y,,,_,:,Boolean,;,V5_,,,_,:,N,),{,},},Class,_,:,__,{,},Class,T,{,},Class,_6_,{,},Class,y,:,_,{,},<EOF>''',101))

    def test_1561(self):
        self.assertTrue(TestLexer.test('''Class ___{Constructor (__,n,_:Boolean ;H:Boolean ;_P,_:Int ;_8:Int ){}$_(){}Constructor (){ {}J::$_();} }Class _N{Constructor (__,a4v,A:Float ){}Val __:Int ;}Class S{}Class _:T_2hF__{}Class F:g{}Class t:V8{}''','''Class,___,{,Constructor,(,__,,,n,,,_,:,Boolean,;,H,:,Boolean,;,_P,,,_,:,Int,;,_8,:,Int,),{,},$_,(,),{,},Constructor,(,),{,{,},J,::,$_,(,),;,},},Class,_N,{,Constructor,(,__,,,a4v,,,A,:,Float,),{,},Val,__,:,Int,;,},Class,S,{,},Class,_,:,T_2hF__,{,},Class,F,:,g,{,},Class,t,:,V8,{,},<EOF>''',101))

    def test_1562(self):
        self.assertTrue(TestLexer.test('''Class gk__or{}Class _{}Class S{J__(bQ:Array [String ,0x3];_h1:__a;q84n:Boolean ){}$__k(){}Constructor (p74___:Array [Float ,7]){} }Class _Ej1:W{Var _7,jGx5,_7:_o_;Var _:Boolean ;Var $_,_:Array [Boolean ,066];}''','''Class,gk__or,{,},Class,_,{,},Class,S,{,J__,(,bQ,:,Array,[,String,,,0x3,],;,_h1,:,__a,;,q84n,:,Boolean,),{,},$__k,(,),{,},Constructor,(,p74___,:,Array,[,Float,,,7,],),{,},},Class,_Ej1,:,W,{,Var,_7,,,jGx5,,,_7,:,_o_,;,Var,_,:,Boolean,;,Var,$_,,,_,:,Array,[,Boolean,,,066,],;,},<EOF>''',101))

    def test_1563(self):
        self.assertTrue(TestLexer.test('''Class _e:_{$6(N:Array [Array [Float ,2],0b1];a4:Array [Float ,0B1];_8__Ie,_,___m7:Array [Array [String ,0b1],0x31];_:Array [Array [Int ,0B1100010],8];_:String ;_x,V,_,_,_,a8__9n,fd,_:String ;B,_23,__:M;__:Array [Array [Array [Array [Array [Int ,06],0xD],06],0B111_0],030]){} }''','''Class,_e,:,_,{,$6,(,N,:,Array,[,Array,[,Float,,,2,],,,0b1,],;,a4,:,Array,[,Float,,,0B1,],;,_8__Ie,,,_,,,___m7,:,Array,[,Array,[,String,,,0b1,],,,0x31,],;,_,:,Array,[,Array,[,Int,,,0B1100010,],,,8,],;,_,:,String,;,_x,,,V,,,_,,,_,,,_,,,a8__9n,,,fd,,,_,:,String,;,B,,,_23,,,__,:,M,;,__,:,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,06,],,,0xD,],,,06,],,,0B1110,],,,030,],),{,},},<EOF>''',101))

    def test_1564(self):
        self.assertTrue(TestLexer.test('''Class _{Val $_:Float ;Var $_,__:Array [Array [Array [Array [Array [Int ,41],0B11011],0X42],4_918_86],35_386_2];Destructor (){} }''','''Class,_,{,Val,$_,:,Float,;,Var,$_,,,__,:,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,41,],,,0B11011,],,,0X42,],,,491886,],,,353862,],;,Destructor,(,),{,},},<EOF>''',101))

    def test_1565(self):
        self.assertTrue(TestLexer.test('''Class lr{}Class _{Var k:A;}Class _{}Class _{Constructor (){}Val v,$6_:E_;Constructor (){}$u_3(){Var _P:Float ;} }Class __:_{Var _:p6_;}''','''Class,lr,{,},Class,_,{,Var,k,:,A,;,},Class,_,{,},Class,_,{,Constructor,(,),{,},Val,v,,,$6_,:,E_,;,Constructor,(,),{,},$u_3,(,),{,Var,_P,:,Float,;,},},Class,__,:,_,{,Var,_,:,p6_,;,},<EOF>''',101))

    def test_1566(self):
        self.assertTrue(TestLexer.test('''Class _5:_J_{Var $2:_f9_00;Constructor (){} }Class o:l{$5(S06k:_8;__:Boolean ){Continue ;} }Class C:_{Var $2,$__,__:_;}''','''Class,_5,:,_J_,{,Var,$2,:,_f9_00,;,Constructor,(,),{,},},Class,o,:,l,{,$5,(,S06k,:,_8,;,__,:,Boolean,),{,Continue,;,},},Class,C,:,_,{,Var,$2,,,$__,,,__,:,_,;,},<EOF>''',101))

    def test_1567(self):
        self.assertTrue(TestLexer.test('''Class _:_{}Class z:Tk_{_0_(I_:_8n_;_,_,_,W,_93,K:rT;S,_,_5_1A:Boolean ;_,_1:Array [String ,0X5B]){} }Class d00__{}''','''Class,_,:,_,{,},Class,z,:,Tk_,{,_0_,(,I_,:,_8n_,;,_,,,_,,,_,,,W,,,_93,,,K,:,rT,;,S,,,_,,,_5_1A,:,Boolean,;,_,,,_1,:,Array,[,String,,,0X5B,],),{,},},Class,d00__,{,},<EOF>''',101))

    def test_1568(self):
        self.assertTrue(TestLexer.test('''Class __:_{Val $iyH,E_:Array [Boolean ,18];}Class p0A:c{}Class J8z:__{}Class _{Constructor (_,_:Array [Int ,7];_,_:Float ;i_T:Array [Array [Array [Array [Array [Boolean ,0B1],9],02],0B1],18]){} }Class B:W{}''','''Class,__,:,_,{,Val,$iyH,,,E_,:,Array,[,Boolean,,,18,],;,},Class,p0A,:,c,{,},Class,J8z,:,__,{,},Class,_,{,Constructor,(,_,,,_,:,Array,[,Int,,,7,],;,_,,,_,:,Float,;,i_T,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0B1,],,,9,],,,02,],,,0B1,],,,18,],),{,},},Class,B,:,W,{,},<EOF>''',101))

    def test_1569(self):
        self.assertTrue(TestLexer.test('''Class _y{Constructor (_1_:Float ;d_5_,h__7,_:Boolean ;hS_,_,_t,n40K,v:z_xt;__QY7:m_9ebC){}Constructor (){} }''','''Class,_y,{,Constructor,(,_1_,:,Float,;,d_5_,,,h__7,,,_,:,Boolean,;,hS_,,,_,,,_t,,,n40K,,,v,:,z_xt,;,__QY7,:,m_9ebC,),{,},Constructor,(,),{,},},<EOF>''',101))

    def test_1570(self):
        self.assertTrue(TestLexer.test('''Class _:hW{Val u,_,___,_,$8:Array [Array [Array [Array [Array [Array [Array [Array [Boolean ,2],0b1_01],0b1000101],0x76],075],0x1B],0b1000101],0XB];Constructor (){}Val $4D_m__C_,$6:Array [Array [Array [String ,0b10],0b10],0116];}''','''Class,_,:,hW,{,Val,u,,,_,,,___,,,_,,,$8,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,2,],,,0b101,],,,0b1000101,],,,0x76,],,,075,],,,0x1B,],,,0b1000101,],,,0XB,],;,Constructor,(,),{,},Val,$4D_m__C_,,,$6,:,Array,[,Array,[,Array,[,String,,,0b10,],,,0b10,],,,0116,],;,},<EOF>''',101))

    def test_1571(self):
        self.assertTrue(TestLexer.test('''Class _H2:vQ{Constructor (__,_:Boolean ;_83,_,_1_:Boolean ){}$9(_t:Array [Array [String ,0x5B],39]){} }Class O{}Class l{}''','''Class,_H2,:,vQ,{,Constructor,(,__,,,_,:,Boolean,;,_83,,,_,,,_1_,:,Boolean,),{,},$9,(,_t,:,Array,[,Array,[,String,,,0x5B,],,,39,],),{,},},Class,O,{,},Class,l,{,},<EOF>''',101))

    def test_1572(self):
        self.assertTrue(TestLexer.test('''Class _:_{}Class Z2_:K{}Class U:m{Var $_5_:_4;V6(){} }Class _:_{}Class I_{Constructor (b:Float ;Y:n){}Var O,j_3:Float ;Var $E,__cu6,b:_;}Class _{Constructor (){} }Class ijD:_S_{}Class c5_{}''','''Class,_,:,_,{,},Class,Z2_,:,K,{,},Class,U,:,m,{,Var,$_5_,:,_4,;,V6,(,),{,},},Class,_,:,_,{,},Class,I_,{,Constructor,(,b,:,Float,;,Y,:,n,),{,},Var,O,,,j_3,:,Float,;,Var,$E,,,__cu6,,,b,:,_,;,},Class,_,{,Constructor,(,),{,},},Class,ijD,:,_S_,{,},Class,c5_,{,},<EOF>''',101))

    def test_1573(self):
        self.assertTrue(TestLexer.test('''Class L{}Class T:_z{Constructor (E,UD:Boolean ;T:Float ;w,_:Array [Array [Int ,0b111100],0B100111]){}Val _cX,_:Int ;}Class Y9{}''','''Class,L,{,},Class,T,:,_z,{,Constructor,(,E,,,UD,:,Boolean,;,T,:,Float,;,w,,,_,:,Array,[,Array,[,Int,,,0b111100,],,,0B100111,],),{,},Val,_cX,,,_,:,Int,;,},Class,Y9,{,},<EOF>''',101))

    def test_1574(self):
        self.assertTrue(TestLexer.test('''Class _o:yE9_{Constructor (D3__:Array [Array [Array [Array [Array [Array [Array [Boolean ,0125],0125],0xD],81],0125],9],25]){}Var _,F1:String ;}''','''Class,_o,:,yE9_,{,Constructor,(,D3__,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0125,],,,0125,],,,0xD,],,,81,],,,0125,],,,9,],,,25,],),{,},Var,_,,,F1,:,String,;,},<EOF>''',101))

    def test_1575(self):
        self.assertTrue(TestLexer.test('''Class _{$1i(_,_,L7_32:_U_){Qe::$__()._8()._()._.__();}Var _0W:Array [String ,0X53];}Class zm_P1:k8C2{Var $0_p_L:Array [Array [Int ,07_61_7_6_3_0],8_3_8];Val _99g_:c;Val $_,_:__6f88;}''','''Class,_,{,$1i,(,_,,,_,,,L7_32,:,_U_,),{,Qe,::,$__,(,),.,_8,(,),.,_,(,),.,_,.,__,(,),;,},Var,_0W,:,Array,[,String,,,0X53,],;,},Class,zm_P1,:,k8C2,{,Var,$0_p_L,:,Array,[,Array,[,Int,,,07617630,],,,838,],;,Val,_99g_,:,c,;,Val,$_,,,_,:,__6f88,;,},<EOF>''',101))

    def test_1576(self):
        self.assertTrue(TestLexer.test('''Class K6{}Class _6{}Class _:R{}Class _:__x{N__(Y,L,D,_2_,_4,_5_:Array [Array [Int ,0b101_0],0B100];_,_FTG,_c9,_:Array [Int ,037]){}Constructor (_o:HS;oOA:v){} }''','''Class,K6,{,},Class,_6,{,},Class,_,:,R,{,},Class,_,:,__x,{,N__,(,Y,,,L,,,D,,,_2_,,,_4,,,_5_,:,Array,[,Array,[,Int,,,0b1010,],,,0B100,],;,_,,,_FTG,,,_c9,,,_,:,Array,[,Int,,,037,],),{,},Constructor,(,_o,:,HS,;,oOA,:,v,),{,},},<EOF>''',101))

    def test_1577(self):
        self.assertTrue(TestLexer.test('''Class _6:_{}Class A:w{$_A4(__:Float ;___,NtP2_:String ;T_:Array [Array [Array [Array [Array [Boolean ,0x9],0x1A],057],0B101],0b1]){} }Class j{Var z_,$__,v0,__:Boolean ;}Class _{Constructor (j,X:Array [Array [Array [Boolean ,057],057],057]){}$G(C:String ){Break ;} }Class __w8_{}''','''Class,_6,:,_,{,},Class,A,:,w,{,$_A4,(,__,:,Float,;,___,,,NtP2_,:,String,;,T_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0x9,],,,0x1A,],,,057,],,,0B101,],,,0b1,],),{,},},Class,j,{,Var,z_,,,$__,,,v0,,,__,:,Boolean,;,},Class,_,{,Constructor,(,j,,,X,:,Array,[,Array,[,Array,[,Boolean,,,057,],,,057,],,,057,],),{,},$G,(,C,:,String,),{,Break,;,},},Class,__w8_,{,},<EOF>''',101))

    def test_1578(self):
        self.assertTrue(TestLexer.test('''Class _:y_{Var S:Boolean ;}Class _l:___{}Class F20Y:_{Constructor (j8_,_:Array [Array [Int ,0x38],9_80]){Break ;} }''','''Class,_,:,y_,{,Var,S,:,Boolean,;,},Class,_l,:,___,{,},Class,F20Y,:,_,{,Constructor,(,j8_,,,_,:,Array,[,Array,[,Int,,,0x38,],,,980,],),{,Break,;,},},<EOF>''',101))

    def test_1579(self):
        self.assertTrue(TestLexer.test('''Class A{Val _:Array [Array [Array [Float ,01],40],05_7];$_0h(K:Boolean ;v,L,O,_:String ;L_:Boolean ;__:Int ;i,__:Array [String ,0x18]){}Constructor (Z,_,_:Float ;__,_:_){} }Class _7:_38_{}''','''Class,A,{,Val,_,:,Array,[,Array,[,Array,[,Float,,,01,],,,40,],,,057,],;,$_0h,(,K,:,Boolean,;,v,,,L,,,O,,,_,:,String,;,L_,:,Boolean,;,__,:,Int,;,i,,,__,:,Array,[,String,,,0x18,],),{,},Constructor,(,Z,,,_,,,_,:,Float,;,__,,,_,:,_,),{,},},Class,_7,:,_38_,{,},<EOF>''',101))

    def test_1580(self):
        self.assertTrue(TestLexer.test('''Class _{$_(__,___t_:Array [Array [Float ,0b101100],0B1];_,_:Int ){Break ;}Var $S_d,_,$_:_;Val PJ__,_:J;Val R_,$__G,$_:Array [Boolean ,0b101100];}''','''Class,_,{,$_,(,__,,,___t_,:,Array,[,Array,[,Float,,,0b101100,],,,0B1,],;,_,,,_,:,Int,),{,Break,;,},Var,$S_d,,,_,,,$_,:,_,;,Val,PJ__,,,_,:,J,;,Val,R_,,,$__G,,,$_,:,Array,[,Boolean,,,0b101100,],;,},<EOF>''',101))

    def test_1581(self):
        self.assertTrue(TestLexer.test('''Class _4:s5{Constructor (e,C,_d,UZ_Wc:Array [Int ,7];y_:r_){}Var ___,_,__,z,$P_,$_:String ;Val $i:Array [Float ,07_51];}''','''Class,_4,:,s5,{,Constructor,(,e,,,C,,,_d,,,UZ_Wc,:,Array,[,Int,,,7,],;,y_,:,r_,),{,},Var,___,,,_,,,__,,,z,,,$P_,,,$_,:,String,;,Val,$i,:,Array,[,Float,,,0751,],;,},<EOF>''',101))

    def test_1582(self):
        self.assertTrue(TestLexer.test('''Class _1:Z{Val __,$__e:Float ;}Class _31{}Class ___1_{}Class o4{Constructor (){ {} }Constructor (_0_3,K:vF3l;k_:_0n_g){} }Class _{Var A9,H:Array [Float ,0b1];$_l_(L___A,R,jJ1__R,x:Array [Array [Array [Array [Array [String ,0X3],3],02],0x17],02];_:Float ){}Val $_,MZ7:vpS6;}''','''Class,_1,:,Z,{,Val,__,,,$__e,:,Float,;,},Class,_31,{,},Class,___1_,{,},Class,o4,{,Constructor,(,),{,{,},},Constructor,(,_0_3,,,K,:,vF3l,;,k_,:,_0n_g,),{,},},Class,_,{,Var,A9,,,H,:,Array,[,Float,,,0b1,],;,$_l_,(,L___A,,,R,,,jJ1__R,,,x,:,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0X3,],,,3,],,,02,],,,0x17,],,,02,],;,_,:,Float,),{,},Val,$_,,,MZ7,:,vpS6,;,},<EOF>''',101))

    def test_1583(self):
        self.assertTrue(TestLexer.test('''Class V:___o{Constructor (D__,_,NY_wm,e:Int ;P8,_1,_P,_2z,_:_){}Val _5:Float ;}Class D:l_f{$72_Od(G__p8,A,h:Array [Array [Array [Float ,9],062],062]){} }''','''Class,V,:,___o,{,Constructor,(,D__,,,_,,,NY_wm,,,e,:,Int,;,P8,,,_1,,,_P,,,_2z,,,_,:,_,),{,},Val,_5,:,Float,;,},Class,D,:,l_f,{,$72_Od,(,G__p8,,,A,,,h,:,Array,[,Array,[,Array,[,Float,,,9,],,,062,],,,062,],),{,},},<EOF>''',101))

    def test_1584(self):
        self.assertTrue(TestLexer.test('''Class _:_{}Class _{}Class _{}Class h_{}Class _{Constructor (_h_o_:Float ){Val a,_,_,t:String ;Break ;}Destructor (){} }''','''Class,_,:,_,{,},Class,_,{,},Class,_,{,},Class,h_,{,},Class,_,{,Constructor,(,_h_o_,:,Float,),{,Val,a,,,_,,,_,,,t,:,String,;,Break,;,},Destructor,(,),{,},},<EOF>''',101))

    def test_1585(self):
        self.assertTrue(TestLexer.test('''Class _:_6_Ln_{$E(){} }Class _{Val $_,$_c:_A;}Class __:___{}Class S15___:___{Val _6M,$E:Array [String ,0102];}Class E:P{}''','''Class,_,:,_6_Ln_,{,$E,(,),{,},},Class,_,{,Val,$_,,,$_c,:,_A,;,},Class,__,:,___,{,},Class,S15___,:,___,{,Val,_6M,,,$E,:,Array,[,String,,,0102,],;,},Class,E,:,P,{,},<EOF>''',101))

    def test_1586(self):
        self.assertTrue(TestLexer.test('''Class _:n4{Val _,$56,a:Array [Array [Array [Array [Array [Array [Array [Boolean ,0X8],4],03],0B101001],0X6],05],0B100];}''','''Class,_,:,n4,{,Val,_,,,$56,,,a,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0X8,],,,4,],,,03,],,,0B101001,],,,0X6,],,,05,],,,0B100,],;,},<EOF>''',101))

    def test_1587(self):
        self.assertTrue(TestLexer.test('''Class v{h8(_4:String ;_8_:Int ){Break ;} }Class s0:kH{}Class _:h{Val _,$69,$w2_,b:Boolean ;}Class _L:__kO{$32(){_6::$D3e2L6._x();_::$5._();} }''','''Class,v,{,h8,(,_4,:,String,;,_8_,:,Int,),{,Break,;,},},Class,s0,:,kH,{,},Class,_,:,h,{,Val,_,,,$69,,,$w2_,,,b,:,Boolean,;,},Class,_L,:,__kO,{,$32,(,),{,_6,::,$D3e2L6,.,_x,(,),;,_,::,$5,.,_,(,),;,},},<EOF>''',101))

    def test_1588(self):
        self.assertTrue(TestLexer.test('''Class _S_5:__zV{Val _:_z;}Class _:g{Constructor (W1:Array [Array [Array [Array [Array [Int ,076],076],0B1110],0x4_A8],0XAF]){} }''','''Class,_S_5,:,__zV,{,Val,_,:,_z,;,},Class,_,:,g,{,Constructor,(,W1,:,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,076,],,,076,],,,0B1110,],,,0x4A8,],,,0XAF,],),{,},},<EOF>''',101))

    def test_1589(self):
        self.assertTrue(TestLexer.test('''Class ____:j8h{}Class _9:_{__(W5f_S0,X,I_,i:Array [Float ,0b1011101];V,yl:Array [Array [Array [Array [Array [Float ,0b1],99],0XA2],0B10100],0b1_1];IQ:Array [Int ,0B10100]){}Constructor (aS8,_:Array [Array [String ,0x139],99]){} }''','''Class,____,:,j8h,{,},Class,_9,:,_,{,__,(,W5f_S0,,,X,,,I_,,,i,:,Array,[,Float,,,0b1011101,],;,V,,,yl,:,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,0b1,],,,99,],,,0XA2,],,,0B10100,],,,0b11,],;,IQ,:,Array,[,Int,,,0B10100,],),{,},Constructor,(,aS8,,,_,:,Array,[,Array,[,String,,,0x139,],,,99,],),{,},},<EOF>''',101))

    def test_1590(self):
        self.assertTrue(TestLexer.test('''Class Q{}Class __:_0{}Class Fu9S_5_{}Class _:_2{Constructor (){Break ;}Var _8,$f:E__7_t2;Wm6(__:O){Continue ;} }''','''Class,Q,{,},Class,__,:,_0,{,},Class,Fu9S_5_,{,},Class,_,:,_2,{,Constructor,(,),{,Break,;,},Var,_8,,,$f,:,E__7_t2,;,Wm6,(,__,:,O,),{,Continue,;,},},<EOF>''',101))

    def test_1591(self):
        self.assertTrue(TestLexer.test('''Class XJ:h_{}Class _:D{Var k:Array [Array [Int ,06],41];}Class _:_c2{_(){}Var S_00,$_3_:Array [Array [Boolean ,41],014];}''','''Class,XJ,:,h_,{,},Class,_,:,D,{,Var,k,:,Array,[,Array,[,Int,,,06,],,,41,],;,},Class,_,:,_c2,{,_,(,),{,},Var,S_00,,,$_3_,:,Array,[,Array,[,Boolean,,,41,],,,014,],;,},<EOF>''',101))

    def test_1592(self):
        self.assertTrue(TestLexer.test('''Class _6{}Class KT:_{Destructor (){}$84(__:String ;_76i7:Float ){} }Class a_{Val $_4t,hP,$_7_,_0823,d8:Array [Array [Array [Array [Int ,0b111],0X4C],0b1_1],64];Destructor (){}Constructor (_R:Boolean ;u,t87Fs,B_:Int ;Z4:Array [Boolean ,0b10];_353_8_:Array [Array [Boolean ,0b111],021]){} }Class _Z:u{Constructor (){} }''','''Class,_6,{,},Class,KT,:,_,{,Destructor,(,),{,},$84,(,__,:,String,;,_76i7,:,Float,),{,},},Class,a_,{,Val,$_4t,,,hP,,,$_7_,,,_0823,,,d8,:,Array,[,Array,[,Array,[,Array,[,Int,,,0b111,],,,0X4C,],,,0b11,],,,64,],;,Destructor,(,),{,},Constructor,(,_R,:,Boolean,;,u,,,t87Fs,,,B_,:,Int,;,Z4,:,Array,[,Boolean,,,0b10,],;,_353_8_,:,Array,[,Array,[,Boolean,,,0b111,],,,021,],),{,},},Class,_Z,:,u,{,Constructor,(,),{,},},<EOF>''',101))

    def test_1593(self):
        self.assertTrue(TestLexer.test('''Class b9d:__{Destructor (){}$_G(_:Array [Boolean ,0X48];Ai,_n:Array [Array [Array [Array [Array [Array [Float ,81],0x698],39],0x37],81],04];_:String ;__x2l:Array [Int ,0b1_01];_:Array [Array [String ,0b1],5];U:Int ;o_7p,i_,__:Int ;k,_:Array [Float ,0B111000]){ {} }}Class V6I:_{}''','''Class,b9d,:,__,{,Destructor,(,),{,},$_G,(,_,:,Array,[,Boolean,,,0X48,],;,Ai,,,_n,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,81,],,,0x698,],,,39,],,,0x37,],,,81,],,,04,],;,_,:,String,;,__x2l,:,Array,[,Int,,,0b101,],;,_,:,Array,[,Array,[,String,,,0b1,],,,5,],;,U,:,Int,;,o_7p,,,i_,,,__,:,Int,;,k,,,_,:,Array,[,Float,,,0B111000,],),{,{,},},},Class,V6I,:,_,{,},<EOF>''',101))

    def test_1594(self):
        self.assertTrue(TestLexer.test('''Class __{Constructor (){Val _8:Array [Array [Float ,889_2],03];}Constructor (s:_;V,w:Array [Float ,944_3];A_,_:Array [Boolean ,0b101000];n_,V,_k:Array [Int ,0X7]){} }''','''Class,__,{,Constructor,(,),{,Val,_8,:,Array,[,Array,[,Float,,,8892,],,,03,],;,},Constructor,(,s,:,_,;,V,,,w,:,Array,[,Float,,,9443,],;,A_,,,_,:,Array,[,Boolean,,,0b101000,],;,n_,,,V,,,_k,:,Array,[,Int,,,0X7,],),{,},},<EOF>''',101))

    def test_1595(self):
        self.assertTrue(TestLexer.test('''Class _3{}Class _Aw:_z{Constructor (YW:String ;_,gt:Array [Boolean ,0X47]){}Var _W:Array [Array [Array [String ,05_4_42],0X47],0b1];Constructor (){Continue ;} }''','''Class,_3,{,},Class,_Aw,:,_z,{,Constructor,(,YW,:,String,;,_,,,gt,:,Array,[,Boolean,,,0X47,],),{,},Var,_W,:,Array,[,Array,[,Array,[,String,,,05442,],,,0X47,],,,0b1,],;,Constructor,(,),{,Continue,;,},},<EOF>''',101))

    def test_1596(self):
        self.assertTrue(TestLexer.test('''Class _n_{Constructor (C,_o2:Array [Array [Array [Array [Array [Array [Array [Array [Array [Array [Boolean ,066],0b1],06_5],0X21],0xC_5],0B1],0B1],0b1100010],0b1100010],066]){ {}Val _,M4__d,__1_:Array [Array [Array [Array [Array [Float ,05],0x21],1_7],0x2],97];Return ;}Destructor (){Break ;} }Class _:U{__I(_hT4:M_Z;G:Boolean ;Wj,i_A:__){}Var _W__e:Int ;Destructor (){} }''','''Class,_n_,{,Constructor,(,C,,,_o2,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,066,],,,0b1,],,,065,],,,0X21,],,,0xC5,],,,0B1,],,,0B1,],,,0b1100010,],,,0b1100010,],,,066,],),{,{,},Val,_,,,M4__d,,,__1_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,05,],,,0x21,],,,17,],,,0x2,],,,97,],;,Return,;,},Destructor,(,),{,Break,;,},},Class,_,:,U,{,__I,(,_hT4,:,M_Z,;,G,:,Boolean,;,Wj,,,i_A,:,__,),{,},Var,_W__e,:,Int,;,Destructor,(,),{,},},<EOF>''',101))

    def test_1597(self):
        self.assertTrue(TestLexer.test('''Class b:_{}Class _v13_G{}Class _{Constructor (_5_:Float ;s__:Array [Int ,7]){}$__(){Break ;{} }}Class sh{Destructor (){} }''','''Class,b,:,_,{,},Class,_v13_G,{,},Class,_,{,Constructor,(,_5_,:,Float,;,s__,:,Array,[,Int,,,7,],),{,},$__,(,),{,Break,;,{,},},},Class,sh,{,Destructor,(,),{,},},<EOF>''',101))

    def test_1598(self):
        self.assertTrue(TestLexer.test('''Class _:_a{Var $_VU:Array [Array [Boolean ,1],0X30];Val _,n:String ;Var q,_K:_;Constructor (p,_7_,_,o:Sx0;__,_K,S_:Int ){} }''','''Class,_,:,_a,{,Var,$_VU,:,Array,[,Array,[,Boolean,,,1,],,,0X30,],;,Val,_,,,n,:,String,;,Var,q,,,_K,:,_,;,Constructor,(,p,,,_7_,,,_,,,o,:,Sx0,;,__,,,_K,,,S_,:,Int,),{,},},<EOF>''',101))

    def test_1599(self):
        self.assertTrue(TestLexer.test('''Class __5f:A{_(I:____s___;_K:Boolean ;R:Array [Int ,0B1_11];_:S;_i:Array [Array [Array [Array [Array [Array [Array [String ,0125],5_0_9_08_4],0xE],4],1],02],0B10];y,x:Array [Array [Int ,6_85],4];g:Float ){Break ;} }''','''Class,__5f,:,A,{,_,(,I,:,____s___,;,_K,:,Boolean,;,R,:,Array,[,Int,,,0B111,],;,_,:,S,;,_i,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0125,],,,509084,],,,0xE,],,,4,],,,1,],,,02,],,,0B10,],;,y,,,x,:,Array,[,Array,[,Int,,,685,],,,4,],;,g,:,Float,),{,Break,;,},},<EOF>''',101))

    def test_1600(self):
        self.assertTrue(TestLexer.test('''Class _J5{Var _42he,n_P,$_r:Array [String ,0X1F];Constructor (){}$c(L,SR,_,___:String ){}Destructor (){}$o(G:Array [Array [Int ,0X3],0116];_8,_O,M2:Float ;N,_:H;R___:K;Qd:Array [Array [Array [Array [Float ,0XA],0116],0B11110],98]){} }Class m6J6:t{}Class U_D:q{}Class _:D{}''','''Class,_J5,{,Var,_42he,,,n_P,,,$_r,:,Array,[,String,,,0X1F,],;,Constructor,(,),{,},$c,(,L,,,SR,,,_,,,___,:,String,),{,},Destructor,(,),{,},$o,(,G,:,Array,[,Array,[,Int,,,0X3,],,,0116,],;,_8,,,_O,,,M2,:,Float,;,N,,,_,:,H,;,R___,:,K,;,Qd,:,Array,[,Array,[,Array,[,Array,[,Float,,,0XA,],,,0116,],,,0B11110,],,,98,],),{,},},Class,m6J6,:,t,{,},Class,U_D,:,q,{,},Class,_,:,D,{,},<EOF>''',101))

    def test_1601(self):
        self.assertTrue(TestLexer.test('''Class _:e{Val __C6,$_c:Array [Boolean ,8];Destructor (){}_E(o:Array [Boolean ,0b100010]){} }Class o5Q:_{_(){Continue ;} }''','''Class,_,:,e,{,Val,__C6,,,$_c,:,Array,[,Boolean,,,8,],;,Destructor,(,),{,},_E,(,o,:,Array,[,Boolean,,,0b100010,],),{,},},Class,o5Q,:,_,{,_,(,),{,Continue,;,},},<EOF>''',101))

    def test_1602(self):
        self.assertTrue(TestLexer.test('''Class __:J{Var q_91c,_g,G,_:Array [Array [Array [Float ,0b111001],2_7],1];Val $_t:Array [Array [Array [Array [String ,0125],37],0B1_01],0125];Constructor (L:w262;T:_){} }Class __7:_{}''','''Class,__,:,J,{,Var,q_91c,,,_g,,,G,,,_,:,Array,[,Array,[,Array,[,Float,,,0b111001,],,,27,],,,1,],;,Val,$_t,:,Array,[,Array,[,Array,[,Array,[,String,,,0125,],,,37,],,,0B101,],,,0125,],;,Constructor,(,L,:,w262,;,T,:,_,),{,},},Class,__7,:,_,{,},<EOF>''',101))

    def test_1603(self):
        self.assertTrue(TestLexer.test('''Class Crub6YRu{Destructor (){} }Class l{Constructor (b_j__,yr_m:Float ;P__:__6__;j9_2_:Array [Float ,0x3]){}Constructor (){} }Class _{}''','''Class,Crub6YRu,{,Destructor,(,),{,},},Class,l,{,Constructor,(,b_j__,,,yr_m,:,Float,;,P__,:,__6__,;,j9_2_,:,Array,[,Float,,,0x3,],),{,},Constructor,(,),{,},},Class,_,{,},<EOF>''',101))

    def test_1604(self):
        self.assertTrue(TestLexer.test('''Class _:_{}Class _e:_{h78(){Val _:i;} }Class _{}Class _{Var _o:Array [Array [Array [Array [Array [Array [Array [Array [Float ,070],070],06],0XA_F],06_3_6],98],0xB],0b1];}''','''Class,_,:,_,{,},Class,_e,:,_,{,h78,(,),{,Val,_,:,i,;,},},Class,_,{,},Class,_,{,Var,_o,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,070,],,,070,],,,06,],,,0XAF,],,,0636,],,,98,],,,0xB,],,,0b1,],;,},<EOF>''',101))

    def test_1605(self):
        self.assertTrue(TestLexer.test('''Class _:_{Constructor (_o_M,_:String ;_,_3F:Float ;_,_,Ba_s8:Array [Boolean ,0B1]){Return ;Var _,MY:String ;} }''','''Class,_,:,_,{,Constructor,(,_o_M,,,_,:,String,;,_,,,_3F,:,Float,;,_,,,_,,,Ba_s8,:,Array,[,Boolean,,,0B1,],),{,Return,;,Var,_,,,MY,:,String,;,},},<EOF>''',101))

    def test_1606(self):
        self.assertTrue(TestLexer.test('''Class g:_{}Class i:C8{}Class F:e047{Val f,$2__:Array [Boolean ,0x10];}Class t:_{Var $j,$_A,E72,Cn,j_:Array [Array [Array [Array [Array [Boolean ,0106],0x7E],217],96],0x10];}''','''Class,g,:,_,{,},Class,i,:,C8,{,},Class,F,:,e047,{,Val,f,,,$2__,:,Array,[,Boolean,,,0x10,],;,},Class,t,:,_,{,Var,$j,,,$_A,,,E72,,,Cn,,,j_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0106,],,,0x7E,],,,217,],,,96,],,,0x10,],;,},<EOF>''',101))

    def test_1607(self):
        self.assertTrue(TestLexer.test('''Class _8_:_{Var _,y7_:_;Val z4t:Array [Array [Boolean ,0B1001111],9];Constructor (){} }Class __8_{Var u:Array [Boolean ,9_4_5_73];Val G_:Boolean ;}Class _{}''','''Class,_8_,:,_,{,Var,_,,,y7_,:,_,;,Val,z4t,:,Array,[,Array,[,Boolean,,,0B1001111,],,,9,],;,Constructor,(,),{,},},Class,__8_,{,Var,u,:,Array,[,Boolean,,,94573,],;,Val,G_,:,Boolean,;,},Class,_,{,},<EOF>''',101))

    def test_1608(self):
        self.assertTrue(TestLexer.test('''Class J:_7_{Destructor (){} }Class _{}Class X:_{$_B_(_L,_:Array [Array [Array [Boolean ,032],0B1],0X59];Z7,B_,EV:Boolean ){}Val q_:Array [Int ,0B1011100]=New _W9().T();}''','''Class,J,:,_7_,{,Destructor,(,),{,},},Class,_,{,},Class,X,:,_,{,$_B_,(,_L,,,_,:,Array,[,Array,[,Array,[,Boolean,,,032,],,,0B1,],,,0X59,],;,Z7,,,B_,,,EV,:,Boolean,),{,},Val,q_,:,Array,[,Int,,,0B1011100,],=,New,_W9,(,),.,T,(,),;,},<EOF>''',101))

    def test_1609(self):
        self.assertTrue(TestLexer.test('''Class _{Val _:String ;Destructor (){}Constructor (Tx,B,_29N__,u,_0z_:Array [Array [Int ,0X1],0b10]){} }Class u:qB{}''','''Class,_,{,Val,_,:,String,;,Destructor,(,),{,},Constructor,(,Tx,,,B,,,_29N__,,,u,,,_0z_,:,Array,[,Array,[,Int,,,0X1,],,,0b10,],),{,},},Class,u,:,qB,{,},<EOF>''',101))

    def test_1610(self):
        self.assertTrue(TestLexer.test('''Class p:_{Constructor (_:Array [Array [Float ,7_0_7],03];_,g1:_){Null .r_();} }Class C{}Class _:I3m{}Class _7:__X{Val _:Array [String ,0113];}''','''Class,p,:,_,{,Constructor,(,_,:,Array,[,Array,[,Float,,,707,],,,03,],;,_,,,g1,:,_,),{,Null,.,r_,(,),;,},},Class,C,{,},Class,_,:,I3m,{,},Class,_7,:,__X,{,Val,_,:,Array,[,String,,,0113,],;,},<EOF>''',101))

    def test_1611(self):
        self.assertTrue(TestLexer.test('''Class __9_8__{}Class ra:m{Constructor (L:Array [String ,6];_:__;_,K__:Array [Int ,0b1];I,_,l:D){}Destructor (){} }Class _7w7t{}Class _E{I(){} }''','''Class,__9_8__,{,},Class,ra,:,m,{,Constructor,(,L,:,Array,[,String,,,6,],;,_,:,__,;,_,,,K__,:,Array,[,Int,,,0b1,],;,I,,,_,,,l,:,D,),{,},Destructor,(,),{,},},Class,_7w7t,{,},Class,_E,{,I,(,),{,},},<EOF>''',101))

    def test_1612(self):
        self.assertTrue(TestLexer.test('''Class _:r60{_(m:_;xr:Array [Array [Array [Array [Array [String ,066],0B1],073],0b101100],65]){} }Class _{Var AJ_fC_:_;}''','''Class,_,:,r60,{,_,(,m,:,_,;,xr,:,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,066,],,,0B1,],,,073,],,,0b101100,],,,65,],),{,},},Class,_,{,Var,AJ_fC_,:,_,;,},<EOF>''',101))

    def test_1613(self):
        self.assertTrue(TestLexer.test('''Class PP{$d(_K:VB;kE:Int ){Break ;}Val $U:Float ;}Class __:zi{Var BN,v_Uy:Array [Array [Array [Array [Array [String ,1],04],6],0XB],0B1];}''','''Class,PP,{,$d,(,_K,:,VB,;,kE,:,Int,),{,Break,;,},Val,$U,:,Float,;,},Class,__,:,zi,{,Var,BN,,,v_Uy,:,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,1,],,,04,],,,6,],,,0XB,],,,0B1,],;,},<EOF>''',101))

    def test_1614(self):
        self.assertTrue(TestLexer.test('''Class C:n_K89{Destructor (){} }Class kk{Constructor (Y:Boolean ){}Constructor (P80O,__,L,d3_:Array [Array [Boolean ,0X4],0b10011];iv:Array [Int ,739];_3,_:Array [Int ,0B11]){Continue ;}Var D,_,$_:Int ;}''','''Class,C,:,n_K89,{,Destructor,(,),{,},},Class,kk,{,Constructor,(,Y,:,Boolean,),{,},Constructor,(,P80O,,,__,,,L,,,d3_,:,Array,[,Array,[,Boolean,,,0X4,],,,0b10011,],;,iv,:,Array,[,Int,,,739,],;,_3,,,_,:,Array,[,Int,,,0B11,],),{,Continue,;,},Var,D,,,_,,,$_,:,Int,;,},<EOF>''',101))

    def test_1615(self):
        self.assertTrue(TestLexer.test('''Class _i:r{Val WJ,_F,_,$3j:Array [Int ,1_0];}Class _:N3_{}Class __:t6{}Class m{}Class _7{Constructor (){} }Class p:_5{}''','''Class,_i,:,r,{,Val,WJ,,,_F,,,_,,,$3j,:,Array,[,Int,,,10,],;,},Class,_,:,N3_,{,},Class,__,:,t6,{,},Class,m,{,},Class,_7,{,Constructor,(,),{,},},Class,p,:,_5,{,},<EOF>''',101))

    def test_1616(self):
        self.assertTrue(TestLexer.test('''Class j3E_g:_N_777{Constructor (G:Array [Array [Array [Float ,0111],0b100011],0430];q,o,t_:zDq9X;J__Sr_0,pidj_lK486O:Array [Array [Boolean ,0X10],2]){} }''','''Class,j3E_g,:,_N_777,{,Constructor,(,G,:,Array,[,Array,[,Array,[,Float,,,0111,],,,0b100011,],,,0430,],;,q,,,o,,,t_,:,zDq9X,;,J__Sr_0,,,pidj_lK486O,:,Array,[,Array,[,Boolean,,,0X10,],,,2,],),{,},},<EOF>''',101))

    def test_1617(self):
        self.assertTrue(TestLexer.test('''Class K_:_7{Var $mV,C_6,$8:Array [Array [Boolean ,91],0B10100];_(_g,_R__B:String ;A,_:Boolean ;T,_:Array [Int ,0435_34];_X:Array [String ,0b1];_,E,_,s:Float ;__:Int ;XdOv,__:Boolean ){} }''','''Class,K_,:,_7,{,Var,$mV,,,C_6,,,$8,:,Array,[,Array,[,Boolean,,,91,],,,0B10100,],;,_,(,_g,,,_R__B,:,String,;,A,,,_,:,Boolean,;,T,,,_,:,Array,[,Int,,,043534,],;,_X,:,Array,[,String,,,0b1,],;,_,,,E,,,_,,,s,:,Float,;,__,:,Int,;,XdOv,,,__,:,Boolean,),{,},},<EOF>''',101))

    def test_1618(self):
        self.assertTrue(TestLexer.test('''Class _3_{R4(_,Q_4s14,___b,jE:Array [Int ,0B1001110];z,___L3_v9,_,qh,X,A:Float ){Break ;}$M__(X4,sW:M;_g9,_:_;l,m28_3:_A){} }Class L_30:_32{Constructor (){}Destructor (){Continue ;} }''','''Class,_3_,{,R4,(,_,,,Q_4s14,,,___b,,,jE,:,Array,[,Int,,,0B1001110,],;,z,,,___L3_v9,,,_,,,qh,,,X,,,A,:,Float,),{,Break,;,},$M__,(,X4,,,sW,:,M,;,_g9,,,_,:,_,;,l,,,m28_3,:,_A,),{,},},Class,L_30,:,_32,{,Constructor,(,),{,},Destructor,(,),{,Continue,;,},},<EOF>''',101))

    def test_1619(self):
        self.assertTrue(TestLexer.test('''Class s{}Class B_9:B_3{$c9(n_:Array [Array [Array [Int ,0x50],03],0133];x:W;VIpM_3:Array [Boolean ,0B100111];_,l,Y_0:Array [Float ,0X45]){} }Class _on{}''','''Class,s,{,},Class,B_9,:,B_3,{,$c9,(,n_,:,Array,[,Array,[,Array,[,Int,,,0x50,],,,03,],,,0133,],;,x,:,W,;,VIpM_3,:,Array,[,Boolean,,,0B100111,],;,_,,,l,,,Y_0,:,Array,[,Float,,,0X45,],),{,},},Class,_on,{,},<EOF>''',101))

    def test_1620(self):
        self.assertTrue(TestLexer.test('''Class _{Destructor (){} }Class s_{G(){Break ;Val X:__;_::$20();{}{} }Var F:_;Constructor (d_:Array [Boolean ,033];y:Int ){Return ;} }''','''Class,_,{,Destructor,(,),{,},},Class,s_,{,G,(,),{,Break,;,Val,X,:,__,;,_,::,$20,(,),;,{,},{,},},Var,F,:,_,;,Constructor,(,d_,:,Array,[,Boolean,,,033,],;,y,:,Int,),{,Return,;,},},<EOF>''',101))

    def test_1621(self):
        self.assertTrue(TestLexer.test('''Class Hf:b{}Class v{Constructor (Y,o,D,Y4,_58D,G,_F_9_8,_,__05__,V__:u_;S1,___,Dk,_z_,K_3_5:l;n_:Boolean ;_x:__9_;D:v){t::$k2a();} }''','''Class,Hf,:,b,{,},Class,v,{,Constructor,(,Y,,,o,,,D,,,Y4,,,_58D,,,G,,,_F_9_8,,,_,,,__05__,,,V__,:,u_,;,S1,,,___,,,Dk,,,_z_,,,K_3_5,:,l,;,n_,:,Boolean,;,_x,:,__9_,;,D,:,v,),{,t,::,$k2a,(,),;,},},<EOF>''',101))

    def test_1622(self):
        self.assertTrue(TestLexer.test('''Class _:_4F{_4a(_,_8g,_,_:Boolean ;__P,Z_AN:Boolean ;jM,_5_:v____){Val R:Array [Array [Array [Boolean ,0B111000],5_0],0b1_1];} }''','''Class,_,:,_4F,{,_4a,(,_,,,_8g,,,_,,,_,:,Boolean,;,__P,,,Z_AN,:,Boolean,;,jM,,,_5_,:,v____,),{,Val,R,:,Array,[,Array,[,Array,[,Boolean,,,0B111000,],,,50,],,,0b11,],;,},},<EOF>''',101))

    def test_1623(self):
        self.assertTrue(TestLexer.test('''Class _{}Class d:T_{__mZ_1_(){Continue ;} }Class _7A{}Class __P{WL(_:Array [Array [String ,69],0x8E]){} }Class k35:_{}''','''Class,_,{,},Class,d,:,T_,{,__mZ_1_,(,),{,Continue,;,},},Class,_7A,{,},Class,__P,{,WL,(,_,:,Array,[,Array,[,String,,,69,],,,0x8E,],),{,},},Class,k35,:,_,{,},<EOF>''',101))

    def test_1624(self):
        self.assertTrue(TestLexer.test('''Class _:_{}Class gN35BVq_{Destructor (){} }Class _:X{Constructor (h,_9,_1:Int ){}Destructor (){}$_(){}Constructor (__21:Array [Array [Array [Float ,87],0X38],0x39];L:_8){} }Class M{Var _,__v3:Array [Array [Array [Array [Array [Array [Array [Array [Array [String ,0b100010],0b100010],46_4_2_2],014],0X38],16],7151_62352],014],014];}''','''Class,_,:,_,{,},Class,gN35BVq_,{,Destructor,(,),{,},},Class,_,:,X,{,Constructor,(,h,,,_9,,,_1,:,Int,),{,},Destructor,(,),{,},$_,(,),{,},Constructor,(,__21,:,Array,[,Array,[,Array,[,Float,,,87,],,,0X38,],,,0x39,],;,L,:,_8,),{,},},Class,M,{,Var,_,,,__v3,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0b100010,],,,0b100010,],,,46422,],,,014,],,,0X38,],,,16,],,,715162352,],,,014,],,,014,],;,},<EOF>''',101))

    def test_1625(self):
        self.assertTrue(TestLexer.test('''Class _{Val $O_,$uA,V_3:Array [Boolean ,4_0];}Class q_{Constructor (){Val _,_,_h:Array [Boolean ,0B1001010];Break ;} }Class g:_2{}''','''Class,_,{,Val,$O_,,,$uA,,,V_3,:,Array,[,Boolean,,,40,],;,},Class,q_,{,Constructor,(,),{,Val,_,,,_,,,_h,:,Array,[,Boolean,,,0B1001010,],;,Break,;,},},Class,g,:,_2,{,},<EOF>''',101))

    def test_1626(self):
        self.assertTrue(TestLexer.test('''Class _y{Val $_,_,$A,_t0,$_,_P0,$_0:Array [Array [Float ,032],4];Constructor (_:Array [Array [Array [Boolean ,0B110],0B1_1_1],0b111]){} }''','''Class,_y,{,Val,$_,,,_,,,$A,,,_t0,,,$_,,,_P0,,,$_0,:,Array,[,Array,[,Float,,,032,],,,4,],;,Constructor,(,_,:,Array,[,Array,[,Array,[,Boolean,,,0B110,],,,0B111,],,,0b111,],),{,},},<EOF>''',101))

    def test_1627(self):
        self.assertTrue(TestLexer.test('''Class v_Xu_{Constructor (__F:Array [Boolean ,0b10_1];f_0:String ;_sW:__;Q,_:Array [Int ,0B111100];W__V,E,_:Array [Boolean ,0B1]){} }''','''Class,v_Xu_,{,Constructor,(,__F,:,Array,[,Boolean,,,0b101,],;,f_0,:,String,;,_sW,:,__,;,Q,,,_,:,Array,[,Int,,,0B111100,],;,W__V,,,E,,,_,:,Array,[,Boolean,,,0B1,],),{,},},<EOF>''',101))

    def test_1628(self):
        self.assertTrue(TestLexer.test('''Class _4__:H{_6(){Break ;} }Class m{Val $K6,q,$l54:___;Destructor (){}Val $__,$_4p:Int ;Val _,_:Array [Float ,02_15];}''','''Class,_4__,:,H,{,_6,(,),{,Break,;,},},Class,m,{,Val,$K6,,,q,,,$l54,:,___,;,Destructor,(,),{,},Val,$__,,,$_4p,:,Int,;,Val,_,,,_,:,Array,[,Float,,,0215,],;,},<EOF>''',101))

    def test_1629(self):
        self.assertTrue(TestLexer.test('''Class d{a(_:Array [Array [Array [Array [Float ,9],0B10_1],0b1],024];M_M8C_4_,KL__:_;__:Int ;kY__:y_9){} }Class t:_o37_{Var $y:Array [Array [Boolean ,024],9];}''','''Class,d,{,a,(,_,:,Array,[,Array,[,Array,[,Array,[,Float,,,9,],,,0B101,],,,0b1,],,,024,],;,M_M8C_4_,,,KL__,:,_,;,__,:,Int,;,kY__,:,y_9,),{,},},Class,t,:,_o37_,{,Var,$y,:,Array,[,Array,[,Boolean,,,024,],,,9,],;,},<EOF>''',101))

    def test_1630(self):
        self.assertTrue(TestLexer.test('''Class _:c9_{Constructor (){iD::$ufW_().c3_18JU6.u8._d.___();} }Class P:_21{Constructor (){Val zO_:Array [Int ,04];} }Class _25__:_{}''','''Class,_,:,c9_,{,Constructor,(,),{,iD,::,$ufW_,(,),.,c3_18JU6,.,u8,.,_d,.,___,(,),;,},},Class,P,:,_21,{,Constructor,(,),{,Val,zO_,:,Array,[,Int,,,04,],;,},},Class,_25__,:,_,{,},<EOF>''',101))

    def test_1631(self):
        self.assertTrue(TestLexer.test('''Class _{Destructor (){}Constructor (){} }Class d2B:g{Var e:dZ;}Class _:__{p(){P_j_::$79();} }Class w:_V_{Val F7_:_0_;}Class j:T3_6U{}Class L{}Class _:__{}''','''Class,_,{,Destructor,(,),{,},Constructor,(,),{,},},Class,d2B,:,g,{,Var,e,:,dZ,;,},Class,_,:,__,{,p,(,),{,P_j_,::,$79,(,),;,},},Class,w,:,_V_,{,Val,F7_,:,_0_,;,},Class,j,:,T3_6U,{,},Class,L,{,},Class,_,:,__,{,},<EOF>''',101))

    def test_1632(self):
        self.assertTrue(TestLexer.test('''Class u88{Constructor (){Break ;} }Class W{_(_F:Float ;_:g_){} }Class a_:j9C{_L(){ {}Continue ;}Destructor (){} }''','''Class,u88,{,Constructor,(,),{,Break,;,},},Class,W,{,_,(,_F,:,Float,;,_,:,g_,),{,},},Class,a_,:,j9C,{,_L,(,),{,{,},Continue,;,},Destructor,(,),{,},},<EOF>''',101))

    def test_1633(self):
        self.assertTrue(TestLexer.test('''Class e:_{}Class _{Val _:Array [Array [Int ,036],036];z2(v:Int ;_G,Ns_1:Boolean ;J,_,P,_,Y0:Array [Float ,07]){ {} }}''','''Class,e,:,_,{,},Class,_,{,Val,_,:,Array,[,Array,[,Int,,,036,],,,036,],;,z2,(,v,:,Int,;,_G,,,Ns_1,:,Boolean,;,J,,,_,,,P,,,_,,,Y0,:,Array,[,Float,,,07,],),{,{,},},},<EOF>''',101))

    def test_1634(self):
        self.assertTrue(TestLexer.test('''Class _{Constructor (F:Array [Float ,0X13];K,_r,_6:Boolean ;_1X,E:Float ;__,_,B:R;_,___,k,__,_:N;g:_;Q,__:x_){} }Class ya0:_0D_{}''','''Class,_,{,Constructor,(,F,:,Array,[,Float,,,0X13,],;,K,,,_r,,,_6,:,Boolean,;,_1X,,,E,:,Float,;,__,,,_,,,B,:,R,;,_,,,___,,,k,,,__,,,_,:,N,;,g,:,_,;,Q,,,__,:,x_,),{,},},Class,ya0,:,_0D_,{,},<EOF>''',101))

    def test_1635(self):
        self.assertTrue(TestLexer.test('''Class _{Constructor (__,_:Array [String ,8_5];_:Array [Boolean ,0X22]){Continue ;} }Class __2:_{Destructor (){}Constructor (){}Destructor (){} }''','''Class,_,{,Constructor,(,__,,,_,:,Array,[,String,,,85,],;,_,:,Array,[,Boolean,,,0X22,],),{,Continue,;,},},Class,__2,:,_,{,Destructor,(,),{,},Constructor,(,),{,},Destructor,(,),{,},},<EOF>''',101))

    def test_1636(self):
        self.assertTrue(TestLexer.test('''Class e:_2_{}Class S:_E_1{Val __,_1,$0:Array [Boolean ,0x31];}Class e:_fg{Var $7:Int ;Constructor (y,_,X,_,wpk,q,_H:Int ){Continue ;} }Class S{}''','''Class,e,:,_2_,{,},Class,S,:,_E_1,{,Val,__,,,_1,,,$0,:,Array,[,Boolean,,,0x31,],;,},Class,e,:,_fg,{,Var,$7,:,Int,;,Constructor,(,y,,,_,,,X,,,_,,,wpk,,,q,,,_H,:,Int,),{,Continue,;,},},Class,S,{,},<EOF>''',101))

    def test_1637(self):
        self.assertTrue(TestLexer.test('''Class _{Y_4(A_:S){Var _:Int ;}Var u0MP_,W:W_L;Constructor (_,S,_:Array [Array [Array [Array [Array [Boolean ,9],0B10],1],033],6];_S3_,XJ7,_,N5:J__){Break ;} }''','''Class,_,{,Y_4,(,A_,:,S,),{,Var,_,:,Int,;,},Var,u0MP_,,,W,:,W_L,;,Constructor,(,_,,,S,,,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,9,],,,0B10,],,,1,],,,033,],,,6,],;,_S3_,,,XJ7,,,_,,,N5,:,J__,),{,Break,;,},},<EOF>''',101))

    def test_1638(self):
        self.assertTrue(TestLexer.test('''Class _{_(EG,__82:Array [Array [Array [Array [Int ,0B1_10_1_1_01],06],82],0XE];__ZI21VX:f){}Val _,$Y:Array [Array [String ,70],70];}Class N_G8:hR_M_96{A2_d(_:B_){ {} }}''','''Class,_,{,_,(,EG,,,__82,:,Array,[,Array,[,Array,[,Array,[,Int,,,0B1101101,],,,06,],,,82,],,,0XE,],;,__ZI21VX,:,f,),{,},Val,_,,,$Y,:,Array,[,Array,[,String,,,70,],,,70,],;,},Class,N_G8,:,hR_M_96,{,A2_d,(,_,:,B_,),{,{,},},},<EOF>''',101))

    def test_1639(self):
        self.assertTrue(TestLexer.test('''Class s:g_S{Destructor (){}Constructor (_m_:Float ;_:SH___V;_:Array [Array [Array [String ,643],0X3_E_3_A_A],0104];_:R_;hB_,_Q_k,__,_6P:L_9){} }Class _:x{$i5(){} }''','''Class,s,:,g_S,{,Destructor,(,),{,},Constructor,(,_m_,:,Float,;,_,:,SH___V,;,_,:,Array,[,Array,[,Array,[,String,,,643,],,,0X3E3AA,],,,0104,],;,_,:,R_,;,hB_,,,_Q_k,,,__,,,_6P,:,L_9,),{,},},Class,_,:,x,{,$i5,(,),{,},},<EOF>''',101))

    def test_1640(self):
        self.assertTrue(TestLexer.test('''Class _z{Constructor (){Val r02,_0:Float ;Return ;}Val _J___Lo1:Array [Array [Float ,0b100101],3];Var $G:_r_;Var w,R:Array [Float ,0133];Var _Yh,_S:_;}Class C5Oi78H:__{}''','''Class,_z,{,Constructor,(,),{,Val,r02,,,_0,:,Float,;,Return,;,},Val,_J___Lo1,:,Array,[,Array,[,Float,,,0b100101,],,,3,],;,Var,$G,:,_r_,;,Var,w,,,R,:,Array,[,Float,,,0133,],;,Var,_Yh,,,_S,:,_,;,},Class,C5Oi78H,:,__,{,},<EOF>''',101))

    def test_1641(self):
        self.assertTrue(TestLexer.test('''Class _:fX{}Class _{Destructor (){}Val $_,_i__,DZ,o,Y0Vr,_4y:h_7;}Class _:_3{Val $_:Array [Float ,0B1101];}Class _:K1{}''','''Class,_,:,fX,{,},Class,_,{,Destructor,(,),{,},Val,$_,,,_i__,,,DZ,,,o,,,Y0Vr,,,_4y,:,h_7,;,},Class,_,:,_3,{,Val,$_,:,Array,[,Float,,,0B1101,],;,},Class,_,:,K1,{,},<EOF>''',101))

    def test_1642(self):
        self.assertTrue(TestLexer.test('''Class kn:_V{Val $PN,$m,$55A42_7:Boolean ;$8(_4,_7:Array [Array [Array [Array [Array [Array [Array [Array [String ,0B1],03],04],0x1F],0B1],0B1],28],03]){Continue ;} }Class x1{}''','''Class,kn,:,_V,{,Val,$PN,,,$m,,,$55A42_7,:,Boolean,;,$8,(,_4,,,_7,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0B1,],,,03,],,,04,],,,0x1F,],,,0B1,],,,0B1,],,,28,],,,03,],),{,Continue,;,},},Class,x1,{,},<EOF>''',101))

    def test_1643(self):
        self.assertTrue(TestLexer.test('''Class _7{}Class D_{Constructor (_:Array [Boolean ,0B1011010];d_2_,w,u,D_:Array [Boolean ,79];__:Array [String ,79];__:Float ){} }''','''Class,_7,{,},Class,D_,{,Constructor,(,_,:,Array,[,Boolean,,,0B1011010,],;,d_2_,,,w,,,u,,,D_,:,Array,[,Boolean,,,79,],;,__,:,Array,[,String,,,79,],;,__,:,Float,),{,},},<EOF>''',101))

    def test_1644(self):
        self.assertTrue(TestLexer.test('''Class __:_{}Class _9:D{}Class N:_{$_9(){}Val B,__5_4Zi:Boolean ;}Class __:_{Var $8_5S___,$_,pAX4:Float ;}Class _:_{}Class _:_{_(){}Constructor (){} }''','''Class,__,:,_,{,},Class,_9,:,D,{,},Class,N,:,_,{,$_9,(,),{,},Val,B,,,__5_4Zi,:,Boolean,;,},Class,__,:,_,{,Var,$8_5S___,,,$_,,,pAX4,:,Float,;,},Class,_,:,_,{,},Class,_,:,_,{,_,(,),{,},Constructor,(,),{,},},<EOF>''',101))

    def test_1645(self):
        self.assertTrue(TestLexer.test('''Class h_190{Var $_0_:Boolean ;_(){ {} }Val $_8:Array [Array [String ,072],033];Constructor (_6_Q:Array [Array [Array [Array [Array [Boolean ,0B1],5_8],38],0b1_1],0B1000]){}Constructor (m__29_:Array [String ,0X11]){Break ;} }''','''Class,h_190,{,Var,$_0_,:,Boolean,;,_,(,),{,{,},},Val,$_8,:,Array,[,Array,[,String,,,072,],,,033,],;,Constructor,(,_6_Q,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0B1,],,,58,],,,38,],,,0b11,],,,0B1000,],),{,},Constructor,(,m__29_,:,Array,[,String,,,0X11,],),{,Break,;,},},<EOF>''',101))

    def test_1646(self):
        self.assertTrue(TestLexer.test('''Class _{Destructor (){}Val T4673,$_I:Array [Boolean ,6];}Class PE_{Constructor (){} }Class h_78_{}Class fm_se:_{}''','''Class,_,{,Destructor,(,),{,},Val,T4673,,,$_I,:,Array,[,Boolean,,,6,],;,},Class,PE_,{,Constructor,(,),{,},},Class,h_78_,{,},Class,fm_se,:,_,{,},<EOF>''',101))

    def test_1647(self):
        self.assertTrue(TestLexer.test('''Class uP:_{Constructor (){}Constructor (nr,_0_,_,a_W:Array [Array [Array [Float ,0B11100],0x2F],72];D:Array [Array [String ,0b111100],05];K,L_,_55:Float ;A_jr5:Array [Array [Array [Boolean ,0b111100],020_7],0x2F]){} }''','''Class,uP,:,_,{,Constructor,(,),{,},Constructor,(,nr,,,_0_,,,_,,,a_W,:,Array,[,Array,[,Array,[,Float,,,0B11100,],,,0x2F,],,,72,],;,D,:,Array,[,Array,[,String,,,0b111100,],,,05,],;,K,,,L_,,,_55,:,Float,;,A_jr5,:,Array,[,Array,[,Array,[,Boolean,,,0b111100,],,,0207,],,,0x2F,],),{,},},<EOF>''',101))

    def test_1648(self):
        self.assertTrue(TestLexer.test('''Class _5{}Class _{_(_:String ;l_V,H,Q3_,_Q:String ;_:Array [Array [Array [Float ,59],042],0b11_1_0]){ {}Val q:String ;} }''','''Class,_5,{,},Class,_,{,_,(,_,:,String,;,l_V,,,H,,,Q3_,,,_Q,:,String,;,_,:,Array,[,Array,[,Array,[,Float,,,59,],,,042,],,,0b1110,],),{,{,},Val,q,:,String,;,},},<EOF>''',101))

    def test_1649(self):
        self.assertTrue(TestLexer.test('''Class _99:g_8U{Var q72_:Int ;Destructor (){Continue ;} }Class i{Var _,_y_:Int ;Destructor (){}Val $0v90,$K:Boolean ;}Class _:bH{Destructor (){}$__(e__W:W;__0,GV7:_7){} }Class p{Constructor (n,_4,___,K:Array [Float ,6];Y_y,___:Array [Array [String ,0X4F],0X4F];__4__8:Array [Array [Array [Array [Array [Array [Float ,9],67],67],0b11110],05],20];b9gr1_:String ;_,__,D:Array [String ,0X2A5]){} }''','''Class,_99,:,g_8U,{,Var,q72_,:,Int,;,Destructor,(,),{,Continue,;,},},Class,i,{,Var,_,,,_y_,:,Int,;,Destructor,(,),{,},Val,$0v90,,,$K,:,Boolean,;,},Class,_,:,bH,{,Destructor,(,),{,},$__,(,e__W,:,W,;,__0,,,GV7,:,_7,),{,},},Class,p,{,Constructor,(,n,,,_4,,,___,,,K,:,Array,[,Float,,,6,],;,Y_y,,,___,:,Array,[,Array,[,String,,,0X4F,],,,0X4F,],;,__4__8,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,9,],,,67,],,,67,],,,0b11110,],,,05,],,,20,],;,b9gr1_,:,String,;,_,,,__,,,D,:,Array,[,String,,,0X2A5,],),{,},},<EOF>''',101))

    def test_1650(self):
        self.assertTrue(TestLexer.test('''Class C6:a4Q5{Constructor (){}Constructor (_:u;_:Array [Array [Array [Array [Float ,0b1],77],0b1],0b1];_E:d){Return ;}w7(){Return ;} }''','''Class,C6,:,a4Q5,{,Constructor,(,),{,},Constructor,(,_,:,u,;,_,:,Array,[,Array,[,Array,[,Array,[,Float,,,0b1,],,,77,],,,0b1,],,,0b1,],;,_E,:,d,),{,Return,;,},w7,(,),{,Return,;,},},<EOF>''',101))

    def test_1651(self):
        self.assertTrue(TestLexer.test('''Class _{Val $_:Array [Boolean ,39];}Class _{}Class A{}Class _{}Class yH:_{}Class _v{Var $_5,s4:String ;Destructor (){} }''','''Class,_,{,Val,$_,:,Array,[,Boolean,,,39,],;,},Class,_,{,},Class,A,{,},Class,_,{,},Class,yH,:,_,{,},Class,_v,{,Var,$_5,,,s4,:,String,;,Destructor,(,),{,},},<EOF>''',101))

    def test_1652(self):
        self.assertTrue(TestLexer.test('''Class _:_{i_(J,f_,W,R:Array [Int ,1_0];_,Z,_7,i,_,_,__:Array [Float ,83];_:_s_W){Return ;} }Class _NS:_{Constructor (){Continue ;} }Class J4Z:_{}Class _v__{}Class _U{}''','''Class,_,:,_,{,i_,(,J,,,f_,,,W,,,R,:,Array,[,Int,,,10,],;,_,,,Z,,,_7,,,i,,,_,,,_,,,__,:,Array,[,Float,,,83,],;,_,:,_s_W,),{,Return,;,},},Class,_NS,:,_,{,Constructor,(,),{,Continue,;,},},Class,J4Z,:,_,{,},Class,_v__,{,},Class,_U,{,},<EOF>''',101))

    def test_1653(self):
        self.assertTrue(TestLexer.test('''Class _6Q3:_p{}Class __f{Constructor (_,___:Array [Boolean ,0B1100]){}Val l:Z;Var $Q,v:Boolean ;}Class _a{}Class Y{}''','''Class,_6Q3,:,_p,{,},Class,__f,{,Constructor,(,_,,,___,:,Array,[,Boolean,,,0B1100,],),{,},Val,l,:,Z,;,Var,$Q,,,v,:,Boolean,;,},Class,_a,{,},Class,Y,{,},<EOF>''',101))

    def test_1654(self):
        self.assertTrue(TestLexer.test('''Class H3{}Class _:_{}Class _5:_{Destructor (){}Constructor (_:_;_:Array [Array [Array [Array [Int ,0X6],0B111100],0xE_C_F],0x6]){Var _Y:Array [Boolean ,075];}Val $_,$_sB:rP;}''','''Class,H3,{,},Class,_,:,_,{,},Class,_5,:,_,{,Destructor,(,),{,},Constructor,(,_,:,_,;,_,:,Array,[,Array,[,Array,[,Array,[,Int,,,0X6,],,,0B111100,],,,0xECF,],,,0x6,],),{,Var,_Y,:,Array,[,Boolean,,,075,],;,},Val,$_,,,$_sB,:,rP,;,},<EOF>''',101))

    def test_1655(self):
        self.assertTrue(TestLexer.test('''Class By 5bA:_{Constructor (_:String ;_Z,_8:Array [Array [String ,7],6_55_1];_15__:_f2;S_:Array [Int ,0b1];W:Boolean ){}Val _7:Float ;Constructor (){} }Class OU___:r4{}Class Yv:q{}''','''Class,By,5,bA,:,_,{,Constructor,(,_,:,String,;,_Z,,,_8,:,Array,[,Array,[,String,,,7,],,,6551,],;,_15__,:,_f2,;,S_,:,Array,[,Int,,,0b1,],;,W,:,Boolean,),{,},Val,_7,:,Float,;,Constructor,(,),{,},},Class,OU___,:,r4,{,},Class,Yv,:,q,{,},<EOF>''',101))

    # def test_1656(self):
    #     self.assertTrue(TestLexer.test('''Class _{}Class E_{Destructor (){} }Class _{Val $_:Array [Boolean ,0b1011111]=!!!!!-Null ._A-!-""/"\n'"".N%_::$7.e__().o()._;}''','''Class,_,{,},Class,E_,{,Destructor,(,),{,},},Class,_,{,Val,$_,:,Array,[,Boolean,,,0b1011111,],=,!,!,!,!,!,-,Null,.,_A,-,!,-,,/,\n'",.,N,%,_,::,$7,.,e__,(,),.,o,(,),.,_,;,},<EOF>''',101))

    def test_1657(self):
        self.assertTrue(TestLexer.test('''Class __U:b__T{$I(_,c_:Int ;O:Array [Float ,023];HIhW8:p){} }Class K6{}Class _601{}Class ___:I2{}Class z_{_VJ1(Q9:Array [Array [Int ,985],023]){}j3(__:Array [Float ,03]){} }''','''Class,__U,:,b__T,{,$I,(,_,,,c_,:,Int,;,O,:,Array,[,Float,,,023,],;,HIhW8,:,p,),{,},},Class,K6,{,},Class,_601,{,},Class,___,:,I2,{,},Class,z_,{,_VJ1,(,Q9,:,Array,[,Array,[,Int,,,985,],,,023,],),{,},j3,(,__,:,Array,[,Float,,,03,],),{,},},<EOF>''',101))

    def test_1658(self):
        self.assertTrue(TestLexer.test('''Class _6{}Class _{}Class _21:_{Constructor (){}Val _16:_5_;}Class x{}Class _{Var $K_42M,G84_,$__S,_:Array [Array [String ,01],0136];}''','''Class,_6,{,},Class,_,{,},Class,_21,:,_,{,Constructor,(,),{,},Val,_16,:,_5_,;,},Class,x,{,},Class,_,{,Var,$K_42M,,,G84_,,,$__S,,,_,:,Array,[,Array,[,String,,,01,],,,0136,],;,},<EOF>''',101))

    def test_1659(self):
        self.assertTrue(TestLexer.test('''Class _{Destructor (){ {}Break ;}C(_,__X_:Array [Array [Array [Float ,3],014],0b10];Z0_C,_J,t_5___2V,q_2_1_:L93){ {} }Var k_6:Boolean ;}''','''Class,_,{,Destructor,(,),{,{,},Break,;,},C,(,_,,,__X_,:,Array,[,Array,[,Array,[,Float,,,3,],,,014,],,,0b10,],;,Z0_C,,,_J,,,t_5___2V,,,q_2_1_,:,L93,),{,{,},},Var,k_6,:,Boolean,;,},<EOF>''',101))

    def test_1660(self):
        self.assertTrue(TestLexer.test('''Class N:O_8V8{Var _3_,$_,$8,_,$s,$_:Array [Array [Array [Boolean ,0B1_0_100],0120],0120];}Class _m{Destructor (){Continue ;}Var _:Array [Int ,04];Val yZ:Boolean ;}''','''Class,N,:,O_8V8,{,Var,_3_,,,$_,,,$8,,,_,,,$s,,,$_,:,Array,[,Array,[,Array,[,Boolean,,,0B10100,],,,0120,],,,0120,],;,},Class,_m,{,Destructor,(,),{,Continue,;,},Var,_,:,Array,[,Int,,,04,],;,Val,yZ,:,Boolean,;,},<EOF>''',101))

    def test_1661(self):
        self.assertTrue(TestLexer.test('''Class __{Val $2,$k,D:Array [Array [Array [Boolean ,0X2],0100],0B101000];Val G,$s,__c76,$_,$_:Array [Array [Array [String ,0X8],0x61],0607];}''','''Class,__,{,Val,$2,,,$k,,,D,:,Array,[,Array,[,Array,[,Boolean,,,0X2,],,,0100,],,,0B101000,],;,Val,G,,,$s,,,__c76,,,$_,,,$_,:,Array,[,Array,[,Array,[,String,,,0X8,],,,0x61,],,,0607,],;,},<EOF>''',101))

    def test_1662(self):
        self.assertTrue(TestLexer.test('''Class Z0q:DbO2{Constructor (_,_,_:Float ;Dc,l:Pu1){} }Class _:Y{}Class __{Var $_:Array [Boolean ,0b110101];}Class v:_{Var __6:Boolean ;_qc2HQh(){} }''','''Class,Z0q,:,DbO2,{,Constructor,(,_,,,_,,,_,:,Float,;,Dc,,,l,:,Pu1,),{,},},Class,_,:,Y,{,},Class,__,{,Var,$_,:,Array,[,Boolean,,,0b110101,],;,},Class,v,:,_,{,Var,__6,:,Boolean,;,_qc2HQh,(,),{,},},<EOF>''',101))

    def test_1663(self):
        self.assertTrue(TestLexer.test('''Class ___1_:_6{}Class NK:q{}Class _{Destructor (){} }Class k:_4_4{Constructor (_:Array [Array [String ,50],050]){} }''','''Class,___1_,:,_6,{,},Class,NK,:,q,{,},Class,_,{,Destructor,(,),{,},},Class,k,:,_4_4,{,Constructor,(,_,:,Array,[,Array,[,String,,,50,],,,050,],),{,},},<EOF>''',101))

    def test_1664(self):
        self.assertTrue(TestLexer.test('''Class Z{}Class pU{}Class _5:_{Destructor (){Break ;} }Class i6{}Class z_{Var $__:Int ;Destructor (){} }Class n:P{}''','''Class,Z,{,},Class,pU,{,},Class,_5,:,_,{,Destructor,(,),{,Break,;,},},Class,i6,{,},Class,z_,{,Var,$__,:,Int,;,Destructor,(,),{,},},Class,n,:,P,{,},<EOF>''',101))

    def test_1665(self):
        self.assertTrue(TestLexer.test('''Class p:rNmc_h_{}Class ___:_{}Class _3_{Constructor (Z,x:Array [Array [Int ,95],0x35];p6:Int ){}Constructor (iJ,Z:Int ){} }''','''Class,p,:,rNmc_h_,{,},Class,___,:,_,{,},Class,_3_,{,Constructor,(,Z,,,x,:,Array,[,Array,[,Int,,,95,],,,0x35,],;,p6,:,Int,),{,},Constructor,(,iJ,,,Z,:,Int,),{,},},<EOF>''',101))

    def test_1666(self):
        self.assertTrue(TestLexer.test('''Class _:G6{Var $4:Array [Array [Array [Float ,0B1011010],0x29],0b10];Var $6,$77r:__;Constructor (e_:_0){} }Class t0q:e_z{}''','''Class,_,:,G6,{,Var,$4,:,Array,[,Array,[,Array,[,Float,,,0B1011010,],,,0x29,],,,0b10,],;,Var,$6,,,$77r,:,__,;,Constructor,(,e_,:,_0,),{,},},Class,t0q,:,e_z,{,},<EOF>''',101))

    def test_1667(self):
        self.assertTrue(TestLexer.test('''Class R:_KN{}Class G{Constructor (_:Array [Array [Array [Boolean ,4_38],066],0x37]){e__::$2_663AW21BD();Break ;} }Class x{}Class _p{}Class _R:__{}Class O1Y2{}Class _{}''','''Class,R,:,_KN,{,},Class,G,{,Constructor,(,_,:,Array,[,Array,[,Array,[,Boolean,,,438,],,,066,],,,0x37,],),{,e__,::,$2_663AW21BD,(,),;,Break,;,},},Class,x,{,},Class,_p,{,},Class,_R,:,__,{,},Class,O1Y2,{,},Class,_,{,},<EOF>''',101))

    def test_1668(self):
        self.assertTrue(TestLexer.test('''Class N3:H{Val $_v,p:Array [Float ,0B1000111];}Class _:_61r_8{}Class k_2{Destructor (){ {Continue ;Return ;}Val TI_g,__8_g:Int ;} }Class r:_{Val $_H,$4,$X:Boolean ;Var __,_U_:Array [String ,0b100001];}''','''Class,N3,:,H,{,Val,$_v,,,p,:,Array,[,Float,,,0B1000111,],;,},Class,_,:,_61r_8,{,},Class,k_2,{,Destructor,(,),{,{,Continue,;,Return,;,},Val,TI_g,,,__8_g,:,Int,;,},},Class,r,:,_,{,Val,$_H,,,$4,,,$X,:,Boolean,;,Var,__,,,_U_,:,Array,[,String,,,0b100001,],;,},<EOF>''',101))

    def test_1669(self):
        self.assertTrue(TestLexer.test('''Class __n:K8{Eb1_d(T,a,__3C,_1:Array [Array [Float ,0X57],02];Oc:Int ;_:__xL9_;_X0,r,_:Int ;P_:Array [Array [Array [Array [Boolean ,8],0X1],0XF292_68_2],0b1]){} }Class _{}''','''Class,__n,:,K8,{,Eb1_d,(,T,,,a,,,__3C,,,_1,:,Array,[,Array,[,Float,,,0X57,],,,02,],;,Oc,:,Int,;,_,:,__xL9_,;,_X0,,,r,,,_,:,Int,;,P_,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,8,],,,0X1,],,,0XF292682,],,,0b1,],),{,},},Class,_,{,},<EOF>''',101))

    def test_1670(self):
        self.assertTrue(TestLexer.test('''Class o{Constructor (K,wy:Q;dX87:_){}r(_:_;__a,W:Array [Array [Array [Array [Array [Array [Array [Array [Int ,034],034],70],0b110011],0b110011],077_0_40],0X7_9_7_2_03],0b10101]){} }''','''Class,o,{,Constructor,(,K,,,wy,:,Q,;,dX87,:,_,),{,},r,(,_,:,_,;,__a,,,W,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,034,],,,034,],,,70,],,,0b110011,],,,0b110011,],,,077040,],,,0X797203,],,,0b10101,],),{,},},<EOF>''',101))

    def test_1671(self):
        self.assertTrue(TestLexer.test('''Class O{}Class _8{Val SA,$__1bu,$C,_:_;$8E(){ {} }Var $_:Float ;Constructor (u__,r,f,f:Array [Array [Array [String ,07],0b1001011],0B10100];d37_:_S_){} }''','''Class,O,{,},Class,_8,{,Val,SA,,,$__1bu,,,$C,,,_,:,_,;,$8E,(,),{,{,},},Var,$_,:,Float,;,Constructor,(,u__,,,r,,,f,,,f,:,Array,[,Array,[,Array,[,String,,,07,],,,0b1001011,],,,0B10100,],;,d37_,:,_S_,),{,},},<EOF>''',101))

    def test_1672(self):
        self.assertTrue(TestLexer.test('''Class _k_7:_{Constructor (){Break ;}Constructor (){} }Class __u4{}Class T7_:J{}Class O_{}Class _:_{$E(_:String ){_bp::$CB7().S._._pJS();Break ;Break ;Return ;} }Class C_:_{}''','''Class,_k_7,:,_,{,Constructor,(,),{,Break,;,},Constructor,(,),{,},},Class,__u4,{,},Class,T7_,:,J,{,},Class,O_,{,},Class,_,:,_,{,$E,(,_,:,String,),{,_bp,::,$CB7,(,),.,S,.,_,.,_pJS,(,),;,Break,;,Break,;,Return,;,},},Class,C_,:,_,{,},<EOF>''',101))

    def test_1673(self):
        self.assertTrue(TestLexer.test('''Class H:D6{Val $15,J_,$f,$_y0_6uP_:String ;}Class __:p_{_9(w_5M:Boolean ;T1A4,q_,_:Array [Array [Int ,8_237],0772];d:v){Continue ;} }''','''Class,H,:,D6,{,Val,$15,,,J_,,,$f,,,$_y0_6uP_,:,String,;,},Class,__,:,p_,{,_9,(,w_5M,:,Boolean,;,T1A4,,,q_,,,_,:,Array,[,Array,[,Int,,,8237,],,,0772,],;,d,:,v,),{,Continue,;,},},<EOF>''',101))

    def test_1674(self):
        self.assertTrue(TestLexer.test('''Class B8:_5_u_0{Var $4:Array [Boolean ,061];Var _P,$6,o_,_:m;}Class t{Val $_1:Int ;Val $6_:Array [String ,387_2];}Class __7{}''','''Class,B8,:,_5_u_0,{,Var,$4,:,Array,[,Boolean,,,061,],;,Var,_P,,,$6,,,o_,,,_,:,m,;,},Class,t,{,Val,$_1,:,Int,;,Val,$6_,:,Array,[,String,,,3872,],;,},Class,__7,{,},<EOF>''',101))

    def test_1675(self):
        self.assertTrue(TestLexer.test('''Class _{Var $__,$m,$E,__,$9:Array [Array [Array [Int ,046],0B1],046];Var $Bz,$mK_9,_:D2h;Var __7,Ej:E;Constructor (p_s,D_,f,ax:Int ;R2_p2,S_W__,_:Int ){Break ;Break ;} }Class _f{Var $0:F;}Class _:N{}Class _:_4{}''','''Class,_,{,Var,$__,,,$m,,,$E,,,__,,,$9,:,Array,[,Array,[,Array,[,Int,,,046,],,,0B1,],,,046,],;,Var,$Bz,,,$mK_9,,,_,:,D2h,;,Var,__7,,,Ej,:,E,;,Constructor,(,p_s,,,D_,,,f,,,ax,:,Int,;,R2_p2,,,S_W__,,,_,:,Int,),{,Break,;,Break,;,},},Class,_f,{,Var,$0,:,F,;,},Class,_,:,N,{,},Class,_,:,_4,{,},<EOF>''',101))

    def test_1676(self):
        self.assertTrue(TestLexer.test('''Class a{Constructor (__GnD,du:Boolean ;Ug:Boolean ;c:N;R:pX;_,_:_5___;_T:Array [Array [Array [Boolean ,27],0B100001],03]){} }''','''Class,a,{,Constructor,(,__GnD,,,du,:,Boolean,;,Ug,:,Boolean,;,c,:,N,;,R,:,pX,;,_,,,_,:,_5___,;,_T,:,Array,[,Array,[,Array,[,Boolean,,,27,],,,0B100001,],,,03,],),{,},},<EOF>''',101))

    def test_1677(self):
        self.assertTrue(TestLexer.test('''Class g:tiT{Constructor (_cm,G,___:Array [String ,0b1001000];_,_:Boolean ;_:h9;T:Array [Array [Boolean ,1_0],41];g:_){} }Class f:__{Constructor (J,M:Array [Array [Array [Int ,03],41],41]){} }Class _2__{}''','''Class,g,:,tiT,{,Constructor,(,_cm,,,G,,,___,:,Array,[,String,,,0b1001000,],;,_,,,_,:,Boolean,;,_,:,h9,;,T,:,Array,[,Array,[,Boolean,,,10,],,,41,],;,g,:,_,),{,},},Class,f,:,__,{,Constructor,(,J,,,M,:,Array,[,Array,[,Array,[,Int,,,03,],,,41,],,,41,],),{,},},Class,_2__,{,},<EOF>''',101))

    def test_1678(self):
        self.assertTrue(TestLexer.test('''Class _g36{}Class _{}Class Z:_{Var _:Array [Boolean ,0B1];}Class W_z_6{Destructor (){Continue ;Return ;} }Class _{}''','''Class,_g36,{,},Class,_,{,},Class,Z,:,_,{,Var,_,:,Array,[,Boolean,,,0B1,],;,},Class,W_z_6,{,Destructor,(,),{,Continue,;,Return,;,},},Class,_,{,},<EOF>''',101))

    def test_1679(self):
        self.assertTrue(TestLexer.test('''Class _:_{}Class _v_9:_{Var _,$_y:_;Destructor (){Continue ;} }Class _:_u{Constructor (W_4,o_:Array [Array [Array [Array [Int ,0B1],0b1011100],74],0X7];_:Boolean ;_Pc6:Array [Boolean ,0X5C];Wx0,V,_4:String ){} }''','''Class,_,:,_,{,},Class,_v_9,:,_,{,Var,_,,,$_y,:,_,;,Destructor,(,),{,Continue,;,},},Class,_,:,_u,{,Constructor,(,W_4,,,o_,:,Array,[,Array,[,Array,[,Array,[,Int,,,0B1,],,,0b1011100,],,,74,],,,0X7,],;,_,:,Boolean,;,_Pc6,:,Array,[,Boolean,,,0X5C,],;,Wx0,,,V,,,_4,:,String,),{,},},<EOF>''',101))

    def test_1680(self):
        self.assertTrue(TestLexer.test('''Class _:Q_75_{$s(_q:X;_e,_:String ;f_0:_;_,P:Int ;_8i2I5_,ps:Array [Array [String ,74_86],0115];JVwg0,_:Array [Array [String ,6],07]){} }''','''Class,_,:,Q_75_,{,$s,(,_q,:,X,;,_e,,,_,:,String,;,f_0,:,_,;,_,,,P,:,Int,;,_8i2I5_,,,ps,:,Array,[,Array,[,String,,,7486,],,,0115,],;,JVwg0,,,_,:,Array,[,Array,[,String,,,6,],,,07,],),{,},},<EOF>''',101))

    def test_1681(self):
        self.assertTrue(TestLexer.test('''Class u_:__{Destructor (){Var __m_6URoG,h3nU,_O_l0,_b,_:Array [Array [Boolean ,0b1],33];}Val _,$m,C,I2s_,B,$po:Array [Float ,061];}Class Cl{}''','''Class,u_,:,__,{,Destructor,(,),{,Var,__m_6URoG,,,h3nU,,,_O_l0,,,_b,,,_,:,Array,[,Array,[,Boolean,,,0b1,],,,33,],;,},Val,_,,,$m,,,C,,,I2s_,,,B,,,$po,:,Array,[,Float,,,061,],;,},Class,Cl,{,},<EOF>''',101))

    def test_1682(self):
        self.assertTrue(TestLexer.test('''Class _{Val _,$_,$I,$_,$U:Array [Float ,57];}Class _:_{Var d:_;}Class _{$_(r__,_8,H,D_l,_,_:Float ;_:Float ){} }Class __7:Q{}Class B_6_J57_:r_k{}''','''Class,_,{,Val,_,,,$_,,,$I,,,$_,,,$U,:,Array,[,Float,,,57,],;,},Class,_,:,_,{,Var,d,:,_,;,},Class,_,{,$_,(,r__,,,_8,,,H,,,D_l,,,_,,,_,:,Float,;,_,:,Float,),{,},},Class,__7,:,Q,{,},Class,B_6_J57_,:,r_k,{,},<EOF>''',101))

    def test_1683(self):
        self.assertTrue(TestLexer.test('''Class _:c{Constructor (){} }Class X{Var PA,$_:_;}Class Y{Constructor (){}$_y_52(){Break ;}Val $x,_z__p,_:String ;}Class _B{}Class w{}Class Im{}''','''Class,_,:,c,{,Constructor,(,),{,},},Class,X,{,Var,PA,,,$_,:,_,;,},Class,Y,{,Constructor,(,),{,},$_y_52,(,),{,Break,;,},Val,$x,,,_z__p,,,_,:,String,;,},Class,_B,{,},Class,w,{,},Class,Im,{,},<EOF>''',101))

    def test_1684(self):
        self.assertTrue(TestLexer.test('''Class r_{}Class W0:M_{Constructor (L:Int ;E:__;_:Array [Array [Array [Array [Array [Boolean ,0101],11],0101],0B110001],0174]){ {} }Var _,$53:L;$_(){}Var e3:Int ;}''','''Class,r_,{,},Class,W0,:,M_,{,Constructor,(,L,:,Int,;,E,:,__,;,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0101,],,,11,],,,0101,],,,0B110001,],,,0174,],),{,{,},},Var,_,,,$53,:,L,;,$_,(,),{,},Var,e3,:,Int,;,},<EOF>''',101))

    def test_1685(self):
        self.assertTrue(TestLexer.test('''Class _{Val b,$r:Array [Array [Array [String ,0B110],02],33];_6d(uUH,e_t,_:Boolean ;G:__c_r1_;_:Boolean ;_7:Array [Float ,0B1]){} }''','''Class,_,{,Val,b,,,$r,:,Array,[,Array,[,Array,[,String,,,0B110,],,,02,],,,33,],;,_6d,(,uUH,,,e_t,,,_,:,Boolean,;,G,:,__c_r1_,;,_,:,Boolean,;,_7,:,Array,[,Float,,,0B1,],),{,},},<EOF>''',101))

    def test_1686(self):
        self.assertTrue(TestLexer.test('''Class y:_{Val E,_,$8,_,$_,$_1,$_,$_:String ;}Class _{$Um(g_,_:Array [Int ,0B1000100];E_,_5_69y:Float ;_1_:Float ;TwjXU:String ){ {} }}Class X{}''','''Class,y,:,_,{,Val,E,,,_,,,$8,,,_,,,$_,,,$_1,,,$_,,,$_,:,String,;,},Class,_,{,$Um,(,g_,,,_,:,Array,[,Int,,,0B1000100,],;,E_,,,_5_69y,:,Float,;,_1_,:,Float,;,TwjXU,:,String,),{,{,},},},Class,X,{,},<EOF>''',101))

    def test_1687(self):
        self.assertTrue(TestLexer.test('''Class H_:_2{Var _:Array [Array [Boolean ,0xCF0],0X25];__Ib(M:Array [Boolean ,0B1000111]){Break ;{Continue ;e::$R.t();} }}''','''Class,H_,:,_2,{,Var,_,:,Array,[,Array,[,Boolean,,,0xCF0,],,,0X25,],;,__Ib,(,M,:,Array,[,Boolean,,,0B1000111,],),{,Break,;,{,Continue,;,e,::,$R,.,t,(,),;,},},},<EOF>''',101))

    def test_1688(self):
        self.assertTrue(TestLexer.test('''Class n{}Class _{Constructor (_5_95:_;u_:_i){}$__dm(a:u1v1){}Constructor (_3:Boolean ;v___,_2_,_tGP:Int ;_:String ){} }''','''Class,n,{,},Class,_,{,Constructor,(,_5_95,:,_,;,u_,:,_i,),{,},$__dm,(,a,:,u1v1,),{,},Constructor,(,_3,:,Boolean,;,v___,,,_2_,,,_tGP,:,Int,;,_,:,String,),{,},},<EOF>''',101))

    def test_1689(self):
        self.assertTrue(TestLexer.test('''Class _d21:_{}Class z{_(){Var dc9,Y:Array [Array [Float ,9],0xA];}Constructor (H,_:Array [String ,0x4C];_:Boolean ){} }''','''Class,_d21,:,_,{,},Class,z,{,_,(,),{,Var,dc9,,,Y,:,Array,[,Array,[,Float,,,9,],,,0xA,],;,},Constructor,(,H,,,_,:,Array,[,String,,,0x4C,],;,_,:,Boolean,),{,},},<EOF>''',101))

    def test_1690(self):
        self.assertTrue(TestLexer.test('''Class XiB{Destructor (){}Constructor (__8_:Array [Boolean ,28];_,_2R:l){Break ;} }Class s{$P(_0:Array [Boolean ,28];_v3:R_Xp___6;_p:Array [String ,05];F91,Q_X,_75:_;H:Array [Array [Array [Array [Array [Array [String ,0B1_01_0_0],4],28],9],0b1_0],5];_,_,_,_:Array [Array [Array [Array [Array [Array [Int ,0x21],0x85],3],0X2],0b1],28]){} }''','''Class,XiB,{,Destructor,(,),{,},Constructor,(,__8_,:,Array,[,Boolean,,,28,],;,_,,,_2R,:,l,),{,Break,;,},},Class,s,{,$P,(,_0,:,Array,[,Boolean,,,28,],;,_v3,:,R_Xp___6,;,_p,:,Array,[,String,,,05,],;,F91,,,Q_X,,,_75,:,_,;,H,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0B10100,],,,4,],,,28,],,,9,],,,0b10,],,,5,],;,_,,,_,,,_,,,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,0x21,],,,0x85,],,,3,],,,0X2,],,,0b1,],,,28,],),{,},},<EOF>''',101))

    def test_1691(self):
        self.assertTrue(TestLexer.test('''Class b{}Class T:Z71{$_(){}Var $8:B;}Class v4:Ew6{}Class __{Val _c_,$_:Array [Array [Array [Array [Array [String ,0b1100000],0b11_0_1],02_14],0XEF],19];}''','''Class,b,{,},Class,T,:,Z71,{,$_,(,),{,},Var,$8,:,B,;,},Class,v4,:,Ew6,{,},Class,__,{,Val,_c_,,,$_,:,Array,[,Array,[,Array,[,Array,[,Array,[,String,,,0b1100000,],,,0b1101,],,,0214,],,,0XEF,],,,19,],;,},<EOF>''',101))

    def test_1692(self):
        self.assertTrue(TestLexer.test('''Class T___s{}Class i:O{}Class _b_{Var _4,VI,L:Array [Float ,0b1011101];Constructor (b_,_:Boolean ;_:Array [Array [Int ,01],0b1];X5:_;g:Os){} }''','''Class,T___s,{,},Class,i,:,O,{,},Class,_b_,{,Var,_4,,,VI,,,L,:,Array,[,Float,,,0b1011101,],;,Constructor,(,b_,,,_,:,Boolean,;,_,:,Array,[,Array,[,Int,,,01,],,,0b1,],;,X5,:,_,;,g,:,Os,),{,},},<EOF>''',101))

    def test_1693(self):
        self.assertTrue(TestLexer.test('''Class _G1:__2_lG_{}Class __:_1_{Var l0,$_1,__:Int ;}Class _{Constructor (T7,m_h_93P_:Array [Array [Float ,0132],03];j,r7:Boolean ){} }''','''Class,_G1,:,__2_lG_,{,},Class,__,:,_1_,{,Var,l0,,,$_1,,,__,:,Int,;,},Class,_,{,Constructor,(,T7,,,m_h_93P_,:,Array,[,Array,[,Float,,,0132,],,,03,],;,j,,,r7,:,Boolean,),{,},},<EOF>''',101))

    def test_1694(self):
        self.assertTrue(TestLexer.test('''Class xB_:v{Var s1V6,g_,$2w9:Array [Int ,7];Constructor (_,v:Uf){}Constructor (K_:Array [Int ,12];_2,x65:Array [Array [Array [Int ,0xC1],0B1_1],1]){Continue ;} }''','''Class,xB_,:,v,{,Var,s1V6,,,g_,,,$2w9,:,Array,[,Int,,,7,],;,Constructor,(,_,,,v,:,Uf,),{,},Constructor,(,K_,:,Array,[,Int,,,12,],;,_2,,,x65,:,Array,[,Array,[,Array,[,Int,,,0xC1,],,,0B11,],,,1,],),{,Continue,;,},},<EOF>''',101))

    def test_1695(self):
        self.assertTrue(TestLexer.test('''Class _R{Destructor (){ {} }}Class yNB:V_{}Class _{}Class L{Val $4:Array [Array [Array [Array [Float ,074],0XB8_8],074],074];}Class ewa:T0_{}Class V{}Class _2_R{Constructor (y:Array [Array [Array [Float ,0X1E],81],0x10_B];_S2,i:Array [Array [Array [Array [Float ,06_0047],0452],01],074];_lY_4:Boolean ){}Constructor (SZ__,bY:Array [Array [Array [String ,06_62_7_1_53],66_2],0x5]){} }''','''Class,_R,{,Destructor,(,),{,{,},},},Class,yNB,:,V_,{,},Class,_,{,},Class,L,{,Val,$4,:,Array,[,Array,[,Array,[,Array,[,Float,,,074,],,,0XB88,],,,074,],,,074,],;,},Class,ewa,:,T0_,{,},Class,V,{,},Class,_2_R,{,Constructor,(,y,:,Array,[,Array,[,Array,[,Float,,,0X1E,],,,81,],,,0x10B,],;,_S2,,,i,:,Array,[,Array,[,Array,[,Array,[,Float,,,060047,],,,0452,],,,01,],,,074,],;,_lY_4,:,Boolean,),{,},Constructor,(,SZ__,,,bY,:,Array,[,Array,[,Array,[,String,,,06627153,],,,662,],,,0x5,],),{,},},<EOF>''',101))

    def test_1696(self):
        self.assertTrue(TestLexer.test('''Class K{}Class _:__I{Constructor (){Var RF,R:Array [Array [Array [Array [Array [Int ,03],7],0X8],0X8],71];}Destructor (){}Constructor (){} }''','''Class,K,{,},Class,_,:,__I,{,Constructor,(,),{,Var,RF,,,R,:,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,03,],,,7,],,,0X8,],,,0X8,],,,71,],;,},Destructor,(,),{,},Constructor,(,),{,},},<EOF>''',101))

    def test_1697(self):
        self.assertTrue(TestLexer.test('''Class q_6_:W{}Class _{}Class o_{$9q(_,V:Array [Boolean ,0B10000];_2B:w;_5,r4:Array [Array [Array [Float ,17],17],398_95_381];z:Boolean ){} }''','''Class,q_6_,:,W,{,},Class,_,{,},Class,o_,{,$9q,(,_,,,V,:,Array,[,Boolean,,,0B10000,],;,_2B,:,w,;,_5,,,r4,:,Array,[,Array,[,Array,[,Float,,,17,],,,17,],,,39895381,],;,z,:,Boolean,),{,},},<EOF>''',101))

    def test_1698(self):
        self.assertTrue(TestLexer.test('''Class __:o{X(t:j51;_Z_:__43){} }Class U{Var ____:I;}Class __C:_h{Var $_:_;}Class U{}Class _1:__{$gH(){} }Class fI{}Class _yz:s2a{}Class F_{Destructor (){} }''','''Class,__,:,o,{,X,(,t,:,j51,;,_Z_,:,__43,),{,},},Class,U,{,Var,____,:,I,;,},Class,__C,:,_h,{,Var,$_,:,_,;,},Class,U,{,},Class,_1,:,__,{,$gH,(,),{,},},Class,fI,{,},Class,_yz,:,s2a,{,},Class,F_,{,Destructor,(,),{,},},<EOF>''',101))

    def test_1699(self):
        self.assertTrue(TestLexer.test('''Class _1:_{Val l3:_;Val $9H:_;}Class _o{}Class _n{Var $0:String ;$wQ4(R,_,_,_t:Int ){}Val $8_,_,n,_,$_,_:_K_y6A;Constructor (){} }Class _:_{t(R:Boolean ){Break ;} }Class __:C5_{}''','''Class,_1,:,_,{,Val,l3,:,_,;,Val,$9H,:,_,;,},Class,_o,{,},Class,_n,{,Var,$0,:,String,;,$wQ4,(,R,,,_,,,_,,,_t,:,Int,),{,},Val,$8_,,,_,,,n,,,_,,,$_,,,_,:,_K_y6A,;,Constructor,(,),{,},},Class,_,:,_,{,t,(,R,:,Boolean,),{,Break,;,},},Class,__,:,C5_,{,},<EOF>''',101))

    def test_1700(self):
        self.assertTrue(TestLexer.test('''Class A_h{Constructor (){} }Class c0_5_8:v{Constructor (){} }Class __:_1{}Class X__0{}Class I{Constructor (){Break ;Break ;} }Class _1{}''','''Class,A_h,{,Constructor,(,),{,},},Class,c0_5_8,:,v,{,Constructor,(,),{,},},Class,__,:,_1,{,},Class,X__0,{,},Class,I,{,Constructor,(,),{,Break,;,Break,;,},},Class,_1,{,},<EOF>''',101))

    def test_1701(self):
        self.assertTrue(TestLexer.test('''Class _X{Constructor (s,_f4,_,vD:t;t_:Array [String ,0xA];A,qL:Int ;y:D;_,_4,__:String ;__9,_q8_,_6,PX,_,_:t_;q91,_,Z,C:Boolean ;U:Array [Int ,06_4_5_2];Z,pgn_,t:Int ){} }''','''Class,_X,{,Constructor,(,s,,,_f4,,,_,,,vD,:,t,;,t_,:,Array,[,String,,,0xA,],;,A,,,qL,:,Int,;,y,:,D,;,_,,,_4,,,__,:,String,;,__9,,,_q8_,,,_6,,,PX,,,_,,,_,:,t_,;,q91,,,_,,,Z,,,C,:,Boolean,;,U,:,Array,[,Int,,,06452,],;,Z,,,pgn_,,,t,:,Int,),{,},},<EOF>''',101))

    def test_1702(self):
        self.assertTrue(TestLexer.test('''Class _:j{Var $i,W6r_:Array [Array [Array [Array [Array [Boolean ,30],0XCE_9],7],0x20],30];}Class _:p4_{}Class X6{Val _78_,K7:String ;}''','''Class,_,:,j,{,Var,$i,,,W6r_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,30,],,,0XCE9,],,,7,],,,0x20,],,,30,],;,},Class,_,:,p4_,{,},Class,X6,{,Val,_78_,,,K7,:,String,;,},<EOF>''',101))

    def test_1703(self):
        self.assertTrue(TestLexer.test('''Class __:N{$G_(_,L9:String ;g:ZO__;__,W,_38_,_:Array [Array [String ,0125],6];__,__0_,J,_:Array [String ,0xC_7A_A]){} }Class J{Var d:Array [Int ,0B1100];}Class IIe:o{}''','''Class,__,:,N,{,$G_,(,_,,,L9,:,String,;,g,:,ZO__,;,__,,,W,,,_38_,,,_,:,Array,[,Array,[,String,,,0125,],,,6,],;,__,,,__0_,,,J,,,_,:,Array,[,String,,,0xC7AA,],),{,},},Class,J,{,Var,d,:,Array,[,Int,,,0B1100,],;,},Class,IIe,:,o,{,},<EOF>''',101))

    def test_1704(self):
        self.assertTrue(TestLexer.test('''Class o:KGw{_(){} }Class _{_(_t_1:Float ;P:Array [Array [String ,0X3F],17];_,E:Int ;bGj,_:Array [Boolean ,0x88];B_:Boolean ){} }''','''Class,o,:,KGw,{,_,(,),{,},},Class,_,{,_,(,_t_1,:,Float,;,P,:,Array,[,Array,[,String,,,0X3F,],,,17,],;,_,,,E,:,Int,;,bGj,,,_,:,Array,[,Boolean,,,0x88,],;,B_,:,Boolean,),{,},},<EOF>''',101))

    def test_1705(self):
        self.assertTrue(TestLexer.test('''Class _9B3__{Val $_:Int ;Val __,Q,v_:I;Val $__:String ;$__(Q:Array [String ,74];__,_6,_,K,_T:Int ){_::$U();} }Class h:f{}''','''Class,_9B3__,{,Val,$_,:,Int,;,Val,__,,,Q,,,v_,:,I,;,Val,$__,:,String,;,$__,(,Q,:,Array,[,String,,,74,],;,__,,,_6,,,_,,,K,,,_T,:,Int,),{,_,::,$U,(,),;,},},Class,h,:,f,{,},<EOF>''',101))

    def test_1706(self):
        self.assertTrue(TestLexer.test('''Class _:__{$1(_,t__,_:_2n;Z,X:String ;Q:Boolean ){Return ;} }Class ___L__0{Destructor (){}Constructor (){_::$20_()._()._7_Z();} }''','''Class,_,:,__,{,$1,(,_,,,t__,,,_,:,_2n,;,Z,,,X,:,String,;,Q,:,Boolean,),{,Return,;,},},Class,___L__0,{,Destructor,(,),{,},Constructor,(,),{,_,::,$20_,(,),.,_,(,),.,_7_Z,(,),;,},},<EOF>''',101))

    def test_1707(self):
        self.assertTrue(TestLexer.test('''Class _1s:m___{}Class __{}Class _7O6:_{}Class N{$t_5c_(Q,z:_8){}$2(_,g:Float ;_,e,_S,t_9Sk,_,_Z,e,uN7I,_:_){} }Class _:K_X{}''','''Class,_1s,:,m___,{,},Class,__,{,},Class,_7O6,:,_,{,},Class,N,{,$t_5c_,(,Q,,,z,:,_8,),{,},$2,(,_,,,g,:,Float,;,_,,,e,,,_S,,,t_9Sk,,,_,,,_Z,,,e,,,uN7I,,,_,:,_,),{,},},Class,_,:,K_X,{,},<EOF>''',101))

    def test_1708(self):
        self.assertTrue(TestLexer.test('''Class _7__:_1{}Class JyZ:b_{Val z:Array [Array [Array [String ,7],21],0B1];$_(j_,_,Weg9:Array [Array [Boolean ,21],0x3A]){} }''','''Class,_7__,:,_1,{,},Class,JyZ,:,b_,{,Val,z,:,Array,[,Array,[,Array,[,String,,,7,],,,21,],,,0B1,],;,$_,(,j_,,,_,,,Weg9,:,Array,[,Array,[,Boolean,,,21,],,,0x3A,],),{,},},<EOF>''',101))

    def test_1709(self):
        self.assertTrue(TestLexer.test('''Class m:u8A_p{Constructor (_8,_66:Array [Int ,0X5E_C4]){}Val _:Array [Array [Array [Array [String ,0b11_111],025],0x3A],074];_9(){} }Class _{Var $aL,X:_xq;}''','''Class,m,:,u8A_p,{,Constructor,(,_8,,,_66,:,Array,[,Int,,,0X5EC4,],),{,},Val,_,:,Array,[,Array,[,Array,[,Array,[,String,,,0b11111,],,,025,],,,0x3A,],,,074,],;,_9,(,),{,},},Class,_,{,Var,$aL,,,X,:,_xq,;,},<EOF>''',101))

    def test_1710(self):
        self.assertTrue(TestLexer.test('''Class O_{}Class _{Var $sQp3,o:Array [Array [Array [Array [Array [Boolean ,874],4_8_9],0X9],0B1000010],73];Val $_0,$6:_;Val _4:_;$_4Rh(){Return ;} }''','''Class,O_,{,},Class,_,{,Var,$sQp3,,,o,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,874,],,,489,],,,0X9,],,,0B1000010,],,,73,],;,Val,$_0,,,$6,:,_,;,Val,_4,:,_,;,$_4Rh,(,),{,Return,;,},},<EOF>''',101))

    def test_1711(self):
        self.assertTrue(TestLexer.test('''Class A{$_(k,k,q0_:Array [Float ,0B1001111];_,L50,a1:_;qZ__:Int ){} }Class _:_Po19{}Class A_ed:_78bv_{Val $_,$5:Float ;}Class P:wX{}Class g{_(__:_K;Q:Boolean ){} }''','''Class,A,{,$_,(,k,,,k,,,q0_,:,Array,[,Float,,,0B1001111,],;,_,,,L50,,,a1,:,_,;,qZ__,:,Int,),{,},},Class,_,:,_Po19,{,},Class,A_ed,:,_78bv_,{,Val,$_,,,$5,:,Float,;,},Class,P,:,wX,{,},Class,g,{,_,(,__,:,_K,;,Q,:,Boolean,),{,},},<EOF>''',101))

    def test_1712(self):
        self.assertTrue(TestLexer.test('''Class m:_{Destructor (){}Var $S_3:Boolean ;Val $2,$___,$9:Array [Array [Array [Array [Boolean ,28],0x39],0104],0x39];}''','''Class,m,:,_,{,Destructor,(,),{,},Var,$S_3,:,Boolean,;,Val,$2,,,$___,,,$9,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,28,],,,0x39,],,,0104,],,,0x39,],;,},<EOF>''',101))

    def test_1713(self):
        self.assertTrue(TestLexer.test('''Class x5:_{}Class _3:x{$TR62(_8,M,__:Array [Array [Int ,0B10],0x18]){Continue ;}__(_S1V,_Q_,aa9_:S_;c_:Array [String ,0x18]){} }''','''Class,x5,:,_,{,},Class,_3,:,x,{,$TR62,(,_8,,,M,,,__,:,Array,[,Array,[,Int,,,0B10,],,,0x18,],),{,Continue,;,},__,(,_S1V,,,_Q_,,,aa9_,:,S_,;,c_,:,Array,[,String,,,0x18,],),{,},},<EOF>''',101))

    def test_1714(self):
        self.assertTrue(TestLexer.test('''Class ___{Destructor (){Var H1,_u,_V,V:Array [Array [Boolean ,56],0B1_1];}Destructor (){}Val _:V0_;Q0(__T,_:_o;h0:Array [Float ,04]){}Val $s7_:String ;Val $_,$4:Boolean ;}''','''Class,___,{,Destructor,(,),{,Var,H1,,,_u,,,_V,,,V,:,Array,[,Array,[,Boolean,,,56,],,,0B11,],;,},Destructor,(,),{,},Val,_,:,V0_,;,Q0,(,__T,,,_,:,_o,;,h0,:,Array,[,Float,,,04,],),{,},Val,$s7_,:,String,;,Val,$_,,,$4,:,Boolean,;,},<EOF>''',101))

    def test_1715(self):
        self.assertTrue(TestLexer.test('''Class E{Constructor (){}Constructor (_m,_:EW80_v){}_(){Break ;}Constructor (_,_Ie:Array [Boolean ,3];_6,pC:Array [Float ,0X1_0_F1]){ {} }Var $_qb,$M:Array [Array [Array [Int ,06_2_0],0B1011111],046];}''','''Class,E,{,Constructor,(,),{,},Constructor,(,_m,,,_,:,EW80_v,),{,},_,(,),{,Break,;,},Constructor,(,_,,,_Ie,:,Array,[,Boolean,,,3,],;,_6,,,pC,:,Array,[,Float,,,0X10F1,],),{,{,},},Var,$_qb,,,$M,:,Array,[,Array,[,Array,[,Int,,,0620,],,,0B1011111,],,,046,],;,},<EOF>''',101))

    def test_1716(self):
        self.assertTrue(TestLexer.test('''Class o:_6I6{Destructor (){}Constructor (){} }Class _7_U_{Val _,$yn_28,$92l:Array [Array [Array [Array [Array [Int ,03],035],01_1],0xE],2_7];}''','''Class,o,:,_6I6,{,Destructor,(,),{,},Constructor,(,),{,},},Class,_7_U_,{,Val,_,,,$yn_28,,,$92l,:,Array,[,Array,[,Array,[,Array,[,Array,[,Int,,,03,],,,035,],,,011,],,,0xE,],,,27,],;,},<EOF>''',101))

    def test_1717(self):
        self.assertTrue(TestLexer.test('''Class q{$q(){} }Class _:C{}Class _{Var _1__14:Int ;Val f_A,eL,d,Z,$0z_,f,_,$_:Int ;}Class __:k{Constructor (X,Y9_,L_:Array [Int ,77];q:V){} }''','''Class,q,{,$q,(,),{,},},Class,_,:,C,{,},Class,_,{,Var,_1__14,:,Int,;,Val,f_A,,,eL,,,d,,,Z,,,$0z_,,,f,,,_,,,$_,:,Int,;,},Class,__,:,k,{,Constructor,(,X,,,Y9_,,,L_,:,Array,[,Int,,,77,],;,q,:,V,),{,},},<EOF>''',101))

    def test_1718(self):
        self.assertTrue(TestLexer.test('''Class J{}Class _8{Constructor (_:Array [Array [Array [Int ,0x8],0b11000],8]){}Destructor (){} }Class Ku9v{}Class ___:__9{_3o(){ {} }Var $_95:_;}Class _AW:si{}''','''Class,J,{,},Class,_8,{,Constructor,(,_,:,Array,[,Array,[,Array,[,Int,,,0x8,],,,0b11000,],,,8,],),{,},Destructor,(,),{,},},Class,Ku9v,{,},Class,___,:,__9,{,_3o,(,),{,{,},},Var,$_95,:,_,;,},Class,_AW,:,si,{,},<EOF>''',101))

    def test_1719(self):
        self.assertTrue(TestLexer.test('''Class _{}Class t8___:k{}Class _:TD{Var $3w_2_sa3,__,$c:Array [Array [Array [Array [Float ,0x41],01],0b111],0B100001];}''','''Class,_,{,},Class,t8___,:,k,{,},Class,_,:,TD,{,Var,$3w_2_sa3,,,__,,,$c,:,Array,[,Array,[,Array,[,Array,[,Float,,,0x41,],,,01,],,,0b111,],,,0B100001,],;,},<EOF>''',101))

    def test_1720(self):
        self.assertTrue(TestLexer.test('''Class _:__5e_G{}Class n:_{}Class __{}Class _4L:_f0__{}Class g{Var _,$6:String ;}Class K{Val $H:_;}Class p:_3{}Class L_3:XzG{}''','''Class,_,:,__5e_G,{,},Class,n,:,_,{,},Class,__,{,},Class,_4L,:,_f0__,{,},Class,g,{,Var,_,,,$6,:,String,;,},Class,K,{,Val,$H,:,_,;,},Class,p,:,_3,{,},Class,L_3,:,XzG,{,},<EOF>''',101))

    def test_1721(self):
        self.assertTrue(TestLexer.test('''Class _26{}Class G_:q{_I_(o,R60,_,I3:Array [Array [Array [String ,017],0B111011],07];_62,h_9_:Int ;_,V:d;_:Float ){} }''','''Class,_26,{,},Class,G_,:,q,{,_I_,(,o,,,R60,,,_,,,I3,:,Array,[,Array,[,Array,[,String,,,017,],,,0B111011,],,,07,],;,_62,,,h_9_,:,Int,;,_,,,V,:,d,;,_,:,Float,),{,},},<EOF>''',101))

    def test_1722(self):
        self.assertTrue(TestLexer.test('''Class __3_7{Var $_L,$y__,$K_b,W,$9,$A7,c,$N:Array [Array [Float ,0B1_0],0B1010001];Constructor (Y:D){}Var F_PO,$oBNG:String ;}Class p:e{}''','''Class,__3_7,{,Var,$_L,,,$y__,,,$K_b,,,W,,,$9,,,$A7,,,c,,,$N,:,Array,[,Array,[,Float,,,0B10,],,,0B1010001,],;,Constructor,(,Y,:,D,),{,},Var,F_PO,,,$oBNG,:,String,;,},Class,p,:,e,{,},<EOF>''',101))

    def test_1723(self):
        self.assertTrue(TestLexer.test('''Class C63{$_(){}Constructor (){} }Class FO{}Class bi2C:b{Var P:Array [Array [Boolean ,027],0XC];Destructor (){} }''','''Class,C63,{,$_,(,),{,},Constructor,(,),{,},},Class,FO,{,},Class,bi2C,:,b,{,Var,P,:,Array,[,Array,[,Boolean,,,027,],,,0XC,],;,Destructor,(,),{,},},<EOF>''',101))

    def test_1724(self):
        self.assertTrue(TestLexer.test('''Class p:_{}Class _{}Class p_3{}Class s{Constructor (){}Constructor (Q:f;_:_;W,_7v:Array [Array [Array [Array [Boolean ,01],0X5],026_3_2],9]){}Val $8n:Array [Array [String ,0xC],0X3];Val $Ie:Int ;}''','''Class,p,:,_,{,},Class,_,{,},Class,p_3,{,},Class,s,{,Constructor,(,),{,},Constructor,(,Q,:,f,;,_,:,_,;,W,,,_7v,:,Array,[,Array,[,Array,[,Array,[,Boolean,,,01,],,,0X5,],,,02632,],,,9,],),{,},Val,$8n,:,Array,[,Array,[,String,,,0xC,],,,0X3,],;,Val,$Ie,:,Int,;,},<EOF>''',101))

    def test_1725(self):
        self.assertTrue(TestLexer.test('''Class nJ:G7f5{}Class _{Constructor (_4,_:Array [Array [Array [Int ,06],81],4_04];_,_:_Aj;__1M:Array [Array [Boolean ,0XD],0B110011];N4,o:Int ){Continue ;} }''','''Class,nJ,:,G7f5,{,},Class,_,{,Constructor,(,_4,,,_,:,Array,[,Array,[,Array,[,Int,,,06,],,,81,],,,404,],;,_,,,_,:,_Aj,;,__1M,:,Array,[,Array,[,Boolean,,,0XD,],,,0B110011,],;,N4,,,o,:,Int,),{,Continue,;,},},<EOF>''',101))

    def test_1726(self):
        self.assertTrue(TestLexer.test('''Class _01{}Class k:l8{Destructor (){} }Class n1I___{Destructor (){Q::$z5.c5().__8()._()._();}Constructor (l:h){} }Class _4_D:f{}Class _{}''','''Class,_01,{,},Class,k,:,l8,{,Destructor,(,),{,},},Class,n1I___,{,Destructor,(,),{,Q,::,$z5,.,c5,(,),.,__8,(,),.,_,(,),.,_,(,),;,},Constructor,(,l,:,h,),{,},},Class,_4_D,:,f,{,},Class,_,{,},<EOF>''',101))

    def test_1727(self):
        self.assertTrue(TestLexer.test('''Class k_{Constructor (K8h__,Y9___,_X,_,I_,o__1:Array [Array [Array [Array [String ,287_95],07_45],03_51],056]){ {Break ;} }Var $_2S9,_8_:Array [Float ,0X1];}Class Uyh8:d57{}''','''Class,k_,{,Constructor,(,K8h__,,,Y9___,,,_X,,,_,,,I_,,,o__1,:,Array,[,Array,[,Array,[,Array,[,String,,,28795,],,,0745,],,,0351,],,,056,],),{,{,Break,;,},},Var,$_2S9,,,_8_,:,Array,[,Float,,,0X1,],;,},Class,Uyh8,:,d57,{,},<EOF>''',101))

    def test_1728(self):
        self.assertTrue(TestLexer.test('''Class _{Val K,Gcn,E:Array [Array [Array [Array [Array [Array [Float ,15],6],047],047],0B1],0x5];Constructor (){}Var __:Int ;}''','''Class,_,{,Val,K,,,Gcn,,,E,:,Array,[,Array,[,Array,[,Array,[,Array,[,Array,[,Float,,,15,],,,6,],,,047,],,,047,],,,0B1,],,,0x5,],;,Constructor,(,),{,},Var,__,:,Int,;,},<EOF>''',101))

    def test_1729(self):
        self.assertTrue(TestLexer.test('''Class I{Var $_,$5,$143:Int ;Constructor (_,___,k,_,_,e:Array [Boolean ,0402];_:Float ){} }Class W{}Class __:_{Constructor (_I26,_,__:_;_:String ){}Constructor (){ {} }}''','''Class,I,{,Var,$_,,,$5,,,$143,:,Int,;,Constructor,(,_,,,___,,,k,,,_,,,_,,,e,:,Array,[,Boolean,,,0402,],;,_,:,Float,),{,},},Class,W,{,},Class,__,:,_,{,Constructor,(,_I26,,,_,,,__,:,_,;,_,:,String,),{,},Constructor,(,),{,{,},},},<EOF>''',101))

    def test_1730(self):
        self.assertTrue(TestLexer.test('''Class _e:_53A_{}Class Jy:_{G(y,C_:Array [Float ,0xC]){} }Class _:_{}Class _m:B{Val $__q:_;Var $a:Int ;A(){Break ;} }''','''Class,_e,:,_53A_,{,},Class,Jy,:,_,{,G,(,y,,,C_,:,Array,[,Float,,,0xC,],),{,},},Class,_,:,_,{,},Class,_m,:,B,{,Val,$__q,:,_,;,Var,$a,:,Int,;,A,(,),{,Break,;,},},<EOF>''',101))

    def test_1731(self):
        self.assertTrue(TestLexer.test('''Class A{}Class z8E{}Class Rg:U{V_(I,_,_:_;N,___7,K6:Boolean ;_:Array [Array [String ,0B100001],022]){Continue ;Continue ;}Constructor (_5___,_,c,h:Int ;m,_e__pa5n1H:_){} }Class X:d__{}Class _:W{}Class _:F{}''','''Class,A,{,},Class,z8E,{,},Class,Rg,:,U,{,V_,(,I,,,_,,,_,:,_,;,N,,,___7,,,K6,:,Boolean,;,_,:,Array,[,Array,[,String,,,0B100001,],,,022,],),{,Continue,;,Continue,;,},Constructor,(,_5___,,,_,,,c,,,h,:,Int,;,m,,,_e__pa5n1H,:,_,),{,},},Class,X,:,d__,{,},Class,_,:,W,{,},Class,_,:,F,{,},<EOF>''',101))

    def test_1732(self):
        self.assertTrue(TestLexer.test('''Class __:a{$_(_2_,_26v,JpX__1__1:C;xx:Int ;Re6iw9_A_mp_,_y,_:c;_Iy:Array [Array [Int ,0xF_3],02_0];j5:Xf;_:String ){}Constructor (){} }''','''Class,__,:,a,{,$_,(,_2_,,,_26v,,,JpX__1__1,:,C,;,xx,:,Int,;,Re6iw9_A_mp_,,,_y,,,_,:,c,;,_Iy,:,Array,[,Array,[,Int,,,0xF3,],,,020,],;,j5,:,Xf,;,_,:,String,),{,},Constructor,(,),{,},},<EOF>''',101))

    def test_1733(self):
        self.assertTrue(TestLexer.test('''Class kQ{Val S,_,$3Q,B_,$9_,t23:Boolean ;}Class E5Zk4____:B{Val $6j__8:_Y;}Class _2445:_{Var $2:Array [Array [Int ,0b111010],0b111010];}''','''Class,kQ,{,Val,S,,,_,,,$3Q,,,B_,,,$9_,,,t23,:,Boolean,;,},Class,E5Zk4____,:,B,{,Val,$6j__8,:,_Y,;,},Class,_2445,:,_,{,Var,$2,:,Array,[,Array,[,Int,,,0b111010,],,,0b111010,],;,},<EOF>''',101))

    def test_1734(self):
        self.assertTrue(TestLexer.test('''Class _6:_1{Var $059_4,$d,$v_2,b8_,$0s9EJU_5:String ;Constructor (){}Val S,$_,$y05_,Y3,$_,$N,$K_7:Array [Boolean ,05_3];Var $4:Array [Array [Array [Float ,0x40],0b1],0b1_1];_(_,hr9_6_:Array [Array [Int ,48],0XE];_:Array [Array [Int ,0115],0b1_0]){} }Class z{Constructor (i4:Boolean ){} }''','''Class,_6,:,_1,{,Var,$059_4,,,$d,,,$v_2,,,b8_,,,$0s9EJU_5,:,String,;,Constructor,(,),{,},Val,S,,,$_,,,$y05_,,,Y3,,,$_,,,$N,,,$K_7,:,Array,[,Boolean,,,053,],;,Var,$4,:,Array,[,Array,[,Array,[,Float,,,0x40,],,,0b1,],,,0b11,],;,_,(,_,,,hr9_6_,:,Array,[,Array,[,Int,,,48,],,,0XE,],;,_,:,Array,[,Array,[,Int,,,0115,],,,0b10,],),{,},},Class,z,{,Constructor,(,i4,:,Boolean,),{,},},<EOF>''',101))

    def test_1735(self):
        self.assertTrue(TestLexer.test('''Class _{}Class __{Val _:Array [Array [Array [Int ,02_1],0b1],011];}Class _Mrg6Ew0XK{}Class E_5{$M_493(_:Float ){}$14__9(c,__:_o_;X:Array [String ,47]){}Val Q_3y:Array [Array [Int ,0b1],0130];}Class r{}''','''Class,_,{,},Class,__,{,Val,_,:,Array,[,Array,[,Array,[,Int,,,021,],,,0b1,],,,011,],;,},Class,_Mrg6Ew0XK,{,},Class,E_5,{,$M_493,(,_,:,Float,),{,},$14__9,(,c,,,__,:,_o_,;,X,:,Array,[,String,,,47,],),{,},Val,Q_3y,:,Array,[,Array,[,Int,,,0b1,],,,0130,],;,},Class,r,{,},<EOF>''',101))

    def test_1736(self):
        self.assertTrue(TestLexer.test('''Class __{Val $W_,$_9:Array [Array [Array [Array [Int ,0XA],32_7],040],02];V__(F:Float ;c,_,O_2_4b,_4,_N_,N:Array [Float ,02]){ {Break ;} }}Class _{}''','''Class,__,{,Val,$W_,,,$_9,:,Array,[,Array,[,Array,[,Array,[,Int,,,0XA,],,,327,],,,040,],,,02,],;,V__,(,F,:,Float,;,c,,,_,,,O_2_4b,,,_4,,,_N_,,,N,:,Array,[,Float,,,02,],),{,{,Break,;,},},},Class,_,{,},<EOF>''',101))

    def test_1737(self):
        self.assertTrue(TestLexer.test('''Class _:_{}Class Y:k_{$K(i4c:Float ;KqB____,_3v:_r;_,_:Array [Float ,03202];_,E,__,y,F:Array [String ,0x20];_,_N9A_,j:Array [Int ,0131];M:_){Val x:Array [String ,24];} }''','''Class,_,:,_,{,},Class,Y,:,k_,{,$K,(,i4c,:,Float,;,KqB____,,,_3v,:,_r,;,_,,,_,:,Array,[,Float,,,03202,],;,_,,,E,,,__,,,y,,,F,:,Array,[,String,,,0x20,],;,_,,,_N9A_,,,j,:,Array,[,Int,,,0131,],;,M,:,_,),{,Val,x,:,Array,[,String,,,24,],;,},},<EOF>''',101))

    def test_1738(self):
        self.assertTrue(TestLexer.test('''Class a:e_{}Class _{s1(_,n:Array [Boolean ,0x44];_s_263,a_:Array [Array [Int ,0B10111],100];l505y:_QL;_:Boolean ){Continue ;} }''','''Class,a,:,e_,{,},Class,_,{,s1,(,_,,,n,:,Array,[,Boolean,,,0x44,],;,_s_263,,,a_,:,Array,[,Array,[,Int,,,0B10111,],,,100,],;,l505y,:,_QL,;,_,:,Boolean,),{,Continue,;,},},<EOF>''',101))

    def test_1739(self):
        self.assertTrue(TestLexer.test('''Class _:_z{Val ___,__x_4:k;Destructor (){}Val _:Array [Array [Array [Array [Array [Boolean ,0x31],0X2A],0B110],03_51],0X2];}''','''Class,_,:,_z,{,Val,___,,,__x_4,:,k,;,Destructor,(,),{,},Val,_,:,Array,[,Array,[,Array,[,Array,[,Array,[,Boolean,,,0x31,],,,0X2A,],,,0B110,],,,0351,],,,0X2,],;,},<EOF>''',101))

    def test_1740(self):
        self.assertTrue(TestLexer.test('''Class eO_:__Lh{$QhIf 7(V8:Float ){}Val $Be,l_,__4f5:Array [Boolean ,55];Val $_,$_c:Array [Array [Int ,0x2_9],0b1];}''','''Class,eO_,:,__Lh,{,$QhIf,7,(,V8,:,Float,),{,},Val,$Be,,,l_,,,__4f5,:,Array,[,Boolean,,,55,],;,Val,$_,,,$_c,:,Array,[,Array,[,Int,,,0x29,],,,0b1,],;,},<EOF>''',101))

    def test_1741(self):
        self.assertTrue(TestLexer.test('''Class _2R:_{Constructor (C:Array [Float ,0X2B];_1,N,_1,D_:Array [Array [Array [Array [Float ,0b1100001],0x5],0X2B],05]){} }''','''Class,_2R,:,_,{,Constructor,(,C,:,Array,[,Float,,,0X2B,],;,_1,,,N,,,_1,,,D_,:,Array,[,Array,[,Array,[,Array,[,Float,,,0b1100001,],,,0x5,],,,0X2B,],,,05,],),{,},},<EOF>''',101))

    def test_1742(self):
        self.assertTrue(TestLexer.test('''Class vb{Constructor (_,Du311,L3_0:Array [Array [Array [Array [Int ,0XF_AE],0b100001],0x6],0X4];z,_,T,_5Q,gF5,_:Int ;_349YQ_L3:_){} }Class F98{Constructor (_,n:Float ;A:Array [Int ,6];R__,x_z:Float ;D,b:Boolean ){ {}Continue ;_::$g_m_u();}Constructor (I0_w,_,M_,W,uB,Ql,__T__,X024__:Int ;_1,d_:Float ){}Val $4:Y;}''','''Class,vb,{,Constructor,(,_,,,Du311,,,L3_0,:,Array,[,Array,[,Array,[,Array,[,Int,,,0XFAE,],,,0b100001,],,,0x6,],,,0X4,],;,z,,,_,,,T,,,_5Q,,,gF5,,,_,:,Int,;,_349YQ_L3,:,_,),{,},},Class,F98,{,Constructor,(,_,,,n,:,Float,;,A,:,Array,[,Int,,,6,],;,R__,,,x_z,:,Float,;,D,,,b,:,Boolean,),{,{,},Continue,;,_,::,$g_m_u,(,),;,},Constructor,(,I0_w,,,_,,,M_,,,W,,,uB,,,Ql,,,__T__,,,X024__,:,Int,;,_1,,,d_,:,Float,),{,},Val,$4,:,Y,;,},<EOF>''',101))

    def test_1743(self):
        self.assertTrue(TestLexer.test('''Class F:_I{Val tQ68c__:String ;}Class _X3__j{}Class D8{$__(h,E,c:_;_32:n){}Val _,$7:Float ;}Class a_h1s27:r7__{}Class _{}Class _4X_{}''','''Class,F,:,_I,{,Val,tQ68c__,:,String,;,},Class,_X3__j,{,},Class,D8,{,$__,(,h,,,E,,,c,:,_,;,_32,:,n,),{,},Val,_,,,$7,:,Float,;,},Class,a_h1s27,:,r7__,{,},Class,_,{,},Class,_4X_,{,},<EOF>''',101))

    def test_1744(self):
        self.assertTrue(TestLexer.test('''Class w_cc{}Class _:UA8_{Constructor (){}h(i_5:Array [Array [Int ,49],0103]){Break ;}$98(){_B8::$Pz();} }Class _O:r{}Class S_:__{}Class Ac:Z{$5(_36:String ;__3:Boolean ){} }Class _j__{}Class _:Q{}Class Q:Mj7{}Class Z{$__L(SG:__81){Return ;}Val $7016,v_4b:p;}Class V9{}Class _{Var $N:_;}''','''Class,w_cc,{,},Class,_,:,UA8_,{,Constructor,(,),{,},h,(,i_5,:,Array,[,Array,[,Int,,,49,],,,0103,],),{,Break,;,},$98,(,),{,_B8,::,$Pz,(,),;,},},Class,_O,:,r,{,},Class,S_,:,__,{,},Class,Ac,:,Z,{,$5,(,_36,:,String,;,__3,:,Boolean,),{,},},Class,_j__,{,},Class,_,:,Q,{,},Class,Q,:,Mj7,{,},Class,Z,{,$__L,(,SG,:,__81,),{,Return,;,},Val,$7016,,,v_4b,:,p,;,},Class,V9,{,},Class,_,{,Var,$N,:,_,;,},<EOF>''',101))