grammar Enquestes;

botGraph:
     (op)+ enquesta END;

enquesta:
     WORD EQ ENQUESTA (IDTEM)+
     ;
op:
     preg
     | resp
     | item
     | alter
     ;
preg:
     IDPREG EQ PREGUNTA (WORD)+ QMARK
     ;
resp:
     IDRES EQ RESPOSTA opcio+
     ;
opcio:
     NUM EQ (WORD)+ SEMIQ
     ;
item:
     IDTEM EQ ITEM IDPREG ASSIG IDRES
     ;
alter:
     IDALT EQ ALTERNATIVA IDTEM RBRAC alterItems LBRAC
     ;
alterItems:
     RPAR NUM COMA IDTEM LPAR (COMA alterItems)*
     ;

COMA : ',';
EQ : ':';
SEMIQ : ';';
QMARK : '?';
ASSIG : '->';
RPAR : '(';
LPAR : ')';
RBRAC : '[';
LBRAC : ']';
PREGUNTA :'PREGUNTA';
RESPOSTA : 'RESPOSTA';
ALTERNATIVA : 'ALTERNATIVA';
ENQUESTA : 'ENQUESTA';
ITEM : 'ITEM';
END : 'END';
NUM : [0-9]+ ;
IDTEM : 'I'[0-9]+;
IDPREG : 'P'[0-9]+;
IDRES : 'R'[0-9]+;
IDALT : 'A'[0-9]+;
WORD : [a-zA-Z]+;
WS : [ \t\r\n\f]+ -> skip;
