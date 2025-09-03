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
