#update: 02/04/2022
from abc import ABC
from AST import *

class Kind(ABC):
    pass

class Class(Kind):
    def __str__(self):
        return "Class"

class Method(Kind):
    def __str__(self):
        return "Method"

class SpecialMethod(Kind):
    def __str__(self):
        return "Special Method"

class Attribute(Kind):
    def __str__(self):
        return "Attribute"

class Parameter(Kind):
    def __str__(self):
        return "Parameter"

class Constant(Kind):
    def __str__(self):
        return "Constant"

class Variable(Kind):
    def __str__(self):
        return "Variable"

class Identifier(Kind):
    def __str__(self):
        return "Identifier"

class StaticError(Exception):
    pass


class Undeclared(StaticError):
    def __init__(self, k, n):
        self.k = k
        self.n = n

    def __str__(self):
        return  "Undeclared "+ str(self.k) + ": " + self.n


class Redeclared(StaticError):
    def __init__(self, k, n):
        self.k = k
        self.n = n

    def __str__(self):
        return  "Redeclared "+ str(self.k) + ": " + self.n


class TypeMismatchInExpression(StaticError):
    def __init__(self, e):
        self.exp = e

    def __str__(self):
        return  "Type Mismatch In Expression: "+ str(self.exp)


class TypeMismatchInStatement(StaticError):
    def __init__(self, s):
        self.stmt = s

    def __str__(self):
        return "Type Mismatch In Statement: "+ str(self.stmt)


class CannotAssignToConstant(StaticError):
    def __init__(self, s):
        self.stmt = s

    def __str__(self):
        return "Cannot Assign To Constant: "+ str(self.stmt)


class TypeMismatchInConstant(StaticError):
    def __init__(self, c):
        self.constdecl = c

    def __str__(self):
        return "Type Mismatch In Constant Declaration: "+ str(self.constdecl)


class MustInLoop(StaticError):
    def __init__(self, s):
        self.stmt = s
        
    def __str__(self):
        return str(self.stmt) + " Not In Loop"


class IllegalConstantExpression(StaticError):
    def __init__(self, e):
        self.expr = e

    def __str__(self):
        return "Illegal Constant Expression: "+ str(self.expr)


class IllegalArrayLiteral(StaticError):
    def __init__(self, a):
        self.arr = a

    def __str__(self):
        return "Illegal Array Literal: "+ str(self.arr)


class IllegalMemberAccess(StaticError):
    def __init__(self, e):
        self.expr = e

    def __str__(self):
        return "Illegal Member Access: " + str(self.expr)


class NoEntryPoint(StaticError):
    def __str__(self):
        return "No Entry Point"
