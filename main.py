import sys
from antlr4 import *
from lpv.DartLexer import DartLexer
from lpv.DartParser import DartParser
from DartCustomVisitor import DartCustomVisitor
 
def main(argv):
    input_stream = FileStream(argv[1])
    lexer = DartLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = DartParser(stream)
    tree = parser.start()

    visitor = DartCustomVisitor()
    visitor.visitStart(tree)

if __name__ == '__main__':
    main(sys.argv)