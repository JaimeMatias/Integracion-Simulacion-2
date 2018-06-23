import convertidor

def mostrar(VARIABLE):
    HORA=convertidor.convertirHora(VARIABLE)
    MINUTOS=convertidor.convertirMinuto(VARIABLE)
    SEGUNDOS=convertidor.convertirSegundo(VARIABLE)
    print(HORA,":",MINUTOS,":",SEGUNDOS)

def imprimir(VARIABLE,ARCHIVO):
    HORA=convertidor.convertirHora(VARIABLE)
    MINUTOS=convertidor.convertirMinuto(VARIABLE)
    SEGUNDOS=convertidor.convertirSegundo(VARIABLE)
    ARCHIVO.write(str(HORA))
    ARCHIVO.write(":")
    ARCHIVO.write(str(MINUTOS))
    ARCHIVO.write(":")
    ARCHIVO.write(str(SEGUNDOS)+ '\n')
