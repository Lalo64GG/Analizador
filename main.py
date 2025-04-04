import sys
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener

from MiniLenguajeLexer import MiniLenguajeLexer
from MiniLenguajeParser import MiniLenguajeParser
# Corrigiendo la importación
# Importamos directamente del archivo que contiene el ASTBuilder
from ASTBuilder import ASTBuilder  # Asumiendo que has guardado el código en ASTBuilder.py
from SemanticAnalyzer import TypeChecker, SemanticError


class MiniLenguajeErrorListener(ErrorListener):
    def __init__(self):
        super(MiniLenguajeErrorListener, self).__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error_msg = f"Error sintáctico en línea {line}, columna {column}: {msg}"
        self.errors.append(error_msg)

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        pass

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        pass

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        pass

def main(input_file=None):
    # Si no se especifica un archivo, usar entrada estándar
    if input_file:
        input_stream = FileStream(input_file, encoding='utf-8')
    else:
        input_stream = InputStream(sys.stdin.read())

    # Configurar lexer
    lexer = MiniLenguajeLexer(input_stream)
    lexer_error_listener = MiniLenguajeErrorListener()
    lexer.removeErrorListeners()
    lexer.addErrorListener(lexer_error_listener)

    # Configurar parser
    token_stream = CommonTokenStream(lexer)
    parser = MiniLenguajeParser(token_stream)
    parser_error_listener = MiniLenguajeErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(parser_error_listener)

    # Ejecutar análisis léxico y sintáctico
    tree = parser.program()

    # Comprobar si hay errores léxicos o sintácticos
    if lexer_error_listener.errors or parser_error_listener.errors:
        print("Errores durante el análisis léxico/sintáctico:")
        for error in lexer_error_listener.errors:
            print(f"- {error}")
        for error in parser_error_listener.errors:
            print(f"- {error}")
        return False

    # Construir AST
    ast_builder = ASTBuilder()
    ast = ast_builder.visit(tree)

    print("Análisis sintáctico completado con éxito.")

    # Realizar análisis semántico
    type_checker = TypeChecker()
    type_checker.check(ast)

    # Comprobar si hay errores semánticos
    if type_checker.errors:
        print("Errores durante el análisis semántico:")
        for error in type_checker.errors:
            print(f"- {error.message}")
        return False

    print("Análisis completado. No se encontraron errores.")
    return True


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print("Uso: python main.py [archivo_entrada]")
        print("Si no se especifica un archivo, se utilizará la entrada estándar.")
        main()