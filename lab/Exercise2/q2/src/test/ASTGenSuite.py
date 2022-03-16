import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_declaration(self):
        """Simple program: int a,b """
        input = """int a;"""
        expect = str(Program([VarDecl(Id("a"),IntType())]))
        self.assertTrue(TestAST.test(input,expect,300))

    def test_one_declaration_with_two_variables(self):
        """More complex program"""
        input = """int a,b;"""
        expect = str(Program([VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())]))
        self.assertTrue(TestAST.test(input,expect,301))
    
    def test_many_declarations_with_many_variables(self):
        """More complex program"""
        input = """int a,b;float c,d,e;"""
        expect = str(Program([VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("c"),FloatType()),VarDecl(Id("d"),FloatType()),VarDecl(Id("e"),FloatType())]))
        self.assertTrue(TestAST.test(input,expect,302))
   