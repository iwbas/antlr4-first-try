from antlr4 import *
from lpv.DartVisitor import DartVisitor

if __name__ is not None and "." in __name__:
    from lpv.DartParser import DartParser
else:
    from lpv.DartParser import DartParser

import operator


class DartCustomVisitor(DartVisitor):

    def __init__(self):
        self.variables = dict()

    def visitStart(self, ctx:DartParser.StartContext):
        print('start')
        return self.visitChildren(ctx)
    
    # Visit a parse tree produced by DartParser#declare.
    def visitDeclare(self, ctx:DartParser.DeclareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DartParser#arithExp.
    def visitArithExp(self, ctx:DartParser.ArithExpContext):
        lhs = self.visitTerm(ctx.term())

        print(type(lhs))
        if ctx.arithExp():
            rhs = self.visitArithExp(ctx.arithExp())
            if ctx.AddOp():
                return lhs + rhs
            if ctx.SubOp():
                return lhs / rhs

        return lhs


    # Visit a parse tree produced by DartParser#term.
    def visitTerm(self, ctx:DartParser.TermContext):
        lhs = self.visitSignedFactor(ctx.signedFactor())
        if ctx.term():
            rhs = self.visitTerm(ctx.term())
            if ctx.MulOp():
                return lhs * rhs
            if ctx.DivOp():
                return lhs / rhs
        
        return lhs

    # Visit a parse tree produced by DartParser#signedFactor.
    def visitSignedFactor(self, ctx:DartParser.SignedFactorContext):
        factor = self.visitFactor(ctx.factor())
        return -factor if ctx.SubOp() else factor


    # Visit a parse tree produced by DartParser#factor.
    def visitFactor(self, ctx:DartParser.FactorContext):
        factor = ctx.getText()

        # return exp

        # if ctx.Id():
        #     key = ctx.Id().getText()
        #     if key in self.variables:
        #         return dict[key]
        #     else:
        #         raise Exception('Variable ' + key + ' doesnt exists')

        if ctx.IntValue():
            return int(factor)
        if ctx.RealValue():
            return float(factor)

        return self.visitChildren(ctx)