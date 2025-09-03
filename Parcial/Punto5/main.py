import sys
from antlr4 import *
from FiboLexer import FiboLexer
from FiboParser import FiboParser


def fibonacci_seq(n):
    seq = [0, 1]
    for i in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq[:n]

def main():
    # Leer entrada desde consola
    input_stream = InputStream(input("Ingrese comando"))

    # Lexer y parser
    lexer = FiboLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = FiboParser(stream)
    tree = parser.prog()

    # Extraer número del árbol
    num_text = tree.INT().getText()
    num = int(num_text)

    # Calcular fibonacci
    seq = fibonacci_seq(num)

    # Imprimir secuencia
    print(", ".join(map(str, seq)))

if __name__ == '__main__':
    main()
