import unittest
from TestUtils import TestAST
from AST import *

# class ASTGenSuite(unittest.TestCase):
#    def test_300(self):
#        """Simple program: int main() {} """
#        input = "Class Program {}"
#        expect = 'Program([ClassDecl(Id(Program),[])])'
#        self.assertTrue(TestAST.test(input,expect,300))
#    def test_301(self):
#        """Simple program: int main() {} """
#        input = "Class A:B {}"
#        expect = 'Program([ClassDecl(Id(A),Id(B),[])])'
#        self.assertTrue(TestAST.test(input,expect,301))
#    def test_302(self):
#        """Simple program: int main() {} """
#        input = "Class A {} Class B {} Class C {}"
#        expect = 'Program([ClassDecl(Id(A),[]),ClassDecl(Id(B),[]),ClassDecl(Id(C),[])])'
#        self.assertTrue(TestAST.test(input,expect,302))
#    def test_303(self):
#        """Simple program: int main() {} """
#        input = """
#        Class A {
#            Var a:Int;
#        }
#        """
#        expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Instance,VarDecl(Id(a),IntType))])])'
#        self.assertTrue(TestAST.test(input,expect,303))
#    def test_304(self):
#        """Simple program: int main() {} """
#        input = """
#        Class A {
#            Var a:Int;
#            Var b:Int;
#        }
#        """
#        expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Instance,VarDecl(Id(a),IntType)),AttributeDecl(Instance,VarDecl(Id(b),IntType))])])'
#        self.assertTrue(TestAST.test(input,expect,304))
#    def test_305(self):
#        """Simple program: int main() {} """
#        input = """
#        Class A {
#            Var a:Array[Int,5];
#        }
#        """
#        expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Instance,VarDecl(Id(a),ArrayType(5,IntType)))])])'
#        self.assertTrue(TestAST.test(input,expect,305))
#    def test_306(self):
#        """Simple program: int main() {} """
#        input = """
#        Class A {
#            Var a:Int=1;
#        }
#        """
#        expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Instance,VarDecl(Id(a),IntType,IntLit(1)))])])'
#        self.assertTrue(TestAST.test(input,expect,306))
#    def test_307(self):
#        """Simple program: int main() {} """
#        input = """
#        Class A {
#            Var a:Int=1+1;
#        }
#        """
#        expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Instance,VarDecl(Id(a),IntType,BinaryOp(+,IntLit(1),IntLit(1))))])])'
#        self.assertTrue(TestAST.test(input,expect,307))
#    def test_308(self):
#        """Simple program: int main() {} """
#        input = """
#        Class A {
#            Var a:Int=1+1*2;
#        }
#        """
#        expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Instance,VarDecl(Id(a),IntType,BinaryOp(+,IntLit(1),BinaryOp(*,IntLit(1),IntLit(2)))))])])'
#        self.assertTrue(TestAST.test(input,expect,308))
#    def test_309(self):
#        """Simple program: int main() {} """
#        input = """
#        Class A {
#            Var a:Int=\"abc\"+.1+2;
#        }
#        """
#        expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Instance,VarDecl(Id(a),IntType,BinaryOp(+.,StringLit(abc),BinaryOp(+,IntLit(1),IntLit(2)))))])])'
#        self.assertTrue(TestAST.test(input,expect,309))
#    def test_310(self):
#        """Simple program: int main() {} """
#        input = """
#        Class A {
#            Var a:Int=!!a---2*---3;
#        }
#        """
#        expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Instance,VarDecl(Id(a),IntType,BinaryOp(-,UnaryOp(!,UnaryOp(!,Id(a))),BinaryOp(*,UnaryOp(-,UnaryOp(-,IntLit(2))),UnaryOp(-,UnaryOp(-,UnaryOp(-,IntLit(3))))))))])])'
#        self.assertTrue(TestAST.test(input,expect,310))
#    def test_311(self):
#        """Simple program: int main() {} """
#        input = """
#        Class A {
#            Val a:Boolean=True;
#        }
#        """
#        expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Instance,ConstDecl(Id(a),BoolType,BooleanLit(True)))])])'
#        self.assertTrue(TestAST.test(input,expect,311))
#    def test_312(self):
#        """Simple program: int main() {} """
#        input = """
#        Class A {
#            Val a:String=b[1][1];
#        }
#        """
#        expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Instance,ConstDecl(Id(a),StringType,ArrayCell(Id(b),[IntLit(1),IntLit(1)])))])])'
#        self.assertTrue(TestAST.test(input,expect,312))
#    def test_313(self):
#        """Simple program: int main() {} """
#        input = """
#        Class A {
#            Var a:Int = New a();
#        }
#        """
#        expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Instance,VarDecl(Id(a),IntType,NewExpr(Id(a),[])))])])'
#        self.assertTrue(TestAST.test(input,expect,313))
#    def test_314(self):
#        """Simple program: int main() {} """
#        input = """
#        Class A {
#            Val b:Int = Null;
#        }
#        """
#        expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Instance,ConstDecl(Id(b),IntType,NullLiteral()))])])'
#        self.assertTrue(TestAST.test(input,expect,314))
#    def test_315(self):
#        """Simple program: int main() {} """
#        input = """
#        Class A {
#            Val b:Int = New a(1+2,Null);
#        }
#        """
#        expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Instance,ConstDecl(Id(b),IntType,NewExpr(Id(a),[BinaryOp(+,IntLit(1),IntLit(2)),NullLiteral()])))])])'
#        self.assertTrue(TestAST.test(input,expect,315))
#    def test_316(self):
#        """Simple program: int main() {} """
#        input = """
#        Class A {
#            Var $b:Float=6.9;
#        }
#        """
#        expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Static,VarDecl(Id($b),FloatType,FloatLit(6.9)))])])'
#        self.assertTrue(TestAST.test(input,expect,316))
#    def test_317(self):
#        input = """
#        Class A {
#            foo(){}
#        }
#        """
#        expect = 'Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[],Block([]))])])'
#        self.assertTrue(TestAST.test(input, expect, 317))
#    def test_318(self):
#        input = """
#        Class A {
#            foo(a,b:Int;c:Float){}
#        }
#        """
#        expect = 'Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),FloatType)],Block([]))])])'
#        self.assertTrue(TestAST.test(input, expect, 318))
#    def test_319(self):
#        input = """
#        Class A {
#            foo(a:Int;b:Boolean;c:String){}
#        }
#        """
#        expect = 'Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[param(Id(a),IntType),param(Id(b),BoolType),param(Id(c),StringType)],Block([]))])])'
#        self.assertTrue(TestAST.test(input, expect, 319))
#    def test_320(self):
#        input = """
#        Class A {
#            foo(){
#                Var a:Int;
#            }
#        }
#        """
#        expect = 'Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[],Block([VarDecl(Id(a),IntType)]))])])'
#        self.assertTrue(TestAST.test(input, expect, 320))
#    def test_321(self):
#        input = """
#        Class A {
#            foo(){
#                Var a:Int = 1;
#            }
#        }
#        """
#        expect = 'Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[],Block([VarDecl(Id(a),IntType,IntLit(1))]))])])'
#        self.assertTrue(TestAST.test(input, expect, 321))
#    def test_322(self):
#        input = """
#        Class A {
#            foo(){
#                Var a:Int = 1;
#                Var b:Float = 1.0;
#                Val c:Boolean = True;
#            }
#        }
#        """
#        expect = 'Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[],Block([VarDecl(Id(a),IntType,IntLit(1)),VarDecl(Id(b),FloatType,FloatLit(1.0)),ConstDecl(Id(c),BoolType,BooleanLit(True))]))])])'
#        self.assertTrue(TestAST.test(input, expect, 322))
#    def test_323(self):
#        input = """
#        Class A {
#            Var $b:Int = 1;
#            foo(){
#                Var a:Int = 1;
#            }
#        }
#        """
#        expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Static,VarDecl(Id($b),IntType,IntLit(1))),MethodDecl(Id(foo),Instance,[],Block([VarDecl(Id(a),IntType,IntLit(1))]))])])'
#        self.assertTrue(TestAST.test(input, expect, 323))
#    def test_324(self):
#        input = """
#        Class A {
#            foo(a,b,c,d,e:Int){
#                Var f:Int = 1+2*3;
#            }
#        }
#        """
#        expect = 'Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType),param(Id(d),IntType),param(Id(e),IntType)],Block([VarDecl(Id(f),IntType,BinaryOp(+,IntLit(1),BinaryOp(*,IntLit(2),IntLit(3))))]))])])'
#        self.assertTrue(TestAST.test(input, expect, 324))
#    def test_325(self):
#        input = """
#        Class A {
#            $foo(){
#                Var a:Int = 2/3;
#                a=1;
#            }
#        }
#        """
#        expect = 'Program([ClassDecl(Id(A),[MethodDecl(Id($foo),Static,[],Block([VarDecl(Id(a),IntType,BinaryOp(/,IntLit(2),IntLit(3))),AssignStmt(Id(a),IntLit(1))]))])])'
#        self.assertTrue(TestAST.test(input, expect, 325))
#    def test_326(self):
#        input = """
#        Class A {
#            $foo(){
#                a[1][3+4]=1;
#            }
#        }
#        """
#        expect = 'Program([ClassDecl(Id(A),[MethodDecl(Id($foo),Static,[],Block([AssignStmt(ArrayCell(Id(a),[IntLit(1),BinaryOp(+,IntLit(3),IntLit(4))]),IntLit(1))]))])])'
#        self.assertTrue(TestAST.test(input, expect, 326))
#    def test_327(self):
#        input = """
#        Class A {
#            foo(){
#                a[1][b[3]]="abc";
#            }
#        }
#        """
#        expect = 'Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[],Block([AssignStmt(ArrayCell(Id(a),[IntLit(1),ArrayCell(Id(b),[IntLit(3)])]),StringLit(abc))]))])])'
#        self.assertTrue(TestAST.test(input, expect, 327))
#    def test_328(self):
#        input = """
#        Class A {
#            foo(){
#                a.b.c="abc";
#            }
#        }
#        """
#        expect = 'Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[],Block([AssignStmt(FieldAccess(FieldAccess(Id(a),Id(b)),Id(c)),StringLit(abc))]))])])'
#        self.assertTrue(TestAST.test(input, expect, 328))
#    def test_329(self):
#        input = """
#        Class A {
#            foo(){
#                a.b.c[1]=d.e.f(1,2+3);
#            }
#        }
#        """
#        expect = 'Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[],Block([AssignStmt(ArrayCell(FieldAccess(FieldAccess(Id(a),Id(b)),Id(c)),[IntLit(1)]),CallExpr(FieldAccess(Id(d),Id(e)),Id(f),[IntLit(1),BinaryOp(+,IntLit(2),IntLit(3))]))]))])])'
#        self.assertTrue(TestAST.test(input, expect, 329))
#    def test_330(self):
#        input = """
#        Class A {
#            foo(){
#                Var a:A = d.e.f(1,2+3) + 2;
#            }
#        }
#        """
#        expect = 'Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[],Block([VarDecl(Id(a),ClassType(Id(A)),BinaryOp(+,CallExpr(FieldAccess(Id(d),Id(e)),Id(f),[IntLit(1),BinaryOp(+,IntLit(2),IntLit(3))]),IntLit(2)))]))])])'
#        self.assertTrue(TestAST.test(input, expect, 330))
#    def test_331(self):
#        input = """
#        Class A {
#            foo(){
#                Var a:Array[Array[Int,5],5];
#            }
#        }
#        """
#        expect = 'Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[],Block([VarDecl(Id(a),ArrayType(5,ArrayType(5,IntType)))]))])])'
#        self.assertTrue(TestAST.test(input, expect, 331))
#    def test_332(self):
#        input = """
#        Class A {
#            foo(){
#                Break;
#                Continue;
#                Return a==.!b;
#                {}
#            }
#        }
#        """
#        expect = 'Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[],Block([Break,Continue,Return(BinaryOp(==.,Id(a),UnaryOp(!,Id(b)))),Block([])]))])])'
#        self.assertTrue(TestAST.test(input, expect, 332))
#    def test_333(self):
#        input = """
#        Class A:B{
#            foo(){
#                a = New a(1+2*3/4).b.c();
#            }
#        }
#        """
#        expect = 'Program([ClassDecl(Id(A),Id(B),[MethodDecl(Id(foo),Instance,[],Block([AssignStmt(Id(a),CallExpr(FieldAccess(NewExpr(Id(a),[BinaryOp(+,IntLit(1),BinaryOp(/,BinaryOp(*,IntLit(2),IntLit(3)),IntLit(4)))]),Id(b)),Id(c),[]))]))])])'
#        self.assertTrue(TestAST.test(input, expect, 333))
#    def test_334(self):
#        input = """
#        Class A:B{
#            foo(){
#                a = New a(1+2*3/4).b.c();
#            }
#        }
#        """
#        expect = 'Program([ClassDecl(Id(A),Id(B),[MethodDecl(Id(foo),Instance,[],Block([AssignStmt(Id(a),CallExpr(FieldAccess(NewExpr(Id(a),[BinaryOp(+,IntLit(1),BinaryOp(/,BinaryOp(*,IntLit(2),IntLit(3)),IntLit(4)))]),Id(b)),Id(c),[]))]))])])'
#        self.assertTrue(TestAST.test(input, expect, 334))
#    def test_335(self):
#        input = """
#        Class A:B{
#            foo(){
#                a = (1+2)*3;
#            }
#        }
#        """
#        expect = 'Program([ClassDecl(Id(A),Id(B),[MethodDecl(Id(foo),Instance,[],Block([AssignStmt(Id(a),BinaryOp(*,BinaryOp(+,IntLit(1),IntLit(2)),IntLit(3)))]))])])'
#        self.assertTrue(TestAST.test(input, expect, 335))
#    def test_336(self):
#        input = """
#        Class A:B{
#            foo(){
#                Return Self.foo();
#            }
#            Constructor (a,b:J){}
#            Destructor (){}
#        }
#        """
#        expect = 'Program([ClassDecl(Id(A),Id(B),[MethodDecl(Id(foo),Instance,[],Block([Return(CallExpr(Self(),Id(foo),[]))])),MethodDecl(Id(Constructor),Instance,[param(Id(a),ClassType(Id(J))),param(Id(b),ClassType(Id(J)))],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))])])'
#        self.assertTrue(TestAST.test(input, expect, 336))
#    def test_337(self):
#        input = """
#        Class A:B{
#            Var a,$b:Int;
#        }
#        """
#        expect = 'Program([ClassDecl(Id(A),Id(B),[AttributeDecl(Instance,VarDecl(Id(a),IntType)),AttributeDecl(Static,VarDecl(Id($b),IntType))])])'
#        self.assertTrue(TestAST.test(input, expect, 337))
#    def test_338(self):
#        input = """
#        Class A:B{
#            Var a,$b:Int = 1,2;
#            Val $c,d:Boolean = True, Null;
#        }
#        """
#        expect = 'Program([ClassDecl(Id(A),Id(B),[AttributeDecl(Instance,VarDecl(Id(a),IntType,IntLit(1))),AttributeDecl(Static,VarDecl(Id($b),IntType,IntLit(2))),AttributeDecl(Static,ConstDecl(Id($c),BoolType,BooleanLit(True))),AttributeDecl(Instance,ConstDecl(Id(d),BoolType,NullLiteral()))])])'
#        self.assertTrue(TestAST.test(input, expect, 338))
#    def test_339(self):
#        input = """
#        Class A:B{
#            Var a, b, c:Int;
#            Foo(){
#                Var a, b, c:Int;
#            }
#        }
#        """
#        expect = 'Program([ClassDecl(Id(A),Id(B),[AttributeDecl(Instance,VarDecl(Id(a),IntType)),AttributeDecl(Instance,VarDecl(Id(b),IntType)),AttributeDecl(Instance,VarDecl(Id(c),IntType)),MethodDecl(Id(Foo),Instance,[],Block([VarDecl(Id(a),IntType),VarDecl(Id(b),IntType),VarDecl(Id(c),IntType)]))])])'
#        self.assertTrue(TestAST.test(input, expect, 339))
#    def test_340(self):
#        input = """
#        Class A:B{
#            Foo(){
#                Val a, b, c:Int = 1,2,3;
#                Var d:Boolean = True;
#            }
#        }
#        """
#        expect = 'Program([ClassDecl(Id(A),Id(B),[MethodDecl(Id(Foo),Instance,[],Block([ConstDecl(Id(a),IntType,IntLit(1)),ConstDecl(Id(b),IntType,IntLit(2)),ConstDecl(Id(c),IntType,IntLit(3)),VarDecl(Id(d),BoolType,BooleanLit(True))]))])])'
#        self.assertTrue(TestAST.test(input, expect, 340))
#    def test_341(self):
#        input = """
#        Class A:B{
#            Var $a:Array[Int,3] = Array(1,1,1);
#        }
#        """
#        expect = 'Program([ClassDecl(Id(A),Id(B),[AttributeDecl(Static,VarDecl(Id($a),ArrayType(3,IntType),[IntLit(1),IntLit(1),IntLit(1)]))])])'
#        self.assertTrue(TestAST.test(input, expect, 341))
#    def test_342(self):
#        input = """
#        Class A:B{
#            Var $a:Array[Array[Int,1],3] = Array(Array(1),Array(1),Array(1));
#        }
#        """
#        expect = 'Program([ClassDecl(Id(A),Id(B),[AttributeDecl(Static,VarDecl(Id($a),ArrayType(3,ArrayType(1,IntType)),[[IntLit(1)],[IntLit(1)],[IntLit(1)]]))])])'
#        self.assertTrue(TestAST.test(input, expect, 342))
#    def test_343(self):
#        input = """
#        Class A:B{
#            Var $0:Int;
#            $foo(i:Array [Boolean ,0105]){
#                a=0105;
#                b.c(Self,Null,Array(1)).d=0x12DEF;
#                d[e][f[g]]=0B1010111011101;
#            }
#        }
#        """
#        expect = 'Program([ClassDecl(Id(A),Id(B),[AttributeDecl(Static,VarDecl(Id($0),IntType)),MethodDecl(Id($foo),Static,[param(Id(i),ArrayType(69,BoolType))],Block([AssignStmt(Id(a),IntLit(69)),AssignStmt(FieldAccess(CallExpr(Id(b),Id(c),[Self(),NullLiteral(),[IntLit(1)]]),Id(d)),IntLit(77295)),AssignStmt(ArrayCell(Id(d),[Id(e),ArrayCell(Id(f),[Id(g)])]),IntLit(5597))]))])])'
#        self.assertTrue(TestAST.test(input, expect, 343))
#    def test_344(self):
#        input = """
#        Class A:B{
#            Var $0,a,$1,b,$2,c:Int = 5,4,3,2,1,0;
#        }
#        """
#        expect = 'Program([ClassDecl(Id(A),Id(B),[AttributeDecl(Static,VarDecl(Id($0),IntType,IntLit(5))),AttributeDecl(Instance,VarDecl(Id(a),IntType,IntLit(4))),AttributeDecl(Static,VarDecl(Id($1),IntType,IntLit(3))),AttributeDecl(Instance,VarDecl(Id(b),IntType,IntLit(2))),AttributeDecl(Static,VarDecl(Id($2),IntType,IntLit(1))),AttributeDecl(Instance,VarDecl(Id(c),IntType,IntLit(0)))])])'
#        self.assertTrue(TestAST.test(input, expect, 344))
#    def test_345(self):
#        input = """
#        Class A:B{
#            Foo(){
#                If(1){}
#            }
#        }
#        """
#        expect = 'Program([ClassDecl(Id(A),Id(B),[MethodDecl(Id(Foo),Instance,[],Block([If(IntLit(1),Block([]))]))])])'
#        self.assertTrue(TestAST.test(input, expect, 345))
#    def test_346(self):
#        input = """
#        Class A:B{
#            Foo(){
#                If(1){}
#                If(2){}Else{}
#                If(3){}Elseif(4){}Else{a=1;}
#            }
#        }
#        """
#        expect = 'Program([ClassDecl(Id(A),Id(B),[MethodDecl(Id(Foo),Instance,[],Block([If(IntLit(1),Block([])),If(IntLit(2),Block([]),Block([])),If(IntLit(3),Block([]),If(IntLit(4),Block([]),Block([AssignStmt(Id(a),IntLit(1))])))]))])])'
#        self.assertTrue(TestAST.test(input, expect, 346))
#    def test_347(self):
#        input = """
#        Class A:B{
#            Foo(){
#                If(3){}Elseif(4){}Elseif(5){}Else{a=1;}
#            }
#        }
#        """
#        expect = 'Program([ClassDecl(Id(A),Id(B),[MethodDecl(Id(Foo),Instance,[],Block([If(IntLit(3),Block([]),If(IntLit(4),Block([]),If(IntLit(5),Block([]),Block([AssignStmt(Id(a),IntLit(1))]))))]))])])'
#        self.assertTrue(TestAST.test(input, expect, 347))
#    def test_348(self):
#        input = """
#        Class A:B{
#            Foo(){
#                a.b(1+2,3*4-5.5);
#                If(1)
#                    {}
#                Elseif(2)
#                    {}
#                Elseif(3)
#                    {}
#            }
#        }
#        """
#        expect = 'Program([ClassDecl(Id(A),Id(B),[MethodDecl(Id(Foo),Instance,[],Block([Call(Id(a),Id(b),[BinaryOp(+,IntLit(1),IntLit(2)),BinaryOp(-,BinaryOp(*,IntLit(3),IntLit(4)),FloatLit(5.5))]),If(IntLit(1),Block([]),If(IntLit(2),Block([]),If(IntLit(3),Block([]))))]))])])'
#        self.assertTrue(TestAST.test(input, expect, 348))
#    def test_349(self):
#        input = """
#        Class A: B
#        {
#            Foo()
#            {
#                If(3)
#                    {Val a: Int = 0X1234;}
#                Elseif(4)
#                    {{}}
#                Elseif(5)
#                    {Return Self;}
#                Else
#                    {a = 1;}
#            }
#        }
#        """
#        expect = 'Program([ClassDecl(Id(A),Id(B),[MethodDecl(Id(Foo),Instance,[],Block([If(IntLit(3),Block([ConstDecl(Id(a),IntType,IntLit(4660))]),If(IntLit(4),Block([Block([])]),If(IntLit(5),Block([Return(Self())]),Block([AssignStmt(Id(a),IntLit(1))]))))]))])])'
#        self.assertTrue(TestAST.test(input, expect, 349))
#    def test_350(self):
#        line = '''Class D:__p{}Class c{}Class _73_{}Class I_:C{Destructor (){ {l::$0V4___();} }}'''
#        expect = '''Program([ClassDecl(Id(D),Id(__p),[]),ClassDecl(Id(c),[]),ClassDecl(Id(_73_),[]),ClassDecl(Id(I_),Id(C),[MethodDecl(Id(Destructor),Instance,[],Block([Block([Call(Id(l),Id($0V4___),[])])]))])])'''
#        self.assertTrue(TestAST.test(line, expect, 350))
#    def test_351(self):
#        line = '''Class Y7t_C2_oW:g__{Constructor (_,s,AN4_F,__,g,_s:v;_:VZV2_;k_,_k,_4,P:Float ){_::$aJ.HF_.UZ._();} }Class _:__{}'''
#        expect = '''Program([ClassDecl(Id(Y7t_C2_oW),Id(g__),[MethodDecl(Id(Constructor),Instance,[param(Id(_),ClassType(Id(v))),param(Id(s),ClassType(Id(v))),param(Id(AN4_F),ClassType(Id(v))),param(Id(__),ClassType(Id(v))),param(Id(g),ClassType(Id(v))),param(Id(_s),ClassType(Id(v))),param(Id(_),ClassType(Id(VZV2_))),param(Id(k_),FloatType),param(Id(_k),FloatType),param(Id(_4),FloatType),param(Id(P),FloatType)],Block([Call(FieldAccess(FieldAccess(FieldAccess(Id(_),Id($aJ)),Id(HF_)),Id(UZ)),Id(_),[])]))]),ClassDecl(Id(_),Id(__),[])])'''
#        self.assertTrue(TestAST.test(line, expect, 351))
#    def test_352(self):
#        line = '''Class G{$Z3(p,_:Array [Array [Array [Int ,0B1001100],061],0b1_0];M:Float ;K,v5_:Int ;p,_,t:_){_::$_()._0._EkG();}$0(j9,E_,_:j){}$_(_xy:Array [Boolean ,061]){} }Class _:_AE{}'''
#        expect = '''Program([ClassDecl(Id(G),[MethodDecl(Id($Z3),Static,[param(Id(p),ArrayType(2,ArrayType(49,ArrayType(76,IntType)))),param(Id(_),ArrayType(2,ArrayType(49,ArrayType(76,IntType)))),param(Id(M),FloatType),param(Id(K),IntType),param(Id(v5_),IntType),param(Id(p),ClassType(Id(_))),param(Id(_),ClassType(Id(_))),param(Id(t),ClassType(Id(_)))],Block([Call(FieldAccess(CallExpr(Id(_),Id($_),[]),Id(_0)),Id(_EkG),[])])),MethodDecl(Id($0),Static,[param(Id(j9),ClassType(Id(j))),param(Id(E_),ClassType(Id(j))),param(Id(_),ClassType(Id(j)))],Block([])),MethodDecl(Id($_),Static,[param(Id(_xy),ArrayType(49,BoolType))],Block([]))]),ClassDecl(Id(_),Id(_AE),[])])'''
#        self.assertTrue(TestAST.test(line, expect, 352))
#    def test_353_683_PN(self):
#        line = """Class D{Var _9f1,_:l_;}Class m_:r_{Val $_:Int =---"\\t";Var _17_:Int ;}"""
#        expect = '''Program([ClassDecl(Id(D),[AttributeDecl(Instance,VarDecl(Id(_9f1),ClassType(Id(l_)),NullLiteral())),AttributeDecl(Instance,VarDecl(Id(_),ClassType(Id(l_)),NullLiteral()))]),ClassDecl(Id(m_),Id(r_),[AttributeDecl(Static,ConstDecl(Id($_),IntType,UnaryOp(-,UnaryOp(-,UnaryOp(-,StringLit(\\t)))))),AttributeDecl(Instance,VarDecl(Id(_17_),IntType))])])'''
#        self.assertTrue(TestAST.test(line, expect, 353))
#    def test_354_905_PN(self):
#        line = '''Class _{}Class l__:_k_6t{}Class W{Val T4:String =!!J_::$__;}'''
#        expect = '''Program([ClassDecl(Id(_),[]),ClassDecl(Id(l__),Id(_k_6t),[]),ClassDecl(Id(W),[AttributeDecl(Instance,ConstDecl(Id(T4),StringType,UnaryOp(!,UnaryOp(!,FieldAccess(Id(J_),Id($__))))))])])'''
#        self.assertTrue(TestAST.test(line, expect, 354))
#    def test_355_745_PN(self):
#        line = '''Class _:x4_{Val _GO:k=!__.F()<=yYF9::$7._()._A_N._.L7K+!tW0::$iw_9();}'''
#        expect = '''Program([ClassDecl(Id(_),Id(x4_),[AttributeDecl(Instance,ConstDecl(Id(_GO),ClassType(Id(k)),BinaryOp(<=,UnaryOp(!,CallExpr(Id(__),Id(F),[])),BinaryOp(+,FieldAccess(FieldAccess(FieldAccess(CallExpr(FieldAccess(Id(yYF9),Id($7)),Id(_),[]),Id(_A_N)),Id(_)),Id(L7K)),UnaryOp(!,CallExpr(Id(tW0),Id($iw_9),[]))))))])])'''
#        self.assertTrue(TestAST.test(line, expect, 355))
#    def test_356_646_PN(self):
#        line = '''Class _V_7{Var _86:Int =!-New k___()._.j_Z._._s3();Destructor (){} }Class _{Var $_5_,z_:Array [Array [String ,2],80];}'''
#        expect = '''Program([ClassDecl(Id(_V_7),[AttributeDecl(Instance,VarDecl(Id(_86),IntType,UnaryOp(!,UnaryOp(-,CallExpr(FieldAccess(FieldAccess(FieldAccess(NewExpr(Id(k___),[]),Id(_)),Id(j_Z)),Id(_)),Id(_s3),[]))))),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(_),[AttributeDecl(Static,VarDecl(Id($_5_),ArrayType(80,ArrayType(2,StringType)))),AttributeDecl(Instance,VarDecl(Id(z_),ArrayType(80,ArrayType(2,StringType))))])])'''
#        self.assertTrue(TestAST.test(line, expect, 356))
#    def test_357_597_PN(self):
#        line = '''Class _j{Constructor (_,_4m_q_R6r:_){}Var $o:String ;Val $3O:H=_::$_;}'''
#        expect = '''Program([ClassDecl(Id(_j),[MethodDecl(Id(Constructor),Instance,[param(Id(_),ClassType(Id(_))),param(Id(_4m_q_R6r),ClassType(Id(_)))],Block([])),AttributeDecl(Static,VarDecl(Id($o),StringType)),AttributeDecl(Static,ConstDecl(Id($3O),ClassType(Id(H)),FieldAccess(Id(_),Id($_))))])])'''
#        self.assertTrue(TestAST.test(line, expect, 357))
#    def test_358_313_PN(self):
#        line = '''Class _:qc0R{}Class E{Var _:E=-New _().kD9.p.F.d().k.h6e71_;}'''
#        expect = '''Program([ClassDecl(Id(_),Id(qc0R),[]),ClassDecl(Id(E),[AttributeDecl(Instance,VarDecl(Id(_),ClassType(Id(E)),UnaryOp(-,FieldAccess(FieldAccess(CallExpr(FieldAccess(FieldAccess(FieldAccess(NewExpr(Id(_),[]),Id(kD9)),Id(p)),Id(F)),Id(d),[]),Id(k)),Id(h6e71_)))))])])'''
#        self.assertTrue(TestAST.test(line, expect, 358))
#    def test_359_233_PN(self):
#        line = '''Class R:_{}Class _8_:_B{}Class _:_4{Var $b:Array [String ,0B1]=!-Self ;}'''
#        expect = '''Program([ClassDecl(Id(R),Id(_),[]),ClassDecl(Id(_8_),Id(_B),[]),ClassDecl(Id(_),Id(_4),[AttributeDecl(Static,VarDecl(Id($b),ArrayType(1,StringType),UnaryOp(!,UnaryOp(-,Self()))))])])'''
#        self.assertTrue(TestAST.test(line, expect, 359))
#    def test_360(self):
#        line = '''Class R:_{foo(){New a(1).a();}}'''
#        expect = '''Program([ClassDecl(Id(R),Id(_),[MethodDecl(Id(foo),Instance,[],Block([Call(NewExpr(Id(a),[IntLit(1)]),Id(a),[])]))])])'''
#        self.assertTrue(TestAST.test(line, expect, 360))
#    def test_361(self):
#        line = '''
#                Class Shape2 {
#            $getNumOfShape() {
#                If (a == (1+1) ){
#                    Var b,c:Boolean = True, False;
#                }
#                Foreach (i In 1 .. 100 By 2) {
#                     Var a:Boolean = True;
#                }
#            }
#        }
#        '''
#        expect = '''Program([ClassDecl(Id(Shape2),[MethodDecl(Id($getNumOfShape),Static,[],Block([If(BinaryOp(==,Id(a),BinaryOp(+,IntLit(1),IntLit(1))),Block([VarDecl(Id(b),BoolType,BooleanLit(True)),VarDecl(Id(c),BoolType,BooleanLit(False))])),For(Id(i),IntLit(1),IntLit(100),IntLit(2),Block([VarDecl(Id(a),BoolType,BooleanLit(True))])])]))])])'''
#        self.assertTrue(TestAST.test(line, expect, 361))
#    def test_362(self):
#        line = """
#                Class Shape{
#                    foo(){
#                        Foreach (x In 1+1 .. 100+100 By a.foo(1+2*3,"abc"+.1+2)){}
#                    }
#                }
#            """
#        expect = '''Program([ClassDecl(Id(Shape),[MethodDecl(Id(foo),Instance,[],Block([For(Id(x),BinaryOp(+,IntLit(1),IntLit(1)),BinaryOp(+,IntLit(100),IntLit(100)),CallExpr(Id(a),Id(foo),[BinaryOp(+,IntLit(1),BinaryOp(*,IntLit(2),IntLit(3))),BinaryOp(+.,StringLit(abc),BinaryOp(+,IntLit(1),IntLit(2)))]),Block([])])]))])])'''
#        self.assertTrue(TestAST.test(line, expect, 362))
#    def test_363(self):
#        line = """
#                Class Shape{
#                    foo(){
#                        Foreach (x In a::$b() .. a.c.c.c By a::$foo){
#                            Foreach (x In a::$b() .. a.c.c.c By a::$foo){}
#                        }
#                    }
#                }
#                """
#        expect = '''Program([ClassDecl(Id(Shape),[MethodDecl(Id(foo),Instance,[],Block([For(Id(x),CallExpr(Id(a),Id($b),[]),FieldAccess(FieldAccess(FieldAccess(Id(a),Id(c)),Id(c)),Id(c)),FieldAccess(Id(a),Id($foo)),Block([For(Id(x),CallExpr(Id(a),Id($b),[]),FieldAccess(FieldAccess(FieldAccess(Id(a),Id(c)),Id(c)),Id(c)),FieldAccess(Id(a),Id($foo)),Block([])])])])]))])])'''
#        self.assertTrue(TestAST.test(line, expect, 363))
#    def test_364(self):
#        line = """
#                Class Shape{
#                    foo(){
#                        If ( a == -1--1){
#                            Foreach(x In 1 .. 100 By 2){
#                                If ( a == -1--1){
#                                    Foreach(x In 1 .. 100 By 2){

#                                    }
#                                }
#                            }
#                        }
#                    }
#                }
#                """

#        expect = '''Program([ClassDecl(Id(Shape),[MethodDecl(Id(foo),Instance,[],Block([If(BinaryOp(==,Id(a),BinaryOp(-,UnaryOp(-,IntLit(1)),UnaryOp(-,IntLit(1)))),Block([For(Id(x),IntLit(1),IntLit(100),IntLit(2),Block([If(BinaryOp(==,Id(a),BinaryOp(-,UnaryOp(-,IntLit(1)),UnaryOp(-,IntLit(1)))),Block([For(Id(x),IntLit(1),IntLit(100),IntLit(2),Block([])])]))])])]))]))])])'''
#        self.assertTrue(TestAST.test(line, expect, 364))
#    def test_365(self):
#        line = """
#        Class Program{
#            main(){}
#            main(a,b,c:Int){}
#        }
#        Class DelPhaiProgram{
#            main(){}
#        }
#        """

#        expect = '''Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([])),MethodDecl(Id(main),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType)],Block([]))]),ClassDecl(Id(DelPhaiProgram),[MethodDecl(Id(main),Instance,[],Block([]))])])'''
#        self.assertTrue(TestAST.test(line, expect, 365))
#    def test_366(self):
#        """Static access, instance and index combine"""
#        input = """Class Program {
#            Val b : Int = ClassABC::$a.a.c.b[1][2][3][(0 + 012 + 0xA2 + 0XA2 +0b101+0B101)];
#            Var c : Int = 0x0 + 0X0 + 0b0 + 0B0 + 00 + 0;
#        }"""
#        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(b),IntType,ArrayCell(FieldAccess(FieldAccess(FieldAccess(FieldAccess(Id(ClassABC),Id($a)),Id(a)),Id(c)),Id(b)),[IntLit(1),IntLit(2),IntLit(3),BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,IntLit(0),IntLit(10)),IntLit(162)),IntLit(162)),IntLit(5)),IntLit(5))]))),AttributeDecl(Instance,VarDecl(Id(c),IntType,BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,IntLit(0),IntLit(0)),IntLit(0)),IntLit(0)),IntLit(0)),IntLit(0))))])])"
#        self.assertTrue(TestAST.test(input, expect, 366))
#    def test_367(self):
#        """Static access, instance and index combine"""
#        input = """Class Program {
#            a() {
#                Val c, d : Float = .e5 , 1e-1;
#            }
#        }"""
#        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([ConstDecl(Id(c),FloatType,FloatLit(0.0)),ConstDecl(Id(d),FloatType,FloatLit(0.1))]))])])"
#        self.assertTrue(TestAST.test(input, expect, 367))
#    def test_368(self):
#        input = """Class Program {
#            main() {
#                (a[1]).func();
#                a[1] = 1;
#                Out.println(a.a[1]);
#                ((((a[1][2]).a[1]).func()[0]).a[1]).func();
#                Return;
#            }
#        }"""
#        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(ArrayCell(Id(a),[IntLit(1)]),Id(func),[]),AssignStmt(ArrayCell(Id(a),[IntLit(1)]),IntLit(1)),Call(Id(Out),Id(println),[ArrayCell(FieldAccess(Id(a),Id(a)),[IntLit(1)])]),Call(ArrayCell(FieldAccess(ArrayCell(CallExpr(ArrayCell(FieldAccess(ArrayCell(Id(a),[IntLit(1),IntLit(2)]),Id(a)),[IntLit(1)]),Id(func),[]),[IntLit(0)]),Id(a)),[IntLit(1)]),Id(func),[]),Return()]))])])"
#        self.assertTrue(TestAST.test(input, expect, 368))
#    def test_369(self):
#        input = """Class Program {
#            main() {
#                (a[1]).func();
#                a[1] = 1;
#                Out.println(a.a[1]);
#                ((((a[1][2]).a[1]).func()[0]).a[1]).func();
#                Return;
#            }
#        }"""
#        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(ArrayCell(Id(a),[IntLit(1)]),Id(func),[]),AssignStmt(ArrayCell(Id(a),[IntLit(1)]),IntLit(1)),Call(Id(Out),Id(println),[ArrayCell(FieldAccess(Id(a),Id(a)),[IntLit(1)])]),Call(ArrayCell(FieldAccess(ArrayCell(CallExpr(ArrayCell(FieldAccess(ArrayCell(Id(a),[IntLit(1),IntLit(2)]),Id(a)),[IntLit(1)]),Id(func),[]),[IntLit(0)]),Id(a)),[IntLit(1)]),Id(func),[]),Return()]))])])"
#        self.assertTrue(TestAST.test(input, expect, 369))
#    def test_370(self):
#        input = """Class Program {
#            a() {
#                A.a.a.foo();
#                (a.a[1][2][3]).foo();
#                MotorBike::$ab.foo();
#                (MotorBike::$a.a[1][2]).foo();
#            }
#        }"""
#        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([Call(FieldAccess(FieldAccess(Id(A),Id(a)),Id(a)),Id(foo),[]),Call(ArrayCell(FieldAccess(Id(a),Id(a)),[IntLit(1),IntLit(2),IntLit(3)]),Id(foo),[]),Call(FieldAccess(Id(MotorBike),Id($ab)),Id(foo),[]),Call(ArrayCell(FieldAccess(FieldAccess(Id(MotorBike),Id($a)),Id(a)),[IntLit(1),IntLit(2)]),Id(foo),[])]))])])"
#        self.assertTrue(TestAST.test(input, expect, 570))

#    def test_371(self):
#        input = """Class D{
#            Var _9f1, $_: l_;
#            foo(){
#                Val a,b:I;
#            }
#        }"""
#        expect = "Program([ClassDecl(Id(D),[AttributeDecl(Instance,VarDecl(Id(_9f1),ClassType(Id(l_)),NullLiteral())),AttributeDecl(Static,VarDecl(Id($_),ClassType(Id(l_)),NullLiteral())),MethodDecl(Id(foo),Instance,[],Block([ConstDecl(Id(a),ClassType(Id(I)),NullLiteral()),ConstDecl(Id(b),ClassType(Id(I)),NullLiteral())]))])])"
#        self.assertTrue(TestAST.test(input, expect, 371))
    
#    def test_372(self):
#        input = """
#   Class NodeClass {
#      Var data : Int;
#      Val next : NodeClass;

#      Constructor(d : Int)
#      {
#         data = d;
#         next = Null;
#      }

#        ## Function to reverse the linked list ##
#        reverse(nodePoint : NodeClass)
#        {
#            Var prev : NodeClass = Null;
#            Val current : NodeClass = nodePoint;
#            Val next : NodeClass = Null;
#            Foreach (i In 1 .. forever By 1) {
#                If (current == Null) {
#                    Break;
#                } Else {
#                    next = current.next;
#                    current.next = prev;
#                    prev = current;
#                    current = next;
#                }
#            }
#            nodePoint = prev;
#            Return nodePoint;
#        }

#        printList(nodePoint : NodeClass)
#        {
#            Foreach (a In 1 .. infinity By 1) {
#                If (nodePoint != Null) {
#                    System.out.print(nodePoint.data +. " ");
#                    nodePoint = nodePoint.next;
#                } Else {
#                    Break;
#                }
#            }
#        }
#    }

#    Class Program {
#        mainA()
#        {
#            Val list : LinkedList = New LinkedList();
#            list.head = New NodeClass(85);
#            list.head.next = New NodeClass(15);
#            list.head.next.next = New NodeClass(4);
#            list.head.next.next.next = New NodeClass(20);

#            System.out.println("Given Linked list");
#            list.printList(head);
#            head = list.reverse(head);
#            System.out.println("");
#            System.out.println("Reversed linked list ");
#            list.printList(head);
#        }
#    }
#        """
#        expect = """Program([ClassDecl(Id(NodeClass),[AttributeDecl(Instance,VarDecl(Id(data),IntType)),AttributeDecl(Instance,ConstDecl(Id(next),ClassType(Id(NodeClass)),NullLiteral())),MethodDecl(Id(Constructor),Instance,[param(Id(d),IntType)],Block([AssignStmt(Id(data),Id(d)),AssignStmt(Id(next),NullLiteral())])),MethodDecl(Id(reverse),Instance,[param(Id(nodePoint),ClassType(Id(NodeClass)))],Block([VarDecl(Id(prev),ClassType(Id(NodeClass)),NullLiteral()),ConstDecl(Id(current),ClassType(Id(NodeClass)),Id(nodePoint)),ConstDecl(Id(next),ClassType(Id(NodeClass)),NullLiteral()),For(Id(i),IntLit(1),Id(forever),IntLit(1),Block([If(BinaryOp(==,Id(current),NullLiteral()),Block([Break]),Block([AssignStmt(Id(next),FieldAccess(Id(current),Id(next))),AssignStmt(FieldAccess(Id(current),Id(next)),Id(prev)),AssignStmt(Id(prev),Id(current)),AssignStmt(Id(current),Id(next))]))])]),AssignStmt(Id(nodePoint),Id(prev)),Return(Id(nodePoint))])),MethodDecl(Id(printList),Instance,[param(Id(nodePoint),ClassType(Id(NodeClass)))],Block([For(Id(a),IntLit(1),Id(infinity),IntLit(1),Block([If(BinaryOp(!=,Id(nodePoint),NullLiteral()),Block([Call(FieldAccess(Id(System),Id(out)),Id(print),[BinaryOp(+.,FieldAccess(Id(nodePoint),Id(data)),StringLit( ))]),AssignStmt(Id(nodePoint),FieldAccess(Id(nodePoint),Id(next)))]),Block([Break]))])])]))]),ClassDecl(Id(Program),[MethodDecl(Id(mainA),Instance,[],Block([ConstDecl(Id(list),ClassType(Id(LinkedList)),NewExpr(Id(LinkedList),[])),AssignStmt(FieldAccess(Id(list),Id(head)),NewExpr(Id(NodeClass),[IntLit(85)])),AssignStmt(FieldAccess(FieldAccess(Id(list),Id(head)),Id(next)),NewExpr(Id(NodeClass),[IntLit(15)])),AssignStmt(FieldAccess(FieldAccess(FieldAccess(Id(list),Id(head)),Id(next)),Id(next)),NewExpr(Id(NodeClass),[IntLit(4)])),AssignStmt(FieldAccess(FieldAccess(FieldAccess(FieldAccess(Id(list),Id(head)),Id(next)),Id(next)),Id(next)),NewExpr(Id(NodeClass),[IntLit(20)])),Call(FieldAccess(Id(System),Id(out)),Id(println),[StringLit(Given Linked list)]),Call(Id(list),Id(printList),[Id(head)]),AssignStmt(Id(head),CallExpr(Id(list),Id(reverse),[Id(head)])),Call(FieldAccess(Id(System),Id(out)),Id(println),[StringLit()]),Call(FieldAccess(Id(System),Id(out)),Id(println),[StringLit(Reversed linked list )]),Call(Id(list),Id(printList),[Id(head)])]))])])"""
#        self.assertTrue(TestAST.test(input, expect, 372))
#    def test_373(self):
#        input = """
#        Class Cak {
#            abcdeFu123(str: Array[String, 10]) {
#                Val parameters: Map = SomeClass::$parseParameters(args);

#                Val builder : ChainedOptionsBuilder = New OptionsBuilder()
#                .include(BigMatrixMultiplicationBenchmarking.class.getSimpleName())
#                .mode(Mode.AverageTime)
#                .forks(2)
#                .warmupIterations(10)
#                .measurementIterations(10)
#                .timeUnit(TimeUnit.SECONDS);

#                Return New Runner(builder.build()).run();
#            }
#    homemadeMatrixMultiplication(matrixProvider : BigMatrixProvider) {
#        Return HomemadeMatrix
#          .multiplyMatrices(matrixProvider.getFirstMatrix(), matrixProvider.getSecondMatrix());
#    }

#    nd4jMatrixMultiplication(matrixProvider : BigMatrixProvider) {
#        Val firstMatrix : INDArray = Nd4j.create(matrixProvider.getFirstMatrix());
#        Val secondMatrix : INDArray = Nd4j.create(matrixProvider.getSecondMatrix());

#        Return firstMatrix.mmul(secondMatrix);
#    }

#    coltMatrixMultiplication(matrixProvider : BigMatrixProvider) {
#        Val doubleFactory2D : DoubleFactory2D = DoubleFactory2D.dense;

#        Val firstMatrix : DoubleMatrix2D= doubleFactory2D.make(matrixProvider.getFirstMatrix());
#        Val secondMatrix : DoubleMatrix2D = doubleFactory2D.make(matrixProvider.getSecondMatrix());

#        Var algebra : Algebra = New Algebra();
#        Return algebra.mult(firstMatrix, secondMatrix);
#    }

#    ejmlMatrixMultiplication(matrixProvider : BigMatrixProvider) {
#        Var firstMatrix : SimpleMatrix = New SimpleMatrix(matrixProvider.getFirstMatrix());
#        Var secondMatrix : SimpleMatrix = New SimpleMatrix(matrixProvider.getSecondMatrix());

#        Return firstMatrix.mult(secondMatrix);
#    }

#    apacheCommonsMatrixMultiplication(matrixProvider : BigMatrixProvider) {
#        Var firstMatrix : RealMatrix = New Array2DRowRealMatrix(matrixProvider.getFirstMatrix());
#        Val secondMatrix : RealMatrix = New Array2DRowRealMatrix(matrixProvider.getSecondMatrix());

#        Return firstMatrix.multiply(secondMatrix);
#    }

#    la4jMatrixMultiplication(matrixProvider : BigMatrixProvider) {
#        Val firstMatrix : TheMatrix = New Basic2DMatrix(matrixProvider.getFirstMatrix());
#        Val secondMatrix : TheMatrix = New Basic2DMatrix(matrixProvider.getSecondMatrix());

#        Return firstMatrix.multiply(secondMatrix);
#    }
#        }
#        Class Program {
#            main() {
#                Val const1, const2: Int = 1 + 5, 2;
#                Var x, y : Int = 0, 0;
#                Val sth : Sth = New Sth();
#                Var a : Int = a.b.c.d();
#                Return;
#            }
#        }"""
#        expect = "Program([ClassDecl(Id(Cak),[MethodDecl(Id(abcdeFu123),Instance,[param(Id(str),ArrayType(10,StringType))],Block([ConstDecl(Id(parameters),ClassType(Id(Map)),CallExpr(Id(SomeClass),Id($parseParameters),[Id(args)])),ConstDecl(Id(builder),ClassType(Id(ChainedOptionsBuilder)),CallExpr(CallExpr(CallExpr(CallExpr(CallExpr(CallExpr(NewExpr(Id(OptionsBuilder),[]),Id(include),[CallExpr(FieldAccess(Id(BigMatrixMultiplicationBenchmarking),Id(class)),Id(getSimpleName),[])]),Id(mode),[FieldAccess(Id(Mode),Id(AverageTime))]),Id(forks),[IntLit(2)]),Id(warmupIterations),[IntLit(10)]),Id(measurementIterations),[IntLit(10)]),Id(timeUnit),[FieldAccess(Id(TimeUnit),Id(SECONDS))])),Return(CallExpr(NewExpr(Id(Runner),[CallExpr(Id(builder),Id(build),[])]),Id(run),[]))])),MethodDecl(Id(homemadeMatrixMultiplication),Instance,[param(Id(matrixProvider),ClassType(Id(BigMatrixProvider)))],Block([Return(CallExpr(Id(HomemadeMatrix),Id(multiplyMatrices),[CallExpr(Id(matrixProvider),Id(getFirstMatrix),[]),CallExpr(Id(matrixProvider),Id(getSecondMatrix),[])]))])),MethodDecl(Id(nd4jMatrixMultiplication),Instance,[param(Id(matrixProvider),ClassType(Id(BigMatrixProvider)))],Block([ConstDecl(Id(firstMatrix),ClassType(Id(INDArray)),CallExpr(Id(Nd4j),Id(create),[CallExpr(Id(matrixProvider),Id(getFirstMatrix),[])])),ConstDecl(Id(secondMatrix),ClassType(Id(INDArray)),CallExpr(Id(Nd4j),Id(create),[CallExpr(Id(matrixProvider),Id(getSecondMatrix),[])])),Return(CallExpr(Id(firstMatrix),Id(mmul),[Id(secondMatrix)]))])),MethodDecl(Id(coltMatrixMultiplication),Instance,[param(Id(matrixProvider),ClassType(Id(BigMatrixProvider)))],Block([ConstDecl(Id(doubleFactory2D),ClassType(Id(DoubleFactory2D)),FieldAccess(Id(DoubleFactory2D),Id(dense))),ConstDecl(Id(firstMatrix),ClassType(Id(DoubleMatrix2D)),CallExpr(Id(doubleFactory2D),Id(make),[CallExpr(Id(matrixProvider),Id(getFirstMatrix),[])])),ConstDecl(Id(secondMatrix),ClassType(Id(DoubleMatrix2D)),CallExpr(Id(doubleFactory2D),Id(make),[CallExpr(Id(matrixProvider),Id(getSecondMatrix),[])])),VarDecl(Id(algebra),ClassType(Id(Algebra)),NewExpr(Id(Algebra),[])),Return(CallExpr(Id(algebra),Id(mult),[Id(firstMatrix),Id(secondMatrix)]))])),MethodDecl(Id(ejmlMatrixMultiplication),Instance,[param(Id(matrixProvider),ClassType(Id(BigMatrixProvider)))],Block([VarDecl(Id(firstMatrix),ClassType(Id(SimpleMatrix)),NewExpr(Id(SimpleMatrix),[CallExpr(Id(matrixProvider),Id(getFirstMatrix),[])])),VarDecl(Id(secondMatrix),ClassType(Id(SimpleMatrix)),NewExpr(Id(SimpleMatrix),[CallExpr(Id(matrixProvider),Id(getSecondMatrix),[])])),Return(CallExpr(Id(firstMatrix),Id(mult),[Id(secondMatrix)]))])),MethodDecl(Id(apacheCommonsMatrixMultiplication),Instance,[param(Id(matrixProvider),ClassType(Id(BigMatrixProvider)))],Block([VarDecl(Id(firstMatrix),ClassType(Id(RealMatrix)),NewExpr(Id(Array2DRowRealMatrix),[CallExpr(Id(matrixProvider),Id(getFirstMatrix),[])])),ConstDecl(Id(secondMatrix),ClassType(Id(RealMatrix)),NewExpr(Id(Array2DRowRealMatrix),[CallExpr(Id(matrixProvider),Id(getSecondMatrix),[])])),Return(CallExpr(Id(firstMatrix),Id(multiply),[Id(secondMatrix)]))])),MethodDecl(Id(la4jMatrixMultiplication),Instance,[param(Id(matrixProvider),ClassType(Id(BigMatrixProvider)))],Block([ConstDecl(Id(firstMatrix),ClassType(Id(TheMatrix)),NewExpr(Id(Basic2DMatrix),[CallExpr(Id(matrixProvider),Id(getFirstMatrix),[])])),ConstDecl(Id(secondMatrix),ClassType(Id(TheMatrix)),NewExpr(Id(Basic2DMatrix),[CallExpr(Id(matrixProvider),Id(getSecondMatrix),[])])),Return(CallExpr(Id(firstMatrix),Id(multiply),[Id(secondMatrix)]))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([ConstDecl(Id(const1),IntType,BinaryOp(+,IntLit(1),IntLit(5))),ConstDecl(Id(const2),IntType,IntLit(2)),VarDecl(Id(x),IntType,IntLit(0)),VarDecl(Id(y),IntType,IntLit(0)),ConstDecl(Id(sth),ClassType(Id(Sth)),NewExpr(Id(Sth),[])),VarDecl(Id(a),IntType,CallExpr(FieldAccess(FieldAccess(Id(a),Id(b)),Id(c)),Id(d),[])),Return()]))])])"
#        self.assertTrue(TestAST.test(input, expect, 373))
#    def test_374(self):
#        input = """
#        Class Map {
#            Val bean: Array[String, 10];
#            Val value: Array[String, 10];
#            Constructor(bean: Array[String, 10]; value: Array[String, 10]) {
#                Self.bean = bean;
#                Self.value = value;
#                Return;
#            }
#            Destructor() {
#                Self.clean(Self.bean);
#                Self.clean(Self.value);
#                Return;
#            }
#            clean() {
#                Out.println("Cleaning");
#                Foreach (k In 0 .. Self.bean.length() By 1)
#                {
#                    el = Self.bean[k];

#                    Self.free(el);
#                    Self.bean = Null;
#                }
#                Self.free(bean);
#                Self.bean = Null;
#                Foreach (v In 0 .. Self.value.length() By 1)
#                {
#                    el = Self.value.a[v];

#                    Self.free(el);
#                    Self.value = Null;
#                }
#                Self.free(value);
#                Self.value = Null;
#                Val a : Boolean = True;
#                Val b : Int = 1;
#                Return (True || False) && (a == b);
#            }
#        }
#        Class Program {
#            mainA() {
#                Val const1, const2: Int = 1 + 5, 2;
#                Var x, y : Int = 0, 0;
#                Val sth : Sth = New Sth();
#                Return;
#            }
#        }
#        """
#        expect = "Program([ClassDecl(Id(Map),[AttributeDecl(Instance,ConstDecl(Id(bean),ArrayType(10,StringType),None)),AttributeDecl(Instance,ConstDecl(Id(value),ArrayType(10,StringType),None)),MethodDecl(Id(Constructor),Instance,[param(Id(bean),ArrayType(10,StringType)),param(Id(value),ArrayType(10,StringType))],Block([AssignStmt(FieldAccess(Self(),Id(bean)),Id(bean)),AssignStmt(FieldAccess(Self(),Id(value)),Id(value)),Return()])),MethodDecl(Id(Destructor),Instance,[],Block([Call(Self(),Id(clean),[FieldAccess(Self(),Id(bean))]),Call(Self(),Id(clean),[FieldAccess(Self(),Id(value))]),Return()])),MethodDecl(Id(clean),Instance,[],Block([Call(Id(Out),Id(println),[StringLit(Cleaning)]),For(Id(k),IntLit(0),CallExpr(FieldAccess(Self(),Id(bean)),Id(length),[]),IntLit(1),Block([AssignStmt(Id(el),ArrayCell(FieldAccess(Self(),Id(bean)),[Id(k)])),Call(Self(),Id(free),[Id(el)]),AssignStmt(FieldAccess(Self(),Id(bean)),NullLiteral())])]),Call(Self(),Id(free),[Id(bean)]),AssignStmt(FieldAccess(Self(),Id(bean)),NullLiteral()),For(Id(v),IntLit(0),CallExpr(FieldAccess(Self(),Id(value)),Id(length),[]),IntLit(1),Block([AssignStmt(Id(el),ArrayCell(FieldAccess(FieldAccess(Self(),Id(value)),Id(a)),[Id(v)])),Call(Self(),Id(free),[Id(el)]),AssignStmt(FieldAccess(Self(),Id(value)),NullLiteral())])]),Call(Self(),Id(free),[Id(value)]),AssignStmt(FieldAccess(Self(),Id(value)),NullLiteral()),ConstDecl(Id(a),BoolType,BooleanLit(True)),ConstDecl(Id(b),IntType,IntLit(1)),Return(BinaryOp(&&,BinaryOp(||,BooleanLit(True),BooleanLit(False)),BinaryOp(==,Id(a),Id(b))))]))]),ClassDecl(Id(Program),[MethodDecl(Id(mainA),Instance,[],Block([ConstDecl(Id(const1),IntType,BinaryOp(+,IntLit(1),IntLit(5))),ConstDecl(Id(const2),IntType,IntLit(2)),VarDecl(Id(x),IntType,IntLit(0)),VarDecl(Id(y),IntType,IntLit(0)),ConstDecl(Id(sth),ClassType(Id(Sth)),NewExpr(Id(Sth),[])),Return()]))])])"
#        self.assertTrue(TestAST.test(input, expect, 374))
class ASTGenSuite(unittest.TestCase):
    def test_0(self):
        line = '''Class _:k{Constructor (O,Cy_:G){Continue ;}Var _,J,J_8:____;}Class g:TZ{Destructor (){}Destructor (){ {}Var _,qY,_:Boolean ;}$T(xi,_10,_:Array [String ,60];_a,C:_c_9;n:M;O:f;_2,_:Array [Boolean ,60]){}Destructor (){} }Class G{}'''
        expect = '''Program([ClassDecl(Id(_),Id(k),[MethodDecl(Id(Constructor),Instance,[param(Id(O),ClassType(Id(G))),param(Id(Cy_),ClassType(Id(G)))],Block([Continue])),AttributeDecl(Instance,VarDecl(Id(_),ClassType(Id(____)),NullLiteral())),AttributeDecl(Instance,VarDecl(Id(J),ClassType(Id(____)),NullLiteral())),AttributeDecl(Instance,VarDecl(Id(J_8),ClassType(Id(____)),NullLiteral()))]),ClassDecl(Id(g),Id(TZ),[MethodDecl(Id(Destructor),Instance,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([Block([]),VarDecl(Id(_),BoolType),VarDecl(Id(qY),BoolType),VarDecl(Id(_),BoolType)])),MethodDecl(Id($T),Static,[param(Id(xi),ArrayType(60,StringType)),param(Id(_10),ArrayType(60,StringType)),param(Id(_),ArrayType(60,StringType)),param(Id(_a),ClassType(Id(_c_9))),param(Id(C),ClassType(Id(_c_9))),param(Id(n),ClassType(Id(M))),param(Id(O),ClassType(Id(f))),param(Id(_2),ArrayType(60,BoolType)),param(Id(_),ArrayType(60,BoolType))],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(G),[])])'''
        self.assertTrue(TestAST.test(line, expect, 0))

    def test_1(self):
        line = '''Class _:_5Q{$a(){Break ;}Destructor (){}Constructor (_8,J,H:Array [Float ,0x1D];___,_:Array [Array [Boolean ,0x33],0X2A];_VL_572D3,_:Array [Float ,0b101_0];_,bI,D_lm:Array [Float ,0x1D];e,A,__,_1,_:HE_){} }'''
        expect = '''Program([ClassDecl(Id(_),Id(_5Q),[MethodDecl(Id($a),Static,[],Block([Break])),MethodDecl(Id(Destructor),Instance,[],Block([])),MethodDecl(Id(Constructor),Instance,[param(Id(_8),ArrayType(29,FloatType)),param(Id(J),ArrayType(29,FloatType)),param(Id(H),ArrayType(29,FloatType)),param(Id(___),ArrayType(42,ArrayType(51,BoolType))),param(Id(_),ArrayType(42,ArrayType(51,BoolType))),param(Id(_VL_572D3),ArrayType(10,FloatType)),param(Id(_),ArrayType(10,FloatType)),param(Id(_),ArrayType(29,FloatType)),param(Id(bI),ArrayType(29,FloatType)),param(Id(D_lm),ArrayType(29,FloatType)),param(Id(e),ClassType(Id(HE_))),param(Id(A),ClassType(Id(HE_))),param(Id(__),ClassType(Id(HE_))),param(Id(_1),ClassType(Id(HE_))),param(Id(_),ClassType(Id(HE_)))],Block([]))])])'''
        self.assertTrue(TestAST.test(line, expect, 1))

    def test_2(self):
        line = '''Class _38:_m{Val $_,T:Float ;Destructor (){Var l56C_r_:Boolean ;}Constructor (){}Constructor (__,_:Array [Array [Array [Boolean ,0111],0111],5_0]){G0::$7t6.b._();Continue ;} }'''
        expect = '''Program([ClassDecl(Id(_38),Id(_m),[AttributeDecl(Static,ConstDecl(Id($_),FloatType,None)),AttributeDecl(Instance,ConstDecl(Id(T),FloatType,None)),MethodDecl(Id(Destructor),Instance,[],Block([VarDecl(Id(l56C_r_),BoolType)])),MethodDecl(Id(Constructor),Instance,[],Block([])),MethodDecl(Id(Constructor),Instance,[param(Id(__),ArrayType(50,ArrayType(73,ArrayType(73,BoolType)))),param(Id(_),ArrayType(50,ArrayType(73,ArrayType(73,BoolType))))],Block([Call(FieldAccess(FieldAccess(Id(G0),Id($7t6)),Id(b)),Id(_),[]),Continue]))])])'''
        self.assertTrue(TestAST.test(line, expect, 2))

    def test_3(self):
        line = '''Class _:____{}Class Q:__{Val K,$0:S;_f(I:String ){} }Class c{}Class U{}Class __:I{___(_:String ;e7o_,_,e3,H_:Array [Boolean ,0X7_CC];____4,_:String ){}Val $c8,_,$J:va;}'''
        expect = '''Program([ClassDecl(Id(_),Id(____),[]),ClassDecl(Id(Q),Id(__),[AttributeDecl(Instance,ConstDecl(Id(K),ClassType(Id(S)),NullLiteral())),AttributeDecl(Static,ConstDecl(Id($0),ClassType(Id(S)),NullLiteral())),MethodDecl(Id(_f),Instance,[param(Id(I),StringType)],Block([]))]),ClassDecl(Id(c),[]),ClassDecl(Id(U),[]),ClassDecl(Id(__),Id(I),[MethodDecl(Id(___),Instance,[param(Id(_),StringType),param(Id(e7o_),ArrayType(1996,BoolType)),param(Id(_),ArrayType(1996,BoolType)),param(Id(e3),ArrayType(1996,BoolType)),param(Id(H_),ArrayType(1996,BoolType)),param(Id(____4),StringType),param(Id(_),StringType)],Block([])),AttributeDecl(Static,ConstDecl(Id($c8),ClassType(Id(va)),NullLiteral())),AttributeDecl(Instance,ConstDecl(Id(_),ClassType(Id(va)),NullLiteral())),AttributeDecl(Static,ConstDecl(Id($J),ClassType(Id(va)),NullLiteral()))])])'''
        self.assertTrue(TestAST.test(line, expect, 3))

    def test_4(self):
        line = '''Class __:_1{Var $u,_:Int ;Constructor (_:Float ;g,__,_q:Float ;f,p:_;Q_0,W,_oq__,M__:Array [String ,3]){Return ;} }Class _:_{Val $1_1Pk,_01_8:j8z9E_;}Class _7{Destructor (){}Var $930h_T,$8,$i,_:Int ;}'''
        expect = '''Program([ClassDecl(Id(__),Id(_1),[AttributeDecl(Static,VarDecl(Id($u),IntType)),AttributeDecl(Instance,VarDecl(Id(_),IntType)),MethodDecl(Id(Constructor),Instance,[param(Id(_),FloatType),param(Id(g),FloatType),param(Id(__),FloatType),param(Id(_q),FloatType),param(Id(f),ClassType(Id(_))),param(Id(p),ClassType(Id(_))),param(Id(Q_0),ArrayType(3,StringType)),param(Id(W),ArrayType(3,StringType)),param(Id(_oq__),ArrayType(3,StringType)),param(Id(M__),ArrayType(3,StringType))],Block([Return()]))]),ClassDecl(Id(_),Id(_),[AttributeDecl(Static,ConstDecl(Id($1_1Pk),ClassType(Id(j8z9E_)),NullLiteral())),AttributeDecl(Instance,ConstDecl(Id(_01_8),ClassType(Id(j8z9E_)),NullLiteral()))]),ClassDecl(Id(_7),[MethodDecl(Id(Destructor),Instance,[],Block([])),AttributeDecl(Static,VarDecl(Id($930h_T),IntType)),AttributeDecl(Static,VarDecl(Id($8),IntType)),AttributeDecl(Static,VarDecl(Id($i),IntType)),AttributeDecl(Instance,VarDecl(Id(_),IntType))])])'''
        self.assertTrue(TestAST.test(line, expect, 4))

    def test_5(self):
        line = '''Class a:__{}Class m:v_h_b__{}Class Z{}Class __{$w(_L,W:Array [Array [Array [Array [Int ,0106],0X5],0b10],5]){} }Class _:l_8h{Val _:Boolean ;y_(D:Array [Array [Array [Boolean ,82],6_3],8]){} }'''
        expect = '''Program([ClassDecl(Id(a),Id(__),[]),ClassDecl(Id(m),Id(v_h_b__),[]),ClassDecl(Id(Z),[]),ClassDecl(Id(__),[MethodDecl(Id($w),Static,[param(Id(_L),ArrayType(5,ArrayType(2,ArrayType(5,ArrayType(70,IntType))))),param(Id(W),ArrayType(5,ArrayType(2,ArrayType(5,ArrayType(70,IntType)))))],Block([]))]),ClassDecl(Id(_),Id(l_8h),[AttributeDecl(Instance,ConstDecl(Id(_),BoolType,None)),MethodDecl(Id(y_),Instance,[param(Id(D),ArrayType(8,ArrayType(63,ArrayType(82,BoolType))))],Block([]))])])'''
        self.assertTrue(TestAST.test(line, expect, 5))

    def test_6(self):
        line = '''Class z{Var $_:Boolean ;S(W_,f47:Int ;z,_y12,_,_Rh,_I9:Float ;A,EN,_6d,g1,M_:Array [Array [Array [Array [Array [Array [Array [Array [Int ,011],74],0x2A],0b1_1_1],0x1_7],0B1],04],0x2A]){} }'''
        expect = '''Program([ClassDecl(Id(z),[AttributeDecl(Static,VarDecl(Id($_),BoolType)),MethodDecl(Id(S),Instance,[param(Id(W_),IntType),param(Id(f47),IntType),param(Id(z),FloatType),param(Id(_y12),FloatType),param(Id(_),FloatType),param(Id(_Rh),FloatType),param(Id(_I9),FloatType),param(Id(A),ArrayType(42,ArrayType(4,ArrayType(1,ArrayType(23,ArrayType(7,ArrayType(42,ArrayType(74,ArrayType(9,IntType))))))))),param(Id(EN),ArrayType(42,ArrayType(4,ArrayType(1,ArrayType(23,ArrayType(7,ArrayType(42,ArrayType(74,ArrayType(9,IntType))))))))),param(Id(_6d),ArrayType(42,ArrayType(4,ArrayType(1,ArrayType(23,ArrayType(7,ArrayType(42,ArrayType(74,ArrayType(9,IntType))))))))),param(Id(g1),ArrayType(42,ArrayType(4,ArrayType(1,ArrayType(23,ArrayType(7,ArrayType(42,ArrayType(74,ArrayType(9,IntType))))))))),param(Id(M_),ArrayType(42,ArrayType(4,ArrayType(1,ArrayType(23,ArrayType(7,ArrayType(42,ArrayType(74,ArrayType(9,IntType)))))))))],Block([]))])])'''
        self.assertTrue(TestAST.test(line, expect, 6))

    def test_7(self):
        line = '''Class _8:B{}Class _n{}Class _:N{Var R,$v_:o;Constructor (_W1,oi:Array [Boolean ,2_9];__:Array [String ,01];_3Q4Q_,B,z:Boolean ;_,_:Array [Array [String ,74],3];O,D9,_,V:Int ;_:Array [Float ,31]){Break ;}Val $G,$4:_;}'''
        expect = '''Program([ClassDecl(Id(_8),Id(B),[]),ClassDecl(Id(_n),[]),ClassDecl(Id(_),Id(N),[AttributeDecl(Instance,VarDecl(Id(R),ClassType(Id(o)),NullLiteral())),AttributeDecl(Static,VarDecl(Id($v_),ClassType(Id(o)),NullLiteral())),MethodDecl(Id(Constructor),Instance,[param(Id(_W1),ArrayType(29,BoolType)),param(Id(oi),ArrayType(29,BoolType)),param(Id(__),ArrayType(1,StringType)),param(Id(_3Q4Q_),BoolType),param(Id(B),BoolType),param(Id(z),BoolType),param(Id(_),ArrayType(3,ArrayType(74,StringType))),param(Id(_),ArrayType(3,ArrayType(74,StringType))),param(Id(O),IntType),param(Id(D9),IntType),param(Id(_),IntType),param(Id(V),IntType),param(Id(_),ArrayType(31,FloatType))],Block([Break])),AttributeDecl(Static,ConstDecl(Id($G),ClassType(Id(_)),NullLiteral())),AttributeDecl(Static,ConstDecl(Id($4),ClassType(Id(_)),NullLiteral()))])])'''
        self.assertTrue(TestAST.test(line, expect, 7))

    def test_8(self):
        line = '''Class V9:M__o{}Class n:j0{Constructor (_,_305TZ,j,Y_,p_,cB:_;_:Array [Float ,1_81];_,_m8,q_3B_:Boolean ;_70k:_;M0,_:Int ;_:Array [Array [String ,5],8_4_0_8];K5:Boolean ;V1:_6){Val _4,V9:Boolean ;New _H().i_._();} }Class _:_u{}'''
        expect = '''Program([ClassDecl(Id(V9),Id(M__o),[]),ClassDecl(Id(n),Id(j0),[MethodDecl(Id(Constructor),Instance,[param(Id(_),ClassType(Id(_))),param(Id(_305TZ),ClassType(Id(_))),param(Id(j),ClassType(Id(_))),param(Id(Y_),ClassType(Id(_))),param(Id(p_),ClassType(Id(_))),param(Id(cB),ClassType(Id(_))),param(Id(_),ArrayType(181,FloatType)),param(Id(_),BoolType),param(Id(_m8),BoolType),param(Id(q_3B_),BoolType),param(Id(_70k),ClassType(Id(_))),param(Id(M0),IntType),param(Id(_),IntType),param(Id(_),ArrayType(8408,ArrayType(5,StringType))),param(Id(K5),BoolType),param(Id(V1),ClassType(Id(_6)))],Block([ConstDecl(Id(_4),BoolType,None),ConstDecl(Id(V9),BoolType,None),Call(FieldAccess(NewExpr(Id(_H),[]),Id(i_)),Id(_),[])]))]),ClassDecl(Id(_),Id(_u),[])])'''
        self.assertTrue(TestAST.test(line, expect, 8))

    def test_9(self):
        line = '''Class Y{}Class U:C0{Constructor (){}$t8s(){}Val $8,$0t,_,$__,_,$_,_:Array [String ,046];Var $_i,q,w:Float ;$_(_dj:Array [Array [String ,0b1],046];_:P;cj,_:Array [Int ,0X4B]){} }'''
        expect = '''Program([ClassDecl(Id(Y),[]),ClassDecl(Id(U),Id(C0),[MethodDecl(Id(Constructor),Instance,[],Block([])),MethodDecl(Id($t8s),Static,[],Block([])),AttributeDecl(Static,ConstDecl(Id($8),ArrayType(38,StringType),None)),AttributeDecl(Static,ConstDecl(Id($0t),ArrayType(38,StringType),None)),AttributeDecl(Instance,ConstDecl(Id(_),ArrayType(38,StringType),None)),AttributeDecl(Static,ConstDecl(Id($__),ArrayType(38,StringType),None)),AttributeDecl(Instance,ConstDecl(Id(_),ArrayType(38,StringType),None)),AttributeDecl(Static,ConstDecl(Id($_),ArrayType(38,StringType),None)),AttributeDecl(Instance,ConstDecl(Id(_),ArrayType(38,StringType),None)),AttributeDecl(Static,VarDecl(Id($_i),FloatType)),AttributeDecl(Instance,VarDecl(Id(q),FloatType)),AttributeDecl(Instance,VarDecl(Id(w),FloatType)),MethodDecl(Id($_),Static,[param(Id(_dj),ArrayType(38,ArrayType(1,StringType))),param(Id(_),ClassType(Id(P))),param(Id(cj),ArrayType(75,IntType)),param(Id(_),ArrayType(75,IntType))],Block([]))])])'''
        self.assertTrue(TestAST.test(line, expect, 9))

    def test_10(self):
        line = '''Class _:q{$Z(){}Constructor (A:T4_;_M2,n:Boolean ;d_9_z,D:Array [String ,05];_H_c__L:_;_,__W:Array [Array [Boolean ,0140],0b1]){Val __G0v,_3,__,fN:H_;}Var y28_:R;Destructor (){} }Class __s:dJi{}'''
        expect = '''Program([ClassDecl(Id(_),Id(q),[MethodDecl(Id($Z),Static,[],Block([])),MethodDecl(Id(Constructor),Instance,[param(Id(A),ClassType(Id(T4_))),param(Id(_M2),BoolType),param(Id(n),BoolType),param(Id(d_9_z),ArrayType(5,StringType)),param(Id(D),ArrayType(5,StringType)),param(Id(_H_c__L),ClassType(Id(_))),param(Id(_),ArrayType(1,ArrayType(96,BoolType))),param(Id(__W),ArrayType(1,ArrayType(96,BoolType)))],Block([ConstDecl(Id(__G0v),ClassType(Id(H_)),NullLiteral()),ConstDecl(Id(_3),ClassType(Id(H_)),NullLiteral()),ConstDecl(Id(__),ClassType(Id(H_)),NullLiteral()),ConstDecl(Id(fN),ClassType(Id(H_)),NullLiteral())])),AttributeDecl(Instance,VarDecl(Id(y28_),ClassType(Id(R)),NullLiteral())),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(__s),Id(dJi),[])])'''
        self.assertTrue(TestAST.test(line, expect, 10))

    def test_11(self):
        line = '''Class _:_3_j{Constructor (L:Boolean ;n:Array [Boolean ,23_9]){W__1_6M1::$C=!tQ__::$SB._;Continue ;} }Class FU__{Constructor (b_,___:String ){Continue ;Break ;}_d__(){Return ;Continue ;Var g:Y;} }'''
        expect = '''Program([ClassDecl(Id(_),Id(_3_j),[MethodDecl(Id(Constructor),Instance,[param(Id(L),BoolType),param(Id(n),ArrayType(239,BoolType))],Block([AssignStmt(FieldAccess(Id(W__1_6M1),Id($C)),UnaryOp(!,FieldAccess(FieldAccess(Id(tQ__),Id($SB)),Id(_)))),Continue]))]),ClassDecl(Id(FU__),[MethodDecl(Id(Constructor),Instance,[param(Id(b_),StringType),param(Id(___),StringType)],Block([Continue,Break])),MethodDecl(Id(_d__),Instance,[],Block([Return(),Continue,VarDecl(Id(g),ClassType(Id(Y)),NullLiteral())]))])])'''
        self.assertTrue(TestAST.test(line, expect, 11))

    def test_12(self):
        line = '''Class _w:Z{Val $z,$_,$Q0__a,$_,_7:_;Var $__01:Array [Int ,0b11101];Constructor (B:Array [Array [Array [Float ,0b11101],0X2E],062];f,_3s,_43Q3,_k2_v_,N:Boolean ;_,a,__65_,vwV_5_,P,_v_:Array [Array [Array [Float ,67],7_71_87_561],061];_:Array [Boolean ,0x42];_,_,Fp8:V){}$_2(H:Int ;x,_:_;S:Float ;RY,Y_H:m){}Constructor (_,_,_,QN:_;_Ym:Int ;A:Array [Int ,0X4];y:Int ){}_0(_:Int ;_,_,i_6:Array [Float ,0B10];__,_Ey_S,M:Float ;_e_Z:Array [Array [Boolean ,4_4],0X2E]){Val __,__:d;}Constructor (){} }'''
        expect = '''Program([ClassDecl(Id(_w),Id(Z),[AttributeDecl(Static,ConstDecl(Id($z),ClassType(Id(_)),NullLiteral())),AttributeDecl(Static,ConstDecl(Id($_),ClassType(Id(_)),NullLiteral())),AttributeDecl(Static,ConstDecl(Id($Q0__a),ClassType(Id(_)),NullLiteral())),AttributeDecl(Static,ConstDecl(Id($_),ClassType(Id(_)),NullLiteral())),AttributeDecl(Instance,ConstDecl(Id(_7),ClassType(Id(_)),NullLiteral())),AttributeDecl(Static,VarDecl(Id($__01),ArrayType(29,IntType))),MethodDecl(Id(Constructor),Instance,[param(Id(B),ArrayType(50,ArrayType(46,ArrayType(29,FloatType)))),param(Id(f),BoolType),param(Id(_3s),BoolType),param(Id(_43Q3),BoolType),param(Id(_k2_v_),BoolType),param(Id(N),BoolType),param(Id(_),ArrayType(49,ArrayType(77187561,ArrayType(67,FloatType)))),param(Id(a),ArrayType(49,ArrayType(77187561,ArrayType(67,FloatType)))),param(Id(__65_),ArrayType(49,ArrayType(77187561,ArrayType(67,FloatType)))),param(Id(vwV_5_),ArrayType(49,ArrayType(77187561,ArrayType(67,FloatType)))),param(Id(P),ArrayType(49,ArrayType(77187561,ArrayType(67,FloatType)))),param(Id(_v_),ArrayType(49,ArrayType(77187561,ArrayType(67,FloatType)))),param(Id(_),ArrayType(66,BoolType)),param(Id(_),ClassType(Id(V))),param(Id(_),ClassType(Id(V))),param(Id(Fp8),ClassType(Id(V)))],Block([])),MethodDecl(Id($_2),Static,[param(Id(H),IntType),param(Id(x),ClassType(Id(_))),param(Id(_),ClassType(Id(_))),param(Id(S),FloatType),param(Id(RY),ClassType(Id(m))),param(Id(Y_H),ClassType(Id(m)))],Block([])),MethodDecl(Id(Constructor),Instance,[param(Id(_),ClassType(Id(_))),param(Id(_),ClassType(Id(_))),param(Id(_),ClassType(Id(_))),param(Id(QN),ClassType(Id(_))),param(Id(_Ym),IntType),param(Id(A),ArrayType(4,IntType)),param(Id(y),IntType)],Block([])),MethodDecl(Id(_0),Instance,[param(Id(_),IntType),param(Id(_),ArrayType(2,FloatType)),param(Id(_),ArrayType(2,FloatType)),param(Id(i_6),ArrayType(2,FloatType)),param(Id(__),FloatType),param(Id(_Ey_S),FloatType),param(Id(M),FloatType),param(Id(_e_Z),ArrayType(46,ArrayType(44,BoolType)))],Block([ConstDecl(Id(__),ClassType(Id(d)),NullLiteral()),ConstDecl(Id(__),ClassType(Id(d)),NullLiteral())])),MethodDecl(Id(Constructor),Instance,[],Block([]))])])'''
        self.assertTrue(TestAST.test(line, expect, 12))

    def test_13(self):
        line = '''Class n{Val _,FQy,$_,$K:Float ;Constructor (v:Int ;L,_8,__,_l_1_6,_:Array [Array [Array [Array [Boolean ,0b1],0b11],57],0101];_,_:Int ;_j,b6_,_5:_jQ){} }Class d{Val $_:Array [Int ,0B1];_(){} }'''
        expect = '''Program([ClassDecl(Id(n),[AttributeDecl(Instance,ConstDecl(Id(_),FloatType,None)),AttributeDecl(Instance,ConstDecl(Id(FQy),FloatType,None)),AttributeDecl(Static,ConstDecl(Id($_),FloatType,None)),AttributeDecl(Static,ConstDecl(Id($K),FloatType,None)),MethodDecl(Id(Constructor),Instance,[param(Id(v),IntType),param(Id(L),ArrayType(65,ArrayType(57,ArrayType(3,ArrayType(1,BoolType))))),param(Id(_8),ArrayType(65,ArrayType(57,ArrayType(3,ArrayType(1,BoolType))))),param(Id(__),ArrayType(65,ArrayType(57,ArrayType(3,ArrayType(1,BoolType))))),param(Id(_l_1_6),ArrayType(65,ArrayType(57,ArrayType(3,ArrayType(1,BoolType))))),param(Id(_),ArrayType(65,ArrayType(57,ArrayType(3,ArrayType(1,BoolType))))),param(Id(_),IntType),param(Id(_),IntType),param(Id(_j),ClassType(Id(_jQ))),param(Id(b6_),ClassType(Id(_jQ))),param(Id(_5),ClassType(Id(_jQ)))],Block([]))]),ClassDecl(Id(d),[AttributeDecl(Static,ConstDecl(Id($_),ArrayType(1,IntType),None)),MethodDecl(Id(_),Instance,[],Block([]))])])'''
        self.assertTrue(TestAST.test(line, expect, 13))

    def test_14(self):
        line = '''Class _y__FL{Val $T:Array [Array [Array [Array [Array [Float ,0142],17],17],0b10],0X12];$3(t_f:Array [Array [String ,0142],17]){} }Class d9V_5_:__{}Class _3t{}Class v:b{Constructor (__8,f:Array [Array [Int ,0X12],0B1]){Break ;} }'''
        expect = '''Program([ClassDecl(Id(_y__FL),[AttributeDecl(Static,ConstDecl(Id($T),ArrayType(18,ArrayType(2,ArrayType(17,ArrayType(17,ArrayType(98,FloatType))))),None)),MethodDecl(Id($3),Static,[param(Id(t_f),ArrayType(17,ArrayType(98,StringType)))],Block([]))]),ClassDecl(Id(d9V_5_),Id(__),[]),ClassDecl(Id(_3t),[]),ClassDecl(Id(v),Id(b),[MethodDecl(Id(Constructor),Instance,[param(Id(__8),ArrayType(1,ArrayType(18,IntType))),param(Id(f),ArrayType(1,ArrayType(18,IntType)))],Block([Break]))])])'''
        self.assertTrue(TestAST.test(line, expect, 14))

    def test_15(self):
        line = '''Class w{Constructor (){}Destructor (){} }Class _{Val L,_,o:Array [Int ,07_6];Constructor (E1S9,TO,_9__,_9,Y_:Tg__6__n){Continue ;}Constructor (d_,M:Int ){} }Class _{}Class z_:_{Var $888S:Boolean ;}'''
        expect = '''Program([ClassDecl(Id(w),[MethodDecl(Id(Constructor),Instance,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(_),[AttributeDecl(Instance,ConstDecl(Id(L),ArrayType(62,IntType),None)),AttributeDecl(Instance,ConstDecl(Id(_),ArrayType(62,IntType),None)),AttributeDecl(Instance,ConstDecl(Id(o),ArrayType(62,IntType),None)),MethodDecl(Id(Constructor),Instance,[param(Id(E1S9),ClassType(Id(Tg__6__n))),param(Id(TO),ClassType(Id(Tg__6__n))),param(Id(_9__),ClassType(Id(Tg__6__n))),param(Id(_9),ClassType(Id(Tg__6__n))),param(Id(Y_),ClassType(Id(Tg__6__n)))],Block([Continue])),MethodDecl(Id(Constructor),Instance,[param(Id(d_),IntType),param(Id(M),IntType)],Block([]))]),ClassDecl(Id(_),[]),ClassDecl(Id(z_),Id(_),[AttributeDecl(Static,VarDecl(Id($888S),BoolType))])])'''
        self.assertTrue(TestAST.test(line, expect, 15))

    def test_16(self):
        line = '''Class ___{Val _:String ;Destructor (){}Val a,$ar,R9:A_qN;Var $3koT:Array [Array [Array [Array [Array [Array [Array [Array [Array [Array [Int ,057],015],057],057],0b10010],0x27],0b10010],0XD5D_7],0B1],0xE];Destructor (){} }'''
        expect = '''Program([ClassDecl(Id(___),[AttributeDecl(Instance,ConstDecl(Id(_),StringType,None)),MethodDecl(Id(Destructor),Instance,[],Block([])),AttributeDecl(Instance,ConstDecl(Id(a),ClassType(Id(A_qN)),NullLiteral())),AttributeDecl(Static,ConstDecl(Id($ar),ClassType(Id(A_qN)),NullLiteral())),AttributeDecl(Instance,ConstDecl(Id(R9),ClassType(Id(A_qN)),NullLiteral())),AttributeDecl(Static,VarDecl(Id($3koT),ArrayType(14,ArrayType(1,ArrayType(54743,ArrayType(18,ArrayType(39,ArrayType(18,ArrayType(47,ArrayType(47,ArrayType(13,ArrayType(47,IntType)))))))))))),MethodDecl(Id(Destructor),Instance,[],Block([]))])])'''
        self.assertTrue(TestAST.test(line, expect, 16))

    def test_17(self):
        line = '''Class _7_r:k{}Class n{Constructor (M_6,_oz7:Array [Array [Array [Array [Array [Array [String ,50],0121],0x6],0b110110],0X24],0B1]){} }Class _I:_7{}Class _pz376:e___{}Class s{Val $_:yi;}Class n5:w{}'''
        expect = '''Program([ClassDecl(Id(_7_r),Id(k),[]),ClassDecl(Id(n),[MethodDecl(Id(Constructor),Instance,[param(Id(M_6),ArrayType(1,ArrayType(36,ArrayType(54,ArrayType(6,ArrayType(81,ArrayType(50,StringType))))))),param(Id(_oz7),ArrayType(1,ArrayType(36,ArrayType(54,ArrayType(6,ArrayType(81,ArrayType(50,StringType)))))))],Block([]))]),ClassDecl(Id(_I),Id(_7),[]),ClassDecl(Id(_pz376),Id(e___),[]),ClassDecl(Id(s),[AttributeDecl(Static,ConstDecl(Id($_),ClassType(Id(yi)),NullLiteral()))]),ClassDecl(Id(n5),Id(w),[])])'''
        self.assertTrue(TestAST.test(line, expect, 17))

    def test_18(self):
        line = '''Class _5:Qp{}Class _:o{_582(__,Xs:kqY;u_:Array [Array [Float ,0X32],0x32];T:_6g_;F,_,__2,js:F_mm_){} }Class h:__{$_9(A:R;FuD11:Boolean ;_:Array [Array [Int ,0575_7_2_0],051_7]){} }Class g{}'''
        expect = '''Program([ClassDecl(Id(_5),Id(Qp),[]),ClassDecl(Id(_),Id(o),[MethodDecl(Id(_582),Instance,[param(Id(__),ClassType(Id(kqY))),param(Id(Xs),ClassType(Id(kqY))),param(Id(u_),ArrayType(50,ArrayType(50,FloatType))),param(Id(T),ClassType(Id(_6g_))),param(Id(F),ClassType(Id(F_mm_))),param(Id(_),ClassType(Id(F_mm_))),param(Id(__2),ClassType(Id(F_mm_))),param(Id(js),ClassType(Id(F_mm_)))],Block([]))]),ClassDecl(Id(h),Id(__),[MethodDecl(Id($_9),Static,[param(Id(A),ClassType(Id(R))),param(Id(FuD11),BoolType),param(Id(_),ArrayType(335,ArrayType(195536,IntType)))],Block([]))]),ClassDecl(Id(g),[])])'''
        self.assertTrue(TestAST.test(line, expect, 18))

    def test_19(self):
        line = '''Class O_{}Class t2{Val _1X,_W_5_:_;}Class V:b_{Val J,$I:Array [Boolean ,4_4];}Class F:hnL{}Class o:_6{Constructor (B6,aBP_:Array [String ,0x42];o,_,_98_,k8208_:Int ;D:String ;m_,U:_b_;_9U09,_,__,O:Float ){ {Break ;}Break ;}Destructor (){}Var O__:Array [Int ,02];}'''
        expect = '''Program([ClassDecl(Id(O_),[]),ClassDecl(Id(t2),[AttributeDecl(Instance,ConstDecl(Id(_1X),ClassType(Id(_)),NullLiteral())),AttributeDecl(Instance,ConstDecl(Id(_W_5_),ClassType(Id(_)),NullLiteral()))]),ClassDecl(Id(V),Id(b_),[AttributeDecl(Instance,ConstDecl(Id(J),ArrayType(44,BoolType),None)),AttributeDecl(Static,ConstDecl(Id($I),ArrayType(44,BoolType),None))]),ClassDecl(Id(F),Id(hnL),[]),ClassDecl(Id(o),Id(_6),[MethodDecl(Id(Constructor),Instance,[param(Id(B6),ArrayType(66,StringType)),param(Id(aBP_),ArrayType(66,StringType)),param(Id(o),IntType),param(Id(_),IntType),param(Id(_98_),IntType),param(Id(k8208_),IntType),param(Id(D),StringType),param(Id(m_),ClassType(Id(_b_))),param(Id(U),ClassType(Id(_b_))),param(Id(_9U09),FloatType),param(Id(_),FloatType),param(Id(__),FloatType),param(Id(O),FloatType)],Block([Block([Break]),Break])),MethodDecl(Id(Destructor),Instance,[],Block([])),AttributeDecl(Instance,VarDecl(Id(O__),ArrayType(2,IntType)))])])'''
        self.assertTrue(TestAST.test(line, expect, 19))

    def test_20(self):
        line = '''Class _:_{Constructor (cI_u:Array [Int ,0B1_0];V:Array [Array [Array [Array [Int ,0B100110],0B100110],0b1],6_077];S_kW,_6,B,_:Array [Array [String ,44],7];n,S:Boolean ;___,U,_,_:Array [Boolean ,44];_,_,E:_){} }'''
        expect = '''Program([ClassDecl(Id(_),Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(cI_u),ArrayType(2,IntType)),param(Id(V),ArrayType(6077,ArrayType(1,ArrayType(38,ArrayType(38,IntType))))),param(Id(S_kW),ArrayType(7,ArrayType(44,StringType))),param(Id(_6),ArrayType(7,ArrayType(44,StringType))),param(Id(B),ArrayType(7,ArrayType(44,StringType))),param(Id(_),ArrayType(7,ArrayType(44,StringType))),param(Id(n),BoolType),param(Id(S),BoolType),param(Id(___),ArrayType(44,BoolType)),param(Id(U),ArrayType(44,BoolType)),param(Id(_),ArrayType(44,BoolType)),param(Id(_),ArrayType(44,BoolType)),param(Id(_),ClassType(Id(_))),param(Id(_),ClassType(Id(_))),param(Id(E),ClassType(Id(_)))],Block([]))])])'''
        self.assertTrue(TestAST.test(line, expect, 20))

    def test_21(self):
        line = '''Class r{Constructor (hN:z;o41_:Array [Array [Float ,0B1],012];h3,__,_:_){ {} }Destructor (){}Constructor (_737,_7,f:_){New O3().____();} }Class U{Constructor (__H5,uK_,_2:Boolean ;_L:W;t:_03){} }'''
        expect = '''Program([ClassDecl(Id(r),[MethodDecl(Id(Constructor),Instance,[param(Id(hN),ClassType(Id(z))),param(Id(o41_),ArrayType(10,ArrayType(1,FloatType))),param(Id(h3),ClassType(Id(_))),param(Id(__),ClassType(Id(_))),param(Id(_),ClassType(Id(_)))],Block([Block([])])),MethodDecl(Id(Destructor),Instance,[],Block([])),MethodDecl(Id(Constructor),Instance,[param(Id(_737),ClassType(Id(_))),param(Id(_7),ClassType(Id(_))),param(Id(f),ClassType(Id(_)))],Block([Call(NewExpr(Id(O3),[]),Id(____),[])]))]),ClassDecl(Id(U),[MethodDecl(Id(Constructor),Instance,[param(Id(__H5),BoolType),param(Id(uK_),BoolType),param(Id(_2),BoolType),param(Id(_L),ClassType(Id(W))),param(Id(t),ClassType(Id(_03)))],Block([]))])])'''
        self.assertTrue(TestAST.test(line, expect, 21))

    def test_22(self):
        line = '''Class _g{}Class x__{}Class __{}Class __:k_{E(R:Array [Boolean ,0B11_01];_8_:Boolean ){} }Class _{oWU(cP:_Q_;_,__:Array [Array [Array [Array [Int ,0x4],0B100010],0B1],0B1]){} }'''
        expect = '''Program([ClassDecl(Id(_g),[]),ClassDecl(Id(x__),[]),ClassDecl(Id(__),[]),ClassDecl(Id(__),Id(k_),[MethodDecl(Id(E),Instance,[param(Id(R),ArrayType(13,BoolType)),param(Id(_8_),BoolType)],Block([]))]),ClassDecl(Id(_),[MethodDecl(Id(oWU),Instance,[param(Id(cP),ClassType(Id(_Q_))),param(Id(_),ArrayType(1,ArrayType(1,ArrayType(34,ArrayType(4,IntType))))),param(Id(__),ArrayType(1,ArrayType(1,ArrayType(34,ArrayType(4,IntType)))))],Block([]))])])'''
        self.assertTrue(TestAST.test(line, expect, 22))

    def test_23(self):
        line = '''Class __:_{$9x(){} }Class _0{Var $30,$__:Array [Int ,0B1];Val $Icd__3L:Array [Array [String ,0XA4],0B1000110];Var H,$UN,_1_K,$76:Q;$_0i(_,_9:Array [Float ,55];V__,P_,__6n:Array [Float ,826]){}Destructor (){} }'''
        expect = '''Program([ClassDecl(Id(__),Id(_),[MethodDecl(Id($9x),Static,[],Block([]))]),ClassDecl(Id(_0),[AttributeDecl(Static,VarDecl(Id($30),ArrayType(1,IntType))),AttributeDecl(Static,VarDecl(Id($__),ArrayType(1,IntType))),AttributeDecl(Static,ConstDecl(Id($Icd__3L),ArrayType(70,ArrayType(164,StringType)),None)),AttributeDecl(Instance,VarDecl(Id(H),ClassType(Id(Q)),NullLiteral())),AttributeDecl(Static,VarDecl(Id($UN),ClassType(Id(Q)),NullLiteral())),AttributeDecl(Instance,VarDecl(Id(_1_K),ClassType(Id(Q)),NullLiteral())),AttributeDecl(Static,VarDecl(Id($76),ClassType(Id(Q)),NullLiteral())),MethodDecl(Id($_0i),Static,[param(Id(_),ArrayType(55,FloatType)),param(Id(_9),ArrayType(55,FloatType)),param(Id(V__),ArrayType(826,FloatType)),param(Id(P_),ArrayType(826,FloatType)),param(Id(__6n),ArrayType(826,FloatType))],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))])])'''
        self.assertTrue(TestAST.test(line, expect, 23))

    def test_24(self):
        line = '''Class L99vxs_{}Class I_B:_{Var $4:Array [Int ,0b10000];}Class __:L{}Class g{Val $j_,$K_2,g:Array [Int ,06];}Class _v:_KW9_{Val $Mf,$03obA,_:Array [Array [String ,0b10000],0B1];}'''
        expect = '''Program([ClassDecl(Id(L99vxs_),[]),ClassDecl(Id(I_B),Id(_),[AttributeDecl(Static,VarDecl(Id($4),ArrayType(16,IntType)))]),ClassDecl(Id(__),Id(L),[]),ClassDecl(Id(g),[AttributeDecl(Static,ConstDecl(Id($j_),ArrayType(6,IntType),None)),AttributeDecl(Static,ConstDecl(Id($K_2),ArrayType(6,IntType),None)),AttributeDecl(Instance,ConstDecl(Id(g),ArrayType(6,IntType),None))]),ClassDecl(Id(_v),Id(_KW9_),[AttributeDecl(Static,ConstDecl(Id($Mf),ArrayType(1,ArrayType(16,StringType)),None)),AttributeDecl(Static,ConstDecl(Id($03obA),ArrayType(1,ArrayType(16,StringType)),None)),AttributeDecl(Instance,ConstDecl(Id(_),ArrayType(1,ArrayType(16,StringType)),None))])])'''
        self.assertTrue(TestAST.test(line, expect, 24))

    def test_25(self):
        line = '''Class O_a9_{}Class b_{}Class Y3F__HWw{}Class _{}Class _:h{Constructor (wh:_12n_;M_n:Array [Float ,0B1000010];o:_){Break ;}V_(bN,o__,N:Array [Float ,0X48];C_:Array [Array [Int ,0b100110],0X2];s_8_:Boolean ){} }'''
        expect = '''Program([ClassDecl(Id(O_a9_),[]),ClassDecl(Id(b_),[]),ClassDecl(Id(Y3F__HWw),[]),ClassDecl(Id(_),[]),ClassDecl(Id(_),Id(h),[MethodDecl(Id(Constructor),Instance,[param(Id(wh),ClassType(Id(_12n_))),param(Id(M_n),ArrayType(66,FloatType)),param(Id(o),ClassType(Id(_)))],Block([Break])),MethodDecl(Id(V_),Instance,[param(Id(bN),ArrayType(72,FloatType)),param(Id(o__),ArrayType(72,FloatType)),param(Id(N),ArrayType(72,FloatType)),param(Id(C_),ArrayType(2,ArrayType(38,IntType))),param(Id(s_8_),BoolType)],Block([]))])])'''
        self.assertTrue(TestAST.test(line, expect, 25))

    def test_26(self):
        line = '''Class _:_{Constructor (Oz,RAs__1e7rZ4_:_EAq_;_:_H_;__:Array [Float ,0x4A];H:t;l:O_f6__8kR;g,_f0__2:Array [Boolean ,031];_:Float ){} }Class L__30:Q_{}Class lw{}Class G_:_{}Class _9{Destructor (){} }Class A:Z__{}Class _:__{Destructor (){}$4(){} }'''
        expect = '''Program([ClassDecl(Id(_),Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(Oz),ClassType(Id(_EAq_))),param(Id(RAs__1e7rZ4_),ClassType(Id(_EAq_))),param(Id(_),ClassType(Id(_H_))),param(Id(__),ArrayType(74,FloatType)),param(Id(H),ClassType(Id(t))),param(Id(l),ClassType(Id(O_f6__8kR))),param(Id(g),ArrayType(25,BoolType)),param(Id(_f0__2),ArrayType(25,BoolType)),param(Id(_),FloatType)],Block([]))]),ClassDecl(Id(L__30),Id(Q_),[]),ClassDecl(Id(lw),[]),ClassDecl(Id(G_),Id(_),[]),ClassDecl(Id(_9),[MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(A),Id(Z__),[]),ClassDecl(Id(_),Id(__),[MethodDecl(Id(Destructor),Instance,[],Block([])),MethodDecl(Id($4),Static,[],Block([]))])])'''
        self.assertTrue(TestAST.test(line, expect, 26))

    def test_27(self):
        line = '''Class _7:f9{Val $H703:Array [Array [Array [Array [Array [Array [Int ,041],0X9],0x4],0X13],0B10_10110_00_0],5];Val $cq:Array [Array [Array [Float ,0X7],0b100011],0X13];Constructor (JT:_){}Destructor (){} }'''
        expect = '''Program([ClassDecl(Id(_7),Id(f9),[AttributeDecl(Static,ConstDecl(Id($H703),ArrayType(5,ArrayType(688,ArrayType(19,ArrayType(4,ArrayType(9,ArrayType(33,IntType)))))),None)),AttributeDecl(Static,ConstDecl(Id($cq),ArrayType(19,ArrayType(35,ArrayType(7,FloatType))),None)),MethodDecl(Id(Constructor),Instance,[param(Id(JT),ClassType(Id(_)))],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))])])'''
        self.assertTrue(TestAST.test(line, expect, 27))

    def test_28(self):
        line = '''Class O_{$_8(hs:_Vk;_:Array [Array [Array [Array [Array [Array [String ,046],0x3],0b1_0011],072],8],0x2B_3_3_EC_6_1_9];_h:Int ){}Destructor (){Return ;}Var $6_,$I,$1:hR;}Class knA_K{Var kG_,_O_,Sk,$u,$o48:String ;}'''
        expect = '''Program([ClassDecl(Id(O_),[MethodDecl(Id($_8),Static,[param(Id(hs),ClassType(Id(_Vk))),param(Id(_),ArrayType(11597170201,ArrayType(8,ArrayType(58,ArrayType(19,ArrayType(3,ArrayType(38,StringType))))))),param(Id(_h),IntType)],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([Return()])),AttributeDecl(Static,VarDecl(Id($6_),ClassType(Id(hR)),NullLiteral())),AttributeDecl(Static,VarDecl(Id($I),ClassType(Id(hR)),NullLiteral())),AttributeDecl(Static,VarDecl(Id($1),ClassType(Id(hR)),NullLiteral()))]),ClassDecl(Id(knA_K),[AttributeDecl(Instance,VarDecl(Id(kG_),StringType)),AttributeDecl(Instance,VarDecl(Id(_O_),StringType)),AttributeDecl(Instance,VarDecl(Id(Sk),StringType)),AttributeDecl(Static,VarDecl(Id($u),StringType)),AttributeDecl(Static,VarDecl(Id($o48),StringType))])])'''
        self.assertTrue(TestAST.test(line, expect, 28))

    def test_29(self):
        line = '''Class B{k_0(___:Array [Boolean ,0B1];T:i039;T_0n,_:A;_,_H1,E,fk:String ){}Destructor (){}$4o(haVA,_,_:Boolean ;I,__,Rr27,_,_eQ5K,_:String ;x,_:Q_T;J:Array [Array [Array [Float ,0X5E],2],2]){} }Class _{}Class D:wB1_S2h197{Destructor (){} }'''
        expect = '''Program([ClassDecl(Id(B),[MethodDecl(Id(k_0),Instance,[param(Id(___),ArrayType(1,BoolType)),param(Id(T),ClassType(Id(i039))),param(Id(T_0n),ClassType(Id(A))),param(Id(_),ClassType(Id(A))),param(Id(_),StringType),param(Id(_H1),StringType),param(Id(E),StringType),param(Id(fk),StringType)],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([])),MethodDecl(Id($4o),Static,[param(Id(haVA),BoolType),param(Id(_),BoolType),param(Id(_),BoolType),param(Id(I),StringType),param(Id(__),StringType),param(Id(Rr27),StringType),param(Id(_),StringType),param(Id(_eQ5K),StringType),param(Id(_),StringType),param(Id(x),ClassType(Id(Q_T))),param(Id(_),ClassType(Id(Q_T))),param(Id(J),ArrayType(2,ArrayType(2,ArrayType(94,FloatType))))],Block([]))]),ClassDecl(Id(_),[]),ClassDecl(Id(D),Id(wB1_S2h197),[MethodDecl(Id(Destructor),Instance,[],Block([]))])])'''
        self.assertTrue(TestAST.test(line, expect, 29))

    def test_30(self):
        line = '''Class l0_{$5_0(_2:Float ;v:Array [String ,0117];__G_:Array [Boolean ,0117];y1Q_,X_N:Array [Float ,0B1010000]){}Constructor (Y,v,__:Int ){} }Class _:J_a0{}Class _16{$_(){}$A(V___9148R2N,_,W,_:Array [Array [Array [Array [Int ,64],0B1010000],0x1D],0x1D]){} }Class _:U_y{}Class q:I{}'''
        expect = '''Program([ClassDecl(Id(l0_),[MethodDecl(Id($5_0),Static,[param(Id(_2),FloatType),param(Id(v),ArrayType(79,StringType)),param(Id(__G_),ArrayType(79,BoolType)),param(Id(y1Q_),ArrayType(80,FloatType)),param(Id(X_N),ArrayType(80,FloatType))],Block([])),MethodDecl(Id(Constructor),Instance,[param(Id(Y),IntType),param(Id(v),IntType),param(Id(__),IntType)],Block([]))]),ClassDecl(Id(_),Id(J_a0),[]),ClassDecl(Id(_16),[MethodDecl(Id($_),Static,[],Block([])),MethodDecl(Id($A),Static,[param(Id(V___9148R2N),ArrayType(29,ArrayType(29,ArrayType(80,ArrayType(64,IntType))))),param(Id(_),ArrayType(29,ArrayType(29,ArrayType(80,ArrayType(64,IntType))))),param(Id(W),ArrayType(29,ArrayType(29,ArrayType(80,ArrayType(64,IntType))))),param(Id(_),ArrayType(29,ArrayType(29,ArrayType(80,ArrayType(64,IntType)))))],Block([]))]),ClassDecl(Id(_),Id(U_y),[]),ClassDecl(Id(q),Id(I),[])])'''
        self.assertTrue(TestAST.test(line, expect, 30))

    def test_31(self):
        line = '''Class k:_{Destructor (){} }Class C8{}Class g:_{}Class D{Destructor (){Val j6k:String ;}g0(_,i:Array [Array [Array [Int ,0X8B],34_35_9],0B111101];Q:Array [Int ,0X18];x:Float ){} }'''
        expect = '''Program([ClassDecl(Id(k),Id(_),[MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(C8),[]),ClassDecl(Id(g),Id(_),[]),ClassDecl(Id(D),[MethodDecl(Id(Destructor),Instance,[],Block([ConstDecl(Id(j6k),StringType,None)])),MethodDecl(Id(g0),Instance,[param(Id(_),ArrayType(61,ArrayType(34359,ArrayType(139,IntType)))),param(Id(i),ArrayType(61,ArrayType(34359,ArrayType(139,IntType)))),param(Id(Q),ArrayType(24,IntType)),param(Id(x),FloatType)],Block([]))])])'''
        self.assertTrue(TestAST.test(line, expect, 31))

    def test_32(self):
        line = '''Class OU_O:k_{Destructor (){} }Class t:_{Constructor (S6q,C_,h0:Array [Array [Array [Array [Array [Float ,0b10],0xE_5],0B1],0b10],15]){Return ;Break ;}Constructor (){} }'''
        expect = '''Program([ClassDecl(Id(OU_O),Id(k_),[MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(t),Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(S6q),ArrayType(15,ArrayType(2,ArrayType(1,ArrayType(229,ArrayType(2,FloatType)))))),param(Id(C_),ArrayType(15,ArrayType(2,ArrayType(1,ArrayType(229,ArrayType(2,FloatType)))))),param(Id(h0),ArrayType(15,ArrayType(2,ArrayType(1,ArrayType(229,ArrayType(2,FloatType))))))],Block([Return(),Break])),MethodDecl(Id(Constructor),Instance,[],Block([]))])])'''
        self.assertTrue(TestAST.test(line, expect, 32))

    def test_33(self):
        line = '''Class X{Val $_,$9,___,__:Array [Array [Boolean ,1_76],03];}Class __:_8_{}Class _{Constructor (_,__C,x,x:Float ;h6_o3,_7__7,__,_8,vI_,v_Z:Boolean ;w9_9:Boolean ;O_w:String ;_,kv:String ){} }'''
        expect = '''Program([ClassDecl(Id(X),[AttributeDecl(Static,ConstDecl(Id($_),ArrayType(3,ArrayType(176,BoolType)),None)),AttributeDecl(Static,ConstDecl(Id($9),ArrayType(3,ArrayType(176,BoolType)),None)),AttributeDecl(Instance,ConstDecl(Id(___),ArrayType(3,ArrayType(176,BoolType)),None)),AttributeDecl(Instance,ConstDecl(Id(__),ArrayType(3,ArrayType(176,BoolType)),None))]),ClassDecl(Id(__),Id(_8_),[]),ClassDecl(Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(_),FloatType),param(Id(__C),FloatType),param(Id(x),FloatType),param(Id(x),FloatType),param(Id(h6_o3),BoolType),param(Id(_7__7),BoolType),param(Id(__),BoolType),param(Id(_8),BoolType),param(Id(vI_),BoolType),param(Id(v_Z),BoolType),param(Id(w9_9),BoolType),param(Id(O_w),StringType),param(Id(_),StringType),param(Id(kv),StringType)],Block([]))])])'''
        self.assertTrue(TestAST.test(line, expect, 33))

    def test_34(self):
        line = '''Class _5CM:_S7_{Constructor (h,_:Array [Array [Float ,0XA_B],68];d:rRp__;_:_;P3_,_:Array [Array [Array [Int ,68],0x79],07]){} }Class _X9_t:_{Var $m1_:R47;Destructor (){} }'''
        expect = '''Program([ClassDecl(Id(_5CM),Id(_S7_),[MethodDecl(Id(Constructor),Instance,[param(Id(h),ArrayType(68,ArrayType(171,FloatType))),param(Id(_),ArrayType(68,ArrayType(171,FloatType))),param(Id(d),ClassType(Id(rRp__))),param(Id(_),ClassType(Id(_))),param(Id(P3_),ArrayType(7,ArrayType(121,ArrayType(68,IntType)))),param(Id(_),ArrayType(7,ArrayType(121,ArrayType(68,IntType))))],Block([]))]),ClassDecl(Id(_X9_t),Id(_),[AttributeDecl(Static,VarDecl(Id($m1_),ClassType(Id(R47)),NullLiteral())),MethodDecl(Id(Destructor),Instance,[],Block([]))])])'''
        self.assertTrue(TestAST.test(line, expect, 34))

    def test_35(self):
        line = '''Class d9{Constructor (_:Array [Boolean ,0x99];B,_:Boolean ;n:Array [Array [Array [Array [Array [Array [String ,0b11],04],015],0b1_1],01_2],1];P:Array [String ,0B10]){}V(W8Y:Array [Boolean ,0b1];M5:Array [String ,01140_3]){Continue ;Continue ;}Destructor (){Continue ;} }Class c_:L{}Class W0_:_p{}'''
        expect = '''Program([ClassDecl(Id(d9),[MethodDecl(Id(Constructor),Instance,[param(Id(_),ArrayType(153,BoolType)),param(Id(B),BoolType),param(Id(_),BoolType),param(Id(n),ArrayType(1,ArrayType(10,ArrayType(3,ArrayType(13,ArrayType(4,ArrayType(3,StringType))))))),param(Id(P),ArrayType(2,StringType))],Block([])),MethodDecl(Id(V),Instance,[param(Id(W8Y),ArrayType(1,BoolType)),param(Id(M5),ArrayType(4867,StringType))],Block([Continue,Continue])),MethodDecl(Id(Destructor),Instance,[],Block([Continue]))]),ClassDecl(Id(c_),Id(L),[]),ClassDecl(Id(W0_),Id(_p),[])])'''
        self.assertTrue(TestAST.test(line, expect, 35))

    def test_36(self):
        line = '''Class _2__{Var $1x,K,$3,ed,E_:Boolean ;}Class _91_:_3_{}Class k4P0_0_{Constructor (_m00,_G5:Int ){Val _R:Array [Array [Array [Boolean ,0X5],0b10111],0126];Continue ;Var _,A,_:Int ;} }'''
        expect = '''Program([ClassDecl(Id(_2__),[AttributeDecl(Static,VarDecl(Id($1x),BoolType)),AttributeDecl(Instance,VarDecl(Id(K),BoolType)),AttributeDecl(Static,VarDecl(Id($3),BoolType)),AttributeDecl(Instance,VarDecl(Id(ed),BoolType)),AttributeDecl(Instance,VarDecl(Id(E_),BoolType))]),ClassDecl(Id(_91_),Id(_3_),[]),ClassDecl(Id(k4P0_0_),[MethodDecl(Id(Constructor),Instance,[param(Id(_m00),IntType),param(Id(_G5),IntType)],Block([ConstDecl(Id(_R),ArrayType(86,ArrayType(23,ArrayType(5,BoolType))),None),Continue,VarDecl(Id(_),IntType),VarDecl(Id(A),IntType),VarDecl(Id(_),IntType)]))])])'''
        self.assertTrue(TestAST.test(line, expect, 36))

    def test_37(self):
        line = '''Class _0P{Constructor (L,qW,_H,_1Xd,y,j6cC:Array [Array [Int ,5_0_19_1],0B1_00]){}u65(i_,_I:_;_,r:Array [Float ,0b1];_c,q8:Float ;A:String ;_:Array [String ,0x5];Y:String ;dCz_j,D,_,q,F_rI0s:Ed3;RHX,_:G_){}d(a,_B,Y3:Float ;e,o,p,xT___0DV:Array [Array [Array [Float ,0xEA_B],0B1],0b111_0]){} }Class _{$_4(){}$P(r_,_,_:Boolean ){ {} }}'''
        expect = '''Program([ClassDecl(Id(_0P),[MethodDecl(Id(Constructor),Instance,[param(Id(L),ArrayType(4,ArrayType(50191,IntType))),param(Id(qW),ArrayType(4,ArrayType(50191,IntType))),param(Id(_H),ArrayType(4,ArrayType(50191,IntType))),param(Id(_1Xd),ArrayType(4,ArrayType(50191,IntType))),param(Id(y),ArrayType(4,ArrayType(50191,IntType))),param(Id(j6cC),ArrayType(4,ArrayType(50191,IntType)))],Block([])),MethodDecl(Id(u65),Instance,[param(Id(i_),ClassType(Id(_))),param(Id(_I),ClassType(Id(_))),param(Id(_),ArrayType(1,FloatType)),param(Id(r),ArrayType(1,FloatType)),param(Id(_c),FloatType),param(Id(q8),FloatType),param(Id(A),StringType),param(Id(_),ArrayType(5,StringType)),param(Id(Y),StringType),param(Id(dCz_j),ClassType(Id(Ed3))),param(Id(D),ClassType(Id(Ed3))),param(Id(_),ClassType(Id(Ed3))),param(Id(q),ClassType(Id(Ed3))),param(Id(F_rI0s),ClassType(Id(Ed3))),param(Id(RHX),ClassType(Id(G_))),param(Id(_),ClassType(Id(G_)))],Block([])),MethodDecl(Id(d),Instance,[param(Id(a),FloatType),param(Id(_B),FloatType),param(Id(Y3),FloatType),param(Id(e),ArrayType(14,ArrayType(1,ArrayType(3755,FloatType)))),param(Id(o),ArrayType(14,ArrayType(1,ArrayType(3755,FloatType)))),param(Id(p),ArrayType(14,ArrayType(1,ArrayType(3755,FloatType)))),param(Id(xT___0DV),ArrayType(14,ArrayType(1,ArrayType(3755,FloatType))))],Block([]))]),ClassDecl(Id(_),[MethodDecl(Id($_4),Static,[],Block([])),MethodDecl(Id($P),Static,[param(Id(r_),BoolType),param(Id(_),BoolType),param(Id(_),BoolType)],Block([Block([])]))])])'''
        self.assertTrue(TestAST.test(line, expect, 37))

    def test_38(self):
        line = '''Class a_G{Val _,Qvs,_,_n:Array [Array [Array [Int ,0b10101],0B1000111],0XB];}Class __6{Val a,D:Array [Boolean ,49_73_6];Val $5:Boolean ;}Class g45k:V{}Class _y____:X{Destructor (){ {} }}'''
        expect = '''Program([ClassDecl(Id(a_G),[AttributeDecl(Instance,ConstDecl(Id(_),ArrayType(11,ArrayType(71,ArrayType(21,IntType))),None)),AttributeDecl(Instance,ConstDecl(Id(Qvs),ArrayType(11,ArrayType(71,ArrayType(21,IntType))),None)),AttributeDecl(Instance,ConstDecl(Id(_),ArrayType(11,ArrayType(71,ArrayType(21,IntType))),None)),AttributeDecl(Instance,ConstDecl(Id(_n),ArrayType(11,ArrayType(71,ArrayType(21,IntType))),None))]),ClassDecl(Id(__6),[AttributeDecl(Instance,ConstDecl(Id(a),ArrayType(49736,BoolType),None)),AttributeDecl(Instance,ConstDecl(Id(D),ArrayType(49736,BoolType),None)),AttributeDecl(Static,ConstDecl(Id($5),BoolType,None))]),ClassDecl(Id(g45k),Id(V),[]),ClassDecl(Id(_y____),Id(X),[MethodDecl(Id(Destructor),Instance,[],Block([Block([])]))])])'''
        self.assertTrue(TestAST.test(line, expect, 38))

    def test_39(self):
        line = '''Class _6T:D9{_(NY_:Array [Array [String ,0111],0b1_1];K__k__,___Nc_lO:Array [Float ,0x36_12];ff:_8;_n:Array [Array [Array [Array [Int ,0b1000001],0X6_6_7],0x14],03]){ {}Var _,K7:Array [Array [Array [String ,0b110_1],0xF],0XA];} }Class sX7_qn___Y2o97:D{}Class _{}Class X2_:__{Var M__,$__p:Array [Boolean ,0b1111];}'''
        expect = '''Program([ClassDecl(Id(_6T),Id(D9),[MethodDecl(Id(_),Instance,[param(Id(NY_),ArrayType(3,ArrayType(73,StringType))),param(Id(K__k__),ArrayType(13842,FloatType)),param(Id(___Nc_lO),ArrayType(13842,FloatType)),param(Id(ff),ClassType(Id(_8))),param(Id(_n),ArrayType(3,ArrayType(20,ArrayType(1639,ArrayType(65,IntType)))))],Block([Block([]),VarDecl(Id(_),ArrayType(10,ArrayType(15,ArrayType(13,StringType)))),VarDecl(Id(K7),ArrayType(10,ArrayType(15,ArrayType(13,StringType))))]))]),ClassDecl(Id(sX7_qn___Y2o97),Id(D),[]),ClassDecl(Id(_),[]),ClassDecl(Id(X2_),Id(__),[AttributeDecl(Instance,VarDecl(Id(M__),ArrayType(15,BoolType))),AttributeDecl(Static,VarDecl(Id($__p),ArrayType(15,BoolType)))])])'''
        self.assertTrue(TestAST.test(line, expect, 39))

    def test_40(self):
        line = '''Class n0I:__{Constructor (){}Constructor (){Return ;} }Class _:D_{Destructor (){} }Class w2506D:T{Constructor (C6,h,_D,_1:___;Q,o,_5iT,r,U:_17){} }Class u9:t08{$8_0_(__:_5){} }'''
        expect = '''Program([ClassDecl(Id(n0I),Id(__),[MethodDecl(Id(Constructor),Instance,[],Block([])),MethodDecl(Id(Constructor),Instance,[],Block([Return()]))]),ClassDecl(Id(_),Id(D_),[MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(w2506D),Id(T),[MethodDecl(Id(Constructor),Instance,[param(Id(C6),ClassType(Id(___))),param(Id(h),ClassType(Id(___))),param(Id(_D),ClassType(Id(___))),param(Id(_1),ClassType(Id(___))),param(Id(Q),ClassType(Id(_17))),param(Id(o),ClassType(Id(_17))),param(Id(_5iT),ClassType(Id(_17))),param(Id(r),ClassType(Id(_17))),param(Id(U),ClassType(Id(_17)))],Block([]))]),ClassDecl(Id(u9),Id(t08),[MethodDecl(Id($8_0_),Static,[param(Id(__),ClassType(Id(_5)))],Block([]))])])'''
        self.assertTrue(TestAST.test(line, expect, 40))

    def test_41(self):
        line = '''Class n:_f{}Class ___:e_{Constructor (m,J,J_,_,_bzF,__:Array [Array [Array [Array [String ,027],9],06],027];_:Array [Array [Array [Int ,04],78],0X48];i,_,F:_;_6_L:w;u_:__vn0;_ak:_;_:Array [Array [Array [Array [Int ,0B101111],4],07_4],0B11]){} }'''
        expect = '''Program([ClassDecl(Id(n),Id(_f),[]),ClassDecl(Id(___),Id(e_),[MethodDecl(Id(Constructor),Instance,[param(Id(m),ArrayType(23,ArrayType(6,ArrayType(9,ArrayType(23,StringType))))),param(Id(J),ArrayType(23,ArrayType(6,ArrayType(9,ArrayType(23,StringType))))),param(Id(J_),ArrayType(23,ArrayType(6,ArrayType(9,ArrayType(23,StringType))))),param(Id(_),ArrayType(23,ArrayType(6,ArrayType(9,ArrayType(23,StringType))))),param(Id(_bzF),ArrayType(23,ArrayType(6,ArrayType(9,ArrayType(23,StringType))))),param(Id(__),ArrayType(23,ArrayType(6,ArrayType(9,ArrayType(23,StringType))))),param(Id(_),ArrayType(72,ArrayType(78,ArrayType(4,IntType)))),param(Id(i),ClassType(Id(_))),param(Id(_),ClassType(Id(_))),param(Id(F),ClassType(Id(_))),param(Id(_6_L),ClassType(Id(w))),param(Id(u_),ClassType(Id(__vn0))),param(Id(_ak),ClassType(Id(_))),param(Id(_),ArrayType(3,ArrayType(60,ArrayType(4,ArrayType(47,IntType)))))],Block([]))])])'''
        self.assertTrue(TestAST.test(line, expect, 41))

    def test_42(self):
        line = '''Class _:FP{Destructor (){ {} }Constructor (_,Vj:String ;_b,_,t:__929_;_,w0_,_,_,i0,_,_:String ;_,TD,b3_,_6,N_:Int ){}Var $3j:Array [String ,0B11110];Destructor (){}y(_,_,_P_,u:Float ){} }'''
        expect = '''Program([ClassDecl(Id(_),Id(FP),[MethodDecl(Id(Destructor),Instance,[],Block([Block([])])),MethodDecl(Id(Constructor),Instance,[param(Id(_),StringType),param(Id(Vj),StringType),param(Id(_b),ClassType(Id(__929_))),param(Id(_),ClassType(Id(__929_))),param(Id(t),ClassType(Id(__929_))),param(Id(_),StringType),param(Id(w0_),StringType),param(Id(_),StringType),param(Id(_),StringType),param(Id(i0),StringType),param(Id(_),StringType),param(Id(_),StringType),param(Id(_),IntType),param(Id(TD),IntType),param(Id(b3_),IntType),param(Id(_6),IntType),param(Id(N_),IntType)],Block([])),AttributeDecl(Static,VarDecl(Id($3j),ArrayType(30,StringType))),MethodDecl(Id(Destructor),Instance,[],Block([])),MethodDecl(Id(y),Instance,[param(Id(_),FloatType),param(Id(_),FloatType),param(Id(_P_),FloatType),param(Id(u),FloatType)],Block([]))])])'''
        self.assertTrue(TestAST.test(line, expect, 42))

    def test_43(self):
        line = '''Class Uk:R441{Constructor (b162:yU;d:Array [Array [Array [Array [Array [Boolean ,0B1],0xB],03_4],5],0x9];o:Array [Array [Array [Array [Array [Array [Boolean ,4_561],0B1100],024],0X51],0B1],024];_:Array [Array [Array [Boolean ,5],0B1000100],0B1000100]){Return ;}_(){Continue ;}_4(_0_,pcL,f:Array [Array [Array [Array [Array [Array [Int ,0x61],0x61],0xB],0B1_0],0B111],0b111];F,_8:Int ;_,i:Float ){Val s4:_7;} }Class J:_3_{}'''
        expect = '''Program([ClassDecl(Id(Uk),Id(R441),[MethodDecl(Id(Constructor),Instance,[param(Id(b162),ClassType(Id(yU))),param(Id(d),ArrayType(9,ArrayType(5,ArrayType(28,ArrayType(11,ArrayType(1,BoolType)))))),param(Id(o),ArrayType(20,ArrayType(1,ArrayType(81,ArrayType(20,ArrayType(12,ArrayType(4561,BoolType))))))),param(Id(_),ArrayType(68,ArrayType(68,ArrayType(5,BoolType))))],Block([Return()])),MethodDecl(Id(_),Instance,[],Block([Continue])),MethodDecl(Id(_4),Instance,[param(Id(_0_),ArrayType(7,ArrayType(7,ArrayType(2,ArrayType(11,ArrayType(97,ArrayType(97,IntType))))))),param(Id(pcL),ArrayType(7,ArrayType(7,ArrayType(2,ArrayType(11,ArrayType(97,ArrayType(97,IntType))))))),param(Id(f),ArrayType(7,ArrayType(7,ArrayType(2,ArrayType(11,ArrayType(97,ArrayType(97,IntType))))))),param(Id(F),IntType),param(Id(_8),IntType),param(Id(_),FloatType),param(Id(i),FloatType)],Block([ConstDecl(Id(s4),ClassType(Id(_7)),NullLiteral())]))]),ClassDecl(Id(J),Id(_3_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 43))

    def test_44(self):
        line = '''Class o{}Class _Q{Constructor (){t_::$_.Q_()._();} }Class E6{$_x(a,E_,_,_BQ1,K0:Array [Array [Int ,90],0b11001];_,oiI:Array [Array [Array [Float ,030],8],0b11001];c_,_,o,__:Boolean ){} }'''
        expect = '''Program([ClassDecl(Id(o),[]),ClassDecl(Id(_Q),[MethodDecl(Id(Constructor),Instance,[],Block([Call(CallExpr(FieldAccess(Id(t_),Id($_)),Id(Q_),[]),Id(_),[])]))]),ClassDecl(Id(E6),[MethodDecl(Id($_x),Static,[param(Id(a),ArrayType(25,ArrayType(90,IntType))),param(Id(E_),ArrayType(25,ArrayType(90,IntType))),param(Id(_),ArrayType(25,ArrayType(90,IntType))),param(Id(_BQ1),ArrayType(25,ArrayType(90,IntType))),param(Id(K0),ArrayType(25,ArrayType(90,IntType))),param(Id(_),ArrayType(25,ArrayType(8,ArrayType(24,FloatType)))),param(Id(oiI),ArrayType(25,ArrayType(8,ArrayType(24,FloatType)))),param(Id(c_),BoolType),param(Id(_),BoolType),param(Id(o),BoolType),param(Id(__),BoolType)],Block([]))])])'''
        self.assertTrue(TestAST.test(line, expect, 44))

    def test_45(self):
        line = '''Class _00:_{Constructor (_:Int ;_0,_,x1,_,v,_Y,T092:Float ;g_,_,v,_N:Array [Array [String ,0b1000010],0B1100001]){} }Class q8__{}Class _:_{Destructor (){Break ;}Val w_:Float ;}Class Q91_:_J99{Var Z,__,ESV_:_;}'''
        expect = '''Program([ClassDecl(Id(_00),Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(_),IntType),param(Id(_0),FloatType),param(Id(_),FloatType),param(Id(x1),FloatType),param(Id(_),FloatType),param(Id(v),FloatType),param(Id(_Y),FloatType),param(Id(T092),FloatType),param(Id(g_),ArrayType(97,ArrayType(66,StringType))),param(Id(_),ArrayType(97,ArrayType(66,StringType))),param(Id(v),ArrayType(97,ArrayType(66,StringType))),param(Id(_N),ArrayType(97,ArrayType(66,StringType)))],Block([]))]),ClassDecl(Id(q8__),[]),ClassDecl(Id(_),Id(_),[MethodDecl(Id(Destructor),Instance,[],Block([Break])),AttributeDecl(Instance,ConstDecl(Id(w_),FloatType,None))]),ClassDecl(Id(Q91_),Id(_J99),[AttributeDecl(Instance,VarDecl(Id(Z),ClassType(Id(_)),NullLiteral())),AttributeDecl(Instance,VarDecl(Id(__),ClassType(Id(_)),NullLiteral())),AttributeDecl(Instance,VarDecl(Id(ESV_),ClassType(Id(_)),NullLiteral()))])])'''
        self.assertTrue(TestAST.test(line, expect, 45))

    def test_46(self):
        line = '''Class h:_q{}Class _:y{Constructor (){}Var $_7_9:Float ;}Class __9{_(){Continue ;}Constructor (_:Array [Array [Array [Array [Array [Float ,0XD],0b1_0],5],01],0b1001001]){ {} }Var KH:Array [Array [Array [Array [Boolean ,6],073],6],8];}'''
        expect = '''Program([ClassDecl(Id(h),Id(_q),[]),ClassDecl(Id(_),Id(y),[MethodDecl(Id(Constructor),Instance,[],Block([])),AttributeDecl(Static,VarDecl(Id($_7_9),FloatType))]),ClassDecl(Id(__9),[MethodDecl(Id(_),Instance,[],Block([Continue])),MethodDecl(Id(Constructor),Instance,[param(Id(_),ArrayType(73,ArrayType(1,ArrayType(5,ArrayType(2,ArrayType(13,FloatType))))))],Block([Block([])])),AttributeDecl(Instance,VarDecl(Id(KH),ArrayType(8,ArrayType(6,ArrayType(59,ArrayType(6,BoolType))))))])])'''
        self.assertTrue(TestAST.test(line, expect, 46))

    def test_47(self):
        line = '''Class ____2_:_{}Class b8:Z092v{Constructor (_Z:Array [Array [Array [Int ,0B11],8],0b111100]){}v(___z:__;_N1:Int ;_:Array [Array [Int ,02_4],0b111100]){} }Class O{}Class ____:_{}'''
        expect = '''Program([ClassDecl(Id(____2_),Id(_),[]),ClassDecl(Id(b8),Id(Z092v),[MethodDecl(Id(Constructor),Instance,[param(Id(_Z),ArrayType(60,ArrayType(8,ArrayType(3,IntType))))],Block([])),MethodDecl(Id(v),Instance,[param(Id(___z),ClassType(Id(__))),param(Id(_N1),IntType),param(Id(_),ArrayType(60,ArrayType(20,IntType)))],Block([]))]),ClassDecl(Id(O),[]),ClassDecl(Id(____),Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 47))

    def test_48(self):
        line = '''Class G_{Val Lg,$8T:Boolean ;}Class I_6{}Class _:S{Val $9__3,$0:Array [Array [Boolean ,38],0100];Constructor (____1,_:Boolean ){Continue ;Continue ;}Var _,w,u:_;Val $_g,_w:Array [Array [Array [Array [String ,0X31_AFE_6],0B110100],4],023];$_(s:Int ){Continue ;}Val _:Array [Boolean ,0b1];}Class _O2_{}Class A:__C_379849{Destructor (){}Val p:Int ;Val j,$l0z,w,$A,$d,_:Array [Float ,0512_0];}'''
        expect = '''Program([ClassDecl(Id(G_),[AttributeDecl(Instance,ConstDecl(Id(Lg),BoolType,None)),AttributeDecl(Static,ConstDecl(Id($8T),BoolType,None))]),ClassDecl(Id(I_6),[]),ClassDecl(Id(_),Id(S),[AttributeDecl(Static,ConstDecl(Id($9__3),ArrayType(64,ArrayType(38,BoolType)),None)),AttributeDecl(Static,ConstDecl(Id($0),ArrayType(64,ArrayType(38,BoolType)),None)),MethodDecl(Id(Constructor),Instance,[param(Id(____1),BoolType),param(Id(_),BoolType)],Block([Continue,Continue])),AttributeDecl(Instance,VarDecl(Id(_),ClassType(Id(_)),NullLiteral())),AttributeDecl(Instance,VarDecl(Id(w),ClassType(Id(_)),NullLiteral())),AttributeDecl(Instance,VarDecl(Id(u),ClassType(Id(_)),NullLiteral())),AttributeDecl(Static,ConstDecl(Id($_g),ArrayType(19,ArrayType(4,ArrayType(52,ArrayType(3256294,StringType)))),None)),AttributeDecl(Instance,ConstDecl(Id(_w),ArrayType(19,ArrayType(4,ArrayType(52,ArrayType(3256294,StringType)))),None)),MethodDecl(Id($_),Static,[param(Id(s),IntType)],Block([Continue])),AttributeDecl(Instance,ConstDecl(Id(_),ArrayType(1,BoolType),None))]),ClassDecl(Id(_O2_),[]),ClassDecl(Id(A),Id(__C_379849),[MethodDecl(Id(Destructor),Instance,[],Block([])),AttributeDecl(Instance,ConstDecl(Id(p),IntType,None)),AttributeDecl(Instance,ConstDecl(Id(j),ArrayType(2640,FloatType),None)),AttributeDecl(Static,ConstDecl(Id($l0z),ArrayType(2640,FloatType),None)),AttributeDecl(Instance,ConstDecl(Id(w),ArrayType(2640,FloatType),None)),AttributeDecl(Static,ConstDecl(Id($A),ArrayType(2640,FloatType),None)),AttributeDecl(Static,ConstDecl(Id($d),ArrayType(2640,FloatType),None)),AttributeDecl(Instance,ConstDecl(Id(_),ArrayType(2640,FloatType),None))])])'''
        self.assertTrue(TestAST.test(line, expect, 48))

    def test_49(self):
        line = '''Class U{Constructor (UV:Int ;_:Boolean ;_,_,r__:Int ;__,P,urV5,Od:_;_,_:Boolean ;Y_6y,A,U8_,QN,_:Array [Array [Array [Int ,0b10111],0XE_1_9_F],0x8_5E];_,w:Array [Array [Array [Array [Array [Array [Array [String ,40],0x3A],012_52],3_2],021],0x6],40];S84x_,w:Boolean ){} }'''
        expect = '''Program([ClassDecl(Id(U),[MethodDecl(Id(Constructor),Instance,[param(Id(UV),IntType),param(Id(_),BoolType),param(Id(_),IntType),param(Id(_),IntType),param(Id(r__),IntType),param(Id(__),ClassType(Id(_))),param(Id(P),ClassType(Id(_))),param(Id(urV5),ClassType(Id(_))),param(Id(Od),ClassType(Id(_))),param(Id(_),BoolType),param(Id(_),BoolType),param(Id(Y_6y),ArrayType(2142,ArrayType(57759,ArrayType(23,IntType)))),param(Id(A),ArrayType(2142,ArrayType(57759,ArrayType(23,IntType)))),param(Id(U8_),ArrayType(2142,ArrayType(57759,ArrayType(23,IntType)))),param(Id(QN),ArrayType(2142,ArrayType(57759,ArrayType(23,IntType)))),param(Id(_),ArrayType(2142,ArrayType(57759,ArrayType(23,IntType)))),param(Id(_),ArrayType(40,ArrayType(6,ArrayType(17,ArrayType(32,ArrayType(682,ArrayType(58,ArrayType(40,StringType)))))))),param(Id(w),ArrayType(40,ArrayType(6,ArrayType(17,ArrayType(32,ArrayType(682,ArrayType(58,ArrayType(40,StringType)))))))),param(Id(S84x_),BoolType),param(Id(w),BoolType)],Block([]))])])'''
        self.assertTrue(TestAST.test(line, expect, 49))