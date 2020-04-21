from SpecLangParser import SpecLangParser
from SpecLangVisitor import SpecLangVisitor


class SpecLangWalker(SpecLangVisitor):
    def __init__(self):
        self.rows = []
        self.rowNum = 0

    operators = {
        '==': ['ID', 'Number', 'String', 'Bool', 'None'],
        '!=': ['ID', 'Number', 'String', 'Bool', 'None'],
        '+': ['ID', 'Number', 'String'],
        '-': ['ID', 'Number'],
        '*': ['ID', 'Number'],
        '/': ['ID', 'Number'],
        '%': ['ID', 'Number'],
        '>': ['ID', 'Number'],
        '<': ['ID', 'Number'],
        '>=': ['ID', 'Number'],
        '<=': ['ID', 'Number'],
        'and': ['ID', 'Bool'],
        'or': ['ID', 'Bool'],
        'not': ['ID', 'Bool'],
    }


<<<<<<< Updated upstream
=======
    def add_row(self, row: []):
        self.rows.append(row)
        self.rowNum += 1

>>>>>>> Stashed changes
    def visitChoice(self, ctx:SpecLangParser.ChoiceContext):
        print(ctx.STRING())
        #return [++self.rowNum, "Choice", {'choices'}]

<<<<<<< Updated upstream
    def visitDialog(self, ctx:SpecLangParser.DialogContext):
        return [++self.rowNum, "Dialog", {'speaker': self.visit(ctx.term(0)), 'emotion': 'Neutral', 'text': self.visit(ctx.term(1))}]

    def visitTerm(self, ctx:SpecLangParser.TermContext):
        return ctx.getText()
=======
    def visitDialog(self, ctx: SpecLangParser.DialogContext):
        self.add_row([self.rowNum, "Dialog", {'speaker': str(ctx.getChild(1)), 'emotion': 'Neutral', 'text': str(ctx.getChild(3)).strip('"')}])

    def visitTerm(self, ctx: SpecLangParser.TermContext):
        if ctx.NUMBER():
            type_str = 'Number'
        elif ctx.TRUE() or ctx.FALSE():
            type_str = 'Bool'
        elif ctx.STRING():
            type_str = 'String'
        elif ctx.ID():
            type_str = 'ID'
        else:
            type_str = 'None'
        return {'type': type_str, 'value': ctx.getText().strip('"')}

    def visitAssignment(self, ctx:SpecLangParser.AssignmentContext):
        if ctx.GLOBAL():
            is_global = 'yes'
        else:
            is_global = 'no'
        expr = self.visit(ctx.expression())
        self.add_row([self.rowNum, "Assign", {'global': is_global, 'ID': str(ctx.ID()), 'type': expr['type'], 'assignment': expr['value']}]) #add type

    def visitMult(self, ctx:SpecLangParser.MultContext):
        term_0 = self.visit(ctx.expression(0))
        term_1 = self.visit(ctx.expression(1))
        expr_op = str(ctx.getChild(1))
        # Assert that the operation is valid
        assert term_0['type'] in self.operators[expr_op], "{} cannot be used with type: {}".format(expr_op, term_0['type'])
        if term_0['type'] == 'ID' or term_1['type'] == 'ID':
            self.add_row([self.rowNum, "Expression", {'operator': expr_op, 'x': term_0['value'], 'y': term_1['value']}])
            return {'type': "Number", 'value': '$'}
        else:  # Return * or / depending on the operator
            return {'type': 'Number', 'value': term_0['value'] * term_1['value'] if expr_op == '*' else term_0['value'] / term_1['value']}

    def visitAdd(self, ctx:SpecLangParser.AddContext):
        term_0 = self.visit(ctx.expression(0))
        term_1 = self.visit(ctx.expression(1))
        expr_op = str(ctx.getChild(1))
        # Assert that the operation is valid
        assert term_0['type'] in self.operators[expr_op], "{} cannot be used with type: {}".format(expr_op, term_0['type'])
        # type is string if term 0 or term 1 are strings else the type is Number
        typeStr = "String" if term_0['type'] == 'String' or term_1['type'] == 'String' else "Number"
        if term_0['type'] == 'ID' or term_1['type'] == 'ID':
            self.add_row([self.rowNum, "Expression", {'operator': expr_op, 'x': term_0['value'], 'y': term_1['value']}])
            return {'type': typeStr, 'value': '$'}
        else:  # Return + or - depending on the operator
            return {'type': typeStr, 'value': term_0['value'] + term_1['value'] if expr_op == '+' else term_0['value'] - term_1['value']}

    def visitEqual(self, ctx:SpecLangParser.EqualContext):
        term_0 = self.visit(ctx.expression(0))
        term_1 = self.visit(ctx.expression(1))
        expr_op = str(ctx.getChild(1))
        # Assert that the operation is valid
        assert term_0['type'] in self.operators[expr_op], "{} cannot be used with type: {}".format(expr_op, term_0['type'])
        if term_0['type'] == 'ID' or term_1['type'] == 'ID':
            self.add_row([self.rowNum, "Expression", {'operator': expr_op, 'x': term_0['value'], 'y': term_1['value']}])
            return {'type': "Bool", 'value': '$'}
        else:
            return {'type': 'Bool', 'value': term_0['value'] == term_1['value'] if expr_op == '==' else term_0['value'] != term_1['value']}

    def visitAnd(self, ctx:SpecLangParser.AndContext):
        term_0 = self.visit(ctx.expression(0))
        term_1 = self.visit(ctx.expression(1))
        assert term_0['type'] in self.operators['and'], "and cannot be used with type: {}".format(term_0['type'])
        if term_0['type'] == 'ID' or term_1['type'] == 'ID':
            self.add_row([self.rowNum, "Expression", {'operator': 'and', 'x': term_0['value'], 'y': term_1['value']}])
            return {'type': "Bool", 'value': '$'}
        else:
            return {'type': 'Bool', 'value': term_0['value'] and term_1['value']}

    def visitOr(self, ctx:SpecLangParser.OrContext):
        term_0 = self.visit(ctx.expression(0))
        term_1 = self.visit(ctx.expression(1))
        assert term_0['type'] in self.operators['or'], "and cannot be used with type: {}".format(term_0['type'])
        if term_0['type'] == 'ID' or term_1['type'] == 'ID':
            self.add_row([self.rowNum, "Expression", {'operator': 'or', 'x': term_0['value'], 'y': term_1['value']}])
            return {'type': "Bool", 'value': '$'}
        else:
            return {'type': 'Bool', 'value': term_0['value'] or term_1['value']}

    def visitUnary(self, ctx:SpecLangParser.UnaryContext):
        term = self.visit(ctx.expression())
        expr_op = str(ctx.getChild(0))
        assert term['type'] in self.operators[expr_op], "{} cannot be used with type: {}".format(expr_op, term['type'])
        if term['type'] == 'ID':
            self.add_row([self.rowNum, "Unary", {'operator': expr_op, 'x': term['value']}])
            return {'type': "Bool" if expr_op == 'not' else "Number", 'value': '$'}
        else:
            return {'type': "Bool" if expr_op == 'not' else "Number", 'value': not term['value'] if expr_op == 'not' else -term['value']}


    def visitParen(self, ctx:SpecLangParser.ParenContext):
        return self.visit(ctx.expression())
>>>>>>> Stashed changes
