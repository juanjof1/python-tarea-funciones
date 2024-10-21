#  Calculadora de Descuentos


def calculadora_descuentos(precio_original, descuento):
    precio_con_descuentos = precio_original-(precio_original * (descuento / 100))


    return precio_con_descuentos

print(calculadora_descuentos(100, 20))
print(calculadora_descuentos(50, 10))
print(calculadora_descuentos(200,0))
