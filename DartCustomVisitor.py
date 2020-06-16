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
        varName = ctx.Id().getText()
        if varName in self.variables:
            raise Exception('Variable ' + varName + ' already exists')

        typeName = ctx.typeName().getText()
        
        # Сделать чтобы exp возвращало готовое значение
        value = 0
        if ctx.exp():
            value = self.visitExp(ctx.exp())
            if type(value) is bool:
                raise Exception("A value of conditional  can't be assigned to a variable of type 'int'/'real'.")
        # Приводится даже если 0, чтобы в visitLet можно было отследить тип
        if typeName == 'int':
            value = int(value)
        elif typeName == 'real':
            value = float(value)
        
        self.variables[varName] = value
        print('declare', value)
        print('var', self.variables[varName])

    # Visit a parse tree produced by DartParser#let.
    def visitLet(self, ctx:DartParser.LetContext):
        varName = ctx.Id().getText()
        if varName not in self.variables:
            raise Exception('Let with unknown variable: ' + varName)
        
        if type(self.variables[varName]) is int:
            self.variables[varName] = int(self.visitExp(ctx.exp()))
        elif type(self.variables[varName]) is float:
            self.variables[varName] = float(self.visitExp(ctx.exp()))
        print('var', self.variables[varName])


    # Visit a parse tree produced by DartParser#in.
    def visitKeyboardIn(self, ctx:DartParser.KeyboardInContext):
        varName = ctx.Id().getText()
        if varName not in self.variables:
            raise Exception('Input in unknown variable: ' + varName)
        
        value = input('> ')

        if type(self.variables[varName]) is int:
            self.variables[varName] = int(value)
        elif type(self.variables[varName]) is float:
            self.variables[varName] = float(value)


    # Visit a parse tree produced by DartParser#out.
    def visitOut(self, ctx:DartParser.OutContext):
        print(self.variables[ctx.Id().getText()])


    # Visit a parse tree produced by DartParser#ifC.
    def visitIfC(self, ctx:DartParser.IfCContext):
        expResult = self.visitExp(ctx.exp())
        if type(expResult) is not bool:
            raise Exception("Non conditional expression in 'if'")
        if expResult:
            self.visitStatementSeq(ctx.statementSeq(0))
        elif ctx.Else():
            self.visitStatementSeq(ctx.statementSeq(1))


    # Visit a parse tree produced by DartParser#whileC.
    def visitWhileC(self, ctx:DartParser.WhileCContext):
        if type(self.visitExp(ctx.exp())) is not bool:
            raise Exception("Non conditional expression in 'if'")
        while self.visitExp(ctx.exp()):
            self.visitChildren(ctx)


    # Visit a parse tree produced by DartParser#exp.
    def visitExp(self, ctx:DartParser.ExpContext):
        lhs = self.visitSimpleExpr(ctx.simpleExpr())
        if ctx.exp():
            rhs = self.visitExp(ctx.exp())
            
            if ctx.BoolEq():
                return lhs == rhs
            if ctx.BoolNeq():
                return lhs != rhs

            if type(lhs) is not bool and type(rhs) is not bool:
                if ctx.BoolG():
                    return lhs > rhs
                if ctx.BoolL():
                    return lhs < rhs
                if ctx.BoolLeq():
                    return lhs <= rhs
                if ctx.BoolGeq():
                    return lhs >= rhs
            else:
                raise Exception('Less/Greater between bool operands')
        return lhs


    # Visit a parse tree produced by DartParser#simpleExpr.
    def visitSimpleExpr(self, ctx:DartParser.SimpleExprContext):
        lhs = self.visitTerm(ctx.term())
        if ctx.simpleExpr():
            rhs = self.visitSimpleExpr(ctx.simpleExpr())
            
            if type(lhs) is bool and type(rhs) is bool:
                if ctx.BoolOr():
                    return lhs or rhs
                else:
                    raise Exception('Arithm operation between conditional   operands')

            if type(lhs) is bool or type(rhs) is bool:
                raise Exception('Operation between bool and non-bool operands')

            if ctx.AddOp():
                return lhs + rhs
            if ctx.SubOp():
                return lhs - rhs

        return lhs


    # Visit a parse tree produced by DartParser#term.
    def visitTerm(self, ctx:DartParser.TermContext):
        lhs = self.visitSignedFactor(ctx.signedFactor())
        if ctx.term():
            rhs = self.visitTerm(ctx.term())
            
            if type(lhs) is bool and type(rhs) is bool:
                if ctx.BoolAnd():
                    return lhs and rhs
                else:
                    raise Exception('Arithm operation between conditional  operands')

            if type(lhs) is bool or type(rhs) is bool:
                raise Exception('Operation between bool and non-bool operands')

            if ctx.MulOp():
                return lhs * rhs
            if ctx.DivOp():
                return lhs / rhs

        return lhs


    # Visit a parse tree produced by DartParser#signedFactor.
    def visitSignedFactor(self, ctx:DartParser.SignedFactorContext):
        subOp = ctx.SubOp()
        factor = self.visitFactor(ctx.factor())
        '''
            Если в visitFactor вернул bool,
            то в factor было логическое выражение
            и перед ним стоит минус, значит вызываем исключение
        '''
        if type(factor) is bool:
            if subOp:
                raise Exception('Minus before conditional  expression')
        '''
            Если мы тут, то visitFactor вернул число
            Проверяем знак
        '''
        if subOp:
            factor = -factor

        return factor


    # Visit a parse tree produced by DartParser#factor.
    def visitFactor(self, ctx:DartParser.FactorContext):
        factor = ctx.getText();

        if ctx.Id():
            key = ctx.Id().getText()
            if key in self.variables:
                return self.variables[key]
            else:
                raise Exception('Variable ' + key + ' doesnt exists')

        if ctx.IntValue():
            return int(factor)
        if ctx.RealValue():
            return float(factor)

        return visitChildren(ctx)
