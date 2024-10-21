# Contador de Vocales

def contar_vocales(palabra):
    vocales = ['a','e','i','o','u']
    contador = 0
    
    for letra in palabra:
        if letra.lower() in vocales:
            contador += 1
    return contador

print(contar_vocales("Python"))         
print(contar_vocales("Programación"))   
print(contar_vocales("AEIOUaeiou"))     
