import unittest

from antlr4 import CommonTokenStream, InputStream

from SpecLangLexer import SpecLangLexer
from SpecLangParser import SpecLangParser
from SpecLangWalker import SpecLangWalker

class RowBuilder(unittest.TestCase):
    def __init__(self):
        super().__init__()
        self.expected = []
        self.text = ""

    @staticmethod
    def of(text: str):
        rb = RowBuilder()
        rb.text = text
        return rb

    def row(self, expected: []):
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


class SpecLangWalkerTest(unittest.TestCase):

    def test_simple_assignment(self):
        RowBuilder\
            .of("x = 0")\
            .row([0, "Assign", {'global': 'no', 'ID': "x", 'type': "Number", 'assignment': "0"}])\
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

    if __name__ == '__main__':
        unittest.main()
