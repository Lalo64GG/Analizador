from ASTBuilder import ASTNode


class SemanticError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class TypeChecker:
    def __init__(self):
        self.symbol_table = {}
        self.errors = []

    def check(self, node):
        if node.type == 'Program':
            self._check_program(node)
        else:
            self.errors.append(SemanticError(f"Nodo raíz inesperado: {node.type}"))

    def _check_program(self, node):
        for stmt in node.children:
            self._check_statement(stmt)

    def _check_statement(self, node):
        if node.type == 'VarDeclaration':
            self._check_var_declaration(node)
        elif node.type == 'Assignment':
            self._check_assignment(node)
        elif node.type == 'IfStatement':
            self._check_if_statement(node)
        elif node.type == 'WhileStatement':
            self._check_while_statement(node)
        elif node.type == 'ForStatement':
            self._check_for_statement(node)
        elif node.type == 'PrintStatement':
            self._check_print_statement(node)
        elif node.type == 'InputStatement':
            self._check_input_statement(node)
        elif node.type == 'Block':
            self._check_block(node)
        else:
            self.errors.append(SemanticError(f"Tipo de nodo de declaración desconocido: {node.type}"))

    def _check_var_declaration(self, node):
        var_name = node.value
        var_type = node.children[0].value

        # Verificar si la variable ya ha sido declarada
        if var_name in self.symbol_table:
            self.errors.append(SemanticError(f"Variable '{var_name}' ya declarada."))
            return

        # Registrar la variable en la tabla de símbolos
        self.symbol_table[var_name] = var_type

        # Si hay una expresión de inicialización, verificar su tipo
        if len(node.children) > 1 and node.children[1] is not None:
            init_expr = node.children[1]
            expr_type = self._get_expression_type(init_expr)

            if expr_type and not self._type_compatible(var_type, expr_type):
                self.errors.append(SemanticError(
                    f"Tipo incompatible: No se puede asignar '{expr_type}' a variable '{var_name}' de tipo '{var_type}'"))

    def _check_assignment(self, node):
        var_name = node.value
        expr = node.children[0]

        # Verificar si la variable ha sido declarada
        if var_name not in self.symbol_table:
            self.errors.append(SemanticError(f"Variable '{var_name}' no declarada."))
            return

        var_type = self.symbol_table[var_name]
        expr_type = self._get_expression_type(expr)

        if expr_type and not self._type_compatible(var_type, expr_type):
            self.errors.append(SemanticError(
                f"Tipo incompatible: No se puede asignar '{expr_type}' a variable '{var_name}' de tipo '{var_type}'"))

    def _check_if_statement(self, node):
        condition = node.children[0]
        then_stmt = node.children[1]

        # Verificar que la condición sea de tipo bool
        condition_type = self._get_expression_type(condition)
        if condition_type and condition_type != 'bool':
            self.errors.append(SemanticError(f"La condición del if debe ser de tipo bool, no '{condition_type}'"))

        # Verificar el bloque then
        self._check_statement(then_stmt)

        # Verificar el bloque else si existe
        if len(node.children) > 2:
            else_stmt = node.children[2]
            self._check_statement(else_stmt)

    def _check_while_statement(self, node):
        condition = node.children[0]
        body = node.children[1]

        # Verificar que la condición sea de tipo bool
        condition_type = self._get_expression_type(condition)
        if condition_type and condition_type != 'bool':
            self.errors.append(SemanticError(f"La condición del while debe ser de tipo bool, no '{condition_type}'"))

        # Verificar el cuerpo del while
        self._check_statement(body)

    def _check_for_statement(self, node):
        init = node.children[0]
        condition = node.children[1]
        update = node.children[2]
        body = node.children[3]

        # Verificar la inicialización
        if init.type in ['VarDeclaration', 'Assignment']:
            self._check_statement(init)

        # Verificar que la condición sea de tipo bool
        condition_type = self._get_expression_type(condition)
        if condition_type and condition_type != 'bool':
            self.errors.append(SemanticError(f"La condición del for debe ser de tipo bool, no '{condition_type}'"))

        # Verificar la expresión de actualización (puede ser de cualquier tipo)
        self._get_expression_type(update)

        # Verificar el cuerpo del for
        self._check_statement(body)

    def _check_print_statement(self, node):
        expr = node.children[0]
        # Solo verificamos que la expresión es válida
        self._get_expression_type(expr)

    def _check_input_statement(self, node):
        var_name = node.value

        # Verificar si la variable ha sido declarada
        if var_name not in self.symbol_table:
            self.errors.append(SemanticError(f"Variable '{var_name}' no declarada."))

    def _check_block(self, node):
        for stmt in node.children:
            self._check_statement(stmt)

    def _get_expression_type(self, node):
        if node.type == 'BinaryOp':
            return self._get_binary_op_type(node)
        elif node.type == 'Identifier':
            return self._get_identifier_type(node)
        elif node.type == 'IntLiteral':
            return 'int'
        elif node.type == 'FloatLiteral':
            return 'float'
        elif node.type == 'StringLiteral':
            return 'string'
        elif node.type == 'BoolLiteral':
            return 'bool'
        else:
            self.errors.append(SemanticError(f"Tipo de expresión desconocido: {node.type}"))
            return None

    def _get_binary_op_type(self, node):
        op = node.value
        left_type = self._get_expression_type(node.children[0])
        right_type = self._get_expression_type(node.children[1])

        if left_type is None or right_type is None:
            return None

        # Verificar compatibilidad de tipos para operadores aritméticos
        if op in ['+', '-', '*', '/']:
            if left_type in ['int', 'float'] and right_type in ['int', 'float']:
                # Si alguno es float, el resultado es float
                if left_type == 'float' or right_type == 'float':
                    return 'float'
                else:
                    return 'int'
            elif op == '+' and (left_type == 'string' or right_type == 'string'):
                # Concatenación de cadenas
                if left_type != 'string' or right_type != 'string':
                    self.errors.append(SemanticError(
                        f"Operación inválida: No se puede usar '+' con tipos '{left_type}' y '{right_type}'"))
                return 'string'
            else:
                self.errors.append(SemanticError(
                    f"Operación inválida: No se puede usar '{op}' con tipos '{left_type}' y '{right_type}'"))
                return None

        # Verificar compatibilidad de tipos para operadores de comparación
        elif op in ['<', '>', '<=', '>=']:
            if (left_type in ['int', 'float'] and right_type in ['int', 'float']) or \
                    (left_type == 'string' and right_type == 'string'):
                return 'bool'
            else:
                self.errors.append(SemanticError(
                    f"Operación inválida: No se puede usar '{op}' con tipos '{left_type}' y '{right_type}'"))
                return None

        # Verificar compatibilidad de tipos para operadores de igualdad
        elif op in ['==', '!=']:
            if left_type == right_type or \
                    (left_type in ['int', 'float'] and right_type in ['int', 'float']):
                return 'bool'
            else:
                self.errors.append(SemanticError(
                    f"Operación inválida: No se puede usar '{op}' con tipos '{left_type}' y '{right_type}'"))
                return None

        # Verificar compatibilidad de tipos para operadores lógicos
        elif op in ['and', 'or']:
            if left_type == 'bool' and right_type == 'bool':
                return 'bool'
            else:
                self.errors.append(SemanticError(
                    f"Operación inválida: No se puede usar '{op}' con tipos '{left_type}' y '{right_type}'"))
                return None

        else:
            self.errors.append(SemanticError(f"Operador desconocido: {op}"))
            return None

    def _get_identifier_type(self, node):
        var_name = node.value

        # Tratar 'true' y 'false' como literales booleanos especiales
        if var_name == 'true' or var_name == 'false':
            return 'bool'

        if var_name not in self.symbol_table:
            self.errors.append(SemanticError(f"Variable '{var_name}' no declarada."))
            return None
        return self.symbol_table[var_name]

    def _type_compatible(self, target_type, source_type):
        # Mismos tipos son compatibles
        if target_type == source_type:
            return True

        # int puede ser asignado a float
        if target_type == 'float' and source_type == 'int':
            return True

        return False