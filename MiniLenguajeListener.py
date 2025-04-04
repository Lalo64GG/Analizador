# Generated from MiniLenguaje.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MiniLenguajeParser import MiniLenguajeParser
else:
    from MiniLenguajeParser import MiniLenguajeParser

# This class defines a complete listener for a parse tree produced by MiniLenguajeParser.
class MiniLenguajeListener(ParseTreeListener):

    # Enter a parse tree produced by MiniLenguajeParser#program.
    def enterProgram(self, ctx:MiniLenguajeParser.ProgramContext):
        pass

    # Exit a parse tree produced by MiniLenguajeParser#program.
    def exitProgram(self, ctx:MiniLenguajeParser.ProgramContext):
        pass


    # Enter a parse tree produced by MiniLenguajeParser#statement.
    def enterStatement(self, ctx:MiniLenguajeParser.StatementContext):
        pass

    # Exit a parse tree produced by MiniLenguajeParser#statement.
    def exitStatement(self, ctx:MiniLenguajeParser.StatementContext):
        pass


    # Enter a parse tree produced by MiniLenguajeParser#varDeclaration.
    def enterVarDeclaration(self, ctx:MiniLenguajeParser.VarDeclarationContext):
        pass

    # Exit a parse tree produced by MiniLenguajeParser#varDeclaration.
    def exitVarDeclaration(self, ctx:MiniLenguajeParser.VarDeclarationContext):
        pass


    # Enter a parse tree produced by MiniLenguajeParser#type.
    def enterType(self, ctx:MiniLenguajeParser.TypeContext):
        pass

    # Exit a parse tree produced by MiniLenguajeParser#type.
    def exitType(self, ctx:MiniLenguajeParser.TypeContext):
        pass


    # Enter a parse tree produced by MiniLenguajeParser#assignment.
    def enterAssignment(self, ctx:MiniLenguajeParser.AssignmentContext):
        pass

    # Exit a parse tree produced by MiniLenguajeParser#assignment.
    def exitAssignment(self, ctx:MiniLenguajeParser.AssignmentContext):
        pass


    # Enter a parse tree produced by MiniLenguajeParser#ifStatement.
    def enterIfStatement(self, ctx:MiniLenguajeParser.IfStatementContext):
        pass

    # Exit a parse tree produced by MiniLenguajeParser#ifStatement.
    def exitIfStatement(self, ctx:MiniLenguajeParser.IfStatementContext):
        pass


    # Enter a parse tree produced by MiniLenguajeParser#whileStatement.
    def enterWhileStatement(self, ctx:MiniLenguajeParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by MiniLenguajeParser#whileStatement.
    def exitWhileStatement(self, ctx:MiniLenguajeParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by MiniLenguajeParser#forStatement.
    def enterForStatement(self, ctx:MiniLenguajeParser.ForStatementContext):
        pass

    # Exit a parse tree produced by MiniLenguajeParser#forStatement.
    def exitForStatement(self, ctx:MiniLenguajeParser.ForStatementContext):
        pass


    # Enter a parse tree produced by MiniLenguajeParser#printStatement.
    def enterPrintStatement(self, ctx:MiniLenguajeParser.PrintStatementContext):
        pass

    # Exit a parse tree produced by MiniLenguajeParser#printStatement.
    def exitPrintStatement(self, ctx:MiniLenguajeParser.PrintStatementContext):
        pass


    # Enter a parse tree produced by MiniLenguajeParser#inputStatement.
    def enterInputStatement(self, ctx:MiniLenguajeParser.InputStatementContext):
        pass

    # Exit a parse tree produced by MiniLenguajeParser#inputStatement.
    def exitInputStatement(self, ctx:MiniLenguajeParser.InputStatementContext):
        pass


    # Enter a parse tree produced by MiniLenguajeParser#block.
    def enterBlock(self, ctx:MiniLenguajeParser.BlockContext):
        pass

    # Exit a parse tree produced by MiniLenguajeParser#block.
    def exitBlock(self, ctx:MiniLenguajeParser.BlockContext):
        pass


    # Enter a parse tree produced by MiniLenguajeParser#MultDivExpr.
    def enterMultDivExpr(self, ctx:MiniLenguajeParser.MultDivExprContext):
        pass

    # Exit a parse tree produced by MiniLenguajeParser#MultDivExpr.
    def exitMultDivExpr(self, ctx:MiniLenguajeParser.MultDivExprContext):
        pass


    # Enter a parse tree produced by MiniLenguajeParser#AndExpr.
    def enterAndExpr(self, ctx:MiniLenguajeParser.AndExprContext):
        pass

    # Exit a parse tree produced by MiniLenguajeParser#AndExpr.
    def exitAndExpr(self, ctx:MiniLenguajeParser.AndExprContext):
        pass


    # Enter a parse tree produced by MiniLenguajeParser#EqualityExpr.
    def enterEqualityExpr(self, ctx:MiniLenguajeParser.EqualityExprContext):
        pass

    # Exit a parse tree produced by MiniLenguajeParser#EqualityExpr.
    def exitEqualityExpr(self, ctx:MiniLenguajeParser.EqualityExprContext):
        pass


    # Enter a parse tree produced by MiniLenguajeParser#ComparisonExpr.
    def enterComparisonExpr(self, ctx:MiniLenguajeParser.ComparisonExprContext):
        pass

    # Exit a parse tree produced by MiniLenguajeParser#ComparisonExpr.
    def exitComparisonExpr(self, ctx:MiniLenguajeParser.ComparisonExprContext):
        pass


    # Enter a parse tree produced by MiniLenguajeParser#PrimaryExpr.
    def enterPrimaryExpr(self, ctx:MiniLenguajeParser.PrimaryExprContext):
        pass

    # Exit a parse tree produced by MiniLenguajeParser#PrimaryExpr.
    def exitPrimaryExpr(self, ctx:MiniLenguajeParser.PrimaryExprContext):
        pass


    # Enter a parse tree produced by MiniLenguajeParser#AddSubExpr.
    def enterAddSubExpr(self, ctx:MiniLenguajeParser.AddSubExprContext):
        pass

    # Exit a parse tree produced by MiniLenguajeParser#AddSubExpr.
    def exitAddSubExpr(self, ctx:MiniLenguajeParser.AddSubExprContext):
        pass


    # Enter a parse tree produced by MiniLenguajeParser#OrExpr.
    def enterOrExpr(self, ctx:MiniLenguajeParser.OrExprContext):
        pass

    # Exit a parse tree produced by MiniLenguajeParser#OrExpr.
    def exitOrExpr(self, ctx:MiniLenguajeParser.OrExprContext):
        pass


    # Enter a parse tree produced by MiniLenguajeParser#IdExpr.
    def enterIdExpr(self, ctx:MiniLenguajeParser.IdExprContext):
        pass

    # Exit a parse tree produced by MiniLenguajeParser#IdExpr.
    def exitIdExpr(self, ctx:MiniLenguajeParser.IdExprContext):
        pass


    # Enter a parse tree produced by MiniLenguajeParser#IntLiteral.
    def enterIntLiteral(self, ctx:MiniLenguajeParser.IntLiteralContext):
        pass

    # Exit a parse tree produced by MiniLenguajeParser#IntLiteral.
    def exitIntLiteral(self, ctx:MiniLenguajeParser.IntLiteralContext):
        pass


    # Enter a parse tree produced by MiniLenguajeParser#FloatLiteral.
    def enterFloatLiteral(self, ctx:MiniLenguajeParser.FloatLiteralContext):
        pass

    # Exit a parse tree produced by MiniLenguajeParser#FloatLiteral.
    def exitFloatLiteral(self, ctx:MiniLenguajeParser.FloatLiteralContext):
        pass


    # Enter a parse tree produced by MiniLenguajeParser#StringLiteral.
    def enterStringLiteral(self, ctx:MiniLenguajeParser.StringLiteralContext):
        pass

    # Exit a parse tree produced by MiniLenguajeParser#StringLiteral.
    def exitStringLiteral(self, ctx:MiniLenguajeParser.StringLiteralContext):
        pass


    # Enter a parse tree produced by MiniLenguajeParser#BoolLiteral.
    def enterBoolLiteral(self, ctx:MiniLenguajeParser.BoolLiteralContext):
        pass

    # Exit a parse tree produced by MiniLenguajeParser#BoolLiteral.
    def exitBoolLiteral(self, ctx:MiniLenguajeParser.BoolLiteralContext):
        pass


    # Enter a parse tree produced by MiniLenguajeParser#ParenExpr.
    def enterParenExpr(self, ctx:MiniLenguajeParser.ParenExprContext):
        pass

    # Exit a parse tree produced by MiniLenguajeParser#ParenExpr.
    def exitParenExpr(self, ctx:MiniLenguajeParser.ParenExprContext):
        pass



del MiniLenguajeParser