
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPUNTOCOMAleftEQUALSleftMENORQMAYORQMENORIGUALMAYORIGUALleftMULTIDIVISIONleftSUMARESTABOOL DECIMAL DIVISION DOUBLE EQUALS FLOAT ID INT MAYORIGUAL MAYORQ MENORIGUAL MENORQ MULTI NUMERO PUNTOCOMA RESTA STRING SUMA TXTdeclaracion : INT expresion EQUALS expresion PUNTOCOMAdeclaracion :   INT expresion PUNTOCOMAdeclaracion : DOUBLE expresion EQUALS expresion PUNTOCOMAdeclaracion :  DOUBLE expresion PUNTOCOMAdeclaracion : FLOAT expresion EQUALS expresion PUNTOCOMAdeclaracion :  FLOAT expresion PUNTOCOMAdeclaracion : BOOL expresion EQUALS expresion PUNTOCOMAdeclaracion :  BOOL expresion PUNTOCOMAdeclaracion : STRING expresion EQUALS expresion PUNTOCOMAdeclaracion :  STRING expresion PUNTOCOMAdeclaracion :  expresion EQUALS expresion PUNTOCOMAdeclaracion : expresion PUNTOCOMA\n    expresion  :   expresion SUMA expresion \n                |   expresion RESTA expresion \n                |   expresion MULTI expresion\n                |   expresion DIVISION expresion \n\n    expresion : RESTA expresion %prec RESTA\n    expresion   :  expresion MENORQ expresion \n                |  expresion MAYORQ expresion \n                |  expresion MENORIGUAL expresion \n                |   expresion MAYORIGUAL expresion \n\n    expresion : DECIMALexpresion : NUMEROexpresion : IDexpresion : TXT'
    
_lr_action_items = {'INT':([0,],[2,]),'DOUBLE':([0,],[4,]),'FLOAT':([0,],[5,]),'BOOL':([0,],[6,]),'STRING':([0,],[7,]),'RESTA':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20,21,22,23,24,25,26,27,28,29,31,32,33,34,35,36,37,38,39,40,42,44,46,48,50,51,52,53,],[8,8,17,8,8,8,8,8,-22,-23,-24,-25,17,8,8,8,8,8,8,8,8,8,17,17,17,17,-17,8,17,-13,-14,17,17,17,17,17,17,8,8,8,8,17,17,17,17,17,]),'DECIMAL':([0,2,4,5,6,7,8,14,16,17,18,19,20,21,22,23,29,40,42,44,46,],[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'NUMERO':([0,2,4,5,6,7,8,14,16,17,18,19,20,21,22,23,29,40,42,44,46,],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'ID':([0,2,4,5,6,7,8,14,16,17,18,19,20,21,22,23,29,40,42,44,46,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'TXT':([0,2,4,5,6,7,8,14,16,17,18,19,20,21,22,23,29,40,42,44,46,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'$end':([1,15,30,41,43,45,47,49,54,55,56,57,58,],[0,-12,-2,-4,-6,-8,-10,-11,-1,-3,-5,-7,-9,]),'EQUALS':([3,9,10,11,12,13,24,25,26,27,28,32,33,34,35,36,37,38,39,],[14,-22,-23,-24,-25,29,40,42,44,46,-17,-13,-14,-15,-16,-18,-19,-20,-21,]),'PUNTOCOMA':([3,9,10,11,12,13,24,25,26,27,28,31,32,33,34,35,36,37,38,39,48,50,51,52,53,],[15,-22,-23,-24,-25,30,41,43,45,47,-17,49,-13,-14,-15,-16,-18,-19,-20,-21,54,55,56,57,58,]),'SUMA':([3,9,10,11,12,13,24,25,26,27,28,31,32,33,34,35,36,37,38,39,48,50,51,52,53,],[16,-22,-23,-24,-25,16,16,16,16,16,-17,16,-13,-14,16,16,16,16,16,16,16,16,16,16,16,]),'MULTI':([3,9,10,11,12,13,24,25,26,27,28,31,32,33,34,35,36,37,38,39,48,50,51,52,53,],[18,-22,-23,-24,-25,18,18,18,18,18,-17,18,-13,-14,-15,-16,18,18,18,18,18,18,18,18,18,]),'DIVISION':([3,9,10,11,12,13,24,25,26,27,28,31,32,33,34,35,36,37,38,39,48,50,51,52,53,],[19,-22,-23,-24,-25,19,19,19,19,19,-17,19,-13,-14,-15,-16,19,19,19,19,19,19,19,19,19,]),'MENORQ':([3,9,10,11,12,13,24,25,26,27,28,31,32,33,34,35,36,37,38,39,48,50,51,52,53,],[20,-22,-23,-24,-25,20,20,20,20,20,-17,20,-13,-14,-15,-16,-18,-19,-20,-21,20,20,20,20,20,]),'MAYORQ':([3,9,10,11,12,13,24,25,26,27,28,31,32,33,34,35,36,37,38,39,48,50,51,52,53,],[21,-22,-23,-24,-25,21,21,21,21,21,-17,21,-13,-14,-15,-16,-18,-19,-20,-21,21,21,21,21,21,]),'MENORIGUAL':([3,9,10,11,12,13,24,25,26,27,28,31,32,33,34,35,36,37,38,39,48,50,51,52,53,],[22,-22,-23,-24,-25,22,22,22,22,22,-17,22,-13,-14,-15,-16,-18,-19,-20,-21,22,22,22,22,22,]),'MAYORIGUAL':([3,9,10,11,12,13,24,25,26,27,28,31,32,33,34,35,36,37,38,39,48,50,51,52,53,],[23,-22,-23,-24,-25,23,23,23,23,23,-17,23,-13,-14,-15,-16,-18,-19,-20,-21,23,23,23,23,23,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'declaracion':([0,],[1,]),'expresion':([0,2,4,5,6,7,8,14,16,17,18,19,20,21,22,23,29,40,42,44,46,],[3,13,24,25,26,27,28,31,32,33,34,35,36,37,38,39,48,50,51,52,53,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> declaracion","S'",1,None,None,None),
  ('declaracion -> INT expresion EQUALS expresion PUNTOCOMA','declaracion',5,'p_declaracion_asignar','Analizador_Sintactico_y_Semantico.py',170),
  ('declaracion -> INT expresion PUNTOCOMA','declaracion',3,'p_declaracion_int','Analizador_Sintactico_y_Semantico.py',182),
  ('declaracion -> DOUBLE expresion EQUALS expresion PUNTOCOMA','declaracion',5,'p_declaracion_asignar2','Analizador_Sintactico_y_Semantico.py',194),
  ('declaracion -> DOUBLE expresion PUNTOCOMA','declaracion',3,'p_declaracion_double','Analizador_Sintactico_y_Semantico.py',206),
  ('declaracion -> FLOAT expresion EQUALS expresion PUNTOCOMA','declaracion',5,'p_declaracion_asignar3','Analizador_Sintactico_y_Semantico.py',217),
  ('declaracion -> FLOAT expresion PUNTOCOMA','declaracion',3,'p_declaracion_float','Analizador_Sintactico_y_Semantico.py',229),
  ('declaracion -> BOOL expresion EQUALS expresion PUNTOCOMA','declaracion',5,'p_declaracion_asignar5','Analizador_Sintactico_y_Semantico.py',240),
  ('declaracion -> BOOL expresion PUNTOCOMA','declaracion',3,'p_declaracion_bool','Analizador_Sintactico_y_Semantico.py',252),
  ('declaracion -> STRING expresion EQUALS expresion PUNTOCOMA','declaracion',5,'p_declaracion_asignar4','Analizador_Sintactico_y_Semantico.py',263),
  ('declaracion -> STRING expresion PUNTOCOMA','declaracion',3,'p_declaracion_string','Analizador_Sintactico_y_Semantico.py',275),
  ('declaracion -> expresion EQUALS expresion PUNTOCOMA','declaracion',4,'p_declaracion_asignarV','Analizador_Sintactico_y_Semantico.py',286),
  ('declaracion -> expresion PUNTOCOMA','declaracion',2,'p_declaracion_expr','Analizador_Sintactico_y_Semantico.py',307),
  ('expresion -> expresion SUMA expresion','expresion',3,'p_expresion_operaciones','Analizador_Sintactico_y_Semantico.py',315),
  ('expresion -> expresion RESTA expresion','expresion',3,'p_expresion_operaciones','Analizador_Sintactico_y_Semantico.py',316),
  ('expresion -> expresion MULTI expresion','expresion',3,'p_expresion_operaciones','Analizador_Sintactico_y_Semantico.py',317),
  ('expresion -> expresion DIVISION expresion','expresion',3,'p_expresion_operaciones','Analizador_Sintactico_y_Semantico.py',318),
  ('expresion -> RESTA expresion','expresion',2,'p_expresion_minus','Analizador_Sintactico_y_Semantico.py',334),
  ('expresion -> expresion MENORQ expresion','expresion',3,'p_expresion_logicas','Analizador_Sintactico_y_Semantico.py',342),
  ('expresion -> expresion MAYORQ expresion','expresion',3,'p_expresion_logicas','Analizador_Sintactico_y_Semantico.py',343),
  ('expresion -> expresion MENORIGUAL expresion','expresion',3,'p_expresion_logicas','Analizador_Sintactico_y_Semantico.py',344),
  ('expresion -> expresion MAYORIGUAL expresion','expresion',3,'p_expresion_logicas','Analizador_Sintactico_y_Semantico.py',345),
  ('expresion -> DECIMAL','expresion',1,'p_expresion_decimal','Analizador_Sintactico_y_Semantico.py',362),
  ('expresion -> NUMERO','expresion',1,'p_expresion_numero','Analizador_Sintactico_y_Semantico.py',369),
  ('expresion -> ID','expresion',1,'p_expresion_id','Analizador_Sintactico_y_Semantico.py',376),
  ('expresion -> TXT','expresion',1,'p_expresion_string','Analizador_Sintactico_y_Semantico.py',383),
]
