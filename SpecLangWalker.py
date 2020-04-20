from SpecLangParser import SpecLangParser
from SpecLangVisitor import SpecLangVisitor


class SpecLangWalker(SpecLangVisitor):
    rowNum = 0
    rows = []

    def visitChoice(self, ctx:SpecLangParser.ChoiceContext):
        print(ctx.STRING())
        #return [++self.rowNum, "Choice", {'choices'}]

    def visitDialog(self, ctx:SpecLangParser.DialogContext):
        return [++self.rowNum, "Dialog", {'speaker': self.visit(ctx.term(0)), 'emotion': 'Neutral', 'text': self.visit(ctx.term(1))}]

    def visitTerm(self, ctx:SpecLangParser.TermContext):
        return ctx.getText()
