import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
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
        self.assertTrue(TestAST.test(input,expect,400))
   