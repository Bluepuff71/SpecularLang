from unittest import TestCase
from antlr4 import CommonTokenStream, InputStream
from SpecularLang.SpecLangLexer import SpecLangLexer
from SpecularLang.SpecLangParser import SpecLangParser
from SpecularLang.SpecLangWalker import SpecLangWalker

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
        self.text += '\r\n{}'.format(text)
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
            .row([1, "StopScene", {}])\
            .check()

    def test_simple_str_add(self):
        RowBuilder \
            .of("scene \"TestScene\";") \
            .nl('\tx = "Test" + 1') \
            .row([0, "Assign", {'global': 'No', 'ID': "x", 'type': "String", 'assignment': '\\"Test1\\"'}]) \
            .row([1, "StopScene", {}]) \
            .check()

    def test_simple_str_add_with_escape_quote(self):
        RowBuilder \
            .of("scene \"TestScene\";") \
            .nl('\tx = "Te\\"st" + 1') \
            .row([0, "Assign", {'global': 'No', 'ID': "x", 'type': "String", 'assignment': '\\"Te\\"st1\\"'}]) \
            .row([1, "StopScene", {}]) \
            .check()

    def test_simple_str_add_with_surround_escape_quote(self):
        RowBuilder \
            .of("scene \"TestScene\";") \
            .nl('\tx = "\\"Test\\"" + 1') \
            .row([0, "Assign", {'global': 'No', 'ID': "x", 'type': "String", 'assignment': '\\"\\"Test\\"1\\"'}]) \
            .row([1, "StopScene", {}]) \
            .check()

    def test_simple_global_assignment(self):
        RowBuilder \
            .of("scene \"TestScene\";") \
            .nl("\tglobal x = 0") \
            .row([0, "Assign", {'global': 'Yes', 'ID': "x", 'type': "Number", 'assignment': "0"}]) \
            .row([1, "StopScene", {}]) \
            .check()

    def test_simple_dialog(self):
        RowBuilder \
            .of("scene \"TestScene\";") \
            .nl("\t@ actor : \"Hello World\"")\
            .row([0, "Dialog", {'speaker': 'actor', 'emotion': 'Neutral', 'text': 'Hello World'}]) \
            .row([1, "StopScene", {}]) \
            .check()

    def test_simple_neg_assignent(self):
        RowBuilder \
            .of("scene \"TestScene\";") \
            .nl("\tx = -1")\
            .row([0, "Assign", {'global': 'No', 'ID': 'x', 'type': 'Number', 'assignment': "-1"}]) \
            .row([1, "StopScene", {}]) \
            .check()

    def test_simple_not_assignment(self):
        RowBuilder \
            .of("scene \"TestScene\";") \
            .nl("\tx = not False") \
            .row([0, "Assign", {'global': 'No', 'ID': 'x', 'type': 'Bool', 'assignment': "True"}]) \
            .row([1, "StopScene", {}]) \
            .check()

    def test_complex_num_only_assignment(self):
        RowBuilder \
            .of("scene \"TestScene\";") \
            .nl("\tx = -(1 + 3) - (4 + (6 * 30) * 3) - 27")\
            .row([0, "Assign", {'global': 'No', 'ID': 'x', 'type': 'Number', 'assignment': "-575"}]) \
            .row([1, "StopScene", {}]) \
            .check()

    def test_double_neg_assignment(self):
        RowBuilder \
            .of("scene \"TestScene\";") \
            .nl("\tx = --4")\
            .row([0, "Assign", {'global': 'No', 'ID': 'x', 'type': 'Number', 'assignment': "4"}]) \
            .row([1, "StopScene", {}]) \
            .check()

    def test_minus_negative_assignment(self):
        RowBuilder \
            .of("scene \"TestScene\";") \
            .nl("\tx = 4 - -4") \
            .row([0, "Assign", {'global': 'No', 'ID': 'x', 'type': 'Number', 'assignment': "8"}]) \
            .row([1, "StopScene", {}]) \
            .check()

    def test_simple_ID_assignment(self):
        RowBuilder \
            .of("scene \"TestScene\";") \
            .nl("\tx = y") \
            .row([0, "Assign", {'global': 'No', 'ID': 'x', 'type': 'ID', 'assignment': "y"}]) \
            .row([1, "StopScene", {}]) \
            .check()

    def test_simple_ID_expression(self):
        RowBuilder \
            .of("scene \"TestScene\";") \
            .nl("\tx = u + w") \
            .row([0, "Expression", {'operator': '+', 'x': 'u', 'y': 'w'}])\
            .row([1, "Assign", {'global': 'No', 'ID': 'x', 'type': 'ID', 'assignment': "$0"}]) \
            .row([2, "StopScene", {}]) \
            .check()

    def test_simple_if_statement(self):
        RowBuilder \
            .of("scene \"TestScene\";") \
            .nl("\tif u != 0;") \
            .nl("\t\tu = 0")\
            .row([0, "Expression", {'operator': '!=', 'x': 'u', 'y': '0'}])\
            .row([1, "If", {'condition': '$0', 'jump': 'endIf_0'}]) \
            .row([2, "Assign", {'global': 'No', 'ID': 'u', 'type': 'Number', 'assignment': "0"}]) \
            .row([3, "Label", {'name': 'endIf_0'}]) \
            .row([4, "StopScene", {}]) \
            .check()

    def test_true_if_reduction(self):
        RowBuilder \
            .of("scene \"TestScene\";") \
            .nl("\tif True;") \
            .nl("\t\tu = 0") \
            .row([0, "Assign", {'global': 'No', 'ID': 'u', 'type': 'Number', 'assignment': "0"}]) \
            .row([1, "StopScene", {}]) \
            .check()

    def test_false_if_reduction(self):
        RowBuilder \
            .of("scene \"TestScene\";") \
            .nl("\tif False;") \
            .nl("\t\tu = 0") \
            .row([0, "StopScene", {}]) \
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
            .row([1, "If", {'condition': '$0', 'jump': 'endIf_0'}]) \
            .row([2, "Assign", {'global': 'No', 'ID': 'u', 'type': 'Number', 'assignment': "0"}])\
            .row([3, "Expression", {'operator': '==', 'x': 'j', 'y': '5'}]) \
            .row([4, "If", {'condition': '$3', 'jump': 'endIf_3'}])\
            .row([5, "Assign", {'global': 'No', 'ID': 'j', 'type': 'Number', 'assignment': "6"}])\
            .row([6, "Label", {'name': 'endIf_3'}]) \
            .row([7, "Label", {'name': 'endIf_0'}]) \
            .row([8, "Assign", {'global': 'No', 'ID': 'u', 'type': 'Number', 'assignment': "8"}]) \
            .row([9, "StopScene", {}]) \
            .check()

    def test_assignment_before_scene(self):
        RowBuilder \
            .of("i = 0")\
            .nl("scene \"TestScene\";") \
            .nl("\tu = 1") \
            .row([0, "Assign", {'global': 'No', 'ID': 'i', 'type': 'Number', 'assignment': "0"}]) \
            .row([1, "Assign", {'global': 'No', 'ID': 'u', 'type': 'Number', 'assignment': "1"}]) \
            .row([2, "StopScene", {}]) \
            .check()

    def test_simple_single_choice_assignment(self):
        RowBuilder \
            .of("scene \"TestScene\";") \
            .nl("\tchoice = {\"Choice1\"}") \
            .row([0, "Choice", {'choice0': "Choice1"}]) \
            .row([1, "Assign", {'global': 'No', 'ID': 'choice', 'type': 'ID', 'assignment': "$0"}]) \
            .row([2, "StopScene", {}]) \
            .check()

    def test_simple_multi_choice_assignment(self):
        RowBuilder \
            .of("scene \"TestScene\";") \
            .nl('\tchoice = {"Choice1", "Choice2"}') \
            .row([0, "Choice", {'choice0': "Choice1", 'choice1': "Choice2"}]) \
            .row([1, "Assign", {'global': 'No', 'ID': 'choice', 'type': 'ID', 'assignment': "$0"}]) \
            .row([2, "StopScene", {}]) \
            .check()

    def test_simple_string_with_escape_quote(self):
        RowBuilder \
            .of("scene \"TestScene\";") \
            .nl('\t' + r'x = "Te\"st"') \
            .row([0, "Assign", {'global': 'No', 'ID': "x", 'type': "String", 'assignment': r'\"Te\"st\"'}]) \
            .row([1, "StopScene", {}]) \
            .check()

    def test_simple_string_surround_escape_quotes(self):
        RowBuilder \
            .of("scene \"TestScene\";") \
            .nl('\t' + r'x = "\"Test\""') \
            .row([0, "Assign", {'global': 'No', 'ID': "x", 'type': "String", 'assignment': r'\"\"Test\"\"'}]) \
            .row([1, "StopScene", {}]) \
            .check()

    def test_expression_with_string(self):
        RowBuilder \
            .of("scene \"TestScene\";") \
            .nl('\tx = "Test"') \
            .row([0, "Assign", {'global': 'No', 'ID': "x", 'type': "String", 'assignment': r'\"Test\"'}]) \
            .row([1, "StopScene", {}]) \
            .check()

    def test_simple_string_with_escape_backslash(self):
        RowBuilder \
            .of("scene \"TestScene\";") \
            .nl('\tx = "\\\\Test"') \
            .row([0, "Assign", {'global': 'No', 'ID': "x", 'type': "String", 'assignment': r'\"\\Test\"'}]) \
            .row([1, "StopScene", {}]) \
            .check()

    def test_simple_while(self):
        RowBuilder \
            .of("scene \"TestScene\";") \
            .nl("\twhile u != 0;") \
            .nl("\t\tu = 0") \
            .row([0, "Label", {'name': 'beginWhile_0'}])\
            .row([1, "Expression", {'operator': '!=', 'x': 'u', 'y': '0'}]) \
            .row([2, "If", {'condition': '$1', 'jump': 'endWhile_0'}]) \
            .row([3, "Assign", {'global': 'No', 'ID': 'u', 'type': 'Number', 'assignment': "0"}]) \
            .row([4, "JumpToLabel", {'name': 'beginWhile_0'}]) \
            .row([5, "Label", {'name': 'endWhile_0'}]) \
            .row([6, "StopScene", {}]) \
            .check()

    def test_simple_while_false_reduction(self):
        RowBuilder \
            .of("scene \"TestScene\";") \
            .nl("\twhile False;") \
            .nl("\t\tu = 0") \
            .row([0, "StopScene", {}]) \
            .check()

    def test_simple_if_else(self):
        RowBuilder \
            .of('scene "TestScene";')\
            .nl('\tif u == 1;')\
            .nl('\t\ty == 1')\
            .nl('\telse;')\
            .nl('\t\tw = 5') \
            .row([0, "Expression", {'operator': '==', 'x': 'u', 'y': '1'}]) \
            .row([1, "If", {'condition': '$0', 'jump': 'elseif_0'}]) \
            .row([2, "Assign", {'global': 'No', 'ID': 'y', 'type': 'Number', 'assignment': "1"}]) \
            .row([3, "JumpToLabel", {'name': 'endIf_0'}])\
            .row([4, "Label", {'name': 'elseif_0'}]) \
            .row([5, "Assign", {'global': 'No', 'ID': 'w', 'type': 'Number', 'assignment': "5"}]) \
            .row([6, "Label", {'name': 'endIf_0'}]) \

    def test_simple_dialog_with_emotion(self):
        RowBuilder \
            .of("scene \"TestScene\";") \
            .nl('\t@ actor ("Thinking"): "Hello World"') \
            .row([0, "Dialog", {'speaker': 'actor', 'emotion': 'Thinking', 'text': 'Hello World'}]) \
            .row([1, "StopScene", {}]) \
            .check()

    def test_simple_custom_direction(self):
        RowBuilder \
            .of("scene \"TestScene\";") \
            .nl('\t["Test"]') \
            .row([0, "Test", {}]) \
            .row([1, "StopScene", {}]) \
            .check()

    def test_complex_custom_direction(self):
        RowBuilder \
            .of("scene \"TestScene\";") \
            .nl('\t["Test", "Test1", "Test2"]') \
            .row([0, "Test", {"param1": "Test1", "param2": "Test2"}]) \
            .row([1, "StopScene", {}]) \
            .check()

#    def test_simple_if_elif(self):
#        RowBuilder \
#            .of('scene "TestScene";') \
#            .nl('\tif u == 1;') \
#            .nl('\t\ty == 1') \
#            .nl('\telif u == 2;') \
#            .nl('\t\tw = 5') \
#            .row([0, "Expression", {'operator': '==', 'x': 'u', 'y': '1'}]) \
#           .row([1, "If", {'condition': '$0', 'jump': 'elseif_0'}]) \
#           .row([2, "Assign", {'global': 'No', 'ID': 'y', 'type': 'Number', 'assignment': "1"}]) \
#           .row([3, "JumpToLabel", {'name': 'endIf_0'}]) \
#           .row([4, "Label", {'name': 'elseif_0'}]) \
#           .row([0, "Expression", {'operator': '==', 'x': 'u', 'y': '2'}]) \
#            .row([1, "If", {'condition': '$0', 'jump': 'elseif_0'}]) \
#            .row([5, "Assign", {'global': 'No', 'ID': 'w', 'type': 'Number', 'assignment': "5"}]) \
#            .row([6, "JumpToLabel", {'name': 'endIf_0'}]) \
#            .row([7, "Label", {'name': 'elseif_0'}]) \
#            .row([8, "Label", {'name': 'endIf_0'}]) \

