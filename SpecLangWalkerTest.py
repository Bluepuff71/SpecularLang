from unittest import TestCase
from antlr4 import CommonTokenStream, InputStream
from SpecLangLexer import SpecLangLexer
from SpecLangParser import SpecLangParser
from SpecLangWalker import SpecLangWalker

TestCase.maxDiff = None

class RowBuilder(TestCase):
    def __init__(self):
        super().__init__()
        self.expected = []
        self.text = ""

    @staticmethod
    def of(text: str):
        rb = RowBuilder()
        rb.text = text
        return rb

    def nl(self, text: str):
        self.text += '\n{}'.format(text)
        return self

    def row(self, expected: []):
        if expected:
            self.expected.append(expected)
        return self

    def check(self):
        lexer = SpecLangLexer(InputStream(self.text))
        stream = CommonTokenStream(lexer)
        parser = SpecLangParser(stream)
        tree = parser.block()
        visitor = SpecLangWalker()
        visitor.visit(tree)
        self.assertListEqual(self.expected, visitor.rows)


class SpecLangWalkerTest(TestCase):

    def test_simple_assignment(self):
        RowBuilder\
            .of("x = 0")\
            .row([0, "Assign", {'global': 'no', 'ID': "x", 'type': "Number", 'assignment': "0"}])\
            .check()

    def test_simple_global_assignment(self):
        RowBuilder \
            .of("global x = 0") \
            .row([0, "Assign", {'global': 'yes', 'ID': "x", 'type': "Number", 'assignment': "0"}]) \
            .check()

    def test_simple_dialog(self):
        RowBuilder\
            .of("@ actor : \"Hello World\"")\
            .row([0, "Dialog", {'speaker': 'actor', 'emotion': 'Neutral', 'text': 'Hello World'}])\
            .check()

    def test_simple_neg_assignent(self):
        RowBuilder\
            .of("x = -1")\
            .row([0, "Assign", {'global': 'no', 'ID': 'x', 'type': 'Number', 'assignment': "-1"}])\
            .check()

    def test_simple_not_assignment(self):
        RowBuilder \
            .of("x = not False") \
            .row([0, "Assign", {'global': 'no', 'ID': 'x', 'type': 'Bool', 'assignment': "True"}]) \
            .check()

    def test_complex_num_only_assignment(self):
        RowBuilder\
            .of("x = -(1 + 3) - (4 + (6 * 30) * 3) - 27")\
            .row([0, "Assign", {'global': 'no', 'ID': 'x', 'type': 'Number', 'assignment': "-575"}]) \
            .check()

    def test_double_neg_assignment(self):
        RowBuilder\
            .of("x = --4")\
            .row([0, "Assign", {'global': 'no', 'ID': 'x', 'type': 'Number', 'assignment': "4"}])\
            .check()

    def test_minus_negative_assignment(self):
        RowBuilder \
            .of("x = 4 - -4") \
            .row([0, "Assign", {'global': 'no', 'ID': 'x', 'type': 'Number', 'assignment': "8"}]) \
            .check()

    def test_simple_ID_assignment(self):
        RowBuilder \
            .of("x = y") \
            .row([0, "Assign", {'global': 'no', 'ID': 'x', 'type': 'ID', 'assignment': "y"}]) \
            .check()

    def test_simple_ID_expression(self):
        RowBuilder \
            .of("x = u + w") \
            .row([0, "Expression", {'operator': '+', 'x': 'u', 'y': 'w'}])\
            .row([1, "Assign", {'global': 'no', 'ID': 'x', 'type': 'Number', 'assignment': "$"}]) \
            .check()

    def test_simple_if_statement(self):
        RowBuilder \
            .of("if u != 0;") \
            .nl("\tu = 0")\
            .row([0, "Expression", {'operator': '!=', 'x': 'u', 'y': '0'}])\
            .row([1, "If", {'condition': '$', 'jump': 'endIf_0'}]) \
            .row([2, "Assign", {'global': 'no', 'ID': 'u', 'type': 'Number', 'assignment': "0"}]) \
            .row([3, "Label", {'name': 'endIf_0'}])\
            .check()

    def test_true_if_reduction(self):
        RowBuilder \
            .of("if True;") \
            .nl("\tu = 0") \
            .row([0, "Assign", {'global': 'no', 'ID': 'u', 'type': 'Number', 'assignment': "0"}]) \
            .check()

    def test_false_if_reduction(self):
        RowBuilder \
            .of("if False;") \
            .nl("\tu = 0") \
            .row(None) \
            .check()

    def test_inner_and_outer_block(self):
        RowBuilder \
            .of("if u != 0;") \
            .nl("\tu = 0") \
            .nl("\tif j == 5;")\
            .nl("\t\tj = 6")\
            .nl("u = 8")\
            .row([0, "Expression", {'operator': '!=', 'x': 'u', 'y': '0'}]) \
            .row([1, "If", {'condition': '$', 'jump': 'endIf_0'}]) \
            .row([2, "Assign", {'global': 'no', 'ID': 'u', 'type': 'Number', 'assignment': "0"}])\
            .row([3, "Expression", {'operator': '==', 'x': 'j', 'y': '5'}]) \
            .row([4, "If", {'condition': '$', 'jump': 'endIf_3'}])\
            .row([5, "Assign", {'global': 'no', 'ID': 'j', 'type': 'Number', 'assignment': "6"}])\
            .row([6, "Label", {'name': 'endIf_3'}]) \
            .row([7, "Label", {'name': 'endIf_0'}]) \
            .row([8, "Assign", {'global': 'no', 'ID': 'u', 'type': 'Number', 'assignment': "8"}])\
            .check()
