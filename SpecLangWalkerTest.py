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

    if __name__ == '__main__':
        unittest.main()