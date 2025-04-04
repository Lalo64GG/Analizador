from antlr4 import *
from MiniLenguajeParser import MiniLenguajeParser
from MiniLenguajeVisitor import MiniLenguajeVisitor


class ASTNode:
    def __init__(self, node_type, value=None, children=None):
        self.type = node_type
        self.value = value
        self.children = children if children else []

    def __str__(self):
        return f"{self.type}: {self.value if self.value else ''}"


class ASTBuilder(MiniLenguajeVisitor):
    def __init__(self):
        super().__init__()

    def visitProgram(self, ctx: MiniLenguajeParser.ProgramContext):
        statements = []
        for stmt in ctx.statement():
            statement = self.visit(stmt)
            if statement:
                statements.append(statement)
        return ASTNode('Program', children=statements)

    # Implementa los métodos visit para cada tipo de nodo en la gramática
    def visitVarDeclaration(self, ctx: MiniLenguajeParser.VarDeclarationContext):
        var_type = self.visit(ctx.type_())
        var_name = ctx.ID().getText()
        init_expr = None
        if ctx.expression():
            init_expr = self.visit(ctx.expression())

            # Corregir literales booleanos que se detectaron como identificadores
            if var_type.value == 'bool' and init_expr.type == 'Identifier':
                if init_expr.value == 'true':
                    init_expr = ASTNode('BoolLiteral', True)
                elif init_expr.value == 'false':
                    init_expr = ASTNode('BoolLiteral', False)

        return ASTNode('VarDeclaration', var_name, [var_type, init_expr] if init_expr else [var_type])

    def visitType(self, ctx: MiniLenguajeParser.TypeContext):
        type_text = ctx.getText()
        return ASTNode('Type', type_text)

    def visitAssignment(self, ctx: MiniLenguajeParser.AssignmentContext):
        var_name = ctx.ID().getText()
        expr = self.visit(ctx.expression())

        # Corregir literales booleanos que se detectaron como identificadores
        if expr.type == 'Identifier':
            if expr.value == 'true':
                expr = ASTNode('BoolLiteral', True)
            elif expr.value == 'false':
                expr = ASTNode('BoolLiteral', False)

        return ASTNode('Assignment', var_name, [expr])

    def visitIfStatement(self, ctx: MiniLenguajeParser.IfStatementContext):
        condition = self.visit(ctx.expression())
        then_stmt = self.visit(ctx.statement(0))
        else_stmt = None
        if len(ctx.statement()) > 1:
            else_stmt = self.visit(ctx.statement(1))
        return ASTNode('IfStatement',
                       children=[condition, then_stmt, else_stmt] if else_stmt else [condition, then_stmt])

    def visitWhileStatement(self, ctx: MiniLenguajeParser.WhileStatementContext):
        condition = self.visit(ctx.expression())
        body = self.visit(ctx.statement())
        return ASTNode('WhileStatement', children=[condition, body])

    def visitForStatement(self, ctx: MiniLenguajeParser.ForStatementContext):
        init = self.visit(ctx.getChild(2))
        condition = self.visit(ctx.expression(0))
        update = self.visit(ctx.expression(1))
        body = self.visit(ctx.statement())
        return ASTNode('ForStatement', children=[init, condition, update, body])

    def visitPrintStatement(self, ctx: MiniLenguajeParser.PrintStatementContext):
        expr = self.visit(ctx.expression())
        return ASTNode('PrintStatement', children=[expr])

    def visitInputStatement(self, ctx: MiniLenguajeParser.InputStatementContext):
        var_name = ctx.ID().getText()
        return ASTNode('InputStatement', var_name)

    def visitBlock(self, ctx: MiniLenguajeParser.BlockContext):
        statements = []
        for stmt in ctx.statement():
            statement = self.visit(stmt)
            if statement:
                statements.append(statement)
        return ASTNode('Block', children=statements)

    def visitPrimaryExpr(self, ctx: MiniLenguajeParser.PrimaryExprContext):
        return self.visit(ctx.primary())

    def visitMultDivExpr(self, ctx: MiniLenguajeParser.MultDivExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        op = ctx.op.text
        return ASTNode('BinaryOp', op, [left, right])

    def visitAddSubExpr(self, ctx: MiniLenguajeParser.AddSubExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        op = ctx.op.text
        return ASTNode('BinaryOp', op, [left, right])

    def visitComparisonExpr(self, ctx: MiniLenguajeParser.ComparisonExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        op = ctx.op.text
        return ASTNode('BinaryOp', op, [left, right])

    def visitEqualityExpr(self, ctx: MiniLenguajeParser.EqualityExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        op = ctx.op.text
        return ASTNode('BinaryOp', op, [left, right])

    def visitAndExpr(self, ctx: MiniLenguajeParser.AndExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))

        # Corregir literales booleanos que se detectaron como identificadores
        if left.type == 'Identifier' and left.value in ['true', 'false']:
            left = ASTNode('BoolLiteral', left.value == 'true')
        if right.type == 'Identifier' and right.value in ['true', 'false']:
            right = ASTNode('BoolLiteral', right.value == 'true')

        return ASTNode('BinaryOp', 'and', [left, right])

    def visitOrExpr(self, ctx: MiniLenguajeParser.OrExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))

        # Corregir literales booleanos que se detectaron como identificadores
        if left.type == 'Identifier' and left.value in ['true', 'false']:
            left = ASTNode('BoolLiteral', left.value == 'true')
        if right.type == 'Identifier' and right.value in ['true', 'false']:
            right = ASTNode('BoolLiteral', right.value == 'true')

        return ASTNode('BinaryOp', 'or', [left, right])

    def visitIdExpr(self, ctx: MiniLenguajeParser.IdExprContext):
        id_text = ctx.ID().getText()

        # Detectar y convertir literales booleanos
        if id_text == 'true':
            return ASTNode('BoolLiteral', True)
        elif id_text == 'false':
            return ASTNode('BoolLiteral', False)

        return ASTNode('Identifier', id_text)

    def visitIntLiteral(self, ctx: MiniLenguajeParser.IntLiteralContext):
        return ASTNode('IntLiteral', int(ctx.INT_LITERAL().getText()))

    def visitFloatLiteral(self, ctx: MiniLenguajeParser.FloatLiteralContext):
        return ASTNode('FloatLiteral', float(ctx.FLOAT_LITERAL().getText()))

    def visitStringLiteral(self, ctx: MiniLenguajeParser.StringLiteralContext):
        # Eliminar las comillas del principio y final
        text = ctx.STRING_LITERAL().getText()
        return ASTNode('StringLiteral', text[1:-1])

    def visitBoolLiteral(self, ctx: MiniLenguajeParser.BoolLiteralContext):
        value = ctx.BOOL_LITERAL().getText()
        return ASTNode('BoolLiteral', value == 'true')

    def visitParenExpr(self, ctx: MiniLenguajeParser.ParenExprContext):
        return self.visit(ctx.expression())