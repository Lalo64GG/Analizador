import sys
import os
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener

from MiniLenguajeLexer import MiniLenguajeLexer
from MiniLenguajeParser import MiniLenguajeParser
from ASTBuilder import ASTBuilder
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


def print_ast(node, indent=0):
    """Función para imprimir el AST en formato de texto"""
    print(' ' * indent + str(node))
    for child in node.children:
        print_ast(child, indent + 2)


def visualize_ast_with_matplotlib(node, filename="ast_tree.png"):
    """Visualiza el AST usando NetworkX y Matplotlib"""
    try:
        import networkx as nx
        import matplotlib.pyplot as plt

        # Crear un grafo dirigido
        G = nx.DiGraph()

        # Contador para nodos sin ID específico
        count = [0]

        def add_node(node, parent_id=None):
            if node is None:
                return

            # Crear ID para este nodo
            node_id = f"{count[0]}"
            count[0] += 1

            # Crear etiqueta del nodo
            node_label = f"{node.type}"
            if node.value is not None:
                node_label += f"\n{node.value}"

            # Añadir nodo al grafo
            G.add_node(node_id, label=node_label)

            # Conectar con el padre si existe
            if parent_id is not None:
                G.add_edge(parent_id, node_id)

            # Procesar nodos hijos
            for child in node.children:
                add_node(child, node_id)

        # Iniciar el proceso con el nodo raíz
        add_node(node)

        # Configurar la figura
        plt.figure(figsize=(12, 8))

        # Crear el layout
        try:
            # Intentar usar el layout de graphviz si está disponible
            pos = nx.nx_agraph.graphviz_layout(G, prog='dot')
        except:
            # Si falla, usar el layout de resortes
            pos = nx.spring_layout(G, seed=42)

        # Dibujar nodos y aristas
        nx.draw(G, pos, with_labels=False, node_color='lightblue',
                node_size=700, arrows=True, edge_color='gray')

        # Añadir etiquetas
        node_labels = {node: data['label'] for node, data in G.nodes(data=True)}
        nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=8)

        # Guardar y mostrar
        plt.axis('off')
        plt.tight_layout()
        plt.savefig(filename, format='png', dpi=300)
        print(f"AST visualizado y guardado como {filename}")

        return True
    except ImportError as e:
        print(f"Error: {e}")
        print("Instala las bibliotecas necesarias con: pip install networkx matplotlib")
        return False
    except Exception as e:
        print(f"Error al generar la visualización: {e}")
        return False


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

    # Generar visualización del AST con matplotlib
    if input_file:
        # Usa el nombre del archivo de entrada como base para el nombre del archivo de salida
        base_name = os.path.splitext(input_file)[0]
        visualize_ast_with_matplotlib(ast, f"{base_name}_ast.png")
    else:
        visualize_ast_with_matplotlib(ast, "programa_ast.png")

    # Imprimir AST en formato de texto
    print("\nÁrbol Sintáctico Abstracto (AST):")
    print_ast(ast)

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