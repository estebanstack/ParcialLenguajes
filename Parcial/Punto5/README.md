# Punto 5

## Gramática ANTLR (`Fibo.g4`)
```antlr
grammar Fibo;

prog: 'FIBO' '(' INT ')' EOF ;

INT : [0-9]+ ;
WS  : [ \t\r\n]+ -> skip ;
```

Esta gramática reconoce entradas como:
```
FIBO(8)
FIBO(20)
```

---

## Implementación en Python (`main.py`)
```python
import sys
from antlr4 import *
from FiboLexer import FiboLexer
from FiboParser import FiboParser

# Función para generar secuencia de Fibonacci
def fibonacci_seq(n):
    seq = [0, 1]
    for i in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq[:n]

def main():
    # Leer comando desde entrada estándar
    input_stream = InputStream(input("Ingrese comando"))

    lexer = FiboLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = FiboParser(stream)
    tree = parser.prog()

    # Extraer número
    num_text = tree.INT().getText()
    num = int(num_text)

    # Calcular y mostrar secuencia
    seq = fibonacci_seq(num)
    print(", ".join(map(str, seq)))

if __name__ == '__main__':
    main()
```

---

## Pasos para ejecutar

1. Generar el lexer y parser en Python con ANTLR:
```bash
antlr4 -Dlanguage=Python3 Fibo.g4
```

2. Ejecutar el programa en Python:
```bash
python3 main.py
```

3. Escribir el comando de prueba, por ejemplo:
```
FIBO(8)
```

---

## Ejemplo de salida
```
Ingrese comando FIBO(8)
0, 1, 1, 2, 3, 5, 8, 13
```

---

## Conclusión
- ANTLR permite definir de manera sencilla la gramática del lenguaje de entrada.  
- La gramática reconoce comandos `FIBO(n)` donde `n` es un número entero.  
- Con el parser en Python se extrae el valor de `n` y se genera la secuencia de Fibonacci correspondiente.  
- La integración de ANTLR y Python facilita la construcción de intérpretes simples.
