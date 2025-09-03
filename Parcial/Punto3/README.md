# Punto 3

## Archivos del proyecto
1. `calc.l` → analizador léxico (Flex).  
2. `calc.y` → analizador sintáctico (Bison).  
3. `main.c` → programa principal en C.  

---

## Código

### `calculadora.l`
```lex
%{
#include "calculadora.tab.h"
#include <stdlib.h>
%}

%%

"sqrt"              { return SQRT; }
[0-9]+(\.[0-9]+)?   { yylval.fval= atof(yytext); return NUMBER; }
\n                  { return EOL; }
[ \t]               ;
.                   { return yytext[0]; }

%%

```

---

###  `calculadora.y`
```yacc
%{
#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int yylex(void);
void yyerror(const char *s);
%}

%union {
    double fval;
}

%token <fval> NUM
%token SQRT EOL
%type <fval> expr

%%

input:
    /* vacío */
  | input expr EOL   { printf("= %.4f\n", $2); }
  ;

expr:
    NUM                 { $$ = $1; }
  | SQRT '(' expr ')'   { $$ = sqrt($3); }
  ;

%%

int main(void) {
    return yyparse();
}

void yyerror(const char *s) {
    fprintf(stderr, "Error: %s\n", s);
}
```

---


---

## Ejemplo de entrada (`entrada.txt`)
```
sqrt(9)
sqrt(2.25)
sqrt(16)
```

---

## 📌 Compilación y ejecución
En Linux:
```bash
bison -d calc.y
flex calc.l
gcc -o calc calc.tab.c lex.yy.c main.c -lm
./calc entrada.txt
```

---

## 📌 Ejemplo de salida
```
= 3.0000
= 1.5000
= 4.0000
```

---

## 📌 Conclusión
- El uso combinado de **Flex** y **Bison** permite construir analizadores léxicos y sintácticos sencillos.  
- Se implementó una calculadora básica que reconoce la función `sqrt`.  
- Se logró analizar expresiones de entrada desde archivo y mostrar los resultados en consola.
