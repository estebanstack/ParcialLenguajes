%{
#include <stdio.h>
#include <math.h>

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

int main(void) {
    return yyparse();
}

void yyerror(const char *s) {
    fprintf(stderr, "error: %s\n", s);
}
