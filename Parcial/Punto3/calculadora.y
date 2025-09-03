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
