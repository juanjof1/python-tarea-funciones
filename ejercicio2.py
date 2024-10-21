# El codigo ya arreglado


def clasificar_numero(numero):

    if numero > 0:
       return("positivo")
    
    elif numero < 0:
        return("Negativo")
    
    else:
        
        return("cero")
    
print(clasificar_numero(5))
print(clasificar_numero(-3))
print(clasificar_numero(0))