import ply.lex as lex

resultado_lexema = []

tokens = [
    'ID', 
    'SUMA', 
    'MULTI',
    'RESTA',
    'DIVISION', 
    'NUMERO', 
    'DECIMAL',
    'EQUALS', 
    'PUNTOCOMA', 
    'MENORQ', 
    'MAYORQ',
    'MENORIGUAL', 
    'MAYORIGUAL',
    'TXT',
]

reservadas = {
    'int' : 'INT',
    'double' : 'DOUBLE',
    'bool' : 'BOOL',
    'string' : 'STRING',
    'float' : 'FLOAT'
}

tokens = tokens + list(reservadas.values())

t_SUMA          = r'\+'
t_RESTA         = r'\-'
t_MULTI         = r'\*'
t_DIVISION      = r'/'
t_EQUALS        = r'='
t_MENORQ        = r'<'
t_MAYORQ        = r'>'
t_MENORIGUAL    = r'<='
t_MAYORIGUAL    = r'>='
t_PUNTOCOMA     = r';'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Caracter ilegal '%s'"%t.value[0])
    t.lexer.skip(1)

def t_DECIMAL(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_TXT(t) :
    r'\".*?\"'
    return t
    
def t_espacio(t):
    r"\s"
    pass

def t_DOUBLE(t):
    r'double'
    return t

def t_FLOAT(t):
    r'float'
    return t

def t_INT(t):
    r'int'
    return t

def t_BOOL(t):
    r'bool'
    return t

def t_STRING(t):
    r'string'
    return t

def t_ID(t):
    r'\w+\=|''\w+'
    return t

lexer = lex.lex()

def lexico(data):
    global resultado_lexema

    analizador = lex.lex()
    analizador.input(data)
    while True:
        tok = analizador.token()
        if not tok:
            break
        estado = "LINEA {:4} | VALOR {:4} ----> TIPO {:4}".format(
            str(tok.lineno), str(tok.value), str(tok.type))
        resultado_lexema.append(estado)

    return resultado_lexema


analizador = lex.lex()