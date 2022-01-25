import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    # def test_lowercase_identifier(self):
    #     """test identifiers"""
    #     self.assertTrue(TestLexer.test("abc","abc,<EOF>",101))
    # def test_lower_upper_id(self):
    #     self.assertTrue(TestLexer.test("aCBbdc","aCBbdc,<EOF>",102))
    # def test_mixed_id(self):
    #     self.assertTrue(TestLexer.test("aAsVN3","aAsVN,3,<EOF>",103))
    # def test_integer(self):
    #     """test integers"""
    #     self.assertTrue(TestLexer.test("123a123","123,a,123,<EOF>",104))

    
    """test identifiers"""

    def test_lowercase_identifier(self):        
        self.assertTrue(TestLexer.test("abc","abc,<EOF>",101))

    def test_lower_upper_id(self):
        self.assertTrue(TestLexer.test("aCBbdc","aCBbdc,<EOF>",102))

    def test_mixed_id(self):
        self.assertTrue(TestLexer.test("aAsVN3","aAsVN3,<EOF>",103))

    def test_id_with_int(self):
        self.assertTrue(TestLexer.test("123a123","123,a123,<EOF>",104))

    def test_underscore_only(self):
        self.assertTrue(TestLexer.test("_","_,<EOF>",105))

    def test_id_with_underscore_and_digit(self):
        self.assertTrue(TestLexer.test("_ab_94","_ab_94,<EOF>",106))

    def test_multiple_id(self):
        self.assertTrue(TestLexer.test("_ab_94 4ac  _99a","_ab_94,4,ac,_99a,<EOF>",107))

    """ Test Int """

    # Test Decimal
    def test_simple_decimal_int(self):
        self.assertTrue(TestLexer.test("123","123,<EOF>",108))

    def test_decimal_with_underscore(self):
        self.assertTrue(TestLexer.test("123_456_789","123456789,<EOF>",109))

    def test_double_underscore_int(self):
        self.assertTrue(TestLexer.test("123__456","123,__456,<EOF>",110))

    def test_zero_int(self):
        self.assertTrue(TestLexer.test("0","0,<EOF>",111))

    # Test Octal

    def test_00_octal(self):
        self.assertTrue(TestLexer.test("00","00,<EOF>",112))

    def test_simple_octal(self):
        self.assertTrue(TestLexer.test("0123","0123,<EOF>",113))

    def test_octal_with_decimal_on_00(self):
        self.assertTrue(TestLexer.test("001234","00,1234,<EOF>",114))

    def test_octal_with_underscore(self):
        self.assertTrue(TestLexer.test("01_23_4","01234,<EOF>",115))

     # Test Hexadecimal

    def test_simple_hexa(self):
        self.assertTrue(TestLexer.test("0x6453","0x6453,<EOF>",116))

    def test_simple_heXa(self):
        self.assertTrue(TestLexer.test("0X6453","0X6453,<EOF>",117))

    def test_hexa_with_underscore(self):
        self.assertTrue(TestLexer.test("0X64_53","0X6453,<EOF>",118))

    def test_hexa_with_0x0(self):
        self.assertTrue(TestLexer.test("0x01234","0x0,1234,<EOF>",119))

    def test_hexa_with_octal(self):
        self.assertTrue(TestLexer.test("0x006453","0x0,06453,<EOF>",120))

    def test_simple_hexa_with_char(self):
        self.assertTrue(TestLexer.test("0x6453ABCDEF","0x6453ABCDEF,<EOF>",121))

    def test_simple_hexa_with_char_and_id(self):
        self.assertTrue(TestLexer.test("0x6453ABCDEFGHIJK","0x6453ABCDEF,GHIJK,<EOF>",122))

    def test_simple_hexa_with_char_id_underscore(self):
        self.assertTrue(TestLexer.test("0x6453ABCDEF_A","0x6453ABCDEFA,<EOF>",123))

    def test_simple_hexa_with_char_id_underscore_2(self):
        self.assertTrue(TestLexer.test("0x6453ABCDEF_XYZ","0x6453ABCDEF,_XYZ,<EOF>",124))
       
    # Test Binary

    def test_simple_binary(self):
        self.assertTrue(TestLexer.test("0b0123","0b0,123,<EOF>",125))

    def test_binary_with_underscore(self):
        self.assertTrue(TestLexer.test("0B1_001_0101","0B10010101,<EOF>",126))

    # Test Boolean

    def test_boolean_become_id(self):
        self.assertTrue(TestLexer.test("TrueFalse_","TrueFalse_,<EOF>",127))

    def test_boolean_simple(self):
        self.assertTrue(TestLexer.test("True False","True,False,<EOF>",128))

    # Test Float

    def test_float_with_3(self):
        self.assertTrue(TestLexer.test("6_4.54e+5","64.54e+5,<EOF>",129))

    def test_float_with_decimal_and_floating(self):
        self.assertTrue(TestLexer.test("64.","64.,<EOF>",130))

    def test_float_with_decimal_and_e(self):
        self.assertTrue(TestLexer.test("64e+5","64e+5,<EOF>",131))

    def test_float_with_float_and_e(self):
        self.assertTrue(TestLexer.test(".e-3",".e-3,<EOF>",132))

    # Test Static ID

    def test_static_id_simple(self):
        self.assertTrue(TestLexer.test("$_$909","$_,$909,<EOF>",133))

    # Test Comment

    def test_comment_simple(self):
        self.assertTrue(TestLexer.test("## This will be remove. ##","<EOF>",134))

    def test_comment_with_symbol(self):
        self.assertTrue(TestLexer.test("## This # will _ be // remove. ##","<EOF>",135))

    # Test String -> Unclosed string; Illegal escape

    def test_simple_string(self):
        self.assertTrue(TestLexer.test(' "Hello everyone" ','"Hello everyone",<EOF>',136))

    def test_simple_unclose_string(self):
        self.assertTrue(TestLexer.test(' "Hello everyone','Unclosed String: "Hello everyone',137))

    def test_simple_escape_string(self):
        self.assertTrue(TestLexer.test(' "Hello everyone \\t" ','"Hello everyone \\t",<EOF>',138))

    def test_simple_illigal_escape(self):
        self.assertTrue(TestLexer.test(' "Hello everyone \\h"','Illegal Escape In String: "Hello everyone \\h',139))
