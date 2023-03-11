from Analizador_Lexico import lexico, resultado_lexema
from Analizador_Sintactico_y_Semantico import *

#--------------------------------------------------#
# Impresion de los resultados de manera ordenada   #
#--------------------------------------------------#
lexico(text)
print()
print('==============Analizador Lexico + Tabla de Simbolos==============')
print()
print('\n'.join(list(map(''.join, resultado_lexema))))
sintactico(text)
print()
print('======================Analizador Sintactico======================')
print()
print('\n'.join(list(map(''.join, resultado_gramatica))))
if(res) : print("ALGUNA SINTAXIS EN EL CODIGO NO ES VALIDA\n")
elif (res == False): print("TODO ESTA CORRECTO\n")

print('\n=====================Analizador Semantico====================\n\n')
print(tipo_salida[0])
print()

# generador(text)
print()
print('======================Generador de Codigo Intermedio======================')
print()
print()
print('Aqui va a ir el lenguaje intermedio')

print("\n")
print('==========================================================================')

