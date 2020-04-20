import sys

from antlr4 import *
from antlr4.tree.Trees import Trees

from SpecLangLexer import SpecLangLexer
from SpecLangParser import SpecLangParser
from SpecLangWalker import SpecLangWalker


def main(argv):
    input_stream = FileStream(argv[1])
    lexer = SpecLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SpecLangParser(stream)
    #parser.removeErrorListeners()
    #parser.addErrorListener(SpecLangErrorListener())
    tree = parser.statement()
    print(Trees.toStringTree(tree, None, parser))
    visitor = SpecLangWalker()
    result = visitor.visit(tree)
    print(visitor.rows)


if __name__ == '__main__':
    main(sys.argv)

