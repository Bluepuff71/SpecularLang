import csv

from SpecLangParser import SpecLangParser
from SpecLangVisitor import SpecLangVisitor


class SpecLangWalker(SpecLangVisitor):
    def __init__(self):
        self.rows = []
        self.allRows = []
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

    def write_rows(self, rows: [], fileName: str):
        assert len(fileName) > 0 and not (" " in fileName), "File name is invalid"
        fileName += '.csv'
        csv_file = open(fileName, 'w', newline='')
        csv_writer = csv.writer(csv_file, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True)
        csv_writer.writerow(["---", "actionType", "params"])
        csv_writer.writerows(rows)
        csv_file.close()

    @staticmethod
    def to_unreal_row_structure(di: {}):
        #(actor=None,characterName={},dialogueColor=(B=0,G=0,R=0,A=255))
        new_dict = "("
        for x, y in di.items():
            new_dict += '("{}","{}"),'.format(x, y)
        new_dict = new_dict.rstrip(",")
        new_dict += ")"
        return new_dict

    def add_row(self, row: []):
        self.rows.append([row[0], row[1], self.to_unreal_row_structure(row[2])])
        self.allRows.append([row[0], row[1], self.to_unreal_row_structure(row[2])])
        self.rowNum += 1

    def visitChoice(self, ctx:SpecLangParser.ChoiceContext):
        #'[' STRING (',' STRING)*? ']' #choice stores a Number in $
        choices = {}
        i = 0
        while ctx.STRING(i) is not None:
            choices["choice{}".format(i)] = str(ctx.STRING(i)).strip('"')
            i += 1
        self.add_row([self.rowNum, "Choice", choices])
        return {'type': "ID", 'value': '$'}

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
            is_global = 'Yes'
        else:
            is_global = 'No'
        expr = self.visit(ctx.expression())
        self.add_row([self.rowNum, "Assign", {'global': is_global, 'ID': str(ctx.ID()), 'type': expr['type'], 'assignment': expr['value']}]) #add type

    def visitMult(self, ctx:SpecLangParser.MultContext):
        term_0 = self.visit(ctx.expression(0))
        term_1 = self.visit(ctx.expression(1))
        expr_op = str(ctx.getChild(1))
        # Assert that the operation is valid
        assert term_0['type'] in self.operators[expr_op] and term_1['type'] in self.operators[expr_op], "{} {} {} is not a valid operation".format(term_0['type'], expr_op, term_1['type'])
        if term_0['type'] == 'ID' or term_1['type'] == 'ID':
            self.add_row([self.rowNum, "Expression", {'operator': expr_op, 'x': term_0['value'], 'y': term_1['value']}])
            return {'type': "ID", 'value': '$'}
        else:  # Return * or / depending on the operator
            return {'type': 'Number', 'value': int(term_0['value']) * int(term_1['value']) if expr_op == '*' else int(term_0['value']) / int(term_1['value'])}

    def visitAdd(self, ctx:SpecLangParser.AddContext):
        term_0 = self.visit(ctx.expression(0))
        term_1 = self.visit(ctx.expression(1))
        expr_op = str(ctx.getChild(1))
        # Assert that the operation is valid
        assert term_0['type'] in self.operators[expr_op] and term_1['type'] in self.operators[expr_op], "{} {} {} is not a valid operation".format(term_0['type'], expr_op, term_1['type'])        # type is string if term 0 or term 1 are strings else the type is Number
        typeStr = "String" if term_0['type'] == 'String' or term_1['type'] == 'String' else "Number"
        if term_0['type'] == 'ID' or term_1['type'] == 'ID':
            self.add_row([self.rowNum, "Expression", {'operator': expr_op, 'x': term_0['value'], 'y': term_1['value']}])
            return {'type': 'ID', 'value': '$'}
        else:  # Return + or - depending on the operator
            if typeStr == "String":
                return {'type': 'String', 'value': term_0['value'] + term_1['value']}
            else:
                return {'type': 'Number', 'value': str(int(term_0['value']) + int(term_1['value'])) if expr_op == '+' else str(int(term_0['value']) - int(term_1['value']))}

    def visitEqual(self, ctx:SpecLangParser.EqualContext):
        term_0 = self.visit(ctx.expression(0))
        term_1 = self.visit(ctx.expression(1))
        expr_op = str(ctx.getChild(1))
        # Assert that the operation is valid
        assert term_0['type'] in self.operators[expr_op] and term_1['type'] in self.operators[expr_op], "{} {} {} is not a valid operation".format(term_0['type'], expr_op, term_1['type'])
        if term_0['type'] == 'ID' or term_1['type'] == 'ID':
            self.add_row([self.rowNum, "Expression", {'operator': expr_op, 'x': term_0['value'], 'y': term_1['value']}])
            return {'type': "ID", 'value': '$'}
        else:
            return {'type': 'Bool', 'value': term_0['value'] == term_1['value'] if expr_op == '==' else term_0['value'] != term_1['value']}

    def visitAnd(self, ctx:SpecLangParser.AndContext):
        term_0 = self.visit(ctx.expression(0))
        term_1 = self.visit(ctx.expression(1))
        assert term_0['type'] in self.operators['and'] and term_1['type'] in self.operators['and'], "{} {} {} is not a valid operation".format(term_0['type'], 'and', term_1['type'])
        if term_0['type'] == 'ID' or term_1['type'] == 'ID':
            self.add_row([self.rowNum, "Expression", {'operator': 'and', 'x': term_0['value'], 'y': term_1['value']}])
            return {'type': "ID", 'value': '$'}
        else:
            return {'type': 'Bool', 'value': term_0['value'] and term_1['value']}

    def visitOr(self, ctx:SpecLangParser.OrContext):
        term_0 = self.visit(ctx.expression(0))
        term_1 = self.visit(ctx.expression(1))
        assert term_0['type'] in self.operators['or'] and term_1['type'] in self.operators['and'], "{} {} {} is not a valid operation".format(term_0['type'], 'or', term_1['type'])
        if term_0['type'] == 'ID' or term_1['type'] == 'ID':
            self.add_row([self.rowNum, "Expression", {'operator': 'or', 'x': term_0['value'], 'y': term_1['value']}])
            return {'type': "ID", 'value': '$'}
        else:
            return {'type': 'Bool', 'value': term_0['value'] or term_1['value']}

    def visitUnary(self, ctx:SpecLangParser.UnaryContext):
        term = self.visit(ctx.expression())
        expr_op = str(ctx.getChild(0))
        assert term['type'] in self.operators[expr_op], "{} cannot be used with type: {}".format(expr_op, term['type'])
        if term['type'] == 'ID':
            self.add_row([self.rowNum, "Unary", {'operator': expr_op, 'x': term['value']}])
            return {'type': 'ID', 'value': '$'}
        else:
            return {'type': "Bool" if expr_op == 'not' else "Number", 'value': str(not self.to_bool(term['value'])) if expr_op == 'not' else str(-int(term['value']))}

    def visitParen(self, ctx:SpecLangParser.ParenContext):
        return self.visit(ctx.expression())

    def visitScene_statement(self, ctx:SpecLangParser.Scene_statementContext):
        self.visit(ctx.block())
        self.write_rows(self.rows, str(ctx.STRING()).strip('"'))
        self.rows = []
        self.rowNum = 0


    def visitIfStatement(self, ctx:SpecLangParser.IfStatementContext):
        current_row = self.rowNum
        term = self.visit(ctx.expression())
        if term['value'] == 'True':
            self.visit(ctx.block())
        elif term['value'] == 'False':
            return
        else:
            self.add_row([self.rowNum, "If", {'condition': term['value'], 'jump': 'endIf_{}'.format(current_row)}])
            self.visit(ctx.block())
            self.add_row([self.rowNum, "Label", {'name': 'endIf_{}'.format(current_row)}])

#TODO
   #def visitElse_if_statement(self, ctx:SpecLangParser.Else_if_statementContext):
    #    current_row = self.rowNum
     #   term = self.visit(ctx.expression())
      #  if term['value'] == 'True':
       #     self.visit(ctx.block())
        #elif term['value'] == 'False':
         #   return
        #else:
         #   self.add_row([self.rowNum, "If", {'condition': term['value'], 'jump': 'endIf_{}'.format(current_row)}])
          #  self.visit(ctx.block())
           # self.add_row([self.rowNum, "Label", {'name': 'endIf_{}'.format(current_row)}])

    def to_bool(self, string: str):
        if string.lower() == 'true':
            return True
        elif string.lower() == 'false':
            return False
        else:
            raise ValueError('ToBool is None!')
