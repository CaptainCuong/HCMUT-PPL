from MPVisitor import MPVisitor
from MPParser import MPParser
from AST import *

class ASTGeneration(MPVisitor):

    def visitProgram(self,ctx:MPParser.ProgramContext):
        return None

    def visitVardecl(self,ctx:MPParser.VardeclContext):
        return None

    def visitMptype(self,ctx:MPParser.MptypeContext): 
        return None

    def visitIds(self,ctx:MPParser.IdsContext):
        return None
  
    

        

