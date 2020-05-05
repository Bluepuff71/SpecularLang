import sys

from antlr4 import *

from SpecLangLexer import SpecLangLexer
from SpecLangParser import SpecLangParser
from SpecLangWalker import SpecLangWalker


def main(argv):
    input_stream = FileStream(argv[1])
    lexer = SpecLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SpecLangParser(stream)
    tree = parser.program()
    visitor = SpecLangWalker()
    visitor.visit(tree)


if __name__ == '__main__':
    main(sys.argv)
