import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
   # def test_300(self):
   #     """Simple program: int main() {} """
   #     input = "Class Program {}"
   #     expect = 'Program([ClassDecl(Id(Program),[])])'
   #     self.assertTrue(TestAST.test(input,expect,300))
   # def test_301(self):
   #     """Simple program: int main() {} """
   #     input = "Class A:B {}"
   #     expect = 'Program([ClassDecl(Id(A),Id(B),[])])'
   #     self.assertTrue(TestAST.test(input,expect,301))
   # def test_302(self):
   #     """Simple program: int main() {} """
   #     input = "Class A {} Class B {} Class C {}"
   #     expect = 'Program([ClassDecl(Id(A),[]),ClassDecl(Id(B),[]),ClassDecl(Id(C),[])])'
   #     self.assertTrue(TestAST.test(input,expect,302))
   # def test_303(self):
   #     """Simple program: int main() {} """
   #     input = """
   #     Class A {
   #         Var a:Int;
   #     }
   #     """
   #     expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Instance,VarDecl(Id(a),IntType))])])'
   #     self.assertTrue(TestAST.test(input,expect,303))
   # def test_304(self):
   #     """Simple program: int main() {} """
   #     input = """
   #     Class A {
   #         Var a:Int;
   #         Var b:Int;
   #     }
   #     """
   #     expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Instance,VarDecl(Id(a),IntType)),AttributeDecl(Instance,VarDecl(Id(b),IntType))])])'
   #     self.assertTrue(TestAST.test(input,expect,304))
   # def test_305(self):
   #     """Simple program: int main() {} """
   #     input = """
   #     Class A {
   #         Var a:Array[Int,5];
   #     }
   #     """
   #     expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Instance,VarDecl(Id(a),ArrayType(5,IntType)))])])'
   #     self.assertTrue(TestAST.test(input,expect,305))
   # def test_306(self):
   #     """Simple program: int main() {} """
   #     input = """
   #     Class A {
   #         Var a:Int=1;
   #     }
   #     """
   #     expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Instance,VarDecl(Id(a),IntType,IntLit(1)))])])'
   #     self.assertTrue(TestAST.test(input,expect,306))
   # def test_307(self):
   #     """Simple program: int main() {} """
   #     input = """
   #     Class A {
   #         Var a:Int=1+1;
   #     }
   #     """
   #     expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Instance,VarDecl(Id(a),IntType,BinaryOp(+,IntLit(1),IntLit(1))))])])'
   #     self.assertTrue(TestAST.test(input,expect,307))
   # def test_308(self):
   #     """Simple program: int main() {} """
   #     input = """
   #     Class A {
   #         Var a:Int=1+1*2;
   #     }
   #     """
   #     expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Instance,VarDecl(Id(a),IntType,BinaryOp(+,IntLit(1),BinaryOp(*,IntLit(1),IntLit(2)))))])])'
   #     self.assertTrue(TestAST.test(input,expect,308))
   # def test_309(self):
   #     """Simple program: int main() {} """
   #     input = """
   #     Class A {
   #         Var a:Int=\"abc\"+.1+2;
   #     }
   #     """
   #     expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Instance,VarDecl(Id(a),IntType,BinaryOp(+.,StringLit(abc),BinaryOp(+,IntLit(1),IntLit(2)))))])])'
   #     self.assertTrue(TestAST.test(input,expect,309))
   # def test_310(self):
   #     """Simple program: int main() {} """
   #     input = """
   #     Class A {
   #         Var a:Int=!!a---2*---3;
   #     }
   #     """
   #     expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Instance,VarDecl(Id(a),IntType,BinaryOp(-,UnaryOp(!,UnaryOp(!,Id(a))),BinaryOp(*,UnaryOp(-,UnaryOp(-,IntLit(2))),UnaryOp(-,UnaryOp(-,UnaryOp(-,IntLit(3))))))))])])'
   #     self.assertTrue(TestAST.test(input,expect,310))
   # def test_311(self):
   #     """Simple program: int main() {} """
   #     input = """
   #     Class A {
   #         Val a:Boolean=True;
   #     }
   #     """
   #     expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Instance,ConstDecl(Id(a),BoolType,BooleanLit(True)))])])'
   #     self.assertTrue(TestAST.test(input,expect,311))
   # def test_312(self):
   #     """Simple program: int main() {} """
   #     input = """
   #     Class A {
   #         Val a:String=b[1][1];
   #     }
   #     """
   #     expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Instance,ConstDecl(Id(a),StringType,ArrayCell(Id(b),[IntLit(1),IntLit(1)])))])])'
   #     self.assertTrue(TestAST.test(input,expect,312))
   # def test_313(self):
   #     """Simple program: int main() {} """
   #     input = """
   #     Class A {
   #         Var a:Int = New a();
   #     }
   #     """
   #     expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Instance,VarDecl(Id(a),IntType,NewExpr(Id(a),[])))])])'
   #     self.assertTrue(TestAST.test(input,expect,313))
   # def test_314(self):
   #     """Simple program: int main() {} """
   #     input = """
   #     Class A {
   #         Val b:Int = Null;
   #     }
   #     """
   #     expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Instance,ConstDecl(Id(b),IntType,NullLiteral()))])])'
   #     self.assertTrue(TestAST.test(input,expect,314))
   # def test_315(self):
   #     """Simple program: int main() {} """
   #     input = """
   #     Class A {
   #         Val b:Int = New a(1+2,Null);
   #     }
   #     """
   #     expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Instance,ConstDecl(Id(b),IntType,NewExpr(Id(a),[BinaryOp(+,IntLit(1),IntLit(2)),NullLiteral()])))])])'
   #     self.assertTrue(TestAST.test(input,expect,315))
   # def test_316(self):
   #     """Simple program: int main() {} """
   #     input = """
   #     Class A {
   #         Var $b:Float=6.9;
   #     }
   #     """
   #     expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Static,VarDecl(Id($b),FloatType,FloatLit(6.9)))])])'
   #     self.assertTrue(TestAST.test(input,expect,316))
   # def test_317(self):
   #     input = """
   #     Class A {
   #         foo(){}
   #     }
   #     """
   #     expect = 'Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[],Block([]))])])'
   #     self.assertTrue(TestAST.test(input, expect, 317))
   # def test_318(self):
   #     input = """
   #     Class A {
   #         foo(a,b:Int;c:Float){}
   #     }
   #     """
   #     expect = 'Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),FloatType)],Block([]))])])'
   #     self.assertTrue(TestAST.test(input, expect, 318))
   # def test_319(self):
   #     input = """
   #     Class A {
   #         foo(a:Int;b:Boolean;c:String){}
   #     }
   #     """
   #     expect = 'Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[param(Id(a),IntType),param(Id(b),BoolType),param(Id(c),StringType)],Block([]))])])'
   #     self.assertTrue(TestAST.test(input, expect, 319))
   # def test_320(self):
   #     input = """
   #     Class A {
   #         foo(){
   #             Var a:Int;
   #         }
   #     }
   #     """
   #     expect = 'Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[],Block([VarDecl(Id(a),IntType)]))])])'
   #     self.assertTrue(TestAST.test(input, expect, 320))
   # def test_321(self):
   #     input = """
   #     Class A {
   #         foo(){
   #             Var a:Int = 1;
   #         }
   #     }
   #     """
   #     expect = 'Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[],Block([VarDecl(Id(a),IntType,IntLit(1))]))])])'
   #     self.assertTrue(TestAST.test(input, expect, 321))
   # def test_322(self):
   #     input = """
   #     Class A {
   #         foo(){
   #             Var a:Int = 1;
   #             Var b:Float = 1.0;
   #             Val c:Boolean = True;
   #         }
   #     }
   #     """
   #     expect = 'Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[],Block([VarDecl(Id(a),IntType,IntLit(1)),VarDecl(Id(b),FloatType,FloatLit(1.0)),ConstDecl(Id(c),BoolType,BooleanLit(True))]))])])'
   #     self.assertTrue(TestAST.test(input, expect, 322))
   # def test_323(self):
   #     input = """
   #     Class A {
   #         Var $b:Int = 1;
   #         foo(){
   #             Var a:Int = 1;
   #         }
   #     }
   #     """
   #     expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Static,VarDecl(Id($b),IntType,IntLit(1))),MethodDecl(Id(foo),Instance,[],Block([VarDecl(Id(a),IntType,IntLit(1))]))])])'
   #     self.assertTrue(TestAST.test(input, expect, 323))
   # def test_324(self):
   #     input = """
   #     Class A {
   #         foo(a,b,c,d,e:Int){
   #             Var f:Int = 1+2*3;
   #         }
   #     }
   #     """
   #     expect = 'Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType),param(Id(d),IntType),param(Id(e),IntType)],Block([VarDecl(Id(f),IntType,BinaryOp(+,IntLit(1),BinaryOp(*,IntLit(2),IntLit(3))))]))])])'
   #     self.assertTrue(TestAST.test(input, expect, 324))
   # def test_325(self):
   #     input = """
   #     Class A {
   #         $foo(){
   #             Var a:Int = 2/3;
   #             a=1;
   #         }
   #     }
   #     """
   #     expect = 'Program([ClassDecl(Id(A),[MethodDecl(Id($foo),Static,[],Block([VarDecl(Id(a),IntType,BinaryOp(/,IntLit(2),IntLit(3))),AssignStmt(Id(a),IntLit(1))]))])])'
   #     self.assertTrue(TestAST.test(input, expect, 325))
   # def test_326(self):
   #     input = """
   #     Class A {
   #         $foo(){
   #             a[1][3+4]=1;
   #         }
   #     }
   #     """
   #     expect = 'Program([ClassDecl(Id(A),[MethodDecl(Id($foo),Static,[],Block([AssignStmt(ArrayCell(Id(a),[IntLit(1),BinaryOp(+,IntLit(3),IntLit(4))]),IntLit(1))]))])])'
   #     self.assertTrue(TestAST.test(input, expect, 326))
   # def test_327(self):
   #     input = """
   #     Class A {
   #         foo(){
   #             a[1][b[3]]="abc";
   #         }
   #     }
   #     """
   #     expect = 'Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[],Block([AssignStmt(ArrayCell(Id(a),[IntLit(1),ArrayCell(Id(b),[IntLit(3)])]),StringLit(abc))]))])])'
   #     self.assertTrue(TestAST.test(input, expect, 327))
   # def test_328(self):
   #     input = """
   #     Class A {
   #         foo(){
   #             a.b.c="abc";
   #         }
   #     }
   #     """
   #     expect = 'Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[],Block([AssignStmt(FieldAccess(FieldAccess(Id(a),Id(b)),Id(c)),StringLit(abc))]))])])'
   #     self.assertTrue(TestAST.test(input, expect, 328))
   # def test_329(self):
   #     input = """
   #     Class A {
   #         foo(){
   #             a.b.c[1]=d.e.f(1,2+3);
   #         }
   #     }
   #     """
   #     expect = 'Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[],Block([AssignStmt(ArrayCell(FieldAccess(FieldAccess(Id(a),Id(b)),Id(c)),[IntLit(1)]),CallExpr(FieldAccess(Id(d),Id(e)),Id(f),[IntLit(1),BinaryOp(+,IntLit(2),IntLit(3))]))]))])])'
   #     self.assertTrue(TestAST.test(input, expect, 329))
   def test_330(self):
       input = """
       Class A {
           foo(){
               Var a:A = d.e.f(1,2+3) + 2;
           }
       }
       """
       expect = 'Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[],Block([VarDecl(Id(a),ClassType(Id(A)),BinaryOp(+,CallExpr(FieldAccess(Id(d),Id(e)),Id(f),[IntLit(1),BinaryOp(+,IntLit(2),IntLit(3))]),IntLit(2)))]))])])'
       self.assertTrue(TestAST.test(input, expect, 330))
   def test_331(self):
       input = """
       Class A {
           foo(){
               Var a:Array[Array[Int,5],5];
           }
       }
       """
       expect = 'Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[],Block([VarDecl(Id(a),ArrayType(5,ArrayType(5,IntType)))]))])])'
       self.assertTrue(TestAST.test(input, expect, 331))
   def test_332(self):
       input = """
       Class A {
           foo(){
               Break;
               Continue;
               Return a==.!b;
               {}
           }
       }
       """
       expect = 'Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[],Block([Break,Continue,Return(BinaryOp(==.,Id(a),UnaryOp(!,Id(b)))),Block([])]))])])'
       self.assertTrue(TestAST.test(input, expect, 332))
   def test_333(self):
       input = """
       Class A:B{
           foo(){
               a = New a(1+2*3/4).b.c();
           }
       }
       """
       expect = 'Program([ClassDecl(Id(A),Id(B),[MethodDecl(Id(foo),Instance,[],Block([AssignStmt(Id(a),CallExpr(FieldAccess(NewExpr(Id(a),[BinaryOp(+,IntLit(1),BinaryOp(/,BinaryOp(*,IntLit(2),IntLit(3)),IntLit(4)))]),Id(b)),Id(c),[]))]))])])'
       self.assertTrue(TestAST.test(input, expect, 333))
   def test_334(self):
       input = """
       Class A:B{
           foo(){
               a = New a(1+2*3/4).b.c();
           }
       }
       """
       expect = 'Program([ClassDecl(Id(A),Id(B),[MethodDecl(Id(foo),Instance,[],Block([AssignStmt(Id(a),CallExpr(FieldAccess(NewExpr(Id(a),[BinaryOp(+,IntLit(1),BinaryOp(/,BinaryOp(*,IntLit(2),IntLit(3)),IntLit(4)))]),Id(b)),Id(c),[]))]))])])'
       self.assertTrue(TestAST.test(input, expect, 334))
   def test_335(self):
       input = """
       Class A:B{
           foo(){
               a = (1+2)*3;
           }
       }
       """
       expect = 'Program([ClassDecl(Id(A),Id(B),[MethodDecl(Id(foo),Instance,[],Block([AssignStmt(Id(a),BinaryOp(*,BinaryOp(+,IntLit(1),IntLit(2)),IntLit(3)))]))])])'
       self.assertTrue(TestAST.test(input, expect, 335))
   def test_336(self):
       input = """
       Class A:B{
           foo(){
               Return Self.foo();
           }
           Constructor (a,b:J){}
           Destructor (){}
       }
       """
       expect = 'Program([ClassDecl(Id(A),Id(B),[MethodDecl(Id(foo),Instance,[],Block([Return(CallExpr(Self(),Id(foo),[]))])),MethodDecl(Id(Constructor),Instance,[param(Id(a),ClassType(Id(J))),param(Id(b),ClassType(Id(J)))],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))])])'
       self.assertTrue(TestAST.test(input, expect, 336))
   def test_337(self):
       input = """
       Class A:B{
           Var a,$b:Int;
       }
       """
       expect = 'Program([ClassDecl(Id(A),Id(B),[AttributeDecl(Instance,VarDecl(Id(a),IntType)),AttributeDecl(Static,VarDecl(Id($b),IntType))])])'
       self.assertTrue(TestAST.test(input, expect, 337))
   def test_338(self):
       input = """
       Class A:B{
           Var a,$b:Int = 1,2;
           Val $c,d:Boolean = True, Null;
       }
       """
       expect = 'Program([ClassDecl(Id(A),Id(B),[AttributeDecl(Instance,VarDecl(Id(a),IntType,IntLit(1))),AttributeDecl(Static,VarDecl(Id($b),IntType,IntLit(2))),AttributeDecl(Static,ConstDecl(Id($c),BoolType,BooleanLit(True))),AttributeDecl(Instance,ConstDecl(Id(d),BoolType,NullLiteral()))])])'
       self.assertTrue(TestAST.test(input, expect, 338))
   def test_339(self):
       input = """
       Class A:B{
           Var a, b, c:Int;
           Foo(){
               Var a, b, c:Int;
           }
       }
       """
       expect = 'Program([ClassDecl(Id(A),Id(B),[AttributeDecl(Instance,VarDecl(Id(a),IntType)),AttributeDecl(Instance,VarDecl(Id(b),IntType)),AttributeDecl(Instance,VarDecl(Id(c),IntType)),MethodDecl(Id(Foo),Instance,[],Block([VarDecl(Id(a),IntType),VarDecl(Id(b),IntType),VarDecl(Id(c),IntType)]))])])'
       self.assertTrue(TestAST.test(input, expect, 339))
   def test_340(self):
       input = """
       Class A:B{
           Foo(){
               Val a, b, c:Int = 1,2,3;
               Var d:Boolean = True;
           }
       }
       """
       expect = 'Program([ClassDecl(Id(A),Id(B),[MethodDecl(Id(Foo),Instance,[],Block([ConstDecl(Id(a),IntType,IntLit(1)),ConstDecl(Id(b),IntType,IntLit(2)),ConstDecl(Id(c),IntType,IntLit(3)),VarDecl(Id(d),BoolType,BooleanLit(True))]))])])'
       self.assertTrue(TestAST.test(input, expect, 340))
   def test_341(self):
       input = """
       Class A:B{
           Var $a:Array[Int,3] = Array(1,1,1);
       }
       """
       expect = 'Program([ClassDecl(Id(A),Id(B),[AttributeDecl(Static,VarDecl(Id($a),ArrayType(3,IntType),[IntLit(1),IntLit(1),IntLit(1)]))])])'
       self.assertTrue(TestAST.test(input, expect, 341))
   def test_342(self):
       input = """
       Class A:B{
           Var $a:Array[Array[Int,1],3] = Array(Array(1),Array(1),Array(1));
       }
       """
       expect = 'Program([ClassDecl(Id(A),Id(B),[AttributeDecl(Static,VarDecl(Id($a),ArrayType(3,ArrayType(1,IntType)),[[IntLit(1)],[IntLit(1)],[IntLit(1)]]))])])'
       self.assertTrue(TestAST.test(input, expect, 342))
   def test_343(self):
       input = """
       Class A:B{
           Var $0:Int;
           $foo(i:Array [Boolean ,0105]){
               a=0105;
               b.c(Self,Null,Array(1)).d=0x12DEF;
               d[e][f[g]]=0B1010111011101;
           }
       }
       """
       expect = 'Program([ClassDecl(Id(A),Id(B),[AttributeDecl(Static,VarDecl(Id($0),IntType)),MethodDecl(Id($foo),Static,[param(Id(i),ArrayType(69,BoolType))],Block([AssignStmt(Id(a),IntLit(69)),AssignStmt(FieldAccess(CallExpr(Id(b),Id(c),[Self(),NullLiteral(),[IntLit(1)]]),Id(d)),IntLit(77295)),AssignStmt(ArrayCell(Id(d),[Id(e),ArrayCell(Id(f),[Id(g)])]),IntLit(5597))]))])])'
       self.assertTrue(TestAST.test(input, expect, 343))
   # def test_344(self):
   #     input = """
   #     Class A:B{
   #         Var $0,a,$1,b,$2,c:Int = 5,4,3,2,1,0;
   #     }
   #     """
   #     expect = 'Program([ClassDecl(Id(A),Id(B),[AttributeDecl(Static,VarDecl(Id($0),IntType,IntLit(5))),AttributeDecl(Instance,VarDecl(Id(a),IntType,IntLit(4))),AttributeDecl(Static,VarDecl(Id($1),IntType,IntLit(3))),AttributeDecl(Instance,VarDecl(Id(b),IntType,IntLit(2))),AttributeDecl(Static,VarDecl(Id($2),IntType,IntLit(1))),AttributeDecl(Instance,VarDecl(Id(c),IntType,IntLit(0)))])])'
   #     self.assertTrue(TestAST.test(input, expect, 344))
   # def test_345(self):
   #     input = """
   #     Class A:B{
   #         Foo(){
   #             If(1){}
   #         }
   #     }
   #     """
   #     expect = 'Program([ClassDecl(Id(A),Id(B),[MethodDecl(Id(Foo),Instance,[],Block([If(IntLit(1),Block([]))]))])])'
   #     self.assertTrue(TestAST.test(input, expect, 345))
   # def test_346(self):
   #     input = """
   #     Class A:B{
   #         Foo(){
   #             If(1){}
   #             If(2){}Else{}
   #             If(3){}Elseif(4){}Else{a=1;}
   #         }
   #     }
   #     """
   #     expect = 'Program([ClassDecl(Id(A),Id(B),[MethodDecl(Id(Foo),Instance,[],Block([If(IntLit(1),Block([])),If(IntLit(2),Block([]),Block([])),If(IntLit(3),Block([]),If(IntLit(4),Block([]),Block([AssignStmt(Id(a),IntLit(1))])))]))])])'
   #     self.assertTrue(TestAST.test(input, expect, 346))
   # def test_347(self):
   #     input = """
   #     Class A:B{
   #         Foo(){
   #             If(3){}Elseif(4){}Elseif(5){}Else{a=1;}
   #         }
   #     }
   #     """
   #     expect = 'Program([ClassDecl(Id(A),Id(B),[MethodDecl(Id(Foo),Instance,[],Block([If(IntLit(3),Block([]),If(IntLit(4),Block([]),If(IntLit(5),Block([]),Block([AssignStmt(Id(a),IntLit(1))]))))]))])])'
   #     self.assertTrue(TestAST.test(input, expect, 347))
   # def test_348(self):
   #     input = """
   #     Class A:B{
   #         Foo(){
   #             a.b(1+2,3*4-5.5);
   #             If(1)
   #                 {}
   #             Elseif(2)
   #                 {}
   #             Elseif(3)
   #                 {}
   #         }
   #     }
   #     """
   #     expect = 'Program([ClassDecl(Id(A),Id(B),[MethodDecl(Id(Foo),Instance,[],Block([Call(Id(a),Id(b),[BinaryOp(+,IntLit(1),IntLit(2)),BinaryOp(-,BinaryOp(*,IntLit(3),IntLit(4)),FloatLit(5.5))]),If(IntLit(1),Block([]),If(IntLit(2),Block([]),If(IntLit(3),Block([]))))]))])])'
   #     self.assertTrue(TestAST.test(input, expect, 348))
   # def test_349(self):
   #     input = """
   #     Class A: B
   #     {
   #         Foo()
   #         {
   #             If(3)
   #                 {Val a: Int = 0X1234;}
   #             Elseif(4)
   #                 {{}}
   #             Elseif(5)
   #                 {Return Self;}
   #             Else
   #                 {a = 1;}
   #         }
   #     }
   #     """
   #     expect = 'Program([ClassDecl(Id(A),Id(B),[MethodDecl(Id(Foo),Instance,[],Block([If(IntLit(3),Block([ConstDecl(Id(a),IntType,IntLit(4660))]),If(IntLit(4),Block([Block([])]),If(IntLit(5),Block([Return(Self())]),Block([AssignStmt(Id(a),IntLit(1))]))))]))])])'
   #     self.assertTrue(TestAST.test(input, expect, 349))
   # def test_350(self):
   #     line = '''Class D:__p{}Class c{}Class _73_{}Class I_:C{Destructor (){ {l::$0V4___();} }}'''
   #     expect = '''Program([ClassDecl(Id(D),Id(__p),[]),ClassDecl(Id(c),[]),ClassDecl(Id(_73_),[]),ClassDecl(Id(I_),Id(C),[MethodDecl(Id(Destructor),Instance,[],Block([Block([Call(Id(l),Id($0V4___),[])])]))])])'''
   #     self.assertTrue(TestAST.test(line, expect, 350))
   # def test_351(self):
   #     line = '''Class Y7t_C2_oW:g__{Constructor (_,s,AN4_F,__,g,_s:v;_:VZV2_;k_,_k,_4,P:Float ){_::$aJ.HF_.UZ._();} }Class _:__{}'''
   #     expect = '''Program([ClassDecl(Id(Y7t_C2_oW),Id(g__),[MethodDecl(Id(Constructor),Instance,[param(Id(_),ClassType(Id(v))),param(Id(s),ClassType(Id(v))),param(Id(AN4_F),ClassType(Id(v))),param(Id(__),ClassType(Id(v))),param(Id(g),ClassType(Id(v))),param(Id(_s),ClassType(Id(v))),param(Id(_),ClassType(Id(VZV2_))),param(Id(k_),FloatType),param(Id(_k),FloatType),param(Id(_4),FloatType),param(Id(P),FloatType)],Block([Call(FieldAccess(FieldAccess(FieldAccess(Id(_),Id($aJ)),Id(HF_)),Id(UZ)),Id(_),[])]))]),ClassDecl(Id(_),Id(__),[])])'''
   #     self.assertTrue(TestAST.test(line, expect, 351))
   # def test_352(self):
   #     line = '''Class G{$Z3(p,_:Array [Array [Array [Int ,0B1001100],061],0b1_0];M:Float ;K,v5_:Int ;p,_,t:_){_::$_()._0._EkG();}$0(j9,E_,_:j){}$_(_xy:Array [Boolean ,061]){} }Class _:_AE{}'''
   #     expect = '''Program([ClassDecl(Id(G),[MethodDecl(Id($Z3),Static,[param(Id(p),ArrayType(2,ArrayType(49,ArrayType(76,IntType)))),param(Id(_),ArrayType(2,ArrayType(49,ArrayType(76,IntType)))),param(Id(M),FloatType),param(Id(K),IntType),param(Id(v5_),IntType),param(Id(p),ClassType(Id(_))),param(Id(_),ClassType(Id(_))),param(Id(t),ClassType(Id(_)))],Block([Call(FieldAccess(CallExpr(Id(_),Id($_),[]),Id(_0)),Id(_EkG),[])])),MethodDecl(Id($0),Static,[param(Id(j9),ClassType(Id(j))),param(Id(E_),ClassType(Id(j))),param(Id(_),ClassType(Id(j)))],Block([])),MethodDecl(Id($_),Static,[param(Id(_xy),ArrayType(49,BoolType))],Block([]))]),ClassDecl(Id(_),Id(_AE),[])])'''
   #     self.assertTrue(TestAST.test(line, expect, 352))
   # def test_353_683_PN(self):
   #     line = """Class D{Var _9f1,_:l_;}Class m_:r_{Val $_:Int =---"\\t";Var _17_:Int ;}"""
   #     expect = '''Program([ClassDecl(Id(D),[AttributeDecl(Instance,VarDecl(Id(_9f1),ClassType(Id(l_)),NullLiteral())),AttributeDecl(Instance,VarDecl(Id(_),ClassType(Id(l_)),NullLiteral()))]),ClassDecl(Id(m_),Id(r_),[AttributeDecl(Static,ConstDecl(Id($_),IntType,UnaryOp(-,UnaryOp(-,UnaryOp(-,StringLit(\\t)))))),AttributeDecl(Instance,VarDecl(Id(_17_),IntType))])])'''
   #     self.assertTrue(TestAST.test(line, expect, 353))
   # def test_354_905_PN(self):
   #     line = '''Class _{}Class l__:_k_6t{}Class W{Val T4:String =!!J_::$__;}'''
   #     expect = '''Program([ClassDecl(Id(_),[]),ClassDecl(Id(l__),Id(_k_6t),[]),ClassDecl(Id(W),[AttributeDecl(Instance,ConstDecl(Id(T4),StringType,UnaryOp(!,UnaryOp(!,FieldAccess(Id(J_),Id($__))))))])])'''
   #     self.assertTrue(TestAST.test(line, expect, 354))
   # def test_355_745_PN(self):
   #     line = '''Class _:x4_{Val _GO:k=!__.F()<=yYF9::$7._()._A_N._.L7K+!tW0::$iw_9();}'''
   #     expect = '''Program([ClassDecl(Id(_),Id(x4_),[AttributeDecl(Instance,ConstDecl(Id(_GO),ClassType(Id(k)),BinaryOp(<=,UnaryOp(!,CallExpr(Id(__),Id(F),[])),BinaryOp(+,FieldAccess(FieldAccess(FieldAccess(CallExpr(FieldAccess(Id(yYF9),Id($7)),Id(_),[]),Id(_A_N)),Id(_)),Id(L7K)),UnaryOp(!,CallExpr(Id(tW0),Id($iw_9),[]))))))])])'''
   #     self.assertTrue(TestAST.test(line, expect, 355))
   # def test_356_646_PN(self):
   #     line = '''Class _V_7{Var _86:Int =!-New k___()._.j_Z._._s3();Destructor (){} }Class _{Var $_5_,z_:Array [Array [String ,2],80];}'''
   #     expect = '''Program([ClassDecl(Id(_V_7),[AttributeDecl(Instance,VarDecl(Id(_86),IntType,UnaryOp(!,UnaryOp(-,CallExpr(FieldAccess(FieldAccess(FieldAccess(NewExpr(Id(k___),[]),Id(_)),Id(j_Z)),Id(_)),Id(_s3),[]))))),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(_),[AttributeDecl(Static,VarDecl(Id($_5_),ArrayType(80,ArrayType(2,StringType)))),AttributeDecl(Instance,VarDecl(Id(z_),ArrayType(80,ArrayType(2,StringType))))])])'''
   #     self.assertTrue(TestAST.test(line, expect, 356))
   # def test_357_597_PN(self):
   #     line = '''Class _j{Constructor (_,_4m_q_R6r:_){}Var $o:String ;Val $3O:H=_::$_;}'''
   #     expect = '''Program([ClassDecl(Id(_j),[MethodDecl(Id(Constructor),Instance,[param(Id(_),ClassType(Id(_))),param(Id(_4m_q_R6r),ClassType(Id(_)))],Block([])),AttributeDecl(Static,VarDecl(Id($o),StringType)),AttributeDecl(Static,ConstDecl(Id($3O),ClassType(Id(H)),FieldAccess(Id(_),Id($_))))])])'''
   #     self.assertTrue(TestAST.test(line, expect, 357))
   # def test_358_313_PN(self):
   #     line = '''Class _:qc0R{}Class E{Var _:E=-New _().kD9.p.F.d().k.h6e71_;}'''
   #     expect = '''Program([ClassDecl(Id(_),Id(qc0R),[]),ClassDecl(Id(E),[AttributeDecl(Instance,VarDecl(Id(_),ClassType(Id(E)),UnaryOp(-,FieldAccess(FieldAccess(CallExpr(FieldAccess(FieldAccess(FieldAccess(NewExpr(Id(_),[]),Id(kD9)),Id(p)),Id(F)),Id(d),[]),Id(k)),Id(h6e71_)))))])])'''
   #     self.assertTrue(TestAST.test(line, expect, 358))
   # def test_359_233_PN(self):
   #     line = '''Class R:_{}Class _8_:_B{}Class _:_4{Var $b:Array [String ,0B1]=!-Self ;}'''
   #     expect = '''Program([ClassDecl(Id(R),Id(_),[]),ClassDecl(Id(_8_),Id(_B),[]),ClassDecl(Id(_),Id(_4),[AttributeDecl(Static,VarDecl(Id($b),ArrayType(1,StringType),UnaryOp(!,UnaryOp(-,Self()))))])])'''
   #     self.assertTrue(TestAST.test(line, expect, 359))
   # def test_360(self):
   #     line = '''Class R:_{foo(){New a(1).a();}}'''
   #     expect = '''Program([ClassDecl(Id(R),Id(_),[MethodDecl(Id(foo),Instance,[],Block([Call(NewExpr(Id(a),[IntLit(1)]),Id(a),[])]))])])'''
   #     self.assertTrue(TestAST.test(line, expect, 360))
   # def test_361(self):
   #     line = '''
   #             Class Shape2 {
   #         $getNumOfShape() {
   #             If (a == (1+1) ){
   #                 Var b,c:Boolean = True, False;
   #             }
   #             Foreach (i In 1 .. 100 By 2) {
   #                  Var a:Boolean = True;
   #             }
   #         }
   #     }
   #     '''
   #     expect = '''Program([ClassDecl(Id(Shape2),[MethodDecl(Id($getNumOfShape),Static,[],Block([If(BinaryOp(==,Id(a),BinaryOp(+,IntLit(1),IntLit(1))),Block([VarDecl(Id(b),BoolType,BooleanLit(True)),VarDecl(Id(c),BoolType,BooleanLit(False))])),For(Id(i),IntLit(1),IntLit(100),IntLit(2),Block([VarDecl(Id(a),BoolType,BooleanLit(True))])])]))])])'''
   #     self.assertTrue(TestAST.test(line, expect, 361))
   # def test_362(self):
   #     line = """
   #             Class Shape{
   #                 foo(){
   #                     Foreach (x In 1+1 .. 100+100 By a.foo(1+2*3,"abc"+.1+2)){}
   #                 }
   #             }
   #         """
   #     expect = '''Program([ClassDecl(Id(Shape),[MethodDecl(Id(foo),Instance,[],Block([For(Id(x),BinaryOp(+,IntLit(1),IntLit(1)),BinaryOp(+,IntLit(100),IntLit(100)),CallExpr(Id(a),Id(foo),[BinaryOp(+,IntLit(1),BinaryOp(*,IntLit(2),IntLit(3))),BinaryOp(+.,StringLit(abc),BinaryOp(+,IntLit(1),IntLit(2)))]),Block([])])]))])])'''
   #     self.assertTrue(TestAST.test(line, expect, 362))
   # def test_363(self):
   #     line = """
   #             Class Shape{
   #                 foo(){
   #                     Foreach (x In a::$b() .. a.c.c.c By a::$foo){
   #                         Foreach (x In a::$b() .. a.c.c.c By a::$foo){}
   #                     }
   #                 }
   #             }
   #             """
   #     expect = '''Program([ClassDecl(Id(Shape),[MethodDecl(Id(foo),Instance,[],Block([For(Id(x),CallExpr(Id(a),Id($b),[]),FieldAccess(FieldAccess(FieldAccess(Id(a),Id(c)),Id(c)),Id(c)),FieldAccess(Id(a),Id($foo)),Block([For(Id(x),CallExpr(Id(a),Id($b),[]),FieldAccess(FieldAccess(FieldAccess(Id(a),Id(c)),Id(c)),Id(c)),FieldAccess(Id(a),Id($foo)),Block([])])])])]))])])'''
   #     self.assertTrue(TestAST.test(line, expect, 363))
   # def test_364(self):
   #     line = """
   #             Class Shape{
   #                 foo(){
   #                     If ( a == -1--1){
   #                         Foreach(x In 1 .. 100 By 2){
   #                             If ( a == -1--1){
   #                                 Foreach(x In 1 .. 100 By 2){

   #                                 }
   #                             }
   #                         }
   #                     }
   #                 }
   #             }
   #             """

   #     expect = '''Program([ClassDecl(Id(Shape),[MethodDecl(Id(foo),Instance,[],Block([If(BinaryOp(==,Id(a),BinaryOp(-,UnaryOp(-,IntLit(1)),UnaryOp(-,IntLit(1)))),Block([For(Id(x),IntLit(1),IntLit(100),IntLit(2),Block([If(BinaryOp(==,Id(a),BinaryOp(-,UnaryOp(-,IntLit(1)),UnaryOp(-,IntLit(1)))),Block([For(Id(x),IntLit(1),IntLit(100),IntLit(2),Block([])])]))])])]))]))])])'''
   #     self.assertTrue(TestAST.test(line, expect, 364))
   # def test_365(self):
   #     line = """
   #     Class Program{
   #         main(){}
   #         main(a,b,c:Int){}
   #     }
   #     Class DelPhaiProgram{
   #         main(){}
   #     }
   #     """

   #     expect = '''Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([])),MethodDecl(Id(main),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType)],Block([]))]),ClassDecl(Id(DelPhaiProgram),[MethodDecl(Id(main),Instance,[],Block([]))])])'''
   #     self.assertTrue(TestAST.test(line, expect, 365))
   # def test_366(self):
   #     """Static access, instance and index combine"""
   #     input = """Class Program {
   #         Val b : Int = ClassABC::$a.a.c.b[1][2][3][(0 + 012 + 0xA2 + 0XA2 +0b101+0B101)];
   #         Var c : Int = 0x0 + 0X0 + 0b0 + 0B0 + 00 + 0;
   #     }"""
   #     expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(b),IntType,ArrayCell(FieldAccess(FieldAccess(FieldAccess(FieldAccess(Id(ClassABC),Id($a)),Id(a)),Id(c)),Id(b)),[IntLit(1),IntLit(2),IntLit(3),BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,IntLit(0),IntLit(10)),IntLit(162)),IntLit(162)),IntLit(5)),IntLit(5))]))),AttributeDecl(Instance,VarDecl(Id(c),IntType,BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,IntLit(0),IntLit(0)),IntLit(0)),IntLit(0)),IntLit(0)),IntLit(0))))])])"
   #     self.assertTrue(TestAST.test(input, expect, 366))
   # def test_367(self):
   #     """Static access, instance and index combine"""
   #     input = """Class Program {
   #         a() {
   #             Val c, d : Float = .e5 , 1e-1;
   #         }
   #     }"""
   #     expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([ConstDecl(Id(c),FloatType,FloatLit(0.0)),ConstDecl(Id(d),FloatType,FloatLit(0.1))]))])])"
   #     self.assertTrue(TestAST.test(input, expect, 367))
   # def test_368(self):
   #     input = """Class Program {
   #         main() {
   #             (a[1]).func();
   #             a[1] = 1;
   #             Out.println(a.a[1]);
   #             ((((a[1][2]).a[1]).func()[0]).a[1]).func();
   #             Return;
   #         }
   #     }"""
   #     expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(ArrayCell(Id(a),[IntLit(1)]),Id(func),[]),AssignStmt(ArrayCell(Id(a),[IntLit(1)]),IntLit(1)),Call(Id(Out),Id(println),[ArrayCell(FieldAccess(Id(a),Id(a)),[IntLit(1)])]),Call(ArrayCell(FieldAccess(ArrayCell(CallExpr(ArrayCell(FieldAccess(ArrayCell(Id(a),[IntLit(1),IntLit(2)]),Id(a)),[IntLit(1)]),Id(func),[]),[IntLit(0)]),Id(a)),[IntLit(1)]),Id(func),[]),Return()]))])])"
   #     self.assertTrue(TestAST.test(input, expect, 368))
   # def test_369(self):
   #     input = """Class Program {
   #         main() {
   #             (a[1]).func();
   #             a[1] = 1;
   #             Out.println(a.a[1]);
   #             ((((a[1][2]).a[1]).func()[0]).a[1]).func();
   #             Return;
   #         }
   #     }"""
   #     expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(ArrayCell(Id(a),[IntLit(1)]),Id(func),[]),AssignStmt(ArrayCell(Id(a),[IntLit(1)]),IntLit(1)),Call(Id(Out),Id(println),[ArrayCell(FieldAccess(Id(a),Id(a)),[IntLit(1)])]),Call(ArrayCell(FieldAccess(ArrayCell(CallExpr(ArrayCell(FieldAccess(ArrayCell(Id(a),[IntLit(1),IntLit(2)]),Id(a)),[IntLit(1)]),Id(func),[]),[IntLit(0)]),Id(a)),[IntLit(1)]),Id(func),[]),Return()]))])])"
   #     self.assertTrue(TestAST.test(input, expect, 368))
   # def test_370(self):
   #     input = """Class Program {
   #         a() {
   #             A.a.a.foo();
   #             (a.a[1][2][3]).foo();
   #             MotorBike::$ab.foo();
   #             (MotorBike::$a.a[1][2]).foo();
   #         }
   #     }"""
   #     expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([Call(FieldAccess(FieldAccess(Id(A),Id(a)),Id(a)),Id(foo),[]),Call(ArrayCell(FieldAccess(Id(a),Id(a)),[IntLit(1),IntLit(2),IntLit(3)]),Id(foo),[]),Call(FieldAccess(Id(MotorBike),Id($ab)),Id(foo),[]),Call(ArrayCell(FieldAccess(FieldAccess(Id(MotorBike),Id($a)),Id(a)),[IntLit(1),IntLit(2)]),Id(foo),[])]))])])"
   #     self.assertTrue(TestAST.test(input, expect, 570))

   # def test_371(self):
   #     input = """Class D{
   #         Var _9f1, $_: l_;
   #         foo(){
   #             Val a,b:I;
   #         }
   #     }"""
   #     expect = "Program([ClassDecl(Id(D),[AttributeDecl(Instance,VarDecl(Id(_9f1),ClassType(Id(l_)),NullLiteral())),AttributeDecl(Static,VarDecl(Id($_),ClassType(Id(l_)),NullLiteral())),MethodDecl(Id(foo),Instance,[],Block([ConstDecl(Id(a),ClassType(Id(I)),NullLiteral()),ConstDecl(Id(b),ClassType(Id(I)),NullLiteral())]))])])"
   #     self.assertTrue(TestAST.test(input, expect, 371))
   #  