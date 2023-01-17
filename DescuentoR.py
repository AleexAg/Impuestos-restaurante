#Practica descuento de restaurante


def principal():
    #datos
    impuestos = 0.75
    descuentoA = 0.10
    descuentoB = 0.20

    print("="*30)
    print("|  RESTAURANTE CALAMUCHITA  |")
    #entrada de datos
    consumoI = float(input("Ingrese la cantidad de consumo: "))

    if consumoI <= 100:
        dato_descuento = "10%"
        consumoI = consumoI - (consumoI*descuentoA)
    else:
        dato_descuento = "20%"
        consumoI = consumoI - (consumoI*descuentoB)

    #Se calcula los impuestos generales
    impuestosF = consumoI * impuestos
    consumoF = consumoI + impuestosF

    #Salida de datos
    print("-"*30)
    print("Descuento aplicado:", dato_descuento)
    print("Impuestos aplicados: $", impuestosF)
    print("Precio final: $", consumoF)
    print("-" * 30)


if __name__ == '__main__':
    principal()