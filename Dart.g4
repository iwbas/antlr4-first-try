grammar Dart;

start: Main LBrace RBrace LFBrace statementSeq RFBrace;
// Done
declare: typeName Id (Assign exp)?;
typeName: Real | Integer;

statementSeq: (statement)*;
statement: simpleStatement | complexStatement;
simpleStatement: (declare | let | keyboardIn | out) Semicolon;
complexStatement: ifC | whileC;

// Done
let: Id Assign exp;
keyboardIn: Input LBrace Id RBrace;
out: Output LBrace Id RBrace;
//Done
ifC: If LBrace exp RBrace LFBrace statementSeq RFBrace (Else LFBrace statementSeq RFBrace)?;
whileC: While LBrace exp RBrace LFBrace statementSeq RFBrace;


// Done
exp: simpleExpr ((BoolEq | BoolNeq | BoolG | BoolL | BoolLeq | BoolGeq) exp)?; 
simpleExpr: term ((AddOp | SubOp | BoolOr) simpleExpr)?;
term: signedFactor ((MulOp | DivOp | BoolAnd) term)?;
signedFactor: (AddOp | SubOp)? factor;
factor:  Id | ( IntValue | RealValue ) | (LBrace exp RBrace);












Main: 'main';

AddOp: '+';
SubOp: '-';
MulOp: '*';
DivOp: '/';
ModOp: '%';

// BitOr: '|';
// BitAnd: '&';
// BitXor: '^';

BoolOr: '||';
BoolAnd: '&&';

BoolEq: '==';
BoolNeq: '!=';
BoolG: '>';
BoolL: '<';
BoolGeq: '>=';
BoolLeq: '<=';
BoolNot: '!';

Colon: ':';
Semicolon: ';';
Comma: ',';
Point: '.';

Let: 'let';
Input: 'input';
Output: 'output';

If: 'if';
Else: 'else';
While: 'while';

LBrace: '(';
RBrace: ')';
LSBrace: '[';
RSBrace: ']';
LFBrace: '{';
RFBrace: '}';
Assign: '=';

// fragment Integer: 'int';
// fragment Real: 'real';

Integer: 'int';
Real: 'real';

fragment Letter: [a-zA-Z];
fragment Digit: [0-9];
IntValue: Digit+;
RealValue: Digit*Point?Digit+([eE][-+]?Digit+)?;
Id: Letter (Letter | Digit)*;

Comment: ('//' ~[\r\n]* | '/*' .*? '*/') -> skip;
Ws: [ \t\r\n] -> skip;
