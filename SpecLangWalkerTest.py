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
            self.expected.append([expected[0], expected[1], SpecLangWalker.to_unreal_row_structure(expected[2])])
        return self

    def check(self):
        lexer = SpecLangLexer(InputStream(self.text))
        stream = CommonTokenStream(lexer)
        parser = SpecLangParser(stream)
        tree = parser.program()
        visitor = SpecLangWalker()
        visitor.visit(tree)
        self.assertListEqual(self.expected, visitor.allRows)


class SpecLangWalkerTest(TestCase):

    def test_simple_assignment(self):
        RowBuilder \
            .of("scene \"TestScene\";") \
            .nl("\tx = 0")\
            .row([0, "Assign", {'global': 'No', 'ID': "x", 'type': "Number", 'assignment': "0"}])\
            .check()

    def test_simple_str_add(self):
        RowBuilder \
            .of("scene \"TestScene\";") \
            .nl("\tx = \"Test\" + 1") \
            .row([0, "Assign", {'global': 'No', 'ID': "x", 'type': "String", 'assignment': "Test1"}]) \
            .check()

    def test_simple_global_assignment(self):
        RowBuilder \
            .of("scene \"TestScene\";") \
            .nl("\tglobal x = 0") \
            .row([0, "Assign", {'global': 'Yes', 'ID': "x", 'type': "Number", 'assignment': "0"}]) \
            .check()

    def test_simple_dialog(self):
        RowBuilder \
            .of("scene \"TestScene\";") \
            .nl("\t@ actor : \"Hello World\"")\
            .row([0, "Dialog", {'speaker': 'actor', 'emotion': 'Neutral', 'text': 'Hello World'}])\
            .check()

    def test_simple_neg_assignent(self):
        RowBuilder \
            .of("scene \"TestScene\";") \
            .nl("\tx = -1")\
            .row([0, "Assign", {'global': 'No', 'ID': 'x', 'type': 'Number', 'assignment': "-1"}])\
            .check()

    def test_simple_not_assignment(self):
        RowBuilder \
            .of("scene \"TestScene\";") \
            .nl("\tx = not False") \
            .row([0, "Assign", {'global': 'No', 'ID': 'x', 'type': 'Bool', 'assignment': "True"}]) \
            .check()

    def test_complex_num_only_assignment(self):
        RowBuilder \
            .of("scene \"TestScene\";") \
            .nl("\tx = -(1 + 3) - (4 + (6 * 30) * 3) - 27")\
            .row([0, "Assign", {'global': 'No', 'ID': 'x', 'type': 'Number', 'assignment': "-575"}]) \
            .check()

    def test_double_neg_assignment(self):
        RowBuilder \
            .of("scene \"TestScene\";") \
            .nl("\tx = --4")\
            .row([0, "Assign", {'global': 'No', 'ID': 'x', 'type': 'Number', 'assignment': "4"}])\
            .check()

    def test_minus_negative_assignment(self):
        RowBuilder \
            .of("scene \"TestScene\";") \
            .nl("\tx = 4 - -4") \
            .row([0, "Assign", {'global': 'No', 'ID': 'x', 'type': 'Number', 'assignment': "8"}]) \
            .check()

    def test_simple_ID_assignment(self):
        RowBuilder \
            .of("scene \"TestScene\";") \
            .nl("\tx = y") \
            .row([0, "Assign", {'global': 'No', 'ID': 'x', 'type': 'ID', 'assignment': "y"}]) \
            .check()

    def test_simple_ID_expression(self):
        RowBuilder \
            .of("scene \"TestScene\";") \
            .nl("\tx = u + w") \
            .row([0, "Expression", {'operator': '+', 'x': 'u', 'y': 'w'}])\
            .row([1, "Assign", {'global': 'No', 'ID': 'x', 'type': 'ID', 'assignment': "$"}]) \
            .check()

    def test_simple_if_statement(self):
        RowBuilder \
            .of("scene \"TestScene\";") \
            .nl("\tif u != 0;") \
            .nl("\t\tu = 0")\
            .row([0, "Expression", {'operator': '!=', 'x': 'u', 'y': '0'}])\
            .row([1, "If", {'condition': '$', 'jump': 'endIf_0'}]) \
            .row([2, "Assign", {'global': 'No', 'ID': 'u', 'type': 'Number', 'assignment': "0"}]) \
            .row([3, "Label", {'name': 'endIf_0'}])\
            .check()

    def test_true_if_reduction(self):
        RowBuilder \
            .of("scene \"TestScene\";") \
            .nl("\tif True;") \
            .nl("\t\tu = 0") \
            .row([0, "Assign", {'global': 'No', 'ID': 'u', 'type': 'Number', 'assignment': "0"}]) \
            .check()

    def test_false_if_reduction(self):
        RowBuilder \
            .of("scene \"TestScene\";") \
            .nl("\tif False;") \
            .nl("\t\tu = 0") \
            .row(None) \
            .check()

    def test_inner_and_outer_block(self):
        RowBuilder \
            .of("scene \"TestScene\";") \
            .nl("\tif u != 0;") \
            .nl("\t\tu = 0") \
            .nl("\t\tif j == 5;")\
            .nl("\t\t\tj = 6")\
            .nl("\tu = 8")\
            .row([0, "Expression", {'operator': '!=', 'x': 'u', 'y': '0'}]) \
            .row([1, "If", {'condition': '$', 'jump': 'endIf_0'}]) \
            .row([2, "Assign", {'global': 'No', 'ID': 'u', 'type': 'Number', 'assignment': "0"}])\
            .row([3, "Expression", {'operator': '==', 'x': 'j', 'y': '5'}]) \
            .row([4, "If", {'condition': '$', 'jump': 'endIf_3'}])\
            .row([5, "Assign", {'global': 'No', 'ID': 'j', 'type': 'Number', 'assignment': "6"}])\
            .row([6, "Label", {'name': 'endIf_3'}]) \
            .row([7, "Label", {'name': 'endIf_0'}]) \
            .row([8, "Assign", {'global': 'No', 'ID': 'u', 'type': 'Number', 'assignment': "8"}])\
            .check()

    def test_assignment_before_scene(self):
        RowBuilder \
            .of("i = 0")\
            .nl("scene \"TestScene\";") \
            .nl("\tu = 1") \
            .row([0, "Assign", {'global': 'No', 'ID': 'i', 'type': 'Number', 'assignment': "0"}]) \
            .row([1, "Assign", {'global': 'No', 'ID': 'u', 'type': 'Number', 'assignment': "1"}])\
            .check()

    def test_simple_single_choice_assignment(self):
        RowBuilder \
            .of("scene \"TestScene\";") \
            .nl("\tchoice = [\"Choice1\"]") \
            .row([0, "Choice", {'choice0': "Choice1"}]) \
            .row([1, "Assign", {'global': 'No', 'ID': 'choice', 'type': 'ID', 'assignment': "$"}]) \
            .check()

    def test_simple_multi_choice_assignment(self):
        RowBuilder \
            .of("scene \"TestScene\";") \
            .nl('\tchoice = ["Choice1", "Choice2"]') \
            .row([0, "Choice", {'choice0': "Choice1", 'choice1': "Choice2"}]) \
            .row([1, "Assign", {'global': 'No', 'ID': 'choice', 'type': 'ID', 'assignment': "$"}]) \
            .check()

    def test_simple_string_with_escape_quotes(self):
        RowBuilder \
            .of("scene \"TestScene\";") \
            .nl('\t' + r'x = "\"Test\""') \
            .row([0, "Assign", {'global': 'No', 'ID': "x", 'type': "String", 'assignment': '"Test"'}]) \
            .check()
