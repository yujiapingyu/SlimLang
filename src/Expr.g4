grammar Expr;

prog:   (stat NEWLINE)* ;

stat:   assignment                    # assignStat
    |   whileLoop                     # whileStat
    |   ifStatement                   # ifStat
    |   expr                          # exprStat
    |   breakLoop                     # breakStat
    |   printStatement                # printStat
    ;

assignment : ID '=' expr ;

whileLoop : 'while' '(' expr ')' '{' NEWLINE whileBody '}';

whileBody: (stat NEWLINE)* (breakLoop NEWLINE)? ;

ifStatement : 'if' '(' expr ')' '{' NEWLINE prog '}' ('else' '{' NEWLINE prog '}')? ;

printStatement : 'print' '(' expr ')' ;

expr:   left=expr op=('*'|'/') right=expr   # mulDivExpr
    |   left=expr op=('+'|'-') right=expr # addSubExpr
    |   left=expr op='%' right=expr # modExpr
    | left=expr op=('>'|'<'|'=='|'!='|'>='|'<=') right=expr # relationalExpr
    | INT # intExpr
    | ID # idExpr
    | '(' expr ')' # parensExpr
    ;

ID : [a-zA-Z_][a-zA-Z_0-9]* ; // 变量名
INT : [0-9]+ ; // 整数
MUL : '*' ; // 乘法
DIV : '/' ; // 除法
ADD : '+' ; // 加法
SUB : '-' ; // 减法
MOD : '%' ; // 求余
GT : '>' ; // 大于
LT : '<' ; // 小于
GTEQ : '>=' ; // 大于等于
LTEQ : '<=' ; // 小于等于
EQ : '==' ; // 等于
NEQ : '!=' ; // 不等于
NEWLINE : [\r\n]+ ; // 新行符号
breakLoop : 'break' ; // break语句

WS : [ \t]+ -> skip ; // 忽略空白