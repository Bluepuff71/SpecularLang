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
    tree = parser.block()
    print(Trees.toStringTree(tree, None, parser))
    visitor = SpecLangWalker()
    result = visitor.visit(tree)
<<<<<<< Updated upstream
    print(visitor.rows)

=======
    for row in visitor.rows:
       print(row)
>>>>>>> Stashed changes

if __name__ == '__main__':
    main(sys.argv)

