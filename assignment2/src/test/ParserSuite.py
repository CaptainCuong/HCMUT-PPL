import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_0(self):
        input = '''Class ___{Constructor (_,N3,R:Boolean ){Continue ;} }Class _2_227O6d:_{Val _744_,e:Int ;}Class _:H3{}Class _:_738_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 0))

    def test_1(self):
        input = '''Class _5_:__8{Constructor (s:Boolean ;bU:String ){Continue ;Return ;} }Class _1P1{$2(){Break ;}Constructor (__j:Boolean ){Return ;}Constructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1))

    def test_2(self):
        input = '''Class b1{}Class j:_{$e(_e,_1,_:Array [Array [Array [Array [Array [Array [Boolean ,0b10],03],68],68],0126],0x1D]){Continue ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 2))

    def test_3(self):
        input = '''Class e:__{Val _5,$G:Float ;Var WT,_,I:Array [Array [Array [Float ,02],0b110101],0b1];Val _,_:Array [Int ,27];}Class J_:b_{}Class _:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 3))

    def test_4(self):
        input = '''Class _:_{Destructor (){}_(CT,__Z_,_O4Uf:Array [Float ,0b1_0]){Var b,_g__,_C27:Array [Array [Array [Boolean ,0b1_0],0X3D],0B1];{} }}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 4))

    def test_5(self):
        input = '''Class L:_{Constructor (B:Array [Array [Array [String ,16],0b10101],023];XCQ32:Float ;t:String ;_,j_:Boolean ;o,_,Z:Y;_:Array [Array [Float ,0b10101],2]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 5))

    def test_6(self):
        input = '''Class _L:_3{$s(){Continue ;}Var _:Array [Array [Array [Array [Array [Array [Array [Float ,9],03],0X5_29],0X1_E_F47],9],0x3],0x8];Val $3,$H:Boolean ;}Class C:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 6))

    def test_7(self):
        input = '''Class h:RB{Destructor (){} }Class _8_S:_{$6_6(_,S,_,_:Cy;_i,tR2,T_96:f){}Destructor (){} }Class vJ9{Constructor (S,Y_95B:String ;C2:_;o:Array [String ,0B10000]){Continue ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 7))

    def test_8(self):
        input = '''Class z3_:ww{}Class r_9{$0(n5_,_:String ){}Val k__R0,$G,$5_8,$_al,TI:Array [Array [Int ,076],06_5];}Class _:__E{}Class M_0:K{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 8))

    def test_9(self):
        input = '''Class _Q{Var iF0,$K,$__,c,v:Array [Array [Array [Boolean ,63],07_3_7_7_3_6],0b110010];}Class _:_F{Constructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 9))

    def test_10(self):
        input = '''Class _69:e{Val $_,$9:JT__;Val Gs5:Boolean ;$0J(e2,y:Array [Array [Float ,05_57],051];D7_:Array [Int ,0b10_0]){ {}Return ;Continue ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 10))

    def test_11(self):
        input = '''Class _{Destructor (){}Val $6_:Array [Array [String ,073],022];Constructor (){} }Class _{}Class b:_{Var _,$w:Array [String ,0X9_A];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 11))

    def test_12(self):
        input = '''Class oG_89_:B{Constructor (){Val _:Int ;}Val $9:String =----New u();Constructor (y,sV:Array [Array [Array [Int ,011_0],06_6],5];V6:_;jr:Array [Array [Array [Int ,0110],0B1],74]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 12))

    def test_13(self):
        input = '''Class _S_:A_{}Class s1:_{Destructor (){}Destructor (){} }Class eu18{}Class __1:uK_{Constructor (_sD2___:String ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 13))

    def test_14(self):
        input = '''Class _{Constructor (K48V_:Array [Array [Array [Float ,9],0b11110],06];n_b,X21E:Boolean ){}Var $3z84_,$__7,_:Boolean ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 14))

    def test_15(self):
        input = '''Class _{}Class __0P_45{Var $_:String ;Var $_,J_:Array [Array [Array [Int ,18],0XF],0b100100];Constructor (i9____,_6:Int ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 15))

    def test_16(self):
        input = '''Class g:C{}Class d:N5w{Var L,_I205,_,$_1k__96,__:String ;}Class _f:F{}Class _F:P__{Constructor (hh9,__,M28_6:Int ;hTJ:_){Break ;Break ;}Val H:String ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 16))

    def test_17(self):
        input = '''Class _:b{Destructor (){Break ;}Val g,$M,X:Array [Array [Array [Int ,0X6],0B1_11],0xF];Destructor (){ {Break ;} }}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 17))

    def test_18(self):
        input = '''Class _:_s_{Val $_,$V_2,R_t,__Q_8,$2:Array [Array [Int ,851_5],80];}Class U:W{__S(p9_,__m5k:Boolean ){Continue ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 18))

    def test_19(self):
        input = '''Class _{}Class p:_{}Class A_{g_89_1_(Z:F5){ {} }}Class _:_{Val __,Yk:Int ;Constructor (){__2::$_F9();} }Class _{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 19))

    def test_20(self):
        input = '''Class K{$_(u,V,_:Float ;__74,__:Float ;_F:String ;PF:String ){}Destructor (){}Destructor (){ {Break ;}{} }Destructor (){} }Class c:A{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 20))

    def test_21(self):
        input = '''Class M{Destructor (){}Constructor (_V,_:Array [Array [Array [Array [Array [Array [Float ,0B1001],0B1],0B1001],01],7],0134]){}Val $S,p_,r,$_60,_:Boolean ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 21))

    def test_22(self):
        input = '''Class A{}Class _7:_{$0_6_i(K:Array [Boolean ,9_64];_:String ;t,K05:Int ;S0_3:Int ;_:Array [Array [String ,0XB_42_5_5],0XD]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 22))

    def test_23(self):
        input = '''Class N:T3{Val $z0,$_X:Array [Array [Int ,0x45],0x45];}Class _:k{Val H:Array [Int ,0x45];Destructor (){}$_(_k:String ;M:String ;VjF18,A_:String ;_,Nm:a1g_6;i:l55B;y,_:String ;Yg:String ;b,_:__7C;_:Array [Array [Int ,066],0X46];_,_,p,A,E:Array [Array [Array [Int ,051],05],0XA_B];D:Float ;_:Float ){}Constructor (){}Constructor (L,Ab,_r:Array [Array [Array [Int ,9_5_6_2_6_1_9],2],9_2_3_0785_4_68]){}Val o:_E___4;}Class J{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 23))

    def test_24(self):
        input = '''Class _{Val _,O,$58__:Array [String ,0117];$a_(M_:_;_:s_;moOq,n,L:U){}Constructor (l9:Array [Array [Array [Array [Array [Int ,0B11000],02703_61_66_60],59],0x56],0xD];_9:Array [Array [Float ,8_6],0B11000]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 24))

    def test_25(self):
        input = '''Class _:B4{Constructor (_p:Boolean ;t,F:Array [Float ,5_7]){} }Class _:_{Constructor (_0_:Boolean ;B2,_:Float ;_V:g;v,_5_,Y,_,_,___,A0_,L,_:Int ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 25))

    def test_26(self):
        input = '''Class I{}Class _:P{Var _:String ;Destructor (){}Var $_S:Array [Int ,0103];Var ___T3,$___6,q_z_0_:vES;Var Z2:Array [Int ,0x5];$__(){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 26))

    def test_27(self):
        input = '''Class _8{$2(){Var __:Array [Boolean ,0b1_1];Var W,D:Array [Array [Array [Array [Boolean ,8],034],0XB_6],0XE];}Val $3,__exp9,_3_,_,o,_:Array [Int ,0b10];}Class ua_8{Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 27))

    def test_28(self):
        input = '''Class _m__:_{Destructor (){} }Class _9:__8{}Class e60_86I_U_q2:Z{Var $i4P1:Array [String ,87];}Class mh:_xp520{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 28))

    def test_29(self):
        input = '''Class J33___7p8_Kn__71{Constructor (O05,__e:Array [Array [Array [Array [Array [Array [Array [Int ,0101],0X6_EF],0x2],72],0x23],0X8],6_43]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 29))

    def test_30(self):
        input = '''Class _:e_h9__q_{}Class _:l{Constructor (_,_y_ZH,__,_:_;W,_:_9){}Var $n6,$_,$_:Array [Array [Array [Array [Array [Array [Float ,0X2],0x4_B_3],0B111011],0B111011],35],07];Destructor (){ {}Return ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 30))

    def test_31(self):
        input = '''Class __:__3{Constructor (){} }Class _:RK_Z{}Class _ABH{}Class B:_M{}Class xu40V{}Class W:i6_{Constructor (_1,_9c4C,_:_n95;Qc,_:B;K2K,n39Q_We:__){}Var $_A1,$_,$E_,__:Def;}Class _:__{}Class _:_03w58{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 31))

    def test_32(self):
        input = '''Class K5:_{Destructor (){}Constructor (___:P_){} }Class _{Constructor (_:Array [Float ,30_88];_C_2_,_w__:Boolean ){} }Class _{}Class __:_{Var $15_:Float ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 32))

    def test_33(self):
        input = '''Class Ndz:_{}Class rP{Constructor (_:Float ;_:Array [Array [Boolean ,93],03];_6,j888:_;k:_){Return ;{}Var t,zw:Array [Boolean ,0x8];} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 33))

    def test_34(self):
        input = '''Class _{Constructor (){}l_(){}nL(_:x){Var x2:Array [Array [Float ,0B110101],0x4D];}Constructor (){ {} }}Class _az{}Class _a4:S{Constructor (____,a:Array [Array [String ,02],0b1_1_0];_05:U){} }Class _3_6N__6{}Class gP345{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 34))

    def test_35(self):
        input = '''Class ___:P5{}Class T:L{}Class ___X:_{Var __58,$_0_,$_:Array [Array [Array [Array [String ,0X9],0b111001],9_22_62],0B1_1_01];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 35))

    def test_36(self):
        input = '''Class _JCJ:Q0{Var Qw_:Boolean ;Val j:Array [Array [Array [Float ,7],68],68];}Class B:P327{Val $TV,Z:Array [Array [String ,68],0b10];Val _:Array [String ,68];Var _,_0:Array [Array [Boolean ,0130],01_3_25_0];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 36))

    def test_37(self):
        input = '''Class t_:X{Var $9h:N;}Class _:Q6r{f__(){ {Break ;} }Val $1q4,_1,$7,p,_,_n:Array [Boolean ,067];Destructor (){}Constructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 37))

    def test_38(self):
        input = '''Class __2{Var $6o_78_,Y,$_:Array [Array [Float ,01_5],0x4D];Constructor (h:Boolean ;n,L,M,_A,_i__,MT:Array [Array [Int ,0x4D],0xE];m_5ue,j_2:Array [Float ,0B111100];TK:Array [Array [Array [Float ,0x9],0X27],42];z,_,_u_a3:__){}Var _:_5_O;Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 38))

    def test_39(self):
        input = '''Class _:_7{$6(_:x10;L,D70_,_t,_,__t,g_:Array [Array [Array [Array [Array [String ,056],0b1001111],0B111],0b1001111],15]){ {} }}Class OSu:s{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 39))

    def test_40(self):
        input = '''Class ___49H:DZ{$__99(kd_S,_:String ;d,_,_:Array [Array [Array [Array [Boolean ,4],0b110011],0X1B],0B111110];M27,_6_m_:Boolean ;_t:String ){Continue ;Val _N,_:I6_76;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 40))

    def test_41(self):
        input = '''Class _{}Class M_8:J2P{G(_D__U8,f_Q68_J:Array [Array [Boolean ,066],0b1];U:J){} }Class p__:_K{_8(U,_:Array [String ,0b1]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 41))

    def test_42(self):
        input = '''Class _{Var $918:t;Var $F,H_q__:Int ;Constructor (__6p:String ){} }Class ___{Var $t_,_,$86,$6,N73__u1_:String ;Val _,r976_,g97_,$6_:Float ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 42))

    def test_43(self):
        input = '''Class xV{$_066_(){}_(){} }Class B{}Class _{Constructor (X:Array [Int ,0x24];o__:Array [Array [Array [Float ,046],04_3_5_5],07716];_g4:String ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 43))

    def test_44(self):
        input = '''Class xlU:t{}Class __{Destructor (){} }Class __4_{Var _,$m,$_:Array [Array [String ,22],05];Var $a:Array [Array [String ,0X34],013];a_(U,ww:M;_:Array [Int ,8]){} }Class j{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 44))

    def test_45(self):
        input = '''Class HL{Destructor (){} }Class _:_{}Class E:_{}Class _D3{Constructor (_9,t,_,_aO5r:k;M4,K,_:Boolean ;_:Array [Array [Float ,0x1E],5];R:String ){}b__9(_F__4_,n_5:Int ){Continue ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 45))

    def test_46(self):
        input = '''Class p:_{}Class a{}Class f_:_T{Val $mJ__:String ;}Class ___:Z_{}Class D{}Class _{Val H0N1,E:_;Constructor (){} }Class _{Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 46))

    def test_47(self):
        input = '''Class _{Var $_g,_70E:Float ;Val $h5e,$_408B,_,r,a_0:Array [Array [Array [Array [Array [Array [Array [Array [Array [Array [Float ,0b101_1],022],022],01_57_1],0B10_0_01_00],5_7],021_1_76],2],0X60],25];}Class o{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 47))

    def test_48(self):
        input = '''Class _:_{}Class _{__f_(){}Val NV:Array [Boolean ,0b1];Destructor (){}Constructor (){Continue ;} }Class b_:m_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 48))

    def test_49(self):
        input = '''Class __G90_:_{}Class _:_b{}Class _8{Var $__:Array [Array [Boolean ,39],0x3AB_8];}Class M19{Constructor (){Continue ;}Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 49))

    def test_50(self):
        input = '''Class _:_61S{}Class _:K{Var $B,_:xqf__;Constructor (_3_M8,V8_:_Z_0_;jE_:Array [Array [Array [Array [String ,21],0b1000011],6_9],056];_:Boolean ){} }Class H9_:l_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 50))

    def test_51(self):
        input = '''Class M:a{}Class _{Constructor (){__Z::$6();{}f__u4_6_g2::$IU2_();}Var $E,Ht:Array [Float ,0x44];Constructor (_d:Array [Array [Array [Boolean ,76],03],0xC];_,__:_8Zq){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 51))

    def test_52(self):
        input = '''Class _:_5{}Class Z{Destructor (){}_1_XH(_,_a8:Array [String ,0X23]){Return ;Val _y,__,k:d1K9623;Var _5P:Int ;Break ;O::$T._.L__.__();} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 52))

    def test_53(self):
        input = '''Class t{Val H7:String ;Val SD__,C:_K_;Constructor (__:Array [Float ,0B1_1]){Val _:Array [Array [String ,0X2D],0b1000101];Var p,N:h5RR;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 53))

    def test_54(self):
        input = '''Class __:F_V2{Constructor (a__,xc,KX:Array [Array [String ,0B100011],0B100011]){}$2(){}Constructor (){}Destructor (){} }Class OO:D{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 54))

    def test_55(self):
        input = '''Class f2:Zl3{}Class W{d28(U3:G;U,_,q,p,UF:Array [Int ,0X4];O,P,a,py,A_:Array [Array [Array [Array [Array [Array [Boolean ,0b1],0X4],0xF],0xF],0XF_3_F],0B1]){} }Class yA{Destructor (){} }Class _U:__{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 55))

    def test_56(self):
        input = '''Class MA{Destructor (){} }Class _:_GV4{Val Dh,$__:Array [Array [Array [Array [Array [Int ,037],037],23],7],2_6];Val _:Int ;Destructor (){}Var I,U,$w,_2,Pc_jIV6_,$2:Array [Array [String ,23],037];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 56))

    def test_57(self):
        input = '''Class U:P6{}Class _:_L{}Class C:__8V_D_7_74_p_qi9{$_(__,q__,A_c_0,f:Array [Array [Boolean ,05_7],020];_,_,xZ:Array [Array [Int ,05],020];m,_,K:Array [Boolean ,0X7_9_0];__qw5:Float ;__,_:Int ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 57))

    def test_58(self):
        input = '''Class R_{Val $6,qG:_;}Class _{}Class _{Val $S,$i:Array [String ,42];H6_K_(_8:Array [Array [Array [Int ,0X5C],07],047]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 58))

    def test_59(self):
        input = '''Class _:x{}Class _75:kj{$0(_:Array [Array [Array [Array [String ,6_9],0x51],6],016];_:Boolean ;___:Array [Array [Array [Array [Boolean ,0X43],0XF],0x51],05];_3:__C){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 59))

    def test_60(self):
        input = '''Class ECh:_8{}Class i_:f{Var $_1ie7e,$1,$9,c,_:Array [String ,54];Val _:Array [Boolean ,0B10];}Class a:uU{}Class __6{Constructor (){}Destructor (){}Val _:Qz;}Class _1S{}Class i:_{Val __0,s_,H,$6:Int ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 60))

    def test_61(self):
        input = '''Class _Ie8_U:__K{}Class _2:__{Constructor (_h,__:Int ;t:Array [Array [Array [String ,0B1111],0x6],07_2];P,_Sk:Boolean ;ZQ,W_:A;_2:x){ {} }}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 61))

    def test_62(self):
        input = '''Class _{Var $qx2,$___k_,E:Array [Array [Int ,9],06];}Class Q57{Var $IK69__,_,$_,M_,$76:C6;Var Q,$b,$X:Array [Boolean ,0B1011101];}Class X__:_E{}Class _C_o{Val $v:p_;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 62))

    def test_63(self):
        input = '''Class _:k{Var _9,__:Array [Array [Boolean ,0XE_A1_A_F_0],0X37];Val _:s;Var $_72_:w_44;Val $_2,$W0u,P,__,$__,$9o:t;}Class f{Val T,m:I;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 63))

    def test_64(self):
        input = '''Class o:Y{$_(E:String ;t:I;M:Array [String ,0x3];W7,m:_;Y:Array [Boolean ,0B1];_,B,_27:Array [Array [Int ,056],0b1];d,_:Boolean ;Z:t;I,e6_0,F1__:Boolean ;____n:__v37j056a;_,br:__;_6_,t:_){}Var _:_;Q(_:L;S_,c:String ;S,_,W,p_0z,r:Array [Array [Float ,8],31]){ {Continue ;}Continue ;Return ;} }Class C{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 64))

    def test_65(self):
        input = '''Class Mk:Iek{Var $C,$87__:H;$7_(_xe:Array [Boolean ,72_9]){}Destructor (){}H7C(cK_,_,_9,O5,RHif,__:_z2__n9_){}Destructor (){Break ;{ {} }Continue ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 65))

    def test_66(self):
        input = '''Class _l3_{$e(y,_,_,W,_,P,_J__:Array [Int ,0x89_5];YN:Int ;C,_,_,J_8__g86_:Array [Int ,26]){}$4m8(J:Array [Array [String ,5_7],04];S_:Int ;f0,__:String ;xe:String ;_,_irv:Boolean ){__::$_().__37_e_().p.l__.n.__.Phb()._7260___()._.F().B4Z();} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 66))

    def test_67(self):
        input = '''Class D0f{Val _,$k,T:Array [Array [Array [Int ,34],0B10001],0X37];Constructor (_1,_,_4_:Array [Array [Int ,01],34]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 67))

    def test_68(self):
        input = '''Class _:Q{Var I,_1u,_22:Array [Array [Float ,83],0XC];Destructor (){Continue ;}$Q__Z61_(L,l,W,_J_,_,G,h,h_,H1,u:String ){} }Class U0D{Val fD:_;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 68))

    def test_69(self):
        input = '''Class f:k{Constructor (_zX,__8,_0a:v9_5__;h:Int ;Y_Rg,_n:__;bI:String ;_:Array [Int ,0b1_111]){} }Class _M:_2{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 69))

    def test_70(self):
        input = '''Class _{}Class iX:v{}Class X50{Var c___:Q67R3;Constructor (M,_:Int ;__,H:Float ;_2k,c,_,_t,zP,_0:n;__:Float ;_,D9,D:Array [Int ,0B1];C,x:Float ;G_5H,a,w,_B,a:Int ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 70))

    def test_71(self):
        input = '''Class L:_K{}Class _{Destructor (){} }Class _I9:_t_{Val dR1:Array [Array [Array [Array [Array [Array [Array [Array [Array [String ,0B1_01],0b1],0X19],0X3],85],0x9_99],0B1],85],85];}Class n8{}Class __3J{}Class y:_9_{Var k:Boolean ;Constructor (){Var O0_3GhW_78:Float ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 71))

    def test_72(self):
        input = '''Class __:Z{}Class ___DGqA3{Constructor (){}Val sHx_:Array [Boolean ,0B1];Constructor (){}Constructor (){Break ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 72))

    def test_73(self):
        input = '''Class ____:x991{$4(_,_,i_,__67,s:String ;yM,_,_7_k:Int ;_:Array [Boolean ,016];_,g:Boolean ){} }Class _:__9_{}Class u:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 73))

    def test_74(self):
        input = '''Class _7_{Var $_p44,$n3,$S,_3_,_:Array [Array [Array [Array [Array [Array [Boolean ,0X3_3],05_6_5],0b1000010],0X6],3],99];Destructor (){} }Class _199{}Class O{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 74))

    def test_75(self):
        input = '''Class S_W{Destructor (){}Val $2M_,___,_,$_4_:Y7_e;}Class o:___{}Class _:_{Var $U:String ;}Class _j:n{Constructor (){} }Class __:___{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 75))

    def test_76(self):
        input = '''Class _M_{Destructor (){Var h,r_,_M9,_I,__:String ;Break ;} }Class __{$__(_:Array [Array [Array [String ,0B10_10],8_8_0],0X4_8]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 76))

    def test_77(self):
        input = '''Class _:_R{CZ8jp8(_,_:_;_:Array [Array [Array [Array [Boolean ,8],03],0B110100],0B1];_:Array [Array [Int ,03],03];L7i5__,D,_,_,i:___;__:Int ;__2_,y_C_:Array [Int ,03];___,F,W:Array [Boolean ,54];Y,E,PZ,J:_){} }Class r_:Da{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 77))

    def test_78(self):
        input = '''Class _:_{Constructor (){}Val $1,$__,J_:Array [Int ,6];$_(w:Array [String ,0105];_,___:Array [Boolean ,0b1_1]){}Var $5,J_:String ;Var Qs9_:Int ;Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 78))

    def test_79(self):
        input = '''Class _:_fH{Val s8_,$_52:__;}Class _{Constructor (_:_){Break ;}$Yu2Ix_4(){}Var _,C_a:Array [Array [Array [String ,0B1],0xE_A],749];}Class _{Val $_n,_:Float ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 79))

    def test_80(self):
        input = '''Class _:_9_{Constructor (_,y,_,s_7,__,Zm4__:Int ;_,T:Int ;Y_,_8_:Float ;__cA,_:_;g:Cwu7;q,__9A4U_L7_:F_){Break ;Break ;} }Class MS6g1du130{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 80))

    def test_81(self):
        input = '''Class _0Q:Q{}Class _{Destructor (){} }Class _{__(_,_C,_,_F:String ;x1:Array [Array [Array [Array [Array [Array [Float ,0X63],4],0x1F],0x1F],31],0B1000010]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 81))

    def test_82(self):
        input = '''Class A_h1_1r7:__{$5(){} }Class V:_{}Class H:__1s{$482(R:__;_:Array [Array [Boolean ,0b101],96];X,E,D:Int ;_:f){Break ;Return ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 82))

    def test_83(self):
        input = '''Class I:m{}Class _:_{}Class __7{Val T_61:Array [Array [Boolean ,43],77494_89];}Class _:__{Var $p_:String ;Val $26_3,$R5,$I_7_,$_,_3R4ISm:_8b8_448;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 83))

    def test_84(self):
        input = '''Class l2:q{Var $2_4_,$y86,_4:Array [String ,073];Constructor (t:Array [Array [Boolean ,073],0x63]){Continue ;Val N___a,_,U2,Y_,___,_9:String ;Break ;Val h1,b:_9;} }Class q{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 84))

    def test_85(self):
        input = '''Class o_:_{Var k:Array [Int ,0B1_1];q2(){}$_7_(v:r35;D:Array [Array [Array [Array [Array [Array [Float ,04],0X1E],0x5D],9],0b1_0],0b101101];_:u){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 85))

    def test_86(self):
        input = '''Class L_5:__Y___{_(_,V:Float ;_8,ga,_:Array [Array [Int ,4_9],83]){} }Class T_67:_{}Class _{}Class R_:k{Constructor (_b:z;_I_,k,__4:Int ;q,rC_,__,s_3,R:Array [Float ,0X2];A:__){Continue ;}$7(){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 86))

    def test_87(self):
        input = '''Class _:_7{Constructor (Nv4,d:Array [Boolean ,011];W_c,_3,NR,V:Boolean ){Continue ;Break ;} }Class a0{Destructor (){} }Class _33_f:L{}Class __M:n7{Destructor (){Break ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 87))

    def test_88(self):
        input = '''Class _:t8{}Class z_{Destructor (){} }Class _zb{Val $Qn,$_,_,K_,_:_p;Var $11W,$0,$_:Array [Float ,0B1];}Class _:_X{Constructor (){} }Class H_{Var $_s0,$u,_:Array [Array [Array [String ,022],0B1],0xB5_2_1_14];}Class __:f_72_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 88))

    def test_89(self):
        input = '''Class S:____{Constructor (F9:Array [Float ,03];__:String ;_:g;_,_,_28_x,_,p,_:p_;xT_,n,_H5_i,_:Int ){}Destructor (){Continue ;} }Class _{Var s,_,X_:C;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 89))

    def test_90(self):
        input = '''Class e__9_{Constructor (_:_){Break ;} }Class _n{Val $7Z:Float ;Destructor (){}Destructor (){}Constructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 90))

    def test_91(self):
        input = '''Class q_g{Val _3c,$3:Array [Array [Array [Array [Array [Array [Array [Array [Boolean ,0b1],03_01],0b11],03],22],0143],0364],9_64_79];}Class _:_{Destructor (){}___(O7,UJ:String ){}$_(){} }Class _{}Class _{bgF(_:_;f:Boolean ){Break ;} }Class PZm_4:ZA_G{}Class _:L_{_(){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 91))

    def test_92(self):
        input = '''Class O__3_2{}Class _W_{Val $21,C:Array [Array [Array [String ,0B1011000],0xD_6],62];}Class n{Constructor (a4,w5:l5){} }Class kx_:__{}Class er:_{Constructor (_:_P){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 92))

    def test_93(self):
        input = '''Class _{}Class CR:d4{}Class i:z{Var _E:Array [String ,012];Var _,$d,$_p,_,$K:Array [Array [String ,012],53];}Class _:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 93))

    def test_94(self):
        input = '''Class _460_be1:_t{}Class _l_{}Class Og_L:K{$__(){}___0Q(y9M7,n,Y:Boolean ;P,_n74d:O4e_;P7_56,_G,Z:Array [Array [Array [Boolean ,3],03],89];_:Array [Array [Boolean ,0B1],0x58];O_9,_5:Array [Array [String ,0B100101],0B100101]){}Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 94))

    def test_95(self):
        input = '''Class __{$z(Ui:V0;f:_1;_,_,_,AM6n06Q_:Array [Boolean ,2]){} }Class _Y_3P:_D_{$Y(){}Var L_:Array [Array [Array [Float ,0b101101],0B1_0_1],0104];Constructor (__:Array [Array [Array [Array [Array [Float ,0b101101],29],03_2],07],0b1_1_0];_,_C,_:O5b){New H().rV();}Var V1,D,Nr,$_2,R:Array [Array [String ,0B1],02];_(p:Array [Array [Array [Array [Float ,01],0XF],29],0B100010];_,__9v,v7,h_:Array [Array [Float ,0104],0104]){} }Class e:d{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 95))

    def test_96(self):
        input = '''Class __{Constructor (b8,q_3__,oy6:Array [Array [Array [Int ,93],0b1000100],93];_,f:Array [Array [Int ,0B100010],0xD];OM:Array [Boolean ,0B1_1111]){Break ;{} }}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 96))

    def test_97(self):
        input = '''Class _{Var $i:y_35_I;Var $_,y:Float ;Var $_6U:Array [Float ,54];}Class d{}Class __{Var $H_,_9:_;}Class _:__{}Class n9:z{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 97))

    def test_98(self):
        input = '''Class b_:_{}Class L{Constructor (_4t:hj;X,_:J){__::$_._();} }Class B{}Class k:q{}Class _{}Class n:__2_{Destructor (){} }Class Z_g{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 98))

    def test_99(self):
        input = '''Class __5:k{}Class r__{Destructor (){} }Class y{Var f_:Float ;}Class _:_9__{}Class _7{$41(_,wH,_3L_,_:Array [Array [Array [Int ,0B1_11_0_1_0],8],0x11]){}u_(P,_:_){} }Class U_i_5:S{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 99))

    def test_100(self):
        input = '''Class _8:Qs{}Class M:s_1{Constructor (r5,__,P,qT_:String ;_,_,C:Array [Float ,0X5];_f:L;v:PB;_,_,h,j,_M:Array [Array [Array [Boolean ,0B101110],0b1010111],0b1010111]){} }Class S{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 100))

    def test_101(self):
        input = '''Class _{Val _0,$i,_GO,_o,$___n,w,$F_:Array [Array [Boolean ,0B101111],0x48];Var $5:Array [Array [String ,2_0_4_4_4_8_4],060];}Class _7{}Class _79:_4z{Val _,_Z4_,$y3,y,$2:npJ_;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 101))

    def test_102(self):
        input = '''Class _8h_K9{}Class __{_Y_(HO,J__J:Int ;_,O,_:V_;P,_,_,I,_,_:Float ;_:Array [String ,014]){Continue ;} }Class d:U{}Class _{Val $Z:Float ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 102))

    def test_103(self):
        input = '''Class _7:i__{Val $_:Array [Array [Boolean ,05],0141];C(I_,_5:Array [Array [Int ,0b1],0141]){}Constructor (){} }Class o:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 103))

    def test_104(self):
        input = '''Class _h1{$0(q_,QKY,m5,_,_,_,_94:Array [Boolean ,6476_921];_:String ;rl,b0:Int ;__2_e,e:Array [Array [Array [Array [String ,07],0133],0133],0133];w,_4,_:Array [Array [Array [String ,0XF345],0B1000000],0133]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 104))

    def test_105(self):
        input = '''Class _:_{Var _2B_:Boolean ;}Class I_{Destructor (){} }Class AB{}Class _{Constructor (B:Int ){}Val A:Boolean ;Constructor (){}$_(){}Var $X_:Array [Array [Boolean ,0XF3],0137];}Class __:cVp{_(v,k_w:_q){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 105))

    def test_106(self):
        input = '''Class __{__(y:Array [Boolean ,0B1011100];m:Int ){}Val $E:vu;Var n7SV,ab_9_,$l_i,$js,_:Array [Boolean ,0B1];$f2X(_fR,l:o){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 106))

    def test_107(self):
        input = '''Class I:__{Val $A__,C,$W5_,$v_,$R,$0,__:Float ;}Class _:_{}Class N6{Val $_1,$3,$31_0,$3,_,_,gD,$_,$_sP:___;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 107))

    def test_108(self):
        input = '''Class __:V_{Constructor (_5TP_0,L,_:O;_:String ;M:Float ;_t6C5e,__3:_;__Zg:Array [Array [Array [Array [Array [Int ,40],40],05],0x2A],0X17];E,P,_s:Int ){} }Class w:__435{}Class _:_{}Class _6:_x{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 108))

    def test_109(self):
        input = '''Class w{W(){}Destructor (){Break ;Continue ;}Destructor (){Return ;Continue ;Return ;}Constructor (){Break ;} }Class J7:_0_{b_HW(){}Val $E:Array [Array [Boolean ,0130],3_9];}Class s{Constructor (){} }Class _:sX{$6y8(){} }Class _{Bo(){Val _9,_6,i,__:Array [Boolean ,0130];}Var $5K__a_l:String ;_(SO4_:Float ;x8:String ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 109))

    def test_110(self):
        input = '''Class x:_6o{}Class Av{Var qG:Array [Array [String ,0X2F],0x8]=fc8::$G[----m67QUKUH::$G._50o.W]&&_::$1;Val $7,$5XC,$fRr_,$P_,$_N:x_;__e(_,_s:Float ){Var _,_K:String ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 110))

    def test_111(self):
        input = '''Class I:_0{Val $_:ZH;}Class _{Val U:Array [Array [Array [Array [Array [Array [Array [Boolean ,06],06],11],0x41],0B101],0x41],11];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 111))

    def test_112(self):
        input = '''Class G{Val _,$_62,$9:Array [String ,0b1];}Class Q:X_6{Constructor (__:String ){}Constructor (o4a,n:___;_,__,E9Z1_:Array [String ,43]){ {} }Val V,_,$_,$L78:String ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 112))

    def test_113(self):
        input = '''Class _:_{Val J_,$747:Array [Array [Array [Array [Boolean ,4],6],0x2C],0b11101];}Class Tr___:O_0{Constructor (G:Int ){}$_(){Break ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 113))

    def test_114(self):
        input = '''Class _:dy{Constructor (p:Array [Array [Array [Array [Int ,05],0X4E],044],0x4F];_,O_F:Array [Boolean ,0x4F];__:String ){} }Class _0{}Class h1:n_6W{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 114))

    def test_115(self):
        input = '''Class _z{$_(O,n,_,C,_,_HW,_:Array [Boolean ,0X19]){}_j(T:K;_,C,_4_537x:Array [Array [Int ,076],076]){Break ;D::$J_e__();}$5_L(){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 115))

    def test_116(self):
        input = '''Class _n{Destructor (){}$Y_(){}c68(_:Array [Array [Int ,0X56],0x54];P,tr__,_:Float ;r_:Int ){}Val ___0:_;}Class _1F:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 116))

    def test_117(self):
        input = '''Class B{Val $j,$D_:__;Var T5,$_3:Int ;}Class _{Constructor (v:Array [Array [Array [String ,4_2_5],0x58],02_0];nR6:String ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 117))

    def test_118(self):
        input = '''Class R_{Val _,$_,z:Boolean ;Val bC,$_,N:Array [Float ,05_0];Var $t_A_32_:Array [Array [Boolean ,05],03_12_1];Val $_,ec_:Array [Array [Float ,0b11],0x45];Constructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 118))

    def test_119(self):
        input = '''Class CN{Constructor (A:_;U:Array [Boolean ,0b1];__W,H,_A5K:Array [Float ,7];_c__:Boolean ;_,j6,_,_,_M:Array [Array [String ,0x22],40];o:Int ){}Constructor (_5M_,_,_:Array [String ,0b1_1]){}Constructor (J3U,_7:_){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 119))

    def test_120(self):
        input = '''Class _{Constructor (){}Constructor (__,e_,A:hypi_y_;__:Boolean ;_,D:e;_,_,ZD:Array [Boolean ,0X7]){}Val $H4:Boolean ;Val $Zr5_:Boolean ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 120))

    def test_121(self):
        input = '''Class _{}Class r:D{Constructor (A5:String ;_:Array [Array [Float ,0B10110],0b10_1];Z:Float ;i_1:Boolean ;G,K,D_:Int ){}__(){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 121))

    def test_122(self):
        input = '''Class _:_{Var $__,$X:Float ;_(_r:Float ){} }Class K{}Class D:_{$_94(){Break ;} }Class _{}Class F1r{A(_,Q_:V){}Var _:i__;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 122))

    def test_123(self):
        input = '''Class _{$_(_8t,_:Array [String ,51]){} }Class __{Var l:Array [Array [Array [Boolean ,0B1100],4_4_7],51];}Class X0:R{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 123))

    def test_124(self):
        input = '''Class _r2:_773{}Class hu9_:y_{Destructor (){}Val $w,_E,$k:Array [Array [Array [Float ,0X5A],49],0x6_21_F0_DA];}Class __:z{}Class _PB7w:__{}Class _6{}Class __{}Class _{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 124))

    def test_125(self):
        input = '''Class w1{}Class _:_D__{Val _:mu_2tA;$2(_S,e,C:Array [Array [Array [Array [Array [Array [Int ,0x5],3],0120],02],0X4D],0b1];_:_;u0t,m:_;y:Int ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 125))

    def test_126(self):
        input = '''Class s:__{}Class O2{Var OC,$_8:Array [Array [Array [Array [Array [Array [Boolean ,0x8],0b1_0],2],04_07_3],0B1_00],03_2];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 126))

    def test_127(self):
        input = '''Class v:_{Val H,$_:Array [Array [Array [Array [Array [Array [Float ,072],0b1100],0x1B],79],79],03_4];}Class x8_t:i{}Class F{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 127))

    def test_128(self):
        input = '''Class _2Z:s_a{}Class b7_:W_{}Class _5:o{$44FS1(){}Val $_:Array [Int ,0B1];Val tW,$5:Float ;Val $_,$h0,$7s,$2u:_3;$E(){Var __nw,L:Array [Array [Int ,0X7],0b1_0];} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 128))

    def test_129(self):
        input = '''Class _:c{}Class _1{$_(){}Val $_,j,$96,$_,$9_,U:_m;}Class U__:_5{Constructor (z,ci_,h:__){} }Class O5{}Class S:p{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 129))

    def test_130(self):
        input = '''Class _{Var $5_O,$_4C:Array [Array [Array [Array [Array [Float ,066],7_77_8],0b100001],9],04_4];Var $_4:Array [String ,02_0];}Class _{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 130))

    def test_131(self):
        input = '''Class _:_6{$_(K__:String ;a_,_,T_,TV:Int ;_,p,_,_h,z,x,d_,F:Float ;N4,nx,_,K,D4uaD,__553,z:Boolean ){ {}Return ;} }Class _T:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 131))

    def test_132(self):
        input = '''Class X:s_{Constructor (_81:Array [Array [Int ,0xBC4],07_4]){}Constructor (_,iz:K_;_g,__:w;_:Array [Int ,0x16]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 132))

    def test_133(self):
        input = '''Class _{Var $RS6,__8ox4_,$__02X:Array [Boolean ,011];Constructor (T__F,zH8_:Array [Int ,0b1000];j___2_9l,_U,_p,_8_y5,l0S_3_:ib;C_B,b,F,_:Boolean ;_G_:D_6){}Val $0B,$__,$_p,$o0,$8,$___8:z;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 133))

    def test_134(self):
        input = '''Class _:__{$O(__,W,b,g__,_,_:Array [Array [Array [Array [Boolean ,0X5_5],0XA2_B_C7_4C0],025],025];_,R,_4:fN667;I2w:Float ;_:qG;_8_h:Boolean ){} }Class F:v{$1dH(){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 134))

    def test_135(self):
        input = '''Class _{Constructor (){} }Class P{}Class x07{Constructor (E:r;__4_N7_:Mm2;h:Array [String ,63];L6,_,_HA_7:n;_,_:Int ;F:Boolean ;h,QN:Array [Array [Array [Array [Int ,0B101001],033],4],0x7]){} }Class k_3d8{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 135))

    def test_136(self):
        input = '''Class A{}Class _G{}Class _5{}Class _8:v__{$_(Q,Q,_,Q_wz:F6n){}Val $_S,$LJ_3n_,Z:Array [Array [Array [Boolean ,0XB8],0B110100],057];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 136))

    def test_137(self):
        input = '''Class _{Val _:Array [Array [Float ,2],0x2E];$9_(_,D_,z_:h;_:no29_;_:Array [Array [Array [Array [Boolean ,11],5],0b1_1_1],05];_:String ){Rg_g::$1_1();} }Class _{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 137))

    def test_138(self):
        input = '''Class __D:_i_{}Class g52{}Class _i_:_{$_(_,Twz,w,uM:w;_4:Array [Array [Array [Array [Array [Int ,0B1],9_0],0b1_0],072],9]){} }Class _{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 138))

    def test_139(self):
        input = '''Class t:_C{Constructor (V0r:h;_:Array [Array [Array [Array [Boolean ,07],0b11],011],7971];y,K:Array [Array [Boolean ,03_51_1],060_40244];_:Float ;g:L_){Break ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 139))

    def test_140(self):
        input = '''Class __u:F{}Class _0__h9A:_u_{Val $__Q,$2,$_:String ;}Class c:_{Constructor (){} }Class __:_{}Class _{}Class Q:e{Val _:Array [String ,2];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 140))

    def test_141(self):
        input = '''Class N{}Class B{Var Me67_:Array [Array [Array [Array [Float ,0b1],0x4],03_6_65],0x7];Constructor (__,v_0m,wn,_,On:_51;_2:_){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 141))

    def test_142(self):
        input = '''Class __:H{Val $__828:String ;Var $e,Q_,e,_,_,$1U_634L_5l_4_,seBRG8:_;Var $__1,S___,_:Array [Float ,753_9_6];Val _:_;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 142))

    def test_143(self):
        input = '''Class t6{$__(_v:Array [Array [Array [Array [Array [Array [Int ,8_2_0],0b1_11_1],0B1],88],0b1010011],0xD1_8_5_D];J__0_:Array [String ,0X51];G5,E,U4,__7__n,DL:Array [Array [Int ,0x6],45]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 143))

    def test_144(self):
        input = '''Class D{$_(i6,E,_q_:k){Break ;}Val $_v6_,Z_,$5Ol,$P:Boolean ;}Class _5:TA_{t(){} }Class _001:_85{Var $H:Boolean ;}Class m:K{Var _:Array [String ,0B1000110];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 144))

    def test_145(self):
        input = '''Class _{}Class G9_:_d_{M__3c(_,_:Int ;o,_,_:_0;p,b:Boolean ;_,_:Array [Array [Array [Array [Array [Array [Float ,0B1],38],0b1111],5],0x3E],0X1]){}Destructor (){Break ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 145))

    def test_146(self):
        input = '''Class _:_7_{Constructor (__,p,___,_:Array [Boolean ,02];P_:__){}Constructor (){}Var $_,P4,_6yK_:OA;}Class _{}Class y{Val $6:Array [String ,02];Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 146))

    def test_147(self):
        input = '''Class __{}Class _s:__5{Var __5oLDA_,$_,Y:Array [Float ,0b110001];}Class _{}Class _{}Class _{Destructor (){}Var $_,_:Array [Float ,39];}Class p{Val S,_:Boolean ;}Class A5{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 147))

    def test_148(self):
        input = '''Class Di:y{}Class j_J:Y99__{}Class P30Nd:F{}Class _{Var N,$_:Array [Array [Boolean ,5],024];}Class M:V1{Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 148))

    def test_149(self):
        input = '''Class F2:__{}Class _U9:g{_(_8_5_,_8__r:Array [Int ,0B1]){} }Class Q:rm{}Class _{Var $_,$6,$9N:Float ;}Class ____{}Class _MsR{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 149))

    def test_150(self):
        input = '''Class f{Var _33,$_:String ;}Class _w:_f{Val $X,$Q_R:Array [Array [Int ,031],0x49];Destructor (){}Constructor (_,a:Array [Array [Float ,0X31],0xE_5F];z_6Xh,Y,N_,_6l,_,_:Boolean ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 150))

    def test_151(self):
        input = '''Class A{Var k4_A,Y1z_DZ,$_1,_:Array [Array [String ,0114],0X26];Destructor (){__::$750();fY::$93z_();}Var gJ:Float ;}Class W{Val _,_3Zr_,$X:Array [Array [Array [Int ,04],2],14_3];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 151))

    def test_152(self):
        input = '''Class _z{Constructor (){}Constructor (__:l;__,_e,_,__,_1_,_F:Array [String ,05];___,_:_3){Var ___,_:Int ;}Val $0QjY:Float ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 152))

    def test_153(self):
        input = '''Class L:M___{Var _,p_09W,_8:Array [Array [Boolean ,55],04];Val _,_0:Array [Array [Array [Boolean ,55],55],0b11100];}Class J{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 153))

    def test_154(self):
        input = '''Class F:q55{}Class _:Cr_{Val $_:Rl3;}Class J:_{Var c,$6_H:Array [Array [Boolean ,3857_2_564_4],0x1];Var _:_k;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 154))

    def test_155(self):
        input = '''Class V{Var $4,$P,_71__3e_:___;$d(v_:b;___E,__r,g:Array [Array [Boolean ,0B1001],44];_,_926n_4,_Hu,_1,__,_:E){Return ;}Val $2_,qC:_;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 155))

    def test_156(self):
        input = '''Class _y_4:_64w{Var $_:Array [Array [Array [Array [Array [String ,02_0],0x5B],0X22],01],0x5B];}Class __{Var $_,$F:FQ_;}Class y__{}Class _Ig{}Class _9:__B____gu{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 156))

    def test_157(self):
        input = '''Class __:__{}Class v{Destructor (){Val L,_:_9Z_;Break ;Var _9:Array [Array [Array [String ,25],6],4_0];}Val $9,$2:Array [Float ,0b1_0_1];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 157))

    def test_158(self):
        input = '''Class _6{$HW(){}Var g:Array [Array [Array [Array [Array [Array [Array [Float ,0X5B],0X9],07_3],0B10],0X5B],8],20];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 158))

    def test_159(self):
        input = '''Class A:_w{}Class _u_8j{}Class Ju:I{}Class _:_Q__61{Val _:z_7;H(_:Array [Array [Array [Boolean ,9],12],0b11]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 159))

    def test_160(self):
        input = '''Class B{}Class _:_7___R_{Constructor (){ {} }Var U:w;}Class _:w{Constructor (n:Float ;_,J__,_1m:Array [Array [Array [Float ,4],0X54],0B11]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 160))

    def test_161(self):
        input = '''Class _:c0{Constructor (d,no_:X){Val c,zK73:String ;Continue ;}Constructor (M:W2;_,Hm,_p:Array [Array [Boolean ,0b1],0b1];_,h_,_,i:Int ;_c,_:a;W_,rr_N,V_,hU,K_:K_9){}Var _,Cy,$_2:Array [Boolean ,0110];}Class _{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 161))

    def test_162(self):
        input = '''Class Y_Ax2:V{Val K,$0_u_dQ,$___,p,$_74,$6:Array [String ,0X3A];Val N8:Q95;P(R,_,N,_0,M:Array [Boolean ,0b10]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 162))

    def test_163(self):
        input = '''Class v:_{Constructor (u,_3,_,_,q_:Float ;I:Array [Array [Array [Array [Int ,0b111110],0b1_0],0b1],0107];Se2_:Int ){}Var _:Array [String ,2];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 163))

    def test_164(self):
        input = '''Class y:H{Val _:Boolean ;}Class _g:_{Destructor (){ {}b6::$Z();}Constructor (_5_j__,__,g:t;g:Array [Array [String ,0B11111_0_00],0b11101];_:Q){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 164))

    def test_165(self):
        input = '''Class T:_{$N(){}Constructor (i,_9:Array [Boolean ,0B1]){}Var $_,$H0_,_u,$5U:Array [Boolean ,178_8];}Class _:_2{Destructor (){Return ;} }Class o{}Class _:L_0{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 165))

    def test_166(self):
        input = '''Class __:_{Val _,$3qg__:Float ;Destructor (){Var __,_,g,z,_,_u_,Z:Boolean ;Break ;} }Class _:o{__4(){} }Class d:_1_{}Class _:_{Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 166))

    def test_167(self):
        input = '''Class xi{Var $D,$1_59:String ;Val $_6,g_e1,$2:r5;Val $_,E_,$K:V;Val _:_;Val $62,___4,$7n:Array [Boolean ,0X2D];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 167))

    def test_168(self):
        input = '''Class dS9e1{Constructor (_5_:Int ;_:Boolean ;_69:Boolean ;_,g6F:Array [Array [Array [Boolean ,0B1001000],0b10010],0b10010]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 168))

    def test_169(self):
        input = '''Class q5:c{Constructor (N_,_x_:__;_,h8,_4,o,_,_,__k4:Array [Array [Int ,03_2],27];N,P_,F_,j__W_s_2_:_C5_2_;U,_,AD4:Array [Array [Array [Float ,076],0X35],27];m:Boolean ){} }Class O{$__(e,H:_m){} }Class _2{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 169))

    def test_170(self):
        input = '''Class l{Destructor (){Continue ;}Var $55:Boolean ;}Class T:J_7{}Class U:O5_{$f(){}$_(){Break ;}Val _,u0:_;Val b_A_,_:H9;Val $U_2a,_u:Hl;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 170))

    def test_171(self):
        input = '''Class _AB:Y{Val $h6,P:Array [Array [Array [Array [Int ,05_5],0B1000010],0b101011],02];}Class _u_{Var CCs34:Array [Array [Array [Array [Array [Array [String ,0x34],48],48],1],0b11_01_11],0XF];}Class o{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 171))

    def test_172(self):
        input = '''Class _{Var _3E:Array [String ,0x1];Constructor (){}$4(_:Int ;y,_8:_;Z,_,_PE_,_,_,e7,R0_2__:q8;_:S){} }Class _:_{}Class u{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 172))

    def test_173(self):
        input = '''Class a:_{Constructor (_:Float ;Ox,__6,_1:Array [Array [String ,0x326],0X8_2];_6985,e,_:u;_3,P,z_4,Z:J){}Var _,$_,SF,$F:Float ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 173))

    def test_174(self):
        input = '''Class n:J_{Constructor (h_,_20G,B,_4_,E:Array [Array [Array [String ,80],07],9];__:Array [Int ,0B1011001];_VA_,yd,_:String ;_,Y,_:Array [String ,0X48]){}Val __,$H:_Z_;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 174))

    def test_175(self):
        input = '''Class S00:q{Val $di__5Y_,$4,_Q:Array [Array [String ,0b1011111],4];Var $_y:Array [Boolean ,041];}Class Z72{Val _O,BT:Float ;Val $_:Array [Array [Array [Array [Array [Array [Array [Array [Int ,67],5_042],0B1_1_0_1],055],03],0X4],4],0x9];}Class __:Y65{}Class _R:qJ9273{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 175))

    def test_176(self):
        input = '''Class T{$98(_:Array [Int ,0B1000110];Ll,d_Q,s_0q:Boolean ;Q:Int ;_,h_9:Int ){} }Class vr_{_(h:qn){} }Class _{Constructor (){Break ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 176))

    def test_177(self):
        input = '''Class r{Constructor (_:Array [Array [Array [Array [Array [Array [String ,07],0b1],0B11],07_52],0x1_3E],1_1]){Var Ym0:Y;}Constructor (Wf_,nF2_l1,_:Array [Array [Float ,0B1100100],0XA_E];d:Int ){ {} }}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 177))

    def test_178(self):
        input = '''Class __:__{}Class _zd_:__8i{Constructor (_,C_0,_,Y,__,__:Array [Boolean ,862];_3,_:_b__;__:String ;_:Array [Array [Float ,0XC],017];_y,d_jz:Float ){}Constructor (){}Val $__6_2:Array [String ,0b1100011];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 178))

    def test_179(self):
        input = '''Class O5x_{}Class _9{Destructor (){}Constructor (){}Var v,x_5,D9,$8:i;$Q(){}DwL(__2,_99:_;_,Cw:_;_,c5W:m){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 179))

    def test_180(self):
        input = '''Class _:_0{}Class y{Val S,$_,$H5_C:_K;}Class b2_mx{Constructor (____,__,__7_:Array [Array [Int ,57],0B101001]){Break ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 180))

    def test_181(self):
        input = '''Class _84_A__:q__{$9(S,_,_:_96wtv){}Var $7,_,$___,__:Array [Array [Array [Boolean ,0x9],15_8],0B1100011];Constructor (_,_:Array [String ,79]){}L(){} }Class i{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 181))

    def test_182(self):
        input = '''Class _{}Class Z:O_{Var $7_B6y_:_Q;Val yE_n,$Y0:Array [Int ,87];LX(D_3:J7){}_5(_:_bYq;m,_O0,_,F:I;_,_k:String ){}Constructor (_:t){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 182))

    def test_183(self):
        input = '''Class _{Var R,$9f,$_:Array [Boolean ,0x3E];$__(_1Cc_F7,_4,_z,m_K_0:_){} }Class x{Var $K,$B:Array [Array [Array [Float ,0X64],1],0675];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 183))

    def test_184(self):
        input = '''Class _:_{Val _T_,_:Array [String ,0XA];Constructor (){} }Class _:g{Destructor (){} }Class _{}Class _:N_Ei{Var $_:Boolean ;}Class _97:K1__w{Constructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 184))

    def test_185(self):
        input = '''Class _s4:k_n__{Val _4:_;Constructor (_,_38X:u){} }Class e_{Var $mN,$_t5:_668h;Destructor (){}Constructor (S___,O:Boolean ;l:__;__m:Int ;G_A,_,i:Y;I_2_,J7,Ik5_,OH,_,__:Array [Boolean ,3];_:X99_5_){Break ;Val _,l,_:Float ;} }Class _:jx_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 185))

    def test_186(self):
        input = '''Class _:_a6__{Val $__6,$N:Array [Array [Array [Float ,0X1E],0B1],0X9A7];}Class __r_A{}Class _1{Val $Q,_:Array [Array [Array [Array [Boolean ,0x1A],035],035],0x3];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 186))

    def test_187(self):
        input = '''Class l_XU:vfD_018{Constructor (___:__){Continue ;}_2(){Val p:Array [Array [Array [Int ,0b1],0116],0116];} }Class _p:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 187))

    def test_188(self):
        input = '''Class _ZM:_B{Var $2,$5t:Array [Boolean ,6_7_69];Constructor (__5,_,_,UY:Array [Float ,07];__:_;uq,_:Boolean ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 188))

    def test_189(self):
        input = '''Class _:l_C05{}Class c__l{Var Uiv:String ;Val $_:Boolean ;}Class o{Val $9,_w_:Array [Boolean ,0b100100];}Class E:_a{Val _,$8,__:v;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 189))

    def test_190(self):
        input = '''Class B_{Var _y4:I;}Class Y{Var $I:Array [Array [Boolean ,0B1100000],34];$K2(){}Constructor (u:_){Continue ;__::$I__();}Var $__:Array [Array [String ,0X52],3_3_5];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 190))

    def test_191(self):
        input = '''Class _:Z{M4Ch(){}Var $__A__1,$_:String ;}Class wFY{Constructor (a,J:_;_w_,lx9zG4,__Wu:Boolean ;__I,n52qa_,b_,S:Array [Array [Float ,05],0141];X:Array [String ,0X17]){Break ;Var K,X94:_N;} }Class _:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 191))

    def test_192(self):
        input = '''Class _:Su{F(_0_:Array [String ,0x61];j,h:String ;D:Array [Array [Float ,0B101010],0b110];O:Array [Float ,65];A:Array [Array [Array [Int ,0105],0B1],02_4]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 192))

    def test_193(self):
        input = '''Class L_{}Class f{_(_:Array [Array [Array [Array [Array [Array [Boolean ,01_1],6_7],0B100001],76],0X3],05_6]){}Var pi:String ;_1(){} }Class u8{}Class _:_4H{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 193))

    def test_194(self):
        input = '''Class _:Q{Val $4,$d,$o_55_6,H:Float ;Val T0_,$4:_14;}Class _:_7{}Class _:_{Val $_:Boolean ;}Class _{Constructor (m,_,_1_,_:Array [Array [Array [Array [Array [Array [Array [Array [Array [Boolean ,0B110111],0x7],100],0b11],100],0B110111],0x4],0x7],0b1];X:_;_,__:Array [Float ,0140]){Continue ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 194))

    def test_195(self):
        input = '''Class SUD7:K_{Constructor (Fh:Float ;_K,K,__8_:Float ;__6,_:Array [Array [Array [Array [String ,0b10],0X2],6],075];_:j_){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 195))

    def test_196(self):
        input = '''Class __w{Val $_:Array [Int ,0x77];}Class _1R2{}Class _8{}Class _1H{Constructor (){}Var _p,__:Int ;Val $PV:Array [Int ,28];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 196))

    def test_197(self):
        input = '''Class D2:TD{Val _g_:Array [Array [Float ,0xF],0XE_E];}Class __:_{}Class S5_{}Class _4_{}Class _n{}Class _:Y{Q__(_:Array [Boolean ,0XE_0];_,_:U3;_,_:Array [Float ,0b1]){} }Class _3{Var Ry__n,$__,P,$4xs__B:String ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 197))

    def test_198(self):
        input = '''Class t3L282:Ux__26{}Class v9:__2{$0(z,y:Array [Int ,0103];Q:Int ){ {}Break ;}Destructor (){}Destructor (){Break ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 198))

    def test_199(self):
        input = '''Class xe:__{}Class _4_{}Class _F:_T{}Class ___:_{Constructor (){}Destructor (){}Constructor (_,_m,__:d;E,_:Float ;_,_,h5,_:Array [Boolean ,0X9];w_,j8:Float ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 199))

    def test_200(self):
        input = '''Class i:gT{}Class __{Val $7_4_,$5,B,__2,$_,N_5_:Boolean ;}Class _i:k{Constructor (_:Array [Array [String ,0xD_4_1],0b101]){} }Class U:b{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 200))

    def test_201(self):
        input = '''Class v_:fp{Var h,$_:String ;Var H,$__1_:Array [Int ,0b10_0_0];Var ___5:Array [Array [Array [Float ,0B11001],6],077];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 201))

    def test_202(self):
        input = '''Class C_{Var $V_h0_4:Int ;}Class q_{Val $_,H,$J,_7_a,_:String ;}Class _2_{}Class _{Val $vp_,_:Array [Array [Int ,2],51];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 202))

    def test_203(self):
        input = '''Class E:d{}Class _4{Var U,_p,$f3Eo1y:Array [Boolean ,50];}Class _:o{Destructor (){} }Class N:D{}Class _:_{Var _:Array [Int ,65_4_9];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 203))

    def test_204(self):
        input = '''Class S{Val d,$c:_;Destructor (){} }Class y_{Var SFP,__:Array [Array [Array [Array [Array [Int ,0XA6_6],02_14],37],0x7],05_2];Destructor (){} }Class l1{}Class e__0:C_{}Class _{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 204))

    def test_205(self):
        input = '''Class __{Constructor (q:String ;eo4__:Array [Array [Boolean ,0b10_1_00],04];_,I,H90__:String ;_6:Boolean ;_,_:_I__;_:b){Continue ;}Var $D_U_,$_,N:_R7_;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 205))

    def test_206(self):
        input = '''Class _:_{Destructor (){} }Class _dH{Constructor (_:String ){} }Class g{Destructor (){ {}__::$_.__9w();} }Class _:_{Var _,__,g,$5,fI_,_:Array [Array [Array [Array [String ,027],0x13],23],0x13];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 206))

    def test_207(self):
        input = '''Class i{Var $_:Array [Array [Array [Array [Int ,0104],0b1_1],2_4],66];}Class q37_3_wCOZ:_{_9_B(___,__:Boolean ){ {Continue ;} }Constructor (){}Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 207))

    def test_208(self):
        input = '''Class a:I{}Class _:X{Destructor (){Break ;}Constructor (){}$_(){Continue ;} }Class _:r{}Class M1{Val WM:Array [Array [Array [Int ,24],06_6],0x7];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 208))

    def test_209(self):
        input = '''Class __:__{}Class s{$C(__,O,_5c,___,_:__;U,_,h,P_:Array [Float ,03_73];i,_,O:Float ){}Constructor (){} }Class _IUZ:r1Cs{Var $s_,$u:v;}Class J{}Class _:_{Val _,_,_l:Array [Boolean ,0b10110];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 209))

    def test_210(self):
        input = '''Class _2:_97{}Class lG{Val _:Array [Array [Array [Array [Array [Array [Int ,0102],0x9],0xA],0756],0102],01_7];}Class m:jPW{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 210))

    def test_211(self):
        input = '''Class _J{}Class __2:_68{q6(n:__B;S__,A9890:Int ;Ho,_B_t:Int ){Break ;Break ;Continue ;Break ;{ {} }_H::$2j.f9._();} }Class _:E{}Class L{Var _:EQ;Val $_,$_7:Array [Float ,20];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 211))

    def test_212(self):
        input = '''Class _R_{}Class B:N{Constructor (d_92,__8_,_l,q,__,T,w,Z_,l:Array [Array [String ,16],0xA]){}Destructor (){}Val _:String ;$n_(V7:Float ;_:String ;_,X,_,___:Float ){}Var $_,_:String ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 212))

    def test_213(self):
        input = '''Class _3_:ze{}Class _{Destructor (){} }Class Q{}Class _{}Class _Jm44A:_2d{}Class __:hm{Destructor (){Continue ;}_(n:Int ;_:Array [Int ,75];__,D1____,_v,D:String ){}Var L,CH1ysE:Int ;Constructor (_qIz2Lz,Zv:Boolean ;_,_:Boolean ;f:Array [Float ,75]){Return ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 213))

    def test_214(self):
        input = '''Class R{Constructor (i:Array [Array [Array [Array [Int ,054],0XA],054],5_4_4];tx49,_w,_Ig:Boolean ){Continue ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 214))

    def test_215(self):
        input = '''Class __:_{Destructor (){}$87X_9(_N,_:Int ;_:Boolean ){Var _,Q___:Array [Float ,06_6];Return ;}Constructor (){i::$_();} }Class I_8{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 215))

    def test_216(self):
        input = '''Class _{Destructor (){Break ;} }Class F{}Class _F:Q6h97{Val $__,$8_v:Array [Array [String ,0b1],0X6_2D_D];$_67c(){}Var _,M,_:Boolean ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 216))

    def test_217(self):
        input = '''Class _:B{Destructor (){_::$A._._4__();}Val e_624:Array [Array [Array [Array [Array [Array [Array [Array [Array [Int ,0134],0B1001111],0134],0b10001],0X61],06],87],0B1001111],0x3];Val Y:String ;Constructor (){} }Class I6On:uN_8{Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 217))

    def test_218(self):
        input = '''Class _:d{Val $CY:String ;}Class X:U1{}Class _:___{Val $e,Q6,U,d7:Boolean ;}Class _H{Destructor (){Val e6,_J:A;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 218))

    def test_219(self):
        input = '''Class GJ_fk6{}Class _Z:_3_Z{I(pT97,l,P:Array [Array [Array [Array [Array [Boolean ,0b1],83],83],54],0X3]){Val _:Array [Boolean ,83];Return ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 219))

    def test_220(self):
        input = '''Class H{$3Y2c_(pE,e,_3,J:Int ;g_,g,jP,_:Array [Array [Array [Array [Array [Array [Int ,0B110111],04647],07_7_2],0125],0125],0X40];_,v:e){Continue ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 220))

    def test_221(self):
        input = '''Class It_iu:_{$_(_,V,n,J4:Array [Boolean ,46];_1:Array [Boolean ,0102];__:u;b,y0,f_,p:d_;c7_:C2H_){} }Class _z{$b(){} }Class _:E_x{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 221))

    def test_222(self):
        input = '''Class _:_WM6j{Constructor (_,IC:Boolean ;__6:String ;l:Array [Float ,0xC];_iFv_8__4a7,____:Array [Boolean ,0B10]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 222))

    def test_223(self):
        input = '''Class _u{Destructor (){} }Class q:_q{Constructor (e12,_,X:Array [Boolean ,0B1001];_:Array [Array [Boolean ,0116],7_9]){} }Class g:___{}Class _{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 223))

    def test_224(self):
        input = '''Class o_W{}Class __9:m_{Destructor (){}$2(_1:Array [Array [Array [Float ,0B10111],22],0X24]){}Destructor (){Var _Z7,_:_;}$_(){} }Class _{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 224))

    def test_225(self):
        input = '''Class e:I{Destructor (){}$Rb2(){Var H,g:Int ;Break ;} }Class u:k2012{Var $6,_,$_6:Array [Array [Boolean ,0XE],0x46];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 225))

    def test_226(self):
        input = '''Class aN:_2{Constructor (_:Array [Array [Array [Array [Array [Array [Array [Int ,54],0126],54],05],0X5],0x55],0b1101]){}Destructor (){Continue ;}$6(){Break ;} }Class __4E_{$n7(__6__rh3:c;_,_9_:Int ){Var p,_:Array [Array [Int ,0126],0b1_111];} }Class j_:g{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 226))

    def test_227(self):
        input = '''Class _:_{Constructor (__:Array [Int ,024];d:B;_,G_,__:Array [Array [Array [Array [Array [String ,932],0b100010],0X3_8F_7],03],024];c,__,P__,_vz0,_3,w__:_u){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 227))

    def test_228(self):
        input = '''Class c_{}Class nz84_{}Class _:_{}Class m_6b_:_D5{Var $__,xc4C,$jd,F:Array [Array [Array [Array [Boolean ,0B11],0B1],056],056];Val X,$r,$4___,W4L:Int ;}Class _F{Var _:Int ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 228))

    def test_229(self):
        input = '''Class _{}Class _{Val $0,$_:String ;}Class Wi0:_{}Class _:ma5{Val $m,r_qMQ:Array [Array [Boolean ,0xB6_F],9];}Class _6{Var Y_k,$78,$3_8:Array [Array [Float ,02],02];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 229))

    def test_230(self):
        input = '''Class _120{Constructor (){}$W(G,ZCg_,_,__,u,kd13S2:Float ;_90__:Float ;_Bf,_,x0:Array [String ,06_2]){Break ;{Break ;} }}Class _:C_64__{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 230))

    def test_231(self):
        input = '''Class X:v66{}Class _:__D1fT{Constructor (X:Array [String ,021];_:_2E5){ {} }Constructor (bD_5_,_:Int ;W,H:Float ;__,__:Float ){Qo::$2soTU();} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 231))

    def test_232(self):
        input = '''Class IL{v(k:Float ;_,__4T5P_:Array [Array [Array [Array [Boolean ,1],35],0b1_1111],072];W:_p62_S;o8,_b:Array [Boolean ,0b11001];_:h;i_:Array [Array [Boolean ,0x38],0b11001];_m:Array [String ,0B1];_,U:Array [Array [Array [Array [Array [Array [Array [Float ,0X2],063],063],063],0B110011],036_1_4_4],0x38]){} }Class r25y{}Class D{$_eK9(){O_::$S(!-_P::$_*C::$p.N._._().c);Break ;} }Class E{Destructor (){} }Class G_:_{Constructor (){Continue ;Continue ;Continue ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 232))

    def test_233(self):
        input = '''Class __{Val _:Array [Array [Array [Array [Array [Array [Int ,0XE],18],0b1],0412_0],9],22];}Class b3:_d{}Class g{}Class __35{}Class T6{}Class Q_:l3_8_iq{}Class ___:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 233))

    def test_234(self):
        input = '''Class __{Constructor (_:_1;_:Array [Array [Boolean ,0b1],0540_4];o:Float ;_:Array [Int ,66]){}Var _296:_;Destructor (){Break ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 234))

    def test_235(self):
        input = '''Class O:_63{Var _,sj,_:__;Var $u_,$_49Nx,$_,$8,E:r_M;Val $si:Array [String ,021];Val __7,$_,$__:Array [String ,06];}Class _5_S:c{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 235))

    def test_236(self):
        input = '''Class _:__{}Class A7_49:_v26{Val $R0__,R_,_:Float ;Val X,_:Array [Array [Array [Array [Array [Float ,3],0b111010],0b1],8],050];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 236))

    def test_237(self):
        input = '''Class __{$5(_G:Boolean ;Z,l,_,P,_,R3,l_____b1_:String ;I:Array [Array [Array [String ,0b1],0X16],024]){ {Break ;} }Var $_:Array [Array [String ,012_5],0XC];Val $_ak_:Array [Array [Array [Int ,0x12],92],92];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 237))

    def test_238(self):
        input = '''Class _{Val _1:Int ;$__N(L:Array [Array [String ,820_0_1_6],0X4F];K,_:String ;_kd_SS,_f_,__,q6a,k,__,B_,_:Array [Boolean ,0b100111]){Return ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 238))

    def test_239(self):
        input = '''Class _{}Class _{}Class _61D{Constructor (____,J_:Array [Float ,0B1];u:W_;_K_,n,_,_:Array [Array [Array [Array [Array [Int ,83],0B101001],0b1_1],04_2],0B1];_,Hn_:Array [Boolean ,0X46];g,q1_83,e:Boolean ;g,_:Boolean ;_0h:Float ;G8_:String ;Z:Array [Array [String ,9629],83]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 239))

    def test_240(self):
        input = '''Class _6A:_96{Constructor (J,Z,KEj:Array [Array [String ,40],15];a:Array [Array [Array [Float ,0x8],40],8_6];_:Array [Array [Float ,40],0xF]){} }Class _mE{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 240))

    def test_241(self):
        input = '''Class _:n{$9(_:Array [Array [Array [Array [Array [Array [Array [Array [Boolean ,0X32],0x42],0X8],85],0xE],07],07],0X1F];W,r:_){} }Class rG_:_{}Class T0__{$_(_:Int ;_:Array [Boolean ,0x42]){} }Class b:__P2_rmqd{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 241))

    def test_242(self):
        input = '''Class __{Val $9:Boolean ;}Class q__B_a:_{}Class _{Val __fV3_,$Z_U,_8,_,_6j:Array [Array [Array [Float ,041],0b1010011],0B1_0];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 242))

    def test_243(self):
        input = '''Class M{}Class p5_:_Z_1{Constructor (S:Array [Boolean ,0X2]){} }Class n_8p_{}Class x_2:q{Constructor (_:Array [Array [String ,035],0x21];_E127,r,_QU:_;_,a,______,_36:Array [Boolean ,78];_,_a:Int ;J6,h:B_4){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 243))

    def test_244(self):
        input = '''Class _:q4{}Class _4Z9:_c6{Constructor (__r,d:Array [Array [String ,6],613_49_1];Y,_:Array [Float ,0x2F]){}Destructor (){Val _:__;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 244))

    def test_245(self):
        input = '''Class _:f{Val l_Dw4:Array [Int ,0X4E];Constructor (_:F_;_0u_:Int ;__,_h_:TO;_,md:Float ){}Val $S_r_5:Array [Array [Array [Array [Boolean ,0b1011],0xE_2_1],0b110],0b10_0_1_11];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 245))

    def test_246(self):
        input = '''Class _:_O{Var $7:Array [Array [Array [String ,04],042],0x32];}Class _{$C6R(){Return ;} }Class __7w:_{$0(){}Val $Z,$_0,$Z_h9:Float ;}Class fD9{Destructor (){Val _9,D:Float ;}Var _p,h:_;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 246))

    def test_247(self):
        input = '''Class _:__{$q9(){} }Class E:_{}Class _c{}Class _{Val _,$A,h4,ka_85JE,u:YI;$e(_f:Int ;A6z:k;G4___:String ;_pn2,_7_,_5PP,M_w6Ct6:X){Return ;Continue ;} }Class C7:E{}Class z:E{}Class X:_{Val q_,Nb_:Float ;}Class O_:z{Var y_,$__:Array [Array [Array [Float ,0x12],65],65];Constructor (_999_F:Array [String ,0XD1];__:Boolean ;_,_:W){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 247))

    def test_248(self):
        input = '''Class H:__F{Var $_MA:Array [Array [Array [Int ,0b11_0],0105],0x1C];}Class _:_{Constructor (z,j,MU,__,j8:k_;o,_:Array [Int ,7_37];_,ix_z3,_:Float ;_,__T7rv,e:String ;_:Array [Boolean ,0x1C]){Continue ;{} }Constructor (){} }Class __8F7:_{Constructor (E_N_5H,D:_M){}$Q1(){Val W,h__:u;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 248))

    def test_249(self):
        input = '''Class Dw_:z__4{Var $_Y:X_Y_V;$U_(){}Val $H570:Array [Array [Array [Float ,0140],0140],0X8];}Class C6{}Class P:l2__{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 249))

    def test_250(self):
        input = '''Class _V4OR6{Constructor (B:Array [Array [Array [Array [Boolean ,07],1],0b1],0B101111]){Return ;} }Class _:_{}Class _l3{Constructor (){Continue ;} }Class u2{Var L2,$kY5:_J;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 250))

    def test_251(self):
        input = '''Class k:dG3{Constructor (){Break ;} }Class _M9:z{Var $0:Array [Array [Array [Int ,0b1],076],3];Val $8:Array [Int ,0b10000];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 251))

    def test_252(self):
        input = '''Class K:fZ{Constructor (__:_k__;_,X:_;_0:Array [Array [Array [Array [Int ,0x6_3F_9_E],05_7],4_1],0x5]){} }Class k{Constructor (JS,_Tv2L,H,q2,a,g,_0:Array [Float ,0X5]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 252))

    def test_253(self):
        input = '''Class sg7{Var K:Int ;}Class _4{}Class _{}Class _{Var $_9_9,Q_,$3:Boolean ;c_(_4_,__,D,_85v_H,_0_F_,C9:String ;_24:Array [Float ,0X32];Z,Z,K4,__:C){Var _,CWh:Array [Array [Array [Boolean ,0x3B],034],034];} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 253))

    def test_254(self):
        input = '''Class EO{kU_(u_C,H:Array [String ,07];_j,G,__,_:U6;_,M88N_J__6:Int ;____Z:Array [Array [Boolean ,0XA],94]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 254))

    def test_255(self):
        input = '''Class __:_4i_{Var $_gn,$C_55,$_,$4gj6q:Array [Array [String ,0B1100001],0136];Constructor (f,_r:Array [Array [Array [Array [Float ,0b1_1_1],01_1_4],0b1],84];ry_:B){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 255))

    def test_256(self):
        input = '''Class __{Var $1:v;}Class _G:_{Destructor (){}Destructor (){Continue ;Continue ;} }Class r_:je{Constructor (k1:Boolean ;_Gx:c){} }Class K:c_9___2{Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 256))

    def test_257(self):
        input = '''Class _{Destructor (){Val _,_8,I,E,_,y_iE:n;}Val $3:Array [Array [Array [Array [Array [Array [String ,0b1010011],0X8],03],033],24],0X3AC_4_2F7];}Class l:OK_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 257))

    def test_258(self):
        input = '''Class _Kt1_:H{Val $__:N;}Class _W{Var $0_V:Array [Array [Int ,0B1010],0X53];}Class N{Val q,qR9l,$p,$p_U,$8:String ;Destructor (){} }Class _92:_{$_(_,K_,_,G47_,_:Array [String ,0b100011]){}$_(){}r(){} }Class _5{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 258))

    def test_259(self):
        input = '''Class _{Var $DjB_,a,$_:Array [Array [Array [Array [Float ,0B11011],9_3],0x10],0B11011];}Class T{}Class _9:_{Constructor (P_,W:_b){Break ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 259))

    def test_260(self):
        input = '''Class _{}Class _4{}Class i{Val $f:_;Constructor (_,_,S,W5:Array [Array [String ,0xF],0b1_0]){} }Class oF:h{Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 260))

    def test_261(self):
        input = '''Class U{Constructor (n7X_MP_,_,_,pN_:Array [Array [Int ,04_0],0xD];___,d9_,_D97,N_:Boolean ){Continue ;}Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 261))

    def test_262(self):
        input = '''Class _i3__{}Class I:_If_{_(__,_3,pQ:__6BD;_,w1_4:Array [Int ,05_2];_:__;_ooT:lx_2){Continue ;{} }}Class cV__:W{Val $_zic:_3;Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 262))

    def test_263(self):
        input = '''Class Z:b{Destructor (){} }Class D:D{Var $bA:Array [Array [Boolean ,0b1101],9];}Class R{Destructor (){} }Class _4cD{}Class M_5:tN5{}Class _tE77{Constructor (){}$_(V:Array [Array [Array [String ,066],0B100000],0xD_4D67]){Break ;} }Class t__:M_w{Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 263))

    def test_264(self):
        input = '''Class K:_{Var $_,_,$8,sn_,$9,$_:v_;Constructor (ix_,J,_:Float ;_A,d:Array [Array [Array [String ,01_6_4],057],0B1]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 264))

    def test_265(self):
        input = '''Class I:N{i(_8,_,_,_Du9:Int ;mR:Array [Array [Array [Float ,0b1],9],0b1];v:Array [Array [Int ,0127],0X4A];_:Y4__4){Return ;} }Class _{}Class _:_{H(J_,Ra,_c:Array [Boolean ,0X4A]){Continue ;} }Class _d:_T{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 265))

    def test_266(self):
        input = '''Class _I{Destructor (){}Destructor (){Return ;Continue ;} }Class X:L{}Class wzR_:_G67{_(_r59:Array [Array [Array [Boolean ,043],0B1_1],0B1100100]){}Val b_8e:_;Var $6T1Eu_9:b_;Val $d6,_8:Boolean ;O42(){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 266))

    def test_267(self):
        input = '''Class U{}Class _{Destructor (){} }Class _:_{_5(){} }Class _7{}Class b_0:w{Var $_:Array [Array [Array [Array [String ,5],7],0B1],88];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 267))

    def test_268(self):
        input = '''Class _{Var zH02:Array [Array [Array [Array [Array [Array [Array [Array [Int ,05],0b1],0X59],68],020],0b110],86_2],0X7_E];}Class _:_{}Class OuJ:EM{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 268))

    def test_269(self):
        input = '''Class A:y{Constructor (_:H_;FR,Z8r,__w:Array [Array [Array [Int ,0x33],05_42],0X1B];_,_,_:Array [Boolean ,0752];__:Array [Int ,13]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 269))

    def test_270(self):
        input = '''Class M9:Z{Constructor (_E:Boolean ;_:_e_;_cM__,j,_:Array [Array [Float ,045275],0B1_1_1_1_0];q,V__,W_g8,Lo4O:String ;_,_,_w6w:sk){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 270))

    def test_271(self):
        input = '''Class _{Val t,C:_;Val __,$_,$K:Array [Array [String ,0X4_D],86];Destructor (){Return _er::$9().E()+!!D::$n.Q(!_::$4_.q0);Break ;Continue ;}Val $3lRc:Int ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 271))

    def test_272(self):
        input = '''Class l_:_{}Class X:_2{Var $7t7:Boolean ;}Class O{Destructor (){}Var vF_:g=----_uL::$_.h()._0*!!!False .A9Z();}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 272))

    def test_273(self):
        input = '''Class D{Val k,$__,j,_9_Cs:Array [Array [Array [Array [Array [String ,0xD],0xD],0B1],054],016];}Class _v65:p{Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 273))

    def test_274(self):
        input = '''Class __{Constructor (XZ:Array [Array [Float ,0x21],0B1001010];_LS7,wm:Array [Boolean ,057];N,w:Int ;i:Array [Array [Array [String ,0X4_0],02_3_56_4_7],0X4E]){}Var $_9:Array [Array [Array [Array [Array [Int ,0x5],02],0b1001101],057],0b1001101];}Class _{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 274))

    def test_275(self):
        input = '''Class _{Destructor (){Break ;}Val D:Q_c;Val B52:_;Constructor (){Var _:Q4;} }Class v_:O{}Class _{}Class Z_1a_:D_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 275))

    def test_276(self):
        input = '''Class _5{}Class _5_f20_{Var $v:_;Val $8i:Array [Int ,05];Var _:Array [Array [Boolean ,0b1100001],0B111001];}Class _MpX_:BM{Val _,$S4,$m,$00:_;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 276))

    def test_277(self):
        input = '''Class w:_{Var $r:Array [Array [String ,0b100110],5_5];}Class _{Constructor (g__t_r:Int ;HE:Float ;_,_,_:Int ){Break ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 277))

    def test_278(self):
        input = '''Class I:l_E8{$763_(_:Array [Array [Array [Boolean ,0x18],81],0X58];__:Float ;__:Array [Array [Array [Array [String ,0141],0b111100],0b111100],0xC_5]){}Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 278))

    def test_279(self):
        input = '''Class g{Constructor (oJ_:Array [Int ,0x23];_:String ;s,_6:_1__V;c___837:Array [Array [Array [Array [Float ,0X17],31],04],02_2]){}Constructor (F8G1u3,_5:X;r,T,t,_X43,Q5:K_D){}O(_,_:Array [Array [Array [Array [Boolean ,0126],0x7],0X4],04];__f_:dn){ {} }}Class _{}Class iw:__{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 279))

    def test_280(self):
        input = '''Class __5{Constructor (x,__3:Int ;T1A,u:Int ;y,_6_,w8,__:Array [Int ,61];wD:Array [Float ,0x51];o:Array [Boolean ,1]){}Constructor (d:_;o9_,_0:_z_0_Y;_Z,_:_){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 280))

    def test_281(self):
        input = '''Class P:_{}Class o{Constructor (U,P_4d,_,_:Array [Array [Int ,0b110101],0B1011101]){}Val $0Lf6:Float ;}Class b{Var _:Array [String ,0XA];}Class _:L67_2{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 281))

    def test_282(self):
        input = '''Class _:J0{Var $k,$e,$_:Int ;Val $H2,e__v_,h,o,C,__:Array [String ,3_8_2];}Class l:o{Var __B:Array [Array [Array [Boolean ,01],070],0X1];Constructor (M,l:Boolean ;th3:Array [String ,1];F:KWvH7){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 282))

    def test_283(self):
        input = '''Class _87c:f{}Class o4:_m{Destructor (){WZY_6e::$kNf92._x().l();} }Class V:M4{}Class CR35_8{_J(U,_4m_:Int ;_:Array [Int ,0143];_j7:String ){}Val $4R_,_Q4:Array [Boolean ,42];}Class _3:_2{Constructor (i2,_t:I;_0,__:g;_,C__:_;_2T,_Lp,a__:s){Var _,_:wG_;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 283))

    def test_284(self):
        input = '''Class M:m_{$cL35O(_:T;_a_F:Array [Float ,05];X_6z_99l,_:yj___;_:Int ;M____,_90_:Array [Float ,0132];e,_:_8){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 284))

    def test_285(self):
        input = '''Class _{Constructor (P:Array [Array [Int ,0121],0X43];_0b,o,_4,W,u,f,_:n){Break ;Var Ct:Array [Array [Int ,030_3],0121];} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 285))

    def test_286(self):
        input = '''Class p:_{Constructor (W72:Array [Boolean ,0101];__,_:Array [Array [Int ,0x49],0x49];_9U,x:z;Q,V:String ){Break ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 286))

    def test_287(self):
        input = '''Class __{Var _,$0:Boolean ;Constructor (t9,_:a;_h,G_:Array [Boolean ,54];_2:String ;Y:Array [String ,0x35]){Continue ;Break ;}Destructor (){ {Break ;} }__(_,_:_u;h:Boolean ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 287))

    def test_288(self):
        input = '''Class ZY{_(K:Array [Array [Array [Array [Array [String ,03],98],98],0XF],9];_,_0W4,V_:Array [Boolean ,0B10001];_4:Array [Array [Float ,02_6],0b11]){}Var $CDt_1,Fp:s_1;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 288))

    def test_289(self):
        input = '''Class Q{Var $69,i,_4_:Boolean ;d4(_,_fw8:_r;_l:Array [Float ,044]){}Val bL,_,_k5,$I,X:_;_Z(_4:Int ){} }Class n:_{}Class t:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 289))

    def test_290(self):
        input = '''Class _:_{Destructor (){t::$9Y().FD.Fe.__();__::$1_Y_741i6();Return ;}Constructor (y,__:Float ;_:Array [Array [Boolean ,12_12],0x9708]){Continue ;} }Class _4_{}Class J{Var S:Array [Boolean ,0X54];Val $J:String ;}Class u74{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 290))

    def test_291(self):
        input = '''Class _:_{}Class X{Var $i5,BY9Y_2_9,$_:Boolean ;$p(){} }Class __5:_F028{}Class L{Var $__,$6_e,$m:Array [Array [Array [Float ,0x2F],34],0b101];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 291))

    def test_292(self):
        input = '''Class J:_{Constructor (__32:Array [Boolean ,0b1];e_:Array [Array [Array [Array [String ,041],0b1_0],0X2E],05]){Break ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 292))

    def test_293(self):
        input = '''Class U:m63_4{_(){}Destructor (){b::$_();}Destructor (){} }Class _M__V{Var e_:_;}Class R_{$I(dl__:g3;_:String ){} }Class pf__5U{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 293))

    def test_294(self):
        input = '''Class m{Constructor (){Var v,_5,_1:D;}Val $__,$io:Array [Array [Array [Array [Int ,51_8_7],0B1],0X37],0B1_10_0];$5(Y_:Array [String ,0x55];_,_79:Float ;io_G_2:_;s,p__:_h;V5__d:Array [Array [String ,0b1100011],070];f,_k:_C4){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 294))

    def test_295(self):
        input = '''Class C_1Gmb{$5n(x6:f){}Val $_:String ;Constructor (){}Val $_:Array [Array [Array [Int ,30_1],053_13],0B111100];Val $73,$x:String ;}Class _{Val g,$T,i:__8x;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 295))

    def test_296(self):
        input = '''Class _{Destructor (){Return !!_35::$T_().D.jJjh()>=--T::$4._;Continue ;Break ;}$V4(_:Boolean ;f:Boolean ){} }Class J:V{Var _:Float ;}Class _{Var $82w2HjF3_:Array [Array [Int ,07],8];Constructor (){}Val J,b:f4;Constructor (___9_LT___m:Array [String ,0b1100];W,_6:Boolean ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 296))

    def test_297(self):
        input = '''Class R{Var X:O;Var $6_:L3;Var __:Array [Array [Array [Float ,0B1_1_0],9],0b1];}Class x7:___l_{Destructor (){ {Var w,eR60,s__Xdi:Array [Array [Array [String ,0x4],634],2];} }}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 297))

    def test_298(self):
        input = '''Class _{_(P_6_:String ;_,F:Array [Array [Int ,0xE],0XF4_4]){}Var $4,Q8:j;Var $3_:JXf;Constructor (__2,C:a){}Constructor (u,__k:i){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 298))

    def test_299(self):
        input = '''Class _{$_(z_,Ap___zw:Boolean ;_:Array [Float ,0b111001]){e::$Q();Continue ;{Return ;} }Var $__m:Boolean ;Constructor (){ {} }Var _,$_:Boolean ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 299))

    def test_300(self):
        input = '''Class o{Constructor (){Return ;}Var n_:String ;}Class _{}Class _:_{}Class _:N{}Class _m{Constructor (_9,_:Boolean ){}$_(_5,__23_:Array [Array [Array [Boolean ,0B10_100],044],0B1_1]){} }Class _{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 300))

    def test_301(self):
        input = '''Class __:_S2h{Var $_c17A_,G:Array [Int ,0X6];Constructor (t,ee,RE,_,B,_____,j:_){Var zy3,_,_jW_,bs,j:String ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 301))

    def test_302(self):
        input = '''Class _:P0_3F{Val _,$T,$5:Int ;Val $_,$k__:D;Var $8,H:Array [String ,06];Val ca:Array [Array [Array [Float ,0XB],02],7];}Class p8{Destructor (){L::$Q();Return ;Continue ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 302))

    def test_303(self):
        input = '''Class _j{l(_,H1_,Za6:Float ;a,__gwnm,_:String ;_,_:Float ){}$4(__,Z6_:String ;_,Y_,_,Zd:W_;W_,W:an){Continue ;} }Class _{}Class _{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 303))

    def test_304(self):
        input = '''Class b_{Destructor (){} }Class _:G6{$T(){} }Class _t3k1_:_R{Constructor (s,_:_;i,__,Cl,_:Array [Boolean ,0x8_0];D,V,De_,__:Float ){Break ;} }Class _{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 304))

    def test_305(self):
        input = '''Class _{_G(LB,_:_wI;_0,X:Int ;_,o:_0_;_3,_4d_,Z_:Boolean ;x____M:Array [Float ,82];_:Array [String ,0101];_:Float ;_,_Ui0V:Boolean ;_:Boolean ;J,____8,Q:Array [String ,0101];_,d2__6Mv49_jy_:Int ;k8_pv:Array [Int ,0X3]){} }Class __:Kg_{Var _:i;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 305))

    def test_306(self):
        input = '''Class _{}Class r{Destructor (){Break ;{} }$j6(i:Array [Array [String ,8],6];Vd_y9:Int ;_,m:Array [Boolean ,3]){Continue ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 306))

    def test_307(self):
        input = '''Class y{Destructor (){} }Class _{z__(_:Array [String ,85];m:Array [Array [Int ,0x2_F7],0B1];bgc,O,_3___xj4o_,_0_:Z2DdW9;Bl,_,D,_:Array [Array [Array [Array [Array [Array [Array [Int ,0X5],04_4420],0B1],07_14],0B11],0b111110],0xA];_,_9,_:Array [Array [Boolean ,50_6],1];e,_,Q_:String ){} }Class _{Val C_3,X,___7,$i:Boolean ;$_1(d_,_:Float ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 307))

    def test_308(self):
        input = '''Class _:L{Val $D,_,$2J:Array [Float ,0xDB];$_40(_:Boolean ;_x_,C,_:Array [Array [Array [Float ,52],0X16],75]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 308))

    def test_309(self):
        input = '''Class _:HI{Constructor (){}Constructor (){} }Class _{Var y90:Boolean ;Constructor (){} }Class Rw3:_{}Class __{Var Cg2_,$_:Array [String ,8];Val m,$_92,_:K_;}Class J{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 309))

    def test_310(self):
        input = '''Class __4{Constructor (O,g:Array [Array [Array [Array [Array [Boolean ,0x53],0X20],0b1],0b1_1_0],0130]){} }Class Z:_{}Class _:_7{}Class _:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 310))

    def test_311(self):
        input = '''Class _{}Class __:K{}Class _:_P{Constructor (){Val Q:Array [Array [Array [Array [Array [Boolean ,0b1],05],015],0xB],0b1000011];Continue ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 311))

    def test_312(self):
        input = '''Class _s:_{Constructor (_:_7587){}Val _5:Array [Array [Array [Array [Array [Int ,054],0B1010111],040],0B11],054];Var _Y:Array [Array [Array [Float ,0b1],0x18],054];Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 312))

    def test_313(self):
        input = '''Class x_9{}Class N{}Class _:_{}Class y_{}Class LzO__:_3{Constructor (_:_;_:Boolean ;__,_01:Array [Float ,8_99]){}A(){} }Class Z_5:G_P{Constructor (){Break ;}Val $2:Array [Array [String ,0B1],07_4];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 313))

    def test_314(self):
        input = '''Class _:_n{}Class O{Val $_i,n:Int ;}Class _{}Class _7dJ:m_Q{}Class __{}Class q:_431{}Class _M{Constructor (){} }Class _{_(_:Array [String ,19_1];_g,_:Int ;_SW:Int ){} }Class Yr7:__{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 314))

    def test_315(self):
        input = '''Class a:_2B81{}Class vJ0:X171{$7(a:Float ;aX,_:Array [Float ,0b1];_9:Array [String ,0124];w___a:Array [Array [Int ,7],3_17]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 315))

    def test_316(self):
        input = '''Class _4__A{}Class _B_:X{}Class w8:_{}Class _3{q9(s:Array [Boolean ,02_4];Pc:Array [Boolean ,0xC];_,_Qr,u:Array [Array [Int ,02_3_2],0xDEFC]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 316))

    def test_317(self):
        input = '''Class _E:_{$g86_s1f0_(){} }Class o_:_2{}Class _O:__{Var _,$1:Array [Array [Int ,0B1],0X5A_F_C4_5];}Class _{Var $7,$M_,$a1,$_:Array [Array [String ,5],0x9];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 317))

    def test_318(self):
        input = '''Class _xMn8:_5_{}Class _:T{}Class R4_{Constructor (_:Array [Array [Array [Boolean ,0125],0X3F],0x4_9_F2_8];S:Boolean ;_A,_F:D){}$_(_,y,_:_;S6,_,_,u,Ux_4y:_){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 318))

    def test_319(self):
        input = '''Class _x:_94{Var __DJ,$T_:Array [Array [Array [Float ,021],0XE47],63];}Class x{n(){}m(_,_:String ){g::$71()._();} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 319))

    def test_320(self):
        input = '''Class V:w{}Class __I7_:l_{}Class __{}Class _0X:z_{}Class ___Q{$_a(_k,V,_:M_;_,R1,z:Float ;__:String ){Break ;}Var p_:Int ;Destructor (){}Var _7,_:_;}Class p9:b{Val $_,f4:String ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 320))

    def test_321(self):
        input = '''Class fm{Var i:__p7m_;}Class r:J__AS{Val $A,$KS_,$J:Array [Array [Array [String ,0X4C],077],077];Constructor (){} }Class __{}Class _{Val $0:g;}Class _{Destructor (){} }Class p6l{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 321))

    def test_322(self):
        input = '''Class R_7:_{Destructor (){Continue ;} }Class _{$6(l:Array [Array [Array [Array [Float ,0B11],67],0x46],0B1];n,r__x3099:Array [Int ,0302]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 322))

    def test_323(self):
        input = '''Class HJ:JPU2{_5_k(){Continue ;{}Break ;} }Class b:_2K{}Class _5_T{}Class P__r_{}Class _:m2{Val $7,_r7:Array [Boolean ,6_8_9];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 323))

    def test_324(self):
        input = '''Class t{Var $_4,_:Array [Array [Array [Array [Array [Array [Array [Int ,0x55],0115],0B100000],0XF_2],31],0115],0115];Val $jB6:Float ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 324))

    def test_325(self):
        input = '''Class _:_S__7{}Class H:_{Var L__:_;}Class P2:_{_(__4,B94,_d4I:_;_:_1;O_3,jb,N,yG:Array [Array [Array [Int ,0X2B],0B1101],040]){}Constructor (){}Destructor (){}Constructor (aU0:Boolean ;o,_:Array [Int ,0B1101];__U,A:Array [Array [Array [Array [Float ,0b1],06],040],3]){} }Class Z_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 325))

    def test_326(self):
        input = '''Class y{Constructor (){Break ;}Constructor (_,__9_,__:Array [Array [Int ,0B1_00_10],23];_,U,___9,_,I6k,n:String ;o:V;_,n:o){}Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 326))

    def test_327(self):
        input = '''Class h5:___k{Constructor (_u_M,_:Int ;_:Array [Boolean ,0b110_0];S,__0,Y___9E:A;j_:Array [Array [Array [Array [Boolean ,0X4],0b10110],017],61]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 327))

    def test_328(self):
        input = '''Class __{Val __,tQ:_2;}Class _:_d{Val $_:Array [Array [Array [Array [Array [Array [Array [Int ,07],3],9_1],0b10001],0x90],0102],70];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 328))

    def test_329(self):
        input = '''Class _1K{}Class _:_{}Class u_{Var $_,$9,__,$9,_,$__,_,$_:String ;}Class _:_{}Class g6{Constructor (){}Constructor (_:Array [String ,0xC];_RL,tU:Float ;j5:Boolean ;x2,_3:Boolean ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 329))

    def test_330(self):
        input = '''Class _U_{Constructor (_0T,SZ6H60BK,k:ixY;_:Array [Array [Array [Array [Boolean ,83],0B1010001],0X5E],1];K,U,_5_:Array [Array [Int ,0B1010001],05]){}Constructor (){Continue ;}Var $__:Array [Float ,0X5E];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 330))

    def test_331(self):
        input = '''Class K{$29_(_:Float ;_,q:Float ;_:Array [Int ,0b1];ku_8,_5_:Array [Array [Int ,0B1],0102];_,Ed,_,b:a_){} }Class _vH{Val $_2p3,$Kn1:Array [Float ,0102];Destructor (){} }Class L683:_n3_k29o5_{}Class N0__:__{Destructor (){} }Class z{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 331))

    def test_332(self):
        input = '''Class aK{}Class _4{Destructor (){}Destructor (){}Val _e_90,WY:Array [Array [Int ,0X339],0B11];Constructor (VL_2_,Q3,__6_:_;MD0,_:K0;aq1H6_,__7:Array [Array [Boolean ,02_44_4_14_7_5],0b1]){Return ;}Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 332))

    def test_333(self):
        input = '''Class _:y6_{Var $__,$P_:Array [Array [Array [Array [Array [Array [String ,0X9_AA6C7],04],0X3],0B1100000],0X5],07];}Class e{$4(Xh_:___i){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 333))

    def test_334(self):
        input = '''Class _:_{$_W(__,_:Float ;_:Array [Int ,40];_:Boolean ;f:_8;_,_R:String ){t::$8();}Constructor (){}Constructor (){Return ;}Constructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 334))

    def test_335(self):
        input = '''Class _:Q{Constructor (){Break ;}Var a:Array [Array [Array [Array [Array [Array [Float ,02],07_5],041],0XF6B_F_D1],0x64],0x59_7];}Class Y:q{}Class _:_20{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 335))

    def test_336(self):
        input = '''Class a__:_{}Class m2:G{Destructor (){ {} }}Class K4:_{$5_(){}Val $_:q_;Constructor (n:Int ){Break ;} }Class _pj_:_5{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 336))

    def test_337(self):
        input = '''Class hue__:_x_{Destructor (){}Constructor (_,_,_:H){}Constructor (A,j,N,Im:Array [Array [Array [Array [Array [Array [Array [Array [Array [Array [Float ,07],0X2A],0B11_1_1_11],51],3],0b1],01],02_0],47],0X2A]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 337))

    def test_338(self):
        input = '''Class I__j:s{}Class _9{}Class xY7___:JG_{}Class q_3_{F_4WY9(J,___v:String ;eh0,_lt,u,p:Boolean ){}Var $4:String ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 338))

    def test_339(self):
        input = '''Class g365{Var _4__,$J:Array [Boolean ,0b1];Destructor (){Continue ;Break ;Continue ;Break ;} }Class k:_{Constructor (__t,_:Array [Float ,070];_075:Array [Float ,0x38]){} }Class _5_Z:F01{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 339))

    def test_340(self):
        input = '''Class PU:q{___(_,ps_:Array [Array [Array [Array [String ,2],0b11011],0b1],0X47]){Val M:Array [Int ,0b1];} }Class XQ_:_5G{Constructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 340))

    def test_341(self):
        input = '''Class _{Var $b,$__:__X_;Val $_,$__:Array [Boolean ,100];}Class _:__C{Constructor (_,_U_:Array [Array [Array [Boolean ,3_3_1],03],024_45_2];yB_:_){}Constructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 341))

    def test_342(self):
        input = '''Class K:_{Destructor (){}Var $_:Float ;}Class o:_{Var $_,$2:__O;Val $_3K:Array [Boolean ,047];$O(M,_06,f:NF){Var _,_T:__;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 342))

    def test_343(self):
        input = '''Class _:B{Constructor (L,_2jgY,U,HaO,_:Boolean ;c:Array [Boolean ,024];__m_,s9_,r:Array [Float ,03]){Break ;} }Class ad{Val $H:_U;Val $A:Int ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 343))

    def test_344(self):
        input = '''Class Tf_L{}Class e6j8:H{Destructor (){} }Class _I{}Class n:tiK5{Val y:String ;Var $_t:n;Var $dO4:Float ;}Class q:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 344))

    def test_345(self):
        input = '''Class _3r8:_{Var $3J:Array [Boolean ,064];Constructor (b:String ){} }Class v_1G06{Constructor (v,__,_6_,_:Array [Array [Array [Boolean ,064],5],035];i,_,_:Array [String ,0b10110]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 345))

    def test_346(self):
        input = '''Class _:_{Val D,j:Array [Array [Array [Array [Array [Array [Array [Array [Float ,0xE],0B100001],33],4_1],33],35],0XE1],0X8];Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 346))

    def test_347(self):
        input = '''Class F:f{}Class Ot_3:JS{Var $_8_:Array [Array [Array [Array [Array [Array [String ,0X48],0x9],4_9_5],07],0B101011],0b100000];}Class c{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 347))

    def test_348(self):
        input = '''Class e{Val _:_8_G7_p_3;$90R(_:l){} }Class U:x{}Class Z{Val R,$7oS,$YS,$7IG,$J:_;Constructor (){}I92(){Val t:_;}$_(_58_VQ:_;tv5:String ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 348))

    def test_349(self):
        input = '''Class _2{Destructor (){}Constructor (){} }Class _s8:u6_9T{Var __:B1;Val $9,$2:Array [Array [Array [Array [Int ,18],054],0X31],06];}Class _x{}Class _D__0:U9Y{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 349))

    def test_350(self):
        input = '''Class y{Var _:Array [Array [String ,0b1],0B10101];}Class va:_{$_(_3,__1r21,_y,H,_5,_,x336_,_:Array [Array [Array [Array [Array [Boolean ,7],0x4],066],04],0X16];_:Array [Int ,0x4]){ {{} }} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 350))

    def test_351(self):
        input = '''Class _{Destructor (){} }Class gG2:_8_8{}Class q_0f:Z1_y{}Class x{}Class _{Val _8:Zy;}Class _K1:j{Val G,_:Array [Array [Array [String ,0B1001100],0B1],0X16];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 351))

    def test_352(self):
        input = '''Class _P_:_n{Destructor (){}Constructor (_:String ;_16_7:_;N_,N:Gn0__k){} }Class ___{}Class _{_(){ {Var I:String ;} }_1(){ {Break ;} }}Class d:y5f_{_zO(){} }Class V_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 352))

    def test_353(self):
        input = '''Class g:_{Val $6:n;Var $o:Array [Array [Array [Int ,0B10101],0B1_1],85];}Class _{Val qp,$Rt,$4M_,$q_:Array [Array [String ,0XF2],033];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 353))

    def test_354(self):
        input = '''Class H:_{Val Jn6:Float ;Val _bs_:__;Var $G:Array [Array [Boolean ,05_5_6],0XA];Constructor (){} }Class y{Destructor (){}Constructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 354))

    def test_355(self):
        input = '''Class C44{Var $__:Array [Boolean ,04_3];t__(_9:l_2sJ;N8,F2,i1:Array [Boolean ,0b100000];_N:Float ){Val _4,h5_,__0,jSp:Array [Array [String ,0XB],0B11];} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 355))

    def test_356(self):
        input = '''Class _6:_{Val O6,_T8:Array [Int ,022];Var $_,O:Array [Array [Array [Array [Array [Array [Array [Array [Boolean ,0125],2],0xB],0XB],0b111000],0125],0x1_A],19];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 356))

    def test_357(self):
        input = '''Class _{Constructor (b2_67G:Array [String ,5];j_,_992:Array [Array [Boolean ,0X1F],23];H,_,_,Q_,_j:_891){}Var $p,_:Array [Boolean ,03];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 357))

    def test_358(self):
        input = '''Class _{Constructor (W9___93y,Y:Array [Float ,93_6];D52:Array [Int ,0xE];_,L:Array [Int ,0xC]){ {}Return ;}Destructor (){}Var $2_,_HE3_XtoH45:_W;Destructor (){} }Class __{}Class ___{}Class T2{}Class _g:Z{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 358))

    def test_359(self):
        input = '''Class _y0{_(){Break ;b::$8_U_();} }Class __c{$4_(nT:_97;_Y__I6:Array [Boolean ,49];i,_:Float ;k,AD3a:i4){} }Class t0{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 359))

    def test_360(self):
        input = '''Class _:_7{}Class __P3_v{_Q0Lf_0_(_:Array [Array [Array [Array [Float ,0b11010],0B1],1],034];YN,l,K0_:Array [Array [Array [Array [Array [Boolean ,0b1_0_01],01],07_4],034],91];__:Array [Array [Array [Boolean ,0b110],0X26],0x8];g_4,g5:a){} }Class u:y{}Class _:_{Var $7,x_:Array [String ,034];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 360))

    def test_361(self):
        input = '''Class _:yU_{}Class u3{Constructor (_Q:Array [Array [Int ,057],0x7];M4:Vb46){} }Class O4:s4i{Val _7e:Array [Array [Boolean ,7],9];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 361))

    def test_362(self):
        input = '''Class Hw_:T{Var u:OE5;Constructor (W9:String ;_:Array [Array [Array [Boolean ,0XFB_7],0b1],63];_F0,y:Int ){}Constructor (_:Int ;_1y_B:String ){}Constructor (){}$_6z_0(){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 362))

    def test_363(self):
        input = '''Class v:c{}Class JA_Vqk2:_6_{Constructor (_,z,___3:Array [Array [Array [String ,066],0xB_D69],0x39]){} }Class M{}Class b_6:G{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 363))

    def test_364(self):
        input = '''Class _w{}Class _:_{Destructor (){} }Class P_8Z{Var _:Array [Array [Array [Array [String ,0X5],0106],03],0106];Constructor (H:Int ){Break ;Continue ;Break ;Var _:m;{} }}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 364))

    def test_365(self):
        input = '''Class cm{Val $_6b__:Array [Array [Array [Array [Array [Array [Int ,06],0X4],05],9],2],49];Destructor (){_48__::$49();}$_(){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 365))

    def test_366(self):
        input = '''Class x{}Class w{Val D:__;Val $5,$_:Array [Array [Array [Array [Array [String ,0B1011011],0b1_1],0B10],054],0x5_ABD_D];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 366))

    def test_367(self):
        input = '''Class S:_N_{Constructor (X,p:Array [Array [String ,0x57],21]){}Destructor (){} }Class _{$0(u,B,BD:_0;I:Float ;_:String ){}Val Ax:E_A;Destructor (){} }Class V{}Class W{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 367))

    def test_368(self):
        input = '''Class _{Constructor (Ou_,Y,_7,g,_,Y,_:Array [Float ,04];_HzH_9C:Array [String ,0XD];__,__6:Int ){Var __:String ;M::$675_80c.E.u._._();}Var $0:_9;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 368))

    def test_369(self):
        input = '''Class x_{}Class R:oO_{Constructor (_,a:Array [Array [Array [Array [Array [Int ,0X3B],0100],5_9_8],0X8],0b1_1_1];P,_,S,K,_:Array [Array [Array [String ,422],0B1011001],015_2_074_75];y,_F,_:_){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 369))

    def test_370(self):
        input = '''Class m_:_9{Destructor (){} }Class E{}Class D{Constructor (_,_8_V_:_;_,P1,_,v_:Array [Array [Boolean ,0b100101],0X46];_,C,q:Array [Array [Int ,0x9],0b100101]){} }Class _{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 370))

    def test_371(self):
        input = '''Class i_HN_o2:_{}Class u:DA__{Var $31,$45:Int ;Constructor (n8:String ){}Constructor (q:Boolean ){}Var $_,pG,$9___,$49_,$Q,C:Boolean ;}Class _:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 371))

    def test_372(self):
        input = '''Class I_{}Class _P{Val $6F3,$M:String ;Constructor (gK:Int ;_,b:Int ;__2:Array [Array [Float ,0b110111],61]){Break ;}Destructor (){} }Class __Q:i1{Val $9_G,v_f3,$W:Array [Array [String ,0122],0x63];$7(){}Constructor (W:Array [Boolean ,0B10];E,c:Boolean ){}Val _,$3:_;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 372))

    def test_373(self):
        input = '''Class _:I_F{$f(___:Array [Array [Array [Array [Array [Array [Array [Array [Array [Array [String ,0XA],1],0b1010010],0X17],0b1010010],0b1010010],0b1010010],031],0XC],9];_r,_,__6_:Float ){Break ;}Var $P,_,_,$_,a:_8;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 373))

    def test_374(self):
        input = '''Class F_{K(){}k(){Break ;} }Class y{}Class c:A{}Class A{$__(_2,S,_J_P:Array [Array [Boolean ,3],1];X:Array [Array [Array [Boolean ,01],0XB],1];_,_b__,Z__:A;_,_,_9_,_,_:Float ;_:Int ;w___,x:String ){} }Class _{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 374))

    def test_375(self):
        input = '''Class _:_{$p__(){Return ;Return ;New z1_().__7P();}C(c:Boolean ){} }Class _{$a5(_G:_p;_:Float ){} }Class _{}Class B:_X{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 375))

    def test_376(self):
        input = '''Class ___a_AlE{$_(o,kD_7,k,l,K,_:Boolean ;_3_,_q7:Array [Array [Array [Float ,0B1011111],3],04]){} }Class _{Val o11,_:R03;Val _1_:Float ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 376))

    def test_377(self):
        input = '''Class u:k_1_{Val _9:Float ;Constructor (_,P:Int ){}Constructor (hVog,_85,l_CY,_d9,w5H__:Array [Array [Boolean ,89],89];_:Array [Float ,0x15]){Continue ;_::$d();} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 377))

    def test_378(self):
        input = '''Class _:a{$c(___4,K:Array [Boolean ,0xD];S0NWi:Array [Array [Array [Array [Float ,0B1],0b1],0B1100],055];Z2P,D2228_:Array [Boolean ,055]){}$__(){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 378))

    def test_379(self):
        input = '''Class U:_7{Var $_:Array [Array [Array [Array [Array [Array [Array [Array [Array [Array [Array [String ,0b1011101],056],6],43],056],0b1011101],0b1],0B110],064],4_9],0X8];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 379))

    def test_380(self):
        input = '''Class bF_0_{}Class __:___v2_f8kn{}Class f:uaX{Var _:Array [Array [Array [String ,051],0b1],0B1_10];}Class _:_7{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 380))

    def test_381(self):
        input = '''Class p9:W{}Class _{Constructor (_f_,_O,_,J,gO5,__:String ;__I5,_,__,_,hH4,_,D5:H;dS:Float ){} }Class r{}Class PV:M{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 381))

    def test_382(self):
        input = '''Class J:XJ___0{Constructor (C4:Array [Array [Array [Array [Array [Array [Boolean ,0x56],01_0],0X4C],95],95],0XD_7]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 382))

    def test_383(self):
        input = '''Class pY{$0(_,_:Array [Array [Int ,0B1],04_5_2];J,_,j__h:_8_;_:E_;_:Array [Array [Array [Float ,0xD7],0b1010000],0b1010000];_u:Array [Array [Float ,5],05_7];_6d:X7t;_ba,S:_V){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 383))

    def test_384(self):
        input = '''Class N{$P(_tLMF,_:IMm;j,_u,_0B:Int ;_Q,_zO,b:Array [Boolean ,0X4_A];___50,_4:Array [Int ,041];c___Z,O_:Array [Boolean ,0B1011111];_,_:Boolean ;QW_,B_,_6S:Float ;w_c_:Boolean ){} }Class CH2_f:I_8_{}Class _:_3{}Class _{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 384))

    def test_385(self):
        input = '''Class s{Constructor (W,Zy,_W,o_:Array [Array [Array [Array [Array [Array [Int ,0x36],044],02_5_4462_1],48],0x65],48]){}d0(q:Boolean ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 385))

    def test_386(self):
        input = '''Class nt9h{S(_:Int ;b:Array [Array [Array [Array [Array [Boolean ,0X7],7],0X8],0b10110],0B1];__q_9,i_:___iCU){ {} }}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 386))

    def test_387(self):
        input = '''Class _{____f(_3_S2:_;_d4,t:String ;_,_,_2:_;ny,o3,_,q_:Float ){}Constructor (vP0:N_3;g,_2,_:Int ){}Val _2,ck__,_4:Array [Array [Float ,1],1];}Class w_{Constructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 387))

    def test_388(self):
        input = '''Class ___:u{Constructor (){ {Continue ;} }}Class g:p_{Destructor (){} }Class W:__{$X6_(){} }Class _{Val __3:Boolean ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 388))

    def test_389(self):
        input = '''Class _:_8M_3{$r7_(_:Array [Array [Float ,0B100101],01];X_:_;_Q,l_:Array [Array [Array [Boolean ,0x58E_5_86],0b1011011],0x15]){}Val $9:Float ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 389))

    def test_390(self):
        input = '''Class c:_2{Constructor (__,ZP9__,__M,p,_0,_G:n){}$_6(){}Var $R:Boolean ;}Class __:_{}Class F2_:J7{Var _:Array [Array [Array [Array [Float ,0B1011110],0x5],04_6],041];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 390))

    def test_391(self):
        input = '''Class __{Destructor (){}Val $_,$_:Boolean ;Constructor (G_2:_){New Cn6().__f();}$__2(z6,dm_:Array [Array [Array [Array [String ,0b1],1],0B1010110],0x33];_:_){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 391))

    def test_392(self):
        input = '''Class __1{}Class oN{Destructor (){Continue ;Break ;Val Of_:Array [Array [Array [Array [Array [String ,99_2],057],0B1_1],041],0b1000011];_::$Q();}Val $r6,$_:Int ;}Class Txi{Val _:M;Var KF:Array [Array [Array [String ,93],0B1011],93];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 392))

    def test_393(self):
        input = '''Class y__:_3{}Class __:_{Val $J,_,T_,$1,d__35,I_46G_5,$0_8,$6:Array [Array [Boolean ,0x34],041];}Class __:n{$d(_l,U:Float ;j_,_3,q,Z_:Array [Boolean ,7]){} }Class VO607_:_{Constructor (_54,rt:Array [String ,0B11]){}Destructor (){}Constructor (){} }Class _:j{}Class f__xV{}Class _0:_{}Class _:IL{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 393))

    def test_394(self):
        input = '''Class gB_:pW47__{}Class S3J7:_{}Class __:_{Var $2h48h_,$C5_,$9d__:_;Constructor (_:Array [Boolean ,031];__:Boolean ){} }Class A:d{}Class HX_O{}Class _:d_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 394))

    def test_395(self):
        input = '''Class _9{Constructor (_,m:Array [Array [Array [Array [Array [Boolean ,054],0b111010],6],5],0XE];W:Array [Boolean ,19]){}Var $a:String ;Val $1_,$a,$_:_;Destructor (){Return ;}Constructor (){Val E,_:Array [Array [Float ,0xB7],19];}Constructor (p_I:L__;_V,Q_:Array [Array [Boolean ,054],77_7];i,__:Array [String ,19]){ {} }}Class _:_{}Class __o_2_:d{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 395))

    def test_396(self):
        input = '''Class _Q534:D{}Class CxU_:_{Constructor (yYvB_,_:Array [Array [Array [Int ,0x40],7],0XC_2]){ {} }}Class __:_LV5{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 396))

    def test_397(self):
        input = '''Class g:_{Var $P_N_:_Y__;z(){}Var $L_:String ;Constructor (s,_8i3R_:String ;__I:Array [Boolean ,0xDF_2]){Continue ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 397))

    def test_398(self):
        input = '''Class ___X{Destructor (){Var __:X;} }Class _3{J_(Ms,Y0,Y1_,Ur_:String ){Var k5i,O,S,_:Array [Int ,0b101];Continue ;} }Class K_O{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 398))

    def test_399(self):
        input = '''Class k5{Destructor (){Break ;}Destructor (){Val N,_,_,_b:h;Var L:Boolean ;}Constructor (C:h_ERm379_0m9;D:_4){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 399))

    def test_400(self):
        input = '''Class _9{Var A:_;Constructor (s,_:F__1_n){}Constructor (wu:_){}Val p_,_3:Int ;___(){} }Class R83__:_{Var I:Int ;Destructor (){}Var $_:Array [Boolean ,0121];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 400))

    def test_401(self):
        input = '''Class _:_{}Class ___:X{Constructor (_0,x_8_,h:a;_A38:Array [Boolean ,0x5B];_9_,_l8,B:Array [Float ,0XCB]){Continue ;} }Class z{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 401))

    def test_402(self):
        input = '''Class _:_{}Class m:_{Destructor (){Break ;Val __hL:__;Continue ;Continue ;} }Class n6:_{}Class _{Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 402))

    def test_403(self):
        input = '''Class ur:dX{}Class _:_{Constructor (){Return ;0B10._.U_()._h_9__s_();BP93::$3_.a();Continue ;Continue ;} }Class r_4_{}Class F_2{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 403))

    def test_404(self):
        input = '''Class n8_{}Class QI674:X9{}Class _{Val $5_,_,$p_,z,_H_,__,$1:Array [Array [Array [Array [Boolean ,06_32],057],0b1_10],057];}Class K:_R_a63{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 404))

    def test_405(self):
        input = '''Class _:_6_{}Class _26_Y:_Ob0C{Var _:E;}Class I_:DtO{Destructor (){} }Class J:__5V{Val $y,$s:Boolean ;}Class YuX{}Class _58{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 405))

    def test_406(self):
        input = '''Class O{Var _,i:Array [Array [Boolean ,0b10001],0x44];$6vC__(__:Array [Boolean ,07_76]){}Val $7,_91,m_7_5e_,$T:_H;}Class P:_{}Class r6__{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 406))

    def test_407(self):
        input = '''Class _:_I{Destructor (){}Constructor (be_:___){Continue ;}Val h1,$N:____;Val F:Array [Array [Float ,0b1011101],0xB];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 407))

    def test_408(self):
        input = '''Class _{Var $qw_8,R_Jl:Int ;Val $3:Array [Array [Array [Array [Array [Array [Float ,0b1],0X32],72],056],0B1],8_0];}Class V53{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 408))

    def test_409(self):
        input = '''Class _rr:__8{}Class _0:X6{Constructor (__2N:hs;s,wl9:Array [Float ,06_2];_e:Boolean ;dx,_3,F__4,__:Float ;U:Array [String ,0b1_1];_,_:Boolean ;_:String ){}Var $_97:String ;Destructor (){Continue ;N::$_();} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 409))

    def test_410(self):
        input = '''Class H0{}Class S:c{$_(J_:Array [Array [Array [Float ,065],42],0B1000010]){} }Class _Q:L1f{Var _,$e206,$N_,G:Array [Array [Array [Array [Array [Int ,0X48],0B1000010],03],5],065];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 410))

    def test_411(self):
        input = '''Class _A{Var _:Array [Array [Int ,8],0x2E];Val _0:Array [String ,0B1];Destructor (){}_E5(){Val _:Array [Boolean ,0b1_0_10];} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 411))

    def test_412(self):
        input = '''Class t:P{Var $yO,$N_:Array [Array [Array [Boolean ,8],0XA_3],06];Val $V__5D:_16;Constructor (_:__;Z_953:Array [Array [String ,3],0b1_01];y:Float ;o:Float ){Continue ;Break ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 412))

    def test_413(self):
        input = '''Class I_:m{Constructor (S__,Q,Fj,_8a,b:Array [Array [Array [Array [Array [Boolean ,0XA],5],5],056],0b1010011]){Break ;Break ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 413))

    def test_414(self):
        input = '''Class _92:_{}Class P1{}Class eg2l_:_2{Constructor (_,K_,_,iUZQ:Array [Array [Array [Float ,0xE],8],0xE]){} }Class f:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 414))

    def test_415(self):
        input = '''Class S{Destructor (){}M4(){}$_8_(_Bs0,y,_y_Q0__,Hi:_S;Bb_U6y,_BF_:String ;_,_:_;_,B_2:String ){}$LLU(_i:Array [Int ,0x1A];W,_,_95:Array [Array [Array [Array [Int ,0B1],0b1_0_0],0x1A],051]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 415))

    def test_416(self):
        input = '''Class _{Constructor (_:_n){} }Class N2:b{Constructor (){}Constructor (r_,_5X6,_:Array [Array [String ,0xA],056]){Return ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 416))

    def test_417(self):
        input = '''Class S:_{}Class _:_{Val n3y693_:Float ;Constructor (RV_,K:Boolean ;h,t:M){}$1T__(h,Q:D9;v:_){} }Class _:l1{Val $__,t:Boolean ;Constructor (ED:Int ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 417))

    def test_418(self):
        input = '''Class _:A_{}Class Z2_b:prJ{Constructor (_,__z,P:Array [Array [Int ,2],025];F4:Array [Int ,01];_:Int ;__:Array [Float ,0X25]){} }Class _:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 418))

    def test_419(self):
        input = '''Class __B1:__{_3_(A:Array [Array [Array [Int ,051],0X22],0X22];_,_9:U;_d,_:Array [Array [Array [Boolean ,3_6],2_2],0B1]){Break ;}Val $___:Array [String ,0b11011];Val $c,_:Boolean ;}Class P:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 419))

    def test_420(self):
        input = '''Class d:O{U(){}Constructor (_:Array [Boolean ,023];IP:a14_V;r,_,_W,_:Array [Boolean ,023]){Continue ;}Constructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 420))

    def test_421(self):
        input = '''Class _O{Constructor (_8qLK:Array [Boolean ,9_4];_,_:String ){Break ;Break ;} }Class c_{}Class _7:n63914{Var _:__;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 421))

    def test_422(self):
        input = '''Class j{Constructor (x_mNj_,t:Float ;_ITI_w,V,m:Array [Boolean ,0B1100010]){}Constructor (){Return ;} }Class _sZ{}Class i:R{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 422))

    def test_423(self):
        input = '''Class o6{Val $w:Float ;Var $m,_m_b_T,__,b6,uW:Boolean ;Constructor (j,_4:k5653;S_x:Boolean ;__,_:_){} }Class _:L{}Class U:_F{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 423))

    def test_424(self):
        input = '''Class _{p(u,f:Int ;e2:Array [Boolean ,062];_:Array [String ,2];_:Array [Array [Array [Array [Boolean ,0X1D],0x3B],0B1],0B101011]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 424))

    def test_425(self):
        input = '''Class H{Val $_95,_P_,$xt,$_v,Cl:String ;Val o,_,$5:Array [Array [Boolean ,0B1],07];}Class W:___9{Constructor (_9,DA__:Boolean ;Q_,_0_K,_3_:N){}Val $n:l5;Var $L_:Float ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 425))

    def test_426(self):
        input = '''Class w{Val $C,$Z:Array [Array [Array [Array [Array [Array [Array [Array [Int ,0114],9_5],0x43],0x43],0b101011],80],01_4],0x2];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 426))

    def test_427(self):
        input = '''Class d6:Wr{_(b:Int ){Val _,K5_:Float ;}Constructor (){}Constructor (vy,d,_,_,V,N:_i){} }Class _V_{}Class t_Q{Var _,$h5__:String ;Val $kf_:Array [Int ,0x3C];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 427))

    def test_428(self):
        input = '''Class _:V{Constructor (_:String ;C,oc,__w,h,v___9:Array [Float ,0X25];l,_:Array [Array [Array [Boolean ,0X3],0140],0B101001]){} }Class _:m{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 428))

    def test_429(self):
        input = '''Class R{Constructor (){} }Class __{}Class CP{Val _:_6;_7_(_,d,M_e:Array [Array [Array [Array [Boolean ,01_0_5],9],0b1],0143]){}Var _,_,F:s;Constructor (F:Boolean ;k:String ;E,v:H7){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 429))

    def test_430(self):
        input = '''Class _:_{Constructor (j,YS,__:Array [Array [Array [Array [Float ,0b111_111],0x27],0b1],2_3];M5,M_P,M8:String ;ix,c,f:x){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 430))

    def test_431(self):
        input = '''Class Cv{Constructor (){Var _,F5:__2;Break ;_::$75._().o30X3();}h(C:_;d,g_,K,f_:_;_eu:__){}Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 431))

    def test_432(self):
        input = '''Class ___T__3x:r{$9O(_D7m0yM__l_71Ed1_,b:Array [Array [String ,0x1],0b1_1_0_10]){}Var $__,$P,I79_8,$B,$_38,o,c_3M____,_,L:Int ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 432))

    def test_433(self):
        input = '''Class _6_{Var $_,$_1_:Array [Float ,02_6];Var _,$R,$hI0,Pt,__,$_Z1,$_JT_,$s:Array [Array [String ,01_6],02];}Class g:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 433))

    def test_434(self):
        input = '''Class _:X6{}Class _:_K5j_{Var $4,$5,$D:Array [Array [Array [Int ,051],12],2];Constructor (){ {} }}Class _:Mn{Val $_:Boolean ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 434))

    def test_435(self):
        input = '''Class c:s{}Class _{Constructor (){c::$_F();Break ;} }Class I{Val $45L:Array [Array [Boolean ,0B11],051_6_7];Fz(w:Array [Float ,0x59]){Continue ;{} }Var $_,_,$8,_9xO,$_:String ;}Class l:H{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 435))

    def test_436(self):
        input = '''Class _:o{}Class L60{Val $4,_,$4,$2,Y,_mK,pd_9,$0_,_,$VX1v:Boolean ;Constructor (Ig_11,a,__y,_V:Array [String ,47]){}Mu4909(){} }Class U{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 436))

    def test_437(self):
        input = '''Class _i5ipf__:G_{}Class __6:_{$_(c_oH_,L,_,_9,____TF:_K;_,q4,_g:Array [Array [Boolean ,0XE],0b10]){Continue ;}Var $x,$d,$6,l895:Boolean ;}Class N_7:r{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 437))

    def test_438(self):
        input = '''Class ei1{}Class __P6{Val $2,_:Int ;Var X,h:Array [Array [Float ,9_5_4_9],4];Destructor (){Continue ;}Var $a:Array [Array [String ,0x22],0B111001];}Class __{Var _:X;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 438))

    def test_439(self):
        input = '''Class _14:_1631{$C1(_,__i:Array [Array [Float ,017],05];l:Array [Float ,0b101001]){Break ;Var _M,K:Array [Array [Int ,0B110],43];} }Class _E_Q{}Class _{}Class _7{}Class _{}Class _3:_{Destructor (){}Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 439))

    def test_440(self):
        input = '''Class _YlB_{}Class _n5:J{Destructor (){}Val y,$p:NqG1;Destructor (){} }Class v{Var _8,$6,$61,$gA:Boolean ;}Class __t{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 440))

    def test_441(self):
        input = '''Class _G:h{}Class _:__q{_(_:String ){}Val $7:Array [Boolean ,4];$_(){}Constructor (){}Var W9:Array [Array [Boolean ,0X9_F],94];}Class D:_{}Class McV{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 441))

    def test_442(self):
        input = '''Class __W:_7_{Val $_,P_,_,$8u_1:H4D;}Class ju_:G9{Val _Zy:Array [Array [Array [Array [Array [Int ,05],0X4A],0B1010010],13],0b100110];}Class l{}Class _{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 442))

    def test_443(self):
        input = '''Class _7{Var M0_:Array [Array [String ,0X5B],74_4];Val v_,_,$8_7,_:Array [Array [Array [Array [Array [Array [Array [Int ,0XEE],5],0X5B],0b1_00],50],025],06];}Class r_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 443))

    def test_444(self):
        input = '''Class X:J{Var T,m__iRG,__7,U_h,_:Array [Array [Array [Array [Float ,0b111],0b1],06_553_2],033];Val $__,_,$W:K;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 444))

    def test_445(self):
        input = '''Class _{}Class _{Constructor (){}$e9_i(){Break ;} }Class __:Mk{}Class x:B{Var Y,_1Z,$K,Rb,tTv_:Array [String ,05];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 445))

    def test_446(self):
        input = '''Class l:_0{Val x:Array [Array [Array [String ,01_3_6],82],82];Constructor (CBGn3_,__:Int ;_6,___i,WB,lgUE_:Array [Array [Boolean ,0x8],0136];V:Array [Float ,0B1100011];D,_63x,Z_:Array [Int ,0136];v_:D;_i:e;__,_G2:__;y_:_){ {} }Constructor (){} }Class Y:J{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 446))

    def test_447(self):
        input = '''Class __9{$J(x_X,X_x,Q,D,_:_;qF0_o:Array [Array [Array [Float ,0X31],14],0X31];l,_,_:_;____,G:_H_){} }Class G2:_{Var $N9Q:__;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 447))

    def test_448(self):
        input = '''Class _{}Class _:gnH____0_6{Destructor (){Q::$_();} }Class p__7{Var $05,$__:Array [Array [Array [Array [Boolean ,0B1],41],0x43],41];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 448))

    def test_449(self):
        input = '''Class l{$_(r_:D;B_:Int ;_k:_h;_6p:Float ;K,lf_5:Array [Float ,79];_:Array [Array [Array [Array [Float ,79],011],0xAC],2];_05,_1,Y_Q:u4){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 449))

    def test_450(self):
        input = '''Class _9{i(_4:_){ {}Return ;}Val m_,m,$9,_1,$x,g,$9:Boolean ;Var $1:Array [Array [Array [String ,0B110101],6_2],037];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 450))

    def test_451(self):
        input = '''Class T{}Class M{}Class C{Constructor (){Continue ;}J(_,YI,p,P:Array [Float ,31];_i:p;_5_,_:Array [String ,0B1]){}Val _:Array [Float ,795];_pW(){Break ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 451))

    def test_452(self):
        input = '''Class D_o98{Constructor (p_N,c:Array [Boolean ,1_216];_:Array [Array [Array [String ,0X27],63],07];D,__:Array [Boolean ,03]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 452))

    def test_453(self):
        input = '''Class t_{Var $G_1:Float ;Var $5_:Array [Array [Array [String ,0B1_1],0B1011100],056];}Class O{}Class w:Av{Val _:_;$5(){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 453))

    def test_454(self):
        input = '''Class _{$___(_:Array [Array [Array [Array [Array [Array [Float ,1_4_3],0XA],1_5889],97],0x2D],0x9_345];_,V02:Boolean ;_bN___:String ){}Val __R__:Array [Array [Array [Float ,97],027],02];}Class n{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 454))

    def test_455(self):
        input = '''Class __{Destructor (){} }Class _{Constructor (_d:Int ){} }Class _:Q{}Class L_7:p{Val c,Y:Array [Array [Boolean ,0B1000101],0b1];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 455))

    def test_456(self):
        input = '''Class U_:_{Constructor (_S:Array [Array [Boolean ,0X20],0x6];S_,e_,_,D:Array [Int ,1];_,q_:Array [Boolean ,0b10011]){Break ;}Val v,__,$_:Array [Int ,0X20];}Class _:_86w{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 456))

    def test_457(self):
        input = '''Class F:_7_9{}Class h_:_uH_{Val $O:Boolean ;Var $_,$_To,$8_Z:Array [Boolean ,0X1];Var $4,_:Array [Boolean ,0x947_E];Constructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 457))

    def test_458(self):
        input = '''Class GRx:p4{}Class _{Constructor (N7,J3_:Array [Int ,67];i2:Y;_S:Q_m){} }Class z1{Val $6_3,$8pR,HZ:l28__g;}Class Ql_B{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 458))

    def test_459(self):
        input = '''Class E5_{Val $9_,h,$_8__:Array [Array [Array [String ,0b1010010],0x2],0X64];}Class _{Constructor (_,_,_56P,C_:String ){} }Class v:_9{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 459))

    def test_460(self):
        input = '''Class _:qk{$q18__(_H,__,_7M:String ){} }Class _2{Constructor (n_:Array [Boolean ,05]){} }Class _:__0_{}Class w:O{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 460))

    def test_461(self):
        input = '''Class cd:j6{$5(_0,YSw_,F,_68:Array [Boolean ,12];w:Float ;X:Array [Array [Int ,0x1],12]){Continue ;}Constructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 461))

    def test_462(self):
        input = '''Class h{_(_,_:Array [Array [Array [Array [Float ,2_3_1],27],0XD_3AF],0b1000010];_v6g:String ){} }Class u:gJ{}Class __l_:__{Constructor (){Val _,K5053:___;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 462))

    def test_463(self):
        input = '''Class QI:K{Constructor (T,Q_,a,Z,Q_,R:Int ){}$__(_4A_,_2W9,_h:Array [Array [Array [Array [Array [Boolean ,8_3_4],01_3],071],0B1],2_4_8];H_5__VHFZ_:g){} }Class b_:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 463))

    def test_464(self):
        input = '''Class y{Var $2_6X:x;}Class _:_{$y(z,Z,_1_:_;_,___,_:EI;_1_l,_:Array [String ,04];ie:Array [String ,79];__,_,j:_;_,g:_0;___,_:String ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 464))

    def test_465(self):
        input = '''Class yr:C_{Constructor (x0,j:_;Z__,f:Array [Array [Array [Array [Array [Array [Array [Int ,0XF],05],0B1011],03],0b11],0B1011],49];__f2,_,Ju:Array [Array [Boolean ,0x5],0b1011]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 465))

    def test_466(self):
        input = '''Class _9:Y0{}Class D{Constructor (){}Destructor (){} }Class vH1{}Class _4f:__{Constructor (){}Val M,$F9,$__3,$SS:Float ;}Class _{}Class U2_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 466))

    def test_467(self):
        input = '''Class R___{Constructor (_3:Array [Array [Array [Array [Boolean ,0x42],0b101111],0x364],40];_:I0){Return ;} }Class _:_{Val $9,$9,_j9,$____:r3;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 467))

    def test_468(self):
        input = '''Class _{Constructor (BB2,v,o,w_kz,__,_,J,_:Array [Array [Array [Array [Array [Array [Array [Int ,0b1],0X15],0b1_1_10],067],59],0x37],6];_,n:Boolean ;_:Int ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 468))

    def test_469(self):
        input = '''Class _Z_0E{Constructor (H1_:Boolean ;s:Array [Float ,0X1A]){}__(){Return ;}Constructor (_2M,R5,z,_B,_5n:Array [Array [Array [Array [Array [Array [Float ,0b1010110],023],86],0B111101],023],93];_:Array [Array [Array [Boolean ,0B111101],0X1A],0B111101];__M_:Float ;__X8Uu3:_9){}r(){Return ;}_(_l,_:Array [Boolean ,06];_l,_,Z__d,n,_,Q6:n;F:M__R9){}Constructor (_0:D_j){Continue ;}Var $9,$Pw:String ;Constructor (){}Val $9,$7,$032_:Boolean ;Constructor (){}Var $0:lN7;}Class z_:Jz{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 469))

    def test_470(self):
        input = '''Class _:___{$Z_X(t_,_,__:Boolean ;j0___i:d;p:Array [Float ,0b1_0]){} }Class fz{Val _9:Float ;Val V:Array [Int ,49];}Class _w_:___4u{Constructor (_M3_1,_,__,_3E:Array [Array [Array [Boolean ,0663],0B1110],0XB]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 470))

    def test_471(self):
        input = '''Class _{Constructor (_q:Float ;_,_,_H:Array [Float ,0xB];_,Y,_8:Int ;O,m_4:Array [Int ,0X8];_34494,_:u9;_9:Int ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 471))

    def test_472(self):
        input = '''Class K:gY{Constructor (_:Array [Array [Array [Boolean ,022],0X6_6_6],0B10];X,_,_d:Array [Boolean ,0B10];sq_,_:Array [Array [Array [Array [Array [String ,0B1001111],0B1001111],03_5],80],0x56];N:Array [Array [String ,8_2],0xB_3_E]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 472))

    def test_473(self):
        input = '''Class Nc_Y8:n{}Class X:_{Var _,$9:Array [Array [Array [Array [Float ,0x61],63],0B100101],06_5_60_5];}Class pP{}Class _:kwl{_(_:Array [Int ,12];J_1__bXW:Float ){}L8(){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 473))

    def test_474(self):
        input = '''Class _:_U{Val $nE,$__,b:String ;}Class _Fe6_{}Class _f:A7{}Class S{Var r8spA:p;}Class _H_:_l{Constructor (G,__:JAs_;_2,_D,U,p,Y35__:Boolean ;_:Array [Array [Boolean ,0B11011],11]){}Constructor (_T:Float ;_,k_:Int ;K9,b_3_2,_Xl01,_:Boolean ;k:clHO){}Destructor (){Break ;} }Class _:_6i_19_{}Class _w:_4f{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 474))

    def test_475(self):
        input = '''Class hZ:u9{}Class _{Val _y,$6_,G:Float ;}Class _{}Class _:R{Var _,$_,a,$m:F_;___(_,a,__7,__:a;H7,_:Array [Array [String ,020],4_0]){}__(p,_mQ,l:Float ;W:Array [String ,020]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 475))

    def test_476(self):
        input = '''Class a{Var _ZFb_h_f9:_;z(_Wo:_;_j:Array [Int ,044];s,_:_;_:Array [Array [Array [Float ,6_8],044],06]){} }Class P{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 476))

    def test_477(self):
        input = '''Class __{Constructor (_:Array [Array [Int ,066],0x12];M_:U;_U,m6,_6:Array [Array [Array [Int ,03_76_5],0x2_4],89];d8,_E,_D,UM:String ){Val VB99h2:Array [String ,720_5_7];{} }Var __m_r,_:m;Var $j,__6,$U:Array [Array [String ,0XD],0X69];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 477))

    def test_478(self):
        input = '''Class _:K0{}Class _:_{Destructor (){} }Class xg7__W:_{}Class eR_H8_:r{Constructor (){}Constructor (L:Array [Array [Array [Int ,07],0xB],0b1001110]){_::$R_();}Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 478))

    def test_479(self):
        input = '''Class E7f6:k1{$uS(_3Y_,F,_,___H:Array [Array [Float ,061],0x5C]){}Constructor (_,T:Boolean ;_:Boolean ){}Destructor (){Break ;}_0(_16:Array [Boolean ,05]){} }Class _6{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 479))

    def test_480(self):
        input = '''Class _0B_:_{}Class _{}Class F:v_5_{Constructor (_R,_:Float ;Q__w8,_,_b57:_4ty;_,_9_,I:Array [Array [Int ,7],0b111]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 480))

    def test_481(self):
        input = '''Class N__:E{Var $5,E_,$3:Array [Array [Array [Array [Array [Boolean ,0xB],0b1],5_7],0X48],0b110];$J(_1:Array [Boolean ,0x71]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 481))

    def test_482(self):
        input = '''Class p49{Var $4,$R_:Int ;}Class _:_{}Class _{}Class _:LR{Var $uc,_d0,__,$0,__2,$7_,$o:String ;Constructor (_:Int ){} }Class __{}Class l8JV{Constructor (z,_:Array [Array [Int ,47],073];_,_,_,_l:Boolean ;_,s:Int ;_,c,s:_){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 482))

    def test_483(self):
        input = '''Class n:_4{Destructor (){}$f_(){Break ;}Val $w,_,$9nI_t94,$1__l__6,$6:_x20;Constructor (){Break ;}Val $J7,yd:Int ;}Class ___:v{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 483))

    def test_484(self):
        input = '''Class g1:__{}Class _:p_{}Class M{}Class _oe_0{Constructor (_:__;M1:Array [Array [Array [String ,045],0X3],38]){}Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 484))

    def test_485(self):
        input = '''Class nt6x:_3{$R_(_p:_){} }Class _9{Val __3,$T2:Array [Array [Array [Array [String ,0x439],0X51],8_4_1_3],0x49];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 485))

    def test_486(self):
        input = '''Class _:P2_7{}Class es{}Class _{$4_(j_,c6_,B,y:Array [Array [Array [Int ,0xC_E7_0_E3],0131],0B1010100];_:Array [String ,0X96];p,k,_Lu:Int ;f9_54,_,w95,_,_:K){Val rHD:K;} }Class Y7JP:_5{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 486))

    def test_487(self):
        input = '''Class _{}Class c_{T(_,_,_5EJ8s,_r_276,_,U,Z_,_:Array [Int ,0b11010];_,c:__k){}N1(H:String ){}Constructor (){} }Class o:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 487))

    def test_488(self):
        input = '''Class ai69a_:a{}Class _P0:l2{Var _,$9,_:sLT4;Constructor (__:String ;_,Hk_:j_;t:String ;_:Array [Array [Float ,66],0x9A9]){}Var _1,_T,_,$V41:Float ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 488))

    def test_489(self):
        input = '''Class __{Constructor (){}Val $3,$5,$_,P:Float ;$5e7Z(_36:Array [Float ,0106];r__,Gc7_:_;_6:Array [Array [String ,0B111110],0B1]){}M(){Continue ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 489))

    def test_490(self):
        input = '''Class R_{O6_(_:Array [Array [Int ,0b1_1_1],0x26]){}Constructor (_,_,_r,Dn8__5,_h,V:String ;_1i:aT_Tk2_;_G6__03TMn,x4,r1:Array [Array [Array [Array [Array [Boolean ,0X9],0x26],02_3_30],0B1001111],0X9];g,_3:_;_,_,Z,L:Array [Array [Float ,59],59]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 490))

    def test_491(self):
        input = '''Class _73:_r5q__Qr_{}Class m5xUf{v_2(){}$Ha(_4,_,mU,B_:Array [String ,6];__,____:Float ;a_,_:String ;_,L:Array [Array [Int ,065],0X3C]){ {} }}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 491))

    def test_492(self):
        input = '''Class _L4u_{$ir2__4c(_3:Array [Array [Array [Array [Array [Array [Array [Array [Array [Array [String ,396_0730],0x3B],72],72],0X3_7],0B1100000],72],0XD_0],0xB_6],0xC]){Continue ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 492))

    def test_493(self):
        input = '''Class H9{Destructor (){}Val bW,$83,$2_B__4h:Array [Array [Array [Array [Boolean ,0b1_1_1_1],066],0b1],0B1000010];Destructor (){Break ;}Val ____,$y:Float ;}Class b_{}Class _7{_(_,J_W_:Array [Array [Array [Array [String ,066],0B1000010],0X2],0x4D];__:Array [Array [Float ,1],0XC];Q,V:_){Continue ;} }Class _:_9_{Val $5g6d:Int ;Val $8,__FL7,X__Fo:_;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 493))

    def test_494(self):
        input = '''Class D___{}Class aw{Constructor (q_:_b7){} }Class Y_{Destructor (){}$2_x_(){Var _:Int ;Break ;}Destructor (){Continue ;Continue ;Val _:Float ;Return ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 494))

    def test_495(self):
        input = '''Class _{}Class _{}Class _{Destructor (){} }Class _f{Val $439_:Array [Array [Array [Int ,033],86],0B1000110];$O_a_(w:Array [Boolean ,4_3];_0,z,_,U,___Gt_:Array [Float ,03]){} }Class H_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 495))

    def test_496(self):
        input = '''Class zj_:f{$4__(){}$__(_,___:Float ){}$_3(F0_59H5:Boolean ){}Constructor (_,_O_,_68x5_U0,Ww66Q__:L;__,_1:String ;_,_:Int ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 496))

    def test_497(self):
        input = '''Class _{}Class YK23_8:n{}Class _:_6{}Class _1w:XeK2TY_{}Class z6Y:__{}Class _:_{}Class ky8{Val b:Boolean ;}Class _{Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 497))

    def test_498(self):
        input = '''Class _:_{Constructor (g_P40:I){}Var f,$_:Array [String ,9];}Class v9:__8z{Val $_V,_z,$1,Dl:Float ;}Class TgvOf:__{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 498))

    def test_499(self):
        input = '''Class _:_9{}Class _:___{}Class K:_{Destructor (){}Constructor (_:Array [Float ,4_4];_8:Bpct){}Constructor (__,n,u:_c;_,a:Float ;_,__:Int ;__X,t6,____6_cu3,_:_;_:__1_6_;_w:Int ){Var Pv6,_:_;Val C:_;Return ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 499))

    def test_500(self):
        input = '''Class _{Constructor (l05FE:Int ;C:String ){} }Class _2{Constructor (_,__,_:C1_;d_,T_:Boolean ;v,_:Float ;Q38,_,_8X:String ){}Constructor (j:Boolean ;_0,dx_:Float ;JeI:String ;_:Array [Int ,03_1_2_1]){}Constructor (P:Float ){} }Class W_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 500))

    def test_501(self):
        input = '''Class _:d{Var _:Array [Array [Array [Array [Array [String ,056],0b1],056],02_5],0B101000];}Class J:S{}Class f{Var $3:_;Constructor (){}Val $_:Array [Float ,8];Constructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 501))

    def test_502(self):
        input = '''Class _E{Constructor (mX9:Array [Array [String ,0B1],04417_74_6_7_0];Y8:Array [Array [Array [Int ,0B110],0X5],0X13];O26,e7_:Array [Array [Int ,0b11101],03];d,H:String ){} }Class M_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 502))

    def test_503(self):
        input = '''Class R_N_:w{Var $qZ:Array [Float ,046];Var $9,B:Array [String ,26];}Class ___{$20(){Break ;}_(s:__){}Constructor (__,_:_MIS_){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 503))

    def test_504(self):
        input = '''Class GO{$2(_qz:_;_:Array [Array [Float ,04],7597];_m__:Int ){}Val ____:__5;Var O,$U:Array [String ,0x1E];$_(T:Array [Int ,0X40]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 504))

    def test_505(self):
        input = '''Class _:___R{}Class _mQ7{xJ_r0(){}Var $5:Float ;Val $L2,_,w0:h_;}Class w{Var $cg:Array [Float ,0B111110];}Class __7OtjVS:jB7_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 505))

    def test_506(self):
        input = '''Class V:N{}Class _{Val $J,$_1:Array [Array [Array [Array [Float ,062],62],0B1_101],0b100111];Destructor (){Return ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 506))

    def test_507(self):
        input = '''Class S:_{Destructor (){} }Class Q_{}Class _00:_{Destructor (){_9::$__();}Destructor (){Return ;Break ;} }Class _{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 507))

    def test_508(self):
        input = '''Class _{}Class L_:Z0{Var ___2X,$9o_7,$_:Array [Array [String ,0X5],71];Var H,$__,__:M_36_;Destructor (){}Constructor (_00:String ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 508))

    def test_509(self):
        input = '''Class _B{Destructor (){}$_O__5(){ {} }Val X,$_,$m_n,$O_:Boolean ;Val e:Float ;Val $9,$7,$__:Float ;}Class _:_6{}Class C_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 509))

    def test_510(self):
        input = '''Class _c{Destructor (){}Destructor (){}Val __7O:S_;Constructor (){}Var $V,X:Array [Boolean ,06];}Class _6{Val $_3,$_:Array [Int ,0140];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 510))

    def test_511(self):
        input = '''Class _1:_6Q___H{}Class n{}Class gb:_{Destructor (){}Destructor (){} }Class E{Destructor (){}E(q_E0_:String ;q:Int ;H:q;_,_,_:String ;__:String ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 511))

    def test_512(self):
        input = '''Class J:X_{Val $g1,_:Int ;Val $0_y1:Array [Array [Array [Array [Array [Array [Array [Array [Array [Array [Array [Float ,0X41],0b100110],4],0132],0B1000],0X41],0B1],0X41],0xC],0X64],0B1_1];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 512))

    def test_513(self):
        input = '''Class F:__94_{A(_:coD1;rW_gE0W:Array [Array [Array [Float ,0131],6],0B1100];_,_:Array [Array [Array [Array [Array [Array [Boolean ,0b11100],050_71_65],6],0X3C3],0b1_000_010],0131];SY_,_6:Array [Array [Boolean ,0b11100],20]){} }Class _:__943{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 513))

    def test_514(self):
        input = '''Class _2_:Q4{Destructor (){} }Class G_J4l{Constructor (_,_1f_x,_y19,U,Rcu:Array [Array [Float ,0b100111],0B1010111]){}Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 514))

    def test_515(self):
        input = '''Class d_67Z_N_AL:k{$n4(S_,_74V,__4_,N___:Array [Array [Array [Array [Int ,0b1],30],30],0B11];wAr,r6_n5:Boolean ;X_:Int ;__,_K5,m_:Array [Array [Int ,0X7],046]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 515))

    def test_516(self):
        input = '''Class _4:_{}Class _{Var _,$_E4,_,$_z,$_,$9F,$r:Float ;}Class VH{Val $_l,$Pf__2:_;c2(_,X:Array [Array [Array [Int ,92_46_822],0B1000010],071];G_I:Boolean ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 516))

    def test_517(self):
        input = '''Class _x{}Class __8:_{}Class _{Val $7ij:Array [Array [Float ,6],2];}Class a:p{Var $6,CANaT_,p:Array [String ,0B100];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 517))

    def test_518(self):
        input = '''Class _{Val qt_37_8_i,_,gJ,$W,i,X5:a;Var _29__:Array [Int ,0XD];}Class hY__{Destructor (){}Destructor (){} }Class f6q{}Class K:__34{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 518))

    def test_519(self):
        input = '''Class ZRN:_{Destructor (){Return ;Return ;}Constructor (){}$__FZ(){}Var $_:Float ;}Class _{Var $e,$_:Array [Array [Float ,90],0X53];Val $l:Array [Int ,0X53];}Class OwR_1:z{Val $9L:Sr;Constructor (__,__,P,_:Int ;W:String ;_:Int ;U,_:_;O_:Array [Float ,0x1A];W,_,_b:_){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 519))

    def test_520(self):
        input = '''Class _B:__4{}Class _0___4o:_{}Class __:R_{}Class _1{Destructor (){} }Class _{}Class _:_e_{}Class _{}Class __:T7q{}Class _cH{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 520))

    def test_521(self):
        input = '''Class _k:_3_{$uJ(K59:Array [Array [Float ,0XD],046]){} }Class I{Val $__,_,k,R,z,gC_4:Float ;Var $A,$2:_;$o(I:Array [Int ,0B11110];kR5:a__80;a:i){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 521))

    def test_522(self):
        input = '''Class S{Constructor (Ge,gI_,W:Array [Array [Array [Array [Array [Boolean ,97],0xC],0B1011011],1_9865_91],0x51];__a4:k){Return ;}Constructor (_H_,J,_:____g_){} }Class __:y{}Class _:_{}Class Tp{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 522))

    def test_523(self):
        input = '''Class _:T{B(j,_f,_1:Boolean ;__p___7,___3B,M:String ;_:Array [Array [Boolean ,0x2E],05];_:String ;U,Eg,_,a:String ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 523))

    def test_524(self):
        input = '''Class S_k___G{Destructor (){}Constructor (){}Destructor (){} }Class Q_:q_{Var _5,_81_,Q5_9:Array [Int ,12686];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 524))

    def test_525(self):
        input = '''Class F:_l___a{Destructor (){} }Class l_c_:_{Constructor (g_,V:Array [Array [Float ,8],0B100];N9,XN,K:X){} }Class M8:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 525))

    def test_526(self):
        input = '''Class zK{$_D(o:Array [Array [Float ,0b11],42];_c0K_6_,_D,QV:String ;_,o,__:Array [Array [Float ,0B1],42];ML,_750_,R__h:_9){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 526))

    def test_527(self):
        input = '''Class _{}Class f{Var _:Array [Array [Boolean ,053],0xA];}Class Y:b{Var $4i:String ;Constructor (_:Array [Array [Array [Array [Int ,0xA],057],0x2_E],3];_6,S:String ;_,_:Int ;A:Array [Float ,0X49]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 527))

    def test_528(self):
        input = '''Class eC{Val $5:Array [Array [Array [Array [String ,037],0b1],0112],0X2B];}Class E:m__4{Var _n,c_,$_,$2t2_1:String ;Constructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 528))

    def test_529(self):
        input = '''Class Y_:T16{}Class yq{}Class c_U0{Constructor (__:Array [Array [Array [Int ,93],0xE],0X38];V:Int ;Q,wCU,g:P){}$2(){Break ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 529))

    def test_530(self):
        input = '''Class B:q_{_0k(f6:Float ;_T3__,m_:Array [Float ,2400_57];_8:Array [Array [Array [Array [Array [Int ,0B1101],06_0],2],0b1_0],52]){} }Class __C{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 530))

    def test_531(self):
        input = '''Class _r{}Class u5L:_{Val _,$7c0:Array [Array [String ,0X3],016];Var F,__:Array [Boolean ,0X6_C_2B_3];}Class a_:R{Destructor (){}Var $_:Array [Array [String ,016],07];}Class __r:_0_Y{Val $A8QK_:B;Constructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 531))

    def test_532(self):
        input = '''Class _:v_2W__9{$DJ(){I::$5._().j5_120_U.Wly_4_.D.r8();}Destructor (){} }Class r_Bu:s{Destructor (){} }Class Ms3_:__{Constructor (_,fa_8d,p14:Array [Array [Int ,0xF],72];P:Array [Array [Float ,06_4_1_43],0B1]){}Var $_el9:Array [Array [Float ,067],05_524];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 532))

    def test_533(self):
        input = '''Class _9_c{}Class z1:J{Var $w:Int ;Constructor (__:Array [Array [String ,0X59],013_3_1];_:Array [Array [Boolean ,8],0b101];v:Array [String ,05_1];_,_,z9:X1;_,__j3:_){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 533))

    def test_534(self):
        input = '''Class b{}Class TQ:_{W(){}Constructor (_YL,___T:Array [Array [Array [Array [Array [Array [Array [Array [Array [Int ,0b1],0277_2],387],2_5_5_1],73],0X9_8],03],0B1],0X495];F:U5;_x__1_9I_,__,_Y:_3_){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 534))

    def test_535(self):
        input = '''Class k7{Constructor (){}Constructor (__,_J___,X_Te:Array [Array [Array [Array [Array [Boolean ,074],0X15],9],0b1010011],7]){Var _00,AGMm,_,_,_8__:Float ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 535))

    def test_536(self):
        input = '''Class Q_3t:_7_{}Class z:_{Var s04_v7:Array [Array [Int ,04],04];Destructor (){Break ;} }Class __{Constructor (w:_tD_){}Val $N_5:Int ;Constructor (){Break ;Continue ;}Var a_71TQ,$4,_,$2F:_;}Class i:s0{Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 536))

    def test_537(self):
        input = '''Class S:_{$4(k6_,s_,__9,__8,_A:Int ;J,_Q6X,PK:_UmN_;_:Array [Array [Array [Array [Boolean ,051_7],0B1011010],45],45];D,V7:_;_1:Array [Array [Array [Array [Array [Float ,020],020],8],8_1],020];__,yh6_A:Array [Array [Boolean ,0B1_1],0b1];_,dj:String ){}Var _:p5n__;}Class e{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 537))

    def test_538(self):
        input = '''Class U1{q0(_L__:Array [Array [Array [Array [Array [Array [Float ,40],0X56],0x4],0b1100100],40],3]){}Var _:Boolean ;}Class _{Destructor (){Continue ;}Destructor (){}Destructor (){} }Class __:_{}Class _:_N{Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 538))

    def test_539(self):
        input = '''Class _:b_{}Class _{}Class l:Y_{Val $Wn,_,p,Y,O_7:Array [String ,90];}Class _:_1_{_(){} }Class _8_65r{Destructor (){Return ;{Val _,_,F,_,u:Int ;} }}Class _a0:__n5{Constructor (_:Float ){Continue ;Val _0_8G:Float ;}$_(A479t,W_:Int ;P:String ;_9:Int ;H__:String ;W,_,W,j,f,_2J_f:Array [Array [Int ,0XB4EC],06_6_3_0];V:Boolean ;_:Array [Int ,9_2_4_66];__:Array [Array [Boolean ,0X48],0b111010]){}Constructor (_,_:_;_,Ns,t,_z:l){} }Class _b:p9{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 539))

    def test_540(self):
        input = '''Class _0:Th{}Class u{Val e:Array [Int ,0b1];Constructor (){} }Class j:_{$9(_2w52:Array [Float ,030]){}$7(){ {} }}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 540))

    def test_541(self):
        input = '''Class _7{}Class MC103{A8(_:Int ;p_,_84_,k:Float ;_:Array [Array [Array [Array [Array [Float ,70],70],01_0_5_7],0b1000110],70]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 541))

    def test_542(self):
        input = '''Class P6{Var l04:Array [Array [Array [Array [Array [Array [Array [Float ,0b1011110],3_5],0x2D],021],5_6],54],0b1];Var Vz,__,$hV6,q0:__T;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 542))

    def test_543(self):
        input = '''Class V_Io_:z4{}Class EK_3Uj:_Zp{}Class _:M{Constructor (_:Array [Array [Array [Float ,04],0X3_D],0x7]){}Destructor (){Continue ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 543))

    def test_544(self):
        input = '''Class _3_{}Class Fm5To_o{Var $_:Boolean ;$x(){}$Np(__0j,_0,My_:Array [Array [Array [Int ,023],0x27],0B1_0]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 544))

    def test_545(self):
        input = '''Class _5:G8{Val $_,$3:Array [Array [Int ,0x72_E_A],020];Var $_,$_,_:W;Var _,$_,$28_,gk,$nd___8m,$7V:JnG;}Class l1oKm{Destructor (){}Destructor (){ {} }Constructor (_3:String ;h,__:ag_){ {} }Val _:_A_;}Class _{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 545))

    def test_546(self):
        input = '''Class l0N_{Constructor (_5ERNm:Array [Array [Array [Array [Boolean ,02],071],0X1_6],03_61_3];_0,__6,yU,s:_){Continue ;}Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 546))

    def test_547(self):
        input = '''Class __8c{Constructor (w,_S,_5,W2:H5;_6z_:_63g;_S:Nd;S,k,C:Array [Array [Array [Array [Int ,73],05_1_1],0XF],22]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 547))

    def test_548(self):
        input = '''Class _8:l_5_{$C(_x7:Array [Array [Array [Array [Int ,0B10],0b10001],0x42],02];_:Int ){}Val $_,$_PR3:_7;}Class B:B3_{Val $_38,__5__,n,T91,$5,$C0N,$_,_:_1;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 548))

    def test_549(self):
        input = '''Class o:_{}Class z_:_9__2{Destructor (){} }Class t:___U_{Var $9e:Int ;}Class _DE4:v{U(I,J:_;B2,_,_:Int ;P:Int ;_q_5,A:_t){Break ;} }Class _:_z{}Class K:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 549))

    def test_550(self):
        input = '''Class _96{$_(n,F:Array [Array [Array [Array [Float ,0b1],0X10],15],0b1];__,_,_:Array [Array [Array [Array [Boolean ,0b1],0213],0B1_11],0b11]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 550))

    def test_551(self):
        input = '''Class _:n{Var $3:Array [Array [Array [Array [Array [Array [Array [Array [Float ,0X2_8],051],0b101],0B1011100],6223],0x7_4_D],0X20],1];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 551))

    def test_552(self):
        input = '''Class g:s1{}Class jK:_{Constructor (__:Array [Array [Array [Float ,0B1010],0x3A],0B1_1_1_0];_,NCd:h26;E_a8_8f:Array [Float ,0102]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 552))

    def test_553(self):
        input = '''Class t0:_{}Class _C{}Class _{}Class L_:i{}Class _:T_{Val $_G,$6I__1__T,m,b:_;Var $F:Array [Array [Boolean ,0x57],0B110101];Val $3:Array [String ,0X7];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 553))

    def test_554(self):
        input = '''Class _{Val kbM,_11,$9__:Array [Array [Array [Array [Boolean ,86],2],0b1],0b1011111];Val $_8:Array [Array [Array [String ,0115],0b100],0b1];}Class m{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 554))

    def test_555(self):
        input = '''Class _:U2{$_(q,U,__:Boolean ;_,_,__C7:_;N:Array [Array [Array [Array [Array [String ,0B1],01],4_7],0B1],0X5A];u8_,__,u_0,_j5:Array [Array [Array [Array [Float ,0B1],0b1001100],82],0X5A];_:Array [Float ,0b1001100];_:String ;_c:Int ;_:Boolean ){}AL(){}Constructor (){Continue ;}Constructor (){} }Class _{}Class _B{Var N7_,$__,$_5v:_79;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 555))

    def test_556(self):
        input = '''Class Ya_{}Class TT{}Class T:X0sq4_{}Class h:x{Constructor (N:Array [Int ,033];_9_:c_e;_D8J:g){} }Class _{$9(){}Var i,_w4,$_j3_821_6:Array [Array [Int ,2_7_0_940_580],0b1011101];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 556))

    def test_557(self):
        input = '''Class _{Val $e,$5t:Boolean ;Var $l,z:Boolean ;$7(){}Var _:Int ;Var $__,$7,$_39__,Z6:_;}Class H{}Class A:i{}Class _:p7{}Class CC{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 557))

    def test_558(self):
        input = '''Class _:d{Constructor (n,__,_:Z4__0){Continue ;}Var $3NV_9_:Array [Array [Int ,0b1],0B101000];Constructor (_,_,l__,U_,n_OgR,_:vQ;k:_;_:Boolean ;V:Array [String ,0B1];_z:Array [Array [String ,044],01]){}_(_n,D3,vl8m,Y5,a_,_:Array [Array [Int ,01],0b1];_8:Boolean ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 558))

    def test_559(self):
        input = '''Class E1P:_k4722h8{Destructor (){Continue ;}Val e,$7E1:Array [Float ,0X45];Var G,$0,$O0,L,Mf:QR5;Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 559))

    def test_560(self):
        input = '''Class z{Destructor (){Break ;Break ;} }Class x_{}Class p:Y_{Var $36_9:_36;Val $____:Array [Array [Boolean ,0b1_0_0],0122];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 560))

    def test_561(self):
        input = '''Class _i:_{Val _4:Array [Array [Array [String ,0b1_1],01],03_277_16];}Class ne:q5_{Val PT,y,n,$_1R,$T1:Array [Array [Array [Array [Float ,9_54_5],0b1100010],0107],0565];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 561))

    def test_562(self):
        input = '''Class H:_326{}Class __q_62iE_{Constructor (In_ ,_8:Array [String ,0b1000000]){}Var _H_:Array [Boolean ,0142];Var $p,$__,$ak9_c:Array [Int ,0x7];}Class R{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 562))

    def test_563(self):
        input = '''Class R:P{Constructor (y:Array [String ,0B1];_ssW_:Array [String ,0B1];E,_:Array [Array [Array [Array [Array [Array [Array [String ,0B11],0B1],021],0b1],0X2],69],021];_:Int ;A_v,Y_UP5,_Gc4,Q,_:Int ;__:_){}Val $lD:Mk_Ar_a_1t9;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 563))

    def test_564(self):
        input = '''Class p{}Class c:J_w{Constructor (_3M:Array [Boolean ,020_6_6];_,M,O,__,_8:Array [Array [Array [Boolean ,0B1000000],060],0b110_0_1];_,__:B_;m,wZ_,Kqv,_Bhg:String ){Var _:Int ;} }Class _54sh{Var $1:K;Destructor (){Var X,S:Array [Array [Array [Array [Array [Array [Int ,060],41],6],8_3],6],060];} }Class G__6_{Val __J_:String ;O_(){}Var $5__1,_:Float ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 564))

    def test_565(self):
        input = '''Class p{_(_,G_:Array [Int ,0B1_10];_h:G_;__:String ;_,J,q_,q_,_,Q:Array [Array [Array [Array [Boolean ,0B1_1],046],0x6C],49];_:sV_){} }Class _:__Z99{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 565))

    def test_566(self):
        input = '''Class __:pG{Val $l__:Array [Array [Array [Array [Array [Array [Array [Array [Array [Float ,52],0xE3],52],0b1000],0B11_1_11_0],52],0B1011_0_1],0b1000],0b1000];Destructor (){}Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 566))

    def test_567(self):
        input = '''Class _v__17:Z{Constructor (){} }Class O:__r9{}Class _{Var _hu:Array [Array [Array [Boolean ,0xB_00],9],58_12_41];Var $7,p:Array [Array [String ,0x4D4494E_8],1];Constructor (_:String ){Break ;Continue ;}Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 567))

    def test_568(self):
        input = '''Class _:_{Val _:L_;}Class k{}Class __:E{Constructor (_:Array [Array [Array [Array [String ,92],0b1001100],0xB],9];e_,____:Mu;l,_:Array [String ,046];q__:V){}$o(){} }Class _:u_{Val $s97:_a4;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 568))

    def test_569(self):
        input = '''Class _q:H{hQ_(e_5,_,__,_:Array [String ,0x51]){Var _,_tw,_0LB:Array [Int ,79];{} }}Class __d:_8n{Var $_1:_;Destructor (){}Constructor (O,d3,G_,_:String ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 569))

    def test_570(self):
        input = '''Class W{Constructor (c_8_:Array [Array [Array [Array [Array [Array [String ,7_9],0b1_0_0_0],0b11100],0142],0b11100],0X23]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 570))

    def test_571(self):
        input = '''Class _1:_{Var $G_:_f__;Constructor (H6:Float ;_,l,_,M:Array [Array [Array [Float ,3],0X7_5_B05],0B100100];Q8,M:Array [Int ,3]){_::$E();} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 571))

    def test_572(self):
        input = '''Class l:__{Constructor (u_1__:Array [Boolean ,0B1001011];R:Array [Array [Boolean ,0b1101],0B1]){ {Var _:_;} }}Class y:G1_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 572))

    def test_573(self):
        input = '''Class e3:F{Constructor (c89:_;u1:String ;_81,KA:Boolean ;___,J_:Array [Array [Float ,0X2_EC_A5],0B11011];_,_:Float ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 573))

    def test_574(self):
        input = '''Class F:_1Z9{Var $v_0f5_:_ax16_;Var $_:Array [Array [Array [Array [Array [Array [Array [Int ,0B1_111],057],057],23],0b10100],05],07];_(){__0::$n();} }Class X:Q53{Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 574))

    def test_575(self):
        input = '''Class my{}Class _H{}Class _:la{Var $5:_;Var $_4:Array [Array [Array [Array [Array [Int ,0B10110],0xF],0X5],25],0b11011];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 575))

    def test_576(self):
        input = '''Class j{$Q(_:Array [Int ,04_5];___9m3:_;E,_2,Z_511,M:_){}Destructor (){}Val j_,$_:Float ;Var A,C,$C:Boolean ;}Class _c:N{}Class _2n:r{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 576))

    def test_577(self):
        input = '''Class __{Constructor (lR,K:Array [Array [Boolean ,0X13],0B1_1];_:Array [Array [Float ,5],0X13];O,B1:Boolean ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 577))

    def test_578(self):
        input = '''Class _{$_(a:Array [String ,0x4E];_8,Hs7Zt,W0:__;m,Y,_,_:Array [Array [Float ,0X1C],05];_5:Array [String ,0B10];_6,_B__r,__6F:Array [Array [Float ,0B1],016];__:___){} }Class m{}Class J_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 578))

    def test_579(self):
        input = '''Class _O82S_{}Class G43o:_8_{Constructor (){} }Class F:dg_42{Constructor (j:String ){} }Class _90:_{}Class _:O0_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 579))

    def test_580(self):
        input = '''Class _m:_{Constructor (_,S,__,_,__:Int ;H,_,i:Array [Array [Array [Array [Int ,0x4_0],0B11],061],769_0];p__,v,Z:D0){}Destructor (){} }Class G__:__f{}Class __:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 580))

    def test_581(self):
        input = '''Class _:A{Destructor (){}Constructor (_s_t:Array [Float ,0x1B]){}Constructor (){}Var T6M,da,$8H__:Array [Array [Array [Array [Int ,0X2A],0B1],2],69];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 581))

    def test_582(self):
        input = '''Class _7{}Class _23:L_8_{Destructor (){}Val V_:l6;Constructor (_:Array [Array [Array [Array [Float ,5],16],0B1_1_0_1_10_1],5]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 582))

    def test_583(self):
        input = '''Class _:Y{Destructor (){ {}Break ;} }Class _{}Class _:__{}Class _{Constructor (b_Dg:_;G,___R:N77_;MR:Array [Array [Boolean ,0X4E],03];_w7__:Float ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 583))

    def test_584(self):
        input = '''Class e___4_:__{Var $08f0,_:_;x_7(f,_,_,Y:Array [Array [String ,0b100011],0x43];VR,D:Array [Array [Int ,0X8],0x43]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 584))

    def test_585(self):
        input = '''Class rS9E_:_{Constructor (Q:_;_:b;_49D1,_,Z2z,__:y0;Z,MM,H_:NV){} }Class SV{}Class QT:H_{}Class G:r{}Class G:_{}Class _:Z3R{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 585))

    def test_586(self):
        input = '''Class p{Val $4:Array [Array [Boolean ,0b1_1],0B1_00];$70(){} }Class l_07{Var $G:Array [Array [Array [Array [String ,89],368],0XF],0b1];}Class _:U1{Var $9,_,r:Int ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 586))

    def test_587(self):
        input = '''Class _4_:_w{}Class a{}Class n{}Class _:__{Val $c,_:M_;Destructor (){}Val $TMV:_E;}Class r{Val _p4_:_9I;Destructor (){Break ;Continue ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 587))

    def test_588(self):
        input = '''Class m745_{Val $D:_;$_(Xp4,O_,T,BN3,__,___,W12:Array [String ,0x37];_,V:_78;_kW2lR_:k_;_C,kz:Z){ {Var Q4_b,x,r_b_,nm4:__;} }Destructor (){} }Class b{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 588))

    def test_589(self):
        input = '''Class _dv_4N:_0_{Val x3d,d,$_,$8,a3:kg;}Class z915:_2{Destructor (){Continue ;_4::$6();Break ;Break ;} }Class l:v{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 589))

    def test_590(self):
        input = '''Class _:L{}Class F_:t{$i(v__:g_){}Val d,U4,$_1,$u3:Float ;Constructor (__,__h6_Q_:Array [Int ,03501]){} }Class Z_6_z7{}Class _2:k56w1_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 590))

    def test_591(self):
        input = '''Class e:J5__{Var _,_,$sPn,$p__:Array [Array [Array [Float ,45],0B111],0b10_0];Constructor (_:A;_f_,__,Yl:_;pU66,_Z2:I){}K_(){}Val $0,_:_9;}Class _5Q3:wX{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 591))

    def test_592(self):
        input = '''Class T{Var $v:Array [String ,05];Var _,$_8,___:Array [String ,0b11];}Class g_E_{}Class _y{Val $_2__8,$_,$F__Zs:D4;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 592))

    def test_593(self):
        input = '''Class U{}Class y_:_{Val $N_z:_=q67::$_;Val $T2skJ__s:Boolean ;}Class _{$5(){}Var $_y:_;Val $58,E,$__4:Array [Array [Array [Int ,0X52],02_4],0B11111];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 593))

    def test_594(self):
        input = '''Class E4{}Class E_:N{$5(){}$7_6(){Continue ;}Val _,$q:o_U;Constructor (u_:Array [Array [Float ,0b1011111],0XEA]){Break ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 594))

    def test_595(self):
        input = '''Class _{Constructor (_I0,b,v7,_,_,__9W:__;E_:q;P:j){} }Class E:_6{}Class _{}Class _{Destructor (){} }Class I{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 595))

    def test_596(self):
        input = '''Class g_{}Class R:oii1{}Class S:o{Constructor (D,S:K7){} }Class _T0C{Constructor (f:Int ;_g4:x_){}Destructor (){} }Class _R_o:HF_{Constructor (){ {Continue ;}{} }}Class Q_:Z{}Class _{}Class V9:_57_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 596))

    def test_597(self):
        input = '''Class x{}Class _4{Destructor (){Return ;}Var __:r55k;}Class s45{Var $7,H:Int ;}Class G{Destructor (){}Destructor (){} }Class z1____:_{_(gWtE,K0,zG,C:B){}Var Q,_,zy,__:Boolean ;Constructor (){} }Class d:y{}Class _:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 597))

    def test_598(self):
        input = '''Class _:_2{Var $PY6Z,$H25:Array [Array [Array [Array [String ,0B1],2_918_1],3],99];_(){} }Class c:i{}Class _:_{Destructor (){} }Class _:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 598))

    def test_599(self):
        input = '''Class _jl:_{$GY(){} }Class _U7_:___{__(_3,_,BN:Array [Array [Float ,0X42],05];JF54f_:String ;r:_t;i8__:Boolean ;a_,__B5g6:Array [Array [String ,0x42],0b1_0];T_4__:Array [Array [Boolean ,04_1],0XA];G:u){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 599))

    def test_600(self):
        input = '''Class _{Val c:Q;Val $Y5_,_,R,$__1,$D9:String ;}Class _:r6V_{}Class YG_{Constructor (hq_U,__:Array [Boolean ,0136];Y,_:C_){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 600))

    def test_601(self):
        input = '''Class _{c_(_80,J,_,O,_Y:Array [Int ,0X5D];r,Qs_4,_,C:Int ;X,_w4_:Array [Float ,0B11111]){}$___d(){Break ;}Constructor (f,c_:m75I_8;_g_e:Array [Array [Array [Array [Array [Array [Int ,9],15],017_4_7],01],0b1],05]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 601))

    def test_602(self):
        input = '''Class _5{Destructor (){ {} }$R_(c:_1_;_:Array [Array [Array [Array [Boolean ,07_6_1_77],0x37],071],071]){Val F_4iH_:Int ;Continue ;}Val $M_1l27:H8;}Class Y:_8{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 602))

    def test_603(self):
        input = '''Class N:_{Var _,V:Array [Array [Array [Array [Array [Array [Array [Array [Float ,0B10000],22],0B10000],073],4],03],0B10000],8];}Class _{Var $q:Boolean ;}Class u{}Class D_:_{Val _:j4o;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 603))

    def test_604(self):
        input = '''Class _C{Val $72Nd:Int ;$i(G:LR){ {} }}Class b:_{Val $7_:__;_(){}Val $1__,$8,V:Array [Float ,0B110110];Var $_,K5,$C,___:Array [Float ,0b1001000];}Class ____N_{}Class _e867:k{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 604))

    def test_605(self):
        input = '''Class __{}Class C:_{Destructor (){_::$1_h();Break ;} }Class _Z4____{Destructor (){}$_j(r,B:Array [Array [Int ,1],3_6_4]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 605))

    def test_606(self):
        input = '''Class z:H_{}Class _:_83{Constructor (_:Boolean ;__N:Array [Array [Array [Array [Array [String ,0xC_F],2],27],01],0xEDC]){Continue ;}Destructor (){}Var $_S7,$8:Boolean ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 606))

    def test_607(self):
        input = '''Class Z:EH_{$k(_J,_,_o,_4:Array [String ,0x44];nE_0,W0,S,p:Array [Float ,66];_6:Array [Float ,0134]){ {} }Val W,$_,Y1,_6_:String ;kb(){}y___471(h:Float ;_99:Boolean ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 607))

    def test_608(self):
        input = '''Class pt{Var w:Array [Array [Array [Array [Float ,034],0xA],0X6E_2],18];Val $A:Array [Array [Int ,18],0x8];Var $_65:Array [Array [Array [Float ,0xA],0b10],0x3E];Var W5_,$_d,$_f:Array [String ,8];Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 608))

    def test_609(self):
        input = '''Class K{_I_(){}Destructor (){} }Class B6:_{Val __,c5,$_5,_,$5_:Float ;Var $_:Array [Array [Array [Array [Int ,0b10001],0B1000001],0X9B31A0_0],0b10001];}Class _8a:pK{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 609))

    def test_610(self):
        input = '''Class uH:_{Val R,$_,$_4:Array [String ,0B11_0];_(){} }Class _B0:U{Var $_r_:R_5;Destructor (){w::$_._8._.O()._s.e()._();} }Class y:_{Var $_,$__5:j_;Val $__:Array [Boolean ,1];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 610))

    def test_611(self):
        input = '''Class _y{Destructor (){}Destructor (){Break ;} }Class _:T{Val $6k,wSq_:Array [String ,0110];Destructor (){}$A_(y:y){}Val $_,$g_:d;Val Q6:String ;Constructor (__:Array [Array [String ,0X60],34]){Return ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 611))

    def test_612(self):
        input = '''Class P3{Constructor (S:Array [Boolean ,0112];_M:Boolean ;_:Float ;v,N:Boolean ;_,_,M6_,_O:_;p_:Array [Array [Int ,0112],100]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 612))

    def test_613(self):
        input = '''Class kM_3_{Destructor (){}$r__(k:Fp;E:Array [Array [Array [Float ,1_3],86],53];q,I,Q:Int ;_:Array [Int ,07];z,z7,j:Float ){Return ;} }Class g:_8{}Class __8Ey8:_{}Class _j5:_R{Destructor (){Continue ;} }Class z:__Q{Destructor (){}Val $u,_N,C_9,_7,$1:Float ;Var $U9,$5_V69o9E:_1;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 613))

    def test_614(self):
        input = '''Class iM0aoY:Y7_{Val $h,_1_,_,$_OI,$_63a6,$7:_;Destructor (){Val R,_3:Array [Boolean ,0b111011];} }Class _:Q{$3_8(){}Val ___,$_292,__y:_8;$7(__:d__g;Yp:Array [Float ,0x3]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 614))

    def test_615(self):
        input = '''Class F_:_{T_(_:Boolean ;_:Array [Array [String ,4],0b1];f,to,D:Array [Boolean ,0137];_,_:Array [Boolean ,0xB]){Break ;Break ;Val B:Array [Array [Float ,0b1011],0B1_00];{} }}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 615))

    def test_616(self):
        input = '''Class oq_L9:V8{}Class E:o___3_x_{Destructor (){}Destructor (){}Val $q_:String ;Val _,$M:T;Val $i_m6,$_:Array [Boolean ,0X7];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 616))

    def test_617(self):
        input = '''Class T_{Constructor (I:String ;_793y,_,N,_s_,_0:Float ;_5_6mmz9:Q;_,P_4,T:Boolean ;_11:K;m_:_;_7,I:Array [Float ,0X11]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 617))

    def test_618(self):
        input = '''Class _:L{$R4(_:Array [Array [Array [Boolean ,29],0b1010000],06];C:Ew;V__,g6__1_:_1_5){} }Class J1Y_:r{Constructor (_:R;_8m:Array [String ,0X30]){}PW_(){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 618))

    def test_619(self):
        input = '''Class _:_59{Constructor (_D:h9;h:Array [Int ,0XF_1_0];__B,Sk:UU;_M3:Boolean ;mb_:k){}Val $Ee,$_,q6n_g:L;}Class nO{Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 619))

    def test_620(self):
        input = '''Class B{Constructor (){}Val $0,_3Em,_:Int ;Constructor (o:Array [Array [Array [Array [Int ,0XE],0X5B],0X96_F],22]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 620))

    def test_621(self):
        input = '''Class e:_{}Class I:HAN636{Destructor (){ {_zx_256::$jC_();}Continue ;}Var $_D,$9,$L_,$B,$___OK,__9:Array [Float ,0b10100];_(_z:Boolean ;_4,_:String ;_:String ;D:String ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 621))

    def test_622(self):
        input = '''Class _C986{}Class _O6347q:_W0{Constructor (){} }Class Pv:_7{Constructor (q,kk_v__,D,__:_){}Var $_:Boolean ;}Class _{}Class _{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 622))

    def test_623(self):
        input = '''Class r9_:o_0{w3qd(z:String ;_,h_0_,w,YJ6:String ;_aJ238:Array [Array [Array [Array [Float ,0XB],0122],25],0122]){Val _f:Boolean ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 623))

    def test_624(self):
        input = '''Class _6{}Class _:Rq2{}Class _:_{}Class y{_2(f:Boolean ;__6L4:Array [Array [Array [Array [Array [Float ,0b1100011],054_52_7],0x1],0X9],050];sm__,__:__){}$_(){} }Class _5{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 624))

    def test_625(self):
        input = '''Class _:_38{Var $2,__8_zl,b,$9p:Array [Boolean ,0b1_00];Destructor (){Val _,_2,l,_Q,__,_,f,RLM:Float ;Val m,U6,_,Z1,jB:_;} }Class a:_2{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 625))

    def test_626(self):
        input = '''Class H:b__{}Class _F{Constructor (q,Kg:k;P_,B_Wt1,_:_;_,_4_:kJ05;_,_iSO:Boolean ){} }Class y6w{Var Z:String ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 626))

    def test_627(self):
        input = '''Class _{$B(b:Float ;_,_,__,_,b___8:o;u3:___;_V:_;m:Array [Array [Float ,0134],0b11]){}_(){Return ;} }Class __:_vY{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 627))

    def test_628(self):
        input = '''Class I{Destructor (){Return ;}Destructor (){} }Class F:_X_9{Var T,_,_,_:Boolean ;__(_q,B_q:Array [Array [Boolean ,1],74_3_86_0];_a5N,rw,__O:Float ;fT__,D5:Array [Array [Array [Array [Array [Boolean ,0xE],2],9],0b101001],0b101001];bZ4_:Float ;kN:_0gw3;_,j:_){Break ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 628))

    def test_629(self):
        input = '''Class h{}Class _{Constructor (l:s;m,_:Float ;_:Float ;Q_1:nS5q;___,_,Jc:_xr;waU_z53,W:LR){} }Class L{Val _,A8:Array [Float ,0X59];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 629))

    def test_630(self):
        input = '''Class s{Destructor (){} }Class c{}Class __j{}Class b{Var $Fi,$61:Boolean ;Val M_8_:Boolean ;Val H:nk;}Class _L:K{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 630))

    def test_631(self):
        input = '''Class t:___UB{}Class _u_0:_{}Class B{}Class _hs{}Class w{Constructor (V,_4:_13;k:String ;d,jH:Array [Array [String ,0B1_1],0b101111]){_::$8_z3_._().CYUnqcr._.W._().z();} }Class _{}Class P:S{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 631))

    def test_632(self):
        input = '''Class _N3:c4p___8__{Var _:o;}Class pk:A{}Class y38:__U_{}Class _{}Class __:_{}Class j:_{Var $_:Array [Float ,1];}Class z4:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 632))

    def test_633(self):
        input = '''Class k{}Class J{Val _a4y:Array [String ,0x56];}Class _:j{Val b3:Float ;}Class _:_{}Class ___:f3_{Constructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 633))

    def test_634(self):
        input = '''Class __5n:__q{Var $_6__,$S,$p:Array [Array [Array [Array [Array [Array [String ,0X4_9_0C6],07],0134],0134],1],0B1100000];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 634))

    def test_635(self):
        input = '''Class __:F{}Class a{Destructor (){Return ;Continue ;}Var $2:Array [Array [Array [Array [Array [Array [Float ,16],051],0x4A],03_4_1],0x4A],012];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 635))

    def test_636(self):
        input = '''Class _:o{Constructor (){}Val $K:Array [Array [Int ,0b1010110],85]=J||!-qus::$_.y/True .__j--""/!!--0165_51.C();Constructor (___1:Float ;sH:Ru00){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 636))

    def test_637(self):
        input = '''Class _{Val $a4_:Array [Array [Array [Array [Array [Array [Int ,23_5_0],02],0X7],0b1_1],316_69],0b1_11];}Class O:J_{Constructor (v:Q_b;_:__c;__:Array [Boolean ,0xE];d2_a,_:Boolean ){}Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 637))

    def test_638(self):
        input = '''Class __{Var $_:Int ;Constructor (B,en:Boolean ;t,C:Array [Boolean ,0136];y_6_:Array [Array [Int ,0x62],0x62];W:Float ){Break ;}Var m:Array [Array [Int ,07],93];Val $ao:Array [Boolean ,06];Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 638))

    def test_639(self):
        input = '''Class K:_x_o4{Var _,$Q_t,$_:Array [Array [Array [Boolean ,067],07],05];Val Z_,$8__4,w,$_a,$__,g4,_:_4T7_;Constructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 639))

    def test_640(self):
        input = '''Class _:RN{}Class _X7{Val $1W_:Float ;}Class _7c6_{Val l:Array [Array [Array [Array [Array [Array [String ,0x6],5],0x3F],9_59_7_81],85],06];Destructor (){_geY::$5();Var C:Array [Array [String ,7],04_210_4];}Var $_,$_25J2,$_k:b0Fw;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 640))

    def test_641(self):
        input = '''Class _:OP{}Class B___:h056_{Val $_,M_1,$Xz,C,_:Float ;}Class _71t0:_9{Var _1292t_a_,$V,$q:Array [Array [Array [Array [Boolean ,0x5B],0B111000],97],0B11];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 641))

    def test_642(self):
        input = '''Class _:_xU{}Class U0p{Constructor (){Return ;}Val $H:Boolean ;}Class U:v{Val $x:Array [Array [Array [Boolean ,0xB],012],0x3E_67];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 642))

    def test_643(self):
        input = '''Class E:B{Var d:Array [Array [Array [Array [Array [Array [Array [Array [Int ,02],0x69_9],0B10110],2],0B1],0100],0100],0b1001010];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 643))

    def test_644(self):
        input = '''Class L:_63__{Constructor (m,u28O,L,X2,Ku:String ;_,M9,_,_1:Array [Float ,01_372]){Continue ;}Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 644))

    def test_645(self):
        input = '''Class _:i{Val J:Int ;}Class C69{}Class _C:X{}Class k34{Constructor (){}$q_f_P5(_,_,__075,n:Array [Array [Array [Array [Array [Array [Array [Boolean ,0b110101],07],070],0X3E],0B1001011],01],0B1001011]){}Destructor (){} }Class Xz_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 645))

    def test_646(self):
        input = '''Class m{}Class _{_(__,g:String ){}Constructor (){} }Class r_:__{}Class _R_N:_{}Class _59ML{}Class _{Var $7_6:Array [Array [Boolean ,1_3],0X9E9_4];}Class _{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 646))

    def test_647(self):
        input = '''Class _:Q{j(){ {}{} }Constructor (j_,g_Q,_:n){} }Class __7:G{}Class _0{_8W(c0:_4__8;p,x:Array [Array [Array [Int ,0125],0125],0x74886_3C_74_F7];u,X,_Q3f:Array [Array [String ,2],0B111101]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 647))

    def test_648(self):
        input = '''Class _:__0___{}Class _:y{}Class _7_:_e{}Class G:z{Constructor (){Break ;{Var _u3,__:Array [Array [Int ,3707],0b10];} }}Class _{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 648))

    def test_649(self):
        input = '''Class _:R{Val $1_:_p;}Class _W_:s{Var $x:Array [Array [Int ,0b1000110],0x3F];}Class __k{Var _,Q,_,_:Array [Array [String ,0XA],21];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 649))

    def test_650(self):
        input = '''Class _9:__p_3{Constructor (_:Array [Boolean ,0B111000];X:Array [Array [Float ,02],5];x_0:_WAG_8;_F:Array [Float ,64];Z,_GD:o){} }Class _{T_(_:Boolean ;q:n;h,_:Array [Array [Float ,0x19],835];s,Y:Boolean ){}Constructor (__,E,jo:Boolean ){Continue ;_::$TK_();}Val $3_Q_5,_2:Array [Int ,2];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 650))

    def test_651(self):
        input = '''Class x_:_{Constructor (m:Array [Array [Array [Array [Array [Array [Array [String ,0b1100000],0B10010],0b1100000],86],057],9],0b1110_1];d:Array [Array [Int ,057],0b1100000];jDB,_,Bb,_:String ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 651))

    def test_652(self):
        input = '''Class __:Z_{Var j8_0,$Sd:Array [Array [Array [Array [Array [Array [Array [String ,809],0b110101],0X5D],0b110101],0b1],0b110101],0x34];$__q(b,_5:Boolean ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 652))

    def test_653(self):
        input = '''Class _{$6(__,_r5,_HU:Array [String ,0XF];_9:Int ;_:Float ;_G:Z8_a8;D_:Int ;_,d,Z8:Array [Array [Array [Float ,0b10100],0123],0b1010_0];G:o3___;__:Array [Array [Boolean ,0b10100],67];D__c_,XP:PW){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 653))

    def test_654(self):
        input = '''Class f{}Class kjz:_{Val _9,$F,$_:Array [String ,0x5];Destructor (){Break ;}Val _:_5_5_;}Class a{Val Xa,s__2_C:Int ;Constructor (C_:Z__8){} }Class o_2u{Val H_:Boolean ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 654))

    def test_655(self):
        input = '''Class n__:_{}Class _{$_(){ {} }}Class _{Var $81lY,_:_;}Class _{}Class __:_s{Var XV:Array [Float ,0b1010100];}Class s:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 655))

    def test_656(self):
        input = '''Class G:__{}Class T:T{Var mK:U;}Class _{Val $o_4713,$0_,__t:Array [Array [Array [Boolean ,0B1],0B1010110],0x12];}Class _8{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 656))

    def test_657(self):
        input = '''Class _{}Class E3:_C{}Class _A3{Constructor (__V:Array [Array [Array [Array [Float ,0B111101],0X3F],0b101000],0x4_F_9_5_2_B]){}$E(N,_:_){}$6(n6_,__T7,U1:q){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 657))

    def test_658(self):
        input = '''Class _:_{}Class _{}Class _{Constructor (_:Float ){}$_z(__:Array [Array [String ,2],2];Aq,__:Array [String ,0x92];z____0w9:Boolean ;cS4:_L4;___:Array [Boolean ,0b10011_11];_,r___:Array [Float ,04_3];Q,tHI:String ;M,b_,_3:Boolean ;w_:Array [Array [Array [Float ,0x4D],38],0x4D];_:Array [Boolean ,05]){Break ;Var w_H:r;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 658))

    def test_659(self):
        input = '''Class __:e{Destructor (){Return ;} }Class F:_{}Class _G:n8{_(snh2,U,_5,h:Array [Float ,0x2]){ {} }Var $__,$_,$10,$W,_y:Array [Array [Array [Array [Array [String ,0B1100],0X629],0B1100],99],0B11_101_1];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 659))

    def test_660(self):
        input = '''Class _a:C{$Rl(){} }Class _:__{}Class y_:A9{Val k,M_,_:Array [Array [Array [Array [Float ,02],0xE],71],0b100110];}Class _:q_{Var q:Array [Int ,71];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 660))

    def test_661(self):
        input = '''Class hu_5:_tJH{}Class T{}Class _{Constructor (_____4,___6w__:Array [Array [Float ,96_9_3],0116];_8:C_0_7;_:Float ){}Val $_:Un;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 661))

    def test_662(self):
        input = '''Class _B_:j{Constructor (_,n3_,V,d:_;_:Array [String ,0X9]){}Var $h_e:Boolean ;Constructor (_17,m,x:Boolean ){}Val $3:M;Val $___9_,$g,_:Array [String ,045];}Class d{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 662))

    def test_663(self):
        input = '''Class _:__1___{Var $_zKL:Array [String ,0x7B_CD9_D];}Class _:y67{}Class _1_:__{}Class _:_V_JV34{Val $f,cj,$W5,$H:Array [Boolean ,037];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 663))

    def test_664(self):
        input = '''Class _I_M{Var $0_:Array [Boolean ,0x37];Constructor (XkO,r__:Array [Float ,0x2]){}Destructor (){}Constructor (){}Destructor (){}io(){} }Class hN{}Class _{__B____(){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 664))

    def test_665(self):
        input = '''Class _:_V{}Class _Uk:N3{Constructor (_,_,ly,_:Array [Array [Array [Array [Int ,0b110001],0X1D],0XB_0_18],0b110001];B:_){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 665))

    def test_666(self):
        input = '''Class R2:i6{}Class _:_{Destructor (){ {Var _:Array [Float ,61];}Continue ;} }Class __S_4_L{}Class _:__{}Class __H_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 666))

    def test_667(self):
        input = '''Class S:tN{}Class _Y:e2rf_4{}Class _6:R{Val z_0Y4,_:String ;Var $6r,_ND:Array [Int ,0XB];Constructor (){T::$_H();}Val $_,$3,$_,$T5M:_T_K_;Var $3_B1V_,bK__5,$_,_9r:Array [Int ,0X12A1];Destructor (){} }Class _:___2{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 667))

    def test_668(self):
        input = '''Class _1c_0z9_{Val $_,f_:Array [Array [Array [Array [Array [String ,067],067],5],067],0B11111];Constructor (__q,_0,_4_e80,v:Int ;_YO,_:Int ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 668))

    def test_669(self):
        input = '''Class _kd{Val _,_AzP__:String ;Destructor (){} }Class _2{$_(){Break ;Var _G:Array [Int ,8];} }Class _{}Class _A3:w{}Class _:p2{Val X:D;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 669))

    def test_670(self):
        input = '''Class ek{}Class _6:D{Destructor (){}Destructor (){}Destructor (){Continue ;}$_r(){Var __:String ;}$6G_9(s:_){}Val _:String ;_(oD,_B_2_0:_){Break ;Continue ;{} }}Class __:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 670))

    def test_671(self):
        input = '''Class __:_7{Var $8,M,$_3_:Array [Array [String ,0B1],065];}Class AW9:__{Val $f:Array [Array [Array [Int ,0b1011001],07_2],7];Constructor (){Return ;} }Class V:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 671))

    def test_672(self):
        input = '''Class _{Var $t,__,$96,W7,$___,__,X,f:String ;Destructor (){}Val z:_F_V;}Class _8{Var _R:Array [Array [Array [Array [Array [Array [Boolean ,0xA6_B],0142],03],0B1],0X32],0B1001101];}Class _{Var x,_6,$R:Float ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 672))

    def test_673(self):
        input = '''Class _o:k{Val C6:_j;Val $_c,$6R_:Array [Int ,0b1_11];Destructor (){}Var G1,Pi_9eW:Float ;}Class u_0:M{Var _m:Int ;_C_(){} }Class _H:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 673))

    def test_674(self):
        input = '''Class _M_:k{}Class _2j{Val Lt5:String ;}Class __{Constructor (g:Array [Array [Array [Array [Boolean ,01],01],0X4],01];y:Array [Boolean ,0B1]){Break ;Continue ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 674))

    def test_675(self):
        input = '''Class H{}Class _0V{Constructor (c:Array [Boolean ,33]){ {Val _:Boolean ;} }Val w,wS0:Boolean ;}Class _:__{}Class l_D{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 675))

    def test_676(self):
        input = '''Class F:Pm{}Class i{Destructor (){}Val $9:Array [Int ,0400];_t(_,o_:Array [Array [Array [Float ,04],99],04];i,_f,l_:String ;_L,F_,Q8_:_5;_:Boolean ;s_:String ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 676))

    def test_677(self):
        input = '''Class DB:Q_{Destructor (){Return ;Var _09,ZmNF3:Array [Array [Int ,0140],0X47];}Constructor (){Break ;}Val $_:Array [String ,0X47];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 677))

    def test_678(self):
        input = '''Class I{Destructor (){}Val _N3,$M:Array [Array [Array [String ,0b111001],0140],0b1_1_0_1_0_0_0_1];}Class U{}Class G_M4_0__5x{}Class _{Constructor (_55:Int ){}Var $1:__;Var _5A,$0:_;Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 678))

    def test_679(self):
        input = '''Class A_{Val $1,_,m_:q_x;Constructor (EG9:Boolean ;d,_,_0:KzI9__;Q15,g1:Q_r;j,_,__4_1,_,u,J,C_:__W7h_;A,w,Q:Array [Int ,64]){}$86_8_5V(){Self =WM3::$L_3_;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 679))

    def test_680(self):
        input = '''Class VK_:k{Q(y:Array [Array [Float ,22],0B1];R,vo,_,B_:Boolean ;_,E:VB9;___,S,n_:Int ;dK:Array [String ,1_8];V2:Array [Array [Array [Float ,0XF_B],30],575];Q8A,So:h;_69_,_,W,G:Array [Float ,0xA3]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 680))

    def test_681(self):
        input = '''Class f:_{Val _6j,_,_70,$5,$4BJ_Y_,$0:Float ;Val z:i;Val $_,_:Array [Array [Array [Int ,0B1],0X6],93];}Class n:_P{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 681))

    def test_682(self):
        input = '''Class h5:_{Var _z_,m:Array [Array [Boolean ,0xB],0X5B];Constructor (__,_:Array [Int ,0XD];_j:Array [Array [String ,0X9],071]){}Val _84,f:Array [Boolean ,38];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 682))

    def test_683(self):
        input = '''Class _{Constructor (_,_:Float ){}Constructor (_:_0;Z_,_,L,_,s:Float ;j,P:String ;_,_,_,AX,a,__6_:e6j_){} }Class a{Constructor (){} }Class Z_:r{}Class _4{}Class _{Val $9,FC8_9,$5,_:Array [Array [Array [Array [Array [String ,7],45],02],37],0B100000];Var _,$h:_x;}Class C7h_5:h_q_5{}Class R2{}Class Fk{Var $_:Int ;Destructor (){} }Class G{}Class _:m6_{}Class _S_1_q{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 683))

    def test_684(self):
        input = '''Class _Y4Q6S_:q{Val $Pq,$N,$_,$_,$_2_,$_S:b;$d(S03F5:Array [String ,0X40];_,p:oa;_cC6,_n,Q74,f72:Array [Float ,0X2_F];m0E:Float ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 684))

    def test_685(self):
        input = '''Class _:_2{Val $8U4:Array [Int ,0134];$1(_27_,y:Array [Int ,97];Bj,G_,_,_1,_A,_,m,_,_:Array [Array [Int ,0b10111],04_35]){}Var $_:_g;Val _:_6;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 685))

    def test_686(self):
        input = '''Class o{Var $__XN,_:Array [Array [Boolean ,0x1],020];}Class T:Cb{Var _Ty:String ;Constructor (_4L,__,Y:Array [Int ,0X10]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 686))

    def test_687(self):
        input = '''Class _:v{Destructor (){}Var $9:_;Val __:L;Val $ms7XbD_:Array [Array [Array [Array [Boolean ,063],8],04],0b1101];Destructor (){}$4s(_:Array [Array [Float ,18],18]){}Var $_9,$_:Int ;}Class _{Val _:Ol;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 687))

    def test_688(self):
        input = '''Class _:_1{$__(_p,g,_9k1a_,_1_5:Array [Array [Float ,0x28],032_4];w:Array [Array [Array [Array [Array [Int ,011],0X57],011],0x28],0x28]){Continue ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 688))

    def test_689(self):
        input = '''Class R{Var f,_,I,__W__8:Array [Array [Int ,0x35],040];$__K9_v(x,_:Boolean ;b_z_ak_:Float ){Var __9_3J_:Array [Array [Array [Boolean ,040],04],06];Var _:_8;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 689))

    def test_690(self):
        input = '''Class K4:_l55{}Class _:X{}Class _09:_{}Class M:B{Var $V,$__:Array [String ,0B110001];Var $0,$__:Array [Array [Array [Boolean ,0b10],0132],9_8];Destructor (){_::$K();} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 690))

    def test_691(self):
        input = '''Class o__{Constructor (_:Boolean ){Val Qu_m:Array [Array [Array [Array [Array [Array [String ,0b1],0b1],58],0x15],0B100010],0X2];Return !!!2.8._;Break ;} }Class J{}Class ___{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 691))

    def test_692(self):
        input = '''Class U:Y{Constructor (){Continue ;Val A_,c:Array [Boolean ,0101];} }Class o{}Class X__7_X:r{$6MU(DR_282:_){} }Class __4:M{}Class tp9_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 692))

    def test_693(self):
        input = '''Class _E_{Var $0_:Array [Float ,067];Constructor (lj_,_,y,__:Array [Int ,0B10_11_1];_:Array [Array [Float ,067],0b10]){}Var $v:Int ;q(){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 693))

    def test_694(self):
        input = '''Class p:_8_{Val $_7,$__,_,$K_,$ze,$sw2k:D88v;}Class _:_S{Val __:Array [Array [Array [Array [Array [Array [Array [Float ,0B1100001],02_60],010],1],3],0xF_5_ED],040];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 694))

    def test_695(self):
        input = '''Class g4:E5f{}Class _{}Class y{}Class p8{}Class X4{_(_6IV,I:o__;__m_:Array [Boolean ,905_19]){ {Break ;} }Constructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 695))

    def test_696(self):
        input = '''Class H{}Class _{Var d_:Array [String ,7_1];}Class Z{}Class A_:_{Destructor (){} }Class A:_1_1{Val g:Array [Int ,0102];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 696))

    def test_697(self):
        input = '''Class _q7{}Class _{Destructor (){}Constructor (){} }Class Z:H{}Class ___75_8:_f{Constructor (E_:_;A,wC6_:_){}sY_(J_,V,__3o,z,D7_,gr_:Array [Array [Array [Array [Array [String ,0114],5],0114],83],0114];J3v:Array [Array [Array [Int ,0X7],6_71_453_0_36],0b1010110];X:Boolean ;_,_k,__k,W,_3_:Array [Array [String ,0B1],0b1010110]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 697))

    def test_698(self):
        input = '''Class o24:C_{q(_a__:_den_R;r:Array [Array [Int ,07_5],0b110101];_:Array [Int ,72];ki,N__,U1:String ;y,__,K,VB:_;W5_3G1R:String ){}Val $jgg,m:Boolean ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 698))

    def test_699(self):
        input = '''Class t{}Class _{}Class t:G{}Class ___U:__{}Class _{}Class _4:y{}Class SW_:r_8{Var _,$_8y04,$Zl,$__,__:Array [Array [Array [Array [Boolean ,0x2_24],034],0b1001101],0671];Constructor (bI:Float ){}_(Y6:Float ){} }Class U:H74{Constructor (){}G(Z0H69_:Array [Float ,32];_T_,_A:Int ){Break ;Return ;} }Class _5:Ul_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 699))

    def test_700(self):
        input = '''Class bld:__DYL{$_(O9,w:_){ {} }Constructor (O_:Int ){}$X(jm:Array [Array [Array [Int ,0B1011001],62],013];_,__,N_:String ){} }Class _:_{}Class _8:qO{Var _5:Boolean ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 700))

    def test_701(self):
        input = '''Class oPr{Var M:Array [Array [Array [Array [Boolean ,184_08],5_0],52],52];}Class Q55:_V{Var _,$4,$V_5:Array [Array [Boolean ,0b1],0B1001111];Val $h:_;}Class _{Destructor (){} }Class JT:U_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 701))

    def test_702(self):
        input = '''Class _:_{w9(_:P;V:J;_,R_,F5,__:Array [Array [Float ,0b1],7];M:Int ){Val dY3,g,T:Array [Array [Array [Int ,64],0x2B],0b1011100];Break ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 702))

    def test_703(self):
        input = '''Class ED:W{_b(L3y,_,_,_,u,_:Array [Array [Array [Boolean ,0x6],7],077];_,_,__:Array [Array [Boolean ,0xA],0xB];_:z){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 703))

    def test_704(self):
        input = '''Class _{Val $N:Array [Float ,0B1000010];}Class _6EY{Var ___y,$D:Array [Array [Array [Array [String ,64],0b1_1_1],0X3F],0b10];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 704))

    def test_705(self):
        input = '''Class J4Aj_{Var $85:Array [Array [Array [Int ,051],0x2_6],0B110101]=!__::$7._()+.!__x::$_R_*!Array ();Val $b_,z,$0__,P,q_Q,$45,___:Int ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 705))

    def test_706(self):
        input = '''Class Yd_:_{Var __:r;}Class _:Y{}Class S84{Var $_B6:Array [Array [Array [Array [Array [Array [Array [Array [Array [Array [String ,0x3F],0X2C],0132],0B10101],50],0b10101],0x3F],21_0],0xC],0X9_5];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 706))

    def test_707(self):
        input = '''Class _IL{}Class o:_{Val N:Array [Array [Array [String ,012],05],1];}Class I0q{Constructor (w___,_:Boolean ;g:u__;_,_,Rr2q5:Boolean ){_::$_K1();} }Class _6_{Var __,__577:y;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 707))

    def test_708(self):
        input = '''Class y9__769:_1{Destructor (){}Var $_1y,$I,$__:Array [Int ,8];}Class _:B{Var _:String ;}Class C{Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 708))

    def test_709(self):
        input = '''Class d{}Class _:g{Constructor (){}Constructor (){}Val $Hb__9:Array [Int ,63];}Class Gd{Var BA7:Array [Array [Array [Array [Float ,04],0X2F],0B1100011],05];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 709))

    def test_710(self):
        input = '''Class Y:m_97{Var _1:_B;Val $__:__;Destructor (){}$5(Z,O,w,_:Float ;Zlt,H:Array [Array [Array [Array [Float ,72],9],0B10],0xF]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 710))

    def test_711(self):
        input = '''Class d:o{$l(XU,E5,e_0,___:__7_BWcJ;X5_:Int ;_,___3:Int ;L_:Boolean ){}FRm(o26_6v,Q4,_0,IPu:Array [String ,0X29];_,ay,w,_Z,r50,_f,y_90:_;_oR,_,_:Array [Array [Float ,0b1],3_6]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 711))

    def test_712(self):
        input = '''Class q3{Constructor (e,t:String ;wt8_h_:String ;_,_:Boolean ;N:Float ;__:___y;_,__5_:Boolean ;l:Array [Array [Array [Array [Array [String ,0XF_9EA],0X37],13],27],8]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 712))

    def test_713(self):
        input = '''Class _R__:_N_{Destructor (){Continue ;}Destructor (){}Var $2,$__:Array [Array [Array [String ,06_7],0x8440],0451];Val R6:Array [Array [String ,0X4A],0x20];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 713))

    def test_714(self):
        input = '''Class m:__{Val $_GI8:Array [Array [Array [String ,0B1110],76],0b111011];d(){} }Class _2:_{}Class m:B{}Class qs:__3Z7Hw6r{}Class ai:_5{}Class W_:H{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 714))

    def test_715(self):
        input = '''Class D{Var __p,$__1_,e_,$A:_;Val $_,As,k,$z_:Array [Array [Array [Float ,0B1010001],0X2],8];}Class a_:t0{Constructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 715))

    def test_716(self):
        input = '''Class Yd{Val I_,$__,D:String ;}Class _:_{}Class _{$_(i:Boolean ){Break ;}Var $gU_B:Array [Array [Array [Array [Array [Array [Array [Int ,0XA_E],0B1_0],0x4],0B1001],0xE],0b1],04];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 716))

    def test_717(self):
        input = '''Class b{Destructor (){Continue ;}Var $q:Array [Array [Array [String ,77],0B111],4_4];Var $K:Array [Array [Array [Array [Array [String ,0B111],0X52],2],0b110_0],05];Var r_,__,K_1I:Float ;}Class _{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 717))

    def test_718(self):
        input = '''Class C2:_u1{}Class _:_XU{Constructor (){} }Class _Qu{V(_:Array [Array [String ,85],0b1]){ {Return ;}Return ;} }Class _:pl{Constructor (_5:Int ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 718))

    def test_719(self):
        input = '''Class wJ7{_l6(_:Array [Boolean ,0B1001110]){} }Class _{M_N_(_,_:Boolean ;_6_:Array [Float ,0xF]){}Constructor (){} }Class _Fv4zX{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 719))

    def test_720(self):
        input = '''Class _{Constructor (){}Var $O,$c_,_,KR,$L__,__b_7,u,$G5_,_7:W;}Class Kz:__0{}Class P{}Class _:_T{Var A:Array [Array [Array [Int ,206_1],59],0X8];T(_,_,_H,r6_:Array [String ,06_2_7];_:_;h_6,__:String ;_6:Boolean ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 720))

    def test_721(self):
        input = '''Class H{Val _7_N,$__,g,A3:Array [Array [Array [Array [Array [Float ,7],04],0XCF],0XB],0103];$____(s,y:Array [Array [Array [Array [String ,0103],0b1011],436_8],0X9AED1];__,Mz:String ;z5,___3,__:_){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 721))

    def test_722(self):
        input = '''Class ___xp:p_R{$3E__rqk(h:Array [Array [Array [Array [Array [Array [Boolean ,0X2],055],02_3_40_2],908],055],26];_8,_:Array [Boolean ,0xC]){___::$_();}Destructor (){}Val $6c_,T,N:Int ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 722))

    def test_723(self):
        input = '''Class W_{Val $s2_0fD2d,___1,$26:__;_(_,_,_:String ;_,_,X:Array [Array [Array [Float ,8],0X4_7_0F],1]){}Val $__,$o2L:Float ;Val $Q5_:Array [Boolean ,0b1];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 723))

    def test_724(self):
        input = '''Class __{Constructor (_:Float ;_,_,_,h9:Array [Int ,0b1001101];x,_,_79:_;Uy,M_,_,j,_:Float ){}Var $6:Float ;_(p6:Int ;S,_,_:Float ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 724))

    def test_725(self):
        input = '''Class c{}Class M{}Class _{}Class __0:_e{Var $7R:Array [Int ,0XD_0B6D];Constructor (){Return ;Continue ;} }Class I_{}Class Zf18_D{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 725))

    def test_726(self):
        input = '''Class _:_{Var $o,$ao4_,_,_:Boolean ;$M(d0_,__3____,_JP0,_I,_2:String ;X,_:Boolean ;_9:Array [Array [Array [Array [String ,0x5],0b1_10],0x6],0b1010]){Break ;} }Class _s:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 726))

    def test_727(self):
        input = '''Class _A:Rr_S{}Class QI{$6(_Y,U,_H8:Array [Array [Array [Array [Array [Int ,0x4A],6],3],0b1],06_3];HO:Float ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 727))

    def test_728(self):
        input = '''Class e{Var $V,O,p:Array [Float ,0b10000];Constructor (n,I9u_,_:Array [Boolean ,05];G:Array [Array [Array [Int ,0B1100011],3],0B1];C_,R_,a:Array [String ,0B1100011];___,xK:String ){} }Class _2_{}Class W:t_5{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 728))

    def test_729(self):
        input = '''Class _J_X__8_:_X{Val $_,$_CU:_;Val $L:Int ;}Class _:C4{Val $_l,T_d0g,$_0T,$95:Array [String ,07];Val $__g_:L5_;}Class Y:__9{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 729))

    def test_730(self):
        input = '''Class B{$e(_06i_:Array [Array [Array [Array [Array [Float ,0b1],075],0b1_001],065_1_2],0X2B]){}Var $_:Array [Array [Int ,0xA],030];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 730))

    def test_731(self):
        input = '''Class bj_{Var _,$0:Array [Boolean ,017];}Class _0{$02_(_:String ;_:Array [Array [Array [Array [Boolean ,0X1A],017],0X1A],15];_N,e_3,__,_:_;d55_s,r:Array [Float ,077];jCZ23_,_:Array [Boolean ,0B11100];d,Y,__W,_8_1,I:K_5){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 731))

    def test_732(self):
        input = '''Class _:_{$_i_11_(_u___,_M2,ag:_f0;Oe1_6:Float ){}Val d,$__,_:Array [Array [Array [Array [Array [Boolean ,0X6A],37],37],37],041];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 732))

    def test_733(self):
        input = '''Class _:__{Constructor (jI,G,__:Array [Array [Array [String ,0X1],0xE],77];X,T:Array [Int ,0133]){}Destructor (){} }Class f{Val _:_;Val E_:Array [Array [Array [Float ,77],7],0133];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 733))

    def test_734(self):
        input = '''Class __{}Class _:__4{Constructor (){}Constructor (B:_r2){} }Class G:_1{Var $3,$if,VNIy,$39,h2,$_61_:Array [Array [Array [Array [Boolean ,0x453_7A_7],015],015],0b1];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 734))

    def test_735(self):
        input = '''Class o:_3{Constructor (){Return ;}Destructor (){} }Class _5_:_d{B1_4(x,Y:_;rM:Float ;_:Array [Int ,0103];_,e,Qe:Boolean ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 735))

    def test_736(self):
        input = '''Class q{Constructor (){}G(_8,__F1,z_E_4,J_H,__6:Boolean ){}Constructor (J:Array [Float ,07];g,_,_g,_ao8,_6:W){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 736))

    def test_737(self):
        input = '''Class U_{}Class __S{Val $15,_V3:Array [Array [Array [String ,1],0112],0b1000001];}Class K:R{}Class a_{}Class _N:Z{Destructor (){} }Class _:_{Constructor (m:Array [Array [Int ,03_6_2],0B11000];dB,Q2_:Int ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 737))

    def test_738(self):
        input = '''Class _{Constructor (c:Array [Float ,0B1110]){}Constructor (s:Array [Array [Boolean ,7_86_8],5];_KP_r:String ;_LGp,z6:Array [Int ,077];O:Array [Array [Array [String ,0B1],0xF],0B1110];_:Float ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 738))

    def test_739(self):
        input = '''Class M__:Jp_{Val uH__8,G_3,$_,O:Array [Array [Array [Array [Float ,0xF_1],38],0B1_1],0xE];Val $9,$87,g:Array [Int ,05];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 739))

    def test_740(self):
        input = '''Class F_{Var _d7_q,J5:Array [Int ,4_2];Val $_:Array [Array [Array [Array [Array [Boolean ,0x97],46],0B1],0B1011010],077];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 740))

    def test_741(self):
        input = '''Class x0_{Constructor (Y_,f,_,_:Array [Boolean ,6_719]){Break ;Return ;Return ;}Val $D,U,$I_u_q_8,_:_z;Val _3,$14,$_:Array [String ,0X31_7];Destructor (){}Var _D_:Boolean ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 741))

    def test_742(self):
        input = '''Class _c{Constructor (){}Var T,__,qM,$o_63,by_,___1:Boolean ;u(_n:p;C:Float ;R2:Array [String ,0xC_2]){Return ;}Val _,$1,$u4_:Int ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 742))

    def test_743(self):
        input = '''Class _w:M{Constructor (_:Array [Float ,3_18_8];z,_z:Float ;N:_Y;_s:Array [Array [Array [Array [String ,80],05],0104],0X6_C]){Continue ;} }Class V:H{}Class W{Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 743))

    def test_744(self):
        input = '''Class _u{Constructor (o8__8:Array [String ,0X6];o_7__4G:Boolean ){}Val _:Array [Array [Boolean ,0x31],04];}Class H{}Class m{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 744))

    def test_745(self):
        input = '''Class X5{Val n:Array [Array [Array [Array [Array [Array [Float ,0X5D],0X5D],0B1],076],0X2BB],045];Var $4U,$26__t7:_;}Class I{}Class a:R_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 745))

    def test_746(self):
        input = '''Class _{Val _,$__q,$Wh9:Int ;Var b,_:Array [Boolean ,07_77_43];_(_,_:N_3){}Constructor (___67_o:Array [Int ,0XE];_:String ){} }Class _0_0:R{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 746))

    def test_747(self):
        input = '''Class Vj5:n{}Class Hj:Q_{Var $_:Array [Array [Array [Array [Array [Array [Array [Int ,23],0XC],4],02],73],07_3],034];}Class _3:_{}Class _:C88t{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 747))

    def test_748(self):
        input = '''Class _:Vp_1{Var $0,$q_L_,$1_:_;Constructor (m,Z,_U:Float ;l_,Hh8,a:Array [Array [Array [Array [Array [Boolean ,7],0XE],0x30],23],0X3C];_:qd){}Var $__dX,$8,_Q:Int ;}Class _:__{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 748))

    def test_749(self):
        input = '''Class O_yQ20{}Class _m:__{Var yNbH:Boolean ;__(){} }Class __{}Class m:by82_{Var $79:Array [Array [Array [Boolean ,0B111111],1],1];_(H3,k:Float ){Continue ;Continue ;}_(){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 749))

    def test_750(self):
        input = '''Class _22:_{Var Y,$_I:_8;Constructor (){}Val W,$lZ1,$___1,_,t,$0j,$3v,$__42z:Array [Array [Boolean ,0B1001101],0124];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 750))

    def test_751(self):
        input = '''Class m:W{}Class ____:m{}Class _{}Class _{Destructor (){}Var $_,_RlA,$_,_g,G__z9:Array [Array [Array [Boolean ,01],0B10],0133];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 751))

    def test_752(self):
        input = '''Class t0:Z_{Val $_C:String ;}Class __9{}Class _bpFaH{}Class q{Constructor (r_:ue){} }Class b{}Class L:Fa_7{}Class _{Constructor (){Continue ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 752))

    def test_753(self):
        input = '''Class M:_{Var __7__,$_:Float ;p(_,_,_20,BiN:Array [Int ,0b1001000]){} }Class _b_{Var mz,_:Array [Array [Array [Array [String ,0b1001000],0b1_0],0B11],0X48];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 753))

    def test_754(self):
        input = '''Class Le_{}Class h:F{Destructor (){}$4827(X:Float ;_,G48:Array [Array [Boolean ,0X8],041];_il_,K:Int ;VM:_Y){t_::$k9();Break ;} }Class _{}Class k8_y:___{}Class d{Val $_4:Array [Array [Boolean ,0B1],041];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 754))

    def test_755(self):
        input = '''Class _5F9_:L_i{Constructor (__:Array [Int ,69];h34Z,_,p7:Array [Array [Array [Array [Array [Array [Int ,037],04_2],69],0XD],035_7_7_1_0],39];r,_K:Array [String ,69];W_,_,_:Array [String ,0B1010010]){} }Class _P_O:R_{}Class _6{}Class _:m1{}Class S{Constructor (m,Tg,_O,_B:Int ;_E:String ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 755))

    def test_756(self):
        input = '''Class _9__{}Class _:_{}Class Q_J{Val $7,b_,u,$8:Array [Array [Array [Array [Float ,0B1010010],0B10],0B1010010],0X48];}Class _9Q2{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 756))

    def test_757(self):
        input = '''Class iE{}Class _:e62{Val $_q_,__:Array [Int ,035];Destructor (){}Constructor (){} }Class __:_0{}Class I333:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 757))

    def test_758(self):
        input = '''Class m_:_7{Constructor (m,K2,_:Array [Array [Array [Array [Array [Array [String ,1_052],0xC3],48],4_8],0B1011011],0x3C]){Return ;{Var _,_x:String ;} }}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 758))

    def test_759(self):
        input = '''Class _{Constructor (_,_,_V:String ;J:Array [Array [Array [Array [String ,0B1],0b1],7_6_9],56]){}$_(y,C:Array [Array [Array [Array [Boolean ,0b1],0X59],0b110011],0X1]){Break ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 759))

    def test_760(self):
        input = '''Class _8_{Val $U9:Array [Boolean ,0B1000000];Constructor (__:D;_:Array [Boolean ,0X5];__6Z_7,dm,c__:Float ;n:Int ;_,__F,P,_,X:_t){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 760))

    def test_761(self):
        input = '''Class E{}Class _4:fP6Oe2_v_g{Var _5:Array [Float ,0B1100011];_(_:Array [Array [Array [Boolean ,46],0136],46];e05rF,_:B){} }Class q_1{}Class Y_{}Class X{}Class e{}Class u_Yj:G_SF{}Class _2{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 761))

    def test_762(self):
        input = '''Class z:__{Constructor (r,A,h,__,U,_:Int ;_G,gH:Int ;_3,_d2o,__6_0t,_,b_H2_,_:Array [Float ,0x4_4_E];__,V_:String ){Val q_:Array [Array [Boolean ,75],0124];} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 762))

    def test_763(self):
        input = '''Class _:_{}Class W{}Class _{Destructor (){} }Class RTrq{}Class _:_{Var $o_c159,$n,$_F:Array [Boolean ,68_4];Var P:Float ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 763))

    def test_764(self):
        input = '''Class _:_{}Class __:_{}Class gK9{}Class TdM{Val $0t:_;$7(G:F__;X,_:Array [Int ,96];_0,_8r69,XR162,T:Array [Boolean ,01];oRC7g_:Float ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 764))

    def test_765(self):
        input = '''Class _7{M_(_fF,U1h___:Array [Array [String ,0b1],0b1101];g9G,_,_X,fC_9:__0_;A,pB:Boolean ){Break ;} }Class _:_{}Class _zn3X{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 765))

    def test_766(self):
        input = '''Class n{Val $DP,$4,_,$v50:Array [Array [Array [Array [String ,0b111001],0x18],0X5D],0B1_10_1_0_1_011];Destructor (){}$5_(){ {} }Val __:String ;}Class _:_{$_(J,B:Array [Boolean ,8]){} }Class _:S4_{}Class _{Constructor (){} }Class _:_B4{Val $_,$__:_;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 766))

    def test_767(self):
        input = '''Class B:_{Var $yR27_6,$_,$4iO,$_03y,_:Float ;}Class h{$f5(C,L,_,C:Float ;Zy:Int ;__:Array [Array [Array [Array [Array [Float ,0X41],32],0B1_0_1_0],0X41],0X89]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 767))

    def test_768(self):
        input = '''Class o_:h{$Y9(){}Constructor (d__:Array [Array [Array [Int ,0X5E],4_1_99],0B111011]){}Constructor (__64,_0W,f_76_4:Int ;IjW,_3w,F_,_,o,_M2C67:Array [Array [Array [Boolean ,7],0b1],06_2];FO,E,h,_,__Y_:Float ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 768))

    def test_769(self):
        input = '''Class _{}Class _:_{Destructor (){Continue ;}Var _:Boolean ;Destructor (){}Val $a:Array [Int ,0X6];}Class Q:G{Val i,_9,$M:Array [Array [Array [Boolean ,0B10010],0X2],8];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 769))

    def test_770(self):
        input = '''Class __{Var Q,$X,$27L,_KP:Float ;Constructor (N:String ;_5:Array [Array [Array [Array [Int ,0b101000],07],0X4],67]){Break ;Return ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 770))

    def test_771(self):
        input = '''Class M:j{Val __g7,x_01_:Array [Boolean ,040];Val $2f:_m1_;m(D_1_2:Int ;_8:Float ;__:D;V,__:Int ){}$C(_:_){} }Class R{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 771))

    def test_772(self):
        input = '''Class _Q{}Class __:X{Val $5:Array [String ,0x8];Var $2K,$_,$9:Array [Array [Array [String ,0B100101],0XB9D_A],2];}Class _G{}Class O6Tuz{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 772))

    def test_773(self):
        input = '''Class __z{Var t:Array [Array [Array [Boolean ,0B1001111],0X3_CDE],04];}Class Vd:S{Constructor (){} }Class X_T1:Z8{Constructor (_n___,yG,n___:a){}Val $k:v;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 773))

    def test_774(self):
        input = '''Class xR{Val _,$Z58:String ;Constructor (__:_6){}Val $_,__,_,I:Int ;$_(){}Destructor (){}Constructor (){} }Class y:_{$3(){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 774))

    def test_775(self):
        input = '''Class Ow_{Var _:Array [Array [Int ,8_5],0B11010];Val $2:Array [Array [Float ,0b1],45];Var $z__:String ;}Class x__j_:_{}Class g:Y{}Class _:otU{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 775))

    def test_776(self):
        input = '''Class _l_Ek09{}Class _9{r(){_::$__();}F_(X:Array [Array [Float ,54],023]){d::$_();Continue ;}Constructor (){}Var V1:Int ;Constructor (_:String ){}Val _1,L73s3:String ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 776))

    def test_777(self):
        input = '''Class y0{Var __,_1:String ;Var z:Float ;Val $3h_,$c:Boolean ;Constructor (){}$8(__E,B,___,l,_:_R;___,_p:Boolean ){} }Class i_:Gz{}Class _:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 777))

    def test_778(self):
        input = '''Class W9:_{}Class K:_{Var M:Array [Int ,0XD_D_3];Var _:Float ;}Class _:_2b{}Class f{}Class I{}Class _u{}Class _1{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 778))

    def test_779(self):
        input = '''Class N_:_s{Destructor (){Return ;} }Class p00:J_1m{Var $EW4,_W,x,__F,$N_,$p:Array [Int ,0x57];}Class D:E{}Class LA{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 779))

    def test_780(self):
        input = '''Class R{Destructor (){}$_(nW_Iz,_35,FF,j_,_,_:Array [String ,60]){}v0(){}Val _:String ;Constructor (){}Val V8:Array [Boolean ,0b11011];}Class __{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 780))

    def test_781(self):
        input = '''Class _q:_Q3{$f_(_S:String ;__,_:Array [Array [Array [Array [Array [Array [Array [Int ,025],16],074],6],0XC],0xFA],0b110001]){} }Class __{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 781))

    def test_782(self):
        input = '''Class O:_{Constructor (T_80ov10M,_:Array [Boolean ,0B10];u,_,BY_T,_:Array [Int ,0x2E];__:Array [Array [Boolean ,0xE02],0B11];p,u0,M_HWg,bR:String ;__,_zA2,h,r,H_b73:_M;_:V08){} }Class DF__{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 782))

    def test_783(self):
        input = '''Class _:b_Ip_{NX28(R9W:Float ){}Val _:Array [Array [Array [Int ,0676],0B1011110],0X52];Val _u:E;}Class D:__{}Class _{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 783))

    def test_784(self):
        input = '''Class _846:S3{}Class IT:_{Var $__y:Array [Array [Boolean ,0B1011101],45];}Class cA{Constructor (kXSa23:Array [String ,54_62];_m,J:Boolean ){} }Class U0_z8Ey{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 784))

    def test_785(self):
        input = '''Class _q{_(z_Q,__6_5:_;Ev_t,__c:Array [Array [String ,021],062];_,__:Array [Float ,0x96];F_:Array [Array [Array [Array [Array [Boolean ,03_4_7],0b1],29],0x9],021]){}Constructor (){Break ;} }Class _A{_(){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 785))

    def test_786(self):
        input = '''Class __:o{Constructor (_,u:Float ;x6,G8,_,qj,_3__59L,_:Array [String ,03_5_5];j:String ;W:String ;g4:Array [Array [Float ,0xF],0b101];_:_;r:_;I:__;_V:Array [Float ,0B1]){} }Class _iCv{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 786))

    def test_787(self):
        input = '''Class U{Val $Tx:Array [Boolean ,0104];Var $_,$1l71z_w7:Array [Array [Array [Int ,0B111110],0104],0b1010100];Val $_:Float ;Destructor (){}Val w:_3_;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 787))

    def test_788(self):
        input = '''Class __{}Class M1:J{Destructor (){} }Class J{Destructor (){}Destructor (){}I_(sCnW_:o_Y;m6,_,Z,__:r;_86,q5,mK_____,z,_:W_){} }Class q_{Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 788))

    def test_789(self):
        input = '''Class ___9841:_{Constructor (oo_:Array [Float ,6_1];_,m:Array [Boolean ,0xA]){ {}Break ;}Constructor (){Return ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 789))

    def test_790(self):
        input = '''Class hl6E:A{$_(f,w26N:String ;hW,__,_,N:Int ;Y:_gR__L;m,U_,k:Array [Boolean ,0134]){Continue ;} }Class __3:__6_r{Var ___0,$_u5B,$a:R;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 790))

    def test_791(self):
        input = '''Class A:v{Constructor (s_:_;I,j,qh,U:l;f,_:Boolean ;Oj:String ;N_,_F:Int ;_:Array [Array [Array [Array [Array [Boolean ,9_9],06],0611],0x34],0x34]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 791))

    def test_792(self):
        input = '''Class _6:_{Val _28,$K:J;Destructor (){} }Class _{}Class Q{}Class __zd6K_2q45u__:_6_{Constructor (o9Q1:Array [Float ,0XE]){}Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 792))

    def test_793(self):
        input = '''Class _:_R_6n_{Constructor (_:_;_4N7:Array [Boolean ,24]){} }Class _:IJC{Val __,kx,$nr3Nv9_1m:Array [Array [Float ,0B10],057];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 793))

    def test_794(self):
        input = '''Class IP:e{Destructor (){}Var $_,$_,j:Array [Array [Array [Array [Array [Float ,52],42_0],073],0b1010011],55];_Yi(){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 794))

    def test_795(self):
        input = '''Class L:M_{Constructor (){}Constructor (pL34_,b,__:Array [String ,0X4C]){}C(VP_,U:_;_u:Int ){}Var A:Array [Boolean ,96];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 795))

    def test_796(self):
        input = '''Class Zq_H{q_H3(__:Boolean ;_:Int ;_v_,_Jv,m:Array [Int ,0B1011110];D6f8_,__,yN46f_v:_LS;_W_5:Array [Float ,0b10001]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 796))

    def test_797(self):
        input = '''Class h:_{Constructor (){Val _,Y:_;} }Class Ir_{Constructor (e2X:Array [String ,0b10];c_t98_,_,_:Array [Array [Array [String ,0142],0B1_1],61];_,I,__78335:_){Return ;}Var $pF,$w,$_0_:_f6N;_7(er:String ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 797))

    def test_798(self):
        input = '''Class __:___J_7{Var _:Array [Array [Array [Array [Array [Array [String ,0x3C],05],0b100100],49],49],0b1_0];Destructor (){}Val a_:Int ;Constructor (){Break ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 798))

    def test_799(self):
        input = '''Class W:__{}Class H{Constructor (an_7_:Array [Array [String ,0x4_AC0_7],53]){Return ;} }Class N{Var _:s;}Class t:_{Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 799))

    def test_800(self):
        input = '''Class _:_{}Class h:_{}Class _:a3{Val _,__,_:Array [Float ,93];$i(R:Boolean ;_:Array [Array [String ,023],0X9]){} }Class _0r:KnV_{}Class v:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 800))

    def test_801(self):
        input = '''Class Ht9{}Class _27:T{}Class __S_:__{Constructor (){} }Class J{Var $_:Array [Array [Array [String ,0x2D],0142],0142];}Class e_43:m{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 801))

    def test_802(self):
        input = '''Class e1f{Val $_,_:Array [Array [Array [String ,1],0B1010],0b10_1];Var _,$nzZ2j_Nn:Float ;Destructor (){}Val $_u:_2H5X5;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 802))

    def test_803(self):
        input = '''Class X_{$9(_,I:Z;GP:__;_:xY;_:Array [Array [String ,0B110011],056];__:Array [Array [String ,0b1_0_1],9];Q:T;O_,U:C42G;k,__a,d9,_:Array [Int ,056];__t_1t,_:Float ;p,m2_G3:_V;_:T2){Continue ;} }Class E{Destructor (){} }Class _zV:H{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 803))

    def test_804(self):
        input = '''Class v_{Val $H,_2:Array [Int ,5];Constructor (W_,L_,U:R){} }Class _{Var $5:Array [Array [Array [Float ,0B1],01],0X1C];}Class _{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 804))

    def test_805(self):
        input = '''Class _5i{Destructor (){}Val $9,F:Array [Float ,042];Var __JQ:v;}Class _93_z:_{Val $q,$_9,$J:Float ;}Class X9{Constructor (w:Q_V){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 805))

    def test_806(self):
        input = '''Class _:_T_{Val y:Float ;$_(_I:Boolean ;_:Array [Boolean ,2];z:String ;u:Array [Int ,05]){}Var $j,$t3,I,$71V:Array [Int ,0B11];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 806))

    def test_807(self):
        input = '''Class X:_L{}Class _:G{}Class _:__{Val n,$5E__W:_;}Class e_{}Class _N{}Class If9___:_{Destructor (){} }Class _{Val __:Array [Array [Array [Float ,060_6_30_56],0120],88];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 807))

    def test_808(self):
        input = '''Class O55{Constructor (){} }Class _7k280b_:s{Val _1:EA;Var _,f__:_o;Destructor (){}Constructor (__:Int ){Break ;} }Class _:X0_{}Class v{Constructor (){} }Class m__1{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 808))

    def test_809(self):
        input = '''Class __b3{_(d,_,mf,nd9:Array [Float ,53];_Y_:_;r,_,Va:Array [String ,05]){} }Class g4{Var $_,l_,i81K:Array [String ,01];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 809))

    def test_810(self):
        input = '''Class _{Val _39,$02_,x:_1;Constructor (_4w,_Ky9:Boolean ;mZ,_,T_,__Zu1,s__96I,_A_p:Array [Boolean ,0b1]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 810))

    def test_811(self):
        input = '''Class g_1{}Class __:K{_(){Continue ;Break ;Break ;Val a,_G:Array [Array [Int ,02_7_0],05];} }Class m_6_{w9(){Continue ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 811))

    def test_812(self):
        input = '''Class w:_S{}Class NB:Q{Destructor (){}__(){Var _,x,_:String ;}Destructor (){Continue ;} }Class N8:_{}Class G:F_02c{}Class z0_{}Class jxz{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 812))

    def test_813(self):
        input = '''Class _{Constructor (T,n_,_,_,_,_:String ;_:_8;_:Array [Array [Int ,0x3],0B10110]){} }Class _:C{P(){} }Class fv:HO{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 813))

    def test_814(self):
        input = '''Class _{}Class __0_9:__{Constructor (P0_7,_,_,b5_:_;_p,_m4,S,__,__82:Array [Array [Float ,0136],047]){}Val $l:Array [String ,0b1];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 814))

    def test_815(self):
        input = '''Class _:__{Constructor (C_:String ;_K7:Array [Array [Array [Boolean ,2],0b1],5];_:String ;_:m;BR,__,_8ub7A:Array [Float ,0b111100]){Val _,A,Iv,sed,v_:Array [String ,71];}Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 815))

    def test_816(self):
        input = '''Class _p:__2_{Val $v,M:_;}Class X8:_3_80i2PGB{Val $9a:Float ;Constructor (r,_2:Array [Array [Array [Array [Boolean ,47],0B1],4_91_7],030];_:Array [String ,0X55]){}Val $9:Array [Boolean ,43];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 816))

    def test_817(self):
        input = '''Class l:_27{}Class e{}Class __:_{Constructor (){} }Class h:LN{}Class U01_6:U{Constructor (M_:Array [Boolean ,0B11_1];_t5v:_3;s3G:__;Z__,_zT,_R,B:Float ;_,__Sr:l;_5T:Int ;v,_91,J_:Array [Int ,043_6_7_21_0_5]){} }Class J54{}Class _r:_{Constructor (){}Val $U,_EZ_U,$i7:Array [String ,0xA_11];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 817))

    def test_818(self):
        input = '''Class k21{$_V(QF:wH;Y,_,lU:Array [Float ,8]){Continue ;Continue ;} }Class _6{}Class U:s_{Var $____2:Array [Array [Int ,0X4E],0107];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 818))

    def test_819(self):
        input = '''Class o:n{Constructor (G_,F_,w,WP:Array [Array [Int ,8_6],6];_:Array [String ,05];__BAP:Array [Array [Array [Int ,6],0121],0b1]){} }Class _{}Class Wl{Constructor (){Break ;} }Class f{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 819))

    def test_820(self):
        input = '''Class _1_0:_{_pk(_:t1;r:Array [Array [Int ,0b1000_001],0X4B];XF:C;M:_){} }Class X930G317{Destructor (){} }Class _{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 820))

    def test_821(self):
        input = '''Class _:u{$V__Y(){}Constructor (_t,_3xO,Y,d,_sA_i,_2_w,_,vH8:Array [Boolean ,0X4E];q_,v:Int ;u:Boolean ;_,_:Boolean ;_:d__){} }Class b8:_x5_i{Destructor (){q8::$c_e___();}Val __:String ;}Class zQ:_{}Class V:_{}Class _n{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 821))

    def test_822(self):
        input = '''Class T:_3{}Class k:K6_{Val _:Int ;_l_(_,__3_:Boolean ;o_1__c,_,__08_:Array [Array [Boolean ,06],2_7_4];_4E2,_IC,__i,d_:String ;_,m_:Float ;s,a,x__,a,_6:Int ){Break ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 822))

    def test_823(self):
        input = '''Class f_M:k{}Class __{}Class q{$D_(_,_:Array [Array [Array [Array [Int ,0b1_1_1],0X2F],05],100];_x_,H,SZ,p:Array [Array [Float ,0107],0B1_1_11];_7P_,F734,u,_5Rr9:Int ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 823))

    def test_824(self):
        input = '''Class _K4:jX{Constructor (){}Destructor (){} }Class E_v:X{}Class _s{Val _:Array [Array [String ,5],0b1];Var _r,$_3:H0v_n;Constructor (s2a_:Array [Array [Array [Float ,062_5],0B11110],0b1_01]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 824))

    def test_825(self):
        input = '''Class F:_{}Class _{}Class t7:w5{}Class G{}Class O{}Class _D:q2q{Val __X,__:Array [String ,0X7_9];Var __,$_7,$__,_,_:Array [Array [Array [Array [Boolean ,02],02_3_2],26],06];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 825))

    def test_826(self):
        input = '''Class _:_58X{Constructor (){ {}Val _g,_,u4_,JJ:Array [Boolean ,0XA];}Var _:Array [Float ,0B10];Val M9g:Array [Float ,05_0];}Class _0:_k{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 826))

    def test_827(self):
        input = '''Class _:__4__8P6{}Class _:_1{}Class _{$_(){} }Class X{Constructor (_,_:Array [String ,0X8];_:Array [Float ,100];_:HN){}Val k,$7:F_;Constructor (){Break ;}Val $H,_,T,u:String ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 827))

    def test_828(self):
        input = '''Class t_W{Var _FK:Array [Array [Array [Float ,99],1],055_74];Var W_:Array [Int ,3];}Class w:_{}Class YK:_{}Class qw{}Class s_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 828))

    def test_829(self):
        input = '''Class _{}Class o{Constructor (sl:Array [Array [String ,0B10],93]){Continue ;} }Class _1:_{}Class _38{Var $j_b2,$_6,$_:Array [Array [Boolean ,0B110101],067];_(_,w_:Array [Float ,93];YN:Int ){}Val R0,$5:Int ;}Class E:W{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 829))

    def test_830(self):
        input = '''Class _9{}Class _:__9E{Val _,_1:Float ;Destructor (){ {{Continue ;Return ;}Break ;} }Constructor (){}Val IQ9,$H7,W:_;Var __:Boolean ;}Class Z_:_5T{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 830))

    def test_831(self):
        input = '''Class _:l{Val __,$_,$F,Np,$0x,_,V:g;Val z,yV_Q9,$0:__;v(i591i,W,___,C,g7_35:Array [Array [Int ,0b111111],0X4B]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 831))

    def test_832(self):
        input = '''Class V_8:k__{}Class e:w{Var b,_33:Boolean ;Var $X:Array [Int ,06_0];Destructor (){}$_(a:Array [Float ,0x8E]){}Var l_:_;}Class s:_{Constructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 832))

    def test_833(self):
        input = '''Class _R1:Z24y2{Destructor (){}Val $v:__;}Class _b:f3{}Class T{Destructor (){} }Class _{Val $Q_m_0,$9_,K,$2w:Array [Array [Array [Array [Int ,02_4],03],0B11111],01_3];Var $__1,$T_2:_Q_;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 833))

    def test_834(self):
        input = '''Class _{Destructor (){}$Y(f096:__;__g:Array [Float ,0X6_2];_:Boolean ;__5:Array [Array [Array [String ,01],0B111010],0XB_A];_:Boolean ){}$_(W:Float ;O_:Int ;_f0,_,_,_,G,___,N:Array [Float ,03]){} }Class b7_2{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 834))

    def test_835(self):
        input = '''Class y6{Destructor (){ {} }}Class _{Var $9Y_,_,S_9_6k,$8,g2_,A,$m,$4:Array [Array [String ,0B11],7];Var $__,$Y__V:_;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 835))

    def test_836(self):
        input = '''Class n:____{Val $_U,$01:Boolean ;}Class s{$6_(){_::$8();}Val a:Array [Boolean ,0xF];Var RT,$_:Array [Array [Array [Array [Array [Int ,0X1D],0b10],0B1],79],79];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 836))

    def test_837(self):
        input = '''Class _E_d:Yv{}Class T_:m3{Destructor (){}Destructor (){Val M2,_,o,_9:i2;} }Class F_:_{$_(U,_:Array [Array [Array [Float ,37],0x39],04];_,T:String ;_:Int ;A:v0;x:QX_;Urm:Hz_B;_2:TMb____;_O_r:Int ){}l(ci:Array [Boolean ,0100];_,_,g_:_88;_:Array [Array [Array [Float ,0x39],37],4]){t::$_b();}Var $74948_:A2;Var $_0:Array [Array [Array [Int ,37],0100],37];}Class o:_V{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 837))

    def test_838(self):
        input = '''Class a7:X{Val _:Q;Constructor (){} }Class __:t_{}Class _:__{}Class b__{Var __,$_y_:Array [Array [Boolean ,0x3],06_4_216];}Class B0D{___(f,_,_,___,__j_7:Float ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 838))

    def test_839(self):
        input = '''Class _Ij:D{Val $3:Boolean ;}Class _:a{Destructor (){}Constructor (F,O,q,M,z,_,_h,_:e;z_,__J,i,_:String ){ {Continue ;}{} }}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 839))

    def test_840(self):
        input = '''Class K{}Class _{__(p:Float ;Jh9M:Array [Array [Array [Array [Array [Array [Array [Array [Array [Float ,65],0x1E],0b1],65],0B111011],056_1],6_3],0b1000100],0B1]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 840))

    def test_841(self):
        input = '''Class Y_d{Constructor (){}Constructor (_,_We:Array [String ,0B1111]){Continue ;} }Class Y{}Class ___:____{Var $9,s:Boolean ;Val Q,$09_:Array [Boolean ,0b1];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 841))

    def test_842(self):
        input = '''Class _{Constructor (){Break ;Break ;Continue ;} }Class k89{}Class t{Val W,$2,$j,$77:Float ;}Class n9:o{Val $ZVZ:Float ;}Class _v{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 842))

    def test_843(self):
        input = '''Class _M{Val $1,v:Boolean ;Destructor (){}$1_e5Q(_9:Boolean ){} }Class S{}Class _Tk{}Class q_{}Class _:_{}Class __5M{Constructor (_,_,_4:Array [Array [Boolean ,0b1_01],025]){} }Class _{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 843))

    def test_844(self):
        input = '''Class __:I{Val $6_,$5,$0T:Float ;}Class __:L{W_m(_o,p:Array [Float ,0b1000];F,_:Array [Int ,0107];o___q3:JH__XG8e_3g_78){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 844))

    def test_845(self):
        input = '''Class _:_{Var p:_;Val $_,g,$_0:Array [Array [Boolean ,0XE],0x23];}Class __7{Destructor (){}Destructor (){}_(){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 845))

    def test_846(self):
        input = '''Class zb9:H{Constructor (_,d,S,_VT,a0_:Array [Boolean ,045_0];_F:Y;J_,t,_1,mn,ur,SnJ:Array [Array [Array [Array [Array [Float ,0b1],05],0B10101],4],0B10101]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 846))

    def test_847(self):
        input = '''Class W:__{}Class c:_{$96A(h:Array [Int ,06];_:Array [Array [Int ,0B111100],053];_N0,O,_p8,__4_Ha99,__:Array [Float ,0X55];E,__3w,O,_,t,_:__){} }Class L{Val Ec_,__,$020:String ;}Class _{}Class _U{Destructor (){} }Class _N{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 847))

    def test_848(self):
        input = '''Class Ti:k{$B___(F_4Qn:_;_,T:Array [Array [Array [Boolean ,0x10],0XE6],0B1100100]){} }Class _9:_{Constructor (_,M:Array [Int ,8]){}Val _,$kLt,_,$6:D_6_;}Class M{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 848))

    def test_849(self):
        input = '''Class __{Destructor (){} }Class yO{}Class __1{Var V:Array [Array [Int ,91],0x35];$NO_(r,_,j,_,_a_,_,a,r_:Array [Int ,035_0]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 849))

    def test_850(self):
        input = '''Class M{Constructor (d,_6,__,__:String ;d,_,_:_4__v;__3:Boolean ){}$9(){}Destructor (){}Var $_M,$_,s:_e_Y;}Class _7p_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 850))

    def test_851(self):
        input = '''Class V_:x{}Class e_6:Y{$3B_9(V__,_E_,J,O:Array [Float ,0b11];_,_8_:_;_,_Q37,__,_,_,_9,_98_,A,_,_,_Ub,_:Float ;g___:Boolean ;L_,E:_){} }Class x:_{Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 851))

    def test_852(self):
        input = '''Class _{Destructor (){}$6f(){}Destructor (){}$__(_:A;VF__,ONG_,_f:Boolean ;_,___20F8,___,_T,UN_,Xw,S:String ;MT:B_){} }Class f{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 852))

    def test_853(self):
        input = '''Class r_Sm_Jn_:_{}Class __87:PQJ02D_ML{}Class _{}Class _:z_{Var Z7E_:Boolean ;Destructor (){Break ;{Break ;Continue ;} }}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 853))

    def test_854(self):
        input = '''Class _{Val p6,_,m:Array [Boolean ,10];Var $N_eK4_A0,$_,$_:Array [Array [Array [Array [Float ,0B111100],5],0X98],0b11];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 854))

    def test_855(self):
        input = '''Class _:_{Destructor (){}$1B0(E,_1M,e,x,_,e_0,w,_8,_:Array [Float ,0x40_9_E7_A_F];l:Int ){} }Class Lq:L6{}Class _7E21{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 855))

    def test_856(self):
        input = '''Class _:__{}Class __F_:__{Constructor (_Xz:Boolean ;FvM__,__,e__J:Int ;__,_45:Array [Boolean ,2]){} }Class _:K{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 856))

    def test_857(self):
        input = '''Class f{Constructor (R:Float ;_e2_:_9__;_9_:Array [Array [Int ,0B1],07]){ {Continue ;}Break ;}cS(){}Destructor (){} }Class _W{}Class _{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 857))

    def test_858(self):
        input = '''Class _U_1{Destructor (){Break ;} }Class i:eH{Constructor (H:Array [Boolean ,0142];p_:tC;_t_,_,R:String ;y:Boolean ;_:_D57;_,_,r,_C_7_:String ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 858))

    def test_859(self):
        input = '''Class t:_Ca{}Class _c:_57_2_7{}Class N{Var $4,_,__,$_H6t_,$5ER7_:Array [Array [Array [Int ,0X35],0X35],5_3_9_5_9];}Class _:_9{}Class p{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 859))

    def test_860(self):
        input = '''Class J742{Constructor (){} }Class _1_4_6{}Class M:_YM{Destructor (){Var _,Y:L;} }Class _{Val v:Array [Array [String ,012],0x43];}Class _{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 860))

    def test_861(self):
        input = '''Class G_{Var $3:Array [Array [Array [Array [Array [Array [Float ,0144],0b11_00_1_10],0B1010000],0B10],04],0144];}Class _:_4_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 861))

    def test_862(self):
        input = '''Class _:_Y{}Class Pk:P{$6(_hB:Array [String ,14];CX:Array [String ,0b11]){}$_(){}Var z:Boolean ;}Class ___:JC{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 862))

    def test_863(self):
        input = '''Class _:a8B{Constructor (i_:String ;__12_,i_3:C6;_R,R_:Array [Array [Array [Array [Boolean ,062],0B11000],9],77];CD,_,Q_,_,M9w6_:W){Break ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 863))

    def test_864(self):
        input = '''Class A_:Q{}Class D_{}Class _U{}Class U:y{Constructor (__:Int ;___,_3X:__;aTo:Boolean ;_BC274:Array [String ,0x4C];D,iA_,_:_;c_3,M,e:Array [String ,28];__,_:Array [Int ,0B110]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 864))

    def test_865(self):
        input = '''Class _{Destructor (){}Var _:Boolean ;}Class __3_1a{Val knv:Int ;Constructor (_:__38;i6_M_T_7_c,_,_c7,A1N_6:Int ){} }Class s{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 865))

    def test_866(self):
        input = '''Class _____:s{Val $4u5a,$_,$b,_,$_r,$1_,X7,$_b,$_:Array [Array [Array [Boolean ,0x6],243],0B101100];Var $p:Array [String ,04_5];Val s,$x__,_,m:Array [Int ,0XDC];}Class W{$7(h:Float ;_,_:Array [Array [String ,0X20],7]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 866))

    def test_867(self):
        input = '''Class _41{FG(A2:Array [Array [Array [Boolean ,0B1],0xB0A1F3_8_72],2]){}Constructor (_,z_6,_,d_,___:Boolean ;___,__,I,_:Float ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 867))

    def test_868(self):
        input = '''Class n5:__z{Val $_6,$__,_,a,$_:Array [Array [Array [Array [Array [Array [String ,0XF],46],0B1001_0],0b1000111],46],0b11_0_01];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 868))

    def test_869(self):
        input = '''Class _0:__{}Class z_{Var $_d:Array [Array [Float ,8],0x8];$A(){Continue ;Continue ;}Val $_:Array [Array [Array [Array [Array [String ,076],0b100111],73],0X51],0b1];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 869))

    def test_870(self):
        input = '''Class j{Var _:Array [Array [Array [Array [Array [Array [Array [Array [String ,0x2],04],73],025],8],0x28],0b1000],0B1100011];}Class _80:_{Constructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 870))

    def test_871(self):
        input = '''Class _:___a__QR{}Class _S{}Class _r{}Class _{Destructor (){} }Class _nf{}Class _{Constructor (VZ_0:Int ;_:Array [Boolean ,0x1E]){Break ;Continue ;}Var $_,_:Boolean ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 871))

    def test_872(self):
        input = '''Class Fd08O_Ar:_{H0(_:Int ){}_H(_,q4:Array [Array [Array [Array [Array [Boolean ,64],9],0X4C],05],0b1];W,___Q5:Array [Array [Boolean ,024],0b101011]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 872))

    def test_873(self):
        input = '''Class _9_:___{Var _,enV,Q,_,b,$_m_,$T8I:_;_3e(_P0_,E,V,_n:Array [Array [Array [Int ,012],012],5_41]){} }Class _:l0_66_{Constructor (vv,_,__,E_:Array [Boolean ,0x6];bUK,_:C3b){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 873))

    def test_874(self):
        input = '''Class N8:TM{Val $B,_X:Boolean ;J0(_3k,sG__8_7_:Float ;_,E,y:Array [Float ,047];_:J_){} }Class _:_t__909{Var $OWFT0,$_5_,__:Array [Boolean ,0xB];}Class __0:_7{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 874))

    def test_875(self):
        input = '''Class d24B26:_{Var $92,w7,$u_3,$___,P3_8:__;}Class _8:_{}Class LW:_{}Class o1v{Constructor (_:Array [Array [Array [Int ,69],04],0x7_D];_7,_,_:Array [Array [Float ,0B1_0],01];_1:_){Break ;Continue ;Break ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 875))

    def test_876(self):
        input = '''Class _1{e(){} }Class _j:_{}Class _E7_{$_(_zk,_8:Array [Array [Array [String ,9],0B1001100],0b1];q:Int ){Continue ;}Var $I,X,$11:Array [String ,45];}Class _:T{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 876))

    def test_877(self):
        input = '''Class b{}Class a:_{}Class _4{Destructor (){} }Class I:f{Constructor (S,FLn86:_;_H__sec0:Array [Array [Array [Boolean ,04_6210],052],01];f:Array [String ,0x49];_,G,_,T__0,F,_5_:Array [Float ,2];_9__7V_,L9,R_98,Os,r,Dq3:_){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 877))

    def test_878(self):
        input = '''Class _{}Class c2X:_O{Var _:_2_Hc8_;}Class w{}Class C:W{}Class c74:_{Val $6_o_:Array [Array [Boolean ,0127],0127];Destructor (){} }Class _:U_99{Val S:Float ;Var $j_,____iy:_;Val $_6,D__k:__F;}Class V{}Class _6:_{Var ___22_,$_,$_,$5_W,_T:D;m(_4o:_989;_:Array [String ,0x3];J:Array [String ,0127]){}$4o_(L:Boolean ){Break ;} }Class T{C(_9D,X_,_,W,_9z__,_9O_:Array [Boolean ,73]){}Constructor (){Break ;{} }}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 878))

    def test_879(self):
        input = '''Class D916{Constructor (__2_e:Array [String ,23];_,_Z,vB,hd,J,_,u,j:W9){} }Class _{}Class _:b{Var $X,$g:Array [Float ,0b1];}Class __s:x0z8{Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 879))

    def test_880(self):
        input = '''Class TZB{Destructor (){}Var xt,u,$F_K,i,$_Ze,$_,$136,$3:K;Constructor (){y_::$O();Break ;}Val $7:String ;}Class _6{Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 880))

    def test_881(self):
        input = '''Class W:_{Var qoB5f9:M;Var $_U,_G_A,__j:Array [Array [Array [Array [Float ,0B1_11],0X4A],02],02];}Class ___n:__{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 881))

    def test_882(self):
        input = '''Class _{Val D:Array [Array [Float ,1],76];}Class _{}Class __:t68O{Var $__,$7U_N:Array [Array [Float ,0x4C],0x4C];}Class _{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 882))

    def test_883(self):
        input = '''Class __a44__:K_{Constructor (_:Array [Array [Boolean ,045],0b1001];_,k9_,j:Array [Array [Boolean ,0x9],0b1001];_,xK,_D7,K:Int ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 883))

    def test_884(self):
        input = '''Class O9{Constructor (){}_9(){}Var $_B4,$_,$_:Array [Array [Array [Array [Float ,0x31],0x2],034],70];}Class _7_{}Class B:_B{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 884))

    def test_885(self):
        input = '''Class __l{Destructor (){}$_(_:Boolean ;_0:Int ;__,_14:Array [Array [Int ,0x59],0B1]){Break ;Break ;{} }Constructor (){ {} }Var _6,u,$K,b,$_m_,O,___,D:_;}Class _E:_{}Class a_:_z{Var b:Boolean ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 885))

    def test_886(self):
        input = '''Class k7{Constructor (r:Array [Array [Int ,053],01_2];___b:uB;_:Float ){}Var $Cu,$9:Array [Array [Boolean ,0X45],30];}Class _9U_5{}Class i:n8E_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 886))

    def test_887(self):
        input = '''Class U{}Class _{Var __,_C:Boolean ;Constructor (){}$_(z:T_;s:Array [Int ,0b1_1_0_0]){}Var u,$y,$v,$91:Array [Array [Array [Array [Float ,062],53_19],0b110010],0X27];Val $5,$wp,$_:_;}Class _t{}Class _{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 887))

    def test_888(self):
        input = '''Class _{}Class RG:_9{}Class _Y_{h(){} }Class k4:M_{Constructor (___1,_Y,A:Array [Array [Array [Boolean ,0B10],0B101_1_1],73];_,H,VU:_64;_0,_:b){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 888))

    def test_889(self):
        input = '''Class __:R{Constructor (){_::$___();}Var $f_,f___,$_,__,_,$O__:Array [String ,0X11];Val _M:Int ;}Class _O:v{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 889))

    def test_890(self):
        input = '''Class N9{Var i72_:String ;Var $p,_:Array [Array [Array [Array [Array [Boolean ,0X58],03],0b1011001],0xE],0122];Constructor (_,_k2,_0:Array [Boolean ,59];_,s,J:Boolean ;v__62,n:_H){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 890))

    def test_891(self):
        input = '''Class m8__5{Destructor (){}_o(){Var p:Array [Array [Float ,3_0_5_6_41],0x4A];}$6(c4:Xn;_:Int ;_:_2){}Constructor (b4:_5X){}Constructor (__,_2_8_7,__X,_Qe,R_,__:Array [String ,0b1000010]){Break ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 891))

    def test_892(self):
        input = '''Class p2_:W_{Constructor (yhq5:Array [Int ,065]){} }Class k{__7(_,_:Array [Array [Array [Float ,065],0X22],0B1011000];i,_,U:Array [Array [Array [Array [Boolean ,06],0B1011000],0b1011],06];_3_h71,__3:Array [Array [Array [Boolean ,0xD],0B1011000],0B1_0]){Continue ;}Constructor (){Return ;}Val _,$_:Array [Int ,0x63];}Class __{}Class _7_jh:_9_{Val V:e;Var _0,_,P:Float ;Var $oa,_:Boolean ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 892))

    def test_893(self):
        input = '''Class cF{Val $_Ku_C:Array [Array [Array [Array [Array [Array [String ,4_6],0B1],0b1001001],05],8184_99_5],4];}Class ZZ{}Class W{}Class k_w_:__0{Val $_Ud,x9_3,$34:Float ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 893))

    def test_894(self):
        input = '''Class _2:___9{Constructor (___:Array [Array [String ,026],0b11_1];l,_:l;s,__:_9;___9q6:Array [String ,9];I:String ;F__24,l:Array [Array [Array [Float ,3_8_3_43],0B1],0B1_0]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 894))

    def test_895(self):
        input = '''Class P:_{Val _Rg,$4,$4:Array [String ,0102];Var $72,$s:Array [Array [Array [Array [Boolean ,0B110101],042],95],0B1];Constructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 895))

    def test_896(self):
        input = '''Class _{Var $N,$rz,G_,$_,$1o,_x,$q,$_4_,B_,$0,$8:Array [Array [Int ,0b1],0125];}Class _{}Class G{$O(){Val _,_BMb,_34E_,D0:_;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 896))

    def test_897(self):
        input = '''Class v{}Class q2{$k(){}Val $_:Int ;}Class _{}Class v{$P27m(__:Array [Array [Array [Int ,053],0x3_7_3B733],0xA];I:Array [Float ,02667];t,_R__:_UU){} }Class U_:__{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 897))

    def test_898(self):
        input = '''Class _d:S{Val $S6:I1;Var $7,Lw,$r7,$_,$___4_,z_,$Q:Array [Array [Boolean ,27],27];}Class _5{Var $r_4_A_,$Q:_a8G;Constructor (){}Constructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 898))

    def test_899(self):
        input = '''Class _S:r{h00(_,_:Array [Array [Boolean ,1],0B110];_,_N__A,U:Array [Array [Array [Float ,2],0X5D],0x2A];_,S,O:Array [String ,05];g:Array [Array [Array [Array [String ,0b1],4],05],0B111110]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 899))

    def test_900(self):
        input = '''Class _90{Var $6Zs4_,$_,_:Array [Array [Array [Array [Array [String ,06],0X3D54],35],0B11011],0B11011];Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 900))

    def test_901(self):
        input = '''Class Q:__a8{Val $_K:Array [Float ,0b1_1];Var $0,$9,U9___0:Array [Int ,05_2];}Class D{Val n,p:Array [Float ,516];}Class _A:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 901))

    def test_902(self):
        input = '''Class o:_{y5(_,M:Boolean ;_,_:Array [Array [Array [Array [Array [Array [String ,036],0X21],0b1],0b10101],4],0B1010011]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 902))

    def test_903(self):
        input = '''Class _d{Val _:String ;Val _,K_:Array [Float ,0XB7C];$f___(_:Array [Array [Array [Array [Array [Array [Array [Int ,0137],28],0137],0b1_01],0x33],0B101001],0x33]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 903))

    def test_904(self):
        input = '''Class __{Var $w_,$_o:String ;$_9OP(_A:Array [String ,0X47];_,a5q1:String ){} }Class _Ux_F{}Class K:_{Constructor (){Val _2_,A9c,B:Array [Array [String ,90],7];} }Class O:__{}Class _:v{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 904))

    def test_905(self):
        input = '''Class _2{$8(){}Val $_,$7:Array [Array [Float ,0X6],0103];Var g,$1,_,$q,P:Array [Array [Float ,0X55],01];}Class xx6{}Class _Pn{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 905))

    def test_906(self):
        input = '''Class __0:_B{Val $_:Boolean ;a_(_5_,_:Array [Array [Array [Array [Array [Boolean ,4_5_4],0xB_6_1],2],0b101],0b1_0]){} }Class _G:_N{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 906))

    def test_907(self):
        input = '''Class a{F(){}Var $p:Array [Float ,62];Constructor (Q,i,y:Boolean ;p:__;h_:Boolean ){}Destructor (){} }Class R:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 907))

    def test_908(self):
        input = '''Class _0:__3_25{Constructor (){}u(__,mS_,___,AB:Array [Array [Boolean ,0X2],010];E3,OM_,S,_,_,_:Array [Array [String ,06],50]){Break ;Continue ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 908))

    def test_909(self):
        input = '''Class E{$_(q8_,i,e:Array [Array [Array [Array [Array [String ,05],0b11110],0B1],47],0XE9]){}Destructor (){}F6T6(_,_7,W:Float ;M,Ys:Boolean ;_2N_j_:utcJ){Break ;}Destructor (){}Constructor (){Break ;}Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 909))

    def test_910(self):
        input = '''Class q:Y{Var _:_0c_2;Constructor (EL___:Int ){Break ;Break ;} }Class _{Val $__,_,_:Array [Float ,0X4B];}Class u:FIQ{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 910))

    def test_911(self):
        input = '''Class ___{Val __,$__5o,xt,n:Array [Array [Array [Array [Array [Array [Array [Array [Float ,0b10],05],0X1],04],0450],0101],67],0xA_C_1];}Class _{}Class k:G{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 911))

    def test_912(self):
        input = '''Class c0_:_{}Class c{Destructor (){Var Z,C,_:Array [Float ,0X5F];}Constructor (){}Val y_:U;Constructor (V_VO:d37;__8:Array [String ,0111];q,_:_e6){Continue ;} }Class aI:__{}Class _{Destructor (){} }Class _2{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 912))

    def test_913(self):
        input = '''Class V6x7_:_9{}Class t:IK{Val Q:Array [Array [String ,0B11],0X1];$0__(_,_,s,v,RPU9,P:Array [Array [Boolean ,2_6_3_05],0b1];_,E:Boolean ;H,N_tx_:Array [Array [Array [Array [Array [Array [Boolean ,0B11],14],2],0134],0134],0x25]){} }Class _S{Val _:Boolean ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 913))

    def test_914(self):
        input = '''Class _{_z(W:String ){ {Continue ;}Val G:Int ;} }Class Y__:_{_(_h,_1,_,N_:K;P_65Be:J;q_:Int ;a,B9,v5:Int ;_:Array [Array [Boolean ,06_5_2_1_36],0114]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 914))

    def test_915(self):
        input = '''Class w_j:_{$7__(X5,_8_:Array [Int ,0x1B1];I_X:Float ){}$_(_,n_,u,F:Array [Array [Boolean ,0b1],0b10110];__,__,__G7:Int ;y:_j0){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 915))

    def test_916(self):
        input = '''Class _{Var $_:Array [Array [Array [Array [Array [Array [Array [Float ,0xE_1_81_E_5_A_AD_8],0143],0b1],0b11],0b11],86],0XE];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 916))

    def test_917(self):
        input = '''Class U:o_76{Val l,$2ts_:Array [Int ,0x50];Constructor (sV:I84){} }Class _5_s{}Class _:A_tC{}Class _:_{Val j_111,L:_;Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 917))

    def test_918(self):
        input = '''Class _v:i{t(_e_,a1598um_,P:M){Break ;_::$_3()._7();}Constructor (_:r;_3,_:Array [String ,4];r1_,Y,e4,l:Array [Array [Float ,1],07_4]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 918))

    def test_919(self):
        input = '''Class f_:u3{$_(__:BB;_,w52_g_R:Array [String ,0X1];G,W__,_,d9_,___,__,_6_:Boolean ){Break ;}Var $_D__9,A:Array [Float ,03];Val $3,P:Array [Float ,06];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 919))

    def test_920(self):
        input = '''Class I8_{}Class __:R__{Var m,o_,_,$2P_56:String ;s(O:Array [String ,04]){} }Class _:B6{Val d:Boolean ;Val _z:Array [Int ,02];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 920))

    def test_921(self):
        input = '''Class a:_{}Class Tx:_{Destructor (){}Val $4_:Array [Array [Array [Boolean ,03],0117],0B1011101];_1_(_,_,_3AGv:Array [String ,0b1_1]){Continue ;}Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 921))

    def test_922(self):
        input = '''Class _:w3f{Constructor (){}Val $__,$_nFO,F_,$2,_,$A:Array [Int ,0x48];Constructor (_:String ){} }Class pj3{}Class T_{Constructor (){} }Class k_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 922))

    def test_923(self):
        input = '''Class W{}Class a5:_{}Class _{Constructor (){}Val $q5,_,$4,$_J,$_0_9:Array [String ,0b1000010];}Class D{$3(_:Boolean ;_:_;_7:Float ;_u9_m:Float ){}$6(t:P0__;_bO:Array [String ,0x13];_o,sB,S_:Array [Array [Array [Boolean ,0x9],0b1],0B100010];E:_){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 923))

    def test_924(self):
        input = '''Class B:xmR{}Class O{}Class Eu{Var F:Int ;$_2(J,_:Array [String ,0x18];d,_:_;__8:Boolean ){_::$6();Var _3,q:Boolean ;}Constructor (O_,n:_2){}Var $__,$W9,_1_,_:String ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 924))

    def test_925(self):
        input = '''Class U0Q_{Constructor (A,v,_9,dm:Array [Int ,0X9_B_3C];o:_;_i:Array [Int ,5];__Y_5R,C5mN3:T___){} }Class _{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 925))

    def test_926(self):
        input = '''Class m{}Class l_:_1{Var u746:M;Constructor (_:Float ;d_4:Boolean ;_,_MV:Boolean ;__,_,tT,raZ,_,___,_,YD,l:Float ){}Constructor (hTR4,o_UP6_,_,____:O){}Val $_,V132_yf1_,$6:Array [Boolean ,0x13];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 926))

    def test_927(self):
        input = '''Class _e:_3a{Val L6,$5_7W:Array [Array [String ,0B10100],0XD];Constructor (){}Var $15y:_70;}Class L:_3P2m10Y_{}Class _:u_7{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 927))

    def test_928(self):
        input = '''Class _c{$594(UQ7_:e){} }Class _:_z_{Constructor (){} }Class b{Constructor (){}Var $S1:Array [String ,77];k758_B(K,__G__,_:__){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 928))

    def test_929(self):
        input = '''Class _:_33_5_8___5{}Class b_J_{$_f9(_,XP_a,_7:O58;_P,Ooi:Array [Array [String ,0b1_10],060]){}Constructor (){Val _:Boolean ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 929))

    def test_930(self):
        input = '''Class T4{Constructor (e,_8i,_,aV4v:Int ;__85J:_;_144_8,_,I:Array [String ,1]){} }Class X{$Ia(){Continue ;}Var c:Boolean ;Constructor (){_::$u();Continue ;}Var _,$_S:_;$7(){}Var $1,_Q0:Boolean ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 930))

    def test_931(self):
        input = '''Class _3:_6t_{}Class dN7{$3TW(h87,q:String ;_8Jv_K,u,_,De18,_,o9,L8K:Array [Array [Float ,0x9],0B10_1]){} }Class __F9:P{Val _,$I,$7_,$_:_;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 931))

    def test_932(self):
        input = '''Class __h{Constructor (){} }Class _:U{Val P_,__Q_0:Array [Boolean ,0XB];p_(l8,x:Array [Array [Array [Array [Array [Int ,65],8],026],0XA_F],0XD3D]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 932))

    def test_933(self):
        input = '''Class O:w{Constructor (m,_:mr;H,__7__:Array [Array [Boolean ,0x17],0B1100011];_A5:F;QB,_:String ;_:Array [Array [Boolean ,98],0b1010110];_:Array [Array [Int ,0110],0x2F_D5]){} }Class __:_{Constructor (_4Hv,_:String ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 933))

    def test_934(self):
        input = '''Class s{}Class _{Constructor (){}Destructor (){} }Class _D2_{Var Z,$9__:Array [Array [Int ,07],0x5B];}Class _ls{Var j6:Array [Array [Float ,13],0B1001];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 934))

    def test_935(self):
        input = '''Class _:_5{N(_,_,_:Array [Int ,70];__,sN1op:ji7){Return ;}Var $_:Boolean ;}Class M52{}Class C{Val $_:Array [Int ,013];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 935))

    def test_936(self):
        input = '''Class x:_3{n(){}Constructor (_20_,C,__x,_9__1:kq;_,_W_,Mk,_:Array [Float ,0b101100];_:Float ;_,__3:L;__,g:z){Break ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 936))

    def test_937(self):
        input = '''Class _{}Class _O:_{Constructor (_,_,_,x:B){Var oE_,hX,_u:_36X9;Continue ;_8090_L::$_();} }Class _M{}Class i:Ft0{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 937))

    def test_938(self):
        input = '''Class B{Constructor (___g14:Array [Array [Array [String ,025],025],025];_,Z4_:Int ;w953,b9,F:Array [Int ,8_5_8]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 938))

    def test_939(self):
        input = '''Class p_47_{Destructor (){}Constructor (){}Constructor (){}Destructor (){}_(_,_6K,_,_5:Boolean ){}Constructor (c:Float ;_,y:Array [Array [Float ,8_95],33];zsWc:Int ;_y,_H,_:Int ){} }Class _S_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 939))

    def test_940(self):
        input = '''Class _6:w1k6_{Destructor (){_56::$_k_51();}Constructor (__n51_5:Array [Array [Array [Array [Array [Int ,6],0x7D],0X40],59],0x18]){}Val $0:Int ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 940))

    def test_941(self):
        input = '''Class dj2{}Class _:o2{Var $_,_014,$__4,$_,$7,_,_8:Array [String ,61];}Class G_:_{Var $0_9:G;Var k:Array [Array [Array [String ,0b11_0_00_01],0b1],0B1_0];B4(){} }Class _{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 941))

    def test_942(self):
        input = '''Class L05___4:YK6Ug__{Val $_,_,$x,G_:s;$_(){}Val F:Float ;}Class _O:__{Constructor (){}Destructor (){Break ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 942))

    def test_943(self):
        input = '''Class _:_{Constructor (O:___nz){}Var $5__,$_:Array [Array [Boolean ,8],05];}Class k:_B{Val $_15:Array [Array [Float ,0B1001110],064];}Class _9_0:___{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 943))

    def test_944(self):
        input = '''Class w_:_qW{Var $F,$RzuiQ:Array [Array [Int ,0106],0X4E];Constructor (_,X_,e:_2;_,k_,z,G6:Boolean ){} }Class __k6:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 944))

    def test_945(self):
        input = '''Class h8{$6_R(m34:Array [Array [Array [String ,01_6],067],0B1];_V,_W:Array [Array [Array [Array [Boolean ,0xA],0b10101],0X2C],0XA]){__::$H();Continue ;}Var $0,__,__:_;}Class _:_8{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 945))

    def test_946(self):
        input = '''Class _7:_{Constructor (){}Constructor (){}Constructor (){}Var $_i:_;}Class _i:_{Destructor (){}Var $0m9,$__2,$Fq1,$__,$k,_:Int ;}Class S{}Class T{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 946))

    def test_947(self):
        input = '''Class _7:_6{}Class s2{$_(_c_:Float ;_2,_:_1;_5,v9:_;H:_;_,_:ls;G3_:p8;_5_:Array [Array [String ,0B1],036];e,_,__:_){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 947))

    def test_948(self):
        input = '''Class ___{}Class A36__:_{}Class Y_:_S{Val qZB6,$4:Int ;Var _,w,tj,$_:Int ;}Class v9H:_{$3__(_,_:Array [Array [Array [Array [Array [String ,0b1],0B111001],74],015],0b1011011];Z,_0,__:Float ){Return ;}h(Y,Q:f;y:Int ;FL:String ){Break ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 948))

    def test_949(self):
        input = '''Class wr_{Var T_:Array [Boolean ,0B1];Val $n,$e,_z,_,_:Array [Array [Array [Array [Int ,7_78],0b1100010],0116],0xA_7];}Class z_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 949))

    def test_950(self):
        input = '''Class _:u{Var $_,$_,V,_:c;Destructor (){}Val h,_:__;}Class a5:i{Var $C:Array [Array [String ,025],0x3A];Constructor (_T:Array [Int ,0XE]){ {{} }} }Class _O:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 950))

    def test_951(self):
        input = '''Class _{Val L:Array [Int ,0B1000001];}Class E_8:e_{Val __:Array [Array [Array [Array [Float ,066],0x1_9_E],0x24],0B10_11];_(){Return ;Break ;Var f,_:Int ;Break ;Break ;}Var FS,___:A;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 951))

    def test_952(self):
        input = '''Class _{}Class e:_{}Class _G:R_{}Class Z0_4_{}Class s_{}Class n{Val P,C__,$f_:Array [Int ,0x14];Var $__,_1,_:D;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 952))

    def test_953(self):
        input = '''Class o{_J(){} }Class R_:K_{}Class i4:_{Val _,_6:Array [Array [Array [String ,84_1_7],66],66];Var B,$_,b:Array [Array [Int ,8_4],66];Val $_x__1:Array [Int ,0B101111];Val _,$_,$Y_,_8_,q,_:U;Constructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 953))

    def test_954(self):
        input = '''Class _:n{}Class Q{$_(_:Array [Array [String ,0B1],0x3C];_:Array [Array [Array [Array [Array [Array [Int ,0x3C],6],0B1000110],0b10111],0504],0445_33]){} }Class _i0{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 954))

    def test_955(self):
        input = '''Class __19__i1{Val $5sy:Array [Int ,1_50];Constructor (_:Boolean ){Var _,_,__,W:Float ;}Val _,$A_,$_:_S;}Class D:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 955))

    def test_956(self):
        input = '''Class _:r4k1m_E{}Class f:O__{Val $_4,$W9h,A_l_:Array [String ,0x5D2];Constructor (){}Constructor (_JP,B:Array [String ,0106];_,_,Z:Int ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 956))

    def test_957(self):
        input = '''Class Y5{Val Ih:String ;}Class _0:T0I_{}Class _{Constructor (_R_,N,GY:Array [Int ,0676];_,D,_:String ;_:Array [Int ,0B1100]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 957))

    def test_958(self):
        input = '''Class x:U7_{Var $2_,_:Array [String ,0X5];}Class n54T{}Class p{Val _,$_:Array [Array [Array [Array [String ,014_05_43],045],0B100010],0X5F];Constructor (){}Val $b_,$7_4,u,$9:A6;$n(_:Float ){} }Class _:P{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 958))

    def test_959(self):
        input = '''Class _:_E{}Class _{}Class _:G{}Class _:lL0{}Class jMe_M{}Class _{$3(_:Int ;W_:Boolean ;w:_){Break ;} }Class _WRZ:y{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 959))

    def test_960(self):
        input = '''Class __W_N0_Aw{W8(){}Constructor (__,h__Z,nV,_,P:Array [String ,0B111101];_:_x;_,Hm744:Array [Int ,0b1111];_0:Array [Array [Array [String ,89_3_6],7_3],56];_,_CJ:i;cV:_){Break ;}Constructor (){}X(_:Int ;Y,__,_l,dSQ:g;_2,Y:Float ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 960))

    def test_961(self):
        input = '''Class h:e{Var _9,$2SP,$d0V:_9_;}Class t:e{Destructor (){}Destructor (){} }Class _:P{}Class p7_4:_{}Class __:U{}Class _1{Destructor (){}_G(){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 961))

    def test_962(self):
        input = '''Class M{Val $836f_,_pS:Float ;J(S:oc;__,_5B:Array [Int ,0X54];_w:m8960;_5o:x){} }Class _:__{}Class Z_{_(){}Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 962))

    def test_963(self):
        input = '''Class __{}Class _:_6_{U40(s:Array [String ,0X64];_:T;__,e:Array [Array [Boolean ,0b111100],0b1];__:Array [Int ,076]){Continue ;Break ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 963))

    def test_964(self):
        input = '''Class __:X{}Class N{Val _:Boolean ;}Class _{}Class ___:yi6{Destructor (){} }Class m2Ro_Q{Var $cb,$_:z;Val _,$4:String ;}Class v_r{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 964))

    def test_965(self):
        input = '''Class _:i{Val L:A;}Class v{_(e,t6f:_6o;_,_P:Array [Array [Boolean ,87],0X20];O:Array [Boolean ,024]){} }Class __s0:hz{Var _,w_32,$_,KFH,z2H_,$_:Boolean ;Val _9_9:Array [Array [Array [Float ,7],07_4],024];}Class _{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 965))

    def test_966(self):
        input = '''Class i{}Class l_BWM{}Class _{Destructor (){} }Class s:Z{}Class E2Wa{Val $g_E:_vL3;}Class _y:a5f{}Class g:_{}Class Yh{}Class d9nu{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 966))

    def test_967(self):
        input = '''Class ___:_s{_(t,_E3,A1R_36:___;f,fI,__:Array [Array [Array [String ,0B1_0],93],0b11011];G:F_;H:Array [Int ,0X52B];U,_899:String ;w,s,_:l){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 967))

    def test_968(self):
        input = '''Class _:c5{Q0(Rt64:Array [Array [Array [Boolean ,0b1010],0B1_1],0B101_0_0_0];__,_9,__:X94;_D:Array [Array [Float ,0B1000011],0B1000011];_:Array [Array [Array [String ,0X41D_6],0B1000011],016]){}$_a_(w:Boolean ){}Constructor (){ {} }}Class _:d{Val $_6E:W;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 968))

    def test_969(self):
        input = '''Class y9:G{$8a(_:Array [Array [Array [Array [Array [Array [Boolean ,0b1_0],067],0b100_11],0x1_5],0x10],0XF]){ {New CW()._5_t977._49();} }Var $x_4_4__:String ;_B(S:Array [Float ,0x10];_s:Float ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 969))

    def test_970(self):
        input = '''Class _{wz1(n_,_:Array [Array [Array [Int ,0b10100],0X4],0X57]){ {} }_(b__,n,u70,E:_q14;_:Int ;f8,_1:_9;k0,_hp9:Boolean ){}Val _YZ,__,_:Array [Array [Boolean ,5_8],0XA_3_A];}Class _{}Class h{Val _0y:Int ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 970))

    def test_971(self):
        input = '''Class _:_{Var __:Float ;Var _4:Array [Array [Boolean ,0x9],0X57];Val $_,_,kN:Array [Array [String ,0103],0x3_5B_B_8_D];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 971))

    def test_972(self):
        input = '''Class _:fX{Var _,__,$6X3_,$9,o,$_,sKP:Int ;}Class _{Val Z:Int ;}Class _:RO{}Class U_{Destructor (){}Var s:Float ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 972))

    def test_973(self):
        input = '''Class __8226:_I1_8{Constructor (){}Constructor (_83,_5_7__:P;H,L:Array [String ,6]){}Val $_:Array [String ,035];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 973))

    def test_974(self):
        input = '''Class _{Var $_E:w;Destructor (){}Val $_D1:String ;Constructor (){} }Class L_R{Constructor (_X:Int ;_8u6U9:Array [Array [Array [Boolean ,0x49],0X25],04]){}Constructor (G_:Int ;iv_,_K,__1:a3;_,__,ZT:Boolean ){Break ;Break ;{Y_::$_();}Break ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 974))

    def test_975(self):
        input = '''Class m:__{}Class __:v{Destructor (){}$___(){} }Class f2{}Class _{}Class _:g{Var R,_0,h_:Array [Float ,07_47];i_(_6,_9,_Y,W:String ){} }Class j{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 975))

    def test_976(self):
        input = '''Class __:D7{Val a,_:String ;Var G6_,$_,_,$L:Array [Array [Array [Array [String ,28],67],0X2303],0x59];Destructor (){}Val S__,_:Array [String ,67];}Class X7{Constructor (__,_a,_f,M_:Int ;wu,_rZ,__9c,g,_:Array [String ,0X20];_,_,_m_,_,m25_:Array [String ,0B11]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 976))

    def test_977(self):
        input = '''Class F:_r{_(E0:Float ){}Val __u_5:_;}Class _{__9_7(__,_,_,Mh7_:String ;_:E){}Val $2_8_:Int ;}Class _t:g{_(A,A:Int ;ro:_){}Destructor (){} }Class _8_:J0f{Var _r_,__:_;}Class W:_{}Class _l{$5(P,pl:Int ){ {Var U:t;Continue ;} }}Class __:o{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 977))

    def test_978(self):
        input = '''Class t_{Destructor (){}Var _6_:Array [Boolean ,0x4E_1];Val $1r:Array [String ,0X2D];Var $m3,$g9:G9;Var $_F:__;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 978))

    def test_979(self):
        input = '''Class _:q7{}Class _:w{}Class _:_{}Class _:___6{Var $2,M,U,$44_,$__i_P,r_:Array [Array [String ,0b10],0X28_F_D83_FC];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 979))

    def test_980(self):
        input = '''Class C_h:_{Constructor (_:Boolean ;_5:Array [Array [Array [Array [Boolean ,0B1_0],0xD74A],55_3],5]){}Var Myh27:Array [Int ,0B1_1_0];}Class _:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 980))

    def test_981(self):
        input = '''Class _:B2{Var ___:Array [Array [Float ,02_7],58];Val $2p2,$Rs:Float ;}Class _{}Class OL{Val $_,_9P,$Z,Q6jg,bm:W_;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 981))

    def test_982(self):
        input = '''Class X9{$0(){} }Class _43_:m{}Class _5O:xV2{$_(_Q0,___,hl,gR,B_:Array [Array [Float ,0B1_1],047]){ {} }}Class _{}Class u{}Class _1_:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 982))

    def test_983(self):
        input = '''Class f_0b{Val J,T_3,_2:String ;}Class _:_{Var _,WkMU:Boolean ;_(_6_J:Array [Array [Array [Int ,0B11],98],02]){Break ;Continue ;Continue ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 983))

    def test_984(self):
        input = '''Class _1__:__6{}Class t_:m{}Class t_6__:_S{}Class x5__:_t6{}Class e:k{Constructor (){} }Class z:_9{}Class n27__{}Class y{Constructor (c,wG,O79,Q9:String ){Break ;{} }}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 984))

    def test_985(self):
        input = '''Class I6_:__{Val _,$_:X;}Class c:G{Constructor (_5:Array [Int ,0B10];S_3,_9_,i:Array [Array [Array [Int ,2],0B1000],1]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 985))

    def test_986(self):
        input = '''Class _1{Constructor (s6:String ;_:Array [Float ,0XB];V_n0:Array [Int ,0x19]){Var g_,_9p,_,SI:Array [Array [String ,0b10],0137];Break ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 986))

    def test_987(self):
        input = '''Class p:iss{}Class _30{K_Q__(c__r,_5M:String ;_,s6_JU__ra,_4__,_,_,_7F,_Up03:Array [Array [Array [Boolean ,0X1E5],01],06];_3_u:sW;l,_:t1){}Constructor (){Break ;}$__(){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 987))

    def test_988(self):
        input = '''Class B{Var W:_6F;Constructor (){Continue ;} }Class D{Val $s,_W__,U,$S_Y:Array [Int ,4_72698];Destructor (){Return ;Break ;}Destructor (){Var z,_:Array [Array [Array [Float ,0B1001101],6_8001_9],0x3_E_9_E8];} }Class __{Destructor (){} }Class I{}Class _I{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 988))

    def test_989(self):
        input = '''Class p5{}Class _:_wp13{Destructor (){}Destructor (){}Var X27R,$J07B0_G_e28_,D__6,G,_,_,$5d:Array [Array [Int ,0624_2],69];}Class f_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 989))

    def test_990(self):
        input = '''Class N{Var _6:String ;}Class L___0_{}Class H:Z{Constructor (f_3_:_w){Break ;} }Class S3{Destructor (){} }Class _S{Var $sb:Int ;Y_(){Var oO__4:Array [Float ,0X3B];Return ;{} }}Class U:E{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 990))

    def test_991(self):
        input = '''Class XN_{Var b_,$_7:Array [Int ,0XB];Destructor (){}Destructor (){}Constructor (o:Array [String ,0b110]){}Var $g1,$_B:Float ;Val $_Y,$0w,$__r_,r,H,pL67,$a5:Array [Int ,0B1_0];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 991))

    def test_992(self):
        input = '''Class A:l{Var $N,$R_,_5H,_d,_,$O,AY,Z,B_,$1l9,Od,O,_:T9_u;Var $K,L,J,$_,$64h:a;$D(R6:Array [Int ,0b111001];_,b:R;_:Array [Boolean ,5];_:Array [Array [Float ,8],0b111001]){}$_(){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 992))

    def test_993(self):
        input = '''Class __{Constructor (g_:Array [Array [Array [Array [Float ,0x2],8_4],0XC3],01]){Break ;Continue ;} }Class EzR:___{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 993))

    def test_994(self):
        input = '''Class _x_:H6{}Class Z_{Val $_,$0,$_,$8,___,_,e,$0:String ;}Class __:_{Val $32Z:Array [Array [Array [Array [Int ,0B1_1],0B10010],0b1100011],0b1_1_1_0];Constructor (){}Constructor (v_,L:Array [Array [Array [Boolean ,6],0B1],24];P:Array [Float ,0B10010];_:Array [Array [Boolean ,0115],0b1];__392v,_:O){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 994))

    def test_995(self):
        input = '''Class _{Constructor (l:Array [Array [Int ,6],0142];W__,C,q_:Int ;_O_,b,_,_,_,__:g;_h,y:Boolean ){Var _M:Array [Boolean ,0X4];}Destructor (){} }Class _D:_{}Class H:L1{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 995))

    def test_996(self):
        input = '''Class _:_{_(h__,N:M){} }Class _:_I_7{$2_(Z0:_){}Var $__,__0_,p_:Boolean ;Var $_0M_10P,k,coL,$9,$U3:Array [Array [String ,0B1],0b1000101];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 996))

    def test_997(self):
        input = '''Class _{}Class _{Val jA:Array [String ,0B1111];_6(a:Array [Array [Array [Boolean ,077],077],07_62_1_0];gyW8,K:Int ){Return ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 997))

    def test_998(self):
        input = '''Class y__:W{Val $y,$9_,$_,$v,$I,$4,_6,$0:Array [Array [Array [Float ,06],646],91];}Class B:i9{A(_:_;f:Array [Array [Array [Array [Array [Array [String ,0xB],06],0b1],0xF],021],91]){Continue ;} }Class J_B{Var _:Array [Array [Int ,0B101010],04_2];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 998))

    def test_999(self):
        input = '''Class fJN:h4_{}Class pa_:_{}Class _9:_{Destructor (){}Constructor (){} }Class W:_S{Constructor (gK_,__7:N){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 999))

    def test_1000(self):
        input = '''Class __:e{Constructor (_:Array [Array [Array [Array [Int ,027],86],027],06];_:_;k9,y:Boolean ){}Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1000))

    def test_1001(self):
        input = '''Class cr3:_{Constructor (Z:__;_,Gl_TR,___:Array [Array [Array [Array [Boolean ,0B101110],0B11],0B101110],9_3];_o:__f){Continue ;{} }Val $_6Z:Array [Boolean ,0140];}Class _:_{}Class _:c_F09_{$C9(R:Array [Array [Array [Array [Float ,0b1_111_0],0X4],02_44_37],79_2]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1001))

    def test_1002(self):
        input = '''Class _8_{}Class _{Val Lx,_U,_:Array [Array [Array [String ,0B111011],0b110000],0b1_0_0];vt_7dk8(_2d:V_;J_6_:w){} }Class _:_3K_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1002))

    def test_1003(self):
        input = '''Class _3Q{}Class _D_u:Sj{}Class N:U1{}Class A_2_{Var _:_y;}Class Qw{Destructor (){}Constructor (){Val _:Boolean ;Continue ;}Constructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1003))

    def test_1004(self):
        input = '''Class _{Constructor (){Break ;} }Class E{Val m:Boolean ;}Class _h:_{Destructor (){}Constructor (__:Array [Int ,072]){}Var _,_6:Array [Int ,6_57_9];Constructor (){ {Break ;} }}Class J{Var g_,D,$Hc,__5,_:m;Constructor (_587,o:Int ;_:_;_:Array [Array [Array [Array [Int ,0x60],97],97],05];i55,_i1,b,G:Array [Boolean ,4]){} }Class Wd:r{}Class __1:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1004))

    def test_1005(self):
        input = '''Class _:_0_{Constructor (A7aJ:Array [Float ,37];__:Array [Boolean ,37];f:Array [Float ,02]){Break ;}Destructor (){}Var N,_:__3;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1005))

    def test_1006(self):
        input = '''Class __j{Destructor (){}Var $eE,TJb:Int ;}Class __{Var $H,$1K:vo;}Class Hr:a4{Var u500m,_,$J,$3,GB,V_:Boolean ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1006))

    def test_1007(self):
        input = '''Class _:_{Constructor (__:M__1_){Break ;}k7(r:L_N___Y;m,__,u5u:Array [Array [String ,027],41];c,t_,_,_1__:_l_Zx){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1007))

    def test_1008(self):
        input = '''Class _{}Class Z:C{}Class _0s:D_S{Destructor (){Var DE_,_,_9:Array [Array [Array [Array [Float ,0X6E],0X24],7],54_2_87_3_4];}Val $t:Array [Array [String ,0X24],0B1100];Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1008))

    def test_1009(self):
        input = '''Class _768_{}Class X{}Class CI44V68:a_Y{Destructor (){}Destructor (){} }Class K:_{Constructor (_:Int ){Var B_,k_:Int ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1009))

    def test_1010(self):
        input = '''Class _H{Constructor (u:Array [Array [Int ,0b111100],38_7_2_1262];_:Array [Array [Array [Boolean ,0X1E],0113],06_4];B9_T6,_25,_:z){} }Class _{}Class _{Constructor (_:String ){}_(){} }Class _2__7:f{Destructor (){Continue ;Break ;} }Class h{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1010))

    def test_1011(self):
        input = '''Class R:_O{}Class r{}Class _3V{}Class _G:____{$_z(p:Float ;z,__:Array [Array [Array [Array [Boolean ,0xC_3],0b1],4_7514],7]){} }Class __{}Class n{$_3_1h(){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1011))

    def test_1012(self):
        input = '''Class _C_{}Class _{}Class _x0:T{$47F(T:Array [Array [Array [Array [Array [String ,0X56],0b101011],0b101011],06],0B100010];N:r__){}Var _,_38533:WR_D__;Var $7_bd,X:d;Val j,$_:_N;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1012))

    def test_1013(self):
        input = '''Class _{}Class S__:_{Constructor (_,_,_8_,_,_,_,A__,N9_:__){}Var $79:Array [Array [Array [Array [Array [Float ,0X3_5],0X9],0x7_0_E1],026],89];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1013))

    def test_1014(self):
        input = '''Class __:uE4{}Class J_:_4{Constructor (_S_40,R,_,R_4:Float ;_,Iq_:Boolean ){}$_(J:Array [Array [Int ,94],7]){}Var K6:I;}Class I0W_:n9N_9sMG4_m{}Class _{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1014))

    def test_1015(self):
        input = '''Class r718{$_(e1Uvp1_,k:Int ;n06:Int ;Mx:____2__){}Val $v,$_,$7,$d1,$p,S,Y_,$Q:Gu;}Class T:m{}Class _i_S{}Class W9:_{Val $g,$_,$3:_;Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1015))

    def test_1016(self):
        input = '''Class J:Qk7{T08(_sTy5__,oQ,_:Float ;B,M:Array [Int ,0X5B];_:Array [Array [Float ,011],0X5B];_:_W2;z:P;Mv_1_Yd_:Boolean ;_,_,Q:String ){} }Class j:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1016))

    def test_1017(self):
        input = '''Class M:Qa{$_(S7:Array [Array [Float ,15],073_4_3]){}Destructor (){Continue ;Continue ;} }Class d:g{Constructor (n:Boolean ;H_,P__:__){}_(){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1017))

    def test_1018(self):
        input = '''Class _{Constructor (_:Array [Array [Array [Array [Array [Array [Int ,0b1],9],0X93],8],0x19],0xA]){}Constructor (D,__,V:_r){}$8S_(){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1018))

    def test_1019(self):
        input = '''Class _{Constructor (_:Float ;K__,_,__,_,_8,_9,_,_:_){}Val $0R5__,$g4:Array [String ,0X3F];Val $9,$8,u:Float ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1019))

    def test_1020(self):
        input = '''Class J:_{}Class n{Var _,__:Array [Array [Array [Int ,2],5],5];Var $8_,$wi:Boolean ;Destructor (){} }Class _{Constructor (){} }Class _:__5{Var _v,$_93NgQ,$8:_;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1020))

    def test_1021(self):
        input = '''Class Hj{Constructor (_q_,__4_7_0_5_,__,_:String ;__,I44x:Float ){}Var $F2:Array [Array [Boolean ,0x49],0XD5];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1021))

    def test_1022(self):
        input = '''Class _0X:_6{u2N(){} }Class _3:b{Val X4:X0_;}Class __7:J{Var $_,$_Yx,W,$__,$8S,d:Boolean ;$H8(_:Int ;_:Array [Boolean ,0X9];__,y__,E,x,z,_8,K:String ;i:Float ;_:ei__e;_,_1:Array [Float ,0b111_0_0]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1022))

    def test_1023(self):
        input = '''Class KU:_{}Class L_{Var y,$y,$72_S__5:Array [Array [Float ,0X5E],0b1_1];}Class z{Var H,L,_i,$x_:_6;Constructor (P,_:_;_55wZ:_;_,_992,Z:Array [Array [Array [Array [String ,0B1000100],070],13],7]){}Var $__s_,y,_,_:Array [Array [Int ,0b1_1],0b10110];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1023))

    def test_1024(self):
        input = '''Class _{Var i:Array [Array [Array [Array [Array [Boolean ,0x34],04_5_3_66],0X37],0B1001110],73];Val $K4:Array [Array [Array [Array [Array [Array [Array [String ,061],0b111],061],6],73],41_66],0b11_1_10_0];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1024))

    def test_1025(self):
        input = '''Class B0r_0_{Constructor (_:Array [Array [Array [String ,0B1100001],8],74];_:Array [Int ,0B11];o6,F:Array [Array [Boolean ,0x15],0B1]){ {} }}Class __2_G{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1025))

    def test_1026(self):
        input = '''Class _:__{}Class _{Constructor (J,E,_7:Array [Array [Array [Array [Array [Boolean ,0X5C],01_3_14],1_5],19],0B10_0_0]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1026))

    def test_1027(self):
        input = '''Class g{Var $A:String ;__(_:_;_:k2;A,V_,_,r_p_:String ;d,hS0:Float ;_U_6:Array [Array [Boolean ,0X2],0B1010]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1027))

    def test_1028(self):
        input = '''Class __4:_w9{$0j__7(xb:Float ;___M_,e1,V7,B12:Boolean ;__,HGC_v,_27F55:Array [String ,0B1_0];_,X_:Array [Array [String ,8],071];_1:Int ){Continue ;__6::$G();} }Class _{Var $4_:Array [Array [Array [Float ,0B1011001],071],0x5B];$7JA(){si::$F1();Break ;} }Class _:_{}Class _e_{Var $_:Array [Float ,0B1011001];Constructor (){Break ;}Var $65,w_:Int ;Val G,_B_84:String ;}Class _x{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1028))

    def test_1029(self):
        input = '''Class _0:j9{Destructor (){}Destructor (){}L1Y(){}Var __:Int ;Val $4_:WG;}Class _6d{Val $9_j__8,_J_,__,$_,_2_4,$12_Do:__9;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1029))

    def test_1030(self):
        input = '''Class D:__Ar_3_56_0_F_k7{Var $8_:Array [Float ,032];Constructor (YN:Array [String ,92];x,_:Array [Array [Int ,0X2],032]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1030))

    def test_1031(self):
        input = '''Class _{$95(_:Array [Boolean ,0XE_9C];__L:Array [Array [Float ,0115],9];_,__e,_,_6_,_:Array [String ,0X43];v:h;_8f0:Array [Array [Array [Array [String ,0b100100],0x5E],0XC],02_2];f4C,_:Float ){s::$M_7();} }Class _l_:t{Destructor (){}Val $9:Array [Float ,0xC0];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1031))

    def test_1032(self):
        input = '''Class _{Destructor (){}Var _:_08;Val $_,$248Um43,$_,$4:Array [Array [Array [String ,0X3_6_6],05],0b110];Var _:Array [Array [String ,0b1],07];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1032))

    def test_1033(self):
        input = '''Class P:_{$5(o_:Ly){}Var $3E__:Array [Array [Array [Float ,0x2],0B1_101],0x10];Val $_3,$FF0:Float ;}Class rWa{}Class pnK{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1033))

    def test_1034(self):
        input = '''Class _{Var $7Tx:Array [Array [Array [Array [Array [Array [Boolean ,0b100111],0b100111],0b100111],0B10100],0b1],0122];}Class lBo:d___f{Constructor (){}Var _,d0,$j__:Array [Array [Array [Array [Array [Array [String ,05],0122],3],0b1],56],07];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1034))

    def test_1035(self):
        input = '''Class K:k_{Var NM:String ;vSh3_Ia(PX1:Array [Int ,70];___,F7,j5P_:Array [Array [String ,01],70];_p:b;__V,C_:String ){Return ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1035))

    def test_1036(self):
        input = '''Class _7{}Class hs3:_F{}Class D:_{$_5(){} }Class _W3h:_L{}Class _{Val $R:_;Var $H5,XO,_:_3_;}Class _{Constructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1036))

    def test_1037(self):
        input = '''Class w_05{Var $_,$30,$BA:Array [Array [Int ,0b1_1],9];}Class _:_{Var __,h,O,$_0:Float ;Constructor (_,__4,_:Int ;V:Array [Array [Array [Float ,0x6_2F],0B1000],0B11_1];_y:Float ;_,z9_:Boolean ){} }Class N{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1037))

    def test_1038(self):
        input = '''Class _:_{Val __190,$_,$_4,N24_k:Array [Array [Array [Float ,57],3],0b1];Val u8f_j__5,$n,$j,$_:Array [Array [Array [Float ,57],0142],57];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1038))

    def test_1039(self):
        input = '''Class _{}Class g:W_O_6_J{Var $_f,__9e,$9,$Y:Array [Array [Int ,0b1000110],0b1];}Class s{Val $c_2,_,$L3m,$5_,$F:Array [Array [String ,0b1],037];}Class _{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1039))

    def test_1040(self):
        input = '''Class _j_9:_2_{Constructor (__,V84ae:Array [Array [Boolean ,015],0b110110];o:_){}Val _:_3;Constructor (p_,R__:Array [String ,0b110110]){Var _6lU:String ;}Var _,$c:Array [Array [String ,0x2D],07];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1040))

    def test_1041(self):
        input = '''Class _Q:C{Val $p4:Vo_;}Class Ch_0_{Constructor (_u,V:Array [Array [Array [Int ,0XA],99],0X60];_:_r){}Val _z:_W_4m_;Var G7__,$2:Int ;Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1041))

    def test_1042(self):
        input = '''Class X20{Constructor (){}Destructor (){} }Class __{Var _q,skS,m8,L,_7,$f38,$MJ5w:Array [Boolean ,033];Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1042))

    def test_1043(self):
        input = '''Class J7{}Class i{}Class _{Destructor (){} }Class _4Jo7F:aA_{}Class _:E{$K(w1_,g:_;V,_:Int ;_,j,T9:_;j_,_,o,K__4,R,_,_,__8:Array [Int ,0XD8]){} }Class S7:El_{}Class W:iu{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1043))

    def test_1044(self):
        input = '''Class _:K{}Class _6:_9{Var _0,$_1_,$u_:Boolean ;Constructor (q:String ;_0,_,Z,Z,_dO:Array [Boolean ,0B1011110]){} }Class N4{Val $_:_QS;U2(){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1044))

    def test_1045(self):
        input = '''Class ___{}Class _{}Class n_{}Class K{Constructor (_8_7_:Float ;_0:Dh1){} }Class __:nS{Constructor (_,_,D3,tM,i:j;op:U){Continue ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1045))

    def test_1046(self):
        input = '''Class __41:X{Val j:String ;}Class _:WV{Destructor (){}A(Y,R4t_:_;_3:Array [Float ,05];_,__,_C:Boolean ;M82:Array [Int ,0B1111]){} }Class a7{}Class __:_{V7(c_:l){}Destructor (){Continue ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1046))

    def test_1047(self):
        input = '''Class S:G{}Class __Z_:_{Val _,_X,$bTC2,WH,$z0,$1_:S;Var $_A,b:Array [Array [Array [Array [Boolean ,0b1],5_3_4],0101],0X36];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1047))

    def test_1048(self):
        input = '''Class _9:d{}Class _R{Constructor (){Val r_:Array [Boolean ,051];}i7(){}$_(___A,__,_6:Array [Int ,0b1001000];D,_74,j8,_:q_y){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1048))

    def test_1049(self):
        input = '''Class fM8{Constructor (){}$E(zI2_:Int ;_1__983,_Q_G:String ;_,S:Array [Float ,06_5];_S1s,b0_1_:__){}Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1049))

    def test_1050(self):
        input = '''Class __{Destructor (){}Destructor (){} }Class D:h_{Constructor (_:Ru){} }Class _{Val $k,r___,a,X_,$7,$b,DC3,_:Float ;Var $_8:Float ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1050))

    def test_1051(self):
        input = '''Class k{Constructor (){}Constructor (){}$64(K0:_;I,_:Array [Array [String ,04],62];X,Gr:_;vY,q:q__12;M,_,l:_;_,YC_,_,_:Boolean ;_0:Array [Int ,0XC];N__44:Int ){} }Class sU:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1051))

    def test_1052(self):
        input = '''Class _0_:Q{Var _:_;}Class X{Var $z,bxy:Array [Boolean ,0x6];}Class _{$W(S23y6P:m_;_:Array [Array [Array [Array [Array [Array [Float ,046],0b1001111],0B1],2],0X4D],539]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1052))

    def test_1053(self):
        input = '''Class T{}Class _:i{Constructor (){Break ;}A(k,_r:Array [Array [String ,0xF],0x4_C_8A_1];_:Float ){} }Class q{}Class e_H:j{Val _:Float ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1053))

    def test_1054(self):
        input = '''Class _t0{__G0_(Z_:Array [Array [Array [Array [Int ,0X5_B0_9],0X29],1],032];j:Boolean ){Continue ;_i::$_._4._(!!_.D()._0_._);} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1054))

    def test_1055(self):
        input = '''Class g:Zc{}Class d:T{s(_5_04__3,_u6__X,_:Array [Array [Float ,07_7],04];j:String ;O_:Array [Int ,01]){} }Class Q{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1055))

    def test_1056(self):
        input = '''Class _:d{Constructor (_,tjEc:Zl__){Continue ;} }Class y{Val u0,TK_0:Float ;Val $_,C,T59_,E09B,$_:String ;}Class AF{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1056))

    def test_1057(self):
        input = '''Class _:_{$2_51W(){Var _5,_5__g_:Float ;}Destructor (){}Var m:String ;jU(mR,_5_LAv:Array [Array [Float ,025],0x7];_,_8Cw,z:Int ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1057))

    def test_1058(self):
        input = '''Class ___{}Class i{Val d:Array [String ,8_6_2_6];Val x__,$ic_2_,$1,$Y,_,$40,x_,P:Array [String ,0xC];Constructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1058))

    def test_1059(self):
        input = '''Class a{Destructor (){Break ;}Constructor (f:Array [Array [Int ,0b1000011],0x51];_:Array [Array [Array [Int ,0b1000011],0141],0141]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1059))

    def test_1060(self):
        input = '''Class M7:s{}Class _{Var _rC,$H:Array [Array [Int ,074],0X9];Var __0,_5:_1_3f9__4_;Var $__,$1:Array [Array [Array [Array [Float ,03_7],041],73],63];}Class b:q{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1060))

    def test_1061(self):
        input = '''Class Us:_MT_2{Val $_,$28_53Z,$_,$_:Float ;Var $_:a_;$65(P3863,I4,s,UjN,_:c;_7_Z,_,_f5,_,Th___h:Float ;_,x4,_,_,g_:Array [Float ,31]){}Var $95_:h;Constructor (){} }Class O{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1061))

    def test_1062(self):
        input = '''Class _{Constructor (_6,G:_5;V:Array [Float ,0X4C];Q3:Boolean ;__,_7,d,_8u6KF,_1__d:Array [Float ,0b1111];X_l9_,N:Float ){}Constructor (VG:Array [Float ,0x2B]){}Val _5:m;Val n7:Boolean ;}Class M5S2:n_{Val m8:Float ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1062))

    def test_1063(self):
        input = '''Class uE:O{Constructor (_,_L1__:_;D,v,F8__,I:Array [Boolean ,0x20];_:Float ;r7,N:Array [Array [Float ,0b1_0_1],013];_:Boolean ;x7_:Array [Array [Float ,0XE],2];F,R,_:Array [Array [Int ,0X2A],0x20]){}$_(M8__w,_j_:Array [Array [Array [Float ,0b1],013],013]){} }Class _g4:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1063))

    def test_1064(self):
        input = '''Class _:__{Var Q0__,_,_,$6R:Array [Array [Int ,06],0x698];Constructor (l:n){Return !!!--New H()+j11::$_._w_();} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1064))

    def test_1065(self):
        input = '''Class _A6_Y8__:i_{Val $_dr_3:Array [String ,0B101110];Var $_87,C:Array [Float ,0x23258_0];}Class _{$_L(){}Val _,__,_9:C;}Class __x{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1065))

    def test_1066(self):
        input = '''Class _:_xD8{}Class X0:Y{Constructor (_0,P:Array [Array [Boolean ,85],0XC_E]){} }Class A:_2{}Class Q{}Class _{}Class _:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1066))

    def test_1067(self):
        input = '''Class _{Destructor (){}Var _,B785,_7_54MeYVWf_:Float ;Val __:Array [Float ,0B1_11];}Class Y{}Class _:Ml{_(_Z,_B,i:Array [Array [Int ,0x20],0B1_00];__A,_:Z){} }Class __A7{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1067))

    def test_1068(self):
        input = '''Class M_:___5{}Class _{$316(_:fcX;M,k:_7n2y7_){Return ;} }Class _{Val $X1:Array [Array [Array [Array [Array [Boolean ,0x5],28],0X7],28],0X34];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1068))

    def test_1069(self):
        input = '''Class __U{Destructor (){Continue ;Val _,Y_:Array [Array [Array [Array [Boolean ,3766],0X13],0X13],02_1_70];} }Class _:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1069))

    def test_1070(self):
        input = '''Class _:Z3_{}Class _{Var _:Array [Array [Array [Array [Array [Float ,0104],0x67],0b10010],70],0XE];_g5(){Break ;Break ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1070))

    def test_1071(self):
        input = '''Class _{Val $W,$0___4,_E8D9:Array [Boolean ,0XC];Constructor (EY:Int ){} }Class Py60__:JC89_2{}Class C{}Class _{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1071))

    def test_1072(self):
        input = '''Class _7{}Class TN:_{Val $0,$_,_55c,_,l4,$08,JZ,$1:Array [Array [Array [Array [Array [Array [Array [String ,072],0x42],0b1],072],0x42],0X58],0b10001];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1072))

    def test_1073(self):
        input = '''Class I__0_Y:_{Constructor (j_1,y2q,p:Array [Array [Array [Array [Array [Array [String ,5],0b1_1],0B11_0],0b1],91],0x41]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1073))

    def test_1074(self):
        input = '''Class O__:S7{$n(){}M(){} }Class _{Var $8:_0R_d;}Class _{}Class Ym:l{Destructor (){}Destructor (){} }Class __:Ij{}Class K:oz7{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1074))

    def test_1075(self):
        input = '''Class __:jd{}Class P:_A_{Var _,_:Array [Array [Array [Array [Array [Array [Float ,0x62],0x62],37],37],0b11_00_1_0_1],0b1011];}Class myxu1b{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1075))

    def test_1076(self):
        input = '''Class _:_{Val $77_,_:Array [Array [Array [Array [String ,0xF],014_6],3],0135];}Class V{Var $6,_:Boolean ;Val $j14_,$Z5:Array [String ,65];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1076))

    def test_1077(self):
        input = '''Class k:_{Var N,i,j:Array [Array [Array [String ,0x9],0X32],0B10011];Var $7,$_,t,CB4,$1,y,R_:Array [Array [Array [Array [Boolean ,031],37],04],0x16];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1077))

    def test_1078(self):
        input = '''Class _:__{}Class OZ__:_{Constructor (_:Array [Array [Array [Array [Array [Array [Int ,0x61],0x5],62],0x5],0b101101],0xA7]){} }Class T{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1078))

    def test_1079(self):
        input = '''Class R{}Class s:hyL{Constructor (_,_:s2f;_l861___,R119a:String ;O,__,_5,_:Array [Boolean ,06_16]){}$m(b:_;W:String ;nV,_u:Array [Float ,0B110001]){Break ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1079))

    def test_1080(self):
        input = '''Class _{Constructor (__28:Boolean ;X3d_6:_;_v,LT,F:Boolean ){}Var $_A,$7_,$_,$1V,_:String ;}Class g2s3J_6:W{}Class _:U_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1080))

    def test_1081(self):
        input = '''Class u_53:e{Var $_:Array [Array [Array [Array [Array [Array [Boolean ,0136],57],0136],0x8],9_2_4],57];$zS(_21_:P;_S:Float ){_::$g();__::$w._1_();} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1081))

    def test_1082(self):
        input = '''Class w9_:_7{Destructor (){Var n4:Array [Array [Array [Array [Float ,89],0b111100],0x5A],0b111100];} }Class P:U{Var $6:Int ;}Class _97I0{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1082))

    def test_1083(self):
        input = '''Class Zu9{Constructor (){}Constructor (L_E,_4:String ;x,_,_,_,A8,J:Array [Boolean ,77_0_6];__:Float ){}Destructor (){} }Class m:_U{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1083))

    def test_1084(self):
        input = '''Class _:_{Val $_4,H:X_;}Class Q:_{}Class _:_T{}Class _7:_{Constructor (){}Var A_8,$U,$4_,_9_8,XY:Array [Boolean ,0x5];Constructor (n_,_,_H,i2,k:Float ;S,_,K_0A8R:a7;_,____:_){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1084))

    def test_1085(self):
        input = '''Class _s_R0{}Class _{Destructor (){}Val _x,y9,$1:Array [Float ,0XB];}Class a{}Class wb{Destructor (){} }Class ek{}Class _{}Class __:n_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1085))

    def test_1086(self):
        input = '''Class _2_{_9(U__:Boolean ;_i_b6,z,_,__,R15:Array [Array [Array [Array [Array [Array [Array [Array [Int ,065],0B1010100],0x10],69],04],0B1_1],0B1010100],02_63];mM,jJ,_i:Array [Int ,69];O7__jE,___j,_:String ){}Destructor (){Break ;}Destructor (){Return ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1086))

    def test_1087(self):
        input = '''Class i_za{Constructor (__0,_:Int ;_n:Int ;q4:Array [Array [Array [String ,0X5C],0B1],0B111111];_2:String ;_:String ;__U,__9J:Float ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1087))

    def test_1088(self):
        input = '''Class h_f{}Class _8:E{_(N6_:Array [String ,9];_97,__z_:Array [Array [Array [String ,0462],0x4],45];_73:String ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1088))

    def test_1089(self):
        input = '''Class _{Var _,c:_K5;}Class g3{Destructor (){Continue ;_2::$R_();} }Class ___{}Class _:W{Var $_5,$_J:_;}Class j{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1089))

    def test_1090(self):
        input = '''Class _I{Var _,$5,$_:Array [Array [Array [Boolean ,3],03],033_3_5];}Class d{Val _w_,lX_,$F,_,$T_:Array [Array [Int ,0b1011101],0XE];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1090))

    def test_1091(self):
        input = '''Class mj{}Class Rs9:___{Val $1_1P:Array [Array [Array [Boolean ,0b1000000],47],0130];}Class _{Var _:Array [Array [Float ,47],0B1];}Class _:_Xz{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1091))

    def test_1092(self):
        input = '''Class _{}Class q{_2fUO(){}$66_(_:Float ){}Constructor (_:Float ;G79:Array [Float ,0b11_00_1_0]){}Var C9s__:String ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1092))

    def test_1093(self):
        input = '''Class _m__J:_{Val $_9,$_,$6,$_,I:Array [Array [Array [Array [Float ,0b10111],0b1_0],0B1],0b1001100];}Class __{Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1093))

    def test_1094(self):
        input = '''Class _{}Class _:l___{Constructor (i_,q_,_:Array [String ,0x8];az,_,t,__6:_5u;_k:s){Var _,d:Array [Array [Int ,07],0b101];} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1094))

    def test_1095(self):
        input = '''Class q_b{}Class __9tc_:t_x{}Class z:_{}Class D3_:r0{}Class _{}Class J_:u{}Class x___:q{}Class _:_{}Class __l_u{}Class S{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1095))

    def test_1096(self):
        input = '''Class _{Destructor (){}Val $q_xp,$926,__p_0,$_x,__,$7g,$m_:Array [Array [Float ,05],0XE];Destructor (){Continue ;}Var $7:_;}Class _{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1096))

    def test_1097(self):
        input = '''Class tN_{}Class J2g8{Var $I___1jL,$_o,$Q:Array [Array [Boolean ,0x41],0B110001];}Class _{Var Es:Array [Int ,05_36_036];Var U,$_e1:Array [Array [Int ,2_2],0B110001];}Class _5{}Class O_{Constructor (){} }Class _:W_{$Z3s(YE,_:_){}Constructor (_,_,_:__;P11_8:G;d6,X2,_,n:_;P__,X:_){} }Class _{Constructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1097))

    def test_1098(self):
        input = '''Class c_:D3{Val _:Array [Array [Array [Array [Array [Array [Float ,9424],4_0],0x5F],0x5F],74],044_67];}Class F4__H7{Val _,K,$9,$_0_:String ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1098))

    def test_1099(self):
        input = '''Class K_1_D0{}Class _{}Class j{}Class Z{}Class v__H{Val ___:_9;Destructor (){} }Class Q3{}Class Y:KH{}Class y{Constructor (){Return ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1099))

    def test_1100(self):
        input = '''Class n{}Class _6{Var _G:_9_;Constructor (u,JZ__,__j,_:Array [Array [Boolean ,0b1],0B1]){Continue ;}Var $pG_:Array [Array [Float ,0B1100011],0X6];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1100))

    def test_1101(self):
        input = '''Class _{Val $l7,$0wZ,__7c8_nu,B_,$_,$P:d_;$P__t(_,Y,m8:Array [Int ,3];_:Int ){}Constructor (WA:Int ;o1,_9_,_0i___4U6,_3:Array [Array [Int ,01_6],04_5_7_5];_:y6;r,_74:Boolean ;_,_,_X,___:Array [String ,0X8_E_D]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1101))

    def test_1102(self):
        input = '''Class W_03:K{Constructor (_,_9,S,f_,_:_h){}Val $_,$B,A3,$8:Array [Array [Float ,02],0X42];Constructor (q_,H6p0,_,d:_){} }Class o:_{}Class _:I{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1102))

    def test_1103(self):
        input = '''Class X{_(_,Xf,z,H1_:Int ;_,e,__,_:Array [Int ,7];____:Array [Boolean ,8];_5i:Array [Boolean ,0XA8];_,r,i:_;e2:Array [Array [Int ,9_7],032]){} }Class hD:_24{Val T,$up:String ;Constructor (_4:Boolean ){}Val $K_8,N:Float ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1103))

    def test_1104(self):
        input = '''Class T:c_733{$2(B:Int ;n:Int ;_4:Array [Int ,0111]){Break ;}$_5(_58,q5ehG:Array [Boolean ,05];_h,V,_:D){Continue ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1104))

    def test_1105(self):
        input = '''Class X{Constructor (_X76,_,t:Array [Array [Array [Boolean ,0B1_1_0],0b11000],0X3_B];_,so:Int ;A:_){} }Class _GZ:_1{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1105))

    def test_1106(self):
        input = '''Class r{Var _,$_Z_9_,a,$__9,$__,_:Int ;}Class _0{Val k,$3___3aK,_:Array [Boolean ,0B100110];Var Jn:Int ;T9(){Break ;} }Class H_f{Constructor (){}Val $__:Float ;}Class _:_{Constructor (){} }Class _:Ine4{}Class vQad8:_U2J{Destructor (){Return ;{Return ;} }}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1106))

    def test_1107(self):
        input = '''Class _{Destructor (){}Var $310,_,P,_7__:Array [Array [Array [Array [Array [Array [String ,0B10100],02],0125],0XA],0X58],0x1_D];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1107))

    def test_1108(self):
        input = '''Class I{Var n,$_,E:Int ;Destructor (){b__uY_::$3M8.C6_.l2_();} }Class p{cT_20(){Val __N:Int ;}Var $v,lc:Int ;}Class _:P_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1108))

    def test_1109(self):
        input = '''Class l:_{Destructor (){Break ;}$_H47(vI0J9_,W,b,X6iL,k,_,_,Fp:Array [Array [Array [Array [Array [Array [Array [Array [Array [Array [Array [String ,0B1_1_0],0X25],0b10111],0b10111],0xE],0xC],3],19],0xC],19],0b10111];b,_6:b){} }Class _{Constructor (){}Var $__5:__0cZ_;Val _:Int ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1109))

    def test_1110(self):
        input = '''Class _:U{$_(){Break ;}$_5(r,XO,RCg:Array [Array [Int ,0B1],73];I1__X:String ;f:Array [Array [String ,0xE0],5];_:String ;cV:x_){}Var _,$6_AV,$1___LG:String ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1110))

    def test_1111(self):
        input = '''Class _5{}Class _m{Destructor (){}K8(I:_;u_:Array [Array [Array [Boolean ,0b10],0B101000],0b1];__vN:Int ;vR:Int ;G,s:_;__E,_:Array [String ,0x23];___,_X,_9_d:Int ){}$3_V(ic:Array [String ,31_54]){}Constructor (G:String ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1111))

    def test_1112(self):
        input = '''Class u8:_f{Var H_,$__:Float ;$_(v_:Array [Array [Array [Array [Int ,0X5C],0b1],0B111011],0b110000];e_:K){_::$4l();Break ;} }Class K5{$___(){}Var $d,$8,$z_5_,_,$5,S:_;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1112))

    def test_1113(self):
        input = '''Class v{Constructor (){} }Class __p{$T(____:Array [Array [Array [Array [Array [Float ,0X5E],0x3],0x3],25],0x5];_:Array [Float ,062];_:Array [String ,25];__:String ;_r:Int ){} }Class _u2{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1113))

    def test_1114(self):
        input = '''Class A:_95{_(p,_:J5){}Destructor (){} }Class _{}Class I:W3{}Class _:Q_{}Class _{}Class e:_Np31{}Class _{Val O:Float ;Val R_Si4,$d,$_,$_,$S__:Array [Array [Array [Float ,0b1],062],34];}Class _5:_0h{}Class _:o{}Class jg_:JW{}Class T:H__9_{}Class x:y{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1114))

    def test_1115(self):
        input = '''Class _:_{Var _5:Array [Array [Float ,034],0b111001];}Class _{Var _2:Int ;Var $3_:O3_;}Class R6_:ngy{}Class mi{Var q_:Dw9;}Class g:a7{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1115))

    def test_1116(self):
        input = '''Class __rL{Destructor (){}Destructor (){}Val $S,$3,$0,$_1_,j:String ;Constructor (t,_,_,_B,W_:Float ;SK:String ;__,Q__:m){}Val _,_,$3,$6__v,$1_:Array [String ,0b111101];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1116))

    def test_1117(self):
        input = '''Class _:_{}Class s__:_{Constructor (){}Var R43Z:Array [Float ,57];Destructor (){}Var $j,$F,$V1_,$Lr:Array [Int ,03];}Class nxqLw_1{Var $__R:Boolean ;Constructor (){} }Class b_Qe:T{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1117))

    def test_1118(self):
        input = '''Class _Vpdz__:xl_0_{Destructor (){New M().Q.i()._().__t_();{}{ {} }}Destructor (){} }Class _K{Destructor (){ {}{} }}Class _:X{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1118))

    def test_1119(self):
        input = '''Class _:_5{_(){}$___G(t:Array [Float ,050];E:Int ){}Val _5:Array [Float ,0b100111];$1n(_,y_,_6,j:Array [Boolean ,64]){Break ;} }Class _:_{}Class _:_5{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1119))

    def test_1120(self):
        input = '''Class fE:_3{Var __9t,_,W6,$4e:Array [Array [Array [Boolean ,0B1_1],9],8];Var $j,_3,_:Array [Array [Array [Array [Float ,89],89],0B110],037];___v5_(){T73::$__31();}Val _:Boolean ;}Class T:t{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1120))

    def test_1121(self):
        input = '''Class E6o78o{Constructor (T9,o,b:Array [Array [Array [Array [Array [Array [Boolean ,1],40],0104],0B1_0_01_0],0b1_0_00],0104];a4:_0_8){} }Class _8:a7{}Class o:J9{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1121))

    def test_1122(self):
        input = '''Class a_:a{Var _,k,G_5,$_,$0,N:Float ;Var $c_,___X_:Array [String ,67];Destructor (){Return ;}Var $_V:K_1;}Class e:_V{}Class _:y{}Class n:R{Var j,_R_4h,$2,$_vRD:Array [Boolean ,0x8_C];}Class K0:XeK_2_3{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1122))

    def test_1123(self):
        input = '''Class __:_{Val _,_,$_w:Array [Array [Array [String ,02_66_0_3],83],03];}Class V:_{Val _9:B;}Class g:F{Var _,D0_,_,$_,$_D2R_:Array [Array [Array [Array [Float ,056],0B10000],83],07_0_0];}Class _{Constructor (){} }Class _:_Tp{}Class M_4{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1123))

    def test_1124(self):
        input = '''Class m:__{}Class _2:_{}Class dD_P_L{Var _O7,M2A:Array [Int ,0X38];Destructor (){}Constructor (){}Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1124))

    def test_1125(self):
        input = '''Class _:_{Val $Z_05_,$_1,$0:Array [Array [Array [Array [Boolean ,0X21],0x4F],0xC4],0B1100001];}Class _W5_{Destructor (){ {} }}Class _6:_{Val v8:Array [Boolean ,0X21];___P(){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1125))

    def test_1126(self):
        input = '''Class _{}Class _0:_{}Class _p{}Class _:_{Constructor (){} }Class c{}Class _{Z(_0___Q,_0,__54,v,L:Boolean ;M___,_:__;y:Array [Float ,63];D4,_2Q_F_,_,__y4__,__R_:Array [Int ,04]){} }Class _{Var $9_7:l;}Class __:__w{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1126))

    def test_1127(self):
        input = '''Class v7{Destructor (){}Val y0,$q_,$4,$4:Boolean ;}Class _5{}Class W{Var $uG,$f:Array [Array [Array [Boolean ,13],03],73];}Class p{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1127))

    def test_1128(self):
        input = '''Class __:_1_B{}Class jV{__(Z,t_PK_2Nk_,ul,Ty9_5:Array [Array [Array [Int ,0b1],0B10001],0B10001];m:g5_a;_,_q6__,Dg6_:_){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1128))

    def test_1129(self):
        input = '''Class h4:c0{Constructor (){}Var F,$69,$8:Boolean ;zt(){}Var $_H44:Float ;Val $i:Array [Array [Boolean ,0x4C],6_10_3_2];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1129))

    def test_1130(self):
        input = '''Class o:__3_3{Var $_4,__:Array [Array [String ,0120],0b11010];}Class V:I{$4u(_:Array [Array [Array [String ,0xE2],63],63]){}$252u(p,_:Array [Array [Array [Boolean ,0120],05],0xD_2_F];__:Array [Int ,63]){}_(rc:Float ;vaW_:Float ){}Val g___Og_l__:P;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1130))

    def test_1131(self):
        input = '''Class _{}Class M0:_{Val $j,_q_4:Array [Array [Array [Array [Array [String ,0B100110],90],0B100110],62],0x54];Constructor (a9_:_V4;_m5z5m_664_u_5P:Int ;_,_:Int ;_,t:_){} }Class A___{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1131))

    def test_1132(self):
        input = '''Class F62:_Q9{}Class _{}Class i:N3Y{}Class C_e:E7{Constructor (W,_:l;_E:H;_9I_8Ss:Array [Array [Array [Array [Array [Array [Array [Array [Float ,0xB_13],0x5],0X4],6],0b10101],0B1001101],6_0],0b10101]){U::$_e();{Continue ;Break ;}Break ;Break ;Continue ;Return ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1132))

    def test_1133(self):
        input = '''Class c{$4(R_q:Int ;b:Array [String ,041];_QQ7_H,__f,__:Array [Array [String ,0X37],0b1]){}Destructor (){}Val __4:x5;Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1133))

    def test_1134(self):
        input = '''Class ____:Ec_78Da{}Class _Y:_9__{}Class _{Val __7,$_:Float ;}Class y{Val N,_:Array [Array [String ,39],0x15];Var __,r,$_,$1_8,$_4,_L_xw,_,X95:Array [String ,0B111100];_G39(g:Array [Float ,0X4D];_,A:Array [Array [Int ,031],071]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1134))

    def test_1135(self):
        input = '''Class d:r__{$_1(Fy7,_:String ;v,_1f_Q181P:String ;O:f;c_:Boolean ;_,_6,_5:Array [Array [Array [Array [Array [Int ,8_232_4_3_5],07_3],06],0X2],48];Z:Array [Array [Boolean ,0130],0b1];__:_;Cb,_6w:Array [Array [Array [String ,0X47],0X47],0x44]){}Var l3__YQ___:Int ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1135))

    def test_1136(self):
        input = '''Class _:F{J(_W,i:Array [Int ,03_6];re_,_Z:j_8;_d,_,_0:Array [Array [Array [Array [Int ,04],0530_5],03],074_2]){}Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1136))

    def test_1137(self):
        input = '''Class _8{}Class O2:_{Var _:Array [Array [Array [Array [Int ,8_5],0x3_E],24],075];}Class P_:_6_{Constructor (_,E:Array [Array [Float ,0B1010111],04]){_::$2();Continue ;}Val $y,D_n95__7,$M,$_,$0,_:Array [Int ,24];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1137))

    def test_1138(self):
        input = '''Class _{Constructor (_,_84,_ou:Array [Array [Int ,0511],06];I,_7I_54zx,bE1,_64,_:A;_:Int ;p,U,x:_03;x,__,____:c){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1138))

    def test_1139(self):
        input = '''Class _:_{Val $__,i_6:Array [Array [String ,02],05];_l(y,_,K_,_:Array [Array [Boolean ,0X1_C],0X26];_:String ;__,_7k7,p,_,F0:E_){} }Class _73:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1139))

    def test_1140(self):
        input = '''Class __:_{Var eF:Array [Array [Float ,051],0b1];Val $IOK,q5,$1D:E;}Class _:b_{R_(){}Destructor (){} }Class AT{}Class g5_5z{Val $_c:Float ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1140))

    def test_1141(self):
        input = '''Class p:O{Destructor (){}Constructor (){ {}Continue ;}Destructor (){} }Class K_c:S_{Var _,_Q_,$6__M:Array [Array [String ,0B11],05_4_5];Val _,__8n,$9,_:Float ;}Class x:u{Constructor (_,W17_7:Float ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1141))

    def test_1142(self):
        input = '''Class X2:_{Destructor (){Var Af_1e,m:Boolean ;Return ;}Destructor (){ {} }}Class _2:__13_{}Class L:_T{_(_,_:Boolean ){}Val $0h1:_;Val _f7,h,$67_031:v_2W;}Class D0J_:Y_Z{}Class M_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1142))

    def test_1143(self):
        input = '''Class U2:j{}Class _J5:_{M(_r:Boolean ;_,_:Float ;_:M;_S_L3_:Array [Array [Array [Array [Array [String ,48],0b11],0b1],030],0x4A];_s:Array [String ,030]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1143))

    def test_1144(self):
        input = '''Class _:Z8{$0_68__v7(_:Array [Array [Boolean ,0b10001],0b10001];__,ln,b0,U:Array [Array [Array [Int ,92],92],0x5B];VtF,K9,__t:String ;_,__588,_:Float ;G,_,l,Hj:_Q_;t0_1,A:Boolean ;__g_,j0:Array [String ,92];_:ghw__){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1144))

    def test_1145(self):
        input = '''Class _3_:b{$9(_,_4_,X_9_,_,_7i:Array [Array [Array [Int ,0b11],0B110],0B1_0];Qx,S1:_09_){}Var $U4:Array [Array [String ,0x23],0b100100];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1145))

    def test_1146(self):
        input = '''Class J:_{$2L5k(K:Float ){F::$m3();}Constructor (E:Boolean ;r,_,G,B,_0,J,C0_:Int ;_r:__){Var _5,_,_:String ;Continue ;Val z:Array [Boolean ,91];} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1146))

    def test_1147(self):
        input = '''Class E:_{}Class _X2{Var $B,$S,$90:Array [String ,3];}Class _s{}Class m{}Class eAfY:Y6{Var $_48:Array [Int ,953];Var $_x2:String ;Var $B_,l:Int ;b_w(_:Array [String ,3]){} }Class _{Var $2,$5b:String ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1147))

    def test_1148(self):
        input = '''Class _:__7{Val $7,R:_;Var _6,N,kZ,$d_,_n,s1i,_r7,$5:Array [Array [Array [Array [Array [Array [Int ,0b1],0x29],0X5],17_4_79_1_8],0x29],0X1_1B_B48];}Class ___i{}Class __65B{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1148))

    def test_1149(self):
        input = '''Class N9:l{Var $p:Array [Int ,0xE];Var $wZ:Array [Array [Int ,0b10],0XF];Val $4:Array [Array [Array [Array [Array [Boolean ,042],69],03],042],05];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1149))

    def test_1150(self):
        input = '''Class Z0{Val $1P,$A5,$_8___897_g3:H;_(_84:Array [Boolean ,8];k,_p:W){Continue ;}$4_9(f1E:_;_,q0:Array [String ,03]){}g5g4Sd(){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1150))

    def test_1151(self):
        input = '''Class e6{}Class _:_{$5_gc___m(y2_,_3,s_00:Array [Array [Array [Float ,0b101100],0x54],17];L,__:Array [Array [String ,04],17];kL:Int ;_:__;_,_v:Array [Boolean ,0xE]){Return ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1151))

    def test_1152(self):
        input = '''Class K{}Class _{$_8(x_,__,J,_:_S;_,_:_;__:Int ;_,_:String ;__:Boolean ;Sw1_,Z_:Array [Array [Float ,0X6],0XF63A3]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1152))

    def test_1153(self):
        input = '''Class mI_:z{}Class S6C:_6{Var J,$8H,Q3,N:M;}Class wd_{}Class _{}Class _:_KF{_g(y:_WUgo_ix7;c7b:Array [Array [Float ,0b1],0X7_9]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1153))

    def test_1154(self):
        input = '''Class m{Val $_:_8U;Destructor (){Continue ;Val __6,s__0V,F:Array [Float ,6];}Constructor (p,ME,xa7:Float ;_:Array [Float ,046];O,rS,_,_L,u_7,IY,_:Array [String ,03];_V_BS:_Ox;g8,S1J7:String ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1154))

    def test_1155(self):
        input = '''Class _{Val $z_,F_:Array [Array [Array [Array [Array [Array [Array [Array [Float ,21],0X51],21],0X51],0b10_0],0x4],0X51],21];}Class _4{Destructor (){}Destructor (){}P_(){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1155))

    def test_1156(self):
        input = '''Class j_2{Constructor (__y:W;_,ed,H_,A2,__:Array [Float ,68];_,_,_u,T,_:Array [Array [Array [Array [Array [Array [Array [Array [Array [Int ,04],0b1000],0b1],0B100],0B101],071],68],68],68];_,p_E,_,_,_,W,__:_;_,Fr:L;_8_8:_yV5_6;__5Ib:Array [Boolean ,0b1]){} }Class ph5:_{Var $_3:String ;}Class _2_247:_{}Class _N{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1156))

    def test_1157(self):
        input = '''Class _{Var _,_l,_:s;$A(_:Int ;_,_b:q3A;y2Q_,RV:Boolean ){} }Class __:T_1nc5{$_(t:Array [Int ,027];_:Array [Float ,0b111111];_,P:Int ;Dm_:Array [Array [Boolean ,0x3C],03];d_:Boolean ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1157))

    def test_1158(self):
        input = '''Class Vl7F__p{$_(_8:Boolean ;_b_,y7:m_f_N;j,c,__2,R_:Float ;l,_K__,l:__;_:__;_:Array [String ,03];m,_Zg:_C;L,_:_){Val _9u:_;Return ;}Destructor (){Break ;} }Class x110:a{Val $5c__O0XY,p,$9,_,P07__,$_:Array [String ,2_882];vq(){} }Class _ik4j4Y4A_7Q__9_Q{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1158))

    def test_1159(self):
        input = '''Class _:_9{Constructor (_,_7B:Array [String ,0X32];__:_;_d:q;_c,_3X_:_4q;h,_11:Array [String ,317_61]){_::$_7().AC();} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1159))

    def test_1160(self):
        input = '''Class _45:k{Var _5,_2_H,_,$j:Array [Array [Float ,0B1],0x5D];_N_55(_9z5:Array [Array [String ,0XF],0xD_40];D,m:Array [Array [Array [Array [Boolean ,0X13],6_81_2],0X1],0XA_6];F:Boolean ;O:T_){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1160))

    def test_1161(self):
        input = '''Class _:_{$_(){} }Class _:__5{}Class R{}Class j{_5(){V::$s___();Val _:Float ;} }Class z_y2839_:_b8{}Class _{}Class d:Mu__M{Var Z:Float ;$83(){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1161))

    def test_1162(self):
        input = '''Class _:_{}Class _7Z:_{Constructor (h,e,mK,t:_8;_g,O,_:Array [Array [Array [Float ,17],17],0X24];_,___:_0;Q31,_f,g:Array [Array [Float ,17],0X24];y_:Boolean ){}t_7(v5:Array [String ,0b101101]){Break ;}Var $j_E:Array [Array [String ,0B110],17];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1162))

    def test_1163(self):
        input = '''Class W{Val _U,$8,hJ:Array [Array [Array [Array [Array [Array [Float ,047],0X64],1],0x56],0X64],0xA_B];Constructor (){Break ;}Val P:_;Constructor (){}Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1163))

    def test_1164(self):
        input = '''Class Q:_5{Constructor (gk,_,PH_:Array [Array [Array [Array [Float ,58],01],58],58]){} }Class m8:_iox{}Class SuP{Var M,_w_:Int ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1164))

    def test_1165(self):
        input = '''Class _:_{Val _,$An0,$_,$___:String ;}Class _k78t__{}Class _:C_d1{$M(_8_:Array [String ,52]){} }Class _z:cH{}Class _9mI_{}Class _{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1165))

    def test_1166(self):
        input = '''Class __X:_{Val D:Array [Boolean ,96];Var x:_;}Class EG:C__8WRU{}Class u_:u3{}Class g:Q{Destructor (){Return ;}Destructor (){} }Class _89S__u__:r_{}Class aK{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1166))

    def test_1167(self):
        input = '''Class _0__0R_{Constructor (_S2e,W:Array [Array [Int ,1],0b111];F:Array [Boolean ,60]){} }Class I99_:s2{}Class od:T6D7{Var $_G:Array [String ,60];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1167))

    def test_1168(self):
        input = '''Class _:dr{Val $__lT:__;Constructor (J_,_:Float ;Z:Int ;m3_:Array [Array [Array [Array [Array [Array [Boolean ,0XD8],4],1],1],0XC],0X57_4A]){k::$9_._.K=!!-f::$_1();}Var $z,$_:Boolean ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1168))

    def test_1169(self):
        input = '''Class _{Val h,__:Array [Array [Int ,05_6_54],23];$39_(){}Val Z,__:__h1H;Constructor (R1__,q,g,f_3_:String ){ {Break ;}Continue ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1169))

    def test_1170(self):
        input = '''Class __:_{}Class I{Val $_,U5,$_7:X33;}Class __:_w_6{}Class pL{Constructor (_4D0,e2_5_,B,O:g;R,_,e:String ;h:o_){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1170))

    def test_1171(self):
        input = '''Class _J:_{}Class B:_{}Class r{Constructor (__,w:String ;_,_,_:_;_J_:Array [String ,03035];_g:Array [String ,0b10010_0_1_0]){Break ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1171))

    def test_1172(self):
        input = '''Class _5q__{}Class _3_:oM5_3{$D(L:i;re_,_o,a,_:Array [Array [Int ,2_128_3_3_4],50_78];_i_:Array [Array [String ,0b100],0XD]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1172))

    def test_1173(self):
        input = '''Class u{Constructor (){}E(_,_6:Array [Int ,0XC]){} }Class _:Q_{Constructor (_:Array [Array [Array [Float ,0XC],33],0XC]){} }Class _:jj{Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1173))

    def test_1174(self):
        input = '''Class N{$0(_3:_80_t2;c:s7;_,B,_B:_;U,_4:Array [Boolean ,0B1]){Continue ;} }Class sU:_{}Class y:K{e(J,qz_,_L:Float ;wk:Float ){ {} }Var $_u__:Array [String ,0X33];Var $B14v6z,_eJ:Array [Array [Array [Float ,0b1],07],0X6_9_8];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1174))

    def test_1175(self):
        input = '''Class _U{}Class d:k{Var CX:Boolean ;Val _:Array [Array [Array [Array [Boolean ,0b10],3],10],0105];Var B:Array [Array [String ,0X1A],0B1001111];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1175))

    def test_1176(self):
        input = '''Class cZv3:mH6WH{}Class _9{$__(){}Val $R7:Array [Array [Array [Array [Float ,0102],85],0102],6_6_2];Destructor (){ {} }}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1176))

    def test_1177(self):
        input = '''Class h:C{_(){}Var a_,f_h8,$9:Float ;}Class Zp_8:_5_{_(){}Constructor (__v_:Boolean ;Y_b_,YAB,_Y:Array [Boolean ,031]){Return ;Break ;__::$d().U();} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1177))

    def test_1178(self):
        input = '''Class f{Constructor (){f_::$O2();}$1y0(){_t::$8_1();}Var $2:_x;}Class i__9{Var $73:Boolean ;Var $_:nJ;$_P31_(S:g1_V){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1178))

    def test_1179(self):
        input = '''Class s2X4{k_(t_E_G:Array [Array [Array [Int ,38],0B110011],0b1];_1P,v_C,I,_6_y,_,F_4:Float ;_r,e___:Array [Array [Float ,0X3D],0x25];_:Boolean ;K:Array [Int ,0X6];_F_,_:__){_::$_._s3()._();Break ;}Val N,$LB__,$_,$C,$0,C,$G_,$__9_:Float ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1179))

    def test_1180(self):
        input = '''Class g:_pc_{Constructor (_,Y:Array [Array [Int ,59],0B1];__,_:String ;Za,_0:Array [Int ,0130]){}Destructor (){}_l(){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1180))

    def test_1181(self):
        input = '''Class __:_{}Class _:a_{$_(P1:Array [Boolean ,93_8_1_3]){} }Class N{Val $T2:Array [Float ,5];}Class J:V{Var _w,_mi,t:E_;}Class _h{x(i:Int ){} }Class O:E{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1181))

    def test_1182(self):
        input = '''Class u:Qc{__0(CY,F:E;H_:Array [Array [Float ,01_7],0X2F]){} }Class dTr_:_{}Class _{Var $a,$0:Z;}Class _{}Class L{}Class _{Destructor (){}Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1182))

    def test_1183(self):
        input = '''Class _:b_{$_(_:Array [Float ,0xA];_3:Boolean ;_:Array [Int ,066];Z,__,L,fZ:Int ){Break ;}n(){}Destructor (){}Val $6X:Array [Float ,0b1001111];}Class _:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1183))

    def test_1184(self):
        input = '''Class Rh_P{}Class _9P{Constructor (K_8_,___z:Array [Array [Array [Array [Array [Array [Boolean ,0117],0B1],0x3],0X9],0X5],0117]){}Var f:g_M;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1184))

    def test_1185(self):
        input = '''Class _3{_4_(_:Array [Int ,0b1011110]){Continue ;}Val V,A:Array [Array [Array [Float ,027],0b1011110],073];U(){Var _,K:Array [Array [Array [Float ,406],073],0x9C];} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1185))

    def test_1186(self):
        input = '''Class _2{$_(_7,_,a_,_T,w_:Float ;_:String ;_,d,_:Array [Array [Array [Float ,0B101],0b1_1],07];_p,u_,_,_,t:Array [Float ,81]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1186))

    def test_1187(self):
        input = '''Class Q{}Class m{Val _ny_,g_:Array [Array [Array [Array [Array [Array [Array [Array [Boolean ,0b1],1],012],0X6_8],0B101110],0x2],6_1],0x35];__(){}Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1187))

    def test_1188(self):
        input = '''Class Y0:_h_0__{}Class _K1:_{Destructor (){} }Class l_C{Val $X6,$0,w4,J3,$__,P,$8:Array [Array [String ,8],0X28];}Class _{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1188))

    def test_1189(self):
        input = '''Class _:_2{L(H,_G3:Array [Array [Array [Array [Array [Float ,03_6_3377_61],0113],0x2],0X7_D],62];_8_,_,_,K,N7,_,__,K__:Boolean ){} }Class _5:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1189))

    def test_1190(self):
        input = '''Class _9:_D7{}Class K_{}Class _6_3:l{}Class e:DI{Var $18,s9_:Array [Array [Array [Array [Array [Int ,0X7],24],0X60],24],0B101111];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1190))

    def test_1191(self):
        input = '''Class s:uT_{Val $h_,$4,$__:Boolean ;Constructor (){}Val $9,$__,$X,_k:Array [Array [Array [Float ,5_0],0b100010],55];}Class _{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1191))

    def test_1192(self):
        input = '''Class ___{}Class _{}Class _l:z{}Class _:_2_52{Val _:Array [Array [Array [Array [Array [Array [Float ,0b11100],5],0X5E],07],9],0X9_FC];}Class _U:____9{Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1192))

    def test_1193(self):
        input = '''Class J:N{Var Z1,____:Array [Int ,0X4];}Class z:_{}Class _2{}Class B_1{Val $_:Array [Array [Boolean ,6],01];Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1193))

    def test_1194(self):
        input = '''Class _:__k{Val K_d,_:Array [Array [Array [Array [Array [Array [Array [Array [Boolean ,81],0b1010100],5],01],81],1],0B1100],0xC_0];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1194))

    def test_1195(self):
        input = '''Class c{Var $d,$5:a_;Val f,Q,__1,$2__O:Int ;}Class B{}Class a{$5_Rj_6(_5:Boolean ;D5:___4){Continue ;}Val $ms04,$p_,L:Array [Array [Int ,0xF586],0B1];}Class _{Constructor (_,O:k){}Constructor (_:Array [Array [Array [Boolean ,921],7],067]){}Val A_:Array [String ,0B11];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1195))

    def test_1196(self):
        input = '''Class _{$k1(){Break ;}Destructor (){}Var _,$D:String ;_2(J,I_:Array [Array [Array [Boolean ,0XF],0B1],06];F8_,d2:Boolean ){}Destructor (){Continue ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1196))

    def test_1197(self):
        input = '''Class En_:_{Val s,vfk,h2,$s:Array [Boolean ,0B101001];$48g(__P_,C9,___r8:a;g:OzLu){Continue ;}Val $_,_,$d56,$F,_,_57:String ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1197))

    def test_1198(self):
        input = '''Class V3{Val $6_:Array [String ,0b1100011];Constructor (C:Array [Array [Array [Boolean ,0B101111],052],01]){G::$_nm_();Break ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1198))

    def test_1199(self):
        input = '''Class G:__{Constructor (_,e_,z,T6:Float ){} }Class _:z3{}Class T{Destructor (){}Destructor (){Return ;_::$_9b();} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1199))

    def test_1200(self):
        input = '''Class _:__{Val $_:Array [Array [Array [String ,79],79],52]=-M26bX::$_();Destructor (){}Val $0,$W,$7:Array [Array [String ,0xB_E],79];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1200))

    def test_1201(self):
        input = '''Class _{Val $6u9,$9:Float ;Destructor (){}B8_(__,L_,_4h___,_f:Array [Array [Array [Array [String ,0b111111],0140],0X2],0b1]){Continue ;Val O2c:T;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1201))

    def test_1202(self):
        input = '''Class Q:S{}Class _:X{Val D,$dr8_,_:Array [Array [Array [Array [Array [Array [String ,0B101100],0x18],6_5_6_5_3028_72_8],0x3_FB],1],04];}Class g:V_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1202))

    def test_1203(self):
        input = '''Class dy:V{Var $8:String ;Constructor (){}Constructor (___y:Array [Array [Int ,0XD_3],0x3];_G_,p7c:q;_,__,H,__,_7,M3A,_:String ;Q56:Array [Array [Int ,0X4C],03_1]){}Destructor (){}Var $_4:Boolean ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1203))

    def test_1204(self):
        input = '''Class _2_:_{}Class _:__4_8{Constructor (l:Array [Array [Int ,99],2_4_6];_:Array [Array [Float ,0x4F],02];_,_j_U,Y,iL6:Boolean ;DV_P,__:J0Z__){}Var _0:v;}Class v{Xl(){}Destructor (){} }Class K:_{}Class _:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1204))

    def test_1205(self):
        input = '''Class _{Constructor (___u,w2n__84:Float ;Hl:__;_u,t7:Array [Array [Array [Array [Array [String ,032_1],4_8],03_11],04],0103]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1205))

    def test_1206(self):
        input = '''Class _:_4{Constructor (Y:Boolean ){}$_(m_:Array [String ,03]){} }Class _:m{Constructor (j,c_7,g6,_:Array [Array [Int ,0x9A_1_3],0B10_1]){Return ;}Var rK,_:Int ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1206))

    def test_1207(self):
        input = '''Class R__:v_I_{Var $__b:Array [Float ,0b11];_4(_35:String ;___:_){Return ;}Val $P,$_d_C,Y2,$__9,$A_:Array [String ,1];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1207))

    def test_1208(self):
        input = '''Class _:_{}Class _zQ{i5(){}Constructor (v,e0,C:s_){ {} }Var $8:String ;Destructor (){}Destructor (){ {}{}Continue ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1208))

    def test_1209(self):
        input = '''Class _:_6X{_(__T5_:Array [Array [Array [Array [Array [Int ,07_7],0b10_10_1_0_0],0X5],0X5],06];g:__8_G){} }Class _{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1209))

    def test_1210(self):
        input = '''Class u{Constructor (){} }Class _{Val _,z:Float ;Var $_,$sl:Array [Array [Array [Array [Boolean ,791],12],054],07_2];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1210))

    def test_1211(self):
        input = '''Class G:v{Val _,$n,_,S,s8,K5_:Array [String ,20];Destructor (){Break ;}p(ZN,S63,sk:Array [Array [Int ,20],0b11111];_,_:q){}Var U8,$n:__;}Class _{Constructor (EY_0L,_,a:Array [Int ,0x535];Y2:_1u){ {} }}Class bg:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1211))

    def test_1212(self):
        input = '''Class _k{r(_,j,_,y4,_5:_){}Val $05,uQ_,_g:Array [Array [Array [Array [Float ,02],7],0x4A],1_6_4_8];Destructor (){Continue ;} }Class i:N56_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1212))

    def test_1213(self):
        input = '''Class _y_{Constructor (I,_,_:Array [String ,2];h7_:String ;g6:_){}Val $9:Array [Array [Boolean ,0x43],0X432_7];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1213))

    def test_1214(self):
        input = '''Class _:_2{Destructor (){} }Class V_C:P{Constructor (){} }Class Zt:E_M1{Constructor (_D__:Array [Float ,79];k5_:Array [Array [Array [Array [String ,0x22],540_2],79],0b1_0_0_0];_:_;u:Array [Array [Float ,0X45],0133];_:Array [Array [Array [Float ,79],0x22],79];_,_2:_D_;RO8d,Rq:_5;_7,_,V:Array [Array [Float ,016],0x9]){}$i(){Break ;} }Class _{Var $8,R,$1,_:Array [Array [Array [Array [Float ,79],0b11010],0B11],0X45];}Class _{Constructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1214))

    def test_1215(self):
        input = '''Class _6_y:_G00W_{Val $_Y_3,____7:Boolean ;}Class I_{}Class ___6{}Class xu:_q{}Class Ei_{x(y:m;J_:Array [Float ,0X6_F2];S_,N,In_ :_;__n_U,_,j:Boolean ;_0__5:Array [String ,0X62];_:Boolean ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1215))

    def test_1216(self):
        input = '''Class G_:_{Destructor (){ {} }Constructor (_5:Array [Float ,017];A,_w,k__,X,o,Ty:String ;_d:Array [String ,8];RvN,_:Array [Array [Boolean ,0X2_0_D],0x5_6]){ {} }Val $2,$_6C_,XtL:Array [Array [Array [String ,0X26],0XF],0b1];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1216))

    def test_1217(self):
        input = '''Class _:_{}Class Y:m{Constructor (__,g:Array [Array [Array [Array [Array [Boolean ,0XF],97],8_5],97],0x5];B_,G:Float ;_29:Array [Float ,054];l,sdet,r:_){} }Class __{Val $_7MU:Float ;Constructor (h,f__J,_,y,S__:_){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1217))

    def test_1218(self):
        input = '''Class Y:fe{}Class R2:I{Val $_,n_,_4,s,$G:Array [Array [Int ,0x7],0B1];Constructor (pJ,_8_1:Array [Array [Float ,0b1010001],18]){} }Class _9:_u{$7(_,r,__,r:String ){} }Class _{Var $G,_,Uz:Boolean ;$8_(_,_,W:Array [Boolean ,0B10_0]){Continue ;Val _140:String ;}Val A_j:_3H_;Destructor (){}__4(){Continue ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1218))

    def test_1219(self):
        input = '''Class P5:_3{Constructor (_:Array [Array [Float ,0xD],0XC8F1];_N,z1___72,b,ZB,___,_,E7,_,_D_xrI:B;p:Array [Array [Int ,0131],0x97]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1219))

    def test_1220(self):
        input = '''Class _:K{}Class __{Destructor (){}$e6_E(_l:_1f;d,E,w8,__,x871d5:Boolean ;_M,_:Array [Int ,036]){Continue ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1220))

    def test_1221(self):
        input = '''Class V:V7vG{}Class F{Destructor (){}Val $_:Array [Array [Float ,1],076]=--Self ._()._5()._n;Var _N:dI6;}Class pR{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1221))

    def test_1222(self):
        input = '''Class z0:E{}Class _:W_hry0_j{}Class _{Constructor (_3f:Float ;W_:_;Q,_Y42_0,__,_,B9,f,_,_a5SF:Boolean ;Y_7XK:_){} }Class _2:lY{}Class _:_{Constructor (u:Float ;u,_F_n2:_;_,__:__){Break ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1222))

    def test_1223(self):
        input = '''Class r{Val $_g:Array [Array [Array [Array [Float ,1],0522],0b11100],0XC];}Class VdiI_:__{}Class _:s{Constructor (__,_,_:_;f5,S:JpX1){} }Class _:l{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1223))

    def test_1224(self):
        input = '''Class _W{}Class _3:_YU{Val $1,$_:U;Val __a,_5,$_:Array [Array [Array [Array [Array [Array [Float ,0x63],0X2D],17],063],07_6],0B1011000];}Class _:Y0{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1224))

    def test_1225(self):
        input = '''Class _3B870_:X__3{}Class _{Var $2__R,$b74V67n:Int ;Constructor (){}Var Rx4,_XoI,$_:Array [Float ,0B1];}Class _:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1225))

    def test_1226(self):
        input = '''Class _0:Ol8{_(z0__562:Array [Array [Float ,0X269],05];_z,_,__3G__K_,_,Uf__,z7:Boolean ;_,_8,_,__S:Array [Int ,0X7_C]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1226))

    def test_1227(self):
        input = '''Class _b:__{Destructor (){Val CfwW,t,_X3,z:Array [Array [Array [Float ,0b1000110],41],0B110101];}Var $9,$o6V48,_N8,$WWd,$_:Boolean ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1227))

    def test_1228(self):
        input = '''Class _1_:E_{Destructor (){Continue ;Continue ;} }Class uD_{Constructor (){} }Class _{Var $2T,$C_h_:_;}Class xc:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1228))

    def test_1229(self):
        input = '''Class _:wB{}Class g{Var _____Lx,k,$59,$2s:Array [Boolean ,04_50];}Class _9:d_{Val Z__,$i:_;}Class _{Val __:Float ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1229))

    def test_1230(self):
        input = '''Class d__0{Val $_,S__ne,__:Array [Boolean ,0X7_E];Constructor (){Continue ;}Constructor (_,n,_S,B_4:_w;h3:Array [Array [Float ,0116],0B1]){Continue ;}Val $a,__P,$J,_v:Boolean ;}Class __{}Class _:_p_l{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1230))

    def test_1231(self):
        input = '''Class __{Var $_ba:Array [Array [Array [String ,07],0B1],05];Val _:Array [Array [Array [Int ,0b101010],0x55],012];Destructor (){} }Class _1{Constructor (Wg:Array [Array [Boolean ,0X2D_7A],0X1];_:Array [Array [Boolean ,5],06_1_4];g,_,_8,M:DT){}$3(){Val b_,o:_6;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1231))

    def test_1232(self):
        input = '''Class __{Val $__7_:Float ;t1(__,I6__,Gv_,_c_,_0_:Float ){} }Class _:__G8{}Class _3{$L(_,T9,_:Array [Array [Array [Float ,043],0B1100],0xE6_3_7_7]){}Var GW:String ;}Class _X__:_{Constructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1232))

    def test_1233(self):
        input = '''Class _____{Var G7,Qd_:Array [Boolean ,0X8];}Class ___:_{Constructor (t,Hq,_,_Ng,I4:i_87;g7D:Array [Array [Array [Array [Array [Array [Boolean ,13],0x8],0b1],0B1011011],0X8],13];n5_K:Float ){} }Class L{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1233))

    def test_1234(self):
        input = '''Class _6:_p24{$0(p,Q39_,b_,cBc,B:v5){} }Class T:C_k{Val __0:Array [Array [Array [Float ,2_315],72],020];}Class KO:_2_{$_4_1(){ {} }}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1234))

    def test_1235(self):
        input = '''Class U{Var $_,_T_K:Int ;Val $_0,f,$m,$u__,_:String ;Var pX,$e,C_8:Array [Float ,63];}Class sq{}Class __:_f___{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1235))

    def test_1236(self):
        input = '''Class J{Constructor (__,__,_,L_E,_,F:e;_37:Array [Array [Array [Array [Boolean ,49],06],061],033];_:g___p21ZK){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1236))

    def test_1237(self):
        input = '''Class O{}Class _:_{Var $8F__x2,$7_A,$__B8_Tn,_,B__:F__12;Destructor (){} }Class D_:_{}Class f{}Class _6__L1:_5_{}Class _2_Nl{Var ___f,$3_:Float ;}Class H{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1237))

    def test_1238(self):
        input = '''Class O{Var $_,$_40:Float ;}Class _{r(_x:_;k,_f,y9:Boolean ;_:String ){}Destructor (){Var _3:Array [Int ,0B1_1];Val mV2:yR;} }Class s_:e58_{}Class J5{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1238))

    def test_1239(self):
        input = '''Class H:t{_(_es_7:Array [Boolean ,6_5];_,X_Q:e){} }Class S4{}Class _{Constructor (){}Constructor (){Continue ;} }Class B:S{}Class T{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1239))

    def test_1240(self):
        input = '''Class Z:_{Val _,k0:Array [Array [Float ,0X5_C],025];Destructor (){Break ;}Constructor (J,gvb,t:_){_Z::$__a();}Var $f0_,N9z,_,$_,_,_:Array [Array [Array [Int ,0b1111],06_72_2],0XA];o8y(X:Array [String ,25];_y,_h:SC;k:Int ;___:String ){}Constructor (){}Constructor (){ {} }}Class _:t{Var $11:Boolean ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1240))

    def test_1241(self):
        input = '''Class ct0{Constructor (_5,_i6_F,n:Array [Boolean ,0xA6]){}Val a__,__:Array [String ,0b11111];Var $iVU:Array [Array [Array [Boolean ,012],05],012];Constructor (ywC:Array [Array [Array [Array [String ,8],012],0X9],07]){}Var $_:Array [Array [Array [Float ,8_4],064],0B11];Constructor (m_,_i,G:_){Return ;} }Class K__c:rv2F{}Class _{Var _:Array [Array [Array [Float ,75],75],041];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1241))

    def test_1242(self):
        input = '''Class v__t:W{}Class K5_{Constructor (w0,N:h6;V_,_,_,_:Array [Int ,0b11]){}Var o:Array [Array [String ,0x17],01];}Class e{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1242))

    def test_1243(self):
        input = '''Class gg{$_(___022:Array [Array [Array [Array [Array [Array [Array [String ,052_2],2],2],0B1],0B11001],0X26],076]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1243))

    def test_1244(self):
        input = '''Class vqX:_cZy52__{}Class _{}Class _{$1(_:Array [Boolean ,033]){} }Class __1:__{_(_L:r8;_,_5:Int ){Continue ;Val h:Array [Array [String ,07],6_3];Break ;}$84(_:Array [String ,0xB];m_:J;_Q_,ZG6:Array [String ,76];_1E:Array [Array [Int ,0b1010100],76]){} }Class E{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1244))

    def test_1245(self):
        input = '''Class _{Destructor (){_::$6o();}Constructor (_:Int ){} }Class _U{Destructor (){}Val $_:Int ;Val $4qa:Array [Float ,0B110111];}Class B{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1245))

    def test_1246(self):
        input = '''Class q_{Var _JZ8__:Array [Array [Array [Array [Array [Array [Array [Int ,0b1_0],74],0b101110],070],0b1],0B1_01],0B1];}Class _:U_{}Class __{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1246))

    def test_1247(self):
        input = '''Class z_:_{Val $2,_g,Z_,$3LkV,_,rE,s,_B1:Int ;Var $_,x,$_,$_Ah9,$6,_:_;$83_n(){}I(__,p,n:Float ){Break ;}Constructor (){Var b:d;} }Class _{Constructor (__W0,_,_:U){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1247))

    def test_1248(self):
        input = '''Class _4{Val __:Array [Array [Array [Array [Array [Array [Array [Boolean ,0b1001101],0X6],07],8],0B1100100],0B1100100],0B1100100];}Class T{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1248))

    def test_1249(self):
        input = '''Class z:_r_{Constructor (_:Float ;_,e6:Array [Boolean ,057];V4:Array [Array [Array [Boolean ,033],0b1100001],057]){Var o_,_:Boolean ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1249))

    def test_1250(self):
        input = '''Class vp3{}Class _:_{Constructor (f:String ;z:Int ){} }Class f5:_{Constructor (){} }Class __{}Class _:Y{$W_(_,_1_R,r:_F;A:_;_5,O,E:_){}Val V_:_tv_;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1250))

    def test_1251(self):
        input = '''Class _4{Val v:Int ;}Class W{_(L_,___4:Int ){}Destructor (){}__(u__3__4m:Array [String ,0xB];_,bT_H2,_,o:Float ){}Constructor (mr,_j:Int ;_:_3B){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1251))

    def test_1252(self):
        input = '''Class S{Constructor (_:foe_8;n:Array [Array [Array [Array [Array [Array [Array [Array [Boolean ,0b110000],73],0B11],0xC4_1],03],0x7],0X37],036];P:Array [Array [Array [Float ,036],0X37],7]){} }Class __5{}Class ___i{}Class i7{Var $_2:T4h_;}Class _{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1252))

    def test_1253(self):
        input = '''Class _372:O{r(){Var Z:B;}l(x_8:Boolean ;_9__5lNH_,_7,G42,_5_:Array [Array [Array [Array [Array [String ,25],0xD],05],25],0x18]){} }Class _:__{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1253))

    def test_1254(self):
        input = '''Class e3_1{}Class _{}Class _:_75{Var $r_:Array [Boolean ,024];$__(){}Var $_,$_,$_:_;Destructor (){} }Class _:__79{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1254))

    def test_1255(self):
        input = '''Class _:_{}Class _:_0{}Class w:X{}Class __{Destructor (){}Constructor (_:wu){} }Class k{Var $_:Float ;Var _6,_:Float ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1255))

    def test_1256(self):
        input = '''Class E4:___{Val $m3,K_43:Array [Array [Array [Array [Array [Int ,0X5_E],0X46],0b1010001],13],0b1010001];Constructor (_L_,p,Pk_B3:Array [Array [Array [Int ,0b1010001],13],13];__:String ;c__,_:Array [String ,0116]){} }Class Pe_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1256))

    def test_1257(self):
        input = '''Class L{}Class _bgx:_{}Class _{Destructor (){}Val $8:Int ;Val $7609__2__:Boolean ;}Class Mv:P6{Val y3I_,$Q2,$2_,_s,$3_:Array [Int ,0b1100];}Class _:Dh{Constructor (_:Boolean ){} }Class P3{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1257))

    def test_1258(self):
        input = '''Class _:J{Constructor (B0,x4_:Float ;i:Array [Array [Array [Array [Array [Int ,0X3],17_1_76_7],9],040],0x4A]){}Val _,_,$4:Array [Float ,0B1];}Class L:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1258))

    def test_1259(self):
        input = '''Class xOn:F_k_S{}Class _:_{}Class r_4{Var $__sv9R,____D,$D__7_o,$1,B6,X,$CZ_,$_,I_,$1:_;Var H89_:Array [Array [Int ,016_5],0X46];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1259))

    def test_1260(self):
        input = '''Class __{Constructor (_8:Float ;Bo:Float ;z_,X,_,rer,_4:__1;_84:String ;rX,S9__3:String ;R:Float ){} }Class J:_75{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1260))

    def test_1261(self):
        input = '''Class E__{Constructor (_,_,_:Hf){}Var $_9:Float ;_7_Caq(){}Destructor (){Break ;}Val $7__:Float ;}Class u_C:_6BH{$r(_:Array [Boolean ,0X4D];h:Array [Float ,062];__:Array [Int ,03];_0o___0:String ;_,o:_9_){}Constructor (){} }Class U:i2{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1261))

    def test_1262(self):
        input = '''Class r:v{}Class _{Var $3:Boolean ;Destructor (){}Destructor (){}Destructor (){}Destructor (){}Constructor (_f,_,M1,X,_Ka9,_,O__,_,_w:Float ;_:_jC){Val _:Float ;UC_E::$1();} }Class _Y7:z{}Class n_:r7{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1262))

    def test_1263(self):
        input = '''Class _UG{$_(_:Array [Boolean ,55];F084,I:Array [Array [Boolean ,7_4_8],1];Y4,_,F_,x:m_;_9,_,s6p8:Float ){Continue ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1263))

    def test_1264(self):
        input = '''Class _{}Class kGV__:b{}Class _:_{}Class VQ{Val $6_,C:Array [Array [Int ,0B111],05];}Class vT1{}Class l{}Class w{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1264))

    def test_1265(self):
        input = '''Class _9{_6_(p:G1;_:Array [Int ,07646];X___37:Float ;A:Array [Array [Array [Array [Int ,0X27],0x14],01],065];_:Array [Float ,0B111011]){Val p3_,d45,U,_46,H_:t__;}Destructor (){Continue ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1265))

    def test_1266(self):
        input = '''Class _{}Class w{}Class _yC_:_{M_1__(_:Boolean ;_T__03,y:_;_,_lhgw,Gn:Array [Boolean ,0B100001]){Return ;Break ;_::$_();} }Class _:p{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1266))

    def test_1267(self):
        input = '''Class _{}Class b:_{}Class _{Constructor (U2HT_zW___:String ;S__q,R:_8){}Constructor (n1,_:_){OdL::$_();} }Class ER{_3(_F:Int ;_,_0_6__,w,_:Array [String ,0131]){} }Class BO{}Class _:U__{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1267))

    def test_1268(self):
        input = '''Class f{Var b,h,_3,KK8_nae5:R4;}Class __:__{$U3(_:_){Val n_2:Int ;}Constructor (_:i_){Break ;Return ;Break ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1268))

    def test_1269(self):
        input = '''Class h90___:_{c___(B_:Array [String ,0137];XU_,_:Array [String ,0xF]){}Destructor (){} }Class _6_S__:_y{Destructor (){Var p,_W_2JO:Array [Boolean ,38];} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1269))

    def test_1270(self):
        input = '''Class _:i{Constructor (__:M_d){} }Class s6:_{Val $6,$z,$P:Array [String ,6];Var $H,__2_w:Array [Boolean ,06];}Class _{Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1270))

    def test_1271(self):
        input = '''Class _84{Constructor (){}Constructor (z,R:__){ {}Continue ;}Val _gQ_:Boolean ;Constructor (w:Array [Array [String ,03_337],73]){}Var $_,$v_ly,$_:F3;}Class _:S{Val $Z,__z:Array [Array [Float ,0337],9];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1271))

    def test_1272(self):
        input = '''Class _:L__{Var _:Array [Array [Boolean ,0b1000010],0X14];}Class b_2{$6_(){}Destructor (){} }Class y_2{}Class R{Constructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1272))

    def test_1273(self):
        input = '''Class _:K{}Class _{Constructor (_,_1:String ){}Constructor (){} }Class p5_:d1{}Class _{Val m6,$37,_:Boolean ;Var $V:f;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1273))

    def test_1274(self):
        input = '''Class J{Var _:WH;}Class Y_31{}Class F8:U{}Class qf6n:n{Constructor (_:Int ){}Val g:String ;Constructor (){} }Class _{}Class m:m{Val W2a7_6:Array [Array [Array [Array [String ,0x3],0b1],6],0x5];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1274))

    def test_1275(self):
        input = '''Class _:_{$_Y(__2:OM;w,_:Array [Array [Array [Array [Boolean ,0x1A],05],0b101110],0142];D:Array [Boolean ,0142];_XN9:String ;m,_:String ;__,nl,Fh,Z:Array [String ,0x1A];u,L:K5w;_,_:Array [Float ,0XA_6_5];E,h:H__j9){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1275))

    def test_1276(self):
        input = '''Class _{Var $9r,_:Array [Array [Array [Array [String ,0x3_8_0],20977_0],8],0117];Constructor (){Var y__b:_;} }Class b1_{Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1276))

    def test_1277(self):
        input = '''Class e:Q{}Class g0{Val _,$5:Array [Array [Array [Array [Array [Array [Int ,0X41],0b100011],0x90],30],30],30];Destructor (){}$5(){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1277))

    def test_1278(self):
        input = '''Class Z:j4r{Constructor (T:Array [Array [Int ,0x5_9_6],0b10001];Q2,__6_:Array [Float ,4]){}Var X,$5,$_:Array [Array [Boolean ,02],0B1010110];}Class _:Uh8l{Var $8:Array [Boolean ,0b1_0];Val ___7__:__;}Class _:_{}Class _E{}Class R:e1{Val _L:Float ;Constructor (_QOd:Int ;_:Array [Array [Array [Array [Array [Float ,0B1010110],02],0B1],11],5_9]){Continue ;} }Class __{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1278))

    def test_1279(self):
        input = '''Class u{}Class s{Constructor (__1:o4I__){Break ;}Destructor (){} }Class _{}Class __:XQ{}Class _uX{Var _b,M653_n5QN_,$41:Array [Boolean ,0B1011011];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1279))

    def test_1280(self):
        input = '''Class __:_{Constructor (XM:Float ;_1,H,_8,f9A,w4,KvRgw_U,of,y_0_o__0P,_,_,_,h9:_;c_,R_mN:Array [Float ,0x29]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1280))

    def test_1281(self):
        input = '''Class q0_8:v{Var $1:_;Destructor (){}Val $_,$8:String ;}Class B__{}Class FQP6:A{Var $71,_L_:Array [Array [String ,0XB01],7_2_5_1];}Class _{}Class _:_{}Class _:S{Destructor (){} }Class _{Var $s_h_,_4,M:__E_;Destructor (){Break ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1281))

    def test_1282(self):
        input = '''Class W_:k_{__(_:g;__6,_8e_,__2I:Array [Boolean ,21];l:Float ;Ih18:Array [Float ,06];_,kYd:_P){Break ;} }Class ___:l{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1282))

    def test_1283(self):
        input = '''Class _:l6_55{Constructor (f_:Array [Array [Array [Array [Array [Array [Array [Int ,0123],0b10000],0b10000],0B10101],0123],0X3_D],0X13]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1283))

    def test_1284(self):
        input = '''Class i0_:_{}Class k81{Constructor (_V_Xir,_0:Array [Float ,0b1]){}Var jO,$__l:Array [Array [Array [Array [Int ,03],0141],41],0X2];}Class _:S{Var _:Float ;Constructor (__,__,x_:J){} }Class _{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1284))

    def test_1285(self):
        input = '''Class _j4:P_{}Class _:__3_{Val ch,_5:Array [Array [Array [Float ,0143],26],0143];}Class yvg7___{Val w9b5_,B:Array [Boolean ,0x2];Var _A:Array [Float ,03];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1285))

    def test_1286(self):
        input = '''Class i:Qg{$k(OS,__,__,iN,__w:Array [String ,0b111110];_,_d,J,_:Array [Array [Array [Int ,0x269D1_8_0_3_05_3],0110],1_3]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1286))

    def test_1287(self):
        input = '''Class _2:w_x{Constructor (z:_;__:Array [String ,6_7];__:Boolean ;__:Array [Array [Array [Array [String ,52],0b1_1],0114],0B1]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1287))

    def test_1288(self):
        input = '''Class j3:H{}Class _{Var $_79:Array [Array [Array [Array [Array [String ,36_1],074],0B1_1],074],0B1011011];Destructor (){Val g:_;}Destructor (){} }Class y:S{}Class e{Var $0:Float ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1288))

    def test_1289(self):
        input = '''Class hA{}Class J{}Class YT{}Class _:DG68_{Destructor (){}Val _:Array [Int ,06_5_6];Val __:Array [Array [String ,22],0B1001010];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1289))

    def test_1290(self):
        input = '''Class a{Var _g_,z:_;}Class _6{Val $_:a;}Class U{Val _,$__:v;Val _,_9,$u:Boolean ;}Class kC:__{Val Vbx,$_3_79P6__9:T;}Class _{Constructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1290))

    def test_1291(self):
        input = '''Class T{}Class ____v{_(){Val x9A0:Array [Array [Float ,0B1_0],8];_5::$8_7.quX_();}_(_W,Hp,HG:Array [Float ,0b1110];M:Float ){}Val _b,T__1:Array [Array [Float ,8],8];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1291))

    def test_1292(self):
        input = '''Class f:_{Var tO,_Y26_,_,v,Nz___S:c_K;Constructor (_n:Array [String ,070]){}Var $6Lb,_,T_p,_Bl_,$v:Array [String ,0b111011];Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1292))

    def test_1293(self):
        input = '''Class P_:_i{$bS_ui(){Return ;{} }$_H(){}Var v:_;Constructor (_,_,p6_H_,K,s:Boolean ;_:Array [Array [Array [Array [Array [Array [Float ,66],02_3_6_7_2],01],97],66],0B1100010];_:Array [Float ,075]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1293))

    def test_1294(self):
        input = '''Class _{Var $_8N,n4,$W,$8,lA_,$_:Array [Array [Array [Array [Float ,0b1],0B1100001],0B1100001],0xF];Constructor (){ {} }Destructor (){}Destructor (){Continue ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1294))

    def test_1295(self):
        input = '''Class O9_5o{}Class _{}Class V{Var _Q_,_v,Y:Array [String ,0b11];}Class M:h_GM_{Val _190,__P:Array [String ,020];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1295))

    def test_1296(self):
        input = '''Class Sa_{_G1(__2,u,V0:HB;_:String ;_:Array [Boolean ,0X3_0_A]){Var _Q_:Boolean ;}Destructor (){}Val $_bC,$_:Array [Array [Int ,91],0137];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1296))

    def test_1297(self):
        input = '''Class __6_{Val _3_4A,$1,R0:Array [Array [Array [Int ,0B1010101],1],03];Constructor (){}Constructor (_:Array [Array [String ,2],03];_F,R_,t:f){}Destructor (){}Val $5:Array [Float ,0b1];Var $d:_99_;}Class _q_:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1297))

    def test_1298(self):
        input = '''Class N{}Class _:j{Destructor (){} }Class _:_7{_8(b:Array [Boolean ,0XD];_,z:F;_,_4:Array [Float ,87];M:Float ){} }Class __:X1_{}Class q298I_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1298))

    def test_1299(self):
        input = '''Class _C:E9{}Class y_42_:E_515_{Val h__LiE,$_,U4_7O2d:Array [Int ,0X9];Destructor (){Val _X4,_28,J7F:String ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1299))

    def test_1300(self):
        input = '''Class L:_{_(_:_6){}Var _:Rn5;}Class _0_:_{}Class _l_1:_4_{Constructor (p0,a__:Array [Array [Float ,0125],0125];S3:_){} }Class ___h{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1300))

    def test_1301(self):
        input = '''Class f:_{B_(_,_,S:Array [Array [Float ,15],0B110]){Break ;}Var _,_,$8g_237,___rM05A_,$JBc:Z;}Class _O{}Class G{Var u0,$Z:Array [Array [String ,0b111110],0136];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1301))

    def test_1302(self):
        input = '''Class a:Ro{}Class _T:_{Var $9M,$2H:Float ;$F4(){}Var _7728,$A7:Array [Boolean ,01];}Class H_{}Class bu_:_{}Class m5Tl_:F__{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1302))

    def test_1303(self):
        input = '''Class _n_:A{}Class Q__8{Constructor (j:c;_,__,mU_2,G,_:String ;I86vO:Boolean ){ {} }Var _9W,_:g4_;Destructor (){}Constructor (){}$E(__:H3U;YY,_,A,ry_4__:Array [Array [Array [Float ,0XB],86],0x21_C49_A];_:Array [Boolean ,0b1];___:Array [Boolean ,0x38]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1303))

    def test_1304(self):
        input = '''Class C__:_h{}Class _{}Class B{}Class _:_a{Constructor (_:Array [Array [Array [Array [Array [Array [Int ,6],0X2B],0xF],0X2B],065],0x4B]){_::$6();} }Class R_{Constructor (_:Float ;i,_,__:String ){Return ;} }Class D{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1304))

    def test_1305(self):
        input = '''Class _g_:C{}Class K:_3{Constructor (c,D__,_0_:Boolean ;Z62:Array [Array [Int ,0140],0140];_:Array [Array [Boolean ,03],104]){ {} }Val $2,$_:B;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1305))

    def test_1306(self):
        input = '''Class _{Var _4:Array [Array [Array [Array [Array [Array [String ,0B110_111],060],0X27],01],1],5];Val p,M,_0:Array [Float ,0X3_B5_DB];$_8F(){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1306))

    def test_1307(self):
        input = '''Class KZ95G{}Class ju{$p(_,B,H,R_A_4:Array [Array [String ,0x7],01_56_6]){}Destructor (){}Constructor (){}Var _,B:String ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1307))

    def test_1308(self):
        input = '''Class _{}Class __m{Destructor (){} }Class _:_{}Class _:_{$_(_,xE:Array [Float ,0b1000001];_1:k;__01:Float ;XV4,_,_88,c:Array [Array [Array [String ,0B1_1_111],8_3],01_7_7_5]){} }Class r9{}Class LP:P4_5I{}Class _:QS4_{}Class C_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1308))

    def test_1309(self):
        input = '''Class z9:_x5{Val lS_9_:RJ_Q;Val $_:Array [Array [Array [Int ,0B100_0_1_11_1],0B1011],58];}Class _:__0884{}Class K_:u{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1309))

    def test_1310(self):
        input = '''Class U{Destructor (){}Var _9Dyu85,$_:Boolean ;$9_k(C:Boolean ;_,__:Array [String ,0b111011]){}$Xq(_8:Array [Array [Array [Int ,0b1],0B1],030];Uf:Array [Array [Array [Int ,02],0b111011],030];_,Y,s_:Boolean ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1310))

    def test_1311(self):
        input = '''Class __:d5_99___{Var $_nn:Array [Float ,0x7];$A_(_:EJ_;_X_,_,_,_9,__I_4:__A_4){}Destructor (){Return ;}Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1311))

    def test_1312(self):
        input = '''Class _{Val $9y1_4__,$o3:Array [Boolean ,047];$_(_89E__J2:Boolean ;_:__;K933O,_:Boolean ;_:Boolean ;H_2:Dq_){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1312))

    def test_1313(self):
        input = '''Class _{}Class _g:SY{}Class _{Destructor (){Var t,s:Array [String ,0b1100001];}Var i:Array [Array [Float ,02_2],0100];}Class r{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1313))

    def test_1314(self):
        input = '''Class _{}Class _:_{_9(k33:K;CT_w,Y_,h_7u_,r:Array [Float ,0b10000]){}_(){} }Class _{Constructor (Y,I6:Array [Float ,03_6]){}Destructor (){}Var _:_d;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1314))

    def test_1315(self):
        input = '''Class _{}Class _pz:O_{}Class _{}Class R___:l8_{Destructor (){} }Class _:M{Destructor (){}_1(){__4::$_p7();}Constructor (){}Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1315))

    def test_1316(self):
        input = '''Class _:_{}Class _70{_s15(_,_E,_,w54,_:Array [String ,0X14];S5,G:Array [Int ,032];_:_f){Val _:Array [Boolean ,59];}E2(){ {} }$S(){}$Z4y_(){} }Class _7:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1316))

    def test_1317(self):
        input = '''Class _{}Class z__:_{}Class _:_{}Class __5{Destructor (){} }Class _7_:_{Var $5:Array [Boolean ,0xF];Destructor (){Continue ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1317))

    def test_1318(self):
        input = '''Class _3{}Class _54:iAt{Constructor (){Val _7:Float ;} }Class H{Val $9:_59;Q(_:Array [Array [Float ,01],0X4D];l,W:Float ){Continue ;Continue ;}Constructor (z_:Int ;_u_e,X_4:Array [Array [Array [Float ,7_6],0X4D],79]){} }Class _h{$_7(u6:Boolean ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1318))

    def test_1319(self):
        input = '''Class b1:Pm6{Constructor (_:Array [Float ,5_9];_0:Float ;_:Array [Array [String ,075],0xD];d,_:Array [Int ,72];_k:String ){Return ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1319))

    def test_1320(self):
        input = '''Class r9:_{}Class C9{}Class _:i{Var $e_o:Array [Boolean ,0b11_1];}Class _:_0{_842(k:String ;eh,_,a_,_:Array [Boolean ,0143];x,_eo,_,M15,_5c_,Xt,_W,_:String ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1320))

    def test_1321(self):
        input = '''Class t{Var CFj,$_,$K:Array [Array [Array [String ,07_563_225],07],05_4];Var T,_,$2:Int ;Constructor (){} }Class _:__{}Class j7{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1321))

    def test_1322(self):
        input = '''Class _K_{}Class lD:g_Y{}Class q:_7{Destructor (){}Val $_W,$h09,$__9__,l:Array [Array [Array [Array [Array [String ,070],0B1000],0XC],19_11],0B1000];Var $__MG:Array [Array [Float ,0b110101],8_58];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1322))

    def test_1323(self):
        input = '''Class s{J6_k(_9:_2;r_,R__:Array [Array [Array [Float ,9],035],0b101100];M4,B41s_,S:Array [Array [Boolean ,0X1],03_12];g:String ;W:Boolean ){}Var $9N,$8,$P:Float ;$_z(){} }Class _k_1{Destructor (){} }Class d__:h{Val CL1,$_:Array [Int ,0X4C];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1323))

    def test_1324(self):
        input = '''Class _{Destructor (){Val _1:Array [Array [Array [Array [Array [Int ,067],37],0b1110],0B11000],02];{ {}R::$69_();} }}Class M{e00(_:String ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1324))

    def test_1325(self):
        input = '''Class kb{Var $60:Array [Float ,07_61];Constructor (_:__;UmX:__x87s_8z){Var _573,_:Array [Boolean ,0b1];} }Class p:A{Constructor (_,HI:_;__5:V;_,r_7H,_D:Array [String ,7]){} }Class f:_{}Class h7X:_{Var _,_:_;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1325))

    def test_1326(self):
        input = '''Class l_:l6E{}Class B6_{Val $_O:S;}Class I:m{Destructor (){}$97_p_(_6F:Array [Array [Float ,72],0b111010];v,_:Boolean ){ {} }}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1326))

    def test_1327(self):
        input = '''Class s{Var _E_Nm:Float ;Var $4,$___,_6,$9Yo:__0;Val $_,$96:_1_l__M;_(C,f:Array [String ,6_1];_5,k2,_:Array [Array [String ,44],0B10];__,hf_____y5F:_;u:Int ;V_:Array [Array [Array [Int ,48],02],44];Mj91a:V___;_:r_;_:Array [Int ,4]){} }Class Y1:R{Val _:String ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1327))

    def test_1328(self):
        input = '''Class _:_{Var _x:Array [Array [Array [Boolean ,0x9],0xC],0X5];Constructor (C,_,x,lf:String ;R:String ){}_(s,U,_9:Array [Array [Boolean ,07_0],0735];c_:_){Break ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1328))

    def test_1329(self):
        input = '''Class B_{}Class _{Var $_:Int ;Constructor (){}Var _,X:String ;Val $_,B,$_G_,$9N4I0T,$_,F_w:Array [Boolean ,0B1000110];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1329))

    def test_1330(self):
        input = '''Class _{}Class d_:_{Var E:Array [Array [Array [Float ,0x16],6],27];Var B_,$_7_u,$v:Array [Array [Int ,27],0b1_111];}Class Iz_:_{Val $_:G;}Class _v0{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1330))

    def test_1331(self):
        input = '''Class N7Ow{Constructor (){} }Class _{}Class _{Constructor (Uka:T1__J;v:Float ;B,_:_;__5:String ){Return ;} }Class D:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1331))

    def test_1332(self):
        input = '''Class E{Constructor (U:U7;_:Array [String ,0b100001];_0:String ;C,__8,_9:__ZB_;E:Array [Float ,0B1_0]){ {}Continue ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1332))

    def test_1333(self):
        input = '''Class _:g_C{Destructor (){} }Class A7{Var $03:Int ;H9(N,h71:Array [Array [Array [Array [Array [Array [Array [Boolean ,1_5],92],87_1_22],0X3_B_B_1_2_6D],0103],03],0103]){} }Class L{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1333))

    def test_1334(self):
        input = '''Class x:_{Constructor (___:Array [Array [Array [Array [Array [Int ,0X3],0b10001],74],7],74];_,O_D:__;Y,n1:Int ;_5,_:_){Return ;}$Z_(){} }Class kQb:__{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1334))

    def test_1335(self):
        input = '''Class LDs:_6{Val u7m_:Array [Array [Array [Array [Boolean ,0x1],0X1D],70],4_3];$0(_,_,n,OAme_2:Array [Array [Boolean ,07_2_6],0B11011];__p,_8_:Int ;J:Int ;_rFA,_mB:__9;__8_,q06,L,__6:Array [Int ,0XE_C_F_3];P6,_mbK:Boolean ){} }Class _24O9r{}Class L{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1335))

    def test_1336(self):
        input = '''Class w{}Class F5_{Constructor (_:Array [Array [Array [Array [Array [Array [String ,4],03],0B1],0b1001100],0B1100],4];S:String ;E:String ;F_I7p_5:_6;b6_97:Float ;_0:Int ;X,rd,G:M){} }Class K_:_o{Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1336))

    def test_1337(self):
        input = '''Class z0{}Class z4c{}Class L:_{Constructor (_:Boolean ;_5_:_;_64,_:Array [Int ,01]){Break ;} }Class __V:_{Constructor (_0:String ){} }Class I:w{Constructor (h,_:Array [Boolean ,07]){}Var _:String ;}Class _{Val $__q:String ;Destructor (){} }Class RV:_{}Class S1vm:__{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1337))

    def test_1338(self):
        input = '''Class eN__1{}Class y_{_(){ {} }Constructor (_8GV:Boolean ;_a79:Array [Array [Array [Array [String ,04_6_2],0X45_4],0B1000110],1];_,P3:Int ){} }Class L{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1338))

    def test_1339(self):
        input = '''Class _Bd{Constructor (g:Int ;_:Boolean ;O,v_k,y:Array [Int ,0121];_0Cv_8,_,P4mF5Nv5:Array [Boolean ,66];_:_;_,y:Int ){}Var $ZS_,$_:Array [String ,4];}Class _:_{Var $W,$G7_:Array [Array [Float ,531_6_8_21_2],0X2E];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1339))

    def test_1340(self):
        input = '''Class e{$7P(F3,p6,DB_5,___,eZ_:Array [Array [Array [Array [Boolean ,0x79A],07],0B10110],1];V:g_;___,_,E:Array [Array [String ,0x48],0xA];x06:Array [String ,8_55];__,_,_,_tN,N__,h550,_,_29:Array [Array [Array [Float ,0x48],0X6],0B1]){Break ;} }Class _{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1340))

    def test_1341(self):
        input = '''Class _1{Destructor (){} }Class _z6c0_U{}Class _{Constructor (_C:Float ;_,FM:String ;_,S,_6,_5_,_,_:Array [Array [Array [String ,015],0X68_3_4],48]){} }Class d_r:___36fn{Destructor (){}Constructor (_,B:zR){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1341))

    def test_1342(self):
        input = '''Class _:_{}Class e_0_:RN_{Var $_l6:Array [Boolean ,0XE_08F_E];Destructor (){}Constructor (){} }Class e2:Ff7P{}Class _1:_1{_b(a:f;_,d,_,sB:_;Q:Boolean ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1342))

    def test_1343(self):
        input = '''Class __d:n{}Class s1_7:__6{Val $o,_b:Array [Array [Array [Array [Array [Array [Float ,0106],2],0xB],0XD],0b1001111],0b1_1_1_0];Val h:Array [Array [Float ,0b1001111],0b1001111];$96M(){Continue ;} }Class _5:_cM6{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1343))

    def test_1344(self):
        input = '''Class m{}Class _{Var $__L:Array [Array [Array [String ,0B10101],2],020];$g(W,R8_:Array [Array [Array [Float ,57],07],0b1]){}Var C,_:jLw;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1344))

    def test_1345(self):
        input = '''Class u53:C__{Val $2:W;Var $25N:Array [Array [Array [Int ,22],0X56],0xF_4_E_C_E];}Class F2:_{Var $_,_8B4J,y3,n_:Boolean ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1345))

    def test_1346(self):
        input = '''Class _:UO{}Class c:_I{}Class S1F{Destructor (){Break ;} }Class _5:_{Constructor (_Z,_P,Q_:Array [Array [Array [Boolean ,0B1000100],0x9],0X5]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1346))

    def test_1347(self):
        input = '''Class _E9{Constructor (qP7_3:Array [Array [Array [Array [Array [Array [Array [Array [Int ,01],0b1010000],0X20],0X6],0B11],0b100],8],0xF_AB];_q56:_){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1347))

    def test_1348(self):
        input = '''Class N:_{Destructor (){} }Class p__:ZhRw_5{Destructor (){} }Class __:_1{Var S,$4,w_,$432A:Array [Array [Array [Array [Boolean ,05],0X4_7],0b111111],07];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1348))

    def test_1349(self):
        input = '''Class _:M{}Class _{}Class l:_4_i_{Var $2,$_,$_17:Array [Array [Array [Array [Array [Int ,0B1_0],0b1_0],97],01],0x9];Destructor (){}$p(){ {} }}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1349))

    def test_1350(self):
        input = '''Class _pQ:n{Destructor (){l_V_P30::$_();Return !!!--_::$72Oe99.__._--k::$9_u7F()._();{} }Destructor (){Return ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1350))

    def test_1351(self):
        input = '''Class _:_{}Class z9_7{}Class __{}Class t:P{}Class _{}Class _S:_kY{Val f,$6r,$N__4_,$E,j,$__4,$4:_;}Class _:Z{Var $Z3,$_,$Ln2,$jC_,x_,__3u:Array [Array [Array [String ,0X51],0123],89];Val $t:Int ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1351))

    def test_1352(self):
        input = '''Class I{I1(_4:Float ;_3:Array [Float ,0B10];Y,ue:Array [Array [Float ,5],0131];___,_,G,z1:Array [Array [Int ,4],20];_:Array [Array [String ,20],0B1];_:Array [Float ,2]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1352))

    def test_1353(self):
        input = '''Class O:Vy_{$C(){} }Class SE:_4{Val R8r466_:Array [Array [Array [String ,0101],0x46],0b1];}Class Wy:_{}Class _:p{}Class _{Val $S_,$_:Int ;$_(){Continue ;}Var p_,$41D_k_,$6:_;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1353))

    def test_1354(self):
        input = '''Class _1{_(KW,_5K_,O_,C:String ;_2,__,_4K,___Y__,_l:Boolean ){}_(_E,J____o,_:Array [Int ,027];_,suRa,_:J8){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1354))

    def test_1355(self):
        input = '''Class l{Constructor (){} }Class g:h_{Val $r_,_,$_,$_:Array [Array [Array [Array [Array [Float ,1],44],032],44],8];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1355))

    def test_1356(self):
        input = '''Class _R_n01n4__{o2kG(){}Val $e,$_,_:EN;Var $B_,$67:Array [Float ,94_7];Destructor (){} }Class nfF_:m{}Class K{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1356))

    def test_1357(self):
        input = '''Class __:_j{}Class b{Destructor (){}Constructor (U4Y_:Array [Array [Array [Array [Boolean ,0B10111],05_1],0b1010011],05];__:Array [Int ,5]){}$_(){} }Class _{}Class S:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1357))

    def test_1358(self):
        input = '''Class _9B{Var hR3,_,$_0_:K;$6EaS2_(te:Array [Boolean ,0x1E];_C_m:_){Continue ;Break ;Break ;}Constructor (){}Destructor (){Var X,vP0:Int ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1358))

    def test_1359(self):
        input = '''Class O:__x5_Qf{}Class _4:_{_(Q_:___;_58ge9d_,_1,_G_,f:Array [Array [Array [Array [Array [String ,0xC_A],011],60],0xB9],0b111];h:Array [Array [Array [Array [Array [Array [Array [Array [Float ,60],0XD],01],60],05],011],0B110111],0b1]){} }Class l2:W_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1359))

    def test_1360(self):
        input = '''Class u:L_C8{}Class o29{Constructor (_:__){}Var $3p_,H,J,v6_,G3:Array [Array [Array [Array [Array [Array [Array [Float ,4],866],0104],0104],0104],01],0B1];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1360))

    def test_1361(self):
        input = '''Class I{$3___8__61w(_,l:Array [Int ,02_0_64]){}Var _,D9,$3,$Y:Boolean ;}Class G:b_H{}Class j{}Class __:s_n{_(Dv,_:b){} }Class d__:_10{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1361))

    def test_1362(self):
        input = '''Class X_2_5_:_{}Class p7:zm{}Class _:KGU_{Constructor (l_,_,R,g__V2_:Array [Array [String ,772],025];_:a_51){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1362))

    def test_1363(self):
        input = '''Class _:d{zi_(_eth,y,_035:Array [Array [String ,39],0B1011001];H:Int ){}Var n_,$67,_,$8,$__F__:Array [String ,073_12];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1363))

    def test_1364(self):
        input = '''Class __:_2A{Val $_z:Array [Int ,12];Destructor (){Val T,u__S_,_,A:__;} }Class _{Var q,j,$_,_5:Array [Array [Boolean ,0XE],0b1];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1364))

    def test_1365(self):
        input = '''Class I:_{}Class S:w{}Class _{Constructor (_S2,Be:Array [Array [Boolean ,623],0xF];_Vh:Array [Boolean ,26];p93__hD_2Ns9,_,s1M:Array [Array [Array [Array [String ,0x4B],0b111001],04_1],03_6];J,_L7:Int ;_,_8,_,z:Array [String ,0b1_1]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1365))

    def test_1366(self):
        input = '''Class _:O0r{Destructor (){}Val $E:_;}Class V8__{}Class k:Ds{}Class _n__:M{$n0(_1e,k_:Boolean ;rP,p_v:Array [String ,0x5_5]){Continue ;}Val $tW,$__,$_w4:_r;_(_:Array [Float ,0X5B]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1366))

    def test_1367(self):
        input = '''Class _:P{Val G7585__U:B;}Class _0ya:_f{_5s(){}u(_3jP_:_t;_p_CI:Array [Boolean ,0B100001]){}Constructor (){}Var $g:Float ;Destructor (){ {}Var v__m:QgQ1___;}Val $9_4,_w7O,$68:Array [Array [Int ,0B11],0xD];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1367))

    def test_1368(self):
        input = '''Class E_X{Constructor (y,_,J1k_,H,_:___;_:K_9;_j8j6_,_348,_,p7HF_:Array [String ,0676622_3];s,_HR8_:_){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1368))

    def test_1369(self):
        input = '''Class t0N{Destructor (){Continue ;}Constructor (g,O6_9,E_,D,L9_:Array [Boolean ,88];fY:_){}e(){}Var $5,__,$3:P;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1369))

    def test_1370(self):
        input = '''Class _:Bx7{Var __,_,_,$U,_7,$b,_,WoK,$91d:Array [Array [Array [Float ,06],61],0x5];Destructor (){Break ;Break ;Continue ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1370))

    def test_1371(self):
        input = '''Class _:H{Val j:Int =!-New n8E().MU1s_4();}Class _:_6__{Constructor (_:Array [Array [Array [Array [Array [Array [Array [Array [Array [String ,022],0b11],022],0b11],022],0b11],7],76_099],5]){}Destructor (){}N(){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1371))

    def test_1372(self):
        input = '''Class _:_{Constructor (__,_G,_,U012:Array [Array [Array [Array [Array [Array [Int ,0B101010],950_5],0B1],030],0xF6_89],030]){Break ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1372))

    def test_1373(self):
        input = '''Class A{$r(_:Boolean ;_:e_;_69,uyA,T,m:Array [Array [Array [String ,3],0b1],0b1];_i,o36__:_){} }Class T:d_{}Class _9{Var $i:Array [Float ,0126];}Class _:_{Constructor (_,_96,G2,_86n4:Array [Float ,0B110011]){Break ;Val e:Float ;Break ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1373))

    def test_1374(self):
        input = '''Class n{Val _,_3:Boolean ;}Class uG_:K{}Class ___:__2{}Class f58{Destructor (){Return ;}Var H:Boolean ;Var $1,t,$_Dl__L5_,$_P,_Q8,__:Array [Int ,82_2];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1374))

    def test_1375(self):
        input = '''Class _:_{Destructor (){}Z(f_:Float ;_0,_0,e,K:Array [Boolean ,04];X:_;_,H:Boolean ;n:_){Continue ;} }Class K:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1375))

    def test_1376(self):
        input = '''Class G{Var $8,$1_:Boolean ;Val __:Array [Float ,0X3A_C8_D_B];Var $_,$7:String ;Val $4,u:_;}Class _T8z_Ps:A{}Class _9:P_{}Class CZ{Val $_,$PR,$0P:gh;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1376))

    def test_1377(self):
        input = '''Class _Q_{Var $2a_:Array [Float ,0b1_0_0];Var _1,$5:z_AZA;_(){Break ;} }Class v6vAFn:_L{Constructor (k__,_,_,_:Array [Int ,0B111100]){} }Class _:Q{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1377))

    def test_1378(self):
        input = '''Class c{Constructor (pvU,w:_9gYS;N,_4:String ;_:Int ){}Constructor (){}Val _,_,Z,$9:_;Z(_92_,e:Y;_A_91:F_A){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1378))

    def test_1379(self):
        input = '''Class _{$_(__:Array [Array [Array [Array [Array [Array [Float ,0x23],0XF],0B10],1_4],077],0X7];U,V_9,w:oE){} }Class p:___b{Val e2,_:h;}Class _x{Var H2:Array [Array [Array [Array [Array [Array [Array [Float ,062],0B100001],7_753],75],0b111011],0B100001],0X7];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1379))

    def test_1380(self):
        input = '''Class _{Constructor (_,_:_6;_:S;_:Array [Boolean ,05];__:Array [String ,0X20];G,r:Boolean ;_z1:Int ;_5,j_Nq:___){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1380))

    def test_1381(self):
        input = '''Class _i{Val $283_:Array [Float ,0B100100];}Class __25:B{Destructor (){}Val F:Float ;Var p:Array [Array [Array [Array [Boolean ,46_99727],0B100100],0B1],077];}Class _{Destructor (){} }Class _0:M{}Class Y_:_{}Class u_:_{Constructor (){}Val $M,$9,$_:U_;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1381))

    def test_1382(self):
        input = '''Class b:N{Constructor (YR_,o_c:Array [Boolean ,4];f06_:Array [Array [Array [Array [Array [Array [Array [Array [Array [Int ,0b110110],041],0xE],051],0x4C],0x4C],0B110001],0b1_1],025]){Break ;}Var $_,K,$_,P:J7;}Class __RK{Val a:Float ;Var _3,$_,_,_,SYIz:Int ;Constructor (_:Array [Array [Array [Array [Boolean ,0b110110],0b1],0X5],53]){}Destructor (){} }Class dF_:c15_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1382))

    def test_1383(self):
        input = '''Class W:_1{Val $3_3_:Array [Array [Array [Int ,015],0x5],07_42];}Class NM:_{}Class _:H{}Class f:__{Constructor (o,_Nz:Array [Boolean ,0X2E]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1383))

    def test_1384(self):
        input = '''Class _:F_{$3(_G_S6:Array [Array [Boolean ,0B1],0B1]){}Val ___:Array [Array [Array [Array [Boolean ,0105],0xD],0b11011],0105];}Class _:e{Val $9:Array [String ,01];Constructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1384))

    def test_1385(self):
        input = '''Class j:___{}Class _{Destructor (){}Destructor (){} }Class U:p{Val Y,t:Array [Boolean ,0XC];Val __o,_:Array [Array [Array [Boolean ,0B101111],0xFC],0x5];}Class c:s52{}Class _{}Class _:_31{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1385))

    def test_1386(self):
        input = '''Class _{Val $3,_1Y:Int ;Val $1,$__v:Array [Array [Boolean ,0b1010100],94];}Class _:y_{Val _3_,_,$v:Boolean ;Destructor (){} }Class _v{}Class __R9_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1386))

    def test_1387(self):
        input = '''Class _:Ss0{$D(_i1,K_,m,LDI,S,a,_,t_,_:Array [Boolean ,0X13];_Y,_,D_,sj:t){p4o::$_J().w().f_3.I.Cs_O();} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1387))

    def test_1388(self):
        input = '''Class TQw_{Zo_9(_8:Array [Float ,89];t_,p_,_:Array [Float ,0141];Ot71,C,h:String ){} }Class _axX:c_{}Class _0R_wI:___2a4{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1388))

    def test_1389(self):
        input = '''Class u0X8E:q{Constructor (Q:Array [Array [Array [Int ,0B110011],0b10101],0x60];t,_,G:c;D_W,_9v,n,xjDD,_H,_:X;__1h,O5_,_0,_:Float ;r:Array [Array [Array [Float ,0x50],0B1],0134]){} }Class _{Val $9:Array [Boolean ,71];}Class __7E{}Class x_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1389))

    def test_1390(self):
        input = '''Class __8:_R_{}Class O:_{a5(k_x:Array [Array [Array [Boolean ,0x440_3_ACC7],02],44608231];W,_w,E,M_:Boolean ;H:Array [Array [String ,0X2],0b11];y_:Int ){}Var iTBq_:Array [String ,10];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1390))

    def test_1391(self):
        input = '''Class B5{}Class L{Constructor (R,H:Int ){}Constructor (V,_g:y;_:_;z,_4O2_T,I_i:Float ;B:J){}Val $b8:Array [Float ,01];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1391))

    def test_1392(self):
        input = '''Class M:__b{}Class _{}Class __:C636z4{Var __,$U_:Array [Array [Int ,0B1_0_1],04];Destructor (){Val _R:Boolean ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1392))

    def test_1393(self):
        input = '''Class y_6Sy8Q_:_{Destructor (){}Val b_P:__Q33;}Class _{Var $57x:Array [Boolean ,55];_(__:Array [Array [Boolean ,0B1],0X13]){Break ;Break ;Continue ;Continue ;}Constructor (_3_:Array [Array [Array [Array [String ,0X13],0126],050],03]){}Constructor (T_,_,P:_){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1393))

    def test_1394(self):
        input = '''Class T{Var $_gA:String ;}Class _:N{Val $_,g_,sl:dO_;}Class _{}Class __:___{Constructor (i_L___:String ){Continue ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1394))

    def test_1395(self):
        input = '''Class _{Val LT,_bC2,t8:__;Val h,___:Array [String ,0B1001110];A(){__::$7e8_().__();} }Class n{Constructor (_:iN_AD;H_k:Float ;_:_;g:_){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1395))

    def test_1396(self):
        input = '''Class M1_h__{Val $o:Array [Array [Boolean ,030],6];Var _7,$A_4s,f:Array [Float ,0X6];}Class B{Constructor (_,_62,G_,J,v:N;h:r){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1396))

    def test_1397(self):
        input = '''Class _:s{Y(){}Constructor (q,_:C22;_02:Array [Array [Array [String ,0x2F],06],4];o_i:VV__y;_,E,U:Array [Array [Int ,5_2],0142];Q:_){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1397))

    def test_1398(self):
        input = '''Class t{$__(){}y(){} }Class _:C{Constructor (){}Constructor (k_,_:Array [Array [Array [Array [Float ,0b10_1],0B111010],0x5_7],0b110]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1398))

    def test_1399(self):
        input = '''Class p7:_{Val $2n,$_,$8:Array [Array [Array [Array [Array [Array [Boolean ,06],0b110],5],0b111011],22],22];Val __:Array [Float ,05_75];$5(){}Destructor (){} }Class m:q{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1399))

    def test_1400(self):
        input = '''Class _L9:__{Constructor (kS_,__4_S_,_,_,W4,_3Of:Int ;z_Z,eV_:Array [Boolean ,0b11];_4:String ;_:Boolean ;KE_,_4u,_:Float ){} }Class _{Var $__,_:Int ;Var ___,$_k,i,Bw,_:_2;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1400))

    def test_1401(self):
        input = '''Class _{}Class __{Var $9i:Boolean ;Val _9,$1,$8:_1;}Class __:q{$_3_(Req_4_:Array [Int ,3_2_7];o6,KT_,_:Float ;E_d:_C;gXQ06,E:Boolean ){_y__::$F3();}Val $E:Array [Array [Boolean ,0B1],7];}Class A3:_{}Class _{Val f:Array [Boolean ,0X8];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1401))

    def test_1402(self):
        input = '''Class ___{Destructor (){Continue ;}Constructor (_k9_2:Float ){}Constructor (){Continue ;}Var _:w;Var $_Y3__:String ;Val D,$1:lK;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1402))

    def test_1403(self):
        input = '''Class _{Constructor (qZ_:Array [Array [Array [Array [Float ,59],0X22],0B10],59]){} }Class X:____{Var $5,f:Array [Int ,59];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1403))

    def test_1404(self):
        input = '''Class R:a{}Class Wt_:Y{Val $3,$_d2:Array [Array [Array [Array [Int ,0xF],71],0b1],06_06_23_4];Var $1m,T:Array [Array [String ,71],3];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1404))

    def test_1405(self):
        input = '''Class f_j:j{$9BH_(C,nzn,rR:u;_:Boolean ;E,Z:Float ){} }Class c{}Class _:pB{}Class _:_{Constructor (){}Destructor (){} }Class _7{Var _,$85k:Array [Array [Array [String ,47],9_8],47];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1405))

    def test_1406(self):
        input = '''Class e{$_h(k,_,_6:a4B){}Destructor (){}Val _,$_,$q5,$I:Array [Array [Float ,0B1],2];Val o,$M,$_:__fdC;Destructor (){} }Class M:wH{}Class s:_Qc{}Class _{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1406))

    def test_1407(self):
        input = '''Class _{Var V_:Array [String ,0133];Var _c42,_0,HV_r92,$y_ylX,v:String ;}Class _Y:w{}Class _3y_n:H{Var $8,$7:Float ;Destructor (){Break ;}Constructor (){}Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1407))

    def test_1408(self):
        input = '''Class Ur:a{}Class Y:_{}Class _{$0(__v_,L,G_XS,_,p:String ;f_,t_:_){}Val X5kjc_,$q0,S,__,_,$i2_6,$_,__:Array [Array [Int ,04],023];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1408))

    def test_1409(self):
        input = '''Class f9:v{Constructor (__h:__Y){}Constructor (e8,__3,_,_:Int ;_T:Array [Array [Array [Boolean ,0b1011011],0b1011011],0b1_0];d,___1_4,IO:Float ;_:Array [String ,1];x_:Int ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1409))

    def test_1410(self):
        input = '''Class _EW:A2{Val _6:Array [Array [Array [Array [Int ,027],3_5],4],9];Constructor (TV:Boolean ){}Constructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1410))

    def test_1411(self):
        input = '''Class _{Destructor (){ {} }P(n:Float ;S:Array [Boolean ,58];_4_09:Float ;_,__:Array [Array [Array [Array [String ,0B1_100],0x63],0144],057];b_:Array [Array [String ,0B1100011],06_0];_Xv,a_,_:_){Continue ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1411))

    def test_1412(self):
        input = '''Class W{}Class _z:__{}Class AL8N4I{_(){Continue ;}Constructor (n,_3_:Float ){} }Class _5:L{}Class __:J4{Constructor (){Var d:Float ;} }Class h:l{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1412))

    def test_1413(self):
        input = '''Class v{Var _,_4:_;Var $D:Int ;Var K_h_:Boolean ;$C(_5mn,B,i_7__K_f:Array [String ,0B10]){t::$_();}Val $9D,___42_2,$_:Array [Float ,2_2_4];}Class __{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1413))

    def test_1414(self):
        input = '''Class _:_{Var _2e,_b_:_7;Constructor (){ {}{} }Constructor (_:Array [String ,0204]){}___(_:Array [Float ,36]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1414))

    def test_1415(self):
        input = '''Class N7___:C{}Class _:TFF5{Val J6:Int ;}Class _K{Val $_:Array [Float ,0XE];}Class _{Val $_5_,$N6_:Array [Float ,0B1];}Class yQa:N{}Class o:U{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1415))

    def test_1416(self):
        input = '''Class __3R2:_{}Class _i2N{Val $vb5,$Va51,U,w,$q:_1J;H(){}Val $_,$I3,_Pc_,$p:String ;}Class n{}Class _38t{}Class _:x{Var $E,$_,tK:Float ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1416))

    def test_1417(self):
        input = '''Class _0{}Class RU_:gS_{Constructor (x,w7t,_1,_f:Ig;_3,_5,J,J:Array [Int ,0X9];_H,W,r9,___Y,j1,_TiN,__g,r1:Array [String ,0x16];_zQ2,_v_9w_,C7:a_P){Break ;}Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1417))

    def test_1418(self):
        input = '''Class a1t{}Class _:t{}Class _{}Class _6hN_Gx_Z{}Class __:L{}Class _6{Constructor (_:_;L1z:Q0_I;_:String ){}Constructor (_v,H:_;c:p2;_5:Boolean ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1418))

    def test_1419(self):
        input = '''Class _:_{r__(p:Array [Boolean ,0x3]){}Val $_h,_,$o:String ;Destructor (){}Constructor (){}Val X9,_,JD73,$6,_,$__:Array [Array [Array [Int ,1],01],0b11111];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1419))

    def test_1420(self):
        input = '''Class N6:_{}Class __{Var _:Boolean ;Val $_j73:Int ;}Class _T_e{}Class H:_{Constructor (__:Array [Array [Float ,04],0143];q1AV5m,__hs_B:Boolean ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1420))

    def test_1421(self):
        input = '''Class _:_{}Class __:_{Var __1:Array [Array [String ,0B1_0_0_1_1],91];}Class _W74_63{Constructor (){}z(b:__6;_,_:_){} }Class _:yF_A6{Val $xu_,R:m;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1421))

    def test_1422(self):
        input = '''Class __:_{Destructor (){}Destructor (){} }Class _X__:_{$T(j,b0:Array [Array [Array [Int ,04_3],0X3],02]){_Dm4::$yf8.E();}Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1422))

    def test_1423(self):
        input = '''Class _:S_3{Val $Q___4:hm6;Constructor (_,__:Boolean ;_1,p,Y,H__:Array [Array [Float ,0B101],6_3];j_,t,Xx40:XC9;_,bY_:Int ;_u:Array [Array [Int ,0X52],0b1010111]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1423))

    def test_1424(self):
        input = '''Class __8:_tX{Constructor (_:_;_,_4,_5:Int ;_,hI,_,ld_23J9,_:Array [Array [Int ,014],73]){ {} }$3pJ__E_0(){Return ;}Var m,_:n;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1424))

    def test_1425(self):
        input = '''Class H__:Tt_W8{}Class L__:m{}Class _p6ic0_3_8_H:__8{Val $4,$70:Array [Float ,0x23];Val $p:Float ;Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1425))

    def test_1426(self):
        input = '''Class _:_{Destructor (){} }Class ___:d__{Var $8:Array [Array [Array [Array [Array [Int ,37],0x4F],37],864],0b111001];Constructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1426))

    def test_1427(self):
        input = '''Class __xyJz_d_k_{}Class _:a2{Constructor (__:Int ;U,_X,B_y:Array [Int ,077]){}Var U,p:_;}Class R:N{Val V:_;Val __E5:Array [Array [String ,0b101],077];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1427))

    def test_1428(self):
        input = '''Class _4{}Class ___z4:Fg_{Constructor (_2Ts9:Int ){Break ;Return ;Break ;}Val s,F:Int ;Var _6_v9,_:d_;Var $4,__:Array [Float ,60];}Class I:t_{}Class ____0{Destructor (){}G_(){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1428))

    def test_1429(self):
        input = '''Class T3:_i{Var $__F:Int ;Var $q6,_,_:Float ;Constructor (_5_,e:Array [Array [Array [Float ,0x49],0143],0143]){} }Class _u{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1429))

    def test_1430(self):
        input = '''Class T__:_{Constructor (_7,_:Array [String ,07];_:D_2){ {{}Continue ;}{Break ;} }Var K,$_I_Q,_o5,$7,$O0_,$93,S:_;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1430))

    def test_1431(self):
        input = '''Class __{Destructor (){}Val $_:Array [Int ,0x48];}Class I:Mrq{Var $__1:Array [Array [Array [Int ,0B10111],89],0x6];$_(_V:Int ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1431))

    def test_1432(self):
        input = '''Class __9n{$tu1_o(){}Constructor (_08,r_,b:Array [Array [Array [String ,0b1_00_0],0X6EA_0],0b1];B36tn:Float ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1432))

    def test_1433(self):
        input = '''Class f_A{Val u3:Boolean ;}Class _:A{}Class _:_9{}Class c:_{Constructor (B5__,X:Array [Boolean ,0125];a:String ;l8_v,_,_3:Int ;_f_,__:Float ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1433))

    def test_1434(self):
        input = '''Class dF4:u_9_F2{Constructor (_66,r:Array [Float ,0b10_1];_,Xp,X,K,__,_99__dw,M,v1,_,h:Array [Array [String ,0b1001011],9_47_51_2]){ {Break ;} }}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1434))

    def test_1435(self):
        input = '''Class _:_{Val A3,$c1,$7,$4:Boolean ;Val _:Array [Array [Int ,81],0B10010];Constructor (){Continue ;Continue ;} }Class _:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1435))

    def test_1436(self):
        input = '''Class O_{$_(__:Int ){Break ;} }Class _{Var n:Array [Array [Array [Array [Array [Array [Float ,8],0X17A],30659],0X4A],0b1],052];}Class D1:y{Constructor (_7,JN2,_x,_,_:_7){ {} }}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1436))

    def test_1437(self):
        input = '''Class U0E_:_i{Destructor (){} }Class _f{}Class __:C{}Class _{Val d:String ;}Class _:_{Var $3P_,_:Float ;Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1437))

    def test_1438(self):
        input = '''Class h{Constructor (_,_L:Array [Array [Array [Array [Array [Int ,0x93],0x7],010],0B1_0],03_0]){}Constructor (_:String ){}N(){Continue ;Continue ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1438))

    def test_1439(self):
        input = '''Class U{Constructor (__:Float ;UB:Array [Array [Array [Float ,02],0B10110],041]){Return ;Break ;}Constructor (Cf_,e_,m:Boolean ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1439))

    def test_1440(self):
        input = '''Class _4{$w_(_96609,__:Array [Array [Boolean ,0b1],015];b,_:Float ;f:Array [Array [Array [Array [String ,418],0xD1_4_4],0b101],2];U:Boolean ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1440))

    def test_1441(self):
        input = '''Class WF:_{}Class B:_7J{Destructor (){Var b,g3:Float ;}Var $5__uIf :String ;$o8__(k2,_:Array [Array [Array [Array [Array [Int ,0x1],02],0B110001],0X25],0106];c___O_:B3){Self .ir0_l();} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1441))

    def test_1442(self):
        input = '''Class ___:_S{Val R3,$_90_,$_,__5:Array [String ,0xE_4_3_2];Destructor (){Var _:Boolean ;} }Class _:d_{Val $0:Array [Float ,0X38];}Class a_:_E{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1442))

    def test_1443(self):
        input = '''Class k:C{Constructor (){}Var $_4:_;}Class __{$0d(_,d,V,a,Y4_9:String ){}V(_,_,L3,m,__4_z:Float ){} }Class G:s{$_V2(T:Array [Float ,68];y6,_,yV_,L,_4,f:_B){Continue ;Var P:Array [Array [String ,02],07_6];} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1443))

    def test_1444(self):
        input = '''Class m:_{}Class k_:___9a{}Class _:_{Constructor (d_:Array [Array [Boolean ,89],0X64]){}Var _:R;Constructor (_1:Int ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1444))

    def test_1445(self):
        input = '''Class w_:_f8{L(o:Float ;_:L_;U,_:Array [Array [String ,0X4CC],29_2];o:Array [Array [Array [Array [Float ,0x8B],0B100011],0X4A],0B100011];__,I_,HM4:Array [Array [Int ,0X2_7],0B100011]){} }Class _s{Constructor (wZ2:_q;_,w,V,_,_,_I99D,___,e:Array [Int ,0b1]){Break ;Continue ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1445))

    def test_1446(self):
        input = '''Class l_:_{Destructor (){Continue ;Var J:Array [Array [Array [Array [Int ,0B111010],0b1000100],0b1],0b1_10_11];}Constructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1446))

    def test_1447(self):
        input = '''Class _7{Val $p:Array [Array [Array [Array [Array [Array [Array [String ,01],0x43],0B1011100],047],066],3],0X36];Constructor (_,X,DZ,V,_,Upl:String ;_s90:rh){}d(K1589r:J2ab_lI;u:Boolean ){Continue ;Val _:__;} }Class __{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1447))

    def test_1448(self):
        input = '''Class w__8:v{Val $2,w,q,$8S:Array [Array [Array [Array [Array [Array [String ,0b100101],9],0B1],05],0b100],0X87C48];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1448))

    def test_1449(self):
        input = '''Class _:_{}Class _:_{Var _,$9:Array [Array [String ,0B1],0b11];Var $9,_7cg,S:Array [Array [Boolean ,0XC9],013];}Class _:s{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1449))

    def test_1450(self):
        input = '''Class M:__{}Class _{Constructor (O1qF__h20,Z:Array [Array [Boolean ,07],0x6];m,u,H,U:Array [Float ,0X3E];awE5:a;D,_q,H_3Y9__:Array [Array [Array [Float ,0B1010010],0b110101],10];_4:OR){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1450))

    def test_1451(self):
        input = '''Class _{Val V,sv:String ;}Class _:nl{}Class i:_{Destructor (){} }Class _{Constructor (){}Var $c_m1:Array [Float ,9885];}Class _:_F_{}Class e{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1451))

    def test_1452(self):
        input = '''Class _R{$9_E5(){}$_(_6_:Array [Array [Array [Array [Array [Int ,0117],017],0x4A],07_4],067];O_,s0:Float ;_,W:Float ;_:Array [Boolean ,79]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1452))

    def test_1453(self):
        input = '''Class _5h2:_{Constructor (){}Val $h,__2g7u:Array [Float ,0b100011];}Class P{$52_zu_(X,_N,_X,s_:String ;_:c){} }Class _:_5{}Class t0:_9{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1453))

    def test_1454(self):
        input = '''Class i{$p_3(){ {Val __,_,_,S5_,_,Q1:Float ;Continue ;} }}Class _U_:e1_{x(){}Constructor (M:Array [Array [Array [Array [Boolean ,0B1001],6],0B1001],0b1000001];G,L:Float ;__1__,__,_,_A_,o,yS,__O__06,Z6:_5ur){} }Class P:J5{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1454))

    def test_1455(self):
        input = '''Class _N8_4:Y{Constructor (k:Float ;_L18:Array [Float ,0X4];_,__:Array [Array [String ,0x3B],0111];_,_,c5_:_5_19_0){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1455))

    def test_1456(self):
        input = '''Class z_{Val h:zO_;Var g,$76T:Boolean ;}Class __b:_{}Class _r_U0Pw:_{}Class __:_{Constructor (y:Float ;_:V_;n__,_,_,N8,Q,Bc_,_,_,T,_,_,X,V6MZHB,_2_K:_7_7){}Var _,_G____:String ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1456))

    def test_1457(self):
        input = '''Class __{Constructor (C_,eY,_Np:Boolean ;_5:Boolean ;_P_,_126:String ;H:t){Var _:Array [Float ,0x6_5];}Constructor (_Q_X:z07){}_(V,p8c_:_q8;_70:y){} }Class _4:_8{}Class __:Zj{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1457))

    def test_1458(self):
        input = '''Class l:_23{Constructor (_:Array [Array [Array [Int ,8],0X60],8]){Var _1_By ,dR_H84:Array [Array [Boolean ,0B1100100],0B10];}Var _6:Array [Array [String ,023_36],0X3];Constructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1458))

    def test_1459(self):
        input = '''Class _:_{Val $v,$S,W,$h_Y_0:_j;__7__(){} }Class _2:_{}Class B46Z_:l{Constructor (Zc:Array [Boolean ,0X1];Z8,f_:Array [Array [Array [Array [Array [String ,0B1110],2],0X5],0B1],27_7]){} }Class t__{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1459))

    def test_1460(self):
        input = '''Class S:Lc{Destructor (){Continue ;}$8s4_5(__:Boolean ){}Constructor (_R,___1:Array [Array [Array [Float ,0b111101],0X2A],06_0];_33,_:Boolean ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1460))

    def test_1461(self):
        input = '''Class TK_:_{}Class Q:__{Var $__,$_N8,$1:_;}Class _{}Class s_a:_{}Class K{Val P:_4H0;Constructor (_ly:Array [Array [Array [Int ,0b1101],0X7_8D_E],077];W:Float ){}Var _5_,$_I__e:Array [Boolean ,49];Constructor (V:Array [Array [String ,49],0XCD62]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1461))

    def test_1462(self):
        input = '''Class _{Constructor (s:Array [Array [Float ,14],0X2_A];_:Boolean ;C,C__:Array [String ,0b10110];S_,_:Float ;_:MUd0_;S,b:qf;L5:Int ){Continue ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1462))

    def test_1463(self):
        input = '''Class _301{$_x(_,h_r,k1_21_b,P_:Int ;i,Sg,_d0,x_y,z,_,K,_:Boolean ;K07_:Int ;K_,D:S_;_s,__61:Array [Array [Array [String ,0X8],0B11],1_7_0];_:Array [Boolean ,0622_6_2_2]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1463))

    def test_1464(self):
        input = '''Class _:e{Constructor (K:Array [Array [Array [Boolean ,0xD],30_5_572_7],0b1];_mR,J,_:Float ;_550_N,M:Array [String ,0X9];_:Array [Boolean ,032];___,N,___,_1_,_,_:__;b__,_0:Array [String ,032]){} }Class v{}Class P__:z{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1464))

    def test_1465(self):
        input = '''Class M:f{Constructor (F3_:Array [Array [Array [Boolean ,0b1001000],7],0x4_2_06];W:Array [Int ,0XF49];__1,_,M,Nb:_M1;_,n:lShq;O__,h,B,__:Array [Float ,0X3_3]){}Var w:s;Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1465))

    def test_1466(self):
        input = '''Class a:__{}Class j7{}Class D_:_{$w(uM652x_6__34,__98:Array [Boolean ,1];r_,M,_1V,c_2,_,R:Int ;o_1,__6,m_s___,Q_6,__:Int ;_:NP0;p:_){}Var _,Joici5,_,$G:Float ;Var X:Array [Int ,0X8];Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1466))

    def test_1467(self):
        input = '''Class Ho5U:_7_i__e_pYY3{}Class _{}Class __{$_(__,d,_:V;D:r_47;W,_,PF,sF,p,x0,_:_f;a9:w_;___,D:Int ;D:Int ;B_KC7,_,V3:Array [Array [Float ,100],0B1_1];Z_78u7:String ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1467))

    def test_1468(self):
        input = '''Class c_{Constructor (_,Z_,i:Array [Array [Array [Array [Array [Float ,0X3E],0B1_1_1],0x61],0x61],01];p:Float ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1468))

    def test_1469(self):
        input = '''Class _:OA_8_{Destructor (){} }Class e_:U7_0C{}Class L_m6bx:_{}Class a:_{Var E5,$k9,$sN,S,$3__:Array [Array [String ,0xD],012];Constructor (_,_,O:Float ){Continue ;}Destructor (){} }Class _O8{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1469))

    def test_1470(self):
        input = '''Class u7{Constructor (j,_,_:Array [Array [Array [Array [Array [Array [Array [Array [Array [Float ,02],0XE],0B101111],0b11],0B1_1],0110],0110],0B1_0],0110]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1470))

    def test_1471(self):
        input = '''Class l{Val $A:String ;Constructor (C,_,I93,J6:Array [Array [String ,01],0b100010]){} }Class _{S_7(__0,_,Y,b:String ;__,G_:_){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1471))

    def test_1472(self):
        input = '''Class __9_:D_{}Class i{Destructor (){} }Class _7{Constructor (){_R::$2();}Destructor (){}w(Gz9:Array [Array [Float ,45],0b1001011];__,ER_:_){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1472))

    def test_1473(self):
        input = '''Class u4:_D8{}Class X:PS9{Destructor (){}Constructor (H:_P;_,Ob:_x;w:String ;wW_:Array [Array [Array [Int ,0b111000],0X11],05];_z:Array [Array [String ,0b1],061];SN,J:String ;_,z:Array [Float ,1]){} }Class _7{}Class _:H_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1473))

    def test_1474(self):
        input = '''Class D{Constructor (_9:Array [Array [Array [Array [Array [Array [Array [Boolean ,5],6],5],0b1011000],064],5],024];_:Array [Boolean ,0b1011000]){Return ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1474))

    def test_1475(self):
        input = '''Class Ps50_:_I{}Class _{}Class __:___{}Class _:_{}Class S_:_{}Class _:_{}Class i{Destructor (){}Val v:Array [Array [Array [Float ,0b1100001],03],05455_556_7_2];}Class S{Val _,$7:_;Var _7:_;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1475))

    def test_1476(self):
        input = '''Class _{Var NC,$5__n4:Float ;Destructor (){}Var $0:Array [Array [Array [Array [Array [Array [String ,0B10010],0135],0xE],0b1_11_1],0x42],7];}Class _:_mX7q4{}Class P3:_{}Class _3:_{}Class _:__6{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1476))

    def test_1477(self):
        input = '''Class rK3_Mq{}Class D8{Constructor (s,_11f,__:Array [Int ,0XE4];T_7x,___,_:Array [Float ,05]){Val e,_:Boolean ;} }Class e{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1477))

    def test_1478(self):
        input = '''Class _:_{Constructor (z:Array [Int ,0x46];_:Array [String ,49_3_711];r_0___9_:Array [Array [Array [Array [Float ,0B11000],0B1],0b1001111],0X12];_,W_2:Float ){ {}Continue ;Continue ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1478))

    def test_1479(self):
        input = '''Class dW{}Class _:l6{}Class _M_{}Class a8C_:n{Val $_,$K:Array [Boolean ,0X21];Destructor (){} }Class __{Constructor (u:_j_N___;__x:N;_:_0___;G_:I7;e6V,Q9_,W_9:Array [Int ,55]){} }Class l:_8{}Class _G:_r{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1479))

    def test_1480(self):
        input = '''Class R_{Constructor (_w_,_N,oI40C:Int ;_:Array [Array [Array [Array [Array [Float ,0xF_2],0xF_8_A4],030],0B1_10],0X4];F:_Kdlu;__:Array [Array [Array [Boolean ,0x3A],35],0XC];p:Array [Float ,9]){}uG(_:k7;Z:Float ;__,_,__,__7,_,_6,_I:String ;_W,_f:G;_,c:Int ){Continue ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1480))

    def test_1481(self):
        input = '''Class _:_5{}Class y{Constructor (h_,_95X,Y5,T20,u__,_:Array [String ,0x50];_4:Array [String ,047]){} }Class _2_:i{Val _:Xm;}Class __s{Destructor (){} }Class _:f{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1481))

    def test_1482(self):
        input = '''Class w:m{d(_,_c:Int ;F,m:Array [Float ,38];b:_YJ8E){}Constructor (_,at,_,_,_:Boolean ){}Destructor (){Continue ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1482))

    def test_1483(self):
        input = '''Class a1:_5{Constructor (){Break ;}Val $_,$C:_;}Class u{}Class _{Val _:Array [Array [Array [Array [String ,0X5B],0X5B],0x4F],0B1];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1483))

    def test_1484(self):
        input = '''Class G:Qo{}Class _0:_{}Class __5aa{}Class o{}Class B{Val $7:Int ;Constructor (){Val Z:String ;}Destructor (){}Val _,$o9_,$m:Float ;Destructor (){} }Class __{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1484))

    def test_1485(self):
        input = '''Class f{Constructor (){} }Class P:_{}Class _36_{}Class a35:c{}Class M:K{}Class X{Constructor (){}q_(Wk8b:Boolean ){}Var $4_,_:Int ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1485))

    def test_1486(self):
        input = '''Class kxr:O7{Val __TqGc:Boolean ;Destructor (){Continue ;}Var $d:Array [Float ,6_3];Var X,_:_eKr5;Val $_6,h,I8,___:U_;}Class R_9{Var $b,v:Boolean ;Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1486))

    def test_1487(self):
        input = '''Class _:Z4_{}Class _7_W{Constructor (__c:_4){Var yy6_H6_G:EZO;}Constructor (){} }Class _8{}Class _:h{Var $5,$LU:Boolean ;Constructor (__5:Float ;_,f:Array [Int ,03_43]){Continue ;Q::$_();} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1487))

    def test_1488(self):
        input = '''Class YS_0_{_737(){}Destructor (){}Var $__,$_:Boolean ;l(_7,o,_0K_7,_:Array [Boolean ,012];D,_,_1,_kv8,_3B:Float ){} }Class F:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1488))

    def test_1489(self):
        input = '''Class j{}Class _:__{Constructor (_1:Array [Array [Array [Array [Float ,0XD],0X7B],02],92]){Val e:Float =_::$_().__;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1489))

    def test_1490(self):
        input = '''Class P8G{Constructor (_,j,F_,W:R7p;__3,m_3NO,_,NH3:Array [Array [Array [Float ,0x3F],0x3F],28];i:Boolean ;I:_;L,g_:Int ;A5I9x:String ){} }Class H{}Class ___:WC_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1490))

    def test_1491(self):
        input = '''Class _:l_{Val $6:Array [Int ,1_23];$1_(){} }Class _:_2{_(_,_:_;j1,_1___:Array [Array [Array [String ,0X46],0XB3_AA4],0x5]){}Val _,_,A_,$7:o;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1491))

    def test_1492(self):
        input = '''Class xp9M63xB{}Class _:_r{Val $_w,$m1:__;}Class H:IQ85{Destructor (){} }Class __a0M:_s0{Var $_w,$Nl,w_,$t,$l9,$_8:Float ;$YW(_2:Array [Array [Int ,41_0],0b11000];xHh,_,_e,Zfj:___){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1492))

    def test_1493(self):
        input = '''Class _i{Constructor (){Val i,D__:nF_;}Destructor (){Return ;Break ;Continue ;} }Class _{$Y1A(){}Constructor (___:Int ;a_,__:Array [String ,0b1];_2z_:Float ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1493))

    def test_1494(self):
        input = '''Class _{Destructor (){}__Z173_J(P:String ;R,_:Array [String ,07_20_56_0];z:Array [Array [String ,0X2],0B111]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1494))

    def test_1495(self):
        input = '''Class _u{Val L,$z,k,$Y_Ok,$36,$_:Int ;}Class _:_{Constructor (){}Var $4:Array [String ,89];Val h,c:Array [String ,985];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1495))

    def test_1496(self):
        input = '''Class _V79{Destructor (){} }Class bU5{Var v,$h_:Boolean ;}Class j9:U_4AC{Val $s:String ;Destructor (){}Val _c_:String ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1496))

    def test_1497(self):
        input = '''Class aOY_:_{}Class __{}Class t:_{}Class __{Var $___,In_ :String ;Constructor (){ {} }}Class _:M8{Val $8:Array [Array [Array [Array [Array [Boolean ,32],0x1E],16],0x2],6];}Class p{}Class _:__{Constructor (){}_K(){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1497))

    def test_1498(self):
        input = '''Class Nx{}Class _Z:_{}Class __{}Class I:_k{Constructor (_1,_,_7,z_:Array [Array [Int ,0b1],0B1_0];nOQ:Float ;_1O_,R:Array [String ,0x9]){} }Class t:_6{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1498))

    def test_1499(self):
        input = '''Class _{}Class R:T_{o(v,E,_,_e,_:Array [String ,56];tRP_,CX:d;_I0__,f7_q,v8:Array [Int ,0x19]){}Val _3_,i,_:Array [Array [Array [Float ,0b1_0],0B1000101],0x19];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1499))

    def test_1500(self):
        input = '''Class m{Constructor (_:Array [String ,25_5_2];___S:Array [Array [Array [Float ,0b1111],6],7];___81:Float ;M:Array [Array [String ,8],07];W,AQ,y:Array [Boolean ,02]){}$e(){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1500))

    def test_1501(self):
        input = '''Class b:_r6{}Class _____1_2_57:_{Destructor (){}Constructor (){} }Class R:u0{Constructor (){}Var $A,$l2,$9__:__9;$_Z(){Break ;}Var a:_U_;}Class _4V06a{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1501))

    def test_1502(self):
        input = '''Class a:_3{Var $_:String ;Val $x,$65,O,$B1,$3_:Array [Float ,9];Val $27:Array [Array [Array [Array [Array [Boolean ,7],0x8],05],0B110],0127];}Class Y:___{Constructor (){Continue ;Break ;Return ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1502))

    def test_1503(self):
        input = '''Class sr{Constructor (Ij,_s3,_:String ;_6,_,N:Array [Array [Boolean ,0X5F],43];_:Float ){} }Class mm{Destructor (){}$__6(){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1503))

    def test_1504(self):
        input = '''Class G{}Class rc_n{Var q,$N:Array [Array [Array [Array [Array [Array [Boolean ,0b1],0b1000011],3_5],37],0x54],0b1_1];Constructor (_:Array [Array [Int ,0X13],034];_8s:String ){Continue ;Break ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1504))

    def test_1505(self):
        input = '''Class R__{O(){} }Class _{$0V(U,V15,_J:Int ;__3_,G9,J,y6Th,S,a240,X:Int ){Return ;} }Class C{P(_:Array [Array [Array [Array [Array [Array [Float ,77],9],77],0x4],9_2],77]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1505))

    def test_1506(self):
        input = '''Class _:E{Constructor (g:Array [String ,6_2_0]){}Val _:Boolean ;}Class _{}Class d_:P_{}Class nyV:_{}Class P_:_t{}Class _{$_0(_:Array [Boolean ,032]){}Constructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1506))

    def test_1507(self):
        input = '''Class M{Val $_:Array [Array [Array [Array [Array [Array [Array [Array [String ,0130],0x8],071],81],0XB_B],0x56],06],04_3_7];}Class __4:E{a2(){ {} }}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1507))

    def test_1508(self):
        input = '''Class _B:_{Destructor (){}$J(w65c_7,_:Int ){Break ;}Val $_6:_;}Class v7{Val _9H,_1p,__2:String ;Constructor (){}Var D_6,q_:Boolean ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1508))

    def test_1509(self):
        input = '''Class Rn{Constructor (_7,_478,W2:A_9;_:Float ){Var V:Array [Array [Float ,05_7_7_6_2],0xF8];Continue ;} }Class _5:q{}Class q36uw{Destructor (){ {} }}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1509))

    def test_1510(self):
        input = '''Class C{_U_(_k_pU,_5,T,eK:_;L:Float ;j_0_,i:_Djl;_C_W0,_:_;_:_2W;_0_Wj:Array [Int ,074_53_62_3]){}Var $_,_:Array [Array [Boolean ,0144],0b1001011];Var $0q_:String ;}Class _{Val $_:Int ;}Class _:Ke_{}Class r{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1510))

    def test_1511(self):
        input = '''Class W238:D67{}Class _:n9{Destructor (){} }Class s45__1{Destructor (){}Var $_:Array [Array [Array [String ,0X65_4B_1],016],0b10111];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1511))

    def test_1512(self):
        input = '''Class Ue__:_{}Class _zd{Var $6,$3,L_V,$_5:Array [String ,043];OP(){}Val $26,h,$Q:Array [Array [Int ,9_2],0B1_1];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1512))

    def test_1513(self):
        input = '''Class _{Val _hvj:t_;Destructor (){}$_(_n7:Array [Array [Array [Array [Array [String ,0B1011010],92],07],04],0b1100]){} }Class C_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1513))

    def test_1514(self):
        input = '''Class ym_y_m{Val $_L_3,_y:Array [String ,0X5E];Val $y:Array [String ,0X5E];}Class _9_:_{Val $3__:Array [Array [Float ,07],0x1];}Class _{Destructor (){}Destructor (){}Destructor (){}Var $g:String ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1514))

    def test_1515(self):
        input = '''Class _:h_4{}Class _:_7_{Val $8:Array [Boolean ,07];}Class C_:Sv{}Class lc_{}Class N:P{Constructor (){Return ;}Destructor (){} }Class w_13:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1515))

    def test_1516(self):
        input = '''Class _:r_b_{}Class _5:b{_l3(g,__K_e6J:Array [Array [Array [Boolean ,92],24],0B1001000]){Break ;F::$7P();}Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1516))

    def test_1517(self):
        input = '''Class Y:_{Destructor (){}Var $_:Array [Array [Array [Array [Array [Array [Int ,0X8],0141],0141],0X959_BE_C_B2],04],0b111];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1517))

    def test_1518(self):
        input = '''Class ro3x:y5{Constructor (U8,F,_,_,J_21_,Y5:String ){Break ;} }Class L{}Class sf{}Class q:_{Var $J8:Array [Array [Array [Boolean ,88],034],0B11000];}Class _l{}Class C_:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1518))

    def test_1519(self):
        input = '''Class _TM7__{}Class h:_{Constructor (H_,_:Array [Array [Float ,0XDC],020];_:Float ;K2,_,Amm:___pC_;W,X:Boolean ){} }Class x10:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1519))

    def test_1520(self):
        input = '''Class m:_{Val $_,D2,_,$_F,$l:Boolean ;$n(Bi,_,H,Qt:Array [Array [Int ,4_66_0],0B1_0];c:Int ){Var _,_4:Array [Array [Array [Array [Array [Array [String ,47],47],0X24],47],0B1],0X24];} }Class Z:_3{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1520))

    def test_1521(self):
        input = '''Class _5:_{Var $_:Array [Array [Array [Array [Array [Int ,0xA],2_8],0X30],02],02];Constructor (__:String ;Q,_n,N__:g_;tb,_M1,_:Array [Int ,0X30];B_,o2,__y:pLu7){}$405_K(){} }Class _26{Var _:Boolean ;}Class _O{}Class p{}Class __6:_{Constructor (_8,_:b3;O_g:Boolean ;M:Array [String ,0X30]){}Constructor (){}Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1521))

    def test_1522(self):
        input = '''Class _9{Var $h5W:Float ;Constructor (p:Array [Array [Int ,7],0b1_0000_1];_1x,_:Boolean ;_:__;E_,W,o,_:Int ){} }Class nL8:__{Val $0_9,$qj:Int ;Var O:String ;$6(){} }Class _5AS{}Class _:W{}Class _:GK_F{Destructor (){}rG_(__,_JmQ,_K3sB6_:Array [Array [Boolean ,03],07_6]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1522))

    def test_1523(self):
        input = '''Class _83_2_3:G{}Class L:_{Constructor (s,b,___,K,V0__,__,_:z){} }Class fW{Val P6j2,q,$L6:Array [Array [Array [String ,0B110011],53],53];}Class _2:j_{}Class __:X{}Class y{Var $9,$__,$3I:Array [Array [Array [Boolean ,0135],0135],0b1011110];Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1523))

    def test_1524(self):
        input = '''Class L2z6{Var _:_z;Constructor (_M0,_:Array [Float ,0X64];_0,_:Array [Array [String ,0x47],0XC]){}$_(__o,_,_17_,imz:P5){Break ;a_::$_2_Sc();} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1524))

    def test_1525(self):
        input = '''Class _6:cv_{}Class _{Val $O9:Array [Float ,05];}Class N{Destructor (){}Constructor (m:E2___;H,_E,F_:Array [Int ,0b1010100];F:Array [Array [String ,79],0116];_9,_R8,_,__,y:Array [Array [Array [String ,79],0X14],0B1110]){}Constructor (T,_:String ){}Var $5_,f6:String ;Destructor (){Break ;}Var _,__,P:Array [String ,0B1];}Class w6{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1525))

    def test_1526(self):
        input = '''Class wB:i_{Destructor (){Break ;} }Class i:G_{}Class L__w:W{}Class _E33M2:_9B{Constructor (){}Val _rm_39:Array [Array [Array [Array [String ,160_4],0x7],0103],0b1];}Class K{}Class k{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1526))

    def test_1527(self):
        input = '''Class s:_{Constructor (_,n:Array [Array [Float ,9],0b100001];P_6,e__2_H,iT3:Array [String ,030]){Continue ;{Val z__8,N,dac:E6Q0_N9x_;} }}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1527))

    def test_1528(self):
        input = '''Class x{}Class R__n52l_{Constructor (y,_:Array [Array [Array [Array [Float ,759],13],13],0116];_2,r:Array [Float ,0B101];_,_,m,tW65_,__:Boolean ;v,FU0,_WJo,L12,_,_X,f:Array [String ,0116];F,__B_:Array [Array [Float ,13],0x32];_:String ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1528))

    def test_1529(self):
        input = '''Class _{}Class __:A{}Class _{Constructor (){Continue ;}Constructor (){Return !!!-T::$_().P9R;Var h:__T2c;} }Class h4_:m_{}Class _8:s{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1529))

    def test_1530(self):
        input = '''Class _:_{}Class _{Val p:A;}Class _B9{Val _Z_0__:Array [Float ,967_507_1];Val $__:Float =!!!---68E-9-!!--_b92_::$3().w;Var $_,$_,_,$w,$_:_;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1530))

    def test_1531(self):
        input = '''Class n{}Class Z_{U_Y(_v:Array [Array [Float ,0x53],7_1]){}Val _:Array [Boolean ,0B1001110];}Class _{}Class _:Mg_M_{f(){} }Class Y8_D:J{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1531))

    def test_1532(self):
        input = '''Class _:_yi{}Class _{y(_:Array [Array [Array [String ,9],0x9_A],0xFBB1B_A]){} }Class x:_9{}Class __{Val $Ng_,$6,_,$_D:Int ;}Class _C{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1532))

    def test_1533(self):
        input = '''Class _9:i5{Constructor (f,_9u:Boolean ){}Constructor (_:Array [Array [Int ,0B11],021_36];_:String ;r,_V4,io:Int ){}Constructor (_7:Boolean ;__E,__f,_,yK_:pLr;H,_:Int ){}Var _O,H7:_;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1533))

    def test_1534(self):
        input = '''Class b3_:_O_{Val $_:Array [Int ,28];Var _,pM,$2,$I_92P,$_:String ;}Class _{_(_1:Int ){} }Class __:_W{}Class _P:___X_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1534))

    def test_1535(self):
        input = '''Class _{Destructor (){} }Class _:_{Var $xE:Array [Array [Array [Array [Array [Array [Array [Array [Array [Boolean ,0X5A],0b11100],0B11_0],10],0b11],0101],0277],3_8],0x7];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1535))

    def test_1536(self):
        input = '''Class j2:_{Constructor (c_:Array [Boolean ,0b100011];_:B;_,n,d,R_F:Array [Array [Boolean ,1],84]){} }Class _:o{}Class _6_4r_5_:g{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1536))

    def test_1537(self):
        input = '''Class Q7l3{}Class _:_71{Constructor (i,s,G:Array [Array [Array [Int ,0B1100001],46],0b111010];Q:_){}$7_(){}Constructor (){} }Class _2{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1537))

    def test_1538(self):
        input = '''Class _:_{}Class __:_J_{Val _,w4:Array [String ,0x55];}Class z_{Val $4_:_;}Class p_e____{Var Kr:_;}Class B2_:__C{}Class r:Q{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1538))

    def test_1539(self):
        input = '''Class _9:t{$4(){b::$0_();}Constructor (){} }Class _R:_{}Class o{}Class _:__{Var o16:Ef;}Class _5{Destructor (){Continue ;Val _9_7knJ:Array [Int ,0B1011101];} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1539))

    def test_1540(self):
        input = '''Class _:_{}Class __{Constructor (_6:Array [Array [Array [Array [Array [Int ,5_9],0b11_1],013],0XA],0xF_9]){} }Class T{Val $t95:_8;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1540))

    def test_1541(self):
        input = '''Class c_897{}Class m48ci:N_3_36{}Class q1__08:_{Val $9__,_:Array [Array [Array [Array [Boolean ,06],0B1010000],0b10_1],0xB];}Class _{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1541))

    def test_1542(self):
        input = '''Class BO6HaC{Var nl9:Int ;Constructor (q_,S2p:v_;dG3:String ;_,F6,_:__){}Destructor (){Break ;} }Class __:H5{}Class _{Constructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1542))

    def test_1543(self):
        input = '''Class _{f(A,Q1L,D7,__P:Boolean ;_7_4,r__Y:Array [Int ,92]){Continue ;Break ;} }Class jk{}Class w___:_o{Destructor (){}Constructor (_1I:Array [Array [Boolean ,0B10010],0b1011110]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1543))

    def test_1544(self):
        input = '''Class N_M7:N{Constructor (F7_9:Array [Array [Array [Array [Array [Array [Array [Array [Array [Boolean ,0XC6],46],0B110001],03],0B1],0b1_0_0_11],0x8F],051],0xC_7];__:Float ){}Constructor (d551A,_:Array [Array [Array [Boolean ,07],051],051]){Return ;Val _,I4:Array [Int ,026];}Destructor (){ {} }}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1544))

    def test_1545(self):
        input = '''Class _:_{}Class ___:y0{Var fa,x,$b,$f,_:L2_;Kih(A7:o){Break ;Val b68vr,_8,o3A,I_,T,G2I:Array [Array [Array [String ,4],0b1001001],0b1001001];} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1545))

    def test_1546(self):
        input = '''Class _9{Var y0___,_,$__5:Array [Array [String ,056],0B1001110];F(_,_:Array [Array [Array [Boolean ,0X1],0b10],47]){Continue ;}Destructor (){}Constructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1546))

    def test_1547(self):
        input = '''Class _0:_U{Var $f_4J,c_,$8_,$6:Array [Boolean ,0b10_01];Var $5_:Array [Array [Array [Array [Array [Boolean ,0113],0711],0113],0X1B],0b1];}Class _:C{}Class _:o{Constructor (){} }Class _O_0__:_h{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1547))

    def test_1548(self):
        input = '''Class Z7_c9{$_7(a,p:u9;_,_:Int ;H0,__p:Float ;_t,n:Float ){} }Class c{Constructor (__7,L:Array [Int ,83];SN,_,R,sz:v6_;_8:_;j:Boolean ;cBt:WL___){ {} }Var $_Kz__E2:_;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1548))

    def test_1549(self):
        input = '''Class AR:c{Var k4,E:Array [Array [Array [Array [Array [Array [Array [Boolean ,0B1],0b1011100],0b10_0_1_0],0b1_0],0107],0x20],49];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1549))

    def test_1550(self):
        input = '''Class X{Constructor (){} }Class _{}Class d{Destructor (){Var __,I3___7,c_2,_,_,_8,__D:Array [Array [String ,0B1],92];Return ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1550))

    def test_1551(self):
        input = '''Class p{Yi8(z_5,__,__5,f_P9_,I2,_i:Array [Array [Array [Array [Float ,15],06_73],030_2_3],15]){}Val $_,$e_,$B:_b0;N3(){}$AB_0X(){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1551))

    def test_1552(self):
        input = '''Class _Hk4{Var _,$2_:_;$__l(_,t5_,_,Z,C:Array [Float ,0112];e0:Array [Float ,0b10101]){Val J5:Array [Array [Float ,0112],0x4D];} }Class _5_13:D1{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1552))

    def test_1553(self):
        input = '''Class B_s{}Class SJ{Constructor (_,_3,E:Array [String ,0X5];__c2,s,_:Int ;R07:String ){Cq::$Lw3();_1::$0();Break ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1553))

    def test_1554(self):
        input = '''Class T1:T{}Class _:_4_{Constructor (mr6:Array [Array [Array [Array [Boolean ,0X1],0x1_0_8_0_5],83],0b11001]){Continue ;}Val $_,$2:Array [Array [Array [Array [Array [Array [Float ,03],0XD],0B111001],83],0b110],04];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1554))

    def test_1555(self):
        input = '''Class RU{}Class _sL:_t7{Val nk:Array [Array [Array [Array [Float ,0B1_1],0x2],0x9_1],0x1];Destructor (){Val kn1___,t:Array [Float ,0B1_111];_U::$_52();N::$5();} }Class _{Val $_P,A_,DX4V___,$W,k57_:Float ;Val $3:K5;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1555))

    def test_1556(self):
        input = '''Class _{Constructor (_,_,f,_,_:h__1){}Val $_,$9:Float ;Val $0,ee0h,$_,$8:Array [Boolean ,0B1];GW(__:_;O:Float ;_:Int ){_::$0zganV_60();} }Class _:LF{uZ_A(S:H;V:n2L){dT::$r.NO0()._1();} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1556))

    def test_1557(self):
        input = '''Class S{}Class J_{$P(_:Array [Float ,0X29];_nxd___37Rg:Int ){Break ;}Var w,f,$q,__f,$N,S:d1_;}Class I:S{}Class s5___{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1557))

    def test_1558(self):
        input = '''Class u{Destructor (){}Val N,$_7,s___:String ;Constructor (){Break ;}Var _:Array [Array [Array [Array [Array [Boolean ,0x27],0X56],040],0B1011111],5_0];Val i3,___W7:Float ;Constructor (__3:String ;S:Boolean ;f9:String ;S_,Z,P:_F;O,_35:Int ){}Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1558))

    def test_1559(self):
        input = '''Class a:___{Constructor (AX,_,_E:Array [Array [String ,0X9],97];X_:Float ;BI76_0,n_1:Array [Array [Array [Array [String ,0x36],06],2_5],0XB_5];r,c038gh4:TQ;W,_:Array [Array [Int ,97],011]){}Constructor (_R6I,_Y7_MaXj:_E___;_4,_,V:Int ){} }Class _{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1559))

    def test_1560(self):
        input = '''Class __:_8{$PV(_:Array [String ,0XD]){}Constructor (c,_45,_I:Array [Array [Array [String ,05],07_2_75],0X2B];_VP:Float ){Return ;Break ;}Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1560))

    def test_1561(self):
        input = '''Class ___H8_:Z{}Class _:T{Destructor (){} }Class _:_{}Class __X{Val $___,$_o,$_,$R,zZ,$42:_;Destructor (){}Val $X_,_:String ;Val C,$93:Array [Boolean ,04_20_632];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1561))

    def test_1562(self):
        input = '''Class _6:n2D{Destructor (){ {} }}Class WQN:W{Constructor (){Continue ;Self .AV.y01().___H();}Var $3,$m,$_j,$6:Float ;Destructor (){} }Class q:D{}Class _316_8___:F{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1562))

    def test_1563(self):
        input = '''Class _{Var ___6:Array [Array [Array [Array [Array [Array [Array [Array [Array [Array [Array [Float ,0x86],0b1],0X57],034],70],0B100_1],70],0xD],0x2F],5],034];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1563))

    def test_1564(self):
        input = '''Class _{Val $7H:Array [Array [Array [Array [Array [Float ,07_22],0X46],0B1],0B10_110],0B1];Var $_VS_:String ;Val M:_;$_LS(w__E_:Int ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1564))

    def test_1565(self):
        input = '''Class _44{}Class _2_1:_{Val _83w:Array [Array [Array [String ,0b101110],10],0XA];}Class _{}Class oV{Var M:a_9;}Class a___4c_{}Class _Y:B{}Class E{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1565))

    def test_1566(self):
        input = '''Class _6{q_X(P3_W_,_8,_,_3:z;_,OU_5,pQ:Array [Array [String ,0X8_E],0b1010101];_1_,_a,_R_1,Ca5:Array [String ,02]){}$_(_L,_,O5R3_,b:tmZG;_s:Array [String ,9];W:i;N,___,_:m){} }Class _{}Class J:q_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1566))

    def test_1567(self):
        input = '''Class _47_9m{Var j3:Boolean ;Constructor (iM,d1,_:Array [Array [Int ,041],01_26];_,H_,d,_,_6,H:_;U_9,_:X;_,_:x){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1567))

    def test_1568(self):
        input = '''Class _{}Class L56P{$P(_Y:Array [Array [Array [String ,0x26],2],0b1000110]){} }Class _:__{}Class y0_{Constructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1568))

    def test_1569(self):
        input = '''Class z{$9t39(_C:Float ;__9_:Boolean ){} }Class _8:_{Var T,_:Array [Array [Array [Array [Array [Array [Array [Array [Boolean ,06],0b1011010],0b1],100],0X35],0b1],0B100101],0xD];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1569))

    def test_1570(self):
        input = '''Class _:_{Val Ff,$G,$_,$1:Array [Boolean ,0X47];Val t6_:String ;Constructor (R6:Array [String ,0b1];B:Array [Array [Boolean ,0XF_F],0b1]){Var iV_:Boolean ;} }Class _:__S_mkj_c____{X(i:Array [Array [Array [Array [Array [Array [Array [Boolean ,0B10101],0x8],0b10101],0B10101],0b10101],83],0x42];K:_n0;_M9,J,v1:f_;u,_,_,_8TJ,_,__:Float ;F,_42y,z:Array [Array [Array [Array [Float ,0X47],0X9],83],0b1]){} }Class R_:_7{}Class _N8{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1570))

    def test_1571(self):
        input = '''Class _:M{Constructor (){Continue ;} }Class _:i9{Val $_6,z0:Array [Float ,0X7];Constructor (JE1_,__:String ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1571))

    def test_1572(self):
        input = '''Class _:_{Val b6:_;}Class e{Var $_j:Array [String ,0B111100]=New I()/!!--Zj9::$_w+---EBb_::$L>=!New s();Var __6_O:v;}Class _{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1572))

    def test_1573(self):
        input = '''Class _n:D4_{}Class G_{}Class S{}Class _:_w2{U_(_:p){}Val $_:U;Val $_:Array [Array [Array [Float ,0B10],0B1000000],0B1];}Class _39_:_{}Class VjTd{Var _JS,$w,O,h5____,$_V_:Boolean ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1573))

    def test_1574(self):
        input = '''Class _5___{Val B_:Array [Int ,0B1010011];$47(){ {}Continue ;Break ;} }Class y_D{}Class e{}Class _:o___{}Class _dG:M_{}Class g_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1574))

    def test_1575(self):
        input = '''Class X:A{Var $h3k:_1__;}Class dt__3_B{Var $_0,D:Boolean ;}Class ___AS:_{__(b_,_J:Array [Array [Float ,05_0],0b111]){}Val $_,$_,_14_,$6n_,S,M6d_c,$_d:Array [Array [Boolean ,0x2D],0126];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1575))

    def test_1576(self):
        input = '''Class G{}Class _4uWi{}Class O11R{}Class _{Constructor (){}Var $8fBy ,w,B,M,i,_E,$4L_w:Array [Array [Array [Float ,23],0b1011010],0X7];Var H,_7,$C:Array [Float ,0xA59_4_7_E];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1576))

    def test_1577(self):
        input = '''Class _{}Class _4:q{U(_,QP:Float ){} }Class F__{Destructor (){}Var _:Array [Array [Array [String ,17],1],0B1_1];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1577))

    def test_1578(self):
        input = '''Class V{Constructor (___:Array [Array [String ,0b1],0b1];__,I8:String ){} }Class yb{Var p:_;Destructor (){Return ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1578))

    def test_1579(self):
        input = '''Class F:I{}Class _0:_S_{Constructor (P,_t6:Array [Float ,06_26_6_1]){} }Class H_Ki:_{Val CU_6,$1,$3,$_:Array [String ,2073];Var $_J:G;d6w1_i(){} }Class _{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1579))

    def test_1580(self):
        input = '''Class w{Val $_T_,$G3k:_;Constructor (){}Var $1_:Int ;}Class X__4x:___{Constructor (_86V_:Array [Int ,062];a:Array [Array [String ,0B1111],0X3];_,R,_:Array [Int ,0X4B]){Continue ;} }Class i{Constructor (_1:String ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1580))

    def test_1581(self):
        input = '''Class _:_z_{}Class p:e{Destructor (){Break ;}Constructor (){}Val l,Z9,_:Boolean ;}Class _:p{$Q(d0_F,_:Int ;R_:Array [Array [Boolean ,393],07];q,_,rV_Ua,_,v:Int ;_5:Boolean ;n,C5:B_;_:Boolean ;z:Boolean ;_,_H:Array [Float ,0X7];___2,_:Boolean ;E:Array [Array [Boolean ,0B1_1],0b1]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1581))

    def test_1582(self):
        input = '''Class k8a:_{Destructor (){} }Class _{}Class __:_W7{Constructor (g_,__,E,_,z_:Int ;_,_,_uw,_H:Boolean ;e:__){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1582))

    def test_1583(self):
        input = '''Class _2{}Class s7{Var $29,FmF:Array [Array [Float ,0b1011100],06];$_8s6Pn(){Var v,G_:Array [Array [Array [Array [Int ,0x6_B1],28],0x13],0b1];}Var _:Array [Array [Array [Float ,04_6],2],0X46];}Class r:th{_2(_i:Array [Int ,0b1];b0,N,_3_57ME_o,_:B9;_de:Boolean ;t:Boolean ;_,_w,xkmP:Array [Array [Int ,0xB9],04_5];_:String ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1583))

    def test_1584(self):
        input = '''Class Bf{Val $C:i7;}Class _{Var $85CvQ,$4f_,o:Array [Array [Array [Array [Array [Float ,0B10],7_2],9],0b1],0B110010];Val $__9,_,z3,H:M_;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1584))

    def test_1585(self):
        input = '''Class _{Constructor (_:__;_Ay__1,_,_0,_3:Float ;J__:_;_,__0U,__,uWPlc:Array [Boolean ,0b1]){}Constructor (_,_:Int ){Var _,z7,m,d,_19B,_:Array [Int ,0X4];}Constructor (){} }Class __9_:_{Val _3D,_:Array [Int ,0b1_00_1];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1585))

    def test_1586(self):
        input = '''Class _6__r:_c{Val $j__9,$T:Array [Float ,0b1001100];}Class A44{Destructor (){} }Class _:H{}Class _1:_R_I{Var T_t,$1__w:Array [String ,0b11];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1586))

    def test_1587(self):
        input = '''Class N7{Constructor (){}Val $i,$_,G7:Array [Float ,0X2D];}Class c_:_{$_6(__:Array [Array [Array [Array [String ,07],0x13],06_65],61]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1587))

    def test_1588(self):
        input = '''Class a_{Constructor (__:Int ){Return ;Return ;}Constructor (_8Q0A,_4c3,_3:Float ;G,_:N___vl;_,_,x__1_JI,_:h30){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1588))

    def test_1589(self):
        input = '''Class Sp{Var _,$g,$I,h1,$1_:Float ;Constructor (h:Array [String ,30_67]){}Val $E:Array [Array [Array [Array [Float ,0B1],29],0X43],0106];Constructor (X,_,HN6,r:Float ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1589))

    def test_1590(self):
        input = '''Class _79:_{__(_,_:Float ){_::$_();} }Class _:__{}Class p600_F4:wa_{$_E(){} }Class k{Val $11:Float ;}Class _:VK56_6{Var $0,$3,_:_;Val $90j:Array [Array [String ,0X3D],1];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1590))

    def test_1591(self):
        input = '''Class e:_6{Destructor (){} }Class _5{Destructor (){}Constructor (_,j:String ;_:Array [Array [Array [Array [Boolean ,0X5_E_8_1C8],01_3],0B1_0],9]){} }Class sA:xt0{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1591))

    def test_1592(self):
        input = '''Class N_0:A5_s_{$1M_u(){}Var x,Q7__,$2,$__n_,$__lS:Array [Boolean ,0b1100];Destructor (){}Val $22_,_,$c:__;}Class lw:p{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1592))

    def test_1593(self):
        input = '''Class _:b{}Class _9:_kv{Val $_,$__:Array [Array [Array [Array [Array [Boolean ,0XC0E],0x1],01],1],0x1];Var x:Array [Array [Boolean ,1],0X91_6A_E_2_0_2];}Class zQ{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1593))

    def test_1594(self):
        input = '''Class _s:__Y6{_V(){}Var $Y0,$_3__1M:Array [Array [Array [Float ,0X9_E_4],0X4B],0B1101];}Class Y:s_{}Class C:_{Constructor (__,__:Array [Array [String ,0b110010],041];___y,_:Array [Boolean ,0b110010];_,u:Array [Array [Int ,0b1],0b1]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1594))

    def test_1595(self):
        input = '''Class W:PIy{Destructor (){Var _,hpW,__c__,_7vD,Ll_,attF,_5:Array [Array [Array [Int ,031],070],0b1_1_10];} }Class Y_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1595))

    def test_1596(self):
        input = '''Class hT0y:_{}Class _{Constructor (__:Array [Array [Array [Array [Array [Array [Boolean ,0b1_10_0],24],0b10_0],24],010],04];_5:H){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1596))

    def test_1597(self):
        input = '''Class e_{Var _9__,$49:Boolean ;N66(_:Array [Int ,1];_,r:L___F;_:Boolean ){Continue ;}Destructor (){} }Class ZM_:yA{Var $W4:Int ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1597))

    def test_1598(self):
        input = '''Class _{Var $4_S_,$_,$_,v,$_45,$i,$P,$5_,Q:_;$2_(Vf:Boolean ;__,j8:Array [Float ,02]){}P7(_,o_4_0,e:Array [Array [Array [String ,04],0xE],0x5F]){} }Class i{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1598))

    def test_1599(self):
        input = '''Class _:_1z{}Class q2:_67{Var _:Array [Int ,0x1B];_(){} }Class __0{}Class _{}Class Rh:y6{}Class n_6_:M9{Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1599))

    def test_1600(self):
        input = '''Class _81a{Val F3B:Array [Array [Array [Array [String ,030_2],0x5A],93],0b110101];$Er(_:Int ;K,C_:Float ;A,N:Array [String ,0X59];z:String ){Continue ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1600))

    def test_1601(self):
        input = '''Class k_32_U{}Class _{Var _Y__:Array [Array [Array [Int ,2],89],0B1];}Class _A{Destructor (){}Var _,_,$7,_,y2:M5_;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1601))

    def test_1602(self):
        input = '''Class _1:p{}Class c9:N__{Constructor (c_,_,g,T:Array [String ,065];Hr,zd:Float ){Return ;}Val CK5:_4;}Class z:_Q_w9{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1602))

    def test_1603(self):
        input = '''Class __{}Class Lq:_K{}Class __{}Class _:r8t{Var $__:Array [Array [Array [Boolean ,0225],3_1],0x44];Destructor (){} }Class jJ_{Var $v1_63:Int ;}Class b{Var _:Float ;Val $7_,$2:Boolean ;Val $7:String ;Var $s,N:Int ;$H(){} }Class X:_1{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1603))

    def test_1604(self):
        input = '''Class _:__{Constructor (A1_,Z,I9_:Int ;_:String ;_g:Array [Array [Array [Int ,0XA1_F],050],0B10011]){ {Break ;Continue ;} }}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1604))

    def test_1605(self):
        input = '''Class _{Var K:Array [Boolean ,0B1111];Constructor (_:n_3Q_y;fw,_9,v:Array [Boolean ,0B1];u_3j:Int ){}Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1605))

    def test_1606(self):
        input = '''Class _:i{Var $0_2,$_12:_;Val _:Array [Array [Array [Array [Array [Boolean ,04],19],0X10],07],6];Val $FNQ0,$3,i,$8:Q_g7G_;}Class _:m{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1606))

    def test_1607(self):
        input = '''Class _xo:_{Val fI:Array [Int ,014];Var $a,B_,$t__,Ly1,_:Array [Array [Array [String ,0xAE_1_1],0b10_0],0X38];}Class _{}Class _{Var _7,_:String ;}Class P:R__{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1607))

    def test_1608(self):
        input = '''Class Lv:z{Val $_,$9:__;}Class T{$_(D:_){} }Class _Z:jg54{$EZ(f2:_;__,_OIA:Int ;B_:Boolean ;_tP:String ;_,U,_,E,_J_:_6){}Destructor (){} }Class J:m{}Class v:Eo{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1608))

    def test_1609(self):
        input = '''Class S:_Fa1__741iF{m(tQS_,_B,__,C:Array [Array [Array [Array [Array [Boolean ,28],0X1_4],063],0x2_2_4],07];_1:Array [Boolean ,02_44];N,o9:x9;S_:_;_Ap49I,_A60:Boolean ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1609))

    def test_1610(self):
        input = '''Class D{Var $2,$__,$X41,fZx_Jv,$4,___,_,s,$8b:Float ;Var $_z:Array [Array [Array [Array [Array [Boolean ,0X5F],0B11011],0X1D9],054],0B11011];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1610))

    def test_1611(self):
        input = '''Class _:_6_{}Class Car:njR{Constructor (w,_,_M6C_8_b,_:U;y,__6:Int ;_7,s,V,__:Array [Array [Array [Array [Array [Array [Int ,0B10101],2],0x14],026],026],05];j2,_:Int ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1611))

    def test_1612(self):
        input = '''Class h__h_:o8{gt(ED:Boolean ;___,_,_,_V34d:M;t0n:Array [Array [Array [Array [Array [Array [Array [Array [Array [Array [Array [String ,06417],074],0XF],555_9_8328],0B1000100],84],0X35],074],23_5],0B1],84];__:Array [Array [Int ,06_7_0],0x7];_o:String ;_O,a:Array [Array [Int ,0X3],0x24];d_ek,j:g;_,M,_:Nwq){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1612))

    def test_1613(self):
        input = '''Class g{Var _:Array [Array [Array [Boolean ,04_6],0X8],0103];Constructor (D_,uV,_dV56,u_7_i_:Boolean ;e8__,_:_){Return ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1613))

    def test_1614(self):
        input = '''Class _:__{}Class x__D_:_{Destructor (){Var _:Float ;Break ;}Val _:Boolean ;Constructor (y5:__r;_,AOQ5_,x,l_:Float ;_kU,j_:F1;L:Array [Array [Array [Float ,0x34],0X5A],0X5A]){}Constructor (fD,p:_Y){Break ;}Val _:v;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1614))

    def test_1615(self):
        input = '''Class h_{}Class W:U{Val $_,u,$7_,$_S:Array [Array [Array [String ,88],0X4_0],0544];Var $_4,$_CR,$u,N6q,$s,$8_HR_,T:_;Constructor (V,WM_:Array [Float ,0b111101];_,g:Array [Array [Float ,0X60],0B1100011];u,_:Float ){Break ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1615))

    def test_1616(self):
        input = '''Class z{Var _76_:Array [Array [Array [Array [Boolean ,06_25],0x5_6],07],98];}Class K:_{}Class Qr_3Y:_{x8(C6,T,C_:Array [Int ,041]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1616))

    def test_1617(self):
        input = '''Class _{Val $4,$513:_;Constructor (_:Boolean ){}$_(_h:Array [Array [Float ,0x17],064]){}Constructor (){} }Class __{}Class _:__4x{}Class l7{Constructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1617))

    def test_1618(self):
        input = '''Class I:yF{Constructor (d:Int ){Val _:Float ;}Var __:Array [Array [Array [Array [Array [String ,0X4F],0B10],0b1001100],0xC2],93];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1618))

    def test_1619(self):
        input = '''Class k2LI:_{}Class S_:u{}Class bF:_{$9zb8(X:Float ;x54,x_,BI9:String ;C73g_5,__,_J_:Array [Float ,0273];_G,__:_5;sh_:Int ){_::$I()._()._();} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1619))

    def test_1620(self):
        input = '''Class _61{}Class _:I{Var _m:Array [Array [Array [Array [Float ,3],0X4D],0X6],073];}Class _2{Constructor (_:Float ;__f_:a;Z:String ){}Destructor (){Val _F_:q_;} }Class rDL{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1620))

    def test_1621(self):
        input = '''Class _:w0qs_60{}Class j:Q{Constructor (_:Array [Array [Array [Array [String ,0b1_10],68],0x56],036]){Var _,r,yI7,w:_;}vlP_8a_(){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1621))

    def test_1622(self):
        input = '''Class _{Var $6,$_:Int ;}Class qN{}Class __4{Constructor (__C__K_,w_,J,moW6_:p;a2,__6,z3,l:Float ){Continue ;}E(){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1622))

    def test_1623(self):
        input = '''Class _{}Class SG:T__2{Destructor (){}Destructor (){Var _L8:Float ;}Constructor (C:Array [Array [String ,0b1010100],0466_5]){} }Class JF____u{}Class _G7_j:B{E1(_:Boolean ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1623))

    def test_1624(self):
        input = '''Class _x__:b{Constructor (K_Q:L;s__,j,xs19:String ;v_K__,D,h,Y:Float ;i,c:_7J;__:Array [Boolean ,0636]){} }Class T_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1624))

    def test_1625(self):
        input = '''Class H_D:g{Constructor (_0,_i,EX_:Float ;O_0R,__,_r,_,I,_:Array [Array [Array [Float ,0b101000],0115],0x4]){Val L,__8,__:Array [Array [Array [Float ,9],9],01616];} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1625))

    def test_1626(self):
        input = '''Class t{Var $_,$4:Array [Array [Array [Array [Array [Array [Array [Array [Boolean ,6],025],0x1B],7_5_87],8],0x1B],075],9];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1626))

    def test_1627(self):
        input = '''Class t:s{Val $YL,x_,$9_:_;Constructor (_8_7:Array [Array [Array [Array [Float ,0xA3],0XA],02],85];R0:Int ;A654:Boolean ;_,e:Array [Boolean ,3_41_7_7]){}Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1627))

    def test_1628(self):
        input = '''Class _:__{}Class _SX:i__{}Class K:_{}Class _:o{Var $_b,i,$_k,g,$C,$C,$04:Array [String ,0B1];}Class _{}Class _4_qD86{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1628))

    def test_1629(self):
        input = '''Class P7{Val Pv:Array [Array [String ,33],026];Val $8:Array [Array [Array [Array [Array [Array [Int ,0b1],4_87_6],0x3D],026],33],0b101001]=q_U_::$Ff_!=!BHs0::$_3.J1*!--_2J8_::$_M();Constructor (_,_P_jzH7,_B:Array [Boolean ,33]){}Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1629))

    def test_1630(self):
        input = '''Class __:_{}Class l7VTj_:x2u{Var $I:Array [Array [Array [Array [Array [Array [Array [Array [String ,0b11001],28],0642],0131],7_2],0B1011001],0X3],0X1F];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1630))

    def test_1631(self):
        input = '''Class _{}Class _3:c{Constructor (N__a_3:Float ){}$97(_n_:Array [Array [Int ,0x78_C],93]){Return ;} }Class _:vA_Y_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1631))

    def test_1632(self):
        input = '''Class A__{e(){}Constructor (__Z,_,_,_,S:Float ){}Val e49,$w3N,_,$43n_z:String ;Var $_:Array [Array [String ,0B1000011],0x6];}Class o_u:g_qVEZz{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1632))

    def test_1633(self):
        input = '''Class __M06{}Class x{Destructor (){}$8(S:Int ;b6___vq,a_J,oZ:l;Z,_f:Array [Boolean ,37];y,_:Array [String ,0B110];E:Boolean ){Return ;Continue ;Return ;}Var Q_I_:q;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1633))

    def test_1634(self):
        input = '''Class TT:__k{_(){}Val $7_,$b,__k,_F5_:Array [Array [Int ,0X3],0b1_0_0];}Class _8{Constructor (){Continue ;{Break ;Var o:Float ;Continue ;}Break ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1634))

    def test_1635(self):
        input = '''Class Vz:nwdig_{}Class dM{Var __,h1,y7_:Array [Array [Array [Float ,0x9],40],5];Var $a_,$_475,$_YJQ_9:Array [Array [Boolean ,40],0117];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1635))

    def test_1636(self):
        input = '''Class x:_{U(O:Float ;F,b,_,O_,t,_,k:String ;__:Array [Array [Array [Array [Array [Int ,0xCE0],60],7_6],60],0X8_478];_I_:Array [Array [Int ,0X16],05];g,__,hB,_:_G){Return ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1636))

    def test_1637(self):
        input = '''Class cUviE9{Constructor (_,W,v,_:Array [Array [String ,41],0B10000];_c:_;XW6_1,_,qwu,j:Array [Int ,41];_0d__t:Float ){} }Class _:t{}Class HK:z{}Class ___8{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1637))

    def test_1638(self):
        input = '''Class _:_n_3_{___(g:Int ;b9_BT1154:Array [Int ,52];r,F,_z:Boolean ;x,_2,_,u:_){}Var _,$7l:Array [Boolean ,0x6_A];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1638))

    def test_1639(self):
        input = '''Class _0_:__{Val $_,___72L,XKO24,$761y,M:Array [Array [Int ,0XF],066];Destructor (){}Val _3:_0m;Val $19k:Boolean ;}Class _4c392:y5{Destructor (){Continue ;} }Class P{}Class _{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1639))

    def test_1640(self):
        input = '''Class _{}Class g:U3J{Val _:Boolean ;Val $_:Array [Array [Int ,044],42];}Class z_s3K:L_{$_I_G(){} }Class _C2H_:__7_r{}Class d{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1640))

    def test_1641(self):
        input = '''Class _:_q{$Jr(Z_,S_C__6,_,_P,__,g:Array [Array [Array [Array [String ,0142],0x5],0554],0x8]){}Destructor (){} }Class __a:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1641))

    def test_1642(self):
        input = '''Class Ai2:_{Val z:Array [Float ,176]=-_::$X();$54(O:qH;v:Array [String ,93];y:Array [Int ,0b1_00_1]){}_(){} }Class d1{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1642))

    def test_1643(self):
        input = '''Class _:_{}Class H3{Var $_9,$_1,_,X_:Array [Array [Array [Array [Float ,0XA_9_D4_64],030],01],0B1_1];Constructor (_,Y,g,_:Array [Int ,030]){} }Class i500:_{}Class L2{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1643))

    def test_1644(self):
        input = '''Class _8__O6__9m_f:Is{Destructor (){}Val $4,$Y_,s85u9,x:Int ;Var $eS:Array [Array [Array [Array [Array [Int ,03],0B1],07_4_0],063],06];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1644))

    def test_1645(self):
        input = '''Class z:__511{}Class o{$_FF_r(){} }Class _{Var $9QlSt:Float ;Constructor (_,_:Boolean ){}Var $fj,$_:p;}Class _L9:L{}Class _{_3__(){}Val $_CS:Array [Array [Array [String ,0B1000011],0B1000011],0X28];}Class G_{}Class EM:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1645))

    def test_1646(self):
        input = '''Class _:_6_{Constructor (KJy7,_2_m_:_1_;R,F,_8,_:u;L,_,Th0,R5pDf:Array [String ,6]){Return ;Var _0_:Array [Array [Float ,42],06];}Constructor (){Return ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1646))

    def test_1647(self):
        input = '''Class K{Val $2:Array [String ,0X5_B];_3Z(g:Array [Array [Array [Float ,0x8],062],0B11110];_9,_,iEvj:Array [String ,06];WV:Int ;_kb,K,w,o5,L:Array [Float ,4]){}d___(kX_,a_:Array [Array [Array [String ,2_5_97],02],0x8]){}Var d87_,_2,__E:_3;}Class _6:a{Constructor (_,Q0_:__;K4:Array [Int ,22];_:String ;A,x,_,n_:_E;W8:b_;_:Array [Array [String ,0x8],22];M_,X,Y:X;__2S:Boolean ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1647))

    def test_1648(self):
        input = '''Class _:Jk{Val $_,$7_o,$_T:Boolean ;}Class R:__9{Constructor (){}Val $_,$1:Array [Boolean ,0b1];Var T_:String ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1648))

    def test_1649(self):
        input = '''Class _:Fs__B63__T{Val $nz,$ga,mQ0:Array [String ,46];}Class __:X{$R6_8(){} }Class _H:_{}Class _4{$_6B(){} }Class _{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1649))

    def test_1650(self):
        input = '''Class k{Var y,$_,$_1,M4_:String ;}Class __:_{Val _0,$9:Array [Array [Array [Int ,34],02],0X1];}Class q:__f{}Class E_:_V6y_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1650))

    def test_1651(self):
        input = '''Class O_a{Constructor (___,c3y:Array [Float ,0X6];_,_q9w:Array [Array [Array [Float ,1_3_2],01],0117]){Var b_,_:Array [Float ,01];} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1651))

    def test_1652(self):
        input = '''Class _2:g{}Class i2:_40{$324(_,_70:Array [Array [Float ,9_8],0B1];_g:Int ;Z,p_:Array [Float ,0B110000]){}Val $24153hF,J:l;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1652))

    def test_1653(self):
        input = '''Class _3:_D{Constructor (A:Array [Array [Array [Array [Boolean ,0x1],012],0X14],012];_:Int ;RF,_01,_,oh,_,__:Int ){Return ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1653))

    def test_1654(self):
        input = '''Class _{}Class _{Val $s:Boolean ;Val $4C:Int ;Constructor (V4_:jB;r____ux,_5,_8:Array [Array [Float ,6_8],19]){} }Class Q__s_:b{Var $s,__,D3E,$t_D,$m:Array [String ,0B110011];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1654))

    def test_1655(self):
        input = '''Class _:J4{Constructor (){}Q4(__8_C,G:Array [Array [Array [Boolean ,0B11001],0x4_1_0],0X64]){}Val _69,OQ,$_,Wq:_;$0(){} }Class dS{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1655))

    def test_1656(self):
        input = '''Class p{U(f:V){Break ;} }Class _{Val _v,$_:Boolean ;__3CN(_,U2:Array [Boolean ,035];fo_,T:Array [Array [Array [Array [Array [Array [Array [Array [Array [Array [String ,80],80],0X4],9],035],035],0x3D],0b100001],0b1],0XE]){}$_8_(__:Array [Array [Float ,0x3D],80];UAP,_,_3_,M:Array [Array [Boolean ,0B1_0],0x3D]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1656))

    def test_1657(self):
        input = '''Class ZUff{Var __,___,r,n,$uJ_,$R,$_:Array [Float ,057];}Class j:O_{Var _,$97,$_b:Array [Array [Float ,02_33_13],057];}Class _a{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1657))

    def test_1658(self):
        input = '''Class G2:W{}Class _:V{$_(){}Destructor (){} }Class _Ib{}Class F{Constructor (_:Float ;_:Array [Array [Array [Float ,014],0b1_1_0],014];z_:n__q2){Continue ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1658))

    def test_1659(self):
        input = '''Class a2:l{Val ZLv_0N_9N,UM:Boolean ;Var $i:Array [Array [Array [Array [Int ,0b1011100],0x3_B_C_5_2],0x1A],0B110100];Val J:Float ;}Class O368:__W78{}Class Nq_66{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1659))

    def test_1660(self):
        input = '''Class _:O{}Class Tv_7:A{Constructor (HW,_,_:Array [Array [Array [Array [Array [String ,0x3],78],0B100111],032],05];_,_9:g){Continue ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1660))

    def test_1661(self):
        input = '''Class Ar:_h_{Var $7,uh5,$F,$_d,y,$T,l:String ;Constructor (){}$z4n(){}Destructor (){} }Class _{Constructor (__T_6q,_,__D,p:Array [Array [Boolean ,0b1001010],0X3A]){Break ;} }Class _1k6n_:_{}Class B_:R82D7__{}Class E{Var _,_0F,$F,$8__6w,$_:Int ;Var _:Array [Int ,066];_(){Break ;Continue ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1661))

    def test_1662(self):
        input = '''Class _p{}Class _yi{}Class _{Val M,$_,$Md:Int ;Var G:Float ;$_4(){I::$j();} }Class __:__{Var _8,$W__dZ5_25,T_L_,$9o,$gP__,$0,$_65dWW_,$_S:Array [Array [Array [Float ,0B11101],0x1B],077];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1662))

    def test_1663(self):
        input = '''Class y:__n{Destructor (){}Destructor (){} }Class o_:_{Constructor (){} }Class u{Constructor (_:o){}Var $3:Array [Array [Array [Int ,6],0b1],14];Constructor (f,_9_X:Array [Array [Array [Array [Array [Array [Array [String ,03],0x54],0B1],0X97],14],03],0b1_0];_:Array [Boolean ,0x54]){} }Class D:_{Constructor (MN,i9___8:v4__){Continue ;}Var _:Boolean ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1663))

    def test_1664(self):
        input = '''Class _{Var $x:Float ;Constructor (){}$6Y(){}Var d:Array [Int ,7];}Class _:T_R4I{}Class _:__{Var A,$7_,$__:Array [Int ,02_0];}Class M33:v_{}Class E{}Class _:u{}Class _f_6P6_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1664))

    def test_1665(self):
        input = '''Class __:j{Constructor (_:Array [Int ,0X17];P:Array [Array [Float ,0B1_0],0b1]){}Val N:Array [Array [Boolean ,02],0B1_0_1];}Class o___5_v_U{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1665))

    def test_1666(self):
        input = '''Class L:_HA{}Class _{T(_,e_06:Array [String ,0b10_11]){}Constructor (l:String ;R:i;__9:Array [Array [Float ,0b1],0X1];_,K,_:String ){}Var $3:__t;Destructor (){}R792(){} }Class q_5{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1666))

    def test_1667(self):
        input = '''Class _7{}Class _5O{}Class B88J{Destructor (){Null ._();}Var _:Array [Boolean ,0123];Constructor (_09:Array [Array [Boolean ,8_4_9],33];_,R_:Array [Array [Int ,0b10],0B1110]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1667))

    def test_1668(self):
        input = '''Class _k:t395{yi(_,N,_,_5:_6;__3PL_:l;_:Array [Int ,0b110111]){}BYU(__,li_:_;TM_8_:O){} }Class q6{Var $8,$_M:Int ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1668))

    def test_1669(self):
        input = '''Class _3{_(zn8,_X_,C2:Array [Array [Array [Array [Array [String ,02],0b1100100],0b1100100],0B101000],0x9];xQ:Boolean ;_:Array [Array [String ,17],17]){} }Class l{Val $pfK_hU:Igg;}Class _{Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1669))

    def test_1670(self):
        input = '''Class l:Y_{Var __:Int ;}Class HD45D_9F{Destructor (){}Val O,$3_hY__,O__3b,V7__q6:_;Constructor (m,_,U_N,_6_:V_z;M9,_,_:Array [Int ,2]){} }Class _{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1670))

    def test_1671(self):
        input = '''Class V1{}Class T:k{}Class _{Val o_:Array [Boolean ,42];}Class _:L{}Class _:Z4{$_5(E_4_F,G_b,q_36_7Km:Int ;_:String ;_1_,___3:String ){}Constructor (__,__l,ab,v8,_,J,p,_,__:Int ){}Destructor (){} }Class W{Val $__c8,pB,_:Array [Array [Float ,0x5E],0b1];Destructor (){Val _,P:_;}Var C_:Array [Float ,0X11];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1671))

    def test_1672(self):
        input = '''Class _m{}Class m{}Class V:__{}Class _:_{}Class D{}Class i78_:I{Constructor (_,_N_,k,_:Array [Int ,92]){}Var $l:__;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1672))

    def test_1673(self):
        input = '''Class _{Var it,z42__:_;}Class ___1:_{Val $C_k3,Y0_,n_:_9jS_3;Destructor (){}Var $4,O:Array [String ,070];T(){Continue ;Return ;}Destructor (){} }Class N{Val T_:String ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1673))

    def test_1674(self):
        input = '''Class _:M7_{l(_:Boolean ;_,_0:_;_,o,L,L,_,G__F_,Tb_,__8,_,_,_:String ){}Val $_9__8:Array [Array [Array [Float ,5_93],0B111011],0b100101];}Class U3{}Class _w{U(_:Array [Array [Array [Int ,03],5],0B11];q6:_;_:Array [Array [Boolean ,5],0x5_1_31_D];t_:Int ;w:Array [Array [String ,05],0X56]){}Constructor (Q,N2,u:_;s_E:String ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1674))

    def test_1675(self):
        input = '''Class Dn0405:X{}Class G9:_{Var _K6,$4,r:Float ;Constructor (__,_p3QWu,__:Array [String ,72_8]){}Var d,E:Array [String ,79];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1675))

    def test_1676(self):
        input = '''Class _:_{Constructor (_,Z,s__:Int ;_:Boolean ;_1kZG98:_X_L;v_,k:String ;C9:Array [String ,0X12];_G_,d,_:__p){} }Class F:n{Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1676))

    def test_1677(self):
        input = '''Class _6:_{Constructor (_:D){ {__7fE::$B3();} }}Class _{}Class D:H_4I{}Class __:_{Var $5,_c:__;a(C2,_0:YFK;_:String ;_,sL:Array [Float ,0B11]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1677))

    def test_1678(self):
        input = '''Class jI4{}Class _k_:__{Constructor (w,X,s2mU:Float ){} }Class wo{}Class GX{Val $N8:Array [Array [Array [String ,0423_3],34],86_3];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1678))

    def test_1679(self):
        input = '''Class J:j{Val $T__,$5,__2:v;}Class _6_{}Class ____y{Var $_:_;}Class yp{$_(){}Var $61:Array [Array [String ,73],0x2];}Class M_Un6{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1679))

    def test_1680(self):
        input = '''Class ____:d_{Constructor (O__,Z:Boolean ;_:Array [Array [Array [Array [Array [String ,4],0b1010001],0x5F],0XE],054]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1680))

    def test_1681(self):
        input = '''Class __:__{t(_,Cm:Array [Array [Float ,29],54]){} }Class _0_{}Class A_J_:_{}Class _:F{Constructor (_,__:Array [Array [Int ,056],0b11]){Return ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1681))

    def test_1682(self):
        input = '''Class o{$_q(_6:Float ;_,s:__;J65__:Array [Array [String ,011],0b11];_tQ,__,sxW7Qv,H,B,l:Array [Boolean ,0B111]){} }Class _2:v{$6S(){} }Class j:_TQ3{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1682))

    def test_1683(self):
        input = '''Class m:B{Constructor (_,q_:Float ){}Constructor (_:Int ){} }Class z:g{Var _W:Array [Array [String ,0b1],0310_5];}Class _{}Class BG_72_E4D7:_F_{Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1683))

    def test_1684(self):
        input = '''Class CC36:T_q_JL_{Constructor (){}m(){Return ;ag::$R();} }Class _{}Class _E:s__{}Class R{Val _:_70;}Class _{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1684))

    def test_1685(self):
        input = '''Class _657:S_u4A{Constructor (oi:Float ;q,w_:String ;G1,T3k1,_1s,_16_:Array [Array [String ,0xD],83];_,_,_B,t:Array [Int ,035_52_6_4_7_052];_:rM0;h:BK_;__,_:Int ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1685))

    def test_1686(self):
        input = '''Class _{Constructor (cPRM,_I0_,YZ,I,j1:___;__:Array [Float ,0B1100];d:Array [Int ,0b11000];x:_;_K:Boolean ;_:String ){} }Class _A_:u_P_{}Class lp:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1686))

    def test_1687(self):
        input = '''Class _:z_{Constructor (G:Float ){}Val _1G_8,$2,$0,$4u,$__,_L4D_N_:q;}Class X:_{}Class o{Destructor (){Break ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1687))

    def test_1688(self):
        input = '''Class f{_(){} }Class _{ocfG3_5(_,a,_,a__:P;z:Boolean ;_BO,_:Boolean ;__:Array [Array [Array [Array [Array [Array [Array [Array [String ,16],4_3],0b1001],0b1],0x3],0b1001],0b1],07];_,u:x;l_:_;x09:u_){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1688))

    def test_1689(self):
        input = '''Class I:_{}Class v{}Class K:m{Val _2,m6:Array [Array [String ,80],0xB5149_6];}Class _{Var $M,_1P_J,bW,_E7L:Array [Array [Array [Float ,057],057],0xF];Destructor (){} }Class _{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1689))

    def test_1690(self):
        input = '''Class M_{Val z,$_,$_9:Array [Array [String ,2],0110];b(i,_:c;U_:A;Z:String ){} }Class _7q{}Class e715g{}Class _{$85_Z(){ {}Break ;}$_g(_Y6:Array [Array [Array [String ,63],86],0X5A_9];V:String ;Q,T:Array [Array [Int ,0110],0110];_:x_){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1690))

    def test_1691(self):
        input = '''Class _:Y{Val $_2:Array [Array [Array [Int ,0XC],0x4B],0x4B];}Class of_:d{$_(_6w,__0,N_7,_,Q,u_:Int ;__Eg,e:Q8;__:Float ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1691))

    def test_1692(self):
        input = '''Class R_k70JR:_{}Class a2:x56{}Class _R:_{Val $77__i,sBG_:Boolean ;l(){HxUP::$3I();Return ;}Var $_0a,m,$K_F0:_;}Class hg:v{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1692))

    def test_1693(self):
        input = '''Class _o{Val $3,$90_:Array [Array [Array [Array [Int ,0X4],016],0B11100],07];}Class n_o4:N_{}Class _{}Class n_N{}Class rY{}Class n_9{}Class c:y{}Class _:_5W{Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1693))

    def test_1694(self):
        input = '''Class H3{}Class _2{Destructor (){} }Class _{Constructor (){}Constructor (p_Lf_:Array [Array [String ,0117],0b10]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1694))

    def test_1695(self):
        input = '''Class _:py{Var $F,T_2,$__:Array [Array [Array [Array [Boolean ,0b100],0b1],01],0142];Var $N___,_B,$B9C:Array [Boolean ,4_6];}Class r{Destructor (){} }Class _:r5{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1695))

    def test_1696(self):
        input = '''Class t:C{Xcd(_,B,_G,_9:_;N,_WY,_,_o:_I_dY4P6o;_,___:Array [Boolean ,06];K5,_,T8:String ;_1:Array [Float ,49];v:_8_4;HY_:Float ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1696))

    def test_1697(self):
        input = '''Class Q_{Var $6,D2,__,$7,$_,J84Z,_:ByJ;Var $c3,$_,__:Float ;Val c,$P:Array [Boolean ,96];Val $3,$_G,$sde4,$6,$yo:Array [Array [Int ,0x2_D_D_0_89],0b1];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1697))

    def test_1698(self):
        input = '''Class g{Var q:Array [Float ,0X7_B0];Var _,_,$6:Array [Array [Array [Int ,0b1_1],033],0B1001101];Var _45,$5,$_New__k2,q_88__,$6,$4:String ;}Class H_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1698))

    def test_1699(self):
        input = '''Class o:c3__{}Class i:__{Constructor (_:Float ;_hn,_:Array [Array [Array [Array [Array [Float ,0B1],87],040],87],0X8]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1699))

    def test_1700(self):
        input = '''Class _{}Class C:C0G_X{}Class To:l{}Class b{}Class __:j{Constructor (){_::$_();}Val __M:Float ;}Class R359m{Val $15_:Array [Array [Array [Array [Array [Float ,29],0X3],0x22],29],29];Val $0:Array [String ,047];Var c9:Int ;}Class _:s{}Class A{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1700))

    def test_1701(self):
        input = '''Class t{Constructor (__,_2f__:Boolean ){Continue ;Val Q:Array [Array [Array [Array [Array [Array [String ,0xA8],0132],8_5_1],72],0132],72];} }Class _V_:v{}Class _V2_:__d{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1701))

    def test_1702(self):
        input = '''Class G_:DN1h{Constructor (_,U:Array [Array [Array [Boolean ,0714],0b1_0],0x1E];_3F,b,_4,_,_1:Boolean ;_,OU,G0:Array [Int ,0b1_0];x:Array [Int ,9];T:Array [String ,9]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1702))

    def test_1703(self):
        input = '''Class _ork:_92{}Class _6_D{_(_:M__3;i,J_:Boolean ;__0:Float ;iD:Array [String ,0x5C]){Break ;}Constructor (){}Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1703))

    def test_1704(self):
        input = '''Class q:RS{_9_(Z,_,_:Array [Array [Boolean ,034_01],0XE];Z35z_1__2_l5,hb:Array [Boolean ,03]){}$_(){} }Class __{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1704))

    def test_1705(self):
        input = '''Class x:__{}Class L_I:U_{Constructor (_5M,_1B2:Array [Boolean ,9_34];_:h;_:I5;__:Boolean ;u,M_j,gK:w_;__K_:C_h;Z:_;_B7,__:Float ;___:___;n,_:Boolean ;_7_,_0_,_7Q:Boolean ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1705))

    def test_1706(self):
        input = '''Class _{}Class __:O{Constructor (__,p_W:Array [Boolean ,0b1];__72,Z,_N:Array [Float ,62_2];cx,_3_,G_:Array [Boolean ,0x1D]){} }Class _:X9{}Class p9_{Constructor (){} }Class _:_{Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1706))

    def test_1707(self):
        input = '''Class _7_:_{Val __7:__;}Class _{Constructor (){}Var $_:Boolean ;}Class H_{Var _7,$3:Array [Float ,0b10];$__5(){}_(C,Y:____){}$_(z_,M,UN,_:_SXoN_){} }Class _8VL:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1707))

    def test_1708(self):
        input = '''Class d{Constructor (Wf_c,U_:Boolean ){}Var $S:Array [Array [String ,033],01_6];}Class z:c{Val $_9,$v:Array [Int ,033];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1708))

    def test_1709(self):
        input = '''Class _v{Destructor (){} }Class GW{Destructor (){}Val $9,$6:Array [Array [Array [Int ,0x38],0B1100],12];}Class _:Nl{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1709))

    def test_1710(self):
        input = '''Class U:Y3{Constructor (_,o:_;v:_;C:Array [Array [Array [Array [String ,0XB_C_D],58],9],0123];T,jiU,_:String ;_,__9,G:Float ){Val _2n_:Array [Boolean ,0B1_1];Continue ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1710))

    def test_1711(self):
        input = '''Class _{Constructor (){}y(__3,R,_7_,_,o,_:Array [Array [Array [Float ,0b101011],03],0b11]){}Var y__:Array [Boolean ,0XD];}Class _:d{S(){}V(){Continue ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1711))

    def test_1712(self):
        input = '''Class q3:_{_(X,TrP:Array [Array [Array [Array [Array [Int ,0b1],99_5],7],0X1],0130]){}Var h:Array [Array [Array [Array [Array [String ,0B1010101],01],0b1_1_0],0B1],02_4];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1712))

    def test_1713(self):
        input = '''Class m{$74(){Return ;}$p9Z6(){} }Class r_W:_{}Class _:UV_3{}Class q{$F_f(p:Int ;YIrRgACN6V:Int ){}Val u:Array [Int ,0X1F];}Class _{Var $985,$B1,_,E,e7_,G:_t;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1713))

    def test_1714(self):
        input = '''Class __:_{}Class q:W5Q_{}Class s_:am{Val $c,_k,I,$_,$N:Array [Array [Array [String ,0X8_9],0X6],3];}Class _:_g_{}Class _AQ{Var fc0,$B:Boolean ;Destructor (){} }Class __c:U{Var _,n_,z,B_a:Array [Array [Array [Int ,0X1],0104],0x57];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1714))

    def test_1715(self):
        input = '''Class __{}Class W31R:j_{Var $VHF,_84R:Array [Boolean ,0X6_1_0C_F];$1_4(){}Constructor (A7UD8:Float ;_,_4:eo_1B7){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1715))

    def test_1716(self):
        input = '''Class _4:_{Constructor (__,_61,m,f_9_0:Array [String ,0b1];q:Array [Array [String ,0x1],0x2A];_2_:__){}w(){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1716))

    def test_1717(self):
        input = '''Class _:_ky{$P8(_:M;G,V3__190S:Array [Array [Array [Array [Array [Float ,0x7],074],0B1011101],0B1],1];_Q__,_4,o_:Boolean ;__:Float ;_N,_,_:F_7;A:Int ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1717))

    def test_1718(self):
        input = '''Class _0:b_UK{}Class _{Constructor (Q,_,__16,___,GxW_,_:Array [Array [Int ,100],070];W_,Wg,_K,L_:__;_i8:_;Y8,b:_;Q__5,_:Array [Array [Array [Boolean ,015],015],0B10010];o50j,kG:Boolean ;L_I,__rU,ZK:I){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1718))

    def test_1719(self):
        input = '''Class __V__:i{Var z,_,_:Array [Int ,06];}Class __{$k(){}Var $5_:_;Q(_,Mo:Array [Array [String ,0B1],0X55];_9_,__,f:String ;N0,_:Boolean ;p:WB){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1719))

    def test_1720(self):
        input = '''Class _{Val S,z_:Boolean ;Constructor (_,XM:a2;i_,LN,__Y_6_9P,__,o_:PZ;_:Boolean ;__4_I:_3){} }Class _:_{Constructor (){Return ;}Val _v,$9:Array [Float ,0X3C];Var _,$M9e:Array [Int ,34];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1720))

    def test_1721(self):
        input = '''Class _:D{Val _0,H,$1e_,$4,_:b7;}Class _4:L{}Class C:k{}Class s_{}Class C:f{Destructor (){} }Class _:_{$_(_,f:Boolean ){}Constructor (){}Val _,$E,$X,_,$0,$w7L,_:Array [Boolean ,0X3];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1721))

    def test_1722(self):
        input = '''Class _{Constructor (K,i__:Array [Array [Array [String ,81],0x6],0B1];H:Array [Array [Array [Boolean ,0b111],0B1],01];_:Boolean ;L:Array [Array [Boolean ,0X5_5],0B1_1_0_0];W:Array [Array [Float ,06],4_4];_:J0){}Constructor (K9:Array [Int ,0xD_2_A];_9:Array [Int ,81]){Return ;}Val _2,$q43,_,$_O:Array [Array [Int ,05_1_2],064];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1722))

    def test_1723(self):
        input = '''Class __:__U{Val $E,x,m:Array [String ,0b11_1_0];Destructor (){}Constructor (_,_,P:_Q904V;_,_:_){Return ;} }Class _:o{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1723))

    def test_1724(self):
        input = '''Class _3_Y{}Class _:_{Constructor (_5,_75j4,_,_:Array [Int ,0X2_9];_:_;Fp:_;k_:H;wea11_:Array [Int ,0X4];_,_:Array [Array [String ,0b1],0x7B_41]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1724))

    def test_1725(self):
        input = '''Class s_:_{}Class cW{Var $_:_=!!!!!!!!--_::$_()._._.k();Destructor (){}_(){ {}Break ;}Val $g,$G,$p,$_3,$M_,$2:_7;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1725))

    def test_1726(self):
        input = '''Class xU{Val x6T_b_:Int ;}Class C__FA{Constructor (WG:Array [Array [Int ,53],0X5_9]){Val _:Array [String ,0XD];} }Class __S{Destructor (){Continue ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1726))

    def test_1727(self):
        input = '''Class __:J{U(Z8:Array [Array [Array [Array [Float ,6128_08_95],03_4_1],65],0B1010111];_,H0,_:String ){} }Class u_cg{}Class F9:_{Constructor (_L4:String ){Continue ;} }Class j7__1{Destructor (){} }Class _7:t{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1727))

    def test_1728(self):
        input = '''Class g6:_8_{Var K_7,Za,V,$j,$_:Array [String ,9];}Class _{Destructor (){}Var $1_,$8_,e_2,$_,_:Array [Float ,0XF7_F];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1728))

    def test_1729(self):
        input = '''Class _:o8T{}Class _3{Constructor (_,i_h:v;_4:Array [Array [Array [Boolean ,02],0144],0B1010100]){Val _,e:_;}Var kR___96,Y52_z,$X0_x4:Y7_;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1729))

    def test_1730(self):
        input = '''Class hj{Constructor (_l,E:X5;_,_,d:Array [Boolean ,0x6];n,a,_,_T,__f:_4;__,_a,Px,x,R___,DN:Array [Array [Boolean ,83],0X8];_82_:Array [Array [Float ,0B11010],0X52];y,_:Array [Int ,06]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1730))

    def test_1731(self):
        input = '''Class _g_{Destructor (){}$kk(_,_93_IZqX59:_y_4_;_,O,i9,HV:_;_US:_691){} }Class _:_{}Class _HO:_{Var h:Float ;Constructor (___,__S0_:Array [Array [Array [Array [Array [Array [Array [String ,0x84],17],0B1010000],076],03],0b1],3];u:D7){} }Class D:_{}Class M4:o{}Class _6{Constructor (_:String ;O:String ;O1_81,O,k,_0:Array [Boolean ,0X8];KQ3:_4_;T_:Array [Boolean ,0X4C]){Continue ;}Val $0,$5:Array [Boolean ,0b1001111];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1731))

    def test_1732(self):
        input = '''Class Jg_1:o{_(a:String ;_a:Array [Array [Array [Array [Array [Array [Boolean ,2_149_24],8_2],0x43],89],0B1100000],0x64];_9:Array [String ,0b100101]){} }Class _49_T{Destructor (){Return ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1732))

    def test_1733(self):
        input = '''Class b:____{Constructor (_,___,Z,z32t8:Float ;U,_,A,_,_,V:Array [Array [Array [Float ,0b1_10_0],0b1_0],030];B,_:Array [Array [String ,0xD],9];T7:Array [String ,030];M:_){} }Class _:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1733))

    def test_1734(self):
        input = '''Class _:b4w{}Class _tNQ9_93j2i3rx5j{Var ___2,j_gf,jQB:Boolean ;}Class _V{}Class _:_1E{Val _5,C:String ;}Class B4c_:H{}Class _6:U{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1734))

    def test_1735(self):
        input = '''Class _{M_8(VN0:Array [Array [Int ,73],0b1_01_0_11];_u:Float ;_2,E,_n,_t:Array [Array [Array [Float ,0b111],07_3],0b1_1]){ {} }}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1735))

    def test_1736(self):
        input = '''Class _:yv{Sy(c,_4:Float ;iH,_:Array [Boolean ,0xEAC]){Break ;}Var a8:Array [Array [Array [Boolean ,30],0B1000011],0B1_1];}Class nx{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1736))

    def test_1737(self):
        input = '''Class _{u_2650_4(_:Array [Array [Array [Array [Boolean ,0x5],014],014],0B10110]){} }Class I{Constructor (){}Var $_,N,$6,$9:Array [Int ,0x5];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1737))

    def test_1738(self):
        input = '''Class J3:s{}Class _:FY{Constructor (_:String ;g:Int ;_:A;n3_:Array [Float ,0x4E]){} }Class _{$_5_0(){}Val _7j,$2B:Boolean ;}Class _{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1738))

    def test_1739(self):
        input = '''Class e5_{Var $x:Boolean ;}Class _:_g91w_{}Class o:J{$y(_,_g,T7:Array [Int ,0x7]){}Constructor (){}Constructor (){}fI(__,_18m,_,_:_6jae_V8){}Var $_tN6,_jva,$_,_3_:_5d;}Class _:__{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1739))

    def test_1740(self):
        input = '''Class W{}Class _:S{_(){}Var F,_,$0:Array [Int ,0b1_000_00_11];$Vt(_:Boolean ;Uc10_:Array [Array [Boolean ,0144],0x26]){}__(){Var n:Float ;Continue ;Continue ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1740))

    def test_1741(self):
        input = '''Class _:H{Constructor (_:OK__1_CR;y:Array [Array [Array [Int ,0x3],0X6_6],64]){_::$_9_();Continue ;Continue ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1741))

    def test_1742(self):
        input = '''Class __{Constructor (f:s_R;_,y:Array [Array [Array [Float ,0xF],50],07_1]){}Constructor (){}Destructor (){} }Class _{}Class _8d_{}Class _{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1742))

    def test_1743(self):
        input = '''Class n:_{Destructor (){}Var $7_8,$_9N:_;Zm4_3(_sMy,_b,_,_:String ){H__::$8().t();} }Class hbt:z__{}Class _9{}Class Z:_kl2{Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1743))

    def test_1744(self):
        input = '''Class _:MXu{Constructor (__:Array [Boolean ,07];_,_,_,iv_6,B91_:Boolean ){} }Class _:_{Destructor (){} }Class k{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1744))

    def test_1745(self):
        input = '''Class _:V_{}Class v{Var $4H,$L,$7:Array [Array [Array [Array [Int ,0766_2],07_0],0B1011111],77];Val _:mV;}Class J0_{Val $_:Int ;Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1745))

    def test_1746(self):
        input = '''Class _M_91{Constructor (){}mrw(Mn_,_,_Gk:Array [Array [Array [String ,2_4_0_99],0B1],0103];_:Array [Array [Int ,52],0X5_1]){} }Class e{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1746))

    def test_1747(self):
        input = '''Class G{Destructor (){}$6(b:Array [Array [Array [Array [Boolean ,0b1001000],0B1],0x11],0b1001000]){}Var _6:Array [Int ,0b1];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1747))

    def test_1748(self):
        input = '''Class AHH:j{}Class z8mq{Destructor (){}Constructor (T,_:_;De77,a8,G,A,_z:Je3;X:Array [Float ,0b1];x0,_:Int ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1748))

    def test_1749(self):
        input = '''Class _:_X__{Constructor (c2,_:Boolean ;_:Array [Array [Array [Array [String ,0b1],0X967],44],44]){} }Class V9_y{}Class M{Var _:w;}Class _X:_{Val S:String ;Var $x3:__;}Class EFrD_5G:_X{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1749))

    def test_1750(self):
        input = '''Class R{}Class Lm7{Destructor (){}Destructor (){} }Class __j{}Class __{Var _2,$1XN,$J_,__,U,_8___:Array [Boolean ,0b10_0_1];}Class d{Val $4J6_:Array [Array [Boolean ,5_8_9_5_2],1_5];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1750))

    def test_1751(self):
        input = '''Class __4:L{Constructor (jY_4,_,O,_4Y,O9O_,_,f,_:Array [Array [Array [Array [Array [Array [Array [Float ,7_8_9486],0XA],6],0b10_0],0x15],73],071];D,s_:_){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1751))

    def test_1752(self):
        input = '''Class _{Var C:Array [Array [Array [Array [Float ,0xD_F_2],020],0B11000],0x23A_E_4];Constructor (){Continue ;}Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1752))

    def test_1753(self):
        input = '''Class X{}Class AP{}Class B{Destructor (){} }Class K:_C_2{Val $T8O4:C_;}Class t:c{Val $t,$H,O3:Boolean ;}Class E:jX{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1753))

    def test_1754(self):
        input = '''Class z{U(){}$3(){} }Class _:t{Constructor (_8I:Float ){}Constructor (){}Constructor (_,iA:String ;BRXm7_:Float ;__:w_7V_;v9,_,__g:Array [Array [Array [Array [String ,1],0B1],05],0b11];_:String ){}Val $6_:Float ;}Class k{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1754))

    def test_1755(self):
        input = '''Class _:v{}Class f:o7_4{Constructor (){Continue ;}Val $c,$__,_:String ;Constructor (G,F_Da3,f0:Ih0;_,SS:Array [Array [Float ,0x2_8_1],8]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1755))

    def test_1756(self):
        input = '''Class _:A{Val $Xb:Array [Array [Array [Array [Array [Array [Array [Array [Array [Int ,0B11010],0141],0B11010],6],51],2_6],0b1001100],8],51];Val $7:Array [String ,0X7B];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1756))

    def test_1757(self):
        input = '''Class K{}Class _{$_(l_:Int ;_:_;_,_:Float ){}Val g:Array [Array [Array [Array [Array [Array [Array [Boolean ,0x43],11],11],11],11],04],01];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1757))

    def test_1758(self):
        input = '''Class _3{}Class D5___4:o_11{Constructor (){Return ;}Var $_,$9,$_Q_V,_,y,$2,$__57__:Array [Array [Array [String ,0b1_1],0B10110],4_09];}Class _:__{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1758))

    def test_1759(self):
        input = '''Class I76:_jh6_{Var $L__W_,M_:Array [Array [Array [Float ,0B1_110],0b110101],42];Constructor (h8__:Float ){} }Class x:Y{}Class k1N{Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1759))

    def test_1760(self):
        input = '''Class W3{}Class _:_z4X_1{}Class S{Constructor (){}Constructor (_:Array [Array [Array [Array [Array [Array [Array [Array [Array [Array [Array [Array [Float ,94],94],0xB],0B1],0X5B],0xB],0xA7],94],0131],04_1],023],0131];K0,el___:Array [Array [Boolean ,0X4],1];_0,A8_,_P,p___T:Float ){} }Class _06:N_{}Class _d_:U{}Class g{}Class Dk{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1760))

    def test_1761(self):
        input = '''Class _:_{Constructor (_9:Array [Array [Array [Array [Boolean ,4],03],0B1100000],022];F:Array [Array [Array [Array [Array [Array [Array [Float ,07_4],59],59],3],0X20],59],0b1]){}$FW_(){} }Class _:y8{Constructor (_,T,_:_){} }Class _{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1761))

    def test_1762(self):
        input = '''Class L7:e_{Val pN:Array [Array [Array [Array [Int ,0X9E],0X2_F_8],0X4C],41];Var $9,$L,$Y,$G_,$mS0e,i:String ;Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1762))

    def test_1763(self):
        input = '''Class O_{Val ___U,$_I7T:Array [Array [Array [Array [Boolean ,0X6],0X9C1C9],0B101],0x50];Var _aP,$bC:Array [Boolean ,0B101];Var $a:L6o___;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1763))

    def test_1764(self):
        input = '''Class _{}Class _{}Class Q{Val $6_k_:Float ;Constructor (w:Array [Float ,0B1];j:String ;_,rk_:__){}Constructor (_:Array [Float ,10];U:String ){}Val $_Rd:Int ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1764))

    def test_1765(self):
        input = '''Class s_:_{Var _b,$_A,u_,$A7:Float ;Constructor (_,D:Array [String ,0B1000110];_:Array [Int ,0703];__4:T){} }Class Q{}Class y9{}Class Y{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1765))

    def test_1766(self):
        input = '''Class kS:_{}Class v_{Val _,_,__PP,$5,_,$6:__D;$697N(o4_:Array [Float ,0X3_3];_:String ){}Constructor (){Continue ;} }Class T:_{}Class _:T{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1766))

    def test_1767(self):
        input = '''Class o6:qRp7T{Val $9:String ;Var E,$G_:Array [String ,04_1_0];Var Q9,_:d;Constructor (_,_:K6;k:S0_){} }Class _{}Class _95_:__{}Class T{}Class a{$D(i0A,_:Float ){} }Class FN:L{}Class _X35:_{Var $_:Array [Array [Array [Float ,025],0XA_4],9];__(__:Array [Int ,0B111110]){}Constructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1767))

    def test_1768(self):
        input = '''Class j{}Class _:___{}Class D:_{}Class __Cy{Val $_:Array [Array [String ,0103],13];Var $898:Array [Array [Array [Array [Boolean ,0B1_00_0],0b1010011],0B110],0b1];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1768))

    def test_1769(self):
        input = '''Class I:_{Var $_9w5:Array [Array [Float ,0B101000],69];S__(_G:Boolean ;P,_:Float ;__:Array [Int ,0X4F]){}__(I,A9K_:String ;A3,_:Array [Array [Array [Float ,0B1],93],0XD_1_C];_:w;U:Array [Float ,69];M:_;S,Q_:Array [Boolean ,01];_N,g_:Int ;_H:_;_:Boolean ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1769))

    def test_1770(self):
        input = '''Class cL:M8{Val N,_:Array [Int ,0X16];___E(_:_h;u,_9W__2rp_j_l,_,_,i,H_s:_){Var s,_0_:_;} }Class __XM6g{}Class __Y{Destructor (){} }Class g{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1770))

    def test_1771(self):
        input = '''Class _{Val i_:Array [Int ,05];}Class i33:_{}Class DGZz9:_Md6{Val _,_R0:Array [Array [Array [Array [Array [Int ,0x3A],0b1100000],0B1011011],0b1100000],0x3A];Var _:RJ;}Class rS7:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1771))

    def test_1772(self):
        input = '''Class _75:_4{Var _,G12,$_:Array [Array [Array [Array [Array [Array [String ,06_6_1],8],0x8],0b10],0x64],7];}Class d:QL{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1772))

    def test_1773(self):
        input = '''Class B{}Class _{Constructor (R1_7:Array [Array [Array [Array [Array [Array [Array [Array [Float ,0144],0x2D],0x6E],0144],93],0B11],0x2D],0b1_1];g1,H:K2;_:e4__;_:String ){}Var $5S_R:Boolean ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1773))

    def test_1774(self):
        input = '''Class _:p{}Class o:Z{c(){}d___b(_,_o_:Array [Array [Array [Array [Array [Int ,07],06],0B1],0XDE34_9],0x8]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1774))

    def test_1775(self):
        input = '''Class W_B:Y5_{}Class _g:Yk23_{Constructor (l__,_:Array [Int ,0B1011111];M,_:Array [Array [String ,0x2F],105]){Break ;} }Class Y{Constructor (_,F_:Array [Float ,0x2F];b,__q,A:String ;_:Boolean ){} }Class Wz556z:m_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1775))

    def test_1776(self):
        input = '''Class _{Val $tmER_:Int ;}Class _4ey:y_1{Var _7s832U0J,$l,_R,$5:Array [String ,0b10011];}Class t:_{Val _,$66_:Array [Array [Array [String ,0B1010101],0X49],5];}Class _O{}Class _{}Class c:i{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1776))

    def test_1777(self):
        input = '''Class b{}Class __:_{_(_u6,_,__p2:f;_7:Array [Int ,0B1]){}Constructor (C647_8_:Array [Array [String ,66],0b11];__:Array [String ,2_0_3_0]){}Var $J:Array [Float ,0x6];Val $70:_;}Class AN{}Class v_:_{}Class Q:_{Constructor (){} }Class A{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1777))

    def test_1778(self):
        input = '''Class p419{}Class _:_{Val $_k9u0:Boolean ;$D(_:Float ;_,_,Th25_,y:Int ;_3O,m7w,__:Boolean ;u_L,_:Array [String ,67]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1778))

    def test_1779(self):
        input = '''Class _6{Val e:String ;Val __m_,Nz:_W_28_3;Constructor (_J_:Boolean ;o,Q_:Float ;X_p:Array [Array [Float ,0b1],0X7]){} }Class _R{Constructor (){} }Class c{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1779))

    def test_1780(self):
        input = '''Class X{$C(_BA,F:Array [Array [Int ,0b11_00],0xF];d_:Array [Array [Array [Array [Boolean ,0X2E_4],0125],22],2_2]){Break ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1780))

    def test_1781(self):
        input = '''Class Ve4Y_:w_{Destructor (){} }Class _f__:w{}Class U{Constructor (i_,_,i8Vex,Z,___3G:String ){Val G,U8d:Float ;} }Class _q{Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1781))

    def test_1782(self):
        input = '''Class Y7:p{Constructor (_1:String ;_:Array [Array [Int ,41],0X59];w:Array [Array [Float ,0x7],01];s:S1){Return ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1782))

    def test_1783(self):
        input = '''Class R{}Class _:_{Var _w,$E:_;}Class w{$7(_,Yj__d6h41_,Q_,y_,_:Array [Array [Array [Float ,0x5_F],0B10],0X3]){}$F(){} }Class t{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1783))

    def test_1784(self):
        input = '''Class E:_{Var $39,$x:Array [Array [Float ,0124],0120];Val TSe,__,$_z0__3:F;Destructor (){}Constructor (){}Constructor (){}S(_,O,i_:String ;L:Boolean ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1784))

    def test_1785(self):
        input = '''Class _2{}Class _{}Class m{Destructor (){} }Class Q_:_86{}Class _K:N_D1id{Constructor (__Y:_;P_,D:_92;_s,O:Array [Boolean ,39]){ {} }}Class _6__:__{y(Q186,_:_){} }Class A{Constructor (){}Constructor (){Return ;}Val $F_B:d_4;Var $V:_;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1785))

    def test_1786(self):
        input = '''Class p{$_(_2:Array [Array [String ,0xB],18];I4,o:String ){Continue ;} }Class e2:P{Val $P6,$q,$8,$__:D_;Val $2:__;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1786))

    def test_1787(self):
        input = '''Class _{$6(_:_;_,V,X5__u1:Float ;__X6d,C_:Boolean ){}J(_,_:Array [Array [Boolean ,0b1_1],0B1100_10_0_1];__Y:Array [Int ,0b100110];L,fm:Array [Float ,0B1_1]){}Constructor (d_:Array [Boolean ,041]){Return ;} }Class W82{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1787))

    def test_1788(self):
        input = '''Class _1S{Constructor (u_1_1_:Array [Array [Array [Float ,0X5],42],0X7A];vfGDv,_:Float ){}_p3(sD,__i:Int ;e1,_5:Array [Array [Array [Array [Array [Array [Boolean ,0B11111],0X1],0B11111],0X9228],0B1],42]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1788))

    def test_1789(self):
        input = '''Class LE:p_{Var wJ_M,__,$_:Array [Array [Int ,0b100],0x7];}Class _21:k7_A_9{Val x41_,_,_,$_:String ;}Class _9:O{}Class n3q_q:z_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1789))

    def test_1790(self):
        input = '''Class WT:__{Var _X_,_,N,$7M_:Array [Array [Array [Array [Array [Array [Float ,0X1],0B110111],017],0b10_0_1],0x5F],0x5F];$6_(){} }Class _:ev{}Class _g__{}Class L{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1790))

    def test_1791(self):
        input = '''Class J:B{}Class A:B5d{}Class _9_:_8{Var Q_,Z7_od_,$RW:Array [Float ,0X34];}Class kpV1:p_{Destructor (){}__7(){Continue ;} }Class _2g{}Class Y_3:q8{Val _Y,$8,a:Float ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1791))

    def test_1792(self):
        input = '''Class n:h__CJ{Val _:Array [Array [Array [Array [Float ,0B10],0x5A],0x7],076];}Class __:z{}Class _{}Class __1{Ac(){ {} }}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1792))

    def test_1793(self):
        input = '''Class s:_{$O_yG(c:Float ){_v7::$_R_();Break ;}Destructor (){New _().S.__._().c().Vhk();}$U5___(Lv:Int ){Return ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1793))

    def test_1794(self):
        input = '''Class Ei{}Class _{Constructor (){}Destructor (){Break ;}Val __:Array [Array [String ,05],0X33];Destructor (){Return ;} }Class _y_m_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1794))

    def test_1795(self):
        input = '''Class _{}Class _:I__g{Val $9_,$71:Array [String ,06];}Class _U_:__{Destructor (){Continue ;} }Class _{Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1795))

    def test_1796(self):
        input = '''Class _:_y{Val $_Z,$_hS_,_:Array [Array [Array [Int ,41],05],3];}Class _{Constructor (B:Array [Boolean ,05];_73:String ;_5W,xv,_,U2m:Float ;nc:String ){Return ;} }Class k{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1796))

    def test_1797(self):
        input = '''Class _1_:_1{}Class __:c{}Class __:V8K8{Constructor (iJ8,E_:Array [Array [Boolean ,0x2_C_3_6_8_1],0X46]){}Constructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1797))

    def test_1798(self):
        input = '''Class j_:_P{}Class __{$_(n5,_PL,q:Array [Int ,0111]){Break ;Return ;}Val $_,$__:Array [String ,0111];Var __FU:Array [Array [Array [Array [Boolean ,68],0XC],0X10E64A],0x12];_(){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1798))

    def test_1799(self):
        input = '''Class B:_{$j__1(k:Array [Array [Array [Boolean ,72],026],0xB];T__z:Array [Array [Array [Boolean ,0b1],0x1],0B10101];L,_z:__){}Destructor (){Continue ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1799))

    def test_1800(self):
        input = '''Class V:_845_{$_45(SK_3,x:Boolean ){}Destructor (){Return ;}Var $l6:Array [Int ,5];Constructor (zt,L,V:Int ;U,n:Int ;_,_:String ){Break ;} }Class _:_j7__9_0{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1800))

    def test_1801(self):
        input = '''Class W{Var $2,$_:K;Val $_:_;}Class _y_9:id9{}Class WF:_{Val $_,_,$637:String ;Val _s_,l,_,k,X:Boolean ;F4(){Continue ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1801))

    def test_1802(self):
        input = '''Class N_:_zs{Constructor (_:Array [Array [Boolean ,0b1],0b111011]){} }Class Q:_{Constructor (){Continue ;}Constructor (_:Array [Array [Boolean ,65],063];__S,_:T){_::$_9A9a();}Val G__st,$5R,Yn:Array [Float ,90];Constructor (_:Array [String ,0B11000]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1802))

    def test_1803(self):
        input = '''Class t:A__{}Class _n{}Class __{}Class __{Destructor (){}Var U__,$_:Array [Array [Array [String ,72],0x53],0X3F];}Class W5:_{$93(){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1803))

    def test_1804(self):
        input = '''Class __{Constructor (tD_:String ;q04,CQ_0iw4,_:Array [Array [Array [Array [String ,0X58],49],49],7_600]){}Var $_:G;Var U,$r1:String ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1804))

    def test_1805(self):
        input = '''Class _4{}Class _6Hga_:g{Constructor (){}$_(C_:Array [String ,22_84];x__,P,b_8,ugH,RW:_F_4){Var _,_,V7:Int ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1805))

    def test_1806(self):
        input = '''Class t7:M{Constructor (i:Array [Float ,0X97F];_:Float ){}Var D:Array [Array [Array [Array [Float ,07],0B100101],0B1_1],011];}Class _8_4_:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1806))

    def test_1807(self):
        input = '''Class __P:_39{$B(C,_:Array [Array [Int ,0b1011100],46];_:Array [Array [String ,03_5_4],0B1_11];sB:Int ){} }Class f_:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1807))

    def test_1808(self):
        input = '''Class _{Destructor (){} }Class QDT{}Class _:CZ{Constructor (){}X(L4,_:Array [Array [String ,0X7],69]){Break ;} }Class B{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1808))

    def test_1809(self):
        input = '''Class l_K:__{Val $gm_:Array [Array [Array [Array [Array [Int ,0b10001],067],0X6],33],067];}Class nb{Var $66,_0F,$z_8,w:_;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1809))

    def test_1810(self):
        input = '''Class _:_Sc{Var NXPk:Array [Array [Array [Array [Array [Array [Array [String ,0x3],0X4],85],1],0x3],0x3],971];}Class _{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1810))

    def test_1811(self):
        input = '''Class A:_1J{Val $_,lv__:Array [Array [Int ,05_7],01];Constructor (){}_(_,_q9:Array [Array [Array [Array [Array [String ,0b1001110],0XC_7],0131],0131],0x21]){Val __,_5:String ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1811))

    def test_1812(self):
        input = '''Class r{Destructor (){}$G(_:_;_Y8_,_7E_d,_,m_5:Array [Int ,0B1011010];H__:Array [Int ,5_7]){Val _Q:Array [Array [Boolean ,0B1_10],0130];} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1812))

    def test_1813(self):
        input = '''Class u_:___{}Class wv:b___24B{$k(f_:_;B,_,E,e,B:_;L843:String ;_,_,mo,_,_59:___){Val r_3:Boolean ;Continue ;{}Break ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1813))

    def test_1814(self):
        input = '''Class K_:d{__(Uq:Boolean ;_7,lY,K,Xz,__:Array [String ,0b1001101];__p9:Array [String ,070]){}Destructor (){Break ;Break ;}Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1814))

    def test_1815(self):
        input = '''Class z{Val $__D2:Array [Array [Array [Float ,0X342],0X3E],07];}Class VK3N{k(){}S(_1_:_S;_,_,K9,E,m,_:Array [Array [Array [Boolean ,031],0b11_1],0x53];_,__,z,K:_L;_:_17_){} }Class zM:ka4p{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1815))

    def test_1816(self):
        input = '''Class f_{Destructor (){Continue ;} }Class _{_9(_,m5_0,_:Float ;i_:Float ;_M,_5_,L,_,e,_,a7h_4Y7,_x_:Float ;N,L3zX_,_mf:Boolean ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1816))

    def test_1817(self):
        input = '''Class JW_{Constructor (_,R_:__a;__:Array [Array [Array [Array [Array [Array [Boolean ,0B11],0142],0B1],0x1],26],02_7_2];i_:Float ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1817))

    def test_1818(self):
        input = '''Class _XXm_D:p_{Constructor (A_u,_,_,L:Array [Boolean ,0B1];e:Array [Array [Array [Array [Float ,0X4A],0B1_1],0X4A],85]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1818))

    def test_1819(self):
        input = '''Class _:s{}Class _:_H{Var $_,__:Array [Int ,43];}Class O9c:f6{Var $_C:Int ;}Class _7:Gl{}Class _g:e{}Class _a:j{}Class X:E_w0_{}Class F:_w{__(Dr:Boolean ){Continue ;} }Class _:j_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1819))

    def test_1820(self):
        input = '''Class q:J{E(_q_e__9:_;_,nD:Array [Int ,0xD_1];i2e,K4I,c961M:Int ;_v_:Float ;___1:Array [Array [Array [Array [String ,88],31],03],0b1010000];_,u27,z__,_2,__r_k,_:I){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1820))

    def test_1821(self):
        input = '''Class L{Val $R0_7r1:Array [Array [Array [Float ,20_8_8],0B110001],033];}Class _3{$V(_:Int ){}Var $ZtQ_:Array [Array [Int ,0B10],0x5];Var $Y_nJ,$2_8_,_,$z:X;$7_(_,hgC:_;_7:Array [Array [Array [Array [Array [Array [Boolean ,1],0b1_0],1_4],0X21],0X2],033];_:Boolean ){ {}Return ;{} }}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1821))

    def test_1822(self):
        input = '''Class _A_4R:Lga_{}Class _:_fJ{Constructor (_D,L,_e5,__,d:Array [Array [Array [Float ,0b1],0B1011111],0B1];_7,W__,_,_,_______:Array [Boolean ,0B1011111];__Um67843Z:Array [Array [Array [String ,03_1],0x9D],11]){Break ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1822))

    def test_1823(self):
        input = '''Class x:__5{y_(){Return ;} }Class F_{Destructor (){R_::$V665.k__();} }Class _L:o{Val $N_0_,I:Float ;}Class _{}Class _:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1823))

    def test_1824(self):
        input = '''Class J:__{}Class l:_{}Class g__:_{$39(__:Array [Array [Array [Boolean ,75],032],032];a__4,H4f,w,_m0_:Array [Boolean ,0X7_3];_ii:Array [Array [Array [Array [Array [Float ,032],02_0211],0XA_7],0X2],0B1_01]){Return ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1824))

    def test_1825(self):
        input = '''Class _S12J{Constructor (){}n_H_0(u__t_Z:Int ;H,_oz_61:Boolean ){}Val $20:x;Val $_,$j_rJ_WF_2,u_A:K;Var d,$g_u,m_4:Boolean ;Var $3:_;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1825))

    def test_1826(self):
        input = '''Class m5{}Class _:w3{Var $0:IU60_;Var iX9:Int ;}Class _4554:c{}Class B{Constructor (u_:Int ;b_9b:Int ;I,_:A){Break ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1826))

    def test_1827(self):
        input = '''Class _:_{Constructor (_,o,Rn:xb;NO__:Array [Int ,0x3B4];Q2:Boolean ;__Y3,_,_K,sc:Array [Array [String ,0b1],015]){}Destructor (){} }Class _s{}Class Y_{Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1827))

    def test_1828(self):
        input = '''Class _{Constructor (_0_,__:_D;lS:_ht){}Val $_6,_9,___,_2:O_;Var $J,Kl,_,__:Array [Boolean ,56];}Class G{Constructor (U:Array [Array [Array [Int ,0b1],56],042]){Break ;Continue ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1828))

    def test_1829(self):
        input = '''Class __:_{}Class _a:R{Var $_,_2xaQ___v_:Array [Float ,85];Destructor (){}Var $_8:Array [String ,0B101101];Var $E_,_Y9t,$3,$_W:String ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1829))

    def test_1830(self):
        input = '''Class __tY{}Class _J{}Class _:Kl{Constructor (_8_4W1,V_,z3:D){}$6(__,___8_Z:Y;v7Ui:Array [Array [Boolean ,27],0b1];_XA:zx0_;B,n__K___,R,_:v){} }Class _:fa{Var N,p,$__,_:Array [Array [Int ,062],062];Val $_:Int ;}Class n_:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1830))

    def test_1831(self):
        input = '''Class _1:m{}Class _{}Class Qh{}Class G{}Class ___{$_F(){Val g:Array [String ,07];Val _,l5,K:Boolean ;Val B,X,_,So__,_:Array [Array [Array [Boolean ,5_4],50],9_3];{} }}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1831))

    def test_1832(self):
        input = '''Class _:C{Val $F,n_U6,l,_,$3U___:Array [Array [Array [String ,51],0X1_7],4];Destructor (){}$_C(f,f:Array [Array [Boolean ,0b1000011],0x5_6_2_33]){Val _q:Boolean ;Break ;} }Class u4m{}Class __{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1832))

    def test_1833(self):
        input = '''Class G2{}Class R7_{}Class D7:_{Var $U,$b_7,__9w:Array [Array [Array [Boolean ,022_7],0X1],0130];$2(_:Array [Array [Array [Boolean ,8_0],0B11101],6_9];__:Array [Array [Array [Array [Array [Array [Array [Array [Array [String ,0x23],06_2],4_7],0X2],10],0b11100],0X7],0b10],0x23];uvi,_,_:_B;_P:Array [Array [Array [Array [Int ,0b10_0_0],0X92],05],0130];K_,_f,_,Q,__:Int ){}Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1833))

    def test_1834(self):
        input = '''Class v8:_{Constructor (_,l2,_,p,xBh,_:_;s2A:String ;H_3:Boolean ){Val _:Int ;}Constructor (){} }Class _{}Class _{}Class b:_{}Class Z{$8(T8i_36_,_Rb,__6,__,_,_039_,o6b:Array [Float ,91];i,e0,fi,_,U,_:Float ){} }Class _{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1834))

    def test_1835(self):
        input = '''Class A:_s1{}Class H{Constructor (){}Destructor (){}Val $750__,$u__5:A;}Class __:O{_zu_(_0,d:Array [Float ,0X1]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1835))

    def test_1836(self):
        input = '''Class M:h_{Constructor (__cU:String ;_1:_K;J:Array [Array [Int ,0X17],0142];mE,Q,H6,L0h,_79:Float ){}Constructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1836))

    def test_1837(self):
        input = '''Class U{_(z:_;_:Array [Array [Array [Array [Array [Int ,25],011236],06],0X9_9],25]){} }Class F{$1(){} }Class E__:y{}Class G:E0_{$__8(_H:U6){} }Class _2:_4m{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1837))

    def test_1838(self):
        input = '''Class _{$___2_(_k,_,Y:Boolean ;_:Array [Array [Float ,0B1001010],68];__E,_:Array [Float ,05];k:Array [Int ,045];_v,_Z:_){ {} }Var $_2_:Array [Array [Array [Array [Boolean ,0X4C],045],68],0X6_7_1EA];}Class N_{}Class K_:g__{}Class Z:c{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1838))

    def test_1839(self):
        input = '''Class _:E2{Destructor (){}Destructor (){}$_(_:Array [Array [Int ,0B1_0_01],0xF]){cS::$EJ();} }Class _{}Class o:r{}Class _u:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1839))

    def test_1840(self):
        input = '''Class _:F{}Class _:d{}Class _0_80_6q_:f{}Class _:_22_d{}Class _:_{$_(_:Array [Array [Int ,0B101000],0x5A];_,E:Boolean ;O,x_,clS17:Array [Array [Float ,05],0X1C]){}Var $_35,_,_:Int ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1840))

    def test_1841(self):
        input = '''Class _9{Var _e3,$_:Boolean ;}Class __:A6g_{Destructor (){Break ;} }Class b_Kl{Val L,$9,$4o8:Y_B;}Class OB{_m8(){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1841))

    def test_1842(self):
        input = '''Class _f9:_{Var $__C:Array [Boolean ,0x30];}Class _:_{}Class _y__{Val $8:Array [Int ,0X28];Constructor (){} }Class O8_Y{Val $3_,s_5_E:Array [Array [String ,0b100111],0xC];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1842))

    def test_1843(self):
        input = '''Class c75:_09{Constructor (L:Int ;_s:Float ;_:Array [Array [Float ,0xB],01]){}Constructor (_1:x;rdP,C_R,cH,_n:Array [Boolean ,025_033]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1843))

    def test_1844(self):
        input = '''Class h{Destructor (){Break ;} }Class _b:T{}Class _:_A_{}Class _4:r{$0(){ {} }}Class f:Z_bft{Val K,_,$6:Array [String ,0x8];Val __8:ktY;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1844))

    def test_1845(self):
        input = '''Class __439_{Constructor (_F:xA2I_;_T7_,X,s_,_,_p_b,l:Int ;_,s_:t_2;_:Array [Float ,0x42]){Continue ;}VF4(x,_,_,_,_:Boolean ){Break ;New S().Es__._Ib();} }Class c:_2{}Class _{}Class rM:M5{Constructor (U,__U,t,_B,_:String ;L,__,_3:Int ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1845))

    def test_1846(self):
        input = '''Class o:_u{Constructor (j:Array [Int ,83_0];__:Array [Array [Array [Array [Array [String ,0104],0104],27],0b100],0B1010010]){Break ;} }Class _:D{}Class w{Var _,Z,_X0_,$_,$L__,_,$I_v,$96l1,t,$_1,$5_:Array [Boolean ,27];}Class _:u_{}Class D:K{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1846))

    def test_1847(self):
        input = '''Class _:_b{Var $8,$5,m,_,_,$C,$_:Array [Array [Array [Array [Array [Array [Float ,0B1],0b1000101],0B1000],07_4],0b1000101],05];Constructor (_,_,_,_,c:Array [Array [Array [Int ,0101],0101],0X47];A__E:Int ;ClM:Array [String ,0101]){}$_zb(q,_,_:String ;b_C,Z_,P,_,_yj,_:Array [Array [Array [Float ,0101],10],0101]){} }Class _:M{Var $R,$_3K47:String ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1847))

    def test_1848(self):
        input = '''Class _9:V_{$_1(c:Array [Array [Array [Array [Array [Boolean ,057],057],0B100100],057],0B100100]){} }Class P__{}Class _W{Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1848))

    def test_1849(self):
        input = '''Class _lrP:G{Val $q,_d:Int ;}Class __9_{Destructor (){}Val $50_Q,$888:Array [Array [Array [String ,0b1011011],15],0B1_0];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1849))

    def test_1850(self):
        input = '''Class Om{Constructor (f_:String ){c::$a();}Constructor (A,N,_,_,u,_WH_7_J_:Array [Array [String ,0751_7],0X1C];T2S,_,_I__7_8,__:b_;oGe_:S27){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1850))

    def test_1851(self):
        input = '''Class P:La{Destructor (){} }Class __t:X{}Class _N_6:_0_{}Class __{$_(r,F_,_O,t:Array [Boolean ,0B10101];_:Array [Array [Boolean ,18],0B10101]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1851))

    def test_1852(self):
        input = '''Class __{}Class __:__{Destructor (){Val ___:Array [Boolean ,0xA];}X(K1_,W,_14w:DMgW){Return ;Var W7,_,U,_,J_:Array [Array [Array [Array [String ,0X7],032],3_5],39];} }Class m{}Class pE11:_{Constructor (BV:Array [Int ,0x15]){Var G3__:t;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1852))

    def test_1853(self):
        input = '''Class _4:xZ{}Class y:_{$_j_6(_:Array [Int ,18];_,U,V,_V:Array [Array [Array [Array [Array [Int ,0460],0X9],0B1001111],4_0_8],0b1001101];_8_:Array [Boolean ,0X5C]){}Val Q_z,K_:Array [Array [Array [Array [Array [Boolean ,0104],8_8],0b1001101],18],18];Destructor (){}Destructor (){}Val eR_7:K;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1853))

    def test_1854(self):
        input = '''Class u{}Class f{Val $D9_:Array [Array [Array [Array [String ,9_2_92_23_291],0B1],03],0b1];Var _,$__:Boolean ;Val XN:_;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1854))

    def test_1855(self):
        input = '''Class i5{}Class oU_:L{Val I_,$0,J__:Array [Array [Array [Array [Float ,0b100100],025],025],0b1];}Class v:R4{_9_3(){Return ;Break ;} }Class OW{Constructor (g:Boolean ){Return ;}Destructor (){}Var $VX:_;}Class y_k{}Class _:I_{w7d(){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1855))

    def test_1856(self):
        input = '''Class Q_33J619:_{}Class D:_{Var v__:Array [Array [String ,0b10],073];Destructor (){}Constructor (Iy46:Boolean ){Continue ;}Var $V6_X8P:Float ;Constructor (__,_:Int ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1856))

    def test_1857(self):
        input = '''Class y:S2{B(__:Array [Array [Array [Int ,0b110111],0b110111],055_5_623];F:Array [Array [Float ,0x16],0b1]){}Val _21,A,_,$_n:Array [Boolean ,0x4];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1857))

    def test_1858(self):
        input = '''Class _:c{Destructor (){}Constructor (){}Destructor (){Continue ;} }Class Fe:I_x__{_b(){} }Class FJ_{}Class z_8:_{$9(___:_M4;__T:Float ;__O,cS:Array [Array [Boolean ,2],0B1_1];z:Int ;L569,Q:T){} }Class _{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1858))

    def test_1859(self):
        input = '''Class X:H3{}Class _{}Class RP__N_95:_{Val $92,_,s,$__:_;_(_4_:_k;___Y8,_:A;_8,a3P,_m,_,A67:X;__a_,_pd:Array [Boolean ,5];f9kKP1,Ho:Array [Array [Float ,0x45],0B1];X_6_:m){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1859))

    def test_1860(self):
        input = '''Class _:f{}Class sN____:_FL5_q{}Class _{Destructor (){Break ;{} }}Class M:_25t{Var _:Array [Array [Array [Boolean ,79],79],0x39];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1860))

    def test_1861(self):
        input = '''Class e{Var $_2378_Eo:Boolean ;}Class e:_8{Constructor (){}Destructor (){} }Class _{}Class KS:_{Var $_l8_X,R_Tx,I:Boolean ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1861))

    def test_1862(self):
        input = '''Class W__Z:h{Constructor (__7_:Array [Int ,72];_:y;_:Boolean ){Return ;}Constructor (_:Int ;H7A_6J,j:Array [Array [String ,0x3],0143]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1862))

    def test_1863(self):
        input = '''Class g:q_{Constructor (l,_,e,_:Array [Array [Array [Array [Array [String ,0X36],39],0x1],0B1_0],1_7_0];P7a_:Array [Float ,0B1];_pJ4:Int ){Continue ;} }Class p1:_RC4__{}Class _{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1863))

    def test_1864(self):
        input = '''Class _{}Class _:_s__{$E8C_31_(T5W,_,tk_,V_,F:Array [Array [String ,0B10_0_1_0],025];V4:_G;_99,_J:Array [Float ,0B1110]){} }Class _9{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1864))

    def test_1865(self):
        input = '''Class _:i93vz{}Class G{}Class JU_I{Val $3P_2,$x,$_F,_:Array [Float ,0X4];$42(_:_Ha;GRz:_7;__:_;I_:mhO){ {} }}Class _86{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1865))

    def test_1866(self):
        input = '''Class _{}Class Lz{_(){} }Class _{Val $pb__:Array [String ,0B11010];__2(k1,BS_,C_Tp,M:w;_,ub_0Qj_,cr__5d:Array [Float ,0x4B];UJ_m_i_:c1_){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1866))

    def test_1867(self):
        input = '''Class _v{_h(l6x_:Float ;t,Wm:w;__,k31,s:Array [Array [String ,01_0],0b101111];I4,_,_z,E,_:Array [Array [Float ,1],0b1];_,E3,C:Array [Array [Array [Array [Boolean ,93],50],02],0b101111];f,_2:Array [Array [Array [String ,50],054],0B10100]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1867))

    def test_1868(self):
        input = '''Class _6{$_(q,I,J:Array [Array [Float ,0140],5_75_2];_,__H,_,J_:Boolean ){} }Class w_:r6{}Class b:d{}Class J{Val $686:Array [Boolean ,0B1001111];Constructor (___,p2,_5,p:String ){} }Class __:_m3P_{Constructor (V,j,___:Array [String ,0xB_D_75_B];p_:_Q;d,Bs:Int ){} }Class _n_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1868))

    def test_1869(self):
        input = '''Class ___{Constructor (u_6:h_;_,_1,_:S;_7:Int ;f:Array [Int ,9];B3:Array [Array [Boolean ,0X21],0x33]){ {}Val X9,_30:Int ;} }Class __:C__8{Val $1,$8:Array [Boolean ,7_8_1];Constructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1869))

    def test_1870(self):
        input = '''Class _{Var _15:Array [Array [Float ,011],29];Constructor (qXD:Array [Boolean ,026_1_7];__H:Array [Array [Float ,0b10],0B1011110]){Continue ;} }Class a{}Class p{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1870))

    def test_1871(self):
        input = '''Class Q:x{$_72_1(){}$00_(g6:Array [String ,0B1000100];pCfD:Array [Array [Array [Float ,0b10101],05],031_2_24_02];ofx,I_611:Int ){Continue ;Z::$J();} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1871))

    def test_1872(self):
        input = '''Class _{Val $_9,_,$__:Array [Array [Array [String ,05],0133],0b1100];}Class j_{Constructor (z,_,_,__Kv_f1x__96n_:Array [String ,0B1]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1872))

    def test_1873(self):
        input = '''Class _k_47:f{_9s(_:Float ;O9:u;_01:String ;_:Array [Array [Array [String ,0B1000100],0B10],0B1000100];_n,_7__,_B:Array [Boolean ,0131]){}E(){}Var $s,o:g7;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1873))

    def test_1874(self):
        input = '''Class _H{}Class h:_{}Class M_:b{}Class A:M{Constructor (R:Float ;a92:Boolean ){} }Class x{Constructor (_k5:Boolean ;S_D7ZJ_:Array [Int ,56];Z8,b5:Int ;J3:Qz){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1874))

    def test_1875(self):
        input = '''Class __{k(r3:String ){m__j::$3_();Continue ;Break ;}_(){}Val $_,_z3:i;_(R_j0:Int ;K:Boolean ;_,Th:Int ;O:fI){Continue ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1875))

    def test_1876(self):
        input = '''Class _yZ_6L{}Class _:_d1__s_7{}Class _{Constructor (_,KC:RA;_nF:Array [Boolean ,0b1100_0];_0_y,JDW,t,_:_;m6y,L9Y_2,K1_,_q,R,_,DY:String ){} }Class z{}Class _0:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1876))

    def test_1877(self):
        input = '''Class K_:z{$_K_(){}__551_(){}Var P_:Boolean ;Val KS:Array [Array [Boolean ,0X63],0b10100];}Class __j1__:Y{Val $5b:_;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1877))

    def test_1878(self):
        input = '''Class _9:w_{e(){} }Class _{Val $T_30_39,$7,$o,_,$1G_V,$9__:Array [Array [Array [Array [Int ,02_7],0102],0x5],0b1_00];Destructor (){}Val $5:String ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1878))

    def test_1879(self):
        input = '''Class _:r{}Class _{}Class _6:__{$e7(U,_7R__R0:Array [String ,0X4];pp,S,h,M:Array [Boolean ,0x140]){} }Class w__:l{}Class _:S{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1879))

    def test_1880(self):
        input = '''Class _W{Constructor (_,i:Array [Array [Array [String ,7_7],04],0X11];R,_,_:Array [Float ,07];__7,_,_,a,_:String ){} }Class _{}Class _d4J:_0{_(){}p_4(){Continue ;} }Class _{}Class R_:Z{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1880))

    def test_1881(self):
        input = '''Class N8{Var $_:Array [Array [Array [Array [Boolean ,0B10100],02],04],0x51];}Class V:N{w(_9__:Boolean ;Bh:Array [Boolean ,0B10100];_,___,_,_6_,__:Array [Int ,0b1_11];_5,j7g70:Int ){} }Class _:_23X__p{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1881))

    def test_1882(self):
        input = '''Class C{Destructor (){}Constructor (s,u:Array [Array [Array [Array [Array [Array [Array [Array [Array [Boolean ,03],56],010],0X1],02],010],013],56],04_3_1]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1882))

    def test_1883(self):
        input = '''Class _:__{Var $S:Int ;$_(){}Constructor (_,_59b,S___,I,_:_3){}$0(__t_:Float ){}Destructor (){}Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1883))

    def test_1884(self):
        input = '''Class dhu{Constructor (A___s,q:Array [Int ,0B1];_:Array [Int ,025];GA:Boolean ;_:o;_9_:Mrn_6R;_0f:Array [Array [Array [String ,01],5],20_5];F8W9,T,_:Float ;_:Array [Array [Int ,01],6_3]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1884))

    def test_1885(self):
        input = '''Class _{$5(r,_6,_a:Array [Array [Boolean ,06],414_4_5_257];_K:Float ;_,K:Array [Boolean ,0B1_11]){}Destructor (){}Constructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1885))

    def test_1886(self):
        input = '''Class n{_(){}_(){} }Class __h__:_{Var _:Array [Array [Boolean ,0B1],0b11101];Destructor (){}Val $E5:String ;}Class _:_{}Class p3{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1886))

    def test_1887(self):
        input = '''Class J_4L{Val _6_q,_:Array [Array [Array [Array [Array [Int ,04],9_3],023],0xE6],0B1];}Class r7_6B3:Z{}Class _e:_{$__(h:Boolean ;x9,V:_){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1887))

    def test_1888(self):
        input = '''Class _981_D{}Class N_r_:l_5q{}Class pP2q{}Class h_g:_{_an(Mc_3A,X,_:String ;_,_:Array [Array [Float ,062],0b1]){Break ;} }Class r6S:_9_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1888))

    def test_1889(self):
        input = '''Class Xm1_{Destructor (){}Var __:Array [Array [Array [Array [String ,07_63],0xB],0x74],06_7_1_6];}Class y:__{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1889))

    def test_1890(self):
        input = '''Class _6{Constructor (){} }Class __{_M6V(){}Val g2:Array [Int ,10];Val $Ln3_,wW82:Array [Boolean ,0x3_E];Var $9:Boolean ;}Class O3b1t{Var __:Array [Int ,10];}Class _6W:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1890))

    def test_1891(self):
        input = '''Class J_0{}Class _:_{__(rvW_z:Array [Boolean ,0143];l:Array [Array [Array [Int ,0X45],05],0b100100];_Q8_,_1,A28:Array [Int ,6];_:H;_kf,_:Float ;L:Float ){}Destructor (){}Val F,_x_e6j,_:_;}Class kw0_:mD1{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1891))

    def test_1892(self):
        input = '''Class Y{}Class is{Constructor (pbyf7_:String ;_,i:String ;N:Array [String ,0x3]){} }Class H:_{Var ME_,$K:h15_xe_;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1892))

    def test_1893(self):
        input = '''Class f_wG:_{$Y6_(_,_1:t__835;__U,h_,I,UM,____:Boolean ;v,R5,_TcG,_o_,_,_,mJa_7:Float ;_1:Boolean ){ {Return ;} }}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1893))

    def test_1894(self):
        input = '''Class _rLs:_{Destructor (){ {Break ;Break ;}Return ;Continue ;}Constructor (F7,_v8_xm6:_){Continue ;}Destructor (){} }Class _2:hE_{Constructor (P:dr;o,_,sA_,D_9:__9){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1894))

    def test_1895(self):
        input = '''Class _{}Class _3{_(_0s,K,q_8__C_4__3,__Y_,_z,k2:Array [Array [Array [Array [Int ,8],0x40],056],025]){}Constructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1895))

    def test_1896(self):
        input = '''Class _{}Class _g:_s_{Constructor (_,m2,A8_:Array [Array [Int ,499],0b1010100];___B63_:String ;m,_:Array [Array [Array [Array [Array [Boolean ,0B1],032],0X16],0B1],0x58];_q9,_3:Array [Array [Array [Array [Array [Array [Array [Int ,0xA],063],1],045],0X50],0B1],0B11011]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1896))

    def test_1897(self):
        input = '''Class t{}Class v{Var $18p,___9A,$L,$L_,$_T,$5M:_;X_2(){Continue ;}Destructor (){}Var l2_,$0:___;}Class l_{}Class d_{}Class _B_:k_92{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1897))

    def test_1898(self):
        input = '''Class __:PW_G{}Class o{Val $Q6m:Array [Array [Array [Array [Array [Array [String ,0X49_8_7],0112],0X11],88_8],01_3],0xF];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1898))

    def test_1899(self):
        input = '''Class _:vA{Var $N:_;Destructor (){Continue ;}Constructor (rfNp__Y65Q,A,a4,__:Array [Array [Array [Float ,0B1010010],5_1],0b11];V:t_3;_,_:Array [Array [Array [Array [Array [Array [Float ,0b1001],0b1],23],23],014],23];W,j,_,P:_;P,_U:Array [Array [Array [Boolean ,06_2_3_7_1],0X79],07];r,l:Array [Array [Array [Array [Array [Int ,014],05_6_2],01],23],0xD]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1899))

    def test_1900(self):
        input = '''Class pH6__3{Val $_f4,$6:___l;Val L:Array [Int ,0B1_00];Val ___,$2,$2:Array [Array [Array [Float ,0x47],0b1],0B1000];}Class N0_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1900))

    def test_1901(self):
        input = '''Class lB{Constructor (_,_,a,_:String ;_C:String ;_:Array [Array [Array [String ,0x7B_A],0xB],0xA_9];G5P7Bmr,Q_z_24l:Array [Array [String ,033],033]){} }Class _{be(){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1901))

    def test_1902(self):
        input = '''Class C{}Class _:__{}Class SR{Constructor (_,_1:String ;W_6,_,_,k:Array [Array [String ,0b10100],0X4B];_,O,_,h1,G:Boolean ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1902))

    def test_1903(self):
        input = '''Class c8_:_{}Class _6{Var _7r5,$hk_y2,_:_;}Class __Mq:_V{}Class _:B8{Constructor (){}Destructor (){}Constructor (){} }Class c8a1u:_{q7(_e50:Array [Array [Float ,05_54],0b1_111_0]){}Var $1,x,$_22:Int ;$Hwmg8j_7(){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1903))

    def test_1904(self):
        input = '''Class __:_{$_(f,u8:Array [Array [Array [Array [Array [Array [Array [Float ,69],69],0X1_1],05],02_3_7],8],0B1_0_1_0]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1904))

    def test_1905(self):
        input = '''Class _:f9_{Destructor (){}Constructor (){} }Class _{}Class _:P{Destructor (){} }Class s65{}Class _{Constructor (_,_,U,aJB_9_:Int ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1905))

    def test_1906(self):
        input = '''Class __2{Val _,$a6,t_:Int ;Var $1:_;Constructor (_:Int ;G,_:Int ;za:_G2;_:___4B){} }Class nT{Var M:Boolean ;Constructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1906))

    def test_1907(self):
        input = '''Class c{Destructor (){}$1(r,_R:d_C9;_B7,_,O:Array [Array [Array [Array [Array [Array [String ,0B1],06],0x33],72],023],72]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1907))

    def test_1908(self):
        input = '''Class _{Val $7_,$6R3:Array [Array [Array [Array [Array [Int ,0XA_E7_7_F_9],064],94],064],0x6];Constructor (sd:Array [Array [Array [String ,0XC_1_0_4],5],0X41]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1908))

    def test_1909(self):
        input = '''Class _l{Constructor (){}Constructor (){_::$z8();} }Class e{$_9Zl_(){} }Class v_114__{Var $8:Array [Array [String ,0X53],0x4_C];}Class __3_2__{Var $K,$22:_;$h293_4__(){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1909))

    def test_1910(self):
        input = '''Class _:_5{}Class _7L93:D{Var $2:Array [Array [Array [Boolean ,0122],36],0X7];}Class C_{Destructor (){} }Class _:_{Var F_,$1AT,__,$B,__:Array [Array [String ,0x64],33];}Class _77__j_Uv:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1910))

    def test_1911(self):
        input = '''Class T{Constructor (X:Array [Array [Array [Boolean ,0x21],056],0X44];_T:_;_,z:Array [Array [Int ,01],0b1011100]){} }Class n:_u{}Class R{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1911))

    def test_1912(self):
        input = '''Class __:_{Constructor (P,___:Array [Array [Int ,84],0B1011]){}$_N(_:Array [Array [Array [Array [Array [Array [Array [Float ,0b1000101],7_9],3],06_4_14],016],0b1000101],0B1011]){Break ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1912))

    def test_1913(self):
        input = '''Class F{Destructor (){}Constructor (){Break ;Continue ;}Var Lw60Mo_3,i_,g_8,$0,$4_H,$3__,D,$_,$z,X__:Float ;Val __O1,$4_A0:z;Constructor (){Return ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1913))

    def test_1914(self):
        input = '''Class __00{$x(_:Int ){} }Class _:_4{}Class _z{Constructor (I26,f,_,_,_,U:Array [Array [String ,0B10110],0B10110];A1rC__L69:Array [Int ,0X5_4]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1914))

    def test_1915(self):
        input = '''Class ti:___{Constructor (){}Val $i_,_3c4:Array [String ,0x2_5];C_(rz,_x,d_:Array [Array [Int ,0X7B7_C_E],0b1]){} }Class _:_c{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1915))

    def test_1916(self):
        input = '''Class __{Constructor (){} }Class Z{Var _:Array [Array [Array [Array [Array [Array [Array [Int ,0x8_2_1],0B1],0b10],0b1_0_0_1100],0x35],0XA],18];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1916))

    def test_1917(self):
        input = '''Class _:_9_0{Constructor (_XS6_l_l,v,V:b_;VZ,Mr_Qz8q,_:Array [Array [Array [Array [Float ,0x5C],0b1_0],032],0b1000011]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1917))

    def test_1918(self):
        input = '''Class _P_:A{}Class Oky__:R1{Val _:Array [Int ,06_0_7];}Class _{}Class _{Constructor (WU3h_9_:Array [Array [Boolean ,0141],0X4C];mJ,W_:String ;Xv_,x:Float ){Ku::$_3();Continue ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1918))

    def test_1919(self):
        input = '''Class V_Y:_{Destructor (){}Var $9_02Q,$z_,$s:Array [Array [Array [Array [String ,0X1D],0B111011],0b101011],0xDDE2];Constructor (e__:m_;_4w:h){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1919))

    def test_1920(self):
        input = '''Class _:b{Var $___,_:Array [String ,2_1_6];}Class F_8:D9h{Constructor (_,_8,_4,H:Array [Array [Array [Float ,0b1],0X23],07_1];ei,R:Array [Array [Array [Array [Array [Array [Float ,0b110011],03_3],06],0XC],0x9],0XA53]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1920))

    def test_1921(self):
        input = '''Class _:G_{_02(_:Array [Int ,0X5_2];_:Array [String ,0x6];__1,__:_;S,G:Array [String ,0B11_10_1];_4,k:o_;X:Float ;iA:_O_N){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1921))

    def test_1922(self):
        input = '''Class _:_8{}Class D:_{O5sT0(n_,k,P,__,__7W:G_;_9_rq:Array [Int ,49]){} }Class _:v3{Val $_3_:Boolean ;$v(){} }Class _:Uz{Constructor (Wu,_,b_6,f:Array [Float ,0x1A]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1922))

    def test_1923(self):
        input = '''Class _6A26__{$704(_4,_e_:Array [Array [String ,1],0X8]){}Constructor (N_s_:M;v_:_;XFX1R,U__,_,b2:_){ {}Break ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1923))

    def test_1924(self):
        input = '''Class D{}Class _:_{Constructor (_:Array [Array [Array [Int ,06],04],0b10101];__:Array [Array [Boolean ,0XE],02];M:Array [Int ,0140]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1924))

    def test_1925(self):
        input = '''Class j1__4{l7R4(_,E,J0,_:__;_,m,Z5:Int ;_,_X:Array [Boolean ,0b1000100];h:Array [String ,0b1];qi,X_1:Array [Array [Array [Int ,0x5C],0b1],0XA];_,wS:Int ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1925))

    def test_1926(self):
        input = '''Class _I_:C4{Var $_g:Array [Array [Float ,0104],9_6];}Class __{Constructor (_:String ;_5,_,X,__19,o__,_,_001,_6:Array [Array [Array [Int ,0104],5],011]){Continue ;Break ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1926))

    def test_1927(self):
        input = '''Class __:_{Val Q,Sn_,$45:Array [Array [Array [Array [Boolean ,0143],0b1],07_3_57],0143];}Class _X1q_{}Class _{}Class M{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1927))

    def test_1928(self):
        input = '''Class w{}Class _1_{Var $_:Boolean ;Var $__7,_,_e___0E:Array [Float ,03];O(){}$9(){Var BU__,O_N1,L_:Array [Array [Array [Array [Array [Int ,0X3],8_3],0xE_5_11_7],76],0B1];}Constructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1928))

    def test_1929(self):
        input = '''Class C{_(_:_6_){}Constructor (_,q_,_0:String ;___,_,Xr,_r2:_;f,_:Boolean ;p_:E1__;GL,Y_,_1,u2,_:_;__89:Array [String ,65];_:Array [Float ,6];_6:Float ;_1,__,h__2,_4,H:Array [String ,0xDF3]){ {} }}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1929))

    def test_1930(self):
        input = '''Class rs{Val $dp1,$p,$r:Array [String ,0B1];V__2(_R,_:Array [Array [Float ,0x41],0x3];l:Boolean ){} }Class Z{Val $_:Boolean ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1930))

    def test_1931(self):
        input = '''Class _u:_y{}Class _:f_C{}Class _3{Val Ud:Array [Array [Array [Array [Boolean ,85],071_5_5],0b10100],0xD];$G(_0__,_3,_k,i,__:_M;_l:Array [Array [String ,050],0b10100]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1931))

    def test_1932(self):
        input = '''Class _{__(_67:Array [Int ,0130];_08_,_y,Q3:Array [Array [String ,05],0X7];_9,D:Array [Array [Array [String ,0B1],06_4],0130]){} }Class __:_8{Var $E__,Z,_,$_,$_:Int ;}Class _{}Class z9_4:W{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1932))

    def test_1933(self):
        input = '''Class o:_{}Class __{Constructor (e8H:_;_24,__,_,_y,_:Rr_){H_::$__.T()._w();}Val _,$_,$88:Array [Float ,0143];}Class V{}Class KR_:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1933))

    def test_1934(self):
        input = '''Class __:_t___{Constructor (_:Array [Array [Int ,97],0x4];_k_,_Im3co6:Array [Float ,0xE3]){}Var $_:Int ;}Class _:_{Val $_,e3_:Array [Array [Boolean ,0B11],07742_40];}Class E{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1934))

    def test_1935(self):
        input = '''Class o:__t{}Class __K3:_k2_t{}Class _3:z_{Var $1,_:A;T(){} }Class _8{Constructor (){} }Class _{Constructor (){} }Class V{Destructor (){}CL6_(_:H;Sw,_:Array [Array [Boolean ,036],04]){} }Class u{Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1935))

    def test_1936(self):
        input = '''Class f9___{Constructor (P,_:Array [Array [Boolean ,0B11_1_0],82];h4:Array [Array [Array [Array [Array [Boolean ,0B10],3_7_54],0XD],067],6_7]){} }Class u3{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1936))

    def test_1937(self):
        input = '''Class V_9{}Class ofby:Q{Destructor (){ {} }Destructor (){}E(P:Array [Array [Array [Float ,9],0B1001101],0X36];A:Array [Float ,0b1]){} }Class w:i_{Var $3_:_;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1937))

    def test_1938(self):
        input = '''Class v_{}Class _3_:S_{Destructor (){} }Class _:m{$_0(_,k,_:Boolean ;Q_,__0PX1:M7;Q,_e_K,_,_:Array [Array [String ,0xF0],05_7_034]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1938))

    def test_1939(self):
        input = '''Class Th{$s_(W,_:Array [Array [Array [Array [Array [Boolean ,0X3A],0b1001110],0XE],03_6],0XCA];_4,_nd_,J,_:Boolean ;_N5,J49:q){_::$V_();Continue ;}Var __,$0:Array [String ,0X3A];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1939))

    def test_1940(self):
        input = '''Class XF:H{Var $__63,$_5,__7:Array [Array [Array [Boolean ,0x2],0134],0X36];Var $_,Cq:Int ;}Class W{}Class hs:IF{Constructor (){}$__(){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1940))

    def test_1941(self):
        input = '''Class N:R_{$D(___T6,_,__B:Array [Array [Array [Array [Float ,92],07],07],07];P,yC,I7i:Float ;_6w:g__;_,a9:Array [Int ,07];_q,H,r3N,__H,_3,W_b:B){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1941))

    def test_1942(self):
        input = '''Class _4{Val M,$pN,$JI__:_;}Class _0{Val v,N:Array [String ,58];Var $7_E,$j,$w,Q:Float ;Val T:Array [Array [Array [Array [Array [Int ,0x1],0B1_11],72],042],58];}Class _5e_4:d_Jm0H_{Val $_Zq__:F;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1942))

    def test_1943(self):
        input = '''Class _:_{Val $1:Array [Array [Float ,0100],67];_(){}Constructor (__4,U,_9:_){}Val $08:e;Destructor (){}Var X,_,_:Array [Array [String ,1],0b1];}Class _w1H:t{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1943))

    def test_1944(self):
        input = '''Class X{$_8(_gX6:_;_,___:Array [Array [Int ,05],07];_:Array [Array [String ,01],02_4];k5,_,_:Array [String ,0x46];_,h__,_,_,_:Array [Array [Int ,0b11],0b1000011];_,__7:_){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1944))

    def test_1945(self):
        input = '''Class _:_kj{Constructor (_,__:Int ;_h,B6j_D:Array [Float ,0b1];i4C,t4,e_:X;i,_6:Array [Array [Array [Boolean ,0x12],0x12],6];y:Array [String ,04_5]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1945))

    def test_1946(self):
        input = '''Class U_5_h__78_:T2{}Class c7R:X{Constructor (_2_V,_,S:Array [Int ,042]){Continue ;}Var _,FAtx772:_L;Val $4,$9,$__79,$__1:B_;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1946))

    def test_1947(self):
        input = '''Class _:_Ty{Destructor (){}$_(R1:Array [Array [Array [Boolean ,032],0b101101],0xA];_:_;t,_:Q;a4_:Array [Array [Array [Int ,0x35],0x35],0B1]){} }Class ___yV:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1947))

    def test_1948(self):
        input = '''Class U9{Var $222_1,$99,R,_j,_:Int ;Constructor (){} }Class I8{Destructor (){}Val $1,$_2g,v_,$_,$K5q5_la:Array [Int ,3];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1948))

    def test_1949(self):
        input = '''Class _{Constructor (_:Array [Int ,0b11110];Y:t9;N8,e___,X:Boolean ){} }Class _{_(_,_z25_k:Array [Array [Float ,072],90];_:Array [Array [Array [Array [Float ,4],072],0B110],0x6]){Val qiC,C,_,_,ZZ,ip,__:Array [Array [Array [Array [Float ,0B1000110],90],0B1000110],0XC];H::$q();} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1949))

    def test_1950(self):
        input = '''Class _Sc{}Class _8__{Var $__:___;Constructor (_,_,U:H_;_,Q7:Array [Array [Array [Boolean ,0124],0B1],0B1010001];_8:String ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1950))

    def test_1951(self):
        input = '''Class ____:_4{}Class _{$B(__,_:Array [Array [Array [Boolean ,02],06],93]){} }Class E_F__:_Y_t___{Var $P_,$aH:Float ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1951))

    def test_1952(self):
        input = '''Class _8:A{}Class _:_5U{$9wRF(){Return ;}Val $4,$e,$r:Array [Float ,0b111110];}Class _:f{Constructor (){}Val __:i;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1952))

    def test_1953(self):
        input = '''Class w_:G{}Class _{Val C0_:Y__;}Class __vE_:___{}Class s:S{Var _,_2,z_,$_,_,_6,$3:Array [Array [Array [Int ,03],0x15],0X1];q8_(){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1953))

    def test_1954(self):
        input = '''Class c{}Class _:__{Constructor (_,_:Array [Int ,0x3_1_0_1]){Continue ;Var __,Nf:Int ;}Var $N_,$_:String ;}Class r_:hO{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1954))

    def test_1955(self):
        input = '''Class mh2_{Q(d:Array [Array [Array [Array [Float ,0X2A],19],0X2],0xE_2];_l,_7a,VLX:Array [Int ,01_06_2_2_46163_4];_o:Float ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1955))

    def test_1956(self):
        input = '''Class O_:_WUg{}Class _7___5T:z6V{Var $8:r6;}Class B{Constructor (){} }Class _{Val $j67j_,K_pvG_f,$__:String ;Constructor (RW_,r,Q_:_3;v,_4X:String ;j,l2:jT_4){ {} }}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1956))

    def test_1957(self):
        input = '''Class v:FQH{}Class _xv{Destructor (){}Var __,$44__:_Q38;}Class _:j{Destructor (){} }Class ba:l{Var $7,_t,eS3,$7,h:Boolean ;}Class _{Val RX5_:O4t;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1957))

    def test_1958(self):
        input = '''Class S1{}Class _:a_6F{Constructor (E:Int ;_,u,Rt77y03RL_2:_){}Val h:Int ;Val M:Array [Array [Boolean ,0B110010],0B1_00_1];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1958))

    def test_1959(self):
        input = '''Class _{Constructor (R,_,n_:Boolean ;W:Array [Float ,12];G,R:Array [Array [String ,0x4],0X1A];y__L_a8W36:_vHW;z,__,_,Bm:Array [Array [Array [Array [Array [Boolean ,0x4],12],0b101011],0B11],0X1A];_,__86d,_,x,_:Float ;_:H){Return ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1959))

    def test_1960(self):
        input = '''Class i{Constructor (n84_,_,_K,_:Array [Array [Array [Int ,8],0XF],0X19];_Y:Ff;J_:Array [Array [Array [Array [Float ,0X19],0101],0XA],0X19]){Continue ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1960))

    def test_1961(self):
        input = '''Class ___{_(c:M__;q_:_;__5_7T,I:Array [String ,32];_,___Q:Array [Array [Array [Float ,051],051],051];U1:i6;s:Array [Boolean ,0B1]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1961))

    def test_1962(self):
        input = '''Class _{}Class sN:_D{}Class _{Constructor (_254,_:Array [Array [Array [Array [Array [Array [Float ,07_1],0x7],07_64],011],0x7],0X25]){}Val $N_:Array [Array [Array [Float ,037],037],0B101101];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1962))

    def test_1963(self):
        input = '''Class ____:MW{Val _,$_,urY6i_68:Float ;}Class _0U9cl_:J9y{Constructor (_:Float ){}Var j2:Array [Array [Array [Array [String ,9],0b110111],96],06];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1963))

    def test_1964(self):
        input = '''Class F:L_F{}Class _{Val $_:_;}Class ___{}Class l{Var _:String ;_(){} }Class Q:u{D(__,J8,_:Array [Boolean ,76];H:Float ;_,_,_:Boolean ;y:String ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1964))

    def test_1965(self):
        input = '''Class _X_:__{}Class l{Val h,$O,_R:Array [Array [Int ,284],0X18];Destructor (){Var __,_,b1,_:Array [String ,8];} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1965))

    def test_1966(self):
        input = '''Class _{Destructor (){Continue ;} }Class _2:X4{Var $A,$9_0,w:Array [Array [Array [Boolean ,0111],0x14],0b10001];Val v:__XLS3_;X(){} }Class k_:_{}Class H{}Class J:F4X_3{}Class _:E2{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1966))

    def test_1967(self):
        input = '''Class __4:_{Var l:Float ;Val $v_:R;Constructor (_,_c,b:Array [Array [Array [Array [Array [Array [Float ,0b1],0B1100],016],3],6],0b1010111]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1967))

    def test_1968(self):
        input = '''Class _{Constructor (){ {}{} }Val _,Z:Array [Array [Array [Array [Array [String ,6],0b1000100],6],0xF],0b1_00];Var $Pj0,$2:String ;Var $4_,_:_L;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1968))

    def test_1969(self):
        input = '''Class _{}Class w_:____h8{$3(d,__:Array [Array [Array [Array [Array [Float ,0X5_5_C],0X1E],015],0b1],0b1011010]){_2::$i();Val u:String ;Break ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1969))

    def test_1970(self):
        input = '''Class L_89{Destructor (){}Destructor (){Continue ;}Val $5:_;Var $19__,$N:Int ;Destructor (){s::$_.E_2_.O___4()._().c();} }Class _:cP{}Class _{Var M,_,$_:T_;}Class _{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1970))

    def test_1971(self):
        input = '''Class xQ{Constructor (_,_,m,_tZK:Float ;Ez,_,G,f:String ;IGn:Array [Array [Array [Array [Array [Float ,6],1],0B1],8_4_7],0B1]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1971))

    def test_1972(self):
        input = '''Class _:u{Constructor (_:Array [Float ,9_2_2_65]){}q(_,S0O,g:Float ;z_,C,T,_:Z;_m_6_:Array [Array [Array [Float ,0x39],0xF_C],87]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1972))

    def test_1973(self):
        input = '''Class Th:m{$X__0466f9(){}$_(__:Boolean ;H,_:Array [Array [Array [Int ,91],0x8C_5],0x3A];_:String ){Var _Wl,m_,__:__;Break ;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1973))

    def test_1974(self):
        input = '''Class AI_{Val A_R3c:g;}Class H_:_{Constructor (){}Constructor (){}hq7(){} }Class f:d_g0{$1(_,_:_){}Constructor (ih0_kR9,i,_2,v_:Boolean ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1974))

    def test_1975(self):
        input = '''Class _5:_{Val Yh_8J_,$DM,_:String ;Val y0,_,o6:Array [Array [Array [Int ,0X82],0103],0b11];}Class Y{Val _,o5,$E__:String ;Val $5Aw:String ;Val _:Boolean ;}Class _:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1975))

    def test_1976(self):
        input = '''Class _{}Class _HkC{Constructor (_:_N;_BB9:String ;A0_:String ;O_:Float ;__3_j__6,_,__Uo:Array [Array [Array [Int ,061],045_3_41553],01];Cq60N,_:_3){} }Class _{Var _:Boolean ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1976))

    def test_1977(self):
        input = '''Class _:g{}Class y:w_71{}Class wf:_{Constructor (t27:Array [Array [Array [Float ,045],17],05_43]){} }Class T_:m{Constructor (_,__9,__,_,Fps,oY57,V,_,_:_){}Destructor (){}Var $v:String ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1977))

    def test_1978(self):
        input = '''Class l:_{}Class E4i{e(E4,s_U,C_5Jp:Boolean ;_0_,__S,g4U,_n__5AS,_,___,_,E,__S,_,_,Q:_;m_57,_,e,W:Float ;_W,m_:Array [Float ,0b1];g,_,_,P,__3,__P5,_8:_;R_,p__9:_;g872:Int ){}Var I:Boolean ;Val _5V3114:Float ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1978))

    def test_1979(self):
        input = '''Class I{}Class s{}Class T:__5{Val $w:Boolean ;}Class _:_9{}Class _{}Class n1_{}Class _9{Destructor (){Break ;} }Class _:B{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1979))

    def test_1980(self):
        input = '''Class _n3{}Class _:Nh{}Class g75R{}Class _9{Destructor (){}Val E0:Array [Array [Array [Array [Boolean ,44],0b1],01],44];}Class _:Y{}Class p0{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1980))

    def test_1981(self):
        input = '''Class __:z6{Val __Y:Array [Boolean ,0B1_0];}Class _0_U:S_{Var $C,_:Array [Array [Array [String ,0X4E],0x5F],0X3];$4_(S:Int ;__:B___;_c,F,Hw,G:Int ){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1981))

    def test_1982(self):
        input = '''Class L8{qZ2(){} }Class _2g:_9{Val $37:Array [Array [Array [Array [Array [Array [Float ,0x26],020],0b11],0B1],020],0b1001101];Var $515:Array [Array [Array [Array [Array [Int ,22],020],0X2_77],0x8_0_9_1],5];}Class G{}Class _:_{Var ur_:_;}Class Q{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1982))

    def test_1983(self):
        input = '''Class S5:_R_8{__(_:Array [Array [Array [Boolean ,0103],0B1],0b1]){} }Class CM5:_c{}Class _r:I{}Class _{}Class _:_{Var $u,_T,_,___:Int ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1983))

    def test_1984(self):
        input = '''Class B{Var $06_,$44,_T,$e_,K:Array [Array [Array [Array [Array [Array [Array [Boolean ,0x30_2A_7],0X4A],0b1100010],056],0X4A],0B11],0XD_3];}Class _{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1984))

    def test_1985(self):
        input = '''Class _0{Constructor (__:_0){}Destructor (){}Constructor (lN_b:Array [Boolean ,98];d,_:Int ;_,x,_z,v99:Array [String ,98];_A_,_:Array [Array [Boolean ,0xB5],0b1];__,z,e:Int ;_1,__:Array [Array [String ,0x31],0b1000000];C:Int ;_:N){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1985))

    def test_1986(self):
        input = '''Class T:e{Constructor (__L:Array [Array [Array [Float ,9],0X1],0b1_0];K_2:Array [Array [Boolean ,0120],0b111]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1986))

    def test_1987(self):
        input = '''Class V_{Constructor (Y71,__xHt2_i__:Array [Array [String ,0XAA],064];___QgM,_6_AX,r,_K:_B_;_P961ZC1:____;H,u:Array [Array [Array [Array [Float ,042_1],0b1000],064],0b1];_,_O5,G,_,x,_,VK,_:String ;_n,E:Array [Array [Array [Array [Boolean ,0b1000],3],9],0X39];_T_:Boolean ;__,y3,vl:Array [Array [Int ,03_4],0B1_0_01_1_0_11];i,_:_4_){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1987))

    def test_1988(self):
        input = '''Class t:K8{Var $_:Float ;Var U_R,S:_d_3;}Class UL:_{}Class V:_{Val pD_,$7,$o:_f;}Class lk{}Class _:Z_{Var $70:HW;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1988))

    def test_1989(self):
        input = '''Class P{Var $_:String ;Val _,$EB:String ;Constructor (){}$0(_:Array [Array [Float ,0x9],0X3]){}Constructor (_r,_:_;_l:_;_,y:V){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1989))

    def test_1990(self):
        input = '''Class eL8_:D_{Destructor (){} }Class U:F6{}Class T{Constructor (Z7_3q7_:Array [String ,0b10]){} }Class __491K6{Destructor (){Break ;} }Class Cz:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1990))

    def test_1991(self):
        input = '''Class U77_d{}Class _{}Class _v:z_{Constructor (T,F_94:Float ;h:Array [Int ,5];C8,fs9,_,Ot:Boolean ){}Var _,$_:String ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1991))

    def test_1992(self):
        input = '''Class _{Destructor (){}$l(P__V,_kN:Array [Int ,8_7_08];K,d,__h,Q_,KJq,_,K,_:F_;E3:_){}Val $9_v,$9:Int ;}Class U8:h_{I(T,P,n:Array [Float ,0102]){} }Class _:_0{y4(){ {}{} }Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1992))

    def test_1993(self):
        input = '''Class _{}Class r79:__2{H_(P,_:_44Z;h5:Array [Array [Float ,96],0B100000];__,_:Float ;_,Ns,vW1_,zI,_,d,a:Int ){}y(){}Val _R,$fi:NkI;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1993))

    def test_1994(self):
        input = '''Class ___4{}Class Y{Constructor (){}Val $n,$_,$qo_3,$h1,$0,$0:Array [Array [Boolean ,0b111_0],44];Destructor (){}_(E,_,d,a,__:v_A){ {} }_S(){} }Class q:_{$_M(){}Destructor (){Continue ;}$2(){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1994))

    def test_1995(self):
        input = '''Class _{Val _,$W,$v8:_R5;}Class _:YM5{}Class _i{}Class _{Constructor (_,_:_){Return ;}$1(_:__;__,m:Array [Boolean ,0B111]){}Var _,___,$_8,$_M:x;}Class _{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1995))

    def test_1996(self):
        input = '''Class _{Var $_m,$B_1Nv_98,yY:C;}Class C:f{Var s:Array [Array [Array [Array [String ,100],0x6],0B11_1],05];}Class _4_1:G{}Class E3{Val _:Boolean ;Var _:_4_;Val F:Array [Array [Array [Array [Int ,100],2],0xEA_E],061];Var D_,_,__82:Boolean ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1996))

    def test_1997(self):
        input = '''Class Z1{}Class _{Var _4U7:Array [Array [Array [Boolean ,32],32],0b1];}Class _f2_{Val _C,$p,_:Array [Boolean ,0B10000];Var _:Int ;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1997))

    def test_1998(self):
        input = '''Class b:g{Val $9_:Array [Array [Array [Array [Array [Array [Array [Float ,73_1_6],1_1_1],02],14],64],0x2A],14];Var _0,G3:Int ;Destructor (){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1998))

    def test_1999(self):
        input = '''Class _:w{Val $_0y:Array [Array [Float ,01_3_6],5];Var $_02_,w:Array [Array [Float ,0110],0x8];}Class R:_{}Class ___:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1999))
