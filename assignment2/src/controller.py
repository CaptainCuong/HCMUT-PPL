TEST_DIR = 'test/testcases/'
SOL_DIR = 'test/solutions/'

test = open('ASTGenSuite.py', 'w')
test.write('class ASTGenSuite(unittest.TestCase):\n')
for i in range(999):
	line = open(TEST_DIR + '%d.txt'%i, 'r')
	expect = open(SOL_DIR + '%d.txt'%i, 'r') 
	test.write('\tdef test_%d(self):\n'%i)
	test.write('\t\tline = \'\'\'' + line.readline() + '\'\'\'\n')
	test.write('\t\texpect = \'\'\'' + expect.readline() + '\'\'\'\n')
	test.write('\t\tself.assertTrue(TestAST.test(line, expect, %d))\n'%i)