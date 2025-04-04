grammar MiniLenguaje;

// Reglas léxicas (Tokens)
VAR         : 'var' ;
IF          : 'if' ;
ELSE        : 'else' ;
WHILE       : 'while' ;
FOR         : 'for' ;
PRINT       : 'print' ;
INPUT       : 'input' ;
INT_TYPE    : 'int' ;
FLOAT_TYPE  : 'float' ;
STRING_TYPE : 'string' ;
BOOL_TYPE   : 'bool' ;

// Operadores
PLUS        : '+' ;
MINUS       : '-' ;
MUL         : '*' ;
DIV         : '/' ;
ASSIGN      : '=' ;
EQ          : '==' ;
NEQ         : '!=' ;
LT          : '<' ;
GT          : '>' ;
LE          : '<=' ;
GE          : '>=' ;
AND         : 'and' ;
OR          : 'or' ;

// Símbolos de separación
SEMICOLON   : ';' ;
COMMA       : ',' ;
LPAREN      : '(' ;
RPAREN      : ')' ;
LBRACE      : '{' ;
RBRACE      : '}' ;

// Identificadores y literales
ID          : [a-zA-Z][a-zA-Z0-9_]* ;
INT_LITERAL : [0-9]+ ;
FLOAT_LITERAL : [0-9]+ '.' [0-9]+ ;
STRING_LITERAL : '"' (~["\r\n] | '\\"')* '"' ;
BOOL_LITERAL : 'true' | 'false' ;

// Ignorar espacios en blanco y comentarios
WS          : [ \t\r\n]+ -> skip ;
COMMENT     : '//' ~[\r\n]* -> skip ;

// Reglas sintácticas
program
    : statement+ EOF
    ;

statement
    : varDeclaration
    | assignment
    | ifStatement
    | whileStatement
    | forStatement
    | printStatement
    | inputStatement
    | block
    ;

varDeclaration
    : type ID (ASSIGN expression)? SEMICOLON
    ;

type
    : INT_TYPE
    | FLOAT_TYPE
    | STRING_TYPE
    | BOOL_TYPE
    ;

assignment
    : ID ASSIGN expression SEMICOLON
    ;

ifStatement
    : IF LPAREN expression RPAREN statement (ELSE statement)?
    ;

whileStatement
    : WHILE LPAREN expression RPAREN statement
    ;

forStatement
    : FOR LPAREN (varDeclaration | assignment | SEMICOLON) expression SEMICOLON expression RPAREN statement
    ;

printStatement
    : PRINT LPAREN expression RPAREN SEMICOLON
    ;

inputStatement
    : INPUT LPAREN ID RPAREN SEMICOLON
    ;

block
    : LBRACE statement* RBRACE
    ;

expression
    : primary                                     # PrimaryExpr
    | expression op=(MUL|DIV) expression         # MultDivExpr
    | expression op=(PLUS|MINUS) expression      # AddSubExpr
    | expression op=(LT|GT|LE|GE) expression     # ComparisonExpr
    | expression op=(EQ|NEQ) expression          # EqualityExpr
    | expression AND expression                  # AndExpr
    | expression OR expression                   # OrExpr
    ;

primary
    : ID                                          # IdExpr
    | INT_LITERAL                                 # IntLiteral
    | FLOAT_LITERAL                               # FloatLiteral
    | STRING_LITERAL                              # StringLiteral
    | BOOL_LITERAL                                # BoolLiteral
    | LPAREN expression RPAREN                    # ParenExpr
    ;