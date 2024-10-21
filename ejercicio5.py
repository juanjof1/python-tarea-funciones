# Filtro de Números Pares

def filter_pares(lista):
    return [num for num in lista if num % 2 == 0]

print(filter_pares([1,2,3,4,5,6,7,8,9,10]))
print(filter_pares([1,3,5,7,9]))
print(filter_pares([2,4,6,8,10])) 
print(filter_pares([]))