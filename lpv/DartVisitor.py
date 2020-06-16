# Generated from e:\University\6 term\automate_python\Dart.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .DartParser import DartParser
else:
    from DartParser import DartParser

# This class defines a complete generic visitor for a parse tree produced by DartParser.

class DartVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by DartParser#start.
    def visitStart(self, ctx:DartParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DartParser#declare.
    def visitDeclare(self, ctx:DartParser.DeclareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DartParser#typeName.
    def visitTypeName(self, ctx:DartParser.TypeNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DartParser#statementSeq.
    def visitStatementSeq(self, ctx:DartParser.StatementSeqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DartParser#statement.
    def visitStatement(self, ctx:DartParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DartParser#simpleStatement.
    def visitSimpleStatement(self, ctx:DartParser.SimpleStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DartParser#complexStatement.
    def visitComplexStatement(self, ctx:DartParser.ComplexStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DartParser#let.
    def visitLet(self, ctx:DartParser.LetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DartParser#keyboardIn.
    def visitKeyboardIn(self, ctx:DartParser.KeyboardInContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DartParser#out.
    def visitOut(self, ctx:DartParser.OutContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DartParser#ifC.
    def visitIfC(self, ctx:DartParser.IfCContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DartParser#whileC.
    def visitWhileC(self, ctx:DartParser.WhileCContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DartParser#exp.
    def visitExp(self, ctx:DartParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DartParser#simpleExpr.
    def visitSimpleExpr(self, ctx:DartParser.SimpleExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DartParser#term.
    def visitTerm(self, ctx:DartParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DartParser#signedFactor.
    def visitSignedFactor(self, ctx:DartParser.SignedFactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DartParser#factor.
    def visitFactor(self, ctx:DartParser.FactorContext):
        return self.visitChildren(ctx)



del DartParser