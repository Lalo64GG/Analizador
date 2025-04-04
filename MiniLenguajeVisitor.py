# Generated from MiniLenguaje.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MiniLenguajeParser import MiniLenguajeParser
else:
    from MiniLenguajeParser import MiniLenguajeParser

# This class defines a complete generic visitor for a parse tree produced by MiniLenguajeParser.

class MiniLenguajeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniLenguajeParser#program.
    def visitProgram(self, ctx:MiniLenguajeParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLenguajeParser#statement.
    def visitStatement(self, ctx:MiniLenguajeParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLenguajeParser#varDeclaration.
    def visitVarDeclaration(self, ctx:MiniLenguajeParser.VarDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLenguajeParser#type.
    def visitType(self, ctx:MiniLenguajeParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLenguajeParser#assignment.
    def visitAssignment(self, ctx:MiniLenguajeParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLenguajeParser#ifStatement.
    def visitIfStatement(self, ctx:MiniLenguajeParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLenguajeParser#whileStatement.
    def visitWhileStatement(self, ctx:MiniLenguajeParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLenguajeParser#forStatement.
    def visitForStatement(self, ctx:MiniLenguajeParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLenguajeParser#printStatement.
    def visitPrintStatement(self, ctx:MiniLenguajeParser.PrintStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLenguajeParser#inputStatement.
    def visitInputStatement(self, ctx:MiniLenguajeParser.InputStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLenguajeParser#block.
    def visitBlock(self, ctx:MiniLenguajeParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLenguajeParser#MultDivExpr.
    def visitMultDivExpr(self, ctx:MiniLenguajeParser.MultDivExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLenguajeParser#AndExpr.
    def visitAndExpr(self, ctx:MiniLenguajeParser.AndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLenguajeParser#EqualityExpr.
    def visitEqualityExpr(self, ctx:MiniLenguajeParser.EqualityExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLenguajeParser#ComparisonExpr.
    def visitComparisonExpr(self, ctx:MiniLenguajeParser.ComparisonExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLenguajeParser#PrimaryExpr.
    def visitPrimaryExpr(self, ctx:MiniLenguajeParser.PrimaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLenguajeParser#AddSubExpr.
    def visitAddSubExpr(self, ctx:MiniLenguajeParser.AddSubExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLenguajeParser#OrExpr.
    def visitOrExpr(self, ctx:MiniLenguajeParser.OrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLenguajeParser#IdExpr.
    def visitIdExpr(self, ctx:MiniLenguajeParser.IdExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLenguajeParser#IntLiteral.
    def visitIntLiteral(self, ctx:MiniLenguajeParser.IntLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLenguajeParser#FloatLiteral.
    def visitFloatLiteral(self, ctx:MiniLenguajeParser.FloatLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLenguajeParser#StringLiteral.
    def visitStringLiteral(self, ctx:MiniLenguajeParser.StringLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLenguajeParser#BoolLiteral.
    def visitBoolLiteral(self, ctx:MiniLenguajeParser.BoolLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLenguajeParser#ParenExpr.
    def visitParenExpr(self, ctx:MiniLenguajeParser.ParenExprContext):
        return self.visitChildren(ctx)



del MiniLenguajeParser