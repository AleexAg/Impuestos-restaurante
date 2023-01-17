#Practica descuento de restaurante


def principal():

    while True:
        print("="*30)
        print("|  RESTAURANTE CALAMUCHITA  |")
        print("--> Ingrese -1 para salir!")
        #entrada de datos
        consumoI = float(input("Ingrese la cantidad de consumo: "))
        if consumoI > 0:
            if consumoI <= 100:
                dato_descuento = "10%"
                consumoI = consumoI - (consumoI*0.10)
            elif consumoI <= 200:
                dato_descuento = "20%"
                consumoI = consumoI - (consumoI * 0.20)
            else:
                dato_descuento = "30%"
                consumoI = consumoI - (consumoI * 0.30)

            # Se calcula los impuestos generales
            impuestosF = consumoI * 0.75
            consumoF = consumoI + impuestosF

            # Salida de datos
            print("-" * 30)
            print("Descuento aplicado:", dato_descuento)
            print("Impuestos: 75%")
            print("Impuestos aplicados: $", impuestosF)
            print("Precio final: $", consumoF)
            print("-" * 30)

        #Cancelar while
        elif consumoI == -1:
            print("Saliendo del programa....")
            break
        else:
            print("La cantidad ingresada no es valida")



if __name__ == '__main__':
    principal()
