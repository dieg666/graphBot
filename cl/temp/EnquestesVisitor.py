# Generated from Enquestes.g by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .EnquestesParser import EnquestesParser
else:
    from EnquestesParser import EnquestesParser

# This class defines a complete generic visitor for a parse tree produced by EnquestesParser.

class EnquestesVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by EnquestesParser#root.
    def visitRoot(self, ctx:EnquestesParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#op.
    def visitOp(self, ctx:EnquestesParser.OpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#stop.
    def visitStop(self, ctx:EnquestesParser.StopContext):
        return self.visitChildren(ctx)



del EnquestesParser