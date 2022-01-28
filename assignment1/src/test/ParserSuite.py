import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_201(self):
        """Simple program: int main() {} """
        input = """Class main{}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))


    def test_202(self):
        """More complex program"""
        input = """Class Rectangle: Shape {
        getArea() {
        Return self.length * self.width;
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,202))

    def test_203(self):
        """More complex program"""
        input = """Var a: Array[Array[Int,5],5];"""
        expect = "Error on line 1 col 0: Var"
        self.assertTrue(TestParser.test(input,expect,203))

    def test_204(self):
        """More complex program"""
        input = """1 + 1 + a.foo()"""
        expect = "Error on line 1 col 0: 1"
        self.assertTrue(TestParser.test(input,expect,204))

    def test_205(self):
        """More complex program"""
        input = """
    Class Shape {
        $getNumOfShape( {
            Return self.length * self.width;
        }
    }
"""
        expect = "Error on line 3 col 24: {"
        self.assertTrue(TestParser.test(input,expect,205))

    def test_206(self):
        """More complex program"""
        input = """
    Class Shape {
        foo(){
            a[b[1]][c][foo()] = 1;
        }
        Var e,f : Int = 1 + 1, 1 - 2;
    }
"""
        expect = "Error on line 4 col 26: ("
        self.assertTrue(TestParser.test(input,expect,206))

    def test_207(self):
        """More complex program"""
        input = """
Class Shape2 {
    $getNumOfShape() {
        If (a == (1+1) ){
            Var b,c:Boolean = True, False;
        }
        Foreach (i In 1 .. 100 By 2) {
             Var a:Boolean = True;
        }
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,207))

    def test_208(self):
            """More complex program"""
            input = """
    Class Shape {
        sum(a,b:Int; c,d:Float){}
    }
    """
            expect = "successful"
            self.assertTrue(TestParser.test(input, expect, 208))

    def test_209(self):
            """More complex program"""
            input = """
    Class Shape {
        Var a :Array[Array[Int,2],2] = Array(Array(1,1),Array(1,1));
    }
    """
            expect = "successful"
            self.assertTrue(TestParser.test(input, expect, 209))
    def test_210(self):
            """More complex program"""
            input = """
    Class Shape {
        foo(){
            Var a: Boolean = !!True;
        }
    }
    """
            expect = "successful"
            self.assertTrue(TestParser.test(input, expect, 210))
    def test_211(self):
        """More complex program"""
        input = """
    Class Shape {
        foo(){
            foo2(1+1,"a"+."b","a"==."b");
        }
    }
    """
        expect = "Error on line 4 col 16: ("
        self.assertTrue(TestParser.test(input, expect, 211))
    def test_212(self):
            """More complex program"""
            input = """
    Class Shape {
        Val $numOfShape: Int = 0;
        Val immutableAttribute: Int = 0;
        Var length, width: Int;
        $getNumOfShape() {
            Return $numOfShape;
        }
    }
    Class Rectangle: Shape {
        getArea() {
            Return self.length * self.width;
        }
    }
    Class Program {
        main() {
            Out.printInt(Shape::$numOfShape);
        }
    }
    """
            expect = "Error on line 7 col 19: $numOfShape"
            self.assertTrue(TestParser.test(input, expect, 212))
    def test_213(self):
            """More complex program"""
            input = """
    Class Shape {
        Constructor(width, height : Int; name:String){
            Self.Area=Self.width*Self.height;
            Self.name="shape"+.name;
        } 
        Destructor(){} 
    }
    """
            expect = "successful"
            self.assertTrue(TestParser.test(input, expect, 213))
    def test_214(self):
            """More complex program"""
            input = """
    Class Shape {
        foo(){
            a=1------1+1--1;
        } 
    }
    """
            expect = "successful"
            self.assertTrue(TestParser.test(input, expect, 214))
    def test_215(self):
            """More complex program"""
            input = """
    Class Shape {
        foo(){
            a=New X().Y();
        } 
    }
    """
            expect = "successful"
            self.assertTrue(TestParser.test(input, expect, 215))

    def test_216(self):
            """More complex program"""
            input = """
    Class Shape {
        foo(){
            a();
        } 
    }
    """
            expect = "Error on line 4 col 13: ("
            self.assertTrue(TestParser.test(input, expect, 216))

    def test_217(self):
            """More complex program"""
            input = """
    Class Shape {
        foo(){
            Var a();
        } 
    }
    """
            expect = "Error on line 4 col 17: ("
            self.assertTrue(TestParser.test(input, expect, 217))

    def test_218(self):
            """More complex program"""
            input = """
    Class Shape {
        foo(){
            Var r, s: Int;
            r = 2.0;
            Var a, b: Array[Int, 5];
            s = r * r * Self.myPI;
            a[0] = s;
        } 
    }
    """
            expect = "successful"
            self.assertTrue(TestParser.test(input, expect, 218))

    def test_218(self):
            """More complex program"""
            input = """
    Class Shape {
        foo(){
            a.b();
        } 
    }
    """
            expect = "successful"
            self.assertTrue(TestParser.test(input, expect, 218))
    def test_219(self):
            """More complex program"""
            input = """
    Class Shape {
        foo(){
            a=b.c.d.e;
        } 
    }
    """
            expect = "successful"
            self.assertTrue(TestParser.test(input, expect, 219))
    def test_220(self):
            """More complex program"""
            input = """
    Class Shape {
        foo(){
            Foreach (i In (1+2) .. (100*2-3) By (16-14)) {
                Out.printInt(i);
            }
        } 
    }
    """
            expect = "successful"
            self.assertTrue(TestParser.test(input, expect, 220))

    def test_221(self):
            """More complex program"""
            input = """
    Class Shape {
        foo(){
            ;
        } 
    }
    """
            expect = "Error on line 4 col 12: ;"
            self.assertTrue(TestParser.test(input, expect, 221))
    def test_222(self):
            """More complex program"""
            input = """
    Class Shape {
        foo(){
            Foreach (i In a[1] .. foo() By _123()) {}
        } 
    }
    """
            expect = "Error on line 4 col 37: ("
            self.assertTrue(TestParser.test(input, expect, 222))
    def test_223(self):
            """More complex program"""
            input = """
    Class Shape {
        foo(){
            a = !!!!!!!!!!!!True;
            b = ------------5;
        } 
    }
    """
            expect = "successful"
            self.assertTrue(TestParser.test(input, expect, 223))
    def test_224(self):
            """More complex program"""
            input = """
    Class Shape {
        foo(){
            a = !!!!!!!!!!!!True;
            b = ------------5;
            c=d.d.d.d.d.d.d.d;
            e=f[1][1][1][1];
        } 
    }
    """
            expect = "successful"
            self.assertTrue(TestParser.test(input, expect, 224))

    def test_225(self):
            """More complex program"""
            input = """
    Class Shape {
        foo(){
            a = (b==c) == True;
        } 
    }
    """
            expect = "successful"
            self.assertTrue(TestParser.test(input, expect, 225))
    # def test_226(self):
    #         """More complex program"""
    #         input = """
    # Class Shape {
    #     foo(){
    #         a = b == c  == True;
    #     } 
    # }
    # """
    #         expect = "Error on line 4 col 24: =="
    #         self.assertTrue(TestParser.test(input, expect, 226))

    def test_227(self):
            """More complex program"""
            input = """
    Class Shape {
        foo(){
            a = (b < c)  == True;
        } 
    }
    """
            expect = "successful"
            self.assertTrue(TestParser.test(input, expect, 227))
    def test_228(self):
            """More complex program"""
            input = """
    Class Shape {
        foo(){
            a = (b < c) < True;
        } 
    }
    """
            expect = "successful"
            self.assertTrue(TestParser.test(input, expect, 228))

    def test_228(self):
            """More complex program"""
            input = """
    Class Shape {
        foo(){
            a = b < c < True;
        } 
    }
    """
            expect = "Error on line 4 col 22: <"
            self.assertTrue(TestParser.test(input, expect, 228))
    def test_229(self):
            """More complex program"""
            input = """
    Class Shape {
        foo(){
            a = ("a"+."b")+."b";
            c = ("a"==."a")==True;
        } 
    }
    """
            expect = "successful"
            self.assertTrue(TestParser.test(input, expect, 229))
    def test_230(self):
            """More complex program"""
            input = """
    Class Shape {
        foo(){
            a = "a"+."b"+."b";
        } 
    }
    """
            expect = "Error on line 4 col 24: +."
            self.assertTrue(TestParser.test(input, expect, 230))
    def test_231(self):
            """More complex program"""
            input = """
    Class Shape {
        foo(){
            a = "a"==."b"==."b";
        } 
    }
    """
            expect = "Error on line 4 col 25: ==."
            self.assertTrue(TestParser.test(input, expect, 231))
    def test_232(self):
            """More complex program"""
            input = """
    Class Shape:a:b{}
    """
            expect = "Error on line 2 col 17: :"
            self.assertTrue(TestParser.test(input, expect, 232))
    def test_233(self):
            """More complex program"""
            input = """
    Class Shape {
        foo(){
            a::$b=2;
            a::$e();
            a::$c::$d=2;
        } 
    }
    """
            expect = "Error on line 6 col 17: ::"
            self.assertTrue(TestParser.test(input, expect, 233))
    def test_234(self):
            """More complex program"""
            input = """
    Class Shape {
        foo(){
            a::$b=2;
            a::$e();
            a::$c()::$d=2;
        } 
    }
    """
            expect = "Error on line 6 col 19: ::"
            self.assertTrue(TestParser.test(input, expect, 234))
    def test_235(self):
            """More complex program"""
            input = """
    Class Shape {
        foo(){
        a+=1;
        } 
    }
    """
            expect = "Error on line 4 col 9: +"
            self.assertTrue(TestParser.test(input, expect, 235))
    def test_236(self):
            """More complex program"""
            input = """
    Class Shape {
        foo(){
        a=+1;
        } 
    }
    """
            expect = "Error on line 4 col 10: +"
            self.assertTrue(TestParser.test(input, expect, 236))
    def test_237(self):
        input = """
            Class Shape {
                foo(){
                a=-1+1;
                b=1+-1;
                } 
            }
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 236))
    def test_238(self):
            """More complex program"""
            input = """
    Class Shape {
        foo(){
            a=-1+1;
            b=1+-1--1+-1---1;
        } 
    }
    """
            expect = "successful"
            self.assertTrue(TestParser.test(input, expect, 238))
    def test_239(self):
            """More complex program"""
            input = """
    Class Shape {
        foo(){
        b=1+-1--1+-1-+-1;
        } 
    }
    """
            expect = "Error on line 4 col 21: +"
            self.assertTrue(TestParser.test(input, expect, 239))
    def test_240(self):
            """More complex program"""
            input = """
    Class Shape {
        foo(){
        Var a :Int = $1-----5;
        } 
    }
    """
            expect = "Error on line 4 col 21: $1"
            self.assertTrue(TestParser.test(input, expect, 240))

    def test_241(self):
        input = """
                Class Shape{
                    foo(){
                        a = New X().Y();
                        Var a: Array[Int, 0];
                    }
                }

            """
        output = """Error on line 5 col 42: 0"""
        self.assertTrue(TestParser.test(input, output, 241))
    def test_242(self):
        input = """
                Class Shape{
                    foo(){
                        b::$f=1;
                    }
                    a = 1;
                }

            """
        output = """Error on line 6 col 22: ="""
        self.assertTrue(TestParser.test(input, output, 242))
    def test_243(self):
        input = """
                Class Shape{
                    foo(){
                        a=1;
                    }
                    Foreach (x In 1 .. 100 by 2){}
                }

            """
        output = """Error on line 6 col 20: Foreach"""
        self.assertTrue(TestParser.test(input, output, 243))
    def test_244(self):
        input = """
                Class Shape{
                    foo(){}
                    Class LamTestMetVaiLoz{}
                }

            """
        output = """Error on line 4 col 20: Class"""
        self.assertTrue(TestParser.test(input, output, 244))
    def test_245(self):
        input = """
                Class Shape{
                    foo(){
                        Class LamTestMetVaiLoz{}
                    }
                }

            """
        output = """Error on line 4 col 24: Class"""
        self.assertTrue(TestParser.test(input, output, 245))
    def test_246(self):
        input = """
                Class Shape{
                    foo(){
                        Var a: Array[Int, 01];
                        Var a: Array[Int, 0x1];
                        Var a: Array[Int, 0X1];
                        Var a: Array[Int, 0b1];
                        Var a: Array[Int, 0B1];
                        Var a: Array[Int, 1];
                        Var a: Array[Int, 00];
                    }
                }

            """
        output = """Error on line 10 col 42: 00"""
        self.assertTrue(TestParser.test(input, output, 246))
    def test_247(self):
        input = """
                Class Shape{
                    foo(){
                        Var a: Array[Int, 0b0];
                    }
                }

            """
        output = """Error on line 4 col 42: 0b0"""
        self.assertTrue(TestParser.test(input, output, 247))
    def test_248(self):
        input = """
                Class Shape{
                    foo(){
                        Var a: Array[Int, 0x0];
                    }
                }

            """
        output = """Error on line 4 col 42: 0x0"""
        self.assertTrue(TestParser.test(input, output, 248))
    def test_249(self):
        input = """
                Class Shape{
                    foo(){
                        Var a: Array[Int, 1_23.456e+7];
                    }
                }

            """
        output = """Error on line 4 col 42: 123.456e+7"""
        self.assertTrue(TestParser.test(input, output, 249))
    def test_250(self):
        input = """
                Class Shape{
                    foo(){
                        Var a: Array[Int, b::$c.foo()];
                    }
                }

            """
        output = """Error on line 4 col 42: b"""
        self.assertTrue(TestParser.test(input, output, 250))
    def test_251(self):
        input = """
                Class Shape{
                    Var a,b:Int=5,6,7;
                }

            """
        output = """Error on line 3 col 35: ,"""
        self.assertTrue(TestParser.test(input, output, 251))
