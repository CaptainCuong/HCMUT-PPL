object Demo {
   def main(args: Array[String]) = {
      val list = List(1, 2, 3 ,4)
      //apply operation to get sum of all elements of the list
      val result = list.foldLeft(2)(_ + _)
      //print result
      println(result)      
   }
}

class Eval: 
    def visitBinExp(self, exp): 
        if exp.op=="+": 
            return exp.left.accept(self) +exp.right.accept(self) 
        if exp.op == "-": 
            return exp.left.accept(self) - exp.right.accept(self) 
        if exp.op=="*": 
            return exp.left.accept(Eval()) *exp.right.accept(Eval()) 
        if exp.op == "/": 
            return exp.left.accept(Eval()) /exp.right.accept(Eval()) 
  
    def visitUnExp(self, exp): 
        if exp.op =="+": 
            return +exp.e.accept(self) 
        if exp.op == "-": 
            return -exp.e.accept(self) 
  
    def visitLit(self, lit): 
        return lit.val 
  
  
class PrintPrefix: 
    def visitBinExp(self, exp): 
        _left = exp.left.accept(self) 
        _right = exp.right.accept(self) 
        return exp.op + " " + _left + " " + _right 
  
    def visitUnExp(self, exp): 
        _e = exp.e.accept(self) 
        return exp.op + ". " + str(_e) 
  
    def visitLit(self, lit): 
        return str(lit.val) 
  
  
class PrintPostfix: 
    def visitBinExp(self, exp): 
        _left = exp.left.accept(PrintPostfix()) 
        _right = exp.right.accept(PrintPostfix()) 
        return _left + " " + _right + " " + exp.op 
  
    def visitUnExp(self, exp): 
        _e = exp.e.accept(PrintPostfix()) 
        return str(_e) + " " + exp.op + "." 
  
    def visitLit(self, lit): 
        return str(lit.val) 
  
  
class Lit: 
    def accept(self, cmd): 
        pass 
  
  
class Exp: 
    def accept(self, cmd): 
        pass 
  
  
class IntLit(Lit): 
    def __init__(self, x): 
       self.val = int(x) 

    def accept(self, cmd): 
        return cmd.visitLit(self) 
  
  
class FloatLit(Lit): 
    def __init__(self, x): 
        self.val = float(x) 
 
    def accept(self, cmd): 
        return cmd.visitLit(self) 
  
  
class BinExp(Exp): 
    def __init__(self, left, op: str, right): 
        self.op = op 
        self.left = left 
        self.right = right 
  
    def accept(self, cmd): 
        return cmd.visitBinExp(self) 
  
  
class UnExp(Exp): 
  
    def __init__(self, op: str, e): 
        self.op =op 
        self.e = e 
  
    def accept(self, cmd): 
        return cmd.visitUnExp(self)