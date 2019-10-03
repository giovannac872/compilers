
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ABRECHAVES ABRECOLCHETE ABREPARENTESES ASPAS ATRIBUICAO CADEIACARACTERE CARACTERE CARACTERECONSTANTE COMENTARIOMAISUMALINHA COMENTARIOUMALINHA COMPARACAODIFERENTE COMPARACAOIGUAL COMPARACAOMAIOR COMPARACAOMAIOROUIGUAL COMPARACAOMENOR COMPARACAOMENOROUIGUAL DOISPONTOS ENQUANTO ENTAO ESCREVA EXECUTE FECHACHAVES FECHACOLCHETE FECHAPARENTESES IDENTIFICADOR INTEIRO INTEIROCONSTANTE LEIA NOVALINHA OPERADORDIVISAO OPERADORLOGICOE OPERADORLOGICOOU OPERADORNEGACAO OPERADORRESTODIVISAO OPERADORSOMA OPERADORSUBTRACAO OPERADORTERNARIO OPERADORVEZES PONTOEVIRGULA PROGRAMA RETORNE SE SENAO VIRGULA\n    programa : declfuncvar declprog\n    \n    declfuncvar : tipo IDENTIFICADOR declvar PONTOEVIRGULA declfuncvar\n    declfuncvar : tipo IDENTIFICADOR ABRECOLCHETE  INTEIROCONSTANTE FECHACOLCHETE declvar PONTOEVIRGULA declfuncvar\n    declfuncvar : tipo IDENTIFICADOR declfunc declfuncvar\n    declfuncvar : \n    \n    declprog : PROGRAMA bloco\n    \n    declvar : VIRGULA IDENTIFICADOR declvar\n    declvar : VIRGULA IDENTIFICADOR ABRECOLCHETE INTEIROCONSTANTE FECHACOLCHETE declvar\n    declvar : \n    \n    declfunc : ABREPARENTESES listaparametros FECHAPARENTESES bloco\n    \n    listaparametros : \n    listaparametros : listaparametroscont\n    \n    listaparametroscont : tipo IDENTIFICADOR\n    listaparametroscont : tipo IDENTIFICADOR ABRECOLCHETE FECHACOLCHETE\n    listaparametroscont : tipo IDENTIFICADOR VIRGULA listaparametroscont\n    listaparametroscont : tipo IDENTIFICADOR ABRECOLCHETE FECHACOLCHETE VIRGULA listaparametroscont\n    \n    bloco : ABRECHAVES listadeclvar listacomando FECHACHAVES\n    bloco : ABRECHAVES listadeclvar FECHACHAVES\n    \n    listadeclvar : \n    listadeclvar : tipo IDENTIFICADOR declvar PONTOEVIRGULA listadeclvar\n    listadeclvar : tipo IDENTIFICADOR ABRECOLCHETE INTEIROCONSTANTE FECHACOLCHETE declvar PONTOEVIRGULA listadeclvar\n    \n    tipo : INTEIRO\n    tipo : CARACTERE\n    \n    listacomando : comando\n    listacomando : comando listacomando\n    \n    comando : PONTOEVIRGULA\n    comando : expr PONTOEVIRGULA\n    comando : RETORNE expr PONTOEVIRGULA\n    comando : LEIA lvalueexpr PONTOEVIRGULA\n    comando : ESCREVA  expr PONTOEVIRGULA\n    comando : ESCREVA CADEIACARACTERE PONTOEVIRGULA\n    comando : NOVALINHA PONTOEVIRGULA\n    comando : SE ABREPARENTESES expr FECHAPARENTESES ENTAO comando\n    comando : SE ABREPARENTESES expr FECHAPARENTESES ENTAO comando SENAO comando\n    comando : ENQUANTO ABREPARENTESES expr FECHAPARENTESES EXECUTE comando\n    comando : bloco\n    \n    expr : assignexpr\n    \n    assignexpr : condexpr\n    assignexpr : lvalueexpr ATRIBUICAO assignexpr\n    \n    condexpr : orexpr\n    condexpr : orexpr OPERADORTERNARIO expr DOISPONTOS condexpr\n    \n    orexpr : orexpr OPERADORLOGICOOU andexpr\n    orexpr : andexpr\n    \n    andexpr : andexpr OPERADORLOGICOE eqexpr\n    andexpr : eqexpr\n    \n    eqexpr : eqexpr COMPARACAOIGUAL desigexpr\n    eqexpr : eqexpr COMPARACAODIFERENTE desigexpr\n    eqexpr : desigexpr\n    \n    desigexpr : desigexpr COMPARACAOMENOR addexpr\n    desigexpr : desigexpr COMPARACAOMAIOR addexpr\n    desigexpr : desigexpr COMPARACAOMAIOROUIGUAL addexpr\n    desigexpr : desigexpr COMPARACAOMENOROUIGUAL addexpr\n    desigexpr : addexpr\n    \n    addexpr : addexpr OPERADORSOMA mulexpr\n    addexpr : addexpr OPERADORSUBTRACAO mulexpr\n    addexpr : mulexpr\n    \n    mulexpr : mulexpr OPERADORVEZES unexpr\n    mulexpr : mulexpr OPERADORDIVISAO unexpr\n    mulexpr : mulexpr OPERADORRESTODIVISAO unexpr\n    mulexpr : unexpr\n    \n    unexpr : OPERADORSUBTRACAO primexpr\n    unexpr : OPERADORNEGACAO primexpr\n    unexpr : primexpr\n    \n    lvalueexpr : IDENTIFICADOR ABRECOLCHETE expr FECHACOLCHETE\n    lvalueexpr : IDENTIFICADOR\n    \n    primexpr : IDENTIFICADOR ABREPARENTESES listexpr FECHAPARENTESES\n    primexpr : IDENTIFICADOR ABREPARENTESES FECHAPARENTESES\n    primexpr : IDENTIFICADOR ABRECOLCHETE expr FECHACOLCHETE\n    primexpr : IDENTIFICADOR\n    primexpr : CARACTERECONSTANTE\n    primexpr : INTEIROCONSTANTE\n    primexpr :  ABREPARENTESES expr FECHAPARENTESES\n    \n    listexpr : assignexpr\n    listexpr : listexpr VIRGULA assignexpr\n   '
    
_lr_action_items = {'COMPARACAOMENOR':([35,41,43,44,47,53,57,60,70,71,79,110,111,114,117,118,122,123,124,125,126,131,132,133,142,143,150,],[-70,-63,-69,-71,-53,90,-60,-56,-69,-62,-61,90,90,-67,-55,-54,-72,-50,-51,-52,-49,-59,-58,-57,-68,-66,-68,]),'INTEIRO':([0,10,13,14,16,42,63,65,96,101,104,136,155,],[2,2,2,2,2,-18,2,-10,-17,2,2,2,2,]),'DOISPONTOS':([35,36,37,41,43,44,47,51,53,54,56,57,60,70,71,79,106,109,110,111,114,117,118,122,123,124,125,126,129,130,131,132,133,142,143,150,154,],[-70,-43,-45,-63,-69,-71,-53,-38,-48,-37,-40,-60,-56,-69,-62,-61,-39,-44,-46,-47,-67,-55,-54,-72,-50,-51,-52,-49,146,-42,-59,-58,-57,-68,-66,-68,-41,]),'ENQUANTO':([14,24,38,42,46,50,75,95,96,104,119,120,127,128,137,149,151,155,156,157,158,159,160,],[-19,33,-36,-18,-26,33,-32,-27,-17,-19,-28,-29,-30,-31,-20,33,33,-19,-35,-33,-21,33,-34,]),'IDENTIFICADOR':([1,2,4,11,14,20,23,24,34,38,42,45,46,48,49,50,52,55,68,69,72,73,74,75,76,77,78,80,81,87,88,89,90,93,94,95,96,97,98,99,104,108,119,120,121,127,128,137,144,146,149,151,155,156,157,158,159,160,],[6,-22,-23,18,-19,29,31,43,70,-36,-18,70,-26,43,84,43,43,43,43,43,70,70,70,-32,43,43,43,70,70,70,70,70,70,43,70,-27,-17,70,70,70,-19,43,-28,-29,43,-30,-31,-20,43,70,43,43,-19,-35,-33,-21,43,-34,]),'INTEIROCONSTANTE':([12,14,24,27,34,38,42,45,46,48,50,52,55,67,68,69,72,73,74,75,76,77,78,80,81,87,88,89,90,93,94,95,96,97,98,99,104,108,119,120,121,127,128,137,144,146,149,151,155,156,157,158,159,160,],[19,-19,44,61,44,-36,-18,44,-26,44,44,44,44,105,44,44,44,44,44,-32,44,44,44,44,44,44,44,44,44,44,44,-27,-17,44,44,44,-19,44,-28,-29,44,-30,-31,-20,44,44,44,44,-19,-35,-33,-21,44,-34,]),'OPERADORSUBTRACAO':([14,24,35,38,41,42,43,44,46,47,48,50,52,55,57,60,68,69,70,71,72,73,74,75,76,77,78,79,80,81,87,88,89,90,93,94,95,96,97,98,99,104,108,114,117,118,119,120,121,122,123,124,125,126,127,128,131,132,133,137,142,143,144,146,149,150,151,155,156,157,158,159,160,],[-19,45,-70,-36,-63,-18,-69,-71,-26,80,45,45,45,45,-60,-56,45,45,-69,-62,45,45,45,-32,45,45,45,-61,45,45,45,45,45,45,45,45,-27,-17,45,45,45,-19,45,-67,-55,-54,-28,-29,45,-72,80,80,80,80,-30,-31,-59,-58,-57,-20,-68,-66,45,45,45,-68,45,-19,-35,-33,-21,45,-34,]),'EXECUTE':([139,],[149,]),'PONTOEVIRGULA':([6,9,14,18,24,26,28,31,35,36,37,38,39,41,42,43,44,46,47,50,51,53,54,56,57,58,60,62,66,70,71,75,79,82,83,84,91,92,95,96,100,104,106,109,110,111,114,117,118,119,120,122,123,124,125,126,127,128,130,131,132,133,134,137,138,142,143,148,149,150,151,153,154,155,156,157,158,159,160,],[-9,16,-19,-9,46,-7,-9,-9,-70,-43,-45,-36,75,-63,-18,-69,-71,-26,-53,46,-38,-48,-37,-40,-60,95,-56,101,104,-69,-62,-32,-61,119,120,-65,127,128,-27,-17,-9,-19,-39,-44,-46,-47,-67,-55,-54,-28,-29,-72,-50,-51,-52,-49,-30,-31,-42,-59,-58,-57,-8,-20,-9,-68,-66,155,46,-68,46,-64,-41,-19,-35,-33,-21,46,-34,]),'CARACTERECONSTANTE':([14,24,34,38,42,45,46,48,50,52,55,68,69,72,73,74,75,76,77,78,80,81,87,88,89,90,93,94,95,96,97,98,99,104,108,119,120,121,127,128,137,144,146,149,151,155,156,157,158,159,160,],[-19,35,35,-36,-18,35,-26,35,35,35,35,35,35,35,35,35,-32,35,35,35,35,35,35,35,35,35,35,35,-27,-17,35,35,35,-19,35,-28,-29,35,-30,-31,-20,35,35,35,35,-19,-35,-33,-21,35,-34,]),'SENAO':([38,42,46,75,95,96,119,120,127,128,156,157,160,],[-36,-18,-26,-32,-27,-17,-28,-29,-30,-31,-35,159,-34,]),'COMPARACAOMAIOR':([35,41,43,44,47,53,57,60,70,71,79,110,111,114,117,118,122,123,124,125,126,131,132,133,142,143,150,],[-70,-63,-69,-71,-53,87,-60,-56,-69,-62,-61,87,87,-67,-55,-54,-72,-50,-51,-52,-49,-59,-58,-57,-68,-66,-68,]),'OPERADORVEZES':([35,41,43,44,57,60,70,71,79,114,117,118,122,131,132,133,142,143,150,],[-70,-63,-69,-71,-60,99,-69,-62,-61,-67,99,99,-72,-59,-58,-57,-68,-66,-68,]),'VIRGULA':([6,18,28,29,31,35,36,37,41,43,44,47,51,53,56,57,60,70,71,79,100,103,106,109,110,111,114,115,116,117,118,122,123,124,125,126,130,131,132,133,138,142,143,150,152,154,],[11,11,11,63,11,-70,-43,-45,-63,-69,-71,-53,-38,-48,-40,-60,-56,-69,-62,-61,11,136,-39,-44,-46,-47,-67,-73,144,-55,-54,-72,-50,-51,-52,-49,-42,-59,-58,-57,11,-68,-66,-68,-74,-41,]),'OPERADORRESTODIVISAO':([35,41,43,44,57,60,70,71,79,114,117,118,122,131,132,133,142,143,150,],[-70,-63,-69,-71,-60,97,-69,-62,-61,-67,97,97,-72,-59,-58,-57,-68,-66,-68,]),'OPERADORDIVISAO':([35,41,43,44,57,60,70,71,79,114,117,118,122,131,132,133,142,143,150,],[-70,-63,-69,-71,-60,98,-69,-62,-61,-67,98,98,-72,-59,-58,-57,-68,-66,-68,]),'RETORNE':([14,24,38,42,46,50,75,95,96,104,119,120,127,128,137,149,151,155,156,157,158,159,160,],[-19,48,-36,-18,-26,48,-32,-27,-17,-19,-28,-29,-30,-31,-20,48,48,-19,-35,-33,-21,48,-34,]),'LEIA':([14,24,38,42,46,50,75,95,96,104,119,120,127,128,137,149,151,155,156,157,158,159,160,],[-19,49,-36,-18,-26,49,-32,-27,-17,-19,-28,-29,-30,-31,-20,49,49,-19,-35,-33,-21,49,-34,]),'$end':([3,7,15,42,96,],[0,-1,-6,-18,-17,]),'ABREPARENTESES':([6,14,24,33,34,38,40,42,43,45,46,48,50,52,55,68,69,70,72,73,74,75,76,77,78,80,81,87,88,89,90,93,94,95,96,97,98,99,104,108,119,120,121,127,128,137,144,146,149,151,155,156,157,158,159,160,],[13,-19,52,69,52,-36,76,-18,78,52,-26,52,52,52,52,52,52,78,52,52,52,-32,52,52,52,52,52,52,52,52,52,52,52,-27,-17,52,52,52,-19,52,-28,-29,52,-30,-31,-20,52,52,52,52,-19,-35,-33,-21,52,-34,]),'FECHACHAVES':([14,24,38,42,46,50,59,75,85,95,96,104,119,120,127,128,137,155,156,157,158,160,],[-19,42,-36,-18,-26,-24,96,-32,-25,-27,-17,-19,-28,-29,-30,-31,-20,-19,-35,-33,-21,-34,]),'OPERADORLOGICOE':([35,36,37,41,43,44,47,53,57,60,70,71,79,109,110,111,114,117,118,122,123,124,125,126,130,131,132,133,142,143,150,],[-70,72,-45,-63,-69,-71,-53,-48,-60,-56,-69,-62,-61,-44,-46,-47,-67,-55,-54,-72,-50,-51,-52,-49,72,-59,-58,-57,-68,-66,-68,]),'OPERADORTERNARIO':([35,36,37,41,43,44,47,53,56,57,60,70,71,79,109,110,111,114,117,118,122,123,124,125,126,130,131,132,133,142,143,150,],[-70,-43,-45,-63,-69,-71,-53,-48,93,-60,-56,-69,-62,-61,-44,-46,-47,-67,-55,-54,-72,-50,-51,-52,-49,-42,-59,-58,-57,-68,-66,-68,]),'OPERADORNEGACAO':([14,24,38,42,46,48,50,52,55,68,69,72,73,74,75,76,77,78,80,81,87,88,89,90,93,94,95,96,97,98,99,104,108,119,120,121,127,128,137,144,146,149,151,155,156,157,158,159,160,],[-19,34,-36,-18,-26,34,34,34,34,34,34,34,34,34,-32,34,34,34,34,34,34,34,34,34,34,34,-27,-17,34,34,34,-19,34,-28,-29,34,-30,-31,-20,34,34,34,34,-19,-35,-33,-21,34,-34,]),'ESCREVA':([14,24,38,42,46,50,75,95,96,104,119,120,127,128,137,149,151,155,156,157,158,159,160,],[-19,55,-36,-18,-26,55,-32,-27,-17,-19,-28,-29,-30,-31,-20,55,55,-19,-35,-33,-21,55,-34,]),'ENTAO':([141,],[151,]),'CARACTERE':([0,10,13,14,16,42,63,65,96,101,104,136,155,],[4,4,4,4,4,-18,4,-10,-17,4,4,4,4,]),'NOVALINHA':([14,24,38,42,46,50,75,95,96,104,119,120,127,128,137,149,151,155,156,157,158,159,160,],[-19,39,-36,-18,-26,39,-32,-27,-17,-19,-28,-29,-30,-31,-20,39,39,-19,-35,-33,-21,39,-34,]),'COMPARACAOMENOROUIGUAL':([35,41,43,44,47,53,57,60,70,71,79,110,111,114,117,118,122,123,124,125,126,131,132,133,142,143,150,],[-70,-63,-69,-71,-53,89,-60,-56,-69,-62,-61,89,89,-67,-55,-54,-72,-50,-51,-52,-49,-59,-58,-57,-68,-66,-68,]),'SE':([14,24,38,42,46,50,75,95,96,104,119,120,127,128,137,149,151,155,156,157,158,159,160,],[-19,40,-36,-18,-26,40,-32,-27,-17,-19,-28,-29,-30,-31,-20,40,40,-19,-35,-33,-21,40,-34,]),'FECHAPARENTESES':([13,21,22,29,35,36,37,41,43,44,47,51,53,54,56,57,60,70,71,78,79,86,102,103,106,107,109,110,111,112,114,115,116,117,118,122,123,124,125,126,130,131,132,133,142,143,147,150,152,154,],[-11,-12,30,-13,-70,-43,-45,-63,-69,-71,-53,-38,-48,-37,-40,-60,-56,-69,-62,114,-61,122,-15,-14,-39,139,-44,-46,-47,141,-67,-73,143,-55,-54,-72,-50,-51,-52,-49,-42,-59,-58,-57,-68,-66,-16,-68,-74,-41,]),'OPERADORLOGICOOU':([35,36,37,41,43,44,47,53,56,57,60,70,71,79,109,110,111,114,117,118,122,123,124,125,126,130,131,132,133,142,143,150,],[-70,-43,-45,-63,-69,-71,-53,-48,94,-60,-56,-69,-62,-61,-44,-46,-47,-67,-55,-54,-72,-50,-51,-52,-49,-42,-59,-58,-57,-68,-66,-68,]),'ABRECHAVES':([8,14,24,30,38,42,46,50,75,95,96,104,119,120,127,128,137,149,151,155,156,157,158,159,160,],[14,-19,14,14,-36,-18,-26,14,-32,-27,-17,-19,-28,-29,-30,-31,-20,14,14,-19,-35,-33,-21,14,-34,]),'COMPARACAOMAIOROUIGUAL':([35,41,43,44,47,53,57,60,70,71,79,110,111,114,117,118,122,123,124,125,126,131,132,133,142,143,150,],[-70,-63,-69,-71,-53,88,-60,-56,-69,-62,-61,88,88,-67,-55,-54,-72,-50,-51,-52,-49,-59,-58,-57,-68,-66,-68,]),'PROGRAMA':([0,5,10,16,17,25,42,65,96,101,135,],[-5,8,-5,-5,-4,-2,-18,-10,-17,-5,-3,]),'ATRIBUICAO':([32,43,142,],[68,-65,-64,]),'CADEIACARACTERE':([55,],[92,]),'COMPARACAOIGUAL':([35,37,41,43,44,47,53,57,60,70,71,79,109,110,111,114,117,118,122,123,124,125,126,131,132,133,142,143,150,],[-70,73,-63,-69,-71,-53,-48,-60,-56,-69,-62,-61,73,-46,-47,-67,-55,-54,-72,-50,-51,-52,-49,-59,-58,-57,-68,-66,-68,]),'ABRECOLCHETE':([6,18,29,31,43,70,84,],[12,27,64,67,77,108,121,]),'FECHACOLCHETE':([19,35,36,37,41,43,44,47,51,53,54,56,57,60,61,64,70,71,79,105,106,109,110,111,113,114,117,118,122,123,124,125,126,130,131,132,133,140,142,143,145,150,154,],[28,-70,-43,-45,-63,-69,-71,-53,-38,-48,-37,-40,-60,-56,100,103,-69,-62,-61,138,-39,-44,-46,-47,142,-67,-55,-54,-72,-50,-51,-52,-49,-42,-59,-58,-57,150,-68,-66,153,-68,-41,]),'OPERADORSOMA':([35,41,43,44,47,57,60,70,71,79,114,117,118,122,123,124,125,126,131,132,133,142,143,150,],[-70,-63,-69,-71,81,-60,-56,-69,-62,-61,-67,-55,-54,-72,81,81,81,81,-59,-58,-57,-68,-66,-68,]),'COMPARACAODIFERENTE':([35,37,41,43,44,47,53,57,60,70,71,79,109,110,111,114,117,118,122,123,124,125,126,131,132,133,142,143,150,],[-70,74,-63,-69,-71,-53,-48,-60,-56,-69,-62,-61,74,-46,-47,-67,-55,-54,-72,-50,-51,-52,-49,-59,-58,-57,-68,-66,-68,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'eqexpr':([24,48,50,52,55,68,69,72,76,77,78,93,94,108,121,144,146,149,151,159,],[37,37,37,37,37,37,37,109,37,37,37,37,37,37,37,37,37,37,37,37,]),'lvalueexpr':([24,48,49,50,52,55,68,69,76,77,78,93,108,121,144,149,151,159,],[32,32,83,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,]),'declvar':([6,18,28,31,100,138,],[9,26,62,66,134,148,]),'primexpr':([24,34,45,48,50,52,55,68,69,72,73,74,76,77,78,80,81,87,88,89,90,93,94,97,98,99,108,121,144,146,149,151,159,],[41,71,79,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,]),'listaparametroscont':([13,63,136,],[21,102,147,]),'desigexpr':([24,48,50,52,55,68,69,72,73,74,76,77,78,93,94,108,121,144,146,149,151,159,],[53,53,53,53,53,53,53,53,110,111,53,53,53,53,53,53,53,53,53,53,53,53,]),'addexpr':([24,48,50,52,55,68,69,72,73,74,76,77,78,87,88,89,90,93,94,108,121,144,146,149,151,159,],[47,47,47,47,47,47,47,47,47,47,47,47,47,123,124,125,126,47,47,47,47,47,47,47,47,47,]),'listaparametros':([13,],[22,]),'andexpr':([24,48,50,52,55,68,69,76,77,78,93,94,108,121,144,146,149,151,159,],[36,36,36,36,36,36,36,36,36,36,36,130,36,36,36,36,36,36,36,]),'listadeclvar':([14,104,155,],[24,137,158,]),'declfuncvar':([0,10,16,101,],[5,17,25,135,]),'comando':([24,50,149,151,159,],[50,50,156,157,160,]),'condexpr':([24,48,50,52,55,68,69,76,77,78,93,108,121,144,146,149,151,159,],[51,51,51,51,51,51,51,51,51,51,51,51,51,51,154,51,51,51,]),'tipo':([0,10,13,14,16,63,101,104,136,155,],[1,1,20,23,1,20,1,23,20,23,]),'declfunc':([6,],[10,]),'programa':([0,],[3,]),'assignexpr':([24,48,50,52,55,68,69,76,77,78,93,108,121,144,149,151,159,],[54,54,54,54,54,106,54,54,54,115,54,54,54,152,54,54,54,]),'bloco':([8,24,30,50,149,151,159,],[15,38,65,38,38,38,38,]),'orexpr':([24,48,50,52,55,68,69,76,77,78,93,108,121,144,146,149,151,159,],[56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,]),'unexpr':([24,48,50,52,55,68,69,72,73,74,76,77,78,80,81,87,88,89,90,93,94,97,98,99,108,121,144,146,149,151,159,],[57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,131,132,133,57,57,57,57,57,57,57,]),'declprog':([5,],[7,]),'expr':([24,48,50,52,55,69,76,77,93,108,121,149,151,159,],[58,82,58,86,91,107,112,113,129,140,145,58,58,58,]),'listacomando':([24,50,],[59,85,]),'mulexpr':([24,48,50,52,55,68,69,72,73,74,76,77,78,80,81,87,88,89,90,93,94,108,121,144,146,149,151,159,],[60,60,60,60,60,60,60,60,60,60,60,60,60,117,118,60,60,60,60,60,60,60,60,60,60,60,60,60,]),'listexpr':([78,],[116,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> declfuncvar declprog','programa',2,'p_programa','mySintatic.py',8),
  ('declfuncvar -> tipo IDENTIFICADOR declvar PONTOEVIRGULA declfuncvar','declfuncvar',5,'p_declfuncvar','mySintatic.py',13),
  ('declfuncvar -> tipo IDENTIFICADOR ABRECOLCHETE INTEIROCONSTANTE FECHACOLCHETE declvar PONTOEVIRGULA declfuncvar','declfuncvar',8,'p_declfuncvar','mySintatic.py',14),
  ('declfuncvar -> tipo IDENTIFICADOR declfunc declfuncvar','declfuncvar',4,'p_declfuncvar','mySintatic.py',15),
  ('declfuncvar -> <empty>','declfuncvar',0,'p_declfuncvar','mySintatic.py',16),
  ('declprog -> PROGRAMA bloco','declprog',2,'p_declprog','mySintatic.py',21),
  ('declvar -> VIRGULA IDENTIFICADOR declvar','declvar',3,'p_declvar','mySintatic.py',26),
  ('declvar -> VIRGULA IDENTIFICADOR ABRECOLCHETE INTEIROCONSTANTE FECHACOLCHETE declvar','declvar',6,'p_declvar','mySintatic.py',27),
  ('declvar -> <empty>','declvar',0,'p_declvar','mySintatic.py',28),
  ('declfunc -> ABREPARENTESES listaparametros FECHAPARENTESES bloco','declfunc',4,'p_declfunc','mySintatic.py',33),
  ('listaparametros -> <empty>','listaparametros',0,'p_listaparametros','mySintatic.py',38),
  ('listaparametros -> listaparametroscont','listaparametros',1,'p_listaparametros','mySintatic.py',39),
  ('listaparametroscont -> tipo IDENTIFICADOR','listaparametroscont',2,'p_listaparametroscont','mySintatic.py',44),
  ('listaparametroscont -> tipo IDENTIFICADOR ABRECOLCHETE FECHACOLCHETE','listaparametroscont',4,'p_listaparametroscont','mySintatic.py',45),
  ('listaparametroscont -> tipo IDENTIFICADOR VIRGULA listaparametroscont','listaparametroscont',4,'p_listaparametroscont','mySintatic.py',46),
  ('listaparametroscont -> tipo IDENTIFICADOR ABRECOLCHETE FECHACOLCHETE VIRGULA listaparametroscont','listaparametroscont',6,'p_listaparametroscont','mySintatic.py',47),
  ('bloco -> ABRECHAVES listadeclvar listacomando FECHACHAVES','bloco',4,'p_bloco','mySintatic.py',52),
  ('bloco -> ABRECHAVES listadeclvar FECHACHAVES','bloco',3,'p_bloco','mySintatic.py',53),
  ('listadeclvar -> <empty>','listadeclvar',0,'p_listadeclvar','mySintatic.py',58),
  ('listadeclvar -> tipo IDENTIFICADOR declvar PONTOEVIRGULA listadeclvar','listadeclvar',5,'p_listadeclvar','mySintatic.py',59),
  ('listadeclvar -> tipo IDENTIFICADOR ABRECOLCHETE INTEIROCONSTANTE FECHACOLCHETE declvar PONTOEVIRGULA listadeclvar','listadeclvar',8,'p_listadeclvar','mySintatic.py',60),
  ('tipo -> INTEIRO','tipo',1,'p_tipo','mySintatic.py',65),
  ('tipo -> CARACTERE','tipo',1,'p_tipo','mySintatic.py',66),
  ('listacomando -> comando','listacomando',1,'p_listacomando','mySintatic.py',71),
  ('listacomando -> comando listacomando','listacomando',2,'p_listacomando','mySintatic.py',72),
  ('comando -> PONTOEVIRGULA','comando',1,'p_comando','mySintatic.py',76),
  ('comando -> expr PONTOEVIRGULA','comando',2,'p_comando','mySintatic.py',77),
  ('comando -> RETORNE expr PONTOEVIRGULA','comando',3,'p_comando','mySintatic.py',78),
  ('comando -> LEIA lvalueexpr PONTOEVIRGULA','comando',3,'p_comando','mySintatic.py',79),
  ('comando -> ESCREVA expr PONTOEVIRGULA','comando',3,'p_comando','mySintatic.py',80),
  ('comando -> ESCREVA CADEIACARACTERE PONTOEVIRGULA','comando',3,'p_comando','mySintatic.py',81),
  ('comando -> NOVALINHA PONTOEVIRGULA','comando',2,'p_comando','mySintatic.py',82),
  ('comando -> SE ABREPARENTESES expr FECHAPARENTESES ENTAO comando','comando',6,'p_comando','mySintatic.py',83),
  ('comando -> SE ABREPARENTESES expr FECHAPARENTESES ENTAO comando SENAO comando','comando',8,'p_comando','mySintatic.py',84),
  ('comando -> ENQUANTO ABREPARENTESES expr FECHAPARENTESES EXECUTE comando','comando',6,'p_comando','mySintatic.py',85),
  ('comando -> bloco','comando',1,'p_comando','mySintatic.py',86),
  ('expr -> assignexpr','expr',1,'p_expr','mySintatic.py',91),
  ('assignexpr -> condexpr','assignexpr',1,'p_assignexpr','mySintatic.py',96),
  ('assignexpr -> lvalueexpr ATRIBUICAO assignexpr','assignexpr',3,'p_assignexpr','mySintatic.py',97),
  ('condexpr -> orexpr','condexpr',1,'p_condexpr','mySintatic.py',102),
  ('condexpr -> orexpr OPERADORTERNARIO expr DOISPONTOS condexpr','condexpr',5,'p_condexpr','mySintatic.py',103),
  ('orexpr -> orexpr OPERADORLOGICOOU andexpr','orexpr',3,'p_orexpr','mySintatic.py',108),
  ('orexpr -> andexpr','orexpr',1,'p_orexpr','mySintatic.py',109),
  ('andexpr -> andexpr OPERADORLOGICOE eqexpr','andexpr',3,'p_andexpr','mySintatic.py',114),
  ('andexpr -> eqexpr','andexpr',1,'p_andexpr','mySintatic.py',115),
  ('eqexpr -> eqexpr COMPARACAOIGUAL desigexpr','eqexpr',3,'p_eqexpr','mySintatic.py',120),
  ('eqexpr -> eqexpr COMPARACAODIFERENTE desigexpr','eqexpr',3,'p_eqexpr','mySintatic.py',121),
  ('eqexpr -> desigexpr','eqexpr',1,'p_eqexpr','mySintatic.py',122),
  ('desigexpr -> desigexpr COMPARACAOMENOR addexpr','desigexpr',3,'p_desigexpr','mySintatic.py',127),
  ('desigexpr -> desigexpr COMPARACAOMAIOR addexpr','desigexpr',3,'p_desigexpr','mySintatic.py',128),
  ('desigexpr -> desigexpr COMPARACAOMAIOROUIGUAL addexpr','desigexpr',3,'p_desigexpr','mySintatic.py',129),
  ('desigexpr -> desigexpr COMPARACAOMENOROUIGUAL addexpr','desigexpr',3,'p_desigexpr','mySintatic.py',130),
  ('desigexpr -> addexpr','desigexpr',1,'p_desigexpr','mySintatic.py',131),
  ('addexpr -> addexpr OPERADORSOMA mulexpr','addexpr',3,'p_addexpr','mySintatic.py',136),
  ('addexpr -> addexpr OPERADORSUBTRACAO mulexpr','addexpr',3,'p_addexpr','mySintatic.py',137),
  ('addexpr -> mulexpr','addexpr',1,'p_addexpr','mySintatic.py',138),
  ('mulexpr -> mulexpr OPERADORVEZES unexpr','mulexpr',3,'p_mulexpr','mySintatic.py',143),
  ('mulexpr -> mulexpr OPERADORDIVISAO unexpr','mulexpr',3,'p_mulexpr','mySintatic.py',144),
  ('mulexpr -> mulexpr OPERADORRESTODIVISAO unexpr','mulexpr',3,'p_mulexpr','mySintatic.py',145),
  ('mulexpr -> unexpr','mulexpr',1,'p_mulexpr','mySintatic.py',146),
  ('unexpr -> OPERADORSUBTRACAO primexpr','unexpr',2,'p_unexpr','mySintatic.py',151),
  ('unexpr -> OPERADORNEGACAO primexpr','unexpr',2,'p_unexpr','mySintatic.py',152),
  ('unexpr -> primexpr','unexpr',1,'p_unexpr','mySintatic.py',153),
  ('lvalueexpr -> IDENTIFICADOR ABRECOLCHETE expr FECHACOLCHETE','lvalueexpr',4,'p_lvalueexpr','mySintatic.py',158),
  ('lvalueexpr -> IDENTIFICADOR','lvalueexpr',1,'p_lvalueexpr','mySintatic.py',159),
  ('primexpr -> IDENTIFICADOR ABREPARENTESES listexpr FECHAPARENTESES','primexpr',4,'p_primexpr','mySintatic.py',163),
  ('primexpr -> IDENTIFICADOR ABREPARENTESES FECHAPARENTESES','primexpr',3,'p_primexpr','mySintatic.py',164),
  ('primexpr -> IDENTIFICADOR ABRECOLCHETE expr FECHACOLCHETE','primexpr',4,'p_primexpr','mySintatic.py',165),
  ('primexpr -> IDENTIFICADOR','primexpr',1,'p_primexpr','mySintatic.py',166),
  ('primexpr -> CARACTERECONSTANTE','primexpr',1,'p_primexpr','mySintatic.py',167),
  ('primexpr -> INTEIROCONSTANTE','primexpr',1,'p_primexpr','mySintatic.py',168),
  ('primexpr -> ABREPARENTESES expr FECHAPARENTESES','primexpr',3,'p_primexpr','mySintatic.py',169),
  ('listexpr -> assignexpr','listexpr',1,'p_listexpr','mySintatic.py',174),
  ('listexpr -> listexpr VIRGULA assignexpr','listexpr',3,'p_listexpr','mySintatic.py',175),
]
