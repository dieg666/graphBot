grammar Enquestes;
root:
    op END EOF
    ;
op :
    assigs
    | link
    ;
assigs:
    ID ASSIG question
    ;
question:
    QUEST (ID)+ QMARK
    ;
link:
    ID
    ;

ASSIG : ':';
LINK : '->';
EOA : ';' ;
COMMA : ',';
LPAR : '(';
RPAR : ')';
LBRA : '[';
RBRA : ']';
QMARK : '?' ;
QUEST : 'PREGUNTA' ;
ANSW : 'RESPOSTA' ;
ALT : 'ALTERNATIVA' ;
ITEM: 'ITEM' ;
ENQUE: 'ENQUESTA' ;
END : 'END' ;
NUM : [0-9]+ ;
ID : [a-zA-Z][a-zA-Z0-9]*[0-9] ;
WORD : [a-zA-Z]+ ;
SPACE: [ \t\r\n] -> skip;
NEWLINE             : ('\r'? '\n' | '\r')+ ;
