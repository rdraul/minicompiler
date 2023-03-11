#-------------------------------------------------------#
#   Importo las librerias y archivos correspondientes   #
#-------------------------------------------------------#
import ply.yacc as yacc
from Analizador_Lexico import tokens, lexico, resultado_lexema

#------------------------------#
#   Inicializo las variables   #
#------------------------------#
variable = ""
type_variables = {}
typo = ""
list_valor = []
tipo_salida = []
resultado_gramatica = []
nombres = {}
precedence = (
    ('left', 'PUNTOCOMA'),
    ('left', 'EQUALS'),
    ('left', 'MENORQ', 'MAYORQ', 'MENORIGUAL', 'MAYORIGUAL'),
    ('left', 'MULTI','DIVISION'),
    ('left', 'SUMA','RESTA'),
)

#-----------------------------------------#
#   Analiza la semantica de los enteros   #
#-----------------------------------------#
def SemanticaINT(t):
    lista = t
    global list_valor
    global tipo_salida
    list_valor = lista[variable]
    if list_valor[0] == (type(list_valor[1]).__name__) :
        tipo_salida.append('TODO ESTA CORRECTO')
    else :
        tipo_salida.append('ERROR: ASIGNACION INCORRECTA DE TIPO {}'.format(list_valor[0]))

#----------------------------------------------------#
#   Analiza la semantica de los float y los double   #
#----------------------------------------------------#
def SemanticaF(t):
    lista = t
    global list_valor
    global tipo_salida
    list_valor = lista[variable]
    if (type(list_valor[1]).__name__) == 'float' : bol = 'double' 
    else : bol = ''
    if list_valor[0] == bol :
        tipo_salida.append('TODO ESTA CORRECTO')
    else :
        tipo_salida.append('ERROR: ASIGNACION INCORRECTA DE TIPO {}”'.format(list_valor[0]))

#---------------------------------------#
#   Analiza la semantica de los float   #
#---------------------------------------#
def SemanticaFloat(t):
    lista = t
    global list_valor
    global tipo_salida
    list_valor = lista[variable]
    if list_valor[0] == (type(list_valor[1]).__name__) :
        tipo_salida.append('TODO ESTA CORRECTO')
    else :
        tipo_salida.append('ERROR: ASIGNACION INCORRECTA DE TIPO {}'.format(list_valor[0]))

#-------------------------------------------#
#   Analiza la semantica de los booleanos   #
#-------------------------------------------#
def SemanticaBool(t):
    lista = t
    global list_valor
    global tipo_salida
    list_valor = lista[variable]
    if list_valor[0] == (type(list_valor[1]).__name__) :
        tipo_salida.append('TODO ESTA CORRECTO')
    else :
        tipo_salida.append('ERROR: ASIGNACION INCORRECTA DE TIPO {}'.format(list_valor[0]))

#----------------------------------------#
#   Analiza la semantica de los string   #
#----------------------------------------#
def SemanticaString(t):
    lista = t
    global list_valor
    global tipo_salida
    list_valor = lista[variable]
    if list_valor[0] == 'string' : bol = 'str' 
    else : bol = ''
    if bol == (type(list_valor[1]).__name__) :
        tipo_salida.append('TODO ESTA CORRECTO')
    else :
        tipo_salida.append('ERROR: ASIGNACION INCORRECTA DE TIPO {}'.format(list_valor[0]))

#------------------------------------------------------------------#
#   Para manejar la semantica de las declaraciones de los string   #
#------------------------------------------------------------------#
def SemanticaString_linedw(t):
    lista = t
    global list_valor
    global tipo_salida
    global aviso
    list_valor = lista[variable]
    if type(typo).__name__ == 'str' : bol = 'string' 
    else : bol = ''
    if list_valor == bol :
        tipo_salida.append('TODO ESTA CORRECTO')
    else :
        tipo_salida.append('ERROR: ASIGNACION INCORRECTA DE TIPO {}'.format(list_valor))

#---------------------------------------------------------------------#
#   Para manejar la semantica de las declaraciones de los booleanos   #
#---------------------------------------------------------------------#
def SemanticaBool_linedw(t):
    lista = t
    global list_valor
    global tipo_salida
    list_valor = lista[variable]
    if list_valor == type(typo).__name__ :
        tipo_salida.append('TODO ESTA CORRECTO')
    else :
        tipo_salida.append('ERROR: ASIGNACION INCORRECTA DE TIPO {}'.format(list_valor))

#-----------------------------------------------------------------#
#   Para manejar la semantica de las declaraciones de los float   #
#-----------------------------------------------------------------#
def SemanticaFloat_linedw(t):
    lista = t
    global list_valor
    global tipo_salida
    list_valor = lista[variable]
    if list_valor == type(typo).__name__ :
        tipo_salida.append('TODO ESTA CORRECTO')
    else :
        tipo_salida.append('ERROR: ASIGNACION INCORRECTA DE TIPO {}'.format(list_valor))

#------------------------------------------------------------------------------#
#   Para manejar la semantica de las declaraciones de los float y los double   #
#------------------------------------------------------------------------------#
def SemanticaF_linedw(t):
    lista = t
    global list_valor
    global tipo_salida
    global aviso
    list_valor = lista[variable]
    if type(typo).__name__ == 'float' : bol = 'double' 
    else : bol = ''
    if list_valor == bol :
        tipo_salida.append('TODO ESTA CORRECTO')
    else :
        tipo_salida.append('ERROR: ASIGNACION INCORRECTA DE TIPO {}'.format(list_valor))

#------------------------------------------------------------------#
#   Para manejar la semantica de las declaraciones de las lineas   #
#------------------------------------------------------------------#
def Semantica_linedw(t):
    lista = t
    global list_valor
    global tipo_salida
    list_valor = lista[variable]
    if list_valor == type(typo).__name__ :
        tipo_salida.append('TODO ESTA CORRECTO')
    else :
        tipo_salida.append('ERROR: ASIGNACION INCORRECTA DE TIPO {}'.format(list_valor))      
    
#-------------------------------------------------------------------#
#   Para manejar como se asignan los valores en las declaraciones   #
#-------------------------------------------------------------------#
def p_declaracion_asignar(t):
    'declaracion : INT expresion EQUALS expresion PUNTOCOMA'
    nombres[t[1]] = t[3]
    global type_variables
    type_variables[t[2]] = [t[1], t[4]]
    global variable
    variable = t[2] 
    SemanticaINT(type_variables)

#----------------------------------------------------------------------------------#
#   Para manejar como se asignan los valores en las declaraciones de los enteros   #
#----------------------------------------------------------------------------------#
def p_declaracion_int(t):
    'declaracion :   INT expresion PUNTOCOMA'
    nombres[t[1]] = t[3]
    global type_variables
    global variable
    type_variables[t[2]] = t[1]
    variable = t[2]


#-----------------------------------------------------------------------#
#   Para manejar como se asignan los valores en varias declaraciones    #
#-----------------------------------------------------------------------#
def p_declaracion_asignar2(t):
    'declaracion : DOUBLE expresion EQUALS expresion PUNTOCOMA'
    nombres[t[1]] = t[3]
    global type_variables
    type_variables[t[2]] = [t[1], t[4]]
    global variable
    variable = t[2]
    SemanticaF(type_variables)
    
#---------------------------------------------------------------------------------#
#   Para manejar como se asignan los valores en las declaraciones de los double   #
#---------------------------------------------------------------------------------#
def p_declaracion_double(t):
    'declaracion :  DOUBLE expresion PUNTOCOMA'
    nombres[t[1]] = t[3]
    global type_variables
    global variable
    type_variables[t[2]] = t[1]
    variable = t[2]

#-----------------------------------------------------------------------#
#   Para manejar como se asignan los valores en varias declaraciones    #
#-----------------------------------------------------------------------#
def p_declaracion_asignar3(t):
    'declaracion : FLOAT expresion EQUALS expresion PUNTOCOMA'
    nombres[t[1]] = t[3]
    global type_variables
    type_variables[t[2]] = [t[1], t[4]]
    global variable
    variable = t[2]
    SemanticaFloat(type_variables)

#--------------------------------------------------------------------------------#
#   Para manejar como se asignan los valores en las declaraciones de los float   #
#--------------------------------------------------------------------------------#
def p_declaracion_float(t):
    'declaracion :  FLOAT expresion PUNTOCOMA'
    nombres[t[1]] = t[3]
    global type_variables
    global variable
    type_variables[t[2]] = t[1]
    variable = t[2]

#-----------------------------------------------------------------------#
#   Para manejar como se asignan los valores en varias declaraciones    #
#-----------------------------------------------------------------------#
def p_declaracion_asignar5(t):
    'declaracion : BOOL expresion EQUALS expresion PUNTOCOMA'
    nombres[t[1]] = t[3]
    global type_variables
    type_variables[t[2]] = [t[1], t[4]]
    global variable
    variable = t[2]
    SemanticaBool(type_variables)

#------------------------------------------------------------------------------------#
#   Para manejar como se asignan los valores en las declaraciones de los booleanos   #
#------------------------------------------------------------------------------------#
def p_declaracion_bool(t):
    'declaracion :  BOOL expresion PUNTOCOMA'
    nombres[t[1]] = t[3]
    global type_variables
    global variable
    type_variables[t[2]] = t[1]
    variable = t[2]

#-----------------------------------------------------------------------#
#   Para manejar como se asignan los valores en varias declaraciones    #
#-----------------------------------------------------------------------#
def p_declaracion_asignar4(t):
    'declaracion : STRING expresion EQUALS expresion PUNTOCOMA'
    nombres[t[1]] = t[3]
    global type_variables
    type_variables[t[2]] = [t[1], t[4]]
    global variable
    variable = t[2]
    SemanticaString(type_variables)

#---------------------------------------------------------------------------------#
#   Para manejar como se asignan los valores en las declaraciones de los string   #
#---------------------------------------------------------------------------------#
def p_declaracion_string(t):
    'declaracion :  STRING expresion PUNTOCOMA'
    nombres[t[1]] = t[3]
    global type_variables
    global variable
    type_variables[t[2]] = t[1]
    variable = t[2]

#-----------------------------------------------------------------------#
#   Para manejar como se asignan los valores en varias declaraciones    #
#-----------------------------------------------------------------------#
def p_declaracion_asignarV(t):
    'declaracion :  expresion EQUALS expresion PUNTOCOMA'
    nombres[t[1]] = t[3]
    global typo
    type_variables[t[3]] = t[1]
    typo = t[3]

    if  type(typo).__name__ == 'int' :
        Semantica_linedw(type_variables)
    elif type_variables[variable] == 'double':
        SemanticaF_linedw(type_variables)
    elif type(typo).__name__ == 'float' :
        SemanticaFloat_linedw(type_variables)
    elif type(typo).__name__ == 'bool' :
        SemanticaBool_linedw(type_variables)
    elif type(typo).__name__ == 'str' :
        SemanticaString_linedw(type_variables)

#-------------------------------------------------------#
#   Para manejar las declaraciones de las expresiones   #
#-------------------------------------------------------#
def p_declaracion_expr(t):
    'declaracion : expresion PUNTOCOMA'
    t[0] = t[1]

#------------------------------------------------#
#   Para manejar las expresiones de operadores   #
#------------------------------------------------#
def p_expresion_operaciones(t):
    '''
    expresion  :   expresion SUMA expresion 
                |   expresion RESTA expresion 
                |   expresion MULTI expresion
                |   expresion DIVISION expresion 

    '''
    if t[2] == '+':
        t[0] = t[1] + t[3]
    elif t[2] == '-':
        t[0] = t[1] - t[3]
    elif t[2] == '*':
        t[0] = t[1] * t[3]
    elif t[2] == '/':
        t[0] = t[1] / t[3]

#-------------------------------------------#
#   Para manejar las expresiones de resta   #
#-------------------------------------------#
def p_expresion_minus(t):
    'expresion : RESTA expresion %prec RESTA'
    t[0] = -t[2]

#-------------------------------------------------------#
#   Para manejar las expresiones logicas > < <= >= ==   #
#-------------------------------------------------------#
def p_expresion_logicas(t):
    '''
    expresion   :  expresion MENORQ expresion 
                |  expresion MAYORQ expresion 
                |  expresion MENORIGUAL expresion 
                |   expresion MAYORIGUAL expresion 

    '''

    if t[2] == "<":
        t[0] = t[1] < t[3]
    elif t[2] == ">":
        t[0] = t[1] > t[3]
    elif t[2] == "<=":
        t[0] = t[1] <= t[3]
    elif t[2] == ">=":
        t[0] = t[1] >= t[3]
        
#---------------------------------------------------#
#   Para manejar las expresiones de los decimales   #
#---------------------------------------------------#
def p_expresion_decimal(t):
    'expresion : DECIMAL'
    t[0] = t[1]

#-------------------------------------------------#
#   Para manejar las expresiones de los numeros   #
#-------------------------------------------------#
def p_expresion_numero(t):
    'expresion : NUMERO'
    t[0] = t[1]

#---------------------------------------------------------#
#   Para manejar las expresiones de los identificadores   #
#---------------------------------------------------------#
def p_expresion_id(t):
    'expresion : ID'
    t[0] = t[1]
    
#------------------------------------------------#
#   Para manejar las expresiones de los string   #
#------------------------------------------------#
def p_expresion_string(t):
    'expresion : TXT'
    t[0] = t[1]

#------------------------------#
#   Para manejar los errores   #
#------------------------------#
res = False
def p_error(t):
    global resultado_gramatica
    if t:
        resultado = "ERROR DE SINTAXIS ---> TIPO {:4} | VALOR {:4}".format(
            str(t.type), str(t.value))
        global res
        res = True
    else:
        resultado = "ERROR DE SINTAXIS {}".format(t)
    resultado_gramatica.append(resultado)

#-------------------------------------------#
#   Instanciamos el analizador sistactico   #
#-------------------------------------------#
parser = yacc.yacc()
    
#---------------------------------------#
#   Funcion para capturar los errores   #
#---------------------------------------#
def sintactico(data):
    global resultado_gramatica

    for item in data.splitlines():
        if item:
            gram = parser.parse(item)
            if gram:
                resultado_gramatica.append(str(gram))
        else:
            print("")
    return resultado_gramatica


#--------------------------------------#
#   Importamos el archivo a analizar   #
#--------------------------------------#
path = "prueba.java"

# Verificacion del archivo #
try:
    archivo = open(path, 'r')
except:
    print("EL ARCHIVO NO FUE ENCONTRADOS")
    quit()

text = ""
for linea in archivo:
    text += linea

