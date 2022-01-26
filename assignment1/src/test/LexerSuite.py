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
        self.assertTrue(TestLexer.test(' "Hello everyone','Unclosed String: Hello everyone',137))

    def test_simple_escape_string(self):
        self.assertTrue(TestLexer.test(' "Hello everyone \\t" ','"Hello everyone \\t",<EOF>',138))

    def test_simple_illigal_escape(self):
        self.assertTrue(TestLexer.test(' "Hello everyone \\h"','Illegal Escape In String: Hello everyone \\h',139))

      
    """Character set 4-10""" 
    def test_charater1(self):
        self.assertTrue(TestLexer.test('"\\b\\r \\zv"','Illegal Escape In String: \\b\\r \\z',140))
    
    def test_charater2(self):
        self.assertTrue(TestLexer.test('"\\b\\n\\t"','"\\b\\n\\t",<EOF>',141))

    def test_charater3(self):
        self.assertTrue(TestLexer.test('"\\f\\b\\r"','"\\f\\b\\r",<EOF>',142))

    def test_charater4(self):
        self.assertTrue(TestLexer.test('"\\mn"',"Illegal Escape In String: \\m",143))

    def test_charater5(self):
        self.assertTrue(TestLexer.test('"\\r\\n \\t\\b\\f"','"\\r\\n \\t\\b\\f",<EOF>',144))

    def test_charater6(self):
        self.assertTrue(TestLexer.test('"abc\\h def"',"Illegal Escape In String: abc\\h",145))

    def test_charater7(self):
        self.assertTrue(TestLexer.test('"\\f\\b\\r\\r"','"\\f\\b\\r\\r",<EOF>',146))

    def test_charater8(self):
        self.assertTrue(TestLexer.test('"    \\a"',"Illegal Escape In String:     \\a",147))

    def test_charater9(self):
        self.assertTrue(TestLexer.test('"\\\\"','"\\\\",<EOF>',148))

    def test_character_mixed_id(self):
        self.assertTrue(TestLexer.test('"pop\\t\\p"',"Illegal Escape In String: pop\\t\\p",149))

    """ Program comment 11 - 20"""

    def test_comment1(self):
        test = "## This is a multi-line comment.  ##"
        expected = "<EOF>"
        self.assertTrue(TestLexer.test(test,expected,150))
    
    def test_comment2(self):
        test = "## This is a multi-line comment.  #"
        expected = "Error Token #"
        self.assertTrue(TestLexer.test(test,expected,151))

    def test_comment3(self):
        test = "#casc##cs"
        expected = "Error Token #"
        self.assertTrue(TestLexer.test(test,expected,152))
        
    # def test_comment_mixed_id(self):
    #     test = "Cacl##123##"
    #     expected = "Cacl,<EOF>"
    #     self.assertTrue(TestLexer.test(test,expected,153))

    # def test_comment4(self):
    #     test = "####"
    #     expected = "<EOF>"
    #     self.assertTrue(TestLexer.test(test,expected,154))

    # def test_comment5(self):
    #     test = "##->-##"
    #     expected = "<EOF>"
    #     self.assertTrue(TestLexer.test(test,expected,155))

    # def test_comment6(self):
    #     test = "## Hello \"#"
    #     expected = "Error Token #"
    #     self.assertTrue(TestLexer.test(test,expected,156))

    # def test_comment_ignore_illegal_escape_errors(self):
    #     test = "## \a ##"
    #     expected = "<EOF>"
    #     self.assertTrue(TestLexer.test(test,expected,157))

    # def test_comment_ignore_illegal_character(self):
    #     test = "## #a ##"
    #     expected = "<EOF>"
    #     self.assertTrue(TestLexer.test(test,expected,158))

    # def test_comment_ignore_unclosed_string(self):
    #     test = "## \"Hello ##"
    #     expected = "<EOF>"
    #     self.assertTrue(TestLexer.test(test,expected,159))

    # """Identifiers 21 -30"""

    # def test_identifier1(self):
    #     test = "aBcd_12"
    #     expected = "aBcd_12,<EOF>"
    #     self.assertTrue(TestLexer.test(test,expected,160))

    # def test_identifier_mixed_float(self):
    #     test = "7.2e-1e1"
    #     expected = "7.2e-1,e1,<EOF>"
    #     self.assertTrue(TestLexer.test(test,expected,161))

    # def test_identifier_mixed_int(self):
    #     test = "12abv23_1"
    #     expected = "12,abv23_1,<EOF>"
    #     self.assertTrue(TestLexer.test(test,expected,162))

    # def test_identifier_mixed_boolean(self):
    #     test = "True vs False"
    #     expected = "True,vs,False,<EOF>"
    #     self.assertTrue(TestLexer.test(test,expected,163))

    # def test_identifier_asg_array(self):
    #     test = "x=Array(1,2)"
    #     expected = "x,=,Array(1,2),<EOF>"
    #     self.assertTrue(TestLexer.test(test,expected,164))

    # def test_identifier_class(self):
    #     test = "Class T"
    #     expected = "Class,T,<EOF>"
    #     self.assertTrue(TestLexer.test(test,expected,165))

    # def test_identifier_create_object(self):
    #     test = "x = New T();"
    #     expected = "x,=,New,T,(,),;,<EOF>"
    #     self.assertTrue(TestLexer.test(test,expected,166))

    # def test_identifier_operator(self):
    #     test = "a*b-c/d"
    #     expected = "a,*,b,-,c,/,d,<EOF>"
    #     self.assertTrue(TestLexer.test(test,expected,167))

    # def test_identifier_instance_method(self):
    #     test = "std.getID(name, age);"
    #     expected = "std,.,getID,(,name,,,age,),;,<EOF>"
    #     self.assertTrue(TestLexer.test(test,expected,168))

    # def test_identifier_string(self):
    #     test = "abc\"sss\""
    #     expected = "abc,\"sss\",<EOF>"
    #     self.assertTrue(TestLexer.test(test,expected,169))

    # """Operators 41-70"""
    # def test_operator1(self):
    #     test = "+..::"
    #     expected = "+.,.,::,<EOF>"
    #     self.assertTrue(TestLexer.test(test,expected,170))

    # def test_operator2(self):
    #     test = "New.::"
    #     expected = "New,.,::,<EOF>"
    #     self.assertTrue(TestLexer.test(test,expected,171))

    # def test_operator3(self):
    #     test = "<=>"
    #     expected = "<=,>,<EOF>"
    #     self.assertTrue(TestLexer.test(test,expected,172))

    # def test_operator4(self):
    #     test = "<====."
    #     expected = "<=,==,=,.,<EOF>"
    #     self.assertTrue(TestLexer.test(test,expected,173))

    # def test_operator5(self):
    #     test = ">==%!=="
    #     expected = ">=,=,%,!=,=,<EOF>"
    #     self.assertTrue(TestLexer.test(test,expected,174))

    # def test_operator_mixed_float(self):
    #     test = "2_1.1.1"
    #     expected = "2_1.1,.,1,<EOF>"
    #     self.assertTrue(TestLexer.test(test,expected,175))

    # def test_operator_mixed_instance_method_invocation(self):
    #     test = "S::$getID()"
    #     expected = "S,::,$getID,(,),<EOF>"
    #     self.assertTrue(TestLexer.test(test,expected,176))

    # def test_operator_mixed_static_method_invocation(self):
    #     test = "a.getID()"
    #     expected = "a,.,getID,(,),<EOF>"
    #     self.assertTrue(TestLexer.test(test,expected,177))

    # def test_operator_mixed_string(self):
    #     test = "\"a\" +. \"bc\""
    #     expected = "\"a\",+.,\"bc\",<EOF>"
    #     self.assertTrue(TestLexer.test(test,expected,178))

    # def test_operator_logical(self):
    #     test = "True || True"
    #     expected = "True,||,True,<EOF>"
    #     self.assertTrue(TestLexer.test(test,expected,179))

    # """Seperators 71 - 80"""

    # def test_seperator1(self):
    #     test = "(12)[2].1"
    #     expected = "(,12,),[,2,],.,1,<EOF>"
    #     self.assertTrue(TestLexer.test(test,expected,180))
        
    # def test_seperator2(self):
    #     test = "a:b:c:([1],)"
    #     expected = "a,:,b,:,c,:,(,[,1,],,,),<EOF>"
    #     self.assertTrue(TestLexer.test(test,expected,181))
    # def test_seperator_mixed_method(self):
    #     test = "foo();"
    #     expected = "foo,(,),;,<EOF>"
    #     self.assertTrue(TestLexer.test(test,expected,182))
        
    # def test_seperator_mixed_integer(self):
    #     test = "A[0x9F][032]"
    #     expected = "A,[,0x9F,],[,032,],<EOF>"
    #     self.assertTrue(TestLexer.test(test,expected,183))
    # def test_seperator_mix_float(self):
    #     test = "192.168.1.2"
    #     expected = "192.168,.,1.2,<EOF>"
    #     self.assertTrue(TestLexer.test(test,expected,184))
        
    # def test_seperator_mixed_initialize_variable(self):
    #     test = "Var a, b: Array[Int, 5];"
    #     expected = "Var,a,,,b,:,Array,[,Int,,,5,],;,<EOF>"
    #     self.assertTrue(TestLexer.test(test,expected,185))
    # def test_seperator1_mixed_class(self):
    #     test = "Class Shape { }"
    #     expected = "Class,Shape,{,},<EOF>"
    #     self.assertTrue(TestLexer.test(test,expected,186))
        
    # def test_seperator1_mixed_expression(self):
    #     test = "(1+2)-(2-3)"
    #     expected = "(,1,+,2,),-,(,2,-,3,),<EOF>"
    #     self.assertTrue(TestLexer.test(test,expected,187))
    # def test_seperator_mixed_stmt(self):
    #     test = "lsh = a[1];"
    #     expected = "lsh,=,a,[,1,],;,<EOF>"
    #     self.assertTrue(TestLexer.test(test,expected,188))

    # """Literals 81-100"""
        
    # def test_integer1(self):
    #     test = "0b10x9"
    #     expected = "0b10,x9,<EOF>"
    #     self.assertTrue(TestLexer.test(test,expected,189))
    # def test_integer2(self):
    #     test = "1_2__3"
    #     expected = "1_2,__3,<EOF>"
    #     self.assertTrue(TestLexer.test(test,expected,190))
        
    # def test_integer3(self):
    #     test = "123_"
    #     expected = "123,_,<EOF>"
    #     self.assertTrue(TestLexer.test(test,expected,191))
    # def test_integer4(self):
    #     test = "12__3"
    #     expected = "12,__3,<EOF>"
    #     self.assertTrue(TestLexer.test(test,expected,192))
        
    # def test_integer5(self):
    #     test = "123___3"
    #     expected = "123,___3,<EOF>"
    #     self.assertTrue(TestLexer.test(test,expected,193))

    # def test_integer6(self):
    #     test = "0X1234AbEf"
    #     expected = "0X1234A,bEf,<EOF>"
    #     self.assertTrue(TestLexer.test(test,expected,194))

    # def test_integer_mixed_identifier1(self):
    #     test = "0X1_234_567/0x0"
    #     expected = "0X1,_234_567,/,0x0,<EOF>"
    #     self.assertTrue(TestLexer.test(test,expected,195))

    # def test_float_mixed_identifier1(self):
    #     test = "_12.2e-5_1"
    #     expected = "_12,.2e-5_1,<EOF>"
    #     self.assertTrue(TestLexer.test(test,expected,196))

    # def test_string1(self):
    #     test = "\"\"\""
    #     expected = "\"\",Unclosed String: \""
    #     self.assertTrue(TestLexer.test(test,expected,197))

    # def test_string2(self):
    #     test = "\"\"\";\""
    #     expected = "\"\",\";\",<EOF>"
    #     self.assertTrue(TestLexer.test(test,expected,198))

    # def test_string_mixed_operator(self):
    #     test = "\"1\" +. \"2\""
    #     expected = "\"1\",+.,\"2\",<EOF>"
    #     self.assertTrue(TestLexer.test(test,expected,199))

    # def test_array_string1(self):
    #     test = "Array(\"1\",\"a\")"
    #     expected = "Array(\"1\",\"a\"),<EOF>"
    #     self.assertTrue(TestLexer.test(test,expected,200))

    # def test_array_mixed_int_string(self):
    #     test = "Array(1,\"a\")"
    #     expected = "Array,(,1,,,\"a\",),<EOF>"
    #     self.assertTrue(TestLexer.test(test,expected,201))

    # def test_array_mixed_comment(self):
    #     test = "Array(1,2##2##)"
    #     expected = "Array,(,1,,,2,),<EOF>"
    #     self.assertTrue(TestLexer.test(test,expected,202))

    # def test_array_float1(self):
    #     test = "Array(1.,2.e-2_1)"
    #     expected = "Array(1.,2.e-2_1),<EOF>"
    #     self.assertTrue(TestLexer.test(test,expected,203))

    # def test_array_empty(self):
    #     test = "Array()"
    #     expected = "Array,(,),<EOF>"
    #     self.assertTrue(TestLexer.test(test,expected,204))

    # def test_multi_array1(self):
    #     test = "Array(Array(\"\"))"
    #     expected = "Array(Array(\"\")),<EOF>"
    #     self.assertTrue(TestLexer.test(test,expected,205))

    # def test_multi_array2(self):
    #     test = "Array(Array(1),Array(Array(3)))"
    #     expected = "Array(Array(1),Array(Array(3))),<EOF>"
    #     self.assertTrue(TestLexer.test(test,expected,206))

    # def test_string_mixed_comment(self):
    #     test = "\"\"##\"\"##"
    #     expected = "\"\",<EOF>"
    #     self.assertTrue(TestLexer.test(test,expected,207))

    # def test_float_mixed_comment(self):
    #     test = "1.2####3"
    #     expected = "1.2,3,<EOF>"
    #     self.assertTrue(TestLexer.test(test,expected,208))

    # def test_octal1(self):
    #     test = "000123"
    #     expected = "00,0123,<EOF>"
    #     self.assertTrue(TestLexer.test(test,expected,209))

    # def test_binary1(self):
    #     test = "0b12"
    #     expected = "0b1,2,<EOF>"
    #     self.assertTrue(TestLexer.test(test,expected,210))

    # def test_binary2(self):
    #     test = "0b100b0"
    #     expected = "0b100,b0,<EOF>"
    #     self.assertTrue(TestLexer.test(test,expected,211))

    # def test_hex1(self):
    #     test = "0xFF0001_2"
    #     expected = "0xFF0001,_2,<EOF>"
    #     self.assertTrue(TestLexer.test(test,expected,212))

    # def test_mixed_int_zero(self):
    #     test = "000X00b00"
    #     expected = "00,0X0,0b0,0,<EOF>"
    #     self.assertTrue(TestLexer.test(test,expected,213))

    # # def test_(self):
    # #     test = ""
    # #     expected = ",<EOF>"
    # #     self.assertTrue(TestLexer.test(test,expected,181))

    # def test_lowercase_identifier(self):
    #     self.assertTrue(TestLexer.test("abc","abc,<EOF>",214))
    # def test_lower_upper_id(self):
    #     self.assertTrue(TestLexer.test("aCBbdc","aCBbdc,<EOF>",215))
    # def test_mixed_id(self):
    #     self.assertTrue(TestLexer.test("aAsVN3","aAsVN3,<EOF>",216))
    # def test_mixed_integer_id(self):
    #     self.assertTrue(TestLexer.test("123a123","123,a123,<EOF>",217))
    # def test_comment(self):
    #     self.assertTrue(TestLexer.test("##qwe##","<EOF>",218))
    # def test_comment_2(self):
    #     self.assertTrue(TestLexer.test("#qwe#","Error Token #",219))
    # def test_float(self):
    #     self.assertTrue(TestLexer.test("1234.2","1234.2,<EOF>",220))
    # def test_mixed_operator_float(self):
    #     self.assertTrue(TestLexer.test(".2",".,2,<EOF>",221))
    # def test_float3(self):
    #     self.assertTrue(TestLexer.test("1.2e3","1.2e3,<EOF>",222))
    # def test_float4(self):
    #     self.assertTrue(TestLexer.test("3_123.8e-1","3123.8e-1,<EOF>",223))
    # def test_integer(self):
    #     self.assertTrue(TestLexer.test("123_123","123123,<EOF>",224))
    # def test_Keywords(self):
    #     self.assertTrue(TestLexer.test("Int Break By","Int,Break,By,<EOF>",225))
    # def test_Keywords2(self):
    #     self.assertTrue(TestLexer.test("If Elseif","If,Elseif,<EOF>",226))
    # def test_Operators(self):
    #     self.assertTrue(TestLexer.test("+!||.==.","+,!,||,.,==.,<EOF>",227))
    # def test_Operator2(self):
    #     self.assertTrue(TestLexer.test("<=>","<=,>,<EOF>",228))
    # def test_Seperator(self):
    #     self.assertTrue(TestLexer.test("()[]","(,),[,],<EOF>",229))
    # def test_octal2(self):
    #     self.assertTrue(TestLexer.test("0123","0123,<EOF>",230))
    # def test_binary3(self):
    #     self.assertTrue(TestLexer.test("0b111","0b111,<EOF>",231))
    # def test_hex2(self):
    #     self.assertTrue(TestLexer.test("0x1A","0x1A,<EOF>",232))
    # def test_boolean(self):
    #     self.assertTrue(TestLexer.test("True False","True,False,<EOF>",233))
    # def test_string(self):
    #     self.assertTrue(TestLexer.test("\"tab \\t\"","\"tab \\t\",<EOF>",234))
    # def test_string3(self):
    #     self.assertTrue(TestLexer.test("\"He asked me: '\"Where is John?'\"\"","\"He asked me: '\"Where is John?'\"\",<EOF>",235))
    # def test_array_int(self):
    #     self.assertTrue(TestLexer.test("Array(1,1,1)","Array(1,1,1),<EOF>",236))
    # def test_array_float(self):
    #     self.assertTrue(TestLexer.test("Array(0.1,1e-1,1_213.4E-7)","Array,(,0.1,,,1e-1,,,1_213.4E-7,),<EOF>",237))
    # def test_array_string(self):
    #     self.assertTrue(TestLexer.test("Array(\"1\",\"12\",\"1_213.4E-7\")","Array(\"1\",\"12\",\"1_213.4E-7\"),<EOF>",238))
    # def test_multi_array(self):
    #     self.assertTrue(TestLexer.test("Array(Array(\"Volvo\",\"22\",\"18\"),Array(\"Saab\",\"5\",\"2\"))",\
    #                                 "Array(Array(\"Volvo\",\"22\",\"18\"),Array(\"Saab\",\"5\",\"2\")),<EOF>",239))