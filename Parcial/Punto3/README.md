# Punto 3

## Archivos del proyecto
1. `calc.l` → analizador léxico (Flex).  
2. `calc.y` → analizador sintáctico (Bison).  

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

extern FILE *yyin;   /* para leer desde archivo */
int yylex(void);
void yyerror(const char *s);
%}


%union {
    double fval;
}

%token <fval> NUMBER
%token SQRT EOL
%type  <fval> expr

%%

calclist:
    /* vacío */
  | calclist expr EOL   { printf("= %.4f\n", $2); }
  ;

expr:
    NUMBER                 { $$ = $1; }
  | SQRT '(' expr ')'      { $$ = sqrt($3); }
  ;

%%

int main(int argc, char **argv) {
       if (argc > 1) {
        yyin = fopen(argv[1], "r");
        if (!yyin) {
            perror("No se pudo abrir el archivo");
            return 1;
        }
    }

    return yyparse();
}

void yyerror(const char *s) {
    fprintf(stderr, "error: %s\n", s);
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
```bash
bison -d calc.y
flex calc.l
gcc -o calc calculadora.tab.c lex.yy.c  -lm -lfl
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
