import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_400(self):
        """Simple program: int main() {} """
        input = """
                    Class c{
                        Var a:Int;
                        Var b:Int;
                        Var c:Int;
                    }
                    Class a{
                    Var a:Int;
                    Var a:Int;
                    }
                    Class b{}
                    Class d{}"""
        expect = "Redeclared Attribute: a"
        self.assertTrue(TestChecker.test(input,expect,400))
    def test_401(self):
        """Simple program: int main() {} """
        input = """Class a{}
        Class a{}"""
        expect = "Redeclared Class: a"
        self.assertTrue(TestChecker.test(input,expect,401))
    def test_402(self):
        """Simple program: int main() {} """
        input = """Class a{
                    a(a:Int;a:String){}
                    }"""
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_403(self):
        """Simple program: int main() {} """
        input = """Class a{
    Var a:Int;
    a(){}
}"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_404(self):
        """Simple program: int main() {} """
        input = """Class a{
                    b(){
                        Var a:Int;
                        Var a:Int;
                    }
                    }"""
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_405(self):
        """Simple program: int main() {} """
        input = """Class a{
                    b(){
                        Val a:Int = 1;
                        Val a:Int = 1;
                    }
                    }"""
        expect = "Redeclared Constant: a"
        self.assertTrue(TestChecker.test(input,expect,405))

    def test_406(self):
        """Simple program: int main() {} """
        input = """Class a{
                    b(a:Int){
                        Val a:Int = 1;
                    }
                    }"""
        expect = "Redeclared Constant: a"
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_407(self):
        """Simple program: int main() {} """
        input = """Class a{
                    b(a:Int){
                        Var a:Int = 1;
                    }
                    }"""
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_408(self):
        """Simple program: int main() {} """
        input = """Class a{
                    b(){
                        Var a:Int = 1;
                        {
                            Var a:Int = 1;
                            Var b:Int = 1;
                            Var b:Int = 1;
                        }
                    }
                    }"""
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input,expect,408))

    def test_409(self):
        """Simple program: int main() {} """
        input = """Class a{
                    b(){
                        Var a:Int = 1;
                        {
                            Var a:Int = 1;
                            Var b:Int = 1;
                            Val b:Int = 1;
                        }
                    }
                    }"""
        expect = "Redeclared Constant: b"
        self.assertTrue(TestChecker.test(input,expect,409))
    def test_410(self):
        """Simple program: int main() {} """
        input = """Class a{
                    b(){
                        Var b:Int = 1;
                        Var c:Int = 1;
                        a=1;
                    }
                    }"""
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_411(self):
        """Simple program: int main() {} """
        input = """
                    Class B{}
                    Class A{
                    b(){
                        Var b:Int = 1;
                        Var c:A;
                        Var a:C;
                    }
                    }"""
        expect = "Undeclared Class: C"
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_412(self):
        """Simple program: int main() {} """
        input = """
                    Class B{
                        Var b:Int = 1;
                    }
                    Class A{
                    b(){
                        Var b:Int = 1;
                        Var c:B;
                        c.b = 1;
                        c.c = 1;
                    }
                    }"""
        expect = "Undeclared Attribute: c"
        self.assertTrue(TestChecker.test(input,expect,412))

    def test_413(self):
        """Simple program: int main() {} """
        input = """
                    Class B{
                        Var b:Int = 1;
                        c(){}
                    }
                    Class A{
                    b(){
                        Var b:Int = 1;
                        Var c:B;
                        c.b = 1;
                        c.c = 1;
                    }
                    }"""
        expect = "Undeclared Attribute: c"
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test_414(self):
        """Simple program: int main() {} """
        input = """
                    Class B{
                        Var b:Int = 1;
                        c(){}
                    }
                    Class A{
                    b(){
                        Var b:Int = 1;
                        Var c:B;
                        c.b = 1;
                        c.c();
                        c.d();
                    }
                    }"""
        expect = "Undeclared Method: d"
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test_415(self):
        """Simple program: int main() {} """
        input = """
                    Class B{
                        Var b:Int = 1;
                        c(){}
                    }
                    Class A:B{
                    }
                    Class C:D{
                    }"""
        expect = "Undeclared Class: D"
        self.assertTrue(TestChecker.test(input, expect, 415))


    def test_416(self):
        """Simple program: int main() {} """
        input = """
                        Class B{
                            Var b:Int = 1;
                            c(){}
                        }
                        Class A:B{
                        }
                        Class C{
                            e(){
                                Var a:A;
                                a.b = 2;
                                a.c();
                                a.e = 2;
                            }
                        }"""
        expect = "Undeclared Attribute: e"
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test_417(self):
        """Simple program: int main() {} """
        input = """ 
                        Class B{
                            Var b:Int = 1;
                            c(){}
                        }
                        Class A:B{
                        }
                        Class C{
                            e(){
                                Var a:A;
                                a.b= 2;
                                a.c();
                                a.e();
                            }
                        }"""
        expect = "Undeclared Method: e"
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test_418(self):
        """Simple program: int main() {} """
        input = """
                        Class C{
                            e(){
                                Val a:Int = 2;
                                a=3;
                            }
                        }"""
        expect = "Cannot Assign To Constant: AssignStmt(Id(a),IntLit(3))"
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test_419(self):
        """Simple program: int main() {} """
        input = """
                        Class C{
                            e(){
                                Var a:Int = 2;
                                Var b:Array[Int,5];
                                b[1]=1;
                                a[1]=1;
                            }
                        }"""
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),[IntLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test_420(self):
        """Simple program: int main() {} """
        input = """
                        Class C{
                            e(){
                                Var a:Int = 2;
                                Var b:Array[Int,5];
                                b[1.2]=1;
                            }
                        }"""
        expect = "Type Mismatch In Expression: ArrayCell(Id(b),[FloatLit(1.2)])"
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test_421(self):
        """Simple program: int main() {} """
        input = """
                        Class C{
                            e(){
                                Var a:Int = 1+2;
                                Var b:Float = 1+2.2;
                                Var c:Float = 1+True;
                            }
                        }"""
        expect = "Type Mismatch In Expression: BinaryOp(+,IntLit(1),BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test_422(self):
        """Simple program: int main() {} """
        input = """
                        Class C{
                            e(){
                                Var c:String = "abc" +. "def";
                                Var d:Boolean = ("abc" +. "def") ==. "ghi";
                                Var e:String = ("abc" ==. "def") +. "ghi";
                            }
                        }"""
        expect = "Type Mismatch In Expression: BinaryOp(+.,BinaryOp(==.,StringLit(abc),StringLit(def)),StringLit(ghi))"
        self.assertTrue(TestChecker.test(input, expect, 422))

    def test_423(self):
        """Simple program: int main() {} """
        input = """
                        Class C{
                            e(){
                                Var c:Float = 1.22;
                                Var d:Boolean = (("abc" +. "def") ==. "ghi") || False;
                                Var e:Boolean = 0==False;
                                Var f:Boolean = "abc"||1;
                            }
                        }"""
        expect = "Type Mismatch In Expression: BinaryOp(||,StringLit(abc),IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test_424(self):
        """Simple program: int main() {} """
        input = """
                        Class C{
                            e(){
                                Var c:Float = --------1.22;
                                Var d:Boolean = !((("abc" +. "def") ==. "ghi") || False);
                                Var e:Float = !!!!--1.22;
                            }
                        }"""
        expect = "Type Mismatch In Expression: UnaryOp(!,UnaryOp(-,UnaryOp(-,FloatLit(1.22))))"
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test_425(self):
        """Simple program: int main() {} """
        input = """
                        Class B{
                            Var b:Int = 1;
                            c(g:Int; h:Float){
                                Return 1;
                            }
                            d(){}
                        }
                        Class C{
                            e(){
                                Var a:B;
                                Var d:Int = a.c(1,2);
                                Var e:Int = a.c(1,"abc");
                            }
                        }"""
        expect = "Type Mismatch In Expression: CallExpr(Id(a),Id(c),[IntLit(1),StringLit(abc)])"
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test_426(self):
        """Simple program: int main() {} """
        input = """
                        Class B{
                            Var b:Int = 1;
                            c(g:Int; h:Float){
                                Return 1;
                            }
                            d(){}
                        }
                        Class C{
                            e(){
                                Var a:B;
                                Var d:Float = a.c(1,2);
                                Var e:String = a.c(1.1,2);
                            }
                        }"""
        expect = "Type Mismatch In Expression: CallExpr(Id(a),Id(c),[FloatLit(1.1),IntLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test_427(self):
        """Simple program: int main() {} """
        input = """
                        Class B{
                            Var b:Int = 1;
                            c(g:Int; h:Float){
                                Return 1;
                            }
                            d(){}
                        }
                        Class C{
                            e(){
                                Var a:B;
                                Var d:Float = a.c(1,2);
                                Var e:String = a.c(1.1,2);
                            }
                        }"""
        expect = "Type Mismatch In Expression: CallExpr(Id(a),Id(c),[FloatLit(1.1),IntLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test_428(self):
        """Simple program: int main() {} """
        input = """
                        Class B{
                            Var b:Int = 1;
                            c(g:Int; h:Float){
                                Return 1;
                            }
                            d(){}
                        }
                        Class C{
                            e(){
                                Var a:B;
                                Var d:Float = a.c(1,2);
                                Var e:String = a.c(1,2);
                            }
                        }"""
        expect = "Type Mismatch In Statement: VarDecl(Id(e),StringType,CallExpr(Id(a),Id(c),[IntLit(1),IntLit(2)]))"
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test_429(self):
        """Simple program: int main() {} """
        input = """
                        Class B{
                            Var b:Int = 1;
                            c(g:Int; h:Float){
                                Return 1;
                            }
                            d(){}
                        }
                        Class C{
                            e(){
                                Var a:B;
                                Var d:Float = a.c(1,2);
                                a.d();
                                Var e:String = a.d();
                            }
                        }"""
        expect = "Type Mismatch In Expression: CallExpr(Id(a),Id(d),[])"
        self.assertTrue(TestChecker.test(input, expect, 429))

    def test_430(self):
        """Simple program: int main() {} """
        input = """
                        Class B{
                            Var b:Int = 1;
                            c(g:Int; h:Float){
                                Return 1;
                            }
                            d(){}
                        }
                        Class C{
                            e(){
                                Var a:B;
                                Var d:Float = a.c(1,2);
                                a.d();
                                Var e:Float = a.b;
                                Var f:Float = a.d;
                            }
                        }"""
        expect = "Undeclared Attribute: d"
        self.assertTrue(TestChecker.test(input, expect, 430))

    def test_431(self):
        """Simple program: int main() {} """
        input = """
                        Class B{
                            Var b:Int = 1;
                            c(g:Int; h:Float){
                                Return 1;
                            }
                            d(){}
                        }
                        Class C{
                            e(){
                                Var a:B;
                                Var d:Float = a.c(1,2);
                                a.d();
                                Var e:Float = a.b;
                                Var f:String = a.b;
                            }
                        }"""
        expect = "Type Mismatch In Statement: VarDecl(Id(f),StringType,FieldAccess(Id(a),Id(b)))"
        self.assertTrue(TestChecker.test(input, expect, 431))

    def test_432(self):
        """Simple program: int main() {} """
        input = """
                        Class B{
                            Var b:Int = 1;
                            c(g:Int; h:Float){
                                Return 1;
                            }
                            d(){}
                        }
                        Class C{
                            e(){
                                Val a:B = New B();
                                Val d:Float = a.c(1,2);
                                Val e:String = a.c(1,2);
                            }
                        }"""
        expect = "Illegal Constant Expression: CallExpr(Id(a),Id(c),[IntLit(1),IntLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 432))
    def test_433(self):
        """Simple program: int main() {} """
        input = """
                        Class C{
                            e(){
                                Val a : Int = 1.2;
                            }
                        }"""
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(a),IntType,FloatLit(1.2))"
        self.assertTrue(TestChecker.test(input, expect, 433))

    def test_434(self):
        """Simple program: int main() {} """
        input = """
                        Class C{
                            e(){
                                Val a : Float = -(1.2 +1);
                                Val b : Float = -(1 + 1);
                                Val c : Boolean = !!((1>2)&&(True || ("abc"==."cef")));
                                Val d :String = ("abc" +. "def")+."ghi";
                                Val e :String = True==1;
                            }
                        }"""
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(e),StringType,BinaryOp(==,BooleanLit(True),IntLit(1)))"
        self.assertTrue(TestChecker.test(input, expect, 434))

    def test_435(self):
        """Simple program: int main() {} """
        input = """
                        Class B{
                            Var b:Int = 1;
                            c(g:Int; h:Float){
                                Return 1;
                            }
                            d(){}
                        }
                        Class C{
                            e(){
                                Val a:B = New B();
                                Val d:Float = a.c(1,2);
                                Val e:String = a.d(1,2);
                            }
                        }"""
        expect = "Illegal Constant Expression: CallExpr(Id(a),Id(c),[IntLit(1),IntLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 435))

    def test_436(self):
        """Simple program: int main() {} """
        input = """
                        Class B{
                            Var b:Int = 1;
                            c(g:Int; h:Float){
                                Return 1;
                            }
                            d(x:Int; y:Float; z:String){}
                        }
                        Class C{
                            e(){
                                Val a:B = New B();
                                Val d:Float = a.c(1,2);
                                a.d(1,2,"a");
                                a.d(1,2,3);
                            }
                        }"""
        expect = "Illegal Constant Expression: CallExpr(Id(a),Id(c),[IntLit(1),IntLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 436))

    def test_437(self):
        """Simple program: int main() {} """
        input = """
                        Class B{
                            Var b:Int = 1;
                            c(g:Int; h:Float){
                                Return 1;
                            }
                            d(x:Int; y:Float; z:String){}
                        }
                        Class C{
                            e(){
                                Val a:B = New B();
                                Val d:Float = a.c(1,2);
                                a.d(1+2,2--2.0,"a"+."bcd");
                                a.c(1,2);
                            }
                        }"""
        expect = "Illegal Constant Expression: CallExpr(Id(a),Id(c),[IntLit(1),IntLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 437))

    def test_438(self):
        """Simple program: int main() {} """
        input = """
                        Class B{
                            Var b:Int = 1;
                            c(g:Int; h:Float){
                                Return 1;
                            }
                            d(x:Int; y:Float; z:String){}
                        }
                        Class C{
                            e(){
                                Val a:B = New B();
                                Val d:Float = a.c(1,2);
                                a.d(1+2,2--2.0,"a"==."bcd");
                            }
                        }"""
        expect = "Illegal Constant Expression: CallExpr(Id(a),Id(c),[IntLit(1),IntLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 438))

    def test_439(self):
        """Simple program: int main() {} """
        input = """
                        Class B{
                            Var b:Int = 1;
                            c(g:Int; h:Float){
                                Return 1;
                            }
                            d(x:Int; y:Float; z:String){}
                        }
                        Class C{
                            e(){
                                Val a:B = New B();
                                Val d:Float = a.c(1,2);
                                a.d(1+2,2--2.0,("a"==."bcd")+1);
                            }
                        }"""
        expect = "Illegal Constant Expression: CallExpr(Id(a),Id(c),[IntLit(1),IntLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 439))

    def test_440(self):
        """Simple program: int main() {} """
        input = """
                        Class B{
                            Var b:Int = 1;
                            c(g:Int; h:Float){
                                Return 1;
                            }
                            d(x:Int; y:Float; z:String){}
                        }
                        Class A{}
                        Class C{
                            e(){
                                Var a:B = New B();
                                a = New A();
                            }
                        }"""
        expect = "Type Mismatch In Statement: AssignStmt(Id(a),NewExpr(Id(A),[]))"
        self.assertTrue(TestChecker.test(input, expect, 440))

    def test_441(self):
        """Simple program: int main() {} """
        input = """
                        Class B{
                            Var b:Int = 1;
                            c(g:Int; h:Float){
                                Return 1;
                            }
                            d(x:Int; y:Float; z:String){}
                        }
                        Class A:B{}
                        Class C{
                            e(){
                                Var x:B = New B();
                                x = New A();
                                Var y:A = New A();
                                y = New B();
                            }
                        }"""
        expect = "Type Mismatch In Statement: AssignStmt(Id(x),NewExpr(Id(A),[]))"
        self.assertTrue(TestChecker.test(input, expect, 441))

    def test_442(self):
        """Simple program: int main() {} """
        input = """
                        Class C{
                            e(){
                                Val a:Int = 1;
                                Val b:Float = 1;
                                Val c:Float = a+b;
                                Val d:Int = a+b;
                            }
                        }"""
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(d),IntType,BinaryOp(+,Id(a),Id(b)))"
        self.assertTrue(TestChecker.test(input, expect, 442))

    def test_443(self):
        """Simple program: int main() {} """
        input = """
                        Class C{
                            e(){
                                Var a:Int = 1;
                                Var b:Float = 1;
                                Var c:Float = a+b;
                                Var d:Int = a+b;
                            }
                        }"""
        expect = "Type Mismatch In Statement: VarDecl(Id(d),IntType,BinaryOp(+,Id(a),Id(b)))"
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test_444(self):
        """Simple program: int main() {} """
        input = """
                        Class C{
                            e(){
                                Var a:Int = 1;
                                Var b:Int = 1;
                                If (True){
                                    Var a:Int = 2;
                                }
                                Elseif(True){
                                    Var a:Int = 2;
                                }
                                Else{
                                    Var a:Int = 2;
                                }
                                Var b:Int = 2 ;
                            }
                        }"""
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input, expect, 444))

    def test_445(self):
        """Simple program: int main() {} """
        input = """
                        Class C{
                            e(){
                                Var a:Int = 1;
                                Var b:Int = 1;
                                Var i:Int = 0;
                                Foreach(i In 1 .. 10 By 1){
                                    Var a:Int = 1;
                                    Break;
                                    If (True){
                                        Var a:Int = 1;
                                        Continue;
                                    }
                                }
                                Var b:Int = 2 ;
                            }
                        }"""
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input, expect, 445))

    def test_446(self):
        """Simple program: int main() {} """
        input = """
                        Class C{
                            e(){
                                Var i:Int = 0;
                                Foreach(i In 1 .. 10 By 1){
                                    Var a:Int = 1;
                                    Break;
                                    If (True){
                                        Var a:Int = 1;
                                        Continue;
                                    }
                                }
                                Break;
                            }
                        }"""
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 446))

    def test_447(self):
        """Simple program: int main() {} """
        input = """
                        Class C{
                            e(){
                                Var i:Int = 0;
                                Foreach(i In 1 .. 10 By 1){
                                    Var a:Int = 1;
                                    Break;
                                    If (True){
                                        Var a:Int = 1;
                                        Continue;
                                    }
                                }
                                Continue;
                            }
                        }"""
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 447))

    def test_448(self):
        """Simple program: int main() {} """
        input = """
                        Class C{
                            e(){
                                Var a:Int = 0;
                                Val b:Int = 1;
                                Val c:Float = b+1;
                                Val d:Float = a+1;
                            }
                        }"""
        expect = "Illegal Constant Expression: BinaryOp(+,Id(a),IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 448))

    def test_449(self):
        """Simple program: int main() {} """
        input = """
                        Class C{
                            e(){
                                Var a:Int = 0;
                                Val b:Int = 1;
                                Val c:Float = b+1;
                                Val d:Float = a + "abc";
                            }
                        }"""
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(a),StringLit(abc))"
        self.assertTrue(TestChecker.test(input, expect, 449))

    def test_450(self):
        """Simple program: int main() {} """
        input = """
                        Class C{
                            e(){
                                Var a:Int = 0;
                                Val b:Int = 1;
                                Val c:Float = b+1;
                                Val d:Float = a + "abc";
                            }
                        }"""
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(a),StringLit(abc))"
        self.assertTrue(TestChecker.test(input, expect, 450))

    def test_451(self):
        """Simple program: int main() {} """
        input = """
                        Class C{
                            e(){
                                Var a:Int = 0;
                                Val b:Int = 1;
                                Val c:Float = b+1;
                            }
                        }
                         Class Car {
                            Var a : Int = 10;
                            foo() {
                                Var x : Int = Self.a;
                                Var y : Int = a;
                            }
                        }"""
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 451))

    def test_452(self):
        """Simple program: int main() {} """
        input = """
                         Class Car {
                            foo() {
                                Var a:Array[Int,2];
                                a = Array(1,2);
                                a = Array(1,2.3);
                            }
                        }"""
        expect = "Illegal Array Literal: [IntLit(1),FloatLit(2.3)]"
        self.assertTrue(TestChecker.test(input, expect, 452))

    def test_453(self):
        """Simple program: int main() {} """
        input = """         
                        Class B{
                        func(){
                            count.foo();
                        }
                        }"""
        expect = "Undeclared Identifier: count"
        self.assertTrue(TestChecker.test(input, expect, 453))

    def test_454(self):
        """Simple program: int main() {} """
        input = """
                        Class A{
                            Var $a:Int = 5;
                            Var b:Int = 4;
                        }         
                        Class B{
                        func(){
                            Var b:Int = A::$a;
                            b = count.foo();
                        }
                        }"""
        expect = "Undeclared Identifier: count"
        self.assertTrue(TestChecker.test(input, expect, 454))

    def test_455(self):
        """Simple program: int main() {} """
        input = """         
                        Class A{
                            Var $a:Int = 5;
                            Var b:Int = 4;
                        }         
                        Class B{
                        func(){
                            Var b:Int = A::$a;
                            b = A.b;
                        }
                        }"""
        expect = "Illegal Member Access: FieldAccess(Id(A),Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 455))

    def test_456(self):
        """Simple program: int main() {} """
        input = """         
                        Class A{
                            Var $a:Int = 5;
                            Var b:Int = 4;
                        }         
                        Class B{
                        func(){
                            Var b:A = New A();
                            Var c:Int = b.b;
                            Var d:Int = b::$a;
                        }
                        }"""
        expect = "Illegal Member Access: FieldAccess(Id(b),Id($a))"
        self.assertTrue(TestChecker.test(input, expect, 456))

    def test_457(self):
        """Simple program: int main() {} """
        input = """         
                        Class A{
                            $a(){}
                            b(){}
                        }         
                        Class B{
                        func(){
                            A::$a();
                            Var b:A = New A();
                            b.b();
                            b::$a();
                        }
                        }"""
        expect = "Illegal Member Access: Call(Id(b),Id($a),[])"
        self.assertTrue(TestChecker.test(input, expect, 457))

    def test_458(self):
        """Simple program: int main() {} """
        input = """         
                        Class A{
                            $a(){}
                            b(){}
                        }         
                        Class B{
                        func(){
                            A::$a();
                            Var b:A = New A();
                            b.b();
                            A.b();
                        }
                        }"""
        expect = "Illegal Member Access: Call(Id(A),Id(b),[])"
        self.assertTrue(TestChecker.test(input, expect, 458))

    def test_459(self):
        """Simple program: int main() {} """
        input = """         
                        Class A{
                            $a(){
                                Return 1;
                            }
                            b(){
                                Return 1;
                            }
                        }         
                        Class B{
                        func(){
                            Var b:A = New A();
                            Var c:Int = A::$a();
                            c = b.b();
                            c = A.b();
                        }
                        }"""
        expect = "Illegal Member Access: CallExpr(Id(A),Id(b),[])"
        self.assertTrue(TestChecker.test(input, expect, 459))

    def test_460(self):
        """Simple program: int main() {} """
        input = """         
                        Class A{
                            $a(){
                                Return 1;
                            }
                            b(){
                                Return 1;
                            }
                        }         
                        Class B{
                        func(){
                            Var b:A = New A();
                            Var c:Int = A::$a();
                            c = b.b();
                            c = b::$a();
                        }
                        }"""
        expect = "Illegal Member Access: CallExpr(Id(b),Id($a),[])"
        self.assertTrue(TestChecker.test(input, expect, 460))

    def test_461(self):
        """Simple program: int main() {} """
        input = """         
                        Class A{
                            $a(){
                                Return 1;
                            }
                            b(){
                                Return 1;
                            }
                        } """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 461))

    def test_462(self):
        """Simple program: int main() {} """
        input = """         
                        Class A{
                            $a(){
                                Return 1;
                            }
                            b(){
                                Return 1;
                            }
                        } 
                        Class Program{
                            c(){
                                Return 1;
                            }
                        }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 462))

    def test_463(self):
        """Simple program: int main() {} """
        input = """         
                        Class A{
                            $a(){
                                Return 1;
                            }
                            b(){
                                Return 1;
                            }
                        } 
                        Class Program{
                            $main(){
                                Return 1;
                            }
                        }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 463))

    def test_464(self):
        """Simple program: int main() {} """
        input = """         
                        Class A{
                            $a(){
                                Return 1;
                            }
                            b(){
                                Return 1;
                            }
                        } 
                        Class Program{
                            $main(a:Int){
                            }
                        }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 464))

    def test_465(self):
        """Simple program: int main() {} """
        input = """         
                        Class A{
                            $a(){
                                Return 1;
                            }
                            b(){
                                Return 1;
                            }
                        } 
                        Class Program{
                            main(){}
                        }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 465))

    def test_466(self):
        """Simple program: int main() {} """
        input = """         
                        Class A{
                            Var a:Int = 1;
                            foo(){
                                Var b:Int = Self.a;
                                Var c:Int = a;
                            }
                        } """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 466))

    def test_467(self):
        """Simple program: int main() {} """
        input = """         
                        Class A{
                        Val y:Int=10;
                        }
                        Class B{
                        Var x:A;
                        func (){
                            Val z:Int=Self.x.y;
                        }
                        } """
        expect = "Illegal Constant Expression: FieldAccess(FieldAccess(Self(),Id(x)),Id(y))"
        self.assertTrue(TestChecker.test(input, expect, 467))

    def test_468(self):
        """Simple program: int main() {} """
        input = """     
                        Class B{
                        Var x:Int = 1;
                        foo(){
                            Return 1;
                        }
                        func (){
                            Var a:Int = Self.x;
                            a = Self.foo();
                            Var b:String = Self.foo();
                        }
                        } """
        expect = "Type Mismatch In Statement: VarDecl(Id(b),StringType,CallExpr(Self(),Id(foo),[]))"
        self.assertTrue(TestChecker.test(input, expect, 468))

    def test_469(self):
        """Simple program: int main() {} """
        input = """     
                        Class B{
                        Var x:Int = 1;
                        foo(){
                            Return 1;
                        }
                        func (){
                            Var a:Int = Self.x;
                            a = Self.foo();
                            Var b:String = Self.foofoo();
                        }
                        } """
        expect = "Undeclared Method: foofoo"
        self.assertTrue(TestChecker.test(input, expect, 469))

    def test_470(self):
        """Simple program: int main() {} """
        input = """     
                        Class E {
                           func() {                        
                           }                        
                        }                        
                        Class Test{                        
                          test() {                        
                                Var e: E = New E();                        
                                Return e.func;                       
                          }                        
                        } """
        expect = "Undeclared Attribute: func"
        self.assertTrue(TestChecker.test(input, expect, 470))

    def test_471(self):
        """Simple program: int main() {} """
        input = """     
                        Class E {
                           func() {                        
                           } 
                           Constructor(a:Int){
                           }                       
                        }                        
                        Class Test{                        
                          Var e: E = New E(1);              
                          Var b: E = New E();                                
                        } """
        expect = "Type Mismatch In Expression: NewExpr(Id(E),[])"
        self.assertTrue(TestChecker.test(input, expect, 471))

    def test_472(self):
        """Simple program: int main() {} """
        input = """     
                        Class E {
                           func() {                        
                           } 
                           Constructor(a:Int){
                           }                       
                        }                        
                        Class Test{                        
                          Var e: E = New E(1);              
                          Val b: String = New E(1);                                
                        } """
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(b),StringType,NewExpr(Id(E),[IntLit(1)]))"
        self.assertTrue(TestChecker.test(input, expect, 472))

    def test_473(self):
        """Simple program: int main() {} """
        input = """     
                        Class E {
                           $func() {                        
                           } 
                           Constructor(a:Int){
                           }                       
                        }                        
                        Class Test{ 
                            cak(){                     
                                E::$func();   
                                E::$foo();                             
                            }
                        }"""
        expect = "Undeclared Method: $foo"
        self.assertTrue(TestChecker.test(input, expect, 473))

    def test_474(self):
        """Simple program: int main() {} """
        input = """     
                        Class E {
                           $func() { 
                                Return 1;                       
                           } 
                           Constructor(a:Int){
                           }                       
                        }                        
                        Class Test{ 
                            cak(){                     
                                Var a:Int = E::$func();   
                                Var b:Int = E::$foo();                             
                            }
                        }"""
        expect = "Undeclared Method: $foo"
        self.assertTrue(TestChecker.test(input, expect, 474))

    def test_475(self):
        """Simple program: int main() {} """
        input = """     
                        Class A {
                           Var a:Int = 1;                      
                        }                        
                        Class B{ 
                            Var b:A = New A(); 
                        }
                        Class C{
                            foo(){
                                Var c:B = New B();
                                Var e:Int = c.b.a;
                                Var f:Int = c.b.g;
                            }
                        }"""
        expect = "Undeclared Attribute: g"
        self.assertTrue(TestChecker.test(input, expect, 475))

    def test_476(self):
        """Simple program: int main() {} """
        input = """     
                        Class A {
                           Var a:Int = 1;                      
                        }                        
                        Class B{ 
                            Var b:A = New A(); 
                        }
                        Class C{
                            foo(){
                                Var c:B = New B();
                                Var e:Int = c.b.a;
                                Var f:Int = c.g.a;
                            }
                        }"""
        expect = "Undeclared Attribute: g"
        self.assertTrue(TestChecker.test(input, expect, 476))

    def test_477(self):
        """Simple program: int main() {} """
        input = """     
                        Class A {
                           Var a:Int = 1;                      
                        }                        
                        Class B{ 
                            Var $b:A = New A(); 
                        }
                        Class C{
                            foo(){
                                Var c:B = New B();
                                Var e:Int = B::$b.a;
                                Var f:Int = B::$b.g;
                            }
                        }"""
        expect = "Undeclared Attribute: g"
        self.assertTrue(TestChecker.test(input, expect, 477))

    def test_478(self):
        """Simple program: int main() {} """
        input = """     
                        Class A {
                           Var a:Int = 1;                      
                        }                        
                        Class B{ 
                            Var $b:A = New A(); 
                        }
                        Class C{
                            foo(){
                                Var c:B = New B();
                                Var e:Int = B::$b.a;
                                Var f:Int = B::$g.a;
                            }
                        }"""
        expect = "Undeclared Attribute: $g"
        self.assertTrue(TestChecker.test(input, expect, 478))

    def test_479(self):
        """Simple program: int main() {} """
        input = """     
                        Class A {
                           Var a:Int = 1;
                           foo(){
                                Return 1;
                           }                      
                        }                        
                        Class B{ 
                            Var b:A = New A();
                            foo(){
                                Return New A();
                            }
                        }
                        Class C{
                            foo(){
                                Var c:B = New B();
                                Var e:Int = c.b.a;
                                e = c.b.foo();
                                e = c.foo().a;
                                e = c.foo().foo();
                                Var f:Int = c.foo();
                            }
                        }"""
        expect = "Type Mismatch In Statement: VarDecl(Id(f),IntType,CallExpr(Id(c),Id(foo),[]))"
        self.assertTrue(TestChecker.test(input, expect, 478))

    def test_480(self):
        """Simple program: int main() {} """
        input = """     
                        Class A {
                           Var a:Int = 1;
                           foo(x:Float; y:String){
                           }                      
                        }                        
                        Class B{ 
                            Var b:A = New A();
                            foo(){
                                Return New A();
                            }
                        }
                        Class C{
                            foo(){
                                Var c:B = New B();
                                c.foo().foo(1,"a");
                                c.b.foo(1.2,"a");
                                c.b.foo(1,1.2);
                            }
                        }"""
        expect = "Type Mismatch In Statement: Call(FieldAccess(Id(c),Id(b)),Id(foo),[IntLit(1),FloatLit(1.2)])"
        self.assertTrue(TestChecker.test(input, expect, 480))

    def test_481(self):
        """Simple program: int main() {} """
        input = """     
                        Class A {
                           Var a:Int = 1;
                           fooExp(x:Float; y:String){
                                Return 1;
                           }  
                           fooCall(x:Float; y:String){}                    
                        }                        
                        Class B{ 
                            Var b:A = New A();
                            foo(){
                                Return New A();
                            }
                            foo2(){
                                Var e:Int = Self.b.a;
                                e = Self.b.fooExp(1, "a");
                                e = Self.foo().a;
                                e = Self.foo().fooExp(1, "a");
                                Self.b.fooCall(1, "a");
                                Self.foo().fooCall(1, "a");
                                Self.g().fooCall(1, "a");
                            }
                        }"""
        expect = "Undeclared Method: g"
        self.assertTrue(TestChecker.test(input, expect, 481))

    def test_482(self):
        """Simple program: int main() {} """
        input = """     
                        Class A {
                           Var a:Int = 1;
                           fooExp(x:Float; y:String){
                                Return 1;
                           }  
                           fooCall(x:Float; y:String){}                    
                        }                        
                        Class B{ 
                            Var b:A = New A();
                            foo(){
                                Return New A();
                            }
                            foo2(){
                                Var e:Int = Self.b.a;
                                e = Self.b.fooExp(1, "a");
                                e = Self.foo().a;
                                e = Self.foo().fooExp(1, "a");
                                Self.b.fooCall(1, "a");
                                Self.foo().fooCall(1, "a");
                                Self.g().fooCall(1, "a");
                            }
                        }"""
        expect = "Undeclared Method: g"
        self.assertTrue(TestChecker.test(input, expect, 482))

    def test_483(self):
        """Simple program: int main() {} """
        input = """     
                        Class A {
                           Var a:Int = 1;
                           $fooExp1(x:Float; y:String){
                                Return Self.a;
                           } 
                           $fooExp2(x:Float; y:String){
                                Return x;
                           }  
                           $fooExp3(x:Float; y:String){
                                Return y;
                           }               
                        }                        
                        Class B{
                            foo2(){
                                Var e:Float = (New A()).a;
                                e = A::$fooExp1(1, "a");
                                e = A::$fooExp2(1, "a");
                                Var f:String = A::$fooExp3(1, "a");
                                Var g:Float = A::$fooExp3(1, "a");
                            }
                        }"""
        expect = "Type Mismatch In Statement: VarDecl(Id(g),FloatType,CallExpr(Id(A),Id($fooExp3),[IntLit(1),StringLit(a)]))"
        self.assertTrue(TestChecker.test(input, expect, 483))

    def test_484(self):
        """Simple program: int main() {} """
        input = """     
                        Class A {
                           Var a:Int = 1;
                           $fooExp1(x:Float; y:String){
                                Return Self.a;
                           } 
                           $fooExp2(x:Float; y:String){
                                Return x;
                           }  
                           $fooExp3(x:Float; y:String){
                                Return y;
                           }               
                        }                        
                        Class BB{
                            foo2(){
                                Var e:Float = (New A()).a - 7;
                                e = A::$fooExp1(1, "a") +2 - -----5;
                                e = A::$fooExp2(1, "a") + 1;
                                Var f:String = A::$fooExp3(1, "a") +. "abc";
                                Var g:String = A::$fooExp3(1, "a") + 1;
                            }
                        }"""
        expect = "Type Mismatch In Expression: BinaryOp(+,CallExpr(Id(A),Id($fooExp3),[IntLit(1),StringLit(a)]),IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 484))

    def test_485(self):
        """Simple program: int main() {} """
        input = """     
                        Class A {
                           $fooExp1(x:Float; y:String){
                                Var a:Array[Int, 2] = Array(1,1);
                                a = Array(1,1,1);
                           }               
                        }"""
        expect = "Type Mismatch In Statement: AssignStmt(Id(a),[IntLit(1),IntLit(1),IntLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 485))

    def test_486(self):
        """Simple program: int main() {} """
        input = """     
                        Class A {
                           $fooExp1(x:Float; y:String){
                                Var a:Array[Int, 2] = Array(1,1);
                                a = Array("a", "b");
                           }               
                        }"""
        expect = "Type Mismatch In Statement: AssignStmt(Id(a),[StringLit(a),StringLit(b)])"
        self.assertTrue(TestChecker.test(input, expect, 486))

    def test_487(self):
        """Simple program: int main() {} """
        input = """     
                        Class A {
                           $fooExp1(x:Float; y:String){
                                Var a: Array[Array[Int, 2],2] = Array(Array(1,1),Array(1,1));
                                Var b: Array[Array[Int, 2],2] = Array(Array(1,1),Array(1));
                           }               
                        }"""
        expect = "Illegal Array Literal: [[IntLit(1),IntLit(1)],[IntLit(1)]]"
        self.assertTrue(TestChecker.test(input, expect, 487))

    def test_488(self):
        """Simple program: int main() {} """
        input = """     
                        Class A {
                           $fooExp1(x:Float; y:String){
                                Var a: Array[Array[Int, 2],2] = Array(Array(1,1),Array(1,1));
                                Var b: Array[Array[Int, 2],2] = Array(Array("a","a"),Array("a","abc"));
                           }               
                        }"""
        expect = "Type Mismatch In Statement: VarDecl(Id(b),ArrayType(2,ArrayType(2,IntType)),[[StringLit(a),StringLit(a)],[StringLit(a),StringLit(abc)]])"
        self.assertTrue(TestChecker.test(input, expect, 488))

    def test_489(self):
        """Simple program: int main() {} """
        input = """     
                        Class A {
                           $fooExp1(x:Float; y:String){
                                Var a: Array[Array[Int, 2],2] = Array(Array(1,1),Array(1,1,"a"));
                           }               
                        }"""
        expect = "Illegal Array Literal: [[IntLit(1),IntLit(1)],[IntLit(1),IntLit(1),StringLit(a)]]"
        self.assertTrue(TestChecker.test(input, expect, 489))

    def test_490(self):
        """Simple program: int main() {} """
        input = """     
                        Class A {
                           $fooExp1(){
                                Var a: Array[Array[Int, 2],2] = Array(Array(1,1),Array(1,1));
                                a[1] = Array(1,1);
                                a[1][1] = 1;
                                a = 1;
                           }               
                        }"""
        expect = "Type Mismatch In Statement: AssignStmt(Id(a),IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 490))

    def test_491(self):
        """Simple program: int main() {} """
        input = """     
                        Class A {
                           $fooExp1(){
                                Val a: Array[Array[Int, 2],2] = Array(Array(1,1),Array(1,1));
                                a[1] = Array(1,1);
                           }               
                        }"""
        expect = "Cannot Assign To Constant: AssignStmt(ArrayCell(Id(a),[IntLit(1)]),[IntLit(1),IntLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 491))

    def test_492(self):
        """Simple program: int main() {} """
        input = """     
                        Class A {
                        Val a:Int = 2;
                           $fooExp1(){
                                Self.a = "abc";
                           }               
                        }"""
        expect = "Cannot Assign To Constant: AssignStmt(FieldAccess(Self(),Id(a)),StringLit(abc))"
        self.assertTrue(TestChecker.test(input, expect, 492))

    def test_493(self):
        input = """
                Class A {
                    Var $myArray: Array[Array[Array[Int,4],2],2] = Array(
                        Array(
                            Array(1,2,3,4),
                            Array(5,6,7,8)
                        ),
                        Array(
                            Array(-1,-2,-3,-4),
                            Array(-5,-6,-7, False)
                        )
                    );
                }
            """
        expect = "Illegal Array Literal: [[[IntLit(1),IntLit(2),IntLit(3),IntLit(4)],[IntLit(5),IntLit(6),IntLit(7),IntLit(8)]],[[UnaryOp(-,IntLit(1)),UnaryOp(-,IntLit(2)),UnaryOp(-,IntLit(3)),UnaryOp(-,IntLit(4))],[UnaryOp(-,IntLit(5)),UnaryOp(-,IntLit(6)),UnaryOp(-,IntLit(7)),BooleanLit(False)]]]"
        self.assertTrue(TestChecker.test(input, expect, 493))

    def test_494(self):
        input = """
                Class A {
                    foo() {
                        Var a: Array[Int, 3] = Array(1,2,3);
                        a[4] = 5; ## Index out of bound ##
                        a[1][2] = 4; ## Error with dimension##
                    }
                }
            """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),[IntLit(1),IntLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 494))

    def test_495(self):
        # NOTE: This case check for param compatiblity of Constructor
        input = """
                        Class Student
                        {
                            Var name: String;
                            Var ID: Int;
                            Constructor(newName: String; newID : Int)
                            {
                                Self.name = newName;
                                Self.ID = newID;
                            }
                        }
                        Class Program
                        {
                            main()
                            {
                                Var myStudent: Student = New Student ();
                            }
                        }
            """

        expect = "Type Mismatch In Expression: NewExpr(Id(Student),[])"
        self.assertTrue(TestChecker.test(input, expect, 495))

    def test_496(self):
        input = """
                        Class A
                        {
                        }
                        Class B:A
                        {
                            Var a: A = New C();
                        }
            """

        expect = "Undeclared Class: C"
        self.assertTrue(TestChecker.test(input, expect, 496))

    def test_497(self):
        # NOTE: This case check for param compatiblity of Constructor
        input = """
                        Class A
                        {
                        }
                        Class B:A
                        {
                            Var a: A = New B();
                        }
            """

        expect = "Type Mismatch In Statement: VarDecl(Id(a),ClassType(Id(A)),NewExpr(Id(B),[]))"
        self.assertTrue(TestChecker.test(input, expect, 497))

    def test_498(self):
        input = """
                        Class Program{
                            Val $someStatic : Int = 10;
                            foo() {
                                Var Program : Float = 1.0;
                                Var x : Int = Program::$someStatic;
                           }
                        }
            """

        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 498))

    def test_499(self):
        input = """
                Class A {
                      Var foo: Int = 1;
                      foo() {
                      }
                }
            """

        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 499))
