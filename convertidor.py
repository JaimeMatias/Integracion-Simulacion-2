
def convertirHora(entrada):
    resultado=int(entrada//3600)
    return(resultado)

def convertirMinuto(entrada):
    hora=convertirHora(entrada)
    resultado=int((entrada-hora*3600)//60)
    return(resultado)

def convertirSegundo(entrada):
    hora=convertirHora(entrada)
    minutos=convertirMinuto(entrada)
    resultado=int(entrada-hora*3600-minutos*60)
    return(resultado)
