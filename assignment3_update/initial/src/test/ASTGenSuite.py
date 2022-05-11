import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_400(self):
        """Simple program: int main() {} """
        input = """
                    Class Program{
                            Val $someStatic : Int = 10;
                            foo() {
                                Var Program : Float = 1.0;
                                Var x : Int = Program::$someStatic;
                           }
                        }"""
        expect = "Redeclared Attribute: a"
        self.assertTrue(TestAST.test(input,expect,400))
   