# Generated from MiniLenguaje.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,37,145,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,4,0,
        28,8,0,11,0,12,0,29,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,
        42,8,1,1,2,1,2,1,2,1,2,3,2,48,8,2,1,2,1,2,1,3,1,3,1,4,1,4,1,4,1,
        4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,66,8,5,1,6,1,6,1,6,1,6,1,6,
        1,6,1,7,1,7,1,7,1,7,1,7,3,7,79,8,7,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,
        8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,5,10,101,8,10,
        10,10,12,10,104,9,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
        1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
        1,11,5,11,129,8,11,10,11,12,11,132,9,11,1,12,1,12,1,12,1,12,1,12,
        1,12,1,12,1,12,1,12,3,12,143,8,12,1,12,0,1,22,13,0,2,4,6,8,10,12,
        14,16,18,20,22,24,0,5,1,0,8,11,1,0,14,15,1,0,12,13,1,0,19,22,1,0,
        17,18,155,0,27,1,0,0,0,2,41,1,0,0,0,4,43,1,0,0,0,6,51,1,0,0,0,8,
        53,1,0,0,0,10,58,1,0,0,0,12,67,1,0,0,0,14,73,1,0,0,0,16,86,1,0,0,
        0,18,92,1,0,0,0,20,98,1,0,0,0,22,107,1,0,0,0,24,142,1,0,0,0,26,28,
        3,2,1,0,27,26,1,0,0,0,28,29,1,0,0,0,29,27,1,0,0,0,29,30,1,0,0,0,
        30,31,1,0,0,0,31,32,5,0,0,1,32,1,1,0,0,0,33,42,3,4,2,0,34,42,3,8,
        4,0,35,42,3,10,5,0,36,42,3,12,6,0,37,42,3,14,7,0,38,42,3,16,8,0,
        39,42,3,18,9,0,40,42,3,20,10,0,41,33,1,0,0,0,41,34,1,0,0,0,41,35,
        1,0,0,0,41,36,1,0,0,0,41,37,1,0,0,0,41,38,1,0,0,0,41,39,1,0,0,0,
        41,40,1,0,0,0,42,3,1,0,0,0,43,44,3,6,3,0,44,47,5,31,0,0,45,46,5,
        16,0,0,46,48,3,22,11,0,47,45,1,0,0,0,47,48,1,0,0,0,48,49,1,0,0,0,
        49,50,5,25,0,0,50,5,1,0,0,0,51,52,7,0,0,0,52,7,1,0,0,0,53,54,5,31,
        0,0,54,55,5,16,0,0,55,56,3,22,11,0,56,57,5,25,0,0,57,9,1,0,0,0,58,
        59,5,2,0,0,59,60,5,27,0,0,60,61,3,22,11,0,61,62,5,28,0,0,62,65,3,
        2,1,0,63,64,5,3,0,0,64,66,3,2,1,0,65,63,1,0,0,0,65,66,1,0,0,0,66,
        11,1,0,0,0,67,68,5,4,0,0,68,69,5,27,0,0,69,70,3,22,11,0,70,71,5,
        28,0,0,71,72,3,2,1,0,72,13,1,0,0,0,73,74,5,5,0,0,74,78,5,27,0,0,
        75,79,3,4,2,0,76,79,3,8,4,0,77,79,5,25,0,0,78,75,1,0,0,0,78,76,1,
        0,0,0,78,77,1,0,0,0,79,80,1,0,0,0,80,81,3,22,11,0,81,82,5,25,0,0,
        82,83,3,22,11,0,83,84,5,28,0,0,84,85,3,2,1,0,85,15,1,0,0,0,86,87,
        5,6,0,0,87,88,5,27,0,0,88,89,3,22,11,0,89,90,5,28,0,0,90,91,5,25,
        0,0,91,17,1,0,0,0,92,93,5,7,0,0,93,94,5,27,0,0,94,95,5,31,0,0,95,
        96,5,28,0,0,96,97,5,25,0,0,97,19,1,0,0,0,98,102,5,29,0,0,99,101,
        3,2,1,0,100,99,1,0,0,0,101,104,1,0,0,0,102,100,1,0,0,0,102,103,1,
        0,0,0,103,105,1,0,0,0,104,102,1,0,0,0,105,106,5,30,0,0,106,21,1,
        0,0,0,107,108,6,11,-1,0,108,109,3,24,12,0,109,130,1,0,0,0,110,111,
        10,6,0,0,111,112,7,1,0,0,112,129,3,22,11,7,113,114,10,5,0,0,114,
        115,7,2,0,0,115,129,3,22,11,6,116,117,10,4,0,0,117,118,7,3,0,0,118,
        129,3,22,11,5,119,120,10,3,0,0,120,121,7,4,0,0,121,129,3,22,11,4,
        122,123,10,2,0,0,123,124,5,23,0,0,124,129,3,22,11,3,125,126,10,1,
        0,0,126,127,5,24,0,0,127,129,3,22,11,2,128,110,1,0,0,0,128,113,1,
        0,0,0,128,116,1,0,0,0,128,119,1,0,0,0,128,122,1,0,0,0,128,125,1,
        0,0,0,129,132,1,0,0,0,130,128,1,0,0,0,130,131,1,0,0,0,131,23,1,0,
        0,0,132,130,1,0,0,0,133,143,5,31,0,0,134,143,5,32,0,0,135,143,5,
        33,0,0,136,143,5,34,0,0,137,143,5,35,0,0,138,139,5,27,0,0,139,140,
        3,22,11,0,140,141,5,28,0,0,141,143,1,0,0,0,142,133,1,0,0,0,142,134,
        1,0,0,0,142,135,1,0,0,0,142,136,1,0,0,0,142,137,1,0,0,0,142,138,
        1,0,0,0,143,25,1,0,0,0,9,29,41,47,65,78,102,128,130,142
    ]

class MiniLenguajeParser ( Parser ):

    grammarFileName = "MiniLenguaje.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'var'", "'if'", "'else'", "'while'", 
                     "'for'", "'print'", "'input'", "'int'", "'float'", 
                     "'string'", "'bool'", "'+'", "'-'", "'*'", "'/'", "'='", 
                     "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "'and'", 
                     "'or'", "';'", "','", "'('", "')'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "VAR", "IF", "ELSE", "WHILE", "FOR", 
                      "PRINT", "INPUT", "INT_TYPE", "FLOAT_TYPE", "STRING_TYPE", 
                      "BOOL_TYPE", "PLUS", "MINUS", "MUL", "DIV", "ASSIGN", 
                      "EQ", "NEQ", "LT", "GT", "LE", "GE", "AND", "OR", 
                      "SEMICOLON", "COMMA", "LPAREN", "RPAREN", "LBRACE", 
                      "RBRACE", "ID", "INT_LITERAL", "FLOAT_LITERAL", "STRING_LITERAL", 
                      "BOOL_LITERAL", "WS", "COMMENT" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_varDeclaration = 2
    RULE_type = 3
    RULE_assignment = 4
    RULE_ifStatement = 5
    RULE_whileStatement = 6
    RULE_forStatement = 7
    RULE_printStatement = 8
    RULE_inputStatement = 9
    RULE_block = 10
    RULE_expression = 11
    RULE_primary = 12

    ruleNames =  [ "program", "statement", "varDeclaration", "type", "assignment", 
                   "ifStatement", "whileStatement", "forStatement", "printStatement", 
                   "inputStatement", "block", "expression", "primary" ]

    EOF = Token.EOF
    VAR=1
    IF=2
    ELSE=3
    WHILE=4
    FOR=5
    PRINT=6
    INPUT=7
    INT_TYPE=8
    FLOAT_TYPE=9
    STRING_TYPE=10
    BOOL_TYPE=11
    PLUS=12
    MINUS=13
    MUL=14
    DIV=15
    ASSIGN=16
    EQ=17
    NEQ=18
    LT=19
    GT=20
    LE=21
    GE=22
    AND=23
    OR=24
    SEMICOLON=25
    COMMA=26
    LPAREN=27
    RPAREN=28
    LBRACE=29
    RBRACE=30
    ID=31
    INT_LITERAL=32
    FLOAT_LITERAL=33
    STRING_LITERAL=34
    BOOL_LITERAL=35
    WS=36
    COMMENT=37

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MiniLenguajeParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLenguajeParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniLenguajeParser.StatementContext,i)


        def getRuleIndex(self):
            return MiniLenguajeParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniLenguajeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 26
                self.statement()
                self.state = 29 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2684358644) != 0)):
                    break

            self.state = 31
            self.match(MiniLenguajeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDeclaration(self):
            return self.getTypedRuleContext(MiniLenguajeParser.VarDeclarationContext,0)


        def assignment(self):
            return self.getTypedRuleContext(MiniLenguajeParser.AssignmentContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(MiniLenguajeParser.IfStatementContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(MiniLenguajeParser.WhileStatementContext,0)


        def forStatement(self):
            return self.getTypedRuleContext(MiniLenguajeParser.ForStatementContext,0)


        def printStatement(self):
            return self.getTypedRuleContext(MiniLenguajeParser.PrintStatementContext,0)


        def inputStatement(self):
            return self.getTypedRuleContext(MiniLenguajeParser.InputStatementContext,0)


        def block(self):
            return self.getTypedRuleContext(MiniLenguajeParser.BlockContext,0)


        def getRuleIndex(self):
            return MiniLenguajeParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MiniLenguajeParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 41
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8, 9, 10, 11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 33
                self.varDeclaration()
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 2)
                self.state = 34
                self.assignment()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 3)
                self.state = 35
                self.ifStatement()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 4)
                self.state = 36
                self.whileStatement()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 5)
                self.state = 37
                self.forStatement()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 6)
                self.state = 38
                self.printStatement()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 7)
                self.state = 39
                self.inputStatement()
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 8)
                self.state = 40
                self.block()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(MiniLenguajeParser.TypeContext,0)


        def ID(self):
            return self.getToken(MiniLenguajeParser.ID, 0)

        def SEMICOLON(self):
            return self.getToken(MiniLenguajeParser.SEMICOLON, 0)

        def ASSIGN(self):
            return self.getToken(MiniLenguajeParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniLenguajeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniLenguajeParser.RULE_varDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDeclaration" ):
                listener.enterVarDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDeclaration" ):
                listener.exitVarDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDeclaration" ):
                return visitor.visitVarDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def varDeclaration(self):

        localctx = MiniLenguajeParser.VarDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_varDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.type_()
            self.state = 44
            self.match(MiniLenguajeParser.ID)
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 45
                self.match(MiniLenguajeParser.ASSIGN)
                self.state = 46
                self.expression(0)


            self.state = 49
            self.match(MiniLenguajeParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_TYPE(self):
            return self.getToken(MiniLenguajeParser.INT_TYPE, 0)

        def FLOAT_TYPE(self):
            return self.getToken(MiniLenguajeParser.FLOAT_TYPE, 0)

        def STRING_TYPE(self):
            return self.getToken(MiniLenguajeParser.STRING_TYPE, 0)

        def BOOL_TYPE(self):
            return self.getToken(MiniLenguajeParser.BOOL_TYPE, 0)

        def getRuleIndex(self):
            return MiniLenguajeParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = MiniLenguajeParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3840) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniLenguajeParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(MiniLenguajeParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniLenguajeParser.ExpressionContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniLenguajeParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniLenguajeParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = MiniLenguajeParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(MiniLenguajeParser.ID)
            self.state = 54
            self.match(MiniLenguajeParser.ASSIGN)
            self.state = 55
            self.expression(0)
            self.state = 56
            self.match(MiniLenguajeParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MiniLenguajeParser.IF, 0)

        def LPAREN(self):
            return self.getToken(MiniLenguajeParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniLenguajeParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MiniLenguajeParser.RPAREN, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLenguajeParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniLenguajeParser.StatementContext,i)


        def ELSE(self):
            return self.getToken(MiniLenguajeParser.ELSE, 0)

        def getRuleIndex(self):
            return MiniLenguajeParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = MiniLenguajeParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_ifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(MiniLenguajeParser.IF)
            self.state = 59
            self.match(MiniLenguajeParser.LPAREN)
            self.state = 60
            self.expression(0)
            self.state = 61
            self.match(MiniLenguajeParser.RPAREN)
            self.state = 62
            self.statement()
            self.state = 65
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 63
                self.match(MiniLenguajeParser.ELSE)
                self.state = 64
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(MiniLenguajeParser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(MiniLenguajeParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniLenguajeParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MiniLenguajeParser.RPAREN, 0)

        def statement(self):
            return self.getTypedRuleContext(MiniLenguajeParser.StatementContext,0)


        def getRuleIndex(self):
            return MiniLenguajeParser.RULE_whileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStatement" ):
                return visitor.visitWhileStatement(self)
            else:
                return visitor.visitChildren(self)




    def whileStatement(self):

        localctx = MiniLenguajeParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(MiniLenguajeParser.WHILE)
            self.state = 68
            self.match(MiniLenguajeParser.LPAREN)
            self.state = 69
            self.expression(0)
            self.state = 70
            self.match(MiniLenguajeParser.RPAREN)
            self.state = 71
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniLenguajeParser.FOR, 0)

        def LPAREN(self):
            return self.getToken(MiniLenguajeParser.LPAREN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLenguajeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniLenguajeParser.ExpressionContext,i)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLenguajeParser.SEMICOLON)
            else:
                return self.getToken(MiniLenguajeParser.SEMICOLON, i)

        def RPAREN(self):
            return self.getToken(MiniLenguajeParser.RPAREN, 0)

        def statement(self):
            return self.getTypedRuleContext(MiniLenguajeParser.StatementContext,0)


        def varDeclaration(self):
            return self.getTypedRuleContext(MiniLenguajeParser.VarDeclarationContext,0)


        def assignment(self):
            return self.getTypedRuleContext(MiniLenguajeParser.AssignmentContext,0)


        def getRuleIndex(self):
            return MiniLenguajeParser.RULE_forStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStatement" ):
                listener.enterForStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStatement" ):
                listener.exitForStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStatement" ):
                return visitor.visitForStatement(self)
            else:
                return visitor.visitChildren(self)




    def forStatement(self):

        localctx = MiniLenguajeParser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_forStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(MiniLenguajeParser.FOR)
            self.state = 74
            self.match(MiniLenguajeParser.LPAREN)
            self.state = 78
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8, 9, 10, 11]:
                self.state = 75
                self.varDeclaration()
                pass
            elif token in [31]:
                self.state = 76
                self.assignment()
                pass
            elif token in [25]:
                self.state = 77
                self.match(MiniLenguajeParser.SEMICOLON)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 80
            self.expression(0)
            self.state = 81
            self.match(MiniLenguajeParser.SEMICOLON)
            self.state = 82
            self.expression(0)
            self.state = 83
            self.match(MiniLenguajeParser.RPAREN)
            self.state = 84
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(MiniLenguajeParser.PRINT, 0)

        def LPAREN(self):
            return self.getToken(MiniLenguajeParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniLenguajeParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MiniLenguajeParser.RPAREN, 0)

        def SEMICOLON(self):
            return self.getToken(MiniLenguajeParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniLenguajeParser.RULE_printStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStatement" ):
                listener.enterPrintStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStatement" ):
                listener.exitPrintStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStatement" ):
                return visitor.visitPrintStatement(self)
            else:
                return visitor.visitChildren(self)




    def printStatement(self):

        localctx = MiniLenguajeParser.PrintStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_printStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(MiniLenguajeParser.PRINT)
            self.state = 87
            self.match(MiniLenguajeParser.LPAREN)
            self.state = 88
            self.expression(0)
            self.state = 89
            self.match(MiniLenguajeParser.RPAREN)
            self.state = 90
            self.match(MiniLenguajeParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InputStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INPUT(self):
            return self.getToken(MiniLenguajeParser.INPUT, 0)

        def LPAREN(self):
            return self.getToken(MiniLenguajeParser.LPAREN, 0)

        def ID(self):
            return self.getToken(MiniLenguajeParser.ID, 0)

        def RPAREN(self):
            return self.getToken(MiniLenguajeParser.RPAREN, 0)

        def SEMICOLON(self):
            return self.getToken(MiniLenguajeParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniLenguajeParser.RULE_inputStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInputStatement" ):
                listener.enterInputStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInputStatement" ):
                listener.exitInputStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInputStatement" ):
                return visitor.visitInputStatement(self)
            else:
                return visitor.visitChildren(self)




    def inputStatement(self):

        localctx = MiniLenguajeParser.InputStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_inputStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(MiniLenguajeParser.INPUT)
            self.state = 93
            self.match(MiniLenguajeParser.LPAREN)
            self.state = 94
            self.match(MiniLenguajeParser.ID)
            self.state = 95
            self.match(MiniLenguajeParser.RPAREN)
            self.state = 96
            self.match(MiniLenguajeParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(MiniLenguajeParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniLenguajeParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLenguajeParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniLenguajeParser.StatementContext,i)


        def getRuleIndex(self):
            return MiniLenguajeParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = MiniLenguajeParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(MiniLenguajeParser.LBRACE)
            self.state = 102
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2684358644) != 0):
                self.state = 99
                self.statement()
                self.state = 104
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 105
            self.match(MiniLenguajeParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniLenguajeParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class MultDivExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLenguajeParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLenguajeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniLenguajeParser.ExpressionContext,i)

        def MUL(self):
            return self.getToken(MiniLenguajeParser.MUL, 0)
        def DIV(self):
            return self.getToken(MiniLenguajeParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultDivExpr" ):
                listener.enterMultDivExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultDivExpr" ):
                listener.exitMultDivExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultDivExpr" ):
                return visitor.visitMultDivExpr(self)
            else:
                return visitor.visitChildren(self)


    class AndExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLenguajeParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLenguajeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniLenguajeParser.ExpressionContext,i)

        def AND(self):
            return self.getToken(MiniLenguajeParser.AND, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndExpr" ):
                listener.enterAndExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndExpr" ):
                listener.exitAndExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndExpr" ):
                return visitor.visitAndExpr(self)
            else:
                return visitor.visitChildren(self)


    class EqualityExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLenguajeParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLenguajeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniLenguajeParser.ExpressionContext,i)

        def EQ(self):
            return self.getToken(MiniLenguajeParser.EQ, 0)
        def NEQ(self):
            return self.getToken(MiniLenguajeParser.NEQ, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqualityExpr" ):
                listener.enterEqualityExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqualityExpr" ):
                listener.exitEqualityExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqualityExpr" ):
                return visitor.visitEqualityExpr(self)
            else:
                return visitor.visitChildren(self)


    class ComparisonExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLenguajeParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLenguajeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniLenguajeParser.ExpressionContext,i)

        def LT(self):
            return self.getToken(MiniLenguajeParser.LT, 0)
        def GT(self):
            return self.getToken(MiniLenguajeParser.GT, 0)
        def LE(self):
            return self.getToken(MiniLenguajeParser.LE, 0)
        def GE(self):
            return self.getToken(MiniLenguajeParser.GE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparisonExpr" ):
                listener.enterComparisonExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparisonExpr" ):
                listener.exitComparisonExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparisonExpr" ):
                return visitor.visitComparisonExpr(self)
            else:
                return visitor.visitChildren(self)


    class PrimaryExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLenguajeParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def primary(self):
            return self.getTypedRuleContext(MiniLenguajeParser.PrimaryContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimaryExpr" ):
                listener.enterPrimaryExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimaryExpr" ):
                listener.exitPrimaryExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaryExpr" ):
                return visitor.visitPrimaryExpr(self)
            else:
                return visitor.visitChildren(self)


    class AddSubExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLenguajeParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLenguajeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniLenguajeParser.ExpressionContext,i)

        def PLUS(self):
            return self.getToken(MiniLenguajeParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(MiniLenguajeParser.MINUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSubExpr" ):
                listener.enterAddSubExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSubExpr" ):
                listener.exitAddSubExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSubExpr" ):
                return visitor.visitAddSubExpr(self)
            else:
                return visitor.visitChildren(self)


    class OrExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLenguajeParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLenguajeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniLenguajeParser.ExpressionContext,i)

        def OR(self):
            return self.getToken(MiniLenguajeParser.OR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrExpr" ):
                listener.enterOrExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrExpr" ):
                listener.exitOrExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrExpr" ):
                return visitor.visitOrExpr(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniLenguajeParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MiniLenguajeParser.PrimaryExprContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 108
            self.primary()
            self._ctx.stop = self._input.LT(-1)
            self.state = 130
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 128
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = MiniLenguajeParser.MultDivExprContext(self, MiniLenguajeParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 110
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 111
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==14 or _la==15):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 112
                        self.expression(7)
                        pass

                    elif la_ == 2:
                        localctx = MiniLenguajeParser.AddSubExprContext(self, MiniLenguajeParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 113
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 114
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==12 or _la==13):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 115
                        self.expression(6)
                        pass

                    elif la_ == 3:
                        localctx = MiniLenguajeParser.ComparisonExprContext(self, MiniLenguajeParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 116
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 117
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7864320) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 118
                        self.expression(5)
                        pass

                    elif la_ == 4:
                        localctx = MiniLenguajeParser.EqualityExprContext(self, MiniLenguajeParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 119
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 120
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==17 or _la==18):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 121
                        self.expression(4)
                        pass

                    elif la_ == 5:
                        localctx = MiniLenguajeParser.AndExprContext(self, MiniLenguajeParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 122
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 123
                        self.match(MiniLenguajeParser.AND)
                        self.state = 124
                        self.expression(3)
                        pass

                    elif la_ == 6:
                        localctx = MiniLenguajeParser.OrExprContext(self, MiniLenguajeParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 125
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 126
                        self.match(MiniLenguajeParser.OR)
                        self.state = 127
                        self.expression(2)
                        pass

             
                self.state = 132
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class PrimaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniLenguajeParser.RULE_primary

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IdExprContext(PrimaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLenguajeParser.PrimaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(MiniLenguajeParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdExpr" ):
                listener.enterIdExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdExpr" ):
                listener.exitIdExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdExpr" ):
                return visitor.visitIdExpr(self)
            else:
                return visitor.visitChildren(self)


    class StringLiteralContext(PrimaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLenguajeParser.PrimaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING_LITERAL(self):
            return self.getToken(MiniLenguajeParser.STRING_LITERAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringLiteral" ):
                listener.enterStringLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringLiteral" ):
                listener.exitStringLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringLiteral" ):
                return visitor.visitStringLiteral(self)
            else:
                return visitor.visitChildren(self)


    class BoolLiteralContext(PrimaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLenguajeParser.PrimaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOOL_LITERAL(self):
            return self.getToken(MiniLenguajeParser.BOOL_LITERAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolLiteral" ):
                listener.enterBoolLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolLiteral" ):
                listener.exitBoolLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolLiteral" ):
                return visitor.visitBoolLiteral(self)
            else:
                return visitor.visitChildren(self)


    class FloatLiteralContext(PrimaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLenguajeParser.PrimaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT_LITERAL(self):
            return self.getToken(MiniLenguajeParser.FLOAT_LITERAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloatLiteral" ):
                listener.enterFloatLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloatLiteral" ):
                listener.exitFloatLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloatLiteral" ):
                return visitor.visitFloatLiteral(self)
            else:
                return visitor.visitChildren(self)


    class IntLiteralContext(PrimaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLenguajeParser.PrimaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT_LITERAL(self):
            return self.getToken(MiniLenguajeParser.INT_LITERAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntLiteral" ):
                listener.enterIntLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntLiteral" ):
                listener.exitIntLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntLiteral" ):
                return visitor.visitIntLiteral(self)
            else:
                return visitor.visitChildren(self)


    class ParenExprContext(PrimaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLenguajeParser.PrimaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(MiniLenguajeParser.LPAREN, 0)
        def expression(self):
            return self.getTypedRuleContext(MiniLenguajeParser.ExpressionContext,0)

        def RPAREN(self):
            return self.getToken(MiniLenguajeParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenExpr" ):
                listener.enterParenExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenExpr" ):
                listener.exitParenExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenExpr" ):
                return visitor.visitParenExpr(self)
            else:
                return visitor.visitChildren(self)



    def primary(self):

        localctx = MiniLenguajeParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_primary)
        try:
            self.state = 142
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                localctx = MiniLenguajeParser.IdExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                self.match(MiniLenguajeParser.ID)
                pass
            elif token in [32]:
                localctx = MiniLenguajeParser.IntLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 134
                self.match(MiniLenguajeParser.INT_LITERAL)
                pass
            elif token in [33]:
                localctx = MiniLenguajeParser.FloatLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 135
                self.match(MiniLenguajeParser.FLOAT_LITERAL)
                pass
            elif token in [34]:
                localctx = MiniLenguajeParser.StringLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 136
                self.match(MiniLenguajeParser.STRING_LITERAL)
                pass
            elif token in [35]:
                localctx = MiniLenguajeParser.BoolLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 137
                self.match(MiniLenguajeParser.BOOL_LITERAL)
                pass
            elif token in [27]:
                localctx = MiniLenguajeParser.ParenExprContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 138
                self.match(MiniLenguajeParser.LPAREN)
                self.state = 139
                self.expression(0)
                self.state = 140
                self.match(MiniLenguajeParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[11] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 1)
         




