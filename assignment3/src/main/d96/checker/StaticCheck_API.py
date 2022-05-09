class Attribute_Check:
def __init__(self, name:str, typ:Type, isStatic = False, const = False):

class Variable_Check:
def __init__(self,name,typ,scope, constant=False):

class Method_Check:
def __init__(self, method_name:str, static=False, para:List[VarDecl]=[], rettype=None):
def _enterScope(self):
def _exitScope(self):
def _change_ret_type(self, rettype):
	
class Class_Check:
def __init__(self, name:str, inherited:Class_Check = None):
def add_attribute(self, name:str, att_type:Type, isStatic=False, const=False):
def add_method(self, name:str, isStatic=False, paratype:List[VarDecl]=[], rettype=None):
def get_method(self, method_name:str):


class ClassManager:
def add_class(self, cls_name:str, inherited:str):
def add_method(self, cls_name:str, method_name:str, isStatic=False, paratype:List[Type]=[], rettype = None):
def add_attribute(self, cls_name:str, att_name:str,att_type:Type,isStatic:bool,const:bool):
def get_class(self, class_name:str):